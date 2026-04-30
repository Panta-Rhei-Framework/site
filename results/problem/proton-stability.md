---
layout: "result-page"
title: "Proton Stability: Address Irresolvability Forbids Baryon Decay"
permalink: "/results/problem/proton-stability/"
id: "result-252"
result_id: "result-252"
problem_ledger_ids: []
topic: "physics"
layer: "physics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "frontier-problem"
importance_class: "domain-level-open-problem"
status_code: "R"
domain_group: "Physics"
summary_short: "Proton stability is a structural theorem in τ (IV.T72): the Confinement Theorem (IV.T71) forbids any isolated color-charged state from attaining a stable address on L, so no baryon-number-violating decay is admissible. Prediction: τ_p = ∞ exactly — distinct from GUT predictions (~10³³-10³⁵ yr, excluded by Super-K) and from the Standard Model's accidental baryon conservation."
canonical_books:
  - "IV"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Physics"
    topic: "Physics"
    status: "Internal"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "formalized"
cascade_layer: "physics-cascade"
foundational_hinge_ids: []
glossary_term_ids:
  - "PG-P02-proton"
  - "PG-Q16-color-charge"
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

The Proton Stability Theorem IV.T72 (Book IV ch39) establishes that the proton cannot decay. The argument is a direct corollary of the Confinement Theorem IV.T71: no isolated color-charged state reaches a stable address on the lemniscate boundary L, because the boundary character sequence fails to converge. Any hypothetical proton-decay channel would either produce a free quark (forbidden by IV.T71) or produce a lighter non-color-neutral composite (forbidden by the color-singlet admissibility rule). The result: τ_p = ∞ exactly — a structural absolute, not an accidental symmetry of the Standard Model, and not a finite lifetime as predicted by Grand Unified Theories.

## Detail

In the Standard Model, baryon-number conservation is accidental — no gauge principle enforces it, and non-perturbative sphaleron effects technically violate it at the B+L level. Grand Unified Theories (minimal SU(5), SO(10), and their SUSY variants) predict proton decay via channels such as p → e⁺π⁰ at lifetimes of ~10³³-10³⁵ years. Super-Kamiokande has excluded minimal SU(5) and placed stringent lower bounds on most GUT scenarios without a single detected decay event. Category τ takes a different structural position. IV.T71 (Confinement Theorem, `books/IV-CategoricalMicrocosm/latex/sections/part05/ch39-proton-stability.tex`) proves that color-charged states with color charge c ≢ 0 (mod 3) have no convergent boundary character sequence — they cannot account for to a stable address on L. Supporting theorems IV.T69 (SU(3) color-neutral vacuum from tracelessness) and IV.T70 (Color Number Theorem, N_c = 3) complete the color-admissibility structure. IV.T72 applies this to the proton: as the lightest color-singlet baryon, the proton cannot decay to a lighter admissible state because none exists, and it cannot decay to a free quark because free quarks are forbidden. IV.R04 (Neutron as First Ontic Particle) places this in the ontological hierarchy: the neutron is the unpolarized T² defect bundle, the proton is its weak-sector-polarized variant, and beta decay (n → p + e⁻ + ν̄) is a T² mode transition within the A-sector, not a violation of baryon number. The claim is sharply falsifiable: any observation of proton decay would refute the framework.

## Result Statement

IV.T72 + IV.T71: The Confinement Theorem forbids isolated color-charged states from reaching stable addresses on L; the Proton Stability Theorem applies this to the lightest color-singlet baryon. Prediction: τ_p = ∞ exactly — not ~10³³-10³⁵ yr (GUTs), not accidental (Standard Model), but structural.
