#!/usr/bin/env python3
"""Assertions for removing the standalone Review Kit surface."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class VisibleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.hidden = 0
        self.text: list[str] = []
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        classes = set(attr.get("class", "").split())
        if tag.lower() in {"head", "script", "style", "svg", "noscript"}:
            self.skip += 1
            return
        if "sr-only" in classes or attr.get("hidden") == "hidden" or attr.get("aria-hidden") == "true":
            self.hidden += 1
            return
        if not self.skip and not self.hidden and tag.lower() == "h1":
            self.h1_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"head", "script", "style", "svg", "noscript"} and self.skip:
            self.skip -= 1
            return
        if self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip and not self.hidden:
            self.text.append(data)

    @property
    def visible(self) -> str:
        return " ".join(" ".join(self.text).replace("\xa0", " ").split())


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing expected file: {path}")
    return path.read_text(encoding="utf-8", errors="ignore")


def page(site: Path, route: str) -> Path:
    return site / "index.html" if route == "/" else site / route.strip("/") / "index.html"


def parse(path: Path) -> tuple[str, str, int]:
    html = read(path)
    parser = VisibleParser()
    parser.feed(html)
    return html, parser.visible, parser.h1_count


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        fail(f"{label} missing expected text: {needle}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        fail(f"{label} contains forbidden text: {needle}")


def assert_one_h1(site: Path, route: str) -> str:
    _html, visible, h1_count = parse(page(site, route))
    if h1_count != 1:
        fail(f"{route} should have exactly one H1, found {h1_count}")
    return visible


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_reviewkit_removal.py _site", file=sys.stderr)
        return 2

    site = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    removed_page = site / "media" / "review-kit" / "index.html"
    if removed_page.exists():
        fail("/media/review-kit/ should not be generated")

    for html_path in site.rglob("*.html"):
        html, visible, _h1_count = parse(html_path)
        label = str(html_path.relative_to(site))
        forbid(html, "/media/review-kit/", label)
        forbid(visible, "Review Kit", label)
        forbid(visible, "Media & Review", label)

    for source_path in [
        repo / "_includes" / "footer.html",
        repo / "_data" / "nav.yml",
        repo / "_data" / "sitemap_v4.yml",
        repo / "media" / "index.md",
        repo / "media" / "journalist-faq.md",
        repo / "engage" / "media.md",
        repo / "engage" / "contact.md",
    ]:
        source = read(source_path)
        forbid(source, "/media/review-kit/", str(source_path.relative_to(repo)))
        forbid(source, "Media & Review", str(source_path.relative_to(repo)))

    media = assert_one_h1(site, "/media/")
    for needle in [
        "How to Verify",
        "Assessment Protocols",
        "Review the Work",
        "Panta Rhei is not reviewed through one standalone kit.",
        "Structured review / technical inspection",
    ]:
        require(media, needle, "/media/")

    how_to = assert_one_h1(site, "/verify/how-to-verify/")
    for needle in [
        "Start with the inspection architecture",
        "Program -> Agenda -> Corpus -> Results -> Verify",
        "First-pass inspection checklist",
        "Is the scope and burden of proof explicit?",
        "Are the Problem Ledger and source-policy rules visible?",
        "Are Core Semantics and answer-shape obligations stated separately from open problems?",
        "Is there a Construction Roadmap / Construction Spine?",
        "Is there a Corpus with stable IDs and dependency routes?",
        "Is there a formalization surface, and are its limits stated?",
        "Are Results status-marked?",
        "Are bridge claims explicit?",
        "Are falsification or failure paths visible?",
        "Are errata and correction routes public?",
        "Are remaining externalities disclosed?",
        "Is there a route to ask questions or report errors?",
        "Life-facing results",
        "Metaphysics / Philosophy-facing results",
    ]:
        require(how_to, needle, "/verify/how-to-verify/")

    protocols = assert_one_h1(site, "/verify/assessment-protocols/")
    for needle in [
        "Package inspection checklists",
        "Package 1 — Inspection Architecture",
        "Package 2 — Theory of Reality",
        "Package 3 — Public Research Observatory",
        "Assessment protocols are triage and review tools, not substitutes for proof, empirical testing, peer review, or external acceptance.",
        "Inspection Architecture for High-Scope Open Research",
        "The Shape of a Theory of Reality",
        "Building a Public Research Observatory for High-Scope Open Research",
    ]:
        require(protocols, needle, "/verify/assessment-protocols/")

    review = assert_one_h1(site, "/engage/review-the-work/")
    for needle in [
        "Review without endorsement",
        "Review routes moved into Verify",
        "Participation does not imply endorsement.",
        "How to Verify",
        "Assessment Protocols",
        "Core Semantics / Recovery item",
    ]:
        require(review, needle, "/engage/review-the-work/")

    contact = assert_one_h1(site, "/engage/contact/")
    require(contact, "Structured Review / Technical Inspection", "/engage/contact/")
    require(contact, "review@panta-rhei.site", "/engage/contact/")

    sitemap_xml = read(site / "sitemap.xml")
    forbid(sitemap_xml, "/media/review-kit/", "sitemap.xml")

    print("v4 Review Kit removal assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
