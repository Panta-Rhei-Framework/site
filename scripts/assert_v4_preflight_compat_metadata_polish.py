#!/usr/bin/env python3
"""Targeted assertions for v4.0 preflight PR4 compatibility and metadata polish."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        if tag.lower() in {"head", "script", "style", "svg", "noscript"}:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"head", "script", "style", "svg", "noscript"} and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self.parts.append(data)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing expected file: {path}")
    return path.read_text(encoding="utf-8", errors="ignore")


def html_path(site: Path, url: str) -> Path:
    stripped = url.strip("/")
    return site / stripped / "index.html" if stripped else site / "index.html"


def visible_text(path: Path) -> str:
    parser = VisibleTextParser()
    parser.feed(read(path))
    return re.sub(r"\s+", " ", " ".join(parser.parts)).strip()


def assert_contains_source(path: Path, needle: str) -> None:
    if needle not in read(path):
        fail(f"{path} missing source text: {needle}")


def assert_not_contains_source(path: Path, needle: str) -> None:
    if needle in read(path):
        fail(f"{path} contains forbidden source text: {needle}")


def assert_contains_text(path: Path, needle: str) -> None:
    text = visible_text(path)
    if needle not in text:
        fail(f"{path} missing visible text: {needle}")


def assert_not_contains_text(path: Path, needle: str) -> None:
    text = visible_text(path)
    if needle in text:
        fail(f"{path} contains forbidden visible text: {needle}")


def assert_frontmatter(path: Path, *needles: str) -> None:
    source = read(path)
    frontmatter = source.split("---", 2)[1] if source.startswith("---") else source
    for needle in needles:
        if needle not in frontmatter:
            fail(f"{path} frontmatter missing: {needle}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_preflight_compat_metadata_polish.py _site", file=sys.stderr)
        return 2

    built = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    # Construction Map / Corpus Monograph stale source checks.
    construction_map = read(repo / "_data" / "construction_map" / "construction-map.json")
    if "part-11-the-final-boundary-from-proof-to-commitment" in construction_map:
        fail("Construction Map still exposes the obsolete Book VII Part XI final-boundary route")
    if "part-12-the-final-boundary-from-proof-to-commitment" not in construction_map:
        fail("Construction Map is missing the Book VII Part XII final-boundary route")

    book_i_chapter = html_path(built, "/corpus/monographs/book-i/part-00-earned-foundations/chapter-01-earned-foundations/")
    assert_contains_text(book_i_chapter, "seventy-nine chapters")
    for stale in ["81 modules", "zero `sorry`", "zero sorry", "seventy-three chapters"]:
        assert_not_contains_text(book_i_chapter, stale)

    book_vii_final = html_path(built, "/corpus/monographs/book-vii/part-12-the-final-boundary-from-proof-to-commitment/chapter-128-the-series-closing-line/")
    assert_contains_text(book_vii_final, "five hundred and thirty-five chapters across the series")
    assert_not_contains_text(book_vii_final, "one hundred and forty-one chapters")

    # Program/Discover P3 polish.
    discover = html_path(built, "/discover/")
    assert_contains_text(discover, "It helps readers move from orientation into the research spine")
    assert_not_contains_source(repo / "discover" / "index.md", "Discover is the entry layer. It helps")

    recovery = read(repo / "program" / "research-agenda" / "recovery-requirements" / "index.md")
    if "label: \"Metaphysics\"" not in recovery:
        fail("Recovery Requirements hero CTAs must include Metaphysics")

    source_policy = repo / "program" / "research-agenda" / "problem-ledger-source-policy" / "index.md"
    assert_contains_source(source_policy, "url: /results/problem-ledger-answers/")
    assert_not_contains_source(source_policy, "url: /results/problem-ledger/\n")

    science_humanities = html_path(built, "/program/research-agenda/science-humanities-and-coherence/")
    assert_contains_text(science_humanities, "Corpus construction surfaces")
    assert_not_contains_text(science_humanities, "framework lanes")

    # Results classification/falsification compatibility.
    classifications = html_path(built, "/results/classifications/")
    for expected in ["Foundational math", "Frontier problem", "Structural readout", "Consequence"]:
        assert_contains_text(classifications, expected)
    assert_not_contains_text(classifications, "v2.2 makes")

    problem_answers = repo / "results" / "problem-answers" / "index.md"
    assert_frontmatter(problem_answers, "v2_lane: results", 'type: "Compatibility Route"', 'status: "Compatibility"')

    n16 = html_path(built, "/falsifications/n16-deuterium-abundance-from-native-b/")
    assert_contains_text(n16, "N16 — Deuterium abundance from")
    assert_not_contains_text(n16, "$$-native")
    assert_not_contains_text(n16, "$_B")

    n23 = html_path(built, "/falsifications/n23-no-dm-detection-ever/")
    assert_contains_text(n23, "ongoing; indefinitely monitored")
    assert_contains_text(n23, "not a settled external fact")
    for stale in ["No DM detection-ever", "No DM detection—ever", "all DM searches", "permanent."]:
        assert_not_contains_text(n23, stale)

    # Verify and compatibility route metadata that the crawl flagged.
    metadata_pages = [
        repo / "verify" / "custom-axiom-inventory.md",
        repo / "verify" / "custom-axioms.md",
        repo / "verify" / "filter-rules.md",
        repo / "verify" / "how-to-audit" / "index.md",
        repo / "verify" / "how-to-audit" / "formal-methods.md",
        repo / "verify" / "how-to-audit" / "journalist-skeptic.md",
        repo / "verify" / "how-to-audit" / "mathematician.md",
        repo / "verify" / "how-to-audit" / "philosopher.md",
        repo / "verify" / "how-to-audit" / "physicist.md",
        repo / "verify" / "how-to-audit" / "prior-art-specialist.md",
        repo / "verify" / "taulib" / "glossary.md",
        repo / "verify" / "taulib" / "scope-labels.md",
        repo / "verify" / "tcb-disclosure.md",
        repo / "verify" / "tcb.md",
        repo / "publications" / "books" / "index.md",
    ]
    for page in metadata_pages:
        assert_frontmatter(page, "v2_lane:", "type:", "status:")

    # Changelog should treat the retired module projection as history, not a current Framework surface.
    changelog = html_path(built, "/changelog/")
    for stale in ["Framework diagrams", "framework lane", "framework modules", "Framework: 69"]:
        assert_not_contains_text(changelog, stale)
    assert_contains_text(changelog, "Legacy diagram projection")

    research_monographs = html_path(built, "/publications/research-monographs/")
    assert_contains_text(research_monographs, "Open Corpus edition")
    assert_not_contains_text(research_monographs, "Amazon.de")

    print("v4 preflight compatibility/metadata polish assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
