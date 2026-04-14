---
layout: taulib-doc
title: "TauLib.BookI.Orbit.Countability"
permalink: /verify/taulib/docs/book-i-orbit-countability/
lane: verify
module_name: "TauLib.BookI.Orbit.Countability"
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

# TauLib.Orbit.Countability


Each orbit ray is countable (bijection with Nat), and Obj(τ) is countable.

## Registry Cross-References


- [I.P04] Orbit Countability — `orbit_countable`, `tauObj_countable`


## Mathematical Content


Each orbit ray O_g is in bijection with Nat via the map n ↦ ⟨g, n⟩.
The full universe Obj(τ) is countable: we construct an injection TauObj → Nat.

---

### `Tau.Orbit.orbitEnumerate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L26-L28)
**def
Tau.Orbit.orbitEnumerate
(g : Kernel.Generator)

(_hg : g ≠ Kernel.Generator.omega)

(n : Nat)
 :Kernel.TauObj**


Canonical enumeration of orbit ray O_g: n ↦ ⟨g, n⟩.
Equations
- Tau.Orbit.orbitEnumerate g _hg n = { seed := g, depth := n }
Instances For

---

### `Tau.Orbit.orbit_enumerate_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L30-L35)
**theorem
Tau.Orbit.orbit_enumerate_injective
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n m : Nat)

(h : orbitEnumerate g hg n = orbitEnumerate g hg m)
 :n = m**


[I.P04 part 1] Orbit enumeration is injective.

---

### `Tau.Orbit.orbit_enumerate_surjective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L37-L43)
**theorem
Tau.Orbit.orbit_enumerate_surjective
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(x : Kernel.TauObj)

(hx : OrbitRay g x)
 :∃ (n : Nat), orbitEnumerate g hg n = x**


[I.P04 part 2] Orbit enumeration hits every orbit ray element.

---

### `Tau.Orbit.orbit_enumerate_in_ray`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L45-L48)
**theorem
Tau.Orbit.orbit_enumerate_in_ray
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : Nat)
 :OrbitRay g (orbitEnumerate g hg n)**


Orbit enumeration produces elements in the orbit ray.

---

### `Tau.Orbit.tauObj_encode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L54-L57)
**def
Tau.Orbit.tauObj_encode
(x : Kernel.TauObj)
 :Nat**


Encode a TauObj as a natural number: 5 * depth + seed_index.
This gives a computable injection TauObj → Nat.
Equations
- Tau.Orbit.tauObj_encode x = 5 * x.depth + x.seed.toNat
Instances For

---

### `Tau.Orbit.tauObj_encode_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L59-L70)
**theorem
Tau.Orbit.tauObj_encode_injective
(x y : Kernel.TauObj)

(h : tauObj_encode x = tauObj_encode y)
 :x = y**


The encoding is injective: distinct TauObjs yield distinct codes.

---

### `Tau.Orbit.tauObj_countable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Orbit/Countability.lean#L72-L74)
**theorem
Tau.Orbit.tauObj_countable :∃ (f : Kernel.TauObj → Nat), Function.Injective f**


[I.P04] Obj(τ) is countable: there exists an injection TauObj → Nat.
