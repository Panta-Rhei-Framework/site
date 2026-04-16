---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.CalibratedSplitComplex"
permalink: /verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/
lane: verify
module_name: "TauLib.BookII.Hartogs.CalibratedSplitComplex"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Hartogs.CalibratedSplitComplex


Calibrated split-complex codomain H_τ^cal: the split-complex algebra
H_τ equipped with the four earned transcendental constants (π, e, j, ι<sub>τ</sub>).

## Registry Cross-References


- [II.D35] Calibrated H_τ — `CalibratedHTau`, `calibrated_htau`

- [II.R10] Geometric Meaning of e± — `geometric_meaning_check`


## Mathematical Content


H_τ^cal is H_τ with the four constants (π, e, j, ι<sub>τ</sub>) installed as
calibration data. The calibration gives the idempotents e₊, e₋
geometric meaning:


- 
e₊ = (1+j)/2 projects onto the **B-channel** (governed by γ-orbit,
calibrated by π). The B-channel carries exponent data; its
characteristic frequency is the circle winding number ~ π.


- 
e₋ = (1-j)/2 projects onto the **C-channel** (governed by η-orbit,
calibrated by e). The C-channel carries tetration height data;
its characteristic growth rate is the factorial eigenvalue ~ e.


- 
ι<sub>τ</sub> = 2/(π+e) couples the two channels: it is the unique constant
that balances the B-channel (π-calibrated) against the C-channel
(e-calibrated).


All arithmetic uses scaled integers (SCALE = 10^6) from the
Transcendentals modules, avoiding Float entirely.

---

### `Tau.BookII.Hartogs.SCALE`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L45-L47)
**def
Tau.BookII.Hartogs.SCALE :ℕ**


Common scale factor for all calibration arithmetic.
Matches the Transcendentals convention: 10^6.
Equations
- Tau.BookII.Hartogs.SCALE = 1000000
Instances For

---

### `Tau.BookII.Hartogs.CalibratedHTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L53-L68)
**structure
Tau.BookII.Hartogs.CalibratedHTau :Type**


[II.D35] Calibrated split-complex codomain H_τ^cal.
Stores the four earned transcendental constants as scaled integers.
Each field represents the constant multiplied by SCALE = 10^6.

The calibration is canonical: there is exactly one CalibratedHTau
instance derived from the earned pi, e, j, iota_tau.

- pi_cal : ℕ
π scaled by 10^6: π * 10^6 ≈ 3141592.

- e_cal : ℕ
e scaled by 10^6: e * 10^6 ≈ 2718281.

- j_cal : ℕ
j² = +1 indicator: 1 means j² = +1 (split-complex), 0 would mean i² = -1.

- iota_cal : ℕ
ι<sub>τ</sub> scaled by 10^6: ι<sub>τ</sub> * 10^6 ≈ 341304.

Instances For

---

### `Tau.BookII.Hartogs.instReprCalibratedHTau.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L68-L68)
**def
Tau.BookII.Hartogs.instReprCalibratedHTau.repr :CalibratedHTau → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.instReprCalibratedHTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L68-L68)
**instance
Tau.BookII.Hartogs.instReprCalibratedHTau :Repr CalibratedHTau**

Equations
- Tau.BookII.Hartogs.instReprCalibratedHTau = { reprPrec := Tau.BookII.Hartogs.instReprCalibratedHTau.repr }

---

### `Tau.BookII.Hartogs.instDecidableEqCalibratedHTau.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L68-L68)
**def
Tau.BookII.Hartogs.instDecidableEqCalibratedHTau.decEq
(x✝ x✝¹ : CalibratedHTau)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.instDecidableEqCalibratedHTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L68-L68)
**instance
Tau.BookII.Hartogs.instDecidableEqCalibratedHTau :DecidableEq CalibratedHTau**

Equations
- Tau.BookII.Hartogs.instDecidableEqCalibratedHTau = Tau.BookII.Hartogs.instDecidableEqCalibratedHTau.decEq

---

### `Tau.BookII.Hartogs.calibrated_htau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L70-L77)
**def
Tau.BookII.Hartogs.calibrated_htau :CalibratedHTau**


The canonical calibrated codomain, using 2000 Leibniz terms for π
and 12 factorial terms for e (matching IotaTauConfirmed).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.pi_cal_range_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L83-L86)
**def
Tau.BookII.Hartogs.pi_cal_range_check :Bool**


π calibration in expected range: π * 10^6 ∈ [3100000, 3200000].
Equations
- Tau.BookII.Hartogs.pi_cal_range_check = (decide (Tau.BookII.Hartogs.calibrated_htau.pi_cal > 3100000) && decide (Tau.BookII.Hartogs.calibrated_htau.pi_cal < 3200000))
Instances For

---

### `Tau.BookII.Hartogs.e_cal_range_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L88-L91)
**def
Tau.BookII.Hartogs.e_cal_range_check :Bool**


e calibration in expected range: e * 10^6 ∈ [2710000, 2730000].
Equations
- Tau.BookII.Hartogs.e_cal_range_check = (decide (Tau.BookII.Hartogs.calibrated_htau.e_cal > 2710000) && decide (Tau.BookII.Hartogs.calibrated_htau.e_cal < 2730000))
Instances For

---

### `Tau.BookII.Hartogs.iota_cal_range_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L93-L96)
**def
Tau.BookII.Hartogs.iota_cal_range_check :Bool**


ι<sub>τ</sub> calibration in expected range: ι<sub>τ</sub> * 10^6 ∈ [335000, 350000].
Equations
- Tau.BookII.Hartogs.iota_cal_range_check = (decide (Tau.BookII.Hartogs.calibrated_htau.iota_cal > 335000) && decide (Tau.BookII.Hartogs.calibrated_htau.iota_cal < 350000))
Instances For

---

### `Tau.BookII.Hartogs.j_squared_calibration_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L102-L107)
**def
Tau.BookII.Hartogs.j_squared_calibration_check :Bool**


j² = +1: the split-complex unit squares to the identity.
This is the algebraic foundation of the calibration:
j² = +1 ⟹ idempotents exist ⟹ bipolar decomposition.
Equations
- Tau.BookII.Hartogs.j_squared_calibration_check = (Tau.BookII.Hartogs.calibrated_htau.j_cal == 1 && Tau.Polarity.SplitComplex.j.mul Tau.Polarity.SplitComplex.j == Tau.Polarity.SplitComplex.one)
Instances For

---

### `Tau.BookII.Hartogs.orthogonality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L113-L116)
**def
Tau.BookII.Hartogs.orthogonality_check :Bool**


e₊ · e₋ = 0 (orthogonality) in sector coordinates.
Sector representation: e₊ = (1,0), e₋ = (0,1).
Equations
- Tau.BookII.Hartogs.orthogonality_check = (Tau.Polarity.e_plus_sector.mul Tau.Polarity.e_minus_sector == { b_sector := 0, c_sector := 0 })
Instances For

---

### `Tau.BookII.Hartogs.completeness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L118-L121)
**def
Tau.BookII.Hartogs.completeness_check :Bool**


e₊ + e₋ = 1 (completeness): the idempotents partition unity.
In sector coordinates: (1,0) + (0,1) = (1,1) = 1.
Equations
- Tau.BookII.Hartogs.completeness_check = (Tau.Polarity.e_plus_sector.add Tau.Polarity.e_minus_sector == { b_sector := 1, c_sector := 1 })
Instances For

---

### `Tau.BookII.Hartogs.idempotency_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L123-L126)
**def
Tau.BookII.Hartogs.idempotency_check :Bool**


e₊² = e₊ and e₋² = e₋ (idempotency).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.coupling_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L132-L146)
**def
Tau.BookII.Hartogs.coupling_check :Bool**


[II.D35, coupling axiom] ι<sub>τ</sub> couples the two channels:
ι<sub>τ</sub> = 2 / (π + e).
In scaled arithmetic: ι<sub>τ</sub> * SCALE ≈ 2 * SCALE² / (π_cal + e_cal).
Verify consistency to within 2%.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.geometric_meaning_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L152-L187)
**def
Tau.BookII.Hartogs.geometric_meaning_check
(bound : Denotation.TauIdx)
 :Bool**


[II.R10] Geometric meaning of the idempotents.

e₊ projects onto the B-channel:


- B carries the exponent (γ-orbit) data

- Calibrated by π (circle winding number)

- At stage k: B-residues form Z/p_k Z, with p_k arcs of angular width 2π/p_k


e₋ projects onto the C-channel:


- C carries the tetration height (η-orbit) data

- Calibrated by e (factorial eigenvalue / growth base)

- Growth rate of the tower: exponential with base related to e


Evidence: for τ-admissible points, e₊-projection extracts B only,
e₋-projection extracts C only.
Equations
- Tau.BookII.Hartogs.geometric_meaning_check bound = Tau.BookII.Hartogs.geometric_meaning_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.geometric_meaning_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L169-L186)@[irreducible]

**def
Tau.BookII.Hartogs.geometric_meaning_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.b_channel_pi_calibration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L189-L211)
**def
Tau.BookII.Hartogs.b_channel_pi_calibration
(stages : Denotation.TauIdx)
 :Bool**


The B-channel is π-calibrated: the number of B-residues at stage k
equals p_k, and each arc has angular width 2π/p_k.
In scaled arithmetic: full circle = 2 * pi_cal, arc = 2 * pi_cal / p_k.
Verify: p_k arcs sum to a full circle.
Equations
- Tau.BookII.Hartogs.b_channel_pi_calibration stages = Tau.BookII.Hartogs.b_channel_pi_calibration.go stages 1 (stages + 1) Tau.BookII.Hartogs.calibrated_htau.pi_cal
Instances For

---

### `Tau.BookII.Hartogs.b_channel_pi_calibration.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L197-L210)@[irreducible]

**def
Tau.BookII.Hartogs.b_channel_pi_calibration.go
(stages : Denotation.TauIdx)

(k fuel pi_cal : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.c_channel_e_calibration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L213-L230)
**def
Tau.BookII.Hartogs.c_channel_e_calibration
(stages : Denotation.TauIdx)
 :Bool**


The C-channel is e-calibrated: the growth ratio P_{k+1}/P_k = p_{k+1},
and primorial growth is super-exponential with base related to e.
Evidence: ln(P_k) ~ sum_{i=1}^{k} ln(p_i) grows; the average
growth factor approaches e for large k via PNT.
At small k: verify p_{k+1} >= 2 (each step at least doubles).
Equations
- Tau.BookII.Hartogs.c_channel_e_calibration stages = Tau.BookII.Hartogs.c_channel_e_calibration.go stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Hartogs.c_channel_e_calibration.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L221-L229)@[irreducible]

**def
Tau.BookII.Hartogs.c_channel_e_calibration.go
(stages : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.calibration_consistency_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L236-L253)
**def
Tau.BookII.Hartogs.calibration_consistency_check :Bool**


[II.D35] Full calibration consistency: all four constants are
mutually consistent and the idempotents have correct geometric meaning.

- π, e, ι<sub>τ</sub> in correct ranges

- j² = +1

- Idempotents: orthogonal, complete, idempotent

- Coupling: ι<sub>τ</sub> = 2/(π+e)

- Geometric meaning: e₊ → B-channel, e₋ → C-channel

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_calibration_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L255-L259)
**def
Tau.BookII.Hartogs.full_calibration_check :Bool**


Extended consistency including channel calibration.
Equations
- Tau.BookII.Hartogs.full_calibration_check = (Tau.BookII.Hartogs.calibration_consistency_check && Tau.BookII.Hartogs.b_channel_pi_calibration 5 && Tau.BookII.Hartogs.c_channel_e_calibration 5)
Instances For

---

### `Tau.BookII.Hartogs.pi_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L303-L303)
**theorem
Tau.BookII.Hartogs.pi_range :pi_cal_range_check = true**


---

### `Tau.BookII.Hartogs.e_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L304-L304)
**theorem
Tau.BookII.Hartogs.e_range :e_cal_range_check = true**


---

### `Tau.BookII.Hartogs.iota_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L305-L305)
**theorem
Tau.BookII.Hartogs.iota_range :iota_cal_range_check = true**


---

### `Tau.BookII.Hartogs.j_sq_cal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L306-L306)
**theorem
Tau.BookII.Hartogs.j_sq_cal :j_squared_calibration_check = true**


---

### `Tau.BookII.Hartogs.ortho`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L307-L307)
**theorem
Tau.BookII.Hartogs.ortho :orthogonality_check = true**


---

### `Tau.BookII.Hartogs.compl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L308-L308)
**theorem
Tau.BookII.Hartogs.compl :completeness_check = true**


---

### `Tau.BookII.Hartogs.idemp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L309-L309)
**theorem
Tau.BookII.Hartogs.idemp :idempotency_check = true**


---

### `Tau.BookII.Hartogs.coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L310-L310)
**theorem
Tau.BookII.Hartogs.coupling :coupling_check = true**


---

### `Tau.BookII.Hartogs.geo_meaning_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L311-L311)
**theorem
Tau.BookII.Hartogs.geo_meaning_30 :geometric_meaning_check 30 = true**


---

### `Tau.BookII.Hartogs.b_pi_cal_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L312-L312)
**theorem
Tau.BookII.Hartogs.b_pi_cal_5 :b_channel_pi_calibration 5 = true**


---

### `Tau.BookII.Hartogs.c_e_cal_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L313-L313)
**theorem
Tau.BookII.Hartogs.c_e_cal_5 :c_channel_e_calibration 5 = true**


---

### `Tau.BookII.Hartogs.cal_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L314-L314)
**theorem
Tau.BookII.Hartogs.cal_consistency :calibration_consistency_check = true**


---

### `Tau.BookII.Hartogs.full_cal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L315-L315)
**theorem
Tau.BookII.Hartogs.full_cal :full_calibration_check = true**
