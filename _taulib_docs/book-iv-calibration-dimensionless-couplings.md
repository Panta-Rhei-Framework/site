---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.DimensionlessCouplings"
permalink: /verify/taulib/docs/book-iv-calibration-dimensionless-couplings/
lane: verify
module_name: "TauLib.BookIV.Calibration.DimensionlessCouplings"
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

# TauLib.BookIV.Calibration.DimensionlessCouplings


The 5 self-couplings + 1 cross-coupling from Chapter 10, with their numerical
values presented as the Dimensionless Cascade.

## Registry Cross-References


- [IV.R247] Origin of the No Knobs Principle — (structural remark)

- [IV.D275] Gravitational self-coupling — `grav_self_coupling`

- [IV.P160] Numerical value κ(D) — `grav_coupling_value`

- [IV.D276] Weak self-coupling — `weak_self_coupling`

- [IV.P161] Numerical value κ(A) — `weak_coupling_value`

- [IV.D277] EM self-coupling — `em_self_coupling`

- [IV.P162] Numerical value κ(B) — `em_coupling_value`

- [IV.D278] Strong self-coupling — `strong_self_coupling`

- [IV.P163] Numerical value κ(C) — `strong_coupling_value`

- [IV.R248] Lean verification — (structural remark)

- [IV.D279] Omega self-coupling — `omega_self_coupling`

- [IV.P164] Numerical value κ(ω) — `omega_coupling_value`

- [IV.D280] Weak-gravity cross-coupling — `weak_grav_cross`


## Ground Truth Sources


- Chapter 10 of Book IV (2nd Edition), first half


---

### `Tau.BookIV.Calibration.grav_self_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L38-L40)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.grav_self_coupling :Sectors.CouplingFormula**


[IV.D275] Gravitational self-coupling κ(D;1) = 1 − ι<sub>τ</sub> ≈ 0.658541.
Depth 1, χ₊-dominant. The largest primitive coupling.
Equations
- Tau.BookIV.Calibration.grav_self_coupling = Tau.BookIV.Sectors.kappa_DD
Instances For

---

### `Tau.BookIV.Calibration.grav_coupling_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L42-L46)
**theorem
Tau.BookIV.Calibration.grav_coupling_value :grav_self_coupling.numer * 1000 > 658 * grav_self_coupling.denom ∧ grav_self_coupling.numer * 1000 < 659 * grav_self_coupling.denom**


[IV.P160] Numerical value: κ(D;1) is in (658, 659)/1000.

---

### `Tau.BookIV.Calibration.weak_self_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L52-L54)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.weak_self_coupling :Sectors.CouplingFormula**


[IV.D276] Weak self-coupling κ(A;1) = ι<sub>τ</sub> ≈ 0.341304.
Depth 1, balanced polarity. Equals the master constant.
Equations
- Tau.BookIV.Calibration.weak_self_coupling = Tau.BookIV.Sectors.kappa_AA
Instances For

---

### `Tau.BookIV.Calibration.weak_coupling_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L56-L60)
**theorem
Tau.BookIV.Calibration.weak_coupling_value :weak_self_coupling.numer * 1000 > 341 * weak_self_coupling.denom ∧ weak_self_coupling.numer * 1000 < 342 * weak_self_coupling.denom**


[IV.P161] Numerical value: κ(A;1) is in (341, 342)/1000.

---

### `Tau.BookIV.Calibration.em_self_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L66-L68)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.em_self_coupling :Sectors.CouplingFormula**


[IV.D277] Electromagnetic self-coupling κ(B;2) = ι<sub>τ</sub>² ≈ 0.116594.
Depth 2, χ₊-dominant.
Equations
- Tau.BookIV.Calibration.em_self_coupling = Tau.BookIV.Sectors.kappa_BB
Instances For

---

### `Tau.BookIV.Calibration.em_coupling_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L70-L74)
**theorem
Tau.BookIV.Calibration.em_coupling_value :em_self_coupling.numer * 1000 > 116 * em_self_coupling.denom ∧ em_self_coupling.numer * 1000 < 117 * em_self_coupling.denom**


[IV.P162] Numerical value: κ(B;2) is in (116, 117)/1000.

---

### `Tau.BookIV.Calibration.strong_self_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L80-L82)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.strong_self_coupling :Sectors.CouplingFormula**


[IV.D278] Strong self-coupling κ(C;3) = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>) ≈ 0.06046.
Depth 3, χ₋-dominant. Confinement coupling.
Equations
- Tau.BookIV.Calibration.strong_self_coupling = Tau.BookIV.Sectors.kappa_CC
Instances For

---

### `Tau.BookIV.Calibration.strong_coupling_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L84-L88)
**theorem
Tau.BookIV.Calibration.strong_coupling_value :strong_self_coupling.numer * 1000 > 60 * strong_self_coupling.denom ∧ strong_self_coupling.numer * 1000 < 61 * strong_self_coupling.denom**


[IV.P163] Numerical value: κ(C;3) is in (60, 61)/1000.

---

### `Tau.BookIV.Calibration.omega_self_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L94-L96)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.omega_self_coupling :Sectors.CouplingFormula**


[IV.D279] Omega self-coupling κ(ω) = ι<sub>τ</sub>³/(1+ι<sub>τ</sub>) ≈ 0.02968.
Crossing-point readout. The smallest primitive coupling.
Equations
- Tau.BookIV.Calibration.omega_self_coupling = Tau.BookIV.Sectors.kappa_BC
Instances For

---

### `Tau.BookIV.Calibration.omega_coupling_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L98-L102)
**theorem
Tau.BookIV.Calibration.omega_coupling_value :omega_self_coupling.numer * 1000 > 29 * omega_self_coupling.denom ∧ omega_self_coupling.numer * 1000 < 30 * omega_self_coupling.denom**


[IV.P164] Numerical value: κ(ω) is in (29, 30)/1000.

---

### `Tau.BookIV.Calibration.weak_grav_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L116-L118)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.weak_grav_cross :Sectors.CouplingFormula**


[IV.D280] Weak-gravity cross-coupling κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>) ≈ 0.2249.
Both sectors on base τ¹. Near sin²θ_W = 0.2312.
Equations
- Tau.BookIV.Calibration.weak_grav_cross = Tau.BookIV.Sectors.kappa_AD
Instances For
