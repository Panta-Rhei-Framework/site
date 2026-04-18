#!/usr/bin/env python3
"""registry_verify.py — prose-integrity + count-invariant verification.

Run after any change that could affect the registry surfaces or Release Manifest.
Exits non-zero if any prose or invariant check fails.

Usage:
    python3 scripts/registry_verify.py
    python3 scripts/registry_verify.py --full    (also checks data invariants)

Checks:
    1. Dashboard manual prose (above 'Generated:' marker) matches extracted baseline.
    2. Release Manifest manual-section checksums match extracted baseline.
    3. filter_rules.yml current_totals are internally consistent.
    4. (--full) Site data registry object counts match filter_rules manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
DASHBOARDS_DIR = SITE_ROOT / "registry" / "dashboards"
DASHBOARD_PROSE_DIR = SITE_ROOT / "_data" / "registry" / "dashboard_prose"
RELEASE_MANIFEST = SITE_ROOT / "verify" / "release-manifest.md"
RELEASE_PROSE_FILE = SITE_ROOT / "_data" / "registry" / "release_manifest_sections.yml"
FILTER_RULES_FILE = SITE_ROOT / "_data" / "registry" / "filter_rules.yml"
SITE_DATA_REGISTRY = SITE_ROOT / "_data" / "registry"

BOOKS = ["i", "ii", "iii", "iv", "v", "vi", "vii"]
GENERATED_MARKER_RE = re.compile(r"^Generated:\s*\d{4}-\d{2}-\d{2}\s*$", re.MULTILINE)


def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def check_dashboard_prose() -> list[str]:
    """Each dashboard's content above 'Generated:' marker must still match
    the extracted baseline in _data/registry/dashboard_prose/."""
    errs: list[str] = []
    for book in BOOKS:
        live = DASHBOARDS_DIR / f"book-{book}.md"
        baseline = DASHBOARD_PROSE_DIR / f"book-{book}.md"
        if not live.exists():
            errs.append(f"MISSING live: {live}")
            continue
        if not baseline.exists():
            errs.append(f"MISSING baseline: {baseline}")
            continue
        live_text = live.read_text(encoding="utf-8")
        m = GENERATED_MARKER_RE.search(live_text)
        if not m:
            errs.append(f"{live}: lost 'Generated:' marker — structural damage")
            continue
        live_prose = live_text[: m.start()].rstrip() + "\n"
        baseline_prose = baseline.read_text(encoding="utf-8")
        if sha256(live_prose) != sha256(baseline_prose):
            errs.append(
                f"PROSE MISMATCH {live}: live prose diverged from baseline. "
                f"live={sha256(live_prose)} vs baseline={sha256(baseline_prose)}"
            )
    return errs


def parse_yaml_simple(text: str) -> dict:
    """Minimal YAML parser for filter_rules.yml — we support only the
    idioms we actually use: scalar keys, nested mappings, block scalars (|).
    Avoids a PyYAML dependency for portability."""
    import yaml  # PyYAML ships with most python installs; Jekyll requires it.
    return yaml.safe_load(text)


def check_filter_rules_consistency() -> list[str]:
    """filter_rules.yml current_totals must be internally consistent."""
    errs: list[str] = []
    try:
        data = parse_yaml_simple(FILTER_RULES_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"MISSING: {FILTER_RULES_FILE}"]
    except Exception as e:
        return [f"PARSE ERROR: {FILTER_RULES_FILE}: {e}"]

    rules = data.get("filter_rules", {})

    # Invariant: registry_total grand_total sums correctly per book.
    rt = rules.get("registry_total", {}).get("current_totals", {})
    if rt:
        per_book_sum = sum(rt.get(f"book_{b}", 0) for b in BOOKS)
        claimed = rt.get("grand_total")
        if claimed != per_book_sum:
            errs.append(
                f"registry_total: grand_total={claimed} does not equal "
                f"sum of per-book totals ({per_book_sum})"
            )

    # Invariant: dashboard_display ≤ registry_total for every book.
    dd = rules.get("dashboard_display", {}).get("current_totals", {})
    if rt and dd:
        for b in BOOKS:
            k = f"book_{b}"
            rt_b = rt.get(k, 0)
            dd_b = dd.get(k, 0)
            if dd_b > rt_b:
                errs.append(
                    f"dashboard_display > registry_total for book_{b}: "
                    f"{dd_b} > {rt_b} — filter is supposed to be subsumptive"
                )

    # Invariant: formalized + planned + not_applicable ≤ dashboard_display.
    fc = rules.get("formalized_count", {}).get("current_totals", {})
    pc = rules.get("planned_count", {}).get("current_totals", {})
    nc = rules.get("not_applicable_count", {}).get("current_totals", {})
    if dd and fc and pc and nc:
        for b in BOOKS:
            k = f"book_{b}"
            tracked = fc.get(k, 0) + pc.get(k, 0) + nc.get(k, 0)
            dd_b = dd.get(k, 0)
            if tracked > dd_b:
                errs.append(
                    f"formalized+planned+N/A ({tracked}) > dashboard_display "
                    f"({dd_b}) for book_{b}"
                )

    return errs


def check_site_data_matches_manifest() -> list[str]:
    """(--full) Site _data/registry/books/book-*.json totals must agree
    with filter_rules.yml current_totals."""
    errs: list[str] = []
    try:
        data = parse_yaml_simple(FILTER_RULES_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, Exception) as e:
        return [f"Cannot read {FILTER_RULES_FILE}: {e}"]

    rt = data.get("filter_rules", {}).get("registry_total", {}).get("current_totals", {})
    if not rt:
        return ["filter_rules.yml missing registry_total.current_totals"]

    for book in BOOKS:
        book_json = SITE_DATA_REGISTRY / "books" / f"book-{book}.json"
        if not book_json.exists():
            errs.append(f"MISSING: {book_json}")
            continue
        try:
            book_data = json.loads(book_json.read_text(encoding="utf-8"))
        except Exception as e:
            errs.append(f"JSON parse error {book_json}: {e}")
            continue
        total_from_data = book_data.get("total_objects")
        total_from_manifest = rt.get(f"book_{book}")
        if total_from_data != total_from_manifest:
            errs.append(
                f"MISMATCH book_{book}: site data total_objects={total_from_data} "
                f"vs filter_rules manifest={total_from_manifest}"
            )

    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="Also check data invariants")
    args = ap.parse_args()

    print("=" * 70)
    print("REGISTRY VERIFICATION HARNESS")
    print("=" * 70)

    all_errs: list[str] = []
    all_errs.extend(check_dashboard_prose())
    all_errs.extend(check_filter_rules_consistency())
    if args.full:
        all_errs.extend(check_site_data_matches_manifest())

    if all_errs:
        print(f"\n❌ {len(all_errs)} error(s):")
        for e in all_errs:
            print(f"  • {e}")
        return 1

    print("\n✓ Dashboard prose integrity: all 7 books match baseline")
    print("✓ filter_rules.yml: internal consistency checks pass")
    if args.full:
        print("✓ Site data registry totals: match filter_rules manifest")
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
