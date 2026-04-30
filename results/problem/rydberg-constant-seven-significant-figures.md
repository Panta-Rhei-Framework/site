---
layout: "result-page"
title: "Rydberg Constant at Seven Significant Figures from τ"
permalink: "/results/problem/rydberg-constant-seven-significant-figures/"
id: "result-052"
result_id: "result-052"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "foundational-math"
importance_class: "structural-support-result"
status_code: "R"
domain_group: "Mathematics"
summary_short: "The Rydberg constant R_∞ is derived to seven significant figures — at 0.026 ppm agreement with CODATA — from the τ-framework with zero free continuous parameters."
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
lean_formalization_status: "formalized"
cascade_layer: "kernel"
foundational_hinge_ids: []
glossary_term_ids:
  - "PG-C11-rydberg-constant"
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

IV.T86 derives the Rydberg constant R_∞ from the τ-framework to seven significant figures, achieving 0.026 ppm agreement with the CODATA value. The Rydberg constant is the energy scale of hydrogen spectroscopy and appears in virtually all atomic physics calculations. Its derivation follows the α → m_e → R_∞ derivation chain: ι<sub>τ</sub> → α⁻¹ → m_e → R_∞, with no free parameters at any step. The result is part of the Chain 1 derivation sequence that ultimately grounds the periodic table.

## Detail

The Rydberg constant R_∞ = 10,973,731.568 m⁻¹ (CODATA 2022) is the most precisely measured fundamental constant, known to 12 significant figures experimentally. IV.T86 derives R_∞ to seven significant figures (0.026 ppm) within the τ-framework. The derivation chain is: ι<sub>τ</sub> = 2/(π+e) → κ_B = ι<sub>τ</sub>² → α⁻¹ = 137.036 (~0 ppm) → m_e (0.025 ppm) → R_∞ = m_e α²/(2h) at 0.026 ppm. Each step is a structural consequence of the previous one; no experimental inputs enter after the calibration anchor m_n.

The Rydberg constant is significant as a gateway to atomic physics: from R_∞ follow the Bohr radius, the hydrogen energy levels, and ultimately the structure of the periodic table. IV.T86 establishes that atomic spectroscopy, which provided the original phenomenology driving the development of quantum mechanics, is derivable from the τ-axioms through a 7-step chain. In the cross-domain analysis (Chain 1: ι<sub>τ</sub> → α → m_e → Periodic Table), the Rydberg constant is the penultimate step before the Bohr radius.

At 0.026 ppm the Rydberg prediction is among the most precise in the framework — ranking alongside the electron mass (0.025 ppm) and the fine-structure constant (~0 ppm) in the sub-1 ppm precision tier of the falsification ledger.

## Result Statement

IV.T86: Rydberg constant R_∞ derived to 7 significant figures at 0.026 ppm agreement with CODATA. Chain: ι<sub>τ</sub> → α → m_e → R_∞. Zero free parameters.
