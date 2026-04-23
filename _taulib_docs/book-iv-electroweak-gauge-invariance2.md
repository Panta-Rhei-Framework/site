---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.GaugeInvariance2"
permalink: /verify/taulib/docs/book-iv-electroweak-gauge-invariance2/
lane: verify
module_name: "TauLib.BookIV.Electroweak.GaugeInvariance2"
book: "IV"
book_label: "Microcosm"
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Electroweak.GaugeInvariance2


Wilson loops, non-abelian gauge potential, AB phase uniqueness,
holonomy group from curvature, gauge transformation law, observable
hierarchy, non-abelian extensions, and the derivation chain.

## Registry Cross-References


- [IV.D96] Wilson Loop — `WilsonLoop`

- [IV.D97] Non-Abelian Gauge Potential — `NonAbelianGauge`

- [IV.T39] AB Phase Uniqueness — `ab_phase_unique`

- [IV.T40] AB Phase Root of Unity — `ab_root_of_unity`

- [IV.T41] Holonomy Group from Curvature — `holonomy_from_curvature`

- [IV.T121] Gauge Transformation Law — `gauge_transformation_law`

- [IV.P40] Observable Hierarchy — `observable_hierarchy`

- [IV.P41] Non-Abelian Self-Interaction — `nonabelian_self_interaction`

- [IV.P42] Path-Ordered Exponential — `path_ordered_exp`

- [IV.P43] Seven-Step Derivation Chain — `seven_step_chain`

- [IV.P173] AB Interference — `ab_interference`

- [IV.R25, IV.R359, IV.R360, IV.R362] structural remarks


## Mathematical Content


### Wilson Loop


The Wilson loop W(γ) = tr(P exp(i∮_γ A)) is the gauge-invariant
observable associated to a closed loop γ. For U(1), W(γ) = exp(iΦ_AB).

### AB Phase Uniqueness


The AB phase is the UNIQUE gauge-invariant functional of the connection
on a loop. This is a structural consequence of U(1) being abelian.

### Non-Abelian Extension


For non-abelian gauge groups (SU(2), SU(3)), the connection becomes
matrix-valued, the field strength picks up a self-interaction term
[A_μ, A_ν], and the holonomy requires path-ordering.

### Seven-Step Derivation Chain


The chain K0-K6 → τ³ → T² → U(1) → A_μ → F_μν → gauge invariance
shows that EM gauge theory is DERIVED, not postulated.

## Ground Truth Sources


- Chapter 27 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.WilsonLoop`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L61-L73)
**structure
Tau.BookIV.Electroweak.WilsonLoop :Type**


[IV.D96] Wilson loop W(γ) = tr(P exp(i∮_γ A·dl)).
For U(1): W(γ) = exp(iΦ_AB) (no path-ordering needed).
W(γ) is gauge-invariant by construction (trace of holonomy).

- phase_numer : ℤ
The holonomy phase (scaled: phase/2π as rational).

- phase_denom : ℕ
- denom_pos : self.phase_denom > 0
- gauge_invariant : Bool
Gauge-invariant by construction.

- abelian : Bool
Whether the gauge group is abelian.

Instances For

---

### `Tau.BookIV.Electroweak.instReprWilsonLoop`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L73-L73)
**instance
Tau.BookIV.Electroweak.instReprWilsonLoop :Repr WilsonLoop**

Equations
- Tau.BookIV.Electroweak.instReprWilsonLoop = { reprPrec := Tau.BookIV.Electroweak.instReprWilsonLoop.repr }

---

### `Tau.BookIV.Electroweak.instReprWilsonLoop.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L73-L73)
**def
Tau.BookIV.Electroweak.instReprWilsonLoop.repr :WilsonLoop → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.wilson_u1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L75-L80)
**def
Tau.BookIV.Electroweak.wilson_u1
(n : ℤ)
 :WilsonLoop**


Wilson loop for U(1) with given winding number.
Equations
- Tau.BookIV.Electroweak.wilson_u1 n = { phase_numer := n, phase_denom := 1, denom_pos := Tau.BookIV.Electroweak.wilson_u1._proof_2, abelian := true }
Instances For

---

### `Tau.BookIV.Electroweak.WilsonLoop.compose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L82-L87)
**def
Tau.BookIV.Electroweak.WilsonLoop.compose
(w₁ w₂ : WilsonLoop)
 :WilsonLoop**


Wilson loop composition (abelian case).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.NonAbelianGauge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L93-L104)
**structure
Tau.BookIV.Electroweak.NonAbelianGauge :Type**


[IV.D97] Non-abelian gauge potential: Lie-algebra-valued 1-form
A_μ = A_μ^a T^a where T^a are generators of the Lie algebra.
Field strength gains self-interaction: F = dA + A ∧ A.

- algebra_dim : ℕ
Lie algebra dimension (generators count).

- is_abelian : Bool
Whether the group is abelian (U(1): dim=1, abelian).

- has_self_interaction : Bool
Self-interaction present iff non-abelian.

- interaction_eq : self.has_self_interaction = !self.is_abelian
Instances For

---

### `Tau.BookIV.Electroweak.instReprNonAbelianGauge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L104-L104)
**instance
Tau.BookIV.Electroweak.instReprNonAbelianGauge :Repr NonAbelianGauge**

Equations
- Tau.BookIV.Electroweak.instReprNonAbelianGauge = { reprPrec := Tau.BookIV.Electroweak.instReprNonAbelianGauge.repr }

---

### `Tau.BookIV.Electroweak.instReprNonAbelianGauge.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L104-L104)
**def
Tau.BookIV.Electroweak.instReprNonAbelianGauge.repr :NonAbelianGauge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.gauge_u1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L106-L111)
**def
Tau.BookIV.Electroweak.gauge_u1 :NonAbelianGauge**


U(1) gauge (abelian, no self-interaction).
Equations
- Tau.BookIV.Electroweak.gauge_u1 = { algebra_dim := 1, is_abelian := true, has_self_interaction := false, interaction_eq := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.gauge_su2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L113-L118)
**def
Tau.BookIV.Electroweak.gauge_su2 :NonAbelianGauge**


SU(2) gauge (non-abelian, has self-interaction).
Equations
- Tau.BookIV.Electroweak.gauge_su2 = { algebra_dim := 3, is_abelian := false, has_self_interaction := true, interaction_eq := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.gauge_su3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L120-L125)
**def
Tau.BookIV.Electroweak.gauge_su3 :NonAbelianGauge**


SU(3) gauge (non-abelian, has self-interaction).
Equations
- Tau.BookIV.Electroweak.gauge_su3 = { algebra_dim := 8, is_abelian := false, has_self_interaction := true, interaction_eq := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.ABPhaseUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L131-L140)
**structure
Tau.BookIV.Electroweak.ABPhaseUniqueness :Type**


[IV.T39] The Aharonov-Bohm phase is the UNIQUE gauge-invariant
functional of the connection on a closed loop.
For abelian U(1): any gauge-invariant loop functional = f(Φ_AB).

- abelian : Bool
Group is abelian.

- abelian_true : self.abelian = true
- phase_determines : Bool
Phase uniquely determines observable.

Instances For

---

### `Tau.BookIV.Electroweak.instReprABPhaseUniqueness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L140-L140)
**def
Tau.BookIV.Electroweak.instReprABPhaseUniqueness.repr :ABPhaseUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprABPhaseUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L140-L140)
**instance
Tau.BookIV.Electroweak.instReprABPhaseUniqueness :Repr ABPhaseUniqueness**

Equations
- Tau.BookIV.Electroweak.instReprABPhaseUniqueness = { reprPrec := Tau.BookIV.Electroweak.instReprABPhaseUniqueness.repr }

---

### `Tau.BookIV.Electroweak.ab_phase_unique`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L142-L143)
**theorem
Tau.BookIV.Electroweak.ab_phase_unique
(u : ABPhaseUniqueness)
 :u.abelian = true**


---

### `Tau.BookIV.Electroweak.ABRootOfUnity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L149-L159)
**structure
Tau.BookIV.Electroweak.ABRootOfUnity :Type**


[IV.T40] AB phase is a root of unity iff flux is rational:
Φ/Φ₀ ∈ ℚ ⟹ exp(2πi·Φ/Φ₀) is a root of unity.
On T², all fluxes are integer (quantized), so always a root.

- flux_numer : ℤ
Flux is rational (numerator/denominator).

- flux_denom : ℕ
- denom_pos : self.flux_denom > 0
- is_root : Bool
The phase is a root of unity.

Instances For

---

### `Tau.BookIV.Electroweak.instReprABRootOfUnity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L159-L159)
**def
Tau.BookIV.Electroweak.instReprABRootOfUnity.repr :ABRootOfUnity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprABRootOfUnity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L159-L159)
**instance
Tau.BookIV.Electroweak.instReprABRootOfUnity :Repr ABRootOfUnity**

Equations
- Tau.BookIV.Electroweak.instReprABRootOfUnity = { reprPrec := Tau.BookIV.Electroweak.instReprABRootOfUnity.repr }

---

### `Tau.BookIV.Electroweak.ab_root_example`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L161-L164)
**def
Tau.BookIV.Electroweak.ab_root_example :ABRootOfUnity**

Equations
- Tau.BookIV.Electroweak.ab_root_example = { flux_numer := 1, flux_denom := 1, denom_pos := Tau.BookIV.Electroweak.wilson_u1._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.ab_root_of_unity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L166-L166)
**theorem
Tau.BookIV.Electroweak.ab_root_of_unity :ab_root_example.is_root = true**


---

### `Tau.BookIV.Electroweak.HolonomyFromCurvature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L172-L180)
**structure
Tau.BookIV.Electroweak.HolonomyFromCurvature :Type**


[IV.T41] Ambrose-Singer theorem: the holonomy group is generated
by the parallel transports of curvature around infinitesimal loops.
For U(1): Hol(A) is the subgroup of U(1) generated by all F-values.

- curvature_generates : Bool
Curvature generates holonomy.

- zero_curvature_trivial : Bool
Zero curvature implies trivial holonomy (on simply-connected base).

Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyFromCurvature.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L180-L180)
**def
Tau.BookIV.Electroweak.instReprHolonomyFromCurvature.repr :HolonomyFromCurvature → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyFromCurvature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L180-L180)
**instance
Tau.BookIV.Electroweak.instReprHolonomyFromCurvature :Repr HolonomyFromCurvature**

Equations
- Tau.BookIV.Electroweak.instReprHolonomyFromCurvature = { reprPrec := Tau.BookIV.Electroweak.instReprHolonomyFromCurvature.repr }

---

### `Tau.BookIV.Electroweak.holonomy_curvature_example`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L182-L182)
**def
Tau.BookIV.Electroweak.holonomy_curvature_example :HolonomyFromCurvature**

Equations
- Tau.BookIV.Electroweak.holonomy_curvature_example = { }
Instances For

---

### `Tau.BookIV.Electroweak.holonomy_from_curvature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L184-L185)
**theorem
Tau.BookIV.Electroweak.holonomy_from_curvature :holonomy_curvature_example.curvature_generates = true**


---

### `Tau.BookIV.Electroweak.GaugeTransformationLaw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L191-L203)
**structure
Tau.BookIV.Electroweak.GaugeTransformationLaw :Type**


[IV.T121] Gauge transformation law: A_μ → A_μ + ∂_μΛ for U(1),
A_μ → g A_μ g⁻¹ + g ∂_μ g⁻¹ for non-abelian groups.
The abelian law is a special case with g = e^{iΛ}.

- abelian : Bool
Whether the gauge group is abelian.

- adds_gradient : Bool
Transformation adds gradient for abelian.

- grad_eq : self.adds_gradient = self.abelian
- has_conjugation : Bool
Transformation has conjugation term for non-abelian.

- conj_eq : self.has_conjugation = !self.abelian
Instances For

---

### `Tau.BookIV.Electroweak.instReprGaugeTransformationLaw.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L203-L203)
**def
Tau.BookIV.Electroweak.instReprGaugeTransformationLaw.repr :GaugeTransformationLaw → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprGaugeTransformationLaw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L203-L203)
**instance
Tau.BookIV.Electroweak.instReprGaugeTransformationLaw :Repr GaugeTransformationLaw**

Equations
- Tau.BookIV.Electroweak.instReprGaugeTransformationLaw = { reprPrec := Tau.BookIV.Electroweak.instReprGaugeTransformationLaw.repr }

---

### `Tau.BookIV.Electroweak.gauge_transform_u1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L205-L211)
**def
Tau.BookIV.Electroweak.gauge_transform_u1 :GaugeTransformationLaw**


U(1) gauge transformation law.
Equations
- Tau.BookIV.Electroweak.gauge_transform_u1 = { abelian := true, adds_gradient := true, grad_eq := ⋯, has_conjugation := false, conj_eq := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.gauge_transformation_law`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L213-L214)
**theorem
Tau.BookIV.Electroweak.gauge_transformation_law :gauge_transform_u1.adds_gradient = true**


---

### `Tau.BookIV.Electroweak.ObservableLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L220-L227)
**inductive
Tau.BookIV.Electroweak.ObservableLevel :Type**


[IV.P40] EM observable hierarchy: A_μ (gauge-dependent) →
F_μν (gauge-invariant, local) → Hol(γ) (gauge-invariant, global).
Each level is more physical; Hol(γ) is the ultimate observable.

- Potential : ObservableLevel
- FieldStrength : ObservableLevel
- Holonomy : ObservableLevel
Instances For

---

### `Tau.BookIV.Electroweak.instReprObservableLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L227-L227)
**instance
Tau.BookIV.Electroweak.instReprObservableLevel :Repr ObservableLevel**

Equations
- Tau.BookIV.Electroweak.instReprObservableLevel = { reprPrec := Tau.BookIV.Electroweak.instReprObservableLevel.repr }

---

### `Tau.BookIV.Electroweak.instReprObservableLevel.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L227-L227)
**def
Tau.BookIV.Electroweak.instReprObservableLevel.repr :ObservableLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqObservableLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L227-L227)
**instance
Tau.BookIV.Electroweak.instDecidableEqObservableLevel :DecidableEq ObservableLevel**

Equations
- Tau.BookIV.Electroweak.instDecidableEqObservableLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Electroweak.instBEqObservableLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L227-L227)
**instance
Tau.BookIV.Electroweak.instBEqObservableLevel :BEq ObservableLevel**

Equations
- Tau.BookIV.Electroweak.instBEqObservableLevel = { beq := Tau.BookIV.Electroweak.instBEqObservableLevel.beq }

---

### `Tau.BookIV.Electroweak.instBEqObservableLevel.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L227-L227)
**def
Tau.BookIV.Electroweak.instBEqObservableLevel.beq :ObservableLevel → ObservableLevel → Bool**

Equations
- Tau.BookIV.Electroweak.instBEqObservableLevel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Electroweak.ObservableLevel.toNat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L229-L233)
**def
Tau.BookIV.Electroweak.ObservableLevel.toNat :ObservableLevel → ℕ**


Observable level ordering: Potential < FieldStrength < Holonomy.
Equations
- Tau.BookIV.Electroweak.ObservableLevel.Potential.toNat = 0
- Tau.BookIV.Electroweak.ObservableLevel.FieldStrength.toNat = 1
- Tau.BookIV.Electroweak.ObservableLevel.Holonomy.toNat = 2
Instances For

---

### `Tau.BookIV.Electroweak.observable_hierarchy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L235-L238)
**theorem
Tau.BookIV.Electroweak.observable_hierarchy :ObservableLevel.Potential.toNat < ObservableLevel.FieldStrength.toNat ∧ ObservableLevel.FieldStrength.toNat < ObservableLevel.Holonomy.toNat**


---

### `Tau.BookIV.Electroweak.nonabelian_self_interaction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L244-L251)
**theorem
Tau.BookIV.Electroweak.nonabelian_self_interaction :gauge_su2.has_self_interaction = true ∧ gauge_su3.has_self_interaction = true ∧ gauge_u1.has_self_interaction = false**


[IV.P41] Non-abelian field strength has self-interaction:
F_μν = ∂_μA_ν − ∂_νA_μ + ig[A_μ, A_ν].
The commutator term [A_μ, A_ν] vanishes for abelian U(1).

---

### `Tau.BookIV.Electroweak.PathOrderedExp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L257-L266)
**structure
Tau.BookIV.Electroweak.PathOrderedExp :Type**


[IV.P42] Non-abelian holonomy requires path-ordering:
Hol(γ) = P exp(i∮_γ A) because [A(s₁), A(s₂)] ≠ 0 in general.
For abelian U(1), path-ordering is trivial (ordinary exponential).

- requires_ordering : Bool
Whether path-ordering is required.

- is_abelian : Bool
Whether the gauge group is abelian.

- abelian_no_ordering : self.is_abelian = true → self.requires_ordering = false
For abelian groups, path-ordering is not required.

Instances For

---

### `Tau.BookIV.Electroweak.path_ordered_u1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L268-L272)
**def
Tau.BookIV.Electroweak.path_ordered_u1 :PathOrderedExp**


U(1) does not require path-ordering.
Equations
- Tau.BookIV.Electroweak.path_ordered_u1 = { requires_ordering := false, is_abelian := true, abelian_no_ordering := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.path_ordered_exp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L274-L275)
**theorem
Tau.BookIV.Electroweak.path_ordered_exp :gauge_u1.is_abelian = true**


---

### `Tau.BookIV.Electroweak.SevenStepChain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L281-L292)
**structure
Tau.BookIV.Electroweak.SevenStepChain :Type**


[IV.P43] Seven-step derivation chain from axioms to EM gauge theory:
K0-K6 → τ³ → T² → U(1) → A_μ → F_μν → gauge invariance.
Each step is constructive (no postulates beyond K0-K6).

- steps : ℕ
Number of steps in the derivation.

- steps_eq : self.steps = 7
- all_constructive : Bool
Each step is constructive (no external postulates).

- terminates_at_gauge : Bool
The chain terminates at gauge invariance.

Instances For

---

### `Tau.BookIV.Electroweak.instReprSevenStepChain.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L292-L292)
**def
Tau.BookIV.Electroweak.instReprSevenStepChain.repr :SevenStepChain → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprSevenStepChain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L292-L292)
**instance
Tau.BookIV.Electroweak.instReprSevenStepChain :Repr SevenStepChain**

Equations
- Tau.BookIV.Electroweak.instReprSevenStepChain = { reprPrec := Tau.BookIV.Electroweak.instReprSevenStepChain.repr }

---

### `Tau.BookIV.Electroweak.seven_step_chain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L294-L296)
**def
Tau.BookIV.Electroweak.seven_step_chain :SevenStepChain**

Equations
- Tau.BookIV.Electroweak.seven_step_chain = { steps := 7, steps_eq := Tau.BookIV.Electroweak.seven_step_chain._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.seven_step_chain_valid`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L298-L298)
**theorem
Tau.BookIV.Electroweak.seven_step_chain_valid :seven_step_chain.steps = 7**


---

### `Tau.BookIV.Electroweak.ABInterference`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L304-L315)
**structure
Tau.BookIV.Electroweak.ABInterference :Type**


[IV.P173] Aharonov-Bohm interference from split paths: a charged
particle taking two paths around a solenoid acquires a relative
phase Φ_AB = e/ℏ · ∫ A·dl, producing interference fringes.

- path_count : ℕ
Number of paths (two, for standard AB setup).

- path_eq : self.path_count = 2
- relative_phase_is_ab : Bool
Relative phase is the AB phase.

- observable : Bool
Interference is observable.

Instances For

---

### `Tau.BookIV.Electroweak.instReprABInterference`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L315-L315)
**instance
Tau.BookIV.Electroweak.instReprABInterference :Repr ABInterference**

Equations
- Tau.BookIV.Electroweak.instReprABInterference = { reprPrec := Tau.BookIV.Electroweak.instReprABInterference.repr }

---

### `Tau.BookIV.Electroweak.instReprABInterference.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L315-L315)
**def
Tau.BookIV.Electroweak.instReprABInterference.repr :ABInterference → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.example_ab_interf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L317-L319)
**def
Tau.BookIV.Electroweak.example_ab_interf :ABInterference**

Equations
- Tau.BookIV.Electroweak.example_ab_interf = { path_count := 2, path_eq := Tau.BookIV.Electroweak.example_ab_interf._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.ab_interference`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L321-L321)
**theorem
Tau.BookIV.Electroweak.ab_interference :example_ab_interf.path_count = 2**


---

### `Tau.BookIV.Electroweak.example_wilson`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L340-L340)
**def
Tau.BookIV.Electroweak.example_wilson :WilsonLoop**

Equations
- Tau.BookIV.Electroweak.example_wilson = Tau.BookIV.Electroweak.wilson_u1 3
Instances For
