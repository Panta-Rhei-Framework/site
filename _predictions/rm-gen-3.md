---
layout: "prediction-page"
title: "Three Generations of Fermions"
title_plain: "Three Generations of Fermions"
permalink: "/predictions/rm-gen-3/"
lane: "results"
prediction_id: "pred-001"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "|rm gen| = 3"
observable_mathml: "<math><mi>H₁(τ³;ℤ) ≅ ℤ³</mi></math>"
formula_plain: "H₁(τ³;ℤ) ≅ ℤ³"
formula_mathml: "<math><mi>H₁(τ³;ℤ) ≅ ℤ³</mi></math>"
formula_display: "H₁(τ³; ℤ) ≅ ℤ³ → |gen| = 3"
tau_value: "3"
observed: "3"
observed_value: "3"
deviation: "exact"
precision_tier: "sub-10-ppm"
cascade_tier: "binary"
precision_display: "Sub-10 ppm"
registry_id: "IV.T171"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Three Generations of Fermions: τ-value 3, observed 3, deviation exact."
right_rail:
  toc: false
  related:
    -
      title: "Predictions Browse"
      url: "/results/predictions/browse/"
    -
      title: "Falsification Pack"
      url: "/results/falsifications/browse/"
    -
      title: "Results Overview"
      url: "/results/"
  meta:
    type: "Physics Prediction"
    domain: "Particle Physics"
    precision: "Sub-10 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**H₁(τ³; ℤ) ≅ ℤ³ → |gen| = 3**

## Derivation

The number of fermion generations
equals the rank
of the first integer homology
of the $τ^3$ fibration:

The result $|gen| = 3$
is established by three independent arguments,
each drawing on different mathematical structures:

- **$H_1$ rank = $(τ^3)$**
(Theorem (thm:ch60-three-gen-rank)).
The first homology group
of $τ^3$ has rank 3
by the K\"unneth computation
(eq:ch60-kunneth).
This is the most direct proof:
the topological structure of $τ^3$
forces exactly three independent one-cycles.

The fiber $T^2 = (R · S^1) × (ι<sub>τ</sub> R · S^1)$
with aspect ratio $r/R = ι<sub>τ</sub>$
carries a Laplacian
whose primitive eigenvalue spectrum
(modes $(n,m)$ with $(n,m) = 1$)
supports exactly three stable generation modes
below the first composite-mode threshold:
$λ_(1,0) = 1$,
$λ_(0,1) = ι<sub>τ</sub>^-2 ≈ 8.585$,
$λ_(1,1) = 1 + ι<sub>τ</sub>^-2 ≈ 9.585$.
The next primitive mode $(2,1)$
has $λ_(2,1) ≈ 12.58$,
exceeding the composite threshold $λ_(2,0) = 4$.
No fourth light generation exists.
*(Registry: IV.T172, Wave 7.)*

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 60 — mass-spectrum), Books IV–V of *Panta Rhei*.
