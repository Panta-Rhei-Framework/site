---
layout: "result-page"
title: "Vacuum Catastrophe Framework Account"
permalink: "/results/problem/vacuum-catastrophe-resolution/"
id: "result-165"
result_id: "result-165"
problem_ledger_ids: []
topic: "physics"
layer: "physics"
result_type: "frontier_problem"
bridge_status: "resolved"
result_kind: "frontier-problem"
importance_class: "core-foundational-problem"
status_code: "R"
domain_group: "FOUND"
summary_short: "The vacuum catastrophe — the 10¹²⁰ discrepancy between the QFT prediction and the observed cosmological constant — is often called the worst prediction in …"
canonical_books:
  - "V"
right_rail:
  meta:
    type: "Frontier Problem"
    layer: "Physics"
    topic: "Physics"
    status: "Internally addressed"
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

The vacuum catastrophe — the 10¹²⁰ discrepancy between the QFT prediction and the observed cosmological constant — is often called the worst prediction in physics. The τ-framework internally addresses it: the cosmological constant is exactly zero because the boundary reading of τ³ has no bulk energy term.

## Result Statement

Vacuum catastrophe internally addressed: the **bare** cosmological constant in the bulk Lagrangian is zero exactly. Boundary reading of τ³ has no bulk vacuum energy term. The 10¹²⁰ discrepancy disappears. Status: Internally addressed.

## Bare vs effective: what "Λ = 0" means here

The framework distinguishes two distinct objects that the literature often conflates under the symbol "Λ":

- **`Λ_bare`** — the bare cosmological constant in the bulk Lagrangian. **Zero exactly** in the τ-framework. The 10¹²⁰ catastrophe assumes a bulk vacuum-energy term scaling with QFT cutoff⁴; the framework introduces no such bulk term, so the catastrophe dissolves at its origin rather than being cancelled by fine-tuning.
- **`Ω_Λ`** — the effective dark-energy density observable from the Hubble rate `H(z)`, CMB acoustic peaks, and BAO. **Distinct object** — a boundary-readout effect, not a bulk Lagrangian term. Computed in the framework as `Ω_Λ = κ_D(1 + ι_τ³) ≈ 0.6849` per *V.T234*, with the canonical-vs-tau-effective bridge characterised by *V.T69* ("dark energy as boundary readout artifact"). See [N20 falsification entry](/falsifications/n20-dark-energy-density-06849/) for the prediction and the comparison to Planck.

The two values can both hold because they refer to different physical objects: `Λ_bare` is bulk-Lagrangian; `Ω_Λ` is boundary-readout. The framework predicts both, exactly, with no contradiction. Cross-references: [Falsification pack](/results/falsifications/browse/), *V.T234* (Ω_Λ value), *V.T69* (boundary-readout / canonical bridge).
