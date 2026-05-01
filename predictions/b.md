---
layout: "prediction-page"
title: "Baryon Density Parameter ω_b"
title_plain: "Baryon Density Parameter ω_b"
permalink: "/predictions/b/"
lane: "results"
prediction_id: "pred-040"
domain: "cosmology"
domain_display: "Cosmology"
observable: "ωb"
observable_mathml: "from <math><mi>ηB</mi></math>"
formula_plain: "from ηB"
formula_mathml: "from <math><mi>ηB</mi></math>"
formula_display: "ω_b from τ-native η_B = 0.02209"
tau_value: "0.02209"
observed: "0.02237"
observed_value: "0.02237"
deviation: "-1.2%"
precision_tier: "1-5-percent"
cascade_tier: "A"
precision_display: "1–5%"
registry_id: "V.T192"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Baryon Density Parameter ω_b: τ-value 0.02209, observed 0.02237, deviation -1.2%."
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
    domain: "Cosmology"
    precision: "1–5%"
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookI.Boundary.Iota"
    formalization: "formalized"
    registry_id_origin: "I.D34"
  -
    module: "TauLib.BookI.Boundary.Ring"
    formalization: "formalized"
    registry_id_origin: "I.D19"
  -
    module: "TauLib.BookI.Boundary.SplitComplex"
    formalization: "formalized"
    registry_id_origin: "I.D20"
  -
    module: "TauLib.BookI.Coordinates.Hyperfact"
    formalization: "formalized"
    registry_id_origin: "I.T04"
  -
    module: "TauLib.BookI.Denotation.TauIdx"
    formalization: "formalized"
    registry_id_origin: "I.D07"
  -
    module: "TauLib.BookI.Orbit.Ladder"
    formalization: "formalized"
    registry_id_origin: "I.D06"
  -
    module: "TauLib.BookI.Polarity.BipolarAlgebra"
    formalization: "formalized"
    registry_id_origin: "I.D28"
  -
    module: "TauLib.BookI.Polarity.Lemniscate"
    formalization: "formalized"
    registry_id_origin: "I.D18"
  -
    module: "TauLib.BookI.Polarity.Polarity"
    formalization: "formalized"
    registry_id_origin: "I.T05"
  -
    module: "TauLib.BookI.Polarity.Spectral"
    formalization: "formalized"
    registry_id_origin: "I.D19e"
  -
    module: "TauLib.BookIII.Enrichment.LayerTemplate"
    formalization: "formalized"
    registry_id_origin: "III.D08"
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIII.Sectors.LanglandsReflection"
    formalization: "formalized"
    registry_id_origin: "III.D17"
  -
    module: "TauLib.BookIII.Sectors.ParityBridge"
    formalization: "formalized"
    registry_id_origin: "III.T07"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D05"
  -
    module: "TauLib.BookV.Cosmology.BBNBaryogenesis"
    formalization: "formalized"
    registry_id_origin: "V.D198"
  -
    module: "TauLib.BookV.Cosmology.BaryogenesisAsymmetry"
    formalization: "formalized"
    registry_id_origin: "V.T172"
  -
    module: "TauLib.BookV.Cosmology.CMBSpectrum"
    formalization: "formalized"
    registry_id_origin: "V.T192"
  -
    module: "TauLib.BookV.Cosmology.HeliumFraction"
    formalization: "formalized"
    registry_id_origin: "V.T149"
  -
    module: "TauLib.BookV.Cosmology.ThresholdLadder"
    formalization: "formalized"
    registry_id_origin: "V.D159"
  -
    module: "TauLib.BookV.GravityField.LinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.D52"
  -
    module: "TauLib.BookV.GravityField.NonlinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.D56"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**ω_b from τ-native η_B = 0.02209**

## Derivation

m_s = m_b(τ) × ι<sub>τ</sub>^53/15
= 4,174.4 × 0.02241
= 93.55\;MeV

at $+1,559$ ppm from PDG $m_s(MS, 2\;GeV)
= 93.4 ± 0.8$ MeV (within $0.2σ$),
where $m_b(τ) = m_t(τ) · ι<sub>τ</sub>^45/13 = 4,174.4$ MeV.

The denominator $15 = (τ^3) · W_3(4)$ is the same product
governing the $m_t/m_b$ fiber correction (Eq. (eq:iv-mt-mb-exponent)).
The numerator $53 = 4\,a_3 + 1$ suggests a four-fold $a_3$ winding
with unit offset—the ``confinement unit'' carried by each of the
$|non-ω generators| = 4$ boundary channels.

The charm-to-strange mass ratio from the $τ$-chain:

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 36 — koide-mass-hierarChapter ies), Books IV–V of *Panta Rhei*.
