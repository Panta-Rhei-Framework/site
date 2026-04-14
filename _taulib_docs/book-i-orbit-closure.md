---
layout: taulib-doc
title: "TauLib.BookI.Orbit.Closure"
permalink: /verify/taulib/docs/book-i-orbit-closure/
lane: verify
module_name: "TauLib.BookI.Orbit.Closure"
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

# TauLib.Orbit.Closure


The Ontic Closure Theorem: Obj(τ) = O_α ∪ O_π ∪ O_γ ∪ O_η ∪ Ω.

## Registry Cross-References


- [I.T01] Ontic Closure Theorem — `ontic_closure`


## Mathematical Content


The Ontic Closure Theorem is the central result of Part II.
It asserts that the universe of τ is:

- Exhaustive: every object is in some orbit ray or is omega

- Disjoint: the five components are pairwise disjoint

- Countable: the universe is countably infinite

- Sealed: no object exists outside these five components


In our Lean representation, property (4) is definitional:
`TauObj` is constructed from `Generator × Nat`, so it is
impossible to create objects outside the orbit structure.

---

### `Tau.Orbit.ontic_closure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L34-L43)
**theorem
Tau.Orbit.ontic_closure
(x : Kernel.TauObj)
 :(∃ (g : Kernel.Generator), g ≠ Kernel.Generator.omega ∧ OrbitRay g x) ∨ x.seed = Kernel.Generator.omega**


[I.T01] Ontic Closure: every TauObj is either in an orbit ray
or has seed omega.

---

### `Tau.Orbit.ontic_closure_five_way`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L45-L55)
**theorem
Tau.Orbit.ontic_closure_five_way
(x : Kernel.TauObj)
 :OrbitRay Kernel.Generator.alpha x ∨ OrbitRay Kernel.Generator.pi x ∨ OrbitRay Kernel.Generator.gamma x ∨ OrbitRay Kernel.Generator.eta x ∨ x.seed = Kernel.Generator.omega**


Ontic closure: five-way decomposition.

---

### `Tau.Orbit.orbit_omega_disjoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L61-L65)
**theorem
Tau.Orbit.orbit_omega_disjoint
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(x : Kernel.TauObj)
 :¬(OrbitRay g x ∧ OmegaFiber x)**


Orbit rays and the omega fiber are disjoint.

---

### `Tau.Orbit.universe_sealed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L71-L76)
**theorem
Tau.Orbit.universe_sealed
(x : Kernel.TauObj)
 :x.seed = Kernel.Generator.alpha ∨ x.seed = Kernel.Generator.pi ∨ x.seed = Kernel.Generator.gamma ∨ x.seed = Kernel.Generator.eta ∨ x.seed = Kernel.Generator.omega**


The universe is sealed: the seed of any TauObj is one of the 5 generators.
This is K6, restated at the orbit level.

---

### `Tau.Orbit.universe_generated`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L78-L82)
**theorem
Tau.Orbit.universe_generated
(x : Kernel.TauObj)

(hx : x.seed ≠ Kernel.Generator.omega)
 :∃ (g : Kernel.Generator), g ≠ Kernel.Generator.omega ∧ x = iter_rho x.depth (Kernel.TauObj.ofGen g)**


Every non-omega TauObj is reached by iterated ρ from a generator.

---

### `Tau.Orbit.omega_fiber_rho_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L88-L91)
**theorem
Tau.Orbit.omega_fiber_rho_fixed
(n : Nat)
 :Kernel.rho { seed := Kernel.Generator.omega, depth := n } = { seed := Kernel.Generator.omega, depth := n }**


All objects in the omega fiber are ρ-fixed.

---

### `Tau.Orbit.omega_obj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Closure.lean#L93-L94)
**def
Tau.Orbit.omega_obj :Kernel.TauObj**


The canonical omega representative.
Equations
- Tau.Orbit.omega_obj = { seed := Tau.Kernel.Generator.omega, depth := 0 }
Instances For
