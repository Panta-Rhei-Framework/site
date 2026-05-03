#!/usr/bin/env python3
"""Assertions for the v4 Core Semantics public relabeling."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


LOCKED_DOCTRINE = (
    "Core Semantics is not a promise to reproduce current semantics unchanged. "
    "It is the obligation to earn the language of the domains the theory addresses. "
    "Where established semantics works, the theory must carry it. "
    "Where established semantics breaks, the theory must retype, bridge, or replace it with reasons."
)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1: list[str] = []
        self.text: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1
        if tag == "h1":
            self._in_h1 = False

    _in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        self.text.append(data)
        if self._in_h1:
            self.h1.append(data)

    @property
    def visible(self) -> str:
        return " ".join(" ".join(self.text).split())

    @property
    def h1_text(self) -> str:
        return " ".join(" ".join(self.h1).split())


def read_page(site: Path, route: str) -> Parser:
    path = site / route.strip("/") / "index.html"
    if route == "/":
        path = site / "index.html"
    if not path.exists():
        raise AssertionError(f"Missing built page: {route}")
    parser = Parser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def require(text: str, needle: str, route: str) -> None:
    if needle not in text:
        raise AssertionError(f"{route} missing expected text: {needle}")


def forbid(text: str, needle: str, route: str) -> None:
    if needle in text:
        raise AssertionError(f"{route} contains forbidden text: {needle}")


def assert_h1(site: Path, route: str, expected: str) -> Parser:
    parser = read_page(site, route)
    if parser.h1_text != expected:
        raise AssertionError(f"{route} expected H1 {expected!r}, got {parser.h1_text!r}")
    return parser


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")

    agenda = assert_h1(site, "/program/research-agenda/", "Agenda")
    require(
        agenda.visible,
        "The Agenda lane states the public burden of the program: what language must be earned, what questions must be faced, what answer could count, and what must be built.",
        "/program/research-agenda/",
    )
    for expected in [
        "Core Semantics",
        "The language the theory must earn: formal reasoning, physical measurement and law, life organization, reflective meaning, and ontic boundary.",
        "Open and foundational questions the program agrees to keep visible, classify, address, reframe, or reject with reason.",
        "Language -> Question -> Answer shape -> Build order -> Corpus construction -> Results -> Verify",
    ]:
        require(agenda.visible, expected, "/program/research-agenda/")
    forbid(agenda.visible, "Core Semantics preserves established theories", "/program/research-agenda/")

    core = assert_h1(site, "/program/research-agenda/recovery-requirements/", "Core Semantics")
    for expected in [
        "The language the theory must earn before it can answer.",
        LOCKED_DOCTRINE,
        "This surface was previously labeled Recovery Requirements.",
        "The point is not to preserve established theories as untouchable primitives.",
    ]:
        require(core.visible, expected, "/program/research-agenda/recovery-requirements/")
    forbid(core.visible, "Recovery Requirements Ledger", "/program/research-agenda/recovery-requirements/")

    domain_h1s = {
        "/program/research-agenda/recovery-requirements/mathematics/": "Mathematics Core Semantics",
        "/program/research-agenda/recovery-requirements/physics/": "Physics Core Semantics",
        "/program/research-agenda/recovery-requirements/life/": "Life Core Semantics",
        "/program/research-agenda/recovery-requirements/metaphysics/": "Metaphysics Core Semantics",
    }
    for route, h1 in domain_h1s.items():
        page = assert_h1(site, route, h1)
        require(page.visible, "Core semantic targets", route)
        forbid(page.visible, "Recovery Requirements", route)

    item = read_page(site, "/program/research-agenda/recovery-requirements/physics/physical-quantity-types/")
    require(item.visible, "Core semantic target", "physical quantity item")
    require(item.visible, "Core Semantic Target", "physical quantity item")
    forbid(item.visible, "Recovery Requirement", "physical quantity item")

    result_mirror = assert_h1(site, "/results/recovery-target-status/", "Core Semantics Status")
    require(result_mirror.visible, "Current program status against the semantic load the theory must earn before it can answer.", "/results/recovery-target-status/")
    forbid(result_mirror.visible, "Recovery Requirements", "/results/recovery-target-status/")

    problem = read_page(site, "/program/research-agenda/problem-ledger/physics/neutrino-mass/")
    require(problem.visible, "Related Core Semantic Targets", "/program/research-agenda/problem-ledger/physics/neutrino-mass/")
    forbid(problem.visible, "Related Recovery Requirements", "/program/research-agenda/problem-ledger/physics/neutrino-mass/")

    discover = read_page(site, "/discover/")
    require(discover.visible, "Agenda states the obligations: Core Semantics, Problem Ledger, answer-shape burden, refusals, and Construction Roadmap.", "/discover/")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
