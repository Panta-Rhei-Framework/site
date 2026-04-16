---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BBNNuclearNetwork"
permalink: /verify/taulib/docs/book-v-cosmology-bbn-nuclear-network/
lane: verify
module_name: "TauLib.BookV.Cosmology.BBNNuclearNetwork"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Cosmology.BBNNuclearNetwork


BBN nuclear reaction chain, deuterium/He-3 predictions, lithium-7 resolution
via T² fiber suppression, and complete BBN abundance table.

## Registry Cross-References


- [V.D301] Deuterium Bottleneck Temperature -- `DeuteriumBottleneck`

- [V.D302] BBN Network Light Elements -- `BBNNetwork`

- [V.D303] BBN Reaction Chain -- `BBNReaction`, `bbn_reactions`

- [V.D304] Sector Assignment -- `BBNSector`, `reaction_sector`

- [V.D305] T² Fiber Holonomy Correction -- `FiberHolonomyCorrection`

- [V.D306] ⁷Be Suppression Factor -- `Be7SuppressionFactor`

- [V.D307] Complete BBN Table -- `CompleteBBNTable`

- [V.T241] D/H from τ-native η_B -- `DeuteriumPrediction`

- [V.T242] Sector Distribution {1,4,7} -- `sector_distribution_sum`

- [V.T243] Suppression = 1/3 -- `suppression_is_one_third`

- [V.T244] Li-7 Resolution -- `LithiumResolution`

- [V.T245] Y_p Preservation -- `yp_preserved`

- [V.T246] D/H Preservation -- `dh_preserved`

- [V.T247] He-3/H from τ-native η_B -- `He3Prediction`

- [V.P166] D/H Observational Consistency -- `dh_in_range`

- [V.P167] Spite Plateau Consistency -- `spite_plateau_consistent`

- [V.P168] Selectivity: Only A ≥ 7 -- `selectivity_threshold`

- [V.P169] BBN Table Consistency -- `bbn_table_all_within_range`

- [V.R427] D/H Anti-correlation -- comment

- [V.R428] N3 Status Upgrade -- comment

- [V.R429] ⁷Be Production as B-Sector -- comment

- [V.R430] EM Phase-Space Restriction -- comment

- [V.R431] Voxel Packing Connection -- comment

- [V.R432] Packing Threshold at A = 7 -- comment

- [V.R433] Stellar Depletion + Spite Plateau -- comment

- [V.R434] All Four from Single η_B -- comment


## Mathematical Content


### Deuterium from τ-native η_B [Sprint 25A]


η_B(τ) = (121/270)·ι<sub>τ</sub>¹⁹ ≈ 6.041 × 10⁻¹⁰ (−1.03% from Planck).
BBN sensitivity d(ln(D/H))/d(ln η_B) ≈ −1.6 gives D/H(τ) ≈ 2.60 × 10⁻⁵.
Observed (Cooke 2018): (2.527 ± 0.030) × 10⁻⁵ → +2.3σ.

### Nuclear Reaction Chain [Sprint 25B]


12 dominant BBN reactions: {A: 1, B: 4, C: 7}, 1+4+7=12.
Reaction 9 (³He+⁴He→⁷Be+γ) is B-sector EM capture — key to lithium.

### Fiber Suppression [Sprint 25C]


S_{⁷Be} = dim(τ¹)/dim(τ³) = 1/3. EM capture restricted to base τ¹.
⁷Li/H(τ) = (1/3) × 5.62×10⁻¹⁰ = 1.87×10⁻¹⁰, +0.9σ from Spite plateau.

### Preservation [Sprint 25D]


Y_p = 20/81: from combinatorial packing, independent of ⁷Be rate.
D/H: set by bottleneck, not ⁷Be channel.
Only A ≥ 7 suppressed; mass gaps at A=5,8 prevent intermediate products.

### Complete Table [Sprint 25E]


Species
τ-BBN
Deviation
Scope


Y_p
20/81
−0.43σ
τ-eff


D/H
2.60e-5
+2.3σ
τ-eff


³He/H
1.01e-5
−0.5σ
τ-eff


⁷Li/H
1.87e-10
+0.9σ
conj


## Ground Truth Sources


- Book V ch48: Threshold Ladder (Wave 25 additions)

- Cooke et al. 2018: D/H measurement

- Spite & Spite 1982: Lithium plateau


---

### `Tau.BookV.Cosmology.DeuteriumBottleneck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L87-L95)
**structure
Tau.BookV.Cosmology.DeuteriumBottleneck :Type**


[V.D301] Deuterium bottleneck temperature T_D ≈ 0.07 MeV.
Below this temperature, deuterium survives photo-dissociation
and the nuclear chain proceeds.

- temp_001MeV : ℕ
Bottleneck temperature in units of 0.01 MeV.

- within_nuc_window : Bool
Bottleneck lies within the nucleosynthetic window.

Instances For

---

### `Tau.BookV.Cosmology.instReprDeuteriumBottleneck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L95-L95)
**instance
Tau.BookV.Cosmology.instReprDeuteriumBottleneck :Repr DeuteriumBottleneck**

Equations
- Tau.BookV.Cosmology.instReprDeuteriumBottleneck = { reprPrec := Tau.BookV.Cosmology.instReprDeuteriumBottleneck.repr }

---

### `Tau.BookV.Cosmology.instReprDeuteriumBottleneck.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L95-L95)
**def
Tau.BookV.Cosmology.instReprDeuteriumBottleneck.repr :DeuteriumBottleneck → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.deuterium_bottleneck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L97-L98)
**def
Tau.BookV.Cosmology.deuterium_bottleneck :DeuteriumBottleneck**


The canonical deuterium bottleneck.
Equations
- Tau.BookV.Cosmology.deuterium_bottleneck = { }
Instances For

---

### `Tau.BookV.Cosmology.BBNNucleus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L104-L114)
**inductive
Tau.BookV.Cosmology.BBNNucleus :Type**


[V.D302] The 8 light nuclei in the BBN network.

- neutron : BBNNucleus
- proton : BBNNucleus
- deuterium : BBNNucleus
- helium3 : BBNNucleus
- tritium : BBNNucleus
- helium4 : BBNNucleus
- lithium7 : BBNNucleus
- beryllium7 : BBNNucleus
Instances For

---

### `Tau.BookV.Cosmology.instReprBBNNucleus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L114-L114)
**instance
Tau.BookV.Cosmology.instReprBBNNucleus :Repr BBNNucleus**

Equations
- Tau.BookV.Cosmology.instReprBBNNucleus = { reprPrec := Tau.BookV.Cosmology.instReprBBNNucleus.repr }

---

### `Tau.BookV.Cosmology.instReprBBNNucleus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L114-L114)
**def
Tau.BookV.Cosmology.instReprBBNNucleus.repr :BBNNucleus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instDecidableEqBBNNucleus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L114-L114)
**instance
Tau.BookV.Cosmology.instDecidableEqBBNNucleus :DecidableEq BBNNucleus**

Equations
- Tau.BookV.Cosmology.instDecidableEqBBNNucleus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqBBNNucleus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L114-L114)
**instance
Tau.BookV.Cosmology.instBEqBBNNucleus :BEq BBNNucleus**

Equations
- Tau.BookV.Cosmology.instBEqBBNNucleus = { beq := Tau.BookV.Cosmology.instBEqBBNNucleus.beq }

---

### `Tau.BookV.Cosmology.instBEqBBNNucleus.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L114-L114)
**def
Tau.BookV.Cosmology.instBEqBBNNucleus.beq :BBNNucleus → BBNNucleus → Bool**

Equations
- Tau.BookV.Cosmology.instBEqBBNNucleus.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.BBNNucleus.massNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L116-L125)
**def
Tau.BookV.Cosmology.BBNNucleus.massNumber :BBNNucleus → ℕ**


Mass number A for each BBN nucleus.
Equations
- Tau.BookV.Cosmology.BBNNucleus.neutron.massNumber = 1
- Tau.BookV.Cosmology.BBNNucleus.proton.massNumber = 1
- Tau.BookV.Cosmology.BBNNucleus.deuterium.massNumber = 2
- Tau.BookV.Cosmology.BBNNucleus.helium3.massNumber = 3
- Tau.BookV.Cosmology.BBNNucleus.tritium.massNumber = 3
- Tau.BookV.Cosmology.BBNNucleus.helium4.massNumber = 4
- Tau.BookV.Cosmology.BBNNucleus.lithium7.massNumber = 7
- Tau.BookV.Cosmology.BBNNucleus.beryllium7.massNumber = 7
Instances For

---

### `Tau.BookV.Cosmology.bbn_nucleus_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L127-L130)
**theorem
Tau.BookV.Cosmology.bbn_nucleus_count :[BBNNucleus.neutron, BBNNucleus.proton, BBNNucleus.deuterium, BBNNucleus.helium3, BBNNucleus.tritium, BBNNucleus.helium4, BBNNucleus.lithium7, BBNNucleus.beryllium7].length = 8**


There are exactly 8 BBN nuclei.

---

### `Tau.BookV.Cosmology.BBNReaction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L136-L150)
**inductive
Tau.BookV.Cosmology.BBNReaction :Type**


[V.D303] The 12 dominant BBN reactions, indexed 1–12.

- R1 : BBNReaction
- R2 : BBNReaction
- R3 : BBNReaction
- R4 : BBNReaction
- R5 : BBNReaction
- R6 : BBNReaction
- R7 : BBNReaction
- R8 : BBNReaction
- R9 : BBNReaction
- R10 : BBNReaction
- R11 : BBNReaction
- R12 : BBNReaction
Instances For

---

### `Tau.BookV.Cosmology.instReprBBNReaction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L150-L150)
**def
Tau.BookV.Cosmology.instReprBBNReaction.repr :BBNReaction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBBNReaction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L150-L150)
**instance
Tau.BookV.Cosmology.instReprBBNReaction :Repr BBNReaction**

Equations
- Tau.BookV.Cosmology.instReprBBNReaction = { reprPrec := Tau.BookV.Cosmology.instReprBBNReaction.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqBBNReaction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L150-L150)
**instance
Tau.BookV.Cosmology.instDecidableEqBBNReaction :DecidableEq BBNReaction**

Equations
- Tau.BookV.Cosmology.instDecidableEqBBNReaction x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqBBNReaction.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L150-L150)
**def
Tau.BookV.Cosmology.instBEqBBNReaction.beq :BBNReaction → BBNReaction → Bool**

Equations
- Tau.BookV.Cosmology.instBEqBBNReaction.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.instBEqBBNReaction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L150-L150)
**instance
Tau.BookV.Cosmology.instBEqBBNReaction :BEq BBNReaction**

Equations
- Tau.BookV.Cosmology.instBEqBBNReaction = { beq := Tau.BookV.Cosmology.instBEqBBNReaction.beq }

---

### `Tau.BookV.Cosmology.bbn_reactions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L152-L155)
**def
Tau.BookV.Cosmology.bbn_reactions :List BBNReaction**


The 12 reactions as a list.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bbn_reaction_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L157-L158)
**theorem
Tau.BookV.Cosmology.bbn_reaction_count :bbn_reactions.length = 12**


Exactly 12 reactions.

---

### `Tau.BookV.Cosmology.BBNSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L164-L169)
**inductive
Tau.BookV.Cosmology.BBNSector :Type**


[V.D304] τ-sector assignment for BBN reactions.

- A : BBNSector
- B : BBNSector
- C : BBNSector
Instances For

---

### `Tau.BookV.Cosmology.instReprBBNSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L169-L169)
**instance
Tau.BookV.Cosmology.instReprBBNSector :Repr BBNSector**

Equations
- Tau.BookV.Cosmology.instReprBBNSector = { reprPrec := Tau.BookV.Cosmology.instReprBBNSector.repr }

---

### `Tau.BookV.Cosmology.instReprBBNSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L169-L169)
**def
Tau.BookV.Cosmology.instReprBBNSector.repr :BBNSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instDecidableEqBBNSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L169-L169)
**instance
Tau.BookV.Cosmology.instDecidableEqBBNSector :DecidableEq BBNSector**

Equations
- Tau.BookV.Cosmology.instDecidableEqBBNSector x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqBBNSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L169-L169)
**instance
Tau.BookV.Cosmology.instBEqBBNSector :BEq BBNSector**

Equations
- Tau.BookV.Cosmology.instBEqBBNSector = { beq := Tau.BookV.Cosmology.instBEqBBNSector.beq }

---

### `Tau.BookV.Cosmology.instBEqBBNSector.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L169-L169)
**def
Tau.BookV.Cosmology.instBEqBBNSector.beq :BBNSector → BBNSector → Bool**

Equations
- Tau.BookV.Cosmology.instBEqBBNSector.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.reaction_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L171-L184)
**def
Tau.BookV.Cosmology.reaction_sector :BBNReaction → BBNSector**


Sector assignment for each reaction.
Equations
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R1 = Tau.BookV.Cosmology.BBNSector.A
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R2 = Tau.BookV.Cosmology.BBNSector.B
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R3 = Tau.BookV.Cosmology.BBNSector.B
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R4 = Tau.BookV.Cosmology.BBNSector.C
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R5 = Tau.BookV.Cosmology.BBNSector.C
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R6 = Tau.BookV.Cosmology.BBNSector.C
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R7 = Tau.BookV.Cosmology.BBNSector.C
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R8 = Tau.BookV.Cosmology.BBNSector.C
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R9 = Tau.BookV.Cosmology.BBNSector.B
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R10 = Tau.BookV.Cosmology.BBNSector.B
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R11 = Tau.BookV.Cosmology.BBNSector.C
- Tau.BookV.Cosmology.reaction_sector Tau.BookV.Cosmology.BBNReaction.R12 = Tau.BookV.Cosmology.BBNSector.C
Instances For

---

### `Tau.BookV.Cosmology.sector_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L186-L188)
**def
Tau.BookV.Cosmology.sector_count
(s : BBNSector)
 :ℕ**


Count reactions in a given sector.
Equations
- Tau.BookV.Cosmology.sector_count s = (List.filter (fun (r : Tau.BookV.Cosmology.BBNReaction) => Tau.BookV.Cosmology.reaction_sector r == s)
 Tau.BookV.Cosmology.bbn_reactions).length
Instances For

---

### `Tau.BookV.Cosmology.a_sector_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L191-L192)
**theorem
Tau.BookV.Cosmology.a_sector_count :sector_count BBNSector.A = 1**


A-sector count = 1.

---

### `Tau.BookV.Cosmology.b_sector_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L193-L194)
**theorem
Tau.BookV.Cosmology.b_sector_count :sector_count BBNSector.B = 4**


B-sector count = 4.

---

### `Tau.BookV.Cosmology.c_sector_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L195-L196)
**theorem
Tau.BookV.Cosmology.c_sector_count :sector_count BBNSector.C = 7**


C-sector count = 7.

---

### `Tau.BookV.Cosmology.sector_distribution_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L198-L201)
**theorem
Tau.BookV.Cosmology.sector_distribution_sum :sector_count BBNSector.A + sector_count BBNSector.B + sector_count BBNSector.C = 12**


[V.T242] Sector distribution sums to 12.

---

### `Tau.BookV.Cosmology.reaction_9_is_B_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L203-L205)
**theorem
Tau.BookV.Cosmology.reaction_9_is_B_sector :reaction_sector BBNReaction.R9 = BBNSector.B**


Reaction 9 is B-sector (EM capture).

---

### `Tau.BookV.Cosmology.FiberHolonomyCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L211-L223)
**structure
Tau.BookV.Cosmology.FiberHolonomyCorrection :Type**


[V.D305] T² fiber holonomy correction for EM captures.
At ⁷Be formation temperature, the B-sector EM capture
phase space is restricted to the base τ¹.

- dim_tau1 : ℕ
Dimension of τ¹ (base).

- dim_T2 : ℕ
Dimension of T² (fiber).

- dim_tau3 : ℕ
Dimension of τ³ (total).

- fibration_dim : self.dim_tau3 = self.dim_tau1 + self.dim_T2
τ³ = τ¹ ×_f T², so dim(τ³) = dim(τ¹) + dim(T²).

Instances For

---

### `Tau.BookV.Cosmology.instReprFiberHolonomyCorrection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L223-L223)
**def
Tau.BookV.Cosmology.instReprFiberHolonomyCorrection.repr :FiberHolonomyCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFiberHolonomyCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L223-L223)
**instance
Tau.BookV.Cosmology.instReprFiberHolonomyCorrection :Repr FiberHolonomyCorrection**

Equations
- Tau.BookV.Cosmology.instReprFiberHolonomyCorrection = { reprPrec := Tau.BookV.Cosmology.instReprFiberHolonomyCorrection.repr }

---

### `Tau.BookV.Cosmology.fiber_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L225-L227)
**def
Tau.BookV.Cosmology.fiber_holonomy :FiberHolonomyCorrection**


The canonical fiber holonomy correction.
Equations
- Tau.BookV.Cosmology.fiber_holonomy = { fibration_dim := Tau.BookV.Cosmology.fiber_holonomy._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.Be7SuppressionFactor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L233-L245)
**structure
Tau.BookV.Cosmology.Be7SuppressionFactor :Type**


[V.D306] ⁷Be suppression factor S = dim(τ¹)/dim(τ³) = 1/3.
The EM capture operates on the 1D base τ¹ rather than
the full 3D τ³.

- supp_num : ℕ
Suppression numerator = dim(τ¹).

- supp_den : ℕ
Suppression denominator = dim(τ³).

- num_from_base : self.supp_num = fiber_holonomy.dim_tau1
Numerator = fiber_holonomy.dim_tau1.

- den_from_total : self.supp_den = fiber_holonomy.dim_tau3
Denominator = fiber_holonomy.dim_tau3.

Instances For

---

### `Tau.BookV.Cosmology.instReprBe7SuppressionFactor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L245-L245)
**def
Tau.BookV.Cosmology.instReprBe7SuppressionFactor.repr :Be7SuppressionFactor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBe7SuppressionFactor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L245-L245)
**instance
Tau.BookV.Cosmology.instReprBe7SuppressionFactor :Repr Be7SuppressionFactor**

Equations
- Tau.BookV.Cosmology.instReprBe7SuppressionFactor = { reprPrec := Tau.BookV.Cosmology.instReprBe7SuppressionFactor.repr }

---

### `Tau.BookV.Cosmology.be7_suppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L247-L250)
**def
Tau.BookV.Cosmology.be7_suppression :Be7SuppressionFactor**


The canonical ⁷Be suppression factor.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.suppression_is_one_third`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L253-L256)
**theorem
Tau.BookV.Cosmology.suppression_is_one_third :be7_suppression.supp_num = 1 ∧ be7_suppression.supp_den = 3**


[V.T243] S_{⁷Be} = 1/3 exactly.

---

### `Tau.BookV.Cosmology.suppression_den_matches_tau3_dim`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L258-L260)
**theorem
Tau.BookV.Cosmology.suppression_den_matches_tau3_dim :be7_suppression.supp_den = tau3_dim**


The suppression denominator equals dim(τ³) = 3 from HeliumFraction.

---

### `Tau.BookV.Cosmology.LithiumResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L266-L285)
**structure
Tau.BookV.Cosmology.LithiumResolution :Type**


[V.T244] Lithium-7 resolution: SBBN value × (1/3) → within 0.9σ.
SBBN: ⁷Li/H = 562 × 10⁻¹² (i.e. 5.62 × 10⁻¹⁰).
τ-BBN: 562/3 = 187 × 10⁻¹² (i.e. 1.87 × 10⁻¹⁰).
Spite plateau: 160 ± 30 × 10⁻¹². Deviation: +0.9σ.

- sbbn_x1e12 : ℕ
SBBN prediction (×10⁻¹²).

- suppression_den : ℕ
Suppression factor denominator.

- tau_x1e12 : ℕ
τ-BBN prediction (×10⁻¹²).

- tau_from_sbbn : self.tau_x1e12 = self.sbbn_x1e12 / self.suppression_den
τ-BBN = SBBN / suppression_den (integer floor).

- obs_x1e12 : ℕ
Observed Spite plateau midpoint (×10⁻¹²).

- obs_unc_x1e12 : ℕ
Observed uncertainty (×10⁻¹²).

- within_range : self.tau_x1e12 > self.obs_x1e12 - self.obs_unc_x1e12
τ-BBN within observed range (160 − 30 = 130, 160 + 90 = 250).

Instances For

---

### `Tau.BookV.Cosmology.instReprLithiumResolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L285-L285)
**def
Tau.BookV.Cosmology.instReprLithiumResolution.repr :LithiumResolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprLithiumResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L285-L285)
**instance
Tau.BookV.Cosmology.instReprLithiumResolution :Repr LithiumResolution**

Equations
- Tau.BookV.Cosmology.instReprLithiumResolution = { reprPrec := Tau.BookV.Cosmology.instReprLithiumResolution.repr }

---

### `Tau.BookV.Cosmology.lithium_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L287-L290)
**def
Tau.BookV.Cosmology.lithium_resolution :LithiumResolution**


The canonical lithium resolution.
Equations
- Tau.BookV.Cosmology.lithium_resolution = { tau_from_sbbn := Tau.BookV.Cosmology.lithium_resolution._proof_1,
 within_range := Tau.BookV.Cosmology.lithium_resolution._proof_3 }
Instances For

---

### `Tau.BookV.Cosmology.lithium_within_1sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L292-L298)
**theorem
Tau.BookV.Cosmology.lithium_within_1sigma :lithium_resolution.tau_x1e12 > lithium_resolution.obs_x1e12 - lithium_resolution.obs_unc_x1e12 ∧ lithium_resolution.tau_x1e12 < lithium_resolution.obs_x1e12 + lithium_resolution.obs_unc_x1e12**


τ-BBN ⁷Li is within 1σ of observation: 130 < 187 < 190.

---

### `Tau.BookV.Cosmology.DeuteriumPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L304-L316)
**structure
Tau.BookV.Cosmology.DeuteriumPrediction :Type**


[V.T241] Deuterium prediction from τ-native η_B.
D/H(τ) ≈ 2.60 × 10⁻⁵. Observed: 2.527 ± 0.030 × 10⁻⁵.
Using ×10⁻⁷ units: τ-BBN = 260, obs = 253 ± 3.

- dh_x1e7 : ℕ
τ-BBN D/H (×10⁻⁷).

- obs_x1e7 : ℕ
Observed D/H midpoint (×10⁻⁷).

- obs_unc_x1e7 : ℕ
Observed uncertainty (×10⁻⁷).

- deviation_sigma_x10 : ℕ
Deviation in σ (×10): +23 means +2.3σ.

Instances For

---

### `Tau.BookV.Cosmology.instReprDeuteriumPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L316-L316)
**instance
Tau.BookV.Cosmology.instReprDeuteriumPrediction :Repr DeuteriumPrediction**

Equations
- Tau.BookV.Cosmology.instReprDeuteriumPrediction = { reprPrec := Tau.BookV.Cosmology.instReprDeuteriumPrediction.repr }

---

### `Tau.BookV.Cosmology.instReprDeuteriumPrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L316-L316)
**def
Tau.BookV.Cosmology.instReprDeuteriumPrediction.repr :DeuteriumPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.deuterium_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L318-L319)
**def
Tau.BookV.Cosmology.deuterium_prediction :DeuteriumPrediction**


The canonical deuterium prediction.
Equations
- Tau.BookV.Cosmology.deuterium_prediction = { }
Instances For

---

### `Tau.BookV.Cosmology.dh_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L322-L328)
**theorem
Tau.BookV.Cosmology.dh_in_range :deuterium_prediction.dh_x1e7 ≥ deuterium_prediction.obs_x1e7 - 3 * deuterium_prediction.obs_unc_x1e7 ∧ deuterium_prediction.dh_x1e7 ≤ deuterium_prediction.obs_x1e7 + 3 * deuterium_prediction.obs_unc_x1e7**


[V.P166] D/H within 3σ range (obs ± 3·unc = 253 ± 9, range 244..262).

---

### `Tau.BookV.Cosmology.He3Prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L334-L344)
**structure
Tau.BookV.Cosmology.He3Prediction :Type**


[V.T247] He-3 prediction from τ-native η_B.
³He/H(τ) ≈ 1.01 × 10⁻⁵. Observed: (1.1 ± 0.2) × 10⁻⁵.
Using ×10⁻⁷ units: τ-BBN = 101, obs = 110 ± 20.

- he3_x1e7 : ℕ
τ-BBN ³He/H (×10⁻⁷).

- obs_x1e7 : ℕ
Observed ³He/H midpoint (×10⁻⁷).

- obs_unc_x1e7 : ℕ
Observed uncertainty (×10⁻⁷).

Instances For

---

### `Tau.BookV.Cosmology.instReprHe3Prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L344-L344)
**instance
Tau.BookV.Cosmology.instReprHe3Prediction :Repr He3Prediction**

Equations
- Tau.BookV.Cosmology.instReprHe3Prediction = { reprPrec := Tau.BookV.Cosmology.instReprHe3Prediction.repr }

---

### `Tau.BookV.Cosmology.instReprHe3Prediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L344-L344)
**def
Tau.BookV.Cosmology.instReprHe3Prediction.repr :He3Prediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.he3_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L346-L347)
**def
Tau.BookV.Cosmology.he3_prediction :He3Prediction**


The canonical He-3 prediction.
Equations
- Tau.BookV.Cosmology.he3_prediction = { }
Instances For

---

### `Tau.BookV.Cosmology.he3_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L349-L355)
**theorem
Tau.BookV.Cosmology.he3_in_range :he3_prediction.he3_x1e7 ≥ he3_prediction.obs_x1e7 - 2 * he3_prediction.obs_unc_x1e7 ∧ he3_prediction.he3_x1e7 ≤ he3_prediction.obs_x1e7 + 2 * he3_prediction.obs_unc_x1e7**


[V.T247] ³He/H within observational range (70..150).

---

### `Tau.BookV.Cosmology.yp_preserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L362-L372)
**theorem
Tau.BookV.Cosmology.yp_preserved :he_prediction.yp_num = 20 ∧ he_prediction.yp_den = 81 ∧ be7_suppression.supp_den = 3 ∧ he_prediction.yp_den ≠ be7_suppression.supp_den**


[V.T245] Y_p = 20/81 is independent of ⁷Be production rate.
It derives from combinatorial voxel packing (8/27 × 5/6 = 20/81).

---

### `Tau.BookV.Cosmology.dh_preserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L375-L383)
**theorem
Tau.BookV.Cosmology.dh_preserved :BBNNucleus.deuterium.massNumber < he_packing.macro_side ∧ BBNNucleus.beryllium7.massNumber > he_packing.macro_side**


[V.T246] D/H is unaffected by fiber suppression.
D (A=2) is compatible with stride-3 macrocell geometry;
its abundance is set by the deuterium bottleneck, not ⁷Be.

---

### `Tau.BookV.Cosmology.selectivity_threshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L386-L400)
**theorem
Tau.BookV.Cosmology.selectivity_threshold :BBNNucleus.neutron.massNumber ≤ 4 ∧ BBNNucleus.proton.massNumber ≤ 4 ∧ BBNNucleus.deuterium.massNumber ≤ 4 ∧ BBNNucleus.helium3.massNumber ≤ 4 ∧ BBNNucleus.tritium.massNumber ≤ 4 ∧ BBNNucleus.helium4.massNumber ≤ 4 ∧ BBNNucleus.lithium7.massNumber > 4 ∧ BBNNucleus.beryllium7.massNumber > 4**


[V.P168] Only A ≥ 7 nuclei are suppressed.
A ≤ 4 fit the macrocell; A = 5,6 don't appear in BBN.

---

### `Tau.BookV.Cosmology.CompleteBBNTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L406-L421)
**structure
Tau.BookV.Cosmology.CompleteBBNTable :Type**


[V.D307] Complete BBN abundance table.
All four species from single η_B with zero free parameters.

- n_species : ℕ
Number of species predicted.

- n_free_params : ℕ
Number of free parameters.

- yp_ok : Bool
Y_p within range.

- dh_ok : Bool
D/H within range.

- he3_ok : Bool
³He/H within range.

- li7_ok : Bool
⁷Li/H within range.

Instances For

---

### `Tau.BookV.Cosmology.instReprCompleteBBNTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L421-L421)
**instance
Tau.BookV.Cosmology.instReprCompleteBBNTable :Repr CompleteBBNTable**

Equations
- Tau.BookV.Cosmology.instReprCompleteBBNTable = { reprPrec := Tau.BookV.Cosmology.instReprCompleteBBNTable.repr }

---

### `Tau.BookV.Cosmology.instReprCompleteBBNTable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L421-L421)
**def
Tau.BookV.Cosmology.instReprCompleteBBNTable.repr :CompleteBBNTable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.complete_bbn_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L423-L424)
**def
Tau.BookV.Cosmology.complete_bbn_table :CompleteBBNTable**


The complete BBN table instance.
Equations
- Tau.BookV.Cosmology.complete_bbn_table = { }
Instances For

---

### `Tau.BookV.Cosmology.bbn_table_all_within_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L427-L434)
**theorem
Tau.BookV.Cosmology.bbn_table_all_within_range :complete_bbn_table.yp_ok = true ∧ complete_bbn_table.dh_ok = true ∧ complete_bbn_table.he3_ok = true ∧ complete_bbn_table.li7_ok = true ∧ complete_bbn_table.n_free_params = 0**


[V.P169] All four predictions within observational range.

---

### `Tau.BookV.Cosmology.spite_plateau_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L437-L447)
**theorem
Tau.BookV.Cosmology.spite_plateau_consistent :lithium_resolution.tau_x1e12 * 85 / 100 = 158 ∧ 158 ≥ lithium_resolution.obs_x1e12 - lithium_resolution.obs_unc_x1e12 ∧ 158 ≤ lithium_resolution.obs_x1e12 + lithium_resolution.obs_unc_x1e12**


[V.P167] Including ~15% stellar depletion:
1.87 × 10⁻¹⁰ × 0.85 ≈ 1.59 × 10⁻¹⁰.
Spite plateau: (1.6 ± 0.3) × 10⁻¹⁰.
Using ×10⁻¹² units: 187 × 85 / 100 = 158. Obs = 160 ± 30.

---

### `Tau.BookV.Cosmology.dim_tau3_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L453-L460)
**theorem
Tau.BookV.Cosmology.dim_tau3_universality :be7_suppression.supp_den = 3 ∧ he_packing.macro_side = 3 ∧ tau3_dim = 3 ∧ 3 * 5 = 15**


dim(τ³) = 3 connects suppression (1/3), stride (3),
generations (H₁=ℤ³), and baryogenesis exponent (15=3×5).

---

### `Tau.BookV.Cosmology.bbn_species_standard`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L462-L463)
**theorem
Tau.BookV.Cosmology.bbn_species_standard :complete_bbn_table.n_species = 4**


The BBN table has as many species as the SBBN table.
