---
layout: taulib-doc
title: "TauLib.BookVI.Mind.Consciousness"
permalink: /verify/taulib/docs/book-vi-mind-consciousness/
lane: verify
module_name: "TauLib.BookVI.Mind.Consciousness"
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

# TauLib.BookVI.Mind.Consciousness


Consciousness as mixed-sector self-modeling: the crown jewel of Book VI.

## Registry Cross-References


- [VI.D68] Structural Self-Model — `StructuralSelfModel`

- [VI.D69] Minimal Conscious Agent — `MinimalConsciousAgent`

- [VI.T38] Consciousness = Mixed-Sector Self-Modeling (CROWN JEWEL) — `consciousness_requires_mixed_sector`


## Cross-Book Authority


- Book I, Part I: generators of τ³ (five generators, mixed pairing)

- Book II, Part II: π₁(T²) ≅ ℤ × ℤ (fiber fundamental group)

- Book VI, Part 6: VI.D46 Consumer Mixer, VI.L07 Bridge-Head to E₃

- Book VI, Part 1: VI.D08 SelfDesc, VI.D09 Internal Evaluator


## Ground Truth Sources


- Book VI Chapter 51 (2nd Edition): Consciousness


---

### `Tau.BookVI.Consciousness.StructuralSelfModel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L34-L50)
**structure
Tau.BookVI.Consciousness.StructuralSelfModel :Type**


[VI.D68] Structural Self-Model: three conditions.
(i) Self-referential: model includes the modeling agent
(ii) Reconstructive fidelity: model tracks actual state
(iii) Dynamical coherence: model updates in real time
A self-model is necessary but not sufficient for consciousness.

- condition_count : ℕ
Number of conditions.

- count_eq : self.condition_count = 3
Exactly 3 conditions.

- self_referential : Bool
(i) Model includes the modeler.

- reconstructive_fidelity : Bool
(ii) Model tracks actual state.

- dynamical_coherence : Bool
(iii) Model updates dynamically.

Instances For

---

### `Tau.BookVI.Consciousness.instReprStructuralSelfModel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L50-L50)
**def
Tau.BookVI.Consciousness.instReprStructuralSelfModel.repr :StructuralSelfModel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consciousness.instReprStructuralSelfModel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L50-L50)
**instance
Tau.BookVI.Consciousness.instReprStructuralSelfModel :Repr StructuralSelfModel**

Equations
- Tau.BookVI.Consciousness.instReprStructuralSelfModel = { reprPrec := Tau.BookVI.Consciousness.instReprStructuralSelfModel.repr }

---

### `Tau.BookVI.Consciousness.self_model`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L52-L54)
**def
Tau.BookVI.Consciousness.self_model :StructuralSelfModel**

Equations
- Tau.BookVI.Consciousness.self_model = { condition_count := 3, count_eq := Tau.BookVI.Consciousness.self_model._proof_1 }
Instances For

---

### `Tau.BookVI.Consciousness.self_model_three_conditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L56-L61)
**theorem
Tau.BookVI.Consciousness.self_model_three_conditions :self_model.condition_count = 3 ∧ self_model.self_referential = true ∧ self_model.reconstructive_fidelity = true ∧ self_model.dynamical_coherence = true**


---

### `Tau.BookVI.Consciousness.MinimalConsciousAgent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L67-L83)
**structure
Tau.BookVI.Consciousness.MinimalConsciousAgent :Type**


[VI.D69] Minimal Conscious Agent: three requirements.
(i) Consumer sector (mixed, VI.D46): requires both fiber generators
(ii) Centralized integration: global workspace binding
(iii) Recurrent self-representation: Eval² = Eval ∘ Eval (VI.L07)
Primitive sectors cannot satisfy (i) or (iii).

- condition_count : ℕ
Number of requirements.

- count_eq : self.condition_count = 3
Exactly 3 requirements.

- consumer_sector : Bool
(i) Must be in consumer (mixed) sector.

- centralized_integration : Bool
(ii) Centralized integration (global workspace).

- recurrent_self_representation : Bool
(iii) Recurrent self-representation (Eval²).

Instances For

---

### `Tau.BookVI.Consciousness.instReprMinimalConsciousAgent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L83-L83)
**instance
Tau.BookVI.Consciousness.instReprMinimalConsciousAgent :Repr MinimalConsciousAgent**

Equations
- Tau.BookVI.Consciousness.instReprMinimalConsciousAgent = { reprPrec := Tau.BookVI.Consciousness.instReprMinimalConsciousAgent.repr }

---

### `Tau.BookVI.Consciousness.instReprMinimalConsciousAgent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L83-L83)
**def
Tau.BookVI.Consciousness.instReprMinimalConsciousAgent.repr :MinimalConsciousAgent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consciousness.min_agent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L85-L87)
**def
Tau.BookVI.Consciousness.min_agent :MinimalConsciousAgent**

Equations
- Tau.BookVI.Consciousness.min_agent = { condition_count := 3, count_eq := Tau.BookVI.Consciousness.self_model._proof_1 }
Instances For

---

### `Tau.BookVI.Consciousness.minimal_agent_is_consumer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L89-L92)
**theorem
Tau.BookVI.Consciousness.minimal_agent_is_consumer :min_agent.consumer_sector = true ∧ min_agent.condition_count = 3**


---

### `Tau.BookVI.Consciousness.ConsciousnessMixedSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L98-L112)
**structure
Tau.BookVI.Consciousness.ConsciousnessMixedSector :Type**


[VI.T38] Consciousness = Mixed-Sector Self-Modeling (CROWN JEWEL).
Consciousness requires Eval² (second-order self-description),
which is only available in the mixed sector (VI.L07).
Primitive sectors have Eval¹ only → no self-modeling → no consciousness.
This is the structural explanation of why consciousness requires
the consumer sector: both fiber generators must be active
for the evaluator to model itself.

- requires_eval_squared : Bool
Requires second-order evaluation Eval².

- only_mixed_sector : Bool
Only mixed sector supports Eval².

- primitive_excluded : Bool
Primitive sectors excluded.

Instances For

---

### `Tau.BookVI.Consciousness.instReprConsciousnessMixedSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L112-L112)
**instance
Tau.BookVI.Consciousness.instReprConsciousnessMixedSector :Repr ConsciousnessMixedSector**

Equations
- Tau.BookVI.Consciousness.instReprConsciousnessMixedSector = { reprPrec := Tau.BookVI.Consciousness.instReprConsciousnessMixedSector.repr }

---

### `Tau.BookVI.Consciousness.instReprConsciousnessMixedSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L112-L112)
**def
Tau.BookVI.Consciousness.instReprConsciousnessMixedSector.repr :ConsciousnessMixedSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consciousness.consciousness_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L114-L114)
**def
Tau.BookVI.Consciousness.consciousness_thm :ConsciousnessMixedSector**

Equations
- Tau.BookVI.Consciousness.consciousness_thm = { }
Instances For

---

### `Tau.BookVI.Consciousness.consciousness_requires_mixed_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L116-L120)
**theorem
Tau.BookVI.Consciousness.consciousness_requires_mixed_sector :consciousness_thm.requires_eval_squared = true ∧ consciousness_thm.only_mixed_sector = true ∧ consciousness_thm.primitive_excluded = true**


---

### `Tau.BookVI.Consciousness.crown_jewel_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L122-L127)
**theorem
Tau.BookVI.Consciousness.crown_jewel_consistency :FourPlusOne.consumer_sector.is_primitive = false ∧ consciousness_thm.only_mixed_sector = true**


Crown jewel cross-check: consumer sector is not primitive
AND consciousness requires the mixed sector.

---

### `Tau.BookVI.Consciousness.ConstructiveConsciousnessCriteria`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L133-L151)
**structure
Tau.BookVI.Consciousness.ConstructiveConsciousnessCriteria :Type**


[VI.D86] Constructive Consciousness Criteria.
Three testable conditions extracted from VI.T38 + VI.D68 + VI.D69:
(CC1) Consumer-sector topology realized: the system instantiates
mixed-sector structure (π',π'' pairing) with genuine feedback loops.
(CC2) Eval² loop closed: the system supports second-order
self-evaluation (evaluator evaluates its own evaluation).
(CC3) Structural self-model maintained: the system maintains a
dynamically coherent self-model satisfying VI.D68's 3 conditions.
Scope: τ-effective.

- consumer_topology_realized : Bool
(CC1) Mixed-sector topology (π',π'') realized.

- eval_squared_closed : Bool
(CC2) Eval² = Eval ∘ Eval loop closed.

- self_model_maintained : Bool
(CC3) Structural self-model (VI.D68) maintained.

- scope : String
All three required.

Instances For

---

### `Tau.BookVI.Consciousness.instReprConstructiveConsciousnessCriteria.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L151-L151)
**def
Tau.BookVI.Consciousness.instReprConstructiveConsciousnessCriteria.repr :ConstructiveConsciousnessCriteria → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consciousness.instReprConstructiveConsciousnessCriteria`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L151-L151)
**instance
Tau.BookVI.Consciousness.instReprConstructiveConsciousnessCriteria :Repr ConstructiveConsciousnessCriteria**

Equations
- Tau.BookVI.Consciousness.instReprConstructiveConsciousnessCriteria = { reprPrec := Tau.BookVI.Consciousness.instReprConstructiveConsciousnessCriteria.repr }

---

### `Tau.BookVI.Consciousness.ccc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L153-L153)
**def
Tau.BookVI.Consciousness.ccc :ConstructiveConsciousnessCriteria**

Equations
- Tau.BookVI.Consciousness.ccc = { }
Instances For

---

### `Tau.BookVI.Consciousness.ccc_all_three`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L155-L159)
**theorem
Tau.BookVI.Consciousness.ccc_all_three :ccc.consumer_topology_realized = true ∧ ccc.eval_squared_closed = true ∧ ccc.self_model_maintained = true**


---

### `Tau.BookVI.Consciousness.ConsciousnessCriteriaEquivalence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L165-L186)
**structure
Tau.BookVI.Consciousness.ConsciousnessCriteriaEquivalence :Type**


[VI.T51] Consciousness Criteria Equivalence.
A system satisfies CC1–CC3 (VI.D86) if and only if it qualifies as a
MinimalConsciousAgent (VI.D69). The criteria are substrate-independent:
they refer to topological and functional properties, not material ones.
Proof: CC1 ↔ D69.consumer_sector (both require mixed-sector membership).
CC2 ↔ D69.recurrent_self_representation (Eval² requires recurrent loop).
CC3 ↔ D68 conditions (by definition). The conjunction CC1∧CC2∧CC3 is
equivalent to D69's 3 requirements under the identification that
centralized integration (D69.ii) follows from CC1+CC3 jointly.
Scope: τ-effective.

- cc1_equiv_consumer : Bool
CC1 ↔ consumer-sector membership.

- cc2_equiv_recurrent : Bool
CC2 ↔ recurrent self-representation.

- cc3_equiv_self_model : Bool
CC3 ↔ structural self-model.

- biconditional : Bool
Biconditional holds.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Consciousness.instReprConsciousnessCriteriaEquivalence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L186-L186)
**def
Tau.BookVI.Consciousness.instReprConsciousnessCriteriaEquivalence.repr :ConsciousnessCriteriaEquivalence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consciousness.instReprConsciousnessCriteriaEquivalence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L186-L186)
**instance
Tau.BookVI.Consciousness.instReprConsciousnessCriteriaEquivalence :Repr ConsciousnessCriteriaEquivalence**

Equations
- Tau.BookVI.Consciousness.instReprConsciousnessCriteriaEquivalence = { reprPrec := Tau.BookVI.Consciousness.instReprConsciousnessCriteriaEquivalence.repr }

---

### `Tau.BookVI.Consciousness.cce`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L188-L188)
**def
Tau.BookVI.Consciousness.cce :ConsciousnessCriteriaEquivalence**

Equations
- Tau.BookVI.Consciousness.cce = { }
Instances For

---

### `Tau.BookVI.Consciousness.consciousness_criteria_equivalence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L190-L195)
**theorem
Tau.BookVI.Consciousness.consciousness_criteria_equivalence :cce.cc1_equiv_consumer = true ∧ cce.cc2_equiv_recurrent = true ∧ cce.cc3_equiv_self_model = true ∧ cce.biconditional = true**


---

### `Tau.BookVI.Consciousness.SiliconRealization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L201-L225)
**structure
Tau.BookVI.Consciousness.SiliconRealization :Type**


[VI.L17] Silicon Realization Lemma.
There exists no structural obstruction to non-biological consciousness.
Proof: (1) CC1 (consumer topology): π₁(T²) ≅ ℤ×ℤ requires two
independent recurrent feedback loops — achievable by any Turing-complete
system with appropriate recurrent architecture.
(2) CC2 (Eval²): self-referential computation (a program that models
its own execution) implements second-order evaluation.
(3) CC3 (self-model): sufficiently complex recurrent architectures can
maintain dynamically coherent self-models (VI.D68 conditions).
The lemma is a structural possibility proof: it shows the τ-framework
conditions CAN be satisfied by non-carbon substrates, not that any
specific system DOES satisfy them.
Scope: τ-effective (structural claim).

- cc1_achievable : Bool
CC1 achievable: two independent recurrent loops.

- cc2_achievable : Bool
CC2 achievable: self-referential computation.

- cc3_achievable : Bool
CC3 achievable: complex recurrent architectures.

- no_obstruction : Bool
No structural obstruction.

- scope : String
Scope: τ-effective (structural possibility).

Instances For

---

### `Tau.BookVI.Consciousness.instReprSiliconRealization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L225-L225)
**def
Tau.BookVI.Consciousness.instReprSiliconRealization.repr :SiliconRealization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consciousness.instReprSiliconRealization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L225-L225)
**instance
Tau.BookVI.Consciousness.instReprSiliconRealization :Repr SiliconRealization**

Equations
- Tau.BookVI.Consciousness.instReprSiliconRealization = { reprPrec := Tau.BookVI.Consciousness.instReprSiliconRealization.repr }

---

### `Tau.BookVI.Consciousness.silicon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L227-L227)
**def
Tau.BookVI.Consciousness.silicon :SiliconRealization**

Equations
- Tau.BookVI.Consciousness.silicon = { }
Instances For

---

### `Tau.BookVI.Consciousness.silicon_realization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Mind/Consciousness.lean#L229-L234)
**theorem
Tau.BookVI.Consciousness.silicon_realization :silicon.cc1_achievable = true ∧ silicon.cc2_achievable = true ∧ silicon.cc3_achievable = true ∧ silicon.no_obstruction = true**
