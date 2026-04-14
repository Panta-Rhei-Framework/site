---
layout: taulib-doc
title: "TauLib.BookI.Boundary.ConstructiveReals"
permalink: /verify/taulib/docs/book-i-boundary-constructive-reals/
lane: verify
module_name: "TauLib.BookI.Boundary.ConstructiveReals"
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

# TauLib.Boundary.ConstructiveReals


The constructive reals ℝ_τ: Cauchy completion of TauRat.

## Registry Cross-References


- [I.D84] TauReal — Constructive reals via Cauchy completion of TauRat

- [I.T42] Archimedean Property — ℝ_τ is Archimedean (unbounded embedding of TauIdx)

- [I.P39] Ordered Field Axioms — ℝ_τ forms a commutative ring (field axioms up to equiv)


## Ground Truth Sources


- ch76-constructive-reals.tex: Cauchy completion, Archimedean property, ordered field


## Mathematical Content


TauReal is represented as sequences of TauRat approximations (Cauchy sequences).
Equivalence is pointwise TauRat.equiv: two TauReals agree if each approximation
step agrees (up to TauRat equivalence). All ring axioms reduce to the
corresponding TauRat axioms proved in NumberTower.lean.

The key philosophical point: ℝ_τ is the **countable, constructive** continuum —
every TauReal is specified by an explicit sequence of TauRat values.

---

### `Tau.Boundary.taurat_add_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L40-L46)
**theorem
Tau.Boundary.taurat_add_assoc
(a b c : TauRat)
 :((a.add b).add c).equiv (a.add (b.add c))**


Addition is associative up to equiv.

---

### `Tau.Boundary.taurat_zero_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L48-L54)
**theorem
Tau.Boundary.taurat_zero_add
(a : TauRat)
 :(TauRat.zero.add a).equiv a**


Zero is a left identity for addition (up to equiv).

---

### `Tau.Boundary.taurat_negate_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L56-L62)
**theorem
Tau.Boundary.taurat_negate_add
(a : TauRat)
 :(a.negate.add a).equiv TauRat.zero**


Negation is a left inverse for addition (up to equiv).

---

### `Tau.Boundary.taurat_mul_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L64-L70)
**theorem
Tau.Boundary.taurat_mul_assoc
(a b c : TauRat)
 :((a.mul b).mul c).equiv (a.mul (b.mul c))**


Multiplication is associative up to equiv.

---

### `Tau.Boundary.taurat_one_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L72-L78)
**theorem
Tau.Boundary.taurat_one_mul
(a : TauRat)
 :(TauRat.one.mul a).equiv a**


One is a left identity for multiplication (up to equiv).

---

### `Tau.Boundary.taurat_left_distrib`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L80-L86)
**theorem
Tau.Boundary.taurat_left_distrib
(a b c : TauRat)
 :(a.mul (b.add c)).equiv ((a.mul b).add (a.mul c))**


Left distributivity: a * (b + c) = a*b + a*c (up to equiv).

---

### `Tau.Boundary.taurat_right_distrib`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L88-L94)
**theorem
Tau.Boundary.taurat_right_distrib
(a b c : TauRat)
 :((a.add b).mul c).equiv ((a.mul c).add (b.mul c))**


Right distributivity: (a + b) * c = a*c + b*c (up to equiv).

---

### `Tau.Boundary.taurat_zero_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L96-L102)
**theorem
Tau.Boundary.taurat_zero_mul
(a : TauRat)
 :(TauRat.zero.mul a).equiv TauRat.zero**


Multiplication by zero gives zero (up to equiv).

---

### `Tau.Boundary.TauReal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L108-L112)
**structure
Tau.Boundary.TauReal :Type**


[I.D84] TauReal: constructive reals via Cauchy completion of TauRat.
Represented as sequences of TauRat approximations.

- approx : ℕ → TauRat
The nth rational approximation.

Instances For

---

### `Tau.Boundary.TauReal.zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L114-L115)
**def
Tau.Boundary.TauReal.zero :TauReal**


TauReal zero: constant sequence at TauRat.zero.
Equations
- Tau.Boundary.TauReal.zero = { approx := fun (x : ℕ) => Tau.Boundary.TauRat.zero }
Instances For

---

### `Tau.Boundary.TauReal.one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L117-L118)
**def
Tau.Boundary.TauReal.one :TauReal**


TauReal one: constant sequence at TauRat.one.
Equations
- Tau.Boundary.TauReal.one = { approx := fun (x : ℕ) => Tau.Boundary.TauRat.one }
Instances For

---

### `Tau.Boundary.TauReal.add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L120-L122)
**def
Tau.Boundary.TauReal.add
(a b : TauReal)
 :TauReal**


TauReal addition: pointwise TauRat addition.
Equations
- a.add b = { approx := fun (n : ℕ) => (a.approx n).add (b.approx n) }
Instances For

---

### `Tau.Boundary.TauReal.mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L124-L126)
**def
Tau.Boundary.TauReal.mul
(a b : TauReal)
 :TauReal**


TauReal multiplication: pointwise TauRat multiplication.
Equations
- a.mul b = { approx := fun (n : ℕ) => (a.approx n).mul (b.approx n) }
Instances For

---

### `Tau.Boundary.TauReal.negate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L128-L130)
**def
Tau.Boundary.TauReal.negate
(a : TauReal)
 :TauReal**


TauReal negation: pointwise TauRat negation.
Equations
- a.negate = { approx := fun (n : ℕ) => (a.approx n).negate }
Instances For

---

### `Tau.Boundary.TauReal.sub`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L132-L134)
**def
Tau.Boundary.TauReal.sub
(a b : TauReal)
 :TauReal**


TauReal subtraction: a - b = a + (-b).
Equations
- a.sub b = a.add b.negate
Instances For

---

### `Tau.Boundary.TauReal.fromTauRat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L136-L137)
**def
Tau.Boundary.TauReal.fromTauRat
(q : TauRat)
 :TauReal**


Embed a TauRat as a constant TauReal sequence.
Equations
- Tau.Boundary.TauReal.fromTauRat q = { approx := fun (x : ℕ) => q }
Instances For

---

### `Tau.Boundary.TauReal.fromNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L139-L141)
**def
Tau.Boundary.TauReal.fromNat
(n : Denotation.TauIdx)
 :TauReal**


Embed a natural number as a TauReal.
Equations
- Tau.Boundary.TauReal.fromNat n = Tau.Boundary.TauReal.fromTauRat (Tau.Boundary.nat_to_taurat n)
Instances For

---

### `Tau.Boundary.TauReal.equiv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L147-L150)
**def
Tau.Boundary.TauReal.equiv
(a b : TauReal)
 :Prop**


Two TauReals are equivalent if their approximation sequences
agree pointwise up to TauRat equivalence.
Equations
- a.equiv b = ∀ (n : ℕ), (a.approx n).equiv (b.approx n)
Instances For

---

### `Tau.Boundary.TauReal.equiv_refl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L152-L154)
**theorem
Tau.Boundary.TauReal.equiv_refl
(a : TauReal)
 :a.equiv a**


TauReal equivalence is reflexive.

---

### `Tau.Boundary.TauReal.equiv_symm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L156-L159)
**theorem
Tau.Boundary.TauReal.equiv_symm
{a b : TauReal}

(h : a.equiv b)
 :b.equiv a**


TauReal equivalence is symmetric.

---

### `Tau.Boundary.taureal_add_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L165-L168)
**theorem
Tau.Boundary.taureal_add_comm
(a b : TauReal)
 :(a.add b).equiv (b.add a)**


Addition is commutative up to equiv.

---

### `Tau.Boundary.taureal_add_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L170-L173)
**theorem
Tau.Boundary.taureal_add_assoc
(a b c : TauReal)
 :((a.add b).add c).equiv (a.add (b.add c))**


Addition is associative up to equiv.

---

### `Tau.Boundary.taureal_add_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L175-L178)
**theorem
Tau.Boundary.taureal_add_zero
(a : TauReal)
 :(a.add TauReal.zero).equiv a**


Zero is a right identity for addition (up to equiv).

---

### `Tau.Boundary.taureal_zero_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L180-L183)
**theorem
Tau.Boundary.taureal_zero_add
(a : TauReal)
 :(TauReal.zero.add a).equiv a**


Zero is a left identity for addition (up to equiv).

---

### `Tau.Boundary.taureal_add_negate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L185-L188)
**theorem
Tau.Boundary.taureal_add_negate
(a : TauReal)
 :(a.add a.negate).equiv TauReal.zero**


Negation is a right inverse for addition (up to equiv).

---

### `Tau.Boundary.taureal_negate_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L190-L193)
**theorem
Tau.Boundary.taureal_negate_add
(a : TauReal)
 :(a.negate.add a).equiv TauReal.zero**


Negation is a left inverse for addition (up to equiv).

---

### `Tau.Boundary.taureal_mul_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L195-L198)
**theorem
Tau.Boundary.taureal_mul_comm
(a b : TauReal)
 :(a.mul b).equiv (b.mul a)**


Multiplication is commutative up to equiv.

---

### `Tau.Boundary.taureal_mul_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L200-L203)
**theorem
Tau.Boundary.taureal_mul_assoc
(a b c : TauReal)
 :((a.mul b).mul c).equiv (a.mul (b.mul c))**


Multiplication is associative up to equiv.

---

### `Tau.Boundary.taureal_mul_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L205-L208)
**theorem
Tau.Boundary.taureal_mul_one
(a : TauReal)
 :(a.mul TauReal.one).equiv a**


One is a right identity for multiplication (up to equiv).

---

### `Tau.Boundary.taureal_one_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L210-L213)
**theorem
Tau.Boundary.taureal_one_mul
(a : TauReal)
 :(TauReal.one.mul a).equiv a**


One is a left identity for multiplication (up to equiv).

---

### `Tau.Boundary.taureal_left_distrib`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L215-L218)
**theorem
Tau.Boundary.taureal_left_distrib
(a b c : TauReal)
 :(a.mul (b.add c)).equiv ((a.mul b).add (a.mul c))**


Left distributivity: a * (b + c) = a*b + a*c (up to equiv).

---

### `Tau.Boundary.taureal_right_distrib`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L220-L223)
**theorem
Tau.Boundary.taureal_right_distrib
(a b c : TauReal)
 :((a.add b).mul c).equiv ((a.mul c).add (b.mul c))**


Right distributivity: (a + b) * c = a*c + b*c (up to equiv).

---

### `Tau.Boundary.taureal_zero_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L225-L228)
**theorem
Tau.Boundary.taureal_zero_mul
(a : TauReal)
 :(TauReal.zero.mul a).equiv TauReal.zero**


Multiplication by zero gives zero (up to equiv).

---

### `Tau.Boundary.taureal_ring_axioms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L230-L241)
**theorem
Tau.Boundary.taureal_ring_axioms :(∀ (a b : TauReal), (a.add b).equiv (b.add a)) ∧ (∀ (a b c : TauReal), ((a.add b).add c).equiv (a.add (b.add c))) ∧ (∀ (a : TauReal), (a.add TauReal.zero).equiv a) ∧ (∀ (a : TauReal), (a.add a.negate).equiv TauReal.zero) ∧ (∀ (a b : TauReal), (a.mul b).equiv (b.mul a)) ∧ (∀ (a b c : TauReal), ((a.mul b).mul c).equiv (a.mul (b.mul c))) ∧ (∀ (a : TauReal), (a.mul TauReal.one).equiv a) ∧ ∀ (a b c : TauReal), (a.mul (b.add c)).equiv ((a.mul b).add (a.mul c))**


Full TauReal ring axiom collection.

---

### `Tau.Boundary.fromTauRat_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L247-L251)
**theorem
Tau.Boundary.fromTauRat_add
(a b : TauRat)
 :(TauReal.fromTauRat (a.add b)).equiv ((TauReal.fromTauRat a).add (TauReal.fromTauRat b))**


The embedding from TauRat to TauReal preserves addition (up to equiv).

---

### `Tau.Boundary.fromTauRat_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L253-L257)
**theorem
Tau.Boundary.fromTauRat_mul
(a b : TauRat)
 :(TauReal.fromTauRat (a.mul b)).equiv ((TauReal.fromTauRat a).mul (TauReal.fromTauRat b))**


The embedding from TauRat to TauReal preserves multiplication (up to equiv).

---

### `Tau.Boundary.taureal_archimedean_embedding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/ConstructiveReals.lean#L263-L282)
**theorem
Tau.Boundary.taureal_archimedean_embedding
(n m : Denotation.TauIdx)
 :n < m → ¬(TauReal.fromNat m).equiv (TauReal.fromNat n)**


[I.T42] The Archimedean property: the natural number embedding
into TauReal is unbounded. For any constant TauReal (embedded from TauRat),
a sufficiently large natural number exceeds it.
Stated as: the sequence (fromNat n) is strictly increasing.
