#!/usr/bin/env python3
"""Targeted assertions for the Results lane v3 release."""

from __future__ import annotations

import html
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


def load_json(path: str) -> list[dict]:
    data = json.loads((ROOT / path).read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("items", [])


def visible_text(markup: str) -> str:
    markup = re.sub(r"<script[\s\S]*?</script>", " ", markup, flags=re.I)
    markup = re.sub(r"<style[\s\S]*?</style>", " ", markup, flags=re.I)
    markup = re.sub(r"<[^>]+>", " ", markup)
    return re.sub(r"\s+", " ", html.unescape(markup)).strip()


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_contains(path: Path, needle: str) -> None:
    if needle not in path.read_text(encoding="utf-8"):
        raise AssertionError(f"{path.relative_to(ROOT)}: missing {needle!r}")


def source_assertions() -> None:
    answers = load_json("_data/problem_answers/problem-answers.json")
    results = load_json("_data/results/results.json")
    predictions = load_json("_data/predictions/predictions.json")
    falsifications = load_json("_data/falsifications/falsifications.json")

    assert_equal(len(answers), 239, "Problem Answers count")
    assert_equal(Counter(item["domain_slug"] for item in answers), Counter({
        "mathematics": 8,
        "physics": 102,
        "life": 102,
        "metaphysics-philosophy": 27,
    }), "Problem Answers domain counts")
    assert_equal(Counter(item["public_answer_status_label"] for item in answers), Counter({
        "Structurally constrained": 141,
        "Partially addressed": 8,
        "Internally addressed": 32,
        "Declared out of scope": 35,
        "Further investigation": 8,
        "Backlog open problem": 15,
    }), "Problem Answers status distribution")
    assert_equal(len(results), 255, "generic Result count")
    assert_equal(len(predictions), 67, "Prediction facet count")
    assert_equal(len(falsifications), 30, "Falsification Path facet count")

    if "234 total result" in (ROOT / "results/index.md").read_text(encoding="utf-8"):
        raise AssertionError("Results root still contains stale 234 result count")
    assert_contains(ROOT / "results/problem-ledger-answers/index.md", "Problem Answers are the one-to-one Results mirror")
    assert_contains(ROOT / "_includes/result-page-crosslinks.html", "Related Problem Answers")
    assert_contains(ROOT / "predictions/index.md", "redirect_to: /results/predictions/browse/")
    assert_contains(ROOT / "falsifications/index.md", "redirect_to: /results/falsifications/browse/")


def built_assertions() -> None:
    if not SITE.exists():
        return
    routes = [
        "results/index.html",
        "results/browse/index.html",
        "results/problem-ledger-answers/index.html",
        "results/problem-ledger-answers/mathematics/index.html",
        "results/problem-ledger-answers/physics/hubble-tension/index.html",
        "results/problem-ledger-answers/mathematics/riemann-hypothesis/index.html",
        "results/problem-ledger-answers/life/blue-whale/index.html",
        "results/problem-ledger-answers/physics/magnetoreception/index.html",
        "results/problem-ledger-answers/physics/fast-radio-bursts-frbs/index.html",
        "results/problem/hubble-tension/index.html",
        "results/predictions/browse/index.html",
        "results/falsifications/browse/index.html",
        "predictions/index.html",
        "falsifications/index.html",
    ]
    for route in routes:
        path = SITE / route
        if not path.exists():
            raise AssertionError(f"built route missing: {route}")
        markup = path.read_text(encoding="utf-8")
        h1_count = len(re.findall(r"<h1\b", markup, flags=re.I))
        assert_equal(h1_count, 1, f"{route} H1 count")

    root_text = visible_text((SITE / "results/index.html").read_text(encoding="utf-8"))
    if "255 total result pages" not in root_text and "full 255-page catalogue" not in root_text:
        raise AssertionError("Results root does not expose the 255-result catalogue")
    if "234 total result pages" in root_text:
        raise AssertionError("Results root still exposes 234 total result pages")

    browse_text = visible_text((SITE / "results/browse/index.html").read_text(encoding="utf-8"))
    forbidden = [
        "Status: Resolved",
        "Resolved —",
        "Resolved -",
        "Trolley Problem Resolution",
        "Vacuum Catastrophe Resolution",
        "Fourth Quadrant Resolution",
    ]
    for phrase in forbidden:
        if phrase in browse_text:
            raise AssertionError(f"Browse visible text still contains {phrase!r}")

    answer_text = visible_text((SITE / "results/problem-ledger-answers/physics/hubble-tension/index.html").read_text(encoding="utf-8"))
    for phrase in ("Registry Evidence", "What This Answer Does Not Claim", "H0 Tension Framework Account"):
        if phrase not in answer_text:
            raise AssertionError(f"Hubble Problem Answer missing {phrase!r}")

    result_text = visible_text((SITE / "results/problem/hubble-tension/index.html").read_text(encoding="utf-8"))
    if "Related Problem Answers" not in result_text or "Hubble tension" not in result_text:
        raise AssertionError("Mapped generic Result page does not expose Related Problem Answers")


def main() -> int:
    source_assertions()
    built_assertions()
    print("Results lane v3 assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
