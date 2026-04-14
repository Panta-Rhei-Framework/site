---
layout: taulib-doc
title: "TauLib.BookVI.CosmicLife.GalaxyBasin"
permalink: /verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/
lane: verify
module_name: "TauLib.BookVI.CosmicLife.GalaxyBasin"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.CosmicLife.GalaxyBasin


Galaxy basins: galaxies as Life basins anchored by SMBHs.

## Registry Cross-References


- [VI.D62] Life Basin — `LifeBasin`

- [VI.D63] Carrier Ladder — `CarrierLadder`

- [VI.D64] Basin Predicate — `BasinPredicate`

- [VI.T33] Galaxy–SMBH Anchor Lemma — `anchor_lemma`

- [VI.L12] Basin Fusion via SMBH Merger — `basin_fusion_lemma`


## Ground Truth Sources


- Book VI Chapter 47 (2nd Edition): Galaxies as Life Basins


---

### `Tau.BookVI.GalaxyBasin.LifeBasin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L26-L38)
**structure
Tau.BookVI.GalaxyBasin.LifeBasin :Type**


[VI.D62] Life Basin: spatial region anchored by a central carrier.
Triple (B, C_anc, F) where B is basin region, C_anc is anchor,
F is carrier family. Boundary at virial radius.

- grav_bound : Bool
Basin region is gravitationally bound.

- anchor_alive : Bool
Anchor carrier satisfies Distinction + SelfDesc.

- has_carrier_family : Bool
Carrier family: collection of all carriers in basin.

- virial_boundary : Bool
Basin boundary = virial radius.

Instances For

---

### `Tau.BookVI.GalaxyBasin.instReprLifeBasin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L38-L38)
**instance
Tau.BookVI.GalaxyBasin.instReprLifeBasin :Repr LifeBasin**

Equations
- Tau.BookVI.GalaxyBasin.instReprLifeBasin = { reprPrec := Tau.BookVI.GalaxyBasin.instReprLifeBasin.repr }

---

### `Tau.BookVI.GalaxyBasin.instReprLifeBasin.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L38-L38)
**def
Tau.BookVI.GalaxyBasin.instReprLifeBasin.repr :LifeBasin → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GalaxyBasin.galaxy_basin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L40-L40)
**def
Tau.BookVI.GalaxyBasin.galaxy_basin :LifeBasin**

Equations
- Tau.BookVI.GalaxyBasin.galaxy_basin = { }
Instances For

---

### `Tau.BookVI.GalaxyBasin.CarrierLadder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L46-L57)
**structure
Tau.BookVI.GalaxyBasin.CarrierLadder :Type**


[VI.D63] Carrier Ladder: 7-level hierarchy from molecules to galaxies.
X_gal[0..6] = molecular, cellular, organismal, ecosystemic,
planetary, stellar, galactic.
Constraints flow downward, realization flows upward.

- level_count : ℕ
Number of hierarchy levels.

- count_eq : self.level_count = 7
Exactly 7 levels (0 through 6).

- functorial : Bool
Constraints compose functorially.

Instances For

---

### `Tau.BookVI.GalaxyBasin.instReprCarrierLadder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L57-L57)
**instance
Tau.BookVI.GalaxyBasin.instReprCarrierLadder :Repr CarrierLadder**

Equations
- Tau.BookVI.GalaxyBasin.instReprCarrierLadder = { reprPrec := Tau.BookVI.GalaxyBasin.instReprCarrierLadder.repr }

---

### `Tau.BookVI.GalaxyBasin.instReprCarrierLadder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L57-L57)
**def
Tau.BookVI.GalaxyBasin.instReprCarrierLadder.repr :CarrierLadder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GalaxyBasin.carrier_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L59-L61)
**def
Tau.BookVI.GalaxyBasin.carrier_ladder :CarrierLadder**

Equations
- Tau.BookVI.GalaxyBasin.carrier_ladder = { level_count := 7, count_eq := Tau.BookVI.GalaxyBasin.carrier_ladder._proof_1 }
Instances For

---

### `Tau.BookVI.GalaxyBasin.ladder_level_names`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L63-L66)
**def
Tau.BookVI.GalaxyBasin.ladder_level_names :List String**


Carrier ladder names for reference.
Equations
- Tau.BookVI.GalaxyBasin.ladder_level_names = ["molecular", "cellular", "organismal", "ecosystemic", "planetary", "stellar", "galactic"]
Instances For

---

### `Tau.BookVI.GalaxyBasin.ladder_has_7_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L68-L71)
**theorem
Tau.BookVI.GalaxyBasin.ladder_has_7_levels :carrier_ladder.level_count = 7 ∧ ladder_level_names.length = 7**


---

### `Tau.BookVI.GalaxyBasin.BasinPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L77-L93)
**structure
Tau.BookVI.GalaxyBasin.BasinPredicate :Type**


[VI.D64] Basin Predicate: admissibility for a Life basin.
Four conditions: (i) anchor alive, (ii) gravitational dominance,
(iii) basin coherence (virialized), (iv) carrier support.

- condition_count : ℕ
Number of admissibility conditions.

- count_eq : self.condition_count = 4
Exactly 4 conditions.

- anchor_alive : Bool
Anchor satisfies Distinction + SelfDesc.

- grav_dominant : Bool
Anchor is gravitationally dominant.

- virialized : Bool
Basin is virialized (2K + U ≤ 0).

- carrier_support : Bool
At least one carrier at level n ≤ 5.

Instances For

---

### `Tau.BookVI.GalaxyBasin.instReprBasinPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L93-L93)
**instance
Tau.BookVI.GalaxyBasin.instReprBasinPredicate :Repr BasinPredicate**

Equations
- Tau.BookVI.GalaxyBasin.instReprBasinPredicate = { reprPrec := Tau.BookVI.GalaxyBasin.instReprBasinPredicate.repr }

---

### `Tau.BookVI.GalaxyBasin.instReprBasinPredicate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L93-L93)
**def
Tau.BookVI.GalaxyBasin.instReprBasinPredicate.repr :BasinPredicate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GalaxyBasin.basin_pred`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L95-L97)
**def
Tau.BookVI.GalaxyBasin.basin_pred :BasinPredicate**

Equations
- Tau.BookVI.GalaxyBasin.basin_pred = { condition_count := 4, count_eq := Tau.BookVI.GalaxyBasin.basin_pred._proof_1 }
Instances For

---

### `Tau.BookVI.GalaxyBasin.AnchorLemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L103-L116)
**structure
Tau.BookVI.GalaxyBasin.AnchorLemma :Type**


[VI.T33] Galaxy–SMBH Anchor Lemma: galactic ω-germ code
factors through SMBH's ω-code.
code(D^gal)[ω] = Φ_bas ∘ code(D^SMBH)[ω]
Empirical grounding: M–σ relation.

- code_factorizes : Bool
Code factors through anchor.

- code_determines_basin : Bool
Same SMBH → same galactic code (up to Φ_bas).

- eval_decomposes : Bool
Evaluator decomposes through anchor.

- m_sigma_grounding : Bool
Φ_bas grounded by M–σ relation.

Instances For

---

### `Tau.BookVI.GalaxyBasin.instReprAnchorLemma.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L116-L116)
**def
Tau.BookVI.GalaxyBasin.instReprAnchorLemma.repr :AnchorLemma → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GalaxyBasin.instReprAnchorLemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L116-L116)
**instance
Tau.BookVI.GalaxyBasin.instReprAnchorLemma :Repr AnchorLemma**

Equations
- Tau.BookVI.GalaxyBasin.instReprAnchorLemma = { reprPrec := Tau.BookVI.GalaxyBasin.instReprAnchorLemma.repr }

---

### `Tau.BookVI.GalaxyBasin.anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L118-L118)
**def
Tau.BookVI.GalaxyBasin.anchor :AnchorLemma**

Equations
- Tau.BookVI.GalaxyBasin.anchor = { }
Instances For

---

### `Tau.BookVI.GalaxyBasin.anchor_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L120-L124)
**theorem
Tau.BookVI.GalaxyBasin.anchor_lemma :anchor.code_factorizes = true ∧ anchor.code_determines_basin = true ∧ anchor.eval_decomposes = true**


---

### `Tau.BookVI.GalaxyBasin.BasinFusion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L130-L144)
**structure
Tau.BookVI.GalaxyBasin.BasinFusion :Type**


[VI.L12] Basin Fusion via SMBH Merger: galaxy merger is basin fusion.
(i) Anchor merger produces single remnant SMBH (V.D171, V.T112)
(ii) Code fusion: merged code via blueprint fusion
(iii) Carrier family union (with dynamical rearrangement)
(iv) Ladder restructuring under new gravitational potential

- anchor_merges : Bool
SMBHs merge to single remnant.

- code_fuses : Bool
Code fuses via blueprint fusion.

- carrier_union : Bool
Carrier family is union of progenitors.

- ladder_restructured : Bool
Ladder restructured under new potential.

Instances For

---

### `Tau.BookVI.GalaxyBasin.instReprBasinFusion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L144-L144)
**instance
Tau.BookVI.GalaxyBasin.instReprBasinFusion :Repr BasinFusion**

Equations
- Tau.BookVI.GalaxyBasin.instReprBasinFusion = { reprPrec := Tau.BookVI.GalaxyBasin.instReprBasinFusion.repr }

---

### `Tau.BookVI.GalaxyBasin.instReprBasinFusion.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L144-L144)
**def
Tau.BookVI.GalaxyBasin.instReprBasinFusion.repr :BasinFusion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GalaxyBasin.basin_fusion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L146-L146)
**def
Tau.BookVI.GalaxyBasin.basin_fusion :BasinFusion**

Equations
- Tau.BookVI.GalaxyBasin.basin_fusion = { }
Instances For

---

### `Tau.BookVI.GalaxyBasin.basin_fusion_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L148-L153)
**theorem
Tau.BookVI.GalaxyBasin.basin_fusion_lemma :basin_fusion.anchor_merges = true ∧ basin_fusion.code_fuses = true ∧ basin_fusion.carrier_union = true ∧ basin_fusion.ladder_restructured = true**
