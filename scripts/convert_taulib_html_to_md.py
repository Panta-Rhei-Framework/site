#!/usr/bin/env python3
"""
convert_taulib_html_to_md.py — Convert 445 TauLib .html collection files
to clean .md Markdown files. Extracts content structure from doc-gen4 HTML,
produces clean Markdown that Jekyll processes faster and Pagefind indexes better.
"""

import os
import re
from html.parser import HTMLParser

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLECTION_DIR = os.path.join(SITE_DIR, "_taulib_docs")
PINNED_TAULIB_COMMIT = "2261c049119c8dd9a4e891457f196745178c02b3"
LEGACY_SOURCE_PREFIX_RE = re.compile(
    r"https://github\.com/ThorFuchs/PantaRhei-2ndEd/blob/"
    r"[0-9a-f]+/lean4/TauLib/TauLib/"
)


class HTML2Markdown(HTMLParser):
    """Convert doc-gen4 HTML content to clean Markdown."""

    def __init__(self):
        super().__init__()
        self.output = []
        self.in_pre = False
        self.in_code = False
        self.in_decl_header = False
        self.in_doc_string = False
        self.in_heading = False
        self.heading_level = 0
        self.skip_tag = False
        self.link_href = None
        self.current_text = []

    def _flush_text(self):
        text = "".join(self.current_text).strip()
        self.current_text = []
        return text

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get("class", "")

        if tag == "pre":
            self.in_pre = True
            self.output.append("\n```\n")
            return

        if tag == "code" and not self.in_pre:
            self.in_code = True
            self.output.append("`")
            return

        if tag in ("h1", "h2", "h3", "h4"):
            self.in_heading = True
            self.heading_level = int(tag[1])
            self.current_text = []
            return

        if tag == "a":
            href = attrs_dict.get("href", "")
            if "hover-link" in cls:
                self.skip_tag = True
                return
            # Keep external links, skip broken internal doc-gen links
            if href.startswith("http"):
                self.link_href = href
            else:
                self.link_href = None
            return

        if tag == "div":
            if "mod_doc" in cls:
                return
            if "decl" in cls and "decl_header" not in cls:
                decl_id = attrs_dict.get("id", "")
                if decl_id:
                    self.output.append(f"\n---\n\n### `{decl_id}`\n\n")
                return
            if "decl_header" in cls:
                self.in_decl_header = True
                self.output.append("\n**")
                return
            if "doc-string" in cls or "doc_string" in cls:
                self.in_doc_string = True
                return
            if "decl_type" in cls:
                self.output.append(" : ")
                return

        if tag == "span":
            if "decl_kind" in cls:
                self.output.append("")
                return

        if tag == "ul":
            self.output.append("\n")
        if tag == "li":
            self.output.append("- ")
        if tag == "p":
            self.output.append("\n")
        if tag == "br":
            self.output.append("\n")
        if tag == "em":
            self.output.append("*")
        if tag == "strong":
            self.output.append("**")

    def handle_endtag(self, tag):
        if tag == "pre":
            self.in_pre = False
            self.output.append("```\n\n")
            return

        if tag == "code" and not self.in_pre:
            self.in_code = False
            self.output.append("`")
            return

        if tag in ("h1", "h2", "h3", "h4") and self.in_heading:
            self.in_heading = False
            text = self._flush_text()
            if text:
                prefix = "#" * self.heading_level
                self.output.append(f"\n{prefix} {text}\n\n")
            return

        if tag == "a":
            if self.skip_tag:
                self.skip_tag = False
                return
            self.link_href = None
            return

        if tag == "div":
            if self.in_decl_header:
                self.in_decl_header = False
                self.output.append("**\n\n")
                return
            if self.in_doc_string:
                self.in_doc_string = False
                self.output.append("\n")
                return

        if tag == "li":
            self.output.append("\n")
        if tag == "p":
            self.output.append("\n")
        if tag == "em":
            self.output.append("*")
        if tag == "strong":
            self.output.append("**")

    def handle_data(self, data):
        if self.skip_tag:
            return
        if self.in_heading:
            # Clean heading text
            clean = data.strip()
            if clean and clean != "#":
                self.current_text.append(clean)
            return
        if self.in_pre:
            self.output.append(data)
            return
        if self.link_href:
            self.output.append(f"[{data}]({self.link_href})")
            self.link_href = None
            return
        self.output.append(data)

    def get_markdown(self):
        md = "".join(self.output)
        # Clean up excessive whitespace
        md = re.sub(r'\n{4,}', '\n\n\n', md)
        md = re.sub(r' +', ' ', md)
        # Clean up empty bold
        md = md.replace("****", "")
        md = md.replace("** **", " ")
        return md.strip()


def convert_file(html_path):
    """Convert a single .html collection file to .md."""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter and body
    if not content.startswith("---"):
        return None

    end_idx = content.index("---", 3)
    frontmatter = content[:end_idx + 3]
    body = content[end_idx + 3:].strip()

    if not body:
        return frontmatter + "\n\n*No documentation content available for this module.*\n"

    # Convert HTML body to Markdown
    converter = HTML2Markdown()
    try:
        converter.feed(body)
    except Exception:
        # If parsing fails, keep a simplified version
        clean = re.sub(r'<[^>]+>', ' ', body)
        clean = re.sub(r'\s+', ' ', clean).strip()
        return frontmatter + "\n\n" + clean[:2000] + "\n"

    md = converter.get_markdown()

    # If conversion produced very little, fall back
    if len(md) < 20:
        clean = re.sub(r'<[^>]+>', ' ', body)
        clean = re.sub(r'\s+', ' ', clean).strip()
        md = clean[:2000]

    result = frontmatter + "\n\n" + md + "\n"
    return LEGACY_SOURCE_PREFIX_RE.sub(
        f"https://github.com/Panta-Rhei-Research/taulib/blob/{PINNED_TAULIB_COMMIT}/TauLib/",
        result,
    )


def main():
    html_files = sorted(f for f in os.listdir(COLLECTION_DIR) if f.endswith(".html"))
    print(f"Converting {len(html_files)} .html files to .md")

    converted = 0
    errors = 0

    for fname in html_files:
        html_path = os.path.join(COLLECTION_DIR, fname)
        md_fname = fname.replace(".html", ".md")
        md_path = os.path.join(COLLECTION_DIR, md_fname)

        result = convert_file(html_path)
        if result:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(result)
            os.remove(html_path)
            converted += 1
        else:
            errors += 1
            print(f"  ERROR: {fname}")

    # Check sizes
    total_size = sum(
        os.path.getsize(os.path.join(COLLECTION_DIR, f))
        for f in os.listdir(COLLECTION_DIR)
        if f.endswith(".md")
    )

    print(f"\nConverted: {converted}")
    print(f"Errors: {errors}")
    print(f"Total collection size: {total_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
