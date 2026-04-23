---
layout: taulib-doc
title: "TauLib.BookI.Denotation.Equality"
permalink: /verify/taulib/docs/book-i-denotation-equality/
lane: verify
module_name: "TauLib.BookI.Denotation.Equality"
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

# TauLib.Denotation.Equality


The three levels of equality in Category τ.

## Registry Cross-References


- [I.D15] Three-Level Equality — `ontic_eq`, `addr_equiv`, `shadow_eq`


## Mathematical Content


Category τ distinguishes three levels of equality:

- **Ontic identity**: primitive structural equality (x = y as TauObj)

- **Address equivalence**: two programs compute the same result (NF-equivalent)

- **Shadow equality**: same coordinates (collapses to ontic for Parts I-III)


All three are decidable. Shadow equality implies ontic equality
(in the current scope; the full ABCD chart in Part IV may distinguish them).

---

### `Tau.Denotation.ontic_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L31-L32)
**def
Tau.Denotation.ontic_eq
(x y : Kernel.TauObj)
 :Prop**


[I.D15, Level 1] Ontic identity: primitive structural equality.
Equations
- Tau.Denotation.ontic_eq x y = (x = y)
Instances For

---

### `Tau.Denotation.addr_equiv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L34-L37)
**def
Tau.Denotation.addr_equiv
(p q : Program)
 :Prop**


[I.D15, Level 2] Address equivalence: two programs yield the same
result on every input.
Equations
- Tau.Denotation.addr_equiv p q = ∀ (x : Tau.Kernel.TauObj), Tau.Denotation.execProgram p x = Tau.Denotation.execProgram q x
Instances For

---

### `Tau.Denotation.shadow_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L39-L42)
**def
Tau.Denotation.shadow_eq
(x y : Kernel.TauObj)
 :Prop**


[I.D15, Level 3] Shadow equality: same coordinates.
In Parts I-III, this collapses to ontic equality.
(The full ABCD chart in Part IV may refine this.)
Equations
- Tau.Denotation.shadow_eq x y = (x = y)
Instances For

---

### `Tau.Denotation.ontic_eq_decidable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L48-L50)
**instance
Tau.Denotation.ontic_eq_decidable
(x y : Kernel.TauObj)
 :Decidable (ontic_eq x y)**


Ontic equality is decidable.
Equations
- Tau.Denotation.ontic_eq_decidable x y = inferInstanceAs (Decidable (x = y))

---

### `Tau.Denotation.addr_equiv_refl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L52-L54)
**theorem
Tau.Denotation.addr_equiv_refl
(p : Program)
 :addr_equiv p p**


Address equivalence is reflexive.

---

### `Tau.Denotation.addr_equiv_symm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L56-L58)
**theorem
Tau.Denotation.addr_equiv_symm
{p q : Program}

(h : addr_equiv p q)
 :addr_equiv q p**


Address equivalence is symmetric.

---

### `Tau.Denotation.addr_equiv_trans`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L60-L63)
**theorem
Tau.Denotation.addr_equiv_trans
{p q r : Program}

(h1 : addr_equiv p q)

(h2 : addr_equiv q r)
 :addr_equiv p r**


Address equivalence is transitive.

---

### `Tau.Denotation.addr_equiv_nil`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L65-L67)
**theorem
Tau.Denotation.addr_equiv_nil :addr_equiv [] []**


The empty program is addr_equiv to itself.

---

### `Tau.Denotation.shadow_implies_ontic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L69-L71)
**theorem
Tau.Denotation.shadow_implies_ontic
(x y : Kernel.TauObj)

(h : shadow_eq x y)
 :ontic_eq x y**


Shadow equality implies ontic equality (trivially, in current scope).

---

### `Tau.Denotation.addr_equiv_compose_left`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L73-L77)
**theorem
Tau.Denotation.addr_equiv_compose_left
{p₁ p₂ : Program}

(h : addr_equiv p₁ p₂)

(q : Program)
 :addr_equiv (p₁.compose q) (p₂.compose q)**


Composition preserves address equivalence (left).

---

### `Tau.Denotation.addr_equiv_compose_right`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/Equality.lean#L79-L83)
**theorem
Tau.Denotation.addr_equiv_compose_right
(p : Program)

{q₁ q₂ : Program}

(h : addr_equiv q₁ q₂)
 :addr_equiv (p.compose q₁) (p.compose q₂)**


Composition preserves address equivalence (right).
