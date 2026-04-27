#!/usr/bin/env python3
"""Assertions for Scientific Plate 09 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-09-engagement-without-endorsement"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_03_OG = "/assets/images/plates/plate-03-public-obligation-layer-og.jpg"
PLATE_04_OG = "/assets/images/plates/plate-04-construction-spine-og.jpg"
PLATE_05_OG = "/assets/images/plates/plate-05-results-world-readout-og.jpg"
PLATE_06_OG = "/assets/images/plates/plate-06-verification-matrix-og.jpg"
PLATE_07_OG = "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
PLATE_08_OG = "/assets/images/plates/plate-08-conditional-impact-strata-og.jpg"
PLATE_09_OG = "/assets/images/plates/plate-09-engagement-without-endorsement-og.jpg"
ALT = (
    "Scientific plate titled Engagement Without Endorsement, showing Engage at the center "
    "with eight engagement modes, routing through the website, GitHub Discussions, "
    "GitHub Issues, Pull Requests, and email, plus open-research principles and the caveat "
    "that participation does not imply endorsement."
)
CANONICAL_CAPTION = (
    "Engage is the open-research participation interface of the program: readers can "
    "read carefully, inspect claims, challenge weak links, review bounded areas, "
    "contribute infrastructure, communicate responsibly, open institutional dialogue, "
    "or support continuation without implying endorsement."
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
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 09 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 09 WebP source")


def assert_plate_og(route: str, parser: Parser) -> None:
    require(
        meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_09_OG}",
        f"{route} missing Plate 09 og:image",
    )
    require(
        meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_09_OG}",
        f"{route} missing Plate 09 twitter:image",
    )
    require(
        "Engage lane" in (meta_content(parser, "property", "og:image:alt") or ""),
        f"{route} missing Plate 09 OG alt text",
    )


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-09-engagement-without-endorsement-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-09-engagement-without-endorsement-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-09-engagement-without-endorsement-hero.jpg",
        "og": site / "assets/images/plates/plate-09-engagement-without-endorsement-og.jpg",
        "thumb": site / "assets/images/plates/plate-09-engagement-without-endorsement-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 09 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 09 asset too small to be valid: {path}")

    engage_targets = {
        "/engage/": [
            "The participation interface at a glance",
            "Engagement Without Endorsement",
            CANONICAL_CAPTION,
            "Open Public Discussions",
            "Learn How to Engage",
            "Review the Work",
            "Contact the Program",
        ],
        "/engage/how-to-engage/": [
            "Choose the kind of attention you can offer",
            "Engagement does not begin with agreement.",
            "The Engage lane separates attention modes from endorsement",
            "without being asked to agree first",
        ],
        "/engage/discussions/": [
            "Where public engagement lives",
            "Public questions, critique, review offers, and correction candidates belong in GitHub Discussions where possible.",
            "Concrete defects belong in Issues",
            "Pull Requests are for proposed changes",
            "email remains for private or institutional contact",
        ],
        "/engage/review-the-work/": [
            "Bounded review as structured attention",
            "A useful review is bounded: it names the page, artifact, result, note, proof route, or formalization surface being inspected.",
            "Review is one form of structured attention",
        ],
        "/engage/for-engineering-contributors/": [
            "Infrastructure contribution",
            "Contributing infrastructure can mean improving documentation, metadata, tooling, templates, search, formalization support, or source structure.",
            "Contribution does not imply endorsement.",
        ],
    }

    for route, required_text in engage_targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        assert_plate_og(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")

    boundary_ogs = {
        "/": PLATE_01_OG,
        "/discover/": PLATE_01_OG,
        "/program/research-agenda/": PLATE_03_OG,
        "/corpus/": PLATE_04_OG,
        "/results/": PLATE_05_OG,
        "/verify/": PLATE_06_OG,
        "/publications/": PLATE_07_OG,
        "/impact/": PLATE_08_OG,
    }
    for route, og_path in boundary_ogs.items():
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 09")
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{og_path}",
            f"{route} should keep its existing scoped og:image",
        )

    forbidden = [
        "Companion Papers",
        "public good papers",
        "deployment papers",
        "deployment portfolio",
        "Status: Resolved",
        "Resolved —",
        "fan community",
        "campaign",
    ]
    checked_routes = [*engage_targets.keys(), *boundary_ogs.keys()]
    for route in checked_routes:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 09 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
