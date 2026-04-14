---
layout: taulib-doc
title: "TauLib.BookI.Denotation.Arithmetic"
permalink: /verify/taulib/docs/book-i-denotation-arithmetic/
lane: verify
module_name: "TauLib.BookI.Denotation.Arithmetic"
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

# TauLib.Denotation.Arithmetic


Earned arithmetic: addition, multiplication, exponentiation, and tetration
derived from the iterator ρ.

## Registry Cross-References


- [I.D10] Index Addition — `idx_add`, `idx_add_eq_nat_add`

- [I.D11] Index Multiplication — `idx_mul`, `idx_mul_eq_nat_mul`

- [I.D12] Index Exponentiation — `idx_exp`, `idx_exp_eq_nat_pow`

- [I.D13] Index Tetration — `idx_tetration`

- [I.P05] Arithmetic Injectivity — `idx_add_injective`, `idx_mul_injective`, `idx_exp_injective`

- [I.P06] Arithmetic Laws — `idx_add_comm`, `idx_add_assoc`, `idx_mul_comm`, etc.


## Ground Truth Sources


- chunk_0057_M000678: Multiplication as stride iteration of ρ

- chunk_0060_M000698: UR-ITER requirement, arithmetic from ρ without algebraic substrate

- chunk_0052_M000622: Binary operators derived, not primitive


## Mathematical Content


The key insight: arithmetic is NOT imported but *earned* from ρ iteration.


- Addition: n + m = depth of ρᵐ(⟨α, n⟩)

- Multiplication: n × m = iterated addition

- Exponentiation: n ^ m = iterated multiplication

- Tetration: ⁿm = iterated exponentiation


The "bridge lemmas" prove each coincides with the Nat operation.

---

### `Tau.Denotation.idx_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L44-L47)
**def
Tau.Denotation.idx_add
(n m : TauIdx)
 :TauIdx**


[I.D10] Index addition: the depth after m applications of ρ to ⟨α, n⟩.
This *earns* addition from the iterator.
Equations
- Tau.Denotation.idx_add n m = (Tau.Orbit.iter_rho m (Tau.Denotation.toAlphaOrbit n)).depth
Instances For

---

### `Tau.Denotation.idx_add_eq_nat_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L49-L51)
**theorem
Tau.Denotation.idx_add_eq_nat_add
(n m : TauIdx)
 :idx_add n m = n + m**


Bridge lemma: idx_add coincides with Nat.add.

---

### `Tau.Denotation.idx_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L57-L61)
**def
Tau.Denotation.idx_mul
(n m : TauIdx)
 :TauIdx**


[I.D11] Index multiplication: iterated addition.
Equations
- Tau.Denotation.idx_mul n 0 = 0
- Tau.Denotation.idx_mul n (Nat.succ m_2) = Tau.Denotation.idx_add (Tau.Denotation.idx_mul n m_2) n
Instances For

---

### `Tau.Denotation.idx_mul_eq_nat_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L63-L69)
**theorem
Tau.Denotation.idx_mul_eq_nat_mul
(n m : TauIdx)
 :idx_mul n m = n * m**


Bridge lemma: idx_mul coincides with Nat.mul.

---

### `Tau.Denotation.idx_exp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L75-L79)
**def
Tau.Denotation.idx_exp
(n m : TauIdx)
 :TauIdx**


[I.D12] Index exponentiation: iterated multiplication.
Equations
- Tau.Denotation.idx_exp n 0 = 1
- Tau.Denotation.idx_exp n (Nat.succ m_2) = Tau.Denotation.idx_mul (Tau.Denotation.idx_exp n m_2) n
Instances For

---

### `Tau.Denotation.idx_exp_eq_nat_pow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L81-L87)
**theorem
Tau.Denotation.idx_exp_eq_nat_pow
(n m : TauIdx)
 :idx_exp n m = n ^ m**


Bridge lemma: idx_exp coincides with Nat.pow.

---

### `Tau.Denotation.idx_tetration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L93-L98)
**def
Tau.Denotation.idx_tetration
(n m : TauIdx)
 :TauIdx**


[I.D13] Index tetration: iterated exponentiation (right-associative tower).
ⁿm means n^(n^(n^...)) with m copies of n.
Equations
- Tau.Denotation.idx_tetration n 0 = 1
- Tau.Denotation.idx_tetration n (Nat.succ m_2) = Tau.Denotation.idx_exp n (Tau.Denotation.idx_tetration n m_2)
Instances For

---

### `Tau.Denotation.idx_tetration_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L100-L106)
**theorem
Tau.Denotation.idx_tetration_eq
(n m : TauIdx)
 :idx_tetration n m = Orbit.tetration n m**


Bridge lemma: idx_tetration matches the Nat tetration from Ladder.

---

### `Tau.Denotation.ladderOp_add_eq_idx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L112-L115)
**theorem
Tau.Denotation.ladderOp_add_eq_idx
(n m : TauIdx)
 :Orbit.ladderOp Orbit.LadderLevel.add_level n m = idx_add n m**


ladderOp at add_level coincides with earned idx_add.

---

### `Tau.Denotation.ladderOp_mul_eq_idx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L117-L120)
**theorem
Tau.Denotation.ladderOp_mul_eq_idx
(n m : TauIdx)
 :Orbit.ladderOp Orbit.LadderLevel.mul_level n m = idx_mul n m**


ladderOp at mul_level coincides with earned idx_mul.

---

### `Tau.Denotation.ladderOp_exp_eq_idx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L122-L125)
**theorem
Tau.Denotation.ladderOp_exp_eq_idx
(n m : TauIdx)
 :Orbit.ladderOp Orbit.LadderLevel.exp_level n m = idx_exp n m**


ladderOp at exp_level coincides with earned idx_exp.

---

### `Tau.Denotation.ladderOp_tet_eq_idx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L127-L130)
**theorem
Tau.Denotation.ladderOp_tet_eq_idx
(n m : TauIdx)
 :Orbit.ladderOp Orbit.LadderLevel.tet_level n m = idx_tetration n m**


ladderOp at tet_level coincides with earned idx_tetration.

---

### `Tau.Denotation.fold_chain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L132-L140)
**theorem
Tau.Denotation.fold_chain :(∀ (n m : TauIdx), idx_add n m = (Orbit.iter_rho m (toAlphaOrbit n)).depth) ∧ (∀ (n m : TauIdx), idx_mul n (m + 1) = idx_add (idx_mul n m) n) ∧ (∀ (n m : TauIdx), idx_exp n (m + 1) = idx_mul (idx_exp n m) n) ∧ ∀ (n m : TauIdx), idx_tetration n (m + 1) = idx_exp n (idx_tetration n m)**


The Fold Chain Principle: each arithmetic level is obtained by
structural recursion on the previous level.
Ground truth: chunk_0060 (UR-ITER), chunk_0057 (counting = time).

---

### `Tau.Denotation.idx_add_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L146-L149)
**theorem
Tau.Denotation.idx_add_comm
(n m : TauIdx)
 :idx_add n m = idx_add m n**


Addition is commutative.

---

### `Tau.Denotation.idx_add_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L151-L155)
**theorem
Tau.Denotation.idx_add_assoc
(a b c : TauIdx)
 :idx_add (idx_add a b) c = idx_add a (idx_add b c)**


Addition is associative.

---

### `Tau.Denotation.idx_add_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L157-L159)
**theorem
Tau.Denotation.idx_add_zero
(n : TauIdx)
 :idx_add n 0 = n**


Addition has identity 0.

---

### `Tau.Denotation.idx_zero_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L161-L163)
**theorem
Tau.Denotation.idx_zero_add
(n : TauIdx)
 :idx_add 0 n = n**


Zero is a left identity for addition.

---

### `Tau.Denotation.idx_mul_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L165-L167)
**theorem
Tau.Denotation.idx_mul_comm
(n m : TauIdx)
 :idx_mul n m = idx_mul m n**


Multiplication is commutative.

---

### `Tau.Denotation.idx_mul_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L169-L172)
**theorem
Tau.Denotation.idx_mul_assoc
(a b c : TauIdx)
 :idx_mul (idx_mul a b) c = idx_mul a (idx_mul b c)**


Multiplication is associative.

---

### `Tau.Denotation.idx_mul_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L174-L176)
**theorem
Tau.Denotation.idx_mul_one
(n : TauIdx)
 :idx_mul n 1 = n**


Multiplication has identity 1.

---

### `Tau.Denotation.idx_one_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L178-L180)
**theorem
Tau.Denotation.idx_one_mul
(n : TauIdx)
 :idx_mul 1 n = n**


One is a left identity for multiplication.

---

### `Tau.Denotation.idx_mul_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L182-L184)
**theorem
Tau.Denotation.idx_mul_zero
(n : TauIdx)
 :idx_mul n 0 = 0**


Multiplication has absorbing element 0.

---

### `Tau.Denotation.idx_distrib`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L186-L190)
**theorem
Tau.Denotation.idx_distrib
(a b c : TauIdx)
 :idx_mul a (idx_add b c) = idx_add (idx_mul a b) (idx_mul a c)**


Distributivity: a × (b + c) = a × b + a × c.

---

### `Tau.Denotation.idx_add_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L196-L201)
**theorem
Tau.Denotation.idx_add_injective
(n : TauIdx)
 :Function.Injective (idx_add n)**


[I.P05] Addition is injective in the second argument.

---

### `Tau.Denotation.idx_mul_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L203-L208)
**theorem
Tau.Denotation.idx_mul_injective
(n : TauIdx)

(hn : n > 0)
 :Function.Injective (idx_mul n)**


Multiplication by n > 0 is injective in the second argument.

---

### `Tau.Denotation.idx_exp_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L210-L215)
**theorem
Tau.Denotation.idx_exp_injective
(n : TauIdx)

(hn : n ≥ 2)
 :Function.Injective (idx_exp n)**


Exponentiation with base ≥ 2 is injective in the exponent.

---

### `Tau.Denotation.idx_exp_non_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Arithmetic.lean#L217-L223)
**theorem
Tau.Denotation.idx_exp_non_comm :¬∀ (n m : TauIdx), idx_exp n m = idx_exp m n**


Exponentiation is not commutative (counterexample: 2^3 ≠ 3^2).
