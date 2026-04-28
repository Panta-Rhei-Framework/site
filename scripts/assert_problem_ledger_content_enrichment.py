#!/usr/bin/env python3
"""Assert that public Problem Ledger pages carry source-enriched content."""

from __future__ import annotations

from collections import Counter
import json
import re
import sys
from pathlib import Path


EXPECTED_COUNTS = {
    "life": 102,
    "mathematics": 8,
    "metaphysics-philosophy": 27,
    "physics": 102,
}
PLACEHOLDER_PHRASES = [
    "included from the physics master ledger",
    "included from the biology master ledger",
    "included from the neuroscience master ledger",
    "included from the philosophical problems master ledger",
    "included in the public problem ledger v1.0 source projection",
    "source questions retained from the pinned source",
    "_no nested source questions were extracted",
]
REPRESENTATIVE_EXPECTATIONS = {
    "phys-dark-matter": ["What is the identity of dark matter?", "https://en.wikipedia.org/wiki/Dark_matter"],
    "life-origin-of-life": ["Exactly how, where, and when did life on Earth originate?", "https://en.wikipedia.org/wiki/Origin_of_life"],
    "life-consciousness": ["brain basis of subjective experience", "https://en.wikipedia.org/wiki/Consciousness"],
    "meta-hard-problem-of-consciousness": ["philosophical zombies", "https://en.wikipedia.org/wiki/hard_problem_of_consciousness"],
    "math-riemann-hypothesis": ["selected institutional mathematics source entry", "https://www.claymath.org/millennium-problems/riemann-hypothesis/"],
}


def page_path(site_dir: Path, url: str) -> Path:
    return site_dir / url.strip("/") / "index.html"


def visible_text(html: str) -> str:
    html = re.sub(r"<script\b.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style\b.*?</style>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: assert_problem_ledger_content_enrichment.py _site", file=sys.stderr)
        return 2
    site_dir = Path(sys.argv[1])
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "_data" / "problem_ledger" / "problem-ledger.json"
    items = json.loads(data_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    if len(items) != 239:
        errors.append(f"expected 239 public Problem Ledger items, found {len(items)}")
    counts = Counter(item.get("domain_slug") for item in items)
    if dict(counts) != EXPECTED_COUNTS:
        errors.append(f"unexpected domain counts: {dict(counts)}")

    by_id = {item["id"]: item for item in items}
    for item in items:
        source = item.get("source", {})
        audit = source.get("content_audit", {})
        records = source.get("source_entry_records", [])
        mapped_entries = item.get("mapping", {}).get("mapped_from_source_entries", [])
        if audit.get("status") != "source_enriched":
            errors.append(f"{item['id']}: content audit status is not source_enriched")
        if len(records) != len(mapped_entries):
            errors.append(f"{item['id']}: source_entry_records does not match mapped source entries")
        if item.get("source", {}).get("source_class") == "master_wholesale_import":
            for record in records:
                if not record.get("problem_statement"):
                    errors.append(f"{item['id']}: source record {record.get('source_entry_id')} missing problem_statement")
                if not record.get("source_permalink"):
                    errors.append(f"{item['id']}: source record {record.get('source_entry_id')} missing source_permalink")
                if not record.get("source_revision_id") or record.get("source_revision_id") == "not_applicable":
                    errors.append(f"{item['id']}: wiki source record {record.get('source_entry_id')} missing pinned revision")
        html_path = page_path(site_dir, item["url"])
        if not html_path.exists():
            errors.append(f"{item['id']}: built page missing at {html_path}")
            continue
        html = html_path.read_text(encoding="utf-8")
        text = visible_text(html).lower()
        for phrase in PLACEHOLDER_PHRASES:
            if phrase in text:
                errors.append(f"{item['id']}: placeholder phrase still visible: {phrase}")
        if source.get("source_links") and "Source Links" not in html:
            errors.append(f"{item['id']}: source links exist in data but Source Links section is not rendered")

    for item_id, snippets in REPRESENTATIVE_EXPECTATIONS.items():
        item = by_id.get(item_id)
        if not item:
            errors.append(f"missing representative item {item_id}")
            continue
        html_path = page_path(site_dir, item["url"])
        html = html_path.read_text(encoding="utf-8") if html_path.exists() else ""
        for snippet in snippets:
            if snippet not in html:
                errors.append(f"{item_id}: expected snippet not found on built page: {snippet}")

    if errors:
        print("Problem Ledger content enrichment assertions failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Problem Ledger content enrichment assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
