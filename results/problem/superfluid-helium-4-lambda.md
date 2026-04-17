---

layout: result-page
title: 'Superfluid Helium-4: Minimal Donut Criterion from ι_τ'
permalink: /results/problem/superfluid-helium-4-lambda/
result_id: result-251
topic: physics
layer: physics
result_type: structural_readout
bridge_status: internal
result_kind: frontier-problem
importance_class: domain-level-open-problem
status_code: R
domain_group: "Physics"
summary_short: 'Superfluid transition in Helium-4 at T_λ ≈ 2.17 K derives from the Minimal Donut Criterion cos(π/N) ≥ 1 − ι_τ (Book IV ch61): N=3 (He-3) fails at 0.500 < 0.659; N=4 (He-4) passes at 0.707 ≥ 0.659. A first-principles selection rule from the master constant ι_τ.'
canonical_books: ["IV"]
right_rail:
  meta:
    type: Structural Readout
    layer: Physics
    topic: Physics
    status: Internal
    updated: April 2026
---

## Overview

Helium-4 exhibits a superfluid λ-transition at T_λ ≈ 2.17 K, while Helium-3 does not (its transition to a BCS-like superfluid state occurs at ~2.5 mK, via Cooper pairing, under entirely different physics). Book IV ch61 ("Superfluids and Superconductors") derives the distinction from first principles. The Minimal Donut Criterion (prop:iv-he4-criterion) states that bosonic superfluidity requires cos(π/N) ≥ 1 − ι_τ, where ι_τ = 2/(π+e) ≈ 0.3413 is the master constant and N is a nucleon-count parameter. Numerically: κ_D = 1 − ι_τ ≈ 0.6587; for N=3 the inequality gives 0.500 < 0.659 (He-3 fails); for N=4 it gives 0.707 ≥ 0.659 (He-4 passes). Helium-4 is the minimal nucleus permitted to form a τ-superfluid.

## Detail

The orthodox picture of superfluid He-4 — Landau's two-fluid model, Bose-Einstein condensation of zero-momentum bosons — correctly describes the phenomenology but does not answer the structural question: why is He-4 the lightest system exhibiting bosonic superfluidity, and why at T_λ ≈ 2.17 K specifically? Book IV (`books/IV-CategoricalMicrocosm/latex/sections/part07/ch61-superfluids-superconductors.tex`) treats bosonic superfluidity as a τ-regime defined on the T² fiber. def:iv-superfluid-regime (line 44) specifies the regime; prop:iv-he4 (line 101) derives the He-4 superfluid state from T² readout, with T_λ ≈ 2.17 K arising as a continuous-to-quantised threshold for the fiber coordinate d̄₂. prop:iv-he4-criterion (line 119) is the Minimal Donut Criterion: a nucleus of nucleon count N can form a τ-superfluid only if cos(π/N) ≥ 1 − ι_τ. The geometric origin is the wedge-point angular defect of the lemniscate L = S¹ ∨ S¹: the donut (torus) that forms the superfluid condensate must accommodate the wedge angle, which sets the threshold 1 − ι_τ. Numerically κ_D = 1 − ι_τ ≈ 0.6587; for N=3 (He-3) one has cos(π/3) = 0.500, below threshold; for N=4 (He-4) cos(π/4) = 0.707, above threshold. Helium-4 is therefore the minimal nucleus capable of forming a τ-superfluid, and the λ-transition temperature follows from the fiber structure rather than from fitted parameters.

## Result Statement

prop:iv-he4 + prop:iv-he4-criterion (Book IV ch61): Minimal Donut Criterion cos(π/N) ≥ 1 − ι_τ. He-3 (N=3) fails at 0.500 < 0.659 = κ_D; He-4 (N=4) passes at 0.707 ≥ 0.659. T_λ ≈ 2.17 K from T² fiber readout — not phenomenological.
