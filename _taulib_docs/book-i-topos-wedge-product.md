---
layout: taulib-doc
title: "TauLib.BookI.Topos.WedgeProduct"
permalink: /verify/taulib/docs/book-i-topos-wedge-product/
lane: verify
module_name: "TauLib.BookI.Topos.WedgeProduct"
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

# TauLib.Topos.WedgeProduct


Wedge product (coproduct) and the bi-monoidal structure of E_τ.

## Registry Cross-References


- [I.D62] Categorical Coproduct — `cat_coproduct`

- [I.T27] Distributivity — `product_distributes_over_coproduct`

- [I.D63] Bi-Monoidal Structure — `BiMonoidal`


## Mathematical Content


The categorical coproduct in E_τ is the pointwise disjunction of presheaves.
The bi-monoidal structure has product (×) distributing over coproduct (∨).

---

### `Tau.Topos.cat_coproduct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L28-L31)
**def
Tau.Topos.cat_coproduct
(P Q : Presheaf)
 :Presheaf**


[I.D62] The categorical coproduct of two presheaves:
pointwise disjunction of support predicates.
Equations
- Tau.Topos.cat_coproduct P Q = Tau.Topos.presheaf_coproduct P Q
Instances For

---

### `Tau.Topos.coprod_inl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L33-L36)
**theorem
Tau.Topos.coprod_inl
(P Q : Presheaf)

(x : Denotation.TauIdx)
 :P.support x = true → (cat_coproduct P Q).support x = true**


Left injection: P → P ∨ Q.

---

### `Tau.Topos.coprod_inr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L38-L41)
**theorem
Tau.Topos.coprod_inr
(P Q : Presheaf)

(x : Denotation.TauIdx)
 :Q.support x = true → (cat_coproduct P Q).support x = true**


Right injection: Q → P ∨ Q.

---

### `Tau.Topos.coproduct_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L43-L46)
**theorem
Tau.Topos.coproduct_comm
(P Q : Presheaf)
 :(cat_coproduct P Q).support = (cat_coproduct Q P).support**


Coproduct is commutative.

---

### `Tau.Topos.coproduct_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L48-L52)
**theorem
Tau.Topos.coproduct_assoc
(P Q R : Presheaf)
 :(cat_coproduct (cat_coproduct P Q) R).support = (cat_coproduct P (cat_coproduct Q R)).support**


Coproduct is associative.

---

### `Tau.Topos.coproduct_initial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L54-L57)
**theorem
Tau.Topos.coproduct_initial
(P : Presheaf)
 :(cat_coproduct P { support := fun (x : Denotation.TauIdx) => false }).support = P.support**


Coproduct with initial is identity.

---

### `Tau.Topos.product_distributes_over_coproduct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L63-L70)
**theorem
Tau.Topos.product_distributes_over_coproduct
(P Q R : Presheaf)
 :(cat_product P (cat_coproduct Q R)).support = (cat_coproduct (cat_product P Q) (cat_product P R)).support**


[I.T27] Product distributes over coproduct:
P × (Q ∨ R) = (P × Q) ∨ (P × R).

---

### `Tau.Topos.product_distributes_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L72-L78)
**theorem
Tau.Topos.product_distributes_right
(P Q R : Presheaf)
 :(cat_product (cat_coproduct P Q) R).support = (cat_coproduct (cat_product P R) (cat_product Q R)).support**


Right distributivity: (P ∨ Q) × R = (P × R) ∨ (Q × R).

---

### `Tau.Topos.BiMonoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L84-L94)
**structure
Tau.Topos.BiMonoidal :Type**


[I.D63] The bi-monoidal structure on E_τ:
product (×) and coproduct (∨) with distributivity.

- times : Presheaf → Presheaf → Presheaf
- wedge : Presheaf → Presheaf → Presheaf
- one : Presheaf
- zero : Presheaf
Instances For

---

### `Tau.Topos.bi_monoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L96-L97)
**def
Tau.Topos.bi_monoidal :BiMonoidal**


The canonical bi-monoidal structure.
Equations
- Tau.Topos.bi_monoidal = { }
Instances For

---

### `Tau.Topos.product_absorb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L99-L102)
**theorem
Tau.Topos.product_absorb
(P : Presheaf)
 :(cat_product P { support := fun (x : Denotation.TauIdx) => false }).support = { support := fun (x : Denotation.TauIdx) => false }.support**


Absorption: P × 0 = 0.

---

### `Tau.Topos.coproduct_terminal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/WedgeProduct.lean#L104-L107)
**theorem
Tau.Topos.coproduct_terminal
(P : Presheaf)
 :(cat_coproduct P { support := fun (x : Denotation.TauIdx) => true }).support = { support := fun (x : Denotation.TauIdx) => true }.support**


Coproduct with terminal: P ∨ 1 = 1.
