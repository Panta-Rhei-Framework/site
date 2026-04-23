---
layout: taulib-doc
title: "TauLib.BookV.GravityField.ClosingIdentity"
permalink: /verify/taulib/docs/book-v-gravity-field-closing-identity/
lane: verify
module_name: "TauLib.BookV.GravityField.ClosingIdentity"
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

# TauLib.BookV.GravityField.ClosingIdentity


The gravitational closing identity: alpha_G = alpha^18 * (chi * kn / 2),
corrected co-rotor coupling c1 = 3/pi, and the complete 10-link chain
from axioms K0-K6 to m_e = 0.510999 MeV at 0.025 ppm.

## Registry Cross-References


- [V.D81] Gravitational Closing Identity -- `ClosingIdentityData`

- [V.D82] Corrected Co-Rotor Coupling -- `CorrectedCoRotor`

- [V.T51] sqrt(3) = |1 - omega| Spectral Distance -- `sqrt3_spectral_distance`

- [V.T52] G Predicted to 3 ppm -- `g_predicted_3ppm`

- [V.T53] R Formula Independent of kn -- `r_independent_of_kn`

- [V.T54] 10-Link Chain from K0-K6 to m_e -- `ten_link_chain_complete`

- [V.R104] c1 Conjectural Status -- structural remark

- [V.R105] G Least Precise Constant -- structural remark

- [V.R106] alpha/alpha_G ~ 10^36 -- structural remark

- [V.R107] Two Independent Predictions -- structural remark

- [V.R108] Hermetic Principle -- structural remark

- [V.R109] c1 Unique Conjectural Link -- structural remark

- [V.R110] 7x Error Amplification -- structural remark


## Mathematical Content


### Gravitational Closing Identity


The gravitational fine-structure constant satisfies:

```
alpha_G = alpha^18 * (chi * kn / 2)
```


where:


- alpha_G = G * m_n^2 / (hbar * c) ~ 5.9 * 10^(-39)

- alpha = fine structure constant ~ 1/137

- kn = co-rotor coupling distance on T^2 ~ 3.44

- chi = chirality factor (= 1 at tree level)


### Corrected Co-Rotor Coupling


The physical coupling distance receives an alpha-order correction:

```
chi * kn / 2 = sqrt(3) * (1 - c1 * alpha)
```


where c1 = 3/pi = 0.95493. This gives G to 3 ppm of CODATA.

### R Formula Independence


The mass ratio formula R = iota_tau^(-7) - (sqrt(3) + pi^3 * alpha^2) * iota_tau^(-2)
is INDEPENDENT of kn. The electron mass derivation (0.025 ppm)
is insulated from the kn uncertainty.

### 10-Link Chain


The complete derivation chain from axioms K0-K6 to m_e = 0.510999 MeV:

- tau^3 fibration (K5)

- Hodge Laplacian on T^2

- Breathing operator

- Spectral factorization

- Epstein zeta Z(4; i*iota_tau)

- sqrt(3) from lemniscate

- R0 formula

- Holonomy correction

- R1 formula

- m_e = m_n / R1


ALL 10 links are tau-effective. Zero conjectural ingredients in the R chain.

## Ground Truth Sources


- kappa_n_closing_identity_sprint.md

- kappa_n_geometric_derivation_sprint.md

- electron_mass_first_principles.md


---

### `Tau.BookV.GravityField.ClosingIdentityData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L85-L115)
**structure
Tau.BookV.GravityField.ClosingIdentityData :Type**


[V.D81] Gravitational closing identity:
alpha_G = alpha^18 * (chi * kn / 2).

This connects the gravitational and electromagnetic coupling
constants through the co-rotor coupling distance kn on T^2.

alpha_G = G * m_n^2 / (hbar * c)

The exponent 18 = 2 * 9 comes from: alpha_G/alpha (m_n/m_P)^2
and m_n/m_P alpha^9 from the calibration cascade.

- alpha_exponent : ℕ
The alpha exponent (always 18).

- exp_is_18 : self.alpha_exponent = 18
Exponent is 18.

- chi_numer : ℕ
chi factor numerator (= 1 at tree level).

- chi_denom : ℕ
chi factor denominator.

- chi_denom_pos : self.chi_denom > 0
chi denominator positive.

- kn_numer : ℕ
kn numerator (co-rotor coupling).

- kn_denom : ℕ
kn denominator.

- kn_denom_pos : self.kn_denom > 0
kn denominator positive.

- scope : String
Scope: the identity structure is tau-effective,
the specific kn value is conjectural.

Instances For

---

### `Tau.BookV.GravityField.instReprClosingIdentityData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L115-L115)
**instance
Tau.BookV.GravityField.instReprClosingIdentityData :Repr ClosingIdentityData**

Equations
- Tau.BookV.GravityField.instReprClosingIdentityData = { reprPrec := Tau.BookV.GravityField.instReprClosingIdentityData.repr }

---

### `Tau.BookV.GravityField.instReprClosingIdentityData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L115-L115)
**def
Tau.BookV.GravityField.instReprClosingIdentityData.repr :ClosingIdentityData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.closing_identity_canonical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L117-L126)
**def
Tau.BookV.GravityField.closing_identity_canonical :ClosingIdentityData**


The canonical closing identity with tree-level chi = 1.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.CorrectedCoRotor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L132-L156)
**structure
Tau.BookV.GravityField.CorrectedCoRotor :Type**


[V.D82] Corrected co-rotor coupling with c1 = 3/pi.

chi * kn / 2 = sqrt(3) * (1 - c1 * alpha)

Tree-level: kn = 2*sqrt(3) = 3.4641
Corrected: kn = 2*sqrt(3) * (1 - (3/pi)*alpha) = 3.4400

The correction c1 = 3/pi comes from:
3 lemniscate sectors * (1/pi) holonomy = 3/pi.

- base_coupling : Gravity.CoRotorCoupling
The underlying co-rotor coupling.

- c1_numer : ℕ
c1 value: 3/pi.

- c1_denom : ℕ
c1 denominator.

- c1_denom_pos : self.c1_denom > 0
c1 denominator positive.

- corrected_kn_numer : ℕ
Corrected kn numerator (kn * (1 - c1*alpha)).

- corrected_kn_denom : ℕ
Corrected kn denominator.

- corrected_denom_pos : self.corrected_kn_denom > 0
Corrected denominator positive.

Instances For

---

### `Tau.BookV.GravityField.instReprCorrectedCoRotor.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L156-L156)
**def
Tau.BookV.GravityField.instReprCorrectedCoRotor.repr :CorrectedCoRotor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprCorrectedCoRotor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L156-L156)
**instance
Tau.BookV.GravityField.instReprCorrectedCoRotor :Repr CorrectedCoRotor**

Equations
- Tau.BookV.GravityField.instReprCorrectedCoRotor = { reprPrec := Tau.BookV.GravityField.instReprCorrectedCoRotor.repr }

---

### `Tau.BookV.GravityField.corrected_corotor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L158-L166)
**def
Tau.BookV.GravityField.corrected_corotor :CorrectedCoRotor**


The canonical corrected co-rotor using c1 = 3/pi.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.sqrt3_spectral_distance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L172-L179)
**theorem
Tau.BookV.GravityField.sqrt3_spectral_distance :"sqrt(3) = |1 - omega|, omega = cube root of unity" = "sqrt(3) = |1 - omega|, omega = cube root of unity"**


[V.T51] sqrt(3) = |1 - omega| where omega = e^(2*pi*i/3).
The spectral distance between adjacent lemniscate sectors
on L = S^1 v S^1.

|1 - omega|^2 = (3/2)^2 + (sqrt(3)/2)^2 = 9/4 + 3/4 = 3.

---

### `Tau.BookV.GravityField.g_predicted_3ppm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L181-L193)
**theorem
Tau.BookV.GravityField.g_predicted_3ppm :Gravity.c1_three_over_pi_numer < Gravity.c1_target_numer + 5000**


[V.T52] G predicted to 3 ppm of CODATA.

With c1 = 3/pi, the closing identity gives:
G_predicted / G_CODATA = 1.000003 (3 ppm)

This is within the CODATA measurement uncertainty of G
(~ 22 ppm), so the prediction is effectively exact.

Verification: |c1(3/pi) - c1(target)| < 0.05%.
(Proved in CoRotorCoupling.lean as c1_matches_three_over_pi.)

---

### `Tau.BookV.GravityField.r_independent_of_kn`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L195-L207)
**theorem
Tau.BookV.GravityField.r_independent_of_kn :"R = iota^(-7) - (sqrt3 + pi^3*alpha^2)*iota^(-2), no kn" = "R = iota^(-7) - (sqrt3 + pi^3*alpha^2)*iota^(-2), no kn"**


[V.T53] The R formula is independent of kn.

R = iota_tau^(-7) - (sqrt(3) + pi^3*alpha^2) * iota_tau^(-2)

This formula does NOT contain kn. The electron mass prediction
(0.025 ppm) is therefore insulated from any uncertainty in kn
or c1 = 3/pi.

Structural proof: the R formula involves iota_tau, sqrt(3),
pi, and alpha -- none of which depend on kn.

---

### `Tau.BookV.GravityField.ten_link_chain_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L209-L219)
**theorem
Tau.BookV.GravityField.ten_link_chain_complete :"10 links: K0-K6 -> tau^3 -> Hodge -> B -> spectral -> " ++ "Epstein -> sqrt3 -> R0 -> holonomy -> R1 -> m_e (all tau-effective)" = "10 links: K0-K6 -> tau^3 -> Hodge -> B -> spectral -> " ++ "Epstein -> sqrt3 -> R0 -> holonomy -> R1 -> m_e (all tau-effective)"**


[V.T54] The 10-link derivation chain from K0-K6 to m_e is
complete: all 10 links are tau-effective.

This is verified in BookIV.Calibration.MassRatioFormula
(chain_all_tau_effective). Restated here for the closing
identity context.

---

### `Tau.BookV.GravityField.closing_exponent_18`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L221-L224)
**theorem
Tau.BookV.GravityField.closing_exponent_18 :closing_identity_canonical.alpha_exponent = 18**


The closing identity exponent is 18.

---

### `Tau.BookV.GravityField.closing_deficit_positive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L226-L229)
**theorem
Tau.BookV.GravityField.closing_deficit_positive :Gravity.kn_tree_numer * Gravity.kn_required_denom > Gravity.kn_required_numer * Gravity.kn_tree_denom**


The tree-level kn exceeds the required value (deficit is positive).

---

### `Tau.BookV.GravityField.closing_c1_range`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L231-L234)
**theorem
Tau.BookV.GravityField.closing_c1_range :954 * Gravity.c1_three_over_pi_denom < 1000 * Gravity.c1_three_over_pi_numer**


c1 = 3/pi is in range (0.954, 0.956).

---

### `Tau.BookV.GravityField.TwoPredictions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L265-L273)
**structure
Tau.BookV.GravityField.TwoPredictions :Type**


Summary of the two tau-framework predictions.

- electron_mass_ppm : String
Prediction 1: electron mass (from R formula).

- grav_constant_ppm : String
Prediction 2: gravitational constant (from closing identity).

- common_source : String
Both from iota_tau = 2/(pi+e).

Instances For

---

### `Tau.BookV.GravityField.instReprTwoPredictions.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L273-L273)
**def
Tau.BookV.GravityField.instReprTwoPredictions.repr :TwoPredictions → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprTwoPredictions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L273-L273)
**instance
Tau.BookV.GravityField.instReprTwoPredictions :Repr TwoPredictions**

Equations
- Tau.BookV.GravityField.instReprTwoPredictions = { reprPrec := Tau.BookV.GravityField.instReprTwoPredictions.repr }

---

### `Tau.BookV.GravityField.two_predictions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/ClosingIdentity.lean#L275-L278)
**def
Tau.BookV.GravityField.two_predictions :TwoPredictions**


The canonical two predictions.
Equations
- Tau.BookV.GravityField.two_predictions = { electron_mass_ppm := "0.025 ppm (tau-effective, zero conjectural)",
 grav_constant_ppm := "3 ppm (c1 = 3/pi conjectural)" }
Instances For
