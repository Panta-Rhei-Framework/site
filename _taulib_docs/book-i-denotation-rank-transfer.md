---
layout: taulib-doc
title: "TauLib.BookI.Denotation.RankTransfer"
permalink: /verify/taulib/docs/book-i-denotation-rank-transfer/
lane: verify
module_name: "TauLib.BookI.Denotation.RankTransfer"
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

# TauLib.Denotation.RankTransfer


Rank transfer maps: canonical bijections TauIdx ↔ OrbitRay g.

## Registry Cross-References


- [I.D08] Rank Transfer — `RT`, `RT_inv`


## Mathematical Content


Since every orbit ray O_g has the form {⟨g, 0⟩, ⟨g, 1⟩, ⟨g, 2⟩, ...},
there is a canonical bijection with TauIdx (= Nat) via depth.
The rank transfer RT_g : TauIdx → O_g maps n ↦ ⟨g, n⟩.

This gives each orbit ray the same arithmetic structure as the alpha orbit:
any operation on TauIdx can be "transferred" to any orbit ray.

---

### `Tau.Denotation.RT`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L30-L31)
**def
Tau.Denotation.RT
(g : Kernel.Generator)

(n : TauIdx)
 :Kernel.TauObj**


[I.D08] Rank transfer: TauIdx → orbit ray O_g, mapping n ↦ ⟨g, n⟩.
Equations
- Tau.Denotation.RT g n = { seed := g, depth := n }
Instances For

---

### `Tau.Denotation.RT_inv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L33-L34)
**def
Tau.Denotation.RT_inv
(x : Kernel.TauObj)
 :TauIdx**


Rank transfer inverse: orbit ray element → TauIdx (extracts depth).
Equations
- Tau.Denotation.RT_inv x = x.depth
Instances For

---

### `Tau.Denotation.RT_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L36-L40)
**theorem
Tau.Denotation.RT_injective
(g : Kernel.Generator)

(n m : TauIdx)

(h : RT g n = RT g m)
 :n = m**


RT is injective.

---

### `Tau.Denotation.RT_surjective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L42-L46)
**theorem
Tau.Denotation.RT_surjective
(g : Kernel.Generator)

(_hg : g ≠ Kernel.Generator.omega)

(x : Kernel.TauObj)

(hx : Orbit.OrbitRay g x)
 :∃ (n : TauIdx), RT g n = x**


RT hits every orbit ray element.

---

### `Tau.Denotation.RT_inv_left`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L48-L51)
**theorem
Tau.Denotation.RT_inv_left
(g : Kernel.Generator)

(n : TauIdx)
 :RT_inv (RT g n) = n**


Round-trip: RT_inv ∘ RT = id.

---

### `Tau.Denotation.RT_inv_right`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L53-L58)
**theorem
Tau.Denotation.RT_inv_right
(g : Kernel.Generator)

(x : Kernel.TauObj)

(h : x.seed = g)
 :RT g (RT_inv x) = x**


Round-trip: RT ∘ RT_inv = id (on orbit ray elements).

---

### `Tau.Denotation.RT_rho_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L60-L64)
**theorem
Tau.Denotation.RT_rho_comm
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : TauIdx)
 :RT g (n + 1) = Kernel.rho (RT g n)**


RT commutes with ρ: RT_g(n+1) = ρ(RT_g(n)) for g ≠ ω.

---

### `Tau.Denotation.RT_in_orbit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L66-L69)
**theorem
Tau.Denotation.RT_in_orbit
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : TauIdx)
 :Orbit.OrbitRay g (RT g n)**


RT lands in the orbit ray.

---

### `Tau.Denotation.RT_alpha_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L71-L74)
**theorem
Tau.Denotation.RT_alpha_eq
(n : TauIdx)
 :RT Kernel.Generator.alpha n = toAlphaOrbit n**


RT for alpha is the same as toAlphaOrbit.

---

### `Tau.Denotation.RT_sigma`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/RankTransfer.lean#L76-L79)
**theorem
Tau.Denotation.RT_sigma
(g h : Kernel.Generator)

(_hg : g ≠ h)

(n : TauIdx)
 :sigma g h (RT g n) = RT h n**


Rank transfer is natural: σ_{g,h} ∘ RT_g = RT_h.
