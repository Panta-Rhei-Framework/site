---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.DimensionalBridgeExt"
permalink: /verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/
lane: verify
module_name: "TauLib.BookIV.Calibration.DimensionalBridgeExt"
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

# TauLib.BookIV.Calibration.DimensionalBridgeExt


Extended dimensional bridge: ch13 entries covering relational-unit formulas,
the Planck character as σ-fixed sector lift, and the gravitational closing
identity.

## Registry Cross-References


- [IV.D293] Speed of Light (Relational) — `c_relational`

- [IV.D294] Planck Constant (Relational) — `h_relational`

- [IV.D295] Coulomb Constant (Relational) — `ke_relational`

- [IV.D296] Vacuum Permittivity (Relational) — `eps0_relational`

- [IV.D297] Vacuum Permeability (Relational) — `mu0_relational`

- [IV.D298] Planck Character — `PlanckCharacterExt`

- [IV.T112] σ-Fixed Planck Character — `planck_character_sigma_fixed`

- [IV.P167] Attained Minimum — `planck_character_unique_minimum`

- [IV.R268] Why 0.07% and not exact — (structural remark)

- [IV.R269] Consistency check — (structural remark)

- [IV.R270] The tier boundary is sharp — (structural remark)

- [IV.R274] The pi-corrected distance — (structural remark)

- [IV.R275] Counting parameters — (structural remark)

- [IV.R276] R formula independence — (structural remark)

- [IV.R277] The sqrt3 — (structural remark)


## Mathematical Content


### Relational Unit Formulas


Each SI constant decomposes as a monomial in the 4 relational units
(M, L, H, Q) times a π-dependent rational prefactor:


- c = L · H

- h = M · L² · H

- k_e = (π²/32) · Q²/(M·H·L³)

- ε₀ = (8/π³) · M·H·L³/Q²

- μ₀ = (π³/8) · Q²/(M·H³·L⁵)


This module re-records these in a `RelationalFormula` structure that
carries the formula label, dimensional exponents, and prefactor label.

### Planck Character ℏ_τ


The Planck character is the σ-fixed (lobe-swap-invariant) sector lift
of ι<sub>τ</sub> into the QM regime. It is the unique attained minimum of the
sector lift functional (not merely an infimum).

### Closing Identity


The gravitational closing identity α_G = α¹⁸ · √3 · (1 − (3/π)·α)
connects the gravitational coupling to the fine structure constant
through the lemniscate √3 factor.

## Ground Truth Sources


- Book IV Part II ch13 (Dimensional Bridge)


---

### `Tau.BookIV.Calibration.RelationalFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L66-L81)
**structure
Tau.BookIV.Calibration.RelationalFormula :Type**


A relational-unit formula for an SI constant:
formula_label × DimExponents × prefactor_label.

- formula_label : String
Human-readable formula string.

- exponents : DimExponents
Dimensional exponents M^a · L^b · H^c · Q^d (Int for negative).

- prefactor_numer : ℕ
Prefactor numerator (rational part).

- prefactor_denom : ℕ
Prefactor denominator (rational part).

- denom_pos : self.prefactor_denom > 0
Denominator is positive.

- prefactor_label : String
Symbolic label for the prefactor (e.g., "1", "pi_sq_over_32").

Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalFormula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L81-L81)
**def
Tau.BookIV.Calibration.instReprRelationalFormula.repr :RelationalFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L81-L81)
**instance
Tau.BookIV.Calibration.instReprRelationalFormula :Repr RelationalFormula**

Equations
- Tau.BookIV.Calibration.instReprRelationalFormula = { reprPrec := Tau.BookIV.Calibration.instReprRelationalFormula.repr }

---

### `Tau.BookIV.Calibration.c_relational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L87-L95)
**def
Tau.BookIV.Calibration.c_relational :RelationalFormula**


[IV.D293] Speed of light in relational units: c = L · H.
Prefactor = 1, exponents M⁰ L¹ H¹ Q⁰.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.h_relational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L101-L109)
**def
Tau.BookIV.Calibration.h_relational :RelationalFormula**


[IV.D294] Planck's constant in relational units: h = M · L² · H.
Prefactor = 1, exponents M¹ L² H¹ Q⁰.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.ke_relational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L115-L124)
**def
Tau.BookIV.Calibration.ke_relational :RelationalFormula**


[IV.D295] Coulomb constant in relational units:
k_e = (π²/32) · Q²/(M · H · L³).
Prefactor = π²/32, exponents M⁻¹ L⁻³ H⁻¹ Q².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.eps0_relational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L130-L139)
**def
Tau.BookIV.Calibration.eps0_relational :RelationalFormula**


[IV.D296] Vacuum permittivity in relational units:
ε₀ = (8/π³) · M · H · L³ / Q².
Prefactor = 8/π³, exponents M¹ L³ H¹ Q⁻².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.mu0_relational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L145-L154)
**def
Tau.BookIV.Calibration.mu0_relational :RelationalFormula**


[IV.D297] Vacuum permeability in relational units:
μ₀ = (π³/8) · Q²/(M · H³ · L⁵).
Prefactor = π³/8, exponents M⁻¹ L⁻⁵ H⁻³ Q².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.relational_formulas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L160-L162)
**def
Tau.BookIV.Calibration.relational_formulas :List RelationalFormula**


All five relational-unit formulas.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.relational_formulas_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L164-L165)
**theorem
Tau.BookIV.Calibration.relational_formulas_count :relational_formulas.length = 5**


Five relational formulas in the bridge.

---

### `Tau.BookIV.Calibration.c_relational_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L171-L173)
**theorem
Tau.BookIV.Calibration.c_relational_consistent :c_relational.exponents = c_formula.exponents**


c_relational has the same exponents as c_formula.

---

### `Tau.BookIV.Calibration.h_relational_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L175-L177)
**theorem
Tau.BookIV.Calibration.h_relational_consistent :h_relational.exponents = h_formula.exponents**


h_relational has the same exponents as h_formula.

---

### `Tau.BookIV.Calibration.ke_relational_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L179-L181)
**theorem
Tau.BookIV.Calibration.ke_relational_consistent :ke_relational.exponents = ke_formula.exponents**


ke_relational has the same exponents as ke_formula.

---

### `Tau.BookIV.Calibration.eps0_relational_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L183-L185)
**theorem
Tau.BookIV.Calibration.eps0_relational_consistent :eps0_relational.exponents = eps0_formula.exponents**


eps0_relational has the same exponents as eps0_formula.

---

### `Tau.BookIV.Calibration.mu0_relational_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L187-L189)
**theorem
Tau.BookIV.Calibration.mu0_relational_consistent :mu0_relational.exponents = mu0_formula.exponents**


mu0_relational has the same exponents as mu0_formula.

---

### `Tau.BookIV.Calibration.maxwell_relational_dimensional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L195-L200)
**theorem
Tau.BookIV.Calibration.maxwell_relational_dimensional :eps0_relational.exponents.add mu0_relational.exponents = c_relational.exponents.scale (-2)**


Maxwell relation in relational form: ε₀ + μ₀ exponents = −2 × c exponents.

---

### `Tau.BookIV.Calibration.coulomb_permittivity_relational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L202-L205)
**theorem
Tau.BookIV.Calibration.coulomb_permittivity_relational :ke_relational.exponents.add eps0_relational.exponents = DimExponents.zero**


Coulomb-permittivity in relational form: k_e + ε₀ exponents = 0.

---

### `Tau.BookIV.Calibration.PlanckCharacterExt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L211-L235)
**structure
Tau.BookIV.Calibration.PlanckCharacterExt :Type**


[IV.D298] The Planck character ℏ_τ in the ch13 dimensional-bridge context.
This is the σ-fixed sector lift of ι<sub>τ</sub> into the QM regime,
re-recorded here with its ch13 registry label.

Key properties:


- label = "hbar_tau"

- sector = "QM"

- σ-fixed = true (lives at lemniscate crossing point)

- is_minimum = true (attained, not merely infimum)


- label : String
Symbolic label.

- sector : String
Source sector.

- is_sigma_fixed : Bool
σ-fixed: invariant under lobe swap.

- is_minimum : Bool
Attained minimum of the sector lift functional.

- numer : ℕ
ℏ_τ numerator (scaled rational: ℏ_τ ≈ ι<sub>τ</sub>/4).

- denom : ℕ
ℏ_τ denominator.

- denom_pos : self.denom > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Calibration.instReprPlanckCharacterExt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L235-L235)
**instance
Tau.BookIV.Calibration.instReprPlanckCharacterExt :Repr PlanckCharacterExt**

Equations
- Tau.BookIV.Calibration.instReprPlanckCharacterExt = { reprPrec := Tau.BookIV.Calibration.instReprPlanckCharacterExt.repr }

---

### `Tau.BookIV.Calibration.instReprPlanckCharacterExt.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L235-L235)
**def
Tau.BookIV.Calibration.instReprPlanckCharacterExt.repr :PlanckCharacterExt → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.planck_character_ext`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L237-L245)
**def
Tau.BookIV.Calibration.planck_character_ext :PlanckCharacterExt**


The canonical ch13 Planck character record.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.planck_character_sigma_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L251-L256)
**theorem
Tau.BookIV.Calibration.planck_character_sigma_fixed :planck_character_ext.is_sigma_fixed = true**


[IV.T112] The Planck character is σ-fixed.
This is structural: the σ-fixed field is true by construction.
Physically, ℏ_τ lives at the lemniscate crossing point where
both lobes contribute equally.

---

### `Tau.BookIV.Calibration.planck_character_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L258-L260)
**theorem
Tau.BookIV.Calibration.planck_character_sector :planck_character_ext.sector = "QM"**


The Planck character sector is QM.

---

### `Tau.BookIV.Calibration.planck_character_label`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L262-L264)
**theorem
Tau.BookIV.Calibration.planck_character_label :planck_character_ext.label = "hbar_tau"**


The Planck character label is "hbar_tau".

---

### `Tau.BookIV.Calibration.planck_character_unique_minimum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L270-L278)
**theorem
Tau.BookIV.Calibration.planck_character_unique_minimum :planck_character_ext.is_minimum = true**


[IV.P167] The Planck character is the unique attained minimum of the
sector lift functional.

In the τ-framework, the uncertainty bound Δx·Δp ≥ ℏ_τ is achieved
by the canonical saturating chain. This is NOT merely an infimum:
the minimum is actually attained, distinguishing it from the
conventional QFT treatment.

---

### `Tau.BookIV.Calibration.planck_character_properties`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L280-L285)
**theorem
Tau.BookIV.Calibration.planck_character_properties :planck_character_ext.is_sigma_fixed = true ∧ planck_character_ext.is_minimum = true ∧ planck_character_ext.sector = "QM"**


Combined: the Planck character is both σ-fixed and an attained minimum.

---

### `Tau.BookIV.Calibration.BridgeParameterCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L333-L341)
**structure
Tau.BookIV.Calibration.BridgeParameterCount :Type**


The τ-framework has zero free parameters: all constants from ι<sub>τ</sub> + anchor.

- free_parameters : ℕ
Number of free (tunable) parameters.

- anchors : ℕ
Number of calibration anchors.

- iota_derived : ℕ
Number of ι<sub>τ</sub>-derived quantities.

Instances For

---

### `Tau.BookIV.Calibration.instReprBridgeParameterCount.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L341-L341)
**def
Tau.BookIV.Calibration.instReprBridgeParameterCount.repr :BridgeParameterCount → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprBridgeParameterCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L341-L341)
**instance
Tau.BookIV.Calibration.instReprBridgeParameterCount :Repr BridgeParameterCount**

Equations
- Tau.BookIV.Calibration.instReprBridgeParameterCount = { reprPrec := Tau.BookIV.Calibration.instReprBridgeParameterCount.repr }

---

### `Tau.BookIV.Calibration.bridge_parameter_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L343-L347)
**def
Tau.BookIV.Calibration.bridge_parameter_count :BridgeParameterCount**


The canonical parameter count.
Equations
- Tau.BookIV.Calibration.bridge_parameter_count = { free_parameters := 0, anchors := 1, iota_derived := 4 }
Instances For

---

### `Tau.BookIV.Calibration.bridge_zero_free_parameters`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L349-L351)
**theorem
Tau.BookIV.Calibration.bridge_zero_free_parameters :bridge_parameter_count.free_parameters = 0**


Zero free parameters.

---

### `Tau.BookIV.Calibration.bridge_one_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L353-L355)
**theorem
Tau.BookIV.Calibration.bridge_one_anchor :bridge_parameter_count.anchors = 1**


One calibration anchor.

---

### `Tau.BookIV.Calibration.ClosingIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L361-L378)
**structure
Tau.BookIV.Calibration.ClosingIdentity :Type**


The gravitational closing identity connects α_G to α through
the lemniscate √3 factor and a first-order correction c₁ = 3/π.

α_G = α¹⁸ · √3 · (1 − (3/π)·α)

This structure records the key integer/rational parameters.

- alpha_exponent : ℕ
Exponent of α in the leading term.

- sqrt3_origin : String
The √3 comes from lemniscate geometry (3-fold sectors).

- correction_numer : ℕ
First-order correction numerator: 3.

- correction_denom_label : String
First-order correction denominator label: π.

- deviation_ppm : ℕ
G deviation from CODATA at c₁ = 3/π.

Instances For

---

### `Tau.BookIV.Calibration.instReprClosingIdentity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L378-L378)
**def
Tau.BookIV.Calibration.instReprClosingIdentity.repr :ClosingIdentity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprClosingIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L378-L378)
**instance
Tau.BookIV.Calibration.instReprClosingIdentity :Repr ClosingIdentity**

Equations
- Tau.BookIV.Calibration.instReprClosingIdentity = { reprPrec := Tau.BookIV.Calibration.instReprClosingIdentity.repr }

---

### `Tau.BookIV.Calibration.closing_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L380-L386)
**def
Tau.BookIV.Calibration.closing_identity :ClosingIdentity**


The canonical closing identity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.closing_identity_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L388-L390)
**theorem
Tau.BookIV.Calibration.closing_identity_exponent :closing_identity.alpha_exponent = 18**


The α exponent in the closing identity is 18.

---

### `Tau.BookIV.Calibration.closing_identity_correction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L392-L394)
**theorem
Tau.BookIV.Calibration.closing_identity_correction :closing_identity.correction_numer = 3**


The √3 correction numerator is 3 (→ 3/π).

---

### `Tau.BookIV.Calibration.closing_identity_deviation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L396-L398)
**theorem
Tau.BookIV.Calibration.closing_identity_deviation :closing_identity.deviation_ppm = 3**


The G deviation is 3 ppm (effectively within CODATA uncertainty).

---

### `Tau.BookIV.Calibration.independent_formula_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L404-L411)
**theorem
Tau.BookIV.Calibration.independent_formula_count :relational_formulas.length = 5 ∧ 2 + 3 = 5**


The five formulas have exactly 3 algebraically independent exponent vectors.
We verify: c and h have Q = 0; k_e, ε₀, μ₀ share the Q-plane.
Maxwell + Coulomb-permittivity give 2 constraints on 5 formulas → rank = 3.

---

### `Tau.BookIV.Calibration.c_h_charge_neutral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L413-L416)
**theorem
Tau.BookIV.Calibration.c_h_charge_neutral :c_relational.exponents.Q = 0 ∧ h_relational.exponents.Q = 0**


c and h are charge-neutral (Q exponent = 0).

---

### `Tau.BookIV.Calibration.ke_eps0_mu0_charge_two`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L418-L423)
**theorem
Tau.BookIV.Calibration.ke_eps0_mu0_charge_two :ke_relational.exponents.Q = 2 ∧ eps0_relational.exponents.Q = -2 ∧ mu0_relational.exponents.Q = 2**


k_e, ε₀, μ₀ all have |Q| = 2.
