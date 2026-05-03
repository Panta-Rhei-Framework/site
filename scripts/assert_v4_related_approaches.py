#!/usr/bin/env python3
"""Assertions for the v4 Related Approaches Program doctrine release."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


HUB = "/program/about/related-approaches/"

CHILDREN = {
    "/program/about/related-approaches/wolfram-ruliad/": "Wolfram Ruliad and Physics Project",
    "/program/about/related-approaches/penrose-twistor-theory/": "Penrose Twistor Theory and Conformal Geometry",
    "/program/about/related-approaches/wheeler-feynman-absorber/": "Wheeler-Feynman Absorber Theory",
    "/program/about/related-approaches/it-from-bit-muh/": "It from Bit and the Mathematical Universe",
    "/program/about/related-approaches/constructor-theory/": "Constructor Theory",
    "/program/about/related-approaches/structural-realism/": "Ontic Structural Realism",
    "/program/about/related-approaches/quantum-interpretations/": "Relational Quantum Mechanics and Many Worlds",
    "/program/about/related-approaches/hott-topos-internal-logic/": "HoTT, Topos Theory, and Internal Logic",
    "/program/about/related-approaches/life-mind-self-organization/": "Autopoiesis, Free Energy, and Integrated Information",
    "/program/about/related-approaches/neutral-russellian-monism/": "Neutral Monism and Russellian Monism",
}

LOCKED_LANGUAGE = [
    "Related Approaches is not a takedown of other theories. It is a positioning map.",
    "Panta Rhei compares related approaches through its own standards: Core Semantics, Earned Language, Internal Standpoint, No Externalities, Construction Spine, and Verify.",
]

REQUIRED_CHILD_SECTIONS = [
    "What this approach tries to solve",
    "What Panta Rhei shares",
    "Where Panta Rhei differs",
    "Where to inspect next",
]

FORBIDDEN_VISIBLE_PATTERNS = [
    r"\bPanta Rhei refutes\b",
    r"\bis wrong\b",
    r"\bfailed\b",
    r"\bsupersedes\b",
    r"\bThis is just like\b",
    r"\bThis is not like\b.*\bat all\b",
    r"\bsmuggle in\b",
]


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


def forbid_patterns(text: str, route: str) -> None:
    for pattern in FORBIDDEN_VISIBLE_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            fail(f"{route} contains forbidden visible wording matching {pattern!r}")


def assert_one_h1(site: Path, route: str) -> tuple[str, str]:
    html, visible, parser = read_page(site, route)
    if len(parser.h1) != 1:
        fail(f"{route} should contain exactly one h1, found {len(parser.h1)}")
    return html, visible


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_related_approaches.py _site", file=sys.stderr)
        return 2

    site = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    hub_html, hub_visible = assert_one_h1(site, HUB)
    for needle in LOCKED_LANGUAGE:
        require(hub_visible, needle, HUB)
    require(hub_visible, "The comparison point is not who is right by assertion, but where each approach places the semantic and construction burden.", HUB)
    for route, title in CHILDREN.items():
        if f'href="{route}"' not in hub_html:
            fail(f"Hub missing child link to {route}")
    forbid_patterns(hub_visible, HUB)

    for route, title in CHILDREN.items():
        html, visible = assert_one_h1(site, route)
        require(visible, title, route)
        for section in REQUIRED_CHILD_SECTIONS:
            require(visible, section, route)
        if 'href="/program/' not in html:
            fail(f"{route} must include a Program or Agenda inspection link")
        if 'href="/corpus/' not in html:
            fail(f"{route} must include a Corpus inspection link")
        if 'href="/verify/' not in html:
            fail(f"{route} must include a Verify inspection link")
        if f'href="{HUB}"' not in html:
            fail(f"{route} must link back to the Related Approaches hub")
        forbid_patterns(visible, route)

    nav_source = read(repo / "_data" / "nav.yml")
    expected_nav = 'title: "Related Approaches"\n            url: "/program/about/related-approaches/"'
    if expected_nav not in nav_source:
        fail("Program/About nav must include Related Approaches")

    for route in [
        "/program/research-agenda/kernel-model-reality/related-approaches/",
        "/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/",
    ]:
        html, visible = assert_one_h1(site, route)
        if f'href="{HUB}"' not in html:
            fail(f"{route} must link to Program Related Approaches")
        require(visible, "Program Related Approaches", route)

    for route in [
        "/program/",
        "/program/about/",
        "/program/about/coherent-theory-of-reality/",
        "/program/about/inspection-observatory/",
        "/discover/",
        "/program/research-agenda/kernel-model-reality/",
        "/program/research-agenda/core-design-principles/",
        "/corpus/construction-spine/",
        "/media/",
        "/media/review-kit/",
    ]:
        html, _visible = assert_one_h1(site, route)
        if f'href="{HUB}"' not in html:
            fail(f"{route} must cross-link to Related Approaches")

    print("v4 Related Approaches assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
