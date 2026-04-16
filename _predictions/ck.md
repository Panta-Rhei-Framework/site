---
layout: prediction-page
title: "Kolmogorov Constant C_K"
title_plain: "Kolmogorov Constant C_K"
permalink: /predictions/ck/
lane: results
prediction_id: "pred-064"
domain: "collective-dynamics"
domain_display: "Collective Dynamics"
observable: "CK"
observable_mathml: "<math><mi>(3/2)(1 + ι_τ⁴/4)</mi></math>"
formula_plain: "(3/2)(1 + ι_τ⁴/4)"
formula_mathml: "<math><mi>(3/2)(1 + ι_τ⁴/4)</mi></math>"
formula_display: "C_K = dim(τ³)/dim(T²) = 3/2 = 1.5"
tau_value: "3/2"
observed_value: "1.5 ± 0.1"
deviation: "∼ 0%"
precision_tier: "1-5-percent"
precision_display: "1–5%"
registry_id: "V.T250"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Kolmogorov Constant C_K: τ-value 3/2, observed 1.5 ± 0.1, deviation ∼ 0%."
right_rail:
  toc: false
  related:
    - title: "Predictions Browse"
      url: /results/predictions/browse/
    - title: "Falsification Pack"
      url: /results/falsifications/browse/
    - title: "Results Overview"
      url: /results/
  meta:
    type: "Physics Prediction"
    domain: "Collective Dynamics"
    precision: "1–5%"
    scope: "τ-Effective"
    updated: "April 2026"
---

## τ-Formula

**C_K = dim(τ³)/dim(T²) = 3/2 = 1.5**

## Derivation

The numerator $5 = (τ^3) + (T^2)
= |gen| + (T^2)$
counts the total number of dissipation channels:
three generation modes
from $H_1(τ^3;ℤ) ≅ ℤ^3$
plus two fiber directions on $T^2$.
The denominator is the spatial dimensionality
of the fibered product.

In the K41 derivation,
the exponent $5/3$ emerges
from dimensional analysis:
$[E(k)] = L^3 T^-2$,
$[] = L^2 T^-3$,
$[k] = L^-1$,
so $E(k) ^2/3 k^-5/3$
by matching dimensions.
This derivation gives the correct answer
but does not explain
*why* the dimensions work out
to produce $5/3$.
The $τ$-decomposition (eq:ch65-53-decomposition)
provides the structural reason:
$5/3$ is the ratio
of dissipation channels
to spatial dimensions
in the fibered product.
The exponent encodes
the topology of $τ^3$.

## Source

This prediction is derived in the Physics Ledger (Chapter 65 — collective-dynamics), Books IV–V of *Panta Rhei*.

