---
layout: taulib-doc
title: "TauLib.BookII.Geometry.Betweenness"
permalink: /verify/taulib/docs/book-ii-geometry-betweenness/
lane: verify
module_name: "TauLib.BookII.Geometry.Betweenness"
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

# TauLib.BookII.Geometry.Betweenness


Betweenness relation from ultrametric distance, executing the Tarski program.

## Registry Cross-References


- [II.D19] Betweenness Relation — `between`

- [II.T15] Betweenness Axioms — `between_identity_check`, `between_connectivity_check`


## Mathematical Content


B(x,y,z) ⟺ δ(x,z) = min(δ(x,y), δ(y,z))

Equivalently: y lies "between" x and z in the ultrametric tree if
y agrees with both endpoints up to their mutual divergence depth.

Tarski axioms:


- T1 (Identity): B(x,y,x) ⟹ x = y

- T2 (Transitivity): B(x,y,z) ∧ B(y,z,w) ⟹ B(x,y,w)

- T3 (Connectivity): For any triple, at least one betweenness holds
(stronger than Tarski: ALL triples, not just collinear)


---

### `Tau.BookII.Geometry.between`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L35-L42)
**def
Tau.BookII.Geometry.between
(x y z db : Denotation.TauIdx)
 :Bool**


[II.D19] Ultrametric betweenness: B(x,y,z) iff
δ(x,z) = min(δ(x,y), δ(y,z)).
y lies on the geodesic from x to z in the profinite tree.
Equations
- Tau.BookII.Geometry.between x y z db = (Tau.BookII.Domains.disagree_depth x z db == min (Tau.BookII.Domains.disagree_depth x y db) (Tau.BookII.Domains.disagree_depth y z db))
Instances For

---

### `Tau.BookII.Geometry.between_identity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L48-L61)
**def
Tau.BookII.Geometry.between_identity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T15, T1] Identity: B(x,y,x) ⟹ x = y.
If δ(x,x) = min(δ(x,y), δ(y,x)), then δ(x,y) = ∞, so x = y.
Check: B(x,y,x) is true only when x = y.
Equations
- Tau.BookII.Geometry.between_identity_check bound db = Tau.BookII.Geometry.between_identity_check.go bound db 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Geometry.between_identity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L54-L60)@[irreducible]

**def
Tau.BookII.Geometry.between_identity_check.go
(bound db : Denotation.TauIdx)

(x y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.between_connectivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L63-L77)
**def
Tau.BookII.Geometry.between_connectivity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T15, T3] Connectivity: for any x, y, z, at least one of
B(x,y,z), B(y,x,z), B(x,z,y) holds.
Ultrametric isosceles property guarantees this.
Equations
- Tau.BookII.Geometry.between_connectivity_check bound db = Tau.BookII.Geometry.between_connectivity_check.go bound db 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Geometry.between_connectivity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L69-L76)@[irreducible]

**def
Tau.BookII.Geometry.between_connectivity_check.go
(bound db : Denotation.TauIdx)

(x y z fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.between_transitivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L79-L95)
**def
Tau.BookII.Geometry.between_transitivity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T15, T2] Outer transitivity: B(x,y,z) ∧ B(x,z,w) ⟹ B(x,y,w).
If y is between x and z, and z is between x and w,
then y is between x and w (monotonic along rays from x).
Verified exhaustively for small range.
Equations
- Tau.BookII.Geometry.between_transitivity_check bound db = Tau.BookII.Geometry.between_transitivity_check.go bound db 2 2 2 2
 ((bound + 1) * (bound + 1) * (bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Geometry.between_transitivity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L86-L94)@[irreducible]

**def
Tau.BookII.Geometry.between_transitivity_check.go
(bound db : Denotation.TauIdx)

(x y z w fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.identity_10`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L114-L114)
**theorem
Tau.BookII.Geometry.identity_10 :between_identity_check 10 5 = true**


---

### `Tau.BookII.Geometry.connectivity_8`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L115-L115)
**theorem
Tau.BookII.Geometry.connectivity_8 :between_connectivity_check 8 5 = true**


---

### `Tau.BookII.Geometry.transitivity_6`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Betweenness.lean#L116-L116)
**theorem
Tau.BookII.Geometry.transitivity_6 :between_transitivity_check 6 5 = true**
