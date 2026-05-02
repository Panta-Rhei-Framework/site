---
title: "Frontier technical SEO sprint — handcrafted metadata across all lanes"
date: 2026-04-15
change_type: "site-release"
summary_short: "Handcrafted SEO metadata across every lane: JSON-LD structured data (17 schema branches), Google Scholar citation meta, Dublin Core, OpenGraph, Twitter cards, BreadcrumbList, and per-page canonical URLs."
affected_lanes:
  - global
  - publications
  - corpus
  - results
  - bibliography
  - registry
  - verify
right_rail:
  toc: false
  related:
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "April 2026"
---

A frontier-level technical SEO sprint added handcrafted metadata to every lane on the site:

- **JSON-LD structured data**: 17 schema branches in `_includes/seo-jsonld.html` covering Book, Chapter, ScholarlyArticle, DefinedTerm, CollectionPage, APIReference, SoftwareSourceCode, BlogPosting, AboutPage, and more.
- **Google Scholar citation meta**: `citation_title`, `citation_author`, `citation_doi`, `citation_date` on all publication and bibliography pages.
- **Dublin Core meta**: `DC.title`, `DC.creator`, `DC.date` on publications.
- **OpenGraph + Twitter cards**: per-page titles, descriptions, and type-appropriate tags.
- **BreadcrumbList**: auto-generated from `_includes/breadcrumb-data.html` and appended as JSON-LD on every page.
- **Canonical URLs**: absolute-URL canonical on every page via `head.html`.
- **SEO description include**: `_includes/seo-description.html` generates per-layout meta descriptions, falling back to `summary_short` → site description.
