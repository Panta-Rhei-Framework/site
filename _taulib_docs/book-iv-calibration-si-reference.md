---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.SIReference"
permalink: /verify/taulib/docs/book-iv-calibration-si-reference/
lane: verify
module_name: "TauLib.BookIV.Calibration.SIReference"
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

# TauLib.BookIV.Calibration.SIReference


SI physical constants as exact scaled Nat pairs — the calibration targets
against which τ-derived values are compared.

## Registry Cross-References


- [IV.D26] SI Reference Table — `SIConstant`, `si_exact_constants`

- [IV.D27] SI Measured Constants — `si_measured_constants`


## Mathematical Content


### SI Exact Defining Constants (2019 revision)


Since the 2019 SI redefinition, seven constants have exact numerical values:
c, h, e, k_B, N_A, Δν_Cs, K_cd. We store the four structurally relevant ones
(Tiers I and II in the τ-classification) as exact Nat pairs.

### SI Measured Constants (CODATA 2022)


Key measured values that the τ-framework must reproduce:


- Neutron mass m_n (the calibration anchor)

- Electron mass m_e (derived via mass ratio R)

- Proton mass m_p (derived via weak polarization)

- Fine-structure constant α (spectral + holonomy routes)

- Weinberg angle sin²θ_W (weak-gravity coupling)

- Strong coupling α_s(M_Z) (confinement coupling)

- Mass ratio R = m_n/m_e

- Gravitational constant G (frontier, Book V)


All values stored as (numer, denom) Nat pairs with positive denominators.
Float display is available via `.toFloat` for smoke tests only.

## Ground Truth Sources


- CODATA 2022 recommended values (NIST)

- Book IV Part II ch12 (Calibration Anchor), ch13 (Dimensional Bridge)


---

### `Tau.BookIV.Calibration.SIConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L48-L62)
**structure
Tau.BookIV.Calibration.SIConstant :Type**


[IV.D26] An SI physical constant stored as an exact scaled rational.
The actual SI value is `numer / denom` in the appropriate SI unit.
`is_exact = true` for constants that are exact by SI 2019 definition.

- name : String
Display name of the constant.

- numer : ℕ
Scaled numerator.

- denom : ℕ
Scale denominator.

- denom_pos : self.denom > 0
Denominator is positive.

- is_exact : Bool
True if the value is exact by SI definition (not measured).

Instances For

---

### `Tau.BookIV.Calibration.instReprSIConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L62-L62)
**instance
Tau.BookIV.Calibration.instReprSIConstant :Repr SIConstant**

Equations
- Tau.BookIV.Calibration.instReprSIConstant = { reprPrec := Tau.BookIV.Calibration.instReprSIConstant.repr }

---

### `Tau.BookIV.Calibration.instReprSIConstant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L62-L62)
**def
Tau.BookIV.Calibration.instReprSIConstant.repr :SIConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.SIConstant.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L64-L66)
**def
Tau.BookIV.Calibration.SIConstant.toFloat
(c : SIConstant)
 :Float**


Float display for SI constant (smoke tests only).
Equations
- c.toFloat = Float.ofNat c.numer / Float.ofNat c.denom
Instances For

---

### `Tau.BookIV.Calibration.si_speed_of_light`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L72-L80)
**def
Tau.BookIV.Calibration.si_speed_of_light :SIConstant**


Speed of light: c = 299 792 458 m/s (EXACT).
Tier I structural constant: base–fiber conversion factor.
Stored as 299792458 / 1.
Equations
- Tau.BookIV.Calibration.si_speed_of_light = { name := "Speed of light c", numer := 299792458, denom := 1,
 denom_pos := Tau.BookIV.Calibration.si_speed_of_light._proof_2, is_exact := true }
Instances For

---

### `Tau.BookIV.Calibration.si_planck_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L82-L90)
**def
Tau.BookIV.Calibration.si_planck_constant :SIConstant**


Planck constant: h = 6.626 070 15 × 10⁻³⁴ J·s (EXACT).
Tier I structural constant: minimal action quantum.
Stored as 662607015 / 10⁴² (numer = h × 10⁴²).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_elementary_charge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L92-L100)
**def
Tau.BookIV.Calibration.si_elementary_charge :SIConstant**


Elementary charge: e = 1.602 176 634 × 10⁻¹⁹ C (EXACT).
Tier II physical constant: EM sector charge quantum.
Stored as 1602176634 / 10²⁸ (numer = e × 10²⁸).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_boltzmann`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L102-L110)
**def
Tau.BookIV.Calibration.si_boltzmann :SIConstant**


Boltzmann constant: k_B = 1.380 649 × 10⁻²³ J/K (EXACT).
Tier II physical constant: entropy–energy bridge.
Stored as 1380649 / 10²⁹ (numer = k_B × 10²⁹).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_avogadro`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L112-L120)
**def
Tau.BookIV.Calibration.si_avogadro :SIConstant**


Avogadro constant: N_A = 6.022 140 76 × 10²³ mol⁻¹ (EXACT).
Tier III conventional constant: counting scale.
Stored as 602214076 / 100 (numer/100 = N_A / 10²¹).
Equations
- Tau.BookIV.Calibration.si_avogadro = { name := "Avogadro constant N_A", numer := 602214076, denom := 100,
 denom_pos := Tau.BookIV.Calibration.si_avogadro._proof_2, is_exact := true }
Instances For

---

### `Tau.BookIV.Calibration.si_exact_constants`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L122-L124)
**def
Tau.BookIV.Calibration.si_exact_constants :List SIConstant**


The 4 structurally relevant SI exact constants.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_neutron_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L130-L139)
**def
Tau.BookIV.Calibration.si_neutron_mass :SIConstant**


[IV.D27] Neutron mass: m_n = 1.674 927 498 04(95) × 10⁻²⁷ kg.
THE calibration anchor — the single experimental input.
Relative uncertainty: 5.7 × 10⁻¹⁰.
Stored as 167492749804 / 10³⁸.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_electron_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L141-L149)
**def
Tau.BookIV.Calibration.si_electron_mass :SIConstant**


Electron mass: m_e = 9.109 383 7015(28) × 10⁻³¹ kg.
Derived via R = m_n/m_e in the τ-framework.
Stored as 91093837015 / 10⁴¹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_proton_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L151-L159)
**def
Tau.BookIV.Calibration.si_proton_mass :SIConstant**


Proton mass: m_p = 1.672 621 923 69(51) × 10⁻²⁷ kg.
Derived as neutron minus weak polarization δ_A.
Stored as 167262192369 / 10³⁸.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_alpha_inverse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L161-L169)
**def
Tau.BookIV.Calibration.si_alpha_inverse :SIConstant**


Fine-structure constant inverse: 1/α = 137.035 999 084(21).
τ-spectral approximation: (8/15)·ι<sub>τ</sub>⁴ → 1/α ≈ 137.9.
Stored as 137035999084 / 10⁹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_weinberg_sin2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L171-L179)
**def
Tau.BookIV.Calibration.si_weinberg_sin2 :SIConstant**


Weinberg angle: sin²θ_W = 0.23121(4) (on-shell, CODATA 2022).
τ-candidate: κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>) ≈ 0.2249.
Stored as 23121 / 100000.
Equations
- Tau.BookIV.Calibration.si_weinberg_sin2 = { name := "Weinberg angle sin²θ_W", numer := 23121, denom := 100000,
 denom_pos := Tau.BookIV.Calibration.si_weinberg_sin2._proof_2, is_exact := false }
Instances For

---

### `Tau.BookIV.Calibration.si_strong_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L181-L189)
**def
Tau.BookIV.Calibration.si_strong_coupling :SIConstant**


Strong coupling: α_s(M_Z) = 0.1180(9).
τ-candidate: 2·κ(C) = 2·ι<sub>τ</sub>³/(1−ι<sub>τ</sub>) ≈ 0.1208.
Stored as 1180 / 10000.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_mass_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L191-L199)
**def
Tau.BookIV.Calibration.si_mass_ratio :SIConstant**


Neutron-to-electron mass ratio: R = m_n/m_e = 1838.683 661 73(89).
Dimensionless — determined by ι<sub>τ</sub> via depth ordering in the τ-framework.
Stored as 183868366173 / 10⁸.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_np_mass_diff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L201-L209)
**def
Tau.BookIV.Calibration.si_np_mass_diff :SIConstant**


Neutron–proton mass difference: Δm = 1.293 332 36(46) MeV/c².
In kg: 2.305 574 35 × 10⁻³⁰ kg.
Stored as MeV value: 129333236 / 10⁸.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_gravitational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L211-L220)
**def
Tau.BookIV.Calibration.si_gravitational :SIConstant**


Gravitational constant: G = 6.674 30(15) × 10⁻¹¹ m³/(kg·s²).
The least precisely known fundamental constant (~22 ppm).
Frontier: requires D-sector base geometry (Book V).
Stored as 667430 / 10¹⁶.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_measured_constants`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L222-L226)
**def
Tau.BookIV.Calibration.si_measured_constants :List SIConstant**


All SI measured constants used for calibration comparison.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.si_tau_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L232-L241)
**def
Tau.BookIV.Calibration.si_tau_length :SIConstant**


τ length scale: L = (π/2)·r_n ≈ 1.32 × 10⁻¹⁵ m.
From the paper's measured neutron charge radius r_n ≈ 0.84 fm.
In the τ-framework: determined by torus shape ratio r/R = ι<sub>τ</sub>.
Stored as 132 / 10¹⁷.
Equations
- Tau.BookIV.Calibration.si_tau_length = { name := "τ length scale L", numer := 132, denom := 100000000000000000,
 denom_pos := Tau.BookIV.Calibration.si_tau_length._proof_2, is_exact := false }
Instances For

---

### `Tau.BookIV.Calibration.si_tau_frequency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L243-L253)
**def
Tau.BookIV.Calibration.si_tau_frequency :SIConstant**


τ frequency scale: H = R·f_e ≈ 2.2714 × 10²³ Hz.
Neutron de Broglie frequency.
In the τ-framework: determined once R and c, h are fixed.
Stored as 22714 / 10⁻¹⁹ → actually: 22714 × 10¹⁹.
Better encoding: H_numer = 22714, H_scale = 10¹⁹ (multiply to get Hz).
Equations
- Tau.BookIV.Calibration.si_tau_frequency = { name := "τ frequency scale H", numer := 22714, denom := 10,
 denom_pos := Tau.BookIV.Calibration.si_tau_frequency._proof_2, is_exact := false }
Instances For

---

### `Tau.BookIV.Calibration.exact_constants_are_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L259-L263)
**theorem
Tau.BookIV.Calibration.exact_constants_are_exact :((List.map SIConstant.is_exact si_exact_constants).all fun (x : Bool) => x == true) = true**


All SI exact constants are flagged as exact.

---

### `Tau.BookIV.Calibration.exact_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L265-L266)
**theorem
Tau.BookIV.Calibration.exact_count :si_exact_constants.length = 4**


Exactly 4 exact constants in our reference table.

---

### `Tau.BookIV.Calibration.measured_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L268-L269)
**theorem
Tau.BookIV.Calibration.measured_count :si_measured_constants.length = 9**


Exactly 9 measured constants in our reference table.

---

### `Tau.BookIV.Calibration.measured_not_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L271-L276)
**theorem
Tau.BookIV.Calibration.measured_not_exact :((List.map SIConstant.is_exact si_measured_constants).all fun (x : Bool) => x == false) = true**


No measured constant is flagged as exact.

---

### `Tau.BookIV.Calibration.c_exact_integer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L278-L279)
**theorem
Tau.BookIV.Calibration.c_exact_integer :si_speed_of_light.denom = 1**


Speed of light is exact integer: c = 299792458.

---

### `Tau.BookIV.Calibration.neutron_heavier_than_proton`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L281-L286)
**theorem
Tau.BookIV.Calibration.neutron_heavier_than_proton :si_neutron_mass.numer * si_proton_mass.denom > si_proton_mass.numer * si_neutron_mass.denom**


The neutron mass is the heaviest measured particle mass.
m_n > m_p (neutron heavier than proton).

---

### `Tau.BookIV.Calibration.mass_ratio_gt_1838`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L288-L291)
**theorem
Tau.BookIV.Calibration.mass_ratio_gt_1838 :si_mass_ratio.numer > 1838 * si_mass_ratio.denom**


The mass ratio R > 1838 (neutron is ~1839× heavier than electron).

---

### `Tau.BookIV.Calibration.mass_ratio_lt_1840`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L293-L296)
**theorem
Tau.BookIV.Calibration.mass_ratio_lt_1840 :si_mass_ratio.numer < 1840 * si_mass_ratio.denom**


The mass ratio R < 1840 (neutron is less than 1840× the electron).

---

### `Tau.BookIV.Calibration.alpha_inverse_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SIReference.lean#L298-L302)
**theorem
Tau.BookIV.Calibration.alpha_inverse_in_range :si_alpha_inverse.numer > 137 * si_alpha_inverse.denom ∧ si_alpha_inverse.numer < 138 * si_alpha_inverse.denom**


α⁻¹ is between 137 and 138 (brackets experimental value).
