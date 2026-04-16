---
layout: prediction-page
title: "Coronal Heating Damping Scale"
title_plain: "Coronal Heating Damping Scale"
permalink: /predictions/pred-66/
lane: results
prediction_id: "pred-066"
domain: "collective-dynamics"
domain_display: "Collective Dynamics"
observable: "ℓᵣₘ ₕₑₐₜ"
observable_mathml: "<math><mi>ι<sub>τ</sub>²,R_⊙</mi></math>"
formula_plain: "ι<sub>τ</sub>²,R_⊙"
formula_mathml: "<math><mi>ι<sub>τ</sub>²,R_⊙</mi></math>"
formula_display: "ℓ_heat = ι<sub>τ</sub>² · R_☉ ≈ 0.117 R_☉"
tau_value: "0.117,R_⊙"
observed_value: "≈!0.1,R_⊙"
deviation: "∼ 15%"
precision_tier: "structural"
precision_display: "Structural"
registry_id: "V.T253"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Coronal Heating Damping Scale: τ-value 0.117,R_⊙, observed ≈!0.1,R_⊙, deviation ∼ 15%."
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
    scope: "τ-Effective"
    updated: "April 2026"
---

## τ-Formula

**ℓ_heat = ι<sub>τ</sub>² · R_☉ ≈ 0.117 R_☉**

## Derivation

F_τ
\;=\;
ρ\,v_A\,v_conv^2
\;(1 - e^-ι<sub>τ</sub>^2\,L/λ_A),

where $ρ$ is the photospheric
mass density,
$v_A$ the Alfv\'en speed,
$v_conv ∼ 1$ km/s
the convective velocity,
$L$ the coronal loop length,
and $λ_A$ the dominant
Alfv\'en wavelength.
No free parameters enter the damping
fraction $ι<sub>τ</sub>^2$.

Numerical evaluation.
For typical active-region parameters
($ρ ∼ 3 × 10^-15$ g cm$^-3$,
$B_0 ∼ 100$ G,
$v_conv ∼ 1$ km/s,
$L ∼ 10^10$ cm,
$λ_A ∼ 10^9$ cm):

- The Alfv\'en speed is
$v_A = B_0/4πρ
≈ 1.6 × 10^8$ cm s$^-1$.
- The wave energy flux is
$F_A = ρ\,v_A\,v_conv^2
≈ 4.9 × 10^5
\;erg\;cm^-2\;s^-1$.
- The damping fraction is
$1 - (-ι<sub>τ</sub>^2\,L/λ_A)
= 1 - (-0.117 × 10)
≈ 0.69$.
- The heating flux is
$F_τ ≈ 3.4 × 10^5
\;erg\;cm^-2\;s^-1$.

## Source

This prediction is derived in the Physics Ledger (Chapter 65 — collective-dynamics), Books IV–V of *Panta Rhei*.

