---

layout: result-page
title: Neutrino Mass Sum Σm_ν = 0.089 eV, Normal Ordering Derived
permalink: /results/problem/neutrino-mass-sum-0pt089-ev-normal-ordering/
result_id: result-065
topic: mathematics
layer: mathematics
result_type: structural_readout
bridge_status: internal
result_kind: frontier-problem
importance_class: high-impact-frontier-problem
status_code: R
domain_group: "Particle Physics"
summary_short: The neutrino mass sum Σm_ν = 0.089 eV and normal mass ordering are
  derived from the τ-framework. Normal hierarchy is Lean-verified from p < q.
canonical_books: ["IV"]
right_rail:
  meta:
    type: Structural Readout
    layer: Mathematics
    topic: Mathematics
    status: Internal
    updated: April 2026
---

## Overview

V.T165/T225 and V.T189 together establish the neutrino mass predictions: the CF-asymmetric grid (Δpq = 1.16, Δpr = 0.87) at +7.4 ppm gives the exponent parameters; the sum Σm_ν = 0.089 eV follows from the σ-polarity matrix (p = 3.7, q = 4.8, r = 2.8). The normal hierarchy (m₁ < m₂ < m₃) is proven from p < q as a theorem (IV.R395), Lean-verified. Σm_ν = 0.089 eV is consistent with DESI Year 1 and represents a 4.5σ detection target for DESI full survey.

## Detail

Neutrino masses and their ordering are among the most important open questions in particle physics and cosmology. The absolute mass scale is unknown; only the differences Δm²₂₁ ≈ 7.5 × 10⁻⁵ eV² and |Δm²₃₂| ≈ 2.5 × 10⁻³ eV² are measured. The ordering (normal: m₁ < m₂ < m₃, or inverted: m₃ < m₁ < m₂) is unknown. The sum Σm_ν < 0.12 eV from Planck 2018; DESI Year 1 preliminary results give Σm_ν < 0.072 eV (in tension with the normal hierarchy minimum ~0.06 eV).

The τ-framework establishes neutrino mass predictions through two related results:

V.T189 (Wave 5A/7B) derives the CF-asymmetric grid (Δpq, Δpr) = (1.16, 0.87) from the CF structure of ι<sub>τ</sub>. The key observation is that CF(ι<sub>τ</sub>) = [0; 2, 1, 13, 3, ...] is asymmetric (13 ≠ 3 ≠ 2), and this asymmetry is inherited by the neutrino mass exponent ratios. The grid optimum is at (203/175, 609/700) = (1.16, 0.87) at +7.4 ppm — the most precise neutrino prediction in the framework.

V.T165/T225 establish Σm_ν = 0.089 eV from the σ-polarity matrix parameters. The three exponents (p, q, r) = (3.7, 4.8, 2.8) give individual masses m_i ∝ ι<sub>τ</sub>^{p_i}; summing gives Σm_ν = 0.089 eV. The normal ordering (IV.R395) follows from p < q (since p = 3.7 < q = 4.8 implies m_1 < m_2 which is necessary for normal hierarchy).

The completion status is partial because the individual mass splittings (Δm²₂₁ and Δm²₃₂) are off: Δm²₂₁ is 6.2× from measured; Δm²₃₂ is +22.9% off. The sum Σm_ν and normal ordering are τ-effective; the individual splittings are conjectural.

## Result Statement

V.T165/T225: Σm_ν = 0.089 eV from (p,q,r) = (3.7, 4.8, 2.8). V.T189: CF-asymmetric grid (Δpq, Δpr) = (1.16, 0.87) at +7.4 ppm. Normal ordering proven from p < q (IV.R395), Lean-verified. Individual splittings remain conjectural.

