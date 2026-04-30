#!/usr/bin/env python3
"""Assertions for Scientific Plates 10-15 integration."""

from __future__ import annotations

import struct
import sys
from html.parser import HTMLParser
from pathlib import Path


SITE_URL = "https://panta-rhei.site"

PLATES = {
    "plate-10-tau-kernel": {
        "title": "The τ-Kernel",
        "alt": (
            "Scientific plate titled The τ-Kernel, showing five generators, one primitive "
            "iterator, a central τ-Kernel block, K0–K6 axiomatic constraints, constructive "
            "closure, and boundary notes for no hidden runtime and no hidden substrate."
        ),
        "routes": ["/corpus/", "/corpus/construction-spine/"],
    },
    "plate-11-four-layer-world": {
        "title": "The Four-Layer World",
        "alt": (
            "Scientific plate titled The Four-Layer World, showing E0 Mathematics, "
            "E1 Physics, E2 Life, and E3 Metaphysics / Reflection as self-enrichment "
            "layers rising from the τ-Kernel construction base."
        ),
        "routes": ["/results/world-readout/"],
        "og_routes": ["/results/world-readout/"],
    },
    "plate-12-self-enrichment-not-reduction": {
        "title": "Self-Enrichment, Not Reduction",
        "alt": (
            "Scientific plate titled Self-Enrichment, Not Reduction, comparing reduction, "
            "self-enrichment, and dualism, with self-enrichment shown as a generated layer "
            "carrying new relational grammar without adding a second world."
        ),
        "routes": ["/impact/foundational-science/", "/program/research-agenda/kernel-model-reality/"],
        "og_routes": ["/impact/foundational-science/"],
    },
    "plate-13-kernel-to-measurement": {
        "title": "From Kernel to Measurement",
        "alt": (
            "Scientific plate titled From Kernel to Measurement, showing a chain from "
            "Kernel through Physical Carrier, Physical Grammar, Constants and Invariants, "
            "Measurement Bridge, SI Observables, Predictions, and Falsification, plus a "
            "calibration cascade and the caveat that formal construction is not measurement."
        ),
        "routes": ["/verify/predictions-and-falsification/", "/results/world-readout/physics/"],
        "og_routes": ["/verify/predictions-and-falsification/"],
    },
    "plate-14-ontic-closure-burden": {
        "title": "The Ontic Closure Burden",
        "alt": (
            "Scientific plate titled The Ontic Closure Burden, showing a no-externalities "
            "boundary with rejected hidden runtime, hidden substrate, hidden semantic load, "
            "and residual boundary by silence, plus allowed treatments such as internalized, "
            "derived, typed, factored out, bridged, or marked unresolved."
        ),
        "routes": ["/program/research-agenda/kernel-model-reality/no-externalities/"],
        "og_routes": ["/program/research-agenda/kernel-model-reality/no-externalities/"],
    },
    "plate-15-bi-square-spine": {
        "title": "The Bi-Square Spine",
        "alt": (
            "Scientific plate titled The Bi-Square Spine, showing a two-by-three pasted "
            "diagram with tower coherence on the left, spectral naturality on the right, "
            "and a pasting constraint across the whole rectangle, followed by a scaling "
            "chain from algebraic to geometric, enriched, and computational bi-squares."
        ),
        "routes": ["/corpus/bi-square/", "/corpus/"],
        "og_routes": ["/corpus/bi-square/"],
    },
}

ASSETS = {
    "master.jpg": (1672, 941),
    "hero.webp": (1536, 864),
    "hero.jpg": (1536, 864),
    "og.jpg": (1200, 630),
    "thumb.webp": (640, 360),
}


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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_page(site: Path, route: str) -> tuple[str, Parser]:
    path = site / route.strip("/") / "index.html"
    if route == "/":
        path = site / "index.html"
    require(path.exists(), f"Missing page: {route}")
    html = path.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)
    return html, parser


def meta_content(parser: Parser, key: str, value: str) -> str | None:
    for meta in parser.metas:
        if meta.get(key) == value:
            return meta.get("content")
    return None


def jpeg_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    require(data[:2] == b"\xff\xd8", f"Not a JPEG: {path}")
    i = 2
    while i < len(data):
        while i < len(data) and data[i] == 0xFF:
            i += 1
        marker = data[i]
        i += 1
        if marker in {0xD8, 0xD9}:
            continue
        length = struct.unpack(">H", data[i : i + 2])[0]
        if 0xC0 <= marker <= 0xC3:
            height = struct.unpack(">H", data[i + 3 : i + 5])[0]
            width = struct.unpack(">H", data[i + 5 : i + 7])[0]
            return width, height
        i += length
    raise AssertionError(f"No JPEG size marker found: {path}")


def uint24le(data: bytes) -> int:
    return data[0] | (data[1] << 8) | (data[2] << 16)


def webp_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    require(data[:4] == b"RIFF" and data[8:12] == b"WEBP", f"Not a WebP: {path}")
    i = 12
    while i + 8 <= len(data):
        chunk = data[i : i + 4]
        size = struct.unpack("<I", data[i + 4 : i + 8])[0]
        payload = i + 8
        if chunk == b"VP8X":
            width = uint24le(data[payload + 4 : payload + 7]) + 1
            height = uint24le(data[payload + 7 : payload + 10]) + 1
            return width, height
        if chunk == b"VP8L":
            bits = struct.unpack("<I", data[payload + 1 : payload + 5])[0]
            width = (bits & 0x3FFF) + 1
            height = ((bits >> 14) & 0x3FFF) + 1
            return width, height
        if chunk == b"VP8 ":
            require(data[payload + 3 : payload + 6] == b"\x9d\x01\x2a", f"Invalid VP8 frame: {path}")
            width = struct.unpack("<H", data[payload + 6 : payload + 8])[0] & 0x3FFF
            height = struct.unpack("<H", data[payload + 8 : payload + 10])[0] & 0x3FFF
            return width, height
        i += 8 + size + (size % 2)
    raise AssertionError(f"No WebP size marker found: {path}")


def image_size(path: Path) -> tuple[int, int]:
    if path.suffix == ".jpg":
        return jpeg_size(path)
    if path.suffix == ".webp":
        return webp_size(path)
    raise AssertionError(f"Unsupported image type: {path}")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")

    for slug, meta in PLATES.items():
        for suffix, expected_size in ASSETS.items():
            path = site / "assets/images/plates" / f"{slug}-{suffix}"
            require(path.exists(), f"Missing asset: {path}")
            require(path.stat().st_size > 10_000, f"Asset too small to be valid: {path}")
            require(image_size(path) == expected_size, f"{path} has size {image_size(path)}, expected {expected_size}")

        for route in meta["routes"]:
            html, parser = read_page(site, route)
            require(parser.h1_count == 1, f"{route} should have exactly one H1")
            require(any(img.get("alt") == meta["alt"] for img in parser.imgs), f"{route} missing alt text for {slug}")
            require(any(slug in (source.get("srcset") or "") for source in parser.sources), f"{route} missing WebP source for {slug}")
            require("formal construction is not measurement" in html or slug != "plate-13-kernel-to-measurement", f"{route} missing Plate 13 measurement caveat")
            require("Visual elegance is evidence of truth" not in parser.visible, f"{route} implies visual evidence of truth")

        for route in meta.get("og_routes", []):
            _, parser = read_page(site, route)
            expected = f"{SITE_URL}/assets/images/plates/{slug}-og.jpg"
            require(meta_content(parser, "property", "og:image") == expected, f"{route} missing scoped og:image for {slug}")
            require(meta_content(parser, "name", "twitter:image") == expected, f"{route} missing scoped twitter:image for {slug}")

    _, home = read_page(site, "/")
    require(
        meta_content(home, "property", "og:image") == f"{SITE_URL}/assets/images/plates/plate-01-public-research-observatory-og.jpg",
        "Homepage should keep Plate 01 as scoped OG image",
    )

    forbidden = [
        "Companion Papers",
        "deployment portfolios",
        "deployment papers",
        "Status: Resolved",
        "Resolved —",
    ]
    checked_routes = sorted({route for meta in PLATES.values() for route in meta["routes"]})
    for route in checked_routes:
        _, parser = read_page(site, route)
        for phrase in forbidden:
            require(phrase not in parser.visible, f"{route} contains forbidden visible phrase: {phrase}")

    print("Scientific Plates 10-15 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
