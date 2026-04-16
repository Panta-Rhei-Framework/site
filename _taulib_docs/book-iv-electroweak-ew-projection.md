---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.EWProjection"
permalink: /verify/taulib/docs/book-iv-electroweak-ew-projection/
lane: verify
module_name: "TauLib.BookIV.Electroweak.EWProjection"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Electroweak.EWProjection


Structural derivation of 5/7 as an EW projection density on A_spec(L),
resolving the spectral origin of the NLO Weinberg coefficient.

## Registry Cross-References


- [IV.D335] EW-Active Mode — `isEWActive`

- [IV.D336] EW 3-Way Partition — `ewActiveModes`, `strongModes`, `ewComplement`

- [IV.T136] EW Partition Theorem — `mode_partition_EW`

- [IV.T137] EW Density = 5/7 — `ew_density_is_5_over_7`

- [IV.T138] EW–CF Bridge — `ew_density_equals_window_ratio`

- [IV.P182] Complement Characterization — `ew_complement_characterization`

- [IV.R392] OQ-B2 Status — RESOLVED (τ-EFFECTIVE)


## Mathematical Content


The 15 boundary modes on A_spec(L) admit a structural 3-way partition
under EW mixing compatibility:


Subspace
Modes
Count
Rule


V_EW
γ×{all 3} + π×{Lobe+, Lobe-}
**5**
B-sector ∪ A-sector charged


V_strong
η×{all 3}
**3**
C-sector (χ₋-dominant fiber)


V_complement
α×{all 3} + π×Crossing + ω×3
**7**
gravity + Z⁰ + Higgs


**Result:** 5/7 = dim(V_EW) / dim(V_complement).

This is the EW analogue of the OQ.11/OQ-A1 resolution:


- OQ.11: 11/15 = EM-active / total → α = (11/15)²·ι<sub>τ</sub>⁴

- OQ-B2: 5/7 = EW-active / complement → NLO coefficient


The derivation uses only carrier type (Base/Fiber from τ³ = τ¹ ×_f T²),
sector assignment (5 generators → 5 sectors), and EW mixing compatibility
(B-sector + A-sector charged). No SM gauge groups or coupling constants.

## Ground Truth Sources


- OQ-B2 (06_open_questions.md): NLO coefficient 5/7

- BoundaryFiltration.lean: carrier + polarity structural rules

- WeinbergNLO.lean: CF window algebra for 5/7


---

### `Tau.BookIV.Electroweak.EWProjection.isEWActive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L59-L70)
**def
Tau.BookIV.Electroweak.EWProjection.isEWActive :Sectors.ModeCensus.BoundaryMode → Bool**


[IV.D335] EW-active: a boundary mode participates in electroweak mixing.

**Rule:** B-sector (γ, all configs) + A-sector charged (π, lobe configs).
Uses sector assignment and polarity, not SM physics.


- B-sector (EM): always EW-active (EM IS electroweak)

- A-sector (Weak): lobes = W± (charged, EW-active), crossing = Z⁰ (neutral, not EW-active)

- All others: not EW-active (strong, gravity, Higgs)

Equations
- Tau.BookIV.Electroweak.EWProjection.isEWActive { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.gamma, config := config } = true
- Tau.BookIV.Electroweak.EWProjection.isEWActive
 { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.pi_, config := Tau.BookIV.Sectors.ModeCensus.LobeConfig.lobePos } = true
- Tau.BookIV.Electroweak.EWProjection.isEWActive
 { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.pi_, config := Tau.BookIV.Sectors.ModeCensus.LobeConfig.lobeNeg } = true
- Tau.BookIV.Electroweak.EWProjection.isEWActive x✝ = false
Instances For

---

### `Tau.BookIV.Electroweak.EWProjection.isStrong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L72-L75)
**def
Tau.BookIV.Electroweak.EWProjection.isStrong :Sectors.ModeCensus.BoundaryMode → Bool**


Strong-sector predicate: η × {all 3 configs}.
Equations
- Tau.BookIV.Electroweak.EWProjection.isStrong { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.eta, config := config } = true
- Tau.BookIV.Electroweak.EWProjection.isStrong x✝ = false
Instances For

---

### `Tau.BookIV.Electroweak.EWProjection.isEWComplement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L77-L79)
**def
Tau.BookIV.Electroweak.EWProjection.isEWComplement
(m : Sectors.ModeCensus.BoundaryMode)
 :Bool**


EW complement: modes outside both EW-active and strong.
Equations
- Tau.BookIV.Electroweak.EWProjection.isEWComplement m = (!Tau.BookIV.Electroweak.EWProjection.isEWActive m && !Tau.BookIV.Electroweak.EWProjection.isStrong m)
Instances For

---

### `Tau.BookIV.Electroweak.EWProjection.ewActiveModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L85-L87)
**def
Tau.BookIV.Electroweak.EWProjection.ewActiveModes :List Sectors.ModeCensus.BoundaryMode**


[IV.D336] EW-active modes on A_spec(L).
Equations
- Tau.BookIV.Electroweak.EWProjection.ewActiveModes = List.filter Tau.BookIV.Electroweak.EWProjection.isEWActive Tau.BookIV.Sectors.ModeCensus.allModes
Instances For

---

### `Tau.BookIV.Electroweak.EWProjection.strongModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L89-L91)
**def
Tau.BookIV.Electroweak.EWProjection.strongModes :List Sectors.ModeCensus.BoundaryMode**


Strong modes on A_spec(L).
Equations
- Tau.BookIV.Electroweak.EWProjection.strongModes = List.filter Tau.BookIV.Electroweak.EWProjection.isStrong Tau.BookIV.Sectors.ModeCensus.allModes
Instances For

---

### `Tau.BookIV.Electroweak.EWProjection.ewComplement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L93-L95)
**def
Tau.BookIV.Electroweak.EWProjection.ewComplement :List Sectors.ModeCensus.BoundaryMode**


EW complement modes on A_spec(L).
Equations
- Tau.BookIV.Electroweak.EWProjection.ewComplement = List.filter Tau.BookIV.Electroweak.EWProjection.isEWComplement Tau.BookIV.Sectors.ModeCensus.allModes
Instances For

---

### `Tau.BookIV.Electroweak.EWProjection.ew_active_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L101-L102)
**theorem
Tau.BookIV.Electroweak.EWProjection.ew_active_count :ewActiveModes.length = 5**


EW-active count = 5 (γ×3 + π×{Lobe+, Lobe-}).

---

### `Tau.BookIV.Electroweak.EWProjection.strong_mode_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L104-L105)
**theorem
Tau.BookIV.Electroweak.EWProjection.strong_mode_count :strongModes.length = 3**


Strong count = 3 (η×3).

---

### `Tau.BookIV.Electroweak.EWProjection.ew_complement_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L107-L108)
**theorem
Tau.BookIV.Electroweak.EWProjection.ew_complement_count :ewComplement.length = 7**


EW complement count = 7 (α×3 + Z⁰ + ω×3).

---

### `Tau.BookIV.Electroweak.EWProjection.mode_partition_EW`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L114-L116)
**theorem
Tau.BookIV.Electroweak.EWProjection.mode_partition_EW :5 + 3 + 7 = 15**


[IV.T136] The 15 boundary modes partition into 5 + 3 + 7.
This is a structural partition: EW-active ⊔ strong ⊔ complement = all.

---

### `Tau.BookIV.Electroweak.EWProjection.partition_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L118-L121)
**theorem
Tau.BookIV.Electroweak.EWProjection.partition_consistent :ewActiveModes.length + strongModes.length + ewComplement.length = Sectors.ModeCensus.allModes.length**


Census consistency: partition sums to total.

---

### `Tau.BookIV.Electroweak.EWProjection.partition_disjoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L123-L128)
**theorem
Tau.BookIV.Electroweak.EWProjection.partition_disjoint :(List.filter (fun (m : Sectors.ModeCensus.BoundaryMode) => isEWActive m && isStrong m)
 Sectors.ModeCensus.allModes).length = 0 ∧ (List.filter (fun (m : Sectors.ModeCensus.BoundaryMode) => isEWActive m && isEWComplement m)
 Sectors.ModeCensus.allModes).length = 0 ∧ (List.filter (fun (m : Sectors.ModeCensus.BoundaryMode) => isStrong m && isEWComplement m)
 Sectors.ModeCensus.allModes).length = 0**


The partition is disjoint: no mode is in two subsets.

---

### `Tau.BookIV.Electroweak.EWProjection.ew_density_is_5_over_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L134-L138)
**theorem
Tau.BookIV.Electroweak.EWProjection.ew_density_is_5_over_7 :ewActiveModes.length * 7 = ewComplement.length * 5**


[IV.T137] The EW projection density is 5/7.
Cross-multiplied: |V_EW| × |V_complement_den| = |V_complement| × |V_EW_num|
where both equal 35.

---

### `Tau.BookIV.Electroweak.EWProjection.ew_complement_characterization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L144-L154)
**theorem
Tau.BookIV.Electroweak.EWProjection.ew_complement_characterization :isEWComplement { gen := Sectors.ModeCensus.Gen5.alpha, config := Sectors.ModeCensus.LobeConfig.lobePos } = true ∧ isEWComplement { gen := Sectors.ModeCensus.Gen5.alpha, config := Sectors.ModeCensus.LobeConfig.lobeNeg } = true ∧ isEWComplement { gen := Sectors.ModeCensus.Gen5.alpha, config := Sectors.ModeCensus.LobeConfig.crossing } = true ∧ isEWComplement { gen := Sectors.ModeCensus.Gen5.pi_, config := Sectors.ModeCensus.LobeConfig.crossing } = true ∧ isEWComplement { gen := Sectors.ModeCensus.Gen5.omega, config := Sectors.ModeCensus.LobeConfig.lobePos } = true ∧ isEWComplement { gen := Sectors.ModeCensus.Gen5.omega, config := Sectors.ModeCensus.LobeConfig.lobeNeg } = true ∧ isEWComplement { gen := Sectors.ModeCensus.Gen5.omega, config := Sectors.ModeCensus.LobeConfig.crossing } = true**


[IV.P182] The 7 complement modes are exactly α×3 + π×crossing(Z⁰) + ω×3.
Physical interpretation: gravity (3) + neutral weak (1) + Higgs (3).

---

### `Tau.BookIV.Electroweak.EWProjection.complement_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L156-L158)
**theorem
Tau.BookIV.Electroweak.EWProjection.complement_structure :3 + 1 + 3 = 7**


The complement has exactly 3 + 1 + 3 = 7 structure:
3 gravity (α) + 1 neutral weak (Z⁰) + 3 Higgs (ω).

---

### `Tau.BookIV.Electroweak.EWProjection.ew_density_equals_window_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L164-L174)
**theorem
Tau.BookIV.Electroweak.EWProjection.ew_density_equals_window_ratio :ewActiveModes.length = CF.windowSum CF.cf_head 3 4 ∧ ewComplement.length = CF.windowSum CF.cf_head 3 3 - 2 * CF.windowSum CF.cf_head 3 4**


[IV.T138] Bridge theorem: the EW mode density equals the CF window ratio.
|V_EW| = W₃(4) = 5 and |V_complement| = W₃(3) − 2·W₃(4) = 7.
This links the structural partition to the CF algebra of ι<sub>τ</sub>.

---

### `Tau.BookIV.Electroweak.EWProjection.strong_equals_solenoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L176-L178)
**theorem
Tau.BookIV.Electroweak.EWProjection.strong_equals_solenoidal :strongModes.length = Kernel.solenoidalGenerators.length**


The strong sector count also matches: 3 = |solenoidal|.

---

### `Tau.BookIV.Electroweak.EWProjection.remark_oq_b2_resolved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWProjection.lean#L184-L197)
**def
Tau.BookIV.Electroweak.EWProjection.remark_oq_b2_resolved :String**


[IV.R392] OQ-B2 RESOLVED (τ-EFFECTIVE).

Derivation chain:

- A_spec(L) has 15 boundary modes (5 generators × 3 configs)

- EW partition: V_EW (5) + V_strong (3) + V_complement (7) = 15

- Density: 5/7 = dim(V_EW) / dim(V_complement)

- CF bridge: 5 = W₃(4), 7 = W₃(3) − 2·W₃(4) (numerical match)

- NLO: sin²θ_W = ι(1−ι) · (1 + (5/7)·ι³) at 86 ppm


Residual open: WHY does CF[ι<sub>τ</sub>] match the mode census?
(CF Compression Thesis — foundational, beyond series scope)
Equations
- Tau.BookIV.Electroweak.EWProjection.remark_oq_b2_resolved = "OQ-B2 RESOLVED: 5/7 = EW projection density on A_spec(L). " ++ "V_EW (5) / V_complement (7) from carrier + polarity + mixing rules."
Instances For
