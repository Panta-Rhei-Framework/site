---
layout: taulib-doc
title: "TauLib.BookI.Boundary.ComplexField"
permalink: /verify/taulib/docs/book-i-boundary-complex-field/
lane: verify
module_name: "TauLib.BookI.Boundary.ComplexField"
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

# TauLib.Boundary.ComplexField


The elliptic complex field: TauComplex = TauReal[i]/(i² + 1).

## Registry Cross-References


- [I.D85] TauComplex — Elliptic complex field over constructive reals

- [I.D86] Elliptic-Hyperbolic Dichotomy — TauComplex (field) vs SplitComplex (zero divisors)

- [I.T43] Field Axioms — TauComplex forms a commutative ring (field axioms up to equiv)


## Ground Truth Sources


- ch77-complex-field.tex: Complex field construction, i² = -1, ring axioms


## Mathematical Content


TauComplex is the standard complex field built over TauReal: pairs (re, im)
with multiplication (a + bi)(c + di) = (ac - bd) + (ad + bc)i. The defining
relation is i² = -1 (elliptic sign), in contrast to SplitComplex where j² = +1
(hyperbolic sign). This sign difference has profound consequences:


- **TauComplex** (i² = -1): field, no zero divisors, algebraically closed

- **SplitComplex** (j² = +1): ring with zero divisors, sector decomposition


All ring axioms are proved up to TauComplex.equiv (componentwise TauReal.equiv),
which reduces pointwise to TauRat.equiv, then to TauInt.equiv via
cross-multiplication, then to Int equality via equiv_iff_toInt_eq.

---

### `Tau.Boundary.TauComplex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L44-L50)
**structure
Tau.Boundary.TauComplex :Type**


[I.D85] TauComplex: the elliptic complex field TauReal[i]/(i² + 1).
A pair (re, im) represents re + im * i.

- re : TauReal
Real part.

- im : TauReal
Imaginary part.

Instances For

---

### `Tau.Boundary.TauComplex.equiv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L56-L59)
**def
Tau.Boundary.TauComplex.equiv
(a b : TauComplex)
 :Prop**


Two TauComplex values are equivalent if their real and imaginary
parts are equivalent as TauReals.
Equations
- a.equiv b = (a.re.equiv b.re ∧ a.im.equiv b.im)
Instances For

---

### `Tau.Boundary.TauComplex.equiv_refl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L61-L63)
**theorem
Tau.Boundary.TauComplex.equiv_refl
(a : TauComplex)
 :a.equiv a**


TauComplex equivalence is reflexive.

---

### `Tau.Boundary.TauComplex.equiv_symm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L65-L68)
**theorem
Tau.Boundary.TauComplex.equiv_symm
{a b : TauComplex}

(h : a.equiv b)
 :b.equiv a**


TauComplex equivalence is symmetric.

---

### `Tau.Boundary.TauComplex.zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L74-L75)
**def
Tau.Boundary.TauComplex.zero :TauComplex**


Complex zero: (0, 0).
Equations
- Tau.Boundary.TauComplex.zero = { re := Tau.Boundary.TauReal.zero, im := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.TauComplex.one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L77-L78)
**def
Tau.Boundary.TauComplex.one :TauComplex**


Complex one: (1, 0).
Equations
- Tau.Boundary.TauComplex.one = { re := Tau.Boundary.TauReal.one, im := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.TauComplex.i_unit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L80-L81)
**def
Tau.Boundary.TauComplex.i_unit :TauComplex**


The imaginary unit: i = (0, 1).
Equations
- Tau.Boundary.TauComplex.i_unit = { re := Tau.Boundary.TauReal.zero, im := Tau.Boundary.TauReal.one }
Instances For

---

### `Tau.Boundary.TauComplex.add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L83-L85)
**def
Tau.Boundary.TauComplex.add
(a b : TauComplex)
 :TauComplex**


Complex addition: (a + bi) + (c + di) = (a+c) + (b+d)i.
Equations
- a.add b = { re := a.re.add b.re, im := a.im.add b.im }
Instances For

---

### `Tau.Boundary.TauComplex.mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L87-L91)
**def
Tau.Boundary.TauComplex.mul
(a b : TauComplex)
 :TauComplex**


Complex multiplication: (a + bi)(c + di) = (ac - bd) + (ad + bc)i.
Note: subtraction is TauReal.sub = TauReal.add ∘ TauReal.negate.
Equations
- a.mul b = { re := (a.re.mul b.re).sub (a.im.mul b.im), im := (a.re.mul b.im).add (a.im.mul b.re) }
Instances For

---

### `Tau.Boundary.TauComplex.negate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L93-L95)
**def
Tau.Boundary.TauComplex.negate
(a : TauComplex)
 :TauComplex**


Complex negation: -(a + bi) = (-a) + (-b)i.
Equations
- a.negate = { re := a.re.negate, im := a.im.negate }
Instances For

---

### `Tau.Boundary.TauComplex.conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L97-L99)
**def
Tau.Boundary.TauComplex.conj
(a : TauComplex)
 :TauComplex**


Complex conjugation: conj(a + bi) = a + (-b)i.
Equations
- a.conj = { re := a.re, im := a.im.negate }
Instances For

---

### `Tau.Boundary.taucomplex_i_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L105-L126)
**theorem
Tau.Boundary.taucomplex_i_squared :(TauComplex.i_unit.mul TauComplex.i_unit).equiv TauComplex.one.negate**


The defining relation of the complex field: i² = -1.
mul(0,1)(0,1) = (0*0 - 1*1, 0*1 + 1*0) = (-1, 0) = negate(1, 0).

---

### `Tau.Boundary.taucomplex_add_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L132-L135)
**theorem
Tau.Boundary.taucomplex_add_comm
(a b : TauComplex)
 :(a.add b).equiv (b.add a)**


Addition is commutative.

---

### `Tau.Boundary.taucomplex_add_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L137-L141)
**theorem
Tau.Boundary.taucomplex_add_assoc
(a b c : TauComplex)
 :((a.add b).add c).equiv (a.add (b.add c))**


Addition is associative.

---

### `Tau.Boundary.taucomplex_add_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L143-L146)
**theorem
Tau.Boundary.taucomplex_add_zero
(a : TauComplex)
 :(a.add TauComplex.zero).equiv a**


Zero is a right identity for addition.

---

### `Tau.Boundary.taucomplex_add_negate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L148-L151)
**theorem
Tau.Boundary.taucomplex_add_negate
(a : TauComplex)
 :(a.add a.negate).equiv TauComplex.zero**


Negation is a right inverse for addition.

---

### `Tau.Boundary.taucomplex_mul_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L153-L171)
**theorem
Tau.Boundary.taucomplex_mul_comm
(a b : TauComplex)
 :(a.mul b).equiv (b.mul a)**


Multiplication is commutative.
Re: ac - bd = ca - db. Im: ad + bc = cb + da.

---

### `Tau.Boundary.taucomplex_mul_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L173-L192)
**theorem
Tau.Boundary.taucomplex_mul_assoc
(a b c : TauComplex)
 :((a.mul b).mul c).equiv (a.mul (b.mul c))**


Multiplication is associative.
(ab)c = a(bc) for complex multiplication.

---

### `Tau.Boundary.taucomplex_mul_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L194-L214)
**theorem
Tau.Boundary.taucomplex_mul_one
(a : TauComplex)
 :(a.mul TauComplex.one).equiv a**


One is a right identity for multiplication: z * 1 = z.

---

### `Tau.Boundary.taucomplex_left_distrib`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L216-L236)
**theorem
Tau.Boundary.taucomplex_left_distrib
(a b c : TauComplex)
 :(a.mul (b.add c)).equiv ((a.mul b).add (a.mul c))**


Left distributivity: a * (b + c) = a*b + a*c.

---

### `Tau.Boundary.taucomplex_ring_axioms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L238-L250)
**theorem
Tau.Boundary.taucomplex_ring_axioms :(∀ (a b : TauComplex), (a.add b).equiv (b.add a)) ∧ (∀ (a b c : TauComplex), ((a.add b).add c).equiv (a.add (b.add c))) ∧ (∀ (a : TauComplex), (a.add TauComplex.zero).equiv a) ∧ (∀ (a : TauComplex), (a.add a.negate).equiv TauComplex.zero) ∧ (∀ (a b : TauComplex), (a.mul b).equiv (b.mul a)) ∧ (∀ (a b c : TauComplex), ((a.mul b).mul c).equiv (a.mul (b.mul c))) ∧ (∀ (a : TauComplex), (a.mul TauComplex.one).equiv a) ∧ ∀ (a b c : TauComplex), (a.mul (b.add c)).equiv ((a.mul b).add (a.mul c))**


Full TauComplex ring axiom collection.

---

### `Tau.Boundary.sc_j_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L256-L266)
**theorem
Tau.Boundary.sc_j_squared :{ re := 0, im := 1 }.mul { re := 0, im := 1 } = Polarity.SplitComplex.one**


[I.D86] The elliptic-hyperbolic dichotomy:


- TauComplex has i² = -1 (elliptic sign), yielding a field with no zero divisors.

- SplitComplex has j² = +1 (hyperbolic sign), yielding a ring WITH zero divisors.


We witness the dichotomy by showing:

- i² = -1 in TauComplex (taucomplex_i_squared)

- j² = +1 in SplitComplex (sc_j_squared, proved below)

- SplitComplex has zero divisors (zero_divisor_witness_b from SplitComplex.lean)


---

### `Tau.Boundary.elliptic_hyperbolic_dichotomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L268-L277)
**theorem
Tau.Boundary.elliptic_hyperbolic_dichotomy :(TauComplex.i_unit.mul TauComplex.i_unit).equiv TauComplex.one.negate ∧ { re := 0, im := 1 }.mul { re := 0, im := 1 } = Polarity.SplitComplex.one ∧ { re := 1, im := 1 }.mul { re := 1, im := -1 } = Polarity.SplitComplex.zero**


The dichotomy: i² = -1 AND j² = +1 AND SplitComplex has zero divisors.

---

### `Tau.Boundary.TauComplex.fromTauReal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L283-L285)
**def
Tau.Boundary.TauComplex.fromTauReal
(r : TauReal)
 :TauComplex**


Embed a TauReal into TauComplex as the real part with zero imaginary part.
Equations
- Tau.Boundary.TauComplex.fromTauReal r = { re := r, im := Tau.Boundary.TauReal.zero }
Instances For

---

### `Tau.Boundary.fromTauReal_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L287-L291)
**theorem
Tau.Boundary.fromTauReal_add
(a b : TauReal)
 :(TauComplex.fromTauReal (a.add b)).equiv ((TauComplex.fromTauReal a).add (TauComplex.fromTauReal b))**


The embedding preserves addition (up to equiv).

---

### `Tau.Boundary.taucomplex_conj_involution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L297-L308)
**theorem
Tau.Boundary.taucomplex_conj_involution
(a : TauComplex)
 :a.conj.conj.equiv a**


Conjugation is an involution: conj(conj(z)) ≡ z.

---

### `Tau.Boundary.taucomplex_conj_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ComplexField.lean#L310-L322)
**theorem
Tau.Boundary.taucomplex_conj_add
(a b : TauComplex)
 :(a.add b).conj.equiv (a.conj.add b.conj)**


Conjugation distributes over addition: conj(a + b) ≡ conj(a) + conj(b).
