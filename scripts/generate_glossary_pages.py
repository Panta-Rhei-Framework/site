#!/usr/bin/env python3
"""Generate per-entry + per-domain glossary pages from `_data/glossary/*.json`.

Phase v3.1 of the Results-Lane release plan. Materializes:

  /results/<domain>/glossary/index.md           — per-domain index (3 files)
  /results/<domain>/glossary/<entry-id>/index.md — per-entry stubs (~241 files)

Each per-entry stub is a minimal markdown page with frontmatter pointing to
the `glossary-entry` layout, which reads the full payload from
`site.data.glossary.<domain>.entries`. Stubs do NOT inline content — the
data file remains the single source of truth.

Per-domain index pages list all entries grouped by category, with chips for
status and Lean coverage. They use a custom layout (program-doc) for v3.1;
v3.3 will swap in the per-domain hub layout.

Idempotent — safe to re-run after `corpus/scripts/sync_corpus_to_site.py`.

Usage:
    python3 scripts/generate_glossary_pages.py
    python3 scripts/generate_glossary_pages.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from collections import defaultdict
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = SITE_ROOT / "_data" / "glossary"
RESULTS_ROOT = SITE_ROOT / "results"

DOMAINS = ["physics", "life", "metaphysics"]

DOMAIN_DESCRIPTIONS = {
    "physics": (
        "The 95-entry physics glossary covers quantities, units, constants, "
        "laws, particles, and objects, all calibrated to the neutron mass anchor "
        "PG-P01-neutron. Every entry carries an SI translation with a numerical "
        "value, uncertainty, and calibration cascade rooted at m_n."
    ),
    "life": (
        "The 78-entry life glossary covers biological structure, process, "
        "information, energy, temporal, systemic, and phenomenal categories. "
        "Every entry carries an empirical correlate (biomarker + measurable "
        "range + observation method), with kinetic-pseudoscalar (LG-Y02, VI.L18) "
        "as the kχ channel anchor for chirality-sensitive correlates."
    ),
    "metaphysics": (
        "The 68-entry metaphysics glossary covers the four canonical registers "
        "(empirical, practical, diagrammatic, commitment), the six original-rule "
        "narrowing principles (OR1–OR6), the four-operator architecture, "
        "ontology, commitment, and phenomenology. Each entry carries a "
        "phenomenological correlate — lived-experience instantiation with "
        "concrete examples and the register codomain it lives in."
    ),
}

DOMAIN_HEADLINES = {
    "physics":      "Physics Glossary — 95 entries, 6 categories",
    "life":         "Life Glossary — 78 entries, 7 categories",
    "metaphysics":  "Metaphysics Glossary — 68 entries, 6 categories",
}


def yaml_scalar(value) -> str:
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    return json.dumps(text, ensure_ascii=False)


def yaml_dump(data: dict, indent: int = 0) -> str:
    pad = " " * indent
    lines: list[str] = []
    for k, v in data.items():
        if isinstance(v, dict):
            lines.append(f"{pad}{k}:")
            lines.append(yaml_dump(v, indent + 2))
        elif isinstance(v, list):
            if not v:
                lines.append(f"{pad}{k}: []")
            else:
                lines.append(f"{pad}{k}:")
                for item in v:
                    if isinstance(item, dict):
                        lines.append(f"{pad}  -")
                        lines.append(yaml_dump(item, indent + 4))
                    else:
                        lines.append(f"{pad}  - {yaml_scalar(item)}")
        else:
            lines.append(f"{pad}{k}: {yaml_scalar(v)}")
    return "\n".join(lines)


def write_markdown(path: Path, frontmatter: dict, body: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml_dump(frontmatter) + "\n---\n\n" + body.strip() + "\n",
                    encoding="utf-8")


def generate_entry_page(domain: str, entry: dict, dry_run: bool) -> Path:
    """Write `/results/<domain>/glossary/<id>/index.md`. Frontmatter only —
    full content is read from data file by the layout."""
    iid = entry["id"]
    target = RESULTS_ROOT / domain / "glossary" / iid / "index.md"
    summary = (entry.get("tau_definition") or {}).get("summary") or ""
    summary_short = (summary[:240] + "…") if len(summary) > 240 else summary
    fm = {
        "layout": "glossary-entry",
        "title": entry["name"],
        "permalink": f"/results/{domain}/glossary/{iid}/",
        "lane": "results",
        "v2_lane": "results",
        "type": "Glossary Entry",
        "status": "Canonical",
        "domain": domain,
        "entry_id": iid,
        "category": entry.get("category"),
        "summary_short": summary_short,
        "generated_from": f"corpus/{domain}-glossary",
        "projection_version": "v0.1",
        "do_not_edit": True,
    }
    body = (
        f"<!-- Stub — full payload rendered by `_layouts/glossary-entry.html` "
        f"from `_data/glossary/{domain}.json` entry `{iid}`. "
        f"Generated by `scripts/generate_glossary_pages.py`; do not edit. -->"
    )
    write_markdown(target, fm, body, dry_run)
    return target


def category_block(domain: str, category: str, entries: list[dict]) -> str:
    """Render a category section with a card grid of entries."""
    lines = [f"## {category.capitalize()} <span class=\"muted\">({len(entries)})</span>"]
    lines.append("")
    lines.append('<ul class="v2-grid v2-card-list">')
    for e in entries:
        title = e["name"]
        iid = e["id"]
        summary = (e.get("tau_definition") or {}).get("summary") or ""
        # Trim to ~180 chars for grid cards
        if len(summary) > 180:
            summary = summary[:177] + "…"
        symbol = e.get("tau_symbol") or ""
        lines.append("  <li>")
        lines.append('    <article class="v2-tile">')
        if symbol:
            lines.append(f'      <h3><a href="{{{{ \'/results/{domain}/glossary/{iid}/\' | relative_url }}}}">{title} <code>{symbol}</code></a></h3>')
        else:
            lines.append(f'      <h3><a href="{{{{ \'/results/{domain}/glossary/{iid}/\' | relative_url }}}}">{title}</a></h3>')
        if summary:
            lines.append(f'      <p>{summary}</p>')
        lines.append(f'      <p class="muted"><code>{iid}</code></p>')
        lines.append("    </article>")
        lines.append("  </li>")
    lines.append("</ul>")
    return "\n".join(lines)


def generate_domain_index(domain: str, entries: list[dict], dry_run: bool) -> Path:
    """Write `/results/<domain>/glossary/index.md` — full domain glossary index."""
    target = RESULTS_ROOT / domain / "glossary" / "index.md"

    # Group entries by category, ordered alphabetically.
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_cat[e.get("category") or "uncategorized"].append(e)
    for cat in by_cat:
        by_cat[cat].sort(key=lambda x: x["id"])

    body_parts = [
        DOMAIN_DESCRIPTIONS[domain],
        "",
        '<div class="notice note"><strong>Glossary contract.</strong> Every entry below carries a 4-section structure: τ-definition (categorical invariant + primary registry anchor), τ-derivation (chain of registry steps), domain-specific Section 3, and Lean coverage. The structure is uniform across all three domains so cross-references resolve unambiguously.</div>',
        "",
        "## Browse by category",
        "",
    ]
    for cat in sorted(by_cat.keys()):
        body_parts.append(category_block(domain, cat, by_cat[cat]))
        body_parts.append("")

    body = "\n".join(body_parts)

    fm = {
        "layout": "program-doc",
        "title": DOMAIN_HEADLINES[domain],
        "permalink": f"/results/{domain}/glossary/",
        "lane": "results",
        "v2_lane": "results",
        "type": "Glossary Index",
        "status": "Canonical",
        "domain": domain,
        "summary_short": (
            f"Glossary for the τ-framework's {domain} domain — "
            f"{len(entries)} canonical entries grouped by category."
        ),
        "generated_from": f"corpus/{domain}-glossary",
        "projection_version": "v0.1",
        "do_not_edit": True,
    }
    write_markdown(target, fm, body, dry_run)
    return target


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be written without touching disk.")
    ap.add_argument("--clean", action="store_true",
                    help="Remove existing /results/<domain>/glossary/ trees first.")
    args = ap.parse_args()

    if not DATA_ROOT.exists():
        print(f"❌ Glossary data not found at {DATA_ROOT}. "
              f"Run `corpus/scripts/sync_corpus_to_site.py` first.",
              file=sys.stderr)
        return 2

    total_entries = 0
    total_indexes = 0

    for domain in DOMAINS:
        data_path = DATA_ROOT / f"{domain}.json"
        if not data_path.exists():
            print(f"⚠  {domain}.json missing — skipping {domain}")
            continue
        payload = json.loads(data_path.read_text(encoding="utf-8"))
        entries = payload.get("entries", [])
        if not entries:
            print(f"⚠  {domain}.json has no entries — skipping {domain}")
            continue

        if args.clean and not args.dry_run:
            target_dir = RESULTS_ROOT / domain / "glossary"
            if target_dir.exists():
                shutil.rmtree(target_dir)
                print(f"  cleaned existing {target_dir.relative_to(SITE_ROOT)}")

        domain_index_path = generate_domain_index(domain, entries, args.dry_run)
        total_indexes += 1
        for entry in entries:
            generate_entry_page(domain, entry, args.dry_run)
            total_entries += 1

        action = "would write" if args.dry_run else "wrote"
        print(f"  [{domain:11s}] {action} 1 index + {len(entries)} entries  → "
              f"{domain_index_path.parent.relative_to(SITE_ROOT)}/")

    action = "would write" if args.dry_run else "wrote"
    print()
    print(f"✅ {action} {total_indexes} domain indexes + {total_entries} entry pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
