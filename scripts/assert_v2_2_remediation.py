#!/usr/bin/env python3
"""Targeted assertions for the v2.2 Batch 1 P0/P1 remediation wave."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.parts: list[str] = []
        self.h1: list[str] = []
        self.stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag)
        if tag in {"script", "style", "svg"}:
            self.skip += 1
        if not self.skip and tag in {"h1", "h2", "h3", "p", "li", "td", "th", "div", "section", "article", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg"} and self.skip:
            self.skip -= 1
        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        if self.stack and self.stack[-1] == "h1":
            self.h1.append(norm(data))
        self.parts.append(data)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def page_text(path: str) -> tuple[str, list[str]]:
    full = SITE / path.strip("/") / "index.html"
    if not full.exists():
        raise AssertionError(f"missing built page: {path}")
    parser = TextParser()
    parser.feed(full.read_text(encoding="utf-8", errors="replace"))
    return norm(" ".join(parser.parts)), [h for h in parser.h1 if h]


def require(path: str, *phrases: str) -> None:
    text, h1 = page_text(path)
    if len(h1) != 1:
        raise AssertionError(f"{path}: expected one h1, found {h1}")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"{path}: missing phrase {phrase!r}")


def forbid(path: str, *phrases: str) -> None:
    text, _ = page_text(path)
    for phrase in phrases:
        if phrase in text:
            raise AssertionError(f"{path}: forbidden phrase still present {phrase!r}")


def main() -> int:
    require(
        "/program/research-agenda/",
        "Program definition",
        "finite, computable, self-contained formal kernel",
        "How to read this page",
        "ontically serious candidate",
    )
    forbid("/program/research-agenda/", "Ledgers Problem Ledger and Recovery Requirements")

    require(
        "/results/problem-ledger-answers/",
        "Internally addressed 32",
        "Partially addressed 8",
        "Structurally constrained 141",
    )
    require(
        "/program/research-agenda/problem-ledger/",
        "Not yet touched 232 public problem items",
        "Partially addressed 7 public problem items",
    )

    require(
        "/corpus/construction-spine/build-the-kernel/",
        "Step 1",
        "What this step is required to do",
        "Previous: Construction Spine overview",
        "Next: Step 2",
    )
    require(
        "/corpus/construction-spine/test-ontic-closure/",
        "Step 10",
        "Previous: Step 9",
        "Next: This is the final construction step; return to the Construction Spine overview",
    )
    forbid("/corpus/construction-spine/build-the-kernel/", "What this step was required to do")

    forbid("/verify/construction-spine-verification/", "No empirical check declared at this step")
    require("/verify/construction-spine-verification/", "Not applicable at this step")

    forbid("/publications/research-notes/", "Category tau")
    require("/publications/research-notes/", "Category τ", "Mechanism-Alignment / Slot-Filler Notes")
    forbid("/publications/research-notes/dark-matter-without-dark-matter-ksz-force-law/", "Category tau")

    require(
        "/publications/monograph-supplements/numerical-physics-ledger/",
        "Status and scope",
        "does not imply external validation",
    )
    print("v2.2 Batch 1 remediation assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
