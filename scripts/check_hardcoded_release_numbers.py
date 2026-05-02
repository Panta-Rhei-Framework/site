#!/usr/bin/env python3
"""Fail on current release metrics that bypass the Atlas manifest.

This is intentionally conservative and source-oriented. It scans public prose
and templates for release-changing count phrases that should be rendered via
`release-metric.html` or a generated README block.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


README_START = "<!-- release-metrics:start -->"
README_END = "<!-- release-metrics:end -->"


SKIP_PARTS = {
    ".git",
    "_site",
    "node_modules",
    "vendor",
    "assets",
    "_data/release",
    "_data/registry/release_manifest_sections.yml",
    "corpus/taulib/docs",
}


CHECK_SUFFIXES = {".md", ".html", ".liquid", ".yml", ".yaml"}


FORBIDDEN = [
    (re.compile(r"\b522\s+modules\b", re.I), "stale TauLib module count"),
    (re.compile(r"\b445\s+Lean\s+4?\s*modules\b", re.I), "stale TauLib module count"),
    (re.compile(r"\b4,139\s+public\s+(?:registry\s+)?objects\b", re.I), "stale registry object count"),
    (re.compile(r"\b4,547\s+(?:typed\s+mathematical\s+)?objects\b", re.I), "hardcoded registry total"),
    (re.compile(r"\b4,863\s+theorem", re.I), "hardcoded theorem/lemma count"),
    (re.compile(r"\b142,406\s+lines\b", re.I), "hardcoded TauLib line count"),
    (re.compile(r"\b1,125\s+references\b", re.I), "stale bibliography count"),
    (re.compile(r"\b67\s+zero-parameter\b", re.I), "hardcoded prediction count"),
    (re.compile(r"\b67\s+(?:numerical\s+)?predictions\b", re.I), "hardcoded prediction count"),
    (re.compile(r"\b30[- ]item\b", re.I), "hardcoded falsification count"),
    (re.compile(r"\b30[- ]prediction\b", re.I), "hardcoded falsification count"),
    (re.compile(r"\b30\s+(?:named|sharp)\b", re.I), "hardcoded falsification count"),
]


def strip_generated_blocks(text: str) -> str:
    if README_START not in text:
        return text
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), re.S)
    return pattern.sub("", text)


def should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    return any(part in rel for part in SKIP_PARTS)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    failures: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in CHECK_SUFFIXES or should_skip(path, root):
            continue
        text = strip_generated_blocks(path.read_text(encoding="utf-8", errors="ignore"))
        for pattern, label in FORBIDDEN:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                rel = path.relative_to(root)
                failures.append(f"{rel}:{line}: {label}: {match.group(0)!r}")
    if failures:
        print("Hardcoded release-changing metric phrases found:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1
    print("✓ No hardcoded release-changing metric phrases found outside manifest-approved blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
