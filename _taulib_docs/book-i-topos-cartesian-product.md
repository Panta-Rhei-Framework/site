---
layout: taulib-doc
title: "TauLib.BookI.Topos.CartesianProduct"
permalink: /verify/taulib/docs/book-i-topos-cartesian-product/
lane: verify
module_name: "TauLib.BookI.Topos.CartesianProduct"
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

# TauLib.Topos.CartesianProduct


Cartesian product as an earned bi-functor in E_τ.

## Registry Cross-References


- [I.D60] Categorical Product — `cat_product`

- [I.T26] Product Universal Property — `product_universal`

- [I.D61] Cartesian Monoidal Structure — `CartesianMonoidal`


## Mathematical Content


The categorical product in E_τ is the pointwise conjunction of presheaves.
The terminal presheaf is the monoidal unit.
Products satisfy the universal property: any pair of morphisms factors
uniquely through the product.

---

### `Tau.Topos.cat_product`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L30-L33)
**def
Tau.Topos.cat_product
(P Q : Presheaf)
 :Presheaf**


[I.D60] The categorical product of two presheaves:
pointwise conjunction of support predicates.
Equations
- Tau.Topos.cat_product P Q = Tau.Topos.presheaf_product P Q
Instances For

---

### `Tau.Topos.cat_proj1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L35-L38)
**theorem
Tau.Topos.cat_proj1
(P Q : Presheaf)

(x : Denotation.TauIdx)

(h : (cat_product P Q).support x = true)
 :P.support x = true**


First projection: product → first factor.

---

### `Tau.Topos.cat_proj2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L40-L43)
**theorem
Tau.Topos.cat_proj2
(P Q : Presheaf)

(x : Denotation.TauIdx)

(h : (cat_product P Q).support x = true)
 :Q.support x = true**


Second projection: product → second factor.

---

### `Tau.Topos.product_universal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L49-L57)
**theorem
Tau.Topos.product_universal
(P Q R : Presheaf)

(hP : ∀ (x : Denotation.TauIdx), R.support x = true → P.support x = true)

(hQ : ∀ (x : Denotation.TauIdx), R.support x = true → Q.support x = true)

(x : Denotation.TauIdx)
 :R.support x = true → (cat_product P Q).support x = true**


[I.T26] Product universal property: if R maps to both P and Q pointwise,
then R maps to P × Q.

---

### `Tau.Topos.product_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L59-L62)
**theorem
Tau.Topos.product_comm
(P Q : Presheaf)
 :(cat_product P Q).support = (cat_product Q P).support**


Product is commutative up to support equality.

---

### `Tau.Topos.product_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L64-L68)
**theorem
Tau.Topos.product_assoc
(P Q R : Presheaf)
 :(cat_product (cat_product P Q) R).support = (cat_product P (cat_product Q R)).support**


Product is associative up to support equality.

---

### `Tau.Topos.product_terminal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L70-L73)
**theorem
Tau.Topos.product_terminal
(P : Presheaf)
 :(cat_product P { support := fun (x : Denotation.TauIdx) => true }).support = P.support**


Product with terminal is identity.

---

### `Tau.Topos.CartesianMonoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L79-L85)
**structure
Tau.Topos.CartesianMonoidal :Type**


[I.D61] The cartesian monoidal structure on E_τ.
Unit: terminal presheaf. Tensor: pointwise product.

- unit : Presheaf
- tensor : Presheaf → Presheaf → Presheaf
Instances For

---

### `Tau.Topos.cartesian_monoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L87-L88)
**def
Tau.Topos.cartesian_monoidal :CartesianMonoidal**


The canonical cartesian monoidal structure.
Equations
- Tau.Topos.cartesian_monoidal = { }
Instances For

---

### `Tau.Topos.monoidal_left_unit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L90-L93)
**theorem
Tau.Topos.monoidal_left_unit
(P : Presheaf)
 :(cat_product { support := fun (x : Denotation.TauIdx) => true } P).support = P.support**


Left unit law.

---

### `Tau.Topos.monoidal_right_unit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L95-L98)
**theorem
Tau.Topos.monoidal_right_unit
(P : Presheaf)
 :(cat_product P { support := fun (x : Denotation.TauIdx) => true }).support = P.support**


Right unit law.

---

### `Tau.Topos.cantor_product_encoding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Topos/CartesianProduct.lean#L104-L106)
**theorem
Tau.Topos.cantor_product_encoding
(a b : Denotation.TauIdx)
 :cantor_pair a b = (a + b) * (a + b + 1) / 2 + b**


Product encoding at the object level via Cantor pairing.
