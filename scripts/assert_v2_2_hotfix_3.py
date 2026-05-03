#!/usr/bin/env python3
"""Targeted assertions for v2.2 hotfix batch 3."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hidden_depth = 0
        self.skip_depth = 0
        self.capture: str | None = None
        self.buffer: list[str] = []
        self.h1: list[str] = []
        self.h2: list[str] = []
        self.h3: list[str] = []
        self.text: list[str] = []
        self.tables: list[str] = []
        self.ul_classes: list[str] = []
        self.ol_classes: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        classes = set(attr.get("class", "").split())
        if tag in {"script", "style"}:
            self.skip_depth += 1
            return
        if "sr-only" in classes or attr.get("hidden") == "hidden":
            self.hidden_depth += 1
        if self.skip_depth or self.hidden_depth:
            return
        if tag in {"h1", "h2", "h3"}:
            self.capture = tag
            self.buffer = []
        if tag == "table":
            self.tables.append(attr.get("class", ""))
        if tag == "ul":
            self.ul_classes.append(attr.get("class", ""))
        if tag == "ol":
            self.ol_classes.append(attr.get("class", ""))

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.hidden_depth:
            self.hidden_depth -= 1
            return
        if self.skip_depth:
            return
        if self.capture == tag:
            text = normalize("".join(self.buffer))
            if tag == "h1":
                self.h1.append(text)
            elif tag == "h2":
                self.h2.append(text)
            elif tag == "h3":
                self.h3.append(text)
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.skip_depth or self.hidden_depth:
            return
        self.text.append(data)
        if self.capture:
            self.buffer.append(data)


def normalize(value: str) -> str:
    return " ".join(value.split())


def parse(site: Path, route: str) -> tuple[str, VisibleTextParser]:
    html_path = site / route.strip("/") / "index.html"
    if route == "/":
        html_path = site / "index.html"
    if not html_path.exists():
        raise AssertionError(f"Missing built route: {route}")
    html = html_path.read_text(encoding="utf-8")
    parser = VisibleTextParser()
    parser.feed(html)
    return html, parser


def assert_contains(text: str, needle: str, route: str) -> None:
    if needle not in text:
        raise AssertionError(f"{route} missing expected text: {needle}")


def assert_not_contains(text: str, needle: str, route: str) -> None:
    if needle in text:
        raise AssertionError(f"{route} contains stale visible text: {needle}")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")

    html, page = parse(site, "/")
    visible = normalize(" ".join(page.text))
    assert_contains(visible, "Research Monographs, a structured Corpus, typed Results, verification routes, and empirical challenge commitments.", "/")
    assert_contains(visible, "Construction Spine, Registry, TauLib projection, Research Monographs, and dependency graph.", "/")
    assert_contains(visible, "Landmark Results, World Readouts, Problem Ledger Answers, Core Semantics Status, Additional Derived Results, and Progress Against Agenda.", "/")
    assert_not_contains(visible, "books, a structured research corpus, typed results", "/")
    assert_not_contains(visible, "Typed answer surfaces, problem mappings, and world readouts", "/")

    html, page = parse(site, "/program/research-agenda/")
    visible = normalize(" ".join(page.text))
    if "The Research Agenda is the program's public obligation layer" not in visible and "The Research Agenda is the program’s public obligation layer" not in visible:
        raise AssertionError("/program/research-agenda/ missing evergreen Research Agenda obligation sentence")
    assert_not_contains(visible, "In v2.2 language", "/program/research-agenda/")
    if "domain-ledger-rules" not in page.tables:
        raise AssertionError("/program/research-agenda/ missing semantic domain-ledger-rules table")
    assert_not_contains(visible, "Program Program Sub-lane Canonical", "/program/research-agenda/")

    html, page = parse(site, "/publications/")
    visible = normalize(" ".join(page.text))
    if "artifact-classification-matrix" not in page.tables:
        raise AssertionError("/publications/ missing artifact-classification-matrix table")
    if not any("v2-card-list" in classes for classes in page.ul_classes):
        raise AssertionError("/publications/ publication categories are not a semantic card list")
    if not page.ol_classes:
        raise AssertionError("/publications/ suggested reading order did not render as an ordered list")
    assert_contains(visible, "Research Briefings", "/publications/")
    assert_contains(visible, "Public-Good Briefings", "/publications/")

    html, page = parse(site, "/publications/research-briefings/")
    visible = normalize(" ".join(page.text))
    assert page.h1 == ["Research Briefings"], "/publications/research-briefings/ should have the Research Briefings H1"
    assert_contains(visible, "framework-grounded synthesis and translation artifacts", "/publications/research-briefings/")
    assert_contains(visible, "Public-Good Briefings", "/publications/research-briefings/")

    html, page = parse(site, "/publications/research-briefings/public-good/")
    visible = normalize(" ".join(page.text))
    assert_contains(visible, "44 conditional scenario briefings across 11 public-good portfolios.", "/publications/research-briefings/public-good/")
    assert_not_contains(visible, "public good papers", "/publications/research-briefings/public-good/")
    expected_groups = {
        "Agriculture — 5 briefings",
        "Biodiversity / Restoration — 1 briefing",
        "Climate — 4 briefings",
        "Disaster — 4 briefings",
        "Energy — 5 briefings",
        "Ocean — 4 briefings",
        "One Health — 4 briefings",
        "Pollution / Circularity — 4 briefings",
        "Solar — 5 briefings",
        "Water / WASH — 5 briefings",
        "Weather — 3 briefings",
    }
    missing_groups = sorted(expected_groups.difference(page.h3))
    if missing_groups:
        raise AssertionError(f"/publications/research-briefings/public-good/ missing grouped headings: {missing_groups}")
    briefing_links = re.findall(r'href="/publications/research-briefings/public-good/[^"]+/"', html)
    if len(set(briefing_links)) != 44:
        raise AssertionError(f"Expected 44 public-good briefing landing links, found {len(set(briefing_links))}")

    html, page = parse(site, "/impact/")
    visible = normalize(" ".join(page.text))
    if not any("v2-card-list" in classes for classes in page.ul_classes):
        raise AssertionError("/impact/ impact strata are not a semantic card list")
    if not any("portfolio-card-list" in classes for classes in page.ul_classes):
        raise AssertionError("/impact/ public-good portfolios are not a semantic card list")
    assert_contains(visible, "Global Public-Good Portfolios", "/impact/")

    for route in ["/impact/", "/publications/", "/publications/research-briefings/public-good/", "/engage/", "/results/"]:
        _, page = parse(site, route)
        visible = normalize(" ".join(page.text))
        for forbidden in ["search_keywords", "true false", "[\"", "\"]"]:
            assert_not_contains(visible, forbidden, route)

    print("v2.2 hotfix batch 3 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
