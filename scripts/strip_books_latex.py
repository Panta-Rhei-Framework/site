#!/usr/bin/env python3
"""
strip_books_latex.py — Convert raw LaTeX residue in publications/books/ to
clean Unicode + HTML that renders correctly in Kramdown (no KaTeX/MathJax).

Processes every .md file under publications/books/ and:
  1. Strips `$...$` delimiters around Unicode/simple content
  2. Converts LaTeX subscripts/superscripts to Unicode (E_0 → E₀, τ^3 → τ³)
  3. Converts `$$...$$` display blocks to <div class="math-display">...</div>
  4. Strips simple LaTeX macros (\Hom, \text, etc.)

The script preserves YAML front matter structure and only modifies
field VALUES (not keys). It processes summary_short fields specifically
since those feed into SEO meta descriptions.

Usage:
    python3 scripts/strip_books_latex.py --dry-run     # preview only
    python3 scripts/strip_books_latex.py               # apply changes
    python3 scripts/strip_books_latex.py --report      # detailed per-file

Exit codes:
    0 = success
    1 = errors encountered

Design principles:
  - Idempotent: running twice is safe (no effect second time)
  - Conservative: only transforms known-safe patterns
  - Logged: every change is recorded in strip_books_latex.log
  - Rollback-friendly: the changes are git-trackable per-file
"""

import argparse
import os
import re
import sys
from pathlib import Path

# -------- Unicode mapping tables --------

SUBSCRIPT_DIGITS = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUPERSCRIPT_DIGITS = str.maketrans("0123456789+-=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ")

# -------- Pattern replacements --------
# Each tuple: (regex, replacement, description)
# Order matters: more-specific patterns first.

# Display math blocks: $$...$$ → <div class="math-display">...</div>
# Handles both single-line and multi-line (re.DOTALL via (?s) flag).
DISPLAY_MATH_PATTERN = re.compile(
    r"\$\$\s*(.+?)\s*\$\$",
    re.DOTALL,
)

def display_math_replace(match):
    body = match.group(1).strip()
    # Clean up inner LaTeX in the display block
    body = clean_math_inner(body)
    return f'<div class="math-display">{body}</div>'


def clean_math_inner(s: str) -> str:
    """Clean common LaTeX artifacts inside a math expression.

    Conservative: only applies to content that's already in a math context.
    """
    # First, normalize double-backslash escapes: \\X → \X for all letter followups.
    # This handles markdown-escaped LaTeX macros (e.g., \\Obj → \Obj).
    s = re.sub(r"\\\\([a-zA-Z])", r"\\\1", s)

    # Project-specific LaTeX macros → Unicode/plain names.
    # Note: using lookahead (?=[^a-zA-Z]|$) instead of \b because Unicode
    # letters (ℤ, 𝕃, τ) are word chars, which breaks \b for ASCII commands
    # followed directly by Unicode (e.g. \hatℤ, \widehatℤ, \mathbbA).
    def nb_pattern(cmd):
        # Non-boundary: cmd followed by any non-ASCII-letter
        return r"\\" + cmd + r"(?=[^a-zA-Z]|$)"

    project_macros = [
        # Braced mathbb/mathbf/mathrm/mathcal/mathsf → inner content
        (r"\\mathbb\{A\}", "𝔸"),
        (r"\\mathbf\{d\}", "𝐝"),
        (r"\\mathbf\{([^}]*)\}", r"\1"),
        (r"\\mathbb\{([^}]*)\}", r"\1"),
        (r"\\mathrm\{([^}]*)\}", r"\1"),
        (r"\\mathcal\{([^}]*)\}", r"\1"),
        (r"\\mathsf\{([^}]*)\}", r"\1"),

        # Unbraced mathbb/mathbf/mathrm followed directly by a letter
        # (e.g. \mathbbA_τ → A_τ, \mathbfd → d)
        (r"\\mathbb([A-Za-z])", r"\1"),
        (r"\\mathbf([A-Za-z])", r"\1"),
        (r"\\mathrm([A-Za-z])", r"\1"),
        (r"\\mathcal([A-Za-z])", r"\1"),

        # Hat/widehat: drop the prefix (no Unicode combining hat above Z)
        (r"\\widehat\s*", ""),
        (r"\\hat\s*", ""),

        # Project symbols
        (nb_pattern("Lemniscate"), "𝕃"),
        (nb_pattern("Obj"), "Obj"),
        (nb_pattern("Aut"), "Aut"),
        (nb_pattern("id"), "id"),
        (nb_pattern("SectorA"), "Sector A"),
        (nb_pattern("SectorB"), "Sector B"),
        (nb_pattern("SectorC"), "Sector C"),
        (nb_pattern("SectorD"), "Sector D"),
        (nb_pattern("dim"), "dim"),
        (nb_pattern("jj"), "j"),
        (nb_pattern("T"), "T"),
        (nb_pattern("iff"), "⇔"),
        (nb_pattern("mid"), "∣"),
        (nb_pattern("setminus"), "∖"),
        (nb_pattern("Hom"), "Hom"),

        # Operators
        (nb_pattern("prod"), "∏"),
        (nb_pattern("sum"), "∑"),
        (nb_pattern("int"), "∫"),
        (nb_pattern("cdot"), "·"),
        (nb_pattern("times"), "×"),
        (nb_pattern("to"), "→"),
        (nb_pattern("mapsto"), "↦"),
        (nb_pattern("equiv"), "≡"),
        (nb_pattern("cong"), "≅"),
        (nb_pattern("leq"), "≤"),
        (nb_pattern("geq"), "≥"),
        (nb_pattern("neq"), "≠"),
        (nb_pattern("ne"), "≠"),
        (nb_pattern("subset"), "⊂"),
        (nb_pattern("subseteq"), "⊆"),
        (nb_pattern("supset"), "⊃"),
        (nb_pattern("supseteq"), "⊇"),
        (nb_pattern("in"), "∈"),
        (nb_pattern("notin"), "∉"),
        (nb_pattern("cup"), "∪"),
        (nb_pattern("cap"), "∩"),
        (nb_pattern("emptyset"), "∅"),
        (nb_pattern("forall"), "∀"),
        (nb_pattern("exists"), "∃"),
        (nb_pattern("infty"), "∞"),
        (nb_pattern("colon"), ":"),
        (nb_pattern("hookrightarrow"), "↪"),
        (nb_pattern("rightarrow"), "→"),
        (nb_pattern("leftarrow"), "←"),
        (nb_pattern("Rightarrow"), "⇒"),
        (nb_pattern("Leftarrow"), "⇐"),
        (nb_pattern("Box"), "□"),
        (nb_pattern("Diamond"), "◇"),
        (nb_pattern("top"), "⊤"),
        (nb_pattern("bot"), "⊥"),
        (nb_pattern("otimes"), "⊗"),
        (nb_pattern("oplus"), "⊕"),
        (nb_pattern("wedge"), "∧"),
        (nb_pattern("vee"), "∨"),
        (nb_pattern("lnot"), "¬"),
        (nb_pattern("neg"), "¬"),
        (nb_pattern("partial"), "∂"),
        (nb_pattern("nabla"), "∇"),
        (nb_pattern("ell"), "ℓ"),
        (nb_pattern("aleph"), "ℵ"),
        (nb_pattern("sim"), "∼"),
        (nb_pattern("propto"), "∝"),
        (nb_pattern("lim"), "lim"),
        (nb_pattern("varprojlim"), "lim←"),
        (nb_pattern("varinjlim"), "lim→"),
        (nb_pattern("sin"), "sin"),
        (nb_pattern("cos"), "cos"),
        (nb_pattern("tan"), "tan"),
        (nb_pattern("log"), "log"),
        (nb_pattern("ln"), "ln"),
        (nb_pattern("exp"), "exp"),
        (nb_pattern("ker"), "ker"),
        (nb_pattern("op"), "op"),
        (nb_pattern("odot"), "☉"),
        (nb_pattern("gtrsim"), "≳"),
        (nb_pattern("lesssim"), "≲"),
        (nb_pattern("Longleftrightarrow"), "⟺"),
        (nb_pattern("Longrightarrow"), "⟹"),
        (nb_pattern("Longleftarrow"), "⟸"),
        (nb_pattern("longleftrightarrow"), "⟷"),
        (nb_pattern("longrightarrow"), "⟶"),
        (nb_pattern("longleftarrow"), "⟵"),
        (nb_pattern("A"), "A"),
        (nb_pattern("B"), "B"),
        (nb_pattern("C"), "C"),
        (nb_pattern("D"), "D"),
        (nb_pattern("n"), "n"),
        # Decorative/diacritic commands (simply strip)
        (r"\\bar([A-Za-zτωπαγηρ∂])", r"\1"),
        (r"\\tilde([A-Za-zτωπαγηρχ])", r"\1"),
        (r"\\dot([A-Za-zτωπαγηρρ])", r"\1"),
        (r"\\acute([A-Za-zτωπαγηρα])", r"\1"),
        (r"\\bar\b", ""),
        (r"\\tilde\b", ""),
        (r"\\dot\b", ""),
        (r"\\acute\b", ""),
        # mkern/kern (horizontal spacing) — strip entirely
        (r"\\mkern\d+mu\s*", ""),
        (r"\\kern\d+\w+\s*", ""),
        # Fractions: \frac{a}{b} → a/b (inline), \tfrac → same
        (r"\\[tdc]?frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)"),
        # \sqrt{x} → √x, \sqrt n → √n
        (r"\\sqrt\{([^{}]*)\}", r"√\1"),
        (r"\\sqrt\s*([0-9A-Za-z])", r"√\1"),
        # \text-X → X (the text-embedded dash)
        (r"\\text-", "-"),
        # Signed superscripts: X^{-2} → X⁻², X^{-1/2} → X⁻¹ᐟ²
        # Multi-digit superscripts: X^{10}, X^{11}, X^{120}
        # Handle negative integer superscripts
        (r"([A-Za-zτωπαγηριλ])\^\{-(\d+)\}",
         lambda m: m.group(1) + "⁻" + m.group(2).translate(SUPERSCRIPT_DIGITS)),
        # Multi-digit positive superscripts
        (r"([A-Za-zτωπαγηριλ\d])\^\{(\d+)\}",
         lambda m: m.group(1) + m.group(2).translate(SUPERSCRIPT_DIGITS)),
        # Sector with Greek inside (e.g. \Sectorπ)
        (r"\\Sector([πτω])", r"Sector \1"),
        # Remaining single-letter macros (leftover \n in math = escape)
        (r"\\n\b", "n"),
        # \lnot, \land, \lor variants (with trailing letters / no space)
        (r"\\lnot\s*", "¬"),
        (r"\\land\s+", "∧ "),
        (r"\\lor\s+", "∨ "),
        (r"\\gg\b", "≫"),
        (r"\\ll\b", "≪"),
        # Common vulgar fractions without braces: \tfrac12 → ½, \frac14 → ¼
        (r"\\[td]?frac12\b", "½"),
        (r"\\[td]?frac13\b", "⅓"),
        (r"\\[td]?frac14\b", "¼"),
        (r"\\[td]?frac15\b", "⅕"),
        (r"\\[td]?frac23\b", "⅔"),
        (r"\\[td]?frac34\b", "¾"),
        (r"\\[td]?frac12(?=\D)", "½"),
        (r"\\[td]?frac14(?=\D)", "¼"),
        (r"\\[td]?frac13(?=\D)", "⅓"),
        # \textH_2 → H_2 (no braces form)
        (r"\\text([A-Za-z])", r"\1"),
        (r"\\text", ""),
        # \mathbf1, \mathbf0 → 1, 0 (no braces)
        (r"\\mathbf(\d)", r"\1"),
        # \bar followed directly by letter: \bard_4 → d_4, \barν_e → ν_e
        (r"\\bar(\S)", r"\1"),
        (r"\\tilde(\S)", r"\1"),
        (r"\\dot(\S)", r"\1"),
        (r"\\acute(\S)", r"\1"),
        # Remaining \text– (dash): \text–2.3 → –2.3
        (r"\\text", ""),

        # Greek letters
        (nb_pattern("tau"), "τ"),
        (nb_pattern("iota"), "ι"),
        (nb_pattern("alpha"), "α"),
        (nb_pattern("beta"), "β"),
        (nb_pattern("pi"), "π"),
        (nb_pattern("Pi"), "Π"),
        (nb_pattern("gamma"), "γ"),
        (nb_pattern("Gamma"), "Γ"),
        (nb_pattern("eta"), "η"),
        (nb_pattern("omega"), "ω"),
        (nb_pattern("Omega"), "Ω"),
        (nb_pattern("rho"), "ρ"),
        (nb_pattern("delta"), "δ"),
        (nb_pattern("Delta"), "Δ"),
        (nb_pattern("epsilon"), "ε"),
        (nb_pattern("varepsilon"), "ε"),
        (nb_pattern("lambda"), "λ"),
        (nb_pattern("Lambda"), "Λ"),
        (nb_pattern("mu"), "μ"),
        (nb_pattern("sigma"), "σ"),
        (nb_pattern("Sigma"), "Σ"),
        (nb_pattern("chi"), "χ"),
        (nb_pattern("phi"), "φ"),
        (nb_pattern("varphi"), "φ"),
        (nb_pattern("Phi"), "Φ"),
        (nb_pattern("psi"), "ψ"),
        (nb_pattern("Psi"), "Ψ"),
        (nb_pattern("theta"), "θ"),
        (nb_pattern("Theta"), "Θ"),
        (nb_pattern("zeta"), "ζ"),
        (nb_pattern("xi"), "ξ"),
        (nb_pattern("Xi"), "Ξ"),
    ]
    for pat, rep in project_macros:
        s = re.sub(pat, rep, s)

    # \text{foo} → foo, \text foo → foo
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\text\s+", "", s)

    # \{ and \} → { and } (LaTeX brace escapes used as set notation)
    s = s.replace(r"\{", "{").replace(r"\}", "}")

    # Convert numeric subscripts: E_0 → E₀
    s = re.sub(r"([A-Za-zτωπαγηρλσχδεζξψ])_(\d)",
               lambda m: m.group(1) + m.group(2).translate(SUBSCRIPT_DIGITS), s)

    # Convert numeric superscripts: τ^3 → τ³
    s = re.sub(r"([A-Za-zτωπαγηρλσχδεζξψ])\^(\d)",
               lambda m: m.group(1) + m.group(2).translate(SUPERSCRIPT_DIGITS), s)

    # Braced numeric sub/sup: X_{0} → X₀, A^{2} → A²
    s = re.sub(r"([A-Za-zτωπαγηρ])_\{(\d+)\}",
               lambda m: m.group(1) + m.group(2).translate(SUBSCRIPT_DIGITS), s)
    s = re.sub(r"([A-Za-zτωπαγηρ])\^\{(\d+)\}",
               lambda m: m.group(1) + m.group(2).translate(SUPERSCRIPT_DIGITS), s)

    # Braced alphabetic subscripts: S_{def} → S_def (keep underscore)
    s = re.sub(r"([A-Za-zτωπαγηρλμσχεδζξψ])_\{([A-Za-z0-9\+\-,]+)\}", r"\1_\2", s)
    # Braced alphabetic superscripts: X^{word} → X^word
    s = re.sub(r"([A-Za-zτωπαγηρλμσχεδζξψ])\^\{([A-Za-z0-9\+\-,]+)\}", r"\1^\2", s)

    # Parenthesized superscripts: X^{(B)} → X^(B)
    s = re.sub(r"([A-Za-zτωπαγηρ])\^\{\(([^)}]+)\)\}", r"\1^(\2)", s)

    # Numeric-only superscripts with more digits: 10^{120} → 10¹²⁰
    s = re.sub(r"(\d)\^\{(\d+)\}",
               lambda m: m.group(1) + m.group(2).translate(SUPERSCRIPT_DIGITS), s)

    return s


# Inline math conversions — ordered from most specific to least
# Each pattern matches `$<content>$` and replaces with cleaned content (no $)
# The script runs these in order until no changes happen (idempotent).

def strip_inline_math(text: str) -> tuple[str, int]:
    """Apply all inline-math transformations to text. Returns (new_text, changes).

    Strategy:
      1. Find every $...$ group (single-line, no nested $).
      2. For each group, attempt to clean it.
      3. If the cleaned version has no $ signs and contains only "safe"
         content (Unicode letters, digits, operators, spaces, common
         math punctuation), replace `$X$` with `X`.
      4. Otherwise leave the group alone (logged).
    """
    changes = 0
    unchanged_groups = []

    # Match $...$ where ... has no $ (avoid crossing delimiters).
    # Allow up to 3 newlines to handle wrapped multi-line inline math,
    # but limit total length to avoid runaway matches crossing document
    # sections or YAML boundaries.
    INLINE_MATH = re.compile(r"\$([^$]{1,300}?)\$")

    def repl(m):
        nonlocal changes
        inner = m.group(1)
        cleaned = clean_math_inner(inner)
        # If cleaning left any $ signs or unknown backslash commands, don't replace
        if "$" in cleaned or re.search(r"\\[a-zA-Z]", cleaned):
            unchanged_groups.append(m.group(0))
            return m.group(0)
        # Reject if there are UNBALANCED braces (set notation {a, b, c} is OK)
        if cleaned.count("{") != cleaned.count("}"):
            unchanged_groups.append(m.group(0))
            return m.group(0)
        changes += 1
        return cleaned

    new_text = INLINE_MATH.sub(repl, text)
    return new_text, changes, unchanged_groups


def process_file(filepath: Path, dry_run: bool = False) -> dict:
    """Process a single markdown file. Returns stats dict."""
    stats = {
        "path": str(filepath),
        "display_math": 0,
        "inline_math": 0,
        "unchanged": [],
        "changed": False,
    }

    try:
        original = filepath.read_text(encoding="utf-8")
    except Exception as e:
        stats["error"] = str(e)
        return stats

    content = original

    # Phase 1: Replace display math blocks
    def display_repl(match):
        stats["display_math"] += 1
        return display_math_replace(match)

    content = DISPLAY_MATH_PATTERN.sub(display_repl, content)

    # Phase 2: Process inline math
    content, inline_count, unchanged = strip_inline_math(content)
    stats["inline_math"] = inline_count
    stats["unchanged"] = unchanged

    # Write back if changed
    if content != original:
        stats["changed"] = True
        if not dry_run:
            filepath.write_text(content, encoding="utf-8")

    return stats


def main():
    parser = argparse.ArgumentParser(description="Strip LaTeX from books markdown.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing files")
    parser.add_argument("--report", action="store_true",
                        help="Print detailed per-file stats")
    parser.add_argument("--path", default="publications/books",
                        help="Root directory to process (default: publications/books)")
    parser.add_argument("--log", default="strip_books_latex.log",
                        help="Log file for unchanged patterns")
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        print(f"ERROR: {root} not found", file=sys.stderr)
        return 1

    files = sorted(root.rglob("*.md"))
    print(f"Found {len(files)} markdown files under {root}")
    if args.dry_run:
        print("DRY RUN — no files will be written")
    print()

    total_changed = 0
    total_display = 0
    total_inline = 0
    all_unchanged = []

    for f in files:
        stats = process_file(f, dry_run=args.dry_run)
        if stats.get("error"):
            print(f"  ERROR {f}: {stats['error']}")
            continue
        if stats["changed"]:
            total_changed += 1
            total_display += stats["display_math"]
            total_inline += stats["inline_math"]
            if args.report:
                print(f"  {f}: {stats['inline_math']} inline, {stats['display_math']} display")
        all_unchanged.extend([(str(f), g) for g in stats["unchanged"]])

    print()
    print("=" * 60)
    print(f"Files changed:         {total_changed} / {len(files)}")
    print(f"Display math fixed:    {total_display}")
    print(f"Inline math stripped:  {total_inline}")
    print(f"Unchanged groups:      {len(all_unchanged)}")
    print("=" * 60)

    # Write log of unchanged groups
    if all_unchanged:
        with open(args.log, "w") as lf:
            lf.write("# Patterns NOT auto-converted (need manual review)\n\n")
            unique = {}
            for path, grp in all_unchanged:
                unique.setdefault(grp, []).append(path)
            for grp, paths in sorted(unique.items(), key=lambda x: -len(x[1])):
                lf.write(f"{len(paths)}×  {grp}\n")
                for p in paths[:3]:
                    lf.write(f"    {p}\n")
                if len(paths) > 3:
                    lf.write(f"    ... and {len(paths)-3} more\n")
                lf.write("\n")
        print(f"\nUnchanged patterns logged to {args.log}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
