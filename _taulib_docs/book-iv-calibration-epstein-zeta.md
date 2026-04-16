---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.EpsteinZeta"
permalink: /verify/taulib/docs/book-iv-calibration-epstein-zeta/
lane: verify
module_name: "TauLib.BookIV.Calibration.EpsteinZeta"
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

# TauLib.BookIV.Calibration.EpsteinZeta


The Epstein zeta function Z(s; iι<sub>τ</sub>) on the torus T² with shape parameter ι<sub>τ</sub>.

## Registry Cross-References


- [IV.D40] Epstein Zeta Structure — `EpsteinZetaStructure`, `epstein_at_T2`

- [IV.D41] Chowla-Selberg Decomposition — `ChowlaSelbergTerms`

- [IV.T10] Leading Exponent — `leading_exponent_is_neg7`

- [IV.R10] Normalization — structural remark on Z(4)/R


## Mathematical Content


### The Epstein Zeta Function on T²


The Epstein zeta function for a rectangular lattice with shape parameter τ is:

```
Z(s; iτ) = Σ'_{(m,n) ∈ ℤ²} (m² + τ²n²)^{-s}
```


where the prime denotes omission of (m,n) = (0,0).

For our torus T² with shape ι<sub>τ</sub> = 2/(π+e):

```
Z(s; iι<sub>τ</sub>) = Σ'_{(m,n)} (m² + ι<sub>τ</sub>²n²)^{-s}
```


### Chowla-Selberg Formula at s = 4


Z(4; iι<sub>τ</sub>) = 2ζ(8) + C(4)·ι<sub>τ</sub>^(-7) + Bessel_sum

where:


- 2ζ(8) = 2π⁸/9450 ≈ 0.002079 (negligible)

- C(4) = (5π/8)·ζ(7) ≈ 1.985 (the leading coefficient)

- Leading term: C(4)·ι<sub>τ</sub>^(-7) ≈ 1985 × (1/ι<sub>τ</sub>)^7 dominates

- Bessel sum: exponentially suppressed corrections


### The Exponent -7


At s = 4, the Chowla-Selberg leading term has exponent 1 - 2s = 1 - 8 = -7.
This is why ι<sub>τ</sub>^(-7) appears as the bulk term in the mass ratio formula.

### Numerical Result (from holonomy_correction_lab.py)


Z(4; iι<sub>τ</sub>) ≈ 10911.756 (lattice sum, N_max = 300)
N = Z(4)/R ≈ 5.935 (normalization factor, NOT algebraic)

## Scope


All claims in this module are **tau-effective**: they follow from the
τ-framework's identification of the torus T² with shape ι<sub>τ</sub>.

## Ground Truth Sources


- electron_mass_first_principles.md §25-§26

- holonomy_correction_sprint.md §8-§11

- mass_decomposition_sprint.md §27, §36


---

### `Tau.BookIV.Calibration.EpsteinZetaStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L68-L85)
**structure
Tau.BookIV.Calibration.EpsteinZetaStructure :Type**


[IV.D40] The Epstein zeta function on a rectangular lattice.

Z(s; iτ) = Σ'_{(m,n) ∈ ℤ²} (m² + τ²n²)^{-s}

The lattice is determined by the shape parameter τ (aspect ratio).
For the τ-framework torus, τ = ι<sub>τ</sub> = 2/(π+e).

- shape_numer : ℕ
Shape parameter numerator (rational approximation).

- shape_denom : ℕ
Shape parameter denominator.

- denom_pos : self.shape_denom > 0
Denominator positive.

- eval_point : ℕ
Critical exponent s at which Z is evaluated.

- scope : String
Scope label.

Instances For

---

### `Tau.BookIV.Calibration.instReprEpsteinZetaStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L85-L85)
**instance
Tau.BookIV.Calibration.instReprEpsteinZetaStructure :Repr EpsteinZetaStructure**

Equations
- Tau.BookIV.Calibration.instReprEpsteinZetaStructure = { reprPrec := Tau.BookIV.Calibration.instReprEpsteinZetaStructure.repr }

---

### `Tau.BookIV.Calibration.instReprEpsteinZetaStructure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L85-L85)
**def
Tau.BookIV.Calibration.instReprEpsteinZetaStructure.repr :EpsteinZetaStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.epstein_at_T2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L87-L92)
**def
Tau.BookIV.Calibration.epstein_at_T2 :EpsteinZetaStructure**


The Epstein zeta function for T² with shape ι<sub>τ</sub> at s = 4.
Equations
- Tau.BookIV.Calibration.epstein_at_T2 = { shape_numer := Tau.Boundary.iota_tau_numer, shape_denom := Tau.Boundary.iota_tau_denom,
 denom_pos := Tau.Boundary.iota_tau_denom_pos, eval_point := 4 }
Instances For

---

### `Tau.BookIV.Calibration.ChowlaSelbergTerms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L98-L114)
**structure
Tau.BookIV.Calibration.ChowlaSelbergTerms :Type**


[IV.D41] The three terms of the Chowla-Selberg decomposition.

Z(s; iι<sub>τ</sub>) = Term1 + Term2 + Term3

Term1 = 2ζ(2s) (constant, negligible at large s)
Term2 = C(s)·ι<sub>τ</sub>^(1-2s) (leading power-law term)
Term3 = Bessel_sum (exponentially suppressed)

- s : ℕ
Evaluation point s.

- leading_exp : ℤ
Leading exponent: 1 - 2s.

- exp_formula : self.leading_exp = 1 - 2 * ↑self.s
Leading exponent equals 1 - 2s.

- constant_negligible : self.s ≥ 2
The constant term 2ζ(2s) is negligible for s ≥ 2.

Instances For

---

### `Tau.BookIV.Calibration.instReprChowlaSelbergTerms.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L114-L114)
**def
Tau.BookIV.Calibration.instReprChowlaSelbergTerms.repr :ChowlaSelbergTerms → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprChowlaSelbergTerms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L114-L114)
**instance
Tau.BookIV.Calibration.instReprChowlaSelbergTerms :Repr ChowlaSelbergTerms**

Equations
- Tau.BookIV.Calibration.instReprChowlaSelbergTerms = { reprPrec := Tau.BookIV.Calibration.instReprChowlaSelbergTerms.repr }

---

### `Tau.BookIV.Calibration.chowla_selberg_s4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L116-L121)
**def
Tau.BookIV.Calibration.chowla_selberg_s4 :ChowlaSelbergTerms**


Chowla-Selberg at s = 4: leading exponent = -7.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.leading_exponent_is_neg7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L127-L133)
**theorem
Tau.BookIV.Calibration.leading_exponent_is_neg7 :chowla_selberg_s4.leading_exp = -7**


[IV.T10] The Chowla-Selberg leading exponent at s = 4 is -7.

This is the origin of ι<sub>τ</sub>^(-7) in the mass ratio formula:
the Epstein zeta function Z(4; iι<sub>τ</sub>) has its leading term
proportional to ι<sub>τ</sub>^(1-2×4) = ι<sub>τ</sub>^(-7).

---

### `Tau.BookIV.Calibration.exponent_formula_s4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L135-L137)
**theorem
Tau.BookIV.Calibration.exponent_formula_s4 :1 - 2 * 4 = -7**


At s = 4, the exponent formula gives 1 - 8 = -7.

---

### `Tau.BookIV.Calibration.s4_unique_from_neg7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L139-L141)
**theorem
Tau.BookIV.Calibration.s4_unique_from_neg7
(s : ℕ)
 :1 - 2 * ↑s = -7 → s = 4**


The exponent -7 = 1 - 2s uniquely determines s = 4.

---

### `Tau.BookIV.Calibration.LatticeMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L147-L151)
**inductive
Tau.BookIV.Calibration.LatticeMode :Type**


Lattice modes classified by their role in the zeta sum.

- Axis : LatticeMode
- Interior : LatticeMode
Instances For

---

### `Tau.BookIV.Calibration.instReprLatticeMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L151-L151)
**instance
Tau.BookIV.Calibration.instReprLatticeMode :Repr LatticeMode**

Equations
- Tau.BookIV.Calibration.instReprLatticeMode = { reprPrec := Tau.BookIV.Calibration.instReprLatticeMode.repr }

---

### `Tau.BookIV.Calibration.instReprLatticeMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L151-L151)
**def
Tau.BookIV.Calibration.instReprLatticeMode.repr :LatticeMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqLatticeMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L151-L151)
**instance
Tau.BookIV.Calibration.instDecidableEqLatticeMode :DecidableEq LatticeMode**

Equations
- Tau.BookIV.Calibration.instDecidableEqLatticeMode x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Calibration.NAxisDominance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L153-L162)
**structure
Tau.BookIV.Calibration.NAxisDominance :Type**


The n-axis modes dominate Z(4; iι<sub>τ</sub>).
Numerical result: Z_{n-axis} / Z(4) ≈ 99.95%.
This is because ι<sub>τ</sub> < 1 amplifies the n-axis contribution
(small shape parameter = elongated torus).

- dominance_lower_bound : ℕ
Z_{n-axis}/Z(4) lower bound (in parts per 10000).

- dominates : self.dominance_lower_bound > 9900
The n-axis modes contribute > 99% of Z(4).

Instances For

---

### `Tau.BookIV.Calibration.instReprNAxisDominance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L162-L162)
**def
Tau.BookIV.Calibration.instReprNAxisDominance.repr :NAxisDominance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprNAxisDominance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L162-L162)
**instance
Tau.BookIV.Calibration.instReprNAxisDominance :Repr NAxisDominance**

Equations
- Tau.BookIV.Calibration.instReprNAxisDominance = { reprPrec := Tau.BookIV.Calibration.instReprNAxisDominance.repr }

---

### `Tau.BookIV.Calibration.n_axis_dominant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L164-L167)
**def
Tau.BookIV.Calibration.n_axis_dominant :NAxisDominance**


The n-axis dominance claim (from numerical lab).
Equations
- Tau.BookIV.Calibration.n_axis_dominant = { dominance_lower_bound := 9995, dominates := Tau.BookIV.Calibration.n_axis_dominant._proof_2 }
Instances For

---

### `Tau.BookIV.Calibration.NormalizationRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L173-L193)
**structure
Tau.BookIV.Calibration.NormalizationRemark :Type**


[IV.R10] The normalization N = Z(4; iι<sub>τ</sub>)/R ≈ 5.935 is NOT algebraic.

Z(4; iι<sub>τ</sub>) ≈ 10912 (total zeta value)
R ≈ 1838.68 (mass ratio)
N = Z(4)/R ≈ 5.935 (not a simple ratio)

The mass ratio R is the bulk-to-surface breathing ratio
of the Hodge Laplacian on T², NOT Z(4) divided by an
integer or simple algebraic constant.

This is a structural observation — the "normalization problem"
is dissolved once we recognize R as the ratio of Hilbert-space
norms, not as Z(4) divided by something.

- z4_approx_scaled : ℕ
Z(4; iι<sub>τ</sub>) approximate value (scaled ×1000).

- r_approx_scaled : ℕ
R approximate value (scaled ×1000).

- not_algebraic : String
The ratio is not a simple integer.

Instances For

---

### `Tau.BookIV.Calibration.instReprNormalizationRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L193-L193)
**instance
Tau.BookIV.Calibration.instReprNormalizationRemark :Repr NormalizationRemark**

Equations
- Tau.BookIV.Calibration.instReprNormalizationRemark = { reprPrec := Tau.BookIV.Calibration.instReprNormalizationRemark.repr }

---

### `Tau.BookIV.Calibration.instReprNormalizationRemark.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L193-L193)
**def
Tau.BookIV.Calibration.instReprNormalizationRemark.repr :NormalizationRemark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.shape_is_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L199-L203)
**theorem
Tau.BookIV.Calibration.shape_is_iota :epstein_at_T2.shape_numer = Boundary.iota_tau_numer ∧ epstein_at_T2.shape_denom = Boundary.iota_tau_denom**


The shape parameter matches ι<sub>τ</sub>.

---

### `Tau.BookIV.Calibration.eval_at_s4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L205-L206)
**theorem
Tau.BookIV.Calibration.eval_at_s4 :epstein_at_T2.eval_point = 4**


The evaluation point is s = 4.

---

### `Tau.BookIV.Calibration.chowla_selberg_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/EpsteinZeta.lean#L208-L211)
**theorem
Tau.BookIV.Calibration.chowla_selberg_consistent :chowla_selberg_s4.leading_exp = 1 - 2 * ↑chowla_selberg_s4.s**


The Chowla-Selberg exponent matches the formula.
