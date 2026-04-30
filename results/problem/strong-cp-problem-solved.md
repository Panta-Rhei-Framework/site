---
layout: "result-page"
title: "Strong CP Problem Solved: θ_QCD = 0 from SA-i Admissibility"
permalink: "/results/problem/strong-cp-problem-solved/"
id: "result-010"
result_id: "result-010"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "foundational-math"
importance_class: "structural-support-result"
status_code: "R"
domain_group: "Mathematics"
summary_short: "θ_QCD = 0 exactly, derived from the SA-i admissibility condition on η-winding mod-3 structure. No axion mechanism needed."
canonical_books:
  - "IV"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Mathematics"
    topic: "Mathematics"
    status: "Internal"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "none"
cascade_layer: "kernel"
foundational_hinge_ids: []
glossary_term_ids: []
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

The Strong CP Problem Theorem (IV.T160) proves that the QCD vacuum angle θ_QCD = 0 exactly. The proof uses the SA-i (self-adjoint admissibility) condition on the η-sector winding structure: SA-i requires the η-winding to satisfy a mod-3 admissibility constraint, and this constraint forces θ_QCD to vanish identically. No Peccei-Quinn mechanism, no axion field, and no fine-tuning is required.

## Detail

The strong CP problem is the puzzling empirical fact that θ_QCD < 10⁻¹⁰ — the QCD vacuum angle is measured to be extraordinarily close to zero, with no theoretical explanation in the Standard Model for why it should be so small rather than of order 1. Proposed orthodox solutions (Peccei-Quinn symmetry, axions) introduce new fields and symmetries that have not been observed. [Book IV]({{ '/publications/books/book-iv/' | relative_url }}) proves θ_QCD = 0 exactly from the structure of the η-sector. The SA-i admissibility condition is a constraint on which η-winding configurations are allowed in the τ-framework: only configurations satisfying a mod-3 integrality condition on their winding numbers are admissible. This mod-3 condition, when translated to the QCD vacuum angle, forces θ_QCD = 2πk/3 for integer k. But CP invariance of the strong force at k = 0 is then selected by the additional requirement that the η-sector integrates consistently with the global τ-structure (no residual holonomy). Result: θ_QCD = 0 exactly, not fine-tuned but structurally forced.

## Result Statement

IV.T160: θ_QCD = 0 exactly, derived from SA-i admissibility condition (mod-3 structure on η-winding). No axion mechanism is needed.
