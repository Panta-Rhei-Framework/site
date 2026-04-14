---
layout: taulib-doc
title: "TauLib.BookII.Domains.Ultrametric"
permalink: /verify/taulib/docs/book-ii-domains-ultrametric/
lane: verify
module_name: "TauLib.BookII.Domains.Ultrametric"
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

# TauLib.BookII.Domains.Ultrametric


First disagreement depth and ultrametric structure on Ẑ_τ.

## Registry Cross-References


- [II.D12] First Disagreement Depth — `disagree_depth`

- [II.D13] Ultrametric Distance — `ultra_dist` (encoded as depth)

- [II.T05] Ultrametric Inequality — `triangle_check`

- [II.P04] Cylinders = Balls — `cyl_eq_ball_check`


## Mathematical Content


δ(x, y) = max { k : π_k(x) = π_k(y) }
d(x, y) = 2^{-δ(x,y)}, d(x, x) = 0

Ultrametric: d(x,z) ≤ max(d(x,y), d(y,z))
Equivalently: δ(x,z) ≥ min(δ(x,y), δ(y,z))

Cylinder-ball correspondence: C_k(x) = { y : δ(x,y) ≥ k }

---

### `Tau.BookII.Domains.disagree_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L34-L46)
**def
Tau.BookII.Domains.disagree_depth
(x y bound : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D12] First disagreement depth δ(x, y).
Returns max { k : π_k(x) = π_k(y) } for k ≤ bound.
If they agree for all k ≤ bound, returns bound + 1 (∞ proxy).
Stage 0 always agrees (primorial 0 = 1), so δ ≥ 0.
Equations
- Tau.BookII.Domains.disagree_depth x y bound = Tau.BookII.Domains.disagree_depth.go x y bound 0 (bound + 2)
Instances For

---

### `Tau.BookII.Domains.disagree_depth.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L41-L45)@[irreducible]

**def
Tau.BookII.Domains.disagree_depth.go
(x y bound : Denotation.TauIdx)

(k fuel : Nat)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.ultra_dist`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L52-L57)
**def
Tau.BookII.Domains.ultra_dist
(x y bound : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D13] Ultrametric distance encoded as agreement depth.
Higher depth = closer (smaller distance).
d(x,y) = 2^{-disagree_depth(x,y)}, d(x,x) = 0.
Convention: depth = bound + 1 represents d = 0 (identity).
Equations
- Tau.BookII.Domains.ultra_dist x y bound = Tau.BookII.Domains.disagree_depth x y bound
Instances For

---

### `Tau.BookII.Domains.symmetry_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L59-L69)
**def
Tau.BookII.Domains.symmetry_check
(bound : Denotation.TauIdx)
 :Bool**


Symmetry: δ(x,y) = δ(y,x). Flat double loop.
Equations
- Tau.BookII.Domains.symmetry_check bound = Tau.BookII.Domains.symmetry_check.go bound 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Domains.symmetry_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L63-L68)@[irreducible]

**def
Tau.BookII.Domains.symmetry_check.go
(bound : Denotation.TauIdx)

(x y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.nondegen_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L71-L82)
**def
Tau.BookII.Domains.nondegen_check
(bound : Denotation.TauIdx)
 :Bool**


Non-degeneracy: δ(x,x) = ∞ and δ(x,y) < ∞ for x ≠ y.
Equations
- Tau.BookII.Domains.nondegen_check bound = Tau.BookII.Domains.nondegen_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Domains.nondegen_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L75-L81)@[irreducible]

**def
Tau.BookII.Domains.nondegen_check.go
(bound : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.triangle_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L88-L105)
**def
Tau.BookII.Domains.triangle_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T05] Ultrametric triangle inequality:
δ(x,z) ≥ min(δ(x,y), δ(y,z)) for all x, y, z ∈ [2, bound].
Equivalent to d(x,z) ≤ max(d(x,y), d(y,z)).
Uses a flat triple loop with single fuel counter.
Equations
- Tau.BookII.Domains.triangle_check bound db = Tau.BookII.Domains.triangle_check.go bound db 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Domains.triangle_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L95-L104)@[irreducible]

**def
Tau.BookII.Domains.triangle_check.go
(bound db : Denotation.TauIdx)

(x y z fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.cyl_eq_ball_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L111-L123)
**def
Tau.BookII.Domains.cyl_eq_ball_check
(k center bound db : Denotation.TauIdx)
 :Bool**


[II.P04] C_k(x) = B(x, 2^{-k}) = { y : δ(x,y) ≥ k }.
Cylinder membership and ultrametric ball membership coincide.
Equations
- Tau.BookII.Domains.cyl_eq_ball_check k center bound db = Tau.BookII.Domains.cyl_eq_ball_check.go k center bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Domains.cyl_eq_ball_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L116-L122)@[irreducible]

**def
Tau.BookII.Domains.cyl_eq_ball_check.go
(k center bound db : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.sym_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L142-L142)
**theorem
Tau.BookII.Domains.sym_15 :symmetry_check 15 = true**


---

### `Tau.BookII.Domains.nondegen_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L143-L143)
**theorem
Tau.BookII.Domains.nondegen_15 :nondegen_check 15 = true**


---

### `Tau.BookII.Domains.triangle_8_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L144-L144)
**theorem
Tau.BookII.Domains.triangle_8_5 :triangle_check 8 5 = true**


---

### `Tau.BookII.Domains.cyl_ball_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L145-L145)
**theorem
Tau.BookII.Domains.cyl_ball_k1 :cyl_eq_ball_check 1 3 20 5 = true**


---

### `Tau.BookII.Domains.cyl_ball_k2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Ultrametric.lean#L146-L146)
**theorem
Tau.BookII.Domains.cyl_ball_k2 :cyl_eq_ball_check 2 7 30 5 = true**
