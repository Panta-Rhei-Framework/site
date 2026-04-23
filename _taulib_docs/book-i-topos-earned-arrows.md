---
layout: taulib-doc
title: "TauLib.BookI.Topos.EarnedArrows"
permalink: /verify/taulib/docs/book-i-topos-earned-arrows/
lane: verify
module_name: "TauLib.BookI.Topos.EarnedArrows"
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

# TauLib.Topos.EarnedArrows


The earned category Cat_τ: objects are τ-indices, morphisms are τ-arrows.

## Registry Cross-References


- [I.D50] τ-Arrow — `TauArrow`

- [I.D51] Cat_τ — `CatTau`

- [I.T22] Category Axioms — `cat_tau_id_left`, `cat_tau_id_right`, `cat_tau_assoc`

- [I.P25] Thin Category — `cat_tau_thin`


## Ground Truth Sources


- chunk_0072_M000759: Program monoid, normal form

- chunk_0155_M001710: Omega-tails, holomorphic structure


## Mathematical Content


A τ-arrow from X to Y is a HolFun that transforms ω-germs at X to ω-germs at Y.
Two HolFuns define the same arrow if they agree on all inputs at all stages
(i.e., they are extensionally equal).

Cat_τ is the category with:


- Objects: TauIdx (the τ-index set)

- Morphisms: τ-arrows (HolFun equivalence classes)

- Identity: id_holfun

- Composition: from composition closure (I.T20)

- Associativity: from I.P24


Cat_τ is THIN: between any two objects there is at most one morphism.
This follows from the τ-Identity Theorem (I.T21).

---

### `Tau.Topos.TauArrow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L45-L50)
**structure
Tau.Topos.TauArrow :Type**


[I.D50] A τ-arrow from source to target, carrying a HolFun.
Two τ-arrows are equal iff their underlying HolFuns agree extensionally.

- source : Denotation.TauIdx
- target : Denotation.TauIdx
- holfun : Holomorphy.HolFun
Instances For

---

### `Tau.Topos.TauArrow.ext_agree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L52-L55)
**def
Tau.Topos.TauArrow.ext_agree
(a₁ a₂ : TauArrow)

(hs : a₁.source = a₂.source)

(ht : a₁.target = a₂.target)
 :a₁.source = a₂.source ∧ a₁.target = a₂.target**


Two τ-arrows with the same source/target agree extensionally.
Equations
- ⋯ = ⋯
Instances For

---

### `Tau.Topos.id_arrow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L61-L63)
**def
Tau.Topos.id_arrow
(x : Denotation.TauIdx)
 :TauArrow**


The identity τ-arrow at object X.
Equations
- Tau.Topos.id_arrow x = { source := x, target := x, holfun := Tau.Holomorphy.id_holfun 0 }
Instances For

---

### `Tau.Topos.arrow_comp_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L65-L67)
**def
Tau.Topos.arrow_comp_stage
(a₁ a₂ : TauArrow)
 :Holomorphy.StageFun**


Compose two τ-arrows stagewise (when source/target match).
Equations
- Tau.Topos.arrow_comp_stage a₁ a₂ = a₁.holfun.transformer.stage_fun.comp a₂.holfun.transformer.stage_fun
Instances For

---

### `Tau.Topos.CatTau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L69-L73)
**structure
Tau.Topos.CatTau :Type**


[I.D51] The data of Cat_τ: objects, identity arrows, and composition.
Cat_τ is the earned category — not imported but built from HolFun.

- id_ : Denotation.TauIdx → TauArrow
Instances For

---

### `Tau.Topos.cat_tau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L75-L76)
**def
Tau.Topos.cat_tau :CatTau**


The canonical Cat_τ instance.
Equations
- Tau.Topos.cat_tau = { id_ := Tau.Topos.id_arrow }
Instances For

---

### `Tau.Topos.cat_tau_id_src`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L78-L79)
**theorem
Tau.Topos.cat_tau_id_src
(x : Denotation.TauIdx)
 :(cat_tau.id_ x).source = x**


Identity arrows have matching source.

---

### `Tau.Topos.cat_tau_id_tgt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L81-L82)
**theorem
Tau.Topos.cat_tau_id_tgt
(x : Denotation.TauIdx)
 :(cat_tau.id_ x).target = x**


Identity arrows have matching target.

---

### `Tau.Topos.cat_tau_id_left_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L88-L92)
**theorem
Tau.Topos.cat_tau_id_left_stage
(f : Holomorphy.StageFun)

(n k : Denotation.TauIdx)
 :(Holomorphy.id_stage.comp f).b_fun n k = Polarity.reduce (f.b_fun n k) k**


[I.T22a] Left identity: id ∘ f gives the same stagewise output as
applying id to the output of f.

---

### `Tau.Topos.cat_tau_id_right_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L94-L97)
**theorem
Tau.Topos.cat_tau_id_right_stage
(f : Holomorphy.StageFun)

(n k : Denotation.TauIdx)
 :(f.comp Holomorphy.id_stage).b_fun n k = f.b_fun (Polarity.reduce n k) k**


[I.T22b] Right identity: f ∘ id gives the same stagewise output.

---

### `Tau.Topos.cat_tau_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L99-L102)
**theorem
Tau.Topos.cat_tau_assoc
(f₁ f₂ f₃ : Holomorphy.StageFun)
 :(f₁.comp f₂).comp f₃ = f₁.comp (f₂.comp f₃)**


[I.T22c] Associativity of stagewise composition.

---

### `Tau.Topos.cat_tau_gt_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L104-L108)
**theorem
Tau.Topos.cat_tau_gt_assoc
(gt₁ gt₂ gt₃ : Holomorphy.GermTransformer)
 :(gt₁.comp gt₂).comp gt₃ = gt₁.comp (gt₂.comp gt₃)**


[I.T22d] GermTransformer composition is associative.

---

### `Tau.Topos.cat_tau_thin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L114-L121)
**theorem
Tau.Topos.cat_tau_thin
(f₁ f₂ : Holomorphy.StageFun)

(h₁ : Holomorphy.TowerCoherent f₁)

(h₂ : Holomorphy.TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hagree : ∀ (n : Denotation.TauIdx), Holomorphy.agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → Holomorphy.agree_at f₁ f₂ n k**


[I.P25] Cat_τ is thin: if two tower-coherent stagewise functions
agree at stage d₀ for all inputs, they agree at all stages ≤ d₀.
This is a direct corollary of the τ-Identity Theorem (I.T21).

---

### `Tau.Topos.cat_tau_self_agree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L123-L125)
**theorem
Tau.Topos.cat_tau_self_agree
(f : Holomorphy.StageFun)

(n k : Denotation.TauIdx)
 :Holomorphy.agree_at f f n k**


Thin category consequence: self-agreement is trivial.

---

### `Tau.Topos.id_holfun_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L131-L133)
**theorem
Tau.Topos.id_holfun_coherent
(d : ℕ)
 :Holomorphy.TowerCoherent (Holomorphy.id_holfun d).transformer.stage_fun**


The identity HolFun at any depth is tower-coherent.

---

### `Tau.Topos.chi_plus_idempotent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L135-L138)
**theorem
Tau.Topos.chi_plus_idempotent :(Holomorphy.chi_plus_stage.comp Holomorphy.chi_plus_stage).b_fun 1 1 = Holomorphy.chi_plus_stage.b_fun 1 1**


χ₊ composed with χ₊ gives the same B-sector output (idempotent, sample).

---

### `Tau.Topos.chi_minus_idempotent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L140-L143)
**theorem
Tau.Topos.chi_minus_idempotent :(Holomorphy.chi_minus_stage.comp Holomorphy.chi_minus_stage).c_fun 1 1 = Holomorphy.chi_minus_stage.c_fun 1 1**


χ₋ composed with χ₋ gives the same C-sector output (idempotent, sample).

---

### `Tau.Topos.at_least_three_holfuns`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedArrows.lean#L149-L152)
**theorem
Tau.Topos.at_least_three_holfuns :Holomorphy.chi_plus_stage.b_fun 1 1 ≠ Holomorphy.chi_minus_stage.b_fun 1 1**


id, χ₊, χ₋ are at least 3 distinct HolFuns:
χ₊ and χ₋ disagree at input 1, stage 1 in the B-sector.
