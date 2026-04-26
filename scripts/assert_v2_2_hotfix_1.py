#!/usr/bin/env python3
"""Targeted assertions for the v2.2 hotfix 1 terminology cleanup."""

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
        self.skip_stack: list[str] = []
        self.stack: list[str] = []
        self.parts: list[str] = []
        self.h1: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag)
        attr_map = {key: value or "" for key, value in attrs}
        classes = set(attr_map.get("class", "").split())
        if tag in {"head", "script", "style", "svg"} or "sr-only" in classes or "data-pagefind-meta" in attr_map:
            self.skip += 1
            self.skip_stack.append(tag)
            return
        if tag in {"h1", "h2", "h3", "p", "li", "td", "th", "div", "section", "article", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.skip_stack and self.skip_stack[-1] == tag and self.skip:
            self.skip_stack.pop()
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


def built_file(route: str) -> Path:
    if route == "/":
        return SITE / "index.html"
    return SITE / route.strip("/") / "index.html"


def page_text(route: str) -> tuple[str, list[str]]:
    full = built_file(route)
    if not full.exists():
        raise AssertionError(f"{route}: missing built page at {full}")
    parser = VisibleTextParser()
    parser.feed(full.read_text(encoding="utf-8", errors="replace"))
    return norm(" ".join(parser.parts)), [heading for heading in parser.h1 if heading]


def require(route: str, *phrases: str) -> None:
    text, h1 = page_text(route)
    if len(h1) != 1:
        raise AssertionError(f"{route}: expected exactly one h1, found {h1}")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{route}: missing phrase {phrase!r}")


def forbid(route: str, *phrases: str) -> None:
    text, h1 = page_text(route)
    visible = norm(" ".join([text, *h1]))
    for phrase in phrases:
        if phrase in visible:
            raise AssertionError(f"{route}: forbidden visible phrase still present {phrase!r}")


def require_redirect(route: str, target: str) -> None:
    full = built_file(route)
    if not full.exists():
        raise AssertionError(f"{route}: missing redirect fallback page")
    html = full.read_text(encoding="utf-8", errors="replace")
    if target not in html:
        raise AssertionError(f"{route}: redirect fallback does not reference {target}")


def main() -> int:
    require(
        "/",
        "Research Monographs, Monograph Supplements, Research Papers, Research Notes, Research Briefings, White Papers, and Release Artifacts.",
        "the site makes status, verification route, and external-acceptance boundaries visible at the page level",
        "Monograph Supplements such as the Numerical Physics Ledger",
    )
    forbid("/", "v2 makes", "companion papers", "Books, Research Briefings", "guided tours")

    require(
        "/publications/",
        "Research Monographs",
        "Monograph Supplements",
        "Research Papers",
        "Research Notes",
        "Research Briefings",
        "White Papers",
        "Release Artifacts",
        "Public-Good Briefings",
        "Artifact classification matrix",
    )
    require("/publications/research-briefings/", "Research Briefings", "Public-Good Briefings")
    require("/publications/research-briefings/public-good/", "Public-Good Briefings", "44", "conditional scenario")
    require_redirect("/publications/companion-papers/", "/publications/research-briefings/public-good/")

    require(
        "/impact/global-public-good/",
        "11 conditional public-good portfolios",
        "44 Public-Good Briefings",
        "scenario maps",
        "not deployment claims",
        "Public-Good Briefings provide the deeper conditional scenario analyses",
    )
    forbid("/impact/global-public-good/", "Companion Papers", "companion papers", "deployment portfolio", "deployment papers")

    for route in [
        "/impact/foundational-science/",
        "/impact/applied-science-and-research/",
        "/impact/global-education/",
        "/impact/existential-orientation/",
        "/impact/societal-coherence/",
    ]:
        require(route, "Reading discipline", "What this does not mean", "Boundary condition")
        forbid(route, "Scope Core Idea Possible Consequences Boundaries")

    require(
        "/program/research-agenda/",
        "Program definition",
        "The four agenda surfaces",
        "Problem Ledger",
        "Recovery Requirements",
        "Kernel, Model & Reality",
        "Construction Roadmap",
        "Together, these four surfaces define the public research contract",
    )
    forbid("/program/research-agenda/", "third major surface")

    require(
        "/results/",
        "Results is where the built Corpus becomes a world",
        "Life-facing results",
        "Metaphysics / Philosophy-facing results",
    )

    for route in ["/engage/", "/program/research-agenda/", "/results/", "/impact/", "/publications/"]:
        forbid(
            route,
            "engage, open-research",
            "github-discussions, scrutiny",
            "Homepage Canonical",
            "Program Program Sub-lane Canonical",
            "Results Lane Root Canonical",
            "Impact Impact Stratum Conditional",
        )

    print("v2.2 hotfix 1 assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
