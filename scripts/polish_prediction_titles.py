#!/usr/bin/env python3
"""
Polish prediction titles and add formula display sections.

For each prediction:
1. Replace the short symbol title with a long-form descriptive title
2. Add a "## τ-Formula" section showing the explicit derivation in ι_τ
3. Preserve existing ## Derivation content
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SITE_ROOT = Path(__file__).parent.parent
PRED_DIR = SITE_ROOT / "_predictions"
DATA_DIR = SITE_ROOT / "_data" / "predictions"
TITLES_FILE = Path(__file__).parent / "prediction_titles.json"


def yaml_str(s: str) -> str:
    if not s:
        return '""'
    return f'"{s.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"'


def main():
    titles = json.loads(TITLES_FILE.read_text(encoding="utf-8"))
    predictions = json.loads(
        (DATA_DIR / "predictions.json").read_text(encoding="utf-8")
    )

    updated_count = 0
    formula_added = 0

    for pred in predictions:
        slug = pred["slug"]
        md_path = PRED_DIR / f"{slug}.md"
        if not md_path.exists():
            continue

        title_info = titles.get(slug)
        if not title_info:
            continue

        new_title = title_info["title"]
        formula_display = title_info.get("formula_display", "")

        content = md_path.read_text(encoding="utf-8")

        # Split frontmatter and body
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        frontmatter = parts[1]
        body = parts[2]

        # Update title in frontmatter
        frontmatter = re.sub(
            r'^title: ".*?"$',
            f'title: {yaml_str(new_title)}',
            frontmatter,
            flags=re.MULTILINE,
        )
        frontmatter = re.sub(
            r'^title_plain: ".*?"$',
            f'title_plain: {yaml_str(new_title)}',
            frontmatter,
            flags=re.MULTILINE,
        )

        # Update summary_short to use new title
        old_observable = pred.get("title", "")
        if old_observable and old_observable in frontmatter:
            # Replace old observable name in summary_short
            frontmatter = frontmatter.replace(
                f'summary_short: "{old_observable}:',
                f'summary_short: "{new_title}:',
            )

        # Add formula_display to frontmatter if not present
        if "formula_display:" not in frontmatter:
            # Insert after formula_mathml line
            frontmatter = re.sub(
                r'(formula_mathml: .*?\n)',
                r'\1' + f'formula_display: {yaml_str(formula_display)}\n',
                frontmatter,
            )

        # Add ## τ-Formula section to body if not already present
        if "## τ-Formula" not in body and formula_display:
            # Insert before ## Derivation if it exists, else at start
            if "## Derivation" in body:
                body = body.replace(
                    "## Derivation",
                    f"## τ-Formula\n\n**{formula_display}**\n\n## Derivation",
                )
                formula_added += 1
            elif "## Source" in body:
                body = body.replace(
                    "## Source",
                    f"## τ-Formula\n\n**{formula_display}**\n\n## Source",
                )
                formula_added += 1
            else:
                # Prepend to body
                body = f"\n\n## τ-Formula\n\n**{formula_display}**\n" + body
                formula_added += 1

        # Write updated file
        updated = f"---{frontmatter}---{body}"
        md_path.write_text(updated, encoding="utf-8")
        updated_count += 1

    # Also update the predictions.json data file with new titles
    for pred in predictions:
        slug = pred["slug"]
        title_info = titles.get(slug)
        if title_info:
            pred["title"] = title_info["title"]
            pred["title_plain"] = title_info["title"]

    (DATA_DIR / "predictions.json").write_text(
        json.dumps(predictions, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"Updated {updated_count} prediction titles")
    print(f"Added τ-Formula section to {formula_added} predictions")
    print(f"Updated predictions.json with new titles")


if __name__ == "__main__":
    main()
