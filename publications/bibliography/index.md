---
layout: program-doc
title: "Bibliography"
lane: publications
permalink: /publications/bibliography/
type: "Publication Support"
publication_type: "Bibliography"
status: "Published"
summary_short: "Publication-facing entry point for the reference corpus, browse interface, and BibTeX artifact."
summary_cards:
  - title: "Reference corpus"
    body: "The bibliography is a support surface for the books, notes, papers, and verification documents."
  - title: "Browsable"
    body: "Readers can browse and filter the citation corpus through the dedicated bibliography interface."
  - title: "Exportable"
    body: "A BibTeX artifact is published for reviewers who want to inspect or reuse the source bibliography."
right_rail:
  related:
    - title: "Bibliography Index"
      url: /bibliography/
    - title: "Browse References"
      url: /bibliography/browse/
    - title: "Books"
      url: /publications/books/
  artifacts:
    - title: "Download BibTeX"
      url: /assets/bibliography/references.bib
  meta:
    type: "Support Surface"
    scope: "Reference corpus"
    status: "Published"
    updated: "April 2026"
---

## Role

The Bibliography is publication support infrastructure. It gives readers a route from released artifacts back to the scholarly sources they cite, without placing the bibliography itself in the top-level public lane navigation.

The dedicated bibliography surfaces remain available:

- [Bibliography index]({{ '/bibliography/' | relative_url }}) for grouped reference context.
- [Browse and filter references]({{ '/bibliography/browse/' | relative_url }}) for search-style exploration.
- [BibTeX artifact]({{ '/assets/bibliography/references.bib' | relative_url }}) for export and review.

## Current Corpus

{% assign bibliography_count = site.bibliography | size %}

The site currently publishes **{{ bibliography_count }} bibliography entries** as structured pages, with citation context generated from the public publication corpus.

## How to Use It

Use the bibliography when you need scholarly context for a book chapter, white paper, Research Note, or verification document. Use [Corpus]({{ '/corpus/' | relative_url }}) when you need internal registered objects, and use [Results]({{ '/results/' | relative_url }}) when you need problem-oriented claims.
