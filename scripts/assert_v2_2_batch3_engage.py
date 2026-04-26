#!/usr/bin/env python3
"""Targeted assertions for the v2.2 Batch 3 Engage lane release."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class H1Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "h1":
            self.h1_count += 1


def read_page(site_dir: Path, route: str) -> str:
    page = site_dir / route.strip("/") / "index.html"
    if route == "/":
        page = site_dir / "index.html"
    if not page.exists():
        raise AssertionError(f"Missing built page for {route}: {page}")
    return page.read_text(encoding="utf-8")


def assert_one_h1(html: str, route: str) -> None:
    parser = H1Parser()
    parser.feed(html)
    if parser.h1_count != 1:
        raise AssertionError(f"{route} has {parser.h1_count} h1 elements, expected 1")


def assert_contains(html: str, route: str, expected: list[str]) -> None:
    for needle in expected:
        if needle not in html:
            raise AssertionError(f"{route} is missing required text/link: {needle}")


def assert_absent(html: str, route: str, forbidden: list[str]) -> None:
    text = re.sub(r"\s+", " ", html)
    for needle in forbidden:
        if needle.lower() in text.lower():
            raise AssertionError(f"{route} contains forbidden public framing: {needle}")


def main() -> int:
    site_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    if not site_dir.exists():
        raise SystemExit(f"Missing site directory: {site_dir}")

    engage_routes = [
        "/engage/",
        "/engage/how-to-engage/",
        "/engage/discussions/",
        "/engage/review-the-work/",
        "/engage/read-explore/",
        "/engage/inspect-verify/",
        "/engage/critique-challenge/",
        "/engage/collaborate/",
        "/engage/contact/",
        "/engage/for-engineering-contributors/",
        "/engage/support-the-research/",
        "/engage/media/",
        "/engage/follow-the-research/",
        "/engage/seminars-and-guided-sessions/",
    ]

    forbidden = [
        "Join the movement",
        "Become a fan",
        "Support the theory",
        "Help us prove",
        "Spread the word",
        "Believe the framework",
        "Help us win acceptance",
        "Community of believers",
        "fan community",
    ]

    pages = {route: read_page(site_dir, route) for route in engage_routes}
    for route, html in pages.items():
        assert_one_h1(html, route)
        assert_absent(html, route, forbidden)

    assert_contains(
        pages["/engage/"],
        "/engage/",
        [
            "Engagement without endorsement.",
            "structured open-research engagement",
            "GitHub is the public discussion and contribution substrate",
            "https://github.com/orgs/Panta-Rhei-Research/discussions",
            "UNESCO Open Science",
            "The Turing Way",
        ],
    )

    assert_contains(
        pages["/engage/discussions/"],
        "/engage/discussions/",
        [
            "GitHub Discussions is the primary public discussion home",
            "What belongs in issues",
            "What belongs in pull requests",
            "What belongs in email",
            "Participation does not imply endorsement.",
            "https://github.com/Panta-Rhei-Research/community",
        ],
    )

    assert_contains(
        pages["/engage/review-the-work/"],
        "/engage/review-the-work/",
        [
            "Help inspect a bounded part of the research program.",
            "Review modes",
            "What to include",
            "Public review offers belong in GitHub Discussions",
        ],
    )

    assert_contains(
        pages["/engage/how-to-engage/"],
        "/engage/how-to-engage/",
        [
            "Discussions, Issues, Pull Requests, Email",
            "Ask a public question",
            "Challenge a claim publicly",
            "Report a concrete defect",
            "Propose a concrete fix",
            "Contact privately",
        ],
    )

    assert_contains(
        pages["/engage/contact/"],
        "/engage/contact/",
        [
            "Before contacting us",
            "Use public GitHub Discussions",
            "Use email when the matter is private",
            "Use GitHub Issues",
            "Use Pull Requests",
            "Institutional review",
            "Publication, library, or archive contact",
        ],
    )

    assert_contains(
        pages["/engage/for-engineering-contributors/"],
        "/engage/for-engineering-contributors/",
        [
            "GitHub workflow",
            "https://github.com/Panta-Rhei-Research/site",
            "https://github.com/Panta-Rhei-Research/taulib",
            "https://github.com/Panta-Rhei-Research/publications",
            "https://github.com/Panta-Rhei-Research/research",
            "https://github.com/Panta-Rhei-Research/community",
        ],
    )

    assert_contains(
        pages["/engage/media/"],
        "/engage/media/",
        [
            "Responsible communication",
            "Please do not describe internal program results as externally accepted scientific conclusions.",
            "Public Discussions",
        ],
    )

    assert_contains(
        pages["/engage/follow-the-research/"],
        "/engage/follow-the-research/",
        [
            "Email subscription is for receiving new notes.",
            "GitHub Discussions is for public questions and discussion about them.",
        ],
    )

    assert_contains(
        pages["/engage/seminars-and-guided-sessions/"],
        "/engage/seminars-and-guided-sessions/",
        ["Public follow-up", "GitHub Discussions"],
    )

    print("v2.2 Batch 3 Engage assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
