#!/usr/bin/env python3
"""Assertions for Press Package 3: Public Research Observatory."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


PDF_PATH = "/assets/pdfs/white-papers/white-paper-2026-05-03-building-a-public-research-observatory.pdf"

NEW_ROUTES = [
    "/publications/white-papers/building-a-public-research-observatory/",
    "/media/public-research-observatory-brief/",
]

LINKED_ROUTES = [
    "/media/",
    "/verify/assessment-protocols/",
    "/engage/review-the-work/",
    "/media/journalist-faq/",
    "/media/social-media-kit/",
    "/discover/",
    "/program/about/inspection-observatory/",
    "/corpus/",
    "/verify/",
    "/engage/",
    "/publications/white-papers/",
]

OBSERVATORY_CHECKLIST_ITEMS = [
    "Does the homepage state the research category without overclaiming completion?",
    "Can a first-time reader move from Discover into Program, Agenda, Corpus, Results, Verify, Impact, and Engage?",
    "Does Program own identity, doctrine, scope, status, and scrutiny posture?",
    "Does Agenda state obligations before answer claims?",
    "Does Corpus expose construction, monographs, registry objects, TauLib projection, and dependency routes?",
    "Do Results separate consequence/status from verification and external acceptance?",
    "Does Verify expose formal checks, bridge checks, predictions, falsification, release manifest, and assessment protocols?",
    "Does Publications keep stable artifacts separate from live Corpus exposition?",
    "Does Impact remain conditional rather than claiming adoption or delivery?",
    "Does Engage provide critique, correction, contribution, and discussion routes without implying endorsement?",
    "Are dynamic public metrics pinned to the Release Manifest rather than hand-owned prose?",
    "Are publication PDFs accompanied by manifest hashes and DOI posture?",
    "Does search help readers find source, status, verification, and artifact routes?",
    "Are compatibility routes, redirects, and legacy labels handled intentionally?",
    "Is the architecture honest about what it cannot prove?",
]

ENDORSEMENT_PATTERNS = [
    r"Jekyll\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"Pagefind\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"GitHub\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"Zenodo\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"(endorsed|certified|validated)\s+by\s+(Jekyll|Pagefind|GitHub|Zenodo)",
]

OVERCLAIM_PATTERNS = [
    r"observatory architecture\s+(validates|certifies)\s+the\s+theory",
    r"website architecture\s+(validates|certifies)\s+the\s+theory",
    r"static publishing\s+(proves|validates|certifies)\s+the\s+theory",
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


def assert_new_routes(site: Path) -> None:
    for route in NEW_ROUTES:
        _, parser = read_page(site, route)
        if parser.h1_count != 1:
            fail(f"{route} should have exactly one H1, found {parser.h1_count}")


def assert_pdf_and_doi(site: Path) -> None:
    pdf = site / PDF_PATH.strip("/")
    if not pdf.exists():
        fail(f"Missing PDF asset: {pdf}")
    if pdf.stat().st_size < 85_000:
        fail(f"PDF asset is unexpectedly small: {pdf.stat().st_size} bytes")
    _, parser = read_page(site, "/publications/white-papers/building-a-public-research-observatory/")
    if PDF_PATH not in parser.links:
        fail("White paper page does not link the Package 3 PDF")
    require(parser.visible, "DOI forthcoming.", "/publications/white-papers/building-a-public-research-observatory/")
    require(parser.visible, "no DOI has been reserved", "/publications/white-papers/building-a-public-research-observatory/")


def assert_core_framing(site: Path) -> None:
    _, paper = read_page(site, "/publications/white-papers/building-a-public-research-observatory/")
    text = paper.visible
    for needle in [
        "public research observatory",
        "Program -> Agenda -> Corpus -> Results -> Verify",
        "Inspection architecture is not validation",
        "Architecture plate",
        "explicitly deferred",
        "does not claim that website architecture proves the theory",
    ]:
        require(text, needle, "/publications/white-papers/building-a-public-research-observatory/")

    _, brief = read_page(site, "/media/public-research-observatory-brief/")
    require(brief.visible, "The observatory is a review interface, not a proof of the theory.", "/media/public-research-observatory-brief/")
    require(brief.visible, "How should a public research program build the interface", "/media/public-research-observatory-brief/")


def assert_media_surfaces(site: Path) -> None:
    _, media = read_page(site, "/media/")
    require(media.visible, "The third safe story is the technical blueprint.", "/media/")
    require(media.visible, "Public Research Observatory Brief", "/media/")
    require(media.visible, "Building a Public Research Observatory for High-Scope Open Research", "/media/")

    _, review = read_page(site, "/verify/assessment-protocols/")
    require(review.visible, "Package 3 — Public Research Observatory", "/verify/assessment-protocols/")
    for item in OBSERVATORY_CHECKLIST_ITEMS:
        require(review.visible, item, "/verify/assessment-protocols/")

    _, faq = read_page(site, "/media/journalist-faq/")
    require(faq.visible, "Package 3: Technical Blueprint / Public Research Observatory", "/media/journalist-faq/")
    require(faq.visible, "Does Package 3 claim the website validates the theory?", "/media/journalist-faq/")

    _, social = read_page(site, "/media/social-media-kit/")
    require(social.visible, "Public Research Observatory launch snippets", "/media/social-media-kit/")
    require(social.visible, "Inspection architecture is not validation", "/media/social-media-kit/")


def assert_doctrine_links(site: Path) -> None:
    for route in LINKED_ROUTES:
        _, parser = read_page(site, route)
        require(parser.visible, "Building a Public Research Observatory", route)


def assert_no_overclaiming(site: Path) -> None:
    for route in NEW_ROUTES + LINKED_ROUTES:
        _, parser = read_page(site, route)
        visible = parser.visible
        for pattern in ENDORSEMENT_PATTERNS + OVERCLAIM_PATTERNS:
            if re.search(pattern, visible, flags=re.IGNORECASE):
                fail(f"{route} appears to imply endorsement or validation via pattern: {pattern}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_press_package_3.py _site", file=sys.stderr)
        return 2
    site = Path(sys.argv[1]).resolve()

    assert_new_routes(site)
    assert_pdf_and_doi(site)
    assert_core_framing(site)
    assert_media_surfaces(site)
    assert_doctrine_links(site)
    assert_no_overclaiming(site)

    print("Press Package 3 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
