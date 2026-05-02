#!/usr/bin/env python3
"""Promote private Public-Good Impact Dossier PDFs into the public site tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

import yaml


SITE_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_ROOT = SITE_ROOT.parent
PAPERS_ROOT = PROGRAM_ROOT / "papers"
SOURCE_ROOT = PAPERS_ROOT / "research-briefings" / "public-good"
PDF_ROOT = SITE_ROOT / "assets" / "pdfs" / "research-briefings" / "public-good"
RELEASE_DATA_PATH = SITE_ROOT / "_data" / "impact" / "public_good_dossier_release.yml"
BRIEFINGS_DATA_PATH = SITE_ROOT / "_data" / "impact" / "public-good-briefings.json"
LANDING_ROOT = SITE_ROOT / "publications" / "research-briefings" / "public-good"
PORTFOLIO_ORDER_PATH = SITE_ROOT / "_data" / "impact" / "portfolio_order.yml"
RELEASE_DATE = "2026-05-02"
RELEASE_LABEL = "May 2026 publication-ready release"
RELEASE_STATUS = "publication_ready"
SOURCE_VERSION = "v3-enriched"
LEGACY_ADVANCED_FISSION_NAME = (
    "public-good-briefing-2026-04-26-"
    "advanced-fission-safety-operations-licensing-fleet-modernization.pdf"
)


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dump_yaml(data: Any) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=96)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def page_count(path: Path) -> int:
    try:
        from pypdf import PdfReader  # type: ignore

        return len(PdfReader(str(path)).pages)
    except Exception:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":", 1)[1].strip())
        raise RuntimeError(f"Could not determine page count for {path}")


def canonical_pdf_name(slug: str) -> str:
    return f"public-good-impact-dossier-{RELEASE_DATE}-{slug}.pdf"


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    frontmatter = yaml.safe_load(text[4:end]) or {}
    return frontmatter, text[end + 5 :]


def render_frontmatter(frontmatter: dict[str, Any], body: str) -> str:
    return "---\n" + dump_yaml(frontmatter) + "---\n" + body.lstrip("\n")


def release_keywords(record: dict[str, Any]) -> list[str]:
    return [
        "Public-Good Impact Dossier",
        "conditional public-good briefing",
        "PDF dossier",
        record["portfolio"]["title"],
        record["title"],
    ]


def build_release_records(records: list[dict[str, Any]], apply: bool) -> dict[str, dict[str, Any]]:
    if len(records) != 44:
        raise RuntimeError(f"expected 44 dossier records, found {len(records)}")
    if apply:
        PDF_ROOT.mkdir(parents=True, exist_ok=True)

    release_records: dict[str, dict[str, Any]] = {}
    for record in records:
        slug = record["slug"]
        source_pdf = SOURCE_ROOT / record["path"].replace("main.tex", "main.pdf")
        if not source_pdf.is_file():
            raise RuntimeError(f"missing built PDF for {slug}: {source_pdf}")

        pdf_name = canonical_pdf_name(slug)
        dest_pdf = PDF_ROOT / pdf_name
        if apply:
            shutil.copy2(source_pdf, dest_pdf)
            if slug == "advanced-fission-safety-operations-licensing-fleet-modernization":
                shutil.copy2(source_pdf, PDF_ROOT / LEGACY_ADVANCED_FISSION_NAME)
        measured_pdf = dest_pdf if apply else source_pdf
        rel_path = f"/assets/pdfs/research-briefings/public-good/{pdf_name}"
        legacy_paths: list[str] = []
        if slug == "advanced-fission-safety-operations-licensing-fleet-modernization":
            legacy_paths.append(
                f"/assets/pdfs/research-briefings/public-good/{LEGACY_ADVANCED_FISSION_NAME}"
            )

        release_records[slug] = {
            "dossier_id": record["dossier_id"],
            "slug": slug,
            "title": record["title"],
            "portfolio": record["portfolio"]["slug"],
            "portfolio_title": record["portfolio"]["title"],
            "pdf_status": "available",
            "pdf_path": rel_path,
            "legacy_pdf_paths": legacy_paths,
            "pdf_sha256": sha256(measured_pdf),
            "pdf_bytes": measured_pdf.stat().st_size,
            "pdf_pages": page_count(measured_pdf),
            "release_date": RELEASE_DATE,
            "release_label": RELEASE_LABEL,
            "release_status": RELEASE_STATUS,
            "source_version": record["version"],
            "domain_review_status": record["domain_review_status"],
            "upstream_review_status": record["upstream_review_status"],
            "deployment_claim": False,
            "product_claim": False,
            "validation_claim": False,
            "evidence_count": record["evidence_count"],
            "source_route": record["source_route"],
            "landing_route": record["landing_route"],
        }
    return release_records


def update_landing_pages(release_records: dict[str, dict[str, Any]], source_records: dict[str, dict[str, Any]]) -> None:
    for slug, release in release_records.items():
        path = LANDING_ROOT / slug / "index.md"
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        record = source_records[slug]
        frontmatter.update(
            {
                "artifact_status": "html_pdf_available",
                "pdf_status": "available",
                "pdf_path": release["pdf_path"],
                "pdf_release_date": RELEASE_DATE,
                "release_status": RELEASE_STATUS,
                "dossier_version": SOURCE_VERSION,
                "domain_review_status": "pending",
                "deployment_claim": False,
                "product_claim": False,
                "validation_claim": False,
                "updated": "May 2026",
                "search_keywords": release_keywords(record),
            }
        )
        tags = list(frontmatter.get("tags") or [])
        for tag in ["public-good-impact-dossier", "pdf-available"]:
            if tag not in tags:
                tags.append(tag)
        frontmatter["tags"] = tags
        path.write_text(render_frontmatter(frontmatter, body), encoding="utf-8")


def update_briefings_data(
    release_records: dict[str, dict[str, Any]],
    source_records: dict[str, dict[str, Any]],
) -> None:
    data = json.loads(BRIEFINGS_DATA_PATH.read_text(encoding="utf-8"))
    if len(data) != 44:
        raise RuntimeError(f"expected 44 public-good briefing data rows, found {len(data)}")
    for item in data:
        slug = item["slug"]
        release = release_records[slug]
        source = source_records[slug]
        item.update(
            {
                "artifact_status": "html_pdf_available",
                "pdf_status": "available",
                "pdf_path": release["pdf_path"],
                "pdf_release_date": RELEASE_DATE,
                "release_status": RELEASE_STATUS,
                "source_version": SOURCE_VERSION,
                "domain_review_status": "pending",
                "upstream_review_status": release["upstream_review_status"],
                "deployment_claim": False,
                "product_claim": False,
                "validation_claim": False,
                "pdf_sha256": release["pdf_sha256"],
                "pdf_bytes": release["pdf_bytes"],
                "pdf_pages": release["pdf_pages"],
                "search_keywords": release_keywords(source),
            }
        )
    BRIEFINGS_DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def update_old_portfolio_routes() -> None:
    for slug in load_yaml(PORTFOLIO_ORDER_PATH):
        path = SITE_ROOT / "impact" / "portfolio" / f"{slug}.md"
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        frontmatter["layout"] = "redirect"
        frontmatter["redirect_to"] = f"/impact/global-public-good/{slug}/"
        frontmatter["summary_short"] = (
            "Redirects to the canonical Global Public Good portfolio page."
        )
        path.write_text(render_frontmatter(frontmatter, body), encoding="utf-8")


def main() -> int:
    global PAPERS_ROOT, SOURCE_ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="copy PDFs and update site source files")
    parser.add_argument(
        "--papers-root",
        type=Path,
        default=PAPERS_ROOT,
        help="private papers repo/worktree containing research-briefings/public-good",
    )
    args = parser.parse_args()
    PAPERS_ROOT = args.papers_root.resolve()
    SOURCE_ROOT = PAPERS_ROOT / "research-briefings" / "public-good"

    records = load_yaml(SOURCE_ROOT / "dossiers.yml")
    source_records = {record["slug"]: record for record in records}
    release_records = build_release_records(records, apply=args.apply)

    if not args.apply:
        print(f"Dry run: {len(release_records)} PDFs ready for release metadata generation.")
        print(f"Destination: {PDF_ROOT}")
        return 0

    RELEASE_DATA_PATH.write_text(dump_yaml(release_records), encoding="utf-8")
    update_landing_pages(release_records, source_records)
    update_briefings_data(release_records, source_records)
    update_old_portfolio_routes()
    print(f"Released {len(release_records)} Public-Good Impact Dossier PDFs into site assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
