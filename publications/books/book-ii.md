---
layout: publication-book
title: "Book II: Categorical Holomorphy"
permalink: /publications/books/book-ii/
lane: publications
publication_type: book
book_id: "II"
book_slug: "book-ii"
subtitle: "Finite Readouts of Infinity"
part_count: 12
chapter_count: 68
page_count: 504
summary_short: "Finite Readouts of Infinity"
summary_cards:
- title: Subtitle
  body: "Finite Readouts of Infinity"
- title: Structure
  body: "12 parts, 68 chapters, 504 pages"
- title: Layer
  body: "E₀ Mathematics"
linked_guided_tour: "/publications/guided-tours/"
linked_verify_page: "/verify/"
linked_dashboard: "/registry/dashboards/book-ii/"
right_rail:
  related:
  - title: Framework Overview
    url: /framework/about/
  - title: Registry
    url: /registry/books/book-ii/
  - title: Guided Tours
    url: /publications/guided-tours/
  artifacts:
  - title: Registry Dashboard
    url: /registry/dashboards/book-ii/
  - title: TauLib (frozen)
    url: https://github.com/Panta-Rhei-Research/formalization
    external: true
  meta:
    type: Canonical Book
    layer: "E₀ Mathematics"
    status: Published
    updated: April 2026
---

## About This Volume

Book I closed with the Bridge Theorem (I.T34):
Category τ is complete.
Five generators, one operator, seven axioms (K0–K6)
have built a full mathematical kernel—numbers, coordinates,
sets, topology (implicit), categories, a topos, holomorphic transformers,
and Global Hartogs Extension proving that
boundary data determines interior structure.

Book II begins where Book I ended:
at the boundary-interior threshold.
The organizing paradigm is **boundary-first**—the
inversion of classical complex analysis.
Orthodox SCV builds from interior to boundary
(holomorphic functions extended to boundary values,
Cauchy integrals encoding interior data);
τ inverts this by building from boundary to interior
(boundary data determines interior structure via Global Hartogs).

Three chapters set the stage.
the relevant chapter
articulates the paradigm shift and the five exports from Book I.
the relevant chapter
explains why the elliptic complex numbers ℂ fail
(Laplacian glue, no canonical propagation, unipolar structure)
and why split-complex H_τ with j² = +1 is forced
(wave-type glue, bipolar idempotents, prime polarity).
the relevant chapter
maps the eleven-Part roadmap and the inverted dependency chain:
*holomorphy ⇒ continuity ⇒ topology ⇒ geometry ⇒ transcendentals ⇒ holomorphic interior* — exact inversion of orthodox order.

A note on terminology: throughout this book,
τ³ means "τ viewed through its geometric coordinate chart."
The superscript 3 is a structural index naming the three-factor
fibered product τ¹ ×_f T².
It is not a dimension count (the interior is four-dimensional),
not a power (τ³ ≠ τ × τ × τ),
and not an independent construction (τ³ *is* τ, read geometrically).
The base τ¹ and fiber T² are coordinate projections,
not standalone entities.
This distinction—between the ontic unity of τ
and the geometric readout τ³—runs through
every chapter that follows.

From here, the ten Parts of the book deploy the interior engine.
Parts I–IV earn the topological and geometric scaffolding
(interior points, cylinders, topology, Tarski geometry).
Part V earns the transcendental constants
π, e, j, ι<sub>τ</sub> from countable discrete structure.
Part VI makes split-complex holomorphy load-bearing
(Mutual Determination, the five-way equivalence).
Part VII proves holomorphic = idempotent-supported
(the three-lemma chain).
Part VIII proves Yoneda as a theorem
(τ enriches over itself).
Part IX proves the Central Theorem
O(τ³) ≅ A_spec(𝕃)—boundary
determines interior, interior encodes boundary.
Part X closes the circle and bridges to Book III.

Welcome to the holomorphic interior.


## Canonical Artifacts

- **Registry**: [68 chapters mapped to registry objects]({{ '/registry/books/book-ii/' | relative_url }})
- **Dashboard**: [Formalization status and dependency graph]({{ '/registry/dashboards/book-ii/' | relative_url }})
- **Formalization**: [TauLib BookII](https://github.com/Panta-Rhei-Research/formalization) — Lean 4 verification
