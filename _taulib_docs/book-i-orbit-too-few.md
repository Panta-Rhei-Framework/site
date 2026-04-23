---
layout: taulib-doc
title: "TauLib.BookI.Orbit.TooFew"
permalink: /verify/taulib/docs/book-i-orbit-too-few/
lane: verify
module_name: "TauLib.BookI.Orbit.TooFew"
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

# TauLib.Orbit.TooFew


Counter-model: a 4-generator tau-like system cannot assign canonical
channels to all 3 rewiring levels of the iterator ladder.

## Registry Cross-References


- [I.T09b] Four-Generator Ladder Incompleteness — `four_gen_ladder_incomplete`


## Mathematical Content


If we drop η (keeping only α, π, γ, ω), only 2 solenoidal generators
remain (π and γ). The iterator ladder needs 3 rewiring channels
(addition, multiplication, exponentiation), so the exponentiation level
is orphaned — no generator carries it.

Interestingly, Gen4 *does* still have rigidity (any automorphism fixing
α and ω must be the identity), because with only 2 solenoidal generators,
there is no same-role pair to swap. This highlights the tradeoff:


- 4 generators: rigidity ✓, completeness ✗

- 5 generators: rigidity ✓, completeness ✓ (sweet spot)

- 6 generators: rigidity ✗, completeness ✓


---

### `Tau.Orbit.TooFew.Gen4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L37-L43)
**inductive
Tau.Orbit.TooFew.Gen4 :Type**


A hypothetical 4-generator alphabet: α, π, γ, ω (no η).

- alpha : Gen4
- pi : Gen4
- gamma : Gen4
- omega : Gen4
Instances For

---

### `Tau.Orbit.TooFew.instDecidableEqGen4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L43-L43)
**instance
Tau.Orbit.TooFew.instDecidableEqGen4 :DecidableEq Gen4**

Equations
- Tau.Orbit.TooFew.instDecidableEqGen4 x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.Orbit.TooFew.instReprGen4.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L43-L43)
**def
Tau.Orbit.TooFew.instReprGen4.repr :Gen4 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
- Tau.Orbit.TooFew.instReprGen4.repr Tau.Orbit.TooFew.Gen4.pi prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Orbit.TooFew.Gen4.pi")).group
 prec✝
Instances For

---

### `Tau.Orbit.TooFew.instReprGen4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L43-L43)
**instance
Tau.Orbit.TooFew.instReprGen4 :Repr Gen4**

Equations
- Tau.Orbit.TooFew.instReprGen4 = { reprPrec := Tau.Orbit.TooFew.instReprGen4.repr }

---

### `Tau.Orbit.TooFew.Gen4.toNat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L47-L52)
**def
Tau.Orbit.TooFew.Gen4.toNat :Gen4 → Nat**


Canonical ordering: α=0, π=1, γ=2, ω=3.
Equations
- Tau.Orbit.TooFew.Gen4.alpha.toNat = 0
- Tau.Orbit.TooFew.Gen4.pi.toNat = 1
- Tau.Orbit.TooFew.Gen4.gamma.toNat = 2
- Tau.Orbit.TooFew.Gen4.omega.toNat = 3
Instances For

---

### `Tau.Orbit.TooFew.solenoidal4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L58-L59)
**def
Tau.Orbit.TooFew.solenoidal4 :List Gen4**


The solenoidal generators of Gen4: only {π, γ}.
Equations
- Tau.Orbit.TooFew.solenoidal4 = [Tau.Orbit.TooFew.Gen4.pi, Tau.Orbit.TooFew.Gen4.gamma]
Instances For

---

### `Tau.Orbit.TooFew.solenoidal4_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L61-L62)
**theorem
Tau.Orbit.TooFew.solenoidal4_count :solenoidal4.length = 2**


Only 2 solenoidal generators in Gen4.

---

### `Tau.Orbit.TooFew.Ladder4Level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L64-L70)
**inductive
Tau.Orbit.TooFew.Ladder4Level :Type**


The 4 hyperoperation levels (same as Gen5, but channel assignment fails).

- rho_level : Ladder4Level
- add_level : Ladder4Level
- mul_level : Ladder4Level
- exp_level : Ladder4Level
Instances For

---

### `Tau.Orbit.TooFew.instDecidableEqLadder4Level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L70-L70)
**instance
Tau.Orbit.TooFew.instDecidableEqLadder4Level :DecidableEq Ladder4Level**

Equations
- Tau.Orbit.TooFew.instDecidableEqLadder4Level x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.Orbit.TooFew.instReprLadder4Level.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L70-L70)
**def
Tau.Orbit.TooFew.instReprLadder4Level.repr :Ladder4Level → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Orbit.TooFew.instReprLadder4Level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L70-L70)
**instance
Tau.Orbit.TooFew.instReprLadder4Level :Repr Ladder4Level**

Equations
- Tau.Orbit.TooFew.instReprLadder4Level = { reprPrec := Tau.Orbit.TooFew.instReprLadder4Level.repr }

---

### `Tau.Orbit.TooFew.ladder4Channel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L72-L78)
**def
Tau.Orbit.TooFew.ladder4Channel :Ladder4Level → Option Gen4**


Channel assignment in Gen4: addition gets π, multiplication gets γ,
but exponentiation has no available channel.
Equations
- Tau.Orbit.TooFew.ladder4Channel Tau.Orbit.TooFew.Ladder4Level.rho_level = none
- Tau.Orbit.TooFew.ladder4Channel Tau.Orbit.TooFew.Ladder4Level.add_level = some Tau.Orbit.TooFew.Gen4.pi
- Tau.Orbit.TooFew.ladder4Channel Tau.Orbit.TooFew.Ladder4Level.mul_level = some Tau.Orbit.TooFew.Gen4.gamma
- Tau.Orbit.TooFew.ladder4Channel Tau.Orbit.TooFew.Ladder4Level.exp_level = none
Instances For

---

### `Tau.Orbit.TooFew.four_gen_exp_no_channel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L84-L85)
**theorem
Tau.Orbit.TooFew.four_gen_exp_no_channel :ladder4Channel Ladder4Level.exp_level = none**


Exponentiation has no canonical channel in Gen4.

---

### `Tau.Orbit.TooFew.solenoidal4_deficit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L87-L88)
**theorem
Tau.Orbit.TooFew.solenoidal4_deficit :solenoidal4.length < 3**


The deficit: 2 solenoidal generators for 3 rewiring levels needed.

---

### `Tau.Orbit.TooFew.four_gen_ladder_incomplete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L90-L100)
**theorem
Tau.Orbit.TooFew.four_gen_ladder_incomplete :ladder4Channel Ladder4Level.exp_level = none ∧ solenoidal4.length < 3**


[I.T09b] **Four-Generator Ladder Incompleteness**:
With only 4 generators, the iterator ladder cannot be completed.
The exponentiation level has no canonical orbit channel because
only 2 solenoidal generators (π, γ) exist, but 3 rewiring levels
(addition, multiplication, exponentiation) are needed.

This shows that dropping a generator from 5 to 4 breaks
ladder completeness — 5 generators is *necessary*.

---

### `Tau.Orbit.TooFew.Obj4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L106-L110)
**structure
Tau.Orbit.TooFew.Obj4 :Type**


Objects of the 4-generator system.

- seed : Gen4
- depth : Nat
Instances For

---

### `Tau.Orbit.TooFew.instDecidableEqObj4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L110-L110)
**instance
Tau.Orbit.TooFew.instDecidableEqObj4 :DecidableEq Obj4**

Equations
- Tau.Orbit.TooFew.instDecidableEqObj4 = Tau.Orbit.TooFew.instDecidableEqObj4.decEq

---

### `Tau.Orbit.TooFew.instDecidableEqObj4.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L110-L110)
**def
Tau.Orbit.TooFew.instDecidableEqObj4.decEq
(x✝ x✝¹ : Obj4)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.Orbit.TooFew.instDecidableEqObj4.decEq { seed := a, depth := a_1 } { seed := b, depth := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.Orbit.TooFew.instReprObj4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L110-L110)
**instance
Tau.Orbit.TooFew.instReprObj4 :Repr Obj4**

Equations
- Tau.Orbit.TooFew.instReprObj4 = { reprPrec := Tau.Orbit.TooFew.instReprObj4.repr }

---

### `Tau.Orbit.TooFew.instReprObj4.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L110-L110)
**def
Tau.Orbit.TooFew.instReprObj4.repr :Obj4 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Orbit.TooFew.rho4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L112-L116)
**def
Tau.Orbit.TooFew.rho4
(x : Obj4)
 :Obj4**


The progression operator ρ₄: fixes ω-fiber, increments depth otherwise.
Equations
- Tau.Orbit.TooFew.rho4 x = match x.seed with
 | Tau.Orbit.TooFew.Gen4.omega => x
 | x_1 => { seed := x.seed, depth := x.depth + 1 }
Instances For

---

### `Tau.Orbit.TooFew.four_gen_order_rigid`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L118-L162)
**theorem
Tau.Orbit.TooFew.four_gen_order_rigid
(f : Gen4 → Gen4)

(hf_alpha : f Gen4.alpha = Gen4.alpha)

(hf_omega : f Gen4.omega = Gen4.omega)

(hf_order : ∀ (g h : Gen4), g.toNat < h.toNat → (f g).toNat < (f h).toNat)

(g : Gen4)
 :f g = g**


The only permutations of Gen4 fixing α and ω are
id and the transposition (π γ). The transposition reverses
the canonical order (π < γ becomes γ > π), so an order-preserving
bijection must be the identity.

---

### `Tau.Orbit.TooFew.four_gen_rigidity_holds`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/TooFew.lean#L164-L178)
**theorem
Tau.Orbit.TooFew.four_gen_rigidity_holds
(f : Gen4 → Gen4)
 :f Gen4.alpha = Gen4.alpha →
 f Gen4.omega = Gen4.omega → (∀ (g h : Gen4), g.toNat < h.toNat → (f g).toNat < (f h).toNat) → ∀ (g : Gen4), f g = g**


**Four-Generator Order-Preserving Rigidity**:
Any order-preserving ρ-automorphism of the 4-generator system is the identity.

Note: unlike the 5-generator system where rigidity holds for ALL automorphisms
(given seed preservation at depth 0), the 4-generator system has rigidity only
for ORDER-PRESERVING automorphisms. The transposition (π γ) is a valid
non-order-preserving automorphism. This weaker form of rigidity is sufficient
for the Minimal Alphabet Theorem.
