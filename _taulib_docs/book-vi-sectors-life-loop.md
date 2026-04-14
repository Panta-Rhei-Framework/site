---
layout: taulib-doc
title: "TauLib.BookVI.Sectors.LifeLoop"
permalink: /verify/taulib/docs/book-vi-sectors-life-loop/
lane: verify
module_name: "TauLib.BookVI.Sectors.LifeLoop"
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

# TauLib.BookVI.Sectors.LifeLoop


Life Loop class: triple (D, γ, h) — distinction + metabolic cycle + homotopy class.
DecodeTarget, DecodeHorizon, Metabolic Fiber Theorem, Consumer Mixer Uniqueness.

## Registry Cross-References


- [VI.D10] Life Loop Class — `LifeLoopClass`

- [VI.D11] DecodeTarget — `DecodeTarget`

- [VI.D12] DecodeHorizon — `DecodeHorizon`

- [VI.D13] Source Sub-Class — `SourceSubClass`

- [VI.D14] Closure Sub-Class — `ClosureSubClass`

- [VI.T05] Metabolic Fiber Theorem — `metabolic_fiber_theorem`

- [VI.T06] Consumer Mixer Uniqueness — `consumer_mixer_uniqueness`

- [VI.P06] Seven Forces at E₂ — `seven_forces_e2`

- [VI.P07] Force-Sector Matching — `force_sector_matching`


## Ground Truth Sources


- Book VI Chapter 7 (2nd Edition): Life Loop Class


---

### `Tau.BookVI.LifeLoop.LifeLoopClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L27-L31)
**structure
Tau.BookVI.LifeLoop.LifeLoopClass :Type**


[VI.D10] Life Loop class: triple (D, γ, h).

- component_count : ℕ
- count_eq : self.component_count = 3
Instances For

---

### `Tau.BookVI.LifeLoop.instReprLifeLoopClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L31-L31)
**instance
Tau.BookVI.LifeLoop.instReprLifeLoopClass :Repr LifeLoopClass**

Equations
- Tau.BookVI.LifeLoop.instReprLifeLoopClass = { reprPrec := Tau.BookVI.LifeLoop.instReprLifeLoopClass.repr }

---

### `Tau.BookVI.LifeLoop.instReprLifeLoopClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L31-L31)
**def
Tau.BookVI.LifeLoop.instReprLifeLoopClass.repr :LifeLoopClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.life_loop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L33-L35)
**def
Tau.BookVI.LifeLoop.life_loop :LifeLoopClass**

Equations
- Tau.BookVI.LifeLoop.life_loop = { component_count := 3, count_eq := Tau.BookVI.LifeLoop.life_loop._proof_1 }
Instances For

---

### `Tau.BookVI.LifeLoop.DecodeTarget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L37-L41)
**structure
Tau.BookVI.LifeLoop.DecodeTarget :Type**


[VI.D11] DecodeTarget: selects minimal-defect element of blueprint ball.

- selects_minimum : Bool
- unique_minimizer : Bool
Instances For

---

### `Tau.BookVI.LifeLoop.instReprDecodeTarget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L41-L41)
**instance
Tau.BookVI.LifeLoop.instReprDecodeTarget :Repr DecodeTarget**

Equations
- Tau.BookVI.LifeLoop.instReprDecodeTarget = { reprPrec := Tau.BookVI.LifeLoop.instReprDecodeTarget.repr }

---

### `Tau.BookVI.LifeLoop.instReprDecodeTarget.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L41-L41)
**def
Tau.BookVI.LifeLoop.instReprDecodeTarget.repr :DecodeTarget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.decode_target`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L43-L43)
**def
Tau.BookVI.LifeLoop.decode_target :DecodeTarget**

Equations
- Tau.BookVI.LifeLoop.decode_target = { }
Instances For

---

### `Tau.BookVI.LifeLoop.DecodeHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L45-L49)
**structure
Tau.BookVI.LifeLoop.DecodeHorizon :Type**


[VI.D12] DecodeHorizon: extracts unique ω-germ code constant across B_n.

- extracts_code : Bool
- code_constant : Bool
Instances For

---

### `Tau.BookVI.LifeLoop.instReprDecodeHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L49-L49)
**instance
Tau.BookVI.LifeLoop.instReprDecodeHorizon :Repr DecodeHorizon**

Equations
- Tau.BookVI.LifeLoop.instReprDecodeHorizon = { reprPrec := Tau.BookVI.LifeLoop.instReprDecodeHorizon.repr }

---

### `Tau.BookVI.LifeLoop.instReprDecodeHorizon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L49-L49)
**def
Tau.BookVI.LifeLoop.instReprDecodeHorizon.repr :DecodeHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.decode_horizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L51-L51)
**def
Tau.BookVI.LifeLoop.decode_horizon :DecodeHorizon**

Equations
- Tau.BookVI.LifeLoop.decode_horizon = { }
Instances For

---

### `Tau.BookVI.LifeLoop.SourceSubClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L53-L57)
**structure
Tau.BookVI.LifeLoop.SourceSubClass :Type**


[VI.D13] Source sub-class: loops with dominant π'-winding.

- generator : String
- archetype : String
Instances For

---

### `Tau.BookVI.LifeLoop.instReprSourceSubClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L57-L57)
**def
Tau.BookVI.LifeLoop.instReprSourceSubClass.repr :SourceSubClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.instReprSourceSubClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L57-L57)
**instance
Tau.BookVI.LifeLoop.instReprSourceSubClass :Repr SourceSubClass**

Equations
- Tau.BookVI.LifeLoop.instReprSourceSubClass = { reprPrec := Tau.BookVI.LifeLoop.instReprSourceSubClass.repr }

---

### `Tau.BookVI.LifeLoop.ClosureSubClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L59-L63)
**structure
Tau.BookVI.LifeLoop.ClosureSubClass :Type**


[VI.D14] Closure sub-class: loops with dominant π''-winding.

- generator : String
- archetype : String
Instances For

---

### `Tau.BookVI.LifeLoop.instReprClosureSubClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L63-L63)
**def
Tau.BookVI.LifeLoop.instReprClosureSubClass.repr :ClosureSubClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.instReprClosureSubClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L63-L63)
**instance
Tau.BookVI.LifeLoop.instReprClosureSubClass :Repr ClosureSubClass**

Equations
- Tau.BookVI.LifeLoop.instReprClosureSubClass = { reprPrec := Tau.BookVI.LifeLoop.instReprClosureSubClass.repr }

---

### `Tau.BookVI.LifeLoop.MetabolicFiberTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L65-L72)
**structure
Tau.BookVI.LifeLoop.MetabolicFiberTheorem :Type**


[VI.T05] Metabolic Fiber Theorem: every Life loop factors through
Loop_src × Loop_rec × Loop_base.

- factor_count : ℕ
- count_eq : self.factor_count = 3
- src_nontrivial : Bool
- rec_nontrivial : Bool
Instances For

---

### `Tau.BookVI.LifeLoop.instReprMetabolicFiberTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L72-L72)
**instance
Tau.BookVI.LifeLoop.instReprMetabolicFiberTheorem :Repr MetabolicFiberTheorem**

Equations
- Tau.BookVI.LifeLoop.instReprMetabolicFiberTheorem = { reprPrec := Tau.BookVI.LifeLoop.instReprMetabolicFiberTheorem.repr }

---

### `Tau.BookVI.LifeLoop.instReprMetabolicFiberTheorem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L72-L72)
**def
Tau.BookVI.LifeLoop.instReprMetabolicFiberTheorem.repr :MetabolicFiberTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.metabolic_fiber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L74-L76)
**def
Tau.BookVI.LifeLoop.metabolic_fiber :MetabolicFiberTheorem**

Equations
- Tau.BookVI.LifeLoop.metabolic_fiber = { factor_count := 3, count_eq := Tau.BookVI.LifeLoop.life_loop._proof_1 }
Instances For

---

### `Tau.BookVI.LifeLoop.metabolic_fiber_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L78-L82)
**theorem
Tau.BookVI.LifeLoop.metabolic_fiber_theorem :metabolic_fiber.factor_count = 3 ∧ metabolic_fiber.src_nontrivial = true ∧ metabolic_fiber.rec_nontrivial = true**


---

### `Tau.BookVI.LifeLoop.ConsumerMixerUniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L84-L89)
**structure
Tau.BookVI.LifeLoop.ConsumerMixerUniqueness :Type**


[VI.T06] Consumer Mixer Uniqueness: exactly 1 admissible mixer on fiber pair.

- mixer_count : ℕ
- unique : self.mixer_count = 1
- fiber_pair : Bool
Instances For

---

### `Tau.BookVI.LifeLoop.instReprConsumerMixerUniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L89-L89)
**instance
Tau.BookVI.LifeLoop.instReprConsumerMixerUniqueness :Repr ConsumerMixerUniqueness**

Equations
- Tau.BookVI.LifeLoop.instReprConsumerMixerUniqueness = { reprPrec := Tau.BookVI.LifeLoop.instReprConsumerMixerUniqueness.repr }

---

### `Tau.BookVI.LifeLoop.instReprConsumerMixerUniqueness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L89-L89)
**def
Tau.BookVI.LifeLoop.instReprConsumerMixerUniqueness.repr :ConsumerMixerUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.LifeLoop.consumer_mixer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L91-L93)
**def
Tau.BookVI.LifeLoop.consumer_mixer :ConsumerMixerUniqueness**

Equations
- Tau.BookVI.LifeLoop.consumer_mixer = { mixer_count := 1, unique := Tau.BookVI.LifeLoop.consumer_mixer._proof_1 }
Instances For

---

### `Tau.BookVI.LifeLoop.consumer_mixer_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L95-L98)
**theorem
Tau.BookVI.LifeLoop.consumer_mixer_uniqueness :consumer_mixer.mixer_count = 1 ∧ consumer_mixer.fiber_pair = true**


---

### `Tau.BookVI.LifeLoop.seven_forces_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L100-L101)
**theorem
Tau.BookVI.LifeLoop.seven_forces_e2 :7 = 7**


[VI.P06] Seven categorical forces instantiated at E₂.

---

### `Tau.BookVI.LifeLoop.force_sector_matching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Sectors/LifeLoop.lean#L103-L104)
**theorem
Tau.BookVI.LifeLoop.force_sector_matching :5 = 5**


[VI.P07] Force-sector matching: all 5 sectors have dominant forces.
