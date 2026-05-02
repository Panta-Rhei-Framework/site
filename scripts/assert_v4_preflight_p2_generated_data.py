#!/usr/bin/env python3
"""Targeted assertions for v4.0 preflight PR2 generated-data integrity fixes."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


STALE_TAULIB_PIN = "37c12411e76f4bb89f7bc463d1443eecc0bd9afe"
CURRENT_TAULIB_PIN = "cb5e83015b54dd72eba560953fe2461820078757"


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


def iter_text_files(root: Path, suffixes: set[str]) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*") if path.is_file() and path.suffix in suffixes)


def assert_no_text(root: Path, needle: str, suffixes: set[str] | None = None, allow: set[Path] | None = None) -> None:
    suffixes = suffixes or {".csv", ".json", ".md", ".ndjson"}
    allow = {path.resolve() for path in (allow or set())}
    for path in iter_text_files(root, suffixes):
        if path.resolve() in allow:
            continue
        if needle in read(path):
            fail(f"{path} contains forbidden text: {needle}")


def load_json(path: Path):
    return json.loads(read(path))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v4_preflight_p2_generated_data.py _site", file=sys.stderr)
        return 2

    built = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    # Construction Map must retain the corrected Book VII final-boundary target.
    construction_map = read(repo / "_data" / "construction_map" / "construction-map.json")
    if "part-11-the-final-boundary-from-proof-to-commitment" in construction_map:
        fail("Construction Map still contains the obsolete Book VII Part XI final-boundary route")
    if "part-12-the-final-boundary-from-proof-to-commitment" not in construction_map:
        fail("Construction Map is missing the corrected Book VII Part XII final-boundary route")

    # TauLib projection URLs and source pins must agree with the public Corpus projection.
    for root in [
        repo / "_data" / "taulib",
        repo / "_data" / "taulib_projections",
        repo / "assets" / "data" / "taulib",
        repo / "assets" / "data" / "taulib-projections",
        repo / "corpus" / "taulib",
    ]:
        assert_no_text(root, "/verify/taulib/docs/")
        assert_no_text(root, STALE_TAULIB_PIN)
        if root.name in {"taulib", "taulib_projections", "taulib-projections"} and CURRENT_TAULIB_PIN not in "".join(read(path)[:2000] for path in iter_text_files(root, {".csv", ".json", ".md", ".ndjson"})[:20]):
            # The complete tree is large; this keeps the assertion cheap while still detecting an accidental blank pin.
            assert_contains(repo / "_data" / "taulib" / "module-inventory.json", CURRENT_TAULIB_PIN)

    # Registry object pages must exist for every public object route in the object index.
    registry_objects = load_json(repo / "_data" / "registry" / "objects.json")
    missing_registry_pages: list[str] = []
    for item in registry_objects:
        registry_id = item.get("id", "")
        url = item.get("url", "")
        if url.startswith("/registry/object/"):
            source_path = repo / "registry" / "object" / f"{registry_id.replace('.', '-')}.md"
            if not source_path.exists():
                missing_registry_pages.append(registry_id)
    if missing_registry_pages:
        fail(f"Missing Registry object pages: {', '.join(missing_registry_pages[:20])}")

    # Monograph projections must not carry the stale Book I chapter-count prose.
    for root in [
        repo / "corpus" / "monographs",
        repo / "corpus" / "construction-map",
        repo / "_data" / "monograph_projections",
        repo / "_data" / "publications",
        repo / "assets" / "data" / "monograph-projections",
        repo / "assets" / "data" / "construction-map",
    ]:
        assert_no_text(root, "sixty-seven chapters")

    # Corpus monograph part pages are not Schema.org Chapter objects.
    part_html = read(html_path(built, "/corpus/monographs/book-i/part-00-earned-foundations/"))
    if '"@type": "Chapter"' in part_html:
        fail("Corpus monograph part pages must not be emitted as Schema.org Chapter objects")

    # Prediction/falsification imports must not leak broken import syntax or raw math placeholders.
    broken_falsification_patterns = [
        "fourth generation!prediction",
        "$$-native",
        "$$'s topological",
        "$_1 = 220.6",
        "$r = _^4",
        "r = _^4",
        "156$$",
        "$_^4",
        "$_b",
        "$_m",
    ]
    for root in [
        repo / "_data" / "falsifications",
        repo / "assets" / "data" / "falsifications",
        repo / "falsifications",
        repo / "_data" / "registry_noteworthy_results",
        repo / "assets" / "data" / "registry-noteworthy-results",
        repo / "results" / "additional-noteworthy-results",
    ]:
        for pattern in broken_falsification_patterns:
            assert_no_text(root, pattern)

    for url in [
        "/falsifications/n9-tensor-to-scalar-ratio-r-4-00136/",
        "/falsifications/n11-first-acoustic-peak-1-2206/",
        "/falsifications/n16-deuterium-abundance-from-native-b/",
    ]:
        html = read(html_path(built, url))
        for pattern in broken_falsification_patterns:
            if pattern in html:
                fail(f"{url} leaks broken falsification text: {pattern}")

    # Result and Problem Answer data must be loaded from rich JSON, not shadowed by CSV/NDJSON twins.
    for incompatible_data_file in [
        repo / "_data" / "results" / "results.csv",
        repo / "_data" / "results" / "results.ndjson",
    ]:
        if incompatible_data_file.exists():
            fail(f"{incompatible_data_file} shadows results.json in Jekyll data")

    results = load_json(repo / "_data" / "results" / "results.json")
    if not results or any(not item.get("primary_domain") for item in results):
        fail("Results records must expose primary_domain for dashboard stats")
    if not any(item.get("bridge_status") or item.get("status_code") for item in results):
        fail("Results records must expose status fields for dashboard stats")

    problem_answers = load_json(repo / "_data" / "problem_answers" / "problem-answers.json")
    if not problem_answers:
        fail("Problem Answer Records data is empty")
    if any(not (item.get("public_answer_status_label") or item.get("answer_strength")) for item in problem_answers):
        fail("Problem Answer Records must expose public status or answer strength labels")

    config = read(repo / "_config.yml")
    for expected in [
        "path: \"framework\"",
        "path: \"research-notes\"",
        "path: \"research-program\"",
        "path: \"brand\"",
        "path: \"verify/assessments\"",
        "source_path: \"corpus/results/facets/predictions\"",
        "source_path: \"corpus/results/facets/falsifications\"",
    ]:
        if expected not in config:
            fail(f"_config.yml missing generated metadata default: {expected}")

    # Compatibility/support and assessment routes should render with exactly one H1.
    for url in [
        "/about/",
        "/framework/",
        "/research-notes/",
        "/research-program/",
        "/brand/voice/",
        "/verify/assessments/",
        "/verify/assessments/book-assessment/",
        "/verify/assessments/domain-assessment/",
        "/verify/assessments/dossier-schema/",
        "/verify/assessments/methodology/",
        "/verify/assessments/reviewer-workflow/",
        "/verify/assessments/scorecard/",
        "/verify/assessments/series-assessment/",
        "/verify/assessments/three-gate-rubric/",
        "/verify/assessments/usage-rules/",
    ]:
        assert_one_h1(html_path(built, url))

    changelog = html_path(built, "/changelog/")
    assert_not_contains(changelog, "<a</a>")
    assert_not_contains(changelog, "framework-diagrams-tikz-svg-pipeline-books-i-vii-60-modules-58-diagrams-a")

    print("v4 preflight P2 generated-data assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
