---
layout: registry-object
lane: registry
title: III.D87 — Arithmetic Translation Functor
permalink: /registry/object/III.D87/
registry_id: III.D87
object_type: definition
book: III
book_slug: book-iii
part: 9
chapter: 80
scope: tau-effective
formalization: formalized
lean_module: TauLib.BookIII.Bridge.TranslationArith
lean_name: arith_translate
summary: Functor Arith_tr maps τ-internal arithmetic to classical ℤ. At stage k, Arith_tr(x)
  = reduce(x, k) — the canonical embedding Z/M_k Z ↪ ℤ. Well-defined and injective
  at each stage.
depends_on:
- III.D71
- III.T40
depended_by:
- III.D88
- III.D89
- III.T59
dep_count: 2
rev_dep_count: 3
is_foundational: false
is_central: false
---
