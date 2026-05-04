#!/usr/bin/env python3
# ruff: noqa: E501
"""Site-wide route migration for the v4 Agenda Lane canonicalization.

Session 1 of the canonicalization (briefing
atlas/website/briefings/v4/15_v4_agenda.md). Touches only route strings;
editorial copy is left for Session 2.

The script is idempotent: re-running on already-migrated files is a no-op.

Replacements (exact-string substitutions, OLD => NEW):

    OLD: %2Fagenda%2Frecovery-requirements%2F  (URL-decoded: /agenda/<the old slug>/)
    NEW: /agenda/core-semantics/

    OLD: _data%2Frecovery_requirements%2F      (URL-decoded: _data/<old underscore name>/)
    NEW: _data/core_semantics/

The OLD strings are URL-encoded in this docstring so the script can scan
itself without re-modifying its own source. The runtime decodes them.

The collection key `recovery_requirements:` and frontmatter `type:` are
NOT swept here — those live in _config.yml and are handled by hand.

Excluded directories (never walked):
    _site/, .git/, node_modules/, vendor/, .jekyll-cache/, .bundle/

Self-exclusion: the script skips its own path so re-runs do not mutate
its source.

Usage:
    python3 scripts/migrate-agenda-core-semantics-routes.py [ROOT]

Default ROOT is the current working directory.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from urllib.parse import unquote

# OLD strings stored URL-encoded so the script's own source does not
# contain literal pre-migration paths (which would otherwise be rewritten
# during a self-scan and break the script).
REPLACEMENTS_ENCODED: list[tuple[str, str]] = [
    ("%2Fagenda%2Frecovery-requirements%2F", "/agenda/core-semantics/"),
    ("_data%2Frecovery_requirements%2F", "_data/core_semantics/"),
]

REPLACEMENTS: list[tuple[str, str]] = [
    (unquote(old), new) for old, new in REPLACEMENTS_ENCODED
]

ALLOW_EXTENSIONS = {
    ".md",
    ".markdown",
    ".html",
    ".htm",
    ".yml",
    ".yaml",
    ".json",
    ".csv",
    ".ndjson",
    ".xml",
    ".txt",
    ".rb",
    ".py",
}

EXCLUDE_DIRS = {
    "_site",
    ".git",
    "node_modules",
    "vendor",
    ".jekyll-cache",
    ".bundle",
}

# Files in this list are skipped to preserve their `permalink:` and
# `redirect_to:` lines, which intentionally retain the legacy slug.
EXCLUDE_FILES_RELATIVE = {
    "agenda/recovery-requirements.md",
    "agenda/recovery-requirements/mathematics.md",
    "agenda/recovery-requirements/physics.md",
    "agenda/recovery-requirements/life.md",
    "agenda/recovery-requirements/metaphysics.md",
    "agenda/recovery-requirements/mathematics-refusals.md",
}

SELF_PATH = Path(__file__).resolve()


def should_walk(dirname: str) -> bool:
    return dirname not in EXCLUDE_DIRS and not dirname.startswith(".git")


def migrate_file(path: Path, root: Path) -> tuple[int, int]:
    """Apply all replacements to one file. Returns (occurrences, files_changed)."""
    if path.resolve() == SELF_PATH:
        return 0, 0
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = ""
    if rel in EXCLUDE_FILES_RELATIVE:
        return 0, 0
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0, 0

    original = text
    occurrences = 0
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count:
            occurrences += count
            text = text.replace(old, new)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return occurrences, 1
    return 0, 0


def walk(root: Path) -> tuple[int, int, int]:
    total_files = 0
    total_changes = 0
    total_occurrences = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if should_walk(d)]
        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            if ext not in ALLOW_EXTENSIONS:
                continue
            total_files += 1
            path = Path(dirpath) / name
            occ, changed = migrate_file(path, root)
            if changed:
                total_changes += 1
                total_occurrences += occ
                rel = path.relative_to(root)
                print(f"  {rel}: {occ} replacement(s)")
    return total_files, total_changes, total_occurrences


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 1

    print(f"Migrating route references under {root}")
    print("Replacements:")
    for old, new in REPLACEMENTS:
        print(f"  {old!r} -> {new!r}")
    print()

    total_files, total_changes, total_occurrences = walk(root)

    print()
    print(
        f"Scanned {total_files} files; modified {total_changes}; "
        f"{total_occurrences} replacement(s) total."
    )
    if total_changes == 0:
        print("(idempotent: nothing to do)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
