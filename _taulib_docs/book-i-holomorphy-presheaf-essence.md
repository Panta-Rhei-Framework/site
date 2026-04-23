---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.PresheafEssence"
permalink: /verify/taulib/docs/book-i-holomorphy-presheaf-essence/
lane: verify
module_name: "TauLib.BookI.Holomorphy.PresheafEssence"
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

# TauLib.Holomorphy.PresheafEssence


The presheaf essence of τ-holomorphy: the bi-square characterization.
**The Book I crown jewel.**

## Registry Cross-References


- [I.D83] Primorial Presheaf — `PrimorialPresheaf`

- [I.T40] Presheaf Characterization — `presheaf_characterization`

- [I.T41] Bi-Square Characterization — `bi_square_characterization`


## Mathematical Content


τ-holomorphy = naturality + sector independence, encoded as a single
pasted commuting diagram — the holomorphy bi-square:

```
 ℤ/M_ℓℤ →T_ℓ→ ℤ/M_ℓℤ[j] →(χ₊,χ₋)→ ℤ/M_ℓℤ × ℤ/M_ℓℤ
 | | |
 π↓ π↓ (π,π)↓
 | | |
 ℤ/M_kℤ →T_k→ ℤ/M_kℤ[j] →(χ₊,χ₋)→ ℤ/M_kℤ × ℤ/M_kℤ
```


Left square: tower coherence. Right square: spectral naturality.
Both together characterize HolFun completely.

Key formalization insight: the right square follows AUTOMATICALLY
from the left because StageFun already separates B/C sectors.

Five generators, seven axioms, one bi-square.

---

### `Tau.Holomorphy.PrimorialPresheaf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L46-L51)
**structure
Tau.Holomorphy.PrimorialPresheaf :Type**


[I.D83] An element of the primorial presheaf lim← ℤ/M_dℤ:
a compatible family of values at each primorial depth.
Compatibility: reduce(value_at ℓ, k) = value_at k for k ≤ ℓ.

- value_at : Denotation.TauIdx → Denotation.TauIdx
- compatible
(k l : Denotation.TauIdx)
 : k ≤ l → Polarity.reduce (self.value_at l) k = self.value_at k
Instances For

---

### `Tau.Holomorphy.presheaf_of_nat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L53-L57)
**def
Tau.Holomorphy.presheaf_of_nat
(n : Denotation.TauIdx)
 :PrimorialPresheaf**


Construct a presheaf element from a natural number:
at each depth d, the value is reduce(n, d) = n mod M_d.
Equations
- Tau.Holomorphy.presheaf_of_nat n = { value_at := fun (d : Tau.Denotation.TauIdx) => Tau.Polarity.reduce n d, compatible := ⋯ }
Instances For

---

### `Tau.Holomorphy.presheaf_value_reduced`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L59-L62)
**theorem
Tau.Holomorphy.presheaf_value_reduced
(p : PrimorialPresheaf)

(d : Denotation.TauIdx)
 :Polarity.reduce (p.value_at d) d = p.value_at d**


Presheaf values are already reduced at their own depth.

---

### `Tau.Holomorphy.IsNatTrans`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L68-L70)
**def
Tau.Holomorphy.IsNatTrans
(f : StageFun)
 :Prop**


A natural transformation F → F_j in the primorial inverse system.
This IS tower coherence (I.D46), repackaged in presheaf language.
Equations
- Tau.Holomorphy.IsNatTrans f = Tau.Holomorphy.TowerCoherent f
Instances For

---

### `Tau.Holomorphy.nat_trans_iff_tower_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L72-L74)
**theorem
Tau.Holomorphy.nat_trans_iff_tower_coherent
(f : StageFun)
 :IsNatTrans f ↔ TowerCoherent f**


Presheaf naturality and tower coherence are definitionally equal.

---

### `Tau.Holomorphy.presheaf_characterization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L80-L84)
**theorem
Tau.Holomorphy.presheaf_characterization
(hf : HolFun)
 :IsNatTrans hf.transformer.stage_fun**


[I.T40] Every τ-holomorphic function is a natural transformation
of the primorial presheaf.

---

### `Tau.Holomorphy.nat_trans_gives_holfun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L86-L90)
**theorem
Tau.Holomorphy.nat_trans_gives_holfun
(sf : SectorFun)

(stf : StageFun)

(d : ℕ)

(hnt : IsNatTrans stf)
 :∃ (hf : HolFun), hf.transformer.stage_fun = stf**


Converse: a natural transformation with sector structure gives a HolFun.

---

### `Tau.Holomorphy.BiSquare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L96-L109)
**structure
Tau.Holomorphy.BiSquare :Type**


[I.T41] The holomorphy bi-square: the minimal complete
characterization of τ-holomorphic functions.

Left square: tower coherence for each sector.
The right square (spectral naturality) follows automatically
from left_b and left_c — see `right_from_left`.

- stage_fun : StageFun
- left_b
(n k l : Denotation.TauIdx)
 : k ≤ l → Polarity.reduce (self.stage_fun.b_fun n l) k = self.stage_fun.b_fun n k
LEFT SQUARE, B-sector: reduce(B_ℓ(n), k) = B_k(n).

- left_c
(n k l : Denotation.TauIdx)
 : k ≤ l → Polarity.reduce (self.stage_fun.c_fun n l) k = self.stage_fun.c_fun n k
LEFT SQUARE, C-sector: reduce(C_ℓ(n), k) = C_k(n).

Instances For

---

### `Tau.Holomorphy.BiSquare.tower_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L115-L117)
**def
Tau.Holomorphy.BiSquare.tower_coherent
(bs : BiSquare)
 :TowerCoherent bs.stage_fun**


Extract tower coherence from a BiSquare.
Equations
- ⋯ = ⋯
Instances For

---

### `Tau.Holomorphy.BiSquare.of_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L119-L121)
**def
Tau.Holomorphy.BiSquare.of_coherent
(f : StageFun)

(htc : TowerCoherent f)
 :BiSquare**


Construct a BiSquare from a tower-coherent StageFun.
Equations
- Tau.Holomorphy.BiSquare.of_coherent f htc = { stage_fun := f, left_b := ⋯, left_c := ⋯ }
Instances For

---

### `Tau.Holomorphy.bi_square_characterization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L123-L129)
**theorem
Tau.Holomorphy.bi_square_characterization
(f : StageFun)
 :TowerCoherent f ↔ (∀ (n k l : Denotation.TauIdx), k ≤ l → Polarity.reduce (f.b_fun n l) k = f.b_fun n k) ∧ ∀ (n k l : Denotation.TauIdx), k ≤ l → Polarity.reduce (f.c_fun n l) k = f.c_fun n k**


[I.T41] The bi-square characterizes τ-holomorphy completely:
TowerCoherent f ↔ both sectors of the left square commute.

---

### `Tau.Holomorphy.BiSquare.toHolFun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L131-L133)
**def
Tau.Holomorphy.BiSquare.toHolFun
(bs : BiSquare)

(sf : SectorFun)

(d : ℕ)
 :HolFun**


Bridge: BiSquare → HolFun (with a chosen SectorFun and depth).
Equations
- bs.toHolFun sf d = { transformer := { sector_fun := sf, stage_fun := bs.stage_fun, depth := d }, coherent := ⋯ }
Instances For

---

### `Tau.Holomorphy.HolFun.toBiSquare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L135-L137)
**def
Tau.Holomorphy.HolFun.toBiSquare
(hf : HolFun)
 :BiSquare**


Bridge: HolFun → BiSquare.
Equations
- hf.toBiSquare = { stage_fun := hf.transformer.stage_fun, left_b := ⋯, left_c := ⋯ }
Instances For

---

### `Tau.Holomorphy.holfun_bisquare_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L139-L141)
**theorem
Tau.Holomorphy.holfun_bisquare_roundtrip
(hf : HolFun)
 :hf.toBiSquare.stage_fun = hf.transformer.stage_fun**


Round-trip preserves the StageFun.

---

### `Tau.Holomorphy.right_from_left`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L153-L170)
**theorem
Tau.Holomorphy.right_from_left
(bs : BiSquare)

(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :spectral_of bs.stage_fun n k = { b_coeff := Polarity.reduce (spectral_of bs.stage_fun n l).b_coeff k,
 c_coeff := Polarity.reduce (spectral_of bs.stage_fun n l).c_coeff k }**


**Key insight.** The right square (spectral naturality) follows
automatically from the left square (tower coherence).

Because `spectral_of f n k = ⟨f.b_fun n k, f.c_fun n k⟩`,
spectral reduction IS sector-wise tower coherence.
The two squares are independent in the LaTeX presentation
but are the same condition in TauLib's concrete formulation.

---

### `Tau.Holomorphy.right_from_left'`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L172-L178)
**theorem
Tau.Holomorphy.right_from_left'
(f : StageFun)

(htc : TowerCoherent f)

(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :spectral_of f n k = { b_coeff := Polarity.reduce (spectral_of f n l).b_coeff k, c_coeff := Polarity.reduce (spectral_of f n l).c_coeff k }**


Right square for any tower-coherent function (not just BiSquare).

---

### `Tau.Holomorphy.limit_determines_stages`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L184-L191)
**theorem
Tau.Holomorphy.limit_determines_stages
(bs₁ bs₂ : BiSquare)

(d₀ : Denotation.TauIdx)

(h : ∀ (n : Denotation.TauIdx), agree_at bs₁.stage_fun bs₂.stage_fun n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at bs₁.stage_fun bs₂.stage_fun n k**


The limit principle: the limit row determines every stage row.
Global Hartogs (I.T31) in bi-square language.

---

### `Tau.Holomorphy.limit_determines_spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L193-L202)
**theorem
Tau.Holomorphy.limit_determines_spectral
(bs₁ bs₂ : BiSquare)

(d₀ : Denotation.TauIdx)

(h : ∀ (n : Denotation.TauIdx), spectral_of bs₁.stage_fun n d₀ = spectral_of bs₂.stage_fun n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → spectral_of bs₁.stage_fun n k = spectral_of bs₂.stage_fun n k**


Limit principle in spectral language.

---

### `Tau.Holomorphy.chi_plus_bisquare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L208-L210)
**def
Tau.Holomorphy.chi_plus_bisquare :BiSquare**


χ₊ as a bi-square.
Equations
- Tau.Holomorphy.chi_plus_bisquare = Tau.Holomorphy.BiSquare.of_coherent Tau.Holomorphy.chi_plus_stage Tau.Holomorphy.chi_plus_coherent
Instances For

---

### `Tau.Holomorphy.chi_minus_bisquare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L212-L214)
**def
Tau.Holomorphy.chi_minus_bisquare :BiSquare**


χ₋ as a bi-square.
Equations
- Tau.Holomorphy.chi_minus_bisquare = Tau.Holomorphy.BiSquare.of_coherent Tau.Holomorphy.chi_minus_stage Tau.Holomorphy.chi_minus_coherent
Instances For

---

### `Tau.Holomorphy.id_bisquare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L216-L218)
**def
Tau.Holomorphy.id_bisquare :BiSquare**


The identity as a bi-square.
Equations
- Tau.Holomorphy.id_bisquare = Tau.Holomorphy.BiSquare.of_coherent Tau.Holomorphy.id_stage Tau.Holomorphy.id_coherent
Instances For

---

### `Tau.Holomorphy.chi_plus_right_square`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L220-L225)
**theorem
Tau.Holomorphy.chi_plus_right_square
(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :spectral_of chi_plus_stage n k = { b_coeff := Polarity.reduce (spectral_of chi_plus_stage n l).b_coeff k,
 c_coeff := Polarity.reduce (spectral_of chi_plus_stage n l).c_coeff k }**


Right square verified for χ₊.

---

### `Tau.Holomorphy.BookICrownJewel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L231-L252)
**structure
Tau.Holomorphy.BookICrownJewel :Prop**


The Book I crown jewel: five generators, seven axioms, one bi-square.
Bundles all structural theorems earned across 19 Parts into
one record that Book II receives.

- presheaf_char
(f : StageFun)
 : TowerCoherent f → IsNatTrans f
[I.T40] Presheaf characterization: HolFun → IsNatTrans.

- bi_square_char
(f : StageFun)
 : TowerCoherent f ↔ (∀ (n k l : Denotation.TauIdx), k ≤ l → Polarity.reduce (f.b_fun n l) k = f.b_fun n k) ∧ ∀ (n k l : Denotation.TauIdx), k ≤ l → Polarity.reduce (f.c_fun n l) k = f.c_fun n k
[I.T41] Bi-square characterization: TowerCoherent ↔ both squares.

- limit_principle
(f₁ f₂ : StageFun)
 : TowerCoherent f₁ →
 TowerCoherent f₂ →
 ∀ (d₀ : Denotation.TauIdx),
 (∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀) → ∀ (n k : Denotation.TauIdx), k ≤ d₀ → agree_at f₁ f₂ n k
[I.T31] The limit principle: agreement at d₀ implies agreement below.

- right_automatic
(f : StageFun)
 : TowerCoherent f →
 ∀ (n k l : Denotation.TauIdx),
 k ≤ l →
 spectral_of f n k = { b_coeff := Polarity.reduce (spectral_of f n l).b_coeff k,
 c_coeff := Polarity.reduce (spectral_of f n l).c_coeff k }
Right square follows from left (structural automaticity).

Instances For

---

### `Tau.Holomorphy.book_i_crown_jewel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/PresheafEssence.lean#L254-L260)
**def
Tau.Holomorphy.book_i_crown_jewel :BookICrownJewel**


The canonical Book I crown jewel.
Five generators, seven axioms, one bi-square.
Equations
- Tau.Holomorphy.book_i_crown_jewel = ⋯
Instances For
