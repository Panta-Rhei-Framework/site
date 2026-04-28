#!/usr/bin/env python3
"""Validate Result page to Problem Ledger ID mappings."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_PAGES = ROOT / "results" / "problem"
RESULTS_JSON = ROOT / "_data" / "results" / "results.json"
PROBLEM_LEDGER_JSON = ROOT / "_data" / "problem_ledger" / "problem-ledger.json"


EXPECTED_EXAMPLES = {
    "hubble-tension": "phys-hubble-tension",
    "riemann-hypothesis": "math-riemann-hypothesis",
    "no-dark-matter-particle": "phys-dark-matter",
    "abiogenesis-inevitability": "life-origin-of-life",
    "consciousness-global-section": "life-consciousness",
    "free-will-as-branching": "life-biology-free-will",
    "why-something-rather-than-nothing": "meta-why-something-rather-than-nothing",
    "quantum-computing": "phys-temperature",
}


def split_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter delimiter")
    return text[4:end]


def parse_scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_ids(frontmatter: str, path: Path) -> list[str]:
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(frontmatter) or {}
        if "problem_ledger_ids" not in data:
            raise AssertionError(f"{path}: missing problem_ledger_ids")
        parsed = data["problem_ledger_ids"]
    except ImportError:
        match = re.search(r"^problem_ledger_ids:[ \t]*(.*)$", frontmatter, re.MULTILINE)
        if not match:
            raise AssertionError(f"{path}: missing problem_ledger_ids")
        value = match.group(1).strip()
        if value == "[]":
            parsed = []
        elif value:
            try:
                parsed = ast.literal_eval(value)
            except Exception as exc:  # pragma: no cover - defensive diagnostics
                raise AssertionError(f"{path}: invalid problem_ledger_ids value {value!r}") from exc
        else:
            parsed = []
            lines = frontmatter[match.end() :].splitlines()
            for line in lines:
                if not line.startswith("  - "):
                    break
                parsed.append(line[4:].strip().strip('"').strip("'"))
    if parsed is None:
        parsed = []
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise AssertionError(f"{path}: problem_ledger_ids must be a list of strings")
    return parsed


def main() -> int:
    problems = json.loads(PROBLEM_LEDGER_JSON.read_text(encoding="utf-8"))
    problem_ids = {problem["id"] for problem in problems}
    records = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
    records_by_id = {record["id"]: record for record in records}

    if len(records_by_id) != len(records):
        raise AssertionError("_data/results/results.json contains duplicate result IDs")

    page_count = 0
    mapped_count = 0
    total_links = 0
    pages_by_slug = {}

    for path in sorted(RESULT_PAGES.glob("*.md")):
        page_count += 1
        frontmatter = split_frontmatter(path.read_text(encoding="utf-8"))
        result_id = parse_scalar(frontmatter, "result_id")
        if not result_id:
            raise AssertionError(f"{path}: missing result_id")
        ids = parse_ids(frontmatter, path)
        pages_by_slug[path.stem] = ids
        unknown = [problem_id for problem_id in ids if problem_id not in problem_ids]
        if unknown:
            raise AssertionError(f"{path}: unknown Problem Ledger IDs: {unknown}")
        if len(ids) != len(set(ids)):
            raise AssertionError(f"{path}: duplicate Problem Ledger IDs")
        if result_id not in records_by_id:
            raise AssertionError(f"{path}: result_id {result_id} missing from results.json")
        json_ids = records_by_id[result_id].get("problem_ledger_ids")
        if json_ids != ids:
            raise AssertionError(
                f"{path}: frontmatter problem_ledger_ids {ids} != results.json {json_ids}"
            )
        if ids:
            mapped_count += 1
            total_links += len(ids)

    if page_count != 255:
        raise AssertionError(f"expected 255 Result pages, found {page_count}")
    if len(records) != page_count:
        raise AssertionError(f"expected results.json parity with {page_count} pages, found {len(records)}")

    for slug, expected_problem_id in EXPECTED_EXAMPLES.items():
        if expected_problem_id not in pages_by_slug.get(slug, []):
            raise AssertionError(f"missing expected mapping: {slug} -> {expected_problem_id}")

    foundation_ids = pages_by_slug.get("tau-kernel-coherence")
    if foundation_ids != []:
        raise AssertionError("tau-kernel-coherence should remain unmapped as a non-ledger foundation result")

    print(f"Result pages: {page_count}")
    print(f"Problem Ledger items: {len(problem_ids)}")
    print(f"Mapped Result pages: {mapped_count}")
    print(f"Unmapped Result pages: {page_count - mapped_count}")
    print(f"Total Result → Problem Ledger links: {total_links}")
    print("Result/Problem Ledger mapping validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
