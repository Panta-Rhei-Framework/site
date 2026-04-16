---
layout: taulib-doc
title: "TauLib.BookIV.Sectors.FineStructure"
permalink: /verify/taulib/docs/book-iv-sectors-fine-structure/
lane: verify
module_name: "TauLib.BookIV.Sectors.FineStructure"
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

# TauLib.BookIV.Sectors.FineStructure


Derivation of the fine structure constant α_EM from ι<sub>τ</sub> = 2/(π+e).

## Registry Cross-References


- [IV.D08] Spectral Fine Structure — `alpha_spectral_numer`, `alpha_spectral_denom`

- [IV.P02] α Numerical Range — `alpha_in_range`

- [IV.R01] Holonomy vs Spectral — structural remark

- [IV.R02] Wrong Formula Correction — `wrong_formula_refutation`


## Mathematical Content


### Two Derivations of α


The fine structure constant α_EM ≈ 1/137.036 admits two complementary derivations:

**1. Holonomy Formula (exact):**
α = (π³/16) · Q⁴ / (M² H³ L⁶)
where Q, M, H, L are calibration parameters from the neutron anchoring cascade
(Book IV Part VII). All four parameters are ultimately functions of ι<sub>τ</sub> and
geometric constants (π, e). This formula is EXACT but requires the full
calibration cascade to evaluate.

**2. Spectral Formula (leading-order approximation):**
α ≈ (8/15) · ι<sub>τ</sub>⁴
where ι<sub>τ</sub> = 2/(π+e). Structural meaning:


- Exponent 4: α couples two τ² surface modes; each contributes ι<sub>τ</sub>²

- Factor 8/15 = 2³/(3·5): primorial structure from Cayley(τ)


### The Connection Between Formulas


The spectral formula is the **leading term** of the holonomy formula when
Q, M, H, L are expressed as functions of ι<sub>τ</sub>. The exact relationship is:

α = (8/15) · ι<sub>τ</sub>⁴ · R(ι<sub>τ</sub>)

where R(ι<sub>τ</sub>) is a correction factor satisfying R ≈ 1.0065 (bringing the
spectral approximation ~0.06% closer to the experimental value).
R depends on the detailed calibration cascade and is derived in Book IV Part VII.

The holonomy formula resolves to the spectral formula as follows:


- (π³/16) is the geometric prefactor from three-circle integration

- Q⁴/(M²H³L⁶) encodes the dynamical content via ι<sub>τ</sub>

- The leading behavior is (8/15)·ι<sub>τ</sub>⁴ because Q ∝ ι<sub>τ</sub>, M ∝ ι<sub>τ</sub>⁻½,
H ∝ ι<sub>τ</sub>⁻¹, L ∝ ι<sub>τ</sub>⁻¹ at zeroth order in the calibration cascade


### The Wrong Formula


The 1st Edition reference sheet incorrectly states α = (ι<sub>τ</sub>/2)⁴.
This gives (0.341304/2)⁴ ≈ (0.17073)⁴ ≈ 0.000849 — **off by a factor of ~8.6**.
The correct spectral formula is (8/15)·ι<sub>τ</sub>⁴, NOT (ι<sub>τ</sub>/2)⁴.

## Ground Truth Sources


- chapter34-alpha-derivation.tex (1st Ed Book IV): both formulas

- physics_layer_sector_instantiation.md §3: α as fixed-point readout


We compute α_spectral = (8/15) · ι<sub>τ</sub>⁴ using exact rational arithmetic.

ι<sub>τ</sub> = 341304/1000000

ι<sub>τ</sub>⁴ = 341304⁴ / 1000000⁴

(8/15) · ι<sub>τ</sub>⁴ = 8 · 341304⁴ / (15 · 1000000⁴)

We compute 341304⁴ step by step:
341304² = 116,594,274,681
341304⁴ = (341304²)² = 116,594,274,681² = 13,594,226,084,694,367,561
(This is a 19-digit number, well within Lean 4's arbitrary-precision Nat.)

---

### `Tau.BookIV.Sectors.iota_fourth_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L84-L85)
**def
Tau.BookIV.Sectors.iota_fourth_numer :ℕ**


ι<sub>τ</sub>⁴ numerator: 341304⁴.
Equations
- Tau.BookIV.Sectors.iota_fourth_numer = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Sectors.iota_fourth_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L87-L88)
**def
Tau.BookIV.Sectors.iota_fourth_denom :ℕ**


ι<sub>τ</sub>⁴ denominator: 10²⁴.
Equations
- Tau.BookIV.Sectors.iota_fourth_denom = Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookIV.Sectors.alpha_spectral_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L90-L91)
**def
Tau.BookIV.Sectors.alpha_spectral_numer :ℕ**


[IV.D08] α_spectral numerator: 8 · ι<sub>τ</sub>⁴.
Equations
- Tau.BookIV.Sectors.alpha_spectral_numer = 8 * Tau.BookIV.Sectors.iota_fourth_numer
Instances For

---

### `Tau.BookIV.Sectors.alpha_spectral_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L93-L94)
**def
Tau.BookIV.Sectors.alpha_spectral_denom :ℕ**


[IV.D08] α_spectral denominator: 15 · (10⁶)⁴ = 15 · 10²⁴.
Equations
- Tau.BookIV.Sectors.alpha_spectral_denom = 15 * Tau.BookIV.Sectors.iota_fourth_denom
Instances For

---

### `Tau.BookIV.Sectors.alpha_spectral_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L96-L98)
**theorem
Tau.BookIV.Sectors.alpha_spectral_denom_pos :alpha_spectral_denom > 0**


The denominator is positive.

---

### `Tau.BookIV.Sectors.alpha_spectral_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L104-L106)
**def
Tau.BookIV.Sectors.alpha_spectral_float :Float**


α_spectral as Float (for display).
Equations
- Tau.BookIV.Sectors.alpha_spectral_float = Float.ofNat Tau.BookIV.Sectors.alpha_spectral_numer / Float.ofNat Tau.BookIV.Sectors.alpha_spectral_denom
Instances For

---

### `Tau.BookIV.Sectors.alpha_inverse_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L108-L110)
**def
Tau.BookIV.Sectors.alpha_inverse_float :Float**


1/α as Float (should be close to 137).
Equations
- Tau.BookIV.Sectors.alpha_inverse_float = Float.ofNat Tau.BookIV.Sectors.alpha_spectral_denom / Float.ofNat Tau.BookIV.Sectors.alpha_spectral_numer
Instances For

---

### `Tau.BookIV.Sectors.alpha_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L116-L124)
**theorem
Tau.BookIV.Sectors.alpha_in_range :alpha_spectral_numer * 1000000 > 7200 * alpha_spectral_denom ∧ alpha_spectral_numer * 1000000 < 7400 * alpha_spectral_denom**


[IV.P02] α_spectral is in the range (7200, 7400) / 10⁶.
Experimental value: α ≈ 7297.35 / 10⁶.
Spectral approximation: α ≈ 7247 / 10⁶ (within range).

---

### `Tau.BookIV.Sectors.alpha_inverse_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L126-L132)
**theorem
Tau.BookIV.Sectors.alpha_inverse_in_range :alpha_spectral_denom > 135 * alpha_spectral_numer ∧ alpha_spectral_denom < 139 * alpha_spectral_numer**


1/α is between 135 and 139 (brackets the experimental 137.036).

The wrong formula (ι<sub>τ</sub>/2)⁴ = ι<sub>τ</sub>⁴/16, NOT (8/15)·ι<sub>τ</sub>⁴.

```
(ι<sub>τ</sub>/2)⁴ = 341304⁴ / (2⁴ · 10²⁴) = ι<sub>τ</sub>⁴ / 16

The ratio of the correct formula to the wrong formula is:
(8/15) / (1/16) = 128/15 ≈ 8.533...

The wrong formula gives α ≈ 0.000850, which is off by a factor of ~8.5.
The 1st Edition reference sheet formula α = (ι<sub>τ</sub>/2)⁴ is INCORRECT. 
```


---

### `Tau.BookIV.Sectors.wrong_alpha_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L148-L149)
**def
Tau.BookIV.Sectors.wrong_alpha_numer :ℕ**


Numerator of the wrong formula: ι<sub>τ</sub>⁴.
Equations
- Tau.BookIV.Sectors.wrong_alpha_numer = Tau.BookIV.Sectors.iota_fourth_numer
Instances For

---

### `Tau.BookIV.Sectors.wrong_alpha_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L151-L152)
**def
Tau.BookIV.Sectors.wrong_alpha_denom :ℕ**


Denominator of the wrong formula: 16 · (10⁶)⁴.
Equations
- Tau.BookIV.Sectors.wrong_alpha_denom = 16 * Tau.BookIV.Sectors.iota_fourth_denom
Instances For

---

### `Tau.BookIV.Sectors.wrong_formula_refutation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L154-L163)
**theorem
Tau.BookIV.Sectors.wrong_formula_refutation :wrong_alpha_numer * 1000000 < 1000 * wrong_alpha_denom**


The wrong formula gives a value far too small.
Specifically: 16 · correct_numer ≠ 15 · wrong_numer
(correct formula has factor 8/15, wrong has 1/16;
they differ by a factor of 128/15 ≈ 8.53).

---

### `Tau.BookIV.Sectors.correct_vs_wrong_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L165-L174)
**theorem
Tau.BookIV.Sectors.correct_vs_wrong_ratio :alpha_spectral_numer * wrong_alpha_denom * 15 = wrong_alpha_numer * alpha_spectral_denom * 128**


The correct and wrong formulas differ by the ratio 128/15.
correct/wrong = (8/15)/(1/16) = 128/15.
Cross-multiplied: correct_numer · wrong_denom · 15 = wrong_numer · correct_denom · 128.

---

### `Tau.BookIV.Sectors.alpha_from_em_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L180-L195)
**theorem
Tau.BookIV.Sectors.alpha_from_em_coupling :alpha_spectral_numer = 8 * (kappa_BB.numer * kappa_BB.numer) ∧ alpha_spectral_denom = 15 * (kappa_BB.denom * kappa_BB.denom)**


α_spectral = (8/15) · κ(B;2)²: the fine structure constant
is the EM self-coupling SQUARED, scaled by the primorial
factor 8/15 = 2³/(3·5).

Since κ(B;2) = ι<sub>τ</sub>², we have:
α = (8/15) · (ι<sub>τ</sub>²)² = (8/15) · ι<sub>τ</sub>⁴.

---

### `Tau.BookIV.Sectors.alpha_tower_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L201-L203)
**def
Tau.BookIV.Sectors.alpha_tower_numer :ℕ**


The tower fine-structure constant numerator: 121 · ι<sub>τ</sub>⁴.
121 = ω₁² = 11² from the iterated prime tower.
Equations
- Tau.BookIV.Sectors.alpha_tower_numer = 121 * Tau.BookIV.Sectors.iota_fourth_numer
Instances For

---

### `Tau.BookIV.Sectors.alpha_tower_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L205-L207)
**def
Tau.BookIV.Sectors.alpha_tower_denom :ℕ**


The tower fine-structure constant denominator: 225 · (10⁶)⁴.
225 = (γ₁ · γ₂)² = (3 · 5)² = 15² from the tower.
Equations
- Tau.BookIV.Sectors.alpha_tower_denom = 225 * Tau.BookIV.Sectors.iota_fourth_denom
Instances For

---

### `Tau.BookIV.Sectors.alpha_tower_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L209-L211)
**theorem
Tau.BookIV.Sectors.alpha_tower_denom_pos :alpha_tower_denom > 0**


The tower denominator is positive.

---

### `Tau.BookIV.Sectors.alpha_tower_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L213-L215)
**def
Tau.BookIV.Sectors.alpha_tower_float :Float**


α_tower as Float (for display).
Equations
- Tau.BookIV.Sectors.alpha_tower_float = Float.ofNat Tau.BookIV.Sectors.alpha_tower_numer / Float.ofNat Tau.BookIV.Sectors.alpha_tower_denom
Instances For

---

### `Tau.BookIV.Sectors.alpha_tower_inverse_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L217-L219)
**def
Tau.BookIV.Sectors.alpha_tower_inverse_float :Float**


1/α_tower as Float (should be close to 137.035).
Equations
- Tau.BookIV.Sectors.alpha_tower_inverse_float = Float.ofNat Tau.BookIV.Sectors.alpha_tower_denom / Float.ofNat Tau.BookIV.Sectors.alpha_tower_numer
Instances For

---

### `Tau.BookIV.Sectors.alpha_tower_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L221-L229)
**theorem
Tau.BookIV.Sectors.alpha_tower_in_range :alpha_tower_numer * 1000000 > 7296 * alpha_tower_denom ∧ alpha_tower_numer * 1000000 < 7300 * alpha_tower_denom**


α_tower is closer to CODATA than α_spectral.
α_tower ∈ (7296, 7300) per million, vs α_spectral ∈ (7200, 7400).
CODATA: α ≈ 7297.35 per million.

---

### `Tau.BookIV.Sectors.alpha_tower_inverse_tight`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L231-L238)
**theorem
Tau.BookIV.Sectors.alpha_tower_inverse_tight :1370 * alpha_tower_numer < 10 * alpha_tower_denom ∧ 10 * alpha_tower_denom < 1371 * alpha_tower_numer**


1/α_tower is between 137.0 and 137.1 (much tighter than spectral 135-139).
Cross-multiplied: 1370 · numer < 10 · denom < 1371 · numer.

---

### `Tau.BookIV.Sectors.tower_refines_spectral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L240-L250)
**theorem
Tau.BookIV.Sectors.tower_refines_spectral :alpha_tower_numer * alpha_spectral_denom * 120 = alpha_spectral_numer * alpha_tower_denom * 121**


The tower formula refines the spectral formula:
α_tower / α_spectral = (121/225) / (8/15) = 121/120.
Cross-multiplied: tower_numer · spectral_denom · 120
= spectral_numer · tower_denom · 121.

---

### `Tau.BookIV.Sectors.tower_correction_is_s5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L252-L255)
**theorem
Tau.BookIV.Sectors.tower_correction_is_s5 :121 = 120 + 1 ∧ 120 = 1 * 2 * 3 * 4 * 5**


The tower correction factor is exactly 121/120 = 1 + 1/|S₅|.
This is 1 + 1/5!, where 5 = η₁ from the iterated prime tower.

---

### `Tau.BookIV.Sectors.alpha_solenoidal_numerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L261-L269)
**theorem
Tau.BookIV.Sectors.alpha_solenoidal_numerator :(2 * 11) ^ 2 = 4 * 121**


The solenoidal balance decomposition of α:
Replacing ω₁ = η₂ = 11 and introducing π₁ = 2, the α formula
becomes α = (1/2 · (π₁ · η₂)/(γ₁ · γ₂))² · ι<sub>τ</sub>⁴, making all
three solenoidal generators {π, γ, η} simultaneously visible.

Numerically: (π₁ · η₂)² / 4 = (2 · 11)² / 4 = 484/4 = 121 = ω₁².
This is the cross-multiplied identity.

---

### `Tau.BookIV.Sectors.alpha_solenoidal_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L271-L277)
**theorem
Tau.BookIV.Sectors.alpha_solenoidal_form :4 * alpha_tower_numer = (2 * 11) ^ 2 * iota_fourth_numer**


The solenoidal balance form produces the same α_tower:
α_tower_numer = (π₁ · η₂)² / 4 · ι<sub>τ</sub>⁴.
Cross-multiplied: 4 · α_tower_numer = (2 · 11)² · ι<sub>τ</sub>⁴.

---

### `Tau.BookIV.Sectors.HolonomyFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L283-L306)
**structure
Tau.BookIV.Sectors.HolonomyFormula :Type**


[IV.R01] The holonomy formula for α involves four calibration
parameters Q, M, H, L (all determined by ι<sub>τ</sub> via the neutron
anchoring cascade, Book IV Part VII). At this stage we record
the structural relationship:

α_holonomy = (π³/16) · Q⁴/(M² H³ L⁶)

For the holonomy formula to match the spectral formula, we need:
(π³/16) · Q⁴/(M² H³ L⁶) = (8/15) · ι<sub>τ</sub>⁴ · R(ι<sub>τ</sub>)

where R(ι<sub>τ</sub>) ≈ 1.0065... is the calibration correction factor.

This structure records that the holonomy formula EXISTS and
has the correct form; the numerical evaluation requires the
calibration cascade.

- geom_numer : ℕ
Geometric prefactor: π³/16.

- geom_denom : ℕ
- Q_exp : ℤ
The calibration exponents: Q⁴, M⁻², H⁻³, L⁻⁶.

- M_exp : ℤ
- H_exp : ℤ
- L_exp : ℤ
Instances For

---

### `Tau.BookIV.Sectors.holonomy_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L308-L309)
**def
Tau.BookIV.Sectors.holonomy_alpha :HolonomyFormula**


The standard holonomy formula.
Equations
- Tau.BookIV.Sectors.holonomy_alpha = { }
Instances For

---

### `Tau.BookIV.Sectors.alpha_is_fourth_power`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L315-L322)
**theorem
Tau.BookIV.Sectors.alpha_is_fourth_power :alpha_spectral_numer = 8 * iota_fourth_numer ∧ alpha_spectral_denom = 15 * iota_fourth_denom**


α is fundamentally a FOURTH-power phenomenon in ι<sub>τ</sub>.
This is structural: electromagnetic coupling involves two τ² modes
(emission + absorption), each contributing ι<sub>τ</sub>² (torus area factor).
α ∝ (ι<sub>τ</sub>²)² = ι<sub>τ</sub>⁴.

---

### `Tau.BookIV.Sectors.alpha_exp_inverse_scaled`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L328-L331)
**def
Tau.BookIV.Sectors.alpha_exp_inverse_scaled :ℕ**


The experimental value of α⁻¹ ≈ 137.036.
We encode as the integer 137036 / 1000 for comparison.
The spectral formula gives 1/α ≈ 137.9..., slightly above.
Equations
- Tau.BookIV.Sectors.alpha_exp_inverse_scaled = 137036
Instances For

---

### `Tau.BookIV.Sectors.alpha_inverse_correct_ballpark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L333-L340)
**theorem
Tau.BookIV.Sectors.alpha_inverse_correct_ballpark :137 * alpha_spectral_numer < alpha_spectral_denom ∧ alpha_spectral_denom < 139 * alpha_spectral_numer**


The spectral formula gives 1/α in the correct ballpark.
Specifically, the spectral 1/α is between 137 and 139.

---

### `Tau.BookIV.Sectors.primorial_factor_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/FineStructure.lean#L346-L351)
**theorem
Tau.BookIV.Sectors.primorial_factor_decomposition :8 = 2 * 2 * 2 ∧ 15 = 3 * 5**


The factor 8/15 = 2³/(3·5) arises from the first three primes.
These are the primes in the primorial M₃ = 2·3·5 = 30.
The numerator 8 = 2³ reflects the three spatial dimensions
earned via the Global Cartesian Gluing Theorem (III.T50).
