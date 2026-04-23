---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.DimensionalBridge"
permalink: /verify/taulib/docs/book-iv-calibration-dimensional-bridge/
lane: verify
module_name: "TauLib.BookIV.Calibration.DimensionalBridge"
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

# TauLib.BookIV.Calibration.DimensionalBridge


The derivation chain from τ-native relational scales to SI physical constants.

## Registry Cross-References


- [IV.D32] Tau Physical Scale — `TauPhysicalScale`

- [IV.D33] Speed of Light — `c_formula`

- [IV.D34] Planck Constant — `h_formula`

- [IV.D35] Coulomb Constant — `ke_formula`

- [IV.D36] Vacuum Permittivity — `eps0_formula`

- [IV.D37] Vacuum Permeability — `mu0_formula`

- [IV.T07] Maxwell Relation — `maxwell_dimensional`, `maxwell_prefactor`

- [IV.T08] Coulomb-Permittivity — `coulomb_permittivity_dimensional`, `coulomb_permittivity_prefactor`

- [IV.R08] G Frontier — `GravityFrontier`


## Mathematical Content


### Dimensional Formulas


Every SI constant is a product of:

- A rational coefficient (integer numerator/denominator)

- A power of π

- A monomial in the four τ-scales M, L, H, Q


The five key derived constants:


- c = L · H (speed of light)

- h = M · L² · H (Planck constant)

- k_e = (π²/32) · Q² / (M · H · L³) (Coulomb constant)

- ε₀ = (8/π³) · M · H · L³ / Q² (vacuum permittivity)

- μ₀ = (π³/8) · Q² / (M · H³ · L⁵) (vacuum permeability)


### Structural Identities (provable algebraically)


- 
**Maxwell relation**: c² = 1/(ε₀ · μ₀)


- Dimensional: ε₀ + μ₀ exponents = (0, −2, −2, 0) = −2 × c exponents

- Prefactors: (8/π³) × (π³/8) = 1


- 
**Coulomb-permittivity**: k_e = 1/(4π · ε₀)


- Dimensional: k_e + ε₀ exponents = (0, 0, 0, 0)

- Prefactors: (π²/32) × (8/π³) × 4π = 1


### Three-Tier SI Classification


- Tier I (Structural): c, ℏ — appear in every sector

- Tier II (Physical): e, k_B — sector-specific

- Tier III (Conventional): N_A, Δν_Cs, K_cd — human-scale


## Ground Truth Sources


- Book IV Part II ch13 (Dimensional Bridge)

- SI 2019 defining constants


---

### `Tau.BookIV.Calibration.DimExponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L63-L69)
**structure
Tau.BookIV.Calibration.DimExponents :Type**


[IV.D32] Dimensional exponent vector: M^a · L^b · H^c · Q^d.

- M : ℤ
- L : ℤ
- H : ℤ
- Q : ℤ
Instances For

---

### `Tau.BookIV.Calibration.instReprDimExponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L69-L69)
**instance
Tau.BookIV.Calibration.instReprDimExponents :Repr DimExponents**

Equations
- Tau.BookIV.Calibration.instReprDimExponents = { reprPrec := Tau.BookIV.Calibration.instReprDimExponents.repr }

---

### `Tau.BookIV.Calibration.instReprDimExponents.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L69-L69)
**def
Tau.BookIV.Calibration.instReprDimExponents.repr :DimExponents → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqDimExponents.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L69-L69)
**def
Tau.BookIV.Calibration.instDecidableEqDimExponents.decEq
(x✝ x✝¹ : DimExponents)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqDimExponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L69-L69)
**instance
Tau.BookIV.Calibration.instDecidableEqDimExponents :DecidableEq DimExponents**

Equations
- Tau.BookIV.Calibration.instDecidableEqDimExponents = Tau.BookIV.Calibration.instDecidableEqDimExponents.decEq

---

### `Tau.BookIV.Calibration.DimExponents.add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L71-L73)
**def
Tau.BookIV.Calibration.DimExponents.add
(a b : DimExponents)
 :DimExponents**


Add two exponent vectors (= multiply the dimensional quantities).
Equations
- a.add b = { M := a.M + b.M, L := a.L + b.L, H := a.H + b.H, Q := a.Q + b.Q }
Instances For

---

### `Tau.BookIV.Calibration.DimExponents.scale`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L75-L77)
**def
Tau.BookIV.Calibration.DimExponents.scale
(a : DimExponents)

(n : ℤ)
 :DimExponents**


Scale an exponent vector by an integer (= raise to a power).
Equations
- a.scale n = { M := n * a.M, L := n * a.L, H := n * a.H, Q := n * a.Q }
Instances For

---

### `Tau.BookIV.Calibration.DimExponents.zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L79-L80)
**def
Tau.BookIV.Calibration.DimExponents.zero :DimExponents**


The zero exponent vector (dimensionless).
Equations
- Tau.BookIV.Calibration.DimExponents.zero = { M := 0, L := 0, H := 0, Q := 0 }
Instances For

---

### `Tau.BookIV.Calibration.DimensionalFormula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L86-L102)
**structure
Tau.BookIV.Calibration.DimensionalFormula :Type**


A dimensional formula: coeff × π^p × M^a L^b H^c Q^d.
Every SI constant in the τ-framework decomposes uniquely
into this form.

- name : String
Name of the constant.

- coeff_numer : ℕ
Rational coefficient numerator.

- coeff_denom : ℕ
Rational coefficient denominator.

- denom_pos : self.coeff_denom > 0
Denominator is positive.

- pi_power : ℤ
Power of π in the prefactor.

- exponents : DimExponents
Dimensional exponents.

Instances For

---

### `Tau.BookIV.Calibration.instReprDimensionalFormula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L102-L102)
**instance
Tau.BookIV.Calibration.instReprDimensionalFormula :Repr DimensionalFormula**

Equations
- Tau.BookIV.Calibration.instReprDimensionalFormula = { reprPrec := Tau.BookIV.Calibration.instReprDimensionalFormula.repr }

---

### `Tau.BookIV.Calibration.instReprDimensionalFormula.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L102-L102)
**def
Tau.BookIV.Calibration.instReprDimensionalFormula.repr :DimensionalFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.c_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L108-L116)
**def
Tau.BookIV.Calibration.c_formula :DimensionalFormula**


[IV.D33] Speed of light: c = L · H.
Coefficient: 1, π⁰, dimensions: L¹ H¹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.h_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L118-L126)
**def
Tau.BookIV.Calibration.h_formula :DimensionalFormula**


[IV.D34] Planck constant: h = M · L² · H.
Coefficient: 1, π⁰, dimensions: M¹ L² H¹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.ke_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L128-L136)
**def
Tau.BookIV.Calibration.ke_formula :DimensionalFormula**


[IV.D35] Coulomb constant: k_e = (π²/32) · Q²/(M · H · L³).
Coefficient: 1/32, π², dimensions: M⁻¹ L⁻³ H⁻¹ Q².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.eps0_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L138-L146)
**def
Tau.BookIV.Calibration.eps0_formula :DimensionalFormula**


[IV.D36] Vacuum permittivity: ε₀ = (8/π³) · M · H · L³ / Q².
Coefficient: 8, π⁻³, dimensions: M¹ L³ H¹ Q⁻².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.mu0_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L148-L156)
**def
Tau.BookIV.Calibration.mu0_formula :DimensionalFormula**


[IV.D37] Vacuum permeability: μ₀ = (π³/8) · Q²/(M · H³ · L⁵).
Coefficient: 1/8, π³, dimensions: M⁻¹ L⁻⁵ H⁻³ Q².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.derivation_chain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L158-L160)
**def
Tau.BookIV.Calibration.derivation_chain :List DimensionalFormula**


All five derivation chain formulas.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.derivation_chain_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L162-L163)
**theorem
Tau.BookIV.Calibration.derivation_chain_count :derivation_chain.length = 5**


Five formulas in the derivation chain.

---

### `Tau.BookIV.Calibration.maxwell_dimensional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L169-L176)
**theorem
Tau.BookIV.Calibration.maxwell_dimensional :eps0_formula.exponents.add mu0_formula.exponents = c_formula.exponents.scale (-2)**


[IV.T07] Maxwell relation (dimensional part):
ε₀ · μ₀ exponents sum to −2 × c exponents.
This means ε₀ · μ₀ = (prefactor) / c², i.e. c² = prefactor / (ε₀ · μ₀).

---

### `Tau.BookIV.Calibration.maxwell_prefactor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L178-L186)
**theorem
Tau.BookIV.Calibration.maxwell_prefactor :eps0_formula.coeff_numer * mu0_formula.coeff_numer = eps0_formula.coeff_denom * mu0_formula.coeff_denom ∧ eps0_formula.pi_power + mu0_formula.pi_power = 0**


[IV.T07] Maxwell relation (prefactor part):
The π-prefactors cancel: (8/1 · π⁻³) × (1/8 · π³) = 1.


- Coefficient product: 8 × 1 = 1 × 8 (both = 8)

- π exponent sum: (−3) + 3 = 0


---

### `Tau.BookIV.Calibration.maxwell_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L188-L200)
**theorem
Tau.BookIV.Calibration.maxwell_complete :(c_formula.exponents.scale 2).add (eps0_formula.exponents.add mu0_formula.exponents) = DimExponents.zero ∧ 2 * c_formula.pi_power + eps0_formula.pi_power + mu0_formula.pi_power = 0**


Complete Maxwell relation: c² = 1/(ε₀ · μ₀).
Both dimensional and prefactor parts combine to give
c² · ε₀ · μ₀ = 1 (dimensionless, coefficient = 1).

---

### `Tau.BookIV.Calibration.coulomb_permittivity_dimensional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L206-L211)
**theorem
Tau.BookIV.Calibration.coulomb_permittivity_dimensional :ke_formula.exponents.add eps0_formula.exponents = DimExponents.zero**


[IV.T08] Coulomb-permittivity (dimensional part):
k_e · ε₀ exponents sum to zero (dimensionless product).
This is the dimensional content of k_e = 1/(4π · ε₀).

---

### `Tau.BookIV.Calibration.coulomb_permittivity_prefactor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L213-L227)
**theorem
Tau.BookIV.Calibration.coulomb_permittivity_prefactor :ke_formula.coeff_numer * eps0_formula.coeff_numer * 4 = ke_formula.coeff_denom * eps0_formula.coeff_denom * 1 ∧ ke_formula.pi_power + eps0_formula.pi_power + 1 = 0**


[IV.T08] Coulomb-permittivity (prefactor part):
k_e · 4π · ε₀ = 1.


- Coefficients: (1/32) × 4 × (8/1) = 32/32 = 1

- π powers: 2 + 1 + (−3) = 0


Cross-multiplied: coeff_numer_product × denom_product = coeff_denom_product × numer_product
k_e: 1/32, ε₀: 8/1, factor 4: 4/1
Product numerators: 1 × 8 × 4 = 32
Product denominators: 32 × 1 × 1 = 32
So 32 = 32 ✓

---

### `Tau.BookIV.Calibration.SITier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L233-L238)
**inductive
Tau.BookIV.Calibration.SITier :Type**


Three-tier classification of SI constants by structural role.

- Structural : SITier
- Physical : SITier
- Conventional : SITier
Instances For

---

### `Tau.BookIV.Calibration.instReprSITier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L238-L238)
**def
Tau.BookIV.Calibration.instReprSITier.repr :SITier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprSITier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L238-L238)
**instance
Tau.BookIV.Calibration.instReprSITier :Repr SITier**

Equations
- Tau.BookIV.Calibration.instReprSITier = { reprPrec := Tau.BookIV.Calibration.instReprSITier.repr }

---

### `Tau.BookIV.Calibration.instDecidableEqSITier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L238-L238)
**instance
Tau.BookIV.Calibration.instDecidableEqSITier :DecidableEq SITier**

Equations
- Tau.BookIV.Calibration.instDecidableEqSITier x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Calibration.TieredConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L240-L244)
**structure
Tau.BookIV.Calibration.TieredConstant :Type**


SI constant with tier assignment.

- constant : SIConstant
- tier : SITier
Instances For

---

### `Tau.BookIV.Calibration.instReprTieredConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L244-L244)
**instance
Tau.BookIV.Calibration.instReprTieredConstant :Repr TieredConstant**

Equations
- Tau.BookIV.Calibration.instReprTieredConstant = { reprPrec := Tau.BookIV.Calibration.instReprTieredConstant.repr }

---

### `Tau.BookIV.Calibration.instReprTieredConstant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L244-L244)
**def
Tau.BookIV.Calibration.instReprTieredConstant.repr :TieredConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.tiered_exact_constants`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L246-L252)
**def
Tau.BookIV.Calibration.tiered_exact_constants :List TieredConstant**


The four structurally relevant exact constants, tiered.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.tiered_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L254-L257)
**theorem
Tau.BookIV.Calibration.tiered_count :(List.filter (fun (x : TieredConstant) => x.tier == SITier.Structural) tiered_exact_constants).length = 2 ∧ (List.filter (fun (x : TieredConstant) => x.tier == SITier.Physical) tiered_exact_constants).length = 2**


Two structural + two physical tier-I/II constants.

---

### `Tau.BookIV.Calibration.GravityFrontier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L263-L279)
**structure
Tau.BookIV.Calibration.GravityFrontier :Type**


[IV.R08] The gravitational constant G is the remaining frontier.
Dimensional skeleton: G = C_D · L³ H² / M
where C_D is a base-sector geometric invariant derived in Book V.

G requires the D-sector base geometry (τ¹ curvature analysis)
which is outside Book IV's scope. We record the structural skeleton
and the SI target for future cross-reference.

- exponents : DimExponents
Dimensional exponents: M⁻¹ L³ H².

- coeff_label : String
The unknown base-sector coefficient (from Book V).

- si_target : SIConstant
SI target for comparison.

- deferred : Bool
This is deferred to Book V.

Instances For

---

### `Tau.BookIV.Calibration.instReprGravityFrontier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L279-L279)
**def
Tau.BookIV.Calibration.instReprGravityFrontier.repr :GravityFrontier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprGravityFrontier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L279-L279)
**instance
Tau.BookIV.Calibration.instReprGravityFrontier :Repr GravityFrontier**

Equations
- Tau.BookIV.Calibration.instReprGravityFrontier = { reprPrec := Tau.BookIV.Calibration.instReprGravityFrontier.repr }

---

### `Tau.BookIV.Calibration.gravity_frontier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L281-L282)
**def
Tau.BookIV.Calibration.gravity_frontier :GravityFrontier**


The canonical G frontier record.
Equations
- Tau.BookIV.Calibration.gravity_frontier = { }
Instances For

---

### `Tau.BookIV.Calibration.g_is_deferred`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L284-L285)
**theorem
Tau.BookIV.Calibration.g_is_deferred :gravity_frontier.deferred = true**


G is deferred.

---

### `Tau.BookIV.Calibration.c_is_velocity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L291-L293)
**theorem
Tau.BookIV.Calibration.c_is_velocity :c_formula.exponents = { M := 0, L := 1, H := 1, Q := 0 }**


c is dimensionally velocity: [c] = L/T = L · H (since H = 1/T).

---

### `Tau.BookIV.Calibration.h_is_action`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L295-L297)
**theorem
Tau.BookIV.Calibration.h_is_action :h_formula.exponents = { M := 1, L := 2, H := 1, Q := 0 }**


h is dimensionally action: [h] = M · L² · T⁻¹ = M · L² · H.

---

### `Tau.BookIV.Calibration.eps0_mu0_inverse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L299-L303)
**theorem
Tau.BookIV.Calibration.eps0_mu0_inverse :eps0_formula.exponents.add mu0_formula.exponents = { M := 0, L := -2, H := -2, Q := 0 }**


ε₀ and μ₀ are dimensional inverses (up to c²).

---

### `Tau.BookIV.Calibration.ke_eps0_inverse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Calibration/DimensionalBridge.lean#L305-L309)
**theorem
Tau.BookIV.Calibration.ke_eps0_inverse :ke_formula.exponents.add eps0_formula.exponents = DimExponents.zero**


k_e and ε₀ are dimensional inverses (up to 4π).
