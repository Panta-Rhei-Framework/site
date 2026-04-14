---
layout: taulib-doc
title: "TauLib.BookI.Orbit.TooMany"
permalink: /verify/taulib/docs/book-i-orbit-too-many/
lane: verify
module_name: "TauLib.BookI.Orbit.TooMany"
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

# TauLib.Orbit.TooMany


Counter-model: a 6-generator tau-like system admits a non-trivial
ρ-automorphism, breaking rigidity.

## Registry Cross-References


- [I.T09a] Six-Generator Rigidity Failure — `six_gen_rigidity_fails`


## Mathematical Content


If we add a 6th generator ζ (between η and ω), the resulting system
satisfies all K-axiom analogues but has a non-trivial automorphism:
the swap η ↔ ζ commutes with ρ₆ and is an involution, yet is not
the identity. This shows that 5 generators is not merely sufficient
for rigidity — it is *necessary*.

The key insight: with 6 generators, η and ζ are both solenoidal
(neither the counting scaffold α nor the fixed-point ω) and play
interchangeable structural roles, so swapping them preserves all
axioms while moving objects.

---

### `Tau.Orbit.TooMany.Gen6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L36-L44)
**inductive
Tau.Orbit.TooMany.Gen6 :Type**


A hypothetical 6-generator alphabet: α, π, γ, η, ζ, ω.

- alpha : Gen6
- pi : Gen6
- gamma : Gen6
- eta : Gen6
- zeta : Gen6
- omega : Gen6
Instances For

---

### `Tau.Orbit.TooMany.instDecidableEqGen6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L44-L44)
**instance
Tau.Orbit.TooMany.instDecidableEqGen6 :DecidableEq Gen6**

Equations
- Tau.Orbit.TooMany.instDecidableEqGen6 x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.Orbit.TooMany.instReprGen6.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L44-L44)
**def
Tau.Orbit.TooMany.instReprGen6.repr :Gen6 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Orbit.TooMany.instReprGen6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L44-L44)
**instance
Tau.Orbit.TooMany.instReprGen6 :Repr Gen6**

Equations
- Tau.Orbit.TooMany.instReprGen6 = { reprPrec := Tau.Orbit.TooMany.instReprGen6.repr }

---

### `Tau.Orbit.TooMany.Gen6.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L48-L55)
**def
Tau.Orbit.TooMany.Gen6.toNat :Gen6 → Nat**


Canonical ordering: α=0, π=1, γ=2, η=3, ζ=4, ω=5.
Equations
- Tau.Orbit.TooMany.Gen6.alpha.toNat = 0
- Tau.Orbit.TooMany.Gen6.pi.toNat = 1
- Tau.Orbit.TooMany.Gen6.gamma.toNat = 2
- Tau.Orbit.TooMany.Gen6.eta.toNat = 3
- Tau.Orbit.TooMany.Gen6.zeta.toNat = 4
- Tau.Orbit.TooMany.Gen6.omega.toNat = 5
Instances For

---

### `Tau.Orbit.TooMany.Obj6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L61-L65)
**structure
Tau.Orbit.TooMany.Obj6 :Type**


Objects of the 6-generator system: (seed, depth) pairs.

- seed : Gen6
- depth : Nat
Instances For

---

### `Tau.Orbit.TooMany.instDecidableEqObj6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L65-L65)
**instance
Tau.Orbit.TooMany.instDecidableEqObj6 :DecidableEq Obj6**

Equations
- Tau.Orbit.TooMany.instDecidableEqObj6 = Tau.Orbit.TooMany.instDecidableEqObj6.decEq

---

### `Tau.Orbit.TooMany.instDecidableEqObj6.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L65-L65)
**def
Tau.Orbit.TooMany.instDecidableEqObj6.decEq
(x✝ x✝¹ : Obj6)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.Orbit.TooMany.instDecidableEqObj6.decEq { seed := a, depth := a_1 } { seed := b, depth := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.Orbit.TooMany.instReprObj6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L65-L65)
**instance
Tau.Orbit.TooMany.instReprObj6 :Repr Obj6**

Equations
- Tau.Orbit.TooMany.instReprObj6 = { reprPrec := Tau.Orbit.TooMany.instReprObj6.repr }

---

### `Tau.Orbit.TooMany.instReprObj6.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L65-L65)
**def
Tau.Orbit.TooMany.instReprObj6.repr :Obj6 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Orbit.TooMany.rho6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L67-L71)
**def
Tau.Orbit.TooMany.rho6
(x : Obj6)
 :Obj6**


The progression operator ρ₆: fixes ω-fiber, increments depth otherwise.
Equations
- Tau.Orbit.TooMany.rho6 x = match x.seed with
 | Tau.Orbit.TooMany.Gen6.omega => x
 | x_1 => { seed := x.seed, depth := x.depth + 1 }
Instances For

---

### `Tau.Orbit.TooMany.K1_six`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L77-L83)
**theorem
Tau.Orbit.TooMany.K1_six :Gen6.alpha.toNat < Gen6.pi.toNat ∧ Gen6.pi.toNat < Gen6.gamma.toNat ∧ Gen6.gamma.toNat < Gen6.eta.toNat ∧ Gen6.eta.toNat < Gen6.zeta.toNat ∧ Gen6.zeta.toNat < Gen6.omega.toNat**


K1₆: The generators are strictly ordered.

---

### `Tau.Orbit.TooMany.K2_six`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L85-L87)
**theorem
Tau.Orbit.TooMany.K2_six
(d : Nat)
 :rho6 { seed := Gen6.omega, depth := d } = { seed := Gen6.omega, depth := d }**


K2₆: ω is the unique fixed point of ρ₆.

---

### `Tau.Orbit.TooMany.K4_six`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L89-L92)
**theorem
Tau.Orbit.TooMany.K4_six
(g : Gen6)

(hg : g ≠ Gen6.omega)

(d : Nat)
 :rho6 { seed := g, depth := d } = { seed := g, depth := d + 1 }**


K4₆: ρ₆ increments depth for non-ω generators.

---

### `Tau.Orbit.TooMany.swap_ez`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L98-L102)
**def
Tau.Orbit.TooMany.swap_ez :Gen6 → Gen6**


Swap η and ζ, fix everything else.
Equations
- Tau.Orbit.TooMany.swap_ez Tau.Orbit.TooMany.Gen6.eta = Tau.Orbit.TooMany.Gen6.zeta
- Tau.Orbit.TooMany.swap_ez Tau.Orbit.TooMany.Gen6.zeta = Tau.Orbit.TooMany.Gen6.eta
- Tau.Orbit.TooMany.swap_ez x✝ = x✝
Instances For

---

### `Tau.Orbit.TooMany.swap6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L104-L105)
**def
Tau.Orbit.TooMany.swap6
(x : Obj6)
 :Obj6**


Lift the generator swap to objects.
Equations
- Tau.Orbit.TooMany.swap6 x = { seed := Tau.Orbit.TooMany.swap_ez x.seed, depth := x.depth }
Instances For

---

### `Tau.Orbit.TooMany.swap_ez_invol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L107-L109)
**theorem
Tau.Orbit.TooMany.swap_ez_invol
(g : Gen6)
 :swap_ez (swap_ez g) = g**


swap_ez is an involution on generators.

---

### `Tau.Orbit.TooMany.swap6_involution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L111-L114)
**theorem
Tau.Orbit.TooMany.swap6_involution
(x : Obj6)
 :swap6 (swap6 x) = x**


swap6 is an involution on objects.

---

### `Tau.Orbit.TooMany.swap6_rho_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L116-L119)
**theorem
Tau.Orbit.TooMany.swap6_rho_comm
(x : Obj6)
 :swap6 (rho6 x) = rho6 (swap6 x)**


swap6 commutes with ρ₆.

---

### `Tau.Orbit.TooMany.swap6_ne_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L121-L123)
**theorem
Tau.Orbit.TooMany.swap6_ne_id :swap6 { seed := Gen6.eta, depth := 0 } ≠ { seed := Gen6.eta, depth := 0 }**


swap6 is NOT the identity: it moves ⟨η, 0⟩.

---

### `Tau.Orbit.TooMany.six_gen_rigidity_fails`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L129-L144)
**theorem
Tau.Orbit.TooMany.six_gen_rigidity_fails :∃ (f : Obj6 → Obj6), (∀ (x : Obj6), f (rho6 x) = rho6 (f x)) ∧ (∀ (x : Obj6), f (f x) = x) ∧ ¬∀ (x : Obj6), f x = x**


[I.T09a] **Six-Generator Rigidity Failure**:
A 6-generator tau-like system admits a non-trivial ρ-automorphism.

The witness is the swap η ↔ ζ, which:
(1) commutes with ρ₆ (preserves all dynamical structure)
(2) is an involution (self-inverse, hence bijective)
(3) is not the identity (moves ⟨η, 0⟩ to ⟨ζ, 0⟩)

This shows that adding a 6th generator breaks the rigidity
property Aut(τ) = {id} that holds for exactly 5 generators.

---

### `Tau.Orbit.TooMany.solenoidal6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L150-L153)
**def
Tau.Orbit.TooMany.solenoidal6 :List Gen6**


In Gen6, the solenoidal generators are {π, γ, η, ζ} — four of them.
This is one more than the 3 rewiring levels need, creating the
η ↔ ζ ambiguity that enables the swap automorphism.
Equations
- Tau.Orbit.TooMany.solenoidal6 = [Tau.Orbit.TooMany.Gen6.pi, Tau.Orbit.TooMany.Gen6.gamma, Tau.Orbit.TooMany.Gen6.eta, Tau.Orbit.TooMany.Gen6.zeta]
Instances For

---

### `Tau.Orbit.TooMany.solenoidal6_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L155-L155)
**theorem
Tau.Orbit.TooMany.solenoidal6_count :solenoidal6.length = 4**


---

### `Tau.Orbit.TooMany.solenoidal6_surplus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/TooMany.lean#L157-L158)
**theorem
Tau.Orbit.TooMany.solenoidal6_surplus :solenoidal6.length > 3**


The surplus: 4 solenoidal generators for only 3 rewiring levels.
