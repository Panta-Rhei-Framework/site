---
layout: taulib-doc
title: "TauLib.BookI.Sets.Powerset"
permalink: /verify/taulib/docs/book-i-sets-powerset/
lane: verify
module_name: "TauLib.BookI.Sets.Powerset"
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

# TauLib.Sets.Powerset


Well-foundedness of strict τ-membership and the powerset hierarchy.

## Registry Cross-References


- [I.D33] Strict Membership — `tau_strict_mem`

- [I.P12] Well-Foundedness — `tau_strict_mem_wf`


## Ground Truth Sources


- chunk_0360_M003055: Well-foundedness of the divisibility order on Nat


## Mathematical Content


In the τ-arithmetic encoding, strict membership a ∈^strict_τ b means
a | b with a ≠ b. For b ≠ 0, this implies a < b, so strict membership
is well-founded (no infinite descending chains).

This well-foundedness is the arithmetic analogue of the Foundation Axiom
(Regularity) in ZF set theory: there is no infinite chain
... ∈_τ x₂ ∈_τ x₁ ∈_τ x₀ (unless 0 is involved).

The restriction to nonzero sets is essential: 0 is the universal set
(everything divides 0), so chains through 0 are degenerate.

---

### `Tau.Sets.tau_strict_mem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L38-L39)
**def
Tau.Sets.tau_strict_mem
(a b : Denotation.TauIdx)
 :Prop**


[I.D33] Strict τ-membership: a properly divides b (a | b and a ≠ b).
Equations
- Tau.Sets.tau_strict_mem a b = (Tau.Sets.tau_mem a b ∧ a ≠ b)
Instances For

---

### `Tau.Sets.tau_strict_mem_irrefl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L41-L43)
**theorem
Tau.Sets.tau_strict_mem_irrefl
(a : Denotation.TauIdx)
 :¬tau_strict_mem a a**


Strict membership is irreflexive.

---

### `Tau.Sets.tau_strict_mem_trans`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L45-L50)
**theorem
Tau.Sets.tau_strict_mem_trans
{a b c : Denotation.TauIdx}

(h1 : tau_strict_mem a b)

(h2 : tau_strict_mem b c)
 :tau_strict_mem a c**


Strict membership is transitive.

---

### `Tau.Sets.tau_strict_mem_lt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L56-L61)
**theorem
Tau.Sets.tau_strict_mem_lt
{a b : Denotation.TauIdx}

(h : tau_strict_mem a b)

(hb : b ≠ 0)
 :a < b**


Strict membership with nonzero target implies strict inequality.
If a | b, a ≠ b, and b ≠ 0, then a < b.

---

### `Tau.Sets.tau_strict_mem_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L63-L65)
**theorem
Tau.Sets.tau_strict_mem_one
{n : Denotation.TauIdx}

(hn : n ≥ 2)
 :tau_strict_mem 1 n**


1 is a strict member of any n ≥ 2.

---

### `Tau.Sets.tau_strict_mem_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L67-L70)
**theorem
Tau.Sets.tau_strict_mem_bound
{a b : Denotation.TauIdx}

(h : tau_strict_mem a b)

(hb : b > 0)
 :a < b**


If a is a strict member of b, and b > 0, then a is strictly smaller.

---

### `Tau.Sets.tau_strict_mem_nz`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L82-L83)
**def
Tau.Sets.tau_strict_mem_nz
(a b : Denotation.TauIdx)
 :Prop**


The "nonzero strict membership" relation: a strictly divides b and b ≠ 0.
Equations
- Tau.Sets.tau_strict_mem_nz a b = (Tau.Sets.tau_strict_mem a b ∧ b ≠ 0)
Instances For

---

### `Tau.Sets.tau_strict_mem_wf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L90-L100)
**theorem
Tau.Sets.tau_strict_mem_wf :WellFounded tau_strict_mem_nz**


[I.P12] Well-foundedness of nonzero strict τ-membership:
there is no infinite descending chain
... ∈^strict_τ x₂ ∈^strict_τ x₁ ∈^strict_τ x₀
when all elements are nonzero.

Proof: tau_strict_mem_nz is a subrelation of Nat.lt (via identity),
and Nat.lt is well-founded.

---

### `Tau.Sets.tau_strict_mem_induction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L102-L108)
**theorem
Tau.Sets.tau_strict_mem_induction
{P : Denotation.TauIdx → Prop}

(h : ∀ (n : Denotation.TauIdx), (∀ (m : Denotation.TauIdx), tau_strict_mem_nz m n → P m) → P n)

(n : Denotation.TauIdx)
 :P n**


From well-foundedness: strong induction on τ-membership.
For nonzero indices, if P holds for all strict τ-members of n,
then P holds for n.

---

### `Tau.Sets.tau_mem_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L114-L117)
**theorem
Tau.Sets.tau_mem_bounded
{b : Denotation.TauIdx}

(hb : b ≠ 0)

(a : Denotation.TauIdx)

(h : tau_mem a b)
 :a ≤ b**


For nonzero b, the set of τ-members is bounded: every member is ≤ b.

---

### `Tau.Sets.strict_mem_chain_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Powerset.lean#L119-L124)
**theorem
Tau.Sets.strict_mem_chain_bound
{a b : Denotation.TauIdx}

(hb : b > 0)

(h : tau_strict_mem a b)
 :a < b**


For nonzero b, strict membership decreases: if a ∈^strict_τ b then a < b.
Combined with a ≥ 1 (since 0 divides nothing nonzero), this bounds
the length of any descending chain to at most b steps.
