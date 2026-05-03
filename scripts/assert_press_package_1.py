#!/usr/bin/env python3
"""Assertions for Press Package 1: Open Research / Inspection Architecture."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


PDF_PATH = "/assets/pdfs/white-papers/white-paper-2026-05-03-inspection-architecture-high-scope-open-research.pdf"

ROUTES = [
    "/publications/white-papers/inspection-architecture-high-scope-open-research/",
    "/media/open-research-brief/",
    "/media/",
    "/media/review-kit/",
    "/media/journalist-faq/",
    "/media/social-media-kit/",
    "/program/about/inspection-observatory/",
    "/discover/",
]

CHECKLIST_ITEMS = [
    "Is the scope and burden of proof explicit?",
    "Are the Problem Ledger and source-policy rules visible?",
    "Are Core Semantics and answer-shape obligations stated separately from open problems?",
    "Is there a Construction Roadmap / Construction Spine?",
    "Is there a Corpus with stable IDs and dependency routes?",
    "Is there a formalization surface, and are its limits stated?",
    "Are Results status-marked?",
    "Are bridge claims explicit?",
    "Are falsification or failure paths visible?",
    "Are errata and correction routes public?",
    "Are remaining externalities disclosed?",
    "Is there a route to ask questions or report errors?",
]

ENDORSEMENT_PATTERNS = [
    r"UNESCO\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"The Turing Way\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"TOP(?:\s*/\s*COS|\s+Guidelines)?\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"Center for Open Science\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"EQUATOR\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"COPE\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"Zenodo\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"(endorsed|certified|validated)\s+by\s+(UNESCO|The Turing Way|TOP|COS|Center for Open Science|EQUATOR|COPE|Zenodo)",
]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.hidden = 0
        self.text: list[str] = []
        self.links: list[str] = []
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        classes = set(attr.get("class", "").split())
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if "sr-only" in classes or attr.get("hidden") == "hidden" or attr.get("aria-hidden") == "true":
            self.hidden += 1
            return
        if self.skip or self.hidden:
            return
        if tag == "h1":
            self.h1_count += 1
        if tag == "a" and attr.get("href"):
            self.links.append(attr["href"])

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1
            return
        if self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip and not self.hidden:
            self.text.append(data)

    @property
    def visible(self) -> str:
        return " ".join(" ".join(self.text).replace("\xa0", " ").split())


def fail(message: str) -> None:
    raise AssertionError(message)


def read_page(site: Path, route: str) -> tuple[str, Parser]:
    path = site / "index.html" if route == "/" else site / route.strip("/") / "index.html"
    if not path.exists():
        fail(f"Missing built page for {route}: {path}")
    html = path.read_text(encoding="utf-8", errors="ignore")
    parser = Parser()
    parser.feed(html)
    return html, parser


def require(text: str, needle: str, route: str) -> None:
    if needle not in text:
        fail(f"{route} missing expected text: {needle}")


def assert_one_h1(site: Path) -> None:
    for route in [
        "/publications/white-papers/inspection-architecture-high-scope-open-research/",
        "/media/open-research-brief/",
    ]:
        _, parser = read_page(site, route)
        if parser.h1_count != 1:
            fail(f"{route} should have exactly one H1, found {parser.h1_count}")


def assert_pdf(site: Path) -> None:
    pdf = site / PDF_PATH.strip("/")
    if not pdf.exists():
        fail(f"Missing PDF asset: {pdf}")
    if pdf.stat().st_size < 50_000:
        fail(f"PDF asset is unexpectedly small: {pdf.stat().st_size} bytes")
    _, parser = read_page(site, "/publications/white-papers/inspection-architecture-high-scope-open-research/")
    if PDF_PATH not in parser.links:
        fail("White paper page does not link the Package 1 PDF")
    require(parser.visible, "DOI forthcoming.", "/publications/white-papers/inspection-architecture-high-scope-open-research/")
    require(parser.visible, "no DOI has been reserved", "/publications/white-papers/inspection-architecture-high-scope-open-research/")


def assert_media_order(site: Path) -> None:
    _, parser = read_page(site, "/media/")
    visible = parser.visible
    require(visible, "The first story is the inspection standard.", "/media/")
    require(visible, "CMB-S4", "/media/")
    if visible.index("The first story is the inspection standard.") > visible.index("CMB-S4"):
        fail("/media/ must place the inspection-standard first story before CMB-S4/decisive-test content")
    require(visible, "Open Research Brief", "/media/")
    require(visible, "Inspection Architecture for High-Scope Open Research", "/media/")


def assert_review_kit(site: Path) -> None:
    _, parser = read_page(site, "/media/review-kit/")
    visible = parser.visible
    require(visible, "inspection-architecture checklist", "/media/review-kit/")
    for item in CHECKLIST_ITEMS:
        require(visible, item, "/media/review-kit/")


def assert_faq_and_social(site: Path) -> None:
    _, faq = read_page(site, "/media/journalist-faq/")
    require(faq.visible, "Package 1: Open Research / Inspection Architecture", "/media/journalist-faq/")
    require(faq.visible, "Is Panta Rhei claiming its theory is proven?", "/media/journalist-faq/")
    require(faq.visible, "Citation is context, not endorsement.", "/media/journalist-faq/")

    _, social = read_page(site, "/media/social-media-kit/")
    require(social.visible, "Open Research / Inspection Architecture launch snippets", "/media/social-media-kit/")
    require(social.visible, "High-scope open research should not ask for belief before it has made itself inspectable.", "/media/social-media-kit/")
    require(social.visible, "first story is the inspection standard", "/media/social-media-kit/")


def assert_links(site: Path) -> None:
    expected_links = {
        "/program/about/inspection-observatory/": "Inspection Architecture for High-Scope Open Research",
        "/discover/": "Open Research Brief",
        "/program/about/": "Inspection Architecture for High-Scope Open Research",
        "/program/about/coherent-theory-of-reality/": "Inspection Architecture for High-Scope Open Research",
    }
    for route, needle in expected_links.items():
        _, parser = read_page(site, route)
        require(parser.visible, needle, route)


def assert_no_implied_endorsement(site: Path) -> None:
    for route in ROUTES:
        _, parser = read_page(site, route)
        visible = parser.visible
        for pattern in ENDORSEMENT_PATTERNS:
            if re.search(pattern, visible, flags=re.IGNORECASE):
                fail(f"{route} appears to imply external endorsement via pattern: {pattern}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_press_package_1.py _site", file=sys.stderr)
        return 2
    site = Path(sys.argv[1]).resolve()

    assert_one_h1(site)
    assert_pdf(site)
    assert_media_order(site)
    assert_review_kit(site)
    assert_faq_and_social(site)
    assert_links(site)
    assert_no_implied_endorsement(site)

    print("Press Package 1 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
