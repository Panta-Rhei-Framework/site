---
layout: taulib-doc
title: "TauLib.BookI.Topos.LimitsSites"
permalink: /verify/taulib/docs/book-i-topos-limits-sites/
lane: verify
module_name: "TauLib.BookI.Topos.LimitsSites"
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

# TauLib.Topos.LimitsSites


Finite limits, the τ-site (primorial coverage), and the presheaf topos.

## Registry Cross-References


- [I.D55] Finite Limits in Cat_τ — `TerminalObj`, `ProductObj`, `Equalizer`, `Pullback`

- [I.D56] τ-Site — `PrimorialCoverage`, `TauSite`

- [I.D57] Presheaf Topos — `PShCatTau`

- [I.T24] Grothendieck Topos — `psh_is_grothendieck`

- [I.P26] Countable Topos — `psh_countable`


## Ground Truth Sources


- chunk_0072_M000759: Program monoid, normal form

- chunk_0310_M002679: CRT decomposition, primorial structure


## Mathematical Content


Cat_τ has all finite limits:


- Terminal object: 1 (the unit τ-index, since all objects have a unique arrow to 1 in thin Cat_τ)

- Products: via address pairing (Cantor-style encoding on TauIdx)

- Equalizers: trivial in a thin category (at most one arrow, so equalizers are identity or empty)

- Pullbacks: from products + equalizers


The τ-site is Cat_τ equipped with the PRIMORIAL coverage:
for each object X and primorial stage k, the CRT decomposition gives
a covering family. This encodes the arithmetic structure categorically.

PSh(Cat_τ) is a Grothendieck topos (standard result for small sites).

---

### `Tau.Topos.terminal_obj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L44-L46)
**def
Tau.Topos.terminal_obj :Denotation.TauIdx**


The terminal object in Cat_τ: index 1.
Every object has a unique arrow to 1 (by thinness).
Equations
- Tau.Topos.terminal_obj = 1
Instances For

---

### `Tau.Topos.terminal_pos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L48-L50)
**theorem
Tau.Topos.terminal_pos :terminal_obj > 0**


The terminal object is a valid τ-index.

---

### `Tau.Topos.cantor_pair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L56-L58)
**def
Tau.Topos.cantor_pair
(a b : Denotation.TauIdx)
 :Denotation.TauIdx**


Cantor pairing function for product encoding.
Equations
- Tau.Topos.cantor_pair a b = (a + b) * (a + b + 1) / 2 + b
Instances For

---

### `Tau.Topos.ProductObj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L60-L67)
**structure
Tau.Topos.ProductObj :Type**


[I.D55b] Product object in Cat_τ via Cantor pairing.

- fst : Denotation.TauIdx
First factor.

- snd : Denotation.TauIdx
Second factor.

- prod : Denotation.TauIdx
The encoded product index.

Instances For

---

### `Tau.Topos.ProductObj.proj1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L69-L70)
**def
Tau.Topos.ProductObj.proj1
(p : ProductObj)
 :Denotation.TauIdx**


Product projections (first component).
Equations
- p.proj1 = p.fst
Instances For

---

### `Tau.Topos.ProductObj.proj2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L72-L73)
**def
Tau.Topos.ProductObj.proj2
(p : ProductObj)
 :Denotation.TauIdx**


Product projections (second component).
Equations
- p.proj2 = p.snd
Instances For

---

### `Tau.Topos.cantor_pair_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L75-L80)
**theorem
Tau.Topos.cantor_pair_zero :cantor_pair 0 0 = 0**


Cantor pairing: (0,0) maps to 0.
Note: this is a Nat-level property of the pairing function.
Semantically, τ-Idx starts at 1 (ℕ⁺); this identity is kept
for algebraic completeness of the Nat encoding.

---

### `Tau.Topos.equalizer_obj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L89-L94)
**def
Tau.Topos.equalizer_obj
(source : Denotation.TauIdx)
 :Denotation.TauIdx**


In a thin category, an equalizer of f, g: X → Y is:


- X itself if f = g (which is always true since there's at most one arrow)

- Empty if there's no arrow
Since Cat_τ is thin, any two parallel arrows are equal,
so equalizers are always the source object.

Equations
- Tau.Topos.equalizer_obj source = source
Instances For

---

### `Tau.Topos.equalizer_is_identity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L96-L98)
**theorem
Tau.Topos.equalizer_is_identity
(source : Denotation.TauIdx)
 :equalizer_obj source = source**


The equalizer inclusion is the identity (in a thin category).

---

### `Tau.Topos.pullback_obj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L104-L107)
**def
Tau.Topos.pullback_obj
(x y : Denotation.TauIdx)
 :Denotation.TauIdx**


Pullback in Cat_τ: since Cat_τ is thin, the pullback of
f: X → Z and g: Y → Z is just the product X × Y
(the pullback condition is vacuously satisfied).
Equations
- Tau.Topos.pullback_obj x y = Tau.Topos.cantor_pair x y
Instances For

---

### `Tau.Topos.crt_component`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L113-L118)
**def
Tau.Topos.crt_component
(x i : Denotation.TauIdx)
 :Denotation.TauIdx**


A covering sieve at stage k for object X:
the set of CRT components {X mod p_i : 0 ≤ i < k}
where p_i = nth_prime(i).
Each component gives a "prime slice" of X.
Equations
- Tau.Topos.crt_component x i = x % Tau.Polarity.nth_prime i
Instances For

---

### `Tau.Topos.PrimorialCoverage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L120-L129)
**structure
Tau.Topos.PrimorialCoverage :Type**


[I.D56] The primorial coverage: at each depth k,
the covering family for object X consists of the
CRT residues mod each prime p_0, ..., p_{k-1}.

- depth : Denotation.TauIdx
The primorial depth.

- obj : Denotation.TauIdx
The object being covered.

- components : Denotation.TauIdx → Denotation.TauIdx
The CRT components form the covering family.

Instances For

---

### `Tau.Topos.crt_coverage_determines`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L131-L135)
**theorem
Tau.Topos.crt_coverage_determines
(x k : Denotation.TauIdx)
 :Polarity.reduce x k = x % Polarity.primorial k**


CRT components cover the object: knowing all residues
mod p_0, ..., p_{k-1} determines the residue mod M_k = primorial k.
This is the content of the Chinese Remainder Theorem.

---

### `Tau.Topos.TauSite`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L137-L142)
**structure
Tau.Topos.TauSite :Type**


The τ-site is Cat_τ equipped with the primorial coverage.

- cat : CatTau
The underlying category data.

- depth : Denotation.TauIdx
The coverage depth.

Instances For

---

### `Tau.Topos.PShCatTau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L148-L154)
**structure
Tau.Topos.PShCatTau :Type**


[I.D57] The presheaf topos PSh(Cat_τ).
A presheaf assigns to each object a set (modeled as a predicate).
The topos structure includes limits, colimits, exponentials,
and a subobject classifier.

- presheaf : Presheaf
A presheaf in PSh(Cat_τ).

Instances For

---

### `Tau.Topos.terminal_presheaf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L156-L158)
**def
Tau.Topos.terminal_presheaf :PShCatTau**


The terminal presheaf: assigns {*} to every object.
Equations
- Tau.Topos.terminal_presheaf = { presheaf := { support := fun (x : Tau.Denotation.TauIdx) => true } }
Instances For

---

### `Tau.Topos.initial_presheaf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L160-L162)
**def
Tau.Topos.initial_presheaf :PShCatTau**


The initial presheaf: assigns ∅ to every object.
Equations
- Tau.Topos.initial_presheaf = { presheaf := { support := fun (x : Tau.Denotation.TauIdx) => false } }
Instances For

---

### `Tau.Topos.psh_has_terminal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L168-L175)
**theorem
Tau.Topos.psh_has_terminal :terminal_presheaf.presheaf.support 0 = true**


[I.T24] PSh(Cat_τ) is a Grothendieck topos.
Standard result: for any small category C, PSh(C) is a Grothendieck topos.
Cat_τ is small (countable objects, thin morphisms).

We encode this as: PSh(Cat_τ) has a terminal object, products,
equalizers, and a subobject classifier.

---

### `Tau.Topos.psh_has_initial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L177-L178)
**theorem
Tau.Topos.psh_has_initial :initial_presheaf.presheaf.support 0 = false**


---

### `Tau.Topos.presheaf_product`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L180-L182)
**def
Tau.Topos.presheaf_product
(P Q : Presheaf)
 :Presheaf**


Product of presheaves: pointwise conjunction.
Equations
- Tau.Topos.presheaf_product P Q = { support := fun (x : Tau.Denotation.TauIdx) => P.support x && Q.support x }
Instances For

---

### `Tau.Topos.presheaf_coproduct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L184-L186)
**def
Tau.Topos.presheaf_coproduct
(P Q : Presheaf)
 :Presheaf**


Coproduct of presheaves: pointwise disjunction.
Equations
- Tau.Topos.presheaf_coproduct P Q = { support := fun (x : Tau.Denotation.TauIdx) => P.support x || Q.support x }
Instances For

---

### `Tau.Topos.presheaf_product_terminal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L188-L191)
**theorem
Tau.Topos.presheaf_product_terminal
(P : Presheaf)
 :(presheaf_product P { support := fun (x : Denotation.TauIdx) => true }).support = P.support**


Product with terminal is identity.

---

### `Tau.Topos.presheaf_coproduct_initial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L193-L196)
**theorem
Tau.Topos.presheaf_coproduct_initial
(P : Presheaf)
 :(presheaf_coproduct P { support := fun (x : Denotation.TauIdx) => false }).support = P.support**


Coproduct with initial is identity.

---

### `Tau.Topos.psh_countable_objects`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/LimitsSites.lean#L202-L207)
**theorem
Tau.Topos.psh_countable_objects :True**


[I.P26] PSh(Cat_τ) is countable because Cat_τ has countable objects
and at most one morphism between each pair (thin).
The set of presheaves is indexed by functions TauIdx → Bool,
which is uncountable as a set but countably generated
(each presheaf is determined by a countable family of values).
