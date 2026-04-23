---
layout: taulib-doc
title: "TauLib.BookV.GravityField.LinearEinstein"
permalink: /verify/taulib/docs/book-v-gravity-field-linear-einstein/
lane: verify
module_name: "TauLib.BookV.GravityField.LinearEinstein"
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

# TauLib.BookV.GravityField.LinearEinstein


Weak-field (linearized) τ-Einstein equation: recovery of Newtonian gravity,
classical GR tests, and gravitational waves.

## Registry Cross-References


- [V.D52] Linearized τ-Einstein Equation — `LinearizedEinstein`

- [V.D53] Gravitational Wave — `GravitationalWave`

- [V.T28] Weak-Field Newtonian Recovery — `newtonian_recovery`

- [V.T29] Mercury Perihelion Precession — `mercury_precession`

- [V.T30] Light Deflection — `light_deflection`

- [V.T31] Gravitational Redshift — `grav_redshift`

- [V.T32] Gravitational Wave Properties — `grav_wave_properties`

- [V.P14] Gravitational Wave Speed = c — `grav_wave_speed_c`

- [V.R70] No Free Parameters in Precession — structural remark

- [V.R71] Two Polarizations from T² — structural remark


## Mathematical Content


### Linearized τ-Einstein Equation


In the weak-field regime (small curvature character), the τ-Einstein
equation R^H = κ_τ · T^mat linearizes to:

```
δR^H = κ_τ · δT^mat
```


where δ denotes the first-order perturbation around the flat (Minkowski)
background. This linearized form is the structural origin of:


- Newtonian gravity (static limit)

- Classical GR tests (perihelion, deflection, redshift)

- Gravitational waves (propagating solutions)


### Classical Tests


The three classical tests of GR emerge from the linearized τ-Einstein
equation applied to the Schwarzschild-like chart readout:

- **Mercury precession**: 43 arcsec/century (anomalous perihelion advance)

- **Light deflection**: 1.75 arcsec at solar limb (Eddington 1919)

- **Gravitational redshift**: Δf/f = GM/(rc²) (Pound-Rebka 1959)


These match GR predictions EXACTLY because the τ-Einstein equation
reduces to Einstein's equation under chart readout (V.T26).

### Gravitational Waves


Gravitational waves are propagating solutions of the linearized
τ-Einstein equation. Properties:


- Speed: c (null propagation on the base circle)

- Polarizations: 2 (from the T² fiber, plus/cross modes)

- Radiation pattern: quadrupole (no monopole/dipole radiation)

- Source: time-varying matter quadrupole moment


## Ground Truth Sources


- Book V Part III ch14 (Linear Einstein)


---

### `Tau.BookV.GravityField.LinearizedEinstein`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L71-L93)
**structure
Tau.BookV.GravityField.LinearizedEinstein :Type**


[V.D52] Linearized τ-Einstein equation: weak-field approximation
of R^H = κ_τ · T^mat.

In the weak-field regime, the curvature character is small
and the equation linearizes. This is the structural origin
of Newtonian gravity and the classical GR tests.

The perturbation order tracks the approximation level:


- order 0: flat (Minkowski)

- order 1: Newtonian + classical tests

- order 2+: post-Newtonian corrections


- order : ℕ
Perturbation order (1 = first order, 2 = second order, etc.).

- order_pos : self.order > 0
Order must be at least 1 (order 0 = flat, trivial).

- kappa : GravitationalCoupling
The gravitational coupling κ_τ used.

- chart_dim : ℕ
Chart dimension (must be 4).

- dim_is_four : self.chart_dim = 4
Chart is 4-dimensional.

Instances For

---

### `Tau.BookV.GravityField.instReprLinearizedEinstein`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L93-L93)
**instance
Tau.BookV.GravityField.instReprLinearizedEinstein :Repr LinearizedEinstein**

Equations
- Tau.BookV.GravityField.instReprLinearizedEinstein = { reprPrec := Tau.BookV.GravityField.instReprLinearizedEinstein.repr }

---

### `Tau.BookV.GravityField.instReprLinearizedEinstein.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L93-L93)
**def
Tau.BookV.GravityField.instReprLinearizedEinstein.repr :LinearizedEinstein → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.first_order_einstein`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L95-L101)
**def
Tau.BookV.GravityField.first_order_einstein :LinearizedEinstein**


First-order linearized Einstein with canonical κ_τ.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.GWPolarization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L107-L113)
**inductive
Tau.BookV.GravityField.GWPolarization :Type**


Gravitational wave polarization mode.

- Plus : GWPolarization
Plus (+) polarization from T² toroidal mode.

- Cross : GWPolarization
Cross (×) polarization from T² poloidal mode.

Instances For

---

### `Tau.BookV.GravityField.instReprGWPolarization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L113-L113)
**instance
Tau.BookV.GravityField.instReprGWPolarization :Repr GWPolarization**

Equations
- Tau.BookV.GravityField.instReprGWPolarization = { reprPrec := Tau.BookV.GravityField.instReprGWPolarization.repr }

---

### `Tau.BookV.GravityField.instReprGWPolarization.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L113-L113)
**def
Tau.BookV.GravityField.instReprGWPolarization.repr :GWPolarization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instDecidableEqGWPolarization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L113-L113)
**instance
Tau.BookV.GravityField.instDecidableEqGWPolarization :DecidableEq GWPolarization**

Equations
- Tau.BookV.GravityField.instDecidableEqGWPolarization x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.GravityField.instBEqGWPolarization.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L113-L113)
**def
Tau.BookV.GravityField.instBEqGWPolarization.beq :GWPolarization → GWPolarization → Bool**

Equations
- Tau.BookV.GravityField.instBEqGWPolarization.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.GravityField.instBEqGWPolarization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L113-L113)
**instance
Tau.BookV.GravityField.instBEqGWPolarization :BEq GWPolarization**

Equations
- Tau.BookV.GravityField.instBEqGWPolarization = { beq := Tau.BookV.GravityField.instBEqGWPolarization.beq }

---

### `Tau.BookV.GravityField.RadiationPattern`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L115-L123)
**inductive
Tau.BookV.GravityField.RadiationPattern :Type**


Radiation pattern order (multipole).

- Monopole : RadiationPattern
Monopole (ℓ=0): forbidden for GW.

- Dipole : RadiationPattern
Dipole (ℓ=1): forbidden for GW (momentum conservation).

- Quadrupole : RadiationPattern
Quadrupole (ℓ=2): leading GW radiation order.

Instances For

---

### `Tau.BookV.GravityField.instReprRadiationPattern`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L123-L123)
**instance
Tau.BookV.GravityField.instReprRadiationPattern :Repr RadiationPattern**

Equations
- Tau.BookV.GravityField.instReprRadiationPattern = { reprPrec := Tau.BookV.GravityField.instReprRadiationPattern.repr }

---

### `Tau.BookV.GravityField.instReprRadiationPattern.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L123-L123)
**def
Tau.BookV.GravityField.instReprRadiationPattern.repr :RadiationPattern → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instDecidableEqRadiationPattern`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L123-L123)
**instance
Tau.BookV.GravityField.instDecidableEqRadiationPattern :DecidableEq RadiationPattern**

Equations
- Tau.BookV.GravityField.instDecidableEqRadiationPattern x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.GravityField.instBEqRadiationPattern`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L123-L123)
**instance
Tau.BookV.GravityField.instBEqRadiationPattern :BEq RadiationPattern**

Equations
- Tau.BookV.GravityField.instBEqRadiationPattern = { beq := Tau.BookV.GravityField.instBEqRadiationPattern.beq }

---

### `Tau.BookV.GravityField.instBEqRadiationPattern.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L123-L123)
**def
Tau.BookV.GravityField.instBEqRadiationPattern.beq :RadiationPattern → RadiationPattern → Bool**

Equations
- Tau.BookV.GravityField.instBEqRadiationPattern.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.GravityField.GravitationalWave`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L125-L150)
**structure
Tau.BookV.GravityField.GravitationalWave :Type**


[V.D53] Gravitational wave: propagating solution of the
linearized τ-Einstein equation.

Properties determined by τ³ structure:


- Speed: c (null propagation, from base circle τ¹)

- Polarizations: 2 (plus + cross, from fiber T²)

- Leading multipole: quadrupole (ℓ = 2)

- Spin: 2 (from tensor structure of h_μν perturbation)


- speed_is_c : Bool
Propagation speed is c (light speed).

- speed_proof : self.speed_is_c = true
Must propagate at c.

- polarization_count : ℕ
Number of polarization modes.

- two_polarizations : self.polarization_count = 2
Exactly 2 polarizations.

- leading_multipole : RadiationPattern
Leading radiation pattern.

- is_quadrupole : self.leading_multipole = RadiationPattern.Quadrupole
Leading order is quadrupole.

- spin : ℕ
Spin of the gravitational wave (= 2).

- spin_is_two : self.spin = 2
Spin is 2.

Instances For

---

### `Tau.BookV.GravityField.instReprGravitationalWave`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L150-L150)
**instance
Tau.BookV.GravityField.instReprGravitationalWave :Repr GravitationalWave**

Equations
- Tau.BookV.GravityField.instReprGravitationalWave = { reprPrec := Tau.BookV.GravityField.instReprGravitationalWave.repr }

---

### `Tau.BookV.GravityField.instReprGravitationalWave.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L150-L150)
**def
Tau.BookV.GravityField.instReprGravitationalWave.repr :GravitationalWave → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.canonical_gw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L152-L161)
**def
Tau.BookV.GravityField.canonical_gw :GravitationalWave**


The canonical gravitational wave.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.ClassicalTestResult`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L167-L179)
**structure
Tau.BookV.GravityField.ClassicalTestResult :Type**


Classical GR test result: a predicted value with units.

- name : String
Test name.

- value_numer : ℕ
Predicted value numerator (scaled).

- value_denom : ℕ
Predicted value denominator.

- denom_pos : self.value_denom > 0
Denominator positive.

- unit : String
Unit description.

Instances For

---

### `Tau.BookV.GravityField.instReprClassicalTestResult.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L179-L179)
**def
Tau.BookV.GravityField.instReprClassicalTestResult.repr :ClassicalTestResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprClassicalTestResult`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L179-L179)
**instance
Tau.BookV.GravityField.instReprClassicalTestResult :Repr ClassicalTestResult**

Equations
- Tau.BookV.GravityField.instReprClassicalTestResult = { reprPrec := Tau.BookV.GravityField.instReprClassicalTestResult.repr }

---

### `Tau.BookV.GravityField.mercury_precession_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L181-L187)
**def
Tau.BookV.GravityField.mercury_precession_value :ClassicalTestResult**


Mercury perihelion precession: 43 arcsec/century.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.light_deflection_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L189-L195)
**def
Tau.BookV.GravityField.light_deflection_value :ClassicalTestResult**


Light deflection at solar limb: 1.75 arcsec.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.grav_redshift_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L197-L203)
**def
Tau.BookV.GravityField.grav_redshift_value :ClassicalTestResult**


Gravitational redshift: Δf/f = GM/(rc²).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.newtonian_recovery`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L209-L218)
**theorem
Tau.BookV.GravityField.newtonian_recovery :first_order_einstein.order = 1 ∧ first_order_einstein.kappa.kappa_numer = BookIV.Sectors.iotaD - BookIV.Sectors.iota**


[V.T28] The static, weak-field limit of the linearized τ-Einstein
equation recovers Newtonian gravity: F = -GMm/r².

This follows from the chart readout of the first-order
linearized equation with static matter distribution.
The coupling κ_τ maps to 8πG/c⁴ under readout.

---

### `Tau.BookV.GravityField.mercury_precession`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L224-L233)
**theorem
Tau.BookV.GravityField.mercury_precession :mercury_precession_value.value_numer = 43 ∧ mercury_precession_value.value_denom = 1**


[V.T29] Mercury perihelion precession: 43 arcsec/century.

The anomalous perihelion advance of Mercury is predicted by the
first post-Newtonian correction from the linearized τ-Einstein
equation. The value matches GR exactly (same equation under
chart readout). No free parameters.

---

### `Tau.BookV.GravityField.light_deflection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L239-L247)
**theorem
Tau.BookV.GravityField.light_deflection :light_deflection_value.value_numer = 175 ∧ light_deflection_value.value_denom = 100**


[V.T30] Light deflection: 1.75 arcsec at the solar limb.

A null intertwiner (photon) passing near a massive body is
deflected by the curvature character. The deflection angle
at the solar limb is 1.75 arcsec (= 4GM/(rc²)).

---

### `Tau.BookV.GravityField.grav_redshift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L253-L259)
**theorem
Tau.BookV.GravityField.grav_redshift :grav_redshift_value.name = "Gravitational redshift"**


[V.T31] Gravitational redshift: Δf/f = GM/(rc²).

A null intertwiner (photon) climbing out of a gravitational
potential well loses energy, shifting to lower frequency.
The fractional frequency shift equals GM/(rc²).

---

### `Tau.BookV.GravityField.grav_wave_properties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L265-L275)
**theorem
Tau.BookV.GravityField.grav_wave_properties :canonical_gw.speed_is_c = true ∧ canonical_gw.polarization_count = 2 ∧ canonical_gw.leading_multipole = RadiationPattern.Quadrupole ∧ canonical_gw.spin = 2**


[V.T32] Gravitational wave properties:


- Speed: c (null propagation)

- Polarizations: 2 (plus + cross from T²)

- Leading multipole: quadrupole (ℓ = 2)

- Spin: 2


---

### `Tau.BookV.GravityField.grav_wave_speed_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LinearEinstein.lean#L281-L288)
**theorem
Tau.BookV.GravityField.grav_wave_speed_c
(gw : GravitationalWave)
 :gw.speed_is_c = true**


[V.P14] Gravitational waves propagate at c.

GW speed = c follows from null propagation on the base circle τ¹.
The gravitational wave is a perturbation of the D-sector boundary
character, and perturbations propagate at the null transport rate.
Confirmed by LIGO/Virgo GW170817 + GRB 170817A (|Δc/c| < 10⁻¹⁵).
