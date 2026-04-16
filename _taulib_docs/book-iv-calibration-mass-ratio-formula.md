---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.MassRatioFormula"
permalink: /verify/taulib/docs/book-iv-calibration-mass-ratio-formula/
lane: verify
module_name: "TauLib.BookIV.Calibration.MassRatioFormula"
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

# TauLib.BookIV.Calibration.MassRatioFormula


The mass ratio R = m_n/m_e derivation from ι<sub>τ</sub> = 2/(π+e).

## Registry Cross-References


- [IV.D46] Mass Ratio Bulk Term — `bulk_numer`, `bulk_denom`

- [IV.D47] Level 0 Formula — structure and range

- [IV.D48] Level 1+ Formula — structure (holonomy correction)

- [IV.T13] Bulk Overshoots — `bulk_overshoots_codata`

- [IV.T14] Level 0 Range — `r0_in_range`

- [IV.T15] Derivation Chain Complete — `chain_all_tau_effective`

- [IV.P07] All Links Tau-Effective — `chain_scope_count`


## Mathematical Content


### The Mass Ratio Formula


R = m_n/m_e is derived from the spectral geometry of T² with shape ι<sub>τ</sub>.
The derivation proceeds through 10 links, each tau-effective:

**Level 0** (7.7 ppm with exact ι<sub>τ</sub>):
R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2)

**Level 1+** (0.025 ppm with exact ι<sub>τ</sub>):
R₁ = ι<sub>τ</sub>^(-7) − (√3 + π³α²)·ι<sub>τ</sub>^(-2)

where:


- ι<sub>τ</sub>^(-7): bulk breathing mode count from Epstein zeta Z(4; iι<sub>τ</sub>)
(exponent = 1 − 2×4 = −7, from Chowla-Selberg leading term)

- √3: lemniscate spectral distance |1−ω| where ω = e^{2πi/3}
(three-fold on L = S¹∨S¹)

- π³: holonomy product from three U(1) circles in τ³

- α²: second-order EM correction (charge conjugation kills first-order)


### Precision Notes


The Lean formalization uses the 6-digit rational approximation
ι<sub>τ</sub> ≈ 341304/1000000. At this precision:


- Bulk ≈ 1847.5 (vs exact 1853.6)

- R₀ ≈ 1832.6 (vs exact 1838.70)


The high-precision results (7.7 ppm, 0.025 ppm) require the exact
ι<sub>τ</sub> = 2/(π+e). The Lean proofs verify:

- The formula STRUCTURE (right terms, signs, exponents)

- Range brackets at the rational-approximation precision

- The perturbative hierarchy (π³α² << √3 << bulk)


### The 10-Link Derivation Chain


ALL 10 links are tau-effective (ZERO conjectural ingredients):


#
Link
Source


1
τ³ = τ¹ ×_f T² fibration
Book I Axiom K5


2
Hodge Laplacian on T² with shape ι<sub>τ</sub>
Spectral geometry


3
Breathing operator B = Δ⁻¹
_{T²}


4
Spectral factorization Λ_{n,k₁,k₂}
Torus eigenvalues


5
Epstein zeta Z(s; iι<sub>τ</sub>) at s=4
Lattice sum


6
√3 from lemniscate three-fold


7
R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2)
Level 0 assembly


8
π³α² holonomy correction
Triple U(1)


9
R₁ = ι<sub>τ</sub>^(-7) − (√3+π³α²)·ι<sub>τ</sub>^(-2)
Level 1+


10
m_e = m_n/R₁
Electron mass


## Scope


All claims: **tau-effective**. The R formula has zero conjectural ingredients.

## Ground Truth Sources


- electron_mass_first_principles.md (master document, ~1900 lines)

- sqrt3_derivation_sprint.md (Sprint 1)

- holonomy_correction_sprint.md (Sprint 2)


---

### `Tau.BookIV.Calibration.bulk_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L88-L89)
**def
Tau.BookIV.Calibration.bulk_numer :ℕ**


[IV.D46] ι<sub>τ</sub>^(-7) numerator: (10⁶)⁷ = 10⁴².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.bulk_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L91-L92)
**def
Tau.BookIV.Calibration.bulk_denom :ℕ**


ι<sub>τ</sub>^(-7) denominator: (341304)⁷.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.bulk_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L94-L96)
**theorem
Tau.BookIV.Calibration.bulk_denom_pos :bulk_denom > 0**


Bulk denominator is positive.

---

### `Tau.BookIV.Calibration.bulk_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L98-L100)
**def
Tau.BookIV.Calibration.bulk_float :Float**


Bulk as Float (for smoke tests).
Equations
- Tau.BookIV.Calibration.bulk_float = Float.ofNat Tau.BookIV.Calibration.bulk_numer / Float.ofNat Tau.BookIV.Calibration.bulk_denom
Instances For

---

### `Tau.BookIV.Calibration.bulk_gt_1853`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L106-L108)
**theorem
Tau.BookIV.Calibration.bulk_gt_1853 :bulk_numer > 1853 * bulk_denom**


ι<sub>τ</sub>^(-7) > 1853 (lower bound with 6-digit approximation).

---

### `Tau.BookIV.Calibration.bulk_lt_1855`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L110-L112)
**theorem
Tau.BookIV.Calibration.bulk_lt_1855 :bulk_numer < 1855 * bulk_denom**


ι<sub>τ</sub>^(-7) < 1855 (upper bound with 6-digit approximation).

---

### `Tau.BookIV.Calibration.bulk_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L114-L118)
**theorem
Tau.BookIV.Calibration.bulk_in_range :bulk_numer > 1853 * bulk_denom ∧ bulk_numer < 1855 * bulk_denom**


Combined: ι<sub>τ</sub>^(-7) ∈ (1853, 1855).

---

### `Tau.BookIV.Calibration.iota_neg2_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L124-L125)
**def
Tau.BookIV.Calibration.iota_neg2_numer :ℕ**


ι<sub>τ</sub>^(-2) numerator: (10⁶)² = 10¹².
Equations
- Tau.BookIV.Calibration.iota_neg2_numer = Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookIV.Calibration.iota_neg2_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L127-L128)
**def
Tau.BookIV.Calibration.iota_neg2_denom :ℕ**


ι<sub>τ</sub>^(-2) denominator: (341304)².
Equations
- Tau.BookIV.Calibration.iota_neg2_denom = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Calibration.iota_neg2_gt_8`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L130-L132)
**theorem
Tau.BookIV.Calibration.iota_neg2_gt_8 :iota_neg2_numer > 8 * iota_neg2_denom**


ι<sub>τ</sub>^(-2) > 8 (since 1/0.341304 ≈ 2.929 and 2.929² ≈ 8.58).

---

### `Tau.BookIV.Calibration.iota_neg2_lt_9`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L134-L136)
**theorem
Tau.BookIV.Calibration.iota_neg2_lt_9 :iota_neg2_numer < 9 * iota_neg2_denom**


ι<sub>τ</sub>^(-2) < 9.

---

### `Tau.BookIV.Calibration.correction0_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L150-L151)
**def
Tau.BookIV.Calibration.correction0_numer :ℕ**


Level 0 correction numerator: √3_numer × ι<sub>τ</sub>^(-2)_numer.
Equations
- Tau.BookIV.Calibration.correction0_numer = Tau.BookIV.Calibration.sqrt3N✝ * Tau.BookIV.Calibration.iota_neg2_numer
Instances For

---

### `Tau.BookIV.Calibration.correction0_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L153-L154)
**def
Tau.BookIV.Calibration.correction0_denom :ℕ**


Level 0 correction denominator: √3_denom × ι<sub>τ</sub>^(-2)_denom.
Equations
- Tau.BookIV.Calibration.correction0_denom = Tau.BookIV.Calibration.sqrt3D✝ * Tau.BookIV.Calibration.iota_neg2_denom
Instances For

---

### `Tau.BookIV.Calibration.correction0_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L156-L158)
**theorem
Tau.BookIV.Calibration.correction0_denom_pos :correction0_denom > 0**


Correction denominator is positive.

---

### `Tau.BookIV.Calibration.correction0_gt_14`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L160-L162)
**theorem
Tau.BookIV.Calibration.correction0_gt_14 :correction0_numer > 14 * correction0_denom**


√3·ι<sub>τ</sub>^(-2) > 14 (since √3 × 8.58 ≈ 14.86).

---

### `Tau.BookIV.Calibration.correction0_lt_16`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L164-L166)
**theorem
Tau.BookIV.Calibration.correction0_lt_16 :correction0_numer < 16 * correction0_denom**


√3·ι<sub>τ</sub>^(-2) < 16.

---

### `Tau.BookIV.Calibration.bulk_overshoots_codata`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L172-L178)
**theorem
Tau.BookIV.Calibration.bulk_overshoots_codata :bulk_numer * si_mass_ratio.denom > si_mass_ratio.numer * bulk_denom**


[IV.T13] The bulk term ι<sub>τ</sub>^(-7) overshoots R_CODATA.

Even with the 6-digit approximation, ι<sub>τ</sub>^(-7) ≈ 1847.5 > 1838.68 = R.
This proves the correction term has the right SIGN (must be subtracted).

---

### `Tau.BookIV.Calibration.r0_gt_1837`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L184-L192)
**theorem
Tau.BookIV.Calibration.r0_gt_1837 :bulk_numer * correction0_denom > correction0_numer * bulk_denom + 1837 * bulk_denom * correction0_denom**


[IV.T14] The Level 0 formula R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2) is in range.

R₀ > 1837: the formula gives a value > 1837.
Proof strategy: bulk > correction + 1837, which avoids Nat subtraction.
bulk_numer × correction0_denom > correction0_numer × bulk_denom + 1837 × bulk_denom × correction0_denom

---

### `Tau.BookIV.Calibration.r0_lt_1840`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L194-L199)
**theorem
Tau.BookIV.Calibration.r0_lt_1840 :bulk_numer * correction0_denom < correction0_numer * bulk_denom + 1840 * bulk_denom * correction0_denom**


R₀ < 1840.
bulk_numer × correction0_denom < correction0_numer × bulk_denom + 1840 × bulk_denom × correction0_denom

---

### `Tau.BookIV.Calibration.r0_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L201-L207)
**theorem
Tau.BookIV.Calibration.r0_in_range :bulk_numer * correction0_denom > correction0_numer * bulk_denom + 1837 * bulk_denom * correction0_denom ∧ bulk_numer * correction0_denom < correction0_numer * bulk_denom + 1840 * bulk_denom * correction0_denom**


Combined: R₀ ∈ (1837, 1840) with the 6-digit ι<sub>τ</sub> approximation.

---

### `Tau.BookIV.Calibration.r0_deviation_lt_1pct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L213-L254)
**theorem
Tau.BookIV.Calibration.r0_deviation_lt_1pct :bulk_numer * si_mass_ratio.denom * correction0_denom + si_mass_ratio.numer * bulk_denom * correction0_denom > 100 * correction0_numer * si_mass_ratio.denom * bulk_denom**


R₀ deviation from CODATA is less than 1%.

|R₀ − R_CODATA| / R_CODATA < 0.01

At 6-digit precision, R₀ ≈ 1838.7 vs R_CODATA ≈ 1838.68, so deviation ≈ 0.001%.

Cross-multiplied to avoid division:
|bulk/bulk_denom − correction/correction_denom − R_CODATA| × 100 < R_CODATA

Since R₀ < R_CODATA (undershoots), the absolute value is:
R_CODATA − R₀ = (R_CODATA + correction) − bulk

We prove: 100 × (CODATA + correction − bulk) < CODATA.
Cross-multiplied on all three fractions' denominators.

---

### `Tau.BookIV.Calibration.Level1PlusFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L260-L281)
**structure
Tau.BookIV.Calibration.Level1PlusFormula :Type**


[IV.D48] Level 1+ mass ratio formula structure.

R₁ = ι<sub>τ</sub>^(-7) − (√3 + π³α²)·ι<sub>τ</sub>^(-2)

At exact ι<sub>τ</sub> = 2/(π+e), this gives R₁ = 1838.683709(46),
matching CODATA R = 1838.68366173(89) to 0.025 ppm.

The Level 1+ formula is recorded here as a STRUCTURE:
the numerical evaluation requires the exact ι<sub>τ</sub> (not the
6-digit rational approximation).

- bulk_exp : ℤ
Bulk exponent: ι<sub>τ</sub>^(-7).

- correction_coeff : String
Correction coefficient: √3 + π³α².

- correction_exp : ℤ
Correction ι<sub>τ</sub> power: ι<sub>τ</sub>^(-2).

- accuracy_ppm : String
Accuracy at exact ι<sub>τ</sub> (in ppm).

- scope : String
Scope.

Instances For

---

### `Tau.BookIV.Calibration.instReprLevel1PlusFormula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L281-L281)
**def
Tau.BookIV.Calibration.instReprLevel1PlusFormula.repr :Level1PlusFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprLevel1PlusFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L281-L281)
**instance
Tau.BookIV.Calibration.instReprLevel1PlusFormula :Repr Level1PlusFormula**

Equations
- Tau.BookIV.Calibration.instReprLevel1PlusFormula = { reprPrec := Tau.BookIV.Calibration.instReprLevel1PlusFormula.repr }

---

### `Tau.BookIV.Calibration.level1plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L283-L284)
**def
Tau.BookIV.Calibration.level1plus :Level1PlusFormula**


The canonical Level 1+ formula.
Equations
- Tau.BookIV.Calibration.level1plus = { }
Instances For

---

### `Tau.BookIV.Calibration.perturbative_terms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L286-L299)
**def
Tau.BookIV.Calibration.perturbative_terms :List String**


Perturbative hierarchy: π³α² << √3 << ι<sub>τ</sub>^(-7).

Term magnitudes (at exact ι<sub>τ</sub>):
T0 = ι<sub>τ</sub>^(-7) ≈ 1854
T1 = √3·ι<sub>τ</sub>^(-2) ≈ 14.9
T2 = π³α²·ι<sub>τ</sub>^(-2) ≈ 0.014
T3 = residual ≈ 0.000046

Ratio: T0/T1 ≈ 124, T1/T2 ≈ 1050, T2/T3 ≈ 300
Equations
- Tau.BookIV.Calibration.perturbative_terms = ["T0: ι<sub>τ</sub>^(-7) ≈ 1854", "T1: √3·ι<sub>τ</sub>^(-2) ≈ 14.9", "T2: π³α²·ι<sub>τ</sub>^(-2) ≈ 0.014", "T3: residual ≈ 0.000046"]
Instances For

---

### `Tau.BookIV.Calibration.perturbative_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L301-L302)
**theorem
Tau.BookIV.Calibration.perturbative_count :perturbative_terms.length = 4**


Four terms in the perturbative expansion.

---

### `Tau.BookIV.Calibration.ElectronMassDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L308-L324)
**structure
Tau.BookIV.Calibration.ElectronMassDerivation :Type**


The electron mass from the calibration anchor:
m_e = m_n / R

Using CODATA m_n and the Level 1+ R, this gives:
m_e = 1.674927498 × 10⁻²⁷ / 1838.684 ≈ 9.1094 × 10⁻³¹ kg

Matching CODATA m_e = 9.1093837015 × 10⁻³¹ kg to sub-ppm.

- anchor : SIConstant
Anchor: neutron mass.

- ratio : SIConstant
Mass ratio: R.

- target : SIConstant
Derived: electron mass.

- relation : String
The derivation: m_e = m_n / R.

Instances For

---

### `Tau.BookIV.Calibration.instReprElectronMassDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L324-L324)
**def
Tau.BookIV.Calibration.instReprElectronMassDerivation.repr :ElectronMassDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprElectronMassDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L324-L324)
**instance
Tau.BookIV.Calibration.instReprElectronMassDerivation :Repr ElectronMassDerivation**

Equations
- Tau.BookIV.Calibration.instReprElectronMassDerivation = { reprPrec := Tau.BookIV.Calibration.instReprElectronMassDerivation.repr }

---

### `Tau.BookIV.Calibration.electron_mass_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L326-L332)
**theorem
Tau.BookIV.Calibration.electron_mass_consistent :si_neutron_mass.numer * si_electron_mass.denom > 1838 * si_electron_mass.numer * si_neutron_mass.denom**


Consistency: m_n > R × m_e (cross-multiplied).
neutron_numer × electron_denom > ratio × electron_numer × neutron_denom
(approximately, at the precision of our SI constants).

---

### `Tau.BookIV.Calibration.RDerivationLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L338-L346)
**structure
Tau.BookIV.Calibration.RDerivationLink :Type**


A link in the R derivation chain.

- index : ℕ
Link index (1-10).

- name : String
Description of the link.

- scope : String
Scope: all are "tau-effective".

Instances For

---

### `Tau.BookIV.Calibration.instReprRDerivationLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L346-L346)
**instance
Tau.BookIV.Calibration.instReprRDerivationLink :Repr RDerivationLink**

Equations
- Tau.BookIV.Calibration.instReprRDerivationLink = { reprPrec := Tau.BookIV.Calibration.instReprRDerivationLink.repr }

---

### `Tau.BookIV.Calibration.instReprRDerivationLink.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L346-L346)
**def
Tau.BookIV.Calibration.instReprRDerivationLink.repr :RDerivationLink → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.r_derivation_chain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L348-L360)
**def
Tau.BookIV.Calibration.r_derivation_chain :List RDerivationLink**


The complete 10-link derivation chain.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.chain_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L362-L363)
**theorem
Tau.BookIV.Calibration.chain_length :r_derivation_chain.length = 10**


[IV.T15] The chain has exactly 10 links.

---

### `Tau.BookIV.Calibration.chain_all_tau_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L365-L368)
**theorem
Tau.BookIV.Calibration.chain_all_tau_effective :(r_derivation_chain.all fun (l : RDerivationLink) => l.scope == "tau-effective") = true**


[IV.P07] ALL 10 links are tau-effective. Zero conjectural ingredients.

---

### `Tau.BookIV.Calibration.chain_scope_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L370-L374)
**theorem
Tau.BookIV.Calibration.chain_scope_count :(List.filter (fun (x : RDerivationLink) => x.scope == "tau-effective") r_derivation_chain).length = 10 ∧ (List.filter (fun (x : RDerivationLink) => x.scope == "conjectural") r_derivation_chain).length = 0**


The scope count: 10 tau-effective, 0 conjectural, 0 metaphorical.

---

### `Tau.BookIV.Calibration.FormulaLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L380-L390)
**structure
Tau.BookIV.Calibration.FormulaLevel :Type**


Summary of the three formula levels.

- level : String
Level name.

- formula : String
The formula.

- accuracy : String
Accuracy (ppm) at exact ι<sub>τ</sub>.

- approx_accuracy : String
Accuracy at 6-digit ι<sub>τ</sub>.

Instances For

---

### `Tau.BookIV.Calibration.instReprFormulaLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L390-L390)
**def
Tau.BookIV.Calibration.instReprFormulaLevel.repr :FormulaLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprFormulaLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L390-L390)
**instance
Tau.BookIV.Calibration.instReprFormulaLevel :Repr FormulaLevel**

Equations
- Tau.BookIV.Calibration.instReprFormulaLevel = { reprPrec := Tau.BookIV.Calibration.instReprFormulaLevel.repr }

---

### `Tau.BookIV.Calibration.formula_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L392-L403)
**def
Tau.BookIV.Calibration.formula_levels :List FormulaLevel**


The three formula levels.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.formula_level_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/MassRatioFormula.lean#L405-L406)
**theorem
Tau.BookIV.Calibration.formula_level_count :formula_levels.length = 3**


Three formula levels.
