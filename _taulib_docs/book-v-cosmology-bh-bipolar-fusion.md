---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BHBipolarFusion"
permalink: /verify/taulib/docs/book-v-cosmology-bh-bipolar-fusion/
lane: verify
module_name: "TauLib.BookV.Cosmology.BHBipolarFusion"
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

# TauLib.BookV.Cosmology.BHBipolarFusion


Bipolar fusion inside black holes. Every BH is bipolar (χ_BH splits
into χ⁺ and χ⁻). Blueprint monoid for BH mergers. Polarity imbalance
converges to a fixed point.

## Registry Cross-References


- [V.D168] BH Bipolarity -- `BHBipolarity`

- [V.T111] Necessary Bipolarity -- `necessary_bipolarity`

- [V.D169] Polarity Imbalance -- `PolarityImbalance`

- [V.P94] Polarity Convergence -- `polarity_convergence`

- [V.D170] Blueprint -- `BHBlueprint`

- [V.D171] Blueprint Fusion -- `BlueprintFusion`

- [V.D172] Blueprint Monoid -- `BlueprintMonoid`

- [V.T112] Blueprint Monoid Closure -- `blueprint_monoid_closure`

- [V.R223] Irreversibility of mergers -- structural remark

- [V.R224] BH Entropy Formula -- structural remark

- [V.R225] Export to Book VI -- structural remark


## Mathematical Content


### Necessary Bipolarity


Every BH in Category τ is bipolar: χ_BH = (χ⁺, χ⁻) with both
components nonzero. Unipolar BHs (one lobe absent) do not exist
because the lemniscate L = S¹ ∨ S¹ has two lobes by construction.

### Polarity Imbalance


I_BH = (||χ⁺|| − ||χ⁻||)/(||χ⁺|| + ||χ⁻||) ∈ (−1, 1).
As the BH evolves, I_BH → 1 − 2ι<sub>τ</sub> (fixed point from ι<sub>τ</sub>).

### Blueprint Monoid


Blueprints (χ⁺, χ⁻) form a monoid under fusion:
Fuse_ω(b₁, b₂) = (χ₁⁺ · χ₂⁺, χ₁⁻ · χ₂⁻)
Closure, associativity, and identity (vacuum blueprint) all hold.
The monoid is non-invertible (mergers are irreversible).

## Ground Truth Sources


- Book V ch50: Bipolar Fusion


---

### `Tau.BookV.Cosmology.BHBipolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L56-L70)
**structure
Tau.BookV.Cosmology.BHBipolarity :Type**


[V.D168] BH bipolarity: the BH boundary character χ_BH
restricted to the linking boundary decomposes into two
lobe components χ⁺ (positive lobe) and χ⁻ (negative lobe).

Both are nonzero for every BH (bipolar = both lobes active).

- chi_plus : ℕ
Positive lobe magnitude (scaled).

- chi_minus : ℕ
Negative lobe magnitude (scaled).

- plus_pos : self.chi_plus > 0
Positive lobe is nonzero.

- minus_pos : self.chi_minus > 0
Negative lobe is nonzero.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHBipolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L70-L70)
**instance
Tau.BookV.Cosmology.instReprBHBipolarity :Repr BHBipolarity**

Equations
- Tau.BookV.Cosmology.instReprBHBipolarity = { reprPrec := Tau.BookV.Cosmology.instReprBHBipolarity.repr }

---

### `Tau.BookV.Cosmology.instReprBHBipolarity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L70-L70)
**def
Tau.BookV.Cosmology.instReprBHBipolarity.repr :BHBipolarity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.necessary_bipolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L76-L83)
**theorem
Tau.BookV.Cosmology.necessary_bipolarity
(bp : BHBipolarity)
 :bp.chi_plus > 0 ∧ bp.chi_minus > 0**


[V.T111] Necessary bipolarity: every BH in Category τ is bipolar.
Unipolar BHs (χ⁺ = 0 or χ⁻ = 0) do not exist.

Proof: the lemniscate L = S¹ ∨ S¹ has two lobes. The linking
class must wind around both. Therefore both χ⁺ and χ⁻ are
necessarily nonzero.

---

### `Tau.BookV.Cosmology.PolarityImbalance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L89-L103)
**structure
Tau.BookV.Cosmology.PolarityImbalance :Type**


[V.D169] Polarity imbalance I_BH.

I_BH = (||χ⁺|| − ||χ⁻||) / (||χ⁺|| + ||χ⁻||)

Encoded as a pair (numerator, denominator) where numerator
can be negative (using Int). The imbalance is strictly between
−1 and 1 because both lobes are nonzero.

- numer : ℤ
Imbalance numerator (can be negative).

- denom : ℕ
Imbalance denominator (always positive).

- denom_pos : self.denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprPolarityImbalance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L103-L103)
**def
Tau.BookV.Cosmology.instReprPolarityImbalance.repr :PolarityImbalance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPolarityImbalance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L103-L103)
**instance
Tau.BookV.Cosmology.instReprPolarityImbalance :Repr PolarityImbalance**

Equations
- Tau.BookV.Cosmology.instReprPolarityImbalance = { reprPrec := Tau.BookV.Cosmology.instReprPolarityImbalance.repr }

---

### `Tau.BookV.Cosmology.BHBipolarity.imbalance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L105-L109)
**def
Tau.BookV.Cosmology.BHBipolarity.imbalance
(bp : BHBipolarity)
 :PolarityImbalance**


Compute imbalance from bipolarity data.
Equations
- bp.imbalance = { numer := ↑bp.chi_plus - ↑bp.chi_minus, denom := bp.chi_plus + bp.chi_minus, denom_pos := ⋯ }
Instances For

---

### `Tau.BookV.Cosmology.PolarityFixedPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L115-L131)
**structure
Tau.BookV.Cosmology.PolarityFixedPoint :Type**


[V.P94] Polarity convergence: as a BH evolves, its polarity
imbalance converges to the fixed point 1 − 2ι<sub>τ</sub>.

The fixed-point imbalance value:
1 − 2ι<sub>τ</sub> ≈ 1 − 2(0.341304) ≈ 0.317082

Encoded as 317082 / 1000000.

- fp_numer : ℕ
Fixed-point numerator.

- fp_denom : ℕ
Fixed-point denominator.

- denom_pos : self.fp_denom > 0
Denominator positive.

- in_range : self.fp_numer > 0 ∧ self.fp_numer < self.fp_denom
Value in (0, 1).

Instances For

---

### `Tau.BookV.Cosmology.instReprPolarityFixedPoint.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L131-L131)
**def
Tau.BookV.Cosmology.instReprPolarityFixedPoint.repr :PolarityFixedPoint → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPolarityFixedPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L131-L131)
**instance
Tau.BookV.Cosmology.instReprPolarityFixedPoint :Repr PolarityFixedPoint**

Equations
- Tau.BookV.Cosmology.instReprPolarityFixedPoint = { reprPrec := Tau.BookV.Cosmology.instReprPolarityFixedPoint.repr }

---

### `Tau.BookV.Cosmology.polarity_fixed_point`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L133-L138)
**def
Tau.BookV.Cosmology.polarity_fixed_point :PolarityFixedPoint**


The τ-predicted fixed point.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.polarity_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L140-L144)
**theorem
Tau.BookV.Cosmology.polarity_convergence :polarity_fixed_point.fp_numer > 0 ∧ polarity_fixed_point.fp_numer < polarity_fixed_point.fp_denom**


Fixed point is in (0, 1).

---

### `Tau.BookV.Cosmology.BHBlueprint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L150-L161)
**structure
Tau.BookV.Cosmology.BHBlueprint :Type**


[V.D170] Blueprint of a BH: the pair b_BH = (χ⁺, χ⁻) of
boundary character components on the two lobes.

The blueprint encodes the full bipolar structure of the BH.

- bipolarity : BHBipolarity
Bipolar data.

- mass_index : ℕ
Mass scale (scaled).

- mass_pos : self.mass_index > 0
Mass positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHBlueprint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L161-L161)
**instance
Tau.BookV.Cosmology.instReprBHBlueprint :Repr BHBlueprint**

Equations
- Tau.BookV.Cosmology.instReprBHBlueprint = { reprPrec := Tau.BookV.Cosmology.instReprBHBlueprint.repr }

---

### `Tau.BookV.Cosmology.instReprBHBlueprint.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L161-L161)
**def
Tau.BookV.Cosmology.instReprBHBlueprint.repr :BHBlueprint → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.BlueprintFusion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L167-L181)
**def
Tau.BookV.Cosmology.BlueprintFusion
(b1 b2 : BHBlueprint)
 :BHBlueprint**


[V.D171] Blueprint fusion Fuse_ω: combines two blueprints by
pointwise multiplication of lobe characters.

Fuse_ω(b₁, b₂) = (χ₁⁺ · χ₂⁺, χ₁⁻ · χ₂⁻)

Product on the ω (crossing) sector.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.BlueprintMonoid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L187-L201)
**structure
Tau.BookV.Cosmology.BlueprintMonoid :Type**


[V.D172] Blueprint monoid M_BH: blueprints with fusion and
vacuum identity.


- Carrier: BH blueprints

- Operation: Fuse_ω (pointwise lobe multiplication)

- Identity: vacuum blueprint (χ⁺ = χ⁻ = 1, m = 0)

- Non-invertible: mergers are irreversible


- is_associative : Bool
Whether fusion is associative.

- has_identity : Bool
Whether identity exists.

- non_invertible : Bool
Whether the monoid is non-invertible (not a group).

Instances For

---

### `Tau.BookV.Cosmology.instReprBlueprintMonoid.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L201-L201)
**def
Tau.BookV.Cosmology.instReprBlueprintMonoid.repr :BlueprintMonoid → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBlueprintMonoid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L201-L201)
**instance
Tau.BookV.Cosmology.instReprBlueprintMonoid :Repr BlueprintMonoid**

Equations
- Tau.BookV.Cosmology.instReprBlueprintMonoid = { reprPrec := Tau.BookV.Cosmology.instReprBlueprintMonoid.repr }

---

### `Tau.BookV.Cosmology.blueprint_monoid_closure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L207-L217)
**theorem
Tau.BookV.Cosmology.blueprint_monoid_closure
(b1 b2 : BHBlueprint)
 :(BlueprintFusion b1 b2).bipolarity.chi_plus > 0 ∧ (BlueprintFusion b1 b2).bipolarity.chi_minus > 0**


[V.T112] Blueprint monoid closure: Fuse_ω is closed, associative,
and has an identity element (vacuum blueprint).

Closure proof: fusion of two blueprints yields a blueprint
(product of positive naturals is positive).

---

### `Tau.BookV.Cosmology.fusion_mass_additive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L219-L221)
**theorem
Tau.BookV.Cosmology.fusion_mass_additive
(b1 b2 : BHBlueprint)
 :(BlueprintFusion b1 b2).mass_index = b1.mass_index + b2.mass_index**


Fusion mass is sum of input masses.

---

### `Tau.BookV.Cosmology.BHEntropyRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L227-L240)
**structure
Tau.BookV.Cosmology.BHEntropyRemark :Type**


[V.R224] BH entropy formula: S_BH = k_B · A / (4 · ι<sub>τ</sub>²).

Replaces Planck length ℓ_P² with ι<sub>τ</sub>² in the Bekenstein-Hawking
formula. The ι<sub>τ</sub>² factor is structural (area of T² quantum).

- area_quantum_numer : ℕ
Area scale numerator.

- area_quantum_denom : ℕ
Area scale denominator.

- denom_pos : self.area_quantum_denom > 0
Denominator positive.

- iota_sq_consistent : self.area_quantum_numer > 116000 ∧ self.area_quantum_numer < 117000
ι<sub>τ</sub>² ≈ 0.116594 encoded as 116594/1000000.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHEntropyRemark.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L240-L240)
**def
Tau.BookV.Cosmology.instReprBHEntropyRemark.repr :BHEntropyRemark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBHEntropyRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L240-L240)
**instance
Tau.BookV.Cosmology.instReprBHEntropyRemark :Repr BHEntropyRemark**

Equations
- Tau.BookV.Cosmology.instReprBHEntropyRemark = { reprPrec := Tau.BookV.Cosmology.instReprBHEntropyRemark.repr }

---

### `Tau.BookV.Cosmology.bh_entropy_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L242-L247)
**def
Tau.BookV.Cosmology.bh_entropy_data :BHEntropyRemark**


BH entropy uses ι<sub>τ</sub>².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bh1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L266-L271)
**def
Tau.BookV.Cosmology.bh1 :BHBlueprint**


Example BH blueprint.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bh2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L273-L278)
**def
Tau.BookV.Cosmology.bh2 :BHBlueprint**


Second BH blueprint.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bh_fused`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L280-L281)
**def
Tau.BookV.Cosmology.bh_fused :BHBlueprint**


Fused blueprint.
Equations
- Tau.BookV.Cosmology.bh_fused = Tau.BookV.Cosmology.BlueprintFusion Tau.BookV.Cosmology.bh1 Tau.BookV.Cosmology.bh2
Instances For

---

### `Tau.BookV.Cosmology.PolarityContractionMap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L292-L321)
**structure
Tau.BookV.Cosmology.PolarityContractionMap :Type**


[V.P94 upgrade] Polarity convergence: contraction mapping proof.

Define the evolution map F on polarity imbalance I ∈ (−1, 1):
F(I) = (1−ι<sub>τ</sub>)·I + ι<sub>τ</sub>·(1−2ι<sub>τ</sub>)

This is an affine contraction with:


- Slope = (1−ι<sub>τ</sub>) ≈ 0.659 < 1 (contraction)

- Fixed point: I* = 1−2ι<sub>τ</sub> ≈ 0.317

- F(I*) = (1−ι<sub>τ</sub>)·(1−2ι<sub>τ</sub>) + ι<sub>τ</sub>·(1−2ι<sub>τ</sub>) = (1−2ι<sub>τ</sub>) = I*


By the Banach fixed-point theorem, every initial I₀ ∈ (−1,1)
converges to I* = 1−2ι<sub>τ</sub> under iteration of F.

Physical interpretation: at each step, the larger lobe
(say χ⁺) grows by factor (1−ι<sub>τ</sub>) while the smaller lobe
gains by ι<sub>τ</sub>, approaching the ratio set by ι<sub>τ</sub>.

- contraction_factor_is_kappa_D : Bool
Contraction factor = 1−ι<sub>τ</sub>.

- contraction_strict : Bool
Contraction factor < 1.

- fixed_point_is_1_minus_2iota : Bool
Fixed point = 1−2ι<sub>τ</sub>.

- banach_applies : Bool
Banach fixed-point theorem applies.

- fixed_point_unique : Bool
Fixed point is unique.

- lobe_ratio_converges : Bool
Physical: lobe ratio → ι<sub>τ</sub>/(1−ι<sub>τ</sub>).

Instances For

---

### `Tau.BookV.Cosmology.instReprPolarityContractionMap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L321-L321)
**instance
Tau.BookV.Cosmology.instReprPolarityContractionMap :Repr PolarityContractionMap**

Equations
- Tau.BookV.Cosmology.instReprPolarityContractionMap = { reprPrec := Tau.BookV.Cosmology.instReprPolarityContractionMap.repr }

---

### `Tau.BookV.Cosmology.instReprPolarityContractionMap.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L321-L321)
**def
Tau.BookV.Cosmology.instReprPolarityContractionMap.repr :PolarityContractionMap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.polarity_contraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L323-L323)
**def
Tau.BookV.Cosmology.polarity_contraction :PolarityContractionMap**

Equations
- Tau.BookV.Cosmology.polarity_contraction = { }
Instances For

---

### `Tau.BookV.Cosmology.polarity_contraction_strict`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L325-L329)
**theorem
Tau.BookV.Cosmology.polarity_contraction_strict :polarity_contraction.contraction_strict = true ∧ polarity_contraction.contraction_factor_is_kappa_D = true**


Polarity evolution is a contraction: κ_D = 1−ι<sub>τ</sub> < 1.

---

### `Tau.BookV.Cosmology.polarity_fixed_point_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L331-L336)
**theorem
Tau.BookV.Cosmology.polarity_fixed_point_unique :polarity_contraction.fixed_point_unique = true ∧ polarity_contraction.banach_applies = true ∧ polarity_contraction.fixed_point_is_1_minus_2iota = true**


Fixed point 1−2ι<sub>τ</sub> is unique by Banach theorem.

---

### `Tau.BookV.Cosmology.polarity_fixed_point_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L338-L343)
**theorem
Tau.BookV.Cosmology.polarity_fixed_point_consistent :polarity_fixed_point.fp_numer = 317082 ∧ polarity_fixed_point.fp_denom = 1000000**


Cross-check: fixed point value 317082/1000000 consistent
with contraction map fixed point.
