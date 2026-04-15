#!/usr/bin/env python3
"""
build_bibliography.py — Parse references.bib and generate Jekyll collection items + data files.

Consumes:
  _data/bibliography/citation_index.json  (from build_citation_index.py)
  _data/bibliography/overrides.yml        (hand-crafted editorial prose)
  scripts/latex_to_mathml.py              (MathML converter)

Outputs:
  _bibliography/<slug>.md                 (one per entry, ~1125 files)
  _data/bibliography/index.json           (flat lookup array)
  _data/bibliography/groups.json          (entries grouped by domain)
  assets/bibliography/references.bib      (downloadable copy)

Per-item frontmatter schema:
  title: MathML-enabled title for <h1> rendering (may contain <math> tags)
  title_plain: Unicode-only title for SEO meta tags, JSON-LD, <title>
  formatted_citation: MathML-enabled citation string
  formatted_citation_plain: Unicode-only citation
  cited_in: [{book, book_title, part, chapter_file, chapter_title, excerpt}, ...]
  is_orphan: true if not cited in any book manuscript
  has_manual_override: true if overrides.yml has an entry for this key

Body content:
  Editorial prose from overrides.yml if present, else orphan template.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

SITE_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(Path(__file__).parent))

from latex_to_mathml import (
    convert_title,
    clean_bibfield,
    latex_accents_to_unicode,
)

BIB_SOURCE = Path(
    os.path.expanduser(
        "~/Books/PantaRhei-2ndEd/website/specs/bibliography-briefing-pack/references.bib"
    )
)
OUT_COLLECTION_DEFAULT = SITE_ROOT / "_bibliography"
OUT_DATA = SITE_ROOT / "_data" / "bibliography"
OUT_ASSET = SITE_ROOT / "assets" / "bibliography"
CITATION_INDEX_PATH = OUT_DATA / "citation_index.json"
OVERRIDES_PATH = OUT_DATA / "overrides.yml"


# ─── BibTeX parser ────────────────────────────────────────────────────────────


def _find_matching_brace(text: str, open_pos: int) -> int:
    """Return the index of the matching `}` for the `{` at open_pos.

    Returns -1 if not found. Handles arbitrary nesting.
    """
    assert text[open_pos] == "{"
    depth = 1
    i = open_pos + 1
    while i < len(text):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def _parse_entry_fields(body: str) -> dict:
    """Parse fields out of a BibTeX entry body with full brace matching."""
    fields = {}
    i = 0
    n = len(body)
    while i < n:
        # Skip whitespace and commas
        while i < n and body[i] in " \t\n\r,":
            i += 1
        if i >= n:
            break

        # Read field name (alphanumeric / underscore)
        name_start = i
        while i < n and (body[i].isalnum() or body[i] == "_"):
            i += 1
        if i == name_start:
            # No valid field name; skip to next safe char
            i += 1
            continue
        field_name = body[name_start:i].lower()

        # Skip to `=`
        while i < n and body[i] in " \t\n\r":
            i += 1
        if i >= n or body[i] != "=":
            continue
        i += 1  # past `=`

        # Skip whitespace
        while i < n and body[i] in " \t\n\r":
            i += 1
        if i >= n:
            break

        # Value is: {nested}, "quoted", or bare number/ident
        if body[i] == "{":
            end = _find_matching_brace(body, i)
            if end == -1:
                break
            value = body[i + 1:end]
            i = end + 1
        elif body[i] == '"':
            # Find closing " (ignore escaped \")
            j = i + 1
            while j < n:
                if body[j] == '"' and (j == 0 or body[j - 1] != "\\"):
                    break
                j += 1
            if j >= n:
                break
            value = body[i + 1:j]
            i = j + 1
        else:
            # Bare value up to comma or newline or `}`
            j = i
            while j < n and body[j] not in ",\n}":
                j += 1
            value = body[i:j].strip()
            i = j

        fields[field_name] = value.strip()

    return fields


def parse_bib(path: Path):
    """Parse a BibTeX file into a list of entry dicts."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    entries = []
    i = 0
    n = len(content)
    while i < n:
        # Find next @entry
        at = content.find("@", i)
        if at == -1:
            break
        i = at + 1

        # Read entry type
        name_start = i
        while i < n and (content[i].isalnum() or content[i] == "_"):
            i += 1
        entry_type = content[name_start:i].lower()

        if entry_type == "comment":
            # Skip the comment
            if i < n and content[i] == "{":
                end = _find_matching_brace(content, i)
                i = end + 1 if end != -1 else n
            continue

        # Skip whitespace
        while i < n and content[i] in " \t\n\r":
            i += 1
        if i >= n or content[i] != "{":
            continue

        # Find matching close brace for the whole entry
        entry_close = _find_matching_brace(content, i)
        if entry_close == -1:
            break
        entry_body_with_key = content[i + 1:entry_close]
        i = entry_close + 1

        # Split key from body: key is everything before the first comma (outside braces)
        depth = 0
        key_end = -1
        for k in range(len(entry_body_with_key)):
            ch = entry_body_with_key[k]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            elif ch == "," and depth == 0:
                key_end = k
                break
        if key_end == -1:
            continue
        key = entry_body_with_key[:key_end].strip()
        body = entry_body_with_key[key_end + 1:]

        fields = _parse_entry_fields(body)
        entries.append({
            "key": key,
            "entry_type": entry_type,
            "_raw": fields,
        })

    return entries


def field(entry: dict, *names: str) -> str:
    """Fetch the first non-empty value for any of the given field names."""
    for name in names:
        val = entry.get("_raw", {}).get(name)
        if val:
            return val
    return ""


def slugify(key: str) -> str:
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


def classify_domain(entry: dict) -> str:
    """Classify an entry into a domain group based on keyword heuristics."""
    search_text = " ".join([
        field(entry, "title"),
        field(entry, "journal", "journaltitle"),
        field(entry, "booktitle"),
        field(entry, "series"),
        field(entry, "publisher"),
        field(entry, "note"),
    ]).lower()

    for domain, keywords in DOMAIN_RULES:
        for kw in keywords:
            if kw in search_text:
                return domain

    return "Foundations and Logic"


def classify_role(entry: dict, domain: str) -> str:
    """Auto-assign a role in the research program."""
    authors = field(entry, "author").lower()
    title = field(entry, "title").lower()
    entry_type = entry.get("entry_type", "")

    # Program authors → foundational-source
    if "fuchs" in authors and ("panta" in title or "categorical" in title):
        return "foundational-source"

    textbook_signals = [
        "introduction", "course", "graduate texts", "textbook",
        "primer", "handbook", "encyclopedia",
    ]
    if entry_type == "book" and any(s in title for s in textbook_signals):
        return "domain-context"

    if domain == "Category Theory":
        return "foundational-source" if entry_type == "book" else "formal-antecedent"

    if domain == "Foundations and Logic":
        return "formal-antecedent"

    if domain == "Metaphysics and Philosophy":
        return "conceptual-bridge"

    if domain in ("Physics", "Life and Biology"):
        return "domain-context"

    return "domain-context"


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


# ─── Orphan editorial prose ───────────────────────────────────────────────────


ORPHAN_TEMPLATES = {
    "foundational-source": (
        "{authors_poss} {title_md}{year_clause} sits in the program's reference "
        "corpus as a standing technical source in {domain}. It forms part of the "
        "foundational literature the program builds upon, though it is not "
        "directly cited in the currently published volumes of *Panta Rhei*."
    ),
    "formal-antecedent": (
        "{authors_poss} {title_md}{year_clause} is part of the program's reference "
        "corpus, acknowledged as a formal antecedent in {domain} whose structures "
        "inform the framework's vocabulary. It is retained in the corpus for "
        "completeness, though it is not directly cited in the currently published "
        "volumes of *Panta Rhei*."
    ),
    "historical-lineage": (
        "{authors_poss} {title_md}{year_clause} sits in the program's reference "
        "corpus as a historical-lineage marker in {domain}, part of the intellectual "
        "tradition the program inhabits. It is not directly cited in the currently "
        "published volumes of *Panta Rhei*."
    ),
    "methodological-anchor": (
        "{authors_poss} {title_md}{year_clause} is retained in the program's "
        "reference corpus as a methodological anchor informing the approach to "
        "{domain}. It is not directly cited in the currently published volumes of "
        "*Panta Rhei*."
    ),
    "conceptual-bridge": (
        "{authors_poss} {title_md}{year_clause} sits in the program's reference "
        "corpus as a conceptual bridge between {domain} and the framework's "
        "broader aims. It is not directly cited in the currently published volumes "
        "of *Panta Rhei*, but remains part of the standing reference shelf."
    ),
    "comparative-reference": (
        "{authors_poss} {title_md}{year_clause} is part of the program's reference "
        "corpus as a comparative reference in {domain}. It is not directly cited "
        "in the currently published volumes of *Panta Rhei*."
    ),
    "contrast-or-foil": (
        "{authors_poss} {title_md}{year_clause} is part of the program's reference "
        "corpus as a contrast or foil in {domain}, marking an alternative framing "
        "the program positions against. It is not directly cited in the currently "
        "published volumes of *Panta Rhei*."
    ),
    "domain-context": (
        "{authors_poss} {title_md}{year_clause} is part of the program's reference "
        "corpus as standard domain context for {domain}. It is not directly cited "
        "in the currently published volumes of *Panta Rhei*, but is retained as "
        "part of the research shelf."
    ),
}


def _possessive(name: str) -> str:
    if not name or name == "Unknown":
        return "The"
    if name.endswith("s"):
        return name + "'"
    return name + "'s"


def _simple_author_label(authors_raw: str) -> str:
    """Produce a simple surname-based label for orphan prose."""
    if not authors_raw:
        return "Unknown"
    # Resolve accents
    s = latex_accents_to_unicode(authors_raw)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    # Handle collaborations
    if "Collaboration" in s or "collaboration" in s:
        return "The collaboration"
    parts = [p.strip() for p in re.split(r"\s+and\s+", s)]

    def surname(person: str) -> str:
        if "," in person:
            return person.split(",")[0].strip()
        tokens = person.split()
        if not tokens:
            return person
        return tokens[-1]

    surnames = [surname(p) for p in parts]
    if len(surnames) == 1:
        return surnames[0]
    if len(surnames) == 2:
        return f"{surnames[0]} and {surnames[1]}"
    return f"{surnames[0]} et al."


def orphan_prose(role: str, domain: str, authors: str, title: str, year: str) -> str:
    """Generate editorial prose for an entry not cited in any book manuscript."""
    template = ORPHAN_TEMPLATES.get(role, ORPHAN_TEMPLATES["domain-context"])
    author_label = _simple_author_label(authors)
    authors_poss = _possessive(author_label)
    # Escape literal asterisks in the title so kramdown doesn't misinterpret
    # them as Markdown italic markers when rendering the <em> block.
    title_escaped = (title or "").rstrip(".").replace("*", "&#42;")
    title_md = f"<em>{title_escaped}</em>" if title_escaped else "this reference"
    year_clause = f" ({year})" if year else ""
    return template.format(
        authors_poss=authors_poss,
        title_md=title_md,
        year_clause=year_clause,
        domain=domain,
    )


# ─── Overrides loading ────────────────────────────────────────────────────────


def load_overrides() -> dict:
    """Load the editorial overrides YAML, or return empty dict if missing."""
    if not OVERRIDES_PATH.exists():
        return {}
    try:
        import yaml
    except ImportError:
        print("WARNING: PyYAML not available; overrides not loaded", file=sys.stderr)
        return {}
    with open(OVERRIDES_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def load_citation_index() -> dict:
    """Load the citation index built by build_citation_index.py."""
    if not CITATION_INDEX_PATH.exists():
        return {}
    with open(CITATION_INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# ─── YAML helpers ─────────────────────────────────────────────────────────────


def yaml_str(s: str) -> str:
    """Safely double-quote a string for YAML frontmatter. Preserves HTML/MathML."""
    if s is None or s == "":
        return '""'
    # Escape backslash and double-quote. MathML uses <tags> and single-quoted
    # attributes, so there are no backslashes or double-quotes in valid output.
    escaped = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_block(text: str, indent: int = 2) -> str:
    """Emit a multi-line string as a YAML block scalar (|)."""
    prefix = " " * indent
    lines = text.rstrip().split("\n")
    return "\n".join(prefix + line for line in lines)


# ─── Generator ────────────────────────────────────────────────────────────────


def build_formatted_citation(
    authors: str, year: str, title_md: str, title_plain: str,
    journal: str, publisher: str, volume: str, number: str, pages: str,
    use_mathml_title: bool = False,
):
    """Build two citation strings: one with MathML title, one plain.

    Uses HTML <em> for italic (not Markdown *...*) because some titles
    start or end with asterisks (e.g., "$*$-Autonomous Categories") which
    break Markdown parsing.
    """
    def build(title_variant):
        parts = []
        if authors:
            parts.append(authors)
        if year:
            parts.append(f"({year})")
        if title_variant:
            parts.append(f"<em>{title_variant}</em>")
        if journal:
            parts.append(f"<em>{journal}</em>")
        if volume:
            vol_str = f"<strong>{volume}</strong>"
            if number:
                vol_str += f"({number})"
            parts.append(vol_str)
        if pages:
            parts.append(f"pp. {pages}")
        if publisher:
            parts.append(publisher)
        return ". ".join(parts) + "."

    return build(title_md), build(title_plain)


def generate_all(entries, out_collection: Path, dry_run: bool = False):
    """Generate all output files."""
    citation_index = load_citation_index()
    overrides = load_overrides()

    if not out_collection.exists():
        out_collection.mkdir(parents=True, exist_ok=True)
    elif not dry_run:
        shutil.rmtree(out_collection)
        out_collection.mkdir(parents=True, exist_ok=True)

    OUT_DATA.mkdir(parents=True, exist_ok=True)
    OUT_ASSET.mkdir(parents=True, exist_ok=True)

    index_data = []
    groups = defaultdict(list)

    stats = {
        "total": 0,
        "overrides_applied": 0,
        "cited_entries": 0,
        "orphan_entries": 0,
        "mathml_titles": 0,
    }

    for entry in entries:
        key = entry["key"]
        slug = slugify(key)

        # Raw fields (still with LaTeX)
        raw_title = field(entry, "title")
        raw_authors = field(entry, "author")
        raw_journal = field(entry, "journal", "journaltitle")
        raw_booktitle = field(entry, "booktitle")
        raw_publisher = field(entry, "publisher")
        raw_series = field(entry, "series")

        # Title → (MathML, plain) pair
        try:
            title_mathml, title_plain = convert_title(raw_title) if raw_title else ("", "")
        except Exception as e:
            print(f"WARN: convert_title failed for {key}: {e}", file=sys.stderr)
            title_mathml = raw_title
            title_plain = raw_title
        if title_mathml != title_plain and "<math" in title_mathml:
            stats["mathml_titles"] += 1

        # Other fields: clean_bibfield (non-destructive)
        authors = clean_bibfield(raw_authors) or "Unknown"
        year = field(entry, "year") or "n.d."
        entry_type = entry.get("entry_type", "misc")
        journal = clean_bibfield(raw_journal) or clean_bibfield(raw_booktitle)
        publisher = clean_bibfield(raw_publisher)
        series = clean_bibfield(raw_series)
        edition = clean_bibfield(field(entry, "edition"))

        volume = field(entry, "volume")
        number = field(entry, "number")
        pages = field(entry, "pages")
        doi = field(entry, "doi")
        url = field(entry, "url")
        isbn = field(entry, "isbn")
        arxiv = field(entry, "eprint", "arxiv")

        # Handle \& in pages etc
        for f_var in ["volume", "number", "pages", "doi", "url", "isbn", "arxiv"]:
            val = locals().get(f_var, "")
            if isinstance(val, str) and "\\" in val:
                locals()[f_var] = clean_bibfield(val)

        # Classification
        entry_for_classify = {
            "_raw": entry["_raw"],
            "entry_type": entry_type,
        }
        domain = classify_domain(entry_for_classify)
        role = classify_role(entry_for_classify, domain)

        # Citation lookup
        citations = citation_index.get(key, [])
        is_orphan = len(citations) == 0
        if is_orphan:
            stats["orphan_entries"] += 1
        else:
            stats["cited_entries"] += 1

        # Build cited_in YAML list
        cited_in_list = []
        for c in citations:
            cited_in_list.append({
                "book": c.get("book", ""),
                "book_title": c.get("book_title", ""),
                "part": c.get("part", ""),
                "chapter_file": c.get("chapter_file", ""),
                "chapter_title": c.get("chapter_title", ""),
                "excerpt": c.get("context", ""),
            })

        # Build body text
        override_entry = overrides.get(key)
        if isinstance(override_entry, dict) and override_entry.get("why_included"):
            body_text = override_entry["why_included"].strip()
            has_override = True
            stats["overrides_applied"] += 1
        else:
            has_override = False
            if is_orphan:
                body_text = orphan_prose(role, domain, authors, title_plain, year)
            else:
                # Entry is cited but has no override — should be rare given Commit 2
                # wrote overrides for all 210 cited keys. Fallback: minimal grounded
                # template using the first citation.
                first = citations[0]
                author_label = _simple_author_label(raw_authors)
                authors_poss = _possessive(author_label)
                title_md = f"*{title_plain.rstrip('.')}*"
                year_clause = f" ({year})" if year else ""
                where = f"Book {first.get('book', '')} ({first.get('part', '')}, {first.get('chapter_title', '')})"
                body_text = (
                    f"{authors_poss} {title_md}{year_clause} is cited in {where} "
                    f"within the program's reference corpus."
                )

        # Build formatted citation (two variants)
        citation_mathml, citation_plain = build_formatted_citation(
            authors=authors,
            year=year,
            title_md=title_mathml if title_mathml else title_plain,
            title_plain=title_plain,
            journal=journal,
            publisher=publisher,
            volume=volume,
            number=number,
            pages=pages,
        )

        type_display = TYPE_DISPLAY.get(entry_type, entry_type.title())
        role_display = ROLE_DISPLAY.get(role, role.replace("-", " ").title())

        # ── Build markdown ──
        md_lines = [
            "---",
            f"title: {yaml_str(title_mathml if title_mathml else title_plain)}",
            f"title_plain: {yaml_str(title_plain)}",
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
            f"formatted_citation: {yaml_str(citation_mathml)}",
            f"formatted_citation_plain: {yaml_str(citation_plain)}",
            f"is_orphan: {'true' if is_orphan else 'false'}",
            f"has_manual_override: {'true' if has_override else 'false'}",
        ]

        if cited_in_list:
            md_lines.append("cited_in:")
            for c in cited_in_list:
                md_lines.append(f"  - book: {yaml_str(c['book'])}")
                md_lines.append(f"    book_title: {yaml_str(c['book_title'])}")
                md_lines.append(f"    part: {yaml_str(c['part'])}")
                md_lines.append(f"    chapter_file: {yaml_str(c['chapter_file'])}")
                md_lines.append(f"    chapter_title: {yaml_str(c['chapter_title'])}")
                md_lines.append(f"    excerpt: {yaml_str(c['excerpt'])}")
        else:
            md_lines.append("cited_in: []")

        md_lines.extend([
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
            f"    cited_in_books: {'true' if cited_in_list else 'false'}",
            '    updated: "April 2026"',
            "---",
            "",
            body_text,
            "",
        ])

        out_path = out_collection / f"{slug}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))

        stats["total"] += 1

        # Compute cited_books: sorted, comma-joined list of unique book
        # Roman numerals that cite this entry. Used by the bibliography browse
        # surface for per-book filtering. Empty string for orphans.
        cited_books_list = sorted(set(
            c["book"] for c in cited_in_list if c.get("book")
        ))
        cited_books_str = ",".join(cited_books_list)

        # ── Index data (uses title_plain for JSON safety) ──
        index_entry = {
            "key": key,
            "slug": slug,
            "title": title_mathml or title_plain,  # MathML OK — Jekyll Liquid doesn't escape
            "title_plain": title_plain,
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
            "is_orphan": is_orphan,
            "cited_in_count": len(cited_in_list),
            "cited_books": cited_books_str,
        }
        index_data.append(index_entry)
        groups[domain].append(index_entry)

    # Sort index by year desc, then author asc
    index_data.sort(
        key=lambda e: (
            -int(e["year"]) if e["year"].isdigit() else 0,
            e["authors"],
        )
    )

    # Sort groups
    domain_order = [d for d, _ in DOMAIN_RULES]
    groups_output = []
    for domain in domain_order:
        items = groups.get(domain, [])
        items.sort(
            key=lambda e: (
                -int(e["year"]) if e["year"].isdigit() else 0,
                e["authors"],
            )
        )
        groups_output.append({
            "domain": domain,
            "slug": slugify(domain),
            "count": len(items),
            "entries": items,
        })

    # Write data files (only on real build, not dry-run)
    if not dry_run:
        with open(OUT_DATA / "index.json", "w", encoding="utf-8") as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
        with open(OUT_DATA / "groups.json", "w", encoding="utf-8") as f:
            json.dump(groups_output, f, indent=2, ensure_ascii=False)
        if BIB_SOURCE.exists():
            shutil.copy2(BIB_SOURCE, OUT_ASSET / "references.bib")

    # Print summary
    print(f"\n{'='*60}")
    print(f"Bibliography build summary")
    print(f"{'='*60}")
    print(f"  Output directory: {out_collection}")
    print(f"  Total items:      {stats['total']:>6}")
    print(f"  Cited entries:    {stats['cited_entries']:>6}")
    print(f"  Orphan entries:   {stats['orphan_entries']:>6}")
    print(f"  Override applied: {stats['overrides_applied']:>6}")
    print(f"  MathML in title:  {stats['mathml_titles']:>6}")
    print(f"\nPer-domain:")
    for g in groups_output:
        print(f"  {g['domain']:<30} {g['count']:>4}")

    return stats


# ─── Main ─────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(description="Build bibliography collection")
    parser.add_argument(
        "--out-dir",
        default=str(OUT_COLLECTION_DEFAULT),
        help="Output directory for bibliography items (default: _bibliography/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write items to out-dir but don't update _data/bibliography/*.json",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)

    print(f"Parsing {BIB_SOURCE}")
    entries = parse_bib(BIB_SOURCE)
    print(f"Found {len(entries)} entries")

    generate_all(entries, out_dir, dry_run=args.dry_run)

    if args.dry_run:
        print("\n[DRY RUN] No changes written to _data/bibliography/")
    else:
        print("\nDone!")


if __name__ == "__main__":
    main()
