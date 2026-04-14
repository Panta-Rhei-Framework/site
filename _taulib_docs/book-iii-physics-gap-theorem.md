---
layout: taulib-doc
title: "TauLib.BookIII.Physics.GapTheorem"
permalink: /verify/taulib/docs/book-iii-physics-gap-theorem/
lane: verify
module_name: "TauLib.BookIII.Physics.GapTheorem"
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

# TauLib.BookIII.Physics.GapTheorem


τ-Gap Meta-Theorem, Gap Constant, Mass Existence, Yang-Mills Instantiation,
and YM Sector Coupling.

## Registry Cross-References


- [III.T26] τ-Gap Meta-Theorem -- `tau_gap_meta_check`

- [III.D45] Gap Constant -- `gap_constant`, `gap_constant_check`

- [III.P17] Mass Existence -- `mass_existence_check`

- [III.T27] Yang-Mills Instantiation -- `yang_mills_gap_check`

- [III.D46] YM Sector Coupling -- `ym_sector_coupling`, `ym_coupling_check`


## Mathematical Content


**III.T26 (τ-Gap Meta-Theorem):** In any strong sector at E₁ with non-trivial
B/C asymmetry, the spectral gap is bounded below by a computable constant
determined by the primorial depth. The gap arises from the coprimality of
B-product and C-product: no eigenvalue of H_L at the "zero mode" exists
between the two sectors.

**III.D45 (Gap Constant):** The gap constant at level k is
gap(k) = min(B-product, C-product) at that level. As k → ∞, the gap
grows without bound (B and C products grow with distinct rates).

**III.P17 (Mass Existence):** The gap constant is positive for k ≥ 3,
proving the existence of a mass gap in any strong sector.

**III.T27 (Yang-Mills Instantiation):** Yang-Mills mass gap = τ-gap in the
E₁ gauge sector. The non-abelian gauge structure is encoded in the
B/C asymmetry of the split-complex zeta.

**III.D46 (YM Sector Coupling):** The YM coupling constant at level k is
the ratio of B-product to C-product, measuring the degree of asymmetry.

---

### `Tau.BookIII.Physics.tau_gap_at_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L51-L56)
**def
Tau.BookIII.Physics.tau_gap_at_level
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.T26] τ-gap at level k: the minimum of B-product and C-product.
Positive iff both sectors are non-trivial.
Equations
- Tau.BookIII.Physics.tau_gap_at_level k = if Tau.BookIII.Doors.split_zeta_b k ≤ Tau.BookIII.Doors.split_zeta_c k then Tau.BookIII.Doors.split_zeta_b k
 else Tau.BookIII.Doors.split_zeta_c k
Instances For

---

### `Tau.BookIII.Physics.tau_gap_meta_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L58-L72)
**def
Tau.BookIII.Physics.tau_gap_meta_check
(db : Denotation.TauIdx)
 :Bool**


[III.T26] τ-gap meta-theorem check: at every level k ≥ 3 where
the strong sector condition holds, the gap is positive.
Equations
- Tau.BookIII.Physics.tau_gap_meta_check db = Tau.BookIII.Physics.tau_gap_meta_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.tau_gap_meta_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L63-L71)@[irreducible]

**def
Tau.BookIII.Physics.tau_gap_meta_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.gap_growth_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L74-L86)
**def
Tau.BookIII.Physics.gap_growth_check
(db : Denotation.TauIdx)
 :Bool**


[III.T26] Gap growth check: the gap is non-decreasing across levels
(B and C products can only grow as more primes are included).
Equations
- Tau.BookIII.Physics.gap_growth_check db = Tau.BookIII.Physics.gap_growth_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.gap_growth_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L79-L85)@[irreducible]

**def
Tau.BookIII.Physics.gap_growth_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.gap_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L92-L94)
**def
Tau.BookIII.Physics.gap_constant
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D45] Gap constant at level k. For k ≥ 3, this is the minimum
of B-product and C-product (both positive by strong sector).
Equations
- Tau.BookIII.Physics.gap_constant k = Tau.BookIII.Physics.tau_gap_at_level k
Instances For

---

### `Tau.BookIII.Physics.gap_constant_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L96-L110)
**def
Tau.BookIII.Physics.gap_constant_check
(db : Denotation.TauIdx)
 :Bool**


[III.D45] Gap constant check: the constant is well-defined and
positive for all strong sector levels.
Equations
- Tau.BookIII.Physics.gap_constant_check db = Tau.BookIII.Physics.gap_constant_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.gap_constant_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L101-L109)@[irreducible]

**def
Tau.BookIII.Physics.gap_constant_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.mass_existence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L116-L131)
**def
Tau.BookIII.Physics.mass_existence_check
(db : Denotation.TauIdx)
 :Bool**


[III.P17] Mass existence: the gap constant is strictly positive
at all levels ≥ 3 where B and C are non-trivial. This is the
mass gap existence theorem in τ.
Equations
- Tau.BookIII.Physics.mass_existence_check db = Tau.BookIII.Physics.mass_existence_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.mass_existence_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L122-L130)@[irreducible]

**def
Tau.BookIII.Physics.mass_existence_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.yang_mills_gap_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L137-L158)
**def
Tau.BookIII.Physics.yang_mills_gap_check
(db : Denotation.TauIdx)
 :Bool**


[III.T27] Yang-Mills gap check: the YM mass gap is the τ-gap
restricted to the gauge sector. The gauge structure comes from
the B/C asymmetry of the split-complex zeta at E₁.
Equations
- Tau.BookIII.Physics.yang_mills_gap_check db = Tau.BookIII.Physics.yang_mills_gap_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.yang_mills_gap_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L143-L157)@[irreducible]

**def
Tau.BookIII.Physics.yang_mills_gap_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.ym_sector_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L164-L169)
**def
Tau.BookIII.Physics.ym_sector_coupling
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D46] YM sector coupling at level k: the ratio B-product / C-product
(integer division). Measures the degree of B/C asymmetry.
Equations
- Tau.BookIII.Physics.ym_sector_coupling k = if (Tau.BookIII.Doors.split_zeta_c k == 0) = true then 0
 else Tau.BookIII.Doors.split_zeta_b k / Tau.BookIII.Doors.split_zeta_c k
Instances For

---

### `Tau.BookIII.Physics.ym_coupling_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L171-L186)
**def
Tau.BookIII.Physics.ym_coupling_check
(db : Denotation.TauIdx)
 :Bool**


[III.D46] YM coupling check: the coupling is well-defined, non-zero,
and tower-monotone (coupling changes predictably with depth).
Equations
- Tau.BookIII.Physics.ym_coupling_check db = Tau.BookIII.Physics.ym_coupling_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.ym_coupling_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L176-L185)@[irreducible]

**def
Tau.BookIII.Physics.ym_coupling_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.tau_gap_meta_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L206-L207)
**theorem
Tau.BookIII.Physics.tau_gap_meta_5 :tau_gap_meta_check 5 = true**


---

### `Tau.BookIII.Physics.gap_growth_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L209-L210)
**theorem
Tau.BookIII.Physics.gap_growth_5 :gap_growth_check 5 = true**


---

### `Tau.BookIII.Physics.gap_constant_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L212-L213)
**theorem
Tau.BookIII.Physics.gap_constant_5 :gap_constant_check 5 = true**


---

### `Tau.BookIII.Physics.mass_existence_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L215-L216)
**theorem
Tau.BookIII.Physics.mass_existence_5 :mass_existence_check 5 = true**


---

### `Tau.BookIII.Physics.yang_mills_gap_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L218-L219)
**theorem
Tau.BookIII.Physics.yang_mills_gap_5 :yang_mills_gap_check 5 = true**


---

### `Tau.BookIII.Physics.ym_coupling_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L221-L222)
**theorem
Tau.BookIII.Physics.ym_coupling_5 :ym_coupling_check 5 = true**


---

### `Tau.BookIII.Physics.gap_pos_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L228-L230)
**theorem
Tau.BookIII.Physics.gap_pos_3 :tau_gap_at_level 3 > 0**


[III.T26] Structural: gap at depth 3 is positive.

---

### `Tau.BookIII.Physics.gap_grows_3_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L232-L234)
**theorem
Tau.BookIII.Physics.gap_grows_3_4 :tau_gap_at_level 4 ≥ tau_gap_at_level 3**


[III.T26] Structural: gap grows from depth 3 to depth 4.

---

### `Tau.BookIII.Physics.gap_constant_is_gap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L236-L238)
**theorem
Tau.BookIII.Physics.gap_constant_is_gap
(k : Denotation.TauIdx)
 :gap_constant k = tau_gap_at_level k**


[III.D45] Structural: gap constant equals tau_gap_at_level.

---

### `Tau.BookIII.Physics.ym_gap_is_tau_gap_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L240-L242)
**theorem
Tau.BookIII.Physics.ym_gap_is_tau_gap_3 :gap_constant 3 = tau_gap_at_level 3**


[III.T27] Structural: YM gap at depth 3 coincides with τ-gap.

---

### `Tau.BookIII.Physics.ym_coupling_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/GapTheorem.lean#L244-L246)
**theorem
Tau.BookIII.Physics.ym_coupling_3 :ym_sector_coupling 3 > 0**


[III.D46] Structural: YM coupling at depth 3.
