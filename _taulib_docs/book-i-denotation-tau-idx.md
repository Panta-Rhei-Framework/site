---
layout: taulib-doc
title: "TauLib.BookI.Denotation.TauIdx"
permalink: /verify/taulib/docs/book-i-denotation-tau-idx/
lane: verify
module_name: "TauLib.BookI.Denotation.TauIdx"
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

# TauLib.Denotation.TauIdx


τ-Idx: the alpha orbit IS the natural numbers. The swap operator σ
permutes seeds between orbits.

## Registry Cross-References


- [I.D07] τ-Idx — `TauIdx`, `toAlphaOrbit`

- [I.D09] Swap Operator — `sigma`, `sigma_involutive`


## Mathematical Content


The alpha orbit O_α = {⟨α, 1⟩, ⟨α, 2⟩, ⟨α, 3⟩, ...} is in canonical
bijection with ℕ⁺ = {1, 2, 3, ...} via n ↦ ⟨α, n⟩. We define TauIdx
as a transparent alias for Nat, emphasizing that the natural numbers
are *discovered* as the depth values of the alpha orbit — not imported.

**Convention**: Semantically, τ-Idx = ℕ⁺ (positive naturals). Lean uses
`TauIdx = Nat` for convenience; orbit-meaningful indices are ≥ 1.
The element ⟨α, 0⟩ = α is the **generator itself** (depth 0 = no ρ
applied), not an orbit element α_0. Zero only enters as an arithmetic
value when ring structures are built (Part VIII).

The swap operator σ_{s,t} exchanges the seeds s and t, providing
canonical bijections between orbit rays.

---

### `Tau.Denotation.TauIdx`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L39-L45)@[reducible, inline]

**abbrev
Tau.Denotation.TauIdx :Type**


[I.D07] τ-Idx: the natural number system discovered as the alpha orbit.
Using `abbrev` makes this definitionally equal to Nat.

Semantically, τ-Idx = ℕ⁺. Orbit indices start at 1:
α_1 = ⟨α, 1⟩, α_2 = ⟨α, 2⟩, etc. The Lean type is Nat
for convenience; orbit-meaningful theorems carry nonzero guards.
Equations
- Tau.Denotation.TauIdx = Nat
Instances For

---

### `Tau.Denotation.toAlphaOrbit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L47-L48)
**def
Tau.Denotation.toAlphaOrbit
(n : TauIdx)
 :Kernel.TauObj**


Canonical embedding: TauIdx → TauObj (into the alpha orbit).
Equations
- Tau.Denotation.toAlphaOrbit n = { seed := Tau.Kernel.Generator.alpha, depth := n }
Instances For

---

### `Tau.Denotation.fromAlphaOrbit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L50-L51)
**def
Tau.Denotation.fromAlphaOrbit
(x : Kernel.TauObj)
 :TauIdx**


Extraction: TauObj (alpha orbit) → TauIdx.
Equations
- Tau.Denotation.fromAlphaOrbit x = x.depth
Instances For

---

### `Tau.Denotation.toAlpha_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L53-L57)
**theorem
Tau.Denotation.toAlpha_injective
(n m : TauIdx)

(h : toAlphaOrbit n = toAlphaOrbit m)
 :n = m**


The embedding is injective.

---

### `Tau.Denotation.toAlpha_fromAlpha`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L59-L62)
**theorem
Tau.Denotation.toAlpha_fromAlpha
(n : TauIdx)
 :fromAlphaOrbit (toAlphaOrbit n) = n**


Round-trip: fromAlpha ∘ toAlpha = id.

---

### `Tau.Denotation.toAlpha_in_orbit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L64-L67)
**theorem
Tau.Denotation.toAlpha_in_orbit
(n : TauIdx)
 :Orbit.OrbitRay Kernel.Generator.alpha (toAlphaOrbit n)**


The embedding lands in the alpha orbit ray.

---

### `Tau.Denotation.toAlpha_rho`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L69-L72)
**theorem
Tau.Denotation.toAlpha_rho
(n : TauIdx)
 :toAlphaOrbit (n + 1) = Kernel.rho (toAlphaOrbit n)**


The embedding commutes with ρ: toAlpha(n+1) = ρ(toAlpha(n)).

---

### `Tau.Denotation.sigma`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L78-L83)
**def
Tau.Denotation.sigma
(s t : Kernel.Generator)

(x : Kernel.TauObj)
 :Kernel.TauObj**


[I.D09] The swap operator σ_{s,t}: exchanges seeds s and t,
leaving all other seeds unchanged. Preserves depth.
Equations
- Tau.Denotation.sigma s t x = if x.seed = s then { seed := t, depth := x.depth } else if x.seed = t then { seed := s, depth := x.depth } else x
Instances For

---

### `Tau.Denotation.sigma_involutive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L85-L89)
**theorem
Tau.Denotation.sigma_involutive
(s t : Kernel.Generator)

(x : Kernel.TauObj)
 :sigma s t (sigma s t x) = x**


σ is an involution: σ_{s,t}(σ_{s,t}(x)) = x.

---

### `Tau.Denotation.sigma_preserves_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L91-L95)
**theorem
Tau.Denotation.sigma_preserves_depth
(s t : Kernel.Generator)

(x : Kernel.TauObj)
 :(sigma s t x).depth = x.depth**


σ preserves depth.

---

### `Tau.Denotation.sigma_self`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L97-L101)
**theorem
Tau.Denotation.sigma_self
(s : Kernel.Generator)

(x : Kernel.TauObj)
 :sigma s s x = x**


σ with s = t is the identity.

---

### `Tau.Denotation.sigma_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/TauIdx.lean#L103-L107)
**theorem
Tau.Denotation.sigma_comm
(s t : Kernel.Generator)

(x : Kernel.TauObj)
 :sigma s t x = sigma t s x**


σ is symmetric in its arguments.
