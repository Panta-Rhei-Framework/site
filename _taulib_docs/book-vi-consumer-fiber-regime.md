---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.FiberRegime"
permalink: /verify/taulib/docs/book-vi-consumer-fiber-regime/
lane: verify
module_name: "TauLib.BookVI.Consumer.FiberRegime"
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

# TauLib.BookVI.Consumer.FiberRegime


Fiber-enabled regime: eukaryotic innovations and multicellularity.

## Registry Cross-References


- [VI.D47] Fiber-Enabled Regime — `FiberEnabledRegime`

- [VI.R19] 1st Edition Correction (mixer placement) — `FirstEdCorrection`

- [VI.D48] Multicellularity as Colimit — `MulticellularityColimit`

- [VI.P18] Development as Controlled Differentiation — `DevelopmentDifferentiation`


## Cross-Book Authority


- Book I, Part VII: colimits (universal constructions)

- Book II, Part II: τ³ = τ¹ ×_f T² fibration structure

- Book II, Part X: ω-germ code (profinite completion)


## Ground Truth Sources


- Book VI Chapter 34 (2nd Edition): Eukarya — The Fiber-Enabled Regime

- Book VI Chapter 35 (2nd Edition): The Cell Cycle


---

### `Tau.BookVI.FiberRegime.FiberEnabledRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L34-L52)
**structure
Tau.BookVI.FiberRegime.FiberEnabledRegime :Type**


[VI.D47] Fiber-Enabled Regime: eukaryotic compartmentalization
unlocked by mixed-sector access to both fiber generators.
Four key innovations: nucleus, mitochondria, endomembrane, cytoskeleton.

- compartmentalization : Bool
Full compartmentalization achieved.

- innovation_count : ℕ
Number of key innovations.

- count_eq : self.innovation_count = 4
Exactly 4 innovations.

- nucleus : Bool
Innovation 1: nuclear envelope.

- mitochondria : Bool
Innovation 2: mitochondria (endosymbiosis).

- endomembrane : Bool
Innovation 3: endomembrane system.

- cytoskeleton : Bool
Innovation 4: cytoskeleton.

Instances For

---

### `Tau.BookVI.FiberRegime.instReprFiberEnabledRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L52-L52)
**def
Tau.BookVI.FiberRegime.instReprFiberEnabledRegime.repr :FiberEnabledRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FiberRegime.instReprFiberEnabledRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L52-L52)
**instance
Tau.BookVI.FiberRegime.instReprFiberEnabledRegime :Repr FiberEnabledRegime**

Equations
- Tau.BookVI.FiberRegime.instReprFiberEnabledRegime = { reprPrec := Tau.BookVI.FiberRegime.instReprFiberEnabledRegime.repr }

---

### `Tau.BookVI.FiberRegime.fiber_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L54-L56)
**def
Tau.BookVI.FiberRegime.fiber_regime :FiberEnabledRegime**

Equations
- Tau.BookVI.FiberRegime.fiber_regime = { innovation_count := 4, count_eq := Tau.BookVI.FiberRegime.fiber_regime._proof_1 }
Instances For

---

### `Tau.BookVI.FiberRegime.fiber_regime_four_innovations`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L58-L61)
**theorem
Tau.BookVI.FiberRegime.fiber_regime_four_innovations :fiber_regime.innovation_count = 4 ∧ fiber_regime.compartmentalization = true**


---

### `Tau.BookVI.FiberRegime.FirstEdCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L67-L77)
**structure
Tau.BookVI.FiberRegime.FirstEdCorrection :Type**


[VI.R19] 1st Edition Correction: mixer placement.
1st Ed paired (α, π) for consumer; 2nd Ed corrects to (π', π'').
The mixed sector requires both fiber generators, not base generators.

- old_pairing : String
Old (incorrect) pairing.

- new_pairing : String
New (correct) pairing.

- rationale : String
Correction rationale: fiber generators required.

Instances For

---

### `Tau.BookVI.FiberRegime.instReprFirstEdCorrection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L77-L77)
**def
Tau.BookVI.FiberRegime.instReprFirstEdCorrection.repr :FirstEdCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FiberRegime.instReprFirstEdCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L77-L77)
**instance
Tau.BookVI.FiberRegime.instReprFirstEdCorrection :Repr FirstEdCorrection**

Equations
- Tau.BookVI.FiberRegime.instReprFirstEdCorrection = { reprPrec := Tau.BookVI.FiberRegime.instReprFirstEdCorrection.repr }

---

### `Tau.BookVI.FiberRegime.correction_r19`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L79-L79)
**def
Tau.BookVI.FiberRegime.correction_r19 :FirstEdCorrection**

Equations
- Tau.BookVI.FiberRegime.correction_r19 = { }
Instances For

---

### `Tau.BookVI.FiberRegime.correction_changes_pairing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L81-L83)
**theorem
Tau.BookVI.FiberRegime.correction_changes_pairing :correction_r19.old_pairing ≠ correction_r19.new_pairing**


---

### `Tau.BookVI.FiberRegime.MulticellularityColimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L89-L102)
**structure
Tau.BookVI.FiberRegime.MulticellularityColimit :Type**


[VI.D48] Multicellularity as Colimit (Book I, Part VII).
A multicellular organism is a colimit over a diagram of
cooperating cell types. The colimit construction ensures
universal properties: any compatible morphism factors through it.

- cell_count : ℕ
Minimum cell count for multicellularity.

- multi : self.cell_count ≥ 2
At least 2 cells.

- cooperative : Bool
Cells are cooperative (not parasitic).

- colimit_construction : Bool
Construction is a categorical colimit.

Instances For

---

### `Tau.BookVI.FiberRegime.instReprMulticellularityColimit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L102-L102)
**def
Tau.BookVI.FiberRegime.instReprMulticellularityColimit.repr :MulticellularityColimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FiberRegime.instReprMulticellularityColimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L102-L102)
**instance
Tau.BookVI.FiberRegime.instReprMulticellularityColimit :Repr MulticellularityColimit**

Equations
- Tau.BookVI.FiberRegime.instReprMulticellularityColimit = { reprPrec := Tau.BookVI.FiberRegime.instReprMulticellularityColimit.repr }

---

### `Tau.BookVI.FiberRegime.multicellular`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L104-L106)
**def
Tau.BookVI.FiberRegime.multicellular :MulticellularityColimit**

Equations
- Tau.BookVI.FiberRegime.multicellular = { cell_count := 2, multi := Tau.BookVI.FiberRegime.multicellular._proof_1 }
Instances For

---

### `Tau.BookVI.FiberRegime.multicellularity_as_colimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L108-L112)
**theorem
Tau.BookVI.FiberRegime.multicellularity_as_colimit :multicellular.cell_count ≥ 2 ∧ multicellular.cooperative = true ∧ multicellular.colimit_construction = true**


---

### `Tau.BookVI.FiberRegime.DevelopmentDifferentiation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L118-L132)
**structure
Tau.BookVI.FiberRegime.DevelopmentDifferentiation :Type**


[VI.P18] Development as Controlled Differentiation.
Embryonic development is a refinement tower: totipotent →
pluripotent → multipotent → unipotent → terminal.
Each step is a controlled restriction of the ω-germ code
(Book II, Part X).

- refinement_tower : Bool
Development proceeds via refinement tower.

- potency_hierarchy : Bool
Potency hierarchy exists (totipotent → terminal).

- potency_levels : ℕ
Number of potency levels.

- levels_eq : self.potency_levels = 5
5 levels: totipotent, pluripotent, multipotent, unipotent, terminal.

Instances For

---

### `Tau.BookVI.FiberRegime.instReprDevelopmentDifferentiation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L132-L132)
**instance
Tau.BookVI.FiberRegime.instReprDevelopmentDifferentiation :Repr DevelopmentDifferentiation**

Equations
- Tau.BookVI.FiberRegime.instReprDevelopmentDifferentiation = { reprPrec := Tau.BookVI.FiberRegime.instReprDevelopmentDifferentiation.repr }

---

### `Tau.BookVI.FiberRegime.instReprDevelopmentDifferentiation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L132-L132)
**def
Tau.BookVI.FiberRegime.instReprDevelopmentDifferentiation.repr :DevelopmentDifferentiation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FiberRegime.development`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L134-L136)
**def
Tau.BookVI.FiberRegime.development :DevelopmentDifferentiation**

Equations
- Tau.BookVI.FiberRegime.development = { potency_levels := 5, levels_eq := Tau.BookVI.FiberRegime.development._proof_1 }
Instances For

---

### `Tau.BookVI.FiberRegime.development_refinement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/FiberRegime.lean#L138-L142)
**theorem
Tau.BookVI.FiberRegime.development_refinement :development.refinement_tower = true ∧ development.potency_hierarchy = true ∧ development.potency_levels = 5**
