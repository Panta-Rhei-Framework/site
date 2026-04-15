---
layout: publication-book
title: "Book III: Categorical Spectrum"
permalink: /publications/books/book-iii/
lane: publications
publication_type: book
book_id: "III"
book_slug: "book-iii"
subtitle: "Where Physics Lives"
part_count: 11
chapter_count: 76
page_count: 437
summary_short: "Where Physics Lives"
summary_cards:
- title: Subtitle
  body: "Where Physics Lives"
- title: Structure
  body: "11 parts, 76 chapters, 437 pages"
- title: Layer
  body: "E₀ Mathematics (Hinge)"
linked_guided_tour: "/publications/guided-tours/"
linked_verify_page: "/verify/"
linked_dashboard: "/registry/dashboards/book-iii/"
right_rail:
  related:
  - title: Framework Overview
    url: /framework/about/
  - title: Registry
    url: /registry/books/book-iii/
  - title: Guided Tours
    url: /publications/guided-tours/
  artifacts:
  - title: Registry Dashboard
    url: /registry/dashboards/book-iii/
  - title: TauLib (frozen)
    url: https://github.com/Panta-Rhei-Research/formalization
    external: true
  meta:
    type: Canonical Book
    layer: "E₀ Mathematics (Hinge)"
    status: Published
    updated: April 2026
---

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


## Canonical Artifacts

- **Registry**: [76 chapters mapped to registry objects]({{ '/registry/books/book-iii/' | relative_url }})
- **Dashboard**: [Formalization status and dependency graph]({{ '/registry/dashboards/book-iii/' | relative_url }})
- **Formalization**: [TauLib BookIII](https://github.com/Panta-Rhei-Research/formalization) — Lean 4 verification
