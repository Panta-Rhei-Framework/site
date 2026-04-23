---
layout: taulib-doc
title: "TauLib.BookI.Polarity.OmegaGerms"
permalink: /verify/taulib/docs/book-i-polarity-omega-germs/
lane: verify
module_name: "TauLib.BookI.Polarity.OmegaGerms"
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

# TauLib.Polarity.OmegaGerms


Omega-tails (compatible towers) and the divergence ultrametric.

## Registry Cross-References


- [I.D25] Omega-Tail — `OmegaTail`, `nat_to_tail`, `divergence_depth`


## Ground Truth Sources


- chunk_0155_M001710: Omega-tails, divergence ultrametric, coupling invariant


## Mathematical Content


An omega-tail is a compatible tower (x_k)_{k ≥ 1} where x_k ∈ Z/M_kZ
and the reduction maps are respected: x_ℓ mod M_k = x_k for k ≤ ℓ.

Every natural number n gives rise to an omega-tail via n ↦ (n mod M_k)_k.
The divergence depth d(t, t') = min{k : x_k ≠ x_k'} defines a canonical
ultrametric on the space of omega-tails.

---

### `Tau.Polarity.OmegaTail`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L33-L40)
**structure
Tau.Polarity.OmegaTail :Type**


[I.D25] Truncated omega-tail up to depth d: components x_k for k = 1..d.
Represented as a list of TauIdx values, where the k-th entry is x_k ∈ Z/M_kZ.
Compatibility: x_k = x_ℓ mod M_k for k ≤ ℓ.

- depth : Denotation.TauIdx
- components : List Denotation.TauIdx
- depth_eq : self.components.length = self.depth
Instances For

---

### `Tau.Polarity.instReprOmegaTail`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L40-L40)
**instance
Tau.Polarity.instReprOmegaTail :Repr OmegaTail**

Equations
- Tau.Polarity.instReprOmegaTail = { reprPrec := Tau.Polarity.instReprOmegaTail.repr }

---

### `Tau.Polarity.instReprOmegaTail.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L40-L40)
**def
Tau.Polarity.instReprOmegaTail.repr :OmegaTail → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.nat_to_tail_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L42-L47)@[irreducible]

**def
Tau.Polarity.nat_to_tail_go
(n k d fuel : Nat)

(acc : List Denotation.TauIdx)
 :List Denotation.TauIdx**


Build omega-tail components for n at depths 1..d.
Equations
- Tau.Polarity.nat_to_tail_go n k d fuel acc = if fuel = 0 then acc
 else if k > d then acc else Tau.Polarity.nat_to_tail_go n (k + 1) d (fuel - 1) (acc ++ [Tau.Polarity.reduce n k])
Instances For

---

### `Tau.Polarity.nat_to_tail_components`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L49-L51)
**def
Tau.Polarity.nat_to_tail_components
(n d : Denotation.TauIdx)
 :List Denotation.TauIdx**


Canonical embedding: n ↦ (n mod M_1, n mod M_2, ..., n mod M_d).
Equations
- Tau.Polarity.nat_to_tail_components n d = Tau.Polarity.nat_to_tail_go n 1 d d []
Instances For

---

### `Tau.Polarity.nat_to_tail`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L53-L56)
**def
Tau.Polarity.nat_to_tail
(n d : Denotation.TauIdx)
 :OmegaTail**


The canonical omega-tail of a natural number n, truncated at depth d.
Equations
- Tau.Polarity.nat_to_tail n d = { depth := (Tau.Polarity.nat_to_tail_components n d).length, components := Tau.Polarity.nat_to_tail_components n d,
 depth_eq := ⋯ }
Instances For

---

### `Tau.Polarity.OmegaTail.get`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L62-L64)
**def
Tau.Polarity.OmegaTail.get
(t : OmegaTail)

(i : Nat)
 :Denotation.TauIdx**


Safe component access with default 0.
Equations
- t.get i = t.components.getD i 0
Instances For

---

### `Tau.Polarity.compat_inner`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L70-L78)@[irreducible]

**def
Tau.Polarity.compat_inner
(comps : List Denotation.TauIdx)

(k l fuel : Nat)
 :Bool**


Check compatibility at indices k ≤ l: component[l-1] mod M_k = component[k-1].
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.compat_outer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L80-L85)@[irreducible]

**def
Tau.Polarity.compat_outer
(comps : List Denotation.TauIdx)

(d k fuel : Nat)
 :Bool**


Check full compatibility of an omega-tail.
Equations
- Tau.Polarity.compat_outer comps d k fuel = if fuel = 0 then true
 else if k > d then true
 else Tau.Polarity.compat_inner comps k d d && Tau.Polarity.compat_outer comps d (k + 1) (fuel - 1)
Instances For

---

### `Tau.Polarity.compat_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L87-L88)
**def
Tau.Polarity.compat_check
(t : OmegaTail)
 :Bool**

Equations
- Tau.Polarity.compat_check t = Tau.Polarity.compat_outer t.components t.depth 1 t.depth
Instances For

---

### `Tau.Polarity.Compatible`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L94-L98)
**def
Tau.Polarity.Compatible
(t : OmegaTail)
 :Prop**


Prop-level compatibility: for all k ≤ l within depth,
the reduction map respects tower components.
Equations
- Tau.Polarity.Compatible t = ∀ (k l : Tau.Denotation.TauIdx),
 1 ≤ k → k ≤ l → l ≤ t.depth → t.components.getD (l - 1) 0 % Tau.Polarity.primorial k = t.components.getD (k - 1) 0
Instances For

---

### `Tau.Polarity.mk_omega_tail`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L115-L117)
**def
Tau.Polarity.mk_omega_tail
(n d : Denotation.TauIdx)
 :OmegaTail**


Omega-tail built from clean spec (for formal reasoning).
Equations
- Tau.Polarity.mk_omega_tail n d = { depth := d, components := Tau.Polarity.tail_list✝ n d, depth_eq := ⋯ }
Instances For

---

### `Tau.Polarity.mk_omega_tail_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L142-L154)
**theorem
Tau.Polarity.mk_omega_tail_compat
(n d : Denotation.TauIdx)
 :Compatible (mk_omega_tail n d)**


The clean-spec omega-tail is compatible: reduction maps compose.
This is the Prop-level soundness theorem for the canonical embedding.

---

### `Tau.Polarity.mk_omega_tail_getD`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L156-L159)
**theorem
Tau.Polarity.mk_omega_tail_getD
(n d i : Nat)

(hi : i < d)
 :(mk_omega_tail n d).components.getD i 0 = reduce n (i + 1)**


Component accessor for mk_omega_tail: the i-th component is reduce n (i+1).

---

### `Tau.Polarity.equiv_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L171-L179)@[irreducible]

**def
Tau.Polarity.equiv_go
(c1 c2 : List Denotation.TauIdx)

(d i fuel : Nat)
 :Bool**


Pointwise equality check of two component lists up to depth d.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.tail_equiv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L181-L184)
**def
Tau.Polarity.tail_equiv
(t1 t2 : OmegaTail)
 :Bool**


Tail equivalence: two omega-tails agree on all shared components.
Equations
- Tau.Polarity.tail_equiv t1 t2 = Tau.Polarity.equiv_go t1.components t2.components (min t1.depth t2.depth) 0 (min t1.depth t2.depth)
Instances For

---

### `Tau.Polarity.diverge_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L190-L199)@[irreducible]

**def
Tau.Polarity.diverge_go
(c1 c2 : List Denotation.TauIdx)

(d i fuel : Nat)
 :Denotation.TauIdx**


Find first disagreement index between two component lists.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.divergence_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L201-L205)
**def
Tau.Polarity.divergence_depth
(t1 t2 : OmegaTail)
 :Denotation.TauIdx**


Divergence depth: first index k where the tails disagree.
Returns 0 if tails are equivalent (up to shared depth).
Equations
- Tau.Polarity.divergence_depth t1 t2 = Tau.Polarity.diverge_go t1.components t2.components (min t1.depth t2.depth) 0 (min t1.depth t2.depth)
Instances For

---

### `Tau.Polarity.ultra_dist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L207-L208)
**def
Tau.Polarity.ultra_dist
(t1 t2 : OmegaTail)
 :Denotation.TauIdx**


Ultrametric distance: 0 if equivalent, k₀ = first disagreement index otherwise.
Equations
- Tau.Polarity.ultra_dist t1 t2 = Tau.Polarity.divergence_depth t1 t2
Instances For

---

### `Tau.Polarity.ultra_symmetric`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L232-L238)
**theorem
Tau.Polarity.ultra_symmetric
(t1 t2 : OmegaTail)
 :ultra_dist t1 t2 = ultra_dist t2 t1**


Ultrametric symmetry: d(t1,t2) = d(t2,t1).

---

### `Tau.Polarity.agree_at_trans`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L240-L243)
**theorem
Tau.Polarity.agree_at_trans
(c1 c2 c3 : List Denotation.TauIdx)

(i : Nat)

(h12 : c1.getD i 0 = c2.getD i 0)

(h23 : c2.getD i 0 = c3.getD i 0)
 :c1.getD i 0 = c3.getD i 0**


Agreement transitivity: if c1[i] = c2[i] and c2[i] = c3[i], then c1[i] = c3[i].

---

### `Tau.Polarity.ultra_symmetry_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L245-L247)
**def
Tau.Polarity.ultra_symmetry_check
(t1 t2 : OmegaTail)
 :Bool**


Check symmetry: d(t1, t2) = d(t2, t1).
Equations
- Tau.Polarity.ultra_symmetry_check t1 t2 = (Tau.Polarity.ultra_dist t1 t2 == Tau.Polarity.ultra_dist t2 t1)
Instances For

---

### `Tau.Polarity.ultra_triangle_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L249-L259)
**def
Tau.Polarity.ultra_triangle_check
(t1 t2 t3 : OmegaTail)
 :Bool**


Check ultrametric strong triangle inequality (divergence-depth convention).
In the raw divergence-depth convention (0 = identical, k = first disagreement
at position k-1), the standard ultrametric triangle d(x,z) ≤ max(d(x,y), d(y,z))
translates to: the first disagreement of (t1,t3) is at least as deep as
the minimum of the first disagreements of the other two pairs.
This holds for all non-identical pairs; when ultra_dist = 0 (identical),
the pair is transparent (d(t1,t3) = d(t2,t3) when t1 ≡ t2).
Equations
- Tau.Polarity.ultra_triangle_check t1 t2 t3 = (Tau.Polarity.ultra_dist t1 t3 == 0 || decide (Tau.Polarity.ultra_dist t1 t3 ≥ min (Tau.Polarity.ultra_dist t1 t2) (Tau.Polarity.ultra_dist t2 t3)))
Instances For

---

### `Tau.Polarity.ultra_triangle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L340-L349)
**theorem
Tau.Polarity.ultra_triangle
(t1 t2 t3 : OmegaTail)

(h12 : t1.depth = t2.depth)

(h13 : t1.depth = t3.depth)
 :ultra_dist t1 t3 = 0 ∨ ultra_dist t1 t3 ≥ Nat.min (ultra_dist t1 t2) (ultra_dist t2 t3)**


Ultrametric triangle inequality (formal, universal) for equal-depth tails.
d(t1,t3) = 0 or d(t1,t3) ≥ min(d(t1,t2), d(t2,t3)).

---

### `Tau.Polarity.ultra_triangle_mk`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaGerms.lean#L351-L357)
**theorem
Tau.Polarity.ultra_triangle_mk
(n1 n2 n3 d : Denotation.TauIdx)
 :ultra_dist (mk_omega_tail n1 d) (mk_omega_tail n3 d) = 0 ∨ ultra_dist (mk_omega_tail n1 d) (mk_omega_tail n3 d) ≥ Nat.min (ultra_dist (mk_omega_tail n1 d) (mk_omega_tail n2 d))
 (ultra_dist (mk_omega_tail n2 d) (mk_omega_tail n3 d))**


Ultrametric triangle for mk_omega_tail (the most common use case).
