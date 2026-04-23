---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.TauHolomorphic"
permalink: /verify/taulib/docs/book-i-holomorphy-tau-holomorphic/
lane: verify
module_name: "TauLib.BookI.Holomorphy.TauHolomorphic"
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

# TauLib.Holomorphy.TauHolomorphic


τ-holomorphic functions: ω-germ transformers with tower coherence.

## Registry Cross-References


- [I.D45] ω-Germ Transformer — `GermTransformer`

- [I.D46] Tower Coherence — `TowerCoherent`

- [I.D47] τ-Holomorphic Function — `HolFun`

- [I.D48] τ-Holomorphic Map — `HolMap`

- [I.T18] CRT Coherence Constraint — `crt_coherence`


## Ground Truth Sources


- chunk_0155_M001710: Omega-tails, compatible towers

- chunk_0228_M002194: Split-complex algebra, sector decomposition

- chunk_0310_M002679: Bipolar partition, character theory


## Mathematical Content


A τ-holomorphic function (HolFun) is an ω-germ transformer that is BOTH:

- D-holomorphic (sector-independent in split-complex coordinates), AND

- Tower-coherent (compatible with primorial reduction maps).


Tower coherence says: reducing the output first, or reducing the input first and
then applying the transformer, gives the same result. This is a naturality condition
that constrains the otherwise-too-flexible D-holomorphic functions.

The CRT Coherence Constraint (I.T18) shows that tower coherence reduces to a
prime-by-prime condition: the transformer is determined by its action on each
individual CRT factor Z/p_iZ.

---

### `Tau.Holomorphy.StageFun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L49-L57)
**structure
Tau.Holomorphy.StageFun :Type**


A stagewise sector function maps (n, k) to a TauIdx value,
representing the action of a sector component at primorial stage M_k
on natural number input n. This is the Nat-level substrate for
germ transformers, avoiding Int coercion issues.

- b_fun : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx
B-sector stagewise function: (n, k) ↦ B-output at stage k.

- c_fun : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx
C-sector stagewise function: (n, k) ↦ C-output at stage k.

Instances For

---

### `Tau.Holomorphy.TowerCoherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L63-L73)
**def
Tau.Holomorphy.TowerCoherent
(f : StageFun)
 :Prop**


[I.D46] Tower coherence for a stagewise sector function:
reducing the output from stage ℓ to stage k agrees with
computing the output at stage k directly.

For the B-sector: reduce(f.b_fun(n, ℓ), k) = f.b_fun(n, k)
For the C-sector: reduce(f.c_fun(n, ℓ), k) = f.c_fun(n, k)

This is a NATURALITY condition on the primorial inverse system.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Holomorphy.tower_coherent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L75-L80)
**def
Tau.Holomorphy.tower_coherent_check
(f : StageFun)

(n k l : Denotation.TauIdx)
 :Bool**


Decidable tower coherence check at given stages (for concrete values).
Equations
- Tau.Holomorphy.tower_coherent_check f n k l = if k > l then true
 else Tau.Polarity.reduce (f.b_fun n l) k == f.b_fun n k && Tau.Polarity.reduce (f.c_fun n l) k == f.c_fun n k
Instances For

---

### `Tau.Holomorphy.GermTransformer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L86-L98)
**structure
Tau.Holomorphy.GermTransformer :Type**


[I.D45] An ω-germ transformer maps omega-tails to sector-pair values.
It carries BOTH:


- A SectorFun giving the D-holomorphic structure (sector independence)

- A StageFun giving the stagewise evaluation (for tower coherence)
The SectorFun provides the algebraic structure; the StageFun provides
the arithmetic evaluation that must be tower-coherent.


- sector_fun : SectorFun
The sector function (D-holomorphic structure).

- stage_fun : StageFun
The stagewise evaluation (arithmetic structure).

- depth : ℕ
Maximum depth.

Instances For

---

### `Tau.Holomorphy.GermTransformer.eval`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L100-L102)
**def
Tau.Holomorphy.GermTransformer.eval
(gt : GermTransformer)

(n k : Denotation.TauIdx)
 :Polarity.SectorPair**


Evaluate a germ transformer at stage k on input n.
Equations
- gt.eval n k = { b_sector := ↑(gt.stage_fun.b_fun n k), c_sector := ↑(gt.stage_fun.c_fun n k) }
Instances For

---

### `Tau.Holomorphy.HolFun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L108-L119)
**structure
Tau.Holomorphy.HolFun :Type**


[I.D47] A τ-holomorphic function (HolFun) is a germ transformer that is:

- D-holomorphic (sector-independent — given by the SectorFun structure)

- Tower-coherent (compatible with primorial reduction maps)


The D-holomorphic condition is structural: the SectorFun ensures sector
independence by construction. The tower coherence condition is the
additional constraint that makes τ-holomorphy rigid.

- transformer : GermTransformer
The underlying germ transformer.

- coherent : TowerCoherent self.transformer.stage_fun
Proof of tower coherence.

Instances For

---

### `Tau.Holomorphy.HolMap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L121-L128)
**structure
Tau.Holomorphy.HolMap :Type**


[I.D48] A τ-holomorphic map bundles a HolFun with source/target data.

- fun_ : HolFun
The underlying holomorphic function.

- source : Denotation.TauIdx
Source object index in τ-Idx.

- target : Denotation.TauIdx
Target object index in τ-Idx.

Instances For

---

### `Tau.Holomorphy.chi_plus_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L134-L136)
**def
Tau.Holomorphy.chi_plus_stage :StageFun**


The χ₊ stagewise function: B-sector gets reduce(n, k), C-sector gets 0.
Equations
- Tau.Holomorphy.chi_plus_stage = { b_fun := fun (n k : Tau.Denotation.TauIdx) => Tau.Polarity.reduce n k,
 c_fun := fun (x x_1 : Tau.Denotation.TauIdx) => 0 }
Instances For

---

### `Tau.Holomorphy.chi_minus_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L138-L140)
**def
Tau.Holomorphy.chi_minus_stage :StageFun**


The χ₋ stagewise function: B-sector gets 0, C-sector gets reduce(n, k).
Equations
- Tau.Holomorphy.chi_minus_stage = { b_fun := fun (x x_1 : Tau.Denotation.TauIdx) => 0,
 c_fun := fun (n k : Tau.Denotation.TauIdx) => Tau.Polarity.reduce n k }
Instances For

---

### `Tau.Holomorphy.id_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L142-L144)
**def
Tau.Holomorphy.id_stage :StageFun**


The identity stagewise function: both sectors get reduce(n, k).
Equations
- Tau.Holomorphy.id_stage = { b_fun := fun (n k : Tau.Denotation.TauIdx) => Tau.Polarity.reduce n k,
 c_fun := fun (n k : Tau.Denotation.TauIdx) => Tau.Polarity.reduce n k }
Instances For

---

### `Tau.Holomorphy.chi_plus_gt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L146-L148)
**def
Tau.Holomorphy.chi_plus_gt
(d : ℕ)
 :GermTransformer**


The χ₊ germ transformer.
Equations
- Tau.Holomorphy.chi_plus_gt d = { sector_fun := Tau.Holomorphy.chi_plus_sf, stage_fun := Tau.Holomorphy.chi_plus_stage, depth := d }
Instances For

---

### `Tau.Holomorphy.chi_minus_gt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L150-L152)
**def
Tau.Holomorphy.chi_minus_gt
(d : ℕ)
 :GermTransformer**


The χ₋ germ transformer.
Equations
- Tau.Holomorphy.chi_minus_gt d = { sector_fun := Tau.Holomorphy.chi_minus_sf, stage_fun := Tau.Holomorphy.chi_minus_stage, depth := d }
Instances For

---

### `Tau.Holomorphy.id_gt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L154-L156)
**def
Tau.Holomorphy.id_gt
(d : ℕ)
 :GermTransformer**


The identity germ transformer.
Equations
- Tau.Holomorphy.id_gt d = { sector_fun := Tau.Holomorphy.SectorFun.id, stage_fun := Tau.Holomorphy.id_stage, depth := d }
Instances For

---

### `Tau.Holomorphy.chi_plus_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L171-L179)
**theorem
Tau.Holomorphy.chi_plus_coherent :TowerCoherent chi_plus_stage**


χ₊ is tower-coherent.

---

### `Tau.Holomorphy.chi_minus_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L181-L189)
**theorem
Tau.Holomorphy.chi_minus_coherent :TowerCoherent chi_minus_stage**


χ₋ is tower-coherent.

---

### `Tau.Holomorphy.id_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L191-L195)
**theorem
Tau.Holomorphy.id_coherent :TowerCoherent id_stage**


The identity is tower-coherent.

---

### `Tau.Holomorphy.chi_plus_holfun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L197-L199)
**def
Tau.Holomorphy.chi_plus_holfun
(d : ℕ)
 :HolFun**


χ₊ as a HolFun.
Equations
- Tau.Holomorphy.chi_plus_holfun d = { transformer := Tau.Holomorphy.chi_plus_gt d, coherent := Tau.Holomorphy.chi_plus_coherent }
Instances For

---

### `Tau.Holomorphy.chi_minus_holfun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L201-L203)
**def
Tau.Holomorphy.chi_minus_holfun
(d : ℕ)
 :HolFun**


χ₋ as a HolFun.
Equations
- Tau.Holomorphy.chi_minus_holfun d = { transformer := Tau.Holomorphy.chi_minus_gt d, coherent := Tau.Holomorphy.chi_minus_coherent }
Instances For

---

### `Tau.Holomorphy.id_holfun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L205-L207)
**def
Tau.Holomorphy.id_holfun
(d : ℕ)
 :HolFun**


The identity as a HolFun.
Equations
- Tau.Holomorphy.id_holfun d = { transformer := Tau.Holomorphy.id_gt d, coherent := Tau.Holomorphy.id_coherent }
Instances For

---

### `Tau.Holomorphy.chi_plus_crt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L219-L223)
**theorem
Tau.Holomorphy.chi_plus_crt
(n k : Denotation.TauIdx)
 :chi_plus_stage.b_fun (Polarity.reduce n k) k = chi_plus_stage.b_fun n k**


CRT coherence for χ₊: the B-sector output depends only on n mod M_k.

---

### `Tau.Holomorphy.chi_minus_crt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L225-L229)
**theorem
Tau.Holomorphy.chi_minus_crt
(n k : Denotation.TauIdx)
 :chi_minus_stage.c_fun (Polarity.reduce n k) k = chi_minus_stage.c_fun n k**


CRT coherence for χ₋: the C-sector output depends only on n mod M_k.

---

### `Tau.Holomorphy.StageFun.comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L235-L241)
**def
Tau.Holomorphy.StageFun.comp
(f₁ f₂ : StageFun)
 :StageFun**


Compose two stagewise functions: apply f₁ to the output of f₂.
B-sector: f₁.b(f₂.b(n, k), k) — f₁'s B acts on f₂'s B output
C-sector: f₁.c(f₂.c(n, k), k) — f₁'s C acts on f₂'s C output
This preserves sector independence (D-holomorphy).
Equations
- f₁.comp f₂ = { b_fun := fun (n k : Tau.Denotation.TauIdx) => f₁.b_fun (f₂.b_fun n k) k,
 c_fun := fun (n k : Tau.Denotation.TauIdx) => f₁.c_fun (f₂.c_fun n k) k }
Instances For

---

### `Tau.Holomorphy.GermTransformer.comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L243-L247)
**def
Tau.Holomorphy.GermTransformer.comp
(gt₁ gt₂ : GermTransformer)
 :GermTransformer**


Composition of sector functions (D-holomorphic structure).
Equations
- gt₁.comp gt₂ = { sector_fun := gt₁.sector_fun.comp gt₂.sector_fun, stage_fun := gt₁.stage_fun.comp gt₂.stage_fun,
 depth := min gt₁.depth gt₂.depth }
Instances For
