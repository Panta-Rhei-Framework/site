---
layout: taulib-doc
title: "TauLib.BookI.Kernel.Axioms"
permalink: /verify/taulib/docs/book-i-kernel-axioms/
lane: verify
module_name: "TauLib.BookI.Kernel.Axioms"
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

# TauLib.Kernel.Axioms


The six structural axioms K1–K6 of Category τ.

The zeroth axiom K0 (Universe Postulate) is implicit in Lean's type system:
the declarations `Generator : Type` and `TauObj : Type` postulate the
existence of the universe of discourse. See `TauLib.Kernel.Signature` for
the K0 documentation.

## Registry Cross-References


- [I.K1] Strict Order — `K1_strict_order`

- [I.K2] Omega Fixed Point — `K2_omega_fixed`

- [I.K3] Orbit-Seeded Generation — `K3_orbit_seeded`

- [I.K4] No-Jump / Cover — `K4_no_jump`

- [I.K5] Beacon Non-Successor — `K5_beacon_non_succ`

- [I.K6] Object Closure — `K6_object_closure`


## Mathematical Content


The 2nd Edition compresses the 1st Edition's 9 axioms into 6 structural axioms
(K1–K6), plus the zeroth axiom K0 (Universe Postulate).
K1–K6 are purely about generation and closure. All structural consequences
are deferred to Parts II–III.

These axioms operate on the `TauObj` type, which represents all objects of τ
(generators + orbit elements produced by ρ).

---

### `Tau.Kernel.TauObj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L37-L54)
**structure
Tau.Kernel.TauObj :Type**


Objects of Category τ: either a generator or an orbit element ρⁿ(g).
This is the type AFTER the generative act (Part II).

An object is represented by its seed generator and the number of ρ-applications.
The generator ω with n=0 is the beacon; ω with n>0 collapses to ω (K2).

**Depth convention**: depth 0 = the generator itself (no ρ applied).
Orbit elements start at depth 1: α_1 = ⟨α, 1⟩ = ρ(α).
The generator α = ⟨α, 0⟩ is the seed, NOT an orbit element "α_0".

NOTE: This representation makes K6 (object closure) definitional rather than axiomatic:
every TauObj is by construction in some orbit ray or is ω.

- seed : Generator
The seed generator of this object's orbit ray

- depth : Nat
Number of ρ-applications (0 = the generator itself, ≥1 = orbit element)

Instances For

---

### `Tau.Kernel.instDecidableEqTauObj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L54-L54)
**instance
Tau.Kernel.instDecidableEqTauObj :DecidableEq TauObj**

Equations
- Tau.Kernel.instDecidableEqTauObj = Tau.Kernel.instDecidableEqTauObj.decEq

---

### `Tau.Kernel.instDecidableEqTauObj.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L54-L54)
**def
Tau.Kernel.instDecidableEqTauObj.decEq
(x✝ x✝¹ : TauObj)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.Kernel.instDecidableEqTauObj.decEq { seed := a, depth := a_1 } { seed := b, depth := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.Kernel.instReprTauObj.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L54-L54)
**def
Tau.Kernel.instReprTauObj.repr :TauObj → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Kernel.instReprTauObj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L54-L54)
**instance
Tau.Kernel.instReprTauObj :Repr TauObj**

Equations
- Tau.Kernel.instReprTauObj = { reprPrec := Tau.Kernel.instReprTauObj.repr }

---

### `Tau.Kernel.TauObj.ofGen`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L56-L57)
**def
Tau.Kernel.TauObj.ofGen
(g : Generator)
 :TauObj**


Construct a TauObj from a generator (depth 0).
Equations
- Tau.Kernel.TauObj.ofGen g = { seed := g, depth := 0 }
Instances For

---

### `Tau.Kernel.rho`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L59-L64)
**def
Tau.Kernel.rho
(x : TauObj)
 :TauObj**


[I.D02] The progression operator ρ: sole primitive iterator.
ρ(ω) = ω (K2 omega fixed point); otherwise increments depth.
Equations
- Tau.Kernel.rho x = match x.seed with
 | Tau.Kernel.Generator.omega => x
 | x_1 => { seed := x.seed, depth := x.depth + 1 }
Instances For

---

### `Tau.Kernel.K1_strict_order`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L71-L80)
**theorem
Tau.Kernel.K1_strict_order :Generator.alpha.toNat < Generator.pi.toNat ∧ Generator.pi.toNat < Generator.gamma.toNat ∧ Generator.gamma.toNat < Generator.eta.toNat ∧ Generator.eta.toNat < Generator.omega.toNat**


[I.K1] **Strict Order**: α < π < γ < η < ω is a strict total order
on the 5 generators.

In our representation, this holds definitionally via `Generator.toNat`.

---

### `Tau.Kernel.K2_omega_fixed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L82-L87)
**theorem
Tau.Kernel.K2_omega_fixed
(n : Nat)
 :rho { seed := Generator.omega, depth := n } = { seed := Generator.omega, depth := n }**


[I.K2] **Omega Fixed Point**: ρ(ω) = ω; ω absorbs all operations.

This holds definitionally from our `rho` definition.

---

### `Tau.Kernel.inOrbitRay`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L89-L94)
**def
Tau.Kernel.inOrbitRay
(g : Generator)

(x : TauObj)
 :Prop**


[I.K3] **Orbit-Seeded Generation**: Each non-omega generator g seeds
its orbit ray O_g = {ρⁿ(g) : n ≥ 0}.

We define the orbit ray predicate.
Equations
- Tau.Kernel.inOrbitRay g x = (x.seed = g ∧ g ≠ Tau.Kernel.Generator.omega)
Instances For

---

### `Tau.Kernel.K3_orbit_seeded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L96-L99)
**theorem
Tau.Kernel.K3_orbit_seeded
(g : Generator)

(h : g ≠ Generator.omega)
 :inOrbitRay g (TauObj.ofGen g)**


[I.K3] Every non-omega generator seeds an orbit ray containing itself.

---

### `Tau.Kernel.K4_no_jump`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L101-L105)
**theorem
Tau.Kernel.K4_no_jump
(g : Generator)

(hg : g ≠ Generator.omega)

(n : Nat)
 :rho { seed := g, depth := n } = { seed := g, depth := n + 1 }**


[I.K4] **No-Jump / Cover**: ρ acts as a successor within each orbit
(no skipping). The cover relation is immediate: ρⁿ(g) covers ρⁿ⁻¹(g).

---

### `Tau.Kernel.K5_beacon_non_succ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L107-L111)
**theorem
Tau.Kernel.K5_beacon_non_succ
(g : Generator)

(hg : g ≠ Generator.omega)

(n : Nat)
 :(rho { seed := g, depth := n }).seed = g**


[I.K5] **Beacon Non-Successor**: ω is NOT in the image of ρ restricted
to any orbit ray. No finite iteration of ρ on a non-omega generator reaches ω.

---

### `Tau.Kernel.K5_omega_unreachable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L113-L121)
**theorem
Tau.Kernel.K5_omega_unreachable
(g : Generator)

(hg : g ≠ Generator.omega)

(n : Nat)
 :{ seed := g, depth := n } ≠ { seed := Generator.omega, depth := 0 }**


[I.K5 corollary] ω is unreachable: no orbit element has seed = omega
(except ω itself with depth 0).

---

### `Tau.Kernel.K6_object_closure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L123-L135)
**theorem
Tau.Kernel.K6_object_closure
(x : TauObj)
 :x.seed = Generator.alpha ∨ x.seed = Generator.pi ∨ x.seed = Generator.gamma ∨ x.seed = Generator.eta ∨ x.seed = Generator.omega**


[I.K6] **Object Closure**: Obj(τ) = {ω} ∪ O_α ∪ O_π ∪ O_γ ∪ O_η.
No other objects exist.

In our representation, this is definitional: every `TauObj` is constructed
from a `Generator` seed, and `Generator` has exactly 5 constructors.

---

### `Tau.Kernel.gen_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L141-L146)
**theorem
Tau.Kernel.gen_distinct
(a b : Generator)
 :a ≠ b → a.toNat ≠ b.toNat**


[I.P01] Generator distinctness: all five generators are pairwise distinct.

---

### `Tau.Kernel.rho_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Kernel/Axioms.lean#L148-L156)
**theorem
Tau.Kernel.rho_injective
(g : Generator)

(hg : g ≠ Generator.omega)

(n m : Nat)
 :rho { seed := g, depth := n } = rho { seed := g, depth := m } → n = m**


[I.P02] ρ is injective on each orbit ray.
