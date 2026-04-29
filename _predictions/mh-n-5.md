---
layout: "prediction-page"
title: "Higgs Boson Mass (n = 5 route)"
title_plain: "Higgs Boson Mass (n = 5 route)"
permalink: "/predictions/mh-n-5/"
lane: "results"
prediction_id: "pred-025"
domain: "electroweak-qcd"
domain_display: "Electroweak & QCD"
observable: "mH (n=5)"
observable_mathml: "<math><mi>(4 - ι<sub>τ</sub>³/(1-5κ_ω))/κ_ω</mi></math>"
formula_plain: "(4 - ι<sub>τ</sub>³/(1-5κ_ω))/κ_ω"
formula_mathml: "<math><mi>(4 - ι<sub>τ</sub>³/(1-5κ_ω))/κ_ω</mi></math>"
formula_display: "m_H = (4 − ι<sub>τ</sub>³/(1 − 5κ_ω)) / κ_ω → 125.26 GeV"
tau_value: "125.26"
observed: "125.20"
observed_value: "125.20"
deviation: "+493~ppm"
precision_tier: "10-1000-ppm"
cascade_tier: "A"
precision_display: "10–1000 ppm"
registry_id: "IV.T151"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Higgs Boson Mass (n = 5 route): τ-value 125.26, observed 125.20, deviation +493~ppm."
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
    domain: "Electroweak & QCD"
    precision: "10–1000 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**m_H = (4 − ι<sub>τ</sub>³/(1 − 5κ_ω)) / κ_ω → 125.26 GeV**

## Derivation

An earlier derivation (Wave 3, Registry IV.T151)
used $n = 5 = W_3(4)$,
the third Waring number at four terms.
The formula

m_H^(n=5)
= 4 - ι<sub>τ</sub>^3 / (1 - 5κ_ω)κ_ω
· (scale factor),

where $κ_ω = ι<sub>τ</sub> / (1 + ι<sub>τ</sub>)$,
gave $m_H ≈ 125.26$ GeV
at $+493$ ppm.
The $n = 7$ result
supersedes this,
improving precision by a factor of 60
and providing a cleaner structural derivation
(the integer 7 arises from the lemniscate geometry itself,
not from a Waring function).

The shift from $n = 5$ to $n = 7$
illustrates the research programme's self-correction.
Wave 3 identified the correct structural form
(a rational function of $ι<sub>τ</sub>$
and sector couplings)
but assigned $n = W_3(4) = 5$.
Wave 5 recognized that $n = 7$
has a more direct structural derivation
from the lemniscate geometry,
and the precision improved from $+493$ to $+8$ ppm.
Both derivations
are honest readings of the $τ$ structure;
the second is the sharper one.
The hierarchy problem is simultaneously dissolved:
there is no UV cutoff in $τ$,
hence no quadratic divergence $δ m_H^2 ∼ Λ^2$
and no fine-tuning problem.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 60 — mass-spectrum), Books IV–V of *Panta Rhei*.
