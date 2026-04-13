#!/usr/bin/env python3
"""
build_publications_depth.py — Generate publication depth pages from outline JSONs.

Reads 7 book outline JSONs and generates:
  - _data/publications/parts.json
  - _data/publications/chapters.json
  - Enriched book pages (publications/books/book-{i}.md)
  - Part pages (publications/books/book-{i}/part-{nn}-{slug}/index.md)
  - Chapter pages (publications/books/book-{i}/part-{nn}-{slug}/chapter-{nn}-{slug}/index.md)

Usage:
  python3 scripts/build_publications_depth.py
"""

import json
import os
import re
import sys
import textwrap
from typing import Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTLINE_DIR = os.path.join(
    os.path.expanduser("~"),
    "Books/PantaRhei-2ndEd/dnb/20260404-1325/outline",
)

ROMAN_TO_INT = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
    "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19,
    "XX": 20, "XXI": 21, "XXII": 22,
}

BOOK_SLUGS = {
    "I": "book-i", "II": "book-ii", "III": "book-iii", "IV": "book-iv",
    "V": "book-v", "VI": "book-vi", "VII": "book-vii",
}

BOOK_LAYERS = {
    "I": ("E₀", "Mathematics"),
    "II": ("E₀", "Mathematics"),
    "III": ("E₀", "Mathematics (Hinge)"),
    "IV": ("E₁", "Physics (Microcosm)"),
    "V": ("E₁", "Physics (Macrocosm)"),
    "VI": ("E₂", "Life"),
    "VII": ("E₃", "Metaphysics"),
}

# Page counts from CLAUDE.md (final 2026-03-18)
BOOK_PAGES = {
    "I": 483, "II": 504, "III": 437, "IV": 479, "V": 542, "VI": 440, "VII": 546,
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Create a URL-safe slug from text."""
    text = clean_title(text)
    text = text.lower()
    # Transliterate common Greek/math chars before stripping
    replacements = {
        "τ": "tau", "π": "pi", "ρ": "rho", "α": "alpha", "γ": "gamma",
        "η": "eta", "ω": "omega", "σ": "sigma", "δ": "delta", "ε": "epsilon",
        "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu", "ν": "nu",
        "φ": "phi", "χ": "chi", "ψ": "psi", "ζ": "zeta", "θ": "theta",
    }
    for greek, latin in replacements.items():
        text = text.replace(greek, latin)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    # Truncate very long slugs
    if len(text) > 60:
        text = text[:60].rsplit("-", 1)[0]
    return text


LATEX_TO_UNICODE = {
    "\\tau": "τ", "\\pi": "π", "\\rho": "ρ", "\\alpha": "α", "\\gamma": "γ",
    "\\eta": "η", "\\omega": "ω", "\\sigma": "σ", "\\delta": "δ",
    "\\epsilon": "ε", "\\varepsilon": "ε", "\\iota": "ι", "\\kappa": "κ",
    "\\lambda": "λ", "\\mu": "μ", "\\nu": "ν", "\\phi": "φ", "\\varphi": "φ",
    "\\chi": "χ", "\\psi": "ψ", "\\zeta": "ζ", "\\theta": "θ",
    "\\ell": "ℓ", "\\infty": "∞", "\\mathbb{N}": "ℕ", "\\mathbb{Z}": "ℤ",
    "\\mathbb{R}": "ℝ", "\\mathbb{C}": "ℂ", "\\mathbb{Q}": "ℚ",
    "\\aleph": "ℵ", "\\times": "×", "\\otimes": "⊗", "\\oplus": "⊕",
    "\\cong": "≅", "\\simeq": "≃", "\\approx": "≈", "\\leq": "≤", "\\geq": "≥",
    "\\neq": "≠", "\\subset": "⊂", "\\supset": "⊃", "\\in": "∈",
    "\\to": "→", "\\rightarrow": "→", "\\leftarrow": "←",
    "\\Rightarrow": "⇒", "\\Leftarrow": "⇐",
    "\\emph": "", "\\textsc": "", "\\textbf": "", "\\textit": "",
    "\\mathrm": "", "\\mathcal": "", "\\mathfrak": "",
}

SUBSCRIPT_MAP = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUPERSCRIPT_MAP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def clean_title(text: str) -> str:
    """Strip LaTeX artifacts from titles, converting to Unicode."""
    # \texorpdfstring{latex}{plain} → use plain text
    text = re.sub(r"\\texorpdfstring\{[^}]*\}\{([^}]*)\}", r"\1", text)
    # Replace known LaTeX commands with Unicode (longest first)
    for latex, uni in sorted(LATEX_TO_UNICODE.items(), key=lambda x: -len(x[0])):
        text = text.replace(latex, uni)
    # Handle subscripts: _{...} or _x
    def sub_repl(m):
        content = m.group(1) if m.group(1) else m.group(2)
        return content.translate(SUBSCRIPT_MAP)
    text = re.sub(r"_\{([^}]*)\}|_([0-9a-z])", sub_repl, text)
    # Handle superscripts: ^{...} or ^x
    def sup_repl(m):
        content = m.group(1) if m.group(1) else m.group(2)
        return content.translate(SUPERSCRIPT_MAP)
    text = re.sub(r"\^\{([^}]*)\}|\^([0-9])", sup_repl, text)
    # Remove remaining backslash commands with braces
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    # Remove remaining bare backslash commands
    text = re.sub(r"\\[a-zA-Z]+", "", text)
    # LaTeX dashes
    text = text.replace("---", "—").replace("--", "–")
    # Strip dollar signs (keep content between them)
    text = text.replace("$", "")
    # Clean leftover braces
    text = text.replace("{", "").replace("}", "")
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def part_number_int(part_num_str: str) -> int:
    """Convert part number string to integer. Prologue/Epilogue → 0/99."""
    upper = part_num_str.strip().upper()
    if "PROLOGUE" in upper:
        return 0
    if "EPILOGUE" in upper:
        return 99
    if upper in ROMAN_TO_INT:
        return ROMAN_TO_INT[upper]
    # Try plain integer
    try:
        return int(part_num_str)
    except ValueError:
        return 0


def part_display_name(part_num_str: str) -> str:
    """Human-readable part display name."""
    upper = part_num_str.strip()
    if upper.upper() in ("PROLOGUE",):
        return "Prologue"
    if upper.upper() in ("EPILOGUE",):
        return "Epilogue"
    return f"Part {upper}"


def truncate_abstract(text: str, length: int = 160) -> str:
    """Truncate to given length at word boundary."""
    if not text:
        return ""
    flat = text.replace("\n", " ").strip()
    flat = re.sub(r"\s+", " ", flat)
    if len(flat) <= length:
        return flat
    return flat[:length].rsplit(" ", 1)[0] + "…"


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def write_file(path: str, content: str):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def yaml_str(s: str) -> str:
    """Safely quote a YAML string value."""
    if not s:
        return '""'
    # Quote if contains special chars
    if any(c in s for c in ":{}[]&*?|>!%@`,#'\"\\") or s.startswith("-") or s.startswith(" "):
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return f'"{s}"'


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def generate_book_page(book: dict, parts_data: list, book_slug: str) -> str:
    """Generate enriched book page Markdown."""
    roman = book["book"]
    title = clean_title(book["title"])
    subtitle = clean_title(book.get("subtitle", ""))
    layer_code, layer_name = BOOK_LAYERS[roman]
    page_count = BOOK_PAGES.get(roman, 0)
    part_count = len(parts_data)
    chapter_count = sum(p["chapter_count"] for p in parts_data)

    # Build part TOC
    part_toc_lines = []
    for p in parts_data:
        part_toc_lines.append(
            f'- **[{p["display_name"]}: {p["title"]}]({p["url"]})** '
            f'— {p["chapter_count"]} chapter{"s" if p["chapter_count"] != 1 else ""}'
        )

    part_toc = "\n".join(part_toc_lines)

    # Abstract
    abstract = ""
    if book["parts"] and book["parts"][0].get("abstract_markdown"):
        # Use prologue abstract as book abstract if available
        first = book["parts"][0]
        if first["number"].strip().upper() == "PROLOGUE":
            abstract = first["abstract_markdown"].strip()

    abstract_section = ""
    if abstract:
        abstract_section = f"\n\n## About This Volume\n\n{abstract}"

    return textwrap.dedent(f"""\
---
layout: publication-book
title: "Book {roman}: {title}"
permalink: /publications/books/{book_slug}/
lane: publications
publication_type: book
book_id: "{roman}"
book_slug: "{book_slug}"
subtitle: {yaml_str(subtitle)}
part_count: {part_count}
chapter_count: {chapter_count}
page_count: {page_count}
summary_short: {yaml_str(subtitle)}
summary_cards:
- title: Subtitle
  body: {yaml_str(subtitle)}
- title: Structure
  body: "{part_count} parts, {chapter_count} chapters, {page_count} pages"
- title: Layer
  body: "{layer_code} {layer_name}"
linked_guided_tour: "/publications/guided-tours/"
linked_verify_page: "/verify/"
linked_dashboard: "/registry/dashboards/{book_slug}/"
right_rail:
  related:
  - title: Framework Overview
    url: /framework/about/
  - title: Registry
    url: /registry/books/{book_slug}/
  - title: Guided Tours
    url: /publications/guided-tours/
  artifacts:
  - title: Registry Dashboard
    url: /registry/dashboards/{book_slug}/
  - title: TauLib (frozen)
    url: https://github.com/Panta-Rhei-Framework/formalization
    external: true
  meta:
    type: Canonical Book
    layer: "{layer_code} {layer_name}"
    status: Published
    updated: April 2026
---

## {subtitle}

Book {roman} is part of the **{layer_name}** layer ({layer_code}) of the Panta Rhei framework.

**{part_count} parts** · **{chapter_count} chapters** · **{page_count} pages**
{abstract_section}

## Parts

{part_toc}

## Canonical Artifacts

- **Registry**: [{chapter_count} chapters mapped to registry objects](/registry/books/{book_slug}/)
- **Dashboard**: [Formalization status and dependency graph](/registry/dashboards/{book_slug}/)
- **Formalization**: [TauLib Book{roman}](https://github.com/Panta-Rhei-Framework/formalization) — Lean 4 verification

## Available Formats

- Hardcover (7×10)
- Paperback (6×9)
- Kindle (print replica)

Available on Amazon KDP.
""")


def generate_part_page(part_info: dict, chapters: list, book: dict) -> str:
    """Generate part page Markdown."""
    roman = book["book"]
    book_slug = BOOK_SLUGS[roman]
    book_title = clean_title(book["title"])
    layer_code, layer_name = BOOK_LAYERS[roman]

    # Build chapter TOC
    ch_toc_lines = []
    for ch in chapters:
        ch_toc_lines.append(
            f'- **[Chapter {ch["chapter_number"]}: {ch["title"]}]({ch["url"]})**'
        )
    ch_toc = "\n".join(ch_toc_lines)

    # Abstract
    abstract = (part_info.get("abstract_markdown") or "").strip()
    abstract_section = ""
    if abstract:
        abstract_section = f"\n\n{abstract}"

    return textwrap.dedent(f"""\
---
layout: publication-part
title: "{part_info["display_name"]}: {part_info["title"]}"
permalink: {part_info["url"]}
lane: publications
publication_type: part
book_id: "{roman}"
book_slug: "{book_slug}"
part_number: {part_info["part_number"]}
part_display: {yaml_str(part_info["display_name"])}
part_slug: "{part_info["slug"]}"
chapter_count: {part_info["chapter_count"]}
summary_short: {yaml_str(part_info["summary_short"])}
canonical_book_url: "/publications/books/{book_slug}/"
canonical_book_title: "Book {roman}: {book_title}"
right_rail:
  related:
  - title: "Book {roman}: {book_title}"
    url: /publications/books/{book_slug}/
  - title: Guided Tours
    url: /publications/guided-tours/
  - title: Registry
    url: /registry/books/{book_slug}/
  meta:
    type: Part
    book: "Book {roman}"
    layer: "{layer_code} {layer_name}"
    chapters: "{part_info["chapter_count"]}"
    updated: April 2026
---
{abstract_section}

## Chapters

{ch_toc}
""")


def generate_chapter_page(ch_info: dict, part_info: dict, book: dict,
                          prev_ch: Optional[dict], next_ch: Optional[dict]) -> str:
    """Generate chapter page Markdown."""
    roman = book["book"]
    book_slug = BOOK_SLUGS[roman]
    book_title = clean_title(book["title"])
    layer_code, layer_name = BOOK_LAYERS[roman]

    abstract = (ch_info.get("abstract_markdown") or "").strip()
    abstract_section = ""
    if abstract:
        abstract_section = f"\n\n{abstract}"

    # Prev/next frontmatter
    nav_lines = ""
    if prev_ch:
        nav_lines += f'prev_chapter_url: "{prev_ch["url"]}"\n'
        nav_lines += f'prev_chapter_title: "Chapter {prev_ch["chapter_number"]}: {prev_ch["title"]}"\n'
    if next_ch:
        nav_lines += f'next_chapter_url: "{next_ch["url"]}"\n'
        nav_lines += f'next_chapter_title: "Chapter {next_ch["chapter_number"]}: {next_ch["title"]}"\n'

    page_line = ""
    if ch_info.get("page_in_book"):
        page_line = f'page_in_book: {ch_info["page_in_book"]}\n'

    return textwrap.dedent(f"""\
---
layout: publication-chapter
title: "Chapter {ch_info["chapter_number"]}: {ch_info["title"]}"
permalink: {ch_info["url"]}
lane: publications
publication_type: chapter
book_id: "{roman}"
book_slug: "{book_slug}"
part_number: {part_info["part_number"]}
part_slug: "{part_info["slug"]}"
chapter_number: {ch_info["chapter_number"]}
chapter_slug: "{ch_info["slug"]}"
{page_line}{nav_lines}summary_short: {yaml_str(ch_info["summary_short"])}
canonical_book_url: "/publications/books/{book_slug}/"
canonical_book_title: "Book {roman}: {book_title}"
canonical_part_url: "{part_info["url"]}"
canonical_part_title: "{part_info["display_name"]}: {part_info["title"]}"
right_rail:
  related:
  - title: "Book {roman}: {book_title}"
    url: /publications/books/{book_slug}/
  - title: "{part_info["display_name"]}: {part_info["title"]}"
    url: {part_info["url"]}
  - title: Registry
    url: /registry/books/{book_slug}/
  meta:
    type: Chapter
    book: "Book {roman}"
    part: {yaml_str(part_info["display_name"])}
    layer: "{layer_code} {layer_name}"
    updated: April 2026
---
{abstract_section}
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not os.path.isdir(OUTLINE_DIR):
        print(f"ERROR: Outline directory not found: {OUTLINE_DIR}", file=sys.stderr)
        sys.exit(1)

    all_parts_data = []
    all_chapters_data = []
    total_part_pages = 0
    total_chapter_pages = 0

    for book_num in range(1, 8):
        outline_path = os.path.join(OUTLINE_DIR, f"book{book_num}-outline.json")
        if not os.path.isfile(outline_path):
            print(f"WARNING: Missing {outline_path}", file=sys.stderr)
            continue

        with open(outline_path, encoding="utf-8") as f:
            book = json.load(f)

        roman = book["book"]
        book_slug = BOOK_SLUGS[roman]
        print(f"\n{'='*60}")
        print(f"Book {roman}: {clean_title(book['title'])}")
        print(f"{'='*60}")

        # Process parts
        book_parts = []
        book_chapters = []  # flat list of all chapters in this book

        for part_raw in book["parts"]:
            pnum = part_number_int(part_raw["number"])
            display = part_display_name(part_raw["number"])
            title = clean_title(part_raw["title"])

            # Strip "Prologue --- " / "Epilogue --- " prefix from title
            title = re.sub(r"^(Prologue|Epilogue)\s*[—–-]+\s*", "", title).strip()
            if not title:
                title = display

            title_slug = slugify(title)
            if not title_slug:
                title_slug = slugify(display)
            slug = f"part-{pnum:02d}-{title_slug}"
            url = f"/publications/books/{book_slug}/{slug}/"

            abstract_md = part_raw.get("abstract_markdown") or ""

            part_info = {
                "id": f"{book_slug}-{slug}",
                "book_id": roman,
                "book_slug": book_slug,
                "part_number": pnum,
                "display_name": display,
                "title": title,
                "slug": slug,
                "url": url,
                "chapter_count": len(part_raw["chapters"]),
                "summary_short": truncate_abstract(abstract_md),
                "abstract_markdown": abstract_md,
            }
            book_parts.append(part_info)

            # Process chapters within this part
            part_chapters = []
            for ch_raw in part_raw["chapters"]:
                ch_num = ch_raw["number"]
                ch_title = clean_title(ch_raw["title"])
                ch_slug = f"chapter-{ch_num:02d}-{slugify(ch_title)}"
                ch_url = f"{url}{ch_slug}/"
                ch_abstract_md = ch_raw.get("abstract_markdown") or ""

                ch_info = {
                    "id": f"{book_slug}-ch-{ch_num:02d}",
                    "book_id": roman,
                    "book_slug": book_slug,
                    "part_number": pnum,
                    "part_slug": slug,
                    "chapter_number": ch_num,
                    "title": ch_title,
                    "slug": ch_slug,
                    "url": ch_url,
                    "page_in_book": ch_raw.get("page"),
                    "summary_short": truncate_abstract(ch_abstract_md),
                    "abstract_markdown": ch_abstract_md,
                }
                part_chapters.append(ch_info)
                book_chapters.append(ch_info)

            # Generate part page
            part_page_content = generate_part_page(part_info, part_chapters, book)
            part_page_path = os.path.join(
                SITE_DIR, "publications", "books", book_slug, slug, "index.md"
            )
            write_file(part_page_path, part_page_content)
            total_part_pages += 1

            # Generate chapter pages
            for i, ch in enumerate(part_chapters):
                prev_ch = part_chapters[i - 1] if i > 0 else None
                next_ch = part_chapters[i + 1] if i < len(part_chapters) - 1 else None

                # Cross-part prev/next: link to last chapter of previous part / first of next
                if prev_ch is None and book_chapters:
                    # Find previous chapter in book-level list
                    idx_in_book = next(
                        (j for j, c in enumerate(book_chapters) if c["id"] == ch["id"]),
                        -1,
                    )
                    if idx_in_book > 0:
                        prev_ch = book_chapters[idx_in_book - 1]

                ch_page_content = generate_chapter_page(ch, part_info, book, prev_ch, next_ch)
                ch_page_path = os.path.join(
                    SITE_DIR, "publications", "books", book_slug, slug, ch["slug"], "index.md"
                )
                write_file(ch_page_path, ch_page_content)
                total_chapter_pages += 1

        # Now handle cross-part next_chapter for the last chapter of each part
        # (already handled in the flat book_chapters list for prev, but next needs
        #  a second pass for the last chapter of each part)
        # We'll regenerate pages that need cross-part next links
        flat_idx = 0
        for part_info_local in book_parts:
            matching = [c for c in book_chapters if c["part_slug"] == part_info_local["slug"]]
            for i, ch in enumerate(matching):
                prev_ch = matching[i - 1] if i > 0 else None
                next_ch = matching[i + 1] if i < len(matching) - 1 else None

                # Cross-part prev
                if prev_ch is None and flat_idx > 0:
                    prev_ch = book_chapters[flat_idx - 1]
                # Cross-part next
                if next_ch is None and flat_idx < len(book_chapters) - 1:
                    next_ch = book_chapters[flat_idx + 1]

                # Only rewrite if we added a cross-part next link
                if i == len(matching) - 1 and next_ch is not None:
                    ch_page_content = generate_chapter_page(ch, part_info_local, book, prev_ch, next_ch)
                    ch_page_path = os.path.join(
                        SITE_DIR, "publications", "books", ch["book_slug"],
                        ch["part_slug"], ch["slug"], "index.md"
                    )
                    write_file(ch_page_path, ch_page_content)

                flat_idx += 1

        # Generate enriched book page
        book_page_content = generate_book_page(book, book_parts, book_slug)
        book_page_path = os.path.join(
            SITE_DIR, "publications", "books", f"{book_slug}.md"
        )
        write_file(book_page_path, book_page_content)

        print(f"  {len(book_parts)} parts, {len(book_chapters)} chapters")

        # Collect for data files (strip abstract_markdown — too large for JSON data)
        for p in book_parts:
            all_parts_data.append({k: v for k, v in p.items() if k != "abstract_markdown"})
        for c in book_chapters:
            all_chapters_data.append({k: v for k, v in c.items() if k != "abstract_markdown"})

    # Write data files
    data_dir = os.path.join(SITE_DIR, "_data", "publications")
    ensure_dir(data_dir)

    parts_json_path = os.path.join(data_dir, "parts.json")
    with open(parts_json_path, "w", encoding="utf-8") as f:
        json.dump(all_parts_data, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {len(all_parts_data)} parts to {parts_json_path}")

    chapters_json_path = os.path.join(data_dir, "chapters.json")
    with open(chapters_json_path, "w", encoding="utf-8") as f:
        json.dump(all_chapters_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(all_chapters_data)} chapters to {chapters_json_path}")

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  Book pages enriched:  7")
    print(f"  Part pages generated: {total_part_pages}")
    print(f"  Chapter pages generated: {total_chapter_pages}")
    print(f"  Data files: parts.json ({len(all_parts_data)} entries), chapters.json ({len(all_chapters_data)} entries)")
    print(f"  Total new pages: {total_part_pages + total_chapter_pages}")


if __name__ == "__main__":
    main()
