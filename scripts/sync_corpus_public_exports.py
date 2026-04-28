#!/usr/bin/env python3
"""Sync public Corpus projections into the v2 site worktree."""

from __future__ import annotations

import argparse
import json
import os
import shutil
from collections import Counter
from pathlib import Path
from typing import Any


SITE_ROOT = Path(__file__).resolve().parents[1]
ORG_ROOT = SITE_ROOT.parent
CORPUS_EXPORTS = Path(os.environ.get("CORPUS_EXPORTS_DIR", ORG_ROOT / "corpus" / "exports" / "public"))


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    print(f"synced {target.relative_to(SITE_ROOT)}")


def copy_tree(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob("*")):
        if path.is_file():
            copy_file(path, target / path.relative_to(source))


def clean_tree(target: Path, suffixes: tuple[str, ...] = (".md", ".json", ".csv", ".ndjson")) -> None:
    if not target.exists():
        return
    for path in sorted(target.rglob("*"), reverse=True):
        if path.is_file() and path.suffix in suffixes:
            path.unlink()
    for path in sorted(target.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass


def clean_child_directories(target: Path) -> None:
    if not target.exists():
        return
    for child in sorted(target.iterdir()):
        if child.is_dir():
            shutil.rmtree(child)


def read_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("items", [])


def yaml_scalar(value: Any) -> str:
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    return json.dumps(text, ensure_ascii=False)


def yaml_dump(data: dict[str, Any], indent: int = 0) -> str:
    lines: list[str] = []
    pad = " " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{key}:")
            lines.append(yaml_dump(value, indent + 2))
        elif isinstance(value, list):
            if not value:
                lines.append(f"{pad}{key}: []")
            else:
                lines.append(f"{pad}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        lines.append(f"{pad}  -")
                        lines.append(yaml_dump(item, indent + 4))
                    else:
                        lines.append(f"{pad}  - {yaml_scalar(item)}")
        else:
            lines.append(f"{pad}{key}: {yaml_scalar(value)}")
    return "\n".join(lines)


def write_markdown(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml_dump(frontmatter) + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")
    print(f"generated {path.relative_to(SITE_ROOT)}")


def domain_label(domain: str) -> str:
    return {
        "mathematics": "Mathematics",
        "physics": "Physics",
        "life": "Life",
        "metaphysics": "Metaphysics",
        "metaphysics-philosophy": "Metaphysics / Philosophy",
        "metaphysics_philosophy": "Metaphysics / Philosophy",
    }.get(domain, domain.replace("-", " ").replace("_", " ").title())


def result_status_label(value: str) -> str:
    labels = {
        "R": "Internally addressed",
        "resolved": "Internally addressed",
        "internally_addressed": "Internally addressed",
        "partially_addressed": "Partially addressed",
        "partial": "Partial",
        "not_yet_classified": "Not yet touched",
        "not_addressed": "Not addressed",
        "not_externally_reviewed": "Not externally reviewed",
        "not_yet_verified": "Not yet verified",
        "pending_bridge_verification": "Pending bridge verification",
        "pending_formal_verification": "Pending formal verification",
        "pending_physics_verification": "Pending physics verification",
        "pending_life_verification": "Pending life verification",
        "pending_metaphysics_verification": "Pending metaphysics verification",
        "route_available": "Route available",
    }
    if not value:
        return "Pending"
    return labels.get(value, value.replace("_", " ").replace("-", " ").title())


def domain_counts(items: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"mathematics": 0, "physics": 0, "life": 0, "metaphysics-philosophy": 0}
    for item in items:
        domain = item.get("domain_slug", "")
        counts[domain] = counts.get(domain, 0) + 1
    return counts


def title_from_url(url: str) -> str:
    stripped = url.strip("/")
    if not stripped:
        return "Linked page"
    if stripped.startswith("verify/domain-verification/"):
        return f"Domain Verification: {domain_label(stripped.split('/')[-1])}"
    if stripped == "verify/construction-spine-verification":
        return "Construction Spine Verification"
    if stripped.startswith("results/world-readout/") and stripped.count("/") == 2:
        return f"World Readout: {domain_label(stripped.split('/')[-1])}"
    parts = stripped.split("/")
    last = parts[-1]
    if last in {"index", "browse"} and len(parts) > 1:
        last = parts[-2]
    return last.replace("-", " ").replace("_", " ").title()


def looks_like_identifier(text: str) -> bool:
    return (
        text.startswith(("CS-", "PREC-", "MREC-", "MREF-", "LREC-", "METH-", "phys-", "math-", "life-", "meta-"))
        or (" " not in text and "." in text)
        or text.isupper()
    )


def bullet_lines(items: list[Any], empty_message: str) -> str:
    if not items:
        return f"- {empty_message}"
    lines: list[str] = []
    for item in items:
        if isinstance(item, dict):
            title = item.get("title") or item.get("url") or item.get("id") or "Linked item"
            url = item.get("url", "")
            if url:
                lines.append(f"- [{title}]({url})")
            else:
                lines.append(f"- {title}")
        elif isinstance(item, str) and item.startswith("/"):
            lines.append(f"- [{title_from_url(item)}]({item})")
        else:
            lines.append(f"- `{item}`" if isinstance(item, str) and looks_like_identifier(item) else f"- {item}")
    return "\n".join(lines)


def generate_problem_answer_pages() -> None:
    problems = read_json(CORPUS_EXPORTS / "problem-ledger.json")
    results = {item.get("id"): item for item in read_json(SITE_ROOT / "_data" / "results" / "results.json") if item.get("id")}
    root = SITE_ROOT / "results" / "problem-ledger-answers"
    domains = sorted({item["domain_slug"] for item in problems})
    counts = domain_counts(problems)
    status_counts = Counter((item.get("program") or {}).get("result_status", "not_yet_classified") for item in problems)

    root_body = f"""## Answer Mirror

> Current program stances against the open and foundational problems accepted in the Research Agenda.

This is the Results-side answer mirror of the Program-side Problem Ledger. It reports where the current public result surface has an answer, partial answer, structural constraint, or pending stance.

<div class="notice note"><strong>Status note.</strong> A program stance is not the same as external acceptance, scientific settlement, or final verification.</div>

## Browse by Domain

The Problem Ledger Answers mirror the Program-side Problem Ledger. Each domain page reports the current program stance against the imported or selected problem obligations.

<div class="v2-grid">
  <a class="v2-tile" href="{{{{ '/results/problem-ledger-answers/mathematics/' | relative_url }}}}">
    <strong>Mathematics</strong>
    <span>{counts.get('mathematics', 0)} public problem items.</span>
  </a>
  <a class="v2-tile" href="{{{{ '/results/problem-ledger-answers/physics/' | relative_url }}}}">
    <strong>Physics</strong>
    <span>{counts.get('physics', 0)} public problem items.</span>
  </a>
  <a class="v2-tile" href="{{{{ '/results/problem-ledger-answers/life/' | relative_url }}}}">
    <strong>Life</strong>
    <span>{counts.get('life', 0)} public problem items.</span>
  </a>
  <a class="v2-tile" href="{{{{ '/results/problem-ledger-answers/metaphysics-philosophy/' | relative_url }}}}">
    <strong>Metaphysics / Philosophy</strong>
    <span>{counts.get('metaphysics-philosophy', 0)} public problem items.</span>
  </a>
</div>

## Current Status Summary

<table>
  <thead>
    <tr>
      <th scope="col">Public status</th>
      <th scope="col">Count</th>
      <th scope="col">Meaning on this site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Partially addressed</th>
      <td>{status_counts.get('partially_addressed', 0)}</td>
      <td>The program has a visible Results-side stance, but not final settlement or external acceptance.</td>
    </tr>
    <tr>
      <th scope="row">Not yet touched</th>
      <td>{status_counts.get('not_yet_classified', 0)}</td>
      <td>The problem is publicly carried as an obligation without a current answer mirror.</td>
    </tr>
  </tbody>
</table>

## Source policy

Problem source policy remains owned by the Research Agenda: [Problem Ledger Source Policy](/program/research-agenda/problem-ledger-source-policy/). The mirror does not republish source prose; it reports the current program stance against pinned or institutionally selected source records.
"""
    write_markdown(
        root / "index.md",
        {
            "layout": "program-doc",
            "title": "Problem Ledger Answers",
            "permalink": "/results/problem-ledger-answers/",
            "lane": "results",
            "v2_lane": "results",
            "type": "Result Mirror",
            "status": "Canonical",
            "summary_short": "Current Results-side stances against public Problem Ledger items.",
        },
        root_body,
    )

    for domain in domains:
        items = [item for item in problems if item["domain_slug"] == domain]
        links = "\n".join(
            f"- [{item['title']}](/results/problem-ledger-answers/{domain}/{item['slug']}/) - {result_status_label(item.get('program', {}).get('result_status', ''))}"
            for item in items
        )
        write_markdown(
            root / domain / "index.md",
            {
                "layout": "program-doc",
                "title": f"Problem Ledger Answers: {domain_label(domain)}",
                "permalink": f"/results/problem-ledger-answers/{domain}/",
                "lane": "results",
                "v2_lane": "results",
                "type": "Result Mirror Domain",
                "status": "Canonical",
                "summary_short": f"Current program stances for {domain_label(domain)} Problem Ledger items.",
            },
            f"""## Status Separation

<div class="notice note"><strong>Status note.</strong> These are current internal program stances unless explicitly marked otherwise.</div>

## Items

{links}
""",
        )

    for item in problems:
        domain = item["domain_slug"]
        related_results = item.get("related", {}).get("results", [])
        related_corpus_steps = item.get("related", {}).get("construction_steps", [])
        result_lines: list[str] = []
        for result_id in related_results:
            result = results.get(result_id)
            if result:
                result_lines.append(f"- [{result['title']}]({result['url']}) - {result.get('status_code', 'status pending')}")
            else:
                result_lines.append(f"- `{result_id}` - mapping pending")
        if not result_lines:
            result_lines.append("- Dedicated Result page pending.")
        verify = item.get("verify_links", {})
        verify_line = f"[{verify.get('verification_mode', 'Verify surface')}]({verify.get('verify_url')})" if verify.get("verify_url") else "Dedicated Verify surface pending."
        program = item.get("program", {})
        body = f"""## Status Separation

<div class="notice note"><strong>Status note.</strong> This page reports the current program stance. It does not imply external acceptance unless explicitly stated.</div>

- Internal stance: **{result_status_label(program.get('result_status', 'not_yet_classified'))}**
- Verification route: **{"Available" if verify.get('exists') else "Pending"}**
- External status: **Not externally reviewed**

## Problem

{item.get('short_title', item['title'])}

## Source

- Source: {item.get('source', {}).get('source_page', 'Source metadata pending.')}
- Import rule: `{item.get('source', {}).get('import_rule', 'pending')}`
- Program ledger item: [{item['id']}]({item['url']})

## Current Program Stance

- Result status: **{result_status_label(program.get('result_status', 'not_yet_classified'))}**
- Tier: `{program.get('tier', 'unclassified')}`
- Agenda role: `{program.get('agenda_role', 'stress_test')}`
- Expressibility: `{program.get('expressibility_status', 'unknown')}`

## Related Construction Steps

{bullet_lines(related_corpus_steps, "Construction Spine mapping pending.")}

## Related Results

{chr(10).join(result_lines)}

## Verify This Answer

{verify_line}

## What remains open

Residual boundaries remain public unless a linked Result page explicitly closes them with status-marked evidence.
"""
        write_markdown(
            root / domain / item["slug"] / "index.md",
            {
                "layout": "program-doc",
                "title": item["title"],
                "permalink": f"/results/problem-ledger-answers/{domain}/{item['slug']}/",
                "lane": "results",
                "v2_lane": "results",
                "type": "Problem Ledger Answer",
                "status": "Canonical",
                "summary_short": f"Current Results-side stance for {item['title']}.",
                "canonical_problem_id": item["id"],
            },
            body,
        )


def recovery_result_path(item: dict[str, Any]) -> str:
    if item.get("item_type") == "mathematical_refusal":
        return f"/results/recovery-target-status/mathematics/refusals/{item['slug']}/"
    return f"/results/recovery-target-status/{item['domain_slug']}/{item['slug']}/"


def generate_recovery_status_pages() -> None:
    items = read_json(CORPUS_EXPORTS / "recovery-requirements.json")
    root = SITE_ROOT / "results" / "recovery-target-status"
    domains = ["mathematics", "physics", "life", "metaphysics"]

    root_body = """> Current program status against the structures the kernel promised to recover.

This is the Results-side mirror of the Program-side Recovery Requirements ledger. Recovery requirements remain obligations; this surface reports their current public status.

<div class="notice note"><strong>Status note.</strong> Partial or internally addressed recovery is not the same as formal verification or external acceptance.</div>

## Browse by domain

{% assign recovery_items = site.data.recovery_requirements["recovery-requirements"] %}
{% assign recovery_domains = "mathematics,physics,life,metaphysics" | split: "," %}
<ul class="v2-grid v2-card-list">
{% for domain in recovery_domains %}
  {% assign domain_items = recovery_items | where: "domain_slug", domain %}
  {% assign partial_count = domain_items | where: "recovery_status", "partial" | size %}
  {% assign not_applicable_count = domain_items | where: "recovery_status", "not_applicable" | size %}
  {% assign pending_count = domain_items | where: "recovery_status", "pending_recovery" | size %}
  {% if partial_count >= not_applicable_count and partial_count >= pending_count %}
    {% assign dominant_status = "Partial" %}
  {% elsif not_applicable_count >= partial_count and not_applicable_count >= pending_count %}
    {% assign dominant_status = "Not applicable / refused" %}
  {% else %}
    {% assign dominant_status = "Pending recovery" %}
  {% endif %}
  <li>
    <article class="v2-tile">
      <h3>{{ domain | replace: '-', ' ' | capitalize }}</h3>
      <p>{{ domain_items | size }} public recovery/refusal item{% unless domain_items.size == 1 %}s{% endunless %}.</p>
      <p><strong>Dominant status:</strong> {{ dominant_status }}</p>
      <p><a href="{{ '/results/recovery-target-status/' | append: domain | append: '/' | relative_url }}">Results mirror</a> · <a href="{{ '/program/research-agenda/recovery-requirements/' | append: domain | append: '/' | relative_url }}">Recovery Requirements</a></p>
    </article>
  </li>
{% endfor %}
</ul>
"""
    write_markdown(
        root / "index.md",
        {
            "layout": "program-doc",
            "title": "Recovery Target Status",
            "permalink": "/results/recovery-target-status/",
            "lane": "results",
            "v2_lane": "results",
            "type": "Result Mirror",
            "status": "Canonical",
            "summary_short": "Current Results-side status against public Recovery Requirements.",
        },
        root_body,
    )

    for domain in domains:
        domain_items = [item for item in items if item["domain_slug"] == domain]
        lines = "\n".join(f"- [{item['title']}]({recovery_result_path(item)}) - {result_status_label(item.get('recovery_status', ''))}" for item in domain_items)
        write_markdown(
            root / domain / "index.md",
            {
                "layout": "program-doc",
                "title": f"Recovery Target Status: {domain_label(domain)}",
                "permalink": f"/results/recovery-target-status/{domain}/",
                "lane": "results",
                "v2_lane": "results",
                "type": "Result Mirror Domain",
                "status": "Canonical",
                "summary_short": f"Current recovery status for {domain_label(domain)} targets.",
            },
            f"""<div class="notice note"><strong>Status note.</strong> Recovery status is internal unless formal or external verification is explicitly linked.</div>

## Items

{lines}
""",
        )

    for item in items:
        related = item.get("related", {})
        verification = item.get("verification", {})
        result_lines = related.get("results") or []
        if result_lines:
            results_body = "\n".join(f"- `{result}`" for result in result_lines)
        else:
            results_body = "- Granular Result mapping pending."
        verify_body = bullet_lines(verification.get("related_verify_pages", related.get("verify", [])), "Dedicated Verify surface pending.")
        corpus_steps_body = bullet_lines(verification.get("related_corpus_steps", related.get("construction_steps", [])), "Construction Spine mapping pending.")
        verification_results_body = bullet_lines(verification.get("related_results", result_lines), "Granular Result mapping pending.")
        body = f"""<div class="notice note"><strong>Status note.</strong> This page reports current recovery status. It does not imply external acceptance unless explicitly stated.</div>

## Status Separation

- Internal status: **{result_status_label(item.get('recovery_status', 'pending'))}**
- Verification state: **{result_status_label(verification.get('status', item.get('verification_status', 'not_yet_verified')))}**
- External status: **Not externally reviewed**

## Requirement

{item.get('public_summary') or item.get('short_title', item['title'])}

## Current Recovery Status

- Recovery status: **{result_status_label(item.get('recovery_status', 'pending'))}**
- Verification status: **{result_status_label(verification.get('status', item.get('verification_status', 'not_yet_verified')))}**
- Program ledger item: [{item['id']}]({item['url']})
- Verification mode: `{verification.get('mode', item.get('program_role', 'pending'))}`

## Result Summary

{item.get('expanded_rationale') or 'Detailed result summary pending.'}

## Related Result Items

{verification_results_body}

## Related Corpus Construction Steps

{corpus_steps_body}

## Related Verify Surfaces

{verify_body}

## What This Status Does Not Yet Establish

{chr(10).join(f'- {entry}' for entry in item.get('what_this_does_not_claim', [])) or '- External acceptance is not implied by this status.'}

## Projection Metadata

- Generated from: `{item.get('generated_from', 'corpus/recovery-requirements')}`
- Projection version: `{item.get('projection_version', 'v0.1')}`
- Do not edit generated projection: `{item.get('do_not_edit', True)}`
"""
        write_markdown(
            SITE_ROOT / recovery_result_path(item).strip("/") / "index.md",
            {
                "layout": "program-doc",
                "title": item["title"],
                "permalink": recovery_result_path(item),
                "lane": "results",
                "v2_lane": "results",
                "type": "Recovery Target Status",
                "status": "Canonical",
                "summary_short": f"Current Results-side recovery status for {item['title']}.",
                "canonical_recovery_id": item["id"],
            },
            body,
        )


def sync_problem_recovery_agenda() -> None:
    for filename in ("problem-ledger.json", "problem-ledger.ndjson", "problem-ledger.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "problem_ledger" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "problem-ledger" / filename)

    for filename in ("recovery-requirements.json", "recovery-requirements.ndjson", "recovery-requirements.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "recovery_requirements" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "recovery-requirements" / filename)

    source = CORPUS_EXPORTS / "agenda-progress.json"
    copy_file(source, SITE_ROOT / "_data" / "agenda_progress" / "agenda-progress.json")
    copy_file(source, SITE_ROOT / "assets" / "data" / "agenda-progress" / "agenda-progress.json")

    clean_tree(SITE_ROOT / "_problem_ledger")
    clean_tree(SITE_ROOT / "_recovery_requirements")
    copy_tree(CORPUS_EXPORTS / "problem-items", SITE_ROOT / "_problem_ledger")
    copy_tree(CORPUS_EXPORTS / "recovery-requirements", SITE_ROOT / "_recovery_requirements")
    generate_problem_answer_pages()
    generate_recovery_status_pages()


def sync_results() -> None:
    for filename in ("results.json", "results.ndjson", "results.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "results" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "results" / filename)
    clean_tree(SITE_ROOT / "results" / "problem")
    copy_tree(CORPUS_EXPORTS / "result-pages", SITE_ROOT / "results" / "problem")


def sync_monograph_projections() -> None:
    clean_tree(SITE_ROOT / "corpus" / "monographs")
    copy_tree(CORPUS_EXPORTS / "monograph-projections" / "pages", SITE_ROOT / "corpus" / "monographs")
    for filename in ("parts.json", "chapters.json"):
        source = CORPUS_EXPORTS / "monograph-projections" / "data" / filename
        copy_file(source, SITE_ROOT / "_data" / "publications" / filename)


def sync_foundations() -> None:
    for filename in ("construction-spine.json", "construction-spine.ndjson", "construction-spine.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "construction_spine" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "construction-spine" / filename)
    copy_file(
        CORPUS_EXPORTS / "construction-spine.json",
        SITE_ROOT / "_data" / "construction_spine" / "construction-spine-data.json",
    )

    for filename in ("foundational-hinges.json", "foundational-hinges.ndjson", "foundational-hinges.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "foundational_hinges" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "foundational-hinges" / filename)
    copy_file(
        CORPUS_EXPORTS / "foundational-hinges.json",
        SITE_ROOT / "_data" / "foundational_hinges" / "foundational-hinges-data.json",
    )

    clean_child_directories(SITE_ROOT / "corpus" / "construction-spine")
    clean_tree(SITE_ROOT / "corpus" / "foundational-hinges")
    copy_tree(CORPUS_EXPORTS / "construction-spine" / "steps", SITE_ROOT / "corpus" / "construction-spine")
    copy_tree(CORPUS_EXPORTS / "foundational-hinges", SITE_ROOT / "corpus" / "foundational-hinges")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scope",
        choices=("all", "foundations", "ledgers", "results", "monographs"),
        default="all",
        help="Sync all Corpus public exports, or one projection family.",
    )
    args = parser.parse_args()

    if not CORPUS_EXPORTS.exists():
        raise SystemExit(f"Missing Corpus public exports: {CORPUS_EXPORTS}")

    if args.scope in ("all", "ledgers"):
        sync_problem_recovery_agenda()
    if args.scope in ("all", "results"):
        sync_results()
    if args.scope in ("all", "monographs"):
        sync_monograph_projections()
    if args.scope in ("all", "foundations"):
        sync_foundations()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
