#!/usr/bin/env bash
# Generate first-page cover thumbnails for research-paper and research-briefing PDFs.
# Output: assets/thumbnails/papers/{slug}-cover.png and assets/thumbnails/briefings/{slug}-cover.png
# Skips files that already have thumbnails.
#
# Pipeline: pdftoppm (first page, 100 DPI PNG) | sips (resize to 600x800) → final PNG.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAPERS_PDF_DIR="$REPO_ROOT/assets/pdfs/research-papers"
BRIEFINGS_PDF_DIR="$REPO_ROOT/assets/pdfs/research-briefings/public-good"
PAPERS_OUT="$REPO_ROOT/assets/thumbnails/papers"
BRIEFINGS_OUT="$REPO_ROOT/assets/thumbnails/briefings"

mkdir -p "$PAPERS_OUT" "$BRIEFINGS_OUT"

generated=0
skipped=0

# Strip a known release-prefix from a PDF basename to recover the publication slug.
extract_slug() {
  local basename="$1"
  local kind="$2"
  # Strip extension
  local name="${basename%.pdf}"
  if [ "$kind" = "paper" ]; then
    # Format: research-paper-YYYY-MM-DD-{slug}
    echo "${name#research-paper-????-??-??-}"
  else
    # Briefings: prefer the public-good-impact-dossier-YYYY-MM-DD-{slug} prefix
    if [[ "$name" == public-good-impact-dossier-* ]]; then
      echo "${name#public-good-impact-dossier-????-??-??-}"
    elif [[ "$name" == public-good-briefing-* ]]; then
      echo "${name#public-good-briefing-????-??-??-}"
    else
      echo "$name"
    fi
  fi
}

generate_thumb() {
  local pdf="$1"
  local out="$2"
  if [ -f "$out" ]; then
    skipped=$((skipped+1))
    return 0
  fi
  local tmp_prefix
  tmp_prefix="$(mktemp -t pdfcover.XXXXXX)"
  rm -f "$tmp_prefix"
  pdftoppm -png -f 1 -l 1 -r 100 "$pdf" "$tmp_prefix" >/dev/null 2>&1
  local rendered="${tmp_prefix}-1.png"
  if [ ! -f "$rendered" ]; then
    rendered="${tmp_prefix}-01.png"
  fi
  if [ ! -f "$rendered" ]; then
    echo "WARN: pdftoppm produced no output for $pdf" >&2
    return 1
  fi
  # Resize so the longer side is 800px while preserving aspect ratio.
  sips --resampleHeight 800 "$rendered" --out "$out" >/dev/null
  rm -f "$rendered"
  generated=$((generated+1))
}

echo "Papers..."
seen_paper_slugs=""
if [ -d "$PAPERS_PDF_DIR" ]; then
  for pdf in "$PAPERS_PDF_DIR"/*.pdf; do
    [ -f "$pdf" ] || continue
    base="$(basename "$pdf")"
    slug="$(extract_slug "$base" paper)"
    case " $seen_paper_slugs " in
      *" $slug "*) continue ;;
    esac
    seen_paper_slugs="$seen_paper_slugs $slug"
    out="$PAPERS_OUT/${slug}-cover.png"
    generate_thumb "$pdf" "$out" || true
  done
fi

echo "Briefings..."
seen_briefing_slugs=""
if [ -d "$BRIEFINGS_PDF_DIR" ]; then
  # Prefer impact-dossier first, then fall back to plain briefing PDFs for the same slug.
  for pdf in "$BRIEFINGS_PDF_DIR"/public-good-impact-dossier-*.pdf "$BRIEFINGS_PDF_DIR"/public-good-briefing-*.pdf; do
    [ -f "$pdf" ] || continue
    base="$(basename "$pdf")"
    slug="$(extract_slug "$base" briefing)"
    case " $seen_briefing_slugs " in
      *" $slug "*) continue ;;
    esac
    seen_briefing_slugs="$seen_briefing_slugs $slug"
    out="$BRIEFINGS_OUT/${slug}-cover.png"
    generate_thumb "$pdf" "$out" || true
  done
fi

echo "Generated: $generated"
echo "Skipped (already exist): $skipped"
