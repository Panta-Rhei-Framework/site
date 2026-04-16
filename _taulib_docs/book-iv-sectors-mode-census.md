---
layout: taulib-doc
title: "TauLib.BookIV.Sectors.ModeCensus"
permalink: /verify/taulib/docs/book-iv-sectors-mode-census/
lane: verify
module_name: "TauLib.BookIV.Sectors.ModeCensus"
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

# TauLib.BookIV.Sectors.ModeCensus


Boundary mode census on L = S¹ ∨ S¹: the 11/15 charge fraction.

## Registry Cross-References


- [IV.D49] Boundary Mode Census — `BoundaryMode`, `emActive`, `allModes`

- [IV.T16] Active/Silent Census — `active_count`, `silent_count`

- [IV.P08] 11/15 Charge Fraction — `active_count`


## Mathematical Content


On the lemniscate boundary L = S¹ ∨ S¹, each of the 5 generators
{α, π, γ, η, ω} contributes 3 boundary modes (Lobe₊, Lobe₋, Crossing),
giving 15 total modes. The EM-activity census classifies each mode as
either electromagnetically active (nonzero U(1) holonomy) or EM-silent.

**Census result (bipolar):**


Generator
Sector
Lobe₊
Lobe₋
Crossing
Active


γ (EM)
B
yes
yes
yes
3


π (Weak)
A
yes
yes
no
2


η (Strong)
C
yes
yes
yes
3


α (Grav)
D
no
no
no
0


ω (Higgs)
B∩C
yes
yes
yes
3


**Total**
**11**


The 4 silent modes: 3 gravitational (α×{Lobe₊,Lobe₋,Crossing}) +
1 weak neutral (π×Crossing = Z⁰ channel).

## Ground Truth Sources


- open_questions_sprint.md Part B: bipolar census

- physics_layer_sector_instantiation.md §4: generator-sector mapping


---

### `Tau.BookIV.Sectors.ModeCensus.Gen5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L44-L51)
**inductive
Tau.BookIV.Sectors.ModeCensus.Gen5 :Type**


The 5 generators of Category τ (local copy for census).

- alpha : Gen5
- pi_ : Gen5
- gamma : Gen5
- eta : Gen5
- omega : Gen5
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instReprGen5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L51-L51)
**instance
Tau.BookIV.Sectors.ModeCensus.instReprGen5 :Repr Gen5**

Equations
- Tau.BookIV.Sectors.ModeCensus.instReprGen5 = { reprPrec := Tau.BookIV.Sectors.ModeCensus.instReprGen5.repr }

---

### `Tau.BookIV.Sectors.ModeCensus.instReprGen5.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L51-L51)
**def
Tau.BookIV.Sectors.ModeCensus.instReprGen5.repr :Gen5 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instDecidableEqGen5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L51-L51)
**instance
Tau.BookIV.Sectors.ModeCensus.instDecidableEqGen5 :DecidableEq Gen5**

Equations
- Tau.BookIV.Sectors.ModeCensus.instDecidableEqGen5 x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Sectors.ModeCensus.instBEqGen5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L51-L51)
**instance
Tau.BookIV.Sectors.ModeCensus.instBEqGen5 :BEq Gen5**

Equations
- Tau.BookIV.Sectors.ModeCensus.instBEqGen5 = { beq := Tau.BookIV.Sectors.ModeCensus.instBEqGen5.beq }

---

### `Tau.BookIV.Sectors.ModeCensus.instBEqGen5.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L51-L51)
**def
Tau.BookIV.Sectors.ModeCensus.instBEqGen5.beq :Gen5 → Gen5 → Bool**

Equations
- Tau.BookIV.Sectors.ModeCensus.instBEqGen5.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.LobeConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L53-L58)
**inductive
Tau.BookIV.Sectors.ModeCensus.LobeConfig :Type**


Lobe configuration on L = S¹ ∨ S¹.

- lobePos : LobeConfig
- lobeNeg : LobeConfig
- crossing : LobeConfig
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instReprLobeConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L58-L58)
**instance
Tau.BookIV.Sectors.ModeCensus.instReprLobeConfig :Repr LobeConfig**

Equations
- Tau.BookIV.Sectors.ModeCensus.instReprLobeConfig = { reprPrec := Tau.BookIV.Sectors.ModeCensus.instReprLobeConfig.repr }

---

### `Tau.BookIV.Sectors.ModeCensus.instReprLobeConfig.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L58-L58)
**def
Tau.BookIV.Sectors.ModeCensus.instReprLobeConfig.repr :LobeConfig → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instDecidableEqLobeConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L58-L58)
**instance
Tau.BookIV.Sectors.ModeCensus.instDecidableEqLobeConfig :DecidableEq LobeConfig**

Equations
- Tau.BookIV.Sectors.ModeCensus.instDecidableEqLobeConfig x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L58-L58)
**def
Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig.beq :LobeConfig → LobeConfig → Bool**

Equations
- Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L58-L58)
**instance
Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig :BEq LobeConfig**

Equations
- Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig = { beq := Tau.BookIV.Sectors.ModeCensus.instBEqLobeConfig.beq }

---

### `Tau.BookIV.Sectors.ModeCensus.BoundaryMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L60-L65)
**structure
Tau.BookIV.Sectors.ModeCensus.BoundaryMode :Type**


[IV.D49] A boundary mode is a (generator, lobe configuration) pair.
There are 5 × 3 = 15 such modes.

- gen : Gen5
- config : LobeConfig
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instReprBoundaryMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L65-L65)
**instance
Tau.BookIV.Sectors.ModeCensus.instReprBoundaryMode :Repr BoundaryMode**

Equations
- Tau.BookIV.Sectors.ModeCensus.instReprBoundaryMode = { reprPrec := Tau.BookIV.Sectors.ModeCensus.instReprBoundaryMode.repr }

---

### `Tau.BookIV.Sectors.ModeCensus.instReprBoundaryMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L65-L65)
**def
Tau.BookIV.Sectors.ModeCensus.instReprBoundaryMode.repr :BoundaryMode → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instDecidableEqBoundaryMode.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L65-L65)
**def
Tau.BookIV.Sectors.ModeCensus.instDecidableEqBoundaryMode.decEq
(x✝ x✝¹ : BoundaryMode)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.instDecidableEqBoundaryMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L65-L65)
**instance
Tau.BookIV.Sectors.ModeCensus.instDecidableEqBoundaryMode :DecidableEq BoundaryMode**

Equations
- Tau.BookIV.Sectors.ModeCensus.instDecidableEqBoundaryMode = Tau.BookIV.Sectors.ModeCensus.instDecidableEqBoundaryMode.decEq

---

### `Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L65-L65)
**instance
Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode :BEq BoundaryMode**

Equations
- Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode = { beq := Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode.beq }

---

### `Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L65-L65)
**def
Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode.beq :BoundaryMode → BoundaryMode → Bool**

Equations
- Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode.beq { gen := a, config := a_1 } { gen := b, config := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIV.Sectors.ModeCensus.instBEqBoundaryMode.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.BoundaryMode.emActive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L71-L86)
**def
Tau.BookIV.Sectors.ModeCensus.BoundaryMode.emActive :BoundaryMode → Bool**


EM-activity: whether a boundary mode carries nonzero U(1) holonomy.

Bipolar census from the Open Questions Sprint:


- γ (EM): always active (γ IS the EM generator)

- π (Weak): Lobe₊ = W⁺ (active), Lobe₋ = W⁻ (active), Crossing = Z⁰ (silent)

- η (Strong): always active (quarks carry fractional EM charge)

- α (Gravity): always silent (gravity is EM-neutral)

- ω (Higgs): always active (Higgs couples to EM charge)

Equations
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.gamma, config := config }.emActive = true
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.pi_, config := Tau.BookIV.Sectors.ModeCensus.LobeConfig.lobePos }.emActive = true
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.pi_, config := Tau.BookIV.Sectors.ModeCensus.LobeConfig.lobeNeg }.emActive = true
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.pi_,
 config := Tau.BookIV.Sectors.ModeCensus.LobeConfig.crossing }.emActive = false
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.eta, config := config }.emActive = true
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.alpha, config := config }.emActive = false
- { gen := Tau.BookIV.Sectors.ModeCensus.Gen5.omega, config := config }.emActive = true
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.allModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L92-L98)
**def
Tau.BookIV.Sectors.ModeCensus.allModes :List BoundaryMode**


[IV.D49] All 15 boundary modes, listed explicitly.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.activeModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L100-L101)
**def
Tau.BookIV.Sectors.ModeCensus.activeModes :List BoundaryMode**


Active modes (EM-active).
Equations
- Tau.BookIV.Sectors.ModeCensus.activeModes = List.filter Tau.BookIV.Sectors.ModeCensus.BoundaryMode.emActive Tau.BookIV.Sectors.ModeCensus.allModes
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.silentModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L103-L104)
**def
Tau.BookIV.Sectors.ModeCensus.silentModes :List BoundaryMode**


Silent modes (EM-silent).
Equations
- Tau.BookIV.Sectors.ModeCensus.silentModes = List.filter (fun (m : Tau.BookIV.Sectors.ModeCensus.BoundaryMode) => !m.emActive)
 Tau.BookIV.Sectors.ModeCensus.allModes
Instances For

---

### `Tau.BookIV.Sectors.ModeCensus.mode_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L110-L111)
**theorem
Tau.BookIV.Sectors.ModeCensus.mode_total :allModes.length = 15**


[IV.T16] Total number of boundary modes = 15.

---

### `Tau.BookIV.Sectors.ModeCensus.active_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L113-L114)
**theorem
Tau.BookIV.Sectors.ModeCensus.active_count :activeModes.length = 11**


[IV.T16] Number of EM-active modes = 11.

---

### `Tau.BookIV.Sectors.ModeCensus.silent_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L116-L117)
**theorem
Tau.BookIV.Sectors.ModeCensus.silent_count :silentModes.length = 4**


[IV.T16] Number of EM-silent modes = 4.

---

### `Tau.BookIV.Sectors.ModeCensus.active_plus_silent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L119-L121)
**theorem
Tau.BookIV.Sectors.ModeCensus.active_plus_silent :activeModes.length + silentModes.length = allModes.length**


Active + silent = total (consistency).

---

### `Tau.BookIV.Sectors.ModeCensus.charge_fraction_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L127-L129)
**theorem
Tau.BookIV.Sectors.ModeCensus.charge_fraction_square :11 * 11 = 121 ∧ 15 * 15 = 225**


[IV.P08] The charge fraction 11/15 satisfies (11/15)² = 121/225.
This is the coefficient in the tower formula α = (121/225)·ι<sub>τ</sub>⁴.

---

### `Tau.BookIV.Sectors.ModeCensus.silent_modes_are_gravity_plus_Z0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L131-L137)
**theorem
Tau.BookIV.Sectors.ModeCensus.silent_modes_are_gravity_plus_Z0 :{ gen := Gen5.alpha, config := LobeConfig.lobePos }.emActive = false ∧ { gen := Gen5.alpha, config := LobeConfig.lobeNeg }.emActive = false ∧ { gen := Gen5.alpha, config := LobeConfig.crossing }.emActive = false ∧ { gen := Gen5.pi_, config := LobeConfig.crossing }.emActive = false**


The 4 silent modes are exactly: α×3 configs + π×crossing.

---

### `Tau.BookIV.Sectors.ModeCensus.euler_sieve_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L143-L146)
**theorem
Tau.BookIV.Sectors.ModeCensus.euler_sieve_identity :2 * 4 * 121 * 225 = 3 * 5 * 120 * 121**


The Euler sieve identity: (1−1/3)·(1−1/5)·(1+1/120) = (11/15)².
Cross-multiplied: 2 · 4 · 121 · 225 = 3 · 5 · 120 · 121.

---

### `Tau.BookIV.Sectors.ModeCensus.s5_correction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L148-L149)
**theorem
Tau.BookIV.Sectors.ModeCensus.s5_correction :121 = 120 + 1 ∧ 120 = 1 * 2 * 3 * 4 * 5**


The S₅ correction factor is 121/120 = 1 + 1/5!.

---

### `Tau.BookIV.Sectors.ModeCensus.mode_product`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/ModeCensus.lean#L151-L152)
**theorem
Tau.BookIV.Sectors.ModeCensus.mode_product :5 * 3 = 15**


Total modes = 5 × 3 = 15.
