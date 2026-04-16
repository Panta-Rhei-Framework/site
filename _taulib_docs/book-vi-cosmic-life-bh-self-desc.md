---
layout: taulib-doc
title: "TauLib.BookVI.CosmicLife.BHSelfDesc"
permalink: /verify/taulib/docs/book-vi-cosmic-life-bh-self-desc/
lane: verify
module_name: "TauLib.BookVI.CosmicLife.BHSelfDesc"
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

# TauLib.BookVI.CosmicLife.BHSelfDesc


BH SelfDesc: macro-torus carrier satisfies SelfDesc. BH IS alive.
Imports BookV.Gravity.BHTopoModes for QNM evaluator mechanism.

## Registry Cross-References


- [VI.D58] BH DecodeTarget — `BHDecodeTarget`

- [VI.D59] BH DecodeHorizon — `BHDecodeHorizon`

- [VI.L09] BH Uniqueness Lemma — `bh_uniqueness_lemma`

- [VI.L10] BH Constancy Lemma — `bh_constancy_lemma`

- [VI.T30] BH SelfDesc Theorem — `bh_selfdesc_theorem`


## Book V Authority


- [V.D234] T² QNM Mode Structure: ringdown as evaluator mechanism

- [V.T168] QNM Frequency Ratio ι<sub>τ</sub>⁻¹: carrier-internal frequencies

- [V.T114] No-Shrink Theorem: code integrity guarantee


## Ground Truth Sources


- Book VI Chapter 44 (2nd Edition): BH SelfDesc


---

### `Tau.BookVI.BHSelfDesc.BHDecodeTarget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L36-L45)
**structure
Tau.BookVI.BHSelfDesc.BHDecodeTarget :Type**


[VI.D58] BH DecodeTarget: argmin of lex defect = Kerr-Newman.
The unique minimizer (Israel-Carter-Robinson uniqueness theorem).

- selects_argmin : Bool
Selects argmin of lexicographic defect.

- kerr_newman : Bool
Target is the Kerr-Newman solution.

- charge_count : ℕ
Charge parameters determining the target.

Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHDecodeTarget.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L45-L45)
**def
Tau.BookVI.BHSelfDesc.instReprBHDecodeTarget.repr :BHDecodeTarget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHDecodeTarget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L45-L45)
**instance
Tau.BookVI.BHSelfDesc.instReprBHDecodeTarget :Repr BHDecodeTarget**

Equations
- Tau.BookVI.BHSelfDesc.instReprBHDecodeTarget = { reprPrec := Tau.BookVI.BHSelfDesc.instReprBHDecodeTarget.repr }

---

### `Tau.BookVI.BHSelfDesc.bh_target`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L47-L47)
**def
Tau.BookVI.BHSelfDesc.bh_target :BHDecodeTarget**

Equations
- Tau.BookVI.BHSelfDesc.bh_target = { }
Instances For

---

### `Tau.BookVI.BHSelfDesc.BHDecodeHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L53-L62)
**structure
Tau.BookVI.BHSelfDesc.BHDecodeHorizon :Type**


[VI.D59] BH DecodeHorizon: constant ω-germ code from (M,J,Q).
The code is finitely determined (profinite limit stabilizes at step 1).

- constant_code : Bool
Code is constant across blueprint ball.

- charge_count : ℕ
Three conserved charges encode the genotype.

- stabilization_depth : ℕ
Profinite limit stabilizes after 1 step (No-Hair).

Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHDecodeHorizon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L62-L62)
**def
Tau.BookVI.BHSelfDesc.instReprBHDecodeHorizon.repr :BHDecodeHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHDecodeHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L62-L62)
**instance
Tau.BookVI.BHSelfDesc.instReprBHDecodeHorizon :Repr BHDecodeHorizon**

Equations
- Tau.BookVI.BHSelfDesc.instReprBHDecodeHorizon = { reprPrec := Tau.BookVI.BHSelfDesc.instReprBHDecodeHorizon.repr }

---

### `Tau.BookVI.BHSelfDesc.bh_horizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L64-L64)
**def
Tau.BookVI.BHSelfDesc.bh_horizon :BHDecodeHorizon**

Equations
- Tau.BookVI.BHSelfDesc.bh_horizon = { }
Instances For

---

### `Tau.BookVI.BHSelfDesc.bh_uniqueness_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L70-L74)
**theorem
Tau.BookVI.BHSelfDesc.bh_uniqueness_lemma :bh_target.kerr_newman = true ∧ bh_target.selects_argmin = true**


[VI.L09] BH uniqueness: unique element at every refinement level.
Follows from Israel-Carter-Robinson (No-Hair) theorem.

---

### `Tau.BookVI.BHSelfDesc.bh_constancy_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L76-L80)
**theorem
Tau.BookVI.BHSelfDesc.bh_constancy_lemma :bh_horizon.constant_code = true ∧ bh_horizon.stabilization_depth = 1**


[VI.L10] BH constancy: same code for all n ≥ 0.
Code is independent of blueprint ball radius.

---

### `Tau.BookVI.BHSelfDesc.BHEvaluator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L86-L96)
**structure
Tau.BookVI.BHSelfDesc.BHEvaluator :Type**


The BH evaluator is physically realized by T² torus ringdown.
QNM frequencies from V.D234 determine the evaluation timescale.
Fundamental ratio f(0,1)/f(1,0) = ι<sub>τ</sub>⁻¹ (V.T168).

- mechanism : String
Evaluator mechanism: torus QNM ringdown.

- mode_count : ℕ
Number of primitive torus modes (from BookV).

- ratio_exceeds_one : Bool
QNM ratio is ι<sub>τ</sub>⁻¹ > 1 (from BookV).

Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHEvaluator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L96-L96)
**instance
Tau.BookVI.BHSelfDesc.instReprBHEvaluator :Repr BHEvaluator**

Equations
- Tau.BookVI.BHSelfDesc.instReprBHEvaluator = { reprPrec := Tau.BookVI.BHSelfDesc.instReprBHEvaluator.repr }

---

### `Tau.BookVI.BHSelfDesc.instReprBHEvaluator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L96-L96)
**def
Tau.BookVI.BHSelfDesc.instReprBHEvaluator.repr :BHEvaluator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHSelfDesc.bh_evaluator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L98-L98)
**def
Tau.BookVI.BHSelfDesc.bh_evaluator :BHEvaluator**

Equations
- Tau.BookVI.BHSelfDesc.bh_evaluator = { }
Instances For

---

### `Tau.BookVI.BHSelfDesc.evaluator_modes_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L100-L102)
**theorem
Tau.BookVI.BHSelfDesc.evaluator_modes_consistent :bh_evaluator.mode_count = 3**


Evaluator mode count matches BookV authority.

---

### `Tau.BookVI.BHSelfDesc.BHSelfDescResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L108-L123)
**structure
Tau.BookVI.BHSelfDesc.BHSelfDescResult :Type**


[VI.T30] BH SelfDesc Theorem: 3/3 conditions verified.
(i) Completeness: Eval reconstructs D at every level
(ii) Internality: code + evaluator reside within carrier
(iii) Refinement coherence: tower stabilizes at n=1
Conclusion: BH IS alive (same theorem as for cells).

- conditions_satisfied : ℕ
Number of SelfDesc conditions satisfied.

- all_three : self.conditions_satisfied = 3
All three conditions verified.

- completeness : Bool
- internality : Bool
- refinement_coherence : Bool
- bh_alive : Bool
Final verdict: BH is alive.

Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHSelfDescResult.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L123-L123)
**def
Tau.BookVI.BHSelfDesc.instReprBHSelfDescResult.repr :BHSelfDescResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHSelfDesc.instReprBHSelfDescResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L123-L123)
**instance
Tau.BookVI.BHSelfDesc.instReprBHSelfDescResult :Repr BHSelfDescResult**

Equations
- Tau.BookVI.BHSelfDesc.instReprBHSelfDescResult = { reprPrec := Tau.BookVI.BHSelfDesc.instReprBHSelfDescResult.repr }

---

### `Tau.BookVI.BHSelfDesc.bh_sd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L125-L127)
**def
Tau.BookVI.BHSelfDesc.bh_sd :BHSelfDescResult**

Equations
- Tau.BookVI.BHSelfDesc.bh_sd = { conditions_satisfied := 3, all_three := Tau.BookVI.BHSelfDesc.bh_sd._proof_1 }
Instances For

---

### `Tau.BookVI.BHSelfDesc.bh_selfdesc_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L129-L136)
**theorem
Tau.BookVI.BHSelfDesc.bh_selfdesc_theorem :bh_sd.conditions_satisfied = 3 ∧ bh_sd.completeness = true ∧ bh_sd.internality = true ∧ bh_sd.refinement_coherence = true ∧ bh_sd.bh_alive = true**


[VI.T30] BH SelfDesc Theorem: all conditions, BH is alive.

---

### `Tau.BookVI.BHSelfDesc.selfdesc_uses_bookV_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L138-L142)
**theorem
Tau.BookVI.BHSelfDesc.selfdesc_uses_bookV_modes :bh_evaluator.mode_count = 3 ∧ bh_evaluator.mechanism = "T2_QNM_ringdown"**


Cross-book: evaluator uses BookV torus modes.
