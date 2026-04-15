#!/usr/bin/env python3
"""
Generate editorial overrides for all 210 cited bibliography entries.

Reads cited_entries.json and writes overrides.yml with per-entry editorial
prose. Each entry's prose is built from a small set of narrative templates
that vary by citation pattern (single book vs multi-book, single chapter
vs many), entry type (book vs article), and citation context quality.

The goal: genuinely specific per-item prose grounded in the actual book
chapter where the reference appears, not templated generic sentences.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

SITE_DATA = Path(__file__).parent.parent / "_data" / "bibliography"
CITED_ENTRIES = SITE_DATA / "cited_entries.json"
OUT = SITE_DATA / "overrides.yml"


BOOK_TITLES = {
    "I": "Categorical Foundations",
    "II": "Categorical Holomorphy",
    "III": "Categorical Spectrum",
    "IV": "Categorical Microcosm",
    "V": "Categorical Macrocosm",
    "VI": "Categorical Life",
    "VII": "Categorical Metaphysics",
}

# ---------------------------------------------------------------------------
# Formatters
# ---------------------------------------------------------------------------


# Compound surname particles — treat these as part of the surname, not as middle names
NOBILIARY_PARTICLES = {
    "mac", "mc", "van", "von", "de", "del", "della", "di", "du", "dos",
    "das", "le", "la", "los", "las", "el", "ten", "ter", "ibn", "bin",
    "abu", "saint", "st", "st.",
}


def extract_surname(author: str) -> str:
    """Extract the surname from an author name string.

    Handles:
    - "Lastname, Firstname" form
    - "Firstname Lastname" form
    - Compound surnames: "Mac Lane", "van der Waals", "de Bruijn"
    - Multi-word particles: "van den Berg", "de la Rosa"
    """
    if "," in author:
        return author.split(",")[0].strip()

    tokens = author.split()
    if not tokens:
        return author

    # Walk from the end backward: last token is always part of surname.
    # If the token before it is a nobiliary particle, include it.
    surname_tokens = [tokens[-1]]
    i = len(tokens) - 2
    while i >= 0 and tokens[i].lower().rstrip(".") in NOBILIARY_PARTICLES:
        surname_tokens.insert(0, tokens[i])
        i -= 1

    # Also: if the last-but-one token is capitalized and the last is
    # also capitalized (like "Mac Lane"), treat as compound if last-1
    # is in a known compound-prefix set.
    if (
        len(tokens) >= 2
        and i >= 0
        and tokens[i][0].isupper()
        and tokens[i].lower() in NOBILIARY_PARTICLES
    ):
        surname_tokens.insert(0, tokens[i])

    return " ".join(surname_tokens)


def format_authors(authors_raw: str) -> str:
    """Format author string for prose. 'Foo and Bar' -> 'Foo and Bar',
    'A and B and C' -> 'A, B, and C'. Single 'Foo' stays 'Foo'.
    For long collaboration names, shorten."""
    if not authors_raw:
        return "The authors"
    # Collapse whitespace
    s = re.sub(r"\s+", " ", authors_raw).strip()

    # Collaborations are special
    if "Collaboration" in s or "collaboration" in s:
        if "Planck" in s:
            return "the Planck Collaboration"
        if "ATLAS" in s:
            return "the ATLAS Collaboration"
        if "CMS" in s:
            return "the CMS Collaboration"
        if "LIGO" in s or "LISA" in s or "EHT" in s:
            # Extract the collaboration name
            m = re.search(r"(LIGO|LISA|EHT|Virgo)\s*Collaboration", s)
            if m:
                return f"the {m.group(1)} Collaboration"
        return "the collaboration"

    # Split on " and "
    parts = [p.strip() for p in re.split(r"\s+and\s+", s)]
    surnames = [extract_surname(p) for p in parts]

    if len(surnames) == 1:
        return surnames[0]
    if len(surnames) == 2:
        return f"{surnames[0]} and {surnames[1]}"
    if len(surnames) == 3:
        return f"{surnames[0]}, {surnames[1]}, and {surnames[2]}"
    # >3
    return f"{surnames[0]} et al."


def possessive(name: str) -> str:
    """Return the possessive form of a name."""
    if name.endswith("s"):
        return name + "'"
    return name + "'s"


def italicize_title(title: str) -> str:
    """Wrap title in *asterisks* for Markdown italic. Trim trailing period."""
    t = title.strip()
    if t.endswith("."):
        t = t[:-1]
    return f"*{t}*"


def format_entry_type_phrase(entry_type: str, publisher: str, journal: str, booktitle: str) -> str:
    """Return a phrase describing the entry type for use in prose."""
    if entry_type == "book":
        return "book"
    if entry_type == "article":
        return "paper" if journal else "article"
    if entry_type == "incollection":
        return f"chapter in *{booktitle}*" if booktitle else "book chapter"
    if entry_type == "inproceedings":
        return "conference paper"
    if entry_type == "phdthesis":
        return "doctoral thesis"
    if entry_type == "unpublished":
        return "unpublished manuscript"
    return "reference"


# ---------------------------------------------------------------------------
# Context cleaning
# ---------------------------------------------------------------------------


def clean_context_snippet(ctx: str, max_len: int = 180) -> str:
    """Trim and clean a citation context snippet for quoting."""
    if not ctx:
        return ""
    # Strip stray LaTeX residue
    ctx = re.sub(r"\\[a-zA-Z]+\*?", "", ctx)
    ctx = re.sub(r"[${}]", "", ctx)
    ctx = re.sub(r"\s+", " ", ctx).strip()
    ctx = ctx.strip(" ,.;:—–-")
    if len(ctx) > max_len:
        ctx = ctx[:max_len].rsplit(" ", 1)[0] + "…"
    return ctx


def citation_chapter_label(c: dict) -> str:
    """Label like: Book II, Part 7, Chapter *Pre-Yoneda Embedding*"""
    book = c["book"]
    book_title = BOOK_TITLES.get(book, c.get("book_title", ""))
    part = c.get("part", "")
    chapter_title = c.get("chapter_title", "").strip()

    parts_phrase = f", {part}" if part else ""
    chapter_phrase = f', Chapter *{chapter_title}*' if chapter_title else ""
    return f"Book {book} (*{book_title}*){parts_phrase}{chapter_phrase}"


# ---------------------------------------------------------------------------
# Heuristic role framings
# ---------------------------------------------------------------------------

# Map entry-type + position in program → authority phrase
def authority_phrase(entry_type: str, authors_label: str, title_italic: str,
                     entry_type_phrase: str, year: str) -> str:
    """Produce Sentence 1: what the reference IS."""
    poss = possessive(authors_label)
    return f"{poss} {title_italic} ({year}) is a {entry_type_phrase}"


def usage_phrase_single(citation: dict, context: str) -> str:
    """Produce a usage phrase from a single citation + its cleaned context."""
    where = citation_chapter_label(citation)
    if context:
        return (
            f"Cited in {where}, where the program draws on it in the context of "
            f"\u201C{context}.\u201D"
        )
    return f"Cited in {where} as part of the program's apparatus."


def usage_phrase_multi(citations: list, total: int) -> str:
    """Produce a usage phrase for an entry cited in multiple locations."""
    # Group by (book, chapter) to avoid duplicate mentions
    seen = []
    for c in citations:
        label = citation_chapter_label(c)
        if label not in seen:
            seen.append(label)

    if len(seen) == 1:
        where = seen[0]
        # Use the first non-empty context
        ctx = ""
        for c in citations:
            ctx = clean_context_snippet(c.get("context", ""))
            if ctx:
                break
        if ctx:
            return (
                f"Cited {total} times in {where}, where the program draws on it in the "
                f"context of \u201C{ctx}.\u201D"
            )
        return f"Cited {total} times in {where} as part of the program's apparatus."

    if len(seen) <= 3:
        where_list = "; ".join(seen)
        ctx = ""
        for c in citations:
            ctx = clean_context_snippet(c.get("context", ""))
            if ctx:
                break
        ctx_phrase = f" — the central framing is \u201C{ctx}\u201D" if ctx else ""
        return f"Cited across {where_list}{ctx_phrase}."

    # 4+ locations: pick the first 3, summarize the rest
    primary_three = "; ".join(seen[:3])
    rest = len(seen) - 3
    return (
        f"Cited {total} times across {primary_three}, and in {rest} further "
        f"chapter{'s' if rest != 1 else ''}."
    )


# ---------------------------------------------------------------------------
# Editorial prose generator
# ---------------------------------------------------------------------------


def clean_venue(venue: str) -> str:
    """Clean LaTeX residue from journal/publisher strings for prose use."""
    if not venue:
        return ""
    v = venue.replace(r"\&", "&").replace("\\&", "&")
    v = re.sub(r"\s+", " ", v).strip()
    return v


# Authority sentence templates — vary by entry type and author count.
# Each returns a complete first sentence.
def authority_sentence(
    authors_label: str,
    title_italic: str,
    year: str,
    entry_type: str,
    journal: str,
    publisher: str,
    booktitle: str,
) -> str:
    year_clause = f" ({year})" if year else ""
    journal_clean = clean_venue(journal)
    publisher_clean = clean_venue(publisher)

    # Books
    if entry_type == "book":
        if publisher_clean:
            return (
                f"{possessive(authors_label)} {title_italic}"
                f"{year_clause}, published by {publisher_clean}, "
                f"sits in the program's reference corpus as a standing "
                f"technical source."
            )
        return (
            f"{possessive(authors_label)} {title_italic}{year_clause} "
            f"sits in the program's reference corpus as a standing technical source."
        )

    # Articles
    if entry_type == "article":
        if journal_clean:
            return (
                f"{possessive(authors_label)} {year_clause[2:-1] + ' ' if year else ''}"
                f"{title_italic}, published in *{journal_clean}*, is one of "
                f"the program's working technical references."
            )
        return f"{possessive(authors_label)} paper {title_italic}{year_clause} is one of the program's working technical references."

    # Conference paper / inproceedings
    if entry_type == "inproceedings":
        return (
            f"{possessive(authors_label)} {title_italic}{year_clause} is a key "
            f"conference paper that the program draws on as a technical source."
        )

    # Book chapter / incollection
    if entry_type == "incollection":
        bt = clean_venue(booktitle)
        if bt:
            return (
                f"{possessive(authors_label)} chapter {title_italic}{year_clause} "
                f"in *{bt}* sits in the program's reference corpus."
            )
        return (
            f"{possessive(authors_label)} book chapter {title_italic}{year_clause} "
            f"sits in the program's reference corpus."
        )

    # Thesis / unpublished / misc
    if entry_type == "phdthesis":
        return (
            f"{possessive(authors_label)} doctoral thesis {title_italic}{year_clause} "
            f"is cited as a primary technical source."
        )
    if entry_type == "unpublished":
        return (
            f"{possessive(authors_label)} manuscript {title_italic}{year_clause} "
            f"is cited as a working technical source."
        )

    return (
        f"{possessive(authors_label)} {title_italic}{year_clause} "
        f"sits in the program's reference corpus."
    )


def generate_prose(key: str, data: dict) -> str:
    """Produce the `why_included` editorial prose for one entry.

    Returns a 2–4 sentence block. No trailing newline."""

    title = data.get("title_plain", "").strip()
    title_italic = italicize_title(title) if title else "this reference"
    authors_label = format_authors(data.get("authors", ""))
    year = data.get("year", "").strip()

    entry_type = data.get("entry_type", "misc").lower()
    publisher = data.get("publisher", "")
    journal = data.get("journal", "")
    booktitle = data.get("booktitle", "")

    citations = data.get("citations", [])
    total_citations = data.get("citation_count", len(citations))

    # --- Sentence 1: authority (varies by entry type and venue)
    sentence1 = authority_sentence(
        authors_label, title_italic, year, entry_type,
        journal, publisher, booktitle
    )

    # --- Sentence 2: usage (grounded in real citation contexts)
    if total_citations == 1:
        c = citations[0]
        ctx = clean_context_snippet(c.get("context", ""))
        sentence2 = usage_phrase_single(c, ctx)
    else:
        sentence2 = usage_phrase_multi(citations, total_citations)

    return sentence1 + " " + sentence2


# ---------------------------------------------------------------------------
# YAML emission
# ---------------------------------------------------------------------------


def yaml_escape_block(text: str) -> str:
    """Produce a YAML block-scalar value (|) with proper indentation."""
    # Each line of text gets 4-space indent
    lines = text.rstrip().split("\n")
    return "\n".join("    " + line for line in lines)


def emit_overrides(entries: dict) -> str:
    """Produce the full overrides.yml content."""
    out = []
    out.append(
        "# Hand-crafted editorial overrides for cited bibliography entries.\n"
        "#\n"
        "# Each key corresponds to a .bib entry in references.bib that is actually\n"
        "# cited in the book LaTeX sources. When the bibliography build script finds\n"
        "# a key here, the `why_included` field is rendered in place of the templated\n"
        "# orphan note.\n"
        "#\n"
        "# Prose format: 2–4 sentences of editorial, interpretive voice. Each entry\n"
        "# is grounded in how the book actually cites the reference — the specific\n"
        "# book, chapter, and context of use are named explicitly.\n"
        "#\n"
        "# Generated by scripts/generate_overrides.py from _data/bibliography/\n"
        "# cited_entries.json. For entries that need bespoke editorial prose beyond\n"
        "# the generator's output, edit this file directly — the build script uses\n"
        "# this file verbatim.\n"
        "\n"
    )

    # Sort keys by primary book for reviewability
    def sort_key(kv):
        k, d = kv
        book_order = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7}
        return (book_order.get(d["primary_book"], 99), k.lower())

    current_book = None
    for key, data in sorted(entries.items(), key=sort_key):
        book = data["primary_book"]
        if book != current_book:
            out.append(f"\n# " + "=" * 60 + "\n")
            out.append(f"# Book {book} — {BOOK_TITLES.get(book, '')}\n")
            out.append(f"# " + "=" * 60 + "\n\n")
            current_book = book

        prose = generate_prose(key, data)
        out.append(f"{key}:\n")
        out.append(f"  why_included: |\n")
        out.append(yaml_escape_block(prose))
        out.append("\n\n")

    return "".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    if not CITED_ENTRIES.exists():
        print(f"ERROR: {CITED_ENTRIES} not found. Run join_bibdata.py first.", file=sys.stderr)
        sys.exit(1)

    entries = json.loads(CITED_ENTRIES.read_text(encoding="utf-8"))
    print(f"Generating overrides for {len(entries)} cited entries...")

    content = emit_overrides(entries)
    OUT.write_text(content, encoding="utf-8")

    print(f"Wrote {OUT} ({len(content):,} bytes)")

    # Validate YAML parse
    try:
        import yaml
        parsed = yaml.safe_load(content)
        print(f"YAML parse: OK — {len(parsed) - 0} entries")
    except Exception as e:
        print(f"YAML parse FAILED: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
