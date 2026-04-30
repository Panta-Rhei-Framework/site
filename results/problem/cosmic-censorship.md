---
layout: "result-page"
title: "Cosmic Censorship: Boundary Compactness + Hartogs Extension"
permalink: "/results/problem/cosmic-censorship/"
id: "result-235"
result_id: "result-235"
problem_ledger_ids:
  - "phys-the-cosmic-censorship-hypothesis-and-the-chronology-protection-conjecture"
topic: "physics"
layer: "physics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "frontier-problem"
importance_class: "domain-level-open-problem"
status_code: "R"
domain_group: "Physics"
summary_short: "Cosmic censorship follows from boundary compactness and the Hartogs extension principle (V.T27). Penrose-Hawking singularity theorems do not apply in τ because τ³ is not a Lorentzian manifold (V.R31) — naked singularities are structurally excluded, not merely censored."
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

V.T27 (Well-posedness via Hartogs, Book V ch13) proves that given boundary data (R^H, T^mat) on L satisfying the τ-Einstein identity, the Hartogs extension principle guarantees a unique holomorphic extension to the τ³ interior. Cosmic censorship — Penrose's conjecture that general relativity does not generically produce naked singularities — follows from boundary compactness. V.R31 (No Initial Singularity, ch06) records the deeper reason: Penrose-Hawking singularity theorems presuppose Lorentzian structure, and τ³ is not a Lorentzian manifold. Their premises fail in τ from the outset.

## Detail

The strong and weak cosmic censorship conjectures are among the longest-standing unsolved problems in mathematical relativity: does a generic smooth initial data set in general relativity produce only singularities hidden behind event horizons, never visible to distant observers? Orthodox approaches either seek counterexamples (Christodoulou, Dafermos, and collaborators) or genericity proofs using PDE techniques, with no global account. Category τ reframes the question ontologically. In V.T27 (`books/V-CategoricalMacrocosm/latex/sections/part02/ch13-tau-einstein-equation.tex`), the τ-Einstein identity is imposed on the boundary lemniscate L = S¹ ∨ S¹, and the Hartogs extension principle — a theorem of several complex variables — guarantees a unique holomorphic extension to the interior of τ³. Because L is compact, this extension is regular everywhere; no naked singularity can appear interior to a compact boundary. V.R31 adds that Penrose-Hawking theorems, which assume pseudo-Riemannian (Lorentzian) signature, have no purchase in τ: τ³ is a complex-analytic structure, not a Lorentzian manifold, so the premises of the singularity theorems are not satisfied. The outcome is that cosmic censorship is not a conjecture awaiting proof but a corollary of holomorphic extension on a compact boundary.

## Result Statement

V.T27 + V.R31: Cosmic censorship follows from Hartogs extension on compact boundary L. Penrose-Hawking singularity theorems inapplicable because τ³ is a complex-analytic, not Lorentzian, manifold.
