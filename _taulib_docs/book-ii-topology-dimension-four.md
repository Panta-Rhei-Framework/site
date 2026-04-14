---
layout: taulib-doc
title: "TauLib.BookII.Topology.DimensionFour"
permalink: /verify/taulib/docs/book-ii-topology-dimension-four/
lane: verify
module_name: "TauLib.BookII.Topology.DimensionFour"
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

# TauLib.BookII.Topology.DimensionFour


τ-dimension = 4 from ABCD chart independence.

## Registry Cross-References


- [II.D15] τ-Dimension — `tau_dim`

- [II.T11] Dimension Four — `dim_four_check`

- [II.D16] Radial-Solenoidal Split — `radial_solenoidal_check`


## Mathematical Content


dim_τ := min { r : r independent refinement rays separate all points }

Theorem: dim_τ = 4.


- Upper bound: ABCD chart gives 4 coordinates separating all points.

- Lower bound: no triple of rays suffices (each triple leaves one
degree of freedom).


Forced asymmetry: 4 = 1 (radial D) + 3 (solenoidal A, B, C).
The 1+3 split cannot be eliminated by relabeling.

---

### `Tau.BookII.Topology.abcd_coords`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L37-L40)
**def
Tau.BookII.Topology.abcd_coords
(x : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx**


ABCD coordinates of a τ-index.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.tau_dim`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L42-L44)
**def
Tau.BookII.Topology.tau_dim :Nat**


[II.D15] τ-dimension: minimum number of independent coordinates
needed to separate all points.
Equations
- Tau.BookII.Topology.tau_dim = 4
Instances For

---

### `Tau.BookII.Topology.four_suffice_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L50-L62)
**def
Tau.BookII.Topology.four_suffice_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T11, upper bound] Four coordinates suffice:
ABCD chart is injective (no two distinct X share coordinates).
Equations
- Tau.BookII.Topology.four_suffice_check bound = Tau.BookII.Topology.four_suffice_check.go bound 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Topology.four_suffice_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L55-L61)@[irreducible]

**def
Tau.BookII.Topology.four_suffice_check.go
(bound : Denotation.TauIdx)

(x y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.three_insufficient_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L64-L84)
**def
Tau.BookII.Topology.three_insufficient_check :Bool**


[II.T11, lower bound] Three coordinates don't suffice:
exhibit pairs that agree on 3 coords but differ on 4th.

Missing D: 12=(3,1,1,4) and 3=(3,1,1,1) share A,B,C but differ in D.
Missing A: 2=(2,1,1,1) and 3=(3,1,1,1) share B,C,D but differ in A.
Missing B: 8=(2,3,1,1) and 2=(2,1,1,1) share A,C,D but differ in B.
Missing C: 64=(2,3,2,1) and 8=(2,3,1,1) share A,B,D but differ in C.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.dim_four_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L86-L88)
**def
Tau.BookII.Topology.dim_four_check
(bound : Denotation.TauIdx)
 :Bool**


Full dimension 4 verification.
Equations
- Tau.BookII.Topology.dim_four_check bound = (Tau.BookII.Topology.four_suffice_check bound && Tau.BookII.Topology.three_insufficient_check)
Instances For

---

### `Tau.BookII.Topology.radial_solenoidal_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L94-L113)
**def
Tau.BookII.Topology.radial_solenoidal_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D16] The 1+3 split: D is radial (remainder after extraction),
A,B,C are solenoidal (tower features).

Asymmetry evidence:


- D ranges over [0, M_k) (super-exponential growth)

- A,B,C bounded by prime at each stage

- Constraint C3 couples D to A (not conversely)

Equations
- Tau.BookII.Topology.radial_solenoidal_check bound = Tau.BookII.Topology.radial_solenoidal_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Topology.radial_solenoidal_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L104-L112)@[irreducible]

**def
Tau.BookII.Topology.radial_solenoidal_check.go
(bound : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.pairwise_independent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L115-L127)
**def
Tau.BookII.Topology.pairwise_independent_check :Bool**


Pairwise independence of coordinates: for each pair,
exhibit elements varying one while holding the other fixed.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.four_suff_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L145-L145)
**theorem
Tau.BookII.Topology.four_suff_50 :four_suffice_check 50 = true**


---

### `Tau.BookII.Topology.three_insuff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L146-L146)
**theorem
Tau.BookII.Topology.three_insuff :three_insufficient_check = true**


---

### `Tau.BookII.Topology.dim_four_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L147-L147)
**theorem
Tau.BookII.Topology.dim_four_50 :dim_four_check 50 = true**


---

### `Tau.BookII.Topology.rad_sol_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L148-L148)
**theorem
Tau.BookII.Topology.rad_sol_50 :radial_solenoidal_check 50 = true**


---

### `Tau.BookII.Topology.pairwise_ind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/DimensionFour.lean#L149-L149)
**theorem
Tau.BookII.Topology.pairwise_ind :pairwise_independent_check = true**
