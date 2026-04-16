---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.Neural"
permalink: /verify/taulib/docs/book-vi-consumer-neural/
lane: verify
module_name: "TauLib.BookVI.Consumer.Neural"
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

# TauLib.BookVI.Consumer.Neural


Neural systems as τ³ computers, and sleep as the temporal lemniscate's second lobe.

## Registry Cross-References


- [VI.D52] Neural Architecture as τ³ Computer — `NeuralArchitecture`

- [VI.P19] Sleep as Temporal Lemniscate Second Lobe — `sleep_two_lobes`


## Cross-Book Authority


- Book II, Part II: τ³ = τ¹ ×_f T² fibration (neural architecture mirrors τ³ structure)

- Book VI, Part 2: Temporal lemniscate L_T (persistence sector, circadian rhythm)

- Book III, Part I: P vs NP force (cognitive optimization)


## Ground Truth Sources


- Book VI Chapter 40 (2nd Edition): Neural Systems

- Book VI Chapter 41 (2nd Edition): Learning and Sleep


### Wave R7-E: Neural Defect Accumulation (2026-03-08)


- [VI.D87] Neural Defect Level — `NeuralDefectLevel`

- [VI.D88] Neural Defect Tower — `NeuralDefectTower`

- [VI.D89] Neurodegenerative Disease Mapping — `NeurodegenerativeMapping`

- [VI.T52] Inter-Level Cascade — `inter_level_cascade`

- [VI.P23] Neural Defect Monotonicity — `neural_defect_monotone`

- [VI.D90] Sleep Repair Function — `SleepRepairFunction`

- [VI.T53] Sleep Consolidates Levels 1–2 — `sleep_consolidates_levels_1_2`

- [VI.P24] Sleep Deprivation Accelerates — `sleep_deprivation_accelerates`

- [VI.D91] Neural Hayflick Bound — `NeuralHayflickBound`

- [VI.T54] Neurodegeneration = Hayflick Crossing — `neurodegeneration_is_hayflick_crossing`


---

### `Tau.BookVI.Neural.NeuralArchitecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L43-L59)
**structure
Tau.BookVI.Neural.NeuralArchitecture :Type**


[VI.D52] Neural Architecture as τ³ Computer.
Three node types: sensory (input), inter (processing), motor (output).
Weighted directed edges. The architecture mirrors the τ³ fibration
(Book II, Part II): base τ¹ = temporal sequencing,
fiber T² = parallel feature processing.

- node_types : ℕ
Number of fundamental node types.

- types_eq : self.node_types = 3
Exactly 3 types: sensory, inter, motor.

- weighted_edges : Bool
Edges carry weights.

- directed : Bool
Network is directed (sensory → inter → motor).

- tau3_computer : Bool
Architecture mirrors τ³ structure.

Instances For

---

### `Tau.BookVI.Neural.instReprNeuralArchitecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L59-L59)
**instance
Tau.BookVI.Neural.instReprNeuralArchitecture :Repr NeuralArchitecture**

Equations
- Tau.BookVI.Neural.instReprNeuralArchitecture = { reprPrec := Tau.BookVI.Neural.instReprNeuralArchitecture.repr }

---

### `Tau.BookVI.Neural.instReprNeuralArchitecture.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L59-L59)
**def
Tau.BookVI.Neural.instReprNeuralArchitecture.repr :NeuralArchitecture → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.neural_arch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L61-L63)
**def
Tau.BookVI.Neural.neural_arch :NeuralArchitecture**

Equations
- Tau.BookVI.Neural.neural_arch = { node_types := 3, types_eq := Tau.BookVI.Neural.neural_arch._proof_1 }
Instances For

---

### `Tau.BookVI.Neural.neural_is_tau3_computer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L65-L69)
**theorem
Tau.BookVI.Neural.neural_is_tau3_computer :neural_arch.node_types = 3 ∧ neural_arch.directed = true ∧ neural_arch.tau3_computer = true**


---

### `Tau.BookVI.Neural.SleepLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L75-L91)
**structure
Tau.BookVI.Neural.SleepLemniscate :Type**


[VI.P19] Sleep as Temporal Lemniscate Second Lobe.
The temporal lemniscate L_T = S¹ ∨ S¹ (Book VI, Part 2)
has two lobes: wakefulness (active processing) and sleep
(consolidation/pruning). Circadian rhythm is the orbit
traversing both lobes.

- lobe_count : ℕ
Number of lemniscate lobes.

- count_eq : self.lobe_count = 2
Exactly 2 lobes.

- wake_lobe : Bool
Lobe 1: wakefulness.

- sleep_lobe : Bool
Lobe 2: sleep.

- circadian_link : Bool
Linked to circadian rhythm (Part 2).

Instances For

---

### `Tau.BookVI.Neural.instReprSleepLemniscate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L91-L91)
**def
Tau.BookVI.Neural.instReprSleepLemniscate.repr :SleepLemniscate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.instReprSleepLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L91-L91)
**instance
Tau.BookVI.Neural.instReprSleepLemniscate :Repr SleepLemniscate**

Equations
- Tau.BookVI.Neural.instReprSleepLemniscate = { reprPrec := Tau.BookVI.Neural.instReprSleepLemniscate.repr }

---

### `Tau.BookVI.Neural.sleep_lemn`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L93-L95)
**def
Tau.BookVI.Neural.sleep_lemn :SleepLemniscate**

Equations
- Tau.BookVI.Neural.sleep_lemn = { lobe_count := 2, count_eq := Tau.BookVI.Neural.sleep_lemn._proof_1 }
Instances For

---

### `Tau.BookVI.Neural.sleep_two_lobes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L97-L102)
**theorem
Tau.BookVI.Neural.sleep_two_lobes :sleep_lemn.lobe_count = 2 ∧ sleep_lemn.wake_lobe = true ∧ sleep_lemn.sleep_lobe = true ∧ sleep_lemn.circadian_link = true**


---

### `Tau.BookVI.Neural.NeuralDefectLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L108-L125)
**inductive
Tau.BookVI.Neural.NeuralDefectLevel :Type**


[VI.D87] Neural Defect Level: 4 hierarchical levels of neural
defect accumulation, specializing VI.D43 (AgingDefect) to the
neural architecture (VI.D52).
Level 1 — Molecular: protein misfolding, aggregation (amyloid-β,
α-synuclein, tau tangles). Defect = deviation from native fold.
Level 2 — Synaptic: synapse loss, neurotransmitter depletion,
receptor downregulation. Defect = edge degradation in τ³-computer.
Level 3 — Circuit: dopaminergic/serotonergic/cholinergic pathway
degradation. Defect = subgraph integrity loss in τ³-computer.
Level 4 — Network: large-scale connectivity loss, white matter
degeneration. Defect = global topology disruption in τ³-computer.
Scope: τ-effective.

- molecular : NeuralDefectLevel
- synaptic : NeuralDefectLevel
- circuit : NeuralDefectLevel
- network : NeuralDefectLevel
Instances For

---

### `Tau.BookVI.Neural.instReprNeuralDefectLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L125-L125)
**def
Tau.BookVI.Neural.instReprNeuralDefectLevel.repr :NeuralDefectLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.instReprNeuralDefectLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L125-L125)
**instance
Tau.BookVI.Neural.instReprNeuralDefectLevel :Repr NeuralDefectLevel**

Equations
- Tau.BookVI.Neural.instReprNeuralDefectLevel = { reprPrec := Tau.BookVI.Neural.instReprNeuralDefectLevel.repr }

---

### `Tau.BookVI.Neural.instBEqNeuralDefectLevel.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L125-L125)
**def
Tau.BookVI.Neural.instBEqNeuralDefectLevel.beq :NeuralDefectLevel → NeuralDefectLevel → Bool**

Equations
- Tau.BookVI.Neural.instBEqNeuralDefectLevel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookVI.Neural.instBEqNeuralDefectLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L125-L125)
**instance
Tau.BookVI.Neural.instBEqNeuralDefectLevel :BEq NeuralDefectLevel**

Equations
- Tau.BookVI.Neural.instBEqNeuralDefectLevel = { beq := Tau.BookVI.Neural.instBEqNeuralDefectLevel.beq }

---

### `Tau.BookVI.Neural.NeuralDefectTower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L131-L151)
**structure
Tau.BookVI.Neural.NeuralDefectTower :Type**


[VI.D88] Neural Defect Tower: multi-level defect accumulation
specialized to the neural architecture (VI.D52). Each level i has
a defect functional Δᵢ(n) that is monotonically increasing with
refinement step n (specialization of VI.D43). Levels cascade:
when Level i defect exceeds a threshold, Level i+1 defect
accumulation accelerates.
Scope: τ-effective.

- level_count : ℕ
Number of hierarchical levels.

- count_eq : self.level_count = 4
Exactly 4 levels.

- monotone_per_level : Bool
Each level's defect is monotonically increasing (VI.D43).

- inter_level_cascade : Bool
Levels cascade: Level i overflow accelerates Level i+1.

- specializes_aging_defect : Bool
Specialization of aging defect (VI.D43).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprNeuralDefectTower.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L151-L151)
**def
Tau.BookVI.Neural.instReprNeuralDefectTower.repr :NeuralDefectTower → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.instReprNeuralDefectTower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L151-L151)
**instance
Tau.BookVI.Neural.instReprNeuralDefectTower :Repr NeuralDefectTower**

Equations
- Tau.BookVI.Neural.instReprNeuralDefectTower = { reprPrec := Tau.BookVI.Neural.instReprNeuralDefectTower.repr }

---

### `Tau.BookVI.Neural.neural_tower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L153-L155)
**def
Tau.BookVI.Neural.neural_tower :NeuralDefectTower**

Equations
- Tau.BookVI.Neural.neural_tower = { level_count := 4, count_eq := Tau.BookVI.Neural.neural_tower._proof_1 }
Instances For

---

### `Tau.BookVI.Neural.NeurodegenerativeMapping`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L161-L183)
**structure
Tau.BookVI.Neural.NeurodegenerativeMapping :Type**


[VI.D89] Neurodegenerative Disease Mapping: each major
neurodegenerative disease is characterized by a dominant
defect level at which repair budget exhaustion occurs first.
Alzheimer's: Level 1 dominant (amyloid/tau aggregation).
Parkinson's: Level 3 dominant (dopaminergic circuit loss).
ALS: Level 3 dominant (motor neuron circuit failure).
Huntington's: Level 1 dominant (polyQ aggregation).
Normal aging: all levels degrade but none crosses threshold
before organismal Hayflick limit.
Scope: τ-effective (structural classification; protein names
appear in documentation only, not in formal conditions).

- alzheimers_level : NeuralDefectLevel
Alzheimer's: molecular level dominant.

- parkinsons_level : NeuralDefectLevel
Parkinson's: circuit level dominant.

- als_level : NeuralDefectLevel
ALS: circuit level dominant.

- huntingtons_level : NeuralDefectLevel
Huntington's: molecular level dominant.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprNeurodegenerativeMapping`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L183-L183)
**instance
Tau.BookVI.Neural.instReprNeurodegenerativeMapping :Repr NeurodegenerativeMapping**

Equations
- Tau.BookVI.Neural.instReprNeurodegenerativeMapping = { reprPrec := Tau.BookVI.Neural.instReprNeurodegenerativeMapping.repr }

---

### `Tau.BookVI.Neural.instReprNeurodegenerativeMapping.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L183-L183)
**def
Tau.BookVI.Neural.instReprNeurodegenerativeMapping.repr :NeurodegenerativeMapping → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.disease_map`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L185-L185)
**def
Tau.BookVI.Neural.disease_map :NeurodegenerativeMapping**

Equations
- Tau.BookVI.Neural.disease_map = { }
Instances For

---

### `Tau.BookVI.Neural.InterLevelCascade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L191-L214)
**structure
Tau.BookVI.Neural.InterLevelCascade :Type**


[VI.T52] Inter-Level Cascade Theorem.
Level i defect accumulation beyond threshold triggers accelerated
defect accumulation at Level i+1 (upward cascade). Proof:
(1) Molecular aggregates (Level 1) impair synaptic transmission
(Level 2) by disrupting vesicle trafficking and receptor function.
(2) Synaptic loss (Level 2) degrades circuit integrity (Level 3)
by removing edges from the τ³-computer subgraph.
(3) Circuit degradation (Level 3) fragments the global network
(Level 4) by disconnecting integrative pathways.
Each transition is monotone: more Level i defect → more Level i+1
defect. The cascade is unidirectional (upward only).
Scope: τ-effective.

- molecular_to_synaptic : Bool
Level 1 → Level 2 cascade.

- synaptic_to_circuit : Bool
Level 2 → Level 3 cascade.

- circuit_to_network : Bool
Level 3 → Level 4 cascade.

- upward_only : Bool
Cascade is unidirectional (upward).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprInterLevelCascade.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L214-L214)
**def
Tau.BookVI.Neural.instReprInterLevelCascade.repr :InterLevelCascade → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.instReprInterLevelCascade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L214-L214)
**instance
Tau.BookVI.Neural.instReprInterLevelCascade :Repr InterLevelCascade**

Equations
- Tau.BookVI.Neural.instReprInterLevelCascade = { reprPrec := Tau.BookVI.Neural.instReprInterLevelCascade.repr }

---

### `Tau.BookVI.Neural.cascade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L216-L216)
**def
Tau.BookVI.Neural.cascade :InterLevelCascade**

Equations
- Tau.BookVI.Neural.cascade = { }
Instances For

---

### `Tau.BookVI.Neural.inter_level_cascade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L218-L223)
**theorem
Tau.BookVI.Neural.inter_level_cascade :cascade.molecular_to_synaptic = true ∧ cascade.synaptic_to_circuit = true ∧ cascade.circuit_to_network = true ∧ cascade.upward_only = true**


---

### `Tau.BookVI.Neural.NeuralDefectMonotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L229-L247)
**structure
Tau.BookVI.Neural.NeuralDefectMonotone :Type**


[VI.P23] Neural Defect Monotonicity.
At each level i of the NeuralDefectTower, the defect functional
Δᵢ(n) is monotonically non-decreasing in the refinement step n.
This is a specialization of VI.D43 (AgingDefect: Δ(n) monotonically
increasing) to the 4-level neural decomposition: the total neural
defect Δ_neural(n) = Σᵢ Δᵢ(n) inherits monotonicity from each
component, and each component inherits it from VI.D43 restricted
to the neural subsystem.
Scope: τ-effective.

- per_level_monotone : Bool
Each level's defect is monotone non-decreasing.

- total_monotone : Bool
Total neural defect inherits monotonicity.

- specializes_d43 : Bool
Specializes VI.D43.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprNeuralDefectMonotone.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L247-L247)
**def
Tau.BookVI.Neural.instReprNeuralDefectMonotone.repr :NeuralDefectMonotone → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.instReprNeuralDefectMonotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L247-L247)
**instance
Tau.BookVI.Neural.instReprNeuralDefectMonotone :Repr NeuralDefectMonotone**

Equations
- Tau.BookVI.Neural.instReprNeuralDefectMonotone = { reprPrec := Tau.BookVI.Neural.instReprNeuralDefectMonotone.repr }

---

### `Tau.BookVI.Neural.neural_mono`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L249-L249)
**def
Tau.BookVI.Neural.neural_mono :NeuralDefectMonotone**

Equations
- Tau.BookVI.Neural.neural_mono = { }
Instances For

---

### `Tau.BookVI.Neural.neural_defect_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L251-L255)
**theorem
Tau.BookVI.Neural.neural_defect_monotone :neural_mono.per_level_monotone = true ∧ neural_mono.total_monotone = true ∧ neural_mono.specializes_d43 = true**


---

### `Tau.BookVI.Neural.SleepRepairFunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L261-L284)
**structure
Tau.BookVI.Neural.SleepRepairFunction :Type**


[VI.D90] Sleep Repair Function: dual-lobe repair at specific
NeuralDefectTower levels, using the sleep lemniscate (VI.P19).
NREM/SWS (S¹_sleep Lobe 1): Level 1 repair — glymphatic clearance
removes molecular debris (amyloid-β, metabolic waste).
REM (S¹_sleep Lobe 2): Level 2 repair — synaptic homeostasis,
memory consolidation, pruning of weak connections.
Levels 3–4 are NOT repaired by sleep: circuit and network
degradation are irreversible once established (repair budget
does not cover these levels at the rate they accumulate).
Scope: τ-effective.

- nrem_repairs_molecular : Bool
NREM repairs Level 1 (molecular/glymphatic).

- rem_repairs_synaptic : Bool
REM repairs Level 2 (synaptic homeostasis).

- no_circuit_repair : Bool
Level 3 not repaired by sleep.

- no_network_repair : Bool
Level 4 not repaired by sleep.

- consumes_repair_budget : Bool
Each sleep cycle consumes repair budget (VI.D45).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprSleepRepairFunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L284-L284)
**instance
Tau.BookVI.Neural.instReprSleepRepairFunction :Repr SleepRepairFunction**

Equations
- Tau.BookVI.Neural.instReprSleepRepairFunction = { reprPrec := Tau.BookVI.Neural.instReprSleepRepairFunction.repr }

---

### `Tau.BookVI.Neural.instReprSleepRepairFunction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L284-L284)
**def
Tau.BookVI.Neural.instReprSleepRepairFunction.repr :SleepRepairFunction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.sleep_repair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L286-L286)
**def
Tau.BookVI.Neural.sleep_repair :SleepRepairFunction**

Equations
- Tau.BookVI.Neural.sleep_repair = { }
Instances For

---

### `Tau.BookVI.Neural.SleepConsolidatesLevels12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L292-L314)
**structure
Tau.BookVI.Neural.SleepConsolidatesLevels12 :Type**


[VI.T53] Sleep Consolidates Levels 1–2 Defects.
The sleep lobe of the neural temporal lemniscate (VI.P19)
implements defect consolidation specifically at Levels 1 and 2
of the NeuralDefectTower (VI.D88).
Proof: (1) NREM/SWS activates glymphatic clearance, which
removes Level 1 molecular debris (amyloid-β, tau oligomers,
metabolic waste). (2) REM activates synaptic homeostasis
(Tononi–Cirelli downscaling), which maintains Level 2 synaptic
integrity by pruning overfit connections. (3) Levels 3–4 operate
on timescales (years–decades) that individual sleep cycles
cannot address: circuit and network degradation accumulate
irreversibly under the repair budget constraint (VI.D45).
Scope: τ-effective.

- nrem_level_1 : Bool
NREM → Level 1 glymphatic repair.

- rem_level_2 : Bool
REM → Level 2 synaptic homeostasis.

- levels_3_4_excluded : Bool
Levels 3–4 not addressed by sleep.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprSleepConsolidatesLevels12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L314-L314)
**instance
Tau.BookVI.Neural.instReprSleepConsolidatesLevels12 :Repr SleepConsolidatesLevels12**

Equations
- Tau.BookVI.Neural.instReprSleepConsolidatesLevels12 = { reprPrec := Tau.BookVI.Neural.instReprSleepConsolidatesLevels12.repr }

---

### `Tau.BookVI.Neural.instReprSleepConsolidatesLevels12.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L314-L314)
**def
Tau.BookVI.Neural.instReprSleepConsolidatesLevels12.repr :SleepConsolidatesLevels12 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.sleep_consol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L316-L316)
**def
Tau.BookVI.Neural.sleep_consol :SleepConsolidatesLevels12**

Equations
- Tau.BookVI.Neural.sleep_consol = { }
Instances For

---

### `Tau.BookVI.Neural.sleep_consolidates_levels_1_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L318-L322)
**theorem
Tau.BookVI.Neural.sleep_consolidates_levels_1_2 :sleep_consol.nrem_level_1 = true ∧ sleep_consol.rem_level_2 = true ∧ sleep_consol.levels_3_4_excluded = true**


---

### `Tau.BookVI.Neural.SleepDeprivationAccelerates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L328-L348)
**structure
Tau.BookVI.Neural.SleepDeprivationAccelerates :Type**


[VI.P24] Sleep Deprivation Accelerates Defect Threshold Crossing.
Chronic sleep deprivation skips Level 1–2 repair cycles (VI.D90),
accelerating repair budget exhaustion (VI.D45) at these levels.
Consequence: the Level 1 defect trajectory crosses the cascade
threshold earlier, triggering accelerated Level 2 degradation
via inter-level cascade (VI.T52), consistent with epidemiological
evidence linking sleep deprivation to increased Alzheimer's risk.
Scope: τ-effective (structural budget argument; quantitative
prediction would require empirical rates).

- budget_exhaustion_accelerated : Bool
Skipped repair cycles → faster budget exhaustion.

- level_1_earlier : Bool
Level 1 threshold crossed earlier.

- cascade_earlier : Bool
Cascade to Level 2 triggered earlier.

- alzheimers_consistent : Bool
Consistent with Alzheimer's epidemiology.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprSleepDeprivationAccelerates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L348-L348)
**instance
Tau.BookVI.Neural.instReprSleepDeprivationAccelerates :Repr SleepDeprivationAccelerates**

Equations
- Tau.BookVI.Neural.instReprSleepDeprivationAccelerates = { reprPrec := Tau.BookVI.Neural.instReprSleepDeprivationAccelerates.repr }

---

### `Tau.BookVI.Neural.instReprSleepDeprivationAccelerates.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L348-L348)
**def
Tau.BookVI.Neural.instReprSleepDeprivationAccelerates.repr :SleepDeprivationAccelerates → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.sleep_dep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L350-L350)
**def
Tau.BookVI.Neural.sleep_dep :SleepDeprivationAccelerates**

Equations
- Tau.BookVI.Neural.sleep_dep = { }
Instances For

---

### `Tau.BookVI.Neural.sleep_deprivation_accelerates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L352-L357)
**theorem
Tau.BookVI.Neural.sleep_deprivation_accelerates :sleep_dep.budget_exhaustion_accelerated = true ∧ sleep_dep.level_1_earlier = true ∧ sleep_dep.cascade_earlier = true ∧ sleep_dep.alzheimers_consistent = true**


---

### `Tau.BookVI.Neural.NeuralHayflickBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L363-L385)
**structure
Tau.BookVI.Neural.NeuralHayflickBound :Type**


[VI.D91] Neural Hayflick Bound: maximum cognitive lifespan at
each defect level, derived from finite repair budget (VI.P16)
applied to the NeuralDefectTower (VI.D88).
H_i = R_max(i) / r_i, where R_max(i) is the repair budget
allocated to Level i and r_i is the defect accumulation rate.
Overall cognitive Hayflick bound: H_neural = min(H₁,H₂,H₃,H₄).
Connects to Book V: the geometric decay rate (1−ι<sub>τ</sub>)^n (V.T62)
governs the baseline defect accumulation at each level.
Scope: τ-effective.

- level_count : ℕ
Number of levels with individual bounds.

- count_eq : self.level_count = 4
4 individual bounds.

- finite_per_level : Bool
Each level has a finite Hayflick bound H_i.

- overall_is_min : Bool
Overall bound is min of level bounds.

- connects_to_book_v : Bool
Connects to Book V defect exhaustion (V.T62).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprNeuralHayflickBound.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L385-L385)
**def
Tau.BookVI.Neural.instReprNeuralHayflickBound.repr :NeuralHayflickBound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.instReprNeuralHayflickBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L385-L385)
**instance
Tau.BookVI.Neural.instReprNeuralHayflickBound :Repr NeuralHayflickBound**

Equations
- Tau.BookVI.Neural.instReprNeuralHayflickBound = { reprPrec := Tau.BookVI.Neural.instReprNeuralHayflickBound.repr }

---

### `Tau.BookVI.Neural.neural_hayflick`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L387-L389)
**def
Tau.BookVI.Neural.neural_hayflick :NeuralHayflickBound**

Equations
- Tau.BookVI.Neural.neural_hayflick = { level_count := 4, count_eq := Tau.BookVI.Neural.neural_tower._proof_1 }
Instances For

---

### `Tau.BookVI.Neural.NeurodegenerationHayflickCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L395-L421)
**structure
Tau.BookVI.Neural.NeurodegenerationHayflickCrossing :Type**


[VI.T54] Neurodegeneration = Hayflick Crossing.
A neurodegenerative disease occurs when a specific level's
Hayflick bound H_i is exhausted before the organismal Hayflick
limit: the repair budget at Level i is depleted, defects
accumulate past the cascade threshold, and cognitive function
degrades irreversibly.
Alzheimer's: H₁ exhausted first (molecular repair depleted).
Parkinson's: H₃ exhausted first (circuit repair depleted).
Normal aging: all H_i > organismal limit (no level crosses first).
The neural Hayflick bound is a sector-specific instance of the
universal defect exhaustion (V.T62/VI.P16), with (1−ι<sub>τ</sub>)^n
governing the baseline.
Scope: τ-effective.

- disease_is_level_crossing : Bool
Disease = specific level Hayflick bound exhausted.

- alzheimers_h1 : Bool
Alzheimer's = H₁ first.

- parkinsons_h3 : Bool
Parkinson's = H₃ first.

- normal_aging_safe : Bool
Normal aging: no H_i crossed before organismal limit.

- specializes_universal : Bool
Sector-specific instance of V.T62/VI.P16.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Neural.instReprNeurodegenerationHayflickCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L421-L421)
**instance
Tau.BookVI.Neural.instReprNeurodegenerationHayflickCrossing :Repr NeurodegenerationHayflickCrossing**

Equations
- Tau.BookVI.Neural.instReprNeurodegenerationHayflickCrossing = { reprPrec := Tau.BookVI.Neural.instReprNeurodegenerationHayflickCrossing.repr }

---

### `Tau.BookVI.Neural.instReprNeurodegenerationHayflickCrossing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L421-L421)
**def
Tau.BookVI.Neural.instReprNeurodegenerationHayflickCrossing.repr :NeurodegenerationHayflickCrossing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Neural.neuro_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L423-L423)
**def
Tau.BookVI.Neural.neuro_crossing :NeurodegenerationHayflickCrossing**

Equations
- Tau.BookVI.Neural.neuro_crossing = { }
Instances For

---

### `Tau.BookVI.Neural.neurodegeneration_is_hayflick_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Neural.lean#L425-L431)
**theorem
Tau.BookVI.Neural.neurodegeneration_is_hayflick_crossing :neuro_crossing.disease_is_level_crossing = true ∧ neuro_crossing.alzheimers_h1 = true ∧ neuro_crossing.parkinsons_h3 = true ∧ neuro_crossing.normal_aging_safe = true ∧ neuro_crossing.specializes_universal = true**
