#!/usr/bin/env python3
"""Assertions for Press Package 2: Theory of Reality."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


PDF_PATH = "/assets/pdfs/white-papers/white-paper-2026-05-03-the-shape-of-a-theory-of-reality.pdf"

NEW_ROUTES = [
    "/publications/white-papers/the-shape-of-a-theory-of-reality/",
    "/media/theory-of-reality-brief/",
]

LINKED_ROUTES = [
    "/media/",
    "/verify/assessment-protocols/",
    "/engage/review-the-work/",
    "/media/journalist-faq/",
    "/media/social-media-kit/",
    "/program/about/",
    "/program/about/coherent-theory-of-reality/",
    "/program/research-agenda/",
    "/program/research-agenda/core-design-principles/",
    "/program/research-agenda/kernel-model-reality/answer-shape-requirements/",
    "/program/research-agenda/construction-roadmap/",
    "/program/about/related-approaches/",
]

CHECKLIST_ITEMS = [
    "Does the program distinguish coherent theory of reality from",
    "Is the canonical claim stated as a building burden",
    "Are Program doctrine, Agenda obligations, Corpus construction, Results consequences, Verify inspection, Impact conditionality, and Engage scrutiny kept distinct?",
    "Are core terms such as reality, proof, observer, life, mind, value, and public good earned rather than borrowed?",
    "Are accepted questions visible before answers are evaluated?",
    "Can a result be traced from Agenda obligation to Corpus construction to Verify route?",
    "Are internal status, formal verification, empirical support, external review, and external acceptance separated?",
    "Are bridge claims and translation assumptions visible?",
    "Are no-externalities and unresolved-frontier boundaries disclosed?",
    "Does Impact use conditional relevance rather than adoption, deployment, or delivery language?",
    "Does Related Approaches function as a positioning map rather than a takedown?",
    "Does Engage make scrutiny possible without implying endorsement?",
]

ENDORSEMENT_PATTERNS = [
    r"Britannica\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"Stanford Encyclopedia of Philosophy\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"UNESCO\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"UKRI\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"ESRC\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"EPSRC\s+(endorses|endorsed|certifies|certified|validates|validated)",
    r"(endorsed|certified|validated)\s+by\s+(Britannica|Stanford Encyclopedia of Philosophy|UNESCO|UKRI|ESRC|EPSRC)",
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
    if pdf.stat().st_size < 80_000:
        fail(f"PDF asset is unexpectedly small: {pdf.stat().st_size} bytes")
    _, parser = read_page(site, "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    if PDF_PATH not in parser.links:
        fail("White paper page does not link the Package 2 PDF")
    require(parser.visible, "DOI forthcoming.", "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    require(parser.visible, "no DOI has been reserved", "/publications/white-papers/the-shape-of-a-theory-of-reality/")


def assert_core_framing(site: Path) -> None:
    _, paper = read_page(site, "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    text = paper.visible
    require(text, "Panta Rhei is not using", "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    require(text, "theory of everything", "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    require(text, "coherent theory of reality", "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    require(text, "earn its language", "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    require(text, "earn its questions", "/publications/white-papers/the-shape-of-a-theory-of-reality/")
    require(text, "build its answers", "/publications/white-papers/the-shape-of-a-theory-of-reality/")

    _, brief = read_page(site, "/media/theory-of-reality-brief/")
    require(brief.visible, "not asking journalists to cover a theory of everything as a settled scientific claim", "/media/theory-of-reality-brief/")
    require(brief.visible, "coherent theory of reality", "/media/theory-of-reality-brief/")


def assert_media_surfaces(site: Path) -> None:
    _, media = read_page(site, "/media/")
    require(media.visible, "The second safe story is the intellectual category.", "/media/")
    require(media.visible, "Theory of Reality Brief", "/media/")
    require(media.visible, "The Shape of a Theory of Reality", "/media/")

    _, review = read_page(site, "/verify/assessment-protocols/")
    require(review.visible, "Package 2 — Theory of Reality", "/verify/assessment-protocols/")
    for item in CHECKLIST_ITEMS:
        require(review.visible, item, "/verify/assessment-protocols/")

    _, faq = read_page(site, "/media/journalist-faq/")
    require(faq.visible, "Package 2: Theory of Reality", "/media/journalist-faq/")
    require(faq.visible, "Is Panta Rhei a theory of everything?", "/media/journalist-faq/")
    require(faq.visible, "Citation is not endorsement", "/media/journalist-faq/")

    _, social = read_page(site, "/media/social-media-kit/")
    require(social.visible, "Theory of Reality launch snippets", "/media/social-media-kit/")
    require(social.visible, "coherent theory of reality, not theory of everything", "/media/social-media-kit/")


def assert_doctrine_links(site: Path) -> None:
    for route in LINKED_ROUTES:
        _, parser = read_page(site, route)
        require(parser.visible, "The Shape of a Theory of Reality", route)

    _, related = read_page(site, "/program/about/related-approaches/")
    require(related.visible, "burden-bearing category", "/program/about/related-approaches/")
    require(related.visible, "rather than", "/program/about/related-approaches/")


def assert_no_implied_endorsement(site: Path) -> None:
    for route in NEW_ROUTES + LINKED_ROUTES:
        _, parser = read_page(site, route)
        visible = parser.visible
        for pattern in ENDORSEMENT_PATTERNS:
            if re.search(pattern, visible, flags=re.IGNORECASE):
                fail(f"{route} appears to imply external endorsement via pattern: {pattern}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_press_package_2.py _site", file=sys.stderr)
        return 2
    site = Path(sys.argv[1]).resolve()

    assert_new_routes(site)
    assert_pdf_and_doi(site)
    assert_core_framing(site)
    assert_media_surfaces(site)
    assert_doctrine_links(site)
    assert_no_implied_endorsement(site)

    print("Press Package 2 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
