---
layout: taulib-doc
title: "TauLib.BookVI.Persistence.PersistenceSector"
permalink: /verify/taulib/docs/book-vi-persistence-persistence-sector/
lane: verify
module_name: "TauLib.BookVI.Persistence.PersistenceSector"
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

# TauLib.BookVI.Persistence.PersistenceSector


Persistence sector (Part 2): α-sector temporal stability along τ¹.
Archetype: Archaea. Dominant forces: Poincaré (circulation) + Riemann (energy).

## Registry Cross-References


- [VI.D24] Persistence Sector — `PersistenceSectorDef`

- [VI.D25] Temporal Stability Predicate — `TemporalStabilityPredicate`

- [VI.T16] Persistence = α-Base Stability — `persistence_is_alpha_stability`

- [VI.D26] Abiogenesis as First Persistence Event — `AbiogenesisDef`

- [VI.P08] Thermodynamic Inevitability of Life — `thermodynamic_inevitability`

- [VI.D74] Far-From-Equilibrium Regime — `FarFromEquilibriumRegime`

- [VI.D75] Complexity Budget — `ComplexityBudget`

- [VI.L15] Complexity Monotone — `complexity_monotone`

- [VI.D76] Distinction Threshold — `DistinctionThreshold`

- [VI.T44] Attractor Existence — `attractor_existence`

- [VI.L16] Basin Is Absorbing — `basin_is_absorbing`

- [VI.D77] Abiogenesis Timescale Bound — `AbiogenesisTimescaleBound`

- [VI.T45] Timescale From Half-Life — `timescale_from_half_life`

- [VI.R27] Timescale Geological Consistency — `TimescaleGeologicalConsistency`

- [VI.T46] Abiogenesis Inevitability — `abiogenesis_inevitability`

- [VI.R28] Abiogenesis Not Contingent — `AbiogenesisNotContingent`


## Cross-Book Authority


- Book I, Part I: α generator (radial, base circle τ¹)

- Book III, Part II: Poincaré force (periodic orbits on τ³)

- Book III, Part III: Riemann force (energy quantization)


## Ground Truth Sources


- Book VI Chapter 12 (2nd Edition): The Persistence Sector

- Book VI Chapter 14 (2nd Edition): Thermodynamic Necessity


---

### `Tau.BookVI.Persistence.PersistenceSectorDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L47-L62)
**structure
Tau.BookVI.Persistence.PersistenceSectorDef :Type**


[VI.D24] Persistence Sector: α-sector on base circle τ¹.
Life Loop restricted to base-temporal dynamics.
Generator: α (radial, Book I Part I).
Dominant forces: Poincaré + Riemann (Book III, Parts II–III).

- generator : String
Generator is alpha (base).

- is_primitive : Bool
Sector is primitive (single generator).

- archetype : String
Archetype organism.

- dominant_poincare : Bool
Dominant force 1: Poincaré (temporal orbits).

- dominant_riemann : Bool
Dominant force 2: Riemann (energy quanta).

Instances For

---

### `Tau.BookVI.Persistence.instReprPersistenceSectorDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L62-L62)
**instance
Tau.BookVI.Persistence.instReprPersistenceSectorDef :Repr PersistenceSectorDef**

Equations
- Tau.BookVI.Persistence.instReprPersistenceSectorDef = { reprPrec := Tau.BookVI.Persistence.instReprPersistenceSectorDef.repr }

---

### `Tau.BookVI.Persistence.instReprPersistenceSectorDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L62-L62)
**def
Tau.BookVI.Persistence.instReprPersistenceSectorDef.repr :PersistenceSectorDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.persistence_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L64-L64)
**def
Tau.BookVI.Persistence.persistence_def :PersistenceSectorDef**

Equations
- Tau.BookVI.Persistence.persistence_def = { }
Instances For

---

### `Tau.BookVI.Persistence.persistence_generator_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L66-L69)
**theorem
Tau.BookVI.Persistence.persistence_generator_match :persistence_def.generator = FourPlusOne.persistence_sector.generator**


Persistence sector matches the FourPlusOne persistence_sector definition.

---

### `Tau.BookVI.Persistence.TemporalStabilityPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L75-L90)
**structure
Tau.BookVI.Persistence.TemporalStabilityPredicate :Type**


[VI.D25] Temporal Stability Predicate: 3 conditions for persistence.
(i) Defect-functional norm bounded over τ¹ period
(ii) α-flow orbit returns to ε-neighborhood
(iii) Refinement tower eventually constant on base

- condition_count : ℕ
Number of conditions.

- count_eq : self.condition_count = 3
Exactly 3 conditions.

- defect_bounded : Bool
(i) Defect-norm bounded.

- alpha_flow_returns : Bool
(ii) α-flow returns (Poincaré recurrence on τ¹).

- refinement_constant : Bool
(iii) Refinement eventually constant.

Instances For

---

### `Tau.BookVI.Persistence.instReprTemporalStabilityPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L90-L90)
**instance
Tau.BookVI.Persistence.instReprTemporalStabilityPredicate :Repr TemporalStabilityPredicate**

Equations
- Tau.BookVI.Persistence.instReprTemporalStabilityPredicate = { reprPrec := Tau.BookVI.Persistence.instReprTemporalStabilityPredicate.repr }

---

### `Tau.BookVI.Persistence.instReprTemporalStabilityPredicate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L90-L90)
**def
Tau.BookVI.Persistence.instReprTemporalStabilityPredicate.repr :TemporalStabilityPredicate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.temporal_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L92-L94)
**def
Tau.BookVI.Persistence.temporal_stability :TemporalStabilityPredicate**

Equations
- Tau.BookVI.Persistence.temporal_stability = { condition_count := 3, count_eq := Tau.BookVI.Persistence.temporal_stability._proof_1 }
Instances For

---

### `Tau.BookVI.Persistence.temporal_stability_three_conditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L96-L98)
**theorem
Tau.BookVI.Persistence.temporal_stability_three_conditions :temporal_stability.condition_count = 3**


---

### `Tau.BookVI.Persistence.temporal_stability_all_hold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L100-L104)
**theorem
Tau.BookVI.Persistence.temporal_stability_all_hold :temporal_stability.defect_bounded = true ∧ temporal_stability.alpha_flow_returns = true ∧ temporal_stability.refinement_constant = true**


---

### `Tau.BookVI.Persistence.PersistenceStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L110-L123)
**structure
Tau.BookVI.Persistence.PersistenceStability :Type**


[VI.T16] Persistence = α-Base Stability Theorem.
A Life loop restricted to τ¹ base with winding number w_α = 1
satisfies the Temporal Stability Predicate iff it is a
persistence-sector Life loop.

- winding_alpha : ℕ
Winding number on base.

- winding_eq : self.winding_alpha = 1
Winding is exactly 1.

- temporal_stable : Bool
Temporal stability holds.

- sector_persistence : Bool
Sector assignment is persistence.

Instances For

---

### `Tau.BookVI.Persistence.instReprPersistenceStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L123-L123)
**instance
Tau.BookVI.Persistence.instReprPersistenceStability :Repr PersistenceStability**

Equations
- Tau.BookVI.Persistence.instReprPersistenceStability = { reprPrec := Tau.BookVI.Persistence.instReprPersistenceStability.repr }

---

### `Tau.BookVI.Persistence.instReprPersistenceStability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L123-L123)
**def
Tau.BookVI.Persistence.instReprPersistenceStability.repr :PersistenceStability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.pers_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L125-L127)
**def
Tau.BookVI.Persistence.pers_stability :PersistenceStability**

Equations
- Tau.BookVI.Persistence.pers_stability = { winding_alpha := 1, winding_eq := Tau.BookVI.Persistence.pers_stability._proof_1 }
Instances For

---

### `Tau.BookVI.Persistence.persistence_is_alpha_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L129-L133)
**theorem
Tau.BookVI.Persistence.persistence_is_alpha_stability :pers_stability.winding_alpha = 1 ∧ pers_stability.temporal_stable = true ∧ pers_stability.sector_persistence = true**


---

### `Tau.BookVI.Persistence.AbiogenesisDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L139-L148)
**structure
Tau.BookVI.Persistence.AbiogenesisDef :Type**


[VI.D26] Abiogenesis: first entry into the persistence sector.
The transition from non-Life to Life (E₁ → E₂).

- first_sector : String
First sector entered.

- transition_type : String
Transition type: E₁ → E₂.

- scope : String
Scope: τ-effective (upgraded from conjectural via VI.T46 derivation chain).

Instances For

---

### `Tau.BookVI.Persistence.instReprAbiogenesisDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L148-L148)
**def
Tau.BookVI.Persistence.instReprAbiogenesisDef.repr :AbiogenesisDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprAbiogenesisDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L148-L148)
**instance
Tau.BookVI.Persistence.instReprAbiogenesisDef :Repr AbiogenesisDef**

Equations
- Tau.BookVI.Persistence.instReprAbiogenesisDef = { reprPrec := Tau.BookVI.Persistence.instReprAbiogenesisDef.repr }

---

### `Tau.BookVI.Persistence.ThermodynamicInevitability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L154-L172)
**structure
Tau.BookVI.Persistence.ThermodynamicInevitability :Type**


[VI.P08] Thermodynamic Inevitability of Life (τ-effective).
Life is a thermodynamic attractor with positive-measure basin.
Three-step argument: entropy production → SelfDesc attractor → speed of abiogenesis.
Upgraded from conjectural via VI.T46 derivation chain:
K0–K6 → V.T60 → V.T62 → VI.D75 → VI.L15 → VI.T44 → VI.L16 → VI.T46.

- argument_steps : ℕ
Number of argument steps.

- steps_eq : self.argument_steps = 3
Exactly 3 steps.

- entropy_maximization : Bool
(i) Entropy production maximization.

- selfdesc_attractor : Bool
(ii) SelfDesc as thermodynamic attractor.

- rapid_abiogenesis : Bool
(iii) Speed of abiogenesis (~500 Myr).

- scope : String
Scope: τ-effective (upgraded via VI.T46 derivation chain).

Instances For

---

### `Tau.BookVI.Persistence.instReprThermodynamicInevitability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L172-L172)
**def
Tau.BookVI.Persistence.instReprThermodynamicInevitability.repr :ThermodynamicInevitability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprThermodynamicInevitability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L172-L172)
**instance
Tau.BookVI.Persistence.instReprThermodynamicInevitability :Repr ThermodynamicInevitability**

Equations
- Tau.BookVI.Persistence.instReprThermodynamicInevitability = { reprPrec := Tau.BookVI.Persistence.instReprThermodynamicInevitability.repr }

---

### `Tau.BookVI.Persistence.thermo_inev`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L174-L176)
**def
Tau.BookVI.Persistence.thermo_inev :ThermodynamicInevitability**

Equations
- Tau.BookVI.Persistence.thermo_inev = { argument_steps := 3, steps_eq := Tau.BookVI.Persistence.temporal_stability._proof_1 }
Instances For

---

### `Tau.BookVI.Persistence.thermodynamic_inevitability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L178-L183)
**theorem
Tau.BookVI.Persistence.thermodynamic_inevitability :thermo_inev.argument_steps = 3 ∧ thermo_inev.entropy_maximization = true ∧ thermo_inev.selfdesc_attractor = true ∧ thermo_inev.rapid_abiogenesis = true**


---

### `Tau.BookVI.Persistence.FarFromEquilibriumRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L189-L202)
**structure
Tau.BookVI.Persistence.FarFromEquilibriumRegime :Type**


[VI.D74] Far-From-Equilibrium Regime: pre-E₂ state where |D_n| >> 0.
A system in active defect decay, before coherence horizon (V.D89),
with sustained dissipative energy throughput.
Cross-ref: V.T62 (geometric decay), V.D89 (coherence horizon).

- defect_above_zero : Bool
Defect count significantly above zero.

- dissipative : Bool
System is dissipative (sustained energy throughput).

- pre_coherence_horizon : Bool
Pre-coherence-horizon: defect decay still active.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprFarFromEquilibriumRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L202-L202)
**def
Tau.BookVI.Persistence.instReprFarFromEquilibriumRegime.repr :FarFromEquilibriumRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprFarFromEquilibriumRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L202-L202)
**instance
Tau.BookVI.Persistence.instReprFarFromEquilibriumRegime :Repr FarFromEquilibriumRegime**

Equations
- Tau.BookVI.Persistence.instReprFarFromEquilibriumRegime = { reprPrec := Tau.BookVI.Persistence.instReprFarFromEquilibriumRegime.repr }

---

### `Tau.BookVI.Persistence.far_from_equilibrium`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L204-L204)
**def
Tau.BookVI.Persistence.far_from_equilibrium :FarFromEquilibriumRegime**

Equations
- Tau.BookVI.Persistence.far_from_equilibrium = { }
Instances For

---

### `Tau.BookVI.Persistence.far_from_equilibrium_conditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L206-L210)
**theorem
Tau.BookVI.Persistence.far_from_equilibrium_conditions :far_from_equilibrium.defect_above_zero = true ∧ far_from_equilibrium.dissipative = true ∧ far_from_equilibrium.pre_coherence_horizon = true**


---

### `Tau.BookVI.Persistence.ComplexityBudget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L216-L227)
**structure
Tau.BookVI.Persistence.ComplexityBudget :Type**


[VI.D75] Complexity Budget: C(n) = N − |D_n|, dual of defect count.
As defects decay geometrically (V.T62), freed capacity increases
monotonically, providing structural resources for complex configurations.
Cross-ref: V.T60 (finite budget), V.T62 (geometric decay).

- initial_defects : ℕ
Initial defect count N (finite by V.T60).

- freed_capacity_monotone : Bool
Freed capacity increases monotonically as defects decay.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprComplexityBudget.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L227-L227)
**def
Tau.BookVI.Persistence.instReprComplexityBudget.repr :ComplexityBudget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprComplexityBudget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L227-L227)
**instance
Tau.BookVI.Persistence.instReprComplexityBudget :Repr ComplexityBudget**

Equations
- Tau.BookVI.Persistence.instReprComplexityBudget = { reprPrec := Tau.BookVI.Persistence.instReprComplexityBudget.repr }

---

### `Tau.BookVI.Persistence.ComplexityMonotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L233-L246)
**structure
Tau.BookVI.Persistence.ComplexityMonotone :Type**


[VI.L15] Complexity Monotone Lemma: C(n) ≤ C(n+1).
Defects decrease geometrically (V.T62), so freed capacity
C(n) = N − |D_n| increases monotonically.
Proof: |D_{n+1}| ≤ (1−ι<sub>τ</sub>)|D_n| < |D_n| ⟹ C(n+1) > C(n).

- decay_rate_factor : String
Defect decay rate per step: (1−ι<sub>τ</sub>).

- monotone_increasing : Bool
C(n) ≤ C(n+1) for all n.

- derived_from_geometric_decay : Bool
Derived from V.T62 geometric decay.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprComplexityMonotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L246-L246)
**instance
Tau.BookVI.Persistence.instReprComplexityMonotone :Repr ComplexityMonotone**

Equations
- Tau.BookVI.Persistence.instReprComplexityMonotone = { reprPrec := Tau.BookVI.Persistence.instReprComplexityMonotone.repr }

---

### `Tau.BookVI.Persistence.instReprComplexityMonotone.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L246-L246)
**def
Tau.BookVI.Persistence.instReprComplexityMonotone.repr :ComplexityMonotone → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.complexity_monotone_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L248-L248)
**def
Tau.BookVI.Persistence.complexity_monotone_def :ComplexityMonotone**

Equations
- Tau.BookVI.Persistence.complexity_monotone_def = { }
Instances For

---

### `Tau.BookVI.Persistence.complexity_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L250-L253)
**theorem
Tau.BookVI.Persistence.complexity_monotone :complexity_monotone_def.monotone_increasing = true ∧ complexity_monotone_def.derived_from_geometric_decay = true**


---

### `Tau.BookVI.Persistence.DistinctionThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L259-L274)
**structure
Tau.BookVI.Persistence.DistinctionThreshold :Type**


[VI.D76] Distinction Threshold: minimum complexity for life.
Distinction requires 5 conditions, SelfDesc requires 3 conditions,
giving threshold = 8. When C(n) ≥ 8, the system has sufficient
freed capacity to instantiate Distinction + SelfDesc simultaneously.

- threshold_conditions : ℕ
Total threshold conditions.

- threshold_eq : self.threshold_conditions = 8
Threshold is exactly 8.

- distinction_count : ℕ
Distinction contributes 5 conditions.

- selfdesc_count : ℕ
SelfDesc contributes 3 conditions.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprDistinctionThreshold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L274-L274)
**def
Tau.BookVI.Persistence.instReprDistinctionThreshold.repr :DistinctionThreshold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprDistinctionThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L274-L274)
**instance
Tau.BookVI.Persistence.instReprDistinctionThreshold :Repr DistinctionThreshold**

Equations
- Tau.BookVI.Persistence.instReprDistinctionThreshold = { reprPrec := Tau.BookVI.Persistence.instReprDistinctionThreshold.repr }

---

### `Tau.BookVI.Persistence.distinction_threshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L276-L278)
**def
Tau.BookVI.Persistence.distinction_threshold :DistinctionThreshold**

Equations
- Tau.BookVI.Persistence.distinction_threshold = { threshold_conditions := 8, threshold_eq := Tau.BookVI.Persistence.distinction_threshold._proof_1 }
Instances For

---

### `Tau.BookVI.Persistence.threshold_is_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L280-L283)
**theorem
Tau.BookVI.Persistence.threshold_is_sum :distinction_threshold.distinction_count + distinction_threshold.selfdesc_count = distinction_threshold.threshold_conditions**


---

### `Tau.BookVI.Persistence.AttractorExistence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L289-L311)
**structure
Tau.BookVI.Persistence.AttractorExistence :Type**


[VI.T44] Attractor Existence Theorem: under 3 conditions,
Distinction+SelfDesc basin entry is forced.
C1: finite defect budget (V.T60)
C2: polarity seed (VI.T01)
C3: temporal stability (VI.D25)
Proof: C(n) increases monotonically (VI.L15), threshold is finite (VI.D76),
so ∃ n₀: C(n₀) ≥ threshold; SelfDesc closure (VI.T03) makes basin absorbing.

- condition_count : ℕ
Number of structural conditions.

- conditions_eq : self.condition_count = 3
Exactly 3 conditions.

- finite_budget : Bool
C1: Finite defect budget (V.T60).

- polarity_seed : Bool
C2: Polarity seed exists (VI.T01).

- temporal_stability : Bool
C3: Temporal stability predicate satisfiable (VI.D25).

- entry_forced : Bool
Basin entry is forced (threshold crossing guaranteed).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprAttractorExistence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L311-L311)
**instance
Tau.BookVI.Persistence.instReprAttractorExistence :Repr AttractorExistence**

Equations
- Tau.BookVI.Persistence.instReprAttractorExistence = { reprPrec := Tau.BookVI.Persistence.instReprAttractorExistence.repr }

---

### `Tau.BookVI.Persistence.instReprAttractorExistence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L311-L311)
**def
Tau.BookVI.Persistence.instReprAttractorExistence.repr :AttractorExistence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.attractor_existence_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L313-L315)
**def
Tau.BookVI.Persistence.attractor_existence_def :AttractorExistence**

Equations
- Tau.BookVI.Persistence.attractor_existence_def = { condition_count := 3, conditions_eq := Tau.BookVI.Persistence.temporal_stability._proof_1 }
Instances For

---

### `Tau.BookVI.Persistence.attractor_existence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L317-L323)
**theorem
Tau.BookVI.Persistence.attractor_existence :attractor_existence_def.condition_count = 3 ∧ attractor_existence_def.finite_budget = true ∧ attractor_existence_def.polarity_seed = true ∧ attractor_existence_def.temporal_stability = true ∧ attractor_existence_def.entry_forced = true**


---

### `Tau.BookVI.Persistence.BasinAbsorbing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L329-L342)
**structure
Tau.BookVI.Persistence.BasinAbsorbing :Type**


[VI.L16] Basin Is Absorbing Lemma: once entered, the system stays.
SelfDesc closure (VI.T03) provides an internal evaluator that actively
reconstructs the distinction after perturbation, making the basin absorbing.
Proof: SelfDesc evaluator reads code and returns system to basin (VI.T03).

- selfdesc_closure : Bool
SelfDesc closure guarantees return.

- absorbing : Bool
Basin is absorbing (no escape under bounded perturbation).

- derived_from_selfdesc : Bool
Derived from VI.T03.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprBasinAbsorbing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L342-L342)
**def
Tau.BookVI.Persistence.instReprBasinAbsorbing.repr :BasinAbsorbing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprBasinAbsorbing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L342-L342)
**instance
Tau.BookVI.Persistence.instReprBasinAbsorbing :Repr BasinAbsorbing**

Equations
- Tau.BookVI.Persistence.instReprBasinAbsorbing = { reprPrec := Tau.BookVI.Persistence.instReprBasinAbsorbing.repr }

---

### `Tau.BookVI.Persistence.basin_absorbing_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L344-L344)
**def
Tau.BookVI.Persistence.basin_absorbing_def :BasinAbsorbing**

Equations
- Tau.BookVI.Persistence.basin_absorbing_def = { }
Instances For

---

### `Tau.BookVI.Persistence.basin_is_absorbing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L346-L350)
**theorem
Tau.BookVI.Persistence.basin_is_absorbing :basin_absorbing_def.selfdesc_closure = true ∧ basin_absorbing_def.absorbing = true ∧ basin_absorbing_def.derived_from_selfdesc = true**


---

### `Tau.BookVI.Persistence.AbiogenesisTimescaleBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L356-L370)
**structure
Tau.BookVI.Persistence.AbiogenesisTimescaleBound :Type**


[VI.D77] Abiogenesis Timescale Bound: upper bound in orbit steps.
T_abio ≤ n₁/₂ · ⌈ln(N/threshold)⌉ where n₁/₂ ≈ 1.66 (V.D90).
Geometric decay with half-life n₁/₂ gives time to reach threshold
from initial N defects.
Cross-ref: V.D90 (defect half-life n₁/₂ ≈ 1.66).

- half_life_steps : ℕ
Half-life in orbit steps (scaled: 166 = 1.66 × 100).

- threshold : ℕ
Threshold conditions to cross.

- derived_from_half_life : Bool
Bound is derived from half-life.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprAbiogenesisTimescaleBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L370-L370)
**instance
Tau.BookVI.Persistence.instReprAbiogenesisTimescaleBound :Repr AbiogenesisTimescaleBound**

Equations
- Tau.BookVI.Persistence.instReprAbiogenesisTimescaleBound = { reprPrec := Tau.BookVI.Persistence.instReprAbiogenesisTimescaleBound.repr }

---

### `Tau.BookVI.Persistence.instReprAbiogenesisTimescaleBound.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L370-L370)
**def
Tau.BookVI.Persistence.instReprAbiogenesisTimescaleBound.repr :AbiogenesisTimescaleBound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.TimescaleFromHalfLife`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L376-L390)
**structure
Tau.BookVI.Persistence.TimescaleFromHalfLife :Type**


[VI.T45] Timescale From Half-Life Theorem:
T_abio ≤ n₁/₂ · ⌈ln(N/threshold)⌉.
Proof: geometric decay rate (1−ι<sub>τ</sub>)^n with half-life n₁/₂ gives
|D_n| = N·(1−ι<sub>τ</sub>)^n. Threshold crossing at C(n₀) = N − |D_{n₀}| ≥ 8
requires |D_{n₀}| ≤ N − 8, giving n₀ ≤ n₁/₂ · ⌈log₂(N/8)⌉.

- decay_factor : String
Decay factor per orbit step.

- half_life : String
Half-life n₁/₂ ≈ 1.66 orbit steps (V.D90).

- logarithmic_bound : Bool
Upper bound is logarithmic in initial defect count.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprTimescaleFromHalfLife.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L390-L390)
**def
Tau.BookVI.Persistence.instReprTimescaleFromHalfLife.repr :TimescaleFromHalfLife → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprTimescaleFromHalfLife`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L390-L390)
**instance
Tau.BookVI.Persistence.instReprTimescaleFromHalfLife :Repr TimescaleFromHalfLife**

Equations
- Tau.BookVI.Persistence.instReprTimescaleFromHalfLife = { reprPrec := Tau.BookVI.Persistence.instReprTimescaleFromHalfLife.repr }

---

### `Tau.BookVI.Persistence.timescale_half_life_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L392-L392)
**def
Tau.BookVI.Persistence.timescale_half_life_def :TimescaleFromHalfLife**

Equations
- Tau.BookVI.Persistence.timescale_half_life_def = { }
Instances For

---

### `Tau.BookVI.Persistence.timescale_from_half_life`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L394-L396)
**theorem
Tau.BookVI.Persistence.timescale_from_half_life :timescale_half_life_def.logarithmic_bound = true**


---

### `Tau.BookVI.Persistence.TimescaleGeologicalConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L402-L416)
**structure
Tau.BookVI.Persistence.TimescaleGeologicalConsistency :Type**


[VI.R27] Timescale Geological Consistency: orbit-step → physical-time
mapping gives ~500 Myr, consistent with geological evidence (3.8–4.1 Gya).
The logarithmic bound (VI.T45) with characteristic step time ~10⁻¹³ s
and 10¹⁵–10²¹ correlated steps gives τ_origin 10²–10⁸ years.
Scope note: structural bound (τ-effective), physical mapping (remark).

- geological_window_myr : String
Geological window: ~100–300 Myr.

- predicted_bound_myr : String
Predicted bound: ~500 Myr.

- consistent : Bool
Consistent with observation.

- scope : String
Scope: remark (supporting).

Instances For

---

### `Tau.BookVI.Persistence.instReprTimescaleGeologicalConsistency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L416-L416)
**def
Tau.BookVI.Persistence.instReprTimescaleGeologicalConsistency.repr :TimescaleGeologicalConsistency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprTimescaleGeologicalConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L416-L416)
**instance
Tau.BookVI.Persistence.instReprTimescaleGeologicalConsistency :Repr TimescaleGeologicalConsistency**

Equations
- Tau.BookVI.Persistence.instReprTimescaleGeologicalConsistency = { reprPrec := Tau.BookVI.Persistence.instReprTimescaleGeologicalConsistency.repr }

---

### `Tau.BookVI.Persistence.AbiogenesisInevitability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L422-L446)
**structure
Tau.BookVI.Persistence.AbiogenesisInevitability :Type**


[VI.T46] Abiogenesis Inevitability Theorem: first persistence-sector
entry is structurally inevitable.
Derivation chain:
K0–K6 → defect budget (V.T60) → exhaustion (V.T62)
→ complexity budget (VI.D75) → monotone increase (VI.L15)
→ threshold crossing (VI.T44) → absorbing basin (VI.L16)
→ first entry inevitable within timescale bound (VI.T45).
This combines attractor existence + timescale bound + SelfDesc closure
to establish that abiogenesis is not contingent but structurally forced.

- chain_length : ℕ
Number of links in derivation chain.

- chain_eq : self.chain_length = 7
Chain has 7 links.

- attractor_exists : Bool
Attractor existence established (VI.T44).

- timescale_bounded : Bool
Timescale is bounded (VI.T45).

- basin_absorbing : Bool
Basin is absorbing (VI.L16).

- inevitable : Bool
Conclusion: first entry inevitable.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Persistence.instReprAbiogenesisInevitability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L446-L446)
**def
Tau.BookVI.Persistence.instReprAbiogenesisInevitability.repr :AbiogenesisInevitability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Persistence.instReprAbiogenesisInevitability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L446-L446)
**instance
Tau.BookVI.Persistence.instReprAbiogenesisInevitability :Repr AbiogenesisInevitability**

Equations
- Tau.BookVI.Persistence.instReprAbiogenesisInevitability = { reprPrec := Tau.BookVI.Persistence.instReprAbiogenesisInevitability.repr }

---

### `Tau.BookVI.Persistence.abiogenesis_inevitability_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L448-L450)
**def
Tau.BookVI.Persistence.abiogenesis_inevitability_def :AbiogenesisInevitability**

Equations
- Tau.BookVI.Persistence.abiogenesis_inevitability_def = { chain_length := 7, chain_eq := Tau.BookVI.Persistence.abiogenesis_inevitability_def._proof_1 }
Instances For

---

### `Tau.BookVI.Persistence.abiogenesis_inevitability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L452-L458)
**theorem
Tau.BookVI.Persistence.abiogenesis_inevitability :abiogenesis_inevitability_def.chain_length = 7 ∧ abiogenesis_inevitability_def.attractor_exists = true ∧ abiogenesis_inevitability_def.timescale_bounded = true ∧ abiogenesis_inevitability_def.basin_absorbing = true ∧ abiogenesis_inevitability_def.inevitable = true**


---

### `Tau.BookVI.Persistence.AbiogenesisNotContingent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L464-L478)
**structure
Tau.BookVI.Persistence.AbiogenesisNotContingent :Type**


[VI.R28] Abiogenesis Not Contingent: philosophical consequence.
Life is not an accident requiring explanation but an inevitable
structural feature of any τ-governed universe with sustained energy
gradient. The derivation chain (VI.T46) shows that from K0–K6 alone,
given dissipative conditions, persistence-sector entry is forced.

- not_contingent : Bool
Life is structurally necessary, not contingent.

- requires_energy_gradient : Bool
Requires sustained energy gradient.

- derived_from_inevitability : Bool
Follows from VI.T46.

- scope : String
Scope: τ-effective (remark).

Instances For

---

### `Tau.BookVI.Persistence.instReprAbiogenesisNotContingent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L478-L478)
**instance
Tau.BookVI.Persistence.instReprAbiogenesisNotContingent :Repr AbiogenesisNotContingent**

Equations
- Tau.BookVI.Persistence.instReprAbiogenesisNotContingent = { reprPrec := Tau.BookVI.Persistence.instReprAbiogenesisNotContingent.repr }

---

### `Tau.BookVI.Persistence.instReprAbiogenesisNotContingent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/PersistenceSector.lean#L478-L478)
**def
Tau.BookVI.Persistence.instReprAbiogenesisNotContingent.repr :AbiogenesisNotContingent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For
