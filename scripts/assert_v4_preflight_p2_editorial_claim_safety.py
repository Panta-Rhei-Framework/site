#!/usr/bin/env python3
"""Targeted assertions for v4.0 preflight PR3 editorial claim-safety fixes."""

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


def assert_contains_text(path: Path, needle: str) -> None:
    text = visible_text(path)
    if needle not in text:
        fail(f"{path} missing visible text: {needle}")


def assert_not_contains_text(path: Path, needle: str) -> None:
    text = visible_text(path)
    if needle in text:
        fail(f"{path} contains forbidden visible text: {needle}")


def assert_contains_source(path: Path, needle: str) -> None:
    if needle not in read(path):
        fail(f"{path} missing source text: {needle}")


def assert_not_contains_source(path: Path, needle: str) -> None:
    if needle in read(path):
        fail(f"{path} contains forbidden source text: {needle}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_preflight_p2_editorial_claim_safety.py _site", file=sys.stderr)
        return 2

    built = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    # Program/About wording must route through the v4 architecture, not a legacy framework lane.
    about = html_path(built, "/program/about/")
    assert_contains_text(about, "Program obligations, Corpus construction, Results status, Verify inspection, Publications artifacts, Impact scenarios, and Engage routes")
    assert_contains_text(about, "Research Agenda, Corpus Construction Spine, a Results mirror, a Verify route, or a citable Publication artifact")
    assert_not_contains_text(about, "public website organized by framework")
    assert_not_contains_text(about, "entering through a framework lane")

    scope = html_path(built, "/program/about/scope-status-and-scrutiny/")
    assert_contains_text(scope, "Research Agenda")
    assert_contains_text(scope, "Corpus")
    assert_contains_text(scope, "Results lanes")
    assert_not_contains_text(scope, "framework and results lanes")
    assert_contains_source(repo / "research-program" / "about" / "scope-status-and-scrutiny.md", "type: \"Compatibility redirect\"")

    red_team = html_path(built, "/program/about/red-team-faq/")
    for expected in [
        "Assessment Protocols",
        "reviewer workflow",
        "dossier schema",
        "three-gate rubric",
        "As of the April 2026 public release manifest",
        "documented as entry N9",
    ]:
        assert_contains_text(red_team, expected)

    # Corpus monographs must frame Book VII mental-health language as metaphor, not diagnosis.
    part = html_path(built, "/corpus/monographs/book-vii/part-08-categorical-societies/")
    assert_contains_text(part, "not as a clinical or diagnostic claim")
    assert_not_contains_text(part, "Information overload fragments into schizophrenia")
    chapter = html_path(built, "/corpus/monographs/book-vii/part-08-categorical-societies/chapter-101-overload-fragmentation-and-schizophrenia/")
    assert_contains_text(chapter, "Mental-health boundary")
    assert_contains_text(chapter, "not a clinical account, diagnostic model, treatment recommendation")

    # TauLib tour must not overstate Lean compilation.
    taulib_tour = html_path(built, "/corpus/taulib/docs/tour-verify-it-yourself/")
    assert_contains_text(taulib_tour, "Formal scope note")
    assert_contains_text(taulib_tour, "does not by itself verify empirical truth, bridge adequacy, semantic correspondence")

    # Falsification status language must separate internal tracking from external acceptance.
    fals_browse = html_path(built, "/results/falsifications/browse/")
    assert_contains_text(fals_browse, "program-side tracking status")
    assert_contains_text(fals_browse, "not external acceptance labels")
    assert_not_contains_text(fals_browse, "4 confirmed")
    n23 = html_path(built, "/falsifications/n23-no-dm-detection-ever/")
    assert_contains_text(n23, "Dark-matter detection non-observation commitment")
    assert_contains_text(n23, "not a settled external fact")
    assert_contains_text(n23, "External Acceptance Not claimed by this page")
    assert_not_contains_text(n23, "No DM detection—ever")

    # Publications and media must expose current counts and artifact boundaries.
    pubs = html_path(built, "/publications/")
    assert_contains_text(pubs, "including the Numerical Physics Ledger")
    npl = html_path(built, "/publications/monograph-supplements/numerical-physics-ledger/")
    assert_contains_text(npl, "Comparison-basis note")
    assert_contains_text(npl, "Chapters 8–12")
    assert_contains_text(npl, "program tracking labels, not external acceptance labels")
    media = html_path(built, "/media/")
    assert_contains_text(media, "67 quantitative prediction records plus 30 named falsification tests")
    assert_contains_text(media, "0 in the published formalized modules")
    assert_not_contains_text(media, "220+ quantitative predictions")
    assert_not_contains_text(media, "0 (across all 7 books)")
    review_kit = html_path(built, "/media/review-kit/")
    assert_not_contains_text(review_kit, "(0 results)")
    assert_contains_text(review_kit, "Life-facing results")
    assert_contains_text(review_kit, "Metaphysics / Philosophy-facing results")

    # Results guides/readouts must carry Results metadata and avoid the old Claims shell wording.
    how_to = html_path(built, "/results/how-to-read-a-result-page/")
    assert_contains_text(how_to, "Every result links to its Corpus, Registry, book, and verification grounding where available")
    assert_not_contains_text(how_to, "books, registry, and framework")
    for url in ["/results/world-readout/mathematics/", "/results/world-readout/metaphysics/"]:
        page = html_path(built, url)
        assert_contains_text(page, "Results")
        assert_contains_text(page, "World Readout")

    # Impact briefings must be conditional scenario artifacts, not deployment claims.
    for url in [
        "/impact/papers/anticipatory-action-humanitarian-logistics-climate-risk-finance/",
        "/impact/papers/aviation-weather-intelligence/",
    ]:
        page = html_path(built, url)
        assert_contains_text(page, "conditional scenario artifact")
        assert_contains_text(page, "not a claim of adoption, deployment, policy implementation, external validation, or operational readiness")
        assert_not_contains_text(page, "Deployment Ladder")
        assert_not_contains_text(page, "deployment program")
        assert_not_contains_text(page, "deployment domain")

    engineering = html_path(built, "/engage/for-engineering-contributors/")
    assert_contains_text(engineering, "Do not open a large-change PR as the first move")
    assert_contains_text(engineering, "Issues are for concrete scoped implementation tasks")

    print("v4 preflight P2 editorial claim-safety assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
