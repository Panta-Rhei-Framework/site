---
layout: taulib-doc
title: "TauLib.BookIV.MassDerivation.HolonomyDetail"
permalink: /verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/
lane: verify
module_name: "TauLib.BookIV.MassDerivation.HolonomyDetail"
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

# TauLib.BookIV.MassDerivation.HolonomyDetail


Triple holonomy H₃ = ∮*{T_π}·∮*{T_γ}·∮_{T_η} and the π³α² correction,
connecting the breathing modes module to the holonomy correction module.

## Registry Cross-References


- [IV.D314] Triple Holonomy H₃ — `TripleHolonomyH3`

- [IV.T116] Holonomy Correction Range — `holonomy_in_range`

- [IV.D315] Holonomy Correction Data — `HolonomyCorrectionDetail`


## Mathematical Content


### Triple Holonomy


The fibered product τ³ = τ¹ ×_f T² contains three independent U(1) circles:


- **T_π**: the base circle in τ¹ (generator π, temporal)

- **T_γ**: the first fiber circle in T² (generator γ, EM sector)

- **T_η**: the second fiber circle in T² (generator η, Strong sector)


The triple holonomy is the product of Wilson loops around these circles:

```
H₃ = ∮_{T_π} · ∮_{T_γ} · ∮_{T_η}
```


Each loop contributes one factor of π (from ∮ dθ = 2π, normalized),
giving the prefactor π³ ≈ 31.006 in the holonomy correction.

### The Correction π³α²


The full holonomy correction to the mass ratio is π³α²·ι<sub>τ</sub>^(-2), where:


- π³ ≈ 31.006: from the three circles (triple holonomy)

- α² ≈ 5.3×10⁻⁵: from charge conjugation (kills first-order α)

- ι<sub>τ</sub>^(-2) ≈ 8.58: from the breathing operator scale


Combined: π³α²·ι<sub>τ</sub>^(-2) ≈ 0.014 (Level 1+ correction to R).

This module wraps the HolonomyCorrection module from Physics and
connects it to the breathing modes framework from BreathingModes.

## Scope


All claims: **tau-effective**.

## Ground Truth Sources


- holonomy_correction_sprint.md §3-§7

- electron_mass_first_principles.md §28, §37


---

### `Tau.BookIV.MassDerivation.TripleHolonomyH3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L62-L91)
**structure
Tau.BookIV.MassDerivation.TripleHolonomyH3 :Type**


[IV.D314] Triple holonomy H₃ = ∮*{T_π}·∮*{T_γ}·∮_{T_η}.

The product of Wilson loops around the three independent U(1)
circles in τ³ = τ¹ ×_f T². Each circle contributes one factor
of π, giving π³ as the holonomy prefactor.

Circle assignments:


- T_π: base τ¹ circle (generator π, Weak/temporal sector A)

- T_γ: first fiber circle (generator γ, EM sector B)

- T_η: second fiber circle (generator η, Strong sector C)


- circle_count : ℕ
Number of independent circles.

- three_circles : self.circle_count = 3
Circle count is 3.

- generators : List String
Generator labels for the three circles.

- gen_count : self.generators.length = self.circle_count
Generators list has correct length.

- pi_exponent : ℕ
π exponent matches circle count.

- exp_eq : self.pi_exponent = self.circle_count
Exponent = circle count.

- pi_cubed_n : ℕ
π³ rational approximation numerator.

- pi_cubed_d : ℕ
π³ rational approximation denominator.

- denom_pos : self.pi_cubed_d > 0
Denominator positive.

Instances For

---

### `Tau.BookIV.MassDerivation.instReprTripleHolonomyH3.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L91-L91)
**def
Tau.BookIV.MassDerivation.instReprTripleHolonomyH3.repr :TripleHolonomyH3 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instReprTripleHolonomyH3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L91-L91)
**instance
Tau.BookIV.MassDerivation.instReprTripleHolonomyH3 :Repr TripleHolonomyH3**

Equations
- Tau.BookIV.MassDerivation.instReprTripleHolonomyH3 = { reprPrec := Tau.BookIV.MassDerivation.instReprTripleHolonomyH3.repr }

---

### `Tau.BookIV.MassDerivation.triple_holonomy_H3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L93-L103)
**def
Tau.BookIV.MassDerivation.triple_holonomy_H3 :TripleHolonomyH3**


The canonical triple holonomy of τ³.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.holonomy_three_circles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L105-L107)
**theorem
Tau.BookIV.MassDerivation.holonomy_three_circles :triple_holonomy_H3.circle_count = 3**


Three circles in the holonomy.

---

### `Tau.BookIV.MassDerivation.holonomy_three_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L109-L111)
**theorem
Tau.BookIV.MassDerivation.holonomy_three_generators :triple_holonomy_H3.generators.length = 3**


Three generators listed.

---

### `Tau.BookIV.MassDerivation.holonomy_pi_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L113-L115)
**theorem
Tau.BookIV.MassDerivation.holonomy_pi_exponent :triple_holonomy_H3.pi_exponent = 3**


The π exponent is 3 (one per circle).

---

### `Tau.BookIV.MassDerivation.holonomy_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L121-L132)
**theorem
Tau.BookIV.MassDerivation.holonomy_in_range :Physics.holonomy_correction.numer * 1000 > Physics.holonomy_correction.denom ∧ Physics.holonomy_correction.numer * 1000 < 2 * Physics.holonomy_correction.denom**


[IV.T116] The holonomy correction π³α² is in (0.001, 0.002).

This wraps the range proofs from HolonomyCorrection:


- π³α² > 0.001 (correction_gt_1_per_mille)

- π³α² < 0.002 (correction_lt_2_per_mille)


Combined: π³α² ∈ (0.001, 0.002), confirming the
perturbative hierarchy (π³α² << √3 by a factor of ~1050).

---

### `Tau.BookIV.MassDerivation.holonomy_perturbative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L134-L138)
**theorem
Tau.BookIV.MassDerivation.holonomy_perturbative :Physics.pi_cubed_numer * Physics.alpha_sq_numer * 1000 * 10000000 < 17320508 * Physics.pi_cubed_denom * Physics.alpha_sq_denom**


The holonomy correction is perturbatively small relative to √3.

---

### `Tau.BookIV.MassDerivation.HolonomyCorrectionDetail`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L144-L170)
**structure
Tau.BookIV.MassDerivation.HolonomyCorrectionDetail :Type**


[IV.D315] Holonomy correction data: the three components that
make up the Level 1+ correction π³α²·ι<sub>τ</sub>^(-2).

- π³ from triple holonomy (31.006)

- α² from charge conjugation (5.3 × 10⁻⁵)

- ι<sub>τ</sub>^(-2) from breathing operator scale (8.58)


The combined correction π³α²·ι<sub>τ</sub>^(-2) ≈ 0.014 refines the mass
ratio from Level 0 (7.7 ppm) to Level 1+ (0.025 ppm).

- pi3_numer : ℕ
π³ numerator.

- pi3_denom : ℕ
π³ denominator.

- alpha2_numer : ℕ
α² numerator.

- alpha2_denom : ℕ
α² denominator.

- iota_neg2_n : ℕ
ι<sub>τ</sub>^(-2) numerator.

- iota_neg2_d : ℕ
ι<sub>τ</sub>^(-2) denominator.

- pi3_denom_pos : self.pi3_denom > 0
All denominators positive.

- alpha2_denom_pos : self.alpha2_denom > 0
- iota_neg2_denom_pos : self.iota_neg2_d > 0
Instances For

---

### `Tau.BookIV.MassDerivation.instReprHolonomyCorrectionDetail`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L170-L170)
**instance
Tau.BookIV.MassDerivation.instReprHolonomyCorrectionDetail :Repr HolonomyCorrectionDetail**

Equations
- Tau.BookIV.MassDerivation.instReprHolonomyCorrectionDetail = { reprPrec := Tau.BookIV.MassDerivation.instReprHolonomyCorrectionDetail.repr }

---

### `Tau.BookIV.MassDerivation.instReprHolonomyCorrectionDetail.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L170-L170)
**def
Tau.BookIV.MassDerivation.instReprHolonomyCorrectionDetail.repr :HolonomyCorrectionDetail → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.holonomy_detail`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L172-L182)
**def
Tau.BookIV.MassDerivation.holonomy_detail :HolonomyCorrectionDetail**


The canonical holonomy correction detail.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.pi3_matches`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L184-L188)
**theorem
Tau.BookIV.MassDerivation.pi3_matches :holonomy_detail.pi3_numer = Physics.pi_cubed_numer ∧ holonomy_detail.pi3_denom = Physics.pi_cubed_denom**


π³ component matches the holonomy correction module.

---

### `Tau.BookIV.MassDerivation.alpha2_matches`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L190-L194)
**theorem
Tau.BookIV.MassDerivation.alpha2_matches :holonomy_detail.alpha2_numer = Physics.alpha_sq_numer ∧ holonomy_detail.alpha2_denom = Physics.alpha_sq_denom**


α² component matches the holonomy correction module.

---

### `Tau.BookIV.MassDerivation.holonomy_correction_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L196-L201)
**def
Tau.BookIV.MassDerivation.holonomy_correction_float :Float**


The combined correction as Float (π³ × α² × ι<sub>τ</sub>^(-2)).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.breathing_epstein_shape_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L207-L212)
**theorem
Tau.BookIV.MassDerivation.breathing_epstein_shape_match :breathing_spectrum.shape_numer = epstein_on_T2.zeta.shape_numer ∧ breathing_spectrum.shape_denom = epstein_on_T2.zeta.shape_denom**


The breathing operator and Epstein zeta share the same shape parameter.

---

### `Tau.BookIV.MassDerivation.charge_conjugation_instance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L214-L215)
**def
Tau.BookIV.MassDerivation.charge_conjugation_instance :Physics.ChargConjugation**


Charge conjugation gives α² (second order), not α (first order).
Equations
- Tau.BookIV.MassDerivation.charge_conjugation_instance = { }
Instances For

---

### `Tau.BookIV.MassDerivation.charge_conjugation_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L217-L218)
**theorem
Tau.BookIV.MassDerivation.charge_conjugation_order :charge_conjugation_instance.surviving_order = 2**
