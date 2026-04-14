---
layout: taulib-doc
title: "TauLib.BookI.Sets.Membership"
permalink: /verify/taulib/docs/book-i-sets-membership/
lane: verify
module_name: "TauLib.BookI.Sets.Membership"
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

# TauLib.Sets.Membership


τ-Membership: divisibility as the internal membership relation on τ-Idx.

## Registry Cross-References


- [I.D31] τ-Membership — `tau_mem`, `tau_mem_iff_dvd`

- [I.P10] Membership Decidability — `instDecidableTauMem`


## Ground Truth Sources


- chunk_0350_M003012: Membership = divisibility in τ-Idx arithmetic


## Mathematical Content


In Category τ, the membership relation a ∈_τ b is identified with
index divisibility: a ∈_τ b iff a | b. This encodes set-membership
arithmetically, where each natural number IS a set (its divisor set).

**Convention**: τ-Idx semantically represents ℕ⁺ = {1, 2, 3, ...},
the positive natural numbers discovered as the α-orbit O_α.
Zero is NOT a valid orbit index — it first appears in ring
structures (Part VIII, boundary ring). Lean uses `TauIdx = Nat`
for convenience; all orbit-meaningful results carry nonzero guards.

**τ as class**: τ is a proper class (a category), not a set.
"x belongs to τ" means x is an object of the category — class
membership, not set membership. The internal set theory developed
here lives INSIDE τ, encoded arithmetically on the α-orbit.

Under this encoding:


- 1 is the unit (α_1 represents {α_1}, the minimal singleton)

- Primes are atoms (only 1 and themselves as members)

- The orbit-set of ω gives the universal collection O_α ∪ {ω}


---

### `Tau.Sets.tau_mem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L47-L49)
**def
Tau.Sets.tau_mem
(a b : Denotation.TauIdx)
 :Prop**


[I.D31] τ-membership: a ∈_τ b iff a divides b.
Every natural number IS its divisor set.
Equations
- Tau.Sets.tau_mem a b = Tau.Coordinates.idx_divides a b
Instances For

---

### `Tau.Sets.tau_mem_iff_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L51-L53)
**theorem
Tau.Sets.tau_mem_iff_dvd
(a b : Denotation.TauIdx)
 :tau_mem a b ↔ a ∣ b**


Bridge: τ-membership is Nat divisibility.

---

### `Tau.Sets.instDecidableTauMem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L55-L57)
**instance
Tau.Sets.instDecidableTauMem
(a b : Denotation.TauIdx)
 :Decidable (tau_mem a b)**


[I.P10] τ-membership is decidable.
Equations
- Tau.Sets.instDecidableTauMem a b = Tau.Coordinates.instDecidableIdxDivides a b

---

### `Tau.Sets.tau_mem_refl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L63-L65)
**theorem
Tau.Sets.tau_mem_refl
(a : Denotation.TauIdx)
 :tau_mem a a**


Reflexivity: every τ-set is a member of itself.

---

### `Tau.Sets.tau_mem_antisymm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L67-L69)
**theorem
Tau.Sets.tau_mem_antisymm
{a b : Denotation.TauIdx}

(h1 : tau_mem a b)

(h2 : tau_mem b a)
 :a = b**


Antisymmetry: mutual membership implies equality.

---

### `Tau.Sets.tau_mem_trans`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L71-L73)
**theorem
Tau.Sets.tau_mem_trans
{a b c : Denotation.TauIdx}

(h1 : tau_mem a b)

(h2 : tau_mem b c)
 :tau_mem a c**


Transitivity: membership is transitive.

---

### `Tau.Sets.tau_mem_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L75-L77)
**theorem
Tau.Sets.tau_mem_one
(b : Denotation.TauIdx)
 :tau_mem 1 b**


1 (the empty set) is a member of every τ-set.

---

### `Tau.Sets.tau_mem_le`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L79-L81)
**theorem
Tau.Sets.tau_mem_le
{a b : Denotation.TauIdx}

(h : tau_mem a b)

(hb : b ≠ 0)
 :a ≤ b**


Membership is bounded: a ∈_τ b with b ≠ 0 implies a ≤ b.

---

### `Tau.Sets.tau_unit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L87-L90)
**def
Tau.Sets.tau_unit :Denotation.TauIdx**


The unit element in τ-arithmetic is 1 (α_1): its only τ-member is 1 itself.
(The only divisor of 1 is 1.) This is the minimal τ-set — not truly
"empty" since α_1 ∈_τ α_1 by reflexivity of divisibility.
Equations
- Tau.Sets.tau_unit = 1
Instances For

---

### `Tau.Sets.tau_unit_char`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L92-L97)
**theorem
Tau.Sets.tau_unit_char
(a : Denotation.TauIdx)

(h : tau_mem a tau_unit)
 :a = 1**


The unit has no members other than itself: if a ∈_τ 1, then a = 1.

---

### `Tau.Sets.singleton_char`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L99-L119)
**theorem
Tau.Sets.singleton_char
(p : Denotation.TauIdx)

(hp0 : p ≠ 0)
 :(∀ (d : Denotation.TauIdx), tau_mem d p → d = 1 ∨ d = p) ↔ p = 1 ∨ Coordinates.idx_prime p**


A nonzero τ-set p is a singleton (only 1 and p are τ-members) iff p = 1 or p is prime.

---

### `Tau.Sets.tau_mem_mul_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L125-L130)
**theorem
Tau.Sets.tau_mem_mul_right
{a b : Denotation.TauIdx}

(h : tau_mem a b)

(c : Denotation.TauIdx)
 :tau_mem a (Denotation.idx_mul b c)**


Product membership: if a ∈_τ b, then a ∈_τ b*c.

---

### `Tau.Sets.tau_mem_mul_left`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Membership.lean#L132-L137)
**theorem
Tau.Sets.tau_mem_mul_left
{a c : Denotation.TauIdx}

(h : tau_mem a c)

(b : Denotation.TauIdx)
 :tau_mem a (Denotation.idx_mul b c)**


Product membership (left): if a ∈_τ c, then a ∈_τ b*c.
