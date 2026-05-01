---
layout: "prediction-page"
title: "Baryonic Tully-Fisher Relation (20 Galaxies)"
title_plain: "Baryonic Tully-Fisher Relation (20 Galaxies)"
permalink: "/predictions/20-galaxy-btfr/"
lane: "results"
prediction_id: "pred-052"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "20-galaxy BTFR"
observable_mathml: "<math><mi>τ</mi></math>-BTFR, zero free params"
formula_plain: "τ-BTFR, zero free params"
formula_mathml: "<math><mi>τ</mi></math>-BTFR, zero free params"
formula_display: "τ-BTFR slope = 3.991 (zero free parameters)"
tau_value: "slope 3.991"
observed: "3.97 ± 0.10"
observed_value: "3.97 ± 0.10"
deviation: "0.067 dex"
precision_tier: "1-5-percent"
cascade_tier: "A"
precision_display: "1–5%"
registry_id: "V.D258"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Baryonic Tully-Fisher Relation (20 Galaxies): τ-value slope 3.991, observed 3.97 ± 0.10, deviation 0.067 dex."
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
    domain: "Astrophysics"
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
    module: "TauLib.BookI.Coordinates.ABCD"
    formalization: "formalized"
    registry_id_origin: "I.D17"
  -
    module: "TauLib.BookI.Coordinates.Descent"
    formalization: "formalized"
    registry_id_origin: "I.L04"
  -
    module: "TauLib.BookI.Coordinates.Hyperfact"
    formalization: "formalized"
    registry_id_origin: "I.T04"
  -
    module: "TauLib.BookI.Coordinates.NoTie"
    formalization: "formalized"
    registry_id_origin: "I.L03"
  -
    module: "TauLib.BookI.Coordinates.NormalForm"
    formalization: "formalized"
    registry_id_origin: "I.D16"
  -
    module: "TauLib.BookI.Coordinates.TowerAtoms"
    formalization: "formalized"
    registry_id_origin: "I.D19c"
  -
    module: "TauLib.BookI.Denotation.Arithmetic"
    formalization: "formalized"
    registry_id_origin: "I.P05"
  -
    module: "TauLib.BookI.Denotation.Order"
    formalization: "formalized"
    registry_id_origin: "I.P07"
  -
    module: "TauLib.BookI.Denotation.TauIdx"
    formalization: "formalized"
    registry_id_origin: "I.D07"
  -
    module: "TauLib.BookI.Kernel.Axioms"
    formalization: "formalized"
    registry_id_origin: "I.K3"
  -
    module: "TauLib.BookI.Orbit.Closure"
    formalization: "formalized"
    registry_id_origin: "I.T01"
  -
    module: "TauLib.BookI.Orbit.Generation"
    formalization: "formalized"
    registry_id_origin: "I.D05"
  -
    module: "TauLib.BookI.Polarity.BipolarAlgebra"
    formalization: "formalized"
    registry_id_origin: "I.D27"
  -
    module: "TauLib.BookI.Polarity.Lemniscate"
    formalization: "formalized"
    registry_id_origin: "I.D18"
  -
    module: "TauLib.BookI.Polarity.OmegaGerms"
    formalization: "formalized"
    registry_id_origin: "I.D25"
  -
    module: "TauLib.BookI.Polarity.Polarity"
    formalization: "formalized"
    registry_id_origin: "I.T05"
  -
    module: "TauLib.BookI.Polarity.PolarizedGerms"
    formalization: "formalized"
    registry_id_origin: "I.D26"
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D04"
  -
    module: "TauLib.BookV.Astrophysics.RotationCurves"
    formalization: "formalized"
    registry_id_origin: "V.D258"
  -
    module: "TauLib.BookV.GravityField.NonlinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.T37"
  -
    module: "TauLib.BookV.GravityField.TauSchwarzschild"
    formalization: "formalized"
    registry_id_origin: "V.D63"
  -
    module: "TauLib.BookV.Temporal.MacroReadout"
    formalization: "formalized"
    registry_id_origin: "V.D31"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**τ-BTFR slope = 3.991 (zero free parameters)**

## Derivation

Ninety-five percent of the universe
is missing.
That is the orthodox verdict:
$27%$ is dark matter,
$68%$ is dark energy,
and the $5%$ that we observe
is all that ordinary physics explains.
After decades of direct detection experiments
(XENON1T, LZ, PandaX),
no dark matter particle has been found.
After two decades
of theoretical effort,
the cosmological constant problem—a
mismatch of $120$ orders of magnitude
between the quantum vacuum prediction
and the observed value—remains
the worst quantitative failure
in the history of science.

This chapter demonstrates
that the dark sector dissolves
within Category $τ$.
The dissolution is not speculative:
it rests on five quantitative results,
each derived from the master constant
$ι<sub>τ</sub> = 2/(π + e)$
with zero free parameters.

- **Flat rotation curves**:
the master formula
$v^4 = G M_b c^2/(2_τ)$
reproduces NGC 3198 at $0.6%$
and passes a 20-galaxy survey
at $0.067$ dex RMS
(V.T85, V.D258).

- **Dark energy density**:
$Ω_Λ = κ_D(1 + ι<sub>τ</sub>^3) = 0.6849$,
matching Planck at $+269$ ppm
(V.T234).

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 63 — dark-sector), Books IV–V of *Panta Rhei*.
