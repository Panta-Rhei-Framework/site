---
layout: taulib-doc
title: "TauLib.BookIII.Doors.Poincare"
permalink: /verify/taulib/docs/book-iii-doors-poincare/
lane: verify
module_name: "TauLib.BookIII.Doors.Poincare"
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

# TauLib.BookIII.Doors.Poincare


Simply Connected in Category τ and Poincaré as Gluing Guarantee.

## Registry Cross-References


- [III.D35] Simply Connected in Category τ -- `simply_connected_check`

- [III.P13] Poincaré as Gluing Guarantee -- `gluing_guarantee_check`


## Mathematical Content


**III.D35 (Simply Connected in τ):** Categorical reinterpretation of simple
connectivity: π₁^τ trivial iff every loop of transition functions in the
Hartogs bulk is contractible. S³ is the terminal object among closed,
simply connected 3-dimensional τ-spaces. Poincaré = uniqueness of
the terminal object.

**III.P13 (Poincaré as Gluing):** Poincaré guarantees that local Hartogs bulk
projections glue into a global space homeomorphic to S³ when the fundamental
group is trivial. Simple connectivity = no obstruction to global coherence.

---

### `Tau.BookIII.Doors.simply_connected_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L37-L62)
**def
Tau.BookIII.Doors.simply_connected_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D35] Simple connectivity at finite level k: every "loop" at
primorial level k is contractible, meaning the transition function
around a cycle is the identity.
In τ-terms: for every x and every prime cycle p₁→p₂→...→p₁,
the CRT decomposition is consistent (no monodromy).
Equations
- Tau.BookIII.Doors.simply_connected_check bound db = Tau.BookIII.Doors.simply_connected_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.simply_connected_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L45-L61)@[irreducible]

**def
Tau.BookIII.Doors.simply_connected_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.terminal_object_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L64-L86)
**def
Tau.BookIII.Doors.terminal_object_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D35] Terminal object check: among all τ-spaces at level k with
trivial fundamental group, the structure is unique up to isomorphism.
In τ-terms: any two elements with the same CRT residues are equal.
Equations
- Tau.BookIII.Doors.terminal_object_check bound db = Tau.BookIII.Doors.terminal_object_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.terminal_object_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L70-L85)@[irreducible]

**def
Tau.BookIII.Doors.terminal_object_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.gluing_guarantee_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L92-L117)
**def
Tau.BookIII.Doors.gluing_guarantee_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P13] Gluing guarantee: local Hartogs bulk projections glue
coherently when fundamental group is trivial.
In τ-terms: the CRT local-to-global reconstruction is exact,
and the bipolar decomposition respects the gluing.
Equations
- Tau.BookIII.Doors.gluing_guarantee_check bound db = Tau.BookIII.Doors.gluing_guarantee_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.gluing_guarantee_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L99-L116)@[irreducible]

**def
Tau.BookIII.Doors.gluing_guarantee_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.obstruction_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L119-L142)
**def
Tau.BookIII.Doors.obstruction_check
(db : Denotation.TauIdx)
 :Bool**


[III.P13] Obstruction detection: when the fundamental group is
non-trivial, the gluing fails. Test: inconsistent residues
cannot be reconstructed coherently.
Equations
- Tau.BookIII.Doors.obstruction_check db = Tau.BookIII.Doors.obstruction_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.obstruction_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L125-L135)@[irreducible]

**def
Tau.BookIII.Doors.obstruction_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.obstruction_check.check_bijectivity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L137-L142)@[irreducible]

**def
Tau.BookIII.Doors.obstruction_check.check_bijectivity
(x pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.simply_connected_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L157-L158)
**theorem
Tau.BookIII.Doors.simply_connected_15_4 :simply_connected_check 15 4 = true**


---

### `Tau.BookIII.Doors.terminal_object_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L160-L161)
**theorem
Tau.BookIII.Doors.terminal_object_10_3 :terminal_object_check 10 3 = true**


---

### `Tau.BookIII.Doors.gluing_guarantee_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L163-L164)
**theorem
Tau.BookIII.Doors.gluing_guarantee_15_4 :gluing_guarantee_check 15 4 = true**


---

### `Tau.BookIII.Doors.obstruction_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L166-L167)
**theorem
Tau.BookIII.Doors.obstruction_4 :obstruction_check 4 = true**


---

### `Tau.BookIII.Doors.crt_bijective_42_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L173-L177)
**theorem
Tau.BookIII.Doors.crt_bijective_42_3 :Polarity.crt_reconstruct (Polarity.crt_decompose 42 3) 3 = 42 % Polarity.primorial 3**


[III.D35] Structural: CRT is bijective at depth 3
(simple connectivity = no monodromy).

---

### `Tau.BookIII.Doors.terminal_depth_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L179-L181)
**theorem
Tau.BookIII.Doors.terminal_depth_1 :simply_connected_check 10 1 = true**


[III.D35] Structural: terminal object at depth 1 (only mod 2).

---

### `Tau.BookIII.Doors.gluing_depth_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/Poincare.lean#L183-L185)
**theorem
Tau.BookIII.Doors.gluing_depth_1 :gluing_guarantee_check 10 1 = true**


[III.P13] Structural: gluing at depth 1.
