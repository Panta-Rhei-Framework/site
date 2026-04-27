#!/usr/bin/env python3
"""Assertions for Scientific Plate 08 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-08-conditional-impact-strata"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_03_OG = "/assets/images/plates/plate-03-public-obligation-layer-og.jpg"
PLATE_04_OG = "/assets/images/plates/plate-04-construction-spine-og.jpg"
PLATE_05_OG = "/assets/images/plates/plate-05-results-world-readout-og.jpg"
PLATE_06_OG = "/assets/images/plates/plate-06-verification-matrix-og.jpg"
PLATE_07_OG = "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
PLATE_08_OG = "/assets/images/plates/plate-08-conditional-impact-strata-og.jpg"
ALT = (
    "Scientific plate titled The Conditional Impact Strata, showing six stacked "
    "impact strata from Foundational Science to Global Public Good, a central "
    "conditional chain from Result to Verification Survival to Translation Layer "
    "to Domain Uptake to Consequence, and a Global Public-Good Portfolios inset."
)
CANONICAL_CAPTION = (
    "Impact is conditional: consequences become meaningful only if Results survive "
    "verification, translation, domain uptake, and real-world constraints. The six "
    "Impact strata range from foundational science to global public-good portfolios."
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
        self.skip_tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        if tag in {"script", "style", "noscript"}:
            self.skip += 1
            self.skip_tags.append(tag)
            return
        if "sr-only" in attr.get("class", "").split() or attr.get("aria-hidden") == "true":
            self.skip += 1
            self.skip_tags.append(tag)
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
        if self.skip_tags and self.skip_tags[-1] == tag and self.skip:
            self.skip -= 1
            self.skip_tags.pop()

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
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 08 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 08 WebP source")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-08-conditional-impact-strata-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-08-conditional-impact-strata-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-08-conditional-impact-strata-hero.jpg",
        "og": site / "assets/images/plates/plate-08-conditional-impact-strata-og.jpg",
        "thumb": site / "assets/images/plates/plate-08-conditional-impact-strata-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 08 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 08 asset too small to be valid: {path}")

    impact_targets = {
        "/impact/": [
            "The conditional consequence layer at a glance",
            "The Conditional Impact Strata",
            CANONICAL_CAPTION,
            "Consequence requires survival under scrutiny.",
            "Read the Impact Framework",
            "Explore Foundational Science",
            "Open Global Public Good",
            "Browse Public-Good Briefings",
        ],
        "/impact/impact-framework/": [
            "The impact chain",
            "The Impact Framework reads every consequence through the same chain",
            "A consequence becomes meaningful only when the relevant Result",
        ],
        "/impact/global-public-good/": [
            "Global Public Good inside the impact strata",
            "Global Public Good is the outermost Impact stratum",
            "conditional scenario maps, not deployment claims",
        ],
    }

    for route, required_text in impact_targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_08_OG}",
            f"{route} missing Plate 08 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_08_OG}",
            f"{route} missing Plate 08 twitter:image",
        )
        require(
            "Impact" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 08 OG alt text",
        )

    _, public_good = read_page(site, "/publications/research-briefings/public-good/")
    assert_plate_present("/publications/research-briefings/public-good/", public_good)
    for needle in [
        "Public-Good Briefings and conditional impact",
        "Public-Good Briefings belong to the outermost Impact stratum.",
        "not validation claims, policy commitments, or deployment plans",
        "They explore what could become valuable if upstream Results survive verification",
    ]:
        require(needle in public_good.visible, f"/publications/research-briefings/public-good/ missing expected text: {needle}")
    require(
        meta_content(public_good, "property", "og:image") == f"https://panta-rhei.site{PLATE_07_OG}",
        "/publications/research-briefings/public-good/ should keep Plate 07 Publications og:image",
    )

    boundary_ogs = {
        "/": PLATE_01_OG,
        "/discover/": PLATE_01_OG,
        "/program/research-agenda/": PLATE_03_OG,
        "/corpus/": PLATE_04_OG,
        "/results/": PLATE_05_OG,
        "/verify/": PLATE_06_OG,
        "/publications/": PLATE_07_OG,
    }
    for route, og_path in boundary_ogs.items():
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 08")
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{og_path}",
            f"{route} should keep its existing scoped og:image",
        )

    html, parser = read_page(site, "/engage/")
    require(parser.h1_count == 1, "/engage/ should have exactly one H1")
    require(PLATE_ID not in html, "/engage/ should not contain Plate 08")

    forbidden = [
        "Companion Papers",
        "public good papers",
        "deployment papers",
        "deployment portfolio",
        "Status: Resolved",
        "Resolved —",
    ]
    checked_routes = [*impact_targets.keys(), "/publications/research-briefings/public-good/", *boundary_ogs.keys(), "/engage/"]
    for route in checked_routes:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 08 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
