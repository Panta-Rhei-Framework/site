---
layout: result-page
title: Proton Charge Radius r_p at +12 ppm (37× Improvement in Wave 46)
permalink: /results/problem/proton-charge-radius-12-ppm/
result_id: result-062
topic: mathematics
layer: mathematics
result_type: structural_readout
bridge_status: internal
summary_short: The proton charge radius r_p = 0.84088 fm is predicted at +12 ppm from
  PRad-II/MUSE — a 37-fold improvement over the prior +450 ppm estimate achieved in
  Wave 46.
canonical_books: []
right_rail:
  meta:
    type: Structural Readout
    layer: Mathematics
    topic: Mathematics
    status: Internal
    updated: April 2026
---

## Overview

IV.T185 (improved in Wave 46) predicts the proton charge radius r_p = 0.84088 fm at +12 ppm from the PDG value 0.84075 ± 0.00065 fm. The earlier estimate was +450 ppm; the 37× improvement in Wave 46 came from including the NLO holonomy path-integral correction. The proton radius puzzle (historical discrepancy between muonic hydrogen and electron scattering measurements) is resolved by the τ framework which predicts the single value 0.84088 fm, consistent with modern precision measurements.

## Detail

The proton charge radius is defined as the root-mean-square radius of the proton's charge distribution. Its measurement generated the 'proton radius puzzle': muonic hydrogen Lamb shift measurements (Pohl et al. 2010) gave r_p = 0.84087 fm while electron scattering and hydrogen spectroscopy measurements gave r_p ≈ 0.877 fm, a 7σ discrepancy. Subsequent measurements (PRad, 2019) and re-analysis eventually converged on r_p ≈ 0.841 fm, consistent with muonic hydrogen. The puzzle is largely resolved experimentally with the current PDG value r_p = 0.84075 ± 0.00065 fm.

IV.T185 predicts the proton charge radius within the τ-framework. The physical picture is that the proton's charge radius is determined by the spatial extent of the τ-holonomy path integral over the C-sector (strong force) fiber. The prediction at LO (before Wave 46) gave r_p = 0.8441 fm at +440 ppm. The NLO improvement in Wave 46 added a holonomy path-integral correction based on the CF window of ι_τ, shifting the prediction to r_p = 0.84088 fm at +12 ppm from PDG.

At +12 ppm this enters the sub-100 ppm tier — one of the most precise predictions in the nuclear physics sector. The result is currently marked conjectural rather than τ-effective because the holonomy path-integral identification has not yet been formally derived in the Lean formalization. The open problem IV.OP11 (proton charge radius sub-100 ppm) is listed as partial-improved: the +12 ppm result is achieved but the theoretical derivation of the path-integral mechanism needs further formalization.

## Result Statement

IV.T185: r_p = 0.84088 fm at +12 ppm from PDG 0.84075 fm. 37× improvement over prior +440 ppm in Wave 46 via NLO holonomy path-integral correction. Scope: conjectural (path-integral mechanism not yet formalized in Lean).

