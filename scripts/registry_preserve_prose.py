#!/usr/bin/env python3
"""registry_preserve_prose.py — one-time extraction of manual prose from
registry dashboards and release-manifest.md, into separate files under
site/_data/registry/, so subsequent regeneration never destroys manual content.

Usage:
    python3 scripts/registry_preserve_prose.py [--dry-run]

Writes:
    _data/registry/dashboard_prose/book-{i..vii}.md   (7 files)
    _data/registry/release_manifest_sections.yml

This script is idempotent: running it twice produces the same output.
It writes only additive files. It does NOT modify any existing site content.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import List

SITE_ROOT = Path(__file__).resolve().parent.parent
DASHBOARDS_DIR = SITE_ROOT / "registry" / "dashboards"
RELEASE_MANIFEST = SITE_ROOT / "verify" / "release-manifest.md"
DASHBOARD_PROSE_OUT = SITE_ROOT / "_data" / "registry" / "dashboard_prose"
RELEASE_PROSE_OUT = SITE_ROOT / "_data" / "registry" / "release_manifest_sections.yml"

BOOKS = ["i", "ii", "iii", "iv", "v", "vi", "vii"]

# Marker inside dashboard files: everything above this line is manual prose,
# everything below is generated stats/tables. The marker line itself
# ("Generated: YYYY-MM-DD") is generator-owned.
GENERATED_MARKER_RE = re.compile(r"^Generated:\s*\d{4}-\d{2}-\d{2}\s*$", re.MULTILINE)


def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def extract_dashboard_prose(path: Path) -> tuple[str, str]:
    """Returns (preserved_prose, checksum)."""
    text = path.read_text(encoding="utf-8")
    m = GENERATED_MARKER_RE.search(text)
    if not m:
        raise ValueError(
            f"{path}: no 'Generated: YYYY-MM-DD' marker found. "
            f"Cannot separate manual prose from generated content."
        )
    # Preserve everything from start of file up to (but not including) the marker line.
    prose = text[: m.start()].rstrip() + "\n"
    return prose, sha256(prose)


def extract_release_manifest_sections(path: Path) -> dict:
    """Extract the manually-authored sections of release-manifest.md.

    The manifest has H2 sections; we preserve everything except the
    'Per-book reconciliation' section's table (lines between the H2 and the
    next H2), which is the only regenerable piece.
    """
    text = path.read_text(encoding="utf-8")

    # Split on top-level H2 headings (##).
    # We keep section boundaries and their content keyed by heading.
    lines = text.split("\n")
    sections: dict[str, List[str]] = {"__frontmatter__": [], "__preamble__": []}
    current = "__frontmatter__"
    in_frontmatter = False
    frontmatter_delim_count = 0

    for i, ln in enumerate(lines):
        if ln.strip() == "---":
            frontmatter_delim_count += 1
            sections[current].append(ln)
            if frontmatter_delim_count == 2:
                current = "__preamble__"
            continue
        if frontmatter_delim_count < 2:
            sections[current].append(ln)
            continue
        if ln.startswith("## "):
            current = ln[3:].strip()
            sections.setdefault(current, []).append(ln)
        else:
            sections[current].append(ln)

    # Join section contents.
    joined = {k: "\n".join(v) for k, v in sections.items()}

    # For each section, compute a checksum that the regeneration must preserve.
    checksums = {k: sha256(v) for k, v in joined.items() if v.strip()}

    return {"sections": joined, "checksums": checksums}


def yaml_escape(s: str) -> str:
    """Quote a string for YAML scalar safety."""
    # Use the block scalar style (|) and indent each line.
    indented = "\n".join("    " + ln for ln in s.split("\n"))
    return "|\n" + indented


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run", action="store_true", help="Report what would be written; don't write."
    )
    args = parser.parse_args()

    report: List[str] = []

    # 1. Extract dashboard prose for 7 books.
    if not args.dry_run:
        DASHBOARD_PROSE_OUT.mkdir(parents=True, exist_ok=True)

    for book in BOOKS:
        dashboard = DASHBOARDS_DIR / f"book-{book}.md"
        if not dashboard.exists():
            report.append(f"✗ MISSING: {dashboard}")
            continue
        try:
            prose, checksum = extract_dashboard_prose(dashboard)
        except ValueError as e:
            report.append(f"✗ ERROR: {e}")
            continue

        out_path = DASHBOARD_PROSE_OUT / f"book-{book}.md"
        if args.dry_run:
            report.append(
                f"  [DRY-RUN] Would write {out_path} ({len(prose)} chars, checksum {checksum})"
            )
        else:
            out_path.write_text(prose, encoding="utf-8")
            report.append(f"✓ Wrote {out_path} ({len(prose)} chars, checksum {checksum})")

    # 2. Extract release manifest sections.
    if not RELEASE_MANIFEST.exists():
        report.append(f"✗ MISSING: {RELEASE_MANIFEST}")
    else:
        data = extract_release_manifest_sections(RELEASE_MANIFEST)
        # Write as YAML. We produce a structured file where each section is
        # addressable by its H2 heading, plus the frontmatter and preamble.
        out_lines = [
            "# Auto-extracted from verify/release-manifest.md by registry_preserve_prose.py",
            "# DO NOT EDIT MANUALLY — regenerate via: python3 scripts/registry_preserve_prose.py",
            "# Checksums under sha256_checksums/ must match the corresponding sections",
            "# after any regeneration; registry_verify.py enforces this.",
            "",
            "sections:",
        ]
        for heading, content in data["sections"].items():
            # Skip empty sections and the per-book reconciliation (which is regenerable).
            if not content.strip():
                continue
            out_lines.append(f"  {repr(heading)}: {yaml_escape(content)}")
        out_lines.append("")
        out_lines.append("sha256_checksums:")
        for heading, checksum in data["checksums"].items():
            out_lines.append(f"  {repr(heading)}: {repr(checksum)}")
        out_lines.append("")

        body = "\n".join(out_lines)
        if args.dry_run:
            report.append(
                f"  [DRY-RUN] Would write {RELEASE_PROSE_OUT} "
                f"({len(body)} chars, {len(data['checksums'])} sections)"
            )
        else:
            RELEASE_PROSE_OUT.parent.mkdir(parents=True, exist_ok=True)
            RELEASE_PROSE_OUT.write_text(body, encoding="utf-8")
            report.append(
                f"✓ Wrote {RELEASE_PROSE_OUT} "
                f"({len(body)} chars, {len(data['checksums'])} sections)"
            )

    print("\n".join(report))
    print()
    print(f"Status: {'DRY-RUN' if args.dry_run else 'APPLIED'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
