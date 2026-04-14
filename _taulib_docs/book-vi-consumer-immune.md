---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.Immune"
permalink: /verify/taulib/docs/book-vi-consumer-immune/
lane: verify
module_name: "TauLib.BookVI.Consumer.Immune"
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

# TauLib.BookVI.Consumer.Immune


Immune systems: cellular distinction via MHC and autoimmunity as failure.

## Registry Cross-References


- [VI.D51] Cellular Distinction Predicate (MHC) — `CellularDistinction`

- [VI.T28] Autoimmunity as Distinction Failure — `autoimmunity_five_failures`


## Cross-Book Authority


- Book I, Part I: τ-Distinction D: X → 2_τ (generators give binary classifier)

- Book VI, Part 1: VI.D04 τ-Distinction (five conditions: clopen, refinement, stability, law, equivariance)


## Ground Truth Sources


- Book VI Chapter 39 (2nd Edition): Immune Systems


---

### `Tau.BookVI.Immune.CellularDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L28-L39)
**structure
Tau.BookVI.Immune.CellularDistinction :Type**


[VI.D51] Cellular Distinction Predicate (MHC).
MHC class I + class II implement τ-Distinction (VI.D04)
at the cellular level: D: Cell → {self, nonself}.
Book I, Part I provides the abstract binary classifier.

- mhc_class_I : Bool
MHC class I present (all nucleated cells).

- mhc_class_II : Bool
MHC class II present (antigen-presenting cells).

- distinction_implementation : Bool
Implements τ-Distinction at cellular level.

Instances For

---

### `Tau.BookVI.Immune.instReprCellularDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L39-L39)
**instance
Tau.BookVI.Immune.instReprCellularDistinction :Repr CellularDistinction**

Equations
- Tau.BookVI.Immune.instReprCellularDistinction = { reprPrec := Tau.BookVI.Immune.instReprCellularDistinction.repr }

---

### `Tau.BookVI.Immune.instReprCellularDistinction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L39-L39)
**def
Tau.BookVI.Immune.instReprCellularDistinction.repr :CellularDistinction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Immune.cell_dist`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L41-L41)
**def
Tau.BookVI.Immune.cell_dist :CellularDistinction**

Equations
- Tau.BookVI.Immune.cell_dist = { }
Instances For

---

### `Tau.BookVI.Immune.cellular_distinction_is_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L43-L47)
**theorem
Tau.BookVI.Immune.cellular_distinction_is_tau :cell_dist.mhc_class_I = true ∧ cell_dist.mhc_class_II = true ∧ cell_dist.distinction_implementation = true**


---

### `Tau.BookVI.Immune.AutoimmunityFailure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L53-L76)
**structure
Tau.BookVI.Immune.AutoimmunityFailure :Type**


[VI.T28] Autoimmunity as Distinction Failure.
Five failure modes, one for each condition of VI.D04:
(1) Clopen violation — boundary leakage
(2) Refinement violation — tolerance breakdown
(3) Stability violation — stochastic misfire
(4) Law violation — regulatory T-cell deficiency
(5) Equivariance violation — molecular mimicry
Each autoimmune disease maps to one or more failure modes.

- failure_modes : ℕ
Total failure modes.

- modes_eq : self.failure_modes = 5
Exactly 5 (one per Distinction condition).

- clopen_violation : Bool
(1) Clopen boundary leakage.

- refinement_violation : Bool
(2) Refinement/tolerance breakdown.

- stability_violation : Bool
(3) Stability/stochastic misfire.

- law_violation : Bool
(4) Law/regulatory T-cell deficiency.

- equivariance_violation : Bool
(5) Equivariance/molecular mimicry.

Instances For

---

### `Tau.BookVI.Immune.instReprAutoimmunityFailure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L76-L76)
**instance
Tau.BookVI.Immune.instReprAutoimmunityFailure :Repr AutoimmunityFailure**

Equations
- Tau.BookVI.Immune.instReprAutoimmunityFailure = { reprPrec := Tau.BookVI.Immune.instReprAutoimmunityFailure.repr }

---

### `Tau.BookVI.Immune.instReprAutoimmunityFailure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L76-L76)
**def
Tau.BookVI.Immune.instReprAutoimmunityFailure.repr :AutoimmunityFailure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Immune.autoimmune`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L78-L80)
**def
Tau.BookVI.Immune.autoimmune :AutoimmunityFailure**

Equations
- Tau.BookVI.Immune.autoimmune = { failure_modes := 5, modes_eq := Tau.BookVI.Immune.autoimmune._proof_1 }
Instances For

---

### `Tau.BookVI.Immune.autoimmunity_five_failures`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Immune.lean#L82-L89)
**theorem
Tau.BookVI.Immune.autoimmunity_five_failures :autoimmune.failure_modes = 5 ∧ autoimmune.clopen_violation = true ∧ autoimmune.refinement_violation = true ∧ autoimmune.stability_violation = true ∧ autoimmune.law_violation = true ∧ autoimmune.equivariance_violation = true**
