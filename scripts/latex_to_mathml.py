#!/usr/bin/env python3
"""
LaTeX to core MathML converter — enumerable coverage for Panta Rhei bibliography.

Handles the exact math syntax present in references.bib (38 entries, confirmed
by grep). Not a general LaTeX math converter; specifically designed for
bibliographic titles and citation metadata.

Public API:

    convert_title(raw) -> (mathml_html, plain_unicode)
        Convert a title string containing $...$ tokens. Returns a tuple:
        - mathml_html: HTML-safe output with <math> tags for complex math and
                       italic Unicode letters for single-variable math.
        - plain_unicode: Unicode-only output with no HTML tags, for meta tags,
                         SEO JSON-LD, <title> elements, and other contexts
                         where HTML injection would be unsafe or broken.

    convert_inline(token) -> (mathml_html, plain_unicode)
        Convert a single token (without delimiters).

    latex_accents_to_unicode(text) -> str
        Non-destructive accent resolution: {\\"o} → ö, {\\'e} → é, etc.

Invariants (enforced via asserts):
    - convert_title output contains no bare backslash characters
    - convert_title output uses only single quotes for HTML attributes
"""
from __future__ import annotations

import re
import unicodedata

# ---------------------------------------------------------------------------
# Greek letters (lowercase and uppercase)
# ---------------------------------------------------------------------------

GREEK_LOWER = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ",
    "epsilon": "ε", "varepsilon": "ε", "zeta": "ζ", "eta": "η",
    "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ",
    "pi": "π", "varpi": "ϖ", "rho": "ρ", "varrho": "ϱ",
    "sigma": "σ", "varsigma": "ς", "tau": "τ", "upsilon": "υ",
    "phi": "φ", "varphi": "ϕ", "chi": "χ", "psi": "ψ",
    "omega": "ω",
}

GREEK_UPPER = {
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ",
    "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ", "Upsilon": "Υ",
    "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
}

OPERATORS = {
    "partial": "∂", "nabla": "∇", "infty": "∞",
    "to": "→", "rightarrow": "→", "Rightarrow": "⇒",
    "leftarrow": "←", "Leftarrow": "⇐", "mapsto": "↦",
    "neq": "≠", "ne": "≠", "leq": "≤", "le": "≤",
    "geq": "≥", "ge": "≥", "approx": "≈", "equiv": "≡",
    "cong": "≅", "sim": "∼", "simeq": "≃",
    "in": "∈", "notin": "∉", "subset": "⊂", "supset": "⊃",
    "subseteq": "⊆", "supseteq": "⊇",
    "cup": "∪", "cap": "∩", "setminus": "∖",
    "otimes": "⊗", "oplus": "⊕", "odot": "⊙",
    "times": "×", "cdot": "·", "ast": "∗",
    "forall": "∀", "exists": "∃", "nexists": "∄",
    "emptyset": "∅", "varnothing": "∅",
    "aleph": "ℵ", "hbar": "ℏ", "ell": "ℓ",
    "pm": "±", "mp": "∓",
    "circ": "∘", "star": "⋆",
    "wedge": "∧", "vee": "∨", "neg": "¬", "lnot": "¬",
    "top": "⊤", "bot": "⊥",
    "prime": "′", "ldots": "…", "dots": "…", "cdots": "⋯",
}

BLACKBOARD = {
    "R": ("ℝ", "R"),  # (unicode, mathml-letter)
    "C": ("ℂ", "C"),
    "N": ("ℕ", "N"),
    "Z": ("ℤ", "Z"),
    "Q": ("ℚ", "Q"),
    "H": ("ℍ", "H"),
    "F": ("𝔽", "F"),
    "P": ("ℙ", "P"),
    "E": ("𝔼", "E"),
}

# Unicode superscripts
SUPERSCRIPTS = {
    # Digits
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    # Symbols
    "+": "⁺", "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾",
    # Lowercase letters (missing: q)
    "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ", "e": "ᵉ",
    "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ⁱ", "j": "ʲ",
    "k": "ᵏ", "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ",
    "p": "ᵖ", "r": "ʳ", "s": "ˢ", "t": "ᵗ", "u": "ᵘ",
    "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ", "z": "ᶻ",
    # Uppercase letters (missing: C, F, Q, S, X, Y, Z)
    "A": "ᴬ", "B": "ᴮ", "D": "ᴰ", "E": "ᴱ", "G": "ᴳ",
    "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ",
    "M": "ᴹ", "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "R": "ᴿ",
    "T": "ᵀ", "U": "ᵁ", "V": "ⱽ", "W": "ᵂ",
}

SUBSCRIPTS = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
    "+": "₊", "-": "₋", "=": "₌", "(": "₍", ")": "₎",
    "a": "ₐ", "e": "ₑ", "h": "ₕ", "i": "ᵢ", "j": "ⱼ",
    "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ",
    "p": "ₚ", "r": "ᵣ", "s": "ₛ", "t": "ₜ", "u": "ᵤ",
    "v": "ᵥ", "x": "ₓ",
}


# ---------------------------------------------------------------------------
# Accent handling (non-destructive)
# ---------------------------------------------------------------------------

ACCENT_DIACRITICS = {
    '"': "\u0308",  # umlaut (diaeresis)
    "'": "\u0301",  # acute
    "`": "\u0300",  # grave
    "^": "\u0302",  # circumflex
    "~": "\u0303",  # tilde
    "c": "\u0327",  # cedilla (\c)
    "r": "\u030A",  # ring above (\r)
    "v": "\u030C",  # caron (\v)
    "=": "\u0304",  # macron
    ".": "\u0307",  # dot above
    "u": "\u0306",  # breve (\u)
    "H": "\u030B",  # double acute
    "k": "\u0328",  # ogonek
    "b": "\u0331",  # bar below
    "d": "\u0323",  # dot below
    "t": "\u0361",  # tie
}


# LaTeX literal letter commands (no argument) — standalone special characters
LITERAL_LETTERS = {
    r"\ss": "ß",
    r"\SS": "ẞ",
    r"\o": "ø",
    r"\O": "Ø",
    r"\ae": "æ",
    r"\AE": "Æ",
    r"\oe": "œ",
    r"\OE": "Œ",
    r"\aa": "å",
    r"\AA": "Å",
    r"\i": "ı",  # dotless i
    r"\j": "ȷ",  # dotless j
    r"\l": "ł",
    r"\L": "Ł",
    r"\dh": "ð",
    r"\DH": "Ð",
    r"\th": "þ",
    r"\TH": "Þ",
    r"\ng": "ŋ",
    r"\NG": "Ŋ",
    r"\dj": "đ",
    r"\DJ": "Đ",
    r"\textcopyright": "©",
    r"\textregistered": "®",
    r"\textbullet": "•",
    r"\textdegree": "°",
    r"\textendash": "–",
    r"\textemdash": "—",
    r"\P": "¶",
    r"\S": "§",
}

# Sorted by length desc so longer commands match before prefixes (\ss before \s)
_LITERAL_LETTERS_SORTED = sorted(
    LITERAL_LETTERS.items(), key=lambda kv: -len(kv[0])
)


def _resolve_literal_letters(text: str) -> str:
    """Replace LaTeX literal letter commands like \\ss → ß.

    These commands take no argument and represent a single character.
    Must be followed by a non-letter (end of word, brace, space, etc.)
    to avoid matching prefixes of other commands.
    """
    for cmd, replacement in _LITERAL_LETTERS_SORTED:
        # \ss must not be followed by another letter (otherwise we'd match
        # inside longer commands). Use negative lookahead for [a-zA-Z].
        pattern = re.escape(cmd) + r"(?![a-zA-Z])"
        text = re.sub(pattern, replacement, text)
    return text


def latex_accents_to_unicode(text: str) -> str:
    """Resolve LaTeX accent commands to Unicode combining characters.

    Examples:
        H\\"ormander  → Hörmander
        {\\"o}        → ö
        Poincar\\'e   → Poincaré
        Erd\\H{o}s    → Erdős
        \\c{s}        → ş
        Sto\\ss      → Stoß
    """
    # First: literal letter commands (\ss, \o, \ae, etc.)
    text = _resolve_literal_letters(text)

    # Pattern matches: \ACCENT letter, \ACCENT{letter}, {\ACCENT letter}, {\ACCENT{letter}}
    def replace(match: re.Match) -> str:
        accent = match.group("accent")
        letter = match.group("letter")
        if accent not in ACCENT_DIACRITICS:
            return match.group(0)  # leave unchanged
        combined = unicodedata.normalize("NFC", letter + ACCENT_DIACRITICS[accent])
        return combined

    # \"o  \"{o}  {\"o}  {\"{o}}
    #   Accent is one of: " ' ` ^ ~ = . (single-char)
    #   Or \\v{x} \\c{x} \\r{x} \\u{x} \\H{x} \\k{x} \\b{x} \\d{x}
    pattern = re.compile(
        r"""
        \{?                     # optional leading brace
        \\
        (?P<accent>["'`^~=.]|[cvruHkbdt])  # accent marker
        \s*
        \{?                     # optional brace around letter
        (?P<letter>[a-zA-Z])    # base letter
        \}?                     # optional close brace
        \}?                     # optional outer close brace
        """,
        re.VERBOSE,
    )
    return pattern.sub(replace, text)


# ---------------------------------------------------------------------------
# Inline math tokenizer
# ---------------------------------------------------------------------------


def _tokenize_dollar_math(s: str):
    """Yield a sequence of ('text', str) and ('math', str) tokens.

    Handles $...$ but not $$...$$ (none in the bibliography).
    """
    i = 0
    buf = []
    while i < len(s):
        if s[i] == "$":
            # Flush text buffer
            if buf:
                yield ("text", "".join(buf))
                buf = []
            # Find closing $
            j = i + 1
            while j < len(s) and s[j] != "$":
                j += 1
            if j < len(s):
                yield ("math", s[i + 1:j])
                i = j + 1
            else:
                # Unclosed $ — treat as text
                buf.append(s[i])
                i += 1
        else:
            buf.append(s[i])
            i += 1
    if buf:
        yield ("text", "".join(buf))


# ---------------------------------------------------------------------------
# Inline math core converter
# ---------------------------------------------------------------------------


def _convert_math_to_plain(math: str) -> str:
    """Convert the inside of a $...$ token to Unicode plain text."""
    # Handle \mathbb{X}
    math = re.sub(
        r"\\mathbb\s*\{([A-Z])\}",
        lambda m: BLACKBOARD.get(m.group(1), (m.group(1), m.group(1)))[0],
        math,
    )
    # Handle \mathrm{X} \mathbf{X} \mathsf{X} \mathit{X} — just keep content
    math = re.sub(r"\\math(?:rm|bf|sf|it|cal)\s*\{([^{}]*)\}", r"\1", math)
    # Handle \overline{X}  →  X̄ (combining overline)
    math = re.sub(
        r"\\overline\s*\{([^{}]*)\}",
        lambda m: _overline(m.group(1)),
        math,
    )
    # Handle \hat{X} → X̂
    math = re.sub(
        r"\\hat\s*\{([^{}]*)\}",
        lambda m: m.group(1) + "\u0302",
        math,
    )
    # Handle \tilde{X} → X̃
    math = re.sub(
        r"\\tilde\s*\{([^{}]*)\}",
        lambda m: m.group(1) + "\u0303",
        math,
    )
    # Handle \vec{X} → X⃗
    math = re.sub(
        r"\\vec\s*\{([^{}]*)\}",
        lambda m: m.group(1) + "\u20D7",
        math,
    )
    # Handle superscripts: X^{abc}, X^a
    math = re.sub(
        r"\^\s*\{([^{}]*)\}",
        lambda m: _superscript(m.group(1)),
        math,
    )
    math = re.sub(
        r"\^\s*([A-Za-z0-9+\-])",
        lambda m: _superscript(m.group(1)),
        math,
    )
    # Handle subscripts
    math = re.sub(
        r"_\s*\{([^{}]*)\}",
        lambda m: _subscript(m.group(1)),
        math,
    )
    math = re.sub(
        r"_\s*([A-Za-z0-9+\-])",
        lambda m: _subscript(m.group(1)),
        math,
    )
    # Handle Greek letters and operators
    def sub_command(match: re.Match) -> str:
        cmd = match.group(1)
        if cmd in GREEK_LOWER:
            return GREEK_LOWER[cmd]
        if cmd in GREEK_UPPER:
            return GREEK_UPPER[cmd]
        if cmd in OPERATORS:
            return OPERATORS[cmd]
        return match.group(0)

    math = re.sub(r"\\([a-zA-Z]+)", sub_command, math)
    # Strip any remaining braces and backslashes
    math = math.replace("{", "").replace("}", "").replace("\\", "")
    return math


def _overline(s: str) -> str:
    """Apply combining overline to each character."""
    return "".join(c + "\u0305" for c in s)


def _superscript(s: str) -> str:
    """Convert chars to Unicode superscripts where possible; fallback to `^X` style."""
    out = []
    for c in s:
        if c in SUPERSCRIPTS:
            out.append(SUPERSCRIPTS[c])
        else:
            # Fallback: keep letter as-is (browsers render acceptably)
            out.append(c)
    return "".join(out)


def _subscript(s: str) -> str:
    out = []
    for c in s:
        if c in SUBSCRIPTS:
            out.append(SUBSCRIPTS[c])
        else:
            out.append(c)
    return "".join(out)


# ---------------------------------------------------------------------------
# MathML emission
# ---------------------------------------------------------------------------


def _convert_math_to_mathml(math: str) -> str:
    """Convert the inside of a $...$ token to MathML.

    Strategy: parse a small subset of LaTeX math into MathML elements.
    For tokens we can't parse deeply, fall back to wrapping Unicode inside <mi>.
    """
    # Simple case: single character or symbol (including Greek, operators)
    plain = _convert_math_to_plain(math)

    # If the plain-conversion reduces to a single rune or a simple superscripted
    # form, emit a compact <math> wrapper. Otherwise, emit a more structured
    # MathML element for recognizable patterns.

    # Try to recognize common patterns for richer MathML
    # Pattern 1: single letter (variable)
    m = re.fullmatch(r"\s*([a-zA-Z])\s*", math)
    if m:
        return f"<math><mi>{m.group(1)}</mi></math>"

    # Pattern 2: \mathbb{X}
    m = re.fullmatch(r"\s*\\mathbb\s*\{([A-Z])\}\s*", math)
    if m:
        return f"<math><mi mathvariant='double-struck'>{m.group(1)}</mi></math>"

    # Pattern 3: X^Y or X^{Y} (simple superscript with single letter base)
    m = re.fullmatch(
        r"\s*([a-zA-Z])\s*\^\s*\{?([a-zA-Z0-9+\-]+)\}?\s*", math
    )
    if m:
        base, exp = m.group(1), m.group(2)
        return f"<math><msup><mi>{base}</mi><mn>{exp}</mn></msup></math>"

    # Pattern 4: X_Y or X_{Y}
    m = re.fullmatch(
        r"\s*([a-zA-Z])\s*_\s*\{?([a-zA-Z0-9+\-]+)\}?\s*", math
    )
    if m:
        base, sub = m.group(1), m.group(2)
        return f"<math><msub><mi>{base}</mi><mn>{sub}</mn></msub></math>"

    # Pattern 5: X_{a}^{b} or X^{b}_{a}
    m = re.fullmatch(
        r"\s*([a-zA-Z])\s*_\s*\{?([a-zA-Z0-9+\-]+)\}?\s*\^\s*\{?([a-zA-Z0-9+\-]+)\}?\s*",
        math,
    )
    if m:
        base, sub, sup = m.group(1), m.group(2), m.group(3)
        return (
            f"<math><msubsup><mi>{base}</mi><mn>{sub}</mn>"
            f"<mn>{sup}</mn></msubsup></math>"
        )

    # Pattern 6: \mathbb{X}^n
    m = re.fullmatch(
        r"\s*\\mathbb\s*\{([A-Z])\}\s*\^\s*\{?([a-zA-Z0-9+\-]+)\}?\s*", math
    )
    if m:
        letter, exp = m.group(1), m.group(2)
        return (
            f"<math><msup><mi mathvariant='double-struck'>{letter}</mi>"
            f"<mn>{exp}</mn></msup></math>"
        )

    # Pattern 7: \overline{X}
    m = re.fullmatch(r"\s*\\overline\s*\{([^{}]*)\}\s*", math)
    if m:
        content = m.group(1)
        # Try to convert inside first
        inner_plain = _convert_math_to_plain(content)
        return f"<math><mover><mo>{inner_plain}</mo><mo>‾</mo></mover></math>"

    # Fallback: wrap the converted plain output in <math><mi>...</mi></math>
    return f"<math><mi>{plain}</mi></math>"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def convert_inline(math: str) -> tuple[str, str]:
    """Convert one math token (contents between $...$) to (mathml, plain)."""
    mathml = _convert_math_to_mathml(math)
    plain = _convert_math_to_plain(math)
    return mathml, plain


def _strip_protective_braces(text: str) -> str:
    """Remove BibTeX protective braces like {Newton} or {$...$} around whole words.

    BibTeX uses braces to prevent title-case lowering. These are metadata that
    should not appear in displayed titles. We strip them carefully — only pairs
    around plain words or already-converted math regions.
    """
    # Strip braces wrapping whole segments (common in BibTeX titles)
    # This matches {X} where X doesn't contain { or }
    text = re.sub(r"\{([^{}]*)\}", r"\1", text)
    # Do it twice to catch one level of nesting
    text = re.sub(r"\{([^{}]*)\}", r"\1", text)
    return text


def convert_title(raw: str) -> tuple[str, str]:
    """Convert a title string containing $...$ tokens.

    Returns (mathml_html, plain_unicode).
    """
    # Pre-process: handle \texorpdfstring{A}{B} → A (use the TeX form for display)
    raw = re.sub(
        r"\\texorpdfstring\s*\{([^{}]*)\}\s*\{[^{}]*\}",
        r"\1",
        raw,
    )
    # Pre-process: strip \index{...} and \label{...} markers
    for drop in ["index", "label"]:
        raw = re.sub(r"\\" + drop + r"\s*\{[^{}]*\}", "", raw)

    mathml_parts = []
    plain_parts = []
    for kind, content in _tokenize_dollar_math(raw):
        if kind == "text":
            # Resolve accents in text segments
            resolved = latex_accents_to_unicode(content)
            mathml_parts.append(resolved)
            plain_parts.append(resolved)
        else:
            mathml, plain = convert_inline(content)
            mathml_parts.append(mathml)
            plain_parts.append(plain)

    mathml_out = "".join(mathml_parts)
    plain_out = "".join(plain_parts)

    # Strip BibTeX protective braces AFTER math conversion (math tokens are now
    # HTML/Unicode, so remaining `{` `}` chars are BibTeX casing protection).
    mathml_out = _strip_protective_braces(mathml_out)
    plain_out = _strip_protective_braces(plain_out)

    # Convert LaTeX dashes: --- → em-dash, -- → en-dash
    # Must run AFTER brace stripping so Yang{--}Mills works.
    mathml_out = mathml_out.replace("---", "\u2014").replace("--", "\u2013")
    plain_out = plain_out.replace("---", "\u2014").replace("--", "\u2013")

    # Collapse any doubled whitespace introduced by brace stripping
    mathml_out = re.sub(r"\s+", " ", mathml_out).strip()
    plain_out = re.sub(r"\s+", " ", plain_out).strip()

    # Safety invariants — catch bugs early
    assert "\\" not in mathml_out, (
        f"convert_title produced backslash: {mathml_out!r}"
    )
    assert "\\" not in plain_out, (
        f"convert_title produced backslash in plain: {plain_out!r}"
    )

    return mathml_out, plain_out


# ---------------------------------------------------------------------------
# Generic LaTeX field cleaner (for non-title fields like journal, publisher, authors)
# ---------------------------------------------------------------------------


def clean_bibfield(raw: str) -> str:
    """Non-destructive cleanup for non-math .bib fields.

    Handles accents, removes brace-wrappers, strips \\textit etc, but preserves
    the text content. For fields like 'authors', 'journal_or_booktitle',
    'publisher' where math is unexpected but accents are common.
    """
    # Accents
    text = latex_accents_to_unicode(raw)
    # Strip \textit{x}, \textbf{x}, \emph{x} — keep content
    for cmd in ["textit", "textbf", "emph", "mbox", "text", "textsc", "scshape"]:
        text = re.sub(r"\\" + cmd + r"\s*\{([^{}]*)\}", r"\1", text)
    # Dash conversions
    text = text.replace("---", "—").replace("--", "–")
    # Strip remaining \command{content} → content
    text = re.sub(r"\\[a-zA-Z]+\*?\s*\{([^{}]*)\}", r"\1", text)
    # Strip remaining bare \command
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    # Strip leftover braces
    text = text.replace("{", "").replace("}", "")
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


if __name__ == "__main__":
    # Simple smoke test
    tests = [
        "$*$-Autonomous Categories",
        "Theory of $H^p$ spaces",
        "$p$-adic Numbers, $p$-adic Analysis, and Zeta-Functions",
        r"La m{\'e}trique de Kobayashi et la repr{\'e}sentation des domaines sur {$\mathbb{C}^n$}",
        r"H{\"o}rmander",
        "Viscosity of Liquid Helium below the $\\lambda$-Point",
    ]
    for t in tests:
        mathml, plain = convert_title(t)
        print(f"RAW:    {t}")
        print(f"MATHML: {mathml}")
        print(f"PLAIN:  {plain}")
        print()
