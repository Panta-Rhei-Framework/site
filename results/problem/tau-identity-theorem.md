---

layout: result-page
title: 'Tau-Identity Theorem: Agreement at One Depth Implies Agreement Everywhere'
permalink: /results/problem/tau-identity-theorem/
result_id: result-028
topic: mathematics
layer: mathematics
result_type: structural_readout
bridge_status: internal
result_kind: foundational-math
importance_class: structural-support-result
status_code: R
domain_group: "Mathematics"
summary_short: If two τ-holomorphic functions agree at any single depth level, they
  agree at all depths — the τ-analogue of the identity theorem for holomorphic functions.
canonical_books: ["I"]
right_rail:
  meta:
    type: Structural Readout
    layer: Mathematics
    topic: Mathematics
    status: Internal
    updated: April 2026
---

## Overview

I.T21 (Tau-Identity Theorem) proves that if two τ-holomorphic functions f and g agree on any single depth stratum of τ³, they agree on all of τ³. This is the τ-analogue of the classical identity theorem for holomorphic functions (agreement on an open set implies agreement everywhere). The result is foundational for proving uniqueness statements throughout the series.

## Detail

The classical identity theorem in complex analysis states that a holomorphic function on a connected domain is uniquely determined by its values on any open subset, or equivalently by agreement with another holomorphic function on any convergent sequence. I.T21 extends this to τ: τ-holomorphic functions are uniquely determined by their values on any single depth level of the tower structure τ³. The depth levels correspond to the tower-grading by enrichment level: depth 0 = E₀ data, depth 1 = E₁ data, etc. Agreement at depth k implies agreement at all depths because the τ-propagator (the mechanism by which data at depth k generates data at depth k+1) is injective. The proof uses the prime polarity structure: γ-even and η-odd components at depth k independently determine the same components at depth k+1, so any difference between f and g at depth k+1 would force a difference at depth k.

## Result Statement

I.T21: If two τ-holomorphic functions agree on any single depth stratum of τ³, they agree on all of τ³. τ-analogue of the classical identity theorem.

