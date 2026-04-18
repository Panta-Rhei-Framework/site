#!/usr/bin/env python3
"""registry_dashboard_regen.py — prose-preserving dashboard regeneration.

Regenerates the seven per-book dashboards at registry/dashboards/book-{i..vii}.md
from the canonical JSONL while preserving manual prose above the
'Generated: YYYY-MM-DD' marker (baselined at
_data/registry/dashboard_prose/book-{slug}.md).

Usage:
    python3 scripts/registry_dashboard_regen.py --dry-run      # stage only
    python3 scripts/registry_dashboard_regen.py --diff         # dry-run + diff vs live
    python3 scripts/registry_dashboard_regen.py --apply        # write to live
    python3 scripts/registry_dashboard_regen.py --check        # fail if live would change

Safeguards:
    • ALLOW_LIST enforces that only registry/dashboards/book-{slug}.md are touched.
    • Pre-flight: each live dashboard's 'above-marker' section must SHA-256-match
      the baseline in _data/registry/dashboard_prose/ — otherwise we abort,
      because that section is manually curated and a mismatch means something
      manual has changed upstream of the marker and must be re-baselined first.
    • Date policy: by default we preserve the existing 'Generated:' date from
      the live dashboard (idempotent). Pass --today-date to stamp today's date.
    • Dry-run writes to _tmp_registry_output/; --apply writes to live only
      after allow-list and pre-flight checks pass.

Body generation follows the format of
    /Users/thorfuchs/Books/PantaRhei-2ndEd/scripts/registry_dashboard.py
so the output is compatible with what the upstream generator produces.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = Path("/Users/thorfuchs/Books/PantaRhei-2ndEd/registry")
DASHBOARDS_DIR = SITE_ROOT / "registry" / "dashboards"
PROSE_BASELINE_DIR = SITE_ROOT / "_data" / "registry" / "dashboard_prose"
STAGING_DIR = SITE_ROOT / "_tmp_registry_output"

BOOKS = [
    ("i", 1, "I"),
    ("ii", 2, "II"),
    ("iii", 3, "III"),
    ("iv", 4, "IV"),
    ("v", 5, "V"),
    ("vi", 6, "VI"),
    ("vii", 7, "VII"),
]

ALLOW_LIST = {DASHBOARDS_DIR / f"book-{slug}.md" for slug, _, _ in BOOKS}
GENERATED_MARKER_RE = re.compile(r"^Generated:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)


def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def load_canonical_book(book_num: int) -> list[dict]:
    path = CANONICAL_DIR / f"book{book_num}_registry.jsonl"
    if not path.exists():
        raise FileNotFoundError(f"Canonical source missing: {path}")
    entries = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def compute_dep_depth(entry_id: str, all_ids: dict, cache: dict) -> int:
    if entry_id in cache:
        return cache[entry_id]
    entry = all_ids.get(entry_id)
    if not entry or not entry.get("depends_on"):
        cache[entry_id] = 0
        return 0
    max_depth = 0
    for dep in entry["depends_on"]:
        if dep in all_ids:
            max_depth = max(max_depth, compute_dep_depth(dep, all_ids, cache) + 1)
    cache[entry_id] = max_depth
    return max_depth


def generate_body(numeral: str, entries: list[dict], all_ids: dict, generated_date: str) -> str:
    """Generate the dashboard body (everything from 'Generated:' onward).
    Format is kept byte-compatible with the upstream registry_dashboard.py."""
    lines: list[str] = [f"Generated: {generated_date}", ""]

    if not entries:
        lines.append("*No entries yet.*")
        return "\n".join(lines) + "\n"

    # Statistics
    type_counts = Counter(e["type"] for e in entries)
    form_counts = Counter(e["formalization"] for e in entries)
    scope_counts = Counter(e["scope"] for e in entries)

    lines.append("## Statistics")
    lines.append(f"- **Total objects:** {len(entries)}")
    type_str = " | ".join(f"{t}: {c}" for t, c in sorted(type_counts.items()))
    lines.append(f"- **By type:** {type_str}")
    form_str = " | ".join(f"{f}: {c}" for f, c in sorted(form_counts.items()))
    lines.append(f"- **Formalization:** {form_str}")
    scope_str = " | ".join(f"{s}: {c}" for s, c in sorted(scope_counts.items()))
    lines.append(f"- **Scope:** {scope_str}")
    lines.append("")

    # Dependency Summary
    depth_cache: dict = {}
    max_depth_entry = ""
    max_depth = 0
    for e in entries:
        d = compute_dep_depth(e["id"], all_ids, depth_cache)
        if d > max_depth:
            max_depth = d
            max_depth_entry = e["id"]

    dep_counts: Counter = Counter()
    for e in entries:
        for dep in e.get("depends_on", []):
            dep_counts[dep] += 1

    lines.append("## Dependency Summary")
    lines.append(f"- **Max chain depth:** {max_depth} ({max_depth_entry})")
    if dep_counts:
        most_used = dep_counts.most_common(3)
        most_str = ", ".join(f"{eid} ({c} uses)" for eid, c in most_used)
        lines.append(f"- **Most depended-on:** {most_str}")
    orphans = [e["id"] for e in entries if not e.get("depends_on")]
    if orphans:
        lines.append(
            f"- **No dependencies (foundational):** {', '.join(orphans[:10])}"
            + (" ..." if len(orphans) > 10 else "")
        )
    lines.append("")

    # Part Coverage
    parts: dict = defaultdict(list)
    for e in entries:
        parts[e.get("part", -1)].append(e)

    lines.append("## Part Coverage")
    lines.append("| Part | Objects | Formalized | Planned | N/A |")
    lines.append("|------|---------|------------|---------|-----|")
    for part_num in sorted(parts.keys(), key=lambda x: (isinstance(x, str), x)):
        part_entries = parts[part_num]
        total = len(part_entries)
        formalized = sum(1 for e in part_entries if e["formalization"] == "formalized")
        planned = sum(1 for e in part_entries if e["formalization"] == "planned")
        na = sum(1 for e in part_entries if e["formalization"] == "not_applicable")
        lines.append(f"| {part_num} | {total} | {formalized} | {planned} | {na} |")
    lines.append("")

    # Object List
    lines.append("## Object List")
    lines.append("| ID | Type | Name | Scope | Lean |")
    lines.append("|----|------|------|-------|------|")
    for e in entries:
        lean_status = e["formalization"][:4] if e.get("lean_module") else "—"
        lines.append(f"| {e['id']} | {e['type']} | {e['name']} | {e['scope'][:5]} | {lean_status} |")
    lines.append("")

    return "\n".join(lines)


def check_baseline_integrity() -> list[str]:
    """For every live dashboard, the content above 'Generated:' must match
    the baseline. If a mismatch is found, regeneration is ABORTED — the
    manual prose has drifted and must be re-baselined (explicitly, out of band)
    before we regenerate."""
    errs: list[str] = []
    for slug, _, _ in BOOKS:
        live = DASHBOARDS_DIR / f"book-{slug}.md"
        baseline = PROSE_BASELINE_DIR / f"book-{slug}.md"
        if not live.exists():
            errs.append(f"Missing live dashboard: {live}")
            continue
        if not baseline.exists():
            errs.append(f"Missing prose baseline: {baseline}")
            continue
        live_text = live.read_text(encoding="utf-8")
        m = GENERATED_MARKER_RE.search(live_text)
        if not m:
            errs.append(f"{live}: lost 'Generated:' marker — structural damage")
            continue
        live_prose = live_text[: m.start()].rstrip() + "\n"
        baseline_text = baseline.read_text(encoding="utf-8")
        if sha256(live_prose) != sha256(baseline_text):
            errs.append(
                f"{live}: live prose drifted from baseline. "
                f"live={sha256(live_prose)} vs baseline={sha256(baseline_text)} — "
                f"re-baseline before regenerating, or restore the prose."
            )
    return errs


def extract_current_date(live_path: Path) -> str | None:
    """Read the 'Generated: YYYY-MM-DD' date from the current live dashboard."""
    if not live_path.exists():
        return None
    text = live_path.read_text(encoding="utf-8")
    m = GENERATED_MARKER_RE.search(text)
    return m.group(1) if m else None


def write_if_allowed(
    path: Path, content: str, dry_run: bool, staging: Path
) -> tuple[Path, bool]:
    """Write to staging (dry-run) or live (apply). did_change compares to LIVE."""
    target = staging / path.relative_to(SITE_ROOT) if dry_run else path
    if not dry_run and path not in ALLOW_LIST:
        raise PermissionError(
            f"REFUSED: {path} is not in the dashboard-regen allow-list."
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    live_text = path.read_text(encoding="utf-8") if path.exists() else None
    did_change = live_text != content
    existing_target = target.read_text(encoding="utf-8") if target.exists() else None
    if existing_target != content:
        target.write_text(content, encoding="utf-8")
    return target, did_change


def diff_vs_live(staging: Path) -> str:
    diffs: list[str] = []
    for slug, _, _ in BOOKS:
        fp = DASHBOARDS_DIR / f"book-{slug}.md"
        staged = staging / fp.relative_to(SITE_ROOT)
        if not staged.exists():
            continue
        live_text = fp.read_text(encoding="utf-8") if fp.exists() else ""
        staged_text = staged.read_text(encoding="utf-8")
        if live_text == staged_text:
            continue
        d = list(
            difflib.unified_diff(
                live_text.splitlines(keepends=True),
                staged_text.splitlines(keepends=True),
                fromfile=f"live/{fp.relative_to(SITE_ROOT)}",
                tofile=f"staged/{fp.relative_to(SITE_ROOT)}",
                n=2,
            )
        )
        if d:
            if len(d) > 200:
                d = d[:100] + [f"... ({len(d) - 200} more lines) ...\n"] + d[-100:]
            diffs.append(f"\n=== {fp.relative_to(SITE_ROOT)} ===\n" + "".join(d))
    return "\n".join(diffs) if diffs else "(no differences)"


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--diff", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument(
        "--today-date",
        action="store_true",
        help="Stamp today's date on the Generated: marker (default: preserve existing)",
    )
    args = ap.parse_args()
    dry_run = args.dry_run or args.diff or args.check

    # Pre-flight: baseline integrity must hold
    errs = check_baseline_integrity()
    if errs:
        print("❌ BASELINE INTEGRITY FAILED — aborting:")
        for e in errs:
            print(f"  • {e}")
        return 1
    print("✓ Baseline integrity: 7 dashboards match extracted prose baselines")

    # Load canonical
    all_entries: list[dict] = []
    per_book: dict[int, list[dict]] = {}
    for slug, num, _ in BOOKS:
        entries = load_canonical_book(num)
        per_book[num] = entries
        all_entries.extend(entries)
    all_ids = {e["id"]: e for e in all_entries}
    print(f"✓ Canonical source: {len(all_entries)} objects across {len(per_book)} books")

    # Clean staging dir
    staging = STAGING_DIR
    if dry_run and staging.exists():
        import shutil

        shutil.rmtree(staging)

    any_changed = False
    today = date.today().isoformat()

    for slug, num, numeral in BOOKS:
        live = DASHBOARDS_DIR / f"book-{slug}.md"
        baseline = PROSE_BASELINE_DIR / f"book-{slug}.md"
        baseline_text = baseline.read_text(encoding="utf-8")
        # Baseline ends with "# Book N Registry Dashboard\n" — append 'Generated:' + body.
        gen_date = today if args.today_date else (extract_current_date(live) or today)
        body = generate_body(numeral, per_book[num], all_ids, gen_date)
        new_content = baseline_text + body

        _, changed = write_if_allowed(live, new_content, dry_run, staging)
        if changed:
            any_changed = True
            print(f"  {'STAGED' if dry_run else 'WROTE'}: {live.relative_to(SITE_ROOT)}")

    if args.diff:
        print()
        print("=" * 70)
        print("DIFF vs live:")
        print("=" * 70)
        print(diff_vs_live(staging))

    if args.check:
        if any_changed:
            print("\n❌ --check: staged dashboards differ from live. Run --diff.")
            return 1
        print("\n✓ --check: staged dashboards bit-identical to live.")
        return 0

    print()
    if args.apply:
        print(f"APPLIED. {'Some' if any_changed else 'No'} dashboards changed.")
    else:
        print(
            f"DRY-RUN. {'Some' if any_changed else 'No'} dashboards would change. "
            f"Staged to {staging.relative_to(SITE_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
