---
layout: result-page
title: Abiogenesis Timescale Bound from Geometric Decay
permalink: /results/problem/abiogenesis-timescale-bound/
result_id: result-068
topic: biology
layer: life
result_type: structural_readout
bridge_status: internal
summary_short: The timescale for abiogenesis is bounded above by T_abio ≤ n_{1/2}
  · ⌈log₂(N/8)⌉, a logarithmic bound from the half-life of the defect complexity budget.
canonical_books: []
right_rail:
  meta:
    type: Structural Readout
    layer: Life
    topic: Biology
    status: Internal
    updated: April 2026
---

## Overview

VI.T45 proves a timescale bound for abiogenesis: the number of steps required for the Distinction+SelfDesc attractor to be reached is at most n_{1/2} · ⌈log₂(N/T)⌉, where n_{1/2} is the half-life of the complexity budget C(n), N is the initial complexity, and T = 8 is the Distinction threshold. The logarithmic scaling means abiogenesis can occur on geological (rather than astronomical) timescales for any reasonably complex prebiotic system, resolving the apparent timescale paradox.

## Detail

A perennial challenge in origin-of-life research is the 'abiogenesis paradox': the probability of life arising by pure chance from a prebiotic soup is astronomically small, suggesting it could not have happened in the age of the universe. This is sometimes called the 'Hoyle fallacy' (Hoyle's 747 assembled by a tornado in a junkyard).

VI.T45 resolves this paradox through a timescale bound. The key definitions (VI.D74–D77):
- Complexity budget C(n) = N – |D_n|: the number of available self-assembly steps minus the number of defects at step n.
- Distinction threshold T = 8: the minimum complexity required to satisfy all five τ-Distinction conditions.
- Half-life n_{1/2}: the number of steps for the defect budget to halve (from the geometric decay rate (1–ι_τ)^n of defect absorption, V part 3).

VI.L15 and VI.L16 prove that C(n) is monotone (non-decreasing) and the attractor basin is absorbing: once C(n) > T, the system cannot leave the basin without an external perturbation. VI.T44 proves the basin is entered under finite defect budget.

VI.T45 gives the timescale: once C(0) > 0 (any non-zero initial complexity), the attractor is reached in at most n_{1/2} · ⌈log₂(N/T)⌉ steps. For N ≈ 10³ (a few hundred chemical components), T = 8, and n_{1/2} ≈ geological timescale (millions of years), the bound is T_abio ≤ n_{1/2} · ⌈log₂(125)⌉ = 7 · n_{1/2} — well within geological time.

The logarithmic dependence on N/T is the key insight: even for very large initial systems, the timescale grows only logarithmically. This transforms the abiogenesis probability argument from an impossibility claim into an inevitability claim.

## Result Statement

VI.T45: Abiogenesis timescale T_abio ≤ n_{1/2} · ⌈log₂(N/8)⌉. Logarithmic bound from geometric defect decay. For any prebiotic system with C(0) > 0, abiogenesis is reached in finite, geologically plausible time.

