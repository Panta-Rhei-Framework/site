---
layout: "falsification-page"
title: "N27 — Magnetic winding number $w = 2$"
permalink: "/falsifications/n27-magnetic-winding-number-w-2/"
lane: "results"
falsification_id: "N27"
n_num: 27
tier: "binary"
domain: "particle-physics"
domain_display: "Particle Physics"
prediction: "magnetic winding!prediction pred:n27 The RM winding theorem (V.T227): $w = (T^2) = 2$. Faraday rotation measure near BH jets encodes toroidal winding."
experiment: "SKA, ngVLA, ngEHT polarimetry"
timeline: "2030–2035."
current_status: "consistent"
registry_id: "V.T227"
canonical_books:
  - "V"
summary_short: "N27: Magnetic winding number $w = 2$. SKA, ngVLA, ngEHT polarimetry."
right_rail:
  toc: false
  related:
    -
      title: "Falsification Pack Browse"
      url: "/results/falsifications/browse/"
    -
      title: "Predictions Browse"
      url: "/results/predictions/browse/"
    -
      title: "Results Overview"
      url: "/results/"
  meta:
    type: "Falsification"
    domain: "Particle Physics"
    status: "Consistent"
    experiment: "SKA, ngVLA, ngEHT polarimetry"
    updated: "April 2026"
generated_from: "corpus/results/facets/falsifications"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/falsifications"
do_not_edit: true
---

## N27: Prediction

The RM winding theorem (V.T227):
$w = (T^2) = 2$.
Faraday rotation measure
near BH jets
encodes toroidal winding.
*Experiment:* SKA, ngVLA, ngEHT polarimetry.
*Timeline:* 2030–2035.


## Derivation Context

The Faraday rotation measure (RM)
around the shadow of a $T^2$ black hole
exhibits winding number

The toroidal magnetic field
on the minor $S^1$ cycle
causes two sign changes per azimuthal circuit,
compared to one for a radial/dipolar field on $S^2$.
The winding number $2$
is a topological invariant
of genus$(T^2) = 1$.

The toroidal B-field wraps around the minor $S^1$
(Definition (def:ch42-toroidal-bfield),
Chapter (ch:book5-ch42-eht-reread)).
As the line of sight traces one azimuthal circuit
around the shadow,
it crosses two sectors
where the toroidal field component $B_$
reverses sign:
once at the ``top'' of the torus
and once at the ``bottom.''
Each reversal produces a sign change in the RM integral
$RM = n_e \,B_ \,dl$.
For $S^2$ with a radial or dipolar field,
only one sign change occurs per circuit.
The winding number is
$w_RM = |number of sign changes|/1 = 2$
for $T^2$ and $1$ for $S^2$.

The Stokes $V$ circular polarization winding number
around the shadow is
