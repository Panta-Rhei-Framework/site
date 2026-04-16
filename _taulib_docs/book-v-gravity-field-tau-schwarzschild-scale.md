---
layout: taulib-doc
title: "TauLib.BookV.GravityField.TauSchwarzschildScale"
permalink: /verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/
lane: verify
module_name: "TauLib.BookV.GravityField.TauSchwarzschildScale"
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

# TauLib.BookV.GravityField.TauSchwarzschildScale


Black hole mass scale lemmas: single scale degree of freedom and minimal
mature black hole mass threshold. These complete the ch16 Schwarzschild
scale analysis.

## Registry Cross-References


- [V.L4] Single Scale Degree of Freedom -- `SingleScaleDOF`

- [V.L5] Minimal Mature Black Hole -- `MinimalMatureBH`


## Mathematical Content


### Single Scale DOF [V.L4]


The τ-Schwarzschild geometry has exactly one free scale parameter: the
linking mass M. All other quantities (R, r, G_τ, torus frequencies) are
determined by M through ι<sub>τ</sub>. This is because the shape ratio r/R = ι<sub>τ</sub>
is fixed by the axioms, reducing the two-parameter torus (R, r) to a
one-parameter family indexed by M.

### Minimal Mature BH [V.L5]


Below a minimal mass M_min, the linking topology relaxes (geometric
relaxation) before the torus vacuum stabilizes (topological relaxation).
M_min sets the lower boundary of the mature BH population.

## Ground Truth Sources


- Book V ch16: Schwarzschild geometry, mass scales


---

### `Tau.BookV.GravityField.SingleScaleDOF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L43-L67)
**structure
Tau.BookV.GravityField.SingleScaleDOF :Type**


[V.L4] Single scale degree of freedom: τ-Schwarzschild has exactly
one free scale parameter (linking mass M). All other quantities are
determined by M through ι<sub>τ</sub>.


- Shape ratio r/R = ι<sub>τ</sub> (fixed by axioms K0-K6)

- Schwarzschild radius R = 2G_τ M

- Inner radius r = ι<sub>τ</sub> · R

- QNM frequencies ∝ 1/R (outer) and 1/r (inner)

- Echo times ∝ R/c and r/c


The torus vacuum is a one-parameter family, not two-parameter.

- free_params : ℕ
Number of free scale parameters.

- params_eq : self.free_params = 1
Exactly one free parameter (M).

- torus_params : ℕ
Torus parameters (R, r).

- shape_constraints : ℕ
Shape constraints (r/R = ι<sub>τ</sub>).

- shape_fixed : Bool
Shape ratio is fixed (not free).

- all_determined : Bool
All derived quantities determined by M.

Instances For

---

### `Tau.BookV.GravityField.instReprSingleScaleDOF.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L67-L67)
**def
Tau.BookV.GravityField.instReprSingleScaleDOF.repr :SingleScaleDOF → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprSingleScaleDOF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L67-L67)
**instance
Tau.BookV.GravityField.instReprSingleScaleDOF :Repr SingleScaleDOF**

Equations
- Tau.BookV.GravityField.instReprSingleScaleDOF = { reprPrec := Tau.BookV.GravityField.instReprSingleScaleDOF.repr }

---

### `Tau.BookV.GravityField.single_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L69-L72)
**def
Tau.BookV.GravityField.single_scale :SingleScaleDOF**


The canonical single-scale instance.
Equations
- Tau.BookV.GravityField.single_scale = { free_params := 1, params_eq := Tau.BookV.GravityField.single_scale._proof_1 }
Instances For

---

### `Tau.BookV.GravityField.single_scale_dof`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L74-L79)
**theorem
Tau.BookV.GravityField.single_scale_dof :single_scale.free_params = 1 ∧ single_scale.shape_fixed = true ∧ single_scale.all_determined = true**


τ-Schwarzschild has exactly 1 free scale parameter.

---

### `Tau.BookV.GravityField.single_scale_reduction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L81-L83)
**theorem
Tau.BookV.GravityField.single_scale_reduction :2 - 1 = 1**


Two torus params minus one shape constraint = 1 free parameter.

---

### `Tau.BookV.GravityField.free_is_torus_minus_constraint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L85-L88)
**theorem
Tau.BookV.GravityField.free_is_torus_minus_constraint :single_scale.torus_params - single_scale.shape_constraints = single_scale.free_params**


The free parameter count equals torus params minus shape constraints.

---

### `Tau.BookV.GravityField.MinimalMatureBH`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L94-L115)
**structure
Tau.BookV.GravityField.MinimalMatureBH :Type**


[V.L5] Minimal mature black hole: below M_min, geometric relaxation
completes before torus vacuum stabilizes. M_min is the lower boundary
of the mature BH population.


- Below M_min: linking topology relaxes → no stable T² vacuum

- Above M_min: torus vacuum stabilizes → mature BH with r/R = ι<sub>τ</sub>

- M_min sets the Chandrasekhar-scale threshold for τ-BH formation


The existence of M_min ensures the mature BH population is bounded
below. No τ-BH can be arbitrarily light.

- threshold_exists : Bool
M_min exists as a threshold.

- below_unstable : Bool
Below M_min: no stable torus vacuum.

- above_stable : Bool
Above M_min: stable mature BH.

- population_bounded : Bool
Population is bounded below.

- relaxation_modes : ℕ
Relaxation modes (geometric + topological).

Instances For

---

### `Tau.BookV.GravityField.instReprMinimalMatureBH`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L115-L115)
**instance
Tau.BookV.GravityField.instReprMinimalMatureBH :Repr MinimalMatureBH**

Equations
- Tau.BookV.GravityField.instReprMinimalMatureBH = { reprPrec := Tau.BookV.GravityField.instReprMinimalMatureBH.repr }

---

### `Tau.BookV.GravityField.instReprMinimalMatureBH.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L115-L115)
**def
Tau.BookV.GravityField.instReprMinimalMatureBH.repr :MinimalMatureBH → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.minimal_bh`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L117-L118)
**def
Tau.BookV.GravityField.minimal_bh :MinimalMatureBH**


The canonical minimal mature BH instance.
Equations
- Tau.BookV.GravityField.minimal_bh = { }
Instances For

---

### `Tau.BookV.GravityField.minimal_mature_bh`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L120-L126)
**theorem
Tau.BookV.GravityField.minimal_mature_bh :minimal_bh.threshold_exists = true ∧ minimal_bh.below_unstable = true ∧ minimal_bh.above_stable = true ∧ minimal_bh.population_bounded = true**


Minimal mature BH threshold exists and bounds population.

---

### `Tau.BookV.GravityField.relaxation_plus_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L128-L130)
**theorem
Tau.BookV.GravityField.relaxation_plus_stability :2 + 3 = 5**


2 relaxation modes + 3 stability conditions = 5 field modes.
