#!/usr/bin/env python3
"""Assertions for the v4 post-launch fixes and polish sprint."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


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


def require_one_h1(site: Path, route: str) -> tuple[str, str]:
    html, visible, parser = read_page(site, route)
    if len(parser.h1) != 1:
        fail(f"{route} should contain exactly one h1, found {len(parser.h1)}")
    return html, visible


def meta_content(html: str, name_or_property: str) -> str:
    pattern = rf'<meta (?:name|property)="{re.escape(name_or_property)}" content="([^"]*)"'
    match = re.search(pattern, html)
    return match.group(1) if match else ""


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_fixes_1.py _site", file=sys.stderr)
        return 2

    site = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    # P0.1: Agenda compatibility route.
    agenda_redirect = read(html_path(site, "/agenda/"))
    require(agenda_redirect, 'content="0; url=/program/research-agenda/"', "/agenda/")
    require(agenda_redirect, 'rel="canonical" href="https://panta-rhei.site/program/research-agenda/"', "/agenda/")
    require(agenda_redirect, '<meta name="robots" content="noindex,follow">', "/agenda/")
    if "/agenda/" in read(site / "sitemap.xml"):
        fail("/agenda/ redirect must not be listed in sitemap.xml")
    worker_source = read(repo / "workers" / "site-edge-headers.js")
    require(worker_source, '["/agenda", "/program/research-agenda/"]', "workers/site-edge-headers.js")
    require(worker_source, '["/agenda/", "/program/research-agenda/"]', "workers/site-edge-headers.js")

    # P0.2/P1.8: doctrine pages load directly, are canonical, sitemap-visible, and tagged at source.
    sitemap = read(site / "sitemap.xml")
    for route, phrase in {
        "/program/about/coherent-theory-of-reality/": "Full doctrine",
        "/program/about/inspection-observatory/": "For journalists and reviewers",
    }.items():
        html, visible = require_one_h1(site, route)
        require(visible, phrase, route)
        require(html, f'rel="canonical" href="https://panta-rhei.site{route}"', route)
        require(sitemap, f"https://panta-rhei.site{route}", "sitemap.xml")

    coherent_source = read(repo / "program" / "about" / "coherent-theory-of-reality" / "index.md")
    observatory_source = read(repo / "program" / "about" / "inspection-observatory" / "index.md")
    for tag in ["coherent-theory-of-reality", "doctrine", "research-program"]:
        require(coherent_source, f"  - {tag}", "coherent doctrine source")
    for tag in ["inspection-observatory", "inspection-before-belief", "public-research-observatory"]:
        require(observatory_source, f"  - {tag}", "inspection observatory source")

    # P0.3: Results metadata and first summary are consequence-layer framed.
    results_html, results_visible = require_one_h1(site, "/results/")
    require(meta_content(results_html, "description"), "Where the built Corpus becomes a world", "/results/")
    require(meta_content(results_html, "og:description"), "Where the built Corpus becomes a world", "/results/")
    require(results_visible, "Results is where the built Corpus becomes a world.", "/results/")
    forbid(results_html, "What the program currently derives", "/results/")
    forbid(results_visible, "organized by domain. Mathematics, Physics, Life, Metaphysics", "/results/")

    # P1.1/P2.1: Agenda terminology and source-rule semantics.
    agenda_html, agenda_visible = require_one_h1(site, "/program/research-agenda/")
    require(agenda_visible, "The program asks whether a constrained kernel can support a coherent theory of reality.", "/program/research-agenda/")
    require(agenda_visible, "what formal shape an admissible theory of reality would need", "/program/research-agenda/")
    forbid(agenda_visible, "coherent kernel-based model of reality", "/program/research-agenda/")
    forbid(agenda_visible, "what formal shape a model would need", "/program/research-agenda/")
    require(agenda_html, '<table class="domain-ledger-rules">', "/program/research-agenda/")
    for heading in [
        '<th scope="col">Domain</th>',
        '<th scope="col">Ledger Rule</th>',
        '<th scope="col">Why Included</th>',
        '<th scope="row">Mathematics</th>',
        '<th scope="row">Physics</th>',
        '<th scope="row">Life</th>',
        '<th scope="row">Metaphysics / Philosophy</th>',
    ]:
        require(agenda_html, heading, "/program/research-agenda/")

    # P1.2/P1.3/P1.9: v4 spine wording and artifact visibility.
    _, program_visible = require_one_h1(site, "/program/")
    require(program_visible, "organized through the v4 public spine", "/program/")
    require(program_visible, "Discover, Program, Agenda, Corpus, Results, Verify, Impact, and Engage", "/program/")
    require(program_visible, "with Publications preserved as the stable artifact and release layer", "/program/")
    forbid(program_visible, "Program, Agenda, Corpus, Results, Verify, Publications, Impact, and Engage surfaces", "/program/")

    header_html = re.search(r"<nav class=\"header-nav\"[\s\S]*?</nav>", read(html_path(site, "/"))).group(0)
    if ">Publications</a>" in header_html:
        fail("Publications must not appear in top nav")
    _, home_visible = require_one_h1(site, "/")
    for needle in [
        "Artifacts & Releases",
        "Publications",
        "Research Monographs",
        "Research Papers",
        "Research Notes",
        "White Papers",
        "Release Artifacts",
        "Errata",
        "Cite",
    ]:
        require(home_visible, needle, "/")

    footer_source = read(repo / "_includes" / "footer.html")
    require(footer_source, "Infrastructure & Artifacts", "_includes/footer.html")
    require(footer_source, "{{ '/publications/' | relative_url }}", "_includes/footer.html")

    # P1.4/P1.5/P1.7: media/review first-contact narrative.
    _, media_visible = require_one_h1(site, "/media/")
    for needle in [
        "Suggested first story angle",
        "The first story is the inspection standard.",
        "If independent open research is allowed to ask large questions, what public burden should it accept before asking anyone to care?",
        "What journalists can responsibly say",
        "What should not be said without further review",
        "Possible headlines",
        "Coherent Theory of Reality",
        "Inspection Observatory",
    ]:
        require(media_visible, needle, "/media/")

    _, review_visible = require_one_h1(site, "/media/review-kit/")
    for needle in [
        "Start with the inspection architecture",
        "Program -> Agenda -> Corpus -> Results -> Verify",
        "First-pass reviewer checklist",
        "Are falsification or failure paths visible?",
        "Is there a route to ask questions or report errors?",
    ]:
        require(review_visible, needle, "/media/review-kit/")

    _, observatory_visible = require_one_h1(site, "/program/about/inspection-observatory/")
    for needle in [
        "For journalists and reviewers",
        "Media Kit",
        "Review Kit",
        "Inspection Architecture for High-Scope Open Research",
        "white paper, DOI forthcoming",
    ]:
        require(observatory_visible, needle, "/program/about/inspection-observatory/")

    # Pagefind indexes are binary; this confirms generation happened after
    # the doctrine pages were built and sitemap-visible.
    pagefind_dir = site / "pagefind"
    if not pagefind_dir.exists() or not list(pagefind_dir.glob("*.pf_meta")):
        fail("Pagefind output is missing; run Pagefind before this assertion")

    print("v4 fixes batch 1 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
