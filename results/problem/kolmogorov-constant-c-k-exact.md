---

layout: result-page
title: Kolmogorov Constant C_K = 3/2 Exact from dim(τ³)/dim(T²)
permalink: /results/problem/kolmogorov-constant-c-k-exact/
result_id: result-063
topic: mathematics
layer: mathematics
result_type: structural_readout
bridge_status: internal
result_kind: foundational-math
importance_class: structural-support-result
status_code: R
domain_group: "Mathematics"
summary_short: The Kolmogorov constant C_K = 3/2 is derived exactly as dim(τ³)/dim(T²)
  = 3/2, with no free parameters.
canonical_books: ["V"]
right_rail:
  meta:
    type: Structural Readout
    layer: Mathematics
    topic: Mathematics
    status: Internal
    updated: April 2026
---

## Overview

V.T251 proves that the Kolmogorov inertial-range constant C_K = 3/2 exactly, as the ratio of the dimensions of τ³ and T²: dim(τ³)/dim(T²) = 3/2. The Kolmogorov constant appears in the energy spectrum E(k) = C_K ε^{2/3} k^{–5/3} of fully developed turbulence. Its empirical value is C_K ≈ 1.5 ± 0.1 from DNS and experiments; the τ-framework predicts the exact value 3/2 without any fitting.

## Detail

The Kolmogorov energy spectrum E(k) = C_K ε^{2/3} k^{–5/3} describes how energy is distributed across scales in fully developed turbulence. The exponent –5/3 (Kolmogorov 1941) is derived from dimensional analysis alone. The prefactor C_K ≈ 1.5, however, is not dimensionally determined — it is a pure number that must be measured experimentally or computed from DNS. Its empirical value is C_K ≈ 1.5 ± 0.1 from direct numerical simulations and laboratory experiments.

V.T250/T251 derive the Kolmogorov spectrum and constant within the τ-framework. The –5/3 exponent follows from the dimensional structure of τ³ with the same argument as the Kolmogorov 1941 derivation. The prefactor C_K = dim(τ³)/dim(T²) = 3/2 follows because the inertial-range cascade occurs on τ³ (3D turbulence) but energy is transferred through T² fiber modes (2D structures). The ratio 3/2 is an exact integer fraction.

This result is in the Crown Jewels list at rank 20 (score 39) and is closely related to the She–Lévêque exponent derivation (V.T248, result-051). Together V.T248 and V.T251 give a complete τ-account of the statistical geometry of turbulence: the anomalous exponents (She–Lévêque) and the prefactor (Kolmogorov) follow from the same dimensional structure dim(τ³) = 3, dim(T²) = 2.

## Result Statement

V.T251: C_K = 3/2 = dim(τ³)/dim(T²) exactly. Zero free parameters. Consistent with experimental value C_K ≈ 1.5 ± 0.1 from DNS.

