---
layout: taulib-doc
title: "TauLib.BookI.Orbit.Generation"
permalink: /verify/taulib/docs/book-i-orbit-generation/
lane: verify
module_name: "TauLib.BookI.Orbit.Generation"
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

# TauLib.Orbit.Generation


Orbit rays, iterated ρ, and the generative act.

## Registry Cross-References


- [I.X01] The Generative Act — `generative_act`

- [I.D05] Orbit Rays — `OrbitRay`

- [I.P03] Pairwise Disjointness — `orbit_disjoint`


## Mathematical Content


The generative act applies ρ to each non-omega generator g,
producing the orbit ray O_g = {g, ρ(g), ρ²(g), ...}.
The four orbit rays are pairwise disjoint (different seeds),
and ω sits alone as a fixed point.

NOTE: We use predicates (TauObj → Prop) rather than Mathlib's `Set`,
since we import Mathlib for tactics only.

---

### `Tau.Orbit.iter_rho`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L33-L36)
**def
Tau.Orbit.iter_rho :Nat → Kernel.TauObj → Kernel.TauObj**


Iterated application of ρ: ρⁿ(x).
Equations
- Tau.Orbit.iter_rho 0 x✝ = x✝
- Tau.Orbit.iter_rho n.succ x✝ = Tau.Kernel.rho (Tau.Orbit.iter_rho n x✝)
Instances For

---

### `Tau.Orbit.iter_rho_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L38-L39)@[simp]

**theorem
Tau.Orbit.iter_rho_zero
(x : Kernel.TauObj)
 :iter_rho 0 x = x**


---

### `Tau.Orbit.iter_rho_succ`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L41-L43)@[simp]

**theorem
Tau.Orbit.iter_rho_succ
(n : Nat)

(x : Kernel.TauObj)
 :iter_rho (n + 1) x = Kernel.rho (iter_rho n x)**


---

### `Tau.Orbit.iter_rho_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L45-L54)
**theorem
Tau.Orbit.iter_rho_depth
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(d n : Nat)
 :iter_rho n { seed := g, depth := d } = { seed := g, depth := d + n }**


iter_rho on a non-omega object increments depth.

---

### `Tau.Orbit.iter_rho_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L56-L62)@[simp]

**theorem
Tau.Orbit.iter_rho_omega
(n d : Nat)
 :iter_rho n { seed := Kernel.Generator.omega, depth := d } = { seed := Kernel.Generator.omega, depth := d }**


iter_rho on omega is the identity.

---

### `Tau.Orbit.iter_rho_seed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L64-L67)
**theorem
Tau.Orbit.iter_rho_seed
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(d n : Nat)
 :(iter_rho n { seed := g, depth := d }).seed = g**


iter_rho preserves the seed for non-omega generators.

---

### `Tau.Orbit.iter_rho_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L69-L75)
**theorem
Tau.Orbit.iter_rho_add
(n m : Nat)

(x : Kernel.TauObj)
 :iter_rho (n + m) x = iter_rho n (iter_rho m x)**


iter_rho composes: ρⁿ⁺ᵐ(x) = ρⁿ(ρᵐ(x)).

---

### `Tau.Orbit.OrbitRay`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L81-L84)
**def
Tau.Orbit.OrbitRay
(g : Kernel.Generator)

(x : Kernel.TauObj)
 :Prop**


[I.D05] Orbit ray membership predicate: x ∈ O_g iff x has seed g
and g is not omega.
Equations
- Tau.Orbit.OrbitRay g x = (x.seed = g ∧ g ≠ Tau.Kernel.Generator.omega)
Instances For

---

### `Tau.Orbit.OmegaFiber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L86-L88)
**def
Tau.Orbit.OmegaFiber
(x : Kernel.TauObj)
 :Prop**


The omega fiber: all TauObj with seed omega.
Equations
- Tau.Orbit.OmegaFiber x = (x.seed = Tau.Kernel.Generator.omega)
Instances For

---

### `Tau.Orbit.orbit_ray_contains_gen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L90-L93)
**theorem
Tau.Orbit.orbit_ray_contains_gen
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)
 :OrbitRay g (Kernel.TauObj.ofGen g)**


Each non-omega generator belongs to its own orbit ray.

---

### `Tau.Orbit.orbit_ray_rho_closed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L95-L102)
**theorem
Tau.Orbit.orbit_ray_rho_closed
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(x : Kernel.TauObj)

(hx : OrbitRay g x)
 :OrbitRay g (Kernel.rho x)**


Orbit rays are closed under ρ.

---

### `Tau.Orbit.orbit_ray_characterize`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L104-L111)
**theorem
Tau.Orbit.orbit_ray_characterize
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(x : Kernel.TauObj)
 :OrbitRay g x ↔ ∃ (n : Nat), x = { seed := g, depth := n }**


Every element of an orbit ray is ⟨g, n⟩ for some n.

---

### `Tau.Orbit.orbit_disjoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L117-L122)
**theorem
Tau.Orbit.orbit_disjoint
(g h : Kernel.Generator)

(hgh : g ≠ h)

(x : Kernel.TauObj)
 :¬(OrbitRay g x ∧ OrbitRay h x)**


[I.P03] Orbit rays are pairwise disjoint: if g ≠ h, no object
belongs to both O_g and O_h.

---

### `Tau.Orbit.omega_not_in_orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L124-L129)
**theorem
Tau.Orbit.omega_not_in_orbit
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : Nat)
 :¬OrbitRay g { seed := Kernel.Generator.omega, depth := n }**


Omega is not in any orbit ray.

---

### `Tau.Orbit.orbit_ray_seed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L131-L133)
**theorem
Tau.Orbit.orbit_ray_seed
(g : Kernel.Generator)

(x : Kernel.TauObj)

(hx : OrbitRay g x)
 :x.seed = g**


Orbit ray elements have seed equal to the generator.

---

### `Tau.Orbit.generative_act`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Generation.lean#L139-L144)
**theorem
Tau.Orbit.generative_act
(x : Kernel.TauObj)

(hx : x.seed ≠ Kernel.Generator.omega)
 :∃ (g : Kernel.Generator), ∃ (n : Nat), g ≠ Kernel.Generator.omega ∧ iter_rho n (Kernel.TauObj.ofGen g) = x**


[I.X01] The generative act: every non-omega TauObj is reachable by
iterated ρ from a generator.
