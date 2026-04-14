---
layout: taulib-doc
title: "TauLib.BookII.Topology.BoundaryMinimality"
permalink: /verify/taulib/docs/book-ii-topology-boundary-minimality/
lane: verify
module_name: "TauLib.BookII.Topology.BoundaryMinimality"
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

# TauLib.BookII.Topology.BoundaryMinimality


Boundary minimality and angular sectors of the lemniscate.

## Registry Cross-References


- [II.T12] Boundary Minimality — `boundary_minimal_check`

- [II.D17] Angular Sectors — `angular_b_sector`, `angular_c_sector`

- [II.P05] Lobes as Clopen Sets — `lobes_clopen_check`


## Mathematical Content


Angular sectors are clopen subsets defined by B,C coordinates:
S⁺_k(b) = { (D,A,B,C) ∈ τ³ : B_k ≡ b (mod p_k) }
S⁻_k(c) = { (D,A,B,C) ∈ τ³ : C_k ≡ c (mod p_k) }

Boundary minimality (II.T12): ℒ = S¹∨S¹ is the minimal topological
quotient of T² preserving both gauge factors with a crossing point.

Lobes as clopen (II.P05): the two lobes L₊, L₋ are complementary
clopen subsets of ℒ \ {p₀}, profinite limits of angular sectors.

---

### `Tau.BookII.Topology.angular_b_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L37-L41)
**def
Tau.BookII.Topology.angular_b_sector
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D17] B-angular sector at stage k:
points with B-coordinate ≡ b (mod p_k).
Equations
- Tau.BookII.Topology.angular_b_sector x k = (Tau.BookII.Interior.from_tau_idx x).b % Tau.Polarity.nth_prime k
Instances For

---

### `Tau.BookII.Topology.angular_c_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L43-L47)
**def
Tau.BookII.Topology.angular_c_sector
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


C-angular sector at stage k:
points with C-coordinate ≡ c (mod p_k).
Equations
- Tau.BookII.Topology.angular_c_sector x k = (Tau.BookII.Interior.from_tau_idx x).c % Tau.Polarity.nth_prime k
Instances For

---

### `Tau.BookII.Topology.angular_sector_mem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L49-L51)
**def
Tau.BookII.Topology.angular_sector_mem
(k b_val c_val x : Denotation.TauIdx)
 :Bool**


Combined angular sector membership.
Equations
- Tau.BookII.Topology.angular_sector_mem k b_val c_val x = (Tau.BookII.Topology.angular_b_sector x k == b_val && Tau.BookII.Topology.angular_c_sector x k == c_val)
Instances For

---

### `Tau.BookII.Topology.lobe_class`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L57-L60)
**def
Tau.BookII.Topology.lobe_class
(x : Denotation.TauIdx)
 :Interior.FiberDominance**


Lobe classification: B-dominant (e₊-lobe), C-dominant (e₋-lobe),
or balanced (crossing point). Uses fiber dominance from II.D04.
Equations
- Tau.BookII.Topology.lobe_class x = (Tau.BookII.Interior.from_tau_idx x).fiber_dominance
Instances For

---

### `Tau.BookII.Topology.lobe_distribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L62-L74)
**def
Tau.BookII.Topology.lobe_distribution
(bound : Denotation.TauIdx)
 :ℕ × ℕ × ℕ**


Count B-dominant, C-dominant, and balanced points in range.
Equations
- Tau.BookII.Topology.lobe_distribution bound = Tau.BookII.Topology.lobe_distribution.go bound 2 (bound + 1) 0 0 0
Instances For

---

### `Tau.BookII.Topology.lobe_distribution.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L67-L73)@[irreducible]

**def
Tau.BookII.Topology.lobe_distribution.go
(bound : Denotation.TauIdx)

(x fuel b_ct c_ct bal : ℕ)
 :ℕ × ℕ × ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.lobes_exhaustive_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L80-L95)
**def
Tau.BookII.Topology.lobes_exhaustive_check
(bound : Denotation.TauIdx)
 :Bool**


[II.P05] Lobes are complementary: every point is B-dominant,
C-dominant, or balanced (no other possibility).
Equations
- Tau.BookII.Topology.lobes_exhaustive_check bound = Tau.BookII.Topology.lobes_exhaustive_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Topology.lobes_exhaustive_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L85-L94)@[irreducible]

**def
Tau.BookII.Topology.lobes_exhaustive_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.lobes_clopen_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L97-L112)
**def
Tau.BookII.Topology.lobes_clopen_check
(bound : Denotation.TauIdx)
 :Bool**


[II.P05] Angular sectors at each stage refine lobe membership:
B-dominant points have B ≥ C, C-dominant have C > B.
Equations
- Tau.BookII.Topology.lobes_clopen_check bound = Tau.BookII.Topology.lobes_clopen_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Topology.lobes_clopen_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L102-L111)@[irreducible]

**def
Tau.BookII.Topology.lobes_clopen_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.boundary_minimal_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L118-L132)
**def
Tau.BookII.Topology.boundary_minimal_check :Bool**


[II.T12] Boundary minimality evidence:
Two independent channels (B and C) cannot be collapsed to one.
Check: there exist points varying B with C fixed, and vice versa.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.crossing_point_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L134-L144)
**def
Tau.BookII.Topology.crossing_point_exists
(bound : Denotation.TauIdx)
 :Bool**


Crossing point witness: balanced points exist (B = C).
Equations
- Tau.BookII.Topology.crossing_point_exists bound = Tau.BookII.Topology.crossing_point_exists.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Topology.crossing_point_exists.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L138-L143)@[irreducible]

**def
Tau.BookII.Topology.crossing_point_exists.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.lobes_exhaust`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L164-L164)
**theorem
Tau.BookII.Topology.lobes_exhaust :lobes_exhaustive_check 50 = true**


---

### `Tau.BookII.Topology.lobes_clopen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L165-L165)
**theorem
Tau.BookII.Topology.lobes_clopen :lobes_clopen_check 50 = true**


---

### `Tau.BookII.Topology.bnd_minimal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L166-L166)
**theorem
Tau.BookII.Topology.bnd_minimal :boundary_minimal_check = true**


---

### `Tau.BookII.Topology.crossing_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/BoundaryMinimality.lean#L167-L167)
**theorem
Tau.BookII.Topology.crossing_exists :crossing_point_exists 100 = true**
