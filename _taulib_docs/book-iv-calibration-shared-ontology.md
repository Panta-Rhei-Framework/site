---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.SharedOntology"
permalink: /verify/taulib/docs/book-iv-calibration-shared-ontology/
lane: verify
module_name: "TauLib.BookIV.Calibration.SharedOntology"
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

# TauLib.BookIV.Calibration.SharedOntology


The shared ontological layer between Category τ and SI physics at E₁.

## Registry Cross-References


- [IV.R242] Part II in perspective — (structural remark)

- [IV.R243] The ladder is not a hierarchy — (structural remark)

- [IV.P159] Calibration is structural — `calibration_structural`

- [IV.R245] The honest timing — (structural remark)


## Ground Truth Sources


- Chapter 9 of Book IV (2nd Edition)


---

### `Tau.BookIV.Calibration.CalibrationMap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SharedOntology.lean#L27-L40)
**structure
Tau.BookIV.Calibration.CalibrationMap :Type**


[IV.P159] The translation between τ-native units and SI units at E₁
is a definable map within the boundary holonomy algebra.
It is not an ad-hoc fitting procedure: the map is forced by
the categorical structure.

- source_dim : ℕ
Source: τ-native coupling space (dim = number of sectors).

- source_eq : self.source_dim = 5
- target_dim : ℕ
Target: SI measurable quantities.

- no_knobs : Bool
The map is determined by ι<sub>τ</sub> alone (No Knobs).

- no_knobs_true : self.no_knobs = true
Instances For

---

### `Tau.BookIV.Calibration.instReprCalibrationMap.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SharedOntology.lean#L40-L40)
**def
Tau.BookIV.Calibration.instReprCalibrationMap.repr :CalibrationMap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprCalibrationMap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SharedOntology.lean#L40-L40)
**instance
Tau.BookIV.Calibration.instReprCalibrationMap :Repr CalibrationMap**

Equations
- Tau.BookIV.Calibration.instReprCalibrationMap = { reprPrec := Tau.BookIV.Calibration.instReprCalibrationMap.repr }

---

### `Tau.BookIV.Calibration.calibration_map`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SharedOntology.lean#L42-L48)
**def
Tau.BookIV.Calibration.calibration_map :CalibrationMap**


The canonical calibration map.
Equations
- Tau.BookIV.Calibration.calibration_map = { source_dim := 5, source_eq := Tau.BookIV.Calibration.calibration_map._proof_1, target_dim := 4, no_knobs := true,
 no_knobs_true := ⋯ }
Instances For

---

### `Tau.BookIV.Calibration.calibration_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/SharedOntology.lean#L50-L55)
**theorem
Tau.BookIV.Calibration.calibration_structural :calibration_map.source_dim = 5 ∧ calibration_map.no_knobs = true**


[IV.P159] Calibration is structural: determined by 5 sectors,
governed by ι<sub>τ</sub> alone.
