---
layout: taulib-doc
title: "TauLib.BookII.Closure.Curvature"
permalink: /verify/taulib/docs/book-ii-closure-curvature/
lane: verify
module_name: "TauLib.BookII.Closure.Curvature"
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

# TauLib.BookII.Closure.Curvature


Curvature and geodesics on the primorial tower.

## Registry Cross-References


- [II.D80] τ-Curvature — `curvature_check`

- [II.D81] τ-Geodesic — `geodesic_check`

- [II.T51] Flat Curvature Vanishing — `flat_curvature_vanishes`

- [II.P17] Geodesic Completeness — `geodesic_completeness_check`

- [II.T52] Lemniscate Holonomy — `lemniscate_holonomy_check`


## Mathematical Content


**II.D80 (τ-Curvature):** Curvature measures the failure of parallel transport
to commute: R(v,w)(x) = Γ(Γ(x,v),w) - Γ(Γ(x,w),v). For the flat connection
on Z/M_k Z, curvature vanishes identically because addition is commutative.

**II.D81 (τ-Geodesic):** A geodesic is a path of minimal length connecting
two points in Z/M_k Z. In the discrete metric, a geodesic from x to y is
any path of length |x-y| mod M_k.

**II.T51 (Flat Curvature Vanishing):** R = 0 for the canonical flat connection.
This is the statement that Z/M_k Z has zero curvature at each stage.

**II.P17 (Geodesic Completeness):** Every geodesic can be extended indefinitely
(Z/M_k Z is compact, hence complete). This holds at every finite stage.

**II.T52 (Lemniscate Holonomy):** The profinite limit acquires nontrivial
holonomy from the fundamental group π₁(L) ≅ ℤ of the lemniscate boundary.
The holonomy representation maps the generator of π₁(L) to a rotation in
the fiber T².

---

### `Tau.BookII.Closure.curvature_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L49-L72)
**def
Tau.BookII.Closure.curvature_check
(conn : TauConnection)

(k : ℕ)
 :Bool**


[II.D80] Curvature check: R(v,w)(x) = Γ(Γ(x,v),w) - Γ(Γ(x,w),v).
For a flat connection, this should be 0.
Equations
- Tau.BookII.Closure.curvature_check conn k = Tau.BookII.Closure.curvature_check.go conn k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.curvature_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L55-L58)@[irreducible]

**def
Tau.BookII.Closure.curvature_check.go
(conn : TauConnection)

(k x pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.curvature_check.go_v`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L60-L63)@[irreducible]

**def
Tau.BookII.Closure.curvature_check.go_v
(conn : TauConnection)

(k x v pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.curvature_check.go_w`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L65-L71)@[irreducible]

**def
Tau.BookII.Closure.curvature_check.go_w
(conn : TauConnection)

(k x v w pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.cyclic_distance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L78-L83)
**def
Tau.BookII.Closure.cyclic_distance
(x y k : ℕ)
 :ℕ**


[II.D81] Distance in Z/M_k Z: min(|x-y|, M_k - |x-y|).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geodesic_direction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L85-L90)
**def
Tau.BookII.Closure.geodesic_direction
(x y k : ℕ)
 :ℕ**


[II.D81] A geodesic from x to y at stage k: the shortest path.
Returns the direction vector.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geodesic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L92-L109)
**def
Tau.BookII.Closure.geodesic_check
(k : ℕ)
 :Bool**


[II.D81] Check that the geodesic direction transports x to y.
Equations
- Tau.BookII.Closure.geodesic_check k = Tau.BookII.Closure.geodesic_check.go k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.geodesic_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L97-L100)@[irreducible]

**def
Tau.BookII.Closure.geodesic_check.go
(k x pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geodesic_check.go_y`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L102-L108)@[irreducible]

**def
Tau.BookII.Closure.geodesic_check.go_y
(k x y pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geodesic_completeness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L115-L134)
**def
Tau.BookII.Closure.geodesic_completeness_check
(k : ℕ)
 :Bool**


[II.P17] Geodesic completeness check: from any point x, transport in
any direction v stays within Z/M_k Z and can be iterated.
Equations
- Tau.BookII.Closure.geodesic_completeness_check k = Tau.BookII.Closure.geodesic_completeness_check.go k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.geodesic_completeness_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L121-L126)@[irreducible]

**def
Tau.BookII.Closure.geodesic_completeness_check.go
(k x pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geodesic_completeness_check.go_v`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L128-L133)@[irreducible]

**def
Tau.BookII.Closure.geodesic_completeness_check.go_v
(k x v pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.lemniscate_holonomy_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L140-L158)
**def
Tau.BookII.Closure.lemniscate_holonomy_check
(k : ℕ)
 :Bool**


[II.T52] The lemniscate L = S¹ ∨ S¹ has π₁(L) ≅ ℤ (free group on 1 gen).
The holonomy representation maps the generator to a "rotation" in the
fiber T². At stage k, this is the shift x ↦ x+1 mod M_k.

Check: the generator of the holonomy is the unit shift.
Equations
- Tau.BookII.Closure.lemniscate_holonomy_check k = (Tau.BookII.Closure.lemniscate_holonomy_check.go 0 1 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k) == Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.lemniscate_holonomy_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L152-L157)@[irreducible]

**def
Tau.BookII.Closure.lemniscate_holonomy_check.go
(pos step pk fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.flat_curvature_vanishes_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L164-L166)
**theorem
Tau.BookII.Closure.flat_curvature_vanishes_1 :curvature_check flat_connection 1 = true**


[II.T51] Flat curvature vanishes at stage 1.

---

### `Tau.BookII.Closure.flat_curvature_vanishes_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L168-L170)
**theorem
Tau.BookII.Closure.flat_curvature_vanishes_2 :curvature_check flat_connection 2 = true**


[II.T51] Flat curvature vanishes at stage 2.

---

### `Tau.BookII.Closure.geodesic_correct_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L172-L174)
**theorem
Tau.BookII.Closure.geodesic_correct_1 :geodesic_check 1 = true**


[II.D81] Geodesics are correct at stage 1.

---

### `Tau.BookII.Closure.geodesic_correct_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L176-L178)
**theorem
Tau.BookII.Closure.geodesic_correct_2 :geodesic_check 2 = true**


[II.D81] Geodesics are correct at stage 2.

---

### `Tau.BookII.Closure.geodesic_complete_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L180-L182)
**theorem
Tau.BookII.Closure.geodesic_complete_1 :geodesic_completeness_check 1 = true**


[II.P17] Geodesic completeness at stage 1.

---

### `Tau.BookII.Closure.geodesic_complete_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L184-L186)
**theorem
Tau.BookII.Closure.geodesic_complete_2 :geodesic_completeness_check 2 = true**


[II.P17] Geodesic completeness at stage 2.

---

### `Tau.BookII.Closure.lemniscate_holonomy_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L188-L190)
**theorem
Tau.BookII.Closure.lemniscate_holonomy_1 :lemniscate_holonomy_check 1 = true**


[II.T52] Lemniscate holonomy has order M_k at stage 1.

---

### `Tau.BookII.Closure.lemniscate_holonomy_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Curvature.lean#L192-L194)
**theorem
Tau.BookII.Closure.lemniscate_holonomy_2 :lemniscate_holonomy_check 2 = true**


[II.T52] Lemniscate holonomy has order M_k at stage 2.
