#!/usr/bin/env python3
"""Assertions for the v2.2 parallel narrative-audit remediation wave."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hidden = 0
        self.skip = 0
        self.capture: str | None = None
        self.buffer: list[str] = []
        self.h1: list[str] = []
        self.h2: list[str] = []
        self.h3: list[str] = []
        self.text: list[str] = []
        self.tables: list[str] = []
        self.ul_classes: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        classes = set(attr.get("class", "").split())
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if "sr-only" in classes or attr.get("hidden") == "hidden" or attr.get("aria-hidden") == "true":
            self.hidden += 1
        if self.skip or self.hidden:
            return
        if tag in {"h1", "h2", "h3"}:
            self.capture = tag
            self.buffer = []
        if tag == "table":
            self.tables.append(attr.get("class", ""))
        if tag == "ul":
            self.ul_classes.append(attr.get("class", ""))

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1
            return
        if self.hidden:
            self.hidden -= 1
            return
        if self.skip:
            return
        if self.capture == tag:
            text = normalize("".join(self.buffer))
            getattr(self, tag).append(text)
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.skip or self.hidden:
            return
        self.text.append(data)
        if self.capture:
            self.buffer.append(data)


def normalize(value: str) -> str:
    return " ".join(value.split())


def read_page(site: Path, route: str) -> tuple[str, str, PageParser]:
    html_path = site / route.strip("/") / "index.html"
    if route == "/":
        html_path = site / "index.html"
    if not html_path.exists():
        raise AssertionError(f"Missing built page for {route}: {html_path}")
    html = html_path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)
    visible = normalize(" ".join(parser.text))
    return html, visible, parser


def require(text: str, needle: str, route: str) -> None:
    if needle not in text:
        raise AssertionError(f"{route} missing expected text: {needle}")


def forbid(text: str, needle: str, route: str) -> None:
    if needle in text:
        raise AssertionError(f"{route} contains forbidden visible text: {needle}")


def require_card_list(parser: PageParser, route: str) -> None:
    if not any("v2-card-list" in classes for classes in parser.ul_classes):
        raise AssertionError(f"{route} missing semantic v2-card-list markup")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")

    all_routes = [
        "/",
        "/discover/",
        "/program/",
        "/program/research-agenda/",
        "/corpus/",
        "/publications/",
        "/publications/research-briefings/public-good/",
        "/impact/",
        "/engage/",
        "/engage/how-to-engage/",
        "/engage/read-explore/",
        "/engage/inspect-verify/",
        "/engage/critique-challenge/",
        "/engage/review-the-work/",
        "/engage/collaborate/",
        "/engage/discussions/",
    ]

    for route in all_routes:
        _, visible, parser = read_page(site, route)
        if len(parser.h1) != 1:
            raise AssertionError(f"{route} should have exactly one visible H1, found {len(parser.h1)}")
        forbid(visible, "· ment", route)

    for route in [
        "/engage/how-to-engage/",
        "/engage/read-explore/",
        "/engage/inspect-verify/",
        "/engage/critique-challenge/",
        "/engage/review-the-work/",
        "/engage/collaborate/",
        "/engage/discussions/",
    ]:
        _, visible, _ = read_page(site, route)
        if "Engagement Route" not in visible and "Engagement Guide" not in visible:
            raise AssertionError(f"{route} should preserve Engagement Route/Guide hero metadata")

    _, visible, _ = read_page(site, "/")
    require(visible, "Research Monographs, a structured Corpus, typed Results", "/")
    require(visible, "Landmark Results, World Readouts, Problem Ledger Answers, Recovery Target Status, and Progress Against Agenda.", "/")
    forbid(visible, "Typed answer surfaces and problem mappings.", "/")

    _, visible, parser = read_page(site, "/program/")
    require_card_list(parser, "/program/")
    for needle in [
        "structured Research Agenda, Corpus, Results, Verify, Publications, Impact, and Engage surfaces",
        "Corpus Construction Spine, Registry, TauLib projection, Results mirrors, and verification routes",
        "GitHub Discussions, issues, pull requests, email, and errata",
        "Research Agenda states the burden of proof through the Problem Ledger, Recovery Requirements, Kernel, Model & Reality, and Construction Roadmap.",
        "Publications organizes stable artifacts through Research Monographs, Monograph Supplements, Research Papers, Research Notes, Research Briefings, White Papers, and Release Artifacts.",
    ]:
        require(visible, needle, "/program/")

    _, visible, parser = read_page(site, "/discover/")
    require_card_list(parser, "/discover/")
    require(visible, "TauLib projection, Research Monographs, and dependency graph", "/discover/")
    require(visible, "Research Monographs, Monograph Supplements, Research Papers, Research Notes, Research Briefings, White Papers, Release Artifacts, and Errata", "/discover/")
    forbid(visible, "released artifacts, notes, ledgers, and errata", "/discover/")

    _, visible, parser = read_page(site, "/corpus/")
    require_card_list(parser, "/corpus/")
    require(visible, "The primary human-readable route into the Corpus is the Construction Spine", "/corpus/")
    forbid(visible, "In v2.1", "/corpus/")

    _, visible, _ = read_page(site, "/program/research-agenda/")
    for label in ["Problem", "Constraint", "Ontic burden", "Build order", "Corpus construction", "Results", "Verify"]:
        require(visible, label, "/program/research-agenda/")
    for stale in ["Question -> Constraint", "Construction -> Derivation", "Derivation -> Scrutiny"]:
        forbid(visible, stale, "/program/research-agenda/")

    _, visible, parser = read_page(site, "/publications/")
    if "artifact-classification-matrix" not in parser.tables:
        raise AssertionError("/publications/ missing semantic artifact classification table")

    html, visible, parser = read_page(site, "/publications/research-briefings/public-good/")
    require(visible, "Agriculture — 5 briefings", "/publications/research-briefings/public-good/")
    require(visible, "Weather — 3 briefings", "/publications/research-briefings/public-good/")
    forbid(visible, "public good papers", "/publications/research-briefings/public-good/")
    if len(set(re.findall(r'href="/publications/research-briefings/public-good/[^"]+/"', html))) != 44:
        raise AssertionError("/publications/research-briefings/public-good/ should link 44 briefing landing pages")

    _, _, parser = read_page(site, "/impact/")
    require_card_list(parser, "/impact/")
    if not any("portfolio-card-list" in classes for classes in parser.ul_classes):
        raise AssertionError("/impact/ missing semantic portfolio-card-list markup")

    print("v2.2 narrative audit remediation assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
