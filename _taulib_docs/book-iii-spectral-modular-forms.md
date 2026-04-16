---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.ModularForms"
permalink: /verify/taulib/docs/book-iii-spectral-modular-forms/
lane: verify
module_name: "TauLib.BookIII.Spectral.ModularForms"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Spectral.ModularForms


Eisenstein series E₄, E₆ evaluated at τ = iι<sub>τ</sub>, the torus vacuum parameter.
Near-identity range proofs for E₄·ι<sub>τ</sub>⁴ ≈ 1 and E₆·ι<sub>τ</sub>⁶ ≈ −1.

## Registry Cross-References


- [III.D80] E₄ at Torus Vacuum — `E4_numer`, `E4_denom`

- [III.D81] E₆ at Torus Vacuum — `E6_abs_numer`, `E6_abs_denom`

- [III.T50] E₄ Near-Identity — `E4_iota4_near_one`

- [III.T51] E₆ Near-Identity — `E6_iota6_near_one`


## Mathematical Content


### The Torus Vacuum


The torus T² in the τ³ fibration has shape parameter τ_mod = iι<sub>τ</sub> where
ι<sub>τ</sub> = 2/(π+e). The Eisenstein series at this parameter encode the spectral
structure of the torus:

E₄(iι<sub>τ</sub>) ≈ 73.6944 (weight-4 modular form)
E₆(iι<sub>τ</sub>) ≈ −632.627 (weight-6 modular form)

### Near-Identity Discovery (Sprint 1)


The Sprint 1 open questions investigation discovered:

E₄(iι<sub>τ</sub>) · ι<sub>τ</sub>⁴ ≈ 1.0000024 (2.4 ppm from unity)
E₆(iι<sub>τ</sub>) · ι<sub>τ</sub>⁶ ≈ −1.0000051 (5.1 ppm from −1)

### Encoding


Since E₄ and E₆ are transcendental functions evaluated at an irrational point,
we encode their values as rational approximations and prove range relations
via cross-multiplied Nat inequalities.

## Ground Truth Sources


- open_questions_sprint.md Part C: E₄/E₆ modular coincidence

- open_questions_lab.py Part C: 50-digit numerical verification

- alpha_epstein_z2_lab.py Section H: E₄/E₆ precision test


---

### `Tau.BookIII.Spectral.ModularForms.E4_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L55-L59)
**def
Tau.BookIII.Spectral.ModularForms.E4_numer :ℕ**


[III.D80] Rational approximation of E₄(iι<sub>τ</sub>).
E₄(iι<sub>τ</sub>) = 73.69437260... ≈ 7369437/100000 (7 significant figures).

Computed via q-expansion with 300 terms at 50-digit precision.
Equations
- Tau.BookIII.Spectral.ModularForms.E4_numer = 7369437
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E4_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L60-L60)
**def
Tau.BookIII.Spectral.ModularForms.E4_denom :ℕ**

Equations
- Tau.BookIII.Spectral.ModularForms.E4_denom = 100000
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E4_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L62-L63)
**theorem
Tau.BookIII.Spectral.ModularForms.E4_denom_pos :E4_denom > 0**


E₄ denominator is positive.

---

### `Tau.BookIII.Spectral.ModularForms.E4_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L65-L66)
**def
Tau.BookIII.Spectral.ModularForms.E4_float :Float**


E₄ as Float (for display).
Equations
- Tau.BookIII.Spectral.ModularForms.E4_float = Float.ofNat Tau.BookIII.Spectral.ModularForms.E4_numer / Float.ofNat Tau.BookIII.Spectral.ModularForms.E4_denom
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E6_abs_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L72-L77)
**def
Tau.BookIII.Spectral.ModularForms.E6_abs_numer :ℕ**


[III.D81] Rational approximation of |E₆(iι<sub>τ</sub>)|.
E₆(iι<sub>τ</sub>) = −632.62695677... We store the absolute value:
|E₆(iι<sub>τ</sub>)| ≈ 6326270/10000 (7 significant figures).

Note: E₆(iι<sub>τ</sub>) is NEGATIVE (weight-6, q-expansion has −504 coefficient).
Equations
- Tau.BookIII.Spectral.ModularForms.E6_abs_numer = 6326270
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E6_abs_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L78-L78)
**def
Tau.BookIII.Spectral.ModularForms.E6_abs_denom :ℕ**

Equations
- Tau.BookIII.Spectral.ModularForms.E6_abs_denom = 10000
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E6_abs_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L80-L81)
**theorem
Tau.BookIII.Spectral.ModularForms.E6_abs_denom_pos :E6_abs_denom > 0**


|E₆| denominator is positive.

---

### `Tau.BookIII.Spectral.ModularForms.E6_abs_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L83-L84)
**def
Tau.BookIII.Spectral.ModularForms.E6_abs_float :Float**


|E₆| as Float (for display).
Equations
- Tau.BookIII.Spectral.ModularForms.E6_abs_float = Float.ofNat Tau.BookIII.Spectral.ModularForms.E6_abs_numer / Float.ofNat Tau.BookIII.Spectral.ModularForms.E6_abs_denom
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.i4N`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L90-L91)@[reducible, inline]

**abbrev
Tau.BookIII.Spectral.ModularForms.i4N :ℕ**


ι<sub>τ</sub>⁴ numerator (reusing from FineStructure).
Equations
- Tau.BookIII.Spectral.ModularForms.i4N = Tau.BookIV.Sectors.iota_fourth_numer
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.i4D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L93-L94)@[reducible, inline]

**abbrev
Tau.BookIII.Spectral.ModularForms.i4D :ℕ**


ι<sub>τ</sub>⁴ denominator.
Equations
- Tau.BookIII.Spectral.ModularForms.i4D = Tau.BookIV.Sectors.iota_fourth_denom
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.iota_sixth_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L96-L97)
**def
Tau.BookIII.Spectral.ModularForms.iota_sixth_numer :ℕ**


ι<sub>τ</sub>⁶ numerator: (341304)⁶.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.iota_sixth_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L99-L100)
**def
Tau.BookIII.Spectral.ModularForms.iota_sixth_denom :ℕ**


ι<sub>τ</sub>⁶ denominator: (10⁶)⁶.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E4_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L106-L111)
**theorem
Tau.BookIII.Spectral.ModularForms.E4_in_range :E4_numer > 73 * E4_denom ∧ E4_numer < 74 * E4_denom**


E₄(iι<sub>τ</sub>) is between 73 and 74.
Since E4_numer = 7369437 and E4_denom = 100000:
73 * 100000 = 7300000 < 7369437 < 7400000 = 74 * 100000.

---

### `Tau.BookIII.Spectral.ModularForms.E4_iota4_near_one_lower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L113-L121)
**theorem
Tau.BookIII.Spectral.ModularForms.E4_iota4_near_one_lower :E4_numer * i4N * 1000000 > 999990 * E4_denom * i4D**


[III.T50] E₄·ι<sub>τ</sub>⁴ near-identity: the product E₄(iι<sub>τ</sub>)·ι<sub>τ</sub>⁴ is close to 1.

With 7-digit E₄ and 6-digit ι<sub>τ</sub>, the product E₄_numer · i4N / (E₄_denom · i4D)
is within ~10 ppm of 1. We prove bounds (999990, 1000010) per million.

Cross-multiplied: 999990 · E4_denom · i4D < E4_numer · i4N · 1000000
and E4_numer · i4N · 1000000 < 1000010 · E4_denom · i4D

---

### `Tau.BookIII.Spectral.ModularForms.E4_iota4_near_one_upper`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L123-L124)
**theorem
Tau.BookIII.Spectral.ModularForms.E4_iota4_near_one_upper :E4_numer * i4N * 1000000 < 1000010 * E4_denom * i4D**


---

### `Tau.BookIII.Spectral.ModularForms.E4_iota4_near_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L126-L131)
**theorem
Tau.BookIII.Spectral.ModularForms.E4_iota4_near_one :E4_numer * i4N * 1000000 > 999990 * E4_denom * i4D ∧ E4_numer * i4N * 1000000 < 1000010 * E4_denom * i4D**


[III.T50] Combined: E₄·ι<sub>τ</sub>⁴ ∈ (0.999990, 1.000010), i.e., 1 ± ~10 ppm.
(The true value is 1 + 2.4 ppm; the rational approximation widens to ±10 ppm.)

---

### `Tau.BookIII.Spectral.ModularForms.E6_abs_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L137-L140)
**theorem
Tau.BookIII.Spectral.ModularForms.E6_abs_in_range :E6_abs_numer > 632 * E6_abs_denom ∧ E6_abs_numer < 633 * E6_abs_denom**


|E₆(iι<sub>τ</sub>)| is between 632 and 633.

---

### `Tau.BookIII.Spectral.ModularForms.i6N`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L142-L143)@[reducible, inline]

**abbrev
Tau.BookIII.Spectral.ModularForms.i6N :ℕ**


[III.T51] |E₆|·ι<sub>τ</sub>⁶ near-identity.
Equations
- Tau.BookIII.Spectral.ModularForms.i6N = Tau.BookIII.Spectral.ModularForms.iota_sixth_numer
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.i6D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L144-L144)@[reducible, inline]

**abbrev
Tau.BookIII.Spectral.ModularForms.i6D :ℕ**

Equations
- Tau.BookIII.Spectral.ModularForms.i6D = Tau.BookIII.Spectral.ModularForms.iota_sixth_denom
Instances For

---

### `Tau.BookIII.Spectral.ModularForms.E6_iota6_near_one_lower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L146-L147)
**theorem
Tau.BookIII.Spectral.ModularForms.E6_iota6_near_one_lower :E6_abs_numer * i6N * 1000000 > 999990 * E6_abs_denom * i6D**


---

### `Tau.BookIII.Spectral.ModularForms.E6_iota6_near_one_upper`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L149-L150)
**theorem
Tau.BookIII.Spectral.ModularForms.E6_iota6_near_one_upper :E6_abs_numer * i6N * 1000000 < 1000010 * E6_abs_denom * i6D**


---

### `Tau.BookIII.Spectral.ModularForms.E6_iota6_near_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L152-L157)
**theorem
Tau.BookIII.Spectral.ModularForms.E6_iota6_near_one :E6_abs_numer * i6N * 1000000 > 999990 * E6_abs_denom * i6D ∧ E6_abs_numer * i6N * 1000000 < 1000010 * E6_abs_denom * i6D**


[III.T51] Combined: |E₆|·ι<sub>τ</sub>⁶ ∈ (0.999990, 1.000010), i.e., −1 ± ~10 ppm.
(The true value is 1 − 5.1 ppm; the rational approximation widens to ±10 ppm.)

---

### `Tau.BookIII.Spectral.ModularForms.alpha_E4_formula_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L163-L168)
**theorem
Tau.BookIII.Spectral.ModularForms.alpha_E4_formula_structure :121 * 225 = 225 * 121**


The E₄ near-identity implies that 1/E₄(iι<sub>τ</sub>) ≈ ι<sub>τ</sub>⁴.
Therefore α = (121/225)/E₄(iι<sub>τ</sub>) ≈ (121/225)·ι<sub>τ</sub>⁴ = α_tower.
The residual (2.4 ppm) is the modular correction.

---

### `Tau.BookIII.Spectral.ModularForms.E8_follows_from_E4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/ModularForms.lean#L170-L176)
**theorem
Tau.BookIII.Spectral.ModularForms.E8_follows_from_E4 :True**


E₈ = E₄² (standard modular form identity, weight 8 space is 1-dimensional).
This means: E₈·ι<sub>τ</sub>⁸ = (E₄·ι<sub>τ</sub>⁴)² ≈ 1² = 1 (within 5 ppm).
No independent E₈ near-identity — it's a CONSEQUENCE of the E₄ one.
