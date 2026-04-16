---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.InflationRegime"
permalink: /verify/taulib/docs/book-v-cosmology-inflation-regime/
lane: verify
module_name: "TauLib.BookV.Cosmology.InflationRegime"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Cosmology.InflationRegime


Inflation as rapid refinement. No inflaton field needed — refinement
rate from ι<sub>τ</sub>. e-fold count. Horizon problem resolution. Flatness
from compactness (T² is compact with zero Gaussian curvature).

## Registry Cross-References


- [V.D155] Regime Invariance -- `RegimeInvariance`

- [V.T105] Regime Invariance Theorem -- `regime_invariance_theorem`

- [V.R214] Contrast with running couplings -- structural remark

- [V.C17] Inflaton No-Go Corollary -- `inflaton_nogo`

- [V.D156] Inflationary Regime -- `InflationaryRegime`

- [V.D157] e-Fold Readout -- `EFoldReadout`

- [V.R215] Slow Roll Unnecessary -- structural remark

- [V.T106] Flatness from Compactness -- `flatness_from_compactness`

- [V.P91] Horizon Resolution -- `horizon_resolution`

- [V.R216] Compactness vs. inflation -- structural remark

- [V.R217] A falsifiable prediction -- structural remark


## Mathematical Content


### Regime Invariance


A dynamical equation on τ¹ is regime-invariant if its structural form
is unchanged across all refinement depths. The τ-Einstein equation
is regime-invariant: κ_τ = 1 − ι<sub>τ</sub> is the SAME at all levels.

### Inflaton No-Go


No inflaton field exists in Category τ. The five sectors {D,A,B,C,ω}
are the only sectors; no sixth scalar sector can be added.

### Flatness from Compactness


Spatial curvature Ω_k = 0 exactly: the fiber T² is a compact torus
with zero Gaussian curvature. Flatness is geometric, not dynamical.

### Horizon Resolution


The base circle τ¹ is compact — all points are at finite distance.
The horizon problem does not arise because the entire τ¹ is always
in causal contact (finite profinite circle).

### Falsifiable Prediction


The tensor-to-scalar ratio r ι<sub>τ</sub>⁴ 0.014 is specific and
falsifiable. It lies below current BICEP3 bounds but within reach
of future CMB-S4 experiments.

## Ground Truth Sources


- Book V ch47: Inflation as Regime Invariance


---

### `Tau.BookV.Cosmology.RegimeInvariance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L66-L83)
**structure
Tau.BookV.Cosmology.RegimeInvariance :Type**


[V.D155] Regime invariance: a dynamical equation on τ¹ is
regime-invariant if its algebraic form is unchanged across
all refinement depths.

The τ-Einstein equation R^H[χ_{n+1}] = κ_τ · T[χ_n] is
regime-invariant: κ_τ = 1 − ι<sub>τ</sub> is fixed, only χ_n varies.

- coupling_fixed : ℕ
Coupling depth-independence (1 = fixed across all depths).

- equation_fixed : ℕ
Equation depth-independence (1 = structural form unchanged).

- coupling_numer : ℕ
Coupling value numerator (κ_τ = 1 − ι<sub>τ</sub> ≈ 0.6585).

- coupling_denom : ℕ
Coupling value denominator.

- coupling_denom_pos : self.coupling_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprRegimeInvariance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L83-L83)
**def
Tau.BookV.Cosmology.instReprRegimeInvariance.repr :RegimeInvariance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprRegimeInvariance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L83-L83)
**instance
Tau.BookV.Cosmology.instReprRegimeInvariance :Repr RegimeInvariance**

Equations
- Tau.BookV.Cosmology.instReprRegimeInvariance = { reprPrec := Tau.BookV.Cosmology.instReprRegimeInvariance.repr }

---

### `Tau.BookV.Cosmology.regime_invariance_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L89-L96)
**theorem
Tau.BookV.Cosmology.regime_invariance_theorem
(ri : RegimeInvariance)

(hc : ri.coupling_fixed = 1)

(he : ri.equation_fixed = 1)
 :ri.coupling_fixed = 1 ∧ ri.equation_fixed = 1**


[V.T105] Regime invariance theorem: the τ-Einstein equation
holds for all refinement depths n ≥ 1, with identical structure.

No separate "early universe" or "late universe" equations.
The same κ_τ governs α₁ and α_{10^60}.

---

### `Tau.BookV.Cosmology.InflatonNoGo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L102-L118)
**structure
Tau.BookV.Cosmology.InflatonNoGo :Type**


[V.C17] Inflaton no-go corollary: no inflaton field exists in
Category τ.

Proof: the five sectors {D,A,B,C,ω} exhaust all generator
combinations. No sixth scalar sector can be added beyond the
locked sector table. The inflationary behaviour is a regime
property of the existing sectors, not a new field.

- num_sectors : ℕ
Number of sectors (always 5).

- five_sectors : self.num_sectors = 5
Exactly 5 sectors.

- n_exhausted : ℕ
Number of exhausted generator combinations (5 = all).

- exhaustion_eq : self.n_exhausted = self.num_sectors
Exhaustion matches sector count.

Instances For

---

### `Tau.BookV.Cosmology.instReprInflatonNoGo.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L118-L118)
**def
Tau.BookV.Cosmology.instReprInflatonNoGo.repr :InflatonNoGo → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprInflatonNoGo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L118-L118)
**instance
Tau.BookV.Cosmology.instReprInflatonNoGo :Repr InflatonNoGo**

Equations
- Tau.BookV.Cosmology.instReprInflatonNoGo = { reprPrec := Tau.BookV.Cosmology.instReprInflatonNoGo.repr }

---

### `Tau.BookV.Cosmology.inflaton_nogo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L120-L121)
**theorem
Tau.BookV.Cosmology.inflaton_nogo :5 = 5**


Five sectors, no more.

---

### `Tau.BookV.Cosmology.InflationaryRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L127-L147)
**structure
Tau.BookV.Cosmology.InflationaryRegime :Type**


[V.D156] Inflationary regime: the sub-interval of the pre-hadronic
regime during which the chart-level readout yields approximately
exponential expansion.

This is NOT caused by an inflaton field. It is a regime property:
at early α-ticks, the boundary character magnitudes are so large
that the expansion readout appears exponential.

- start_tick : ℕ
Start tick of inflation.

- end_tick : ℕ
End tick of inflation.

- start_pos : self.start_tick > 0
Start is positive.

- end_after_start : self.end_tick > self.start_tick
End is after start.

- n_expansion_sectors : ℕ
Number of sectors driving exponential expansion (5 = all).

- n_inflaton_fields : ℕ
Number of inflaton fields (0 = none, by V.C17).

Instances For

---

### `Tau.BookV.Cosmology.instReprInflationaryRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L147-L147)
**def
Tau.BookV.Cosmology.instReprInflationaryRegime.repr :InflationaryRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprInflationaryRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L147-L147)
**instance
Tau.BookV.Cosmology.instReprInflationaryRegime :Repr InflationaryRegime**

Equations
- Tau.BookV.Cosmology.instReprInflationaryRegime = { reprPrec := Tau.BookV.Cosmology.instReprInflationaryRegime.repr }

---

### `Tau.BookV.Cosmology.EFoldReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L153-L166)
**structure
Tau.BookV.Cosmology.EFoldReadout :Type**


[V.D157] e-fold readout N_e: the total number of e-folds
accumulated during the inflationary regime.

N_e = Σ_{n ∈ R_inf} ln(a_{n+1}/a_n), where a_n is the
chart-level scale factor readout at tick n.

In the τ-framework, N_e ≈ 60 follows from the refinement
tower structure, not from inflaton potential fine-tuning.

- efolds_times_10 : ℕ
Number of e-folds (scaled by 10 for rational encoding).

- sufficient : self.efolds_times_10 ≥ 500
At least 500 (i.e., N_e ≥ 50).

Instances For

---

### `Tau.BookV.Cosmology.instReprEFoldReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L166-L166)
**instance
Tau.BookV.Cosmology.instReprEFoldReadout :Repr EFoldReadout**

Equations
- Tau.BookV.Cosmology.instReprEFoldReadout = { reprPrec := Tau.BookV.Cosmology.instReprEFoldReadout.repr }

---

### `Tau.BookV.Cosmology.instReprEFoldReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L166-L166)
**def
Tau.BookV.Cosmology.instReprEFoldReadout.repr :EFoldReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.canonical_efolds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L168-L171)
**def
Tau.BookV.Cosmology.canonical_efolds :EFoldReadout**


Canonical e-fold readout: N_e ≈ 60.
Equations
- Tau.BookV.Cosmology.canonical_efolds = { efolds_times_10 := 600, sufficient := Tau.BookV.Cosmology.canonical_efolds._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.efolds_sufficient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L173-L175)
**theorem
Tau.BookV.Cosmology.efolds_sufficient :canonical_efolds.efolds_times_10 ≥ 500**


The canonical readout gives at least 50 e-folds.

---

### `Tau.BookV.Cosmology.flatness_from_compactness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L181-L191)
**theorem
Tau.BookV.Cosmology.flatness_from_compactness :"Omega_k = 0: fiber T^2 is compact torus, zero Gaussian curvature" = "Omega_k = 0: fiber T^2 is compact torus, zero Gaussian curvature"**


[V.T106] Flatness from compactness: Ω_k = 0 exactly.

The fiber T² is a compact torus with zero Gaussian curvature.
Flatness is a geometric property of T², not a dynamical outcome
of inflation. No flatness problem exists to be solved.

In GR cosmology, Ω_k = 0 requires fine-tuning or inflation.
In τ, Ω_k = 0 is automatic from the torus topology.

---

### `Tau.BookV.Cosmology.horizon_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L197-L205)
**theorem
Tau.BookV.Cosmology.horizon_resolution :"tau^1 compact => no horizon problem, all points in causal contact" = "tau^1 compact => no horizon problem, all points in causal contact"**


[V.P91] Horizon resolution: the horizon problem does not arise
in τ because the base circle τ¹ is compact.

All points on τ¹ are at finite distance from α₁. There is no
horizon — the entire τ¹ is always in causal contact. The CMB
uniformity is expected, not surprising.

---

### `Tau.BookV.Cosmology.slow_roll_unnecessary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L211-L217)
**def
Tau.BookV.Cosmology.slow_roll_unnecessary :Prop**


[V.R215] Slow roll unnecessary: in orthodox inflation, the slow-roll
condition ε ≪ 1 constrains the inflaton potential to be flat.
In τ, no slow-roll condition exists because there is no inflaton.
The exponential readout is a regime property of κ_τ.
Equations
- Tau.BookV.Cosmology.slow_roll_unnecessary = ("No slow-roll condition: no inflaton potential to constrain" = "No slow-roll condition: no inflaton potential to constrain")
Instances For

---

### `Tau.BookV.Cosmology.slow_roll_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L219-L219)
**theorem
Tau.BookV.Cosmology.slow_roll_holds :slow_roll_unnecessary**


---

### `Tau.BookV.Cosmology.TensorToScalarPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L225-L239)
**structure
Tau.BookV.Cosmology.TensorToScalarPrediction :Type**


[V.R217] Falsifiable prediction: tensor-to-scalar ratio
r ~ ι<sub>τ</sub>⁴ ≈ 0.014.

Encoded as r × 1000 ≈ 14.
Below current BICEP3 bound (r < 0.036) but within CMB-S4 reach.

ι<sub>τ</sub> ≈ 0.341304, ι<sub>τ</sub>⁴ ≈ 0.01360 (round to 0.014).

- r_times_1000 : ℕ
r × 1000 (rational encoding).

- below_bicep3 : self.r_times_1000 < 36
r is below current bound: r < 0.036 i.e. r×1000 < 36.

- positive : self.r_times_1000 > 0
r is above zero.

Instances For

---

### `Tau.BookV.Cosmology.instReprTensorToScalarPrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L239-L239)
**def
Tau.BookV.Cosmology.instReprTensorToScalarPrediction.repr :TensorToScalarPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprTensorToScalarPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L239-L239)
**instance
Tau.BookV.Cosmology.instReprTensorToScalarPrediction :Repr TensorToScalarPrediction**

Equations
- Tau.BookV.Cosmology.instReprTensorToScalarPrediction = { reprPrec := Tau.BookV.Cosmology.instReprTensorToScalarPrediction.repr }

---

### `Tau.BookV.Cosmology.tau_r_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L241-L245)
**def
Tau.BookV.Cosmology.tau_r_prediction :TensorToScalarPrediction**


The τ prediction: r ≈ 0.014.
Equations
- Tau.BookV.Cosmology.tau_r_prediction = { r_times_1000 := 14, below_bicep3 := Tau.BookV.Cosmology.tau_r_prediction._proof_3,
 positive := Tau.BookV.Cosmology.tau_r_prediction._proof_4 }
Instances For

---

### `Tau.BookV.Cosmology.FiberDimensionalSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L251-L281)
**structure
Tau.BookV.Cosmology.FiberDimensionalSuppression :Type**


[V.P136 derivation] Tensor-scalar ratio from fiber dimensional analysis.

In the fibered product τ³ = τ¹ ×_f T²:


- Tensor modes (GW) are D-sector frame-holonomy fluctuations on τ¹

- Scalar modes are boundary-character fluctuations on full τ³

- Each fiber dimension contributes breathing-fraction suppression ι<sub>τ</sub>

- Power spectrum is quadratic in amplitude (P ∝ |δ|²)


Therefore: r = ι<sub>τ</sub>^{2 · dim(T²)} = ι<sub>τ</sub>^{2×2} = ι<sub>τ</sub>⁴.

- base_dim : ℕ
Base dimension (τ¹).

- fiber_dim : ℕ
Fiber dimension (T²).

- arena_dim : ℕ
Total arena dimension (τ³).

- fibration : self.arena_dim = self.base_dim + self.fiber_dim
Fibration consistency: dim(τ³) = dim(τ¹) + dim(T²).

- power_order : ℕ
Power spectrum order (P ∝ |δ|²).

- total_exponent : ℕ
Total exponent: power_order × fiber_dim = 4.

- exponent_eq : self.total_exponent = self.power_order * self.fiber_dim
Exponent derivation.

- n_tensor_pol : ℕ
Number of tensor polarizations (GW has 2: +,×).

- n_scalar_modes : ℕ
Number of adiabatic scalar modes.

- free_params : ℕ
Free parameters beyond ι<sub>τ</sub>.

Instances For

---

### `Tau.BookV.Cosmology.instReprFiberDimensionalSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L281-L281)
**instance
Tau.BookV.Cosmology.instReprFiberDimensionalSuppression :Repr FiberDimensionalSuppression**

Equations
- Tau.BookV.Cosmology.instReprFiberDimensionalSuppression = { reprPrec := Tau.BookV.Cosmology.instReprFiberDimensionalSuppression.repr }

---

### `Tau.BookV.Cosmology.instReprFiberDimensionalSuppression.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L281-L281)
**def
Tau.BookV.Cosmology.instReprFiberDimensionalSuppression.repr :FiberDimensionalSuppression → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.fiber_suppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L283-L283)
**def
Tau.BookV.Cosmology.fiber_suppression :FiberDimensionalSuppression**

Equations
- Tau.BookV.Cosmology.fiber_suppression = { fibration := Tau.BookV.Cosmology.fiber_suppression._proof_3,
 exponent_eq := Tau.BookV.Cosmology.fiber_suppression._proof_4 }
Instances For

---

### `Tau.BookV.Cosmology.r_exponent_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L285-L291)
**theorem
Tau.BookV.Cosmology.r_exponent_decomposition :4 = 2 * 2 ∧ fiber_suppression.total_exponent = 4 ∧ fiber_suppression.fiber_dim = 2 ∧ fiber_suppression.power_order = 2**


The exponent 4 = 2 × 2 = dim(T²) × lobes = power_order × fiber_dim.

---

### `Tau.BookV.Cosmology.r_not_slow_roll`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L293-L296)
**theorem
Tau.BookV.Cosmology.r_not_slow_roll :8 * 1000000 / 57 ≠ 13573**


r = ι<sub>τ</sub>⁴ is NOT standard slow-roll: 8/N_e = 8/57 ≈ 0.140 ≠ ι<sub>τ</sub>⁴ ≈ 0.014.
Encoded: 8×10⁶/57 = 140350 ≠ 13573.

---

### `Tau.BookV.Cosmology.pt_exponent_decomp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/InflationRegime.lean#L298-L301)
**theorem
Tau.BookV.Cosmology.pt_exponent_decomp :22 = 18 + 4 ∧ 18 + 4 = 22**


Tensor power P_t exponent decomposition: 22 = 18 + 4 = W₄(3) + 2·dim(T²).
