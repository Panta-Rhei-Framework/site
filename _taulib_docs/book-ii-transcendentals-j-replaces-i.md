---
layout: taulib-doc
title: "TauLib.BookII.Transcendentals.JReplacesI"
permalink: /verify/taulib/docs/book-ii-transcendentals-j-replaces-i/
lane: verify
module_name: "TauLib.BookII.Transcendentals.JReplacesI"
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

# TauLib.BookII.Transcendentals.JReplacesI


j replaces i: the split-complex unit j (j^2 = +1) replaces the
imaginary unit i (i^2 = -1) as the fundamental algebraic unit.

## Registry Cross-References


- [II.D32] Interior j-Unit -- `j_unit`, `j_squared_check`

- [II.D33] Bipolar Idempotents Interior -- `idempotent_check`

- [II.T24] j Replaces i -- `j_vs_i_check`


## Mathematical Content


The split-complex unit j with j^2 = +1 forces hyperbolic (wave) geometry
rather than elliptic (Laplacian) geometry. The idempotents e_+ = (1+j)/2
and e_- = (1-j)/2 provide the bipolar decomposition.

Key contrast:


- i^2 = -1 (Gaussian): rotation, elliptic PDE, NO nontrivial idempotents over Z

- j^2 = +1 (split-complex): polarity, wave PDE, idempotents e_+, e_-


The split-complex structure is FORCED by the bipolar prime partition (I.T10).
This module verifies the algebraic properties at the interior level.

---

### `Tau.BookII.Transcendentals.j_unit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L40-L41)
**def
Tau.BookII.Transcendentals.j_unit :Polarity.SplitComplex**


[II.D32] The interior j-unit: j = (0, 1) in SplitComplex.
Equations
- Tau.BookII.Transcendentals.j_unit = { re := 0, im := 1 }
Instances For

---

### `Tau.BookII.Transcendentals.j_squared_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L43-L45)
**def
Tau.BookII.Transcendentals.j_squared_check :Bool**


j^2 = 1: the defining property. (0,1)*(0,1) = (0*0+1*1, 0*1+1*0) = (1,0).
Equations
- Tau.BookII.Transcendentals.j_squared_check = (Tau.BookII.Transcendentals.j_unit.mul Tau.BookII.Transcendentals.j_unit == { re := 1, im := 0 })
Instances For

---

### `Tau.BookII.Transcendentals.j_nontrivial_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L47-L49)
**def
Tau.BookII.Transcendentals.j_nontrivial_check :Bool**


j is not trivial: j != 0 and j != 1.
Equations
- Tau.BookII.Transcendentals.j_nontrivial_check = (Tau.BookII.Transcendentals.j_unit != Tau.Polarity.SplitComplex.zero && Tau.BookII.Transcendentals.j_unit != Tau.Polarity.SplitComplex.one)
Instances For

---

### `Tau.BookII.Transcendentals.j_involution_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L51-L53)
**def
Tau.BookII.Transcendentals.j_involution_check :Bool**


Polarity involution: sigma(j) = -j.
Equations
- Tau.BookII.Transcendentals.j_involution_check = (Tau.Polarity.polarity_inv Tau.BookII.Transcendentals.j_unit == Tau.BookII.Transcendentals.j_unit.neg)
Instances For

---

### `Tau.BookII.Transcendentals.idempotent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L59-L75)
**def
Tau.BookII.Transcendentals.idempotent_check :Bool**


[II.D33] Bipolar idempotents in sector coordinates.
e_+ = (1, 0) and e_- = (0, 1) in SectorPair.

Algebraic properties:

- e_+^2 = e_+ (idempotent)

- e_-^2 = e_- (idempotent)

- e_+ * e_- = 0 (orthogonal)

- e_+ + e_- = (1,1) = unity

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.interior_projection_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L77-L87)
**def
Tau.BookII.Transcendentals.interior_projection_check :Bool**


Interior projection: idempotent action on interior bipolar pairs.
e_+ * (b, c) = (b, 0): keeps B-sector, kills C-sector.
e_- * (b, c) = (0, c): kills B-sector, keeps C-sector.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.j_vs_i_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L93-L111)
**def
Tau.BookII.Transcendentals.j_vs_i_check :Bool**


[II.T24] j replaces i: comprehensive comparison.

- j^2 = +1 (split-complex, hyperbolic)

- i^2 = -1 (Gaussian, elliptic)

- j admits nontrivial idempotents; i does not (I.T10)

- Zero divisors in H_tau witness polarity structure


The wave equation u_tt = u_xx comes from j^2 = +1.
The Laplace equation u_tt + u_xx = 0 would come from i^2 = -1.
Category tau chooses j (waves, polarity) over i (rotation).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.wave_vs_laplace_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L113-L123)
**def
Tau.BookII.Transcendentals.wave_vs_laplace_check :Bool**


Wave vs Laplace: the two signatures in sector coordinates.
j^2 = +1: sector product is componentwise (wave eq characteristic coords)
i^2 = -1: Gaussian product mixes components (elliptic)
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.interior_bipolar_via_j`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L129-L146)
**def
Tau.BookII.Transcendentals.interior_bipolar_via_j
(bound : Denotation.TauIdx)
 :Bool**


Every tau-admissible point inherits bipolar decomposition via j.
The B-coordinate maps to the e_+-sector, C to e_-.
Equations
- Tau.BookII.Transcendentals.interior_bipolar_via_j bound = Tau.BookII.Transcendentals.interior_bipolar_via_j.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Transcendentals.interior_bipolar_via_j.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L134-L145)@[irreducible]

**def
Tau.BookII.Transcendentals.interior_bipolar_via_j.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.j_sq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L171-L171)
**theorem
Tau.BookII.Transcendentals.j_sq :j_squared_check = true**


---

### `Tau.BookII.Transcendentals.j_nontriv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L172-L172)
**theorem
Tau.BookII.Transcendentals.j_nontriv :j_nontrivial_check = true**


---

### `Tau.BookII.Transcendentals.j_invol`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L173-L173)
**theorem
Tau.BookII.Transcendentals.j_invol :j_involution_check = true**


---

### `Tau.BookII.Transcendentals.idemp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L174-L174)
**theorem
Tau.BookII.Transcendentals.idemp :idempotent_check = true**


---

### `Tau.BookII.Transcendentals.int_proj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L175-L175)
**theorem
Tau.BookII.Transcendentals.int_proj :interior_projection_check = true**


---

### `Tau.BookII.Transcendentals.j_vs_i`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L176-L176)
**theorem
Tau.BookII.Transcendentals.j_vs_i :j_vs_i_check = true**


---

### `Tau.BookII.Transcendentals.wave_laplace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L177-L177)
**theorem
Tau.BookII.Transcendentals.wave_laplace :wave_vs_laplace_check = true**


---

### `Tau.BookII.Transcendentals.int_bipolar_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/JReplacesI.lean#L178-L178)
**theorem
Tau.BookII.Transcendentals.int_bipolar_30 :interior_bipolar_via_j 30 = true**
