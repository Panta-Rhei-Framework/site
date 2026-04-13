#!/usr/bin/env python3
"""
build_bibliography.py — Parse references.bib and generate Jekyll collection items + data files.

Outputs:
  _bibliography/<slug>.md          (one per entry, ~1125 files)
  _data/bibliography/index.json    (flat lookup array)
  _data/bibliography/groups.json   (entries grouped by domain)
  assets/bibliography/references.bib (downloadable copy)
"""

import re
import os
import json
import shutil
from collections import defaultdict

# ─── Paths ────────────────────────────────────────────────────────────────────

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB_SOURCE = os.path.join(
    os.path.expanduser("~"),
    "Books/PantaRhei-2ndEd/website/specs/bibliography-briefing-pack/references.bib",
)
OUT_COLLECTION = os.path.join(SITE_ROOT, "_bibliography")
OUT_DATA = os.path.join(SITE_ROOT, "_data", "bibliography")
OUT_ASSET = os.path.join(SITE_ROOT, "assets", "bibliography")


# ─── BibTeX parser ────────────────────────────────────────────────────────────

def parse_bib(path):
    """Parse a BibTeX file into a list of dicts. No external deps needed."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    entries = []
    # Match @type{key, ... }  (handles nested braces up to 3 levels)
    pattern = r"@(\w+)\{([^,]+),\s*((?:[^{}]|\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\})*)\}"
    for m in re.finditer(pattern, content):
        entry_type = m.group(1).lower()
        key = m.group(2).strip()
        body = m.group(3)

        if entry_type == "comment":
            continue

        entry = {"key": key, "entry_type": entry_type}

        # Parse fields: field = {value} or field = "value" or field = number
        field_pat = r"(\w+)\s*=\s*(?:\{((?:[^{}]|\{[^{}]*\})*)\}|\"([^\"]*)\"|(\d+))"
        for fm in re.finditer(field_pat, body):
            field_name = fm.group(1).lower()
            value = fm.group(2) or fm.group(3) or fm.group(4) or ""
            entry[field_name] = clean_latex(value.strip())

        entries.append(entry)

    return entries


def clean_latex(s):
    """Remove common LaTeX markup from field values."""
    s = re.sub(r"\\texorpdfstring\{[^}]*\}\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\textit\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\textbf\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\emph\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\textsc\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\{\\em\s+([^}]*)\}", r"\1", s)
    s = s.replace("\\&", "&")
    s = s.replace("\\%", "%")
    s = s.replace("\\'e", "e")
    s = s.replace("\\'a", "a")
    s = s.replace('\\"o', "o")
    s = s.replace('\\"u', "u")
    s = s.replace('\\"a', "a")
    s = s.replace("\\`e", "e")
    s = s.replace("\\^e", "e")
    s = s.replace("\\c{c}", "c")
    s = s.replace("---", "\u2014")
    s = s.replace("--", "\u2013")
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def slugify(key):
    """Turn a BibTeX key into a URL-safe slug."""
    s = key.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s


# ─── Domain classification ────────────────────────────────────────────────────

DOMAIN_RULES = [
    ("Category Theory", [
        "categ", "topos", "functor", "adjoint", "sheaf", "sheaves", "monad",
        "enriched", "lawvere", "mac lane", "maclane", "grothendieck", "fibr",
        "presheaf", "yoneda", "kan extension", "operads",
    ]),
    ("Foundations and Logic", [
        "logic", "set theory", "axiom", "proof", "decidab", "godel", "goedel",
        "computab", "incomplet", "type theory", "foundati", "constructiv",
        "model theory", "forcing", "cardinal", "ordinal", "peano",
    ]),
    ("Topology and Geometry", [
        "topolog", "manifold", "homotop", "cohomol", "homolog", "geom",
        "bundle", "fibration", "algebraic geometry", "riemann surface",
        "differential", "curvatur", "metric space", "poincare",
    ]),
    ("Number Theory and Analysis", [
        "number theory", "prime", "zeta", "l-function", "riemann hypothesis",
        "analytic", "arithmetic", "dirichlet", "modular form", "automorphic",
        "elliptic curve", "langlands", "galois", "algebraic number",
        "bsd conjecture", "birch", "swinnerton",
    ]),
    ("Physics", [
        "physic", "quantum", "relativity", "cosmolog", "gauge", "field theory",
        "particle", "gravitati", "planck", "standard model", "boson", "fermion",
        "higgs", "electroweak", "yang-mills", "navier-stokes", "thermodynamic",
        "entropy", "hubble", "dark matter", "dark energy", "cmb",
    ]),
    ("Life and Biology", [
        "biolog", "evolut", "cell", "genetic", "organism", "ecolog", "neural",
        "cogniti", "animal", "brain", "life", "species", "dna", "rna",
        "protein", "origin of life", "abiogenesis", "darwi",
    ]),
    ("Metaphysics and Philosophy", [
        "metaphysic", "ontolog", "epistem", "phenomenol", "heidegger",
        "husserl", "whitehead", "modal", "philosophy", "existence",
        "consciousness", "ethics", "aesthetic", "hermeneutic", "wittgenstein",
        "kant", "hegel", "nietzsche", "aristotle", "plato",
    ]),
    ("Computation and Complexity", [
        "complexity", "algorithm", "turing", "computat", "automata",
        "np-hard", "np-complete", "polynomial", "circuit", "information theory",
        "kolmogorov", "halting", "recursive",
    ]),
]


def classify_domain(entry):
    """Classify an entry into a domain group based on keyword heuristics."""
    search_text = " ".join([
        entry.get("title", ""),
        entry.get("journal", ""),
        entry.get("booktitle", ""),
        entry.get("series", ""),
        entry.get("publisher", ""),
        entry.get("note", ""),
    ]).lower()

    for domain, keywords in DOMAIN_RULES:
        for kw in keywords:
            if kw in search_text:
                return domain

    return "Foundations and Logic"  # conservative default


# ─── Role classification ──────────────────────────────────────────────────────

def classify_role(entry, domain):
    """Auto-assign a role in the research program."""
    authors = entry.get("author", "").lower()
    title = entry.get("title", "").lower()
    entry_type = entry.get("entry_type", "")

    # Program authors → foundational-source
    if "fuchs" in authors and ("panta" in title or "categorical" in title):
        return "foundational-source"

    # Standard textbooks
    textbook_signals = ["introduction", "course", "graduate texts", "textbook",
                        "primer", "handbook", "encyclopedia"]
    if entry_type == "book" and any(s in title for s in textbook_signals):
        return "domain-context"

    # Core category theory
    if domain == "Category Theory":
        if entry_type == "book":
            return "foundational-source"
        return "formal-antecedent"

    # Foundations
    if domain == "Foundations and Logic":
        return "formal-antecedent"

    # Philosophy → conceptual bridge
    if domain == "Metaphysics and Philosophy":
        return "conceptual-bridge"

    # Physics/biology → domain context
    if domain in ("Physics", "Life and Biology"):
        return "domain-context"

    # Default
    return "domain-context"


# ─── Editorial notes ──────────────────────────────────────────────────────────

ROLE_NOTE_TEMPLATES = {
    "foundational-source":
        "Included as a foundational source for {domain} on which the program directly builds.",
    "formal-antecedent":
        "Included as a formal antecedent establishing structures that the program extends or reinterprets.",
    "historical-lineage":
        "Included as a historical lineage marker in the intellectual tradition the program inhabits.",
    "methodological-anchor":
        "Included as a methodological anchor informing the program's approach to {domain}.",
    "conceptual-bridge":
        "Included as a conceptual bridge connecting {domain} to the program's coherence framework.",
    "comparative-reference":
        "Included as a comparative reference against which the program's claims can be measured.",
    "contrast-or-foil":
        "Included as a contrast or foil defining an alternative framing the program positions against.",
    "domain-context":
        "Included to provide standard reference context for {domain}.",
}

ROLE_DISPLAY = {
    "foundational-source": "Foundational Source",
    "formal-antecedent": "Formal Antecedent",
    "historical-lineage": "Historical Lineage",
    "methodological-anchor": "Methodological Anchor",
    "conceptual-bridge": "Conceptual Bridge",
    "comparative-reference": "Comparative Reference",
    "contrast-or-foil": "Contrast / Foil",
    "domain-context": "Domain Context",
}

TYPE_DISPLAY = {
    "book": "Book",
    "article": "Article",
    "incollection": "Book Chapter",
    "inproceedings": "Conference Paper",
    "phdthesis": "PhD Thesis",
    "misc": "Miscellaneous",
    "unpublished": "Unpublished",
}


def editorial_note(role, domain):
    template = ROLE_NOTE_TEMPLATES.get(role, ROLE_NOTE_TEMPLATES["domain-context"])
    return template.format(domain=domain)


# ─── YAML helpers ─────────────────────────────────────────────────────────────

def yaml_str(s):
    """Safely quote a string for YAML frontmatter."""
    if not s:
        return '""'
    # If it contains special characters, quote it
    if any(c in s for c in ':"\'{}[]&*?|>!%@`#,'):
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    if s.startswith(("-", " ")) or s.endswith(" "):
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    return f'"{s}"'


# ─── Generator ────────────────────────────────────────────────────────────────

def generate_all(entries):
    """Generate all output files."""
    # Clean output directories
    if os.path.exists(OUT_COLLECTION):
        shutil.rmtree(OUT_COLLECTION)
    os.makedirs(OUT_COLLECTION, exist_ok=True)
    os.makedirs(OUT_DATA, exist_ok=True)
    os.makedirs(OUT_ASSET, exist_ok=True)

    index_data = []
    groups = defaultdict(list)

    for entry in entries:
        key = entry["key"]
        slug = slugify(key)
        title = entry.get("title", key)
        authors = entry.get("author", "Unknown")
        year = entry.get("year", "n.d.")
        entry_type = entry.get("entry_type", "misc")
        journal = entry.get("journal", entry.get("booktitle", ""))
        publisher = entry.get("publisher", "")
        volume = entry.get("volume", "")
        number = entry.get("number", "")
        pages = entry.get("pages", "")
        doi = entry.get("doi", "")
        url = entry.get("url", "")
        isbn = entry.get("isbn", "")
        series = entry.get("series", "")
        edition = entry.get("edition", "")
        arxiv = entry.get("eprint", entry.get("arxiv", ""))

        domain = classify_domain(entry)
        role = classify_role(entry, domain)
        note = editorial_note(role, domain)

        type_display = TYPE_DISPLAY.get(entry_type, entry_type.title())
        role_display = ROLE_DISPLAY.get(role, role.replace("-", " ").title())

        # Build formatted citation
        citation_parts = []
        if authors:
            citation_parts.append(authors)
        if year:
            citation_parts.append(f"({year})")
        if title:
            citation_parts.append(f"*{title}*")
        if journal:
            citation_parts.append(journal)
        if volume:
            vol_str = f"**{volume}**"
            if number:
                vol_str += f"({number})"
            citation_parts.append(vol_str)
        if pages:
            citation_parts.append(f"pp. {pages}")
        if publisher:
            citation_parts.append(publisher)
        citation = ". ".join(citation_parts) + "."

        # ── Write collection item ──
        md_lines = [
            "---",
            f"title: {yaml_str(title)}",
            f"bib_key: {yaml_str(key)}",
            f"entry_type: {yaml_str(entry_type)}",
            f"authors: {yaml_str(authors)}",
            f"year: {yaml_str(year)}",
            f"journal_or_booktitle: {yaml_str(journal)}",
            f"publisher: {yaml_str(publisher)}",
            f"volume: {yaml_str(volume)}",
            f"number: {yaml_str(number)}",
            f"pages: {yaml_str(pages)}",
            f"doi: {yaml_str(doi)}",
            f"url: {yaml_str(url)}",
            f"isbn: {yaml_str(isbn)}",
            f"arxiv: {yaml_str(arxiv)}",
            f"series: {yaml_str(series)}",
            f"edition: {yaml_str(edition)}",
            f"domain_group: {yaml_str(domain)}",
            f"role_in_program: {yaml_str(role)}",
            f"role_display: {yaml_str(role_display)}",
            f"type_display: {yaml_str(type_display)}",
            f"formatted_citation: {yaml_str(citation)}",
            "right_rail:",
            "  toc: false",
            "  related:",
            '    - title: "Bibliography"',
            "      url: /bibliography/",
            '    - title: "About the Research"',
            "      url: /research-program/about/",
            "  artifacts:",
            '    - title: "Download references.bib"',
            "      url: /assets/bibliography/references.bib",
            "  meta:",
            f"    type: {yaml_str(type_display)}",
            f"    year: {yaml_str(year)}",
            f"    domain: {yaml_str(domain)}",
            f"    role: {yaml_str(role_display)}",
            '    updated: "April 2026"',
            "---",
            "",
            note,
            "",
        ]

        out_path = os.path.join(OUT_COLLECTION, f"{slug}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))

        # ── Index data ──
        index_entry = {
            "key": key,
            "slug": slug,
            "title": title,
            "authors": authors,
            "year": year,
            "entry_type": entry_type,
            "type_display": type_display,
            "domain_group": domain,
            "role_in_program": role,
            "role_display": role_display,
            "journal_or_booktitle": journal,
            "publisher": publisher,
            "doi": doi,
            "url": f"/bibliography/{slug}/",
        }
        index_data.append(index_entry)
        groups[domain].append(index_entry)

    # Sort index by year desc, then author asc
    index_data.sort(key=lambda e: (-int(e["year"]) if e["year"].isdigit() else 0, e["authors"]))

    # Sort groups
    domain_order = [d for d, _ in DOMAIN_RULES]
    groups_output = []
    for domain in domain_order:
        items = groups.get(domain, [])
        items.sort(key=lambda e: (-int(e["year"]) if e["year"].isdigit() else 0, e["authors"]))
        groups_output.append({
            "domain": domain,
            "slug": slugify(domain),
            "count": len(items),
            "entries": items,
        })

    # Write data files
    with open(os.path.join(OUT_DATA, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT_DATA, "groups.json"), "w", encoding="utf-8") as f:
        json.dump(groups_output, f, indent=2, ensure_ascii=False)

    # Copy raw .bib as downloadable asset
    shutil.copy2(BIB_SOURCE, os.path.join(OUT_ASSET, "references.bib"))

    # Summary
    print(f"Generated {len(entries)} collection items in {OUT_COLLECTION}/")
    print(f"Generated index.json ({len(index_data)} entries)")
    print(f"Generated groups.json ({len(groups_output)} groups)")
    for g in groups_output:
        print(f"  {g['domain']}: {g['count']} entries")
    print(f"Copied references.bib to {OUT_ASSET}/")


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Parsing {BIB_SOURCE}...")
    entries = parse_bib(BIB_SOURCE)
    print(f"Found {len(entries)} entries")
    generate_all(entries)
    print("Done!")
