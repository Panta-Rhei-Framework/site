---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.Thinness"
permalink: /verify/taulib/docs/book-i-holomorphy-thinness/
lane: verify
module_name: "TauLib.BookI.Holomorphy.Thinness"
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

# TauLib.Holomorphy.Thinness


Primorial thinness and the removable singularity criterion.

## Registry Cross-References


- [I.D67] Primorial Thinness — `PrimoriallyThin`

- [I.T30] Removable Singularity — `removable_singularity`

- [I.L08] CRT Extension — `crt_extension_b`


## Mathematical Content


A subset K ⊂ L is primordially thin if at each primorial stage k,
K misses at least 2 independent CRT directions.
This is the τ-analog of classical "codimension ≥ 2".

The Removable Singularity Theorem: if two tower-coherent functions
agree outside a finite set, and we know they agree at one common depth,
then they agree everywhere (via the Identity Theorem).

---

### `Tau.Holomorphy.count_in_K`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L33-L35)
**def
Tau.Holomorphy.count_in_K
(inK : Denotation.TauIdx → Bool)

(k : Denotation.TauIdx)
 :Denotation.TauIdx**


Count how many of the first k indices are in K.
Equations
- Tau.Holomorphy.count_in_K inK k = List.countP (fun (i : Tau.Denotation.TauIdx) => inK i) (List.range k)
Instances For

---

### `Tau.Holomorphy.PrimoriallyThin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L37-L41)
**def
Tau.Holomorphy.PrimoriallyThin
(inK : Denotation.TauIdx → Bool)

(k : Denotation.TauIdx)
 :Prop**


[I.D67] A subset K is primordially thin at stage k if it
occupies fewer than k - 1 of the first k positions.
This leaves ≥ 2 "free" CRT directions.
Equations
- Tau.Holomorphy.PrimoriallyThin inK k = (k ≥ 2 ∧ Tau.Holomorphy.count_in_K inK k + 2 ≤ k)
Instances For

---

### `Tau.Holomorphy.primordially_thin_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L43-L45)
**def
Tau.Holomorphy.primordially_thin_check
(inK : Denotation.TauIdx → Bool)

(k : Denotation.TauIdx)
 :Bool**


Boolean check for primorial thinness.
Equations
- Tau.Holomorphy.primordially_thin_check inK k = (decide (k ≥ 2) && decide (Tau.Holomorphy.count_in_K inK k + 2 ≤ k))
Instances For

---

### `Tau.Holomorphy.GloballyThin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L47-L49)
**def
Tau.Holomorphy.GloballyThin
(inK : Denotation.TauIdx → Bool)
 :Prop**


A subset K is globally thin if it is thin at all sufficiently large stages.
Equations
- Tau.Holomorphy.GloballyThin inK = ∃ (k₀ : Tau.Denotation.TauIdx), ∀ (k : Tau.Denotation.TauIdx), k ≥ k₀ → Tau.Holomorphy.PrimoriallyThin inK k
Instances For

---

### `Tau.Holomorphy.count_empty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L51-L53)
**theorem
Tau.Holomorphy.count_empty
(k : Denotation.TauIdx)
 :count_in_K (fun (x : Denotation.TauIdx) => false) k = 0**


Empty set has 0 occupied directions.

---

### `Tau.Holomorphy.empty_thin_at`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L55-L60)
**theorem
Tau.Holomorphy.empty_thin_at
(k : Denotation.TauIdx)

(hk : k ≥ 2)
 :PrimoriallyThin (fun (x : Denotation.TauIdx) => false) k**


The empty set is thin at every stage ≥ 2.

---

### `Tau.Holomorphy.empty_globally_thin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L62-L64)
**theorem
Tau.Holomorphy.empty_globally_thin :GloballyThin fun (x : Denotation.TauIdx) => false**


The empty set is globally thin.

---

### `Tau.Holomorphy.crt_extension_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L82-L90)
**theorem
Tau.Holomorphy.crt_extension_b
(f : StageFun)

(hcoh : TowerCoherent f)

(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :Polarity.reduce (f.b_fun n l) k = f.b_fun n k**


[I.L08] CRT Extension: tower coherence constrains function output
via the reduce map. The output at stage k is always reduced mod
primorial k — this is the vertical consistency that enables extension.

For the B-sector: reduce(f.b_fun(n, l), k) = f.b_fun(n, k) for k ≤ l.

---

### `Tau.Holomorphy.crt_extension_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L92-L96)
**theorem
Tau.Holomorphy.crt_extension_c
(f : StageFun)

(hcoh : TowerCoherent f)

(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :Polarity.reduce (f.c_fun n l) k = f.c_fun n k**


CRT extension for C-sector.

---

### `Tau.Holomorphy.output_reduced`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L98-L102)
**theorem
Tau.Holomorphy.output_reduced
(f : StageFun)

(hcoh : TowerCoherent f)

(n k : Denotation.TauIdx)
 :Polarity.reduce (f.b_fun n k) k = f.b_fun n k**


Self-consistency: output at stage k is already reduced.

---

### `Tau.Holomorphy.removable_singularity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L108-L119)
**theorem
Tau.Holomorphy.removable_singularity
(f₁ f₂ : StageFun)

(hcoh1 : TowerCoherent f₁)

(hcoh2 : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hagree : ∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at f₁ f₂ n k**


[I.T30] Removable Singularity: if two tower-coherent functions
agree at depth d₀ for all inputs, they agree at all depths ≤ d₀.

This is a repackaging of the Identity Theorem (I.T21)
in the language of extensions. The "removable singularity" interpretation:
knowing f on a dense set of inputs at stage d₀ determines f everywhere
(because reduced inputs form a finite set at each stage).

---

### `Tau.Holomorphy.extension_from_restriction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/Thinness.lean#L121-L128)
**theorem
Tau.Holomorphy.extension_from_restriction
(f₁ f₂ : StageFun)

(hcoh1 : TowerCoherent f₁)

(hcoh2 : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hagree_d0 : ∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → f₁.b_fun n k = f₂.b_fun n k**


Extension from restriction: if f₁ restricted to inputs NOT in K
equals f₂ restricted to inputs NOT in K, and both are tower-coherent
with agreement at some depth, then they agree everywhere.
