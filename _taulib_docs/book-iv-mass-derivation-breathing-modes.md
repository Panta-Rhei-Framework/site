---
layout: taulib-doc
title: "TauLib.BookIV.MassDerivation.BreathingModes"
permalink: /verify/taulib/docs/book-iv-mass-derivation-breathing-modes/
lane: verify
module_name: "TauLib.BookIV.MassDerivation.BreathingModes"
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

# TauLib.BookIV.MassDerivation.BreathingModes


Breathing operator, torus spectral modes, three-fold lemniscate, and their
connection to the Epstein zeta function and √3 spectral distance.

## Registry Cross-References


- [IV.R336] Three-tier mass hierarchy — `MassHierarchy`

- [IV.D309] Breathing operator — `BreathingOperator`

- [IV.P171] Breathing spectrum discrete — `breathing_spectrum_discrete`

- [IV.D310] Epstein zeta on T² — `EpsteinZetaOnT2`

- [IV.R337] Toroidal modes 99.95% — `toroidal_dominance`

- [IV.D311] Chowla-Selberg — wraps `ChowlaSelbergTerms`

- [IV.T114] Leading term ∝ ι<sub>τ</sub>^{-7} — `leading_exponent_seven`

- [IV.R338] s=4 forced — `s4_forced`

- [IV.D312] Three-fold lemniscate — `ThreeFoldLemniscate`

- [IV.D313] Spectral distance √3 — `spectral_distance_sq`

- [IV.T115] d²=3 — `adjacent_distance_sq_is_3`

- [IV.R339-R343] structural remarks


## Ground Truth Sources


- electron_mass_first_principles.md §22-§28

- sqrt3_derivation_sprint.md §11-§15


---

### `Tau.BookIV.MassDerivation.MassHierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L39-L48)
**structure
Tau.BookIV.MassDerivation.MassHierarchy :Type**


[IV.R336] Three-tier mass hierarchy:
bulk ι<sub>τ</sub>^(-7) ≈ 1848, surface √3·ι<sub>τ</sub>^(-2) ≈ 14.9,
coupling π³α²·ι<sub>τ</sub>^(-2) ≈ 0.014.

- bulk_approx : ℕ
- surface_approx : ℕ
- coupling_approx : ℕ
- bulk_gt_surface : self.bulk_approx > self.surface_approx
- surface_gt_coupling : self.surface_approx > self.coupling_approx
Instances For

---

### `Tau.BookIV.MassDerivation.instReprMassHierarchy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L48-L48)
**def
Tau.BookIV.MassDerivation.instReprMassHierarchy.repr :MassHierarchy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instReprMassHierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L48-L48)
**instance
Tau.BookIV.MassDerivation.instReprMassHierarchy :Repr MassHierarchy**

Equations
- Tau.BookIV.MassDerivation.instReprMassHierarchy = { reprPrec := Tau.BookIV.MassDerivation.instReprMassHierarchy.repr }

---

### `Tau.BookIV.MassDerivation.mass_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L50-L52)
**def
Tau.BookIV.MassDerivation.mass_hierarchy :MassHierarchy**

Equations
- Tau.BookIV.MassDerivation.mass_hierarchy = { bulk_gt_surface := Tau.BookIV.MassDerivation.mass_hierarchy._proof_3,
 surface_gt_coupling := Tau.BookIV.MassDerivation.mass_hierarchy._proof_4 }
Instances For

---

### `Tau.BookIV.MassDerivation.BreathingOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L58-L64)
**structure
Tau.BookIV.MassDerivation.BreathingOperator :Type**


[IV.D309] Breathing operator B = (1/ι<sub>τ</sub>²)·Δ_Hodge⁻¹ on fiber T².

- inv_coeff_numer : ℕ
- inv_coeff_denom : ℕ
- denom_pos : self.inv_coeff_denom > 0
- fiber_restricted : Bool
Instances For

---

### `Tau.BookIV.MassDerivation.instReprBreathingOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L64-L64)
**instance
Tau.BookIV.MassDerivation.instReprBreathingOperator :Repr BreathingOperator**

Equations
- Tau.BookIV.MassDerivation.instReprBreathingOperator = { reprPrec := Tau.BookIV.MassDerivation.instReprBreathingOperator.repr }

---

### `Tau.BookIV.MassDerivation.instReprBreathingOperator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L64-L64)
**def
Tau.BookIV.MassDerivation.instReprBreathingOperator.repr :BreathingOperator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.breathing_operator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L66-L69)
**def
Tau.BookIV.MassDerivation.breathing_operator :BreathingOperator**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.breathing_is_inverse_iota_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L71-L74)
**theorem
Tau.BookIV.MassDerivation.breathing_is_inverse_iota_sq :breathing_operator.inv_coeff_numer = Sectors.iota_sq_denom ∧ breathing_operator.inv_coeff_denom = Sectors.iota_sq_numer**


---

### `Tau.BookIV.MassDerivation.BreathingSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L80-L87)
**structure
Tau.BookIV.MassDerivation.BreathingSpectrum :Type**


[IV.P171] Breathing spectrum on T²: discrete positive eigenvalues.

- is_discrete : Bool
- all_positive : Bool
- shape_numer : ℕ
- shape_denom : ℕ
- denom_pos : self.shape_denom > 0
Instances For

---

### `Tau.BookIV.MassDerivation.instReprBreathingSpectrum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L87-L87)
**def
Tau.BookIV.MassDerivation.instReprBreathingSpectrum.repr :BreathingSpectrum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instReprBreathingSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L87-L87)
**instance
Tau.BookIV.MassDerivation.instReprBreathingSpectrum :Repr BreathingSpectrum**

Equations
- Tau.BookIV.MassDerivation.instReprBreathingSpectrum = { reprPrec := Tau.BookIV.MassDerivation.instReprBreathingSpectrum.repr }

---

### `Tau.BookIV.MassDerivation.breathing_spectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L89-L92)
**def
Tau.BookIV.MassDerivation.breathing_spectrum :BreathingSpectrum**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.breathing_spectrum_discrete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L94-L95)
**theorem
Tau.BookIV.MassDerivation.breathing_spectrum_discrete :breathing_spectrum.is_discrete = true**


---

### `Tau.BookIV.MassDerivation.EpsteinZetaOnT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L101-L105)
**structure
Tau.BookIV.MassDerivation.EpsteinZetaOnT2 :Type**


[IV.D310] Epstein zeta Z(s; iι<sub>τ</sub>) as spectral zeta of B on T².

- zeta : Calibration.EpsteinZetaStructure
- interpretation : String
Instances For

---

### `Tau.BookIV.MassDerivation.instReprEpsteinZetaOnT2.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L105-L105)
**def
Tau.BookIV.MassDerivation.instReprEpsteinZetaOnT2.repr :EpsteinZetaOnT2 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instReprEpsteinZetaOnT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L105-L105)
**instance
Tau.BookIV.MassDerivation.instReprEpsteinZetaOnT2 :Repr EpsteinZetaOnT2**

Equations
- Tau.BookIV.MassDerivation.instReprEpsteinZetaOnT2 = { reprPrec := Tau.BookIV.MassDerivation.instReprEpsteinZetaOnT2.repr }

---

### `Tau.BookIV.MassDerivation.epstein_on_T2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L107-L108)
**def
Tau.BookIV.MassDerivation.epstein_on_T2 :EpsteinZetaOnT2**

Equations
- Tau.BookIV.MassDerivation.epstein_on_T2 = { zeta := Tau.BookIV.Calibration.epstein_at_T2 }
Instances For

---

### `Tau.BookIV.MassDerivation.epstein_shape_is_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L110-L113)
**theorem
Tau.BookIV.MassDerivation.epstein_shape_is_iota :epstein_on_T2.zeta.shape_numer = Boundary.iota_tau_numer ∧ epstein_on_T2.zeta.shape_denom = Boundary.iota_tau_denom**


---

### `Tau.BookIV.MassDerivation.toroidal_dominance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L119-L122)
**theorem
Tau.BookIV.MassDerivation.toroidal_dominance :Calibration.n_axis_dominant.dominance_lower_bound > 9900**


[IV.R337] n-axis modes contribute 99.95% of Z(4).

---

### `Tau.BookIV.MassDerivation.chowla_selberg_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L124-L125)
**def
Tau.BookIV.MassDerivation.chowla_selberg_data :Calibration.ChowlaSelbergTerms**


[IV.D311] Chowla-Selberg data at s=4.
Equations
- Tau.BookIV.MassDerivation.chowla_selberg_data = Tau.BookIV.Calibration.chowla_selberg_s4
Instances For

---

### `Tau.BookIV.MassDerivation.leading_exponent_seven`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L127-L130)
**theorem
Tau.BookIV.MassDerivation.leading_exponent_seven :Calibration.chowla_selberg_s4.leading_exp = -7**


[IV.T114] Leading term ∝ ι<sub>τ</sub>^{-7} (exponent = 1−2×4 = −7).

---

### `Tau.BookIV.MassDerivation.s4_forced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L132-L135)
**theorem
Tau.BookIV.MassDerivation.s4_forced
(s : ℕ)
 :1 - 2 * ↑s = -7 → s = 4**


[IV.R338] s=4 forced by mass operator: 1−2s = −7 → s = 4.

---

### `Tau.BookIV.MassDerivation.ThreeFoldLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L141-L147)
**structure
Tau.BookIV.MassDerivation.ThreeFoldLemniscate :Type**


[IV.D312] Three-fold lemniscate: Lobe_B, Lobe_C, Crossing_ω.

- three_fold_data : Physics.LemniscateThreeFold
- sector_B : String
- sector_C : String
- sector_omega : String
Instances For

---

### `Tau.BookIV.MassDerivation.instReprThreeFoldLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L147-L147)
**instance
Tau.BookIV.MassDerivation.instReprThreeFoldLemniscate :Repr ThreeFoldLemniscate**

Equations
- Tau.BookIV.MassDerivation.instReprThreeFoldLemniscate = { reprPrec := Tau.BookIV.MassDerivation.instReprThreeFoldLemniscate.repr }

---

### `Tau.BookIV.MassDerivation.instReprThreeFoldLemniscate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L147-L147)
**def
Tau.BookIV.MassDerivation.instReprThreeFoldLemniscate.repr :ThreeFoldLemniscate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.three_fold_lemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L149-L150)
**def
Tau.BookIV.MassDerivation.three_fold_lemniscate :ThreeFoldLemniscate**

Equations
- Tau.BookIV.MassDerivation.three_fold_lemniscate = { three_fold_data := Tau.BookIV.Physics.three_fold }
Instances For

---

### `Tau.BookIV.MassDerivation.three_supports`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L152-L154)
**theorem
Tau.BookIV.MassDerivation.three_supports :three_fold_lemniscate.three_fold_data.supports.length = 3**


---

### `Tau.BookIV.MassDerivation.spectral_distance_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L156-L158)
**theorem
Tau.BookIV.MassDerivation.spectral_distance_sq :three_fold_lemniscate.three_fold_data.distance_sq = 3**


[IV.D313] Spectral distance² = 3 (distance = √3).

---

### `Tau.BookIV.MassDerivation.adjacent_distance_sq_is_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L160-L163)
**theorem
Tau.BookIV.MassDerivation.adjacent_distance_sq_is_3 :Physics.omega_real_sq + Physics.omega_imag_sq = 3 * Physics.omega_denom**


[IV.T115] d²=3 from |1 − e^{2πi/3}|² = (3/2)² + (√3/2)² = 3.

---

### `Tau.BookIV.MassDerivation.bulk_dominates_surface`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L169-L171)
**theorem
Tau.BookIV.MassDerivation.bulk_dominates_surface :mass_hierarchy.bulk_approx > 100 * mass_hierarchy.surface_approx**


---

### `Tau.BookIV.MassDerivation.surface_dominates_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/BreathingModes.lean#L173-L175)
**theorem
Tau.BookIV.MassDerivation.surface_dominates_coupling :mass_hierarchy.surface_approx > 100 * mass_hierarchy.coupling_approx**
