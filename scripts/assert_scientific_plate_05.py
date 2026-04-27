#!/usr/bin/env python3
"""Assertions for Scientific Plate 05 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-05-results-world-readout"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_05_OG = "/assets/images/plates/plate-05-results-world-readout-og.jpg"
ALT = (
    "Scientific plate titled The Results World Readout, showing Results at the center "
    "with six surrounding result surfaces, four world readouts for mathematics, physics, "
    "life, and metaphysics, a status legend, and a route from results to inspection."
)
CANONICAL_CAPTION = (
    "Results are not isolated claims. They are consequences of the built Corpus, "
    "organized through Landmark Results, World Readouts, Problem Ledger Answers, "
    "Recovery Target Status, Additional Derived Results, and Progress Against Agenda, "
    "with internal status labels separated from external acceptance."
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
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 05 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 05 WebP source")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-05-results-world-readout-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-05-results-world-readout-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-05-results-world-readout-hero.jpg",
        "og": site / "assets/images/plates/plate-05-results-world-readout-og.jpg",
        "thumb": site / "assets/images/plates/plate-05-results-world-readout-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 05 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 05 asset too small to be valid: {path}")

    targets = {
        "/results/": [
            "The consequence layer at a glance",
            "The Results World Readout",
            CANONICAL_CAPTION,
            "Results are not isolated claims. They are consequences of the built Corpus, organized through status-marked result surfaces and routed toward inspection.",
            "Explore Landmark Results",
            "Open World Readouts",
            "Read Problem Ledger Answers",
            "Track Progress Against Agenda",
        ],
        "/results/world-readout/": [
            "World readouts inside the Results layer",
            "The World Readouts are one Results surface within a larger status-marked consequence layer.",
            "Mathematics, physics, life, and metaphysics are read as world-level consequence surfaces within the broader Results architecture.",
        ],
        "/results/progress-against-agenda/": [
            "Progress as a Results surface",
            "Progress Against Agenda is one of the Results surfaces: a dashboard over obligations, recovery targets, and current program stance.",
            "Progress Against Agenda tracks current program stance against public obligations and recovery targets.",
        ],
    }

    for route, required_text in targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")

    for route in ["/results/", "/results/world-readout/"]:
        _, parser = read_page(site, route)
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_05_OG}",
            f"{route} missing Plate 05 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_05_OG}",
            f"{route} missing Plate 05 twitter:image",
        )
        require(
            "Results lane as a status-marked consequence layer" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 05 OG alt text",
        )

    _, discover = read_page(site, "/discover/")
    require(
        meta_content(discover, "property", "og:image") == f"https://panta-rhei.site{PLATE_01_OG}",
        "/discover/ should keep Plate 01 og:image",
    )

    for route in ["/", "/discover/", "/program/research-agenda/", "/corpus/", "/verify/"]:
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 05")

    forbidden = ["Companion Papers", "deployment portfolios", "Status: Resolved", "Resolved —", "Resolved"]
    for route in [*targets.keys()]:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 05 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
