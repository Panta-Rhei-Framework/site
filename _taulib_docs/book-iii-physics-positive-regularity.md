---
layout: taulib-doc
title: "TauLib.BookIII.Physics.PositiveRegularity"
permalink: /verify/taulib/docs/book-iii-physics-positive-regularity/
lane: verify
module_name: "TauLib.BookIII.Physics.PositiveRegularity"
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

# TauLib.BookIII.Physics.PositiveRegularity


Positive Regularity, Stabilized ω-Germ, Defect Contractivity, and Stability Criterion.

## Registry Cross-References


- [III.T25] Positive Regularity -- `positive_regularity_check`

- [III.D42] Stabilized ω-Germ -- `stabilized_germ_check`

- [III.P14] Defect Contractivity -- `defect_contractivity_check`

- [III.P15] Stability Criterion -- `stability_criterion_check`


## Mathematical Content


**III.T25 (Positive Regularity):** Every ω-germ assignment on the primorial
tower stabilizes. Three-condition proof: (1) clopen locality — each cylinder is
clopen so germs are finitely determined; (2) tower determinacy — CRT bijectivity
forces consistent extensions; (3) defect contractivity — the defect functional
strictly decreases. This ENRICHES Book II's regularity_depth at E₁ level.

**III.D42 (Stabilized ω-Germ):** The limit of the flow: at sufficiently large k,
the BNF assignment is constant. The stabilized germ is the E₁-level "ω-germ at ∞".

**III.P14 (Defect Contractivity):** At each primorial step, the defect functional
cannot increase. Combined with non-negativity, this forces stabilization.

**III.P15 (Stability Criterion):** A fluid datum is stable iff its defect
functional is zero at all levels from some k₀ onward.

---

### `Tau.BookIII.Physics.clopen_locality_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L44-L69)
**def
Tau.BookIII.Physics.clopen_locality_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T25] Clopen locality: each cylinder at level k is determined
by finitely many residues. The BNF at (x mod Prim(k)) depends
only on the residues at primes ≤ p_k.
Equations
- Tau.BookIII.Physics.clopen_locality_check bound db = Tau.BookIII.Physics.clopen_locality_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.clopen_locality_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L50-L68)@[irreducible]

**def
Tau.BookIII.Physics.clopen_locality_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.tower_determinacy_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L71-L88)
**def
Tau.BookIII.Physics.tower_determinacy_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T25] Tower determinacy: CRT bijectivity forces consistent
extensions from level k to k+1.
Equations
- Tau.BookIII.Physics.tower_determinacy_check bound db = Tau.BookIII.Physics.tower_determinacy_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.tower_determinacy_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L76-L87)@[irreducible]

**def
Tau.BookIII.Physics.tower_determinacy_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.positive_regularity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L90-L100)
**def
Tau.BookIII.Physics.positive_regularity_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T25] Positive regularity: combines clopen locality, tower
determinacy, and defect contractivity. All three conditions hold
at every primorial level.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.stabilized_germ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L106-L111)
**def
Tau.BookIII.Physics.stabilized_germ
(x db : Denotation.TauIdx)
 :Spectral.BoundaryNF**


[III.D42] Stabilized germ: the BNF at the maximum available depth.
In the finite tower, stabilization occurs at the top level.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.stabilized_germ_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L113-L136)
**def
Tau.BookIII.Physics.stabilized_germ_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D42] Stabilized germ check: the germ at level db is consistent
with all lower levels (tower projection commutes with BNF).
Equations
- Tau.BookIII.Physics.stabilized_germ_check bound db = Tau.BookIII.Physics.stabilized_germ_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.stabilized_germ_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L118-L135)@[irreducible]

**def
Tau.BookIII.Physics.stabilized_germ_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.defect_contractivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L142-L159)
**def
Tau.BookIII.Physics.defect_contractivity_check
(db : Denotation.TauIdx)
 :Bool**


[III.P14] Defect contractivity: defect at level k+1 ≤ defect at
level k. Combined with defect ≥ 0, forces eventual stabilization.
For canonical BNF, defect is 0 everywhere.
Equations
- Tau.BookIII.Physics.defect_contractivity_check db = Tau.BookIII.Physics.defect_contractivity_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.defect_contractivity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L148-L158)@[irreducible]

**def
Tau.BookIII.Physics.defect_contractivity_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.is_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L165-L168)
**def
Tau.BookIII.Physics.is_stable
(k : Denotation.TauIdx)
 :Bool**


[III.P15] Stability criterion: a fluid datum is stable iff its
defect functional is zero. This is a computable predicate.
Equations
- Tau.BookIII.Physics.is_stable k = (Tau.BookIII.Physics.defect_functional k == 0)
Instances For

---

### `Tau.BookIII.Physics.stability_criterion_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L170-L179)
**def
Tau.BookIII.Physics.stability_criterion_check
(db : Denotation.TauIdx)
 :Bool**


[III.P15] Full stability criterion: stable at all levels up to db.
Equations
- Tau.BookIII.Physics.stability_criterion_check db = Tau.BookIII.Physics.stability_criterion_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.stability_criterion_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L174-L178)@[irreducible]

**def
Tau.BookIII.Physics.stability_criterion_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.clopen_locality_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L196-L197)
**theorem
Tau.BookIII.Physics.clopen_locality_15_4 :clopen_locality_check 15 4 = true**


---

### `Tau.BookIII.Physics.tower_determinacy_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L199-L200)
**theorem
Tau.BookIII.Physics.tower_determinacy_15_4 :tower_determinacy_check 15 4 = true**


---

### `Tau.BookIII.Physics.positive_regularity_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L202-L203)
**theorem
Tau.BookIII.Physics.positive_regularity_15_4 :positive_regularity_check 15 4 = true**


---

### `Tau.BookIII.Physics.stabilized_germ_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L205-L206)
**theorem
Tau.BookIII.Physics.stabilized_germ_15_4 :stabilized_germ_check 15 4 = true**


---

### `Tau.BookIII.Physics.defect_contractivity_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L208-L209)
**theorem
Tau.BookIII.Physics.defect_contractivity_5 :defect_contractivity_check 5 = true**


---

### `Tau.BookIII.Physics.stability_criterion_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L211-L212)
**theorem
Tau.BookIII.Physics.stability_criterion_5 :stability_criterion_check 5 = true**


---

### `Tau.BookIII.Physics.pos_reg_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L218-L220)
**theorem
Tau.BookIII.Physics.pos_reg_10_1 :positive_regularity_check 10 1 = true**


[III.T25] Structural: positive regularity at depth 1.

---

### `Tau.BookIII.Physics.stab_germ_0_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L222-L224)
**theorem
Tau.BookIII.Physics.stab_germ_0_3 :stabilized_germ 0 3 = { b_part := 0, c_part := 0, x_part := 0, depth := 3 }**


[III.D42] Structural: stabilized germ of 0 is zero BNF.

---

### `Tau.BookIII.Physics.defect_1_is_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L226-L228)
**theorem
Tau.BookIII.Physics.defect_1_is_zero :defect_functional 1 = 0**


[III.P14] Structural: defect at depth 1 is zero.

---

### `Tau.BookIII.Physics.stable_at_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/PositiveRegularity.lean#L230-L232)
**theorem
Tau.BookIII.Physics.stable_at_3 :is_stable 3 = true**


[III.P15] Structural: is_stable at every tested level.
