---
layout: taulib-doc
title: "TauLib.BookIII.Spectrum.InterfaceWidth"
permalink: /verify/taulib/docs/book-iii-spectrum-interface-width/
lane: verify
module_name: "TauLib.BookIII.Spectrum.InterfaceWidth"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Spectrum.InterfaceWidth


Interface width and τ-admissibility.

## Registry Cross-References


- [I.D71] Interface Width — `interface_width`

- [I.D72] τ-Admissibility — `TauAdmissible`

- [I.T33] Interface Width Principle — `width_principle`

- [I.P30] Earned Admissibility — `chi_plus_admissible`, `chi_minus_admissible`


## Mathematical Content


Interface width measures how many primorial stages a computation crosses.
For a tower-coherent StageFun f, the interface width at input n is the
smallest d₀ such that all deeper stages agree with d₀ after reduction.

A HolFun is τ-admissible if its interface width is uniformly bounded.
All earned HolFuns (χ₊, χ₋, id) are τ-admissible with width 1.

---

### `Tau.Spectrum.interface_width_at`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L33-L47)
**def
Tau.Spectrum.interface_width_at
(f : Holomorphy.StageFun)

(n : Denotation.TauIdx)
 :Denotation.TauIdx → Prop**


[I.D71] The interface width of a StageFun f at input n:
the smallest depth d₀ such that the output at stage d₀
determines all coarser stages via reduction.

For a tower-coherent function, this always holds at d₀ = k
for each individual k (by tower coherence). The interface
width captures the minimum depth at which the function
"stabilizes" — i.e., computing at deeper stages doesn't
change the visible output.

We define it as the depth at which the function's B-sector
output first equals reduce(n, d₀): the point where the
function acts as a simple reduction.
Equations
- Tau.Spectrum.interface_width_at f n d₀ = ∀ (k : Tau.Denotation.TauIdx), k ≤ d₀ → f.b_fun n k = Tau.Polarity.reduce (f.b_fun n d₀) k
Instances For

---

### `Tau.Spectrum.width_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L49-L53)
**def
Tau.Spectrum.width_check
(f : Holomorphy.StageFun)

(n d₀ k : Denotation.TauIdx)
 :Bool**


A concrete width check: does f stabilize at depth d₀ for input n
when tested against depth k?
Equations
- Tau.Spectrum.width_check f n d₀ k = if k > d₀ then true else f.b_fun n k == Tau.Polarity.reduce (f.b_fun n d₀) k
Instances For

---

### `Tau.Spectrum.TauAdmissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L59-L67)
**def
Tau.Spectrum.TauAdmissible
(f : Holomorphy.StageFun)
 :Prop**


[I.D72] A StageFun is τ-admissible if there exists a uniform
depth bound D such that for all inputs n, the function
stabilizes at depth D.

Equivalently: the function is completely determined by its
action on ℤ/M_D ℤ for some finite D.
Equations
- Tau.Spectrum.TauAdmissible f = ∃ (D : Tau.Denotation.TauIdx), ∀ (n k : Tau.Denotation.TauIdx), k ≤ D → Tau.Polarity.reduce (f.b_fun n D) k = f.b_fun n k
Instances For

---

### `Tau.Spectrum.TauAdmissibleFull`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L69-L73)
**def
Tau.Spectrum.TauAdmissibleFull
(f : Holomorphy.StageFun)
 :Prop**


τ-admissibility for both sectors.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.width_principle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L79-L89)
**theorem
Tau.Spectrum.width_principle
(f : Holomorphy.StageFun)

(hcoh : Holomorphy.TowerCoherent f)

(D n k : Denotation.TauIdx)
 :k ≤ D → Polarity.reduce (f.b_fun n D) k = f.b_fun n k**


[I.T33] Interface Width Principle: tower-coherent functions
are τ-admissible at EVERY depth — tower coherence itself
gives the stabilization property.

For any tower-coherent f and any choice of depth D:
reduce(f.b_fun(n, D), k) = f.b_fun(n, k) for all k ≤ D.

This is exactly the tower coherence condition (I.D46).

---

### `Tau.Spectrum.width_principle_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L91-L94)
**theorem
Tau.Spectrum.width_principle_c
(f : Holomorphy.StageFun)

(hcoh : Holomorphy.TowerCoherent f)

(D n k : Denotation.TauIdx)
 :k ≤ D → Polarity.reduce (f.c_fun n D) k = f.c_fun n k**


Width principle for C-sector.

---

### `Tau.Spectrum.coherent_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L96-L99)
**theorem
Tau.Spectrum.coherent_admissible
(f : Holomorphy.StageFun)

(hcoh : Holomorphy.TowerCoherent f)
 :TauAdmissible f**


Tower coherence implies τ-admissibility (at any depth D).

---

### `Tau.Spectrum.chi_plus_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L105-L108)
**theorem
Tau.Spectrum.chi_plus_admissible :TauAdmissible Holomorphy.chi_plus_stage**


[I.P30] χ₊ is τ-admissible: at any depth D, it stabilizes
because χ₊ is tower-coherent.

---

### `Tau.Spectrum.chi_minus_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L110-L112)
**theorem
Tau.Spectrum.chi_minus_admissible :TauAdmissible Holomorphy.chi_minus_stage**


χ₋ is τ-admissible.

---

### `Tau.Spectrum.id_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L114-L116)
**theorem
Tau.Spectrum.id_admissible :TauAdmissible Holomorphy.id_stage**


The identity is τ-admissible.

---

### `Tau.Spectrum.comp_chi_plus_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L118-L126)
**theorem
Tau.Spectrum.comp_chi_plus_admissible :TauAdmissible (Holomorphy.chi_plus_stage.comp Holomorphy.chi_plus_stage)**


Composition of χ₊ with itself is τ-admissible.

---

### `Tau.Spectrum.chi_plus_crt_complexity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L132-L136)
**theorem
Tau.Spectrum.chi_plus_crt_complexity
(n k : Denotation.TauIdx)
 :Holomorphy.chi_plus_stage.b_fun n k = Holomorphy.chi_plus_stage.b_fun (Polarity.reduce n k) k**


τ-admissible functions have finite CRT complexity:
χ₊ depends only on n mod M_k at stage k.

---

### `Tau.Spectrum.chi_minus_crt_complexity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L138-L141)
**theorem
Tau.Spectrum.chi_minus_crt_complexity
(n k : Denotation.TauIdx)
 :Holomorphy.chi_minus_stage.c_fun n k = Holomorphy.chi_minus_stage.c_fun (Polarity.reduce n k) k**


χ₋ C-sector depends only on n mod M_k.

---

### `Tau.Spectrum.id_crt_complexity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L143-L146)
**theorem
Tau.Spectrum.id_crt_complexity
(n k : Denotation.TauIdx)
 :Holomorphy.id_stage.b_fun n k = Holomorphy.id_stage.b_fun (Polarity.reduce n k) k**


The identity depends only on n mod M_k.
