#!/usr/bin/env python3
"""
Enrich Physics Ledger prediction and falsification pages with derivation
prose extracted from the LaTeX manuscript chapters (ch59-ch68).

For each prediction: search the LaTeX chapters for the registry ID,
extract surrounding theorem + derivation paragraphs, clean to readable
markdown, add cross-link metadata.

For each falsification: extract the full N-paragraph from ch68, clean,
add cross-link metadata.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from latex_to_mathml import clean_bibfield, latex_accents_to_unicode

SITE_ROOT = Path(__file__).parent.parent
LEDGER_DIR = Path(os.path.expanduser(
    "~/Books/PantaRhei-2ndEd/books/V-CategoricalMacrocosm/latex/sections/part07"
))
BOOK4_DIR = Path(os.path.expanduser(
    "~/Books/PantaRhei-2ndEd/books/IV-CategoricalMicrocosm/latex/sections"
))
PRED_DIR = SITE_ROOT / "_predictions"
FALS_DIR = SITE_ROOT / "_falsifications"


# ---------------------------------------------------------------------------
# LaTeX cleaning (multi-paragraph prose → readable markdown)
# ---------------------------------------------------------------------------

GREEK_MAP = {
    r"\alpha": "α", r"\beta": "β", r"\gamma": "γ", r"\delta": "δ",
    r"\epsilon": "ε", r"\zeta": "ζ", r"\eta": "η", r"\theta": "θ",
    r"\iota": "ι", r"\kappa": "κ", r"\lambda": "λ", r"\mu": "μ",
    r"\nu": "ν", r"\xi": "ξ", r"\pi": "π", r"\rho": "ρ",
    r"\sigma": "σ", r"\tau": "τ", r"\phi": "φ", r"\chi": "χ",
    r"\psi": "ψ", r"\omega": "ω", r"\Gamma": "Γ", r"\Delta": "Δ",
    r"\Theta": "Θ", r"\Lambda": "Λ", r"\Xi": "Ξ", r"\Pi": "Π",
    r"\Sigma": "Σ", r"\Phi": "Φ", r"\Psi": "Ψ", r"\Omega": "Ω",
    r"\partial": "∂", r"\infty": "∞", r"\nabla": "∇",
    r"\to": "→", r"\neq": "≠", r"\leq": "≤", r"\geq": "≥",
    r"\approx": "≈", r"\equiv": "≡", r"\cong": "≅", r"\sim": "∼",
    r"\in": "∈", r"\subset": "⊂", r"\times": "×", r"\cdot": "·",
    r"\otimes": "⊗", r"\oplus": "⊕", r"\forall": "∀", r"\exists": "∃",
    r"\emptyset": "∅", r"\pm": "±",
    r"\mathbb{R}": "ℝ", r"\mathbb{C}": "ℂ", r"\mathbb{N}": "ℕ",
    r"\mathbb{Z}": "ℤ", r"\mathbb{Q}": "ℚ",
}

# Sort by length descending so longer commands match first (\theta before \the)
_GREEK_SORTED = sorted(GREEK_MAP.items(), key=lambda kv: -len(kv[0]))

# Simple accent resolution — ONLY handles the common {\"o}, {\'e} brace forms
# that appear in author names within prose. Does NOT touch bare \t, \c, etc.
SIMPLE_ACCENTS = {
    r'\"': "\u0308",  # umlaut
    r"\'": "\u0301",  # acute
    r"\`": "\u0300",  # grave
    r"\^": "\u0302",  # circumflex
    r"\~": "\u0303",  # tilde
}


def clean_prose(text: str) -> str:
    """Convert LaTeX prose to clean readable markdown.

    This is a CONSERVATIVE cleaner for full LaTeX prose — it does NOT use
    the aggressive latex_accents_to_unicode function (which corrupts
    multi-letter commands like \\tau, \\theta). Instead it:
    1. Strips environment/metadata markers
    2. Resolves known Greek letters and math symbols by exact match
    3. Handles only brace-form accents ({\\\"o} etc)
    4. Unwraps formatting commands (\\textit, \\textbf, \\emph)
    5. Strips remaining unknown \\commands
    """
    # texorpdfstring
    text = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", text)
    # Strip \index{...} including nested (3 levels)
    for _ in range(3):
        text = re.sub(r"\\index\s*\{(?:[^{}]|\{[^{}]*\})*\}", "", text)
    # Strip \label{...}
    text = re.sub(r"\\label\s*\{[^{}]*\}", "", text)
    # Strip \begin{...} \end{...} environment markers
    text = re.sub(r"\\begin\s*\{[^{}]*\}(?:\[[^\]]*\])?", "", text)
    text = re.sub(r"\\end\s*\{[^{}]*\}", "", text)
    # \item → bullet
    text = re.sub(r"\\item\b\s*(?:\[[^\]]*\]\s*)?", "- ", text)
    # Escapes (BEFORE Greek resolution)
    text = text.replace(r"\&", "&").replace(r"\%", "%")
    text = text.replace(r"\_", "_").replace(r"\#", "#")
    text = text.replace(r"\colon", ":").replace(r"\ldots", "…")
    text = text.replace(r"\ss", "ß")
    # Dashes
    text = text.replace("---", "\u2014").replace("--", "\u2013")
    # Tilde (non-breaking space)
    text = text.replace("~", " ")
    # \\ (row separator / forced newline) → space
    text = re.sub(r"\\\\\s*(?:\[.*?\])?\s*", " ", text)
    # Greek letters and math operators (exact match, longest first)
    for cmd, replacement in _GREEK_SORTED:
        # Only match if followed by non-letter (to avoid partial matches)
        text = re.sub(re.escape(cmd) + r"(?![a-zA-Z])", replacement, text)
    # Formatting commands → markdown
    text = re.sub(r"\\textit\{([^{}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", text)
    text = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textsc\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\text\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\mbox\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\mathrm\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\mathbf\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\boldsymbol\{([^{}]*)\}", r"\1", text)
    # Brace-form accents ONLY: {\"o} → ö, {\'e} → é, etc.
    import unicodedata
    for cmd, diacritic in SIMPLE_ACCENTS.items():
        pattern = re.compile(re.escape(cmd) + r"\{([a-zA-Z])\}")
        text = pattern.sub(
            lambda m: unicodedata.normalize("NFC", m.group(1) + diacritic),
            text,
        )
    # \cite{...} → strip
    text = re.sub(r"\\cite[a-zA-Z]*\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}", "", text)
    # \ref{...}, \eqref{...} → just the label text
    text = re.sub(r"\\(?:eq)?ref\{([^{}]*)\}", r"(\1)", text)
    # Remaining \command{content} → keep content
    text = re.sub(r"\\[a-zA-Z]+\*?\s*\{([^{}]*)\}", r"\1", text)
    # Remaining bare \commands → strip
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    # Clean braces and $
    text = text.replace("{", "").replace("}", "")
    # Keep $...$ for potential inline math rendering
    # But strip tabular & column separators
    text = text.replace(" & ", " | ")  # table column → pipe
    # Collapse whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    # Trim lines
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    return text.strip()


# ---------------------------------------------------------------------------
# Registry ID search in LaTeX files
# ---------------------------------------------------------------------------

def strip_tex_comments(text: str) -> str:
    """Remove % comment lines but preserve \\%."""
    lines = []
    for line in text.split("\n"):
        # Find first unescaped %
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                line = line[:i]
                break
            i += 1
        lines.append(line)
    return "\n".join(lines)


def load_tex_files() -> dict[str, str]:
    """Load all Part VII chapter .tex files into a dict keyed by filename.
    Comments are stripped so searches don't hit comment blocks."""
    files = {}
    for tex in sorted(LEDGER_DIR.glob("ch*.tex")):
        try:
            raw = tex.read_text(encoding="utf-8")
            files[tex.stem] = strip_tex_comments(raw)
        except Exception:
            pass
    # Also load select Book IV chapters for IV.T* references
    for part_dir in sorted(BOOK4_DIR.glob("part*")):
        for tex in sorted(part_dir.glob("ch*.tex")):
            try:
                raw = tex.read_text(encoding="utf-8")
                files[tex.stem] = strip_tex_comments(raw)
            except Exception:
                pass
    return files


def find_derivation_prose(
    tex_files: dict[str, str],
    registry_id: str,
    observable: str,
) -> tuple[str, str]:
    """Find derivation prose for a registry ID.

    Returns (prose, source_chapter).
    """
    if not registry_id:
        return "", ""

    # Search strategy: look for the registry ID in the text, then
    # extract the surrounding paragraph(s).
    for filename, content in tex_files.items():
        # Skip ch68 (that's the inventory chapter, not derivations)
        if "ch68" in filename:
            continue

        # Search for the registry ID
        # Format: IV.T166 or V.T190 — search as literal text
        if registry_id not in content:
            continue

        # Find the position of the registry ID
        pos = content.find(registry_id)
        if pos == -1:
            continue

        # Extract a window around the ID (backward to previous section,
        # forward to next section or ~2000 chars)
        # Walk backward to find section/subsection/paragraph start
        start = max(0, pos - 1500)
        # Find the nearest \section, \subsection, \paragraph, or theorem before pos
        section_markers = [
            (m.start(), m.group(0))
            for m in re.finditer(
                r"\\(?:section|subsection|paragraph|begin\{theorem\}|begin\{proposition\}|begin\{definition\})",
                content[start:pos],
            )
        ]
        if section_markers:
            # Use the last (nearest) marker
            marker_offset = section_markers[-1][0]
            start = start + marker_offset

        # Forward: find next section or ~2000 chars
        end = min(len(content), pos + 2000)
        next_section = re.search(
            r"\\(?:section|subsection\*?\{|chapter)",
            content[pos + len(registry_id):end],
        )
        if next_section:
            end = pos + len(registry_id) + next_section.start()

        raw_block = content[start:end]

        # Clean it
        prose = clean_prose(raw_block)

        # Trim to first 3-4 meaningful paragraphs (split by double newline)
        paragraphs = [p.strip() for p in prose.split("\n\n") if p.strip()]
        # Skip very short paragraphs (section titles, labels)
        meaningful = [p for p in paragraphs if len(p) > 50]
        if not meaningful:
            meaningful = paragraphs[:3]
        else:
            meaningful = meaningful[:4]

        result = "\n\n".join(meaningful)
        if len(result) > 100:  # meaningful content found
            return result, filename

    return "", ""


# ---------------------------------------------------------------------------
# Enrichment
# ---------------------------------------------------------------------------


def enrich_predictions(tex_files: dict[str, str]):
    """Enrich each prediction .md file with derivation prose."""
    pred_json = SITE_ROOT / "_data" / "predictions" / "predictions.json"
    predictions = json.loads(pred_json.read_text(encoding="utf-8"))

    enriched_count = 0
    for pred in predictions:
        slug = pred["slug"]
        registry_id = pred.get("registry_id", "")
        observable = pred.get("title", "")

        md_path = PRED_DIR / f"{slug}.md"
        if not md_path.exists():
            continue

        # Find derivation prose
        prose, source_chapter = find_derivation_prose(
            tex_files, registry_id, observable
        )

        if not prose:
            continue

        # Read the existing file
        content = md_path.read_text(encoding="utf-8")

        # Find the body section (after the closing ---)
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        frontmatter = parts[1]
        old_body = parts[2].strip()

        # Build enriched body
        new_body = f"""## Derivation

{prose}

## Source

This prediction is derived in the Physics Ledger ({source_chapter.replace('ch', 'Chapter ').replace('-', ' — ', 1) if source_chapter else 'Physics Ledger'}), Books IV–V of *Panta Rhei*.
"""

        # Write enriched file
        enriched = f"---{frontmatter}---\n\n{new_body}\n"
        md_path.write_text(enriched, encoding="utf-8")
        enriched_count += 1

    print(f"  Enriched {enriched_count} of {len(predictions)} prediction pages")


def enrich_falsifications(tex_files: dict[str, str]):
    """Enrich falsification pages with fuller prose from ch68."""
    fals_json = SITE_ROOT / "_data" / "falsifications" / "falsifications.json"
    falsifications = json.loads(fals_json.read_text(encoding="utf-8"))

    ch68 = tex_files.get("ch68-inventory-falsification", "")
    if not ch68:
        print("  WARN: ch68 not found")
        return

    enriched_count = 0
    for fals in falsifications:
        slug = fals["slug"]
        nid = fals["id"]  # e.g., "N9"
        registry_id = fals.get("registry_id", "")

        md_path = FALS_DIR / f"{slug}.md"
        if not md_path.exists():
            continue

        # Find the N-paragraph in ch68
        # Pattern: \paragraph{Nk: Title.} ... until next \paragraph{N or \subsection
        n_num = fals["n_num"]
        pattern = re.compile(
            rf"\\paragraph\{{N{n_num}:?\s*(.*?)\}}(.*?)(?=\\paragraph\{{N\d+|\\subsection|\\section|$)",
            re.DOTALL,
        )
        match = pattern.search(ch68)
        if not match:
            continue

        raw_body = match.group(2).strip()
        prose = clean_prose(raw_body)

        # Also search for derivation context from the source chapter
        extra_prose = ""
        if registry_id:
            extra, source = find_derivation_prose(tex_files, registry_id, "")
            if extra and len(extra) > 100:
                extra_prose = f"\n\n## Derivation Context\n\n{extra}"

        # Read existing file
        content = md_path.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        frontmatter = parts[1]

        # Build enriched body
        new_body = f"""## {nid}: Prediction

{prose}
{extra_prose}
"""

        # Write enriched file
        enriched = f"---{frontmatter}---\n\n{new_body}\n"
        md_path.write_text(enriched, encoding="utf-8")
        enriched_count += 1

    print(f"  Enriched {enriched_count} of {len(falsifications)} falsification pages")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Loading LaTeX files...")
    tex_files = load_tex_files()
    print(f"  Loaded {len(tex_files)} .tex files")

    print("\nEnriching predictions...")
    enrich_predictions(tex_files)

    print("\nEnriching falsifications...")
    enrich_falsifications(tex_files)

    print("\nDone!")


if __name__ == "__main__":
    main()
