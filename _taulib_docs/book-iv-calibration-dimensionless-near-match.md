---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.DimensionlessNearMatch"
permalink: /verify/taulib/docs/book-iv-calibration-dimensionless-near-match/
lane: verify
module_name: "TauLib.BookIV.Calibration.DimensionlessNearMatch"
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

# TauLib.BookIV.Calibration.DimensionlessNearMatch


Maps τ-derived dimensionless couplings to physical constants with range proofs.

## Registry Cross-References


- [IV.D28] Weinberg Near-Match — `WeinbergNearMatch`, `weinberg_range`

- [IV.D29] Strong Near-Match — `StrongNearMatch`, `strong_range`

- [IV.P05] All Near-Matches in Range — `all_near_matches_in_range`


## Mathematical Content


### Dimensionless Near-Matches


The τ-framework produces dimensionless couplings from ι<sub>τ</sub> alone.
Three such couplings can be compared to measured physical constants:


τ-coupling
Formula
τ-value
SI value
Deviation


α_EM
(8/15)·ι<sub>τ</sub>⁴
~1/137.9
1/137.036
0.6%


sin²θ_W
ι<sub>τ</sub>(1−ι<sub>τ</sub>)
~0.2249
0.23121
2.7%


α_s(M_Z)
2·ι<sub>τ</sub>³/(1−ι<sub>τ</sub>)
~0.1208
0.1180
2.4%


All three are CONJECTURAL: the numerical near-matches are observed but
the exact mechanism connecting ι<sub>τ</sub> formulas to measured values requires
the full calibration cascade (Parts III–X).

## Ground Truth Sources


- Book IV Part II ch10 (Sector Couplings), ch11 (Fine-Structure α)

- CODATA 2022 for experimental values


---

### `Tau.BookIV.Calibration.WeinbergNearMatch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L45-L56)
**structure
Tau.BookIV.Calibration.WeinbergNearMatch :Type**


[IV.D28] Weinberg angle near-match: κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>) vs sin²θ_W.

τ-derived: κ(A,D) ≈ 0.2249
Experimental: sin²θ_W = 0.23121(4) (on-shell, CODATA 2022)
Deviation: ~2.7%

- tau_coupling : Sectors.CouplingFormula
τ-derived coupling formula.

- si_value : SIConstant
SI reference value.

- scope : String
Scope: established (near-match with range proof).

Instances For

---

### `Tau.BookIV.Calibration.weinberg_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L58-L61)
**theorem
Tau.BookIV.Calibration.weinberg_range :Sectors.kappa_AD.numer * 1000 > 224 * Sectors.kappa_AD.denom ∧ Sectors.kappa_AD.numer * 1000 < 226 * Sectors.kappa_AD.denom**


κ(A,D) is in the range (0.224, 0.226).

---

### `Tau.BookIV.Calibration.weinberg_undershoots`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L63-L66)
**theorem
Tau.BookIV.Calibration.weinberg_undershoots :Sectors.kappa_AD.numer * si_weinberg_sin2.denom < si_weinberg_sin2.numer * Sectors.kappa_AD.denom**


κ(A,D) < sin²θ_W: the τ-approximation undershoots the experimental value.

---

### `Tau.BookIV.Calibration.weinberg_deviation_lt_3pct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L68-L74)
**theorem
Tau.BookIV.Calibration.weinberg_deviation_lt_3pct :(si_weinberg_sin2.numer * Sectors.kappa_AD.denom - Sectors.kappa_AD.numer * si_weinberg_sin2.denom) * 100 < 3 * si_weinberg_sin2.numer * Sectors.kappa_AD.denom**


The Weinberg deviation is less than 3%.
(sin²θ_W − κ(A,D)) × 100 < 3 × sin²θ_W
Cross-multiplied on Nat pairs.

---

### `Tau.BookIV.Calibration.StrongNearMatch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L80-L93)
**structure
Tau.BookIV.Calibration.StrongNearMatch :Type**


[IV.D29] Strong coupling near-match: 2·κ(C,C) vs α_s(M_Z).

τ-derived: 2·κ(C) = 2·ι<sub>τ</sub>³/(1−ι<sub>τ</sub>) ≈ 0.1208
Experimental: α_s(M_Z) = 0.1180(9)
Deviation: ~2.4%

- tau_coupling : Sectors.CouplingFormula
τ-derived coupling formula (doubled).

- factor : ℕ
Multiplication factor.

- si_value : SIConstant
SI reference value.

- scope : String
Scope: established (near-match with range proof).

Instances For

---

### `Tau.BookIV.Calibration.strong_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L95-L98)
**theorem
Tau.BookIV.Calibration.strong_range :2 * Sectors.kappa_CC.numer * 1000 > 119 * Sectors.kappa_CC.denom ∧ 2 * Sectors.kappa_CC.numer * 1000 < 122 * Sectors.kappa_CC.denom**


2·κ(C) is in the range (0.119, 0.122), bracketing α_s ≈ 0.1180.

---

### `Tau.BookIV.Calibration.strong_overshoots`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L100-L103)
**theorem
Tau.BookIV.Calibration.strong_overshoots :2 * Sectors.kappa_CC.numer * si_strong_coupling.denom > si_strong_coupling.numer * Sectors.kappa_CC.denom**


2·κ(C) > α_s: the τ-approximation overshoots the experimental value.

---

### `Tau.BookIV.Calibration.strong_deviation_lt_3pct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L105-L111)
**theorem
Tau.BookIV.Calibration.strong_deviation_lt_3pct :(2 * Sectors.kappa_CC.numer * si_strong_coupling.denom - si_strong_coupling.numer * Sectors.kappa_CC.denom) * 100 < 3 * si_strong_coupling.numer * Sectors.kappa_CC.denom**


The strong coupling deviation is less than 3%.
(2κ(C) − α_s) × 100 < 3 × α_s
Cross-multiplied on Nat pairs.

---

### `Tau.BookIV.Calibration.alpha_spectral_overshoots`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L117-L122)
**theorem
Tau.BookIV.Calibration.alpha_spectral_overshoots :Sectors.alpha_spectral_denom * si_alpha_inverse.denom > si_alpha_inverse.numer * Sectors.alpha_spectral_numer**


The spectral 1/α overshoots the experimental value:
α_spectral < α_exp (i.e. 1/α_spectral > 1/α_exp).
Spectral: 1/α ≈ 137.9, Experimental: 1/α ≈ 137.036.

---

### `Tau.BookIV.Calibration.all_near_matches_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L128-L141)
**theorem
Tau.BookIV.Calibration.all_near_matches_in_range :(Sectors.alpha_spectral_denom > 137 * Sectors.alpha_spectral_numer ∧ Sectors.alpha_spectral_denom < 139 * Sectors.alpha_spectral_numer) ∧ (Sectors.kappa_AD.numer * 1000 > 224 * Sectors.kappa_AD.denom ∧ Sectors.kappa_AD.numer * 1000 < 226 * Sectors.kappa_AD.denom) ∧ 2 * Sectors.kappa_CC.numer * 1000 > 119 * Sectors.kappa_CC.denom ∧ 2 * Sectors.kappa_CC.numer * 1000 < 122 * Sectors.kappa_CC.denom**


[IV.P05] All three dimensionless near-matches are within their
respective range brackets. This is a structural observation,
NOT a proof of correctness — all three are CONJECTURAL.

---

### `Tau.BookIV.Calibration.NearMatchEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L147-L155)
**structure
Tau.BookIV.Calibration.NearMatchEntry :Type**


Near-match entry for the summary table.

- name : String
- tau_numer : ℕ
- tau_denom : ℕ
- si_numer : ℕ
- si_denom : ℕ
- overshoots : Bool
Instances For

---

### `Tau.BookIV.Calibration.instReprNearMatchEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L155-L155)
**def
Tau.BookIV.Calibration.instReprNearMatchEntry.repr :NearMatchEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprNearMatchEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L155-L155)
**instance
Tau.BookIV.Calibration.instReprNearMatchEntry :Repr NearMatchEntry**

Equations
- Tau.BookIV.Calibration.instReprNearMatchEntry = { reprPrec := Tau.BookIV.Calibration.instReprNearMatchEntry.repr }

---

### `Tau.BookIV.Calibration.near_match_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L157-L171)
**def
Tau.BookIV.Calibration.near_match_table :List NearMatchEntry**


The three dimensionless near-match entries.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.near_match_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L173-L174)
**theorem
Tau.BookIV.Calibration.near_match_count :near_match_table.length = 3**


Three near-match entries.
