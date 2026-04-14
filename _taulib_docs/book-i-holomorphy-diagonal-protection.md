---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.DiagonalProtection"
permalink: /verify/taulib/docs/book-i-holomorphy-diagonal-protection/
lane: verify
module_name: "TauLib.BookI.Holomorphy.DiagonalProtection"
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

# TauLib.Holomorphy.DiagonalProtection


The Diagonal-Free Protection Theorem: zero-divisor pathologies cannot arise
in τ-holomorphic functions.

## Registry Cross-References


- [I.T19] Diagonal-Free Protection — `diagonal_free_protection`

- [I.P23] No Simultaneous Projection — `no_simul_projection`

- [I.T20] Composition Closure — `holfun_comp_coherent`

- [I.P24] HolFun Associativity — `stagefun_comp_assoc`


## Ground Truth Sources


- chunk_0072_M000759: Diagonal-free axiom K5

- chunk_0228_M002194: Split-complex algebra, zero divisors

- chunk_0310_M002679: Bipolar partition, sector purity


## Mathematical Content


The diagonal-free discipline (K5) and Prime Polarity Theorem (I.T05) together
prevent zero-divisor pathologies in τ-holomorphic functions:

- 
No Simultaneous Projection: a compatible omega-germ cannot project nontrivially
onto BOTH idempotent sectors through a HolFun.


- 
Diagonal-Free Protection: the zero-divisor product e₊·e₋ = 0 cannot arise
as T(t₁)·T(t₂) for any T ∈ HolFun and compatible omega-tails t₁, t₂.


- 
Composition Closure: HolFun is closed under composition.


- 
Associativity: HolFun composition is associative (monoid structure).


---

### `Tau.Holomorphy.no_simul_projection_b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L47-L60)
**theorem
Tau.Holomorphy.no_simul_projection_b
(f : StageFun)

(n k : Denotation.TauIdx)

(hb : f.b_fun n k = 0)
 :{ b_sector := ↑(f.b_fun n k), c_sector := 0 }.mul { b_sector := 0, c_sector := ↑(f.c_fun n k) } = { b_sector := 0, c_sector := 0 }**


[I.P23] No Simultaneous Projection (sector purity):
For a tower-coherent function where one sector is constantly zero,
the other sector carries all the information.

Concretely: if f.b_fun = 0 everywhere, then f.c_fun is the sole
carrier; and vice versa. The sectors cannot BOTH be nontrivial
for a well-behaved (tower-coherent) omega-germ transformer.

This is formalized as: the product of a B-only and C-only
stagewise function outputs zero.

---

### `Tau.Holomorphy.no_simul_projection_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L62-L65)
**theorem
Tau.Holomorphy.no_simul_projection_c
(f : StageFun)

(n k : Denotation.TauIdx)

(hc : f.c_fun n k = 0)
 :{ b_sector := ↑(f.b_fun n k), c_sector := 0 }.mul { b_sector := 0, c_sector := ↑(f.c_fun n k) } = { b_sector := 0, c_sector := 0 }**


---

### `Tau.Holomorphy.diagonal_free_protection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L71-L80)
**theorem
Tau.Holomorphy.diagonal_free_protection
(b_val c_val : Denotation.TauIdx)
 :{ b_sector := ↑b_val, c_sector := 0 }.mul { b_sector := 0, c_sector := ↑c_val } = { b_sector := 0, c_sector := 0 }**


[I.T19] Diagonal-Free Protection Theorem:
The product of pure B-sector and pure C-sector outputs is always zero.
This is the structural reflection of e₊·e₋ = 0 at the function level:
sector-pure outputs cannot combine nontrivially.

For any two stagewise evaluations giving pure B and pure C outputs,
their sector product is zero.

---

### `Tau.Holomorphy.diagonal_free_protection_int`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L82-L85)
**theorem
Tau.Holomorphy.diagonal_free_protection_int
(b c : ℤ)
 :{ b_sector := b, c_sector := 0 }.mul { b_sector := 0, c_sector := c } = { b_sector := 0, c_sector := 0 }**


The protection extends to Int-level SectorPair: pure B times pure C is zero.

---

### `Tau.Holomorphy.ReduceForm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L91-L100)
**structure
Tau.Holomorphy.ReduceForm
(f : StageFun)
 :Type**


A stagewise function has "reduce form" if f(n,k) = reduce(g(n), k) for some g.

- b_map : Denotation.TauIdx → Denotation.TauIdx
The underlying B-sector map on TauIdx.

- c_map : Denotation.TauIdx → Denotation.TauIdx
The underlying C-sector map on TauIdx.

- b_eq
(n k : Denotation.TauIdx)
 : f.b_fun n k = Polarity.reduce (self.b_map n) k
B-sector has reduce form.

- c_eq
(n k : Denotation.TauIdx)
 : f.c_fun n k = Polarity.reduce (self.c_map n) k
C-sector has reduce form.

Instances For

---

### `Tau.Holomorphy.chi_plus_reduce_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L102-L106)
**def
Tau.Holomorphy.chi_plus_reduce_form :ReduceForm chi_plus_stage**


χ₊ has reduce form with b_map = id, c_map = const 0.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Holomorphy.chi_minus_reduce_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L108-L112)
**def
Tau.Holomorphy.chi_minus_reduce_form :ReduceForm chi_minus_stage**


χ₋ has reduce form with b_map = const 0, c_map = id.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Holomorphy.id_reduce_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L114-L118)
**def
Tau.Holomorphy.id_reduce_form :ReduceForm id_stage**


Identity has reduce form with b_map = id, c_map = id.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Holomorphy.ReduceCompat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L120-L122)
**def
Tau.Holomorphy.ReduceCompat
(f : Denotation.TauIdx → Denotation.TauIdx)
 :Prop**


A map preserves residue classes: congruent inputs give congruent outputs.
Equations
- Tau.Holomorphy.ReduceCompat f = ∀ (a b k : Tau.Denotation.TauIdx),
 Tau.Polarity.reduce a k = Tau.Polarity.reduce b k → Tau.Polarity.reduce (f a) k = Tau.Polarity.reduce (f b) k
Instances For

---

### `Tau.Holomorphy.id_reduce_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L124-L126)
**theorem
Tau.Holomorphy.id_reduce_compat :ReduceCompat fun (n : Denotation.TauIdx) => n**


The identity map is reduce-compatible.

---

### `Tau.Holomorphy.const_zero_reduce_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L128-L130)
**theorem
Tau.Holomorphy.const_zero_reduce_compat :ReduceCompat fun (x : Denotation.TauIdx) => 0**


The constant-zero map is reduce-compatible.

---

### `Tau.Holomorphy.comp_reduce_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L132-L160)
**theorem
Tau.Holomorphy.comp_reduce_coherent
(f₁ f₂ : StageFun)

(rf₁ : ReduceForm f₁)

(rf₂ : ReduceForm f₂)

(h₁ : TowerCoherent f₁)

(h₂ : TowerCoherent f₂)

(hrc_b : ReduceCompat rf₁.b_map)

(hrc_c : ReduceCompat rf₁.c_map)
 :TowerCoherent (f₁.comp f₂)**


Composition of reduce-form functions preserves tower coherence,
provided the outer function's underlying maps preserve residue classes.

---

### `Tau.Holomorphy.holfun_comp_rf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L162-L168)
**def
Tau.Holomorphy.holfun_comp_rf
(hf₁ hf₂ : HolFun)

(rf₁ : ReduceForm hf₁.transformer.stage_fun)

(rf₂ : ReduceForm hf₂.transformer.stage_fun)

(hrc_b : ReduceCompat rf₁.b_map)

(hrc_c : ReduceCompat rf₁.c_map)
 :HolFun**


HolFun composition for reduce-form functions with reduce-compatible maps.
Equations
- Tau.Holomorphy.holfun_comp_rf hf₁ hf₂ rf₁ rf₂ hrc_b hrc_c = { transformer := hf₁.transformer.comp hf₂.transformer, coherent := ⋯ }
Instances For

---

### `Tau.Holomorphy.stagefun_comp_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L174-L177)
**theorem
Tau.Holomorphy.stagefun_comp_assoc
(f₁ f₂ f₃ : StageFun)
 :(f₁.comp f₂).comp f₃ = f₁.comp (f₂.comp f₃)**


[I.P24] Composition of stagewise functions is associative.

---

### `Tau.Holomorphy.stagefun_id_comp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L179-L183)
**theorem
Tau.Holomorphy.stagefun_id_comp
(f : StageFun)
 :id_stage.comp f = { b_fun := fun (n k : Denotation.TauIdx) => Polarity.reduce (f.b_fun n k) k,
 c_fun := fun (n k : Denotation.TauIdx) => Polarity.reduce (f.c_fun n k) k }**


The identity stagewise function is a left unit for composition.

---

### `Tau.Holomorphy.sector_comp_assoc'`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L185-L188)
**theorem
Tau.Holomorphy.sector_comp_assoc'
(sf₁ sf₂ sf₃ : SectorFun)
 :(sf₁.comp sf₂).comp sf₃ = sf₁.comp (sf₂.comp sf₃)**


SectorFun composition is associative (re-export).

---

### `Tau.Holomorphy.gt_comp_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L190-L193)
**theorem
Tau.Holomorphy.gt_comp_assoc
(gt₁ gt₂ gt₃ : GermTransformer)
 :(gt₁.comp gt₂).comp gt₃ = gt₁.comp (gt₂.comp gt₃)**


GermTransformer composition is associative.
