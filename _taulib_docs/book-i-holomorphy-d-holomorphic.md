---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.DHolomorphic"
permalink: /verify/taulib/docs/book-i-holomorphy-d-holomorphic/
lane: verify
module_name: "TauLib.BookI.Holomorphy.DHolomorphic"
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

# TauLib.Holomorphy.DHolomorphic


D-holomorphy on the split-complex algebra H_τ = Z[j], j² = +1.

## Registry Cross-References


- [I.D42] D-Differentiability — `SectorFun`, `is_sector_independent`

- [I.D43] Split-CR Equations — `split_cr_form`

- [I.P22] Sector Independence — `sector_independence`, `sector_fun_of_sector_independent`


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, sector decomposition

- chunk_0310_M002679: Bipolar partition, D-holomorphic structure


## Mathematical Content


A function f: H_τ → H_τ is D-holomorphic if in sector coordinates (u,v) = (a+b, a-b),
f decomposes as f(u,v) = (g(u), h(v)) — each sector component depends on only one
sector variable. This is the split-complex analog of the Cauchy-Riemann equations.

The split-CR equations are: ∂U/∂a = ∂V/∂b, ∂U/∂b = ∂V/∂a (note the + sign,
contrasting with the classical − sign). In sector coordinates: ∂F₊/∂v = 0, ∂F₋/∂u = 0.

D-holomorphic functions are too flexible: any pair (g, h) works, giving no rigidity.
Zero divisors e₊ · e₋ = 0 are the root cause. τ-holomorphy (Chapter 47) adds tower
coherence to rescue rigidity.

---

### `Tau.Holomorphy.SectorFun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L42-L49)
**structure
Tau.Holomorphy.SectorFun :Type**


[I.D42] A sector function is a pair of Z → Z functions (g, h) representing
f(u,v) = (g(u), h(v)) in sector coordinates. This is the canonical form
of a D-holomorphic function.

- g : ℤ → ℤ
B-sector component: depends only on u = a + b.

- h : ℤ → ℤ
C-sector component: depends only on v = a - b.

Instances For

---

### `Tau.Holomorphy.SectorFun.apply`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L51-L53)
**def
Tau.Holomorphy.SectorFun.apply
(sf : SectorFun)

(s : Polarity.SectorPair)
 :Polarity.SectorPair**


Apply a sector function to a SectorPair.
Equations
- sf.apply s = { b_sector := sf.g s.b_sector, c_sector := sf.h s.c_sector }
Instances For

---

### `Tau.Holomorphy.SectorFun.apply_sc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L55-L57)
**def
Tau.Holomorphy.SectorFun.apply_sc
(sf : SectorFun)

(z : Polarity.SplitComplex)
 :Polarity.SplitComplex**


Apply a sector function to a SplitComplex (via sector coordinates).
Equations
- sf.apply_sc z = Tau.Boundary.from_sectors (sf.apply (Tau.Polarity.to_sectors z))
Instances For

---

### `Tau.Holomorphy.is_sector_independent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L63-L69)
**def
Tau.Holomorphy.is_sector_independent
(f : Polarity.SectorPair → Polarity.SectorPair)
 :Prop**


[I.P22] A function f: SectorPair → SectorPair is sector-independent if
its B-output depends only on the B-input and its C-output depends only
on the C-input. This is the content of the split-CR equations.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Holomorphy.sector_fun_independent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L71-L78)
**theorem
Tau.Holomorphy.sector_fun_independent
(sf : SectorFun)
 :is_sector_independent sf.apply**


[I.P22] Every SectorFun is sector-independent by construction.

---

### `Tau.Holomorphy.has_split_cr_form`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L84-L88)
**def
Tau.Holomorphy.has_split_cr_form
(f : Polarity.SplitComplex → Polarity.SplitComplex)
 :Prop**


[I.D43] A function f: SplitComplex → SplitComplex satisfies the split-CR
form if it factors through sector coordinates as a SectorFun.
That is, there exist g, h such that f = from_sectors ∘ (g, h) ∘ to_sectors.
Equations
- Tau.Holomorphy.has_split_cr_form f = ∃ (sf : Tau.Holomorphy.SectorFun), ∀ (z : Tau.Polarity.SplitComplex), f z = sf.apply_sc z
Instances For

---

### `Tau.Holomorphy.SectorFun.comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L94-L96)
**def
Tau.Holomorphy.SectorFun.comp
(sf₁ sf₂ : SectorFun)
 :SectorFun**


Composition of sector functions: component-wise composition.
Equations
- sf₁.comp sf₂ = { g := sf₁.g ∘ sf₂.g, h := sf₁.h ∘ sf₂.h }
Instances For

---

### `Tau.Holomorphy.sector_comp_apply`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L98-L101)
**theorem
Tau.Holomorphy.sector_comp_apply
(sf₁ sf₂ : SectorFun)

(s : Polarity.SectorPair)
 :(sf₁.comp sf₂).apply s = sf₁.apply (sf₂.apply s)**


Composition of sector functions gives sectorial composition in sector coordinates.

---

### `Tau.Holomorphy.sector_comp_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L103-L105)
**theorem
Tau.Holomorphy.sector_comp_assoc
(sf₁ sf₂ sf₃ : SectorFun)
 :(sf₁.comp sf₂).comp sf₃ = sf₁.comp (sf₂.comp sf₃)**


Composition of sector functions is associative.

---

### `Tau.Holomorphy.SectorFun.id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L107-L108)
**def
Tau.Holomorphy.SectorFun.id :SectorFun**


The identity sector function.
Equations
- Tau.Holomorphy.SectorFun.id = { g := fun (x : ℤ) => x, h := fun (x : ℤ) => x }
Instances For

---

### `Tau.Holomorphy.sector_id_comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L110-L113)
**theorem
Tau.Holomorphy.sector_id_comp
(sf : SectorFun)
 :SectorFun.id.comp sf = sf**


Identity is a left unit for composition.

---

### `Tau.Holomorphy.sector_comp_id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L115-L118)
**theorem
Tau.Holomorphy.sector_comp_id
(sf : SectorFun)
 :sf.comp SectorFun.id = sf**


Identity is a right unit for composition.

---

### `Tau.Holomorphy.zero_div_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L124-L128)
**theorem
Tau.Holomorphy.zero_div_sectors :Polarity.e_plus_sector.mul Polarity.e_minus_sector = { b_sector := 0, c_sector := 0 }**


e₊ · e₋ = 0: the zero divisor product in sector coordinates.
This is the fundamental pathology of D-holomorphy:
functions can be zero on one sector and arbitrary on the other.

---

### `Tau.Holomorphy.zero_div_sc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L130-L132)
**theorem
Tau.Holomorphy.zero_div_sc :{ re := 1, im := 1 }.mul { re := 1, im := -1 } = Polarity.SplitComplex.zero**


Concrete witness: (1+j)(1-j) = 0 in split-complex coordinates.

---

### `Tau.Holomorphy.b_only_fun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L138-L140)
**def
Tau.Holomorphy.b_only_fun
(g : ℤ → ℤ)
 :SectorFun**


A sector function that is zero on the C-sector: f(u,v) = (g(u), 0).
This is D-holomorphic but has no C-sector information.
Equations
- Tau.Holomorphy.b_only_fun g = { g := g, h := fun (x : ℤ) => 0 }
Instances For

---

### `Tau.Holomorphy.c_only_fun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L142-L144)
**def
Tau.Holomorphy.c_only_fun
(h : ℤ → ℤ)
 :SectorFun**


A sector function that is zero on the B-sector: f(u,v) = (0, h(v)).
This is D-holomorphic but has no B-sector information.
Equations
- Tau.Holomorphy.c_only_fun h = { g := fun (x : ℤ) => 0, h := h }
Instances For

---

### `Tau.Holomorphy.b_only_comp_c_only`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L146-L150)
**theorem
Tau.Holomorphy.b_only_comp_c_only
(g h : ℤ → ℤ)

(s : Polarity.SectorPair)
 :(b_only_fun g).apply ((c_only_fun h).apply s) = { b_sector := g 0, c_sector := 0 }**


B-only and C-only sector functions compose to zero
(the functional analog of e₊ · e₋ = 0).

---

### `Tau.Holomorphy.chi_plus_sf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L156-L157)
**def
Tau.Holomorphy.chi_plus_sf :SectorFun**


χ₊ as a sector function: projects to B-sector.
Equations
- Tau.Holomorphy.chi_plus_sf = { g := fun (u : ℤ) => u, h := fun (x : ℤ) => 0 }
Instances For

---

### `Tau.Holomorphy.chi_minus_sf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L159-L160)
**def
Tau.Holomorphy.chi_minus_sf :SectorFun**


χ₋ as a sector function: projects to C-sector.
Equations
- Tau.Holomorphy.chi_minus_sf = { g := fun (x : ℤ) => 0, h := fun (v : ℤ) => v }
Instances For

---

### `Tau.Holomorphy.chi_plus_sf_apply`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L162-L165)
**theorem
Tau.Holomorphy.chi_plus_sf_apply
(s : Polarity.SectorPair)
 :chi_plus_sf.apply s = { b_sector := s.b_sector, c_sector := 0 }**


χ₊ applied to sector coordinates gives the B-sector projection.

---

### `Tau.Holomorphy.chi_minus_sf_apply`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L167-L170)
**theorem
Tau.Holomorphy.chi_minus_sf_apply
(s : Polarity.SectorPair)
 :chi_minus_sf.apply s = { b_sector := 0, c_sector := s.c_sector }**


χ₋ applied to sector coordinates gives the C-sector projection.

---

### `Tau.Holomorphy.chi_sector_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L172-L175)
**theorem
Tau.Holomorphy.chi_sector_complete
(s : Polarity.SectorPair)
 :(chi_plus_sf.apply s).add (chi_minus_sf.apply s) = s**


χ₊ and χ₋ sum to the identity in sector coordinates.

---

### `Tau.Holomorphy.chi_sector_orthogonal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/DHolomorphic.lean#L177-L180)
**theorem
Tau.Holomorphy.chi_sector_orthogonal
(s : Polarity.SectorPair)
 :(chi_plus_sf.apply s).mul (chi_minus_sf.apply s) = { b_sector := 0, c_sector := 0 }**


χ₊ and χ₋ are orthogonal: their sector product is zero.
