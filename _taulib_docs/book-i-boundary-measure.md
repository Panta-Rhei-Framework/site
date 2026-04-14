---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Measure"
permalink: /verify/taulib/docs/book-i-boundary-measure/
lane: verify
module_name: "TauLib.BookI.Boundary.Measure"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Boundary.Measure


Constructive measure theory on the primorial tower.

## Registry Cross-References


- [I.D95] τ-Measure Space — `TauMeasureSpace`, `tau_measure_check`

- [I.D96] Tower σ-Algebra — `TowerSigmaAlgebra`, `sigma_algebra_check`

- [I.T49] Countable Additivity — `countable_additivity_check`

- [I.P43] Measure Compatibility — `measure_compatibility_check`


## Mathematical Content


**I.D95 (τ-Measure Space):** At each primorial stage k, the set Z/M_k Z
carries the normalized counting measure μ_k(S) = |S| / M_k. This is the
unique translation-invariant probability measure on the finite cyclic group.
The τ-measure space is the projective family (Z/M_k Z, μ_k)_{k≥1}.

**I.D96 (Tower σ-Algebra):** At finite stage k, every subset of Z/M_k Z is
measurable (the σ-algebra is the full power set). A "tower-measurable" set is
a compatible family of subsets S_k ⊆ Z/M_k Z such that the preimage of S_k
under reduction is S_{k+1} ∩ Z/M_{k+1} Z.

**I.T49 (Countable Additivity):** The stage-k measure is finitely additive
(trivially, since Z/M_k Z is finite). Tower compatibility ensures that
measures at different stages agree: μ_{k+1}(π^{-1}(S_k)) = μ_k(S_k),
where π is the reduction map.

**I.P43 (Measure Compatibility):** The projective family of measures is
compatible: for any tower-measurable set, the measure is independent of
the stage at which it is evaluated.

---

### `Tau.Boundary.count_satisfying`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L49-L57)
**def
Tau.Boundary.count_satisfying
(p : ℕ → Bool)

(k : ℕ)
 :ℕ**


[I.D95] Count elements of a predicate-defined subset of Z/M_k Z.
count_satisfying p k = |{x ∈ [0, M_k) : p(x) = true}|.
Equations
- Tau.Boundary.count_satisfying p k = Tau.Boundary.count_satisfying.go p 0 (Tau.Polarity.primorial k) 0
Instances For

---

### `Tau.Boundary.count_satisfying.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L54-L56)@[irreducible]

**def
Tau.Boundary.count_satisfying.go
(p : ℕ → Bool)

(x bound acc : ℕ)
 :ℕ**

Equations
- Tau.Boundary.count_satisfying.go p x bound acc = if x ≥ bound then acc else Tau.Boundary.count_satisfying.go p (x + 1) bound (if p x = true then acc + 1 else acc)
Instances For

---

### `Tau.Boundary.StageMeasure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L59-L64)
**structure
Tau.Boundary.StageMeasure :Type**


[I.D95] The normalized counting measure: μ_k(S) as a rational
pair (numerator, denominator) = (|S|, M_k).

- numerator : ℕ
- denominator : ℕ
Instances For

---

### `Tau.Boundary.instReprStageMeasure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L64-L64)
**def
Tau.Boundary.instReprStageMeasure.repr :StageMeasure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.instReprStageMeasure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L64-L64)
**instance
Tau.Boundary.instReprStageMeasure :Repr StageMeasure**

Equations
- Tau.Boundary.instReprStageMeasure = { reprPrec := Tau.Boundary.instReprStageMeasure.repr }

---

### `Tau.Boundary.stage_measure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L66-L71)
**def
Tau.Boundary.stage_measure
(p : ℕ → Bool)

(k : ℕ)
 :StageMeasure**


[I.D95] Compute the stage-k measure of a predicate-defined subset.
Equations
- Tau.Boundary.stage_measure p k = { numerator := Tau.Boundary.count_satisfying p k, denominator := Tau.Polarity.primorial k }
Instances For

---

### `Tau.Boundary.TowerMeasurableSet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L77-L80)
**structure
Tau.Boundary.TowerMeasurableSet :Type**


[I.D96] A tower-measurable set is a family of predicates, one per stage,
that are compatible under the reduction map.

- predicate : ℕ → ℕ → Bool
Instances For

---

### `Tau.Boundary.tower_compatible_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L82-L94)
**def
Tau.Boundary.tower_compatible_check
(tms : TowerMeasurableSet)

(k : ℕ)
 :Bool**


[I.D96] Check tower compatibility at stages k and k+1:
x satisfies S_{k+1} implies reduce(x, k) satisfies S_k.
Equations
- Tau.Boundary.tower_compatible_check tms k = Tau.Boundary.tower_compatible_check.go tms k 0 (Tau.Polarity.primorial (k + 1))
Instances For

---

### `Tau.Boundary.tower_compatible_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L87-L93)@[irreducible]

**def
Tau.Boundary.tower_compatible_check.go
(tms : TowerMeasurableSet)

(k x bound : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.sigma_algebra_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L96-L104)
**def
Tau.Boundary.sigma_algebra_check
(tms : TowerMeasurableSet)

(db : ℕ)
 :Bool**


[I.D96] Check tower compatibility for all stages 1..db.
Equations
- Tau.Boundary.sigma_algebra_check tms db = Tau.Boundary.sigma_algebra_check.go tms db 1 (db + 1)
Instances For

---

### `Tau.Boundary.sigma_algebra_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L100-L103)@[irreducible]

**def
Tau.Boundary.sigma_algebra_check.go
(tms : TowerMeasurableSet)

(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.disjoint_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L110-L120)
**def
Tau.Boundary.disjoint_check
(p q : ℕ → Bool)

(k : ℕ)
 :Bool**


[I.T49] Disjoint union measure check: for predicates p, q with
p ∩ q = ∅ at stage k, verify μ(p ∪ q) = μ(p) + μ(q).
Equations
- Tau.Boundary.disjoint_check p q k = Tau.Boundary.disjoint_check.go p q 0 (Tau.Polarity.primorial k)
Instances For

---

### `Tau.Boundary.disjoint_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L115-L119)@[irreducible]

**def
Tau.Boundary.disjoint_check.go
(p q : ℕ → Bool)

(x bound : ℕ)
 :Bool**

Equations
- Tau.Boundary.disjoint_check.go p q x bound = if x ≥ bound then true
 else have ok := !(p x && q x);
 ok && Tau.Boundary.disjoint_check.go p q (x + 1) bound
Instances For

---

### `Tau.Boundary.countable_additivity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L122-L129)
**def
Tau.Boundary.countable_additivity_check
(p q : ℕ → Bool)

(k : ℕ)
 :Bool**


[I.T49] Additivity check: if p ∩ q = ∅, then |p ∪ q| = |p| + |q|.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.measure_compatibility_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L135-L144)
**def
Tau.Boundary.measure_compatibility_check
(tms : TowerMeasurableSet)

(k : ℕ)
 :Bool**


[I.P43] Measure compatibility check: the measure of a tower-measurable
set at stage k+1 (projected down) equals the measure at stage k.
Formally: count_{k+1}(S_{k+1}) / M_{k+1} = count_k(S_k) / M_k
i.e., count_{k+1}(S_{k+1}) * M_k = count_k(S_k) * M_{k+1}.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.measure_compatibility_full`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L146-L154)
**def
Tau.Boundary.measure_compatibility_full
(tms : TowerMeasurableSet)

(db : ℕ)
 :Bool**


[I.P43] Full measure compatibility for stages 1..db.
Equations
- Tau.Boundary.measure_compatibility_full tms db = Tau.Boundary.measure_compatibility_full.go tms db 1 (db + 1)
Instances For

---

### `Tau.Boundary.measure_compatibility_full.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L150-L153)@[irreducible]

**def
Tau.Boundary.measure_compatibility_full.go
(tms : TowerMeasurableSet)

(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.full_set`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L160-L162)
**def
Tau.Boundary.full_set :TowerMeasurableSet**


The full set: every element satisfies the predicate.
Equations
- Tau.Boundary.full_set = { predicate := fun (x x_1 : ℕ) => true }
Instances For

---

### `Tau.Boundary.empty_set`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L164-L166)
**def
Tau.Boundary.empty_set :TowerMeasurableSet**


The empty set: no element satisfies the predicate.
Equations
- Tau.Boundary.empty_set = { predicate := fun (x x_1 : ℕ) => false }
Instances For

---

### `Tau.Boundary.even_set`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L168-L170)
**def
Tau.Boundary.even_set :TowerMeasurableSet**


Even elements at each stage.
Equations
- Tau.Boundary.even_set = { predicate := fun (x x_1 : ℕ) => x_1 % 2 == 0 }
Instances For

---

### `Tau.Boundary.b_sector_set`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L172-L174)
**def
Tau.Boundary.b_sector_set :TowerMeasurableSet**


B-sector elements (≡ 1 mod 4) at each stage.
Equations
- Tau.Boundary.b_sector_set = { predicate := fun (x x_1 : ℕ) => x_1 % 4 == 1 }
Instances For

---

### `Tau.Boundary.primorial_pos_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L180-L181)
**theorem
Tau.Boundary.primorial_pos_1 :Polarity.primorial 1 > 0**


[I.D95] Primorial is always positive (stages 1-3).

---

### `Tau.Boundary.primorial_pos_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L182-L182)
**theorem
Tau.Boundary.primorial_pos_2 :Polarity.primorial 2 > 0**


---

### `Tau.Boundary.primorial_pos_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L183-L183)
**theorem
Tau.Boundary.primorial_pos_3 :Polarity.primorial 3 > 0**


---

### `Tau.Boundary.additivity_even_odd_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L185-L188)
**theorem
Tau.Boundary.additivity_even_odd_3 :countable_additivity_check (fun (x : ℕ) => x % 2 == 0) (fun (x : ℕ) => x % 2 == 1) 3 = true**


[I.T49] Additivity for even/odd partition at stage 3.

---

### `Tau.Boundary.additivity_bc_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L190-L193)
**theorem
Tau.Boundary.additivity_bc_3 :countable_additivity_check (fun (x : ℕ) => x % 4 == 1) (fun (x : ℕ) => x % 4 == 3) 3 = true**


[I.T49] Additivity for B/C sector partition at stage 3.

---

### `Tau.Boundary.full_set_compatible_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L195-L197)
**theorem
Tau.Boundary.full_set_compatible_3 :sigma_algebra_check full_set 3 = true**


[I.P43] Full set is tower-compatible up to stage 3.

---

### `Tau.Boundary.empty_set_compatible_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L199-L201)
**theorem
Tau.Boundary.empty_set_compatible_3 :sigma_algebra_check empty_set 3 = true**


[I.P43] Empty set is tower-compatible up to stage 3.

---

### `Tau.Boundary.even_set_compatible_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L203-L205)
**theorem
Tau.Boundary.even_set_compatible_3 :sigma_algebra_check even_set 3 = true**


[I.P43] Even set is tower-compatible up to stage 3.

---

### `Tau.Boundary.full_set_measure_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L207-L209)
**theorem
Tau.Boundary.full_set_measure_3 :count_satisfying (fun (x : ℕ) => true) 3 = Polarity.primorial 3**


[I.D95] Full set measure at stage 3: M_3 / M_3 = 1.

---

### `Tau.Boundary.empty_set_measure_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L211-L213)
**theorem
Tau.Boundary.empty_set_measure_3 :count_satisfying (fun (x : ℕ) => false) 3 = 0**


[I.D95] Empty set measure at stage 3: 0 / M_3 = 0.

---

### `Tau.Boundary.TauMeasureSpace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L219-L223)
**structure
Tau.Boundary.TauMeasureSpace :Type**


[I.D95] The τ-measure space: a collection of stages with
compatible counting measures.

- max_stage : ℕ
- measurable_sets : List TowerMeasurableSet
Instances For

---

### `Tau.Boundary.tau_measure_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Measure.lean#L225-L227)
**def
Tau.Boundary.tau_measure_check
(tms : TauMeasureSpace)
 :Bool**


[I.D95] Validate a τ-measure space: all sets tower-compatible.
Equations
- Tau.Boundary.tau_measure_check tms = tms.measurable_sets.all fun (s : Tau.Boundary.TowerMeasurableSet) => Tau.Boundary.sigma_algebra_check s tms.max_stage
Instances For
