#!/usr/bin/env python3
"""Assertions for Scientific Plate 03 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-03-public-obligation-layer"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_03_OG = "/assets/images/plates/plate-03-public-obligation-layer-og.jpg"
ALT = (
    "Scientific plate titled The Public Obligation Layer, showing the Research Agenda "
    "as a public research contract connected to four surfaces: Problem Ledger, "
    "Recovery Requirements, Kernel, Model & Reality, and Construction Roadmap."
)
CANONICAL_CAPTION = (
    "The Research Agenda is the program's public obligation layer: it records "
    "the open problems, recovery requirements, answer-shape burden, and "
    "construction order that must be stated before Results are read as consequences."
)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1_count = 0
        self.imgs: list[dict[str, str]] = []
        self.sources: list[dict[str, str]] = []
        self.metas: list[dict[str, str]] = []
        self.text: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            return
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.imgs.append(attr)
        if tag == "source":
            self.sources.append(attr)
        if tag == "meta":
            self.metas.append(attr)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip:
            self.text.append(data)

    @property
    def visible(self) -> str:
        return " ".join(" ".join(self.text).split())


def read_page(site: Path, route: str) -> tuple[str, Parser]:
    path = site / route.strip("/") / "index.html"
    if route == "/":
        path = site / "index.html"
    if not path.exists():
        raise AssertionError(f"Missing page: {route}")
    html = path.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)
    return html, parser


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def meta_content(parser: Parser, key: str, value: str) -> str | None:
    for meta in parser.metas:
        if meta.get(key) == value:
            return meta.get("content")
    return None


def assert_plate_present(route: str, parser: Parser) -> None:
    require(parser.h1_count == 1, f"{route} should have exactly one H1")
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 03 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 03 WebP source")


def assert_before(text: str, first: str, second: str, route: str) -> None:
    left = text.find(first)
    right = text.find(second)
    require(left >= 0, f"{route} missing expected text: {first}")
    require(right >= 0, f"{route} missing expected text: {second}")
    require(left < right, f"{route} expected '{first}' before '{second}'")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-03-public-obligation-layer-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-03-public-obligation-layer-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-03-public-obligation-layer-hero.jpg",
        "og": site / "assets/images/plates/plate-03-public-obligation-layer-og.jpg",
        "thumb": site / "assets/images/plates/plate-03-public-obligation-layer-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 03 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 03 asset too small to be valid: {path}")

    targets = {
        "/program/research-agenda/": [
            "The obligation layer at a glance",
            "The public obligation layer",
            CANONICAL_CAPTION,
            "It states what the program accepts as a burden before Results are allowed to sound like consequences.",
            "Open the Problem Ledger",
            "Read Recovery Requirements",
            "Explore Kernel, Model & Reality",
            "Follow the Construction Roadmap",
        ],
        "/discover/": [
            "Before Results, there is obligation",
            "Before Results, there is obligation: the Research Agenda records the external problems",
            "The Research Agenda states the burden: what must be kept visible",
        ],
    }

    for route, required_text in targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")

    _, agenda = read_page(site, "/program/research-agenda/")
    assert_before(agenda.visible, "The public obligation layer", "How to read this page", "/program/research-agenda/")
    assert_before(agenda.visible, "The four agenda surfaces", "The public obligation layer", "/program/research-agenda/")

    for route in ["/program/research-agenda/", "/program/"]:
        _, parser = read_page(site, route)
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_03_OG}",
            f"{route} missing Plate 03 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_03_OG}",
            f"{route} missing Plate 03 twitter:image",
        )
        require(
            "Research Agenda as the public obligation layer" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 03 OG alt text",
        )

    _, discover = read_page(site, "/discover/")
    require(
        meta_content(discover, "property", "og:image") == f"https://panta-rhei.site{PLATE_01_OG}",
        "/discover/ should keep Plate 01 og:image",
    )

    home_html, home = read_page(site, "/")
    require(PLATE_ID not in home_html, "/ should not contain Plate 03")
    require(home.h1_count == 1, "/ should have exactly one H1")

    for route in ["/results/", "/verify/"]:
        html, _ = read_page(site, route)
        require(PLATE_ID not in html, f"{route} should not contain Plate 03")

    forbidden = ["Companion Papers", "deployment portfolios", "Status: Resolved", "Resolved —"]
    for route in [*targets.keys(), "/", "/results/", "/verify/"]:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 03 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
