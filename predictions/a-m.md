---
layout: "prediction-page"
title: "Proton–Neutron Mass Splitting"
title_plain: "Proton–Neutron Mass Splitting"
permalink: "/predictions/a-m/"
lane: "results"
prediction_id: "pred-006"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "δA / mₙ"
observable_mathml: "<math><mi>(tfrac316)sqrt3,ι<sub>τ</sub>⁵</mi></math>"
formula_plain: "(tfrac316)sqrt3,ι<sub>τ</sub>⁵"
formula_mathml: "<math><mi>(tfrac316)sqrt3,ι<sub>τ</sub>⁵</mi></math>"
formula_display: "Δm / mₙ = (3/16)√3 · ι<sub>τ</sub>⁵ − (3/20)α · ι<sub>τ</sub>²"
tau_value: "1.38!×!10⁻³"
observed: "1.378!×!10⁻³"
observed_value: "1.378!×!10⁻³"
deviation: "+33~ppm"
precision_tier: "10-1000-ppm"
cascade_tier: "A"
precision_display: "10–1000 ppm"
registry_id: "IV.T142"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Proton–Neutron Mass Splitting: τ-value 1.38!×!10⁻³, observed 1.378!×!10⁻³, deviation +33~ppm."
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
lean_modules:
  -
    module: "TauLib.BookII.Closure.GeometricBiSquare"
    formalization: "formalized"
    registry_id_origin: "II.T49"
  -
    module: "TauLib.BookIII.Enrichment.Functor"
    formalization: "formalized"
    registry_id_origin: "III.D04"
  -
    module: "TauLib.BookIII.Enrichment.LayerTemplate"
    formalization: "formalized"
    registry_id_origin: "III.D05"
  -
    module: "TauLib.BookIII.Sectors.BoundaryCharacters"
    formalization: "formalized"
    registry_id_origin: "III.D11"
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIII.Sectors.LanglandsReflection"
    formalization: "formalized"
    registry_id_origin: "III.T06"
  -
    module: "TauLib.BookIII.Sectors.ParityBridge"
    formalization: "formalized"
    registry_id_origin: "III.T08"
  -
    module: "TauLib.BookIV.Arena.Tau3Arena"
    formalization: "formalized"
    registry_id_origin: "IV.D255"
  -
    module: "TauLib.BookIV.Physics.NucleonMassSplitting"
    formalization: "formalized"
    registry_id_origin: "IV.T142"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D02"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**Δm / mₙ = (3/16)√3 · ι<sub>τ</sub>⁵ − (3/20)α · ι<sub>τ</sub>²**

## Derivation

The proton–neutron mass splitting
is given by the **two-sector formula**:

where $α ≈ 1/137.036$
is the fine-structure constant
and $ι<sub>τ</sub> = 2/(π + e)$.
The first term is the strong-sector (C-sector) contribution;
the second is the electromagnetic correction (B-sector).
Numerically:

in agreement with the measured value
at $+33$ ppm.
*(Registry: IV.T142, Wave 1.)*

Structural anatomy.
The two-sector formula (eq:ch60-pn-formula)
has a transparent structure:

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 60 — mass-spectrum), Books IV–V of *Panta Rhei*.
