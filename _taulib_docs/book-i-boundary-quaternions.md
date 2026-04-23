---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Quaternions"
permalink: /verify/taulib/docs/book-i-boundary-quaternions/
lane: verify
module_name: "TauLib.BookI.Boundary.Quaternions"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Boundary.Quaternions


The elliptic quaternions: TauQuaternion = R_tau-algebra {1,i,j,k}.

## Registry Cross-References


- [I.D87] TauQuaternion — Elliptic quaternions over constructive reals

- [I.T44] Division Algebra — Hamilton product, i^2=j^2=k^2=ijk=-1

- [I.R22] Hurwitz — Only R, C, H, O are normed division algebras


## Ground Truth Sources


- Hamilton product structure: (a1+b1i+c1j+d1k)(a2+b2i+c2j+d2k)


## Mathematical Content


TauQuaternion is the 4-dimensional R_tau-algebra with basis {1,i,j,k}
satisfying i^2 = j^2 = k^2 = ijk = -1. This is a non-commutative
division algebra (the Hamilton quaternions over the constructive reals).

All operations are defined in terms of TauReal arithmetic. Equivalence
is componentwise TauReal.equiv. The key results are:


- i^2 = j^2 = k^2 = -1 (up to equiv)

- ijk = -1 (up to equiv)

- Non-commutativity: ij != ji

- Additive ring axioms (componentwise from TauReal)

- Multiplicative identity (one_mul, mul_one)


---

### `Tau.Boundary.TauQuaternion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L43-L49)
**structure
Tau.Boundary.TauQuaternion :Type**


[I.D87] TauQuaternion: elliptic quaternions over constructive reals.
Components: w (scalar/real), x (i), y (j), z (k).

- w : TauReal
- x : TauReal
- y : TauReal
- z : TauReal
Instances For

---

### `Tau.Boundary.TauQuaternion.equiv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L55-L58)
**def
Tau.Boundary.TauQuaternion.equiv
(a b : TauQuaternion)
 :Prop**


Two TauQuaternions are equivalent if all four components agree.
Equations
- a.equiv b = (a.w.equiv b.w ∧ a.x.equiv b.x ∧ a.y.equiv b.y ∧ a.z.equiv b.z)
Instances For

---

### `Tau.Boundary.TauQuaternion.equiv_refl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L60-L63)
**theorem
Tau.Boundary.TauQuaternion.equiv_refl
(a : TauQuaternion)
 :a.equiv a**


TauQuaternion equivalence is reflexive.

---

### `Tau.Boundary.TauQuaternion.equiv_symm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L65-L69)
**theorem
Tau.Boundary.TauQuaternion.equiv_symm
{a b : TauQuaternion}

(h : a.equiv b)
 :b.equiv a**


TauQuaternion equivalence is symmetric.

---

### `Tau.Boundary.TauQuaternion.zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L75-L77)
**def
Tau.Boundary.TauQuaternion.zero :TauQuaternion**


Quaternion zero: (0, 0, 0, 0).
Equations
- Tau.Boundary.TauQuaternion.zero = { w := Tau.Boundary.TauReal.zero, x := Tau.Boundary.TauReal.zero, y := Tau.Boundary.TauReal.zero,
 z := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.TauQuaternion.one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L79-L81)
**def
Tau.Boundary.TauQuaternion.one :TauQuaternion**


Quaternion one: (1, 0, 0, 0).
Equations
- Tau.Boundary.TauQuaternion.one = { w := Tau.Boundary.TauReal.one, x := Tau.Boundary.TauReal.zero, y := Tau.Boundary.TauReal.zero,
 z := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.TauQuaternion.qi`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L83-L85)
**def
Tau.Boundary.TauQuaternion.qi :TauQuaternion**


Quaternion i: (0, 1, 0, 0).
Equations
- Tau.Boundary.TauQuaternion.qi = { w := Tau.Boundary.TauReal.zero, x := Tau.Boundary.TauReal.one, y := Tau.Boundary.TauReal.zero,
 z := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.TauQuaternion.qj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L87-L89)
**def
Tau.Boundary.TauQuaternion.qj :TauQuaternion**


Quaternion j: (0, 0, 1, 0).
Equations
- Tau.Boundary.TauQuaternion.qj = { w := Tau.Boundary.TauReal.zero, x := Tau.Boundary.TauReal.zero, y := Tau.Boundary.TauReal.one,
 z := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.TauQuaternion.qk`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L91-L93)
**def
Tau.Boundary.TauQuaternion.qk :TauQuaternion**


Quaternion k: (0, 0, 0, 1).
Equations
- Tau.Boundary.TauQuaternion.qk = { w := Tau.Boundary.TauReal.zero, x := Tau.Boundary.TauReal.zero, y := Tau.Boundary.TauReal.zero,
 z := Tau.Boundary.TauReal.one }
Instances For

---

### `Tau.Boundary.TauQuaternion.add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L99-L101)
**def
Tau.Boundary.TauQuaternion.add
(a b : TauQuaternion)
 :TauQuaternion**


Quaternion addition: componentwise.
Equations
- a.add b = { w := a.w.add b.w, x := a.x.add b.x, y := a.y.add b.y, z := a.z.add b.z }
Instances For

---

### `Tau.Boundary.TauQuaternion.negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L103-L105)
**def
Tau.Boundary.TauQuaternion.negate
(a : TauQuaternion)
 :TauQuaternion**


Quaternion negation: componentwise.
Equations
- a.negate = { w := a.w.negate, x := a.x.negate, y := a.y.negate, z := a.z.negate }
Instances For

---

### `Tau.Boundary.TauQuaternion.mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L107-L117)
**def
Tau.Boundary.TauQuaternion.mul
(a b : TauQuaternion)
 :TauQuaternion**


Hamilton product:
(a1 + b1i + c1j + d1k)(a2 + b2i + c2j + d2k) =
(a1a2 - b1b2 - c1c2 - d1d2)


- (a1b2 + b1a2 + c1d2 - d1c2)i

- (a1c2 - b1d2 + c1a2 + d1b2)j

- (a1d2 + b1c2 - c1b2 + d1a2)k

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.TauQuaternion.conj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L119-L121)
**def
Tau.Boundary.TauQuaternion.conj
(a : TauQuaternion)
 :TauQuaternion**


Quaternion conjugation: conj(a + bi + cj + dk) = a - bi - cj - dk.
Equations
- a.conj = { w := a.w, x := a.x.negate, y := a.y.negate, z := a.z.negate }
Instances For

---

### `Tau.Boundary.TauQuaternion.normSq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L123-L125)
**def
Tau.Boundary.TauQuaternion.normSq
(a : TauQuaternion)
 :TauReal**


Quaternion norm squared: |a|^2 = w^2 + x^2 + y^2 + z^2.
Equations
- a.normSq = ((a.w.mul a.w).add (a.x.mul a.x)).add ((a.y.mul a.y).add (a.z.mul a.z))
Instances For

---

### `Tau.Boundary.TauQuaternion.neg_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L141-L142)
**def
Tau.Boundary.TauQuaternion.neg_one :TauQuaternion**


The negation of one: (-1, 0, 0, 0).
Equations
- Tau.Boundary.TauQuaternion.neg_one = Tau.Boundary.TauQuaternion.one.negate
Instances For

---

### `Tau.Boundary.qi_squared`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L144-L157)
**theorem
Tau.Boundary.qi_squared :(TauQuaternion.qi.mul TauQuaternion.qi).equiv TauQuaternion.neg_one**


i^2 = -1: qi * qi is equivalent to negate one.

---

### `Tau.Boundary.qj_squared`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L159-L172)
**theorem
Tau.Boundary.qj_squared :(TauQuaternion.qj.mul TauQuaternion.qj).equiv TauQuaternion.neg_one**


j^2 = -1: qj * qj is equivalent to negate one.

---

### `Tau.Boundary.qk_squared`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L174-L187)
**theorem
Tau.Boundary.qk_squared :(TauQuaternion.qk.mul TauQuaternion.qk).equiv TauQuaternion.neg_one**


k^2 = -1: qk * qk is equivalent to negate one.

---

### `Tau.Boundary.ijk_relation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L189-L203)
**theorem
Tau.Boundary.ijk_relation :((TauQuaternion.qi.mul TauQuaternion.qj).mul TauQuaternion.qk).equiv TauQuaternion.neg_one**


ijk = -1: qi * qj * qk is equivalent to negate one.

---

### `Tau.Boundary.non_commutativity_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L209-L225)
**theorem
Tau.Boundary.non_commutativity_witness :¬(TauQuaternion.qi.mul TauQuaternion.qj).equiv (TauQuaternion.qj.mul TauQuaternion.qi)**


Non-commutativity witness: qi * qj and qj * qi differ in the z-component.
qi * qj has z = 1 while qj * qi has z = -1.

---

### `Tau.Boundary.tauquat_add_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L231-L235)
**theorem
Tau.Boundary.tauquat_add_comm
(a b : TauQuaternion)
 :(a.add b).equiv (b.add a)**


Quaternion addition is commutative (up to equiv).

---

### `Tau.Boundary.tauquat_add_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L237-L242)
**theorem
Tau.Boundary.tauquat_add_assoc
(a b c : TauQuaternion)
 :((a.add b).add c).equiv (a.add (b.add c))**


Quaternion addition is associative (up to equiv).

---

### `Tau.Boundary.tauquat_add_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L244-L248)
**theorem
Tau.Boundary.tauquat_add_zero
(a : TauQuaternion)
 :(a.add TauQuaternion.zero).equiv a**


Quaternion zero is a right identity for addition (up to equiv).

---

### `Tau.Boundary.tauquat_add_negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L250-L254)
**theorem
Tau.Boundary.tauquat_add_negate
(a : TauQuaternion)
 :(a.add a.negate).equiv TauQuaternion.zero**


Quaternion negation is a right inverse for addition (up to equiv).

---

### `Tau.Boundary.tauquat_mul_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L260-L271)
**theorem
Tau.Boundary.tauquat_mul_one
(a : TauQuaternion)
 :(a.mul TauQuaternion.one).equiv a**


One is a right identity for quaternion multiplication (up to equiv).

---

### `Tau.Boundary.tauquat_one_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Quaternions.lean#L273-L284)
**theorem
Tau.Boundary.tauquat_one_mul
(a : TauQuaternion)
 :(TauQuaternion.one.mul a).equiv a**


One is a left identity for quaternion multiplication (up to equiv).
