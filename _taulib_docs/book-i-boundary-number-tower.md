---
layout: taulib-doc
title: "TauLib.BookI.Boundary.NumberTower"
permalink: /verify/taulib/docs/book-i-boundary-number-tower/
lane: verify
module_name: "TauLib.BookI.Boundary.NumberTower"
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

# TauLib.Boundary.NumberTower


The τ number tower: TauInt (formal differences) and TauRat (formal fractions).

## Registry Cross-References


- [I.D14] TauInt — Formal difference integers earned from TauIdx

- [I.D15] TauRat — Formal fraction rationals earned from TauIdx

- [I.D16] Number Tower — TauIdx ↪ TauInt ↪ TauRat → [deferred] TauReal → TauComplex


## Ground Truth Sources


- chunk_0065_M000740: Integer construction from natural differences

- chunk_0070_M000780: Rational field as formal fractions

- chunk_0095_M001050: Number tower architecture, deferred completions


## Mathematical Content


The number tower is built purely from earned arithmetic on TauIdx:

- 
**TauInt**: Formal differences (a, b) representing a - b, with equivalence
(a₁, b₁) ~ (a₂, b₂) iff a₁ + b₂ = a₂ + b₁.


- 
**TauRat**: Formal fractions (p, q) with q > 0, with equivalence
via cross-multiplication through TauInt.equiv.


- 
**TauReal / TauComplex**: Deferred to Book II (require Cauchy completion
and algebraic closure, which need earned topology from Global Hartogs).


All ring axioms are proved up to the respective equivalence relations.

---

### `Tau.Boundary.TauInt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L48-L53)
**structure
Tau.Boundary.TauInt :Type**


[I.D14] Formal difference representation of integers earned from TauIdx.
The pair (pos, neg) represents the integer pos - neg.

- pos : Denotation.TauIdx
- neg : Denotation.TauIdx
Instances For

---

### `Tau.Boundary.instDecidableEqTauInt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L53-L53)
**instance
Tau.Boundary.instDecidableEqTauInt :DecidableEq TauInt**

Equations
- Tau.Boundary.instDecidableEqTauInt = Tau.Boundary.instDecidableEqTauInt.decEq

---

### `Tau.Boundary.instDecidableEqTauInt.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L53-L53)
**def
Tau.Boundary.instDecidableEqTauInt.decEq
(x✝ x✝¹ : TauInt)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.Boundary.instDecidableEqTauInt.decEq { pos := a, neg := a_1 } { pos := b, neg := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.Boundary.instReprTauInt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L53-L53)
**instance
Tau.Boundary.instReprTauInt :Repr TauInt**

Equations
- Tau.Boundary.instReprTauInt = { reprPrec := Tau.Boundary.instReprTauInt.repr }

---

### `Tau.Boundary.instReprTauInt.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L53-L53)
**def
Tau.Boundary.instReprTauInt.repr :TauInt → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.TauInt.zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L55-L56)
**def
Tau.Boundary.TauInt.zero :TauInt**


TauInt zero: 0 = 0 - 0.
Equations
- Tau.Boundary.TauInt.zero = { pos := 0, neg := 0 }
Instances For

---

### `Tau.Boundary.TauInt.one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L58-L59)
**def
Tau.Boundary.TauInt.one :TauInt**


TauInt one: 1 = 1 - 0.
Equations
- Tau.Boundary.TauInt.one = { pos := 1, neg := 0 }
Instances For

---

### `Tau.Boundary.TauInt.add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L61-L63)
**def
Tau.Boundary.TauInt.add
(a b : TauInt)
 :TauInt**


TauInt addition: (a - b) + (c - d) = (a + c) - (b + d).
Equations
- a.add b = { pos := a.pos + b.pos, neg := a.neg + b.neg }
Instances For

---

### `Tau.Boundary.TauInt.negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L65-L67)
**def
Tau.Boundary.TauInt.negate
(a : TauInt)
 :TauInt**


TauInt negation: -(a - b) = (b - a).
Equations
- a.negate = { pos := a.neg, neg := a.pos }
Instances For

---

### `Tau.Boundary.TauInt.mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L69-L71)
**def
Tau.Boundary.TauInt.mul
(a b : TauInt)
 :TauInt**


TauInt multiplication: (p₁ - n₁)(p₂ - n₂) = (p₁p₂ + n₁n₂) - (p₁n₂ + n₁p₂).
Equations
- a.mul b = { pos := a.pos * b.pos + a.neg * b.neg, neg := a.pos * b.neg + a.neg * b.pos }
Instances For

---

### `Tau.Boundary.TauInt.sub`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L73-L75)
**def
Tau.Boundary.TauInt.sub
(a b : TauInt)
 :TauInt**


TauInt subtraction: a - b = a + (-b).
Equations
- a.sub b = a.add b.negate
Instances For

---

### `Tau.Boundary.TauInt.fromNat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L77-L78)
**def
Tau.Boundary.TauInt.fromNat
(n : Denotation.TauIdx)
 :TauInt**


Embed a natural number (TauIdx) into TauInt.
Equations
- Tau.Boundary.TauInt.fromNat n = { pos := n, neg := 0 }
Instances For

---

### `Tau.Boundary.TauInt.equiv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L84-L87)
**def
Tau.Boundary.TauInt.equiv
(a b : TauInt)
 :Prop**


Two TauInts are equivalent when they represent the same integer:
(a, b) ~ (c, d) iff a + d = c + b.
Equations
- a.equiv b = (a.pos + b.neg = b.pos + a.neg)
Instances For

---

### `Tau.Boundary.TauInt.equiv_refl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L89-L91)
**theorem
Tau.Boundary.TauInt.equiv_refl
(a : TauInt)
 :a.equiv a**


TauInt equivalence is reflexive.

---

### `Tau.Boundary.TauInt.equiv_symm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L93-L98)
**theorem
Tau.Boundary.TauInt.equiv_symm
{a b : TauInt}

(h : a.equiv b)
 :b.equiv a**


TauInt equivalence is symmetric.

---

### `Tau.Boundary.TauInt.equiv_trans`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L100-L107)
**theorem
Tau.Boundary.TauInt.equiv_trans
{a b c : TauInt}

(hab : a.equiv b)

(hbc : b.equiv c)
 :a.equiv c**


TauInt equivalence is transitive.

---

### `Tau.Boundary.TauInt.toInt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L113-L115)
**def
Tau.Boundary.TauInt.toInt
(a : TauInt)
 :ℤ**


Semantic bridge: compute the Int value represented by a TauInt.
Equations
- a.toInt = ↑a.pos - ↑a.neg
Instances For

---

### `Tau.Boundary.equiv_of_int_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L117-L122)
**theorem
Tau.Boundary.equiv_of_int_eq
(a b : TauInt)

(h : ↑a.pos - ↑a.neg = ↑b.pos - ↑b.neg)
 :a.equiv b**


Convert Int difference equality to TauInt.equiv.

---

### `Tau.Boundary.int_eq_of_equiv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L124-L129)
**theorem
Tau.Boundary.int_eq_of_equiv
(a b : TauInt)

(h : a.equiv b)
 :↑a.pos - ↑a.neg = ↑b.pos - ↑b.neg**


TauInt.equiv implies Int difference equality.

---

### `Tau.Boundary.equiv_iff_toInt_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L131-L136)
**theorem
Tau.Boundary.equiv_iff_toInt_eq
(a b : TauInt)
 :a.equiv b ↔ a.toInt = b.toInt**


Equiv iff same Int value.

---

### `Tau.Boundary.toInt_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L138-L141)
**theorem
Tau.Boundary.toInt_add
(a b : TauInt)
 :(a.add b).toInt = a.toInt + b.toInt**


toInt of add.

---

### `Tau.Boundary.toInt_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L143-L146)
**theorem
Tau.Boundary.toInt_mul
(a b : TauInt)
 :(a.mul b).toInt = a.toInt * b.toInt**


toInt of mul.

---

### `Tau.Boundary.toInt_negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L148-L151)
**theorem
Tau.Boundary.toInt_negate
(a : TauInt)
 :a.negate.toInt = -a.toInt**


toInt of negate.

---

### `Tau.Boundary.toInt_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L153-L155)
**theorem
Tau.Boundary.toInt_zero :TauInt.zero.toInt = 0**


toInt of zero.

---

### `Tau.Boundary.toInt_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L157-L159)
**theorem
Tau.Boundary.toInt_one :TauInt.one.toInt = 1**


toInt of one.

---

### `Tau.Boundary.toInt_fromNat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L161-L164)
**theorem
Tau.Boundary.toInt_fromNat
(n : Denotation.TauIdx)
 :(TauInt.fromNat n).toInt = ↑n**


toInt of fromNat.

---

### `Tau.Boundary.tauint_add_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L170-L173)
**theorem
Tau.Boundary.tauint_add_comm
(a b : TauInt)
 :(a.add b).equiv (b.add a)**


Addition is commutative up to equiv.

---

### `Tau.Boundary.tauint_add_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L175-L178)
**theorem
Tau.Boundary.tauint_add_assoc
(a b c : TauInt)
 :((a.add b).add c).equiv (a.add (b.add c))**


Addition is associative up to equiv.

---

### `Tau.Boundary.tauint_add_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L180-L183)
**theorem
Tau.Boundary.tauint_add_zero
(a : TauInt)
 :(a.add TauInt.zero).equiv a**


Zero is a right identity for addition (up to equiv).

---

### `Tau.Boundary.tauint_zero_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L185-L188)
**theorem
Tau.Boundary.tauint_zero_add
(a : TauInt)
 :(TauInt.zero.add a).equiv a**


Zero is a left identity for addition (up to equiv).

---

### `Tau.Boundary.tauint_add_negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L190-L193)
**theorem
Tau.Boundary.tauint_add_negate
(a : TauInt)
 :(a.add a.negate).equiv TauInt.zero**


Negation is a right inverse for addition (up to equiv).

---

### `Tau.Boundary.tauint_negate_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L195-L198)
**theorem
Tau.Boundary.tauint_negate_add
(a : TauInt)
 :(a.negate.add a).equiv TauInt.zero**


Negation is a left inverse for addition (up to equiv).

---

### `Tau.Boundary.tauint_mul_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L200-L203)
**theorem
Tau.Boundary.tauint_mul_comm
(a b : TauInt)
 :(a.mul b).equiv (b.mul a)**


Multiplication is commutative up to equiv.

---

### `Tau.Boundary.tauint_mul_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L205-L208)
**theorem
Tau.Boundary.tauint_mul_assoc
(a b c : TauInt)
 :((a.mul b).mul c).equiv (a.mul (b.mul c))**


Multiplication is associative up to equiv.

---

### `Tau.Boundary.tauint_mul_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L210-L213)
**theorem
Tau.Boundary.tauint_mul_one
(a : TauInt)
 :(a.mul TauInt.one).equiv a**


One is a right identity for multiplication (up to equiv).

---

### `Tau.Boundary.tauint_one_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L215-L218)
**theorem
Tau.Boundary.tauint_one_mul
(a : TauInt)
 :(TauInt.one.mul a).equiv a**


One is a left identity for multiplication (up to equiv).

---

### `Tau.Boundary.tauint_distrib`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L220-L223)
**theorem
Tau.Boundary.tauint_distrib
(a b c : TauInt)
 :(a.mul (b.add c)).equiv ((a.mul b).add (a.mul c))**


Left distributivity: a * (b + c) = a * b + a * c (up to equiv).

---

### `Tau.Boundary.tauint_distrib_right`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L225-L228)
**theorem
Tau.Boundary.tauint_distrib_right
(a b c : TauInt)
 :((a.add b).mul c).equiv ((a.mul c).add (b.mul c))**


Right distributivity: (a + b) * c = a * c + b * c (up to equiv).

---

### `Tau.Boundary.tauint_mul_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L230-L233)
**theorem
Tau.Boundary.tauint_mul_zero
(a : TauInt)
 :(a.mul TauInt.zero).equiv TauInt.zero**


Multiplication by zero gives zero (up to equiv).

---

### `Tau.Boundary.nat_to_tauint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L239-L240)
**def
Tau.Boundary.nat_to_tauint
(n : Denotation.TauIdx)
 :TauInt**


Canonical embedding from TauIdx to TauInt.
Equations
- Tau.Boundary.nat_to_tauint n = Tau.Boundary.TauInt.fromNat n
Instances For

---

### `Tau.Boundary.nat_to_tauint_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L242-L246)
**theorem
Tau.Boundary.nat_to_tauint_injective
{a b : Denotation.TauIdx}

(h : nat_to_tauint a = nat_to_tauint b)
 :a = b**


The embedding is injective.

---

### `Tau.Boundary.toInt_nat_to_tauint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L248-L251)
**theorem
Tau.Boundary.toInt_nat_to_tauint
(n : Denotation.TauIdx)
 :(nat_to_tauint n).toInt = ↑n**


toInt of nat_to_tauint.

---

### `Tau.Boundary.nat_to_tauint_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L253-L258)
**theorem
Tau.Boundary.nat_to_tauint_add
(a b : Denotation.TauIdx)
 :(nat_to_tauint (a + b)).equiv ((nat_to_tauint a).add (nat_to_tauint b))**


The embedding preserves addition (up to equiv).

---

### `Tau.Boundary.nat_to_tauint_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L260-L265)
**theorem
Tau.Boundary.nat_to_tauint_mul
(a b : Denotation.TauIdx)
 :(nat_to_tauint (a * b)).equiv ((nat_to_tauint a).mul (nat_to_tauint b))**


The embedding preserves multiplication (up to equiv).

---

### `Tau.Boundary.TauRat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L271-L277)
**structure
Tau.Boundary.TauRat :Type**


[I.D15] Formal fraction representation of rationals earned from TauIdx.
The pair (num, den) with den > 0 represents num / den.

- num : TauInt
- den : Denotation.TauIdx
- den_pos : self.den > 0
Instances For

---

### `Tau.Boundary.instReprTauRat.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L277-L277)
**def
Tau.Boundary.instReprTauRat.repr :TauRat → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.instReprTauRat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L277-L277)
**instance
Tau.Boundary.instReprTauRat :Repr TauRat**

Equations
- Tau.Boundary.instReprTauRat = { reprPrec := Tau.Boundary.instReprTauRat.repr }

---

### `Tau.Boundary.TauRat.zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L279-L281)
**def
Tau.Boundary.TauRat.zero :TauRat**


TauRat zero: 0/1.
Equations
- Tau.Boundary.TauRat.zero = { num := Tau.Boundary.TauInt.zero, den := 1, den_pos := Nat.one_pos }
Instances For

---

### `Tau.Boundary.TauRat.one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L283-L285)
**def
Tau.Boundary.TauRat.one :TauRat**


TauRat one: 1/1.
Equations
- Tau.Boundary.TauRat.one = { num := Tau.Boundary.TauInt.one, den := 1, den_pos := Nat.one_pos }
Instances For

---

### `Tau.Boundary.TauRat.add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L287-L291)
**def
Tau.Boundary.TauRat.add
(a b : TauRat)
 :TauRat**


TauRat addition: a/b + c/d = (a*d + c*b) / (b*d).
Equations
- a.add b = { num := (a.num.mul (Tau.Boundary.TauInt.fromNat b.den)).add (b.num.mul (Tau.Boundary.TauInt.fromNat a.den)),
 den := a.den * b.den, den_pos := ⋯ }
Instances For

---

### `Tau.Boundary.TauRat.mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L293-L297)
**def
Tau.Boundary.TauRat.mul
(a b : TauRat)
 :TauRat**


TauRat multiplication: (a/b) * (c/d) = (a*c) / (b*d).
Equations
- a.mul b = { num := a.num.mul b.num, den := a.den * b.den, den_pos := ⋯ }
Instances For

---

### `Tau.Boundary.TauRat.negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L299-L301)
**def
Tau.Boundary.TauRat.negate
(a : TauRat)
 :TauRat**


TauRat negation: -(a/b) = (-a)/b.
Equations
- a.negate = { num := a.num.negate, den := a.den, den_pos := ⋯ }
Instances For

---

### `Tau.Boundary.TauRat.sub`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L303-L305)
**def
Tau.Boundary.TauRat.sub
(a b : TauRat)
 :TauRat**


TauRat subtraction: a - b = a + (-b).
Equations
- a.sub b = a.add b.negate
Instances For

---

### `Tau.Boundary.TauRat.equiv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L311-L315)
**def
Tau.Boundary.TauRat.equiv
(a b : TauRat)
 :Prop**


Two TauRats are equivalent when they represent the same rational:
a/b ~ c/d iff a*d = c*b (as TauInt equiv).
Equations
- a.equiv b = (a.num.mul (Tau.Boundary.TauInt.fromNat b.den)).equiv (b.num.mul (Tau.Boundary.TauInt.fromNat a.den))
Instances For

---

### `Tau.Boundary.TauRat.equiv_refl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L317-L320)
**theorem
Tau.Boundary.TauRat.equiv_refl
(a : TauRat)
 :a.equiv a**


TauRat equivalence is reflexive.

---

### `Tau.Boundary.TauRat.equiv_symm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L322-L326)
**theorem
Tau.Boundary.TauRat.equiv_symm
{a b : TauRat}

(h : a.equiv b)
 :b.equiv a**


TauRat equivalence is symmetric.

---

### `Tau.Boundary.taurat_add_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L332-L338)
**theorem
Tau.Boundary.taurat_add_comm
(a b : TauRat)
 :(a.add b).equiv (b.add a)**


Addition is commutative up to equiv.

---

### `Tau.Boundary.taurat_add_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L340-L346)
**theorem
Tau.Boundary.taurat_add_zero
(a : TauRat)
 :(a.add TauRat.zero).equiv a**


Zero is a right identity for addition (up to equiv).

---

### `Tau.Boundary.taurat_add_negate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L348-L354)
**theorem
Tau.Boundary.taurat_add_negate
(a : TauRat)
 :(a.add a.negate).equiv TauRat.zero**


Negation is a right inverse for addition (up to equiv).

---

### `Tau.Boundary.taurat_mul_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L356-L362)
**theorem
Tau.Boundary.taurat_mul_comm
(a b : TauRat)
 :(a.mul b).equiv (b.mul a)**


Multiplication is commutative up to equiv.

---

### `Tau.Boundary.taurat_mul_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L364-L370)
**theorem
Tau.Boundary.taurat_mul_one
(a : TauRat)
 :(a.mul TauRat.one).equiv a**


One is a right identity for multiplication (up to equiv).

---

### `Tau.Boundary.int_to_taurat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L376-L378)
**def
Tau.Boundary.int_to_taurat
(z : TauInt)
 :TauRat**


Canonical embedding from TauInt to TauRat: z ↦ z/1.
Equations
- Tau.Boundary.int_to_taurat z = { num := z, den := 1, den_pos := Nat.one_pos }
Instances For

---

### `Tau.Boundary.int_to_taurat_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L380-L384)
**theorem
Tau.Boundary.int_to_taurat_injective
{a b : TauInt}

(h : int_to_taurat a = int_to_taurat b)
 :a = b**


The embedding is injective (on TauInt structures).

---

### `Tau.Boundary.int_to_taurat_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L386-L393)
**theorem
Tau.Boundary.int_to_taurat_add
(a b : TauInt)
 :(int_to_taurat (a.add b)).equiv ((int_to_taurat a).add (int_to_taurat b))**


The embedding preserves addition (up to equiv).

---

### `Tau.Boundary.int_to_taurat_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L395-L400)
**theorem
Tau.Boundary.int_to_taurat_mul
(a b : TauInt)
 :(int_to_taurat (a.mul b)).equiv ((int_to_taurat a).mul (int_to_taurat b))**


The embedding preserves multiplication (up to equiv).

---

### `Tau.Boundary.nat_to_taurat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L406-L408)
**def
Tau.Boundary.nat_to_taurat
(n : Denotation.TauIdx)
 :TauRat**


Full tower embedding: TauIdx → TauRat via nat_to_tauint then int_to_taurat.
Equations
- Tau.Boundary.nat_to_taurat n = Tau.Boundary.int_to_taurat (Tau.Boundary.nat_to_tauint n)
Instances For

---

### `Tau.Boundary.nat_to_taurat_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/NumberTower.lean#L410-L413)
**theorem
Tau.Boundary.nat_to_taurat_injective
{a b : Denotation.TauIdx}

(h : nat_to_taurat a = nat_to_taurat b)
 :a = b**


The full tower embedding is injective.
