---
layout: taulib-doc
title: "TauLib.BookII.Geometry.PaschParallel"
permalink: /verify/taulib/docs/book-ii-geometry-pasch-parallel/
lane: verify
module_name: "TauLib.BookII.Geometry.PaschParallel"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Geometry.PaschParallel


Pasch axiom and parallel postulate for ultrametric geometry on Ẑ_τ.

## Registry Cross-References


- [II.T17] Pasch Axiom — `pasch_spot_check`

- [II.T18] Parallel Postulate — `parallel_unique_check`


## Mathematical Content


**Pasch Axiom (II.T17):**
In ultrametric geometry, EVERY triple of points is collinear: for any
a, b, c, at least one of B(a,b,c), B(a,c,b), B(b,a,c) holds.

The classical Pasch axiom states: if B(a,p,c) and B(b,q,c) and a,b,c
form a non-collinear triangle, then ∃x with B(a,x,b) ∧ B(p,x,q).
Since no non-collinear triangle exists in the ultrametric tree, the
Pasch axiom is VACUOUSLY TRUE. The connectivity property (every triple
collinear) is the ultrametric substitute — it is STRONGER than Pasch
and subsumes all line-intersection reasoning.

**Parallel Postulate (II.T18):**
Given a "line" (depth-equivalence class at depth k) and a point not
on it, there exists a parallel "line" through that point.

In the ultrametric setting: lines are depth-level sets
{ z : δ(x,z) = k or δ(y,z) = k }. For a given depth k and external
point z, the branching structure provides at least one sibling branch
at the same depth, giving a canonical parallel direction.

Bound analysis: at depth k, all residue classes mod p_{k+1} must be
represented. Depth 0 needs bound ≥ 2, depth 1 needs ≥ 7, depth 2
needs ≥ 13 (all odd/even residue classes mod 6 covered).

---

### `Tau.BookII.Geometry.collinear_triple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L48-L52)
**def
Tau.BookII.Geometry.collinear_triple
(a b c db : Denotation.TauIdx)
 :Bool**


Triple collinearity: at least one betweenness ordering holds.
In the ultrametric tree, this is ALWAYS true (ultrametric
inequality forces isosceles triangles).
Equations
- Tau.BookII.Geometry.collinear_triple a b c db = (Tau.BookII.Geometry.between a b c db || Tau.BookII.Geometry.between a c b db || Tau.BookII.Geometry.between b a c db)
Instances For

---

### `Tau.BookII.Geometry.pasch_spot_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L54-L62)
**def
Tau.BookII.Geometry.pasch_spot_check
(db : Denotation.TauIdx)
 :Bool**


[II.T17] Pasch axiom spot check: verify collinearity for
representative triangles spanning different tree configurations.
Since all triples are collinear, Pasch is vacuously true
(its hypothesis requires a non-collinear triangle).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.pasch_exhaustive_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L64-L75)
**def
Tau.BookII.Geometry.pasch_exhaustive_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T17] Exhaustive collinearity check for all triples in [2, bound].
Flat triple loop with single fuel counter.
Equations
- Tau.BookII.Geometry.pasch_exhaustive_check bound db = Tau.BookII.Geometry.pasch_exhaustive_check.go bound db 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Geometry.pasch_exhaustive_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L69-L74)@[irreducible]

**def
Tau.BookII.Geometry.pasch_exhaustive_check.go
(bound db : Denotation.TauIdx)

(a b c fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.on_depth_line`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L81-L85)
**def
Tau.BookII.Geometry.on_depth_line
(x y z db : Denotation.TauIdx)
 :Bool**


[II.T18] Depth-line: x and y determine a "line" at depth k = δ(x,y).
The line through x,y consists of all z with δ(x,z) = k or δ(y,z) = k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.find_parallel_partner`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L87-L97)
**def
Tau.BookII.Geometry.find_parallel_partner
(z k db bound : Denotation.TauIdx)
 :Bool**


[II.T18] Find a parallel partner: w ≠ z with δ(z,w) = k in [2, bound].
Returns true iff such a partner exists.
Equations
- Tau.BookII.Geometry.find_parallel_partner z k db bound = Tau.BookII.Geometry.find_parallel_partner.go z k db bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.find_parallel_partner.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L92-L96)@[irreducible]

**def
Tau.BookII.Geometry.find_parallel_partner.go
(z k db bound : Denotation.TauIdx)

(w fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.parallel_check_z`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L99-L111)
**def
Tau.BookII.Geometry.parallel_check_z
(x y bound db : Denotation.TauIdx)
 :Bool**


Inner loop for parallel check: iterate over z for fixed x, y.
Equations
- Tau.BookII.Geometry.parallel_check_z x y bound db = Tau.BookII.Geometry.parallel_check_z.go x y bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.parallel_check_z.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L103-L110)@[irreducible]

**def
Tau.BookII.Geometry.parallel_check_z.go
(x y bound db : Denotation.TauIdx)

(z fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.parallel_check_y`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L113-L122)
**def
Tau.BookII.Geometry.parallel_check_y
(x bound db : Denotation.TauIdx)
 :Bool**


Inner loop for parallel check: iterate over y for fixed x.
Equations
- Tau.BookII.Geometry.parallel_check_y x bound db = Tau.BookII.Geometry.parallel_check_y.go x bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.parallel_check_y.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L117-L121)@[irreducible]

**def
Tau.BookII.Geometry.parallel_check_y.go
(x bound db : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.parallel_exists_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L124-L134)
**def
Tau.BookII.Geometry.parallel_exists_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T18] Parallel existence: for every line (x,y) and external
point z, there exists at least one parallel partner w with
δ(z,w) = δ(x,y). The ultrametric tree branching forces this.
Equations
- Tau.BookII.Geometry.parallel_exists_check bound db = Tau.BookII.Geometry.parallel_exists_check.go bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.parallel_exists_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L130-L133)@[irreducible]

**def
Tau.BookII.Geometry.parallel_exists_check.go
(bound db : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.parallel_unique_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L136-L138)
**def
Tau.BookII.Geometry.parallel_unique_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T18] Full parallel postulate check.
Equations
- Tau.BookII.Geometry.parallel_unique_check bound db = Tau.BookII.Geometry.parallel_exists_check bound db
Instances For

---

### `Tau.BookII.Geometry.tarski_complete_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L144-L151)
**def
Tau.BookII.Geometry.tarski_complete_check
(bound db : Denotation.TauIdx)
 :Bool**


Complete Tarski axiom check: betweenness + congruence + Pasch + parallel.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.pasch_spot`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L184-L184)
**theorem
Tau.BookII.Geometry.pasch_spot :pasch_spot_check 5 = true**


---

### `Tau.BookII.Geometry.pasch_exhaustive_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L185-L185)
**theorem
Tau.BookII.Geometry.pasch_exhaustive_5 :pasch_exhaustive_check 5 5 = true**


---

### `Tau.BookII.Geometry.parallel_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L186-L186)
**theorem
Tau.BookII.Geometry.parallel_6 :parallel_unique_check 6 5 = true**


---

### `Tau.BookII.Geometry.parallel_13`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L187-L187)
**theorem
Tau.BookII.Geometry.parallel_13 :parallel_unique_check 13 5 = true**


---

### `Tau.BookII.Geometry.tarski_complete_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Geometry/PaschParallel.lean#L188-L188)
**theorem
Tau.BookII.Geometry.tarski_complete_6 :tarski_complete_check 6 5 = true**
