---
layout: prediction-page
title: "mₑ (MeV)"
title_plain: "mₑ (MeV)"
permalink: /predictions/m-mev/
lane: results
prediction_id: "pred-002"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "mₑ (MeV)"
observable_mathml: "<math><mi>mₙ / R</mi></math> (10-link chain)"
formula_plain: "mₙ / R (10-link chain)"
formula_mathml: "<math><mi>mₙ / R</mi></math> (10-link chain)"
tau_value: "0.510999"
observed_value: "0.510999"
deviation: "0.025~ppm"
precision_tier: "sub-10-ppm"
precision_display: "Sub-10 ppm"
registry_id: "IV.T25"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "mₑ (MeV): τ-value 0.510999, observed 0.510999, deviation 0.025~ppm."
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
    domain: "Particle Physics"
    precision: "Sub-10 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
---

## Derivation

The electron mass is the program's highest-precision prediction, derived in Book IV, Chapter 6 (*The Neutron as Minimal Defect*) and Chapter 10 (*The Fine-Structure Constant*). The derivation proceeds through a 10-link spectral chain on the fiber T², starting from the neutron mass as the single calibration anchor (IV.D59).

The neutron emerges as the minimal quasi-stable defect bundle on T² — the simplest configuration whose breathing amplitude is nonzero and whose bi-rotation is locked by ι_τ = 2/(π+e). The electron mass is then derived as m_e = m_n / R, where R is the ratio determined by a 10-link chain of spectral exponents on the lemniscate boundary. Each link in the chain corresponds to a step in the refinement tower, with the exponents governed by the sector coupling hierarchy κ(A), κ(B), κ(C), κ(D).

The resulting value m_e = 0.510999 MeV matches the CODATA value to 0.025 ppm — the sharpest numerical prediction in the entire Physics Ledger. This precision is not a fit: it follows from the 10-link chain structure with zero adjustable parameters. The same chain, extended to different winding classes, yields the muon and tau lepton masses (the Koide relation Q = 2/3, IV.T143).

## Source

This prediction is derived in Book IV, Part 1, Chapters 6 and 10. The 10-link chain is the spectral backbone of the mass spectrum; all other particle masses are downstream of this derivation.
