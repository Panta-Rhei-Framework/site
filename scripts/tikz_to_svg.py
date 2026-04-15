#!/usr/bin/env python3
"""
TikZ → SVG Conversion Pipeline for Framework Module Diagrams

Extracts a specific figure (by label) from a book LaTeX chapter file,
wraps it in a standalone document with shared styles, compiles it with
lualatex, and converts the resulting PDF to SVG via pdf2svg.

Single-diagram usage:
    python3 scripts/tikz_to_svg.py \\
        --tex-file /path/to/ch01-five-generators.tex \\
        --label fig:bookI-ch01-generators-order \\
        --output assets/diagrams/framework/book-i/my-diagram.svg

Batch mode (reads mapping JSON):
    python3 scripts/tikz_to_svg.py --mapping scripts/framework-diagrams-mapping.json
    python3 scripts/tikz_to_svg.py --mapping ... --book I    # only book I
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
STANDALONE_STYLES = SCRIPT_DIR / "tikz-standalone-styles.tex"
SITE_ROOT = SCRIPT_DIR.parent.resolve()
BOOKS_ROOT = Path("/Users/thorfuchs/Books/PantaRhei-2ndEd")

STANDALONE_TEMPLATE = r"""\documentclass[tikz,border=4pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{tikz-cd}
\usetikzlibrary{positioning,calc,shapes.geometric,arrows.meta,matrix,decorations.pathreplacing,decorations.markings}
\input{%(styles)s}
\begin{document}
%(body)s
\end{document}
"""


class ConversionError(Exception):
    """Raised when any step in the pipeline fails."""


def extract_figure_block(tex_path: Path, label: str) -> str:
    """Find the \\begin{figure}...\\end{figure} block containing the given label.

    Returns the full figure block as a string. Raises if not found.
    """
    text = tex_path.read_text(encoding="utf-8")

    # Find all figure environments
    figure_pattern = re.compile(
        r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}",
        re.DOTALL,
    )
    for match in figure_pattern.finditer(text):
        block = match.group(0)
        if f"\\label{{{label}}}" in block:
            return block

    raise ConversionError(
        f"Figure label '{label}' not found in {tex_path}"
    )


def extract_tikzpicture(figure_block: str) -> str:
    """Extract the \\begin{tikzpicture}...\\end{tikzpicture} portion from a figure block.

    If the figure contains a tikz-cd block, use that instead.
    """
    # Prefer tikzpicture if present
    tikz_pattern = re.compile(
        r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
        re.DOTALL,
    )
    tikz_match = tikz_pattern.search(figure_block)
    if tikz_match:
        return tikz_match.group(0)

    # Fall back to tikzcd
    tikzcd_pattern = re.compile(
        r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}",
        re.DOTALL,
    )
    tikzcd_match = tikzcd_pattern.search(figure_block)
    if tikzcd_match:
        return tikzcd_match.group(0)

    raise ConversionError("No tikzpicture or tikzcd environment found in figure block")


def compile_standalone(tikz_body: str, work_dir: Path) -> Path:
    """Compile a standalone .tex file containing tikz_body. Returns path to PDF."""
    tex_file = work_dir / "diagram.tex"
    content = STANDALONE_TEMPLATE % {
        "styles": str(STANDALONE_STYLES).replace("\\", "/"),
        "body": tikz_body,
    }
    tex_file.write_text(content, encoding="utf-8")

    result = subprocess.run(
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "diagram.tex"],
        cwd=work_dir,
        capture_output=True,
        text=True,
    )

    pdf_file = work_dir / "diagram.pdf"
    if not pdf_file.exists():
        # Show last 30 lines of output for diagnostics
        tail = "\n".join(result.stdout.splitlines()[-30:])
        raise ConversionError(
            f"lualatex failed to produce PDF:\n{tail}"
        )

    return pdf_file


def pdf_to_svg(pdf_file: Path, output_svg: Path) -> None:
    """Convert PDF to SVG using pdf2svg."""
    output_svg.parent.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        ["pdf2svg", str(pdf_file), str(output_svg)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0 or not output_svg.exists():
        raise ConversionError(
            f"pdf2svg failed: {result.stderr}\n{result.stdout}"
        )


def optimize_svg(svg_file: Path) -> None:
    """Light optimization: strip extraneous whitespace and comments."""
    content = svg_file.read_text(encoding="utf-8")
    # Remove XML comments
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    # Collapse blank lines
    content = re.sub(r"\n\s*\n", "\n", content)
    svg_file.write_text(content.strip() + "\n", encoding="utf-8")


def convert_one(tex_file: Path, label: str, output_svg: Path, verbose: bool = True) -> None:
    """Run the full pipeline for a single diagram."""
    if not tex_file.exists():
        raise ConversionError(f"Source .tex not found: {tex_file}")
    if not STANDALONE_STYLES.exists():
        raise ConversionError(f"Standalone styles not found: {STANDALONE_STYLES}")

    if verbose:
        print(f"  Extracting {label} from {tex_file.name}")

    figure_block = extract_figure_block(tex_file, label)
    tikz_body = extract_tikzpicture(figure_block)

    with tempfile.TemporaryDirectory() as tmp:
        work_dir = Path(tmp)
        if verbose:
            print(f"  Compiling with lualatex...")
        pdf_file = compile_standalone(tikz_body, work_dir)

        if verbose:
            print(f"  Converting PDF → SVG...")
        pdf_to_svg(pdf_file, output_svg)

    optimize_svg(output_svg)

    size = output_svg.stat().st_size
    if verbose:
        try:
            rel = output_svg.resolve().relative_to(SITE_ROOT)
            display = str(rel)
        except ValueError:
            display = str(output_svg)
        print(f"  ✓ {display} ({size:,} bytes)")


def resolve_tex_path(tex_ref: str) -> Path:
    """Resolve a tex file reference to an absolute path.

    Accepts: absolute paths, or relative paths starting with 'books/'.
    """
    if tex_ref.startswith("/"):
        return Path(tex_ref)
    if tex_ref.startswith("books/"):
        return BOOKS_ROOT / tex_ref
    # Try both interpretations
    abs_path = Path(tex_ref)
    if abs_path.exists():
        return abs_path
    books_path = BOOKS_ROOT / tex_ref
    if books_path.exists():
        return books_path
    raise ConversionError(f"Cannot resolve tex file path: {tex_ref}")


def svg_path_for(module_slug: str, book: str, label: str) -> tuple[Path, str]:
    """Return (absolute_path, web_path) for a diagram SVG."""
    book_dir_name = f"book-{book.lower()}"
    short_id = re.sub(r"^fig:book[IVX]+-ch\d+-", "", label)
    filename = f"{module_slug}-{short_id}.svg"
    abs_path = SITE_ROOT / "assets" / "diagrams" / "framework" / book_dir_name / filename
    web_path = f"/assets/diagrams/framework/{book_dir_name}/{filename}"
    return abs_path, web_path


ROMAN_TO_INT = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7}


def derive_source_citation(tex_file: str) -> str:
    """Derive a human-readable source citation from a tex path.

    Example: 'books/I-CategoricalFoundations/latex/sections/part01/ch06-generative-act.tex'
    → 'Book I, Chapter 6'
    """
    # Match book number via the I-… prefix of the top-level directory
    book_match = re.search(r"books/([IVX]+)-", tex_file)
    book = book_match.group(1) if book_match else "?"
    # Match chapter number from chNN- pattern
    chap_match = re.search(r"/ch(\d+)-", tex_file)
    chapter = int(chap_match.group(1)) if chap_match else 0
    return f"Book {book}, Chapter {chapter}"


def derive_alt_text(caption: str, max_len: int = 160) -> str:
    """Short alt text derived from the caption, truncated cleanly."""
    # Strip markdown/LaTeX remnants and collapse whitespace
    alt = re.sub(r"\s+", " ", caption).strip()
    if len(alt) <= max_len:
        return alt
    # Truncate at a word boundary, append ellipsis
    truncated = alt[: max_len - 1].rsplit(" ", 1)[0]
    return truncated + "…"


def update_module_frontmatter(module_slug: str, new_diagrams: list) -> bool:
    """Update (or insert) the `diagrams:` field in a framework module's frontmatter.

    Idempotent: replaces existing `diagrams:` block if present.

    Returns True if the file was modified.
    """
    module_file = SITE_ROOT / "_framework" / f"{module_slug}.md"
    if not module_file.exists():
        raise ConversionError(f"Module file not found: {module_file}")

    text = module_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ConversionError(f"Module file missing frontmatter: {module_file}")

    # Find frontmatter bounds
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        raise ConversionError(f"Module file missing closing frontmatter: {module_file}")
    frontmatter = text[4:end_idx]  # between --- markers
    body = text[end_idx + 5:]  # after closing ---\n

    # Remove any existing diagrams: block
    # The block starts with "diagrams:\n" and includes subsequent lines indented with spaces
    lines = frontmatter.split("\n")
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^diagrams:\s*$", line) or re.match(r"^diagrams:\s*\[\]\s*$", line):
            # Skip this line
            i += 1
            # Skip subsequent indented block
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("- ") or lines[i].strip() == ""):
                # Stop at next non-indented field
                if lines[i].strip() == "" and i + 1 < len(lines) and not lines[i + 1].startswith(("  ", "-")):
                    break
                if lines[i] and not lines[i].startswith(" ") and not lines[i].startswith("-"):
                    break
                i += 1
            continue
        new_lines.append(line)
        i += 1
    frontmatter = "\n".join(new_lines)

    # Build the new diagrams block
    diagram_lines = ["diagrams:"]
    for d in new_diagrams:
        diagram_lines.append(f"- src: {d['src']}")
        # Caption: use double quotes, escape any embedded double quotes
        caption_escaped = d["caption"].replace("\\", "\\\\").replace('"', '\\"')
        diagram_lines.append(f'  caption: "{caption_escaped}"')
        alt_escaped = d["alt"].replace("\\", "\\\\").replace('"', '\\"')
        diagram_lines.append(f'  alt: "{alt_escaped}"')
        diagram_lines.append(f'  source: "{d["source"]}"')
        diagram_lines.append(f'  label: "{d["label"]}"')
    diagrams_block = "\n".join(diagram_lines)

    # Insert diagrams block after summary_short: line (or after thesis: if summary_short is missing)
    # Use regex to find either line and insert after its (possibly multi-line) value
    insertion_done = False

    # Try to insert after summary_short (which may span multiple lines in YAML)
    fm_lines = frontmatter.split("\n")
    result_lines = []
    i = 0
    while i < len(fm_lines):
        result_lines.append(fm_lines[i])
        if fm_lines[i].startswith("summary_short:") and not insertion_done:
            # Skip continuation lines (indented)
            j = i + 1
            while j < len(fm_lines) and (fm_lines[j].startswith("  ") and not fm_lines[j].startswith("  -")):
                result_lines.append(fm_lines[j])
                j += 1
            # Now insert diagrams block
            result_lines.append(diagrams_block)
            insertion_done = True
            i = j
            continue
        i += 1

    if not insertion_done:
        raise ConversionError(f"Could not find summary_short: field in {module_file}")

    new_frontmatter = "\n".join(result_lines)
    new_text = f"---\n{new_frontmatter}\n---\n{body}"
    module_file.write_text(new_text, encoding="utf-8")
    return True


def convert_mapping(mapping_file: Path, book_filter: str = None, wire: bool = True) -> dict:
    """Process a batch mapping file. Returns stats dict.

    If wire=True, also updates each affected module's frontmatter with the
    diagrams: field pointing at the newly generated SVGs.
    """
    mapping = json.loads(mapping_file.read_text(encoding="utf-8"))

    stats = {"total": 0, "succeeded": 0, "failed": 0, "modules_wired": 0, "errors": []}

    for module_slug, module_data in mapping.items():
        if module_slug.startswith("_"):  # skip _metadata keys
            continue
        if book_filter and module_data.get("source_book") != book_filter:
            continue
        if module_data.get("status") == "done-in-phase-1":
            continue

        diagrams = module_data.get("diagrams", [])
        if not diagrams:
            continue

        book = module_data["source_book"]
        module_succeeded = True
        wired_entries = []

        for idx, diag in enumerate(diagrams):
            stats["total"] += 1
            label = diag["label"]
            output_file, web_path = svg_path_for(module_slug, book, label)

            try:
                tex_path = resolve_tex_path(diag["tex_file"])
                print(f"\n[{module_slug}] diagram {idx+1}/{len(diagrams)}")
                convert_one(tex_path, label, output_file, verbose=True)
                stats["succeeded"] += 1
                wired_entries.append({
                    "src": web_path,
                    "caption": diag["caption"],
                    "alt": derive_alt_text(diag["caption"]),
                    "source": derive_source_citation(diag["tex_file"]),
                    "label": label,
                })
            except ConversionError as e:
                print(f"  ✗ FAILED: {e}", file=sys.stderr)
                stats["failed"] += 1
                stats["errors"].append({
                    "module": module_slug,
                    "label": label,
                    "error": str(e),
                })
                module_succeeded = False

        # Wire the frontmatter if ALL diagrams for this module succeeded
        if wire and module_succeeded and wired_entries:
            try:
                update_module_frontmatter(module_slug, wired_entries)
                stats["modules_wired"] += 1
                print(f"  ✓ wired {module_slug}.md frontmatter ({len(wired_entries)} diagrams)")
            except ConversionError as e:
                print(f"  ✗ FRONTMATTER FAILED: {e}", file=sys.stderr)
                stats["errors"].append({
                    "module": module_slug,
                    "label": "<frontmatter>",
                    "error": str(e),
                })

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Convert TikZ figures from book manuscripts to SVG.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--mapping", help="Path to batch mapping JSON")
    group.add_argument("--tex-file", help="Single-mode: source .tex path")

    parser.add_argument("--label", help="Single-mode: figure label to extract")
    parser.add_argument("--output", help="Single-mode: output SVG path")
    parser.add_argument("--book", help="Batch mode: filter to one book (I, II, …)")

    args = parser.parse_args()

    # Verify tools
    if not shutil.which("lualatex"):
        print("ERROR: lualatex not found on PATH", file=sys.stderr)
        sys.exit(1)
    if not shutil.which("pdf2svg"):
        print("ERROR: pdf2svg not found on PATH (brew install pdf2svg)", file=sys.stderr)
        sys.exit(1)

    if args.mapping:
        mapping_file = Path(args.mapping)
        if not mapping_file.exists():
            print(f"ERROR: mapping file not found: {mapping_file}", file=sys.stderr)
            sys.exit(1)
        stats = convert_mapping(mapping_file, book_filter=args.book)
        print(f"\n{'='*60}")
        print(f"  Total:     {stats['total']}")
        print(f"  Succeeded: {stats['succeeded']}")
        print(f"  Failed:    {stats['failed']}")
        print(f"  Modules wired: {stats.get('modules_wired', 0)}")
        if stats["errors"]:
            print(f"\n  Errors:")
            for err in stats["errors"]:
                print(f"    - {err['module']} / {err['label']}")
                print(f"      {err['error']}")
        sys.exit(1 if stats["failed"] > 0 else 0)

    # Single mode
    if not args.label or not args.output:
        parser.error("--tex-file requires --label and --output")

    try:
        convert_one(Path(args.tex_file), args.label, Path(args.output))
    except ConversionError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
