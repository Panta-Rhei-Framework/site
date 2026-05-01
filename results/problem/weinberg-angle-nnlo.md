---
layout: "result-page"
title: "Weinberg Angle NNLO at −0.7 ppm"
permalink: "/results/problem/weinberg-angle-nnlo/"
id: "result-035"
result_id: "result-035"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "foundational-math"
importance_class: "structural-support-result"
status_code: "R"
domain_group: "Mathematics"
summary_short: "The weak mixing angle sin²θ_W is derived at NNLO to −0.7 ppm accuracy using the Window Universality W₃(4) = 5 correction."
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
  - "PG-C16-weinberg-angle"
  - "MG-O06-universal"
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

IV.D337 gives the NNLO derivation of sin²θ_W = sin²θ_W^LO [1 + correction(ι<sub>τ</sub>, α, W₃(4))] at −0.7 ppm from the PDG value. The NLO and NNLO corrections are both governed by Window Universality: W₃(4) = 5 appears at each order. This is one of three EW precision observables derived at sub-ppm accuracy in the τ-framework.

## Detail

The Weinberg angle sin²θ_W ≈ 0.23122 is one of the most precisely measured parameters in particle physics. At LO in the τ-framework, sin²θ_W arises from the A-B sector mixing angle (weak-EM mixing). The LO formula gives a value at a few hundred ppm from experiment. The NLO correction uses the Window Universality: W₃(4) = 5 generates the first correction term `(1 − αW₃(4)ι_τ²) = (1 − 5αι_τ²)`. The NNLO correction is governed by the *same* universal modulus at the next perturbative order: per the Lean source `TauHiggs2.lean` (lines 597–600), the k-th perturbative order receives a `W₃(4)^k` factor — *one lemniscate traversal at NLO, double traversal at NNLO* — so the NNLO correction is `(1 + α²W₃(4)²ι_τ⁴) = (1 + 25α²ι_τ⁴)`. The full NNLO formula (IV.D337) gives −0.7 ppm from the PDG value sin²θ_W = 0.23122. **There is no W₃(3) factor in the NNLO term**; the universal modulus across orders is W₃(4) = 5 alone. (Earlier drafts of this page erroneously introduced a "W₃(3) = 4" symbol in the NNLO formula — that was a bug; the canonical W₃(3) = 17 per Lean `TauLib/BookI/CF/WindowAlgebra.lean:w3_at_3`, and W₃(3) does not appear in the Weinberg derivation at any order.) This is part of the electroweak precision programme in Book IV that also produces M_W at −0.5 ppm (IV.T177); sin²θ_W is the most precisely derived EW parameter.

## Result Statement

IV.D337: sin²θ_W at NNLO, governed by Window Universality W₃(4) = 5 (single universal modulus, with `W₃(4)^k` at the k-th perturbative order), at −0.7 ppm from PDG value. Lean-certified: `TauLib/BookIV/Electroweak/WeinbergNLO.lean:consecutive_window_integers` proves W₃(3) = 17, W₄(3) = 18, W₅(3) = 19; the W₃(4) = 5 modulus is at `TauLib/BookI/CF/WindowAlgebra.lean:w3_at_4`.
