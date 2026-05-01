#!/usr/bin/env python3
"""Targeted assertions for v4.0 preflight P1 structural fixes."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing expected file: {path}")
    return path.read_text(encoding="utf-8", errors="ignore")


def html_path(site: Path, url: str) -> Path:
    return site / url.strip("/") / "index.html"


def assert_contains(path: Path, needle: str) -> None:
    if needle not in read(path):
        fail(f"{path} missing expected text: {needle}")


def assert_not_contains(path: Path, needle: str) -> None:
    if needle in read(path):
        fail(f"{path} contains forbidden text: {needle}")


def assert_one_h1(path: Path) -> None:
    count = len(re.findall(r"<h1\b", read(path), flags=re.I))
    if count != 1:
        fail(f"{path} should contain exactly one h1, found {count}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_preflight_p1.py _site", file=sys.stderr)
        return 2

    built = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    # Corpus Monograph part navigation must never render empty previous/next hrefs.
    for url in [
        "/corpus/monographs/book-i/part-00-earned-foundations/",
        "/corpus/monographs/book-iv/part-07-condensed-matter-and-fluid-dynamics/",
        "/corpus/monographs/book-vii/part-08-categorical-societies/",
    ]:
        path = html_path(built, url)
        assert_one_h1(path)
        html = read(path)
        if 'class="content-card sequence-nav"' not in html:
            fail(f"{url} missing sequence navigation")
        if 'href=""' in html or "href=''" in html:
            fail(f"{url} contains an empty link")

    # TauLib Corpus docs and explorers must point to Corpus-owned module pages.
    for data_name in ["modules.json", "modules.ndjson", "modules.csv"]:
        assert_not_contains(repo / "_data" / "taulib_projections" / data_name, "/verify/taulib/docs/")
        assert_not_contains(repo / "assets" / "data" / "taulib-projections" / data_name, "/verify/taulib/docs/")

    for data_path in [
        repo / "_data" / "construction_spine" / "construction-spine.json",
        repo / "_data" / "construction_spine" / "construction-spine-data.json",
        repo / "_data" / "construction_spine" / "construction-spine.ndjson",
        repo / "assets" / "data" / "construction-spine" / "construction-spine.json",
        repo / "assets" / "data" / "construction-spine" / "construction-spine.ndjson",
        repo / "_data" / "foundational_hinges" / "foundational-hinges.json",
        repo / "_data" / "foundational_hinges" / "foundational-hinges-data.json",
        repo / "_data" / "foundational_hinges" / "foundational-hinges.ndjson",
        repo / "assets" / "data" / "foundational-hinges" / "foundational-hinges.json",
        repo / "assets" / "data" / "foundational-hinges" / "foundational-hinges.ndjson",
    ]:
        assert_not_contains(data_path, "/verify/taulib/docs/book-")

    config = read(repo / "_config.yml")
    if "_taulib_docs" not in config:
        fail("_taulib_docs must be excluded from active Jekyll collection output")
    for incompatible_data_file in [
        repo / "_data" / "results" / "results.csv",
        repo / "_data" / "results" / "results.ndjson",
    ]:
        if incompatible_data_file.exists():
            fail(f"{incompatible_data_file} shadows results.json in Jekyll data")

    for url in ["/corpus/taulib/docs/", "/corpus/taulib/modules/", "/verify/taulib/docs/"]:
        html = read(html_path(built, url))
        if "/verify/taulib/docs/book-" in html:
            fail(f"{url} leaks legacy Verify module links")
        if "/corpus/taulib/docs/book-" not in html:
            fail(f"{url} should link to Corpus TauLib module pages")

    construction_map = html_path(built, "/corpus/construction-map/")
    assert_contains(
        construction_map,
        "/corpus/monographs/book-vii/part-12-the-final-boundary-from-proof-to-commitment/",
    )
    assert_not_contains(
        construction_map,
        "/corpus/monographs/book-vii/part-11-the-final-boundary-from-proof-to-commitment/",
    )

    # Legacy module detail URLs are edge redirects; the root browser remains live.
    worker_source = read(repo / "workers" / "site-edge-headers.js")
    assert_contains(repo / "workers" / "site-edge-headers.js", 'pathname.startsWith("/verify/taulib/docs/")')
    if 'pathname !== "/verify/taulib/docs/"' not in worker_source:
        fail("Worker redirect must leave /verify/taulib/docs/ root browser live")

    # Recovery items with empty optional fields must fall back to generated body content.
    for url in [
        "/program/research-agenda/recovery-requirements/mathematics/mechanical-formal-checkability/",
        "/program/research-agenda/recovery-requirements/life/life-as-a-recoverable-category/",
        "/program/research-agenda/recovery-requirements/metaphysics/reality-as-a-recoverable-field/",
    ]:
        html = read(html_path(built, url))
        if "<h2>Requirement</h2>\n    <p></p>" in html:
            fail(f"{url} renders empty Requirement paragraph")
        if "<h2>Why This Matters</h2>\n    <p></p>" in html:
            fail(f"{url} renders empty Why This Matters paragraph")

    # Prediction/falsification generated pages must expose default metadata.
    for url in [
        "/predictions/20-galaxy-btfr/",
        "/falsifications/n16-deuterium-abundance-from-native-b/",
        "/falsifications/n23-no-dm-detection-ever/",
    ]:
        html = read(html_path(built, url))
        if "Numerical Physics Ledger" not in html:
            fail(f"{url} missing Results-side prediction/falsification shell")

    # Result guide status grammar and shell metadata must be v4 safe.
    result_guide = html_path(built, "/results/how-to-read-a-result-page/")
    assert_contains(result_guide, "Internally addressed")
    assert_not_contains(result_guide, "Every claim carries a status: resolved")
    assert_not_contains(result_guide, "How to Read a Claim")
    assert_not_contains(result_guide, "Browse All Claims")

    # Media kit must not claim zero sorry across all seven books while Book VI is planned.
    media = html_path(built, "/media/")
    assert_not_contains(media, "0 sorry across all 7 books")
    assert_not_contains(media, "zero sorry across all 7 books")
    assert_contains(media, "published formalized modules are built without")

    # Glossary constant and metadata.
    glossary = html_path(built, "/verify/taulib/glossary/")
    assert_contains(glossary, "W_3(3)")
    assert_contains(glossary, "<td>17</td>")
    assert_not_contains(glossary, "<td>4</td><td>—</td><td>Continued-fraction window sum (3 partial quotients from index 3)")

    # Impact full-text collection now has a real route with metadata and one H1.
    impact_papers = html_path(built, "/impact/papers/")
    assert_one_h1(impact_papers)
    assert_contains(impact_papers, "Public-Good Briefing Full Texts")
    assert_contains(impact_papers, "/publications/research-briefings/public-good/")

    print("v4 preflight P1 assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
