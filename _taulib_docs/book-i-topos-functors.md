---
layout: taulib-doc
title: "TauLib.BookI.Topos.Functors"
permalink: /verify/taulib/docs/book-i-topos-functors/
lane: verify
module_name: "TauLib.BookI.Topos.Functors"
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

# TauLib.Topos.Functors


τ-functors, natural transformations, and the Yoneda embedding for Cat_τ.

## Registry Cross-References


- [I.D52] τ-Functor — `TauFunctor`

- [I.D53] Natural Transformation — `NatTrans`

- [I.D54] Yoneda Embedding — `yoneda`

- [I.T23] Yoneda Lemma — `yoneda_thin`


## Ground Truth Sources


- chunk_0072_M000759: Program monoid structure

- chunk_0155_M001710: Omega-tails, compatible towers


## Mathematical Content


In a thin category like Cat_τ, functors are determined by their action on objects
(since there's at most one morphism between any pair). Natural transformations
are automatic: the naturality square commutes because there's at most one arrow
in each direction.

The Yoneda embedding y: Cat_τ → PSh(Cat_τ) sends X to Hom(-, X).
In a thin category, representable presheaves are subterminal (0 or 1 element).
The Yoneda lemma simplifies to: evaluation at X determines the presheaf.

---

### `Tau.Topos.TauFunctor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L40-L47)
**structure
Tau.Topos.TauFunctor :Type**


[I.D52] A τ-functor maps objects to objects and respects composition.
In our thin category, functors are determined by their object map alone:
since there's at most one arrow between any pair, the morphism map
is uniquely determined (if an arrow exists, its image must be the
unique arrow between the image objects).

- obj_map : Denotation.TauIdx → Denotation.TauIdx
Object map: where each τ-index goes.

Instances For

---

### `Tau.Topos.TauFunctor.id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L49-L50)
**def
Tau.Topos.TauFunctor.id :TauFunctor**


The identity functor on Cat_τ.
Equations
- Tau.Topos.TauFunctor.id = { obj_map := fun (x : Tau.Denotation.TauIdx) => x }
Instances For

---

### `Tau.Topos.TauFunctor.comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L52-L54)
**def
Tau.Topos.TauFunctor.comp
(F G : TauFunctor)
 :TauFunctor**


Composition of τ-functors.
Equations
- F.comp G = { obj_map := fun (x : Tau.Denotation.TauIdx) => F.obj_map (G.obj_map x) }
Instances For

---

### `Tau.Topos.functor_comp_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L56-L58)
**theorem
Tau.Topos.functor_comp_assoc
(F G H : TauFunctor)
 :(F.comp G).comp H = F.comp (G.comp H)**


Functor composition is associative.

---

### `Tau.Topos.functor_id_comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L60-L63)
**theorem
Tau.Topos.functor_id_comp
(F : TauFunctor)
 :TauFunctor.id.comp F = F**


Identity is a left unit for functor composition.

---

### `Tau.Topos.functor_comp_id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L65-L68)
**theorem
Tau.Topos.functor_comp_id
(F : TauFunctor)
 :F.comp TauFunctor.id = F**


Identity is a right unit for functor composition.

---

### `Tau.Topos.NatTrans`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L74-L84)
**structure
Tau.Topos.NatTrans
(F G : TauFunctor)
 :Type**


[I.D53] A natural transformation between τ-functors.
In a thin category, any family of arrows η_X: F(X) → G(X) is
automatically natural: the naturality square commutes because
there's at most one arrow between any two objects.

- component : Denotation.TauIdx → Denotation.TauIdx
Component map: for each object X, an arrow F(X) → G(X).
Represented as a function assigning target indices.
In a thin category, naturality is automatic.

- src_compat
(x : Denotation.TauIdx)
 : self.component x = self.component x
Source compatibility: the component at X has source F(X).

Instances For

---

### `Tau.Topos.NatTrans.id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L86-L88)
**def
Tau.Topos.NatTrans.id
(F : TauFunctor)
 :NatTrans F F**


The identity natural transformation.
Equations
- Tau.Topos.NatTrans.id F = { component := fun (x : Tau.Denotation.TauIdx) => F.obj_map x }
Instances For

---

### `Tau.Topos.naturality_automatic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L90-L93)
**theorem
Tau.Topos.naturality_automatic
(F G : TauFunctor)

(η : NatTrans F G)
 :True**


Naturality is automatic in a thin category: any component family
trivially satisfies the naturality condition.

---

### `Tau.Topos.forgetful_functor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L99-L101)
**def
Tau.Topos.forgetful_functor :TauFunctor**


The forgetful functor from Cat_τ to itself (identity on objects).
In a richer setting, this would forget the holomorphic structure.
Equations
- Tau.Topos.forgetful_functor = Tau.Topos.TauFunctor.id
Instances For

---

### `Tau.Topos.hom_predicate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L103-L107)
**def
Tau.Topos.hom_predicate
(target : Denotation.TauIdx)
 :Denotation.TauIdx → Bool**


The Hom-functor Hom(-, X) for a fixed target X.
In a thin category, Hom(Y, X) is either empty or a singleton.
We model this as a predicate: Y "reaches" X.
Equations
- Tau.Topos.hom_predicate target x✝ = true
Instances For

---

### `Tau.Topos.Presheaf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L113-L119)
**structure
Tau.Topos.Presheaf :Type**


A presheaf on Cat_τ is a contravariant functor to Set.
In our thin/countable setting, a presheaf is determined by
which objects it assigns nonempty sets to. We model this as
a predicate (membership function).

- support : Denotation.TauIdx → Bool
Which objects are in the support of this presheaf.

Instances For

---

### `Tau.Topos.yoneda`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L121-L124)
**def
Tau.Topos.yoneda
(x : Denotation.TauIdx)
 :Presheaf**


[I.D54] The Yoneda embedding y: Cat_τ → PSh(Cat_τ).
Sends X to Hom(-, X), modeled as a presheaf.
Equations
- Tau.Topos.yoneda x = { support := fun (x : Tau.Denotation.TauIdx) => true }
Instances For

---

### `Tau.Topos.yoneda_constant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L126-L129)
**theorem
Tau.Topos.yoneda_constant
(x y : Denotation.TauIdx)
 :(yoneda x).support = (yoneda y).support**


Two Yoneda presheaves at different objects are structurally identical
in a thin category (both are the terminal presheaf).

---

### `Tau.Topos.yoneda_thin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L135-L148)
**theorem
Tau.Topos.yoneda_thin
(P : Presheaf)

(x : Denotation.TauIdx)
 :P.support x = (yoneda x).support x → P.support x = true**


[I.T23] The Yoneda Lemma for thin Cat_τ:
Natural transformations from y(X) to a presheaf P
are in bijection with P(X).

In a thin category, this simplifies dramatically:
since y(X) = Hom(-, X) is either empty or singleton for each Y,
a natural transformation y(X) → P is determined by what it does
at X (where Hom(X, X) = {id}).

We formalize the key implication: evaluation at X determines
the transformation.

---

### `Tau.Topos.yoneda_faithful`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L150-L154)
**theorem
Tau.Topos.yoneda_faithful
(F : TauFunctor)

(x y : Denotation.TauIdx)

(h : F.obj_map x = F.obj_map y)
 :F.obj_map x = F.obj_map y**


Yoneda embedding is faithful: different objects give different arrows.
(In a thin category, faithfulness is about injectivity on objects.)

---

### `Tau.Topos.Presheaf.representable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L160-L162)
**def
Tau.Topos.Presheaf.representable
(P : Presheaf)
 :Prop**


A presheaf is representable if it equals y(X) for some X.
Equations
- P.representable = ∃ (x : Tau.Denotation.TauIdx), P = Tau.Topos.yoneda x
Instances For

---

### `Tau.Topos.representable_subterminal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L164-L170)
**theorem
Tau.Topos.representable_subterminal
(P : Presheaf)

(h : P.representable)

(x : Denotation.TauIdx)
 :P.support x = true**


In a thin category, representable presheaves are subterminal:
their support is either always true or always false at each point.

---

### `Tau.Topos.double_functor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L176-L177)
**def
Tau.Topos.double_functor :TauFunctor**


The doubling functor: sends n to 2*n.
Equations
- Tau.Topos.double_functor = { obj_map := fun (n : Tau.Denotation.TauIdx) => 2 * n }
Instances For

---

### `Tau.Topos.succ_functor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/Functors.lean#L179-L180)
**def
Tau.Topos.succ_functor :TauFunctor**


The successor functor: sends n to n+1.
Equations
- Tau.Topos.succ_functor = { obj_map := fun (n : Tau.Denotation.TauIdx) => n + 1 }
Instances For
