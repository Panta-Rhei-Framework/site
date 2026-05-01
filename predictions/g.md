---
layout: "prediction-page"
title: "Gravitational Constant G"
title_plain: "Gravitational Constant G"
permalink: "/predictions/g/"
lane: "results"
prediction_id: "pred-026"
domain: "electroweak-qcd"
domain_display: "Electroweak & QCD"
observable: "G"
observable_mathml: "<math><mi>(c³/ℏ),ι<sub>τ</sub>²</mi></math>"
formula_plain: "(c³/ℏ),ι<sub>τ</sub>²"
formula_mathml: "<math><mi>(c³/ℏ),ι<sub>τ</sub>²</mi></math>"
formula_display: "G = (c³/ℏ) · ι<sub>τ</sub>² ≈ 6.674 × 10⁻¹¹"
tau_value: "6.674!×!10⁻¹¹"
observed: "CODATA"
observed_value: "CODATA"
deviation: "∼ 3~ppm"
precision_tier: "sub-10-ppm"
cascade_tier: "B"
precision_display: "Sub-10 ppm"
registry_id: "V.T11"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Gravitational Constant G: τ-value 6.674!×!10⁻¹¹, observed CODATA, deviation ∼ 3~ppm."
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
    precision: "Sub-10 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookI.Coordinates.ABCD"
    formalization: "formalized"
    registry_id_origin: "I.D17"
  -
    module: "TauLib.BookI.Coordinates.NormalForm"
    formalization: "formalized"
    registry_id_origin: "I.D16"
  -
    module: "TauLib.BookI.Coordinates.Primes"
    formalization: "formalized"
    registry_id_origin: "I.T09"
  -
    module: "TauLib.BookI.Coordinates.TowerAtoms"
    formalization: "formalized"
    registry_id_origin: "I.D19c"
  -
    module: "TauLib.BookI.Kernel.Axioms"
    formalization: "formalized"
    registry_id_origin: "I.D02"
  -
    module: "TauLib.BookI.Kernel.Signature"
    formalization: "formalized"
    registry_id_origin: "I.D01"
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIII.Sectors.ParityBridge"
    formalization: "formalized"
    registry_id_origin: "III.T08"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D05"
  -
    module: "TauLib.BookV.Prologue.ExportContract"
    formalization: "formalized"
    registry_id_origin: "V.D14"
  -
    module: "TauLib.BookV.Prologue.HermeticPrinciple"
    formalization: "formalized"
    registry_id_origin: "V.T06"
  -
    module: "TauLib.BookV.Temporal.BaseCircle"
    formalization: "formalized"
    registry_id_origin: "V.D17"
  -
    module: "TauLib.BookV.Temporal.TemporalIgnition"
    formalization: "formalized"
    registry_id_origin: "V.T11"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**G = (c³/ℏ) · ι<sub>τ</sub>² ≈ 6.674 × 10⁻¹¹**

## Derivation

The gravitational constant G is derived in Book V, Chapter 6 (*High Energy and High Entropy at the Beginning*), as part of the Opening Regime Theorem (V.T11). In the τ-framework, G is not a free parameter — it is read out from the D-sector coupling structure of the boundary holonomy algebra.

The τ-native expression for G follows from the identification of the D-sector (gravitational sector) coupling at depth 1: the gravitational coupling κ(D;1) = 1 − ι<sub>τ</sub> = κ_D, combined with the dimensional calibration set by the neutron mass anchor (IV.D59). The gravitational constant emerges as G = (c³/ℏ) · ι<sub>τ</sub>² in natural units, yielding G ≈ 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² at approximately 3 ppm from the CODATA 2018 value.

The derivation depends on the Opening Regime Theorem (V.T11), which establishes that at the ignition depth the gravitational character is at its maximum — the boundary holonomy algebra first supports stable oscillating modes, and the gravitational coupling is structurally fixed by the sector template.

The closing identity α_G = α¹⁸ · √3 · (1 − 3α/π) (V.T20, the G–α Bridge) provides an independent cross-check: gravity and electromagnetism are connected by a single equation containing no free parameters.

## Source

This prediction is derived in Book V, Part 1, Chapter 6 (*High Energy and High Entropy at the Beginning*), with the G–α Bridge identity in Book V, Part 8, Chapter 70.
