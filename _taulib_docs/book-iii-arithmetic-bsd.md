---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.BSD"
permalink: /verify/taulib/docs/book-iii-arithmetic-bsd/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.BSD"
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

# TauLib.BookIII.Arithmetic.BSD


BSD Coherence Theorem and BSD Three-Ingredient Proof.

## Registry Cross-References


- [III.T35] BSD Coherence Theorem -- `bsd_coherence_check`

- [III.P27] BSD Three-Ingredient Proof -- `bsd_three_ingredient_check`


## Mathematical Content


**III.T35 (BSD Coherence):** For τ-admissible elliptic data, BSD_τ(k) stabilizes
and equals the rank of the τ-rational point group. The functional encodes
the analytic rank (L-value derivative) and the algebraic rank (tower depth).

**III.P27 (BSD Three-Ingredient Proof):** BSD coherence follows from three
ingredients: (1) rank stabilization at finite depth, (2) L-value stabilization
via primorial cofinality, (3) E₁ Mutual Determination equality.

---

### `Tau.BookIII.Arithmetic.bsd_coherence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L36-L55)
**def
Tau.BookIII.Arithmetic.bsd_coherence_check
(db : Denotation.TauIdx)
 :Bool**


[III.T35] BSD coherence: the BSD functional stabilizes across depths.
BSD_τ(k) at k is compatible with BSD_τ(k+1) at k+1.
Equations
- Tau.BookIII.Arithmetic.bsd_coherence_check db = Tau.BookIII.Arithmetic.bsd_coherence_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_coherence_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L41-L54)@[irreducible]

**def
Tau.BookIII.Arithmetic.bsd_coherence_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_rank_agreement_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L57-L86)
**def
Tau.BookIII.Arithmetic.bsd_rank_agreement_check
(db : Denotation.TauIdx)
 :Bool**


[III.T35] BSD functional-rank agreement: the BSD functional at level k
is related to the number of stabilized rational points.
Equations
- Tau.BookIII.Arithmetic.bsd_rank_agreement_check db = Tau.BookIII.Arithmetic.bsd_rank_agreement_check.go db 0 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_rank_agreement_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L62-L79)@[irreducible]

**def
Tau.BookIII.Arithmetic.bsd_rank_agreement_check.go
(db : Denotation.TauIdx)

(dummy k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_rank_agreement_check.check_all_rational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L81-L85)@[irreducible]

**def
Tau.BookIII.Arithmetic.bsd_rank_agreement_check.check_all_rational
(x pk k fuel2 : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_three_ingredient_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L92-L117)
**def
Tau.BookIII.Arithmetic.bsd_three_ingredient_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P27] BSD three-ingredient proof:
(1) Rank stabilization: ranks are bounded
(2) L-value stabilization: split-zeta products stabilize
(3) E₁ MD equality: boundary determines interior determines spectral
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_three_ingredient_check.l_value_stab_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L106-L116)@[irreducible]

**def
Tau.BookIII.Arithmetic.bsd_three_ingredient_check.l_value_stab_go
(k db fuel : ℕ)
 :Bool**


L-value stabilization: B and C products at k divide those at k+1.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_coherence_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L131-L132)
**theorem
Tau.BookIII.Arithmetic.bsd_coherence_5 :bsd_coherence_check 5 = true**


---

### `Tau.BookIII.Arithmetic.bsd_rank_agreement_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L134-L135)
**theorem
Tau.BookIII.Arithmetic.bsd_rank_agreement_4 :bsd_rank_agreement_check 4 = true**


---

### `Tau.BookIII.Arithmetic.bsd_three_ingredient_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L137-L138)
**theorem
Tau.BookIII.Arithmetic.bsd_three_ingredient_15_3 :bsd_three_ingredient_check 15 3 = true**


---

### `Tau.BookIII.Arithmetic.bsd_coherence_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L144-L146)
**theorem
Tau.BookIII.Arithmetic.bsd_coherence_1 :bsd_coherence_check 1 = true**


[III.T35] Structural: BSD coherence at depth 1.

---

### `Tau.BookIII.Arithmetic.bsd_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L148-L149)
**theorem
Tau.BookIII.Arithmetic.bsd_level :Doors.problem_level Doors.MillenniumProblem.BSD = Enrichment.EnrLevel.E2**


[III.P27] Structural: BSD is at E₁→E₂ interface.

---

### `Tau.BookIII.Arithmetic.bsd_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/BSD.lean#L150-L150)
**theorem
Tau.BookIII.Arithmetic.bsd_part :Doors.problem_part Doors.MillenniumProblem.BSD = 6**
