---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.Reionization"
permalink: /verify/taulib/docs/book-v-cosmology-reionization/
lane: verify
module_name: "TauLib.BookV.Cosmology.Reionization"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Cosmology.Reionization


21cm hydrogen line prediction from τ-native cosmological inputs.
The brightness temperature uses Ω_m, ω_b, z_reion — all derived
from the τ-framework with zero free parameters.

## Registry Cross-References


- [V.D334] 21cm Brightness Temperature -- `BrightnessTemp21cm`

- [V.D335] Spin Temperature Coupling Regimes -- `SpinTempCoupling`

- [V.T271] 21cm Absorption Trough from τ-Native Inputs -- `absorption_trough_21cm`

- [V.P189] EDGES/HERA/SKA Predictions -- structural

- [V.R470] V.OP9 Status: PARTIAL-IMPROVED -- structural remark


## Mathematical Content


### 21cm Brightness Temperature [V.D334]


T₂₁(z) ≈ 27 mK · x_HI · (1 − T_CMB/T_S) · √((1+z)/10 · 0.15/Ω_m) · (ω_b/0.023)

### Absorption Trough [V.T271]


At z ≈ 17 (cosmic dawn), with τ-native Ω_m = 0.315 and ω_b = 0.02238:
T₂₁(z=17) ≈ −209 mK (standard ΛCDM evaluated at τ parameters).

## Ground Truth Sources


- Book V ch48: Threshold ladder, 21cm section (Wave 48A)

- EDGES collaboration (2018): −500 mK reported (unconfirmed)

- Standard 21cm cosmology: Furlanetto, Oh, Briggs (2006)


---

### `Tau.BookV.Cosmology.BrightnessTemp21cm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L41-L55)
**structure
Tau.BookV.Cosmology.BrightnessTemp21cm :Type**


21cm brightness temperature structure [V.D334].
Stores the τ-native cosmological parameters and computes
the differential brightness temperature against the CMB.
Scope: τ-effective (formula uses only τ-derived inputs).

- redshift : ℕ
Redshift of observation.

- x_HI_permille : ℕ
Neutral hydrogen fraction (0 to 1000, in per-mille).

- T_S_mK : ℕ
Spin temperature in mK.

- T_S_pos : self.T_S_mK > 0
T_S > 0.

- T_CMB_mK : ℕ
CMB temperature at redshift z in mK: 2725 × (1+z).

Instances For

---

### `Tau.BookV.Cosmology.SpinTempCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L57-L68)
**inductive
Tau.BookV.Cosmology.SpinTempCoupling :Type**


Spin temperature coupling regimes [V.D335].
Scope: conjectural (astrophysical modelling of x_α).

- collisional : SpinTempCoupling
Collisional coupling: z > 200, T_S ≈ T_K ≈ T_CMB.

- dark_ages : SpinTempCoupling
Dark ages: 30 < z < 200, T_K decouples, adiabatic cooling.

- cosmic_dawn : SpinTempCoupling
Cosmic dawn: z_reion < z < 30, Wouthuysen–Field effect.

- post_reion : SpinTempCoupling
Post-reionization: z < z_reion, emission.

Instances For

---

### `Tau.BookV.Cosmology.instDecidableEqSpinTempCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L68-L68)
**instance
Tau.BookV.Cosmology.instDecidableEqSpinTempCoupling :DecidableEq SpinTempCoupling**

Equations
- Tau.BookV.Cosmology.instDecidableEqSpinTempCoupling x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instReprSpinTempCoupling.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L68-L68)
**def
Tau.BookV.Cosmology.instReprSpinTempCoupling.repr :SpinTempCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprSpinTempCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L68-L68)
**instance
Tau.BookV.Cosmology.instReprSpinTempCoupling :Repr SpinTempCoupling**

Equations
- Tau.BookV.Cosmology.instReprSpinTempCoupling = { reprPrec := Tau.BookV.Cosmology.instReprSpinTempCoupling.repr }

---

### `Tau.BookV.Cosmology.absorption_trough_z17_mK`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L74-L77)
**def
Tau.BookV.Cosmology.absorption_trough_z17_mK :ℤ**


Absorption trough at z = 17 from τ-native inputs [V.T271].
T₂₁(z=17) ≈ −209 mK.
Scope: conjectural (depends on spin coupling model).
Equations
- Tau.BookV.Cosmology.absorption_trough_z17_mK = -209
Instances For

---

### `Tau.BookV.Cosmology.z_reion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L79-L81)
**def
Tau.BookV.Cosmology.z_reion :ℕ**


Reionization redshift from τ-axioms [already V.P139].
z_reion = a₃ − W₃(4) = 13 − 5 = 8.
Equations
- Tau.BookV.Cosmology.z_reion = 8
Instances For

---

### `Tau.BookV.Cosmology.z_reion_pos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L83-L84)
**theorem
Tau.BookV.Cosmology.z_reion_pos :z_reion > 0**


z_reion = 8 is positive.

---

### `Tau.BookV.Cosmology.trough_is_absorption`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/Reionization.lean#L86-L87)
**theorem
Tau.BookV.Cosmology.trough_is_absorption :absorption_trough_z17_mK < 0**


The trough prediction is an absorption signal (negative).
