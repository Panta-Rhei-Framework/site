---
layout: registry-object
title: III.D10 — Ladder Checker
permalink: /registry/object/III.D10/
registry_id: III.D10
object_type: definition
book: III
book_slug: book-iii
part: 1
chapter: 8
scope: tau-effective
formalization: formalized
lean_module: TauLib.BookIII.Enrichment.Functor
lean_name: ladder_checker
summary: 'Lean-grade proof harness for verifying ladder properties: existence_checker(k)
  verifies non-emptiness at level k, stability_checker(k) verifies template preservation,
  strictness_checker(k) verifies E_k \ E_{k-1} ≠ ∅, saturation_checker(k_max) verifies
  [E_{k_max}^op, E_{k_max}] ⊆ E_{k_max}.'
depends_on:
- III.T04
depended_by:
- III.D66
- III.D74
- III.P30
- III.R40
dep_count: 1
rev_dep_count: 4
is_foundational: false
is_central: false
---
