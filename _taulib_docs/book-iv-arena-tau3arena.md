---
layout: taulib-doc
title: "TauLib.BookIV.Arena.Tau3Arena"
permalink: /verify/taulib/docs/book-iv-arena-tau3arena/
lane: verify
module_name: "TauLib.BookIV.Arena.Tau3Arena"
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

# TauLib.BookIV.Arena.Tau3Arena


The τ³ = τ¹ ×_f T² arena: base, fiber, fibered product, master constant,
and the 4-dimensional physical reading.

## Registry Cross-References


- [IV.D252] Base τ¹ — `Tau1Base`

- [IV.D253] Fiber T² — `FiberT2`

- [IV.D254] Fibered product arena τ³ — `Tau3Arena`

- [IV.D255] Master constant ι<sub>τ</sub> — `master_constant`

- [IV.P149] Quasi-ergodicity — `quasi_ergodic`

- [IV.R211] One constant to rule them all — (structural remark)

- [IV.R212] Lean formalization — (formalization note)

- [IV.P150] Four dimensions earned — `four_dim_earned`

- [IV.R213] CR-structure — (structural remark)

- [IV.D256] Lemniscate boundary — `LemniscateBoundary`

- [IV.P151] Micro/Macro decomposition — `micro_macro_split`

- [IV.R216] The coupling connects them — (structural remark)

- [IV.D257] Chart readout homomorphism — `ChartReadout`


## Ground Truth Sources


- Chapter 4 of Book IV (2nd Edition)


---

### `Tau.BookIV.Arena.Tau1Base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L38-L52)
**structure
Tau.BookIV.Arena.Tau1Base :Type**


[IV.D252] Base τ¹ = ⟨α, π⟩: the temporal base circle carrying
gravity (D-sector, α) and weak force (A-sector, π).
Physically: 1 temporal dimension.

- gen_count : ℕ
Base generators (exactly 2).

- gen_count_eq : self.gen_count = 2
Two base generators.

- gravity_gen : Kernel.Generator
Gravity generator.

- gravity_is_alpha : self.gravity_gen = Kernel.Generator.alpha
- weak_gen : Kernel.Generator
Weak generator.

- weak_is_pi : self.weak_gen = Kernel.Generator.pi
Instances For

---

### `Tau.BookIV.Arena.instReprTau1Base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L52-L52)
**instance
Tau.BookIV.Arena.instReprTau1Base :Repr Tau1Base**

Equations
- Tau.BookIV.Arena.instReprTau1Base = { reprPrec := Tau.BookIV.Arena.instReprTau1Base.repr }

---

### `Tau.BookIV.Arena.instReprTau1Base.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L52-L52)
**def
Tau.BookIV.Arena.instReprTau1Base.repr :Tau1Base → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.tau1_base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L54-L61)
**def
Tau.BookIV.Arena.tau1_base :Tau1Base**


The canonical base τ¹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.FiberT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L67-L83)
**structure
Tau.BookIV.Arena.FiberT2 :Type**


[IV.D253] Fiber T² = ⟨γ, η, ω⟩: the spatial fiber torus carrying
EM (B-sector, γ), strong (C-sector, η), and Higgs (ω-sector).
Physically: 3 spatial dimensions.

- gen_count : ℕ
Fiber generators (exactly 3).

- gen_count_eq : self.gen_count = 3
- em_gen : Kernel.Generator
EM generator.

- em_is_gamma : self.em_gen = Kernel.Generator.gamma
- strong_gen : Kernel.Generator
Strong generator.

- strong_is_eta : self.strong_gen = Kernel.Generator.eta
- higgs_gen : Kernel.Generator
Higgs generator (crossing).

- higgs_is_omega : self.higgs_gen = Kernel.Generator.omega
Instances For

---

### `Tau.BookIV.Arena.instReprFiberT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L83-L83)
**instance
Tau.BookIV.Arena.instReprFiberT2 :Repr FiberT2**

Equations
- Tau.BookIV.Arena.instReprFiberT2 = { reprPrec := Tau.BookIV.Arena.instReprFiberT2.repr }

---

### `Tau.BookIV.Arena.instReprFiberT2.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L83-L83)
**def
Tau.BookIV.Arena.instReprFiberT2.repr :FiberT2 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.fiber_t2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L85-L94)
**def
Tau.BookIV.Arena.fiber_t2 :FiberT2**


The canonical fiber T².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.Tau3Arena`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L100-L110)
**structure
Tau.BookIV.Arena.Tau3Arena :Type**


[IV.D254] The arena τ³ = τ¹ ×_f T²: fibered product of base and fiber.
Total generators: 2 + 3 = 5. Total physical dimensions: 1 + 3 = 4.

- base : Tau1Base
The temporal base.

- fiber : FiberT2
The spatial fiber.

- total_gens : ℕ
Total generator count.

- total_eq : self.total_gens = self.base.gen_count + self.fiber.gen_count
Instances For

---

### `Tau.BookIV.Arena.instReprTau3Arena`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L110-L110)
**instance
Tau.BookIV.Arena.instReprTau3Arena :Repr Tau3Arena**

Equations
- Tau.BookIV.Arena.instReprTau3Arena = { reprPrec := Tau.BookIV.Arena.instReprTau3Arena.repr }

---

### `Tau.BookIV.Arena.instReprTau3Arena.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L110-L110)
**def
Tau.BookIV.Arena.instReprTau3Arena.repr :Tau3Arena → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.tau3_arena`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L112-L117)
**def
Tau.BookIV.Arena.tau3_arena :Tau3Arena**


The canonical τ³ arena.
Equations
- Tau.BookIV.Arena.tau3_arena = { base := Tau.BookIV.Arena.tau1_base, fiber := Tau.BookIV.Arena.fiber_t2, total_gens := 5,
 total_eq := Tau.BookIV.Arena.tau3_arena._proof_1 }
Instances For

---

### `Tau.BookIV.Arena.MasterConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L123-L135)
**structure
Tau.BookIV.Arena.MasterConstant :Type**


[IV.D255] The master constant ι<sub>τ</sub> = 2/(π+e) ≈ 0.341304.
Represented as the Nat pair (341304, 1000000) from TauLib.Boundary.Iota.
All couplings, masses, and constants derive from this single number.

- numer : ℕ
Numerator at scale 10⁶.

- denom : ℕ
Denominator at scale 10⁶.

- numer_eq : self.numer = Boundary.iota_tau_numer
The specific values.

- denom_eq : self.denom = Boundary.iota_tau_denom
- denom_pos : self.denom > 0
Denominator positive.

Instances For

---

### `Tau.BookIV.Arena.master_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L137-L143)
**def
Tau.BookIV.Arena.master_constant :MasterConstant**


The canonical master constant.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.quasi_ergodic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L149-L157)
**theorem
Tau.BookIV.Arena.quasi_ergodic :Sectors.gravity_sector.coupling_numer > 0 ∧ Sectors.weak_sector.coupling_numer > 0 ∧ Sectors.em_sector.coupling_numer > 0 ∧ Sectors.strong_sector.coupling_numer > 0 ∧ Sectors.higgs_sector.coupling_numer > 0**


[IV.P149] Quasi-ergodicity: every sector contributes to every sufficiently
deep orbit level. Formalized: all 5 sectors are active (positive coupling).

---

### `Tau.BookIV.Arena.four_dim_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L163-L168)
**theorem
Tau.BookIV.Arena.four_dim_earned :tau1_base.gen_count + fiber_t2.gen_count = 5 ∧ tau1_base.gen_count = 2 ∧ fiber_t2.gen_count = 3**


[IV.P150] Four dimensions earned: 2 base generators + 3 fiber generators
= 1 temporal + 3 spatial = 4 physical dimensions.

---

### `Tau.BookIV.Arena.LemniscateBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L183-L193)
**structure
Tau.BookIV.Arena.LemniscateBoundary :Type**


[IV.D256] The lemniscate boundary L = S¹ ∨ S¹: algebraic lemniscate
arising as the boundary of τ³. Two lobes (χ₊, χ₋) meeting at the
crossing point ω.

- lobe_count : ℕ
Number of lobes.

- lobe_count_eq : self.lobe_count = 2
- has_crossing : Bool
Has a crossing point (ω).

- crossing_true : self.has_crossing = true
Instances For

---

### `Tau.BookIV.Arena.instReprLemniscateBoundary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L193-L193)
**def
Tau.BookIV.Arena.instReprLemniscateBoundary.repr :LemniscateBoundary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprLemniscateBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L193-L193)
**instance
Tau.BookIV.Arena.instReprLemniscateBoundary :Repr LemniscateBoundary**

Equations
- Tau.BookIV.Arena.instReprLemniscateBoundary = { reprPrec := Tau.BookIV.Arena.instReprLemniscateBoundary.repr }

---

### `Tau.BookIV.Arena.lemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L195-L200)
**def
Tau.BookIV.Arena.lemniscate :LemniscateBoundary**


The canonical lemniscate boundary.
Equations
- Tau.BookIV.Arena.lemniscate = { lobe_count := 2, lobe_count_eq := Tau.BookIV.Arena.tau1_base._proof_1, has_crossing := true, crossing_true := ⋯ }
Instances For

---

### `Tau.BookIV.Arena.micro_macro_split`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L206-L210)
**theorem
Tau.BookIV.Arena.micro_macro_split :fiber_t2.gen_count = 3 ∧ tau1_base.gen_count = 2**


[IV.P151] Physics splits into microcosm (fiber T², Book IV)
and macrocosm (base τ¹, Book V).

---

### `Tau.BookIV.Arena.ChartReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L219-L237)
**structure
Tau.BookIV.Arena.ChartReadout :Type**


[IV.D257] Chart readout homomorphism: the map R: τ³ → ℝ⁴ that projects
categorical structure to measurable coordinates.
Target dimension = 1 (temporal) + 3 (spatial) = 4.

- source_dim : ℕ
Source dimension (generators).

- source_eq : self.source_dim = 5
- target_dim : ℕ
Target dimension (physical).

- target_eq : self.target_dim = 4
- temporal : ℕ
Temporal dimensions in target.

- temporal_eq : self.temporal = 1
- spatial : ℕ
Spatial dimensions in target.

- spatial_eq : self.spatial = 3
- dim_sum : self.temporal + self.spatial = self.target_dim
Sum check.

Instances For

---

### `Tau.BookIV.Arena.instReprChartReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L237-L237)
**instance
Tau.BookIV.Arena.instReprChartReadout :Repr ChartReadout**

Equations
- Tau.BookIV.Arena.instReprChartReadout = { reprPrec := Tau.BookIV.Arena.instReprChartReadout.repr }

---

### `Tau.BookIV.Arena.instReprChartReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L237-L237)
**def
Tau.BookIV.Arena.instReprChartReadout.repr :ChartReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.chart_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/Tau3Arena.lean#L239-L249)
**def
Tau.BookIV.Arena.chart_readout :ChartReadout**


The canonical chart readout.
Equations
- One or more equations did not get rendered due to their size.
Instances For
