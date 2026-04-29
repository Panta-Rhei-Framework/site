---
layout: "prediction-page"
title: "Fast Magnetic Reconnection Rate"
title_plain: "Fast Magnetic Reconnection Rate"
permalink: "/predictions/v-c/"
lane: "results"
prediction_id: "pred-065"
domain: "collective-dynamics"
domain_display: "Collective Dynamics"
observable: "vᵣₘ ᵣₑc"
observable_mathml: "<math><mi>ι<sub>τ</sub>²,vA</mi></math>"
formula_plain: "ι<sub>τ</sub>²,vA"
formula_mathml: "<math><mi>ι<sub>τ</sub>²,vA</mi></math>"
formula_display: "v_rec = ι<sub>τ</sub>² · v_A ≈ 0.117 v_A"
tau_value: "0.117,vA"
observed: "0.01–0.1,vA"
observed_value: "0.01–0.1,vA"
deviation: "–"
precision_tier: "structural"
cascade_tier: "A"
precision_display: "Structural"
registry_id: "V.T251"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Fast Magnetic Reconnection Rate: τ-value 0.117,vA, observed 0.01–0.1,vA, deviation –."
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
    domain: "Collective Dynamics"
    precision: "Structural"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**v_rec = ι<sub>τ</sub>² · v_A ≈ 0.117 v_A**

## Derivation

Observational agreement.
The experimental value
$C_K = 1.5 ± 0.1$
(Sreenivasan 1995;
Yeung and Zhou 1997;
Ishihara et al.\ 2009)
matches the $τ$-prediction exactly.
The central value coincides;
the deviation is $0.0%$
(Proposition (prop:ch28-ck-match)).

Why the Kolmogorov constant has been hard to determine.

The experimental determination of $C_K$
has historically been uncertain:
values ranging from $1.4$ to $1.7$
have been reported,
depending on the experiment,
the Reynolds number,
and the method of compensating
for finite-$Re$ effects.
DNS values have converged
toward $C_K ≈ 1.5$
as resolution has increased,
but the prefactor remains
one of the least precisely known
``universal'' constants
in turbulence theory.
The $τ$-prediction $C_K = 3/2$ exactly
provides a sharp target
for future high-resolution experiments.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 65 — collective-dynamics), Books IV–V of *Panta Rhei*.
