#!/usr/bin/env python3
"""Targeted assertions for the v2.2 Batch 2 publications/impact release."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.parts: list[str] = []
        self.h1: list[str] = []
        self.stack: list[str] = []
        self.skip_element_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag)
        attr_map = {key: value or "" for key, value in attrs}
        classes = set(attr_map.get("class", "").split())
        skip_this = tag in {"head", "script", "style", "svg"} or "sr-only" in classes or "data-pagefind-meta" in attr_map
        if skip_this:
            self.skip += 1
            self.skip_element_stack.append(tag)
        if not self.skip and tag in {"h1", "h2", "h3", "p", "li", "td", "th", "div", "section", "article", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.skip_element_stack and self.skip_element_stack[-1] == tag and self.skip:
            self.skip_element_stack.pop()
            self.skip -= 1
        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        if self.stack and self.stack[-1] == "h1":
            self.h1.append(norm(data))
        self.parts.append(data)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def built_file(path: str) -> Path:
    return SITE / path.strip("/") / "index.html"


def page_text(path: str) -> tuple[str, list[str]]:
    full = built_file(path)
    if not full.exists():
        raise AssertionError(f"{path}: missing built page at {full}")
    parser = VisibleTextParser()
    parser.feed(full.read_text(encoding="utf-8", errors="replace"))
    return norm(" ".join(parser.parts)), [heading for heading in parser.h1 if heading]


def require(path: str, *phrases: str) -> None:
    text, h1 = page_text(path)
    if len(h1) != 1:
        raise AssertionError(f"{path}: expected exactly one h1, found {h1}")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path}: missing phrase {phrase!r}")


def forbid_visible(path: str, *phrases: str) -> None:
    text, h1 = page_text(path)
    for phrase in phrases:
        if phrase in text or any(phrase in heading for heading in h1):
            raise AssertionError(f"{path}: forbidden visible phrase still present {phrase!r}")


def require_redirect(path: str, target: str) -> None:
    full = built_file(path)
    if not full.exists():
        raise AssertionError(f"{path}: missing redirect fallback page")
    html = full.read_text(encoding="utf-8", errors="replace")
    if target not in html:
        raise AssertionError(f"{path}: redirect fallback does not reference {target}")


def main() -> int:
    require(
        "/publications/",
        "Research Monographs",
        "Monograph Supplements",
        "Research Papers",
        "Research Notes",
        "Research Briefings",
        "White Papers",
        "Release Artifacts",
        "How we classify new artifacts",
        "Artifact classification matrix",
        "Suggested reading order",
    )
    require("/publications/research-monographs/", "Research Monographs", "Book I", "Book VII")
    require("/publications/monograph-supplements/", "Monograph Supplements", "Numerical Physics Ledger", "Categorical Genesis")
    require("/publications/research-papers/", "Research Papers")
    require("/publications/research-briefings/", "Research Briefings", "Public-Good Briefings")
    require("/publications/research-briefings/public-good/", "Public-Good Briefings", "44", "Reading discipline")
    require("/publications/release-artifacts/", "Release Artifacts")
    require(
        "/publications/monograph-supplements/numerical-physics-ledger/",
        "Numerical Physics Ledger",
        "Status and scope",
        "Monograph Supplement",
    )
    require("/publications/monograph-supplements/categorical-genesis/", "Categorical Genesis", "Monograph Supplement")

    require_redirect("/publications/books/", "/publications/research-monographs/")
    require_redirect("/publications/companion-papers/", "/publications/research-briefings/public-good/")
    require_redirect("/publications/numerical-physics-ledger/", "/publications/monograph-supplements/numerical-physics-ledger/")
    require_redirect("/publications/physics-ledger/", "/publications/monograph-supplements/numerical-physics-ledger/")
    require_redirect("/publications/categorical-genesis/", "/publications/monograph-supplements/categorical-genesis/")

    landing_pages = [
        path
        for path in (SITE / "publications/research-briefings/public-good").glob("*/index.html")
        if path.parent.name != "public-good"
    ]
    if len(landing_pages) != 44:
        raise AssertionError(f"expected 44 Public-Good Briefing landing pages, found {len(landing_pages)}")
    require(
        "/publications/research-briefings/public-good/advanced-fission-safety-operations-licensing-fleet-modernization/",
        "Abstract",
        "Key Takeaways",
        "What this briefing assumes",
        "What this briefing does not claim",
        "Read full text as HTML",
        "PDF Available",
        "Download PDF",
    )
    require(
        "/impact/papers/advanced-fission-safety-operations-licensing-fleet-modernization/",
        "Briefing landing page",
        "conditional scenario artifact",
    )

    for impact_path in [
        "/impact/",
        "/impact/impact-framework/",
        "/impact/foundational-science/",
        "/impact/applied-science-and-research/",
        "/impact/global-education/",
        "/impact/existential-orientation/",
        "/impact/societal-coherence/",
        "/impact/global-public-good/",
        "/impact/portfolio/agriculture/",
    ]:
        require(impact_path, "Result", "Verification survival", "Translation layer", "Domain uptake", "Consequence")

    for public_good_path in ["/impact/", "/impact/global-public-good/", "/impact/portfolio/agriculture/"]:
        require(public_good_path, "conditional public-good portfolio")

    forbidden = (
        "Companion Papers",
        "Companion Paper",
        "companion paper",
        "deployment papers",
        "deployment portfolio",
        "deployment work",
        "public-good deployment portfolio",
    )
    checked = 0
    for html_file in SITE.glob("**/*.html"):
        rel = "/" + str(html_file.relative_to(SITE)).removesuffix("index.html")
        if rel.startswith("/pagefind/"):
            continue
        parser = VisibleTextParser()
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        visible = norm(" ".join(parser.parts + parser.h1))
        for phrase in forbidden:
            if phrase in visible:
                raise AssertionError(f"{rel}: forbidden visible phrase still present {phrase!r}")
        checked += 1
    if checked < 100:
        raise AssertionError(f"site crawl looked too small: checked {checked} HTML pages")

    print("v2.2 Batch 2 publications/impact assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
