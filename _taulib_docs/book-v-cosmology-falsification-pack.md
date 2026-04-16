---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.FalsificationPack"
permalink: /verify/taulib/docs/book-v-cosmology-falsification-pack/
lane: verify
module_name: "TauLib.BookV.Cosmology.FalsificationPack"
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

# TauLib.BookV.Cosmology.FalsificationPack


Falsification package. Three falsification levels with specific
testable predictions. Experimental program for the τ-framework.

## Registry Cross-References


- [V.R243] Scope note: CMB predictions C2, C5, C6 -- structural remark

- [V.D184] Falsification Levels -- `FalsificationLevels`


## Mathematical Content


### Three Falsification Levels


Level 1 (Structural): fundamental predictions that, if falsified,
would refute the τ-framework entirely:


- A sixth force

- Dark matter particle

- c_gw ≠ c (gravitational wave speed ≠ light speed)

- GW echoes (would indicate S² instead of T² horizon)


Level 2 (Quantitative): precise numerical predictions:


- m_e = 0.510999 MeV (0.025 ppm from R formula)

- G to 3 ppm (from closing identity with c₁ = 3/π)

- r ι<sub>τ</sub>⁴ 0.014 (tensor-to-scalar ratio)

- sin²θ_W from sector coupling ratios


Level 3 (Observational frontier): predictions that require future
technology to test:


- T²-topology BH shadows (vs. S²)

- Profinite discreteness at Planck scale

- No trans-Planckian modes in CMB


### CMB Predictions (Scope Note)


CMB predictions C2, C5, C6 involve mapping τ-native quantities
to standard CMB observables. The mapping itself is tau-effective,
but the numerical calibration carries observational uncertainties.

## Ground Truth Sources


- Book V ch55: Falsification Package


---

### `Tau.BookV.Cosmology.FalsificationLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L55-L63)
**inductive
Tau.BookV.Cosmology.FalsificationLevel :Type**


Falsification level classification.

- Structural : FalsificationLevel
Level 1: structural (refutes framework).

- Quantitative : FalsificationLevel
Level 2: quantitative (tests specific numbers).

- ObservationalFrontier : FalsificationLevel
Level 3: observational frontier (needs future tech).

Instances For

---

### `Tau.BookV.Cosmology.instReprFalsificationLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L63-L63)
**def
Tau.BookV.Cosmology.instReprFalsificationLevel.repr :FalsificationLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFalsificationLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L63-L63)
**instance
Tau.BookV.Cosmology.instReprFalsificationLevel :Repr FalsificationLevel**

Equations
- Tau.BookV.Cosmology.instReprFalsificationLevel = { reprPrec := Tau.BookV.Cosmology.instReprFalsificationLevel.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqFalsificationLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L63-L63)
**instance
Tau.BookV.Cosmology.instDecidableEqFalsificationLevel :DecidableEq FalsificationLevel**

Equations
- Tau.BookV.Cosmology.instDecidableEqFalsificationLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqFalsificationLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L63-L63)
**instance
Tau.BookV.Cosmology.instBEqFalsificationLevel :BEq FalsificationLevel**

Equations
- Tau.BookV.Cosmology.instBEqFalsificationLevel = { beq := Tau.BookV.Cosmology.instBEqFalsificationLevel.beq }

---

### `Tau.BookV.Cosmology.instBEqFalsificationLevel.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L63-L63)
**def
Tau.BookV.Cosmology.instBEqFalsificationLevel.beq :FalsificationLevel → FalsificationLevel → Bool**

Equations
- Tau.BookV.Cosmology.instBEqFalsificationLevel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.TestablePrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L65-L77)
**structure
Tau.BookV.Cosmology.TestablePrediction :Type**


A single testable prediction.

- name : String
Prediction identifier.

- level : FalsificationLevel
Falsification level.

- description : String
Description of the prediction.

- status : String
Current experimental status.

- currently_testable : Bool
Whether currently testable.

Instances For

---

### `Tau.BookV.Cosmology.instReprTestablePrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L77-L77)
**instance
Tau.BookV.Cosmology.instReprTestablePrediction :Repr TestablePrediction**

Equations
- Tau.BookV.Cosmology.instReprTestablePrediction = { reprPrec := Tau.BookV.Cosmology.instReprTestablePrediction.repr }

---

### `Tau.BookV.Cosmology.instReprTestablePrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L77-L77)
**def
Tau.BookV.Cosmology.instReprTestablePrediction.repr :TestablePrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.FalsificationLevels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L79-L99)
**structure
Tau.BookV.Cosmology.FalsificationLevels :Type**


[V.D184] Falsification levels: three-tier classification of
τ-framework predictions by falsifiability strength and
experimental accessibility.

Level 1: structural — would refute entire framework
Level 2: quantitative — tests specific numerical values
Level 3: frontier — requires future technology

- structural : List TestablePrediction
Level 1 predictions.

- quantitative : List TestablePrediction
Level 2 predictions.

- frontier : List TestablePrediction
Level 3 predictions.

- has_structural : self.structural.length > 0
At least one structural prediction.

- has_quantitative : self.quantitative.length > 0
At least one quantitative prediction.

- has_frontier : self.frontier.length > 0
At least one frontier prediction.

Instances For

---

### `Tau.BookV.Cosmology.instReprFalsificationLevels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L99-L99)
**instance
Tau.BookV.Cosmology.instReprFalsificationLevels :Repr FalsificationLevels**

Equations
- Tau.BookV.Cosmology.instReprFalsificationLevels = { reprPrec := Tau.BookV.Cosmology.instReprFalsificationLevels.repr }

---

### `Tau.BookV.Cosmology.instReprFalsificationLevels.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L99-L99)
**def
Tau.BookV.Cosmology.instReprFalsificationLevels.repr :FalsificationLevels → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_no_sixth_force`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L105-L111)
**def
Tau.BookV.Cosmology.pred_no_sixth_force :TestablePrediction**


S1: No sixth force.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_no_dm_particle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L113-L119)
**def
Tau.BookV.Cosmology.pred_no_dm_particle :TestablePrediction**


S2: No dark matter particle.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_cgw_equals_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L121-L127)
**def
Tau.BookV.Cosmology.pred_cgw_equals_c :TestablePrediction**


S3: c_gw = c exactly.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_no_gw_echoes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L129-L135)
**def
Tau.BookV.Cosmology.pred_no_gw_echoes :TestablePrediction**


S4: No GW echoes.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_electron_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L141-L147)
**def
Tau.BookV.Cosmology.pred_electron_mass :TestablePrediction**


Q1: Electron mass at 0.025 ppm.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_grav_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L149-L155)
**def
Tau.BookV.Cosmology.pred_grav_constant :TestablePrediction**


Q2: Gravitational constant at 3 ppm.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_tensor_scalar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L157-L163)
**def
Tau.BookV.Cosmology.pred_tensor_scalar :TestablePrediction**


Q3: Tensor-to-scalar ratio r ~ 0.014.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_torus_shadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L169-L175)
**def
Tau.BookV.Cosmology.pred_torus_shadow :TestablePrediction**


F1: T² topology BH shadows.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_discreteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L177-L183)
**def
Tau.BookV.Cosmology.pred_discreteness :TestablePrediction**


F2: Profinite discreteness at Planck scale.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pred_no_transplanckian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L185-L191)
**def
Tau.BookV.Cosmology.pred_no_transplanckian :TestablePrediction**


F3: No trans-Planckian modes in CMB.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.falsification_package`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L197-L205)
**def
Tau.BookV.Cosmology.falsification_package :FalsificationLevels**


The complete falsification package.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.structural_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L207-L209)
**theorem
Tau.BookV.Cosmology.structural_count :falsification_package.structural.length = 4**


4 structural predictions.

---

### `Tau.BookV.Cosmology.quantitative_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L211-L213)
**theorem
Tau.BookV.Cosmology.quantitative_count :falsification_package.quantitative.length = 3**


3 quantitative predictions.

---

### `Tau.BookV.Cosmology.frontier_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L215-L217)
**theorem
Tau.BookV.Cosmology.frontier_count :falsification_package.frontier.length = 3**


3 frontier predictions.

---

### `Tau.BookV.Cosmology.total_predictions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L219-L223)
**theorem
Tau.BookV.Cosmology.total_predictions :falsification_package.structural.length + falsification_package.quantitative.length + falsification_package.frontier.length = 10**


Total: 10 testable predictions.

---

### `Tau.BookV.Cosmology.cmb_scope_note`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L229-L235)
**def
Tau.BookV.Cosmology.cmb_scope_note :Prop**


[V.R243] Scope note: CMB predictions C2, C5, C6 involve mapping
τ-native quantities to standard CMB observables (angular power
spectrum, polarization). The mapping is tau-effective, but
numerical calibration carries observational uncertainties.
Equations
- Tau.BookV.Cosmology.cmb_scope_note = ("CMB predictions: tau-effective mapping, observational calibration" = "CMB predictions: tau-effective mapping, observational calibration")
Instances For

---

### `Tau.BookV.Cosmology.cmb_scope_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/FalsificationPack.lean#L237-L237)
**theorem
Tau.BookV.Cosmology.cmb_scope_holds :cmb_scope_note**
