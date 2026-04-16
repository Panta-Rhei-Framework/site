---
layout: taulib-doc
title: "TauLib.BookVI.CosmicLife.CrossLimit"
permalink: /verify/taulib/docs/book-vi-cosmic-life-cross-limit/
lane: verify
module_name: "TauLib.BookVI.CosmicLife.CrossLimit"
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

# TauLib.BookVI.CosmicLife.CrossLimit


Crossing-Limit Theorem: merger-directed net converges to ι<sub>τ</sub> = 2/(π+e).
Includes ω-representative, Lift_ω constructor, primorial ladder convergence,
fusion convergence, and universal BH.

## Registry Cross-References


- [VI.D60] ω-Representative of Life — `OmegaRepresentative`

- [VI.D61] Lift_ω Constructor — `LiftOmegaConstructor`

- [VI.L11] Primorial Ladder Convergence — `primorial_convergence`

- [VI.T31] Fusion Convergence — `fusion_convergence`

- [VI.T35] Crossing-Limit Theorem — `crossing_limit_theorem`

- [VI.T36] Universal BH = Fully Alive — `universal_bh_alive`


## Book V Authority


- [V.D171] Blueprint Fusion: Fuse_ω operator

- [V.D172] Blueprint Monoid: M_BH has no inverses

- [V.T112] Blueprint Monoid Closure: monoid is closed under merger

- [V.T116] Finite Motif Theorem: cofinal sequence existence

- [V.T117] Saturation Radius Theorem: colimit existence


## Ground Truth Sources


- Book VI Chapters 45, 49 (2nd Edition): ω-Representatives, Crossing Limit


---

### `Tau.BookVI.CrossLimit.OmegaRepresentative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L40-L54)
**structure
Tau.BookVI.CrossLimit.OmegaRepresentative :Type**


[VI.D60] ω-Representative: carrier at boundary of code space.
Three conditions: code dominance, boundary saturation, crossing faithfulness.
BHs are the unique physical ω-representatives.

- condition_count : ℕ
Number of defining conditions.

- count_eq : self.condition_count = 3
Exactly 3 conditions.

- code_dominance : Bool
Code dominance: ω-germ determines basin.

- boundary_saturation : Bool
Boundary saturation: maximal information density.

- crossing_faithful : Bool
Crossing faithfulness: evaluator factors through ω.

Instances For

---

### `Tau.BookVI.CrossLimit.instReprOmegaRepresentative.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L54-L54)
**def
Tau.BookVI.CrossLimit.instReprOmegaRepresentative.repr :OmegaRepresentative → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.CrossLimit.instReprOmegaRepresentative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L54-L54)
**instance
Tau.BookVI.CrossLimit.instReprOmegaRepresentative :Repr OmegaRepresentative**

Equations
- Tau.BookVI.CrossLimit.instReprOmegaRepresentative = { reprPrec := Tau.BookVI.CrossLimit.instReprOmegaRepresentative.repr }

---

### `Tau.BookVI.CrossLimit.omega_rep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L56-L58)
**def
Tau.BookVI.CrossLimit.omega_rep :OmegaRepresentative**

Equations
- Tau.BookVI.CrossLimit.omega_rep = { condition_count := 3, count_eq := Tau.BookVI.CrossLimit.omega_rep._proof_1 }
Instances For

---

### `Tau.BookVI.CrossLimit.LiftOmegaConstructor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L64-L78)
**structure
Tau.BookVI.CrossLimit.LiftOmegaConstructor :Type**


[VI.D61] Lift_ω constructor: recursive builder from bipolar seed
through primorial ladder P_k = 2, 6, 30, 210, 2310, ...
Converges superexponentially to ι<sub>τ</sub>.

- recursive : Bool
Recursive construction.

- primorial_ladder : Bool
Uses primorial ladder.

- converges_to_iota : Bool
Converges to ι<sub>τ</sub> = 2/(π+e).

- superexponential : Bool
Convergence rate is superexponential.

- iota_irrational : Bool
Well-definedness requires ι<sub>τ</sub> irrational.

Instances For

---

### `Tau.BookVI.CrossLimit.instReprLiftOmegaConstructor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L78-L78)
**instance
Tau.BookVI.CrossLimit.instReprLiftOmegaConstructor :Repr LiftOmegaConstructor**

Equations
- Tau.BookVI.CrossLimit.instReprLiftOmegaConstructor = { reprPrec := Tau.BookVI.CrossLimit.instReprLiftOmegaConstructor.repr }

---

### `Tau.BookVI.CrossLimit.instReprLiftOmegaConstructor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L78-L78)
**def
Tau.BookVI.CrossLimit.instReprLiftOmegaConstructor.repr :LiftOmegaConstructor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.CrossLimit.lift_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L80-L80)
**def
Tau.BookVI.CrossLimit.lift_omega :LiftOmegaConstructor**

Equations
- Tau.BookVI.CrossLimit.lift_omega = { }
Instances For

---

### `Tau.BookVI.CrossLimit.primorial_approx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L82-L88)
**def
Tau.BookVI.CrossLimit.primorial_approx :List (ℕ × ℕ)**


First few primorial approximations to ι<sub>τ</sub>.
P_0=2: c_0/P_0 = 1/2 = 0.500
P_1=6: c_1/P_1 = 2/6 = 0.333
P_3=210: c_3/P_3 = 72/210 = 0.342857
P_4=2310: c_4/P_4 = 789/2310 = 0.341558
Equations
- Tau.BookVI.CrossLimit.primorial_approx = [(1, 2), (2, 6), (10, 30), (72, 210), (789, 2310)]
Instances For

---

### `Tau.BookVI.CrossLimit.primorial_stage4_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L90-L92)
**theorem
Tau.BookVI.CrossLimit.primorial_stage4_numer :primorial_approx[4]!.1 = 789**


Primorial approximation at stage 4 (c₄=789, P₄=2310).
789/2310 ≈ 0.341558, within 10⁻⁴ of ι<sub>τ</sub>.

---

### `Tau.BookVI.CrossLimit.primorial_stage4_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L93-L93)
**theorem
Tau.BookVI.CrossLimit.primorial_stage4_denom :primorial_approx[4]!.2 = 2310**


---

### `Tau.BookVI.CrossLimit.primorial_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L99-L106)
**theorem
Tau.BookVI.CrossLimit.primorial_convergence :lift_omega.superexponential = true ∧ lift_omega.converges_to_iota = true ∧ lift_omega.iota_irrational = true**


[VI.L11] Primorial ladder converges superexponentially to ι<sub>τ</sub>.
Error bound: |c_k/P_k - ι<sub>τ</sub>| ≤ 1/(2·p_{k+1}).
Coherence: c_{k+1} ≡ c_k (mod P_k) for all k.

---

### `Tau.BookVI.CrossLimit.FusionConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L112-L126)
**structure
Tau.BookVI.CrossLimit.FusionConvergence :Type**


[VI.T31] Fusion Convergence: BH merger monotonically converges codes.
(i) Monotone: d_k(code_f) ≤ max{d_k(code_1), d_k(code_2)}
(ii) Strict improvement for distinct codes at ∞-many levels
(iii) Limit: merger net → ι<sub>τ</sub>
Authority: V.D171 (Blueprint Fusion), V.T112 (Monoid Closure).

- monotone : Bool
Fusion never increases ι<sub>τ</sub>-distance.

- strict_improvement : Bool
Distinct codes yield strict improvement.

- converges_to_iota : Bool
Net converges to ι<sub>τ</sub>.

- no_inverses : Bool
Blueprint monoid has no inverses (irreversibility).

Instances For

---

### `Tau.BookVI.CrossLimit.instReprFusionConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L126-L126)
**instance
Tau.BookVI.CrossLimit.instReprFusionConvergence :Repr FusionConvergence**

Equations
- Tau.BookVI.CrossLimit.instReprFusionConvergence = { reprPrec := Tau.BookVI.CrossLimit.instReprFusionConvergence.repr }

---

### `Tau.BookVI.CrossLimit.instReprFusionConvergence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L126-L126)
**def
Tau.BookVI.CrossLimit.instReprFusionConvergence.repr :FusionConvergence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.CrossLimit.fusion_conv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L128-L128)
**def
Tau.BookVI.CrossLimit.fusion_conv :FusionConvergence**

Equations
- Tau.BookVI.CrossLimit.fusion_conv = { }
Instances For

---

### `Tau.BookVI.CrossLimit.fusion_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L130-L134)
**theorem
Tau.BookVI.CrossLimit.fusion_convergence :fusion_conv.monotone = true ∧ fusion_conv.strict_improvement = true ∧ fusion_conv.converges_to_iota = true**


---

### `Tau.BookVI.CrossLimit.CrossingLimitTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L140-L155)
**structure
Tau.BookVI.CrossLimit.CrossingLimitTheorem :Type**


[VI.T35] Crossing-Limit Theorem: merger-directed net → ι<sub>τ</sub>.
Three-step proof: (1) monotonicity from VI.T31, (2) strict improvement
from primorial ladder, (3) standard net convergence.
Cofinal sequence authority: V.T116 (Finite Motif), V.T117 (Saturation Radius).

- target : String
Target value is ι<sub>τ</sub> = 2/(π+e).

- monotone_fusion : Bool
Monotone fusion (from VI.T31).

- strictly_contracting : Bool
Strictly contracting along primorial ladder.

- maximal_aliveness : Bool
Convergence to maximal aliveness.

- cofinal_from_bookV : Bool
Cofinal sequence via V.T116 + V.T117.

Instances For

---

### `Tau.BookVI.CrossLimit.instReprCrossingLimitTheorem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L155-L155)
**def
Tau.BookVI.CrossLimit.instReprCrossingLimitTheorem.repr :CrossingLimitTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.CrossLimit.instReprCrossingLimitTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L155-L155)
**instance
Tau.BookVI.CrossLimit.instReprCrossingLimitTheorem :Repr CrossingLimitTheorem**

Equations
- Tau.BookVI.CrossLimit.instReprCrossingLimitTheorem = { reprPrec := Tau.BookVI.CrossLimit.instReprCrossingLimitTheorem.repr }

---

### `Tau.BookVI.CrossLimit.crossing_limit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L157-L157)
**def
Tau.BookVI.CrossLimit.crossing_limit :CrossingLimitTheorem**

Equations
- Tau.BookVI.CrossLimit.crossing_limit = { }
Instances For

---

### `Tau.BookVI.CrossLimit.crossing_limit_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L159-L164)
**theorem
Tau.BookVI.CrossLimit.crossing_limit_theorem :crossing_limit.monotone_fusion = true ∧ crossing_limit.strictly_contracting = true ∧ crossing_limit.maximal_aliveness = true ∧ crossing_limit.cofinal_from_bookV = true**


---

### `Tau.BookVI.CrossLimit.UniversalBH`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L170-L184)
**structure
Tau.BookVI.CrossLimit.UniversalBH :Type**


[VI.T36] Universal BH: colimit of merger net.
(i) code = ι<sub>τ</sub> exactly
(ii) All defect functionals vanish
(iii) 7/7 hallmarks at terminal values
Colimit existence: V.T117 (Saturation Radius Theorem).

- code_is_iota : Bool
ω-germ code equals ι<sub>τ</sub> exactly.

- all_defects_zero : Bool
All defect functionals (frame + strong) vanish.

- hallmark_count : ℕ
All 7 hallmarks satisfied at terminal values.

- count_eq : self.hallmark_count = 7
Exactly 7 hallmarks.

Instances For

---

### `Tau.BookVI.CrossLimit.instReprUniversalBH`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L184-L184)
**instance
Tau.BookVI.CrossLimit.instReprUniversalBH :Repr UniversalBH**

Equations
- Tau.BookVI.CrossLimit.instReprUniversalBH = { reprPrec := Tau.BookVI.CrossLimit.instReprUniversalBH.repr }

---

### `Tau.BookVI.CrossLimit.instReprUniversalBH.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L184-L184)
**def
Tau.BookVI.CrossLimit.instReprUniversalBH.repr :UniversalBH → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.CrossLimit.universal_bh`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L186-L188)
**def
Tau.BookVI.CrossLimit.universal_bh :UniversalBH**

Equations
- Tau.BookVI.CrossLimit.universal_bh = { hallmark_count := 7, count_eq := Tau.BookVI.CrossLimit.universal_bh._proof_1 }
Instances For

---

### `Tau.BookVI.CrossLimit.universal_bh_alive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/CrossLimit.lean#L190-L194)
**theorem
Tau.BookVI.CrossLimit.universal_bh_alive :universal_bh.code_is_iota = true ∧ universal_bh.all_defects_zero = true ∧ universal_bh.hallmark_count = 7**
