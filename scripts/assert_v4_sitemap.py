#!/usr/bin/env python3
"""Assertions for the v4 human-readable sitemap."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse


PRIMARY_LANES = [
    "discover",
    "program",
    "agenda",
    "corpus",
    "results",
    "verify",
    "impact",
    "engage",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def strip_tags(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def route_exists(site_root: Path, href: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith("mailto:"):
        return True
    path = parsed.path
    if path == "/sitemap.xml":
        return (site_root / "sitemap.xml").is_file()
    if path == "/":
        return (site_root / "index.html").is_file()
    normalized = path.lstrip("/")
    return (
        (site_root / normalized).is_file()
        or (site_root / normalized / "index.html").is_file()
        or (site_root / f"{normalized}.html").is_file()
    )


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: assert_v4_sitemap.py <built-site-root>")
    site_root = Path(sys.argv[1]).resolve()
    sitemap_path = site_root / "sitemap" / "index.html"
    if not sitemap_path.is_file():
        fail(f"missing built sitemap at {sitemap_path}")

    html = sitemap_path.read_text(encoding="utf-8")
    visible = strip_tags(html)

    if visible.count("Sitemap") < 1:
        fail("sitemap title is not visible")
    if len(re.findall(r"<h1\b", html, flags=re.I)) != 1:
        fail("sitemap must render exactly one h1")
    if "Core lanes" in visible:
        fail("stale 'Core lanes' copy remains visible")
    if "Human-readable map of the Panta Rhei public research observatory" not in visible:
        fail("locked v4 sitemap intro is missing")
    if "Where the built Corpus becomes a world" not in visible:
        fail("Results card does not use the v4 built-Corpus-becomes-a-world description")
    if "/sitemap.xml" not in html:
        fail("machine-readable /sitemap.xml link is missing")
    if "sitemap-chip" in html:
        fail("sitemap still renders pill/chip link classes instead of mini-card tiles")
    if "sitemap-link-grid" not in html or "sitemap-mini-card" not in html:
        fail("sitemap mini-card grid classes are missing")

    card_lanes = re.findall(r'data-sitemap-lane="([^"]+)"', html)
    for lane in PRIMARY_LANES:
        if card_lanes.count(lane) != 1:
            fail(f"expected exactly one primary {lane} card")
    if card_lanes.count("support") != 1:
        fail("expected exactly one support card")
    if "publications" in card_lanes:
        fail("Publications must not render as a primary sitemap lane")

    primary_match = re.search(
        r'<section class="sitemap-section"[^>]*aria-labelledby="sitemap-primary-lanes-heading".*?</section>',
        html,
        flags=re.S,
    )
    if not primary_match:
        fail("primary lanes section is missing")
    primary_html = primary_match.group(0)
    if "Agenda" not in strip_tags(primary_html):
        fail("Agenda is missing from primary lanes")
    if re.search(r"<h3>\s*Publications\s*</h3>", primary_html):
        fail("Publications appears as a primary lane heading")

    for lane in PRIMARY_LANES:
        card_match = re.search(
            rf'<article class="sitemap-card sitemap-card-primary" data-sitemap-lane="{lane}".*?</article>',
            html,
            flags=re.S,
        )
        if not card_match:
            fail(f"{lane} card markup missing")
        card_html = card_match.group(0)
        if 'class="sitemap-card-cta"' not in card_html:
            fail(f"{lane} card has no root CTA")
        if 'class="sitemap-link-grid"' not in card_html:
            fail(f"{lane} card does not use the mini-card link grid")
        if len(re.findall(r'class="sitemap-mini-card"', card_html)) < 4:
            fail(f"{lane} card does not expose useful second-level links")
        if re.search(r'<li class="sitemap-mini-card">\s*<a href="[^"]+">\s*<span>[^<]+</span>\s*</a>\s*</li>', card_html) is None:
            fail(f"{lane} card mini-card links must render as li > a > span")

    support_match = re.search(
        r'<article class="sitemap-card sitemap-card-support" data-sitemap-lane="support".*?</article>',
        html,
        flags=re.S,
    )
    if not support_match:
        fail("support card markup missing")
    support_text = strip_tags(support_match.group(0))
    if "Support layer" not in support_text:
        fail("support card eyebrow should read 'Support layer'")
    for required in ["Publications", "Release Artifacts", "Errata", "Media Kit", "XML Sitemap"]:
        if required not in support_text:
            fail(f"support card missing {required}")

    hrefs = re.findall(r'href="([^"]+)"', html)
    missing = sorted({
        href
        for href in hrefs
        if href.startswith("/")
        and not href.startswith(("/assets/", "/pagefind/"))
        and not route_exists(site_root, href)
    })
    if missing:
        fail("sitemap links do not resolve in built site: " + ", ".join(missing[:20]))

    print("v4 sitemap assertions passed")


if __name__ == "__main__":
    main()
