#!/usr/bin/env python3
"""Assertions for Scientific Plate 02 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-02-from-obligation-to-inspection"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_02_OG = "/assets/images/plates/plate-02-from-obligation-to-inspection-og.jpg"
ALT = (
    "Scientific plate titled From Obligation to Inspection, showing the Panta Rhei accountability "
    "chain from Research Agenda to Corpus to Results to Verify, with corresponding stages of "
    "obligation, construction, consequence, and inspection."
)
CANONICAL_CAPTION = (
    "Panta Rhei asks to be read through a public chain of accountability: Research Agenda states "
    "the obligations, Corpus carries the construction, Results reports what follows, and Verify "
    "exposes how claims can be inspected, challenged, and tested."
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
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 02 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 02 WebP source")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-02-from-obligation-to-inspection-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-02-from-obligation-to-inspection-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-02-from-obligation-to-inspection-hero.jpg",
        "og": site / "assets/images/plates/plate-02-from-obligation-to-inspection-og.jpg",
        "thumb": site / "assets/images/plates/plate-02-from-obligation-to-inspection-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 02 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 02 asset too small to be valid: {path}")

    targets = {
        "/program/research-agenda/": [
            "From obligation to inspection",
            CANONICAL_CAPTION,
            "The Research Agenda is the obligation layer.",
            "Read the Research Agenda",
            "Follow the Construction Spine",
            "See Progress Against Agenda",
            "Verify the Construction Spine",
        ],
        "/discover/": [
            "How to evaluate the program",
            "The core reading chain of the site: obligations are stated before construction, construction supports results, and results remain open to inspection.",
            "Use this chain to read the site: obligations first, construction second, consequences third, inspection always.",
        ],
        "/verify/": [
            "Follow the chain before checking the claim",
            "Verification begins before a claim is checked: the obligation must be visible, the construction must be traceable, and the result must have an inspection route.",
            "Verification begins with traceability",
        ],
    }

    for route, required_text in targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")

    for route in ["/verify/"]:
        _, parser = read_page(site, route)
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_02_OG}",
            f"{route} missing Plate 02 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_02_OG}",
            f"{route} missing Plate 02 twitter:image",
        )
        require(
            "Scientific plate showing the Panta Rhei accountability chain" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 02 OG alt text",
        )

    _, discover = read_page(site, "/discover/")
    require(
        meta_content(discover, "property", "og:image") == f"https://panta-rhei.site{PLATE_01_OG}",
        "/discover/ should keep Plate 01 og:image",
    )

    for route in ["/", "/results/"]:
        page_html, parser = read_page(site, route)
        require(PLATE_ID not in page_html, f"{route} should not contain Plate 02")
        require(parser.h1_count == 1, f"{route} should have exactly one H1")

    forbidden = ["Companion Papers", "deployment portfolios", "Status: Resolved", "Resolved —"]
    for route in [*targets.keys(), "/", "/results/"]:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 02 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
