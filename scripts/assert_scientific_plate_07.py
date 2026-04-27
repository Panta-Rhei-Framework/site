#!/usr/bin/env python3
"""Assertions for Scientific Plate 07 integration."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path


PLATE_ID = "plate-07-stable-artifact-layer"
PLATE_01_OG = "/assets/images/plates/plate-01-public-research-observatory-og.jpg"
PLATE_03_OG = "/assets/images/plates/plate-03-public-obligation-layer-og.jpg"
PLATE_04_OG = "/assets/images/plates/plate-04-construction-spine-og.jpg"
PLATE_05_OG = "/assets/images/plates/plate-05-results-world-readout-og.jpg"
PLATE_06_OG = "/assets/images/plates/plate-06-verification-matrix-og.jpg"
PLATE_07_OG = "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
ALT = (
    "Scientific plate titled The Stable Artifact Layer, showing Publications at "
    "the center with seven publication categories, a Public-Good Briefings inset "
    "under Research Briefings, a classification decision band, and links to "
    "Corpus, Results, Verify, and Impact."
)
CANONICAL_CAPTION = (
    "Publications is the stable artifact layer of the program: a typed system "
    "of citable objects, including Research Monographs, Monograph Supplements, "
    "Research Papers, Research Notes, Research Briefings, White Papers, and "
    "Release Artifacts. Artifact type is not claim status."
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
    require(any(img.get("alt") == ALT for img in parser.imgs), f"{route} missing Plate 07 alt text")
    require(any(PLATE_ID in (source.get("srcset") or "") for source in parser.sources), f"{route} missing Plate 07 WebP source")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    assets = {
        "master": site / "assets/images/plates/plate-07-stable-artifact-layer-master.jpg",
        "hero_webp": site / "assets/images/plates/plate-07-stable-artifact-layer-hero.webp",
        "hero_jpg": site / "assets/images/plates/plate-07-stable-artifact-layer-hero.jpg",
        "og": site / "assets/images/plates/plate-07-stable-artifact-layer-og.jpg",
        "thumb": site / "assets/images/plates/plate-07-stable-artifact-layer-thumb.webp",
    }
    for label, path in assets.items():
        require(path.exists(), f"Missing Plate 07 asset {label}: {path}")
        require(path.stat().st_size > 10_000, f"Plate 07 asset too small to be valid: {path}")

    targets = {
        "/publications/": [
            "The artifact taxonomy at a glance",
            "The Stable Artifact Layer",
            CANONICAL_CAPTION,
            "Artifact type is not claim status.",
            "Browse Research Monographs",
            "Open Monograph Supplements",
            "Read Research Notes",
            "Explore Research Briefings",
        ],
        "/publications/research-briefings/": [
            "Research Briefings inside the publication taxonomy",
            "Research Briefings are one publication category inside the larger stable artifact layer.",
            "They do not primarily introduce new technical research claims",
        ],
        "/publications/research-briefings/public-good/": [
            "Public-Good Briefings as Research Briefings",
            "Public-Good Briefings are a family of Research Briefings: conditional scenario briefings",
            "not validation claims or deployment plans",
        ],
        "/publications/research-notes/": [
            "Research Notes inside the publication taxonomy",
            "Research Notes are shorter scholarly artifacts in the ongoing research stream",
            "distinct from Research Papers, Research Briefings, and White Papers",
        ],
        "/publications/monograph-supplements/": [
            "Monograph Supplements inside the publication taxonomy",
            "Monograph Supplements are book-style extensions, appendices, ledgers, or supporting parts",
            "Their category says how the artifact should be read",
        ],
        "/publications/white-papers/": [
            "White Papers inside the publication taxonomy",
            "White Papers are explanatory artifacts in the stable publication layer",
            "without primarily carrying new original research claims",
        ],
        "/publications/release-artifacts/": [
            "Release Artifacts inside the publication taxonomy",
            "Release Artifacts document version state, provenance, corrections, manifests, changelogs",
            "They are governance and provenance artifacts, not primary research claims",
        ],
    }

    for route, required_text in targets.items():
        _, parser = read_page(site, route)
        assert_plate_present(route, parser)
        for needle in required_text:
            require(needle in parser.visible, f"{route} missing expected text: {needle}")
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{PLATE_07_OG}",
            f"{route} missing Plate 07 og:image",
        )
        require(
            meta_content(parser, "name", "twitter:image") == f"https://panta-rhei.site{PLATE_07_OG}",
            f"{route} missing Plate 07 twitter:image",
        )
        require(
            "Publications" in (meta_content(parser, "property", "og:image:alt") or ""),
            f"{route} missing Plate 07 OG alt text",
        )

    boundary_ogs = {
        "/": PLATE_01_OG,
        "/discover/": PLATE_01_OG,
        "/program/research-agenda/": PLATE_03_OG,
        "/corpus/": PLATE_04_OG,
        "/results/": PLATE_05_OG,
        "/verify/": PLATE_06_OG,
    }
    for route, og_path in boundary_ogs.items():
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 07")
        require(
            meta_content(parser, "property", "og:image") == f"https://panta-rhei.site{og_path}",
            f"{route} should keep its existing scoped og:image",
        )

    for route in ["/impact/", "/engage/"]:
        html, parser = read_page(site, route)
        require(parser.h1_count == 1, f"{route} should have exactly one H1")
        require(PLATE_ID not in html, f"{route} should not contain Plate 07")

    forbidden = [
        "Companion Papers",
        "public good papers",
        "deployment papers",
        "deployment portfolio",
        "Status: Resolved",
        "Resolved —",
    ]
    for route in [*targets.keys(), "/", "/discover/", "/results/", "/verify/", "/impact/", "/engage/"]:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plate 07 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
