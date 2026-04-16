---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.DimensionlessCouplings2"
permalink: /verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/
lane: verify
module_name: "TauLib.BookIV.Calibration.DimensionlessCouplings2"
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

# TauLib.BookIV.Calibration.DimensionlessCouplings2


Cross-couplings (ch10 second half), temporal complement, multiplicative
closure, and power hierarchy — all wrapping existing CouplingFormulas proofs.

## Registry Cross-References


- [IV.D281] Electroweak cross-coupling — `ew_cross`

- [IV.D282] Weak-strong cross-coupling — `weak_strong_cross`

- [IV.D283] EM-strong cross-coupling — `em_strong_cross`

- [IV.D284] EM-gravity cross-coupling — `em_grav_cross`

- [IV.D285] Strong-gravity cross-coupling — `strong_grav_cross`

- [IV.R250] Lean verification — (structural remark)

- [IV.T104] Temporal Complement — `temporal_complement_ch10`

- [IV.T105] Temporal Multiplicative Closure — `temporal_mult_ch10`

- [IV.R252] Lean formalization — (structural remark)

- [IV.T106] Power Hierarchy — `power_hierarchy_ch10`

- [IV.P165] Hierarchy Resolution — `hierarchy_resolution`

- [IV.R254] No landscape — (structural remark)


## Ground Truth Sources


- Chapter 10 of Book IV (2nd Edition), second half


---

### `Tau.BookIV.Calibration.ew_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L36-L38)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.ew_cross :Sectors.CouplingFormula**


[IV.D281] Electroweak cross-coupling κ(A,B) = ι<sub>τ</sub>³ ≈ 0.03982.
Connects weak (base) to EM (fiber).
Equations
- Tau.BookIV.Calibration.ew_cross = Tau.BookIV.Sectors.kappa_AB
Instances For

---

### `Tau.BookIV.Calibration.weak_strong_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L40-L42)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.weak_strong_cross :Sectors.CouplingFormula**


[IV.D282] Weak-strong cross-coupling κ(A,C) = ι<sub>τ</sub>⁴/(1−ι<sub>τ</sub>) ≈ 0.02063.
Note: kappa_AC is ι<sub>τ</sub>⁴/(1−ι<sub>τ</sub>) = κ(A)·κ(C), the Weak-Strong = beta decay channel.
Equations
- Tau.BookIV.Calibration.weak_strong_cross = Tau.BookIV.Sectors.kappa_AC
Instances For

---

### `Tau.BookIV.Calibration.em_strong_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L44-L46)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.em_strong_cross :Sectors.CouplingFormula**


[IV.D283] EM-strong cross-coupling κ(B,C) = ι<sub>τ</sub>³/(1+ι<sub>τ</sub>) ≈ 0.02968.
The weakest primitive cross-coupling.
Equations
- Tau.BookIV.Calibration.em_strong_cross = Tau.BookIV.Sectors.kappa_BC
Instances For

---

### `Tau.BookIV.Calibration.em_grav_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L48-L50)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.em_grav_cross :Sectors.CouplingFormula**


[IV.D284] EM-gravity cross-coupling κ(B,D) = ι<sub>τ</sub>²(1−ι<sub>τ</sub>)² ≈ 0.05061.
Gravitational lensing channel.
Equations
- Tau.BookIV.Calibration.em_grav_cross = Tau.BookIV.Sectors.kappa_BD
Instances For

---

### `Tau.BookIV.Calibration.strong_grav_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L52-L54)@[reducible, inline]

**abbrev
Tau.BookIV.Calibration.strong_grav_cross :Sectors.CouplingFormula**


[IV.D285] Strong-gravity cross-coupling κ(C,D) = ι<sub>τ</sub>³(1−ι<sub>τ</sub>) ≈ 0.02623.
Mass curves time.
Equations
- Tau.BookIV.Calibration.strong_grav_cross = Tau.BookIV.Sectors.kappa_CD
Instances For

---

### `Tau.BookIV.Calibration.temporal_complement_ch10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L63-L67)
**theorem
Tau.BookIV.Calibration.temporal_complement_ch10 :Sectors.kappa_AA.numer + Sectors.kappa_DD.numer = Sectors.kappa_AA.denom**


[IV.T104] Temporal complement: κ(A;1) + κ(D;1) = 1.
Wraps CouplingFormulas.temporal_complement.

---

### `Tau.BookIV.Calibration.temporal_mult_ch10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L73-L78)
**theorem
Tau.BookIV.Calibration.temporal_mult_ch10 :Sectors.kappa_AD.numer * (Sectors.kappa_AA.denom * Sectors.kappa_DD.denom) = Sectors.kappa_AA.numer * Sectors.kappa_DD.numer * Sectors.kappa_AD.denom**


[IV.T105] Temporal multiplicative closure: κ(A,D) = κ(A;1)·κ(D;1).
Wraps CouplingFormulas.temporal_multiplicative.

---

### `Tau.BookIV.Calibration.power_hierarchy_ch10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L87-L97)
**theorem
Tau.BookIV.Calibration.power_hierarchy_ch10 :Sectors.kappa_BB.numer * (Sectors.kappa_AA.denom * Sectors.kappa_AA.denom) = Sectors.kappa_AA.numer * Sectors.kappa_AA.numer * Sectors.kappa_BB.denom ∧ Sectors.kappa_AC.numer * (Sectors.kappa_AA.denom * Sectors.kappa_CC.denom) = Sectors.kappa_AA.numer * Sectors.kappa_CC.numer * Sectors.kappa_AC.denom**


[IV.T106] Power hierarchy: κ(B;2) = κ(A;1)² and κ(A,C) = κ(A;1)·κ(C;3).
The EM coupling is the square of the weak coupling; weak-strong is
the multiplicative closure of weak × strong.

---

### `Tau.BookIV.Calibration.hierarchy_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L103-L109)
**theorem
Tau.BookIV.Calibration.hierarchy_resolution :Sectors.kappa_DD.numer > Sectors.kappa_AA.numer**


[IV.P165] The gravitational self-coupling κ(D;1) = 1−ι<sub>τ</sub> is the
LARGEST primitive coupling. The apparent weakness of gravity
is a readout artifact: G involves ι<sub>τ</sub>² from the torus vacuum.
