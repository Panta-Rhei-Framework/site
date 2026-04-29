---
layout: "prediction-page"
title: "Neutrino NNLO Mass Ratios"
title_plain: "Neutrino NNLO Mass Ratios"
permalink: "/predictions/nnlo-ratio/"
lane: "results"
prediction_id: "pred-010"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "ν NNLO ratio"
observable_mathml: "<math><mi>(8/7+3/175,,6/7+9/700)</mi></math>"
formula_plain: "(8/7+3/175,,6/7+9/700)"
formula_mathml: "<math><mi>(8/7+3/175,,6/7+9/700)</mi></math>"
formula_display: "(Δpq, Δpr) = (8/7 + 3/175, 6/7 + 9/700) ≈ (1.16, 0.87)"
tau_value: "(1.16,,0.87)"
observed: "–"
observed_value: "–"
deviation: "+18.5~ppm"
precision_tier: "10-1000-ppm"
cascade_tier: "A"
precision_display: "10–1000 ppm"
registry_id: "V.T189"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Neutrino NNLO Mass Ratios: τ-value (1.16,,0.87), observed –, deviation +18.5~ppm."
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
    precision: "10–1000 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**(Δpq, Δpr) = (8/7 + 3/175, 6/7 + 9/700) ≈ (1.16, 0.87)**

## Derivation

(Δ_pq,\, Δ_pr)
\;=\;
(87 + 3175,\;
67 + 9700)
\;=\;
(1.16,\; 0.87),

where the NNLO shifts are
$δ_1 = 3/175 = 3/(7 · W_3(4)^2)
= dim(τ^3)/(n · W_3(4)^2)$
and
$δ_2 = 9/700 = 9/(n · 2|lobes| · W_3(4)^2)$,
with $n = 7 = 2|lobes| + |sectors|$,
$|lobes| = 2$, $|sectors| = 3$,
$dim(τ^3) = 3$, $W_3(4) = 5$.
Equivalently $700 = 7 · 100$
where $100 = 2|lobes| · W_3(4)^2 = 4 · 25$;
every integer in the denominators
is traceable to the $τ$-framework's
structural constants
(no free integers).
Three structural properties hold:

- **4/3 ratio preserved at every order:**
$Δ_pq/Δ_pr = 4/3$,
where $4/3 = 2 · |lobes|/|sectors|$.

- **Self-similarity:**
$δ_1/δ_0 = 3/25$,
where $δ_0 = 1/7$
is the leading-order unit
and $25 = W_3(4)^2$
is the window-squared normalization.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 61 — mixing-baryogenesis), Books IV–V of *Panta Rhei*.
