---
layout: "result-page"
title: "Chronology Protection: Closed Timelike Curves Structurally Excluded"
permalink: "/results/problem/chronology-protection-no-ctcs/"
id: "result-236"
result_id: "result-236"
problem_ledger_ids: []
topic: "physics"
layer: "physics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "frontier-problem"
importance_class: "domain-level-open-problem"
status_code: "R"
domain_group: "Physics"
summary_short: "Closed timelike curves are structurally forbidden by the strict irreflexive partial order on the α-orbit (V.T09, Causal Ordering Theorem). Hawking's chronology protection becomes a theorem, not a speculative mechanism."
canonical_books:
  - "V"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Physics"
    topic: "Physics"
    status: "Internal"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "none"
cascade_layer: "physics-cascade"
foundational_hinge_ids: []
glossary_term_ids: []
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

V.T09 (Causal Ordering Theorem, Book V ch04 "Proto-Chronos") proves that the causal relation α_m < α_n iff m < n on the α-orbit is a strict, transitive, irreflexive partial order. Closed timelike curves (CTCs) are structurally impossible. Hawking's chronology protection conjecture — that quantum effects should prevent CTC formation — becomes a theorem in τ, but for a different reason: CTCs cannot form because the causal structure is a partial order, not because some mechanism prevents them.

## Detail

In general relativity, solutions containing closed timelike curves are known — Gödel's rotating cosmology, Tipler's cylinders, traversable wormholes. Hawking's chronology protection conjecture asserts that quantum effects (vacuum polarization divergences, renormalization stress-energy feedback) should prevent such configurations from forming in practice, rendering time travel impossible. The conjecture remains unproved. Category τ approaches the question from a different direction. The α-orbit on τ¹ carries a natural index m ∈ ℤ arising from the generator α. V.D18 (Causal Ordering Relation) defines α_m < α_n iff m < n; V.T09 proves this is a strict, transitive, irreflexive relation — a partial order on the α-orbit. A closed timelike curve would require some α_m to satisfy α_m < α_m, which contradicts irreflexivity. V.R18 ("Causality precedes light cones", `books/V-CategoricalMacrocosm/latex/sections/part01/ch04-proto-chronos.tex`) records that the causal kernel is prior to metric geometry: light cones are derived structure, not primitive. Chronology protection in τ is therefore not a conjecture about quantum back-reaction but a direct consequence of the kernel axioms.

## Result Statement

V.T09 + V.D18: The α-orbit carries a strict irreflexive partial order. Closed timelike curves are structurally impossible; chronology protection is a theorem, not a conjecture.
