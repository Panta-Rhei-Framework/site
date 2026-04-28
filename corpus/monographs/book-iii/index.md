---
layout: "corpus-monograph-book"
title: "Book III: Categorical Spectrum"
permalink: "/corpus/monographs/book-iii/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_book"
book_id: "III"
book_slug: "book-iii"
subtitle: "Where Physics Lives"
part_count: 11
chapter_count: 76
page_count: 437
summary_short: "Where Physics Lives"
publication_book_url: "/publications/books/book-iii/"
legacy_publication_url: "/publications/books/book-iii/"
summary_cards:
  -
    title: "Subtitle"
    body: "Where Physics Lives"
  -
    title: "Structure"
    body: "11 parts, 76 chapters, 437 pages"
  -
    title: "Layer"
    body: "E₀ Mathematics (Hinge)"
right_rail:
  related:
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-iii/"
    -
      title: "Registry"
      url: "/registry/books/book-iii/"
    -
      title: "Construction Spine"
      url: "/corpus/construction-spine/"
  meta:
    type: "Corpus Monograph"
    layer: "E₀ Mathematics (Hinge)"
    parts: "11"
    chapters: "76"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
---

## Reading edition

This is the Corpus projection of Book III. It exposes the monograph in Book → Part → Chapter order as part of the constructed research body.

For citation metadata, DOI records, cover images, and retail/download status, use the [Research Monograph artifact]({{ '/publications/books/book-iii/' | relative_url }}).

## About This Volume

The Central Theorem is proved and the holomorphic machinery is in hand.
But τ³ = τ¹ ×_f T² does not look like Cartesian three-dimensional space.
Where, then, does physics live?

The naïve answer—take three solenoidal coordinates (π, γ, η) and call them spatial dimensions—fails:
solenoidal coordinates are one-sided rays, not two-sided axes, and they carry no canonical linear structure.
The correct answer is subtler. The fibre T² at each worldline point is a *surface*—the two-dimensional boundary of a solid torus.
The Hartogs extension projects boundary data from this surface into the three-dimensional *bulk* interior,
and the interior coordinates *are* genuinely linear.
Perceived three-dimensional Cartesian space is this Hartogs-projected bulk.

The central task of Book III is to show that these local bulk projections—one per worldline—glue together
into a single, globally coherent three-dimensional space. Each of the seven Clay Millennium Problems,
together with the Langlands programme, provides a specific piece of this gluing guarantee.
The self-enrichment layer E₁ is precisely the statement that local spatial structures cohere globally.
Physics *is* E₁.



## Linked publication and verification artifacts

- **Registry**: [76 chapters mapped to registry objects]({{ '/registry/books/book-iii/' | relative_url }})
- **Dashboard**: [Formalization status and dependency graph]({{ '/registry/dashboards/book-iii/' | relative_url }})
- **Formalization**: [TauLib BookIII](https://github.com/Panta-Rhei-Research/formalization) — Lean 4 verification
