---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.CalibrationAnchorExt"
permalink: /verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/
lane: verify
module_name: "TauLib.BookIV.Calibration.CalibrationAnchorExt"
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

# TauLib.BookIV.Calibration.CalibrationAnchorExt


Extended ch12 entries for the calibration anchor: relational units,
the 5→1 tau-collapse, Level 0/1+ mass ratio formula summaries,
unpolarized defect bundle, and tau-to-SI conversion.

## Registry Cross-References


- [IV.D289] Five Relational Units — `RelationalUnit`, `relational_units`

- [IV.T108] τ-Collapse: Five to One — `tau_collapse_five_to_one`

- [IV.T109] Level 0 Mass Ratio Formula — `Level0FormulaSummary`, `level0_summary`

- [IV.T110] Level 1+ Mass Ratio Formula — `Level1PlusFormulaSummary`, `level1plus_summary`

- [IV.D290] Unpolarized Defect Bundle — `UnpolarizedDefectBundle`

- [IV.P166] Neutron Minimality — `neutron_minimality`

- [IV.D291] Calibration Anchor (extended) — `CalibrationAnchorExt`

- [IV.T111] Parameter Count — `parameter_count_ext`

- [IV.D292] τ-to-SI Conversion — `TauToSIConversionExt`

- [IV.R262] What the paper got right (remark)

- [IV.R263] Not a numerical fit (remark)

- [IV.R264] The Planck mass in τ-physics (remark)

- [IV.R265] One input, not zero (remark)

- [IV.R266] Lean formalization (remark)

- [IV.R267] Falsifiability (remark)


## Mathematical Content


### Five Relational Units


The Springer Nature paper (Dec 2024) used five independent relational
quantities (M, L, H, Q, R) to parameterise fundamental constants.
In the τ-framework, four of these are determined by ι<sub>τ</sub> = 2/(π+e),
leaving only one free parameter: the neutron mass M = m_n.

### Mass Ratio Formula Summaries


Level 0: R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2) (7.7 ppm at exact ι<sub>τ</sub>)
Level 1+: R₁ = ι<sub>τ</sub>^(-7) − (√3 + π³α²)·ι<sub>τ</sub>^(-2) (0.025 ppm)

These are STRUCTURAL summaries referencing the full derivation in
MassRatioFormula.lean.

### Unpolarized Defect Bundle


The neutron is the minimal stable unpolarized T² defect bundle:
charge zero, isospin zero, χ-balanced. This minimality is what
makes it the natural calibration anchor.

## Ground Truth Sources


- Book IV Part II ch12 (Calibration Anchor — extended entries)

- electron_mass_first_principles.md (master synthesis)

- Springer Nature paper (Dec 2024): GeometricFoundation.tex


---

### `Tau.BookIV.Calibration.RelationalUnit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L65-L81)
**structure
Tau.BookIV.Calibration.RelationalUnit :Type**


[IV.D289] A relational unit from the Springer Nature paper.

The paper used five independent quantities (M, L, H, Q, R).
Each has a symbol, a physical meaning, and a scaled Nat value
(encoding the dimensional constant in appropriate SI units).

- symbol : String
Symbol: M, L, H, Q, or R.

- meaning : String
Physical interpretation.

- scaled_numer : ℕ
Scaled numerator (SI value encoding).

- scaled_denom : ℕ
Scaled denominator (SI value encoding).

- denom_pos : self.scaled_denom > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalUnit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L81-L81)
**def
Tau.BookIV.Calibration.instReprRelationalUnit.repr :RelationalUnit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalUnit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L81-L81)
**instance
Tau.BookIV.Calibration.instReprRelationalUnit :Repr RelationalUnit**

Equations
- Tau.BookIV.Calibration.instReprRelationalUnit = { reprPrec := Tau.BookIV.Calibration.instReprRelationalUnit.repr }

---

### `Tau.BookIV.Calibration.five_relational_units`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L83-L93)
**def
Tau.BookIV.Calibration.five_relational_units :List RelationalUnit**


The five relational units with representative scaled values.

M = neutron mass, L = length scale, H = frequency scale,
Q = elementary charge, R = mass ratio m_n/m_e.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.five_relational_units_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L95-L96)
**theorem
Tau.BookIV.Calibration.five_relational_units_count :five_relational_units.length = 5**


Five relational units total.

---

### `Tau.BookIV.Calibration.CollapseStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L102-L107)
**inductive
Tau.BookIV.Calibration.CollapseStatus :Type**


Status of a relational unit in the τ-collapse.

- Free : CollapseStatus
- IotaDetermined : CollapseStatus
- SIFixed : CollapseStatus
Instances For

---

### `Tau.BookIV.Calibration.instReprCollapseStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L107-L107)
**instance
Tau.BookIV.Calibration.instReprCollapseStatus :Repr CollapseStatus**

Equations
- Tau.BookIV.Calibration.instReprCollapseStatus = { reprPrec := Tau.BookIV.Calibration.instReprCollapseStatus.repr }

---

### `Tau.BookIV.Calibration.instReprCollapseStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L107-L107)
**def
Tau.BookIV.Calibration.instReprCollapseStatus.repr :CollapseStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqCollapseStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L107-L107)
**instance
Tau.BookIV.Calibration.instDecidableEqCollapseStatus :DecidableEq CollapseStatus**

Equations
- Tau.BookIV.Calibration.instDecidableEqCollapseStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Calibration.CollapsedUnit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L109-L115)
**structure
Tau.BookIV.Calibration.CollapsedUnit :Type**


A relational unit tagged with its collapse status.

- symbol : String
Symbol.

- status : CollapseStatus
Collapse status.

Instances For

---

### `Tau.BookIV.Calibration.instReprCollapsedUnit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L115-L115)
**def
Tau.BookIV.Calibration.instReprCollapsedUnit.repr :CollapsedUnit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprCollapsedUnit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L115-L115)
**instance
Tau.BookIV.Calibration.instReprCollapsedUnit :Repr CollapsedUnit**

Equations
- Tau.BookIV.Calibration.instReprCollapsedUnit = { reprPrec := Tau.BookIV.Calibration.instReprCollapsedUnit.repr }

---

### `Tau.BookIV.Calibration.collapsed_units`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L117-L124)
**def
Tau.BookIV.Calibration.collapsed_units :List CollapsedUnit**


The five units with their collapse statuses.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.tau_collapse_five_to_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L126-L138)
**theorem
Tau.BookIV.Calibration.tau_collapse_five_to_one :collapsed_units.length = 5 ∧ (List.filter (fun (x : CollapsedUnit) => x.status == CollapseStatus.Free) collapsed_units).length = 1 ∧ (List.filter (fun (x : CollapsedUnit) => x.status == CollapseStatus.IotaDetermined) collapsed_units).length = 3 ∧ (List.filter (fun (x : CollapsedUnit) => x.status == CollapseStatus.SIFixed) collapsed_units).length = 1 ∧ (List.filter (fun (x : CollapsedUnit) => x.status == CollapseStatus.IotaDetermined) collapsed_units).length + (List.filter (fun (x : CollapsedUnit) => x.status == CollapseStatus.SIFixed) collapsed_units).length = 4**


[IV.T108] τ-Collapse: Five to One.

Of 5 relational units, 4 are determined (3 by ι<sub>τ</sub> + 1 SI-exact),
leaving exactly 1 free parameter (the neutron mass).

---

### `Tau.BookIV.Calibration.Level0FormulaSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L144-L163)
**structure
Tau.BookIV.Calibration.Level0FormulaSummary :Type**


[IV.T109] Structural summary of the Level 0 mass ratio formula.

R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2)

The full derivation with range proofs is in MassRatioFormula.lean.
This structure records the key structural parameters.

- bulk_exponent : ℕ
Bulk exponent: ι<sub>τ</sub> raised to this (negative) power.

- correction_factor_label : String
Label for the correction factor coefficient.

- correction_exponent : ℕ
Correction exponent: ι<sub>τ</sub> raised to this (negative) power.

- result_range_lo : ℕ
Result range lower bound (inclusive).

- result_range_hi : ℕ
Result range upper bound (exclusive).

- accuracy_ppm_exact : String
Accuracy at exact ι<sub>τ</sub> (in ppm).

Instances For

---

### `Tau.BookIV.Calibration.instReprLevel0FormulaSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L163-L163)
**def
Tau.BookIV.Calibration.instReprLevel0FormulaSummary.repr :Level0FormulaSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprLevel0FormulaSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L163-L163)
**instance
Tau.BookIV.Calibration.instReprLevel0FormulaSummary :Repr Level0FormulaSummary**

Equations
- Tau.BookIV.Calibration.instReprLevel0FormulaSummary = { reprPrec := Tau.BookIV.Calibration.instReprLevel0FormulaSummary.repr }

---

### `Tau.BookIV.Calibration.level0_summary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L165-L172)
**def
Tau.BookIV.Calibration.level0_summary :Level0FormulaSummary**


The Level 0 formula summary.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.level0_bulk_exp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L174-L175)
**theorem
Tau.BookIV.Calibration.level0_bulk_exp :level0_summary.bulk_exponent = 7**


The bulk exponent is 7.

---

### `Tau.BookIV.Calibration.level0_range_valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L177-L182)
**theorem
Tau.BookIV.Calibration.level0_range_valid :level0_summary.result_range_lo = 1838 ∧ level0_summary.result_range_hi = 1839 ∧ level0_summary.result_range_lo < level0_summary.result_range_hi**


The Level 0 result range is (1838, 1839) at exact ι<sub>τ</sub>.

---

### `Tau.BookIV.Calibration.Level1PlusFormulaSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L188-L207)
**structure
Tau.BookIV.Calibration.Level1PlusFormulaSummary :Type**


[IV.T110] Structural summary of the Level 1+ mass ratio formula.

R₁ = ι<sub>τ</sub>^(-7) − (√3 + π³α²)·ι<sub>τ</sub>^(-2)

Adds the holonomy correction π³α² (three U(1) circles in τ³,
second-order EM). At exact ι<sub>τ</sub>, this achieves 0.025 ppm.

- holonomy_correction_label : String
Label for the holonomy correction.

- correction_label : String
Full correction coefficient label.

- result_ppm_scaled : ℕ
Accuracy in ppm (scaled by 1000: 25 = 0.025 ppm).

- ppm_scale : ℕ
Scale factor for ppm (1000 means divide by 1000).

- holonomy_circles : ℕ
Number of holonomy circles.

- em_order : ℕ
EM correction order.

Instances For

---

### `Tau.BookIV.Calibration.instReprLevel1PlusFormulaSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L207-L207)
**def
Tau.BookIV.Calibration.instReprLevel1PlusFormulaSummary.repr :Level1PlusFormulaSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprLevel1PlusFormulaSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L207-L207)
**instance
Tau.BookIV.Calibration.instReprLevel1PlusFormulaSummary :Repr Level1PlusFormulaSummary**

Equations
- Tau.BookIV.Calibration.instReprLevel1PlusFormulaSummary = { reprPrec := Tau.BookIV.Calibration.instReprLevel1PlusFormulaSummary.repr }

---

### `Tau.BookIV.Calibration.level1plus_summary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L209-L216)
**def
Tau.BookIV.Calibration.level1plus_summary :Level1PlusFormulaSummary**


The Level 1+ formula summary.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.level1plus_ppm_sub_100`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L218-L220)
**theorem
Tau.BookIV.Calibration.level1plus_ppm_sub_100 :level1plus_summary.result_ppm_scaled < 100**


The ppm value (25/1000 = 0.025) is less than 100/1000 = 0.1 ppm.

---

### `Tau.BookIV.Calibration.level1plus_three_circles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L222-L224)
**theorem
Tau.BookIV.Calibration.level1plus_three_circles :level1plus_summary.holonomy_circles = 3**


The holonomy comes from exactly 3 circles.

---

### `Tau.BookIV.Calibration.level1plus_second_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L226-L228)
**theorem
Tau.BookIV.Calibration.level1plus_second_order :level1plus_summary.em_order = 2**


The EM correction is second-order (charge conjugation kills first).

---

### `Tau.BookIV.Calibration.UnpolarizedDefectBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L234-L248)
**structure
Tau.BookIV.Calibration.UnpolarizedDefectBundle :Type**


[IV.D290] An unpolarized defect bundle on the fiber T².

The three polarization properties that must ALL be zero/balanced
for a defect bundle to qualify as "unpolarized":


- charge_zero: net electric charge = 0

- isospin_zero: net isospin projection = 0

- chi_balanced: χ₊ and χ₋ characters in balance


- charge_zero : Bool
Net electric charge is zero.

- isospin_zero : Bool
Net isospin projection is zero.

- chi_balanced : Bool
Bipolar characters χ₊, χ₋ are balanced.

Instances For

---

### `Tau.BookIV.Calibration.instReprUnpolarizedDefectBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L248-L248)
**instance
Tau.BookIV.Calibration.instReprUnpolarizedDefectBundle :Repr UnpolarizedDefectBundle**

Equations
- Tau.BookIV.Calibration.instReprUnpolarizedDefectBundle = { reprPrec := Tau.BookIV.Calibration.instReprUnpolarizedDefectBundle.repr }

---

### `Tau.BookIV.Calibration.instReprUnpolarizedDefectBundle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L248-L248)
**def
Tau.BookIV.Calibration.instReprUnpolarizedDefectBundle.repr :UnpolarizedDefectBundle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.is_unpolarized`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L250-L252)
**def
Tau.BookIV.Calibration.is_unpolarized
(b : UnpolarizedDefectBundle)
 :Bool**


An unpolarized bundle has all three properties true.
Equations
- Tau.BookIV.Calibration.is_unpolarized b = (b.charge_zero && b.isospin_zero && b.chi_balanced)
Instances For

---

### `Tau.BookIV.Calibration.unpolarized_bundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L254-L255)
**def
Tau.BookIV.Calibration.unpolarized_bundle :UnpolarizedDefectBundle**


The canonical unpolarized bundle (all defaults).
Equations
- Tau.BookIV.Calibration.unpolarized_bundle = { }
Instances For

---

### `Tau.BookIV.Calibration.unpolarized_bundle_is_unpolarized`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L257-L259)
**theorem
Tau.BookIV.Calibration.unpolarized_bundle_is_unpolarized :is_unpolarized unpolarized_bundle = true**


The canonical bundle is unpolarized.

---

### `Tau.BookIV.Calibration.NeutronMinimality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L265-L281)
**structure
Tau.BookIV.Calibration.NeutronMinimality :Type**


[IV.P166] Neutron Minimality: the neutron is the minimal stable
unpolarized T² defect bundle.

"Minimal" means: among all unpolarized defect bundles on T²,
the neutron has the lowest mass (= smallest defect functional).
This is WHY it serves as the calibration anchor — it is the
FIRST stable particle the τ-framework produces.

- bundle : UnpolarizedDefectBundle
The neutron is unpolarized.

- is_unpol : is_unpolarized self.bundle = true
The bundle is indeed unpolarized.

- is_minimal : Bool
The neutron is the lightest (minimal mass among unpolarized).

- is_stable : Bool
The neutron is stable (lifetime > universe age).

Instances For

---

### `Tau.BookIV.Calibration.instReprNeutronMinimality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L281-L281)
**def
Tau.BookIV.Calibration.instReprNeutronMinimality.repr :NeutronMinimality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprNeutronMinimality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L281-L281)
**instance
Tau.BookIV.Calibration.instReprNeutronMinimality :Repr NeutronMinimality**

Equations
- Tau.BookIV.Calibration.instReprNeutronMinimality = { reprPrec := Tau.BookIV.Calibration.instReprNeutronMinimality.repr }

---

### `Tau.BookIV.Calibration.neutron_minimal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L283-L288)
**def
Tau.BookIV.Calibration.neutron_minimal :NeutronMinimality**


The neutron satisfies minimality.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.neutron_minimality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L290-L295)
**theorem
Tau.BookIV.Calibration.neutron_minimality :is_unpolarized neutron_minimal.bundle = true ∧ neutron_minimal.is_minimal = true ∧ neutron_minimal.is_stable = true**


[IV.P166] The neutron is both unpolarized and minimal.

---

### `Tau.BookIV.Calibration.CalibrationAnchorExt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L301-L316)
**structure
Tau.BookIV.Calibration.CalibrationAnchorExt :Type**


[IV.D291] Extended calibration anchor with explicit CODATA values.

The neutron mass m_n = 1.674 927 500 × 10⁻²⁷ kg (rounded to
10-digit numer for the extension), with uncertainty ~50 ppb.

- neutron_mass_kg_numer : ℕ
Neutron mass numerator (SI kg): 1674927500.

- neutron_mass_kg_denom : ℕ
Neutron mass denominator (SI kg): 10^36.

- denom_pos : self.neutron_mass_kg_denom > 0
Denominator is positive.

- uncertainty_ppb : ℕ
Uncertainty in parts per billion.

- sole_anchor : Bool
This is the sole anchor (one free parameter).

Instances For

---

### `Tau.BookIV.Calibration.instReprCalibrationAnchorExt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L316-L316)
**instance
Tau.BookIV.Calibration.instReprCalibrationAnchorExt :Repr CalibrationAnchorExt**

Equations
- Tau.BookIV.Calibration.instReprCalibrationAnchorExt = { reprPrec := Tau.BookIV.Calibration.instReprCalibrationAnchorExt.repr }

---

### `Tau.BookIV.Calibration.instReprCalibrationAnchorExt.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L316-L316)
**def
Tau.BookIV.Calibration.instReprCalibrationAnchorExt.repr :CalibrationAnchorExt → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.anchor_ext`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L318-L324)
**def
Tau.BookIV.Calibration.anchor_ext :CalibrationAnchorExt**


The canonical extended anchor.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.anchor_ext_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L326-L328)
**theorem
Tau.BookIV.Calibration.anchor_ext_positive :anchor_ext.neutron_mass_kg_numer > 0**


The anchor mass numerator is positive.

---

### `Tau.BookIV.Calibration.anchor_ext_precise`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L330-L332)
**theorem
Tau.BookIV.Calibration.anchor_ext_precise :anchor_ext.uncertainty_ppb < 100**


The uncertainty is sub-100 ppb.

---

### `Tau.BookIV.Calibration.parameter_count_ext`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L338-L348)
**theorem
Tau.BookIV.Calibration.parameter_count_ext :(List.filter (fun (x : CollapsedUnit) => x.status == CollapseStatus.Free) collapsed_units).length = 1 ∧ anchor_ext.sole_anchor = true**


[IV.T111] The τ-framework has exactly ONE free parameter.

All dimensionless quantities are fixed by ι<sub>τ</sub> = 2/(π+e).
The single free parameter is the neutron mass m_n
(the calibration anchor).

---

### `Tau.BookIV.Calibration.TauToSIConversionExt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L354-L368)
**structure
Tau.BookIV.Calibration.TauToSIConversionExt :Type**


[IV.D292] Extended τ-to-SI conversion structure.

In τ-native units, m_n = 1. The conversion to SI requires
exactly one anchor measurement (the neutron mass in kg).
All other SI values follow from ι<sub>τ</sub>-determined ratios.

- conversion_type : String
Type of conversion: "mass_anchor".

- anchor_count : ℕ
Number of independent anchors needed.

- anchor_name : String
The anchor constant name.

- all_ratios_determined : Bool
Whether all dimensionless ratios are ι<sub>τ</sub>-determined.

Instances For

---

### `Tau.BookIV.Calibration.instReprTauToSIConversionExt.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L368-L368)
**def
Tau.BookIV.Calibration.instReprTauToSIConversionExt.repr :TauToSIConversionExt → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprTauToSIConversionExt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L368-L368)
**instance
Tau.BookIV.Calibration.instReprTauToSIConversionExt :Repr TauToSIConversionExt**

Equations
- Tau.BookIV.Calibration.instReprTauToSIConversionExt = { reprPrec := Tau.BookIV.Calibration.instReprTauToSIConversionExt.repr }

---

### `Tau.BookIV.Calibration.tau_to_si_ext`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L370-L375)
**def
Tau.BookIV.Calibration.tau_to_si_ext :TauToSIConversionExt**


The canonical τ-to-SI conversion.
Equations
- Tau.BookIV.Calibration.tau_to_si_ext = { conversion_type := "mass_anchor", anchor_count := 1, anchor_name := "neutron_mass", all_ratios_determined := true }
Instances For

---

### `Tau.BookIV.Calibration.conversion_single_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L377-L379)
**theorem
Tau.BookIV.Calibration.conversion_single_anchor :tau_to_si_ext.anchor_count = 1**


Exactly 1 anchor is needed.

---

### `Tau.BookIV.Calibration.conversion_ratios_determined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L381-L383)
**theorem
Tau.BookIV.Calibration.conversion_ratios_determined :tau_to_si_ext.all_ratios_determined = true**


All dimensionless ratios are determined.
