#!/usr/bin/env python3
"""Assertions for the v2.2 final polish wave."""

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
        self.article_classes: list[str] = []

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
        if tag == "article":
            self.article_classes.append(attr.get("class", ""))

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
    return " ".join(value.replace("-&gt;", "->").replace("&gt;", ">").split())


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
    routes = [
        "/",
        "/program/",
        "/program/research-agenda/",
        "/corpus/",
        "/publications/",
        "/publications/research-briefings/public-good/",
        "/impact/",
        "/verify/",
        "/engage/",
    ]

    forbidden_visible = [
        "· ment",
        "public good papers",
        "Companion Papers",
        "deployment portfolio",
        "deployment papers",
        "In v2.1",
        "In v2.2 language",
        "Status: Resolved",
        "Resolved —",
    ]

    for route in routes:
        _, visible, parser = read_page(site, route)
        if len(parser.h1) != 1:
            raise AssertionError(f"{route} should have exactly one visible H1, found {len(parser.h1)}")
        for phrase in forbidden_visible:
            forbid(visible, phrase, route)

    _, visible, parser = read_page(site, "/program/")
    require_card_list(parser, "/program/")
    for needle in [
        "Panta Rhei is currently:",
        "organized through the v4 public spine",
        "with Publications preserved as the stable artifact and release layer",
        "publicly inspectable through Problem Ledger v1.0, Core Semantics, Construction Spine, Registry, Results mirrors, verification routes, Research Notes, Public-Good Briefings, and correction surfaces",
        "open to structured questions, critique, review, and contribution through GitHub Discussions, Issues, Pull Requests, and email",
        "not socially settled and not a substitute for expert peer review",
        "Corpus shows how the structure is built through the Construction Spine, Registry, TauLib projection, Research Monographs, and dependency graph",
        "What this lane is",
        "What this lane is not",
        "identity and doctrine layer",
    ]:
        require(visible, needle, "/program/")

    _, visible, _ = read_page(site, "/")
    require(visible, "independent open research program dedicated to building a coherent theory of reality", "/")
    require(visible, "spine, map, monographs, registry, TauLib projection, and dependency graph", "/")
    require(visible, "Five generators, one operator, and K0-K6 axioms", "/")

    _, visible, parser = read_page(site, "/program/research-agenda/")
    if "domain-ledger-rules" not in parser.tables:
        raise AssertionError("/program/research-agenda/ missing semantic domain-ledger-rules table")
    require(visible, "Problem -> Constraint -> Ontic burden -> Build order -> Corpus construction -> Results -> Verify", "/program/research-agenda/")

    _, visible, parser = read_page(site, "/corpus/")
    require_card_list(parser, "/corpus/")
    require(visible, "The primary human-readable route into the Corpus is the Construction Spine", "/corpus/")

    _, _, parser = read_page(site, "/publications/")
    if "artifact-classification-matrix" not in parser.tables:
        raise AssertionError("/publications/ missing semantic artifact classification table")

    html, visible, parser = read_page(site, "/publications/research-briefings/public-good/")
    require(visible, "Publications · Research Briefings · Public-Good Briefings", "/publications/research-briefings/public-good/")
    require(visible, "44 conditional scenario briefings across 11 public-good portfolios.", "/publications/research-briefings/public-good/")
    if "Publications · Publication Family · Canonical" in visible:
        raise AssertionError("/publications/research-briefings/public-good/ still shows generic publication-family metadata")
    if not any("briefing-list" in classes for classes in parser.ul_classes):
        raise AssertionError("/publications/research-briefings/public-good/ missing briefing-list markup")
    if sum("briefing-card" in classes for classes in parser.article_classes) != 44:
        raise AssertionError("/publications/research-briefings/public-good/ should render 44 briefing-card articles")
    if len(set(re.findall(r'href="/publications/research-briefings/public-good/[^"]+/"', html))) != 44:
        raise AssertionError("/publications/research-briefings/public-good/ should link 44 briefing landing pages")
    for heading in ["Agriculture — 5 briefings", "Weather — 3 briefings"]:
        require(visible, heading, "/publications/research-briefings/public-good/")

    for route in ["/impact/", "/verify/", "/engage/"]:
        _, _, parser = read_page(site, route)
        require_card_list(parser, route)
    _, _, parser = read_page(site, "/impact/")
    if not any("portfolio-card-list" in classes for classes in parser.ul_classes):
        raise AssertionError("/impact/ missing semantic portfolio-card-list markup")

    print("v2.2 final polish assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
