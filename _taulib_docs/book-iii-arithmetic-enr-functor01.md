---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.EnrFunctor01"
permalink: /verify/taulib/docs/book-iii-arithmetic-enr-functor01/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.EnrFunctor01"
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

# TauLib.BookIII.Arithmetic.EnrFunctor01


Enrichment Functor Enr₀₁, E₁ Mutual Determination Instance,
and Three-Reading Equivalence.

## Registry Cross-References


- [III.D57] Enrichment Functor Enr₀₁ -- `enr_01_check`

- [III.D58] E₁ Mutual Determination Instance -- `e1_md_instance_check`

- [III.P24] Three-Reading Equivalence at E₁ -- `three_reading_check`


## Mathematical Content


**III.D57 (Enrichment Functor Enr₀₁):** Faithful functor
Enr₀₁: Cat_τ(E₀) → Cat_τ(E₁) enriching algebraic tower data with
split-complex dynamics and sector structure.

**III.D58 (E₁ Mutual Determination Instance):** Unified triple (B₁, S₁, I₁)
at E₁ with NS regularity, YM gap, and Hodge addressability as three readings.

**III.P24 (Three-Reading Equivalence):** The E₁ MD instance admits exactly
three non-trivial sector-restricted readings (NS, YM, Hodge).

---

### `Tau.BookIII.Arithmetic.enr_01_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L40-L67)
**def
Tau.BookIII.Arithmetic.enr_01_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D57] Enrichment functor check: E₀ → E₁ enrichment preserves
tower structure while adding sector decomposition. Each E₀ object
(BNF at level k) is enriched to an E₁ object (BNF + gauge data).
Equations
- Tau.BookIII.Arithmetic.enr_01_check bound db = Tau.BookIII.Arithmetic.enr_01_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.enr_01_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L46-L66)@[irreducible]

**def
Tau.BookIII.Arithmetic.enr_01_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.enr_01_faithful_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L69-L87)
**def
Tau.BookIII.Arithmetic.enr_01_faithful_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D57] Functor composition check: Enr₀₁ at level k composed with
projection back to E₀ is the identity.
Equations
- Tau.BookIII.Arithmetic.enr_01_faithful_check bound db = Tau.BookIII.Arithmetic.enr_01_faithful_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.enr_01_faithful_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L74-L86)@[irreducible]

**def
Tau.BookIII.Arithmetic.enr_01_faithful_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.e1_md_instance_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L93-L104)
**def
Tau.BookIII.Arithmetic.e1_md_instance_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D58] E₁ MD instance: the triple (B₁, S₁, I₁) at E₁ level.
B₁ = boundary (flow data), S₁ = spectral (gap data),
I₁ = interior (addressability data). All three determine each other.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.three_reading_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L110-L121)
**def
Tau.BookIII.Arithmetic.three_reading_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P24] Three-reading equivalence: the E₁ MD instance has exactly
three non-trivial sector-restricted readings: NS, YM, Hodge.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.enr_01_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L136-L137)
**theorem
Tau.BookIII.Arithmetic.enr_01_15_4 :enr_01_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.enr_01_faithful_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L139-L140)
**theorem
Tau.BookIII.Arithmetic.enr_01_faithful_15_4 :enr_01_faithful_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.e1_md_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L142-L143)
**theorem
Tau.BookIII.Arithmetic.e1_md_15_3 :e1_md_instance_check 15 3 = true**


---

### `Tau.BookIII.Arithmetic.three_reading_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L145-L146)
**theorem
Tau.BookIII.Arithmetic.three_reading_15_3 :three_reading_check 15 3 = true**


---

### `Tau.BookIII.Arithmetic.enr_01_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L152-L154)
**theorem
Tau.BookIII.Arithmetic.enr_01_10_1 :enr_01_check 10 1 = true**


[III.D57] Structural: enrichment at depth 1.

---

### `Tau.BookIII.Arithmetic.e1_level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L156-L157)
**theorem
Tau.BookIII.Arithmetic.e1_level :Enrichment.EnrLevel.E1.toNat = 1**


[III.D58] Structural: E₁ level is 1.

---

### `Tau.BookIII.Arithmetic.all_e1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L159-L163)
**theorem
Tau.BookIII.Arithmetic.all_e1 :(Doors.problem_level Doors.MillenniumProblem.NS == Enrichment.EnrLevel.E1 && Doors.problem_level Doors.MillenniumProblem.YM == Enrichment.EnrLevel.E1 && Doors.problem_level Doors.MillenniumProblem.Hodge == Enrichment.EnrLevel.E1) = true**


[III.P24] Structural: NS, YM, Hodge are all at E₁.
