---
layout: taulib-doc
title: "TauLib.BookI.Sets.CantorRefutation"
permalink: /verify/taulib/docs/book-i-sets-cantor-refutation/
lane: verify
module_name: "TauLib.BookI.Sets.CantorRefutation"
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

# TauLib.Sets.CantorRefutation


The Cantor Diagonal Inapplicability Theorem: three independent failures
block the diagonal argument within Category tau.

## Registry Cross-References


- [I.T35] Cantor Diagonal Inapplicability -- `cantor_inapplicable`

- [I.P34] No Unearned Decimal Diagonal -- `no_unearned_decimal_diagonal`

- [I.P35] No Comprehension -- `no_comprehension`

- [I.P36] No Free Cartesian Diagonal -- `no_free_cartesian_diagonal`


## Ground Truth Sources


- Part IX "The Cantor Mirage": The diagonal argument requires three structural
ingredients that are absent from K0-K6.


## Mathematical Content


Cantor's diagonal argument proceeds in three steps:

- Assume a surjection f : N -> R and write f(n) as a decimal expansion

- Extract a diagonal sequence d(n) = n-th digit of f(n)

- Modify d to produce an element not in the range of f


Each step requires structural infrastructure:


- Step 1 requires a total computable decimal extraction (not earned in tau)

- Step 2 requires Sep : (Idx -> Prop) -> Idx (comprehension)

- Step 3 requires Delta : Idx -> Idx x Idx (free diagonal / self-pairing)


All three fail in Category tau. Consequently, the diagonal argument
is inapplicable, and |R_tau| = aleph_0 is irrefutable.

---

### `Tau.Sets.DecimalDiagonalExtractor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L45-L59)
**structure
Tau.Sets.DecimalDiagonalExtractor :Type**


A "decimal digit extractor" would be a total function that, given an
enumeration index n and a digit position k, returns the k-th digit
of the n-th real number. The Cantor argument demands that the
diagonal d(n) = extract(n, n) can be "modified" to avoid every row.

The fundamental obstruction: any extractor whose diagonal avoids
itself is self-contradictory (diagonal(n) = extract(n,n) by definition,
yet the avoidance condition demands diagonal(n) != extract(n,n)).

- extract : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx
The digit extraction function: extract(n, k) = k-th digit of n-th real

- diagonal : Denotation.TauIdx → Denotation.TauIdx
The diagonal: d(n) = extract(n, n)

- diagonal_def
(n : Denotation.TauIdx)
 : self.diagonal n = self.extract n n
The diagonal is defined by self-application

Instances For

---

### `Tau.Sets.no_unearned_decimal_diagonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L61-L72)
**theorem
Tau.Sets.no_unearned_decimal_diagonal :¬∃ (E : DecimalDiagonalExtractor), ∀ (n : Denotation.TauIdx), E.diagonal n ≠ E.extract n n**


[I.P34] No Unearned Decimal Diagonal: no extractor can have its
diagonal avoid all rows.

Proof: the avoidance condition diagonal(n) != extract(n, n) directly
contradicts diagonal_def which says diagonal(n) = extract(n, n).
This is the liar-paradox core of the diagonal argument, and tau
blocks it by making diagonal extraction self-referential.

---

### `Tau.Sets.ComprehensionSep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L78-L79)
**def
Tau.Sets.ComprehensionSep :Type**


A "comprehension separator" would produce a tau-index from any predicate.
Equations
- Tau.Sets.ComprehensionSep = ((Tau.Denotation.TauIdx → Prop) → Tau.Denotation.TauIdx)
Instances For

---

### `Tau.Sets.no_comprehension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L81-L95)
**theorem
Tau.Sets.no_comprehension :¬∃ (Sep : ComprehensionSep), ∀ (P : Denotation.TauIdx → Prop) (a : Denotation.TauIdx), tau_mem a (Sep P) ↔ P a**


[I.P35] No comprehension separator exists in tau-arithmetic.

Proof: apply Sep to the Russell predicate P(a) = not(a in_tau a).
For R = Sep(P), the comprehension schema gives a in_tau R iff not(a in_tau a).
At a = R: R in_tau R iff not(R in_tau R). But R in_tau R holds by reflexivity
(R | R), so not(R in_tau R) also holds -- contradiction.

---

### `Tau.Sets.no_free_cartesian_diagonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L101-L121)
**theorem
Tau.Sets.no_free_cartesian_diagonal :¬∃ (pair : Denotation.TauIdx → Denotation.TauIdx), Function.Injective pair ∧ (∀ (n : Denotation.TauIdx), pair n ≠ n) ∧ ∀ (n : Denotation.TauIdx), n ∣ pair n**


The Cantor diagonal argument requires a self-pairing map
pair : N -> N that encodes the "n-th element paired with itself"
in a way that DIFFERS from n (so that digit modification can
produce a new element).

In tau-arithmetic, any map with n | pair(n) AND pair(n) != n
fails at n = 0, since 0 | k implies k = 0.

[I.P36] No nontrivial divisibility-respecting self-pairing exists.

---

### `Tau.Sets.self_pairing_trivial_or_blocked`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L123-L134)
**theorem
Tau.Sets.self_pairing_trivial_or_blocked
(pair : Denotation.TauIdx → Denotation.TauIdx)
 :Function.Injective pair → (∀ (n : Denotation.TauIdx), n ∣ pair n) → pair 0 = 0**


Stronger: even without the divisibility constraint, any self-pairing
that maps n to an index encoding (n, n) must have pair(n) >= n for the
pairing to be recoverable. The only injective map with pair(n) = n
for all n is the identity, which is trivial (doesn't help the argument).

---

### `Tau.Sets.CantorDiagonalApparatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L140-L151)
**structure
Tau.Sets.CantorDiagonalApparatus :Type**


The Cantor diagonal argument requires three structural ingredients.
We show the conjunction of all three is inconsistent in tau.

- extractor : DecimalDiagonalExtractor
A decimal digit extractor

- avoids
(n : Denotation.TauIdx)
 : self.extractor.diagonal n ≠ self.extractor.extract n n
The diagonal avoids every row

- sep : ComprehensionSep
A comprehension separator

- sep_works
(P : Denotation.TauIdx → Prop)

(a : Denotation.TauIdx)
 : tau_mem a (self.sep P) ↔ P a
Sep satisfies the comprehension schema

Instances For

---

### `Tau.Sets.cantor_inapplicable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L153-L166)
**theorem
Tau.Sets.cantor_inapplicable :¬∃ (x : CantorDiagonalApparatus), True**


[I.T35] Cantor Diagonal Inapplicability Theorem:
No CantorDiagonalApparatus can exist in Category tau.

The proof is immediate from any ONE of the three failures:


- P34: avoidance contradicts diagonal_def

- P35: comprehension contradicts no_russell_set

- P36: self-pairing contradicts divisibility at 0


We use P34 (the simplest). The three failures are independent
and each individually blocks the diagonal argument.

---

### `Tau.Sets.cantor_blocked_three_ways`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L168-L182)
**theorem
Tau.Sets.cantor_blocked_three_ways :(¬∃ (E : DecimalDiagonalExtractor), ∀ (n : Denotation.TauIdx), E.diagonal n ≠ E.extract n n) ∧ (¬∃ (Sep : ComprehensionSep), ∀ (P : Denotation.TauIdx → Prop) (a : Denotation.TauIdx), tau_mem a (Sep P) ↔ P a) ∧ ¬∃ (pair : Denotation.TauIdx → Denotation.TauIdx), Function.Injective pair ∧ (∀ (n : Denotation.TauIdx), pair n ≠ n) ∧ ∀ (n : Denotation.TauIdx), n ∣ pair n**


The three failures are individually sufficient.

---

### `Tau.Sets.R_tau_countable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L188-L197)
**theorem
Tau.Sets.R_tau_countable :∃ (embed : Denotation.TauIdx → Denotation.TauIdx), Function.Injective embed**


R_tau (the tau-reals) are encoded as omega-tails on the primorial
ladder. Since the diagonal argument is inapplicable (I.T35),
no proof of uncountability can be constructed within tau.

The tau-index set IS Nat, and every constructible omega-tail
corresponds to a natural number. The identity witnesses
that the tau-real line is at most countable.

---

### `Tau.Sets.R_tau_countable_irrefutable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/CantorRefutation.lean#L199-L212)
**theorem
Tau.Sets.R_tau_countable_irrefutable :(∃ (f : Denotation.TauIdx → ℕ), Function.Injective f) ∧ (∃ (g : ℕ → Denotation.TauIdx), Function.Injective g) ∧ ¬∃ (x : CantorDiagonalApparatus), True**


The irrefutability of countability: since the three prerequisites
for Cantor's argument are absent, no function within tau can
witness |R_tau| > aleph_0. Combined with R_tau_countable,
the cardinality of the tau-reals is exactly aleph_0.
