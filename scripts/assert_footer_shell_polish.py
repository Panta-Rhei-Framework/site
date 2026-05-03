#!/usr/bin/env python3
"""Assertions for footer compacting and shell-width alignment."""

from __future__ import annotations

import re
import sys
from pathlib import Path


CORE_LANE_LABELS = [
    "Discover",
    "Program",
    "Agenda",
    "Corpus",
    "Results",
    "Verify",
    "Impact",
    "Engage",
]


def normalize(value: str) -> str:
    return " ".join(value.split())


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing expected text: {needle}")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    home = read(site / "index.html")
    css = read(site / "assets/css/main.css")

    require(home, 'class="footer-link-group footer-link-group-core"', "home footer")
    require(home, 'class="footer-core-lanes"', "home footer")
    if home.count('class="footer-core-lane-column"') != 2:
        raise AssertionError("Footer Core Lanes should render exactly two visual subcolumns")
    if home.count("<span class=\"footer-group-title\">Core Lanes</span>") != 1:
        raise AssertionError("Footer should render one Core Lanes group title")

    footer_match = re.search(
        r'<div class="footer-link-group footer-link-group-core">(?P<body>.*?)</div>\s*</div>\s*<div class="footer-link-group">',
        home,
        re.S,
    )
    if not footer_match:
        raise AssertionError("Could not isolate Core Lanes footer group")
    core_group = footer_match.group("body")
    labels = re.findall(r">([^<]+)</a>", core_group)
    if labels != CORE_LANE_LABELS:
        raise AssertionError(f"Footer Core Lanes should be {CORE_LANE_LABELS}, found {labels}")

    require(home, "--site-shell-max:calc(260px + 860px + 240px + 36px)", "critical CSS")
    require(home, "--site-home-shell-max:1164px", "critical CSS")
    require(home, "max-width:var(--site-shell-max)", "critical CSS")
    require(home, ".shell-home .site-header{max-width:var(--site-home-shell-max)}", "critical CSS")

    compact_css = normalize(css)
    for selector in [".site-header", ".page-grid", ".site-footer"]:
        pattern = re.compile(rf"{re.escape(selector)}\{{[^}}]*max-width:var\(--site-shell-max\)")
        if not pattern.search(compact_css):
            raise AssertionError(f"{selector} should use --site-shell-max")
    require(compact_css, "body.shell-home .site-header{max-width:var(--site-home-shell-max)}", "compiled shell CSS")
    require(compact_css, "body.shell-home .site-footer{max-width:var(--site-home-shell-max)}", "compiled shell CSS")
    for needle in [
        ".footer-link-group-core",
        ".footer-core-lanes",
        "grid-template-columns:repeat(2, minmax(84px, 1fr))",
        "max-width:224px",
    ]:
        require(compact_css, needle, "compiled footer CSS")

    print("footer shell polish assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
