---
layout: taulib-doc
title: "TauLib.BookI.Sets.OrbitSets"
permalink: /verify/taulib/docs/book-i-sets-orbit-sets/
lane: verify
module_name: "TauLib.BookI.Sets.OrbitSets"
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

# TauLib.Sets.OrbitSets


Orbit-Set Correspondence: each τ-object x determines a characteristic
set Set(x) inside the α-orbit, defined by orbit-specific formulas.

## Registry Cross-References


- [I.D94] Orbit-Set Map — `orbit_set_alpha`, `orbit_set_pi`,
`orbit_set_gamma`, `orbit_set_eta`, `orbit_set_omega`

- [I.P40] Extensionality — `prime_atom`, `orbit_set_alpha_has_one`

- [I.P41] Self-Containment Partition — `self_containment_alpha`,
`self_containment_omega`, `not_self_containment_pi`

- [I.P42] Order Bound — `orbit_set_order_bound`

- [I.R28] Inseparability of ℕ and ω — `nat_not_internal_set`

- [I.R29] Finite-Infinite Boundary — structural (γ/η infinite, α/π finite)

- [I.R30] Duality and Atoms — `prime_atom`, `gamma_eta_intersection`


## Ground Truth Sources


- Chapter 83 (Book I, 2nd Ed): Orbit-Set Correspondence


## Mathematical Content


Each generator g determines a "set function" Set(g_n) that maps
a τ-object to a predicate on TauIdx. The five formulas:


- Set(α_n) = { α_k : k ∈_τ n } (= { α_k : k | n }, divisor set)

- Set(π_n) = { α_k : k = 1 ∨ ∃ j ≤ n, k = nthPrime j }

- Set(γ_n) = { α_k : ∃ e, k = (nthPrime n) ^ e }

- Set(η_n) = { α_k : ∃ j, k = (nthPrime j) ^ n } (n ≥ 1)

- Set(ω) = { x : TauObj : x.seed = alpha ∨ (x.seed = omega ∧ x.depth = 0) }


**Key identity**: orbit_set_alpha IS τ-membership (I.D31).
Set(α_n) = {α_k : tau_mem k n}. This is not merely an equivalence
but the SAME relation: the orbit-set for the α-orbit and the
internal membership relation from Part VIII are one concept.

All orbit indices are meaningful only for n ≥ 1 (ℕ⁺).

---

### `Tau.Sets.orbit_set_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L52-L58)
**def
Tau.Sets.orbit_set_alpha
(n k : Denotation.TauIdx)
 :Prop**


[I.D94] Set(α_n): the divisor set = τ-membership.
α_k ∈ Set(α_n) iff tau_mem k n (iff k | n).

This IS τ-membership (I.D31) — the orbit-set for α and the
internal membership relation are the same concept. We define
orbit_set_alpha in terms of tau_mem to enforce this identity.
Equations
- Tau.Sets.orbit_set_alpha n k = Tau.Sets.tau_mem k n
Instances For

---

### `Tau.Sets.orbit_set_alpha_iff_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L60-L63)@[simp]

**theorem
Tau.Sets.orbit_set_alpha_iff_dvd
(n k : Denotation.TauIdx)
 :orbit_set_alpha n k ↔ k ∣ n**


Simp lemma: orbit_set_alpha unfolds to Nat divisibility for proofs.

---

### `Tau.Sets.instDecidableOrbitSetAlpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L65-L66)
**noncomputable instance
Tau.Sets.instDecidableOrbitSetAlpha
(n k : Denotation.TauIdx)
 :Decidable (orbit_set_alpha n k)**

Equations
- Tau.Sets.instDecidableOrbitSetAlpha n k = Classical.dec (Tau.Sets.orbit_set_alpha n k)

---

### `Tau.Sets.orbit_set_alpha_eq_tau_mem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L72-L78)
**theorem
Tau.Sets.orbit_set_alpha_eq_tau_mem
(n k : Denotation.TauIdx)
 :orbit_set_alpha n k ↔ tau_mem k n**


The orbit-set for α IS τ-membership — by definition.
This is a definitional identity, not just a propositional equivalence.
Part VIII's single-orbit set theory (∈_τ = divisibility) and the
five-orbit representation theory of Chapter 83 are one theory.

---

### `Tau.Sets.orbit_set_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L84-L88)
**def
Tau.Sets.orbit_set_pi
(n k : Denotation.TauIdx)
 :Prop**


[I.D94] Set(π_n): the set of α-orbit indices belonging to the
orbit-set of π_n.
α_k ∈ Set(π_n) iff k = 1 or there exists j ≤ n with k = nthPrime j.
Equations
- Tau.Sets.orbit_set_pi n k = (k = 1 ∨ ∃ (j : Tau.Denotation.TauIdx), j ≤ n ∧ k = Tau.Coordinates.nthPrime j)
Instances For

---

### `Tau.Sets.instDecidableOrbitSetPi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L90-L91)
**noncomputable instance
Tau.Sets.instDecidableOrbitSetPi
(n k : Denotation.TauIdx)
 :Decidable (orbit_set_pi n k)**

Equations
- Tau.Sets.instDecidableOrbitSetPi n k = Classical.dec (Tau.Sets.orbit_set_pi n k)

---

### `Tau.Sets.orbit_set_gamma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L97-L101)
**def
Tau.Sets.orbit_set_gamma
(n k : Denotation.TauIdx)
 :Prop**


[I.D94] Set(γ_n): the set of α-orbit indices belonging to the
orbit-set of γ_n.
α_k ∈ Set(γ_n) iff k = p_n ^ e for some e ≥ 0, where p_n = nthPrime n.
Equations
- Tau.Sets.orbit_set_gamma n k = ∃ (e : Tau.Denotation.TauIdx), k = Tau.Coordinates.nthPrime n ^ e
Instances For

---

### `Tau.Sets.instDecidableOrbitSetGamma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L103-L104)
**noncomputable instance
Tau.Sets.instDecidableOrbitSetGamma
(n k : Denotation.TauIdx)
 :Decidable (orbit_set_gamma n k)**

Equations
- Tau.Sets.instDecidableOrbitSetGamma n k = Classical.dec (Tau.Sets.orbit_set_gamma n k)

---

### `Tau.Sets.orbit_set_eta`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L110-L114)
**def
Tau.Sets.orbit_set_eta
(n k : Denotation.TauIdx)
 :Prop**


[I.D94] Set(η_n) for n ≥ 1: the set of α-orbit indices belonging
to the orbit-set of η_n.
α_k ∈ Set(η_n) iff k = p_j ^ n for some j.
Equations
- Tau.Sets.orbit_set_eta n k = ∃ (j : Tau.Denotation.TauIdx), k = Tau.Coordinates.nthPrime j ^ n
Instances For

---

### `Tau.Sets.instDecidableOrbitSetEta`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L116-L117)
**noncomputable instance
Tau.Sets.instDecidableOrbitSetEta
(n k : Denotation.TauIdx)
 :Decidable (orbit_set_eta n k)**

Equations
- Tau.Sets.instDecidableOrbitSetEta n k = Classical.dec (Tau.Sets.orbit_set_eta n k)

---

### `Tau.Sets.orbit_set_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L123-L131)
**def
Tau.Sets.orbit_set_omega
(x : Kernel.TauObj)
 :Prop**


[I.D94] Set(ω): the set of τ-objects belonging to the orbit-set of ω.
x ∈ Set(ω) iff x.seed = alpha or (x.seed = omega and x.depth = 0).

Note: this predicate acts on TauObj, not TauIdx — ω's orbit-set
includes itself (the TauObj ⟨omega, 0⟩), which cannot be represented
as a pure TauIdx predicate. Set(ω) = O_α ∪ {ω} is the universal
collection — one-point compactification of the counting scaffold.
Equations
- Tau.Sets.orbit_set_omega x = (x.seed = Tau.Kernel.Generator.alpha ∨ x.seed = Tau.Kernel.Generator.omega ∧ x.depth = 0)
Instances For

---

### `Tau.Sets.instDecidableOrbitSetOmega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L133-L135)
**instance
Tau.Sets.instDecidableOrbitSetOmega
(x : Kernel.TauObj)
 :Decidable (orbit_set_omega x)**

Equations
- Tau.Sets.instDecidableOrbitSetOmega x = id instDecidableOr

---

### `Tau.Sets.self_containment_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L141-L144)
**theorem
Tau.Sets.self_containment_alpha
(n : Denotation.TauIdx)
 :orbit_set_alpha n n**


[I.P41a] Self-containment for α: α_n ∈ Set(α_n) for all n.
This is tau_mem_refl restated in orbit-set language.

---

### `Tau.Sets.self_containment_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L146-L149)
**theorem
Tau.Sets.self_containment_omega :orbit_set_omega { seed := Kernel.Generator.omega, depth := 0 }**


[I.P41b] Self-containment for ω: ⟨omega, 0⟩ ∈ Set(ω).
Proof: seed = omega and depth = 0.

---

### `Tau.Sets.not_self_containment_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L155-L164)
**theorem
Tau.Sets.not_self_containment_pi
(n : Denotation.TauIdx)
 :{ seed := Kernel.Generator.pi, depth := n }.seed ≠ Kernel.Generator.alpha**


[I.P41c] Type-level separation for π: π_n (as a TauObj) cannot
appear in Set(π_n), because orbit_set_pi maps TauIdx → Prop
(it selects α-orbit indices), while π_n = ⟨pi, n⟩ has seed ≠ alpha.

We formalize this as: for every n, ⟨pi, n⟩.seed ≠ alpha.
The orbit-set and the original object live in different
type-level compartments.

---

### `Tau.Sets.orbit_set_order_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L170-L174)
**theorem
Tau.Sets.orbit_set_order_bound
(n k : Denotation.TauIdx)

(h : orbit_set_alpha n k)

(hn : n ≠ 0)
 :k ≤ n**


[I.P42] Order bound: if α_k ∈ Set(α_n) and n ≠ 0, then k ≤ n.
This is tau_mem_le restated in orbit-set language.

---

### `Tau.Sets.prime_atom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L180-L191)
**theorem
Tau.Sets.prime_atom
(p : Denotation.TauIdx)

(hp : Coordinates.idx_prime p)

(k : Denotation.TauIdx)
 :orbit_set_alpha p k ↔ k = 1 ∨ k = p**


[I.R30] Prime atom theorem: if p is prime, then
Set(α_p) = {1, p}.
The only divisors of a prime are 1 and itself.

---

### `Tau.Sets.orbit_set_alpha_has_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L197-L200)
**theorem
Tau.Sets.orbit_set_alpha_has_one
(n : Denotation.TauIdx)
 :orbit_set_alpha n 1**


1 is always in Set(α_n) for every n.
This is tau_mem_one restated in orbit-set language.

---

### `Tau.Sets.orbit_set_alpha_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L206-L211)
**theorem
Tau.Sets.orbit_set_alpha_bounded
(n : Denotation.TauIdx)

(hn : n ≠ 0)
 :¬orbit_set_alpha n (n + 1)**


For nonzero n, n+1 is NOT in Set(α_n) (bounded by n).

---

### `Tau.Sets.alpha_orbit_set_not_all`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L213-L216)
**theorem
Tau.Sets.alpha_orbit_set_not_all
(n : Denotation.TauIdx)

(hn : n ≠ 0)
 :∃ (m : Denotation.TauIdx), ¬orbit_set_alpha n m**


For nonzero n, no single Set(α_n) captures all natural numbers.

---

### `Tau.Sets.omega_orbit_set_exceeds_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L218-L222)
**theorem
Tau.Sets.omega_orbit_set_exceeds_alpha :orbit_set_omega { seed := Kernel.Generator.omega, depth := 0 } ∧ { seed := Kernel.Generator.omega, depth := 0 }.seed ≠ Kernel.Generator.alpha**


[I.R28] ω's orbit-set includes ω itself, so it does not live purely
in the α-orbit. This is the TauObj-level witness that Set(ω) ≠ O_α.

---

### `Tau.Sets.nat_not_internal_set`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L224-L232)
**theorem
Tau.Sets.nat_not_internal_set :(∀ (n : Denotation.TauIdx), n ≠ 0 → ∃ (m : Denotation.TauIdx), ¬orbit_set_alpha n m) ∧ orbit_set_omega { seed := Kernel.Generator.omega, depth := 0 } ∧ { seed := Kernel.Generator.omega, depth := 0 }.seed ≠ Kernel.Generator.alpha**


[I.R28] Combined "no internal copy" result: for nonzero n, no Set(α_n)
captures all of ℕ⁺, and Set(ω) strictly exceeds O_α.

This expresses the inseparability of ℕ and ω: O_α ≅ ℕ⁺ is NOT
a valid τ-internal set. The closest is Set(ω) = O_α ∪ {ω}.

---

### `Tau.Sets.gamma_eta_intersection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L238-L241)
**theorem
Tau.Sets.gamma_eta_intersection
(n m : Denotation.TauIdx)
 :orbit_set_gamma n (Coordinates.nthPrime n ^ m) ∧ orbit_set_eta m (Coordinates.nthPrime n ^ m)**


γ-η duality witness: (nthPrime n)^m is in both Set(γ_n) and Set(η_m).

---

### `Tau.Sets.orbit_set_pi_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L247-L252)
**theorem
Tau.Sets.orbit_set_pi_monotone
(n k : Denotation.TauIdx)

(h : orbit_set_pi n k)
 :orbit_set_pi (n + 1) k**


Set(π_n) ⊆ Set(π_{n+1}): the π orbit-set grows monotonically.

---

### `Tau.Sets.orbit_set_gamma_has_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/OrbitSets.lean#L258-L260)
**theorem
Tau.Sets.orbit_set_gamma_has_one
(n : Denotation.TauIdx)
 :orbit_set_gamma n 1**


1 ∈ Set(γ_n) for all n: take e = 0, so (nthPrime n)^0 = 1.
