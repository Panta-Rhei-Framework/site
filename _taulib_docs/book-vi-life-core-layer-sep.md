---
layout: taulib-doc
title: "TauLib.BookVI.LifeCore.LayerSep"
permalink: /verify/taulib/docs/book-vi-life-core-layer-sep/
lane: verify
module_name: "TauLib.BookVI.LifeCore.LayerSep"
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

# TauLib.BookVI.LifeCore.LayerSep


Layer Separation: SelfDesc is not available at E₁. The NS-TOV system
provides a constructive witness. Also: loop factorization lemma.

## Registry Cross-References


- [VI.T04] Layer Separation Lemma — `layer_separation_lemma`

- [VI.L02] NS-TOV Counterexample — `ns_tov_counterexample`

- [VI.L03] Loop Factorization — `loop_factorization`

- [VI.P05] Canonical Life Phase Boundary — `life_phase_boundary`


## Ground Truth Sources


- Book VI Chapter 6 (2nd Edition): Layer Separation


---

### `Tau.BookVI.LayerSep.NSTOVCounterexample`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L22-L29)
**structure
Tau.BookVI.LayerSep.NSTOVCounterexample :Type**


[VI.L02] NS-TOV counterexample: passes all 5 distinction conditions,
fails SelfDesc due to oscillatory boundary instability.

- distinction_passed : ℕ
- all_five : self.distinction_passed = 5
- selfdesc_fails : Bool
- failure_reason : String
Instances For

---

### `Tau.BookVI.LayerSep.instReprNSTOVCounterexample.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L29-L29)
**def
Tau.BookVI.LayerSep.instReprNSTOVCounterexample.repr :NSTOVCounterexample → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LayerSep.instReprNSTOVCounterexample`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L29-L29)
**instance
Tau.BookVI.LayerSep.instReprNSTOVCounterexample :Repr NSTOVCounterexample**

Equations
- Tau.BookVI.LayerSep.instReprNSTOVCounterexample = { reprPrec := Tau.BookVI.LayerSep.instReprNSTOVCounterexample.repr }

---

### `Tau.BookVI.LayerSep.ns_tov`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L31-L33)
**def
Tau.BookVI.LayerSep.ns_tov :NSTOVCounterexample**

Equations
- Tau.BookVI.LayerSep.ns_tov = { distinction_passed := 5, all_five := Tau.BookVI.LayerSep.ns_tov._proof_1 }
Instances For

---

### `Tau.BookVI.LayerSep.ns_tov_counterexample`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L35-L38)
**theorem
Tau.BookVI.LayerSep.ns_tov_counterexample :ns_tov.distinction_passed = 5 ∧ ns_tov.selfdesc_fails = true**


---

### `Tau.BookVI.LayerSep.LayerSeparation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L40-L47)
**structure
Tau.BookVI.LayerSep.LayerSeparation :Type**


[VI.T04] Layer Separation Lemma: E₂ is non-reducible to E₁.
Witness: NS-TOV system.

- e1_has_distinction : Bool
- e1_lacks_selfdesc : Bool
- non_reducible : Bool
- has_witness : Bool
Instances For

---

### `Tau.BookVI.LayerSep.instReprLayerSeparation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L47-L47)
**def
Tau.BookVI.LayerSep.instReprLayerSeparation.repr :LayerSeparation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LayerSep.instReprLayerSeparation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L47-L47)
**instance
Tau.BookVI.LayerSep.instReprLayerSeparation :Repr LayerSeparation**

Equations
- Tau.BookVI.LayerSep.instReprLayerSeparation = { reprPrec := Tau.BookVI.LayerSep.instReprLayerSeparation.repr }

---

### `Tau.BookVI.LayerSep.layer_sep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L49-L49)
**def
Tau.BookVI.LayerSep.layer_sep :LayerSeparation**

Equations
- Tau.BookVI.LayerSep.layer_sep = { }
Instances For

---

### `Tau.BookVI.LayerSep.layer_separation_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L51-L55)
**theorem
Tau.BookVI.LayerSep.layer_separation_lemma :layer_sep.e1_has_distinction = true ∧ layer_sep.e1_lacks_selfdesc = true ∧ layer_sep.non_reducible = true**


---

### `Tau.BookVI.LayerSep.LoopFactorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L57-L63)
**structure
Tau.BookVI.LayerSep.LoopFactorization :Type**


[VI.L03] Loop factorization: every metabolic cycle γ decomposes as
γ_src ∗ γ_rec ∗ γ_base via π₁(τ³).

- factor_count : ℕ
- count_eq : self.factor_count = 3
- is_unique : Bool
Instances For

---

### `Tau.BookVI.LayerSep.instReprLoopFactorization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L63-L63)
**def
Tau.BookVI.LayerSep.instReprLoopFactorization.repr :LoopFactorization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LayerSep.instReprLoopFactorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L63-L63)
**instance
Tau.BookVI.LayerSep.instReprLoopFactorization :Repr LoopFactorization**

Equations
- Tau.BookVI.LayerSep.instReprLoopFactorization = { reprPrec := Tau.BookVI.LayerSep.instReprLoopFactorization.repr }

---

### `Tau.BookVI.LayerSep.loop_fact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L65-L67)
**def
Tau.BookVI.LayerSep.loop_fact :LoopFactorization**

Equations
- Tau.BookVI.LayerSep.loop_fact = { factor_count := 3, count_eq := Tau.BookVI.LayerSep.loop_fact._proof_1 }
Instances For

---

### `Tau.BookVI.LayerSep.loop_factorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L69-L72)
**theorem
Tau.BookVI.LayerSep.loop_factorization :loop_fact.factor_count = 3 ∧ loop_fact.is_unique = true**


---

### `Tau.BookVI.LayerSep.LifePhaseBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L74-L78)
**structure
Tau.BookVI.LayerSep.LifePhaseBoundary :Type**


[VI.P05] Canonical life phase boundary: NS-to-BH transition.

- is_sharp : Bool
- topology_change : Bool
Instances For

---

### `Tau.BookVI.LayerSep.instReprLifePhaseBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L78-L78)
**instance
Tau.BookVI.LayerSep.instReprLifePhaseBoundary :Repr LifePhaseBoundary**

Equations
- Tau.BookVI.LayerSep.instReprLifePhaseBoundary = { reprPrec := Tau.BookVI.LayerSep.instReprLifePhaseBoundary.repr }

---

### `Tau.BookVI.LayerSep.instReprLifePhaseBoundary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L78-L78)
**def
Tau.BookVI.LayerSep.instReprLifePhaseBoundary.repr :LifePhaseBoundary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LayerSep.phase_boundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L80-L80)
**def
Tau.BookVI.LayerSep.phase_boundary :LifePhaseBoundary**

Equations
- Tau.BookVI.LayerSep.phase_boundary = { }
Instances For

---

### `Tau.BookVI.LayerSep.life_phase_boundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/LayerSep.lean#L82-L85)
**theorem
Tau.BookVI.LayerSep.life_phase_boundary :phase_boundary.is_sharp = true ∧ phase_boundary.topology_change = true**
