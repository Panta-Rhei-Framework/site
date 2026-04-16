#!/usr/bin/env python3
"""
Build Physics Ledger: Parse prediction tables and falsification pack from
Book V ch68 LaTeX, generate Jekyll collections (_predictions/ + _falsifications/)
and data files for browse surfaces.

Usage:
    python3 scripts/build_physics_ledger.py

Outputs:
    _predictions/*.md         (one per prediction entry)
    _falsifications/*.md      (one per N1-N30 entry)
    _data/predictions/predictions.json
    _data/falsifications/falsifications.json
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from latex_to_mathml import convert_title, latex_accents_to_unicode, clean_bibfield

SITE_ROOT = Path(__file__).parent.parent
CH68 = Path(
    os.path.expanduser(
        "~/Books/PantaRhei-2ndEd/books/V-CategoricalMacrocosm/latex/sections/part07/ch68-inventory-falsification.tex"
    )
)

OUT_PREDICTIONS = SITE_ROOT / "_predictions"
OUT_FALSIFICATIONS = SITE_ROOT / "_falsifications"
OUT_DATA_PRED = SITE_ROOT / "_data" / "predictions"
OUT_DATA_FALS = SITE_ROOT / "_data" / "falsifications"


# ---------------------------------------------------------------------------
# LaTeX table parser
# ---------------------------------------------------------------------------


def strip_comments(text: str) -> str:
    """Remove % comments but preserve \\%."""
    lines = []
    for line in text.split("\n"):
        idx = 0
        while idx < len(line):
            if line[idx] == "%" and (idx == 0 or line[idx - 1] != "\\"):
                line = line[:idx]
                break
            idx += 1
        lines.append(line)
    return "\n".join(lines)


def clean_cell(cell: str) -> str:
    """Clean a LaTeX table cell into readable text."""
    s = cell.strip()
    # Strip \\[3pt] etc at end
    s = re.sub(r"\\+\s*\[.*?\]\s*$", "", s)
    s = re.sub(r"\\+\s*$", "", s)
    # texorpdfstring
    s = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", s)
    # Math mode: convert to plain text
    _, plain = convert_title(s)
    return plain.strip()


def clean_cell_mathml(cell: str) -> str:
    """Clean a LaTeX table cell, returning MathML version."""
    s = cell.strip()
    s = re.sub(r"\\+\s*\[.*?\]\s*$", "", s)
    s = re.sub(r"\\+\s*$", "", s)
    s = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", s)
    mathml, _ = convert_title(s)
    return mathml.strip()


def parse_domain_table(text: str, domain_label: str, start_after: str) -> list[dict]:
    """Extract rows from a longtable environment after `start_after` marker."""
    # Find the table
    marker = start_after
    pos = text.find(marker)
    if pos == -1:
        print(f"  WARN: marker not found: {marker}")
        return []

    # Find the table body (between first \\endhead or \\endfirsthead and \\end{longtable})
    table_start = text.find("\\endlastfoot", pos)
    if table_start == -1:
        table_start = text.find("\\endfirsthead", pos)
    if table_start == -1:
        return []

    table_end = text.find("\\end{longtable}", table_start)
    if table_end == -1:
        return []

    body = text[table_start:table_end]

    # Split into rows by \\[3pt] or \\  (row separator in longtable)
    # Each row has 7 columns separated by &
    rows = []
    current_row = ""
    for line in body.split("\n"):
        line = line.strip()
        if not line or line.startswith("\\") and not line.startswith("$"):
            if line.startswith("\\endlastfoot") or line.startswith("\\endhead"):
                continue
            if line.startswith("\\midrule") or line.startswith("\\bottomrule"):
                continue
        current_row += " " + line

        # Check if we have a row terminator (\\[3pt] or \\ at end)
        if re.search(r"\\\\(\s*\[.*?\])?\s*$", current_row):
            # Split by & to get columns
            cells = current_row.split("&")
            if len(cells) >= 6:
                observable = clean_cell(cells[0])
                formula_plain = clean_cell(cells[1])
                formula_mathml = clean_cell_mathml(cells[1])
                tau_value = clean_cell(cells[2])
                observed = clean_cell(cells[3])
                deviation = clean_cell(cells[4])
                registry_id = clean_cell(cells[5]) if len(cells) > 5 else ""
                scope = clean_cell(cells[6]) if len(cells) > 6 else ""

                if observable and observable not in ("Observable", ""):
                    rows.append({
                        "observable": observable,
                        "formula_plain": formula_plain,
                        "formula_mathml": formula_mathml,
                        "tau_value": tau_value,
                        "observed": observed,
                        "deviation": deviation,
                        "registry_id": registry_id.strip(),
                        "scope_raw": scope.strip(),
                        "domain": domain_label,
                    })
            current_row = ""

    return rows


def classify_precision(deviation: str) -> str:
    """Classify a deviation string into a precision tier."""
    if not deviation:
        return "structural"
    # Normalize: replace ~ and non-breaking spaces with regular space
    d = deviation.replace("~", " ").replace("\u00a0", " ").strip()
    if d in ("--", "–", "—", "exact", "", "0"):
        if d == "exact":
            return "sub-10-ppm"  # exact match is the best precision
        return "structural"
    # Extract numeric value before "ppm"
    m = re.search(r"([\d.]+)\s*ppm", d)
    if m:
        val = float(m.group(1))
        if val <= 10:
            return "sub-10-ppm"
        if val <= 1000:
            return "10-1000-ppm"
        return "1-5-percent"
    if "%" in d:
        return "1-5-percent"
    if "dex" in d:
        return "1-5-percent"
    return "structural"


def classify_scope(scope_raw: str) -> str:
    """Normalize scope labels."""
    s = scope_raw.lower().strip()
    if "est" in s:
        return "established"
    if "eff" in s or "τ" in s:
        return "tau-effective"
    if "conj" in s:
        return "conjectural"
    if "meta" in s:
        return "metaphorical"
    return "tau-effective"


def slugify(text: str) -> str:
    """Make a URL-safe slug from text."""
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:80]


DOMAIN_DISPLAY = {
    "particle-physics": "Particle Physics",
    "electroweak-qcd": "Electroweak & QCD",
    "cosmology": "Cosmology",
    "astrophysics": "Astrophysics",
    "collective-dynamics": "Collective Dynamics",
}

SCOPE_DISPLAY = {
    "established": "Established",
    "tau-effective": "τ-Effective",
    "conjectural": "Conjectural",
    "metaphorical": "Metaphorical",
}

PRECISION_DISPLAY = {
    "sub-10-ppm": "Sub-10 ppm",
    "10-1000-ppm": "10–1000 ppm",
    "1-5-percent": "1–5%",
    "structural": "Structural",
}


# ---------------------------------------------------------------------------
# Falsification pack parser
# ---------------------------------------------------------------------------


def parse_falsification_pack(text: str) -> list[dict]:
    """Extract N1-N30 entries from the falsification pack section."""
    entries = []

    # Find the section
    start = text.find("\\section{The 30-Prediction Falsification Pack}")
    if start == -1:
        start = text.find("30-Prediction Falsification Pack")
    if start == -1:
        print("  WARN: Falsification pack section not found")
        return []

    # Find the end (next \\section)
    end = text.find("\\section{Falsifiable Seams", start + 100)
    if end == -1:
        end = len(text)

    section = text[start:end]

    # Parse each N-entry: \paragraph{Nk: Title.}
    pattern = re.compile(
        r"\\paragraph\{(N\d+):?\s*(.*?)\}(.*?)(?=\\paragraph\{N\d+|\\subsection|$)",
        re.DOTALL,
    )

    for m in pattern.finditer(section):
        nid = m.group(1).strip()
        title_raw = m.group(2).strip().rstrip(".")
        body = m.group(3).strip()

        # Clean title — use clean_bibfield for robustness (titles may contain
        # \texorpdfstring, nested math, and other LaTeX)
        title = clean_bibfield(title_raw).strip()
        if not title:
            title = title_raw.strip()

        # Extract experiment
        exp_match = re.search(r"\\emph\{Experiment:?\}\s*(.+?)(?:\.\s|\\emph|\\paragraph|$)", body)
        experiment = clean_bibfield(exp_match.group(1)) if exp_match else ""

        # Extract timeline
        tl_match = re.search(r"\\emph\{Timeline:?\}\s*(.+?)(?:\.\s|\\emph|\\paragraph|$)", body)
        timeline = clean_bibfield(tl_match.group(1)) if tl_match else ""

        # Extract decisive-if
        dec_match = re.search(r"\\emph\{Decisive\s+(?:if|at)\}\s*(.+?)(?:\.\s|\\emph|\\paragraph|$)", body)
        decisive = clean_bibfield(dec_match.group(1)) if dec_match else ""

        # Clean the body for prediction text (use clean_bibfield which is
        # more forgiving than clean_cell/convert_title for multi-sentence LaTeX)
        pred_raw = body.split("\\emph{Experiment")[0] if "\\emph{Experiment" in body else body
        pred_text = clean_bibfield(pred_raw)
        pred_text = re.sub(r"\s+", " ", pred_text).strip()

        # Extract registry ID
        reg_match = re.search(r"([IVX]+\.[TDPLRCX]\d+)", body)
        registry_id = reg_match.group(1) if reg_match else ""

        # Determine domain from subsection context
        # Find which subsection this entry belongs to
        domain = "particle-physics"  # default
        pre_text = section[:m.start()]
        if "CMB and Inflation" in pre_text[max(0, len(pre_text) - 500):]:
            domain = "cmb-inflation"
        elif "BBN" in pre_text[max(0, len(pre_text) - 300):]:
            domain = "bbn"
        elif "Dark Sector" in pre_text[max(0, len(pre_text) - 500):]:
            domain = "dark-sector"
        elif "Black Holes" in pre_text[max(0, len(pre_text) - 500):]:
            domain = "black-holes"
        elif "Collective Dynamics" in pre_text[max(0, len(pre_text) - 500):]:
            domain = "collective-dynamics"

        # Determine seam
        seam = None
        for seam_num in range(1, 8):
            if f"Seam {seam_num}" in body or f"seam {seam_num}" in body.lower():
                seam = seam_num
                break

        # Determine status
        status = "consistent"
        if "confirmed" in body.lower() or deviation_word_in("exact", body):
            status = "confirmed"
        elif "pending" in body.lower() or "(pending)" in body:
            status = "testable"

        n_num = int(nid[1:])
        # Clean title for slug (remove any remaining LaTeX artifacts)
        slug_title = re.sub(r"\\texorpdfstring\{[^{}]*\}\{[^{}]*\}", "", title)
        slug_title = re.sub(r"[^a-zA-Z0-9\s-]", "", slug_title).strip()
        entries.append({
            "id": nid,
            "n_num": n_num,
            "slug": slugify(f"{nid}-{slug_title}"),
            "title": title,
            "domain": domain,
            "domain_display": {
                "particle-physics": "Particle Physics",
                "cmb-inflation": "CMB & Inflation",
                "bbn": "BBN",
                "dark-sector": "Dark Sector",
                "black-holes": "Black Holes",
                "collective-dynamics": "Collective Dynamics",
            }.get(domain, domain),
            "prediction": pred_text[:400],
            "experiment": experiment,
            "timeline": timeline,
            "decisive": decisive,
            "current_status": status,
            "seam": seam,
            "registry_id": registry_id,
            "canonical_books": ["V"] if "V." in registry_id else ["IV"],
            "summary_short": f"{nid}: {title}. {experiment}.",
        })

    return entries


def deviation_word_in(word: str, text: str) -> bool:
    return word in text.lower()


# ---------------------------------------------------------------------------
# YAML / Markdown generators
# ---------------------------------------------------------------------------


def yaml_str(s: str) -> str:
    """Safely double-quote a string for YAML."""
    if s is None or s == "":
        return '""'
    escaped = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def generate_prediction_md(pred: dict) -> str:
    """Generate a prediction collection item markdown file."""
    lines = [
        "---",
        f"layout: prediction-page",
        f"title: {yaml_str(pred['title'])}",
        f"title_plain: {yaml_str(pred.get('title_plain', pred['title']))}",
        f"permalink: /predictions/{pred['slug']}/",
        f"lane: results",
        f"prediction_id: {yaml_str(pred['id'])}",
        f"domain: {yaml_str(pred['domain'])}",
        f"domain_display: {yaml_str(pred['domain_display'])}",
        f"observable: {yaml_str(pred['observable'])}",
        f"observable_mathml: {yaml_str(pred.get('observable_mathml', pred['observable']))}",
        f"formula_plain: {yaml_str(pred['formula_plain'])}",
        f"formula_mathml: {yaml_str(pred['formula_mathml'])}",
        f"tau_value: {yaml_str(pred['tau_value'])}",
        f"observed_value: {yaml_str(pred['observed'])}",
        f"deviation: {yaml_str(pred['deviation'])}",
        f"precision_tier: {yaml_str(pred['precision_tier'])}",
        f"precision_display: {yaml_str(pred['precision_display'])}",
        f"registry_id: {yaml_str(pred['registry_id'])}",
        f"scope: {yaml_str(pred['scope'])}",
        f"scope_display: {yaml_str(pred['scope_display'])}",
        f"canonical_books:",
    ]
    for b in pred.get("canonical_books", []):
        lines.append(f'  - "{b}"')
    lines.extend([
        f"summary_short: {yaml_str(pred['summary_short'])}",
        "right_rail:",
        "  toc: false",
        "  related:",
        '    - title: "Predictions Browse"',
        "      url: /results/predictions/browse/",
        '    - title: "Falsification Pack"',
        "      url: /results/falsifications/browse/",
        '    - title: "Results Overview"',
        "      url: /results/",
        "  meta:",
        f"    type: {yaml_str('Physics Prediction')}",
        f"    domain: {yaml_str(pred['domain_display'])}",
        f"    precision: {yaml_str(pred['precision_display'])}",
        f"    scope: {yaml_str(pred['scope_display'])}",
        '    updated: "April 2026"',
        "---",
        "",
        pred.get("body_text", pred["summary_short"]),
        "",
    ])
    return "\n".join(lines)


def generate_falsification_md(fals: dict) -> str:
    """Generate a falsification collection item markdown file."""
    lines = [
        "---",
        f"layout: falsification-page",
        f"title: {yaml_str(fals['id'] + ' — ' + fals['title'])}",
        f"permalink: /falsifications/{fals['slug']}/",
        f"lane: results",
        f"falsification_id: {yaml_str(fals['id'])}",
        f"n_num: {fals['n_num']}",
        f"domain: {yaml_str(fals['domain'])}",
        f"domain_display: {yaml_str(fals['domain_display'])}",
        f"prediction: {yaml_str(fals['prediction'][:300])}",
        f"experiment: {yaml_str(fals['experiment'])}",
        f"timeline: {yaml_str(fals['timeline'])}",
        f"decisive: {yaml_str(fals.get('decisive', ''))}",
        f"current_status: {yaml_str(fals['current_status'])}",
    ]
    if fals.get("seam") is not None:
        lines.append(f"seam: {fals['seam']}")
    else:
        lines.append("seam: null")
    lines.extend([
        f"registry_id: {yaml_str(fals['registry_id'])}",
        "canonical_books:",
    ])
    for b in fals.get("canonical_books", []):
        lines.append(f'  - "{b}"')
    lines.extend([
        f"summary_short: {yaml_str(fals['summary_short'])}",
        "right_rail:",
        "  toc: false",
        "  related:",
        '    - title: "Falsification Pack Browse"',
        "      url: /results/falsifications/browse/",
        '    - title: "Predictions Browse"',
        "      url: /results/predictions/browse/",
        '    - title: "Results Overview"',
        "      url: /results/",
        "  meta:",
        f"    type: {yaml_str('Falsification')}",
        f"    domain: {yaml_str(fals['domain_display'])}",
        f"    status: {yaml_str(fals['current_status'].capitalize())}",
        f"    experiment: {yaml_str(fals['experiment'][:60])}",
        '    updated: "April 2026"',
        "---",
        "",
        fals.get("prediction", fals["summary_short"]),
        "",
    ])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print(f"Reading {CH68}")
    raw = CH68.read_text(encoding="utf-8")
    text = strip_comments(raw)
    print(f"  {len(text)} chars after comment stripping")

    # Parse domain tables
    domain_markers = [
        ("particle-physics", "Domain A: Particle Physics"),
        ("electroweak-qcd", "Domain B: Electroweak and QCD"),
        ("cosmology", "Domain C: Cosmology"),
        ("astrophysics", "Domain D: Astrophysics"),
        ("collective-dynamics", "Domain E: Collective Dynamics"),
    ]

    all_predictions = []
    for domain_slug, marker in domain_markers:
        rows = parse_domain_table(text, domain_slug, marker)
        print(f"  Domain {domain_slug}: {len(rows)} rows")
        all_predictions.extend(rows)

    print(f"\nTotal predictions parsed: {len(all_predictions)}")

    # Enrich each prediction (with unique slugs)
    pred_idx = 0
    seen_slugs = set()
    for pred in all_predictions:
        pred_idx += 1
        pred["id"] = f"pred-{pred_idx:03d}"
        base_slug = slugify(pred["observable"])
        # Ensure uniqueness by appending index if needed
        slug = base_slug
        if slug in seen_slugs or not slug:
            slug = f"{base_slug}-{pred_idx}" if base_slug else f"pred-{pred_idx}"
        seen_slugs.add(slug)
        pred["slug"] = slug
        pred["title"] = pred["observable"]
        pred["title_plain"] = pred["observable"]
        pred["observable_mathml"] = pred.get("formula_mathml", pred["observable"])
        pred["precision_tier"] = classify_precision(pred["deviation"])
        pred["precision_display"] = PRECISION_DISPLAY.get(pred["precision_tier"], "")
        pred["scope"] = classify_scope(pred["scope_raw"])
        pred["scope_display"] = SCOPE_DISPLAY.get(pred["scope"], "")
        pred["domain_display"] = DOMAIN_DISPLAY.get(pred["domain"], pred["domain"])
        # Derive canonical books from registry ID
        if pred["registry_id"].startswith("V."):
            pred["canonical_books"] = ["V"]
        elif pred["registry_id"].startswith("IV."):
            pred["canonical_books"] = ["IV"]
        else:
            pred["canonical_books"] = ["IV", "V"]
        pred["summary_short"] = (
            f"{pred['observable']}: τ-value {pred['tau_value']}"
            f"{', observed ' + pred['observed'] if pred['observed'] and pred['observed'] not in ('--', '(pending)') else ''}"
            f"{', deviation ' + pred['deviation'] if pred['deviation'] and pred['deviation'] != '--' else ''}."
        )
        pred["body_text"] = pred["summary_short"]

    # Parse falsification pack
    falsifications = parse_falsification_pack(text)
    print(f"Falsifications parsed: {len(falsifications)}")

    # Generate collection files
    OUT_PREDICTIONS.mkdir(parents=True, exist_ok=True)
    OUT_FALSIFICATIONS.mkdir(parents=True, exist_ok=True)
    OUT_DATA_PRED.mkdir(parents=True, exist_ok=True)
    OUT_DATA_FALS.mkdir(parents=True, exist_ok=True)

    # Write predictions
    for pred in all_predictions:
        path = OUT_PREDICTIONS / f"{pred['slug']}.md"
        path.write_text(generate_prediction_md(pred), encoding="utf-8")

    print(f"\nWrote {len(all_predictions)} prediction files to {OUT_PREDICTIONS}/")

    # Write falsifications
    for fals in falsifications:
        path = OUT_FALSIFICATIONS / f"{fals['slug']}.md"
        path.write_text(generate_falsification_md(fals), encoding="utf-8")

    print(f"Wrote {len(falsifications)} falsification files to {OUT_FALSIFICATIONS}/")

    # Write data JSON files
    pred_data = []
    for pred in all_predictions:
        pred_data.append({
            "id": pred["id"],
            "slug": pred["slug"],
            "title": pred["title"],
            "title_plain": pred.get("title_plain", pred["title"]),
            "domain": pred["domain"],
            "domain_display": pred["domain_display"],
            "tau_value": pred["tau_value"],
            "observed": pred["observed"],
            "deviation": pred["deviation"],
            "precision_tier": pred["precision_tier"],
            "precision_display": pred["precision_display"],
            "scope": pred["scope"],
            "scope_display": pred["scope_display"],
            "registry_id": pred["registry_id"],
            "canonical_books": pred["canonical_books"],
            "summary_short": pred["summary_short"],
            "url": f"/predictions/{pred['slug']}/",
        })

    (OUT_DATA_PRED / "predictions.json").write_text(
        json.dumps(pred_data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Wrote predictions.json ({len(pred_data)} entries)")

    fals_data = []
    for fals in falsifications:
        fals_data.append({
            "id": fals["id"],
            "n_num": fals["n_num"],
            "slug": fals["slug"],
            "title": fals["title"],
            "domain": fals["domain"],
            "domain_display": fals["domain_display"],
            "prediction": fals["prediction"][:300],
            "experiment": fals["experiment"],
            "timeline": fals["timeline"],
            "current_status": fals["current_status"],
            "seam": fals["seam"],
            "registry_id": fals["registry_id"],
            "canonical_books": fals["canonical_books"],
            "summary_short": fals["summary_short"],
            "url": f"/falsifications/{fals['slug']}/",
        })

    (OUT_DATA_FALS / "falsifications.json").write_text(
        json.dumps(fals_data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Wrote falsifications.json ({len(fals_data)} entries)")

    # Summary
    print("\n" + "=" * 60)
    print("Physics Ledger build summary")
    print("=" * 60)
    print(f"  Predictions:     {len(all_predictions)}")
    print(f"  Falsifications:  {len(falsifications)}")
    print()
    print("  Predictions by domain:")
    from collections import Counter
    for domain, count in Counter(p["domain"] for p in all_predictions).most_common():
        print(f"    {DOMAIN_DISPLAY.get(domain, domain):<30} {count}")
    print()
    print("  Predictions by precision:")
    for tier, count in Counter(p["precision_tier"] for p in all_predictions).most_common():
        print(f"    {PRECISION_DISPLAY.get(tier, tier):<30} {count}")
    print()
    print("  Predictions by scope:")
    for scope, count in Counter(p["scope"] for p in all_predictions).most_common():
        print(f"    {SCOPE_DISPLAY.get(scope, scope):<30} {count}")


if __name__ == "__main__":
    main()
