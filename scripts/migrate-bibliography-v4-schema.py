#!/usr/bin/env python3
"""
Bibliography v4 schema migration.

Applies the extended schema spec from
atlas/website/doctrine/bibliography-schema.md to all _bibliography/
collection items.

The migration is ADDITIVE: existing fields are untouched; new fields
are added with sensible defaults if absent. Idempotent — safe to run
multiple times.

Usage:
    python3 scripts/migrate-bibliography-v4-schema.py [--dry-run]

Flags:
    --dry-run   Print intended changes without writing files.
    --check     Verify all files have v4 schema fields; exit 1 if any are missing.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BIB_DIR = REPO_ROOT / "_bibliography"

# v4 schema fields with defaults. Order chosen to keep frontmatter readable.
NEW_FIELDS_DEFAULTS = [
    # Identifier extensions
    ("openalex_id", None),
    ("crossref_id", None),
    ("datacite_id", None),
    ("orcid_authors", []),
    # Domain + subdomain + keyword granularity
    ("domain", []),
    ("subdomains", []),
    ("keywords", []),
    # Construction-step + Core Semantics linkage
    ("construction_steps", []),
    ("core_semantics", []),
    # Cross-surface linkage
    ("problem_ledger_items", []),
    ("related_results", []),
    ("related_verify", []),
    ("related_approaches", []),
    # Prior-art role + novelty positioning
    ("prior_art_role", []),
    # Source quality
    ("source_quality", []),
]

NEW_NOVELTY_POSITION = {
    "relation_type": "unknown",
    "summary": "",
}

NEW_STATUS = {
    "reviewed": False,
    "needs_metadata_review": True,
    "needs_source_check": False,
    "needs_prior_art_review": True,
}


def split_frontmatter(text: str) -> tuple[list[str], list[str]] | None:
    """Split a markdown file into (frontmatter_lines, body_lines).

    Returns None if the file does not start with `---` frontmatter delimiter.
    Frontmatter delimiters are stripped; body retains everything after the
    closing delimiter (including any leading blank line).
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\n") != "---":
        return None
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].rstrip("\n") == "---":
            end_idx = idx
            break
    if end_idx is None:
        return None
    return lines[1:end_idx], lines[end_idx + 1 :]


def has_top_level_key(frontmatter_lines: list[str], key: str) -> bool:
    """Return True if a top-level YAML key already exists in the frontmatter.

    Uses naive line-prefix matching — fine for our flat-frontmatter convention.
    Top-level keys are at column 0.
    """
    prefix = f"{key}:"
    return any(line.startswith(prefix) for line in frontmatter_lines)


def render_default(field: str, value) -> str:
    """Render a (key, default) pair as YAML lines."""
    if value is None:
        return f"{field}:\n"
    if isinstance(value, list):
        if not value:
            return f"{field}: []\n"
        return f"{field}:\n" + "".join(f"  - {item}\n" for item in value)
    if isinstance(value, dict):
        return f"{field}:\n" + "".join(f"  {k}: {repr_yaml_scalar(v)}\n" for k, v in value.items())
    return f"{field}: {repr_yaml_scalar(value)}\n"


def repr_yaml_scalar(value) -> str:
    """Repr a scalar for YAML output."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        if value == "":
            return '""'
        return value
    return str(value)


def migrate_file(path: Path, dry_run: bool, check_only: bool) -> tuple[bool, list[str]]:
    """Migrate a single bibliography file.

    Returns (changed, missing_fields). `missing_fields` is non-empty in
    --check mode when fields are absent.
    """
    text = path.read_text(encoding="utf-8")
    split = split_frontmatter(text)
    if split is None:
        return (False, [f"NO_FRONTMATTER:{path.name}"])
    fm_lines, body_lines = split

    missing = []
    for field, _default in NEW_FIELDS_DEFAULTS:
        if not has_top_level_key(fm_lines, field):
            missing.append(field)
    if not has_top_level_key(fm_lines, "novelty_position"):
        missing.append("novelty_position")
    if not has_top_level_key(fm_lines, "citation_status"):
        missing.append("citation_status")
    if not has_top_level_key(fm_lines, "status"):
        missing.append("status")
    if not has_top_level_key(fm_lines, "last_reviewed"):
        missing.append("last_reviewed")
    if not has_top_level_key(fm_lines, "review_notes"):
        missing.append("review_notes")

    if not missing:
        return (False, [])

    if check_only:
        return (False, missing)

    # Determine citation_status default based on cited_in
    citation_status_default = (
        "cited" if any(line.startswith("cited_in:") and "[]" not in line for line in fm_lines) else "corpus_only"
    )
    # Try to detect cited_in being non-empty (multi-line list).
    # Heuristic: if cited_in appears followed by a `-` indented line in the next ~10 lines, treat as cited.
    for idx, line in enumerate(fm_lines):
        if line.startswith("cited_in:"):
            for follow in fm_lines[idx + 1 : idx + 12]:
                if follow.startswith("  -"):
                    citation_status_default = "cited"
                    break
                if follow and not follow.startswith(" ") and not follow.startswith("\t"):
                    break

    additions: list[str] = ["\n# v4 schema fields (Session 2 migration)\n"]
    for field, default in NEW_FIELDS_DEFAULTS:
        if not has_top_level_key(fm_lines, field):
            additions.append(render_default(field, default))
    if not has_top_level_key(fm_lines, "novelty_position"):
        additions.append(render_default("novelty_position", NEW_NOVELTY_POSITION))
    if not has_top_level_key(fm_lines, "citation_status"):
        additions.append(render_default("citation_status", citation_status_default))
    if not has_top_level_key(fm_lines, "status"):
        additions.append(render_default("status", NEW_STATUS))
    if not has_top_level_key(fm_lines, "last_reviewed"):
        additions.append("last_reviewed: null\n")
    if not has_top_level_key(fm_lines, "review_notes"):
        additions.append('review_notes: ""\n')

    new_fm = "".join(fm_lines) + "".join(additions)
    new_text = "---\n" + new_fm + "---\n" + "".join(body_lines)

    if dry_run:
        return (True, missing)

    path.write_text(new_text, encoding="utf-8")
    return (True, missing)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--check", action="store_true", help="Verify schema; exit 1 if missing")
    args = parser.parse_args()

    if not BIB_DIR.is_dir():
        print(f"ERROR: bibliography dir not found: {BIB_DIR}", file=sys.stderr)
        return 2

    files = sorted(BIB_DIR.glob("*.md"))
    print(f"Bibliography files: {len(files)}")

    changed = 0
    skipped = 0
    failures: list[str] = []
    missing_total = 0

    for path in files:
        try:
            did_change, missing = migrate_file(path, dry_run=args.dry_run, check_only=args.check)
        except Exception as exc:
            failures.append(f"{path.name}: {exc}")
            continue
        if did_change:
            changed += 1
        elif missing and args.check:
            missing_total += 1
            if missing_total <= 5:
                print(f"  MISSING in {path.name}: {missing[:6]}")
        else:
            skipped += 1

    if args.check:
        print(f"\n=== CHECK ===")
        print(f"Files with missing v4 fields: {missing_total}")
        print(f"Files already migrated:       {skipped}")
        return 1 if missing_total > 0 else 0

    print(f"\n=== {'DRY RUN' if args.dry_run else 'APPLY'} ===")
    print(f"Migrated:  {changed}")
    print(f"Already up-to-date: {skipped}")
    if failures:
        print(f"Failures: {len(failures)}")
        for f in failures[:10]:
            print(f"  {f}")
    return 0 if not failures else 3


if __name__ == "__main__":
    sys.exit(main())
