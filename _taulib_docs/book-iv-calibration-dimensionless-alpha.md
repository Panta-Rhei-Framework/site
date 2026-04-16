---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.DimensionlessAlpha"
permalink: /verify/taulib/docs/book-iv-calibration-dimensionless-alpha/
lane: verify
module_name: "TauLib.BookIV.Calibration.DimensionlessAlpha"
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

# TauLib.BookIV.Calibration.DimensionlessAlpha


The fine structure constant α: spectral formula, holonomy formula,
five relational units, and the correction factor.

## Registry Cross-References


- [IV.D286] Spectral Fine-Structure Formula — `alpha_spec`

- [IV.R255] The meaning of 0.6% — (structural remark)

- [IV.R256] Lean verification — (structural remark)

- [IV.D287] Five Relational Units — `RelationalUnits`

- [IV.T107] Holonomy Fine-Structure Formula — `holonomy_formula_ch11`

- [IV.R257] Origin of the formula — (structural remark)

- [IV.R258] The three holonomy circles — (structural remark)

- [IV.D288] Holonomy Correction Factor — `CorrectionFactor`

- [IV.R260] The value of being wrong — (structural remark)


## Ground Truth Sources


- Chapter 11 of Book IV (2nd Edition)


---

### `Tau.BookIV.Calibration.alpha_spec_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L34-L37)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.alpha_spec_numer :ℕ**


[IV.D286] Spectral fine-structure formula: α_spec = (8/15)·ι<sub>τ</sub>⁴.
The prefactor 8/15 = 2³/(3·5) arises from the primorial structure.
Wraps FineStructure.alpha_spectral_*.
Equations
- Tau.BookIV.Calibration.alpha_spec_numer = Tau.BookIV.Sectors.alpha_spectral_numer
Instances For

---

### `Tau.BookIV.Calibration.alpha_spec_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L38-L38)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.alpha_spec_denom :ℕ**

Equations
- Tau.BookIV.Calibration.alpha_spec_denom = Tau.BookIV.Sectors.alpha_spectral_denom
Instances For

---

### `Tau.BookIV.Calibration.alpha_spec_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L40-L44)
**theorem
Tau.BookIV.Calibration.alpha_spec_range :alpha_spec_denom > 137 * alpha_spec_numer ∧ alpha_spec_denom < 139 * alpha_spec_numer**


The spectral formula gives 1/α between 137 and 139.

---

### `Tau.BookIV.Calibration.RelationalUnits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L57-L73)
**structure
Tau.BookIV.Calibration.RelationalUnits :Type**


[IV.D287] The five relational units M, L, H, Q, R derived from
the neutron mass anchor m_n and ι<sub>τ</sub>. The τ-framework collapses
the SI unit system from 7 base units to 1 anchor + 1 constant.

- mass_is_neutron : Bool
M = m_n (mass anchor).

- mass_true : self.mass_is_neutron = true
- unit_count : ℕ
Total relational units.

- count_eq : self.unit_count = 5
- si_base : ℕ
SI base units collapsed from.

- si_eq : self.si_base = 7
- free_params : ℕ
Effective free parameters.

- free_eq : self.free_params = 1
Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalUnits.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L73-L73)
**def
Tau.BookIV.Calibration.instReprRelationalUnits.repr :RelationalUnits → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalUnits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L73-L73)
**instance
Tau.BookIV.Calibration.instReprRelationalUnits :Repr RelationalUnits**

Equations
- Tau.BookIV.Calibration.instReprRelationalUnits = { reprPrec := Tau.BookIV.Calibration.instReprRelationalUnits.repr }

---

### `Tau.BookIV.Calibration.relational_units`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L75-L84)
**def
Tau.BookIV.Calibration.relational_units :RelationalUnits**


The canonical relational units.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.holonomy_formula_ch11`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L90-L102)
**theorem
Tau.BookIV.Calibration.holonomy_formula_ch11 :Sectors.holonomy_alpha.geom_numer = 31 ∧ Sectors.holonomy_alpha.geom_denom = 16 ∧ Sectors.holonomy_alpha.Q_exp + Sectors.holonomy_alpha.M_exp + Sectors.holonomy_alpha.H_exp + Sectors.holonomy_alpha.L_exp = -7**


[IV.T107] Holonomy fine-structure formula:
α = (π³/16) · Q⁴/(M²·H³·L⁶).
The factor π³ arises from three independent U(1) holonomy integrations
around the circles T_π, T_γ, T_η in τ³ = τ¹ ×_f T².
Wraps FineStructure.holonomy_alpha with holonomy_correction.

---

### `Tau.BookIV.Calibration.CorrectionFactor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L115-L126)
**structure
Tau.BookIV.Calibration.CorrectionFactor :Type**


[IV.D288] The holonomy correction factor R(ι<sub>τ</sub>) ≈ 1.006 measures
the deviation of the spectral approximation from the exact holonomy
formula. Wraps HolonomyCorrection module.

- near_unity_numer : ℕ
Correction is close to 1 (> 1000/1000).

- near_unity_denom : ℕ
- denom_pos : self.near_unity_denom > 0
- pi_cubed_approx : ℕ
π³ ≈ 31 holonomy circles.

- pi_cubed_eq : self.pi_cubed_approx = 31
Instances For

---

### `Tau.BookIV.Calibration.instReprCorrectionFactor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L126-L126)
**instance
Tau.BookIV.Calibration.instReprCorrectionFactor :Repr CorrectionFactor**

Equations
- Tau.BookIV.Calibration.instReprCorrectionFactor = { reprPrec := Tau.BookIV.Calibration.instReprCorrectionFactor.repr }

---

### `Tau.BookIV.Calibration.instReprCorrectionFactor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L126-L126)
**def
Tau.BookIV.Calibration.instReprCorrectionFactor.repr :CorrectionFactor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.correction_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L128-L134)
**def
Tau.BookIV.Calibration.correction_factor :CorrectionFactor**


The canonical correction factor.
Equations
- One or more equations did not get rendered due to their size.
Instances For
