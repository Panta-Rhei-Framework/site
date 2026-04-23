#!/usr/bin/env python3
"""
import_taulib_docs.py — Import doc-gen4 output into Jekyll collection.

Reads 454 HTML files from TauLib docbuild, extracts <main> content,
creates Jekyll collection pages with Atlas-compatible frontmatter.
"""

import os
import re
import json
from html.parser import HTMLParser

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC_DIR = os.path.join(
    os.path.expanduser("~"),
    "Books/PantaRhei-2ndEd/lean4/TauLib/docbuild/.lake/build/doc",
)
COLLECTION_DIR = os.path.join(SITE_DIR, "_taulib_docs")
ASSETS_DIR = os.path.join(SITE_DIR, "assets", "taulib")
PINNED_TAULIB_COMMIT = "2261c049119c8dd9a4e891457f196745178c02b3"
LEGACY_SOURCE_PREFIX_RE = re.compile(
    r"https://github\.com/ThorFuchs/PantaRhei-2ndEd/blob/"
    r"[0-9a-f]+/lean4/TauLib/TauLib/"
)

BOOK_LABELS = {
    "BookI": ("I", "Foundations"),
    "BookII": ("II", "Holomorphy"),
    "BookIII": ("III", "Spectrum"),
    "BookIV": ("IV", "Microcosm"),
    "BookV": ("V", "Macrocosm"),
    "BookVI": ("VI", "Life"),
    "BookVII": ("VII", "Metaphysics"),
    "Tour": ("Tour", "Tours"),
}


class MainExtractor(HTMLParser):
    """Extract content inside <main> tags from doc-gen4 HTML."""
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.main_content = []
        self.title = ""
        self.in_title = False
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main = True
            return
        if tag == "title":
            self.in_title = True
        if self.in_main:
            attrs_str = ""
            for k, v in attrs:
                if v is not None:
                    attrs_str += f' {k}="{v}"'
                else:
                    attrs_str += f' {k}'
            self.main_content.append(f"<{tag}{attrs_str}>")

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
            return
        if tag == "title":
            self.in_title = False
        if self.in_main:
            self.main_content.append(f"</{tag}>")

    def handle_data(self, data):
        if self.in_title and not self.title:
            self.title = data.strip()
        if self.in_main:
            self.main_content.append(data)

    def get_content(self):
        return "".join(self.main_content)


def module_to_slug(module_name):
    """Convert TauLib.BookI.Kernel.Signature → book-i-kernel-signature."""
    # Remove TauLib. prefix
    name = module_name.replace("TauLib.", "")
    # Convert CamelCase segments
    parts = name.split(".")
    slug_parts = []
    for part in parts:
        # Insert hyphens before uppercase letters
        slugged = re.sub(r'([a-z])([A-Z])', r'\1-\2', part)
        slugged = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', slugged)
        slug_parts.append(slugged.lower())
    return "-".join(slug_parts)


def get_book_from_path(rel_path):
    """Determine which book a module belongs to from its file path."""
    parts = rel_path.split("/")
    if len(parts) >= 2 and parts[0] == "TauLib":
        book_key = parts[1]
        if book_key in BOOK_LABELS:
            return BOOK_LABELS[book_key]
    return None, None


def process_html_file(filepath, rel_path):
    """Extract content and metadata from a doc-gen4 HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    extractor = MainExtractor()
    extractor.feed(html)

    title = extractor.title or rel_path.replace(".html", "").replace("/", ".")
    content = extractor.get_content()

    # Clean up content: fix relative links to point within the collection
    # Remove doc-gen4 internal links that won't work
    content = re.sub(r'href="(\.\./)*\./style\.css"', '', content)
    content = LEGACY_SOURCE_PREFIX_RE.sub(
        f"https://github.com/Panta-Rhei-Research/taulib/blob/{PINNED_TAULIB_COMMIT}/TauLib/",
        content,
    )

    return title, content


def main():
    os.makedirs(COLLECTION_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)

    # Copy doc-gen4 CSS for code highlighting
    src_css = os.path.join(DOC_DIR, "style.css")
    if os.path.isfile(src_css):
        with open(src_css) as f:
            css = f.read()
        # Extract just the code/declaration styling, not the full shell
        with open(os.path.join(ASSETS_DIR, "docgen.css"), "w") as f:
            f.write(css)
        print("Copied doc-gen4 CSS")

    # Find all HTML files
    all_files = []
    for root, dirs, files in os.walk(DOC_DIR):
        for fname in sorted(files):
            if not fname.endswith(".html"):
                continue
            filepath = os.path.join(root, fname)
            rel = os.path.relpath(filepath, DOC_DIR)
            all_files.append((filepath, rel))

    print(f"Found {len(all_files)} HTML files")

    # Process module pages (under TauLib/)
    module_index = []
    created = 0
    skipped = 0

    for filepath, rel in all_files:
        # Skip top-level non-module pages (we handle those separately)
        if "/" not in rel and rel != "TauLib.html":
            skipped += 1
            continue

        # Skip navbar, search, etc
        basename = os.path.basename(rel)
        if basename in ("navbar.html", "search.html", "404.html", "stats.html",
                        "depgraph.html", "references.html", "index.html"):
            skipped += 1
            continue

        title, content = process_html_file(filepath, rel)
        if not content.strip():
            skipped += 1
            continue

        # Determine module name from title or path
        module_name = title if title.startswith("TauLib.") else "TauLib." + rel.replace("/", ".").replace(".html", "")
        slug = module_to_slug(module_name)

        # Determine book
        book_info = get_book_from_path(rel)
        book_roman = book_info[0] if book_info[0] else ""
        book_label = book_info[1] if book_info[1] else ""

        # Create Jekyll collection page
        permalink = f"/verify/taulib/docs/{slug}/"

        frontmatter = f"""---
layout: taulib-doc
title: "{title}"
permalink: {permalink}
lane: verify
module_name: "{module_name}"
book: "{book_roman}"
book_label: "{book_label}"
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book {book_roman}"
    status: "Frozen"
    updated: "April 2026"
---
"""

        page_content = frontmatter + "\n" + content + "\n"

        out_path = os.path.join(COLLECTION_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_content)

        module_index.append({
            "module": module_name,
            "slug": slug,
            "book": book_roman,
            "book_label": book_label,
            "url": permalink,
            "title": title,
        })
        created += 1

    # Write module index data
    os.makedirs(os.path.join(SITE_DIR, "_data", "verify"), exist_ok=True)
    index_path = os.path.join(SITE_DIR, "_data", "verify", "taulib_modules.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(module_index, f, indent=2, ensure_ascii=False)

    print(f"\nCreated: {created} collection pages")
    print(f"Skipped: {skipped} (top-level/utility pages)")
    print(f"Module index: {len(module_index)} entries → {index_path}")

    # Count by book
    by_book = {}
    for m in module_index:
        b = m["book"] or "Other"
        by_book[b] = by_book.get(b, 0) + 1
    for b, c in sorted(by_book.items()):
        print(f"  Book {b}: {c}")


if __name__ == "__main__":
    main()
