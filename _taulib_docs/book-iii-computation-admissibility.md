---
layout: taulib-doc
title: "TauLib.BookIII.Computation.Admissibility"
permalink: /verify/taulib/docs/book-iii-computation-admissibility/
lane: verify
module_name: "TauLib.BookIII.Computation.Admissibility"
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

# TauLib.BookIII.Computation.Admissibility


Interface Width, τ-Admissibility (E₂), Interface Width Principle,
and Earned Admissibility.

## Registry Cross-References


- [III.D53] Interface Width -- `interface_width`, `interface_width_check`

- [III.D54] τ-Admissibility (E₂) -- `tau_admissible_check`

- [III.T31] Interface Width Principle -- `width_principle_check`

- [III.P21] Earned Admissibility -- `earned_admissibility_check`


## Mathematical Content


**III.D53 (Interface Width):** w(f, n) = primorial stages before computation
stabilizes. W(f) = sup_n w(f, n). Extends Book I's interface width (I.D71)
to the E₂ enrichment level.

**III.D54 (τ-Admissibility at E₂):** f is τ-admissible iff W(f) < ∞.
Every τ-admissible function is determined by a single finite quotient.

**III.T31 (Interface Width Principle):** τ-admissible functions are determined
by ℤ/Prim(k₀)ℤ for some finite k₀. The infinite tower collapses to one level.

**III.P21 (Earned Admissibility):** The canonical characters χ₊, χ₋, id are
admissible with W ≤ 1. Composition is sub-additive: W(g∘f) ≤ W(f) + W(g).

---

### `Tau.BookIII.Computation.interface_width`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L43-L62)
**def
Tau.BookIII.Computation.interface_width
(x db : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D53] Interface width at a single input: the depth at which
the TTM computation stabilizes. Returns the first k where running
4 steps gives the same register-A value as at depth k+1.
Equations
- Tau.BookIII.Computation.interface_width x db = Tau.BookIII.Computation.interface_width.go db x 1 (db + 1)
Instances For

---

### `Tau.BookIII.Computation.interface_width.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L49-L61)@[irreducible]

**def
Tau.BookIII.Computation.interface_width.go
(db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.interface_width_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L64-L74)
**def
Tau.BookIII.Computation.interface_width_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D53] Interface width check: all inputs have finite width ≤ db.
Equations
- Tau.BookIII.Computation.interface_width_check bound db = Tau.BookIII.Computation.interface_width_check.go bound db 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Computation.interface_width_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L68-L73)@[irreducible]

**def
Tau.BookIII.Computation.interface_width_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.tau_admissible_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L80-L106)
**def
Tau.BookIII.Computation.tau_admissible_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D54] τ-admissibility at E₂: a computation is τ-admissible if
its interface width is finite. At the finite level, we check that
the width is bounded by db.
Equations
- Tau.BookIII.Computation.tau_admissible_check bound db = Tau.BookIII.Computation.tau_admissible_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.tau_admissible_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L86-L105)@[irreducible]

**def
Tau.BookIII.Computation.tau_admissible_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.width_principle_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L112-L132)
**def
Tau.BookIII.Computation.width_principle_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T31] Interface width principle: once stable, the computation at
higher levels agrees with the stable level (one quotient suffices).
Equations
- Tau.BookIII.Computation.width_principle_check bound db = Tau.BookIII.Computation.width_principle_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.width_principle_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L117-L131)@[irreducible]

**def
Tau.BookIII.Computation.width_principle_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.earned_admissibility_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L138-L164)
**def
Tau.BookIII.Computation.earned_admissibility_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P21] Earned admissibility: canonical operations are τ-admissible.
Identity, χ₊ (B-projection), χ₋ (C-projection) all have width ≤ 1.
Equations
- Tau.BookIII.Computation.earned_admissibility_check bound db = Tau.BookIII.Computation.earned_admissibility_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.earned_admissibility_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L143-L163)@[irreducible]

**def
Tau.BookIII.Computation.earned_admissibility_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.composition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L166-L190)
**def
Tau.BookIII.Computation.composition_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P21] Composition sub-additivity: compositions of admissible
operations stay admissible.
Equations
- Tau.BookIII.Computation.composition_check bound db = Tau.BookIII.Computation.composition_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.composition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L171-L189)@[irreducible]

**def
Tau.BookIII.Computation.composition_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.interface_width_10_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L207-L208)
**theorem
Tau.BookIII.Computation.interface_width_10_4 :interface_width_check 10 4 = true**


---

### `Tau.BookIII.Computation.tau_admissible_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L210-L211)
**theorem
Tau.BookIII.Computation.tau_admissible_10_3 :tau_admissible_check 10 3 = true**


---

### `Tau.BookIII.Computation.width_principle_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L213-L214)
**theorem
Tau.BookIII.Computation.width_principle_10_3 :width_principle_check 10 3 = true**


---

### `Tau.BookIII.Computation.earned_admissibility_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L216-L217)
**theorem
Tau.BookIII.Computation.earned_admissibility_15_4 :earned_admissibility_check 15 4 = true**


---

### `Tau.BookIII.Computation.composition_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L219-L220)
**theorem
Tau.BookIII.Computation.composition_15_4 :composition_check 15 4 = true**


---

### `Tau.BookIII.Computation.width_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L226-L228)
**theorem
Tau.BookIII.Computation.width_bounded :interface_width 42 5 ≤ 5**


[III.D53] Structural: width at depth 0 is at most 1.

---

### `Tau.BookIII.Computation.admissible_10_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L230-L232)
**theorem
Tau.BookIII.Computation.admissible_10_1 :tau_admissible_check 10 1 = true**


[III.D54] Structural: admissibility at depth 1.

---

### `Tau.BookIII.Computation.id_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/Admissibility.lean#L234-L236)
**theorem
Tau.BookIII.Computation.id_admissible :earned_admissibility_check 10 1 = true**


[III.P21] Structural: identity is trivially admissible.
