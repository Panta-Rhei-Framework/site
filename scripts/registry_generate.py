#!/usr/bin/env python3
"""registry_generate.py — canonical JSONL → site _data/registry/ pipeline.

Reads the authoritative registry from
    /Users/thorfuchs/Books/PantaRhei-2ndEd/registry/book{1..7}_registry.jsonl
and produces the site-side derived data files:
    _data/registry/objects.json           (flattened array of all objects)
    _data/registry/books/book-{i..vii}.json  (per-book summaries, 7 files)

Usage:
    python3 scripts/registry_generate.py --dry-run     # write to _tmp_registry_output/
    python3 scripts/registry_generate.py --diff        # dry-run + show diff
    python3 scripts/registry_generate.py --apply       # write to _data/registry/
    python3 scripts/registry_generate.py --check       # dry-run + assert bit-identical

Regression safeguards:
    • --dry-run and --check are non-destructive (no writes to _data/registry/).
    • --apply writes only to files in ALLOW_LIST (enforced per-write).
    • Adjacency/reverse-adjacency files are NOT regenerated here — those are
      data-integrity-sensitive and stay under their existing generation flow.
    • Object pages (site/registry/object/*.md) are NOT regenerated here — they
      are frontmatter-only and the Jekyll layout renders them from objects.json.
    • Dashboards are NOT regenerated here — see registry_dashboard_regen.py
      which handles prose-preservation.

The script is idempotent: running --apply twice against unchanged canonical
source produces no file changes on the second run.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import sys
from collections import Counter
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = Path("/Users/thorfuchs/Books/PantaRhei-2ndEd/registry")
SITE_DATA_DIR = SITE_ROOT / "_data" / "registry"
STAGING_DIR = SITE_ROOT / "_tmp_registry_output"

BOOKS = [
    ("i", 1, "Categorical Foundations", "I"),
    ("ii", 2, "Categorical Holomorphy", "II"),
    ("iii", 3, "Categorical Spectrum", "III"),
    ("iv", 4, "Categorical Microcosm", "IV"),
    ("v", 5, "Categorical Macrocosm", "V"),
    ("vi", 6, "Categorical Life", "VI"),
    ("vii", 7, "Categorical Metaphysics", "VII"),
]

# Files this script is allowed to write. Any write attempt outside this list aborts.
ALLOW_LIST = {
    SITE_DATA_DIR / "objects.json",
    *(SITE_DATA_DIR / "books" / f"book-{slug}.json" for slug, _, _, _ in BOOKS),
}


def load_canonical_book(book_num: int) -> list[dict]:
    """Load one book's JSONL into a list of dicts."""
    path = CANONICAL_DIR / f"book{book_num}_registry.jsonl"
    if not path.exists():
        raise FileNotFoundError(f"Canonical source missing: {path}")
    entries = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entries.append(json.loads(line))
    return entries


def build_flat_objects(all_books: dict[int, list[dict]], book_roman: dict[int, str]) -> list[dict]:
    """Build the flattened objects.json — one row per object across all 7 books.
    URL preserves the raw object id (e.g., /registry/object/I.K0/) to match live format."""
    flat = []
    for book_num in sorted(all_books.keys()):
        roman = book_roman[book_num]
        for obj in all_books[book_num]:
            flat.append(
                {
                    "id": obj["id"],
                    "type": obj.get("type", ""),
                    "name": obj.get("name", ""),
                    "book": obj.get("book", roman),
                    "scope": obj.get("scope", "established"),
                    "formalization": obj.get("formalization", ""),
                    "dep_count": len(obj.get("depends_on", [])),
                    "rev_dep_count": len(obj.get("depended_by", [])),
                    "url": f"/registry/object/{obj['id']}/",
                }
            )
    return flat


def build_book_summary(
    book_num: int, book_slug: str, book_title: str, book_roman: str, objs: list[dict]
) -> dict:
    """Build the per-book summary object matching existing live shape.
    book field is Roman numeral ("I"), slug is "book-i", top_central is top 5."""
    types_count = Counter(o.get("type", "") for o in objs)
    scopes_count = Counter(o.get("scope", "established") for o in objs)
    formalizations_count = Counter(o.get("formalization", "") for o in objs)

    # Top central (most-depended-upon) — top 5 by rev_dep_count, stable by canonical order
    sorted_by_rev_deps = sorted(
        enumerate(objs),
        key=lambda pair: (-len(pair[1].get("depended_by", [])), pair[0]),
    )
    top_central = [
        {
            "id": o["id"],
            "name": o.get("name", ""),
            "rev_dep_count": len(o.get("depended_by", [])),
        }
        for _, o in sorted_by_rev_deps[:5]
    ]

    object_ids = [o["id"] for o in objs]

    return {
        "book": book_roman,
        "slug": f"book-{book_slug}",
        "title": book_title,
        "total_objects": len(objs),
        "types": dict(types_count),
        "scopes": dict(scopes_count),
        "formalizations": dict(formalizations_count),
        "top_central": top_central,
        "object_ids": object_ids,
    }


def write_if_allowed(path: Path, content: str, dry_run: bool, staging: Path) -> tuple[Path, bool]:
    """Write content to path (if allowed) or to staging dir (if dry-run).
    Returns (actual_path_written, did_change_vs_live).
    For dry-run, 'did_change' compares the staged content to the LIVE file
    (not the staging target, which is always empty at start of a run)."""
    target = staging / path.relative_to(SITE_ROOT) if dry_run else path
    if not dry_run and path not in ALLOW_LIST:
        raise PermissionError(
            f"REFUSED: {path} is not in the write allow-list. Generator aborted."
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    # Change detection always compares staged/new content to the LIVE file
    live_text = path.read_text(encoding="utf-8") if path.exists() else None
    did_change = live_text != content
    # Write only if the actual target doesn't already have that content
    existing_target = target.read_text(encoding="utf-8") if target.exists() else None
    if existing_target != content:
        target.write_text(content, encoding="utf-8")
    return target, did_change


def diff_against_live(staging: Path) -> str:
    """Produce a unified diff of staging vs live _data/registry/ for each generated file."""
    diffs: list[str] = []
    for fp in [SITE_DATA_DIR / "objects.json"] + [
        SITE_DATA_DIR / "books" / f"book-{slug}.json" for slug, _, _, _ in BOOKS
    ]:
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
            # Clip very long diffs
            if len(d) > 200:
                d = d[:100] + [f"... ({len(d) - 200} more lines) ...\n"] + d[-100:]
            diffs.append(f"\n=== {fp.relative_to(SITE_ROOT)} ===\n" + "".join(d))
    return "\n".join(diffs) if diffs else "(no differences — generation is bit-identical to current live)"


def main() -> int:
    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Write to staging, no live changes")
    mode.add_argument("--diff", action="store_true", help="Dry-run + show diff vs live")
    mode.add_argument("--apply", action="store_true", help="Write to _data/registry/")
    mode.add_argument(
        "--check",
        action="store_true",
        help="Dry-run + assert bit-identical to current live (fail non-zero if drift)",
    )
    args = ap.parse_args()

    dry_run = args.dry_run or args.diff or args.check

    # 1. Load canonical sources
    all_books: dict[int, list[dict]] = {}
    book_roman: dict[int, str] = {}
    for slug, num, title, roman in BOOKS:
        try:
            all_books[num] = load_canonical_book(num)
            book_roman[num] = roman
        except FileNotFoundError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1

    total_objects = sum(len(v) for v in all_books.values())
    print(f"Loaded {total_objects} objects across {len(all_books)} books from canonical source.")

    # 2. Build derived artifacts
    flat_objects = build_flat_objects(all_books, book_roman)
    book_summaries = {
        slug: build_book_summary(num, slug, title, roman, all_books[num])
        for slug, num, title, roman in BOOKS
    }

    # 3. Write (to staging or live)
    staging = STAGING_DIR
    if dry_run and staging.exists():
        # Clean staging dir
        import shutil
        shutil.rmtree(staging)

    any_changed = False

    # objects.json — live format: 1-space indent, ASCII-escaped, no trailing newline
    objects_path = SITE_DATA_DIR / "objects.json"
    content = json.dumps(flat_objects, indent=1)
    _, changed = write_if_allowed(objects_path, content, dry_run, staging)
    if changed:
        any_changed = True
        print(f"  {'STAGED' if dry_run else 'WROTE'}: {objects_path.relative_to(SITE_ROOT)}")

    # books/book-*.json — live format: 2-space indent, ASCII-escaped, no trailing newline
    for slug, _, _, _ in BOOKS:
        out = SITE_DATA_DIR / "books" / f"book-{slug}.json"
        content = json.dumps(book_summaries[slug], indent=2)
        _, changed = write_if_allowed(out, content, dry_run, staging)
        if changed:
            any_changed = True
            print(f"  {'STAGED' if dry_run else 'WROTE'}: {out.relative_to(SITE_ROOT)}")

    # 4. Report mode
    if args.diff:
        print()
        print("=" * 70)
        print("DIFF vs live _data/registry/:")
        print("=" * 70)
        print(diff_against_live(staging))

    if args.check:
        if any_changed:
            print("\n❌ --check: staged output differs from live. Run --diff to inspect.")
            return 1
        print("\n✓ --check: staged output is bit-identical to current live.")

    print()
    if args.apply:
        print(f"APPLIED. {'Some' if any_changed else 'No'} files changed in _data/registry/.")
    elif args.dry_run or args.diff:
        print(f"DRY-RUN. {'Some' if any_changed else 'No'} files would change. Staged to {staging.relative_to(SITE_ROOT)}.")
    elif args.check:
        print(f"CHECK. Staged output {'differs' if any_changed else 'matches'} live.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
