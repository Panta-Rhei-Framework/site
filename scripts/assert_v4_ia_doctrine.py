#!/usr/bin/env python3
"""Assertions for the v4 IA doctrine release."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


CANONICAL_STATEMENT = (
    "The Panta Rhei Research Program is an independent open research program "
    "dedicated to building a coherent theory of reality."
)

V4_NAV = ["Discover", "Program", "Agenda", "Corpus", "Results", "Verify", "Impact", "Engage"]


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.hidden = 0
        self.text: list[str] = []
        self.h1: list[str] = []
        self.capture: str | None = None
        self.buffer: list[str] = []

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
            self.capture = tag
            self.buffer = []

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
            self.h1.append(normalize("".join(self.buffer)))
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.skip or self.hidden:
            return
        self.text.append(data)
        if self.capture:
            self.buffer.append(data)


def normalize(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split())


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing expected file: {path}")
    return path.read_text(encoding="utf-8", errors="ignore")


def html_path(site: Path, route: str) -> Path:
    return site / "index.html" if route == "/" else site / route.strip("/") / "index.html"


def read_page(site: Path, route: str) -> tuple[str, str, VisibleTextParser]:
    html = read(html_path(site, route))
    parser = VisibleTextParser()
    parser.feed(html)
    return html, normalize(" ".join(parser.text)), parser


def require(text: str, needle: str, route: str) -> None:
    if needle not in text:
        fail(f"{route} missing expected text: {needle}")


def forbid(text: str, needle: str, route: str) -> None:
    if needle in text:
        fail(f"{route} contains forbidden text: {needle}")


def assert_header(site: Path) -> None:
    html, _, _ = read_page(site, "/")
    match = re.search(r"<nav class=\"header-nav\"[\s\S]*?</nav>", html)
    if not match:
        fail("Homepage missing header nav")
    header = match.group(0)
    labels = re.findall(r'class="header-nav-link[^"]*">([^<]+)</a>', header)
    if labels != V4_NAV:
        fail(f"Header nav labels should be {V4_NAV}, found {labels}")
    if 'href="/program/research-agenda/"' not in header or ">Agenda</a>" not in header:
        fail("Agenda header link must point to /program/research-agenda/")
    if ">Publications</a>" in header:
        fail("Publications must not appear in the primary header nav")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_ia_doctrine.py _site", file=sys.stderr)
        return 2

    site = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    assert_header(site)

    html, visible, parser = read_page(site, "/")
    if len(parser.h1) != 1:
        fail(f"/ should contain exactly one h1, found {len(parser.h1)}")
    require(visible, CANONICAL_STATEMENT, "/")
    require(
        visible,
        "Discover for orientation, Program for identity, Agenda for obligations, Corpus for construction, Results for consequences, Verify for inspection, Impact for conditional relevance, and Engage for open scrutiny.",
        "/",
    )
    require(visible, "Agenda Obligations", "/")
    require(visible, "Artifacts & Releases", "/")
    require(visible, "Research Monographs, Monograph Supplements, Research Papers, Research Notes, Research Briefings, White Papers, TauLib, assessment protocols, Release Artifacts, and errata", "/")
    require(visible, "Publications", "/")

    _, visible, parser = read_page(site, "/program/")
    if len(parser.h1) != 1:
        fail(f"/program/ should contain exactly one h1, found {len(parser.h1)}")
    require(visible, CANONICAL_STATEMENT, "/program/")
    require(visible, "Program explains what kind of research object this is", "/program/")
    require(visible, "Agenda states the obligations. Corpus shows the construction. Results presents consequences. Verify makes the work inspectable.", "/program/")
    require(visible, "What We Mean by Coherence", "/program/")
    require(visible, "Why an Inspection Observatory", "/program/")
    forbid(visible, "It is deliberately split into two routes", "/program/")
    forbid(visible, "Research Agenda as obligation layer", "/program/")

    for route in [
        "/program/about/coherent-theory-of-reality/",
        "/program/about/inspection-observatory/",
    ]:
        _, visible, parser = read_page(site, route)
        if len(parser.h1) != 1:
            fail(f"{route} should contain exactly one h1, found {len(parser.h1)}")
        require(visible, "What this page does not claim", route)

    html, visible, parser = read_page(site, "/program/research-agenda/")
    if len(parser.h1) != 1:
        fail(f"/program/research-agenda/ should contain exactly one h1, found {len(parser.h1)}")
    if 'data-lane="agenda"' not in html or 'class="site-body lane-agenda' not in html:
        fail("/program/research-agenda/ must render as the Agenda lane")
    require(visible, "The Agenda lane states the public burden of the program: what language must be earned, what questions must be faced, what answer could count, and what must be built.", "/program/research-agenda/")
    require(visible, "Agenda is the program's public obligation layer", "/program/research-agenda/")

    _, visible, _ = read_page(site, "/discover/")
    for needle in [
        "Program Identity",
        "Agenda Obligations",
        "Corpus Construction",
        "Results Consequences",
        "Verify Inspection",
        "Impact Conditional Relevance",
        "Engage Open Scrutiny",
        "Publications remains the stable artifact and release layer",
    ]:
        require(visible, needle, "/discover/")
    forbid(visible, "Program states the research contract and Research Agenda", "/discover/")

    for route, needle in {
        "/corpus/": "The Corpus is the construction body of the theory",
        "/results/": "Results is where the built Corpus becomes a world.",
        "/verify/": "Verify is where building becomes accountable.",
        "/impact/": "Impact maps what could matter if the work survives inspection.",
        "/engage/": "Engage is where openness becomes operational.",
        "/media/": "Program for identity and doctrine, Agenda for obligations",
        "/media/review-kit/": "independent open research program dedicated to building a coherent theory of reality",
    }.items():
        _, visible, parser = read_page(site, route)
        if len(parser.h1) != 1:
            fail(f"{route} should contain exactly one h1, found {len(parser.h1)}")
        require(visible, needle, route)

    nav_source = read(repo / "_data" / "nav.yml")
    if 'title: "Publications"\n    url: "/publications/"\n    match: "/publications/"' in nav_source:
        fail("Publications must not remain in the header nav data")
    if 'title: "Agenda"\n    url: "/program/research-agenda/"' not in nav_source:
        fail("Header nav data must include Agenda pointing to /program/research-agenda/")

    print("v4 IA doctrine assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
