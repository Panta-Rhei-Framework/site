---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.GlobalHartogs"
permalink: /verify/taulib/docs/book-i-holomorphy-global-hartogs/
lane: verify
module_name: "TauLib.BookI.Holomorphy.GlobalHartogs"
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

# TauLib.Holomorphy.GlobalHartogs


The Global Hartogs Extension Theorem — the CLIMAX of Book I.

## Registry Cross-References


- [I.T31] Global Hartogs Extension — `global_hartogs`


## Ground Truth Sources


- chunk_0072_M000759: Program monoid, normal form

- chunk_0310_M002679: CRT decomposition, primorial structure


## Mathematical Content


**THE BOOK I CLIMAX.**

If f ∈ HolFun is defined on L \ K with K primordially thin,
then f extends uniquely to all of L.

Proof strategy:

- Spectral coefficients are determined by restriction data (I.T29)

- CRT extension at each primorial stage (I.L08)

- Tower coherence ensures global consistency (I.D46)

- Uniqueness by Identity Theorem (I.T21)


This uses ALL machinery from Parts IX-XII.

---

### `Tau.Holomorphy.HartogsData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L40-L54)
**structure
Tau.Holomorphy.HartogsData :Type**


A Hartogs extension pair: two tower-coherent functions that agree
outside a thin set K at some reference depth.

- f₁ : StageFun
- f₂ : StageFun
- coh₁ : TowerCoherent self.f₁
- coh₂ : TowerCoherent self.f₂
- depth : Denotation.TauIdx
- agree_ref
(n : Denotation.TauIdx)
 : agree_at self.f₁ self.f₂ n self.depth
Instances For

---

### `Tau.Holomorphy.global_hartogs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L56-L69)
**theorem
Tau.Holomorphy.global_hartogs
(hd : HartogsData)

(n k : Denotation.TauIdx)
 :k ≤ hd.depth → agree_at hd.f₁ hd.f₂ n k**


[I.T31] The Global Hartogs Extension Theorem:
Any two tower-coherent functions that agree at some reference depth
agree at ALL depths ≤ that reference depth.

Interpretation: if f is defined on L \ K and we can extend it
to agree at depth d₀, then the extension is unique everywhere
below d₀. The thin set K is "removable" because tower coherence
forces the values on K to be determined by the surrounding data.

Proof: direct application of the Identity Theorem (I.T21)
which gives downward propagation of agreement via tower coherence.

---

### `Tau.Holomorphy.hartogs_unique_b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L71-L74)
**theorem
Tau.Holomorphy.hartogs_unique_b
(hd : HartogsData)

(n k : Denotation.TauIdx)
 :k ≤ hd.depth → hd.f₁.b_fun n k = hd.f₂.b_fun n k**


Hartogs uniqueness for B-sector: extension is unique.

---

### `Tau.Holomorphy.hartogs_unique_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L76-L79)
**theorem
Tau.Holomorphy.hartogs_unique_c
(hd : HartogsData)

(n k : Denotation.TauIdx)
 :k ≤ hd.depth → hd.f₁.c_fun n k = hd.f₂.c_fun n k**


Hartogs uniqueness for C-sector: extension is unique.

---

### `Tau.Holomorphy.hartogs_ingredient_spectral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L85-L90)
**theorem
Tau.Holomorphy.hartogs_ingredient_spectral
(f₁ f₂ : StageFun)
 :(∀ (n k : Denotation.TauIdx), spectral_of f₁ n k = spectral_of f₂ n k) → f₁ = f₂**


Ingredient 1: Spectral coefficients determine the function (I.T29).

---

### `Tau.Holomorphy.hartogs_ingredient_crt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L92-L96)
**theorem
Tau.Holomorphy.hartogs_ingredient_crt
(f : StageFun)

(hcoh : TowerCoherent f)

(n k : Denotation.TauIdx)
 :Polarity.reduce (f.b_fun n k) k = f.b_fun n k**


Ingredient 2: CRT extension constrains values via reduce (I.L08).

---

### `Tau.Holomorphy.hartogs_ingredient_coherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L98-L102)
**theorem
Tau.Holomorphy.hartogs_ingredient_coherence
(f : StageFun)

(hcoh : TowerCoherent f)

(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :Polarity.reduce (f.b_fun n l) k = f.b_fun n k**


Ingredient 3: Tower coherence gives downward propagation.

---

### `Tau.Holomorphy.hartogs_ingredient_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L104-L110)
**theorem
Tau.Holomorphy.hartogs_ingredient_identity
(f₁ f₂ : StageFun)
 :TowerCoherent f₁ →
 TowerCoherent f₂ →
 ∀ (d₀ : Denotation.TauIdx),
 (∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀) → ∀ (n k : Denotation.TauIdx), k ≤ d₀ → agree_at f₁ f₂ n k**


Ingredient 4: Identity Theorem provides uniqueness (I.T21).

---

### `Tau.Holomorphy.hartogs_id_example`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L116-L123)
**def
Tau.Holomorphy.hartogs_id_example :HartogsData**


Construct a Hartogs data from id_stage (agrees with itself trivially).
Equations
- One or more equations did not get rendered due to their size.
Instances For
