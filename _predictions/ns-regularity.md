---
layout: prediction-page
title: "Navier–Stokes Regularity (No Blow-Up)"
title_plain: "Navier–Stokes Regularity (No Blow-Up)"
permalink: /predictions/ns-regularity/
lane: results
prediction_id: "pred-067"
domain: "collective-dynamics"
domain_display: "Collective Dynamics"
observable: "NS regularity"
observable_mathml: "profinite decompactification"
formula_plain: "profinite decompactification"
formula_mathml: "profinite decompactification"
formula_display: "Profinite decompactification → no finite-time blow-up"
tau_value: "no blow-up"
observed_value: "(open)"
deviation: "–"
precision_tier: "structural"
precision_display: "Structural"
registry_id: "V.T254"
scope: "conjectural"
scope_display: "Conjectural"
canonical_books:
  - "V"
summary_short: "Navier–Stokes Regularity (No Blow-Up): τ-value no blow-up, observed (open), deviation –."
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
    precision: "Structural"
    scope: "Conjectural"
    updated: "April 2026"
---

## τ-Formula

**Profinite decompactification → no finite-time blow-up**

## Derivation

where $p_n^#$
is the $n$th primorial.
The convergence to the Leray exponent
$α = 1$ is super-exponential:

$n$ | $p_n^#$
| $α_n$
| Gap $1 - α_n$
1 | 2 | 0.500 | $5.0 × 10^-1$ 2 | 6 | 0.833 | $1.7 × 10^-1$ 3 | 30 | 0.967 | $3.3 × 10^-2$ 4 | 210 | 0.995 | $4.8 × 10^-3$ 5 | 2310 | 0.9996 | $4.3 × 10^-4$ 6 | 30030 | 0.99997 | $3.3 × 10^-5$

By depth $5$,
the exponent is within $0.04%$
of the Leray value.
The gap closes super-exponentially:
the primorials grow faster
than any exponential.

The gap to the Millennium Problem.
The decompactification theorem
shows that the $τ$-regularity
exponent converges
to the Leray value
faster than any geometric sequence.
This is strong structural evidence
for Navier–Stokes regularity,
but it is not a proof
in the Clay Mathematics Institute sense:
the Millennium Problem
requires regularity on $ℝ^3$,
not on a sequence of compact approximations.
The scope remains conjectural
(Chapter (ch:book5-ch27-navier-stokes-macro),
Section (sec:ch27-clay-bridge)).

## Source

This prediction is derived in the Physics Ledger (Chapter 65 — collective-dynamics), Books IV–V of *Panta Rhei*.

