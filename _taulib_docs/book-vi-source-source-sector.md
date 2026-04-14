---
layout: taulib-doc
title: "TauLib.BookVI.Source.SourceSector"
permalink: /verify/taulib/docs/book-vi-source-source-sector/
lane: verify
module_name: "TauLib.BookVI.Source.SourceSector"
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

# TauLib.BookVI.Source.SourceSector


Source sector (Part 4): π'-sector structure generation on fiber.
Archetype: Plants. Dominant forces: Hodge + BSD.

## Registry Cross-References


- [VI.D36] Source Sector — `SourceSectorDef`

- [VI.D37] Structure Generation Predicate — `StructureGenerationPredicate`

- [VI.T20] Source = π'-Fiber Production — `source_is_pi_prime_production`

- [VI.D38] Carbon Fixation as Canonical Production — `CarbonFixation`

- [VI.P13] Quantum Coherence in FMO Complex — `fmo_quantum_coherence`


## Cross-Book Authority


- Book I, Part I: π' generator (solenoidal, fiber T²)

- Book II, Part II: τ³ = τ¹ ×_f T² fibration structure

- Book III, Part IV: Hodge force (harmonic decomposition, morphogenesis)

- Book III, Part V: BSD force (rational points, genetic code)

- Book III, Part I: P vs NP force (quantum coherence)


## Ground Truth Sources


- Book VI Chapter 23 (2nd Edition): The Source Sector

- Book VI Chapter 24 (2nd Edition): Photosynthesis


---

### `Tau.BookVI.Source.SourceSectorDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L38-L53)
**structure
Tau.BookVI.Source.SourceSectorDef :Type**


[VI.D36] Source Sector: π'-sector on fiber T².
Life Loop restricted to structure generation on the fiber.
Generator: π' (solenoidal, Book I Part I).
Dominant forces: Hodge + BSD (Book III, Parts IV–V).

- generator : String
Generator is pi' (fiber).

- is_primitive : Bool
Sector is primitive (single generator).

- archetype : String
Archetype organism.

- dominant_hodge : Bool
Dominant force 1: Hodge (harmonic decomposition → morphogenesis).

- dominant_bsd : Bool
Dominant force 2: BSD (rank of rational points → genetic code).

Instances For

---

### `Tau.BookVI.Source.instReprSourceSectorDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L53-L53)
**instance
Tau.BookVI.Source.instReprSourceSectorDef :Repr SourceSectorDef**

Equations
- Tau.BookVI.Source.instReprSourceSectorDef = { reprPrec := Tau.BookVI.Source.instReprSourceSectorDef.repr }

---

### `Tau.BookVI.Source.instReprSourceSectorDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L53-L53)
**def
Tau.BookVI.Source.instReprSourceSectorDef.repr :SourceSectorDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Source.source_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L55-L55)
**def
Tau.BookVI.Source.source_def :SourceSectorDef**

Equations
- Tau.BookVI.Source.source_def = { }
Instances For

---

### `Tau.BookVI.Source.source_generator_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L57-L60)
**theorem
Tau.BookVI.Source.source_generator_match :source_def.generator = FourPlusOne.source_sector.generator**


Source sector matches the FourPlusOne source_sector definition.

---

### `Tau.BookVI.Source.StructureGenerationPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L66-L81)
**structure
Tau.BookVI.Source.StructureGenerationPredicate :Type**


[VI.D37] Structure Generation Predicate: 3 conditions.
(i) Net production of structural complexity on T² fiber
(ii) Hodge capacity gradient positive (Book III, Part IV)
(iii) Energy input from base τ¹ (photon capture or equivalent)

- condition_count : ℕ
Number of conditions.

- count_eq : self.condition_count = 3
Exactly 3 conditions.

- net_production : Bool
(i) Net production on fiber.

- hodge_gradient_positive : Bool
(ii) Hodge capacity gradient positive.

- base_energy_input : Bool
(iii) Energy input from base.

Instances For

---

### `Tau.BookVI.Source.instReprStructureGenerationPredicate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L81-L81)
**def
Tau.BookVI.Source.instReprStructureGenerationPredicate.repr :StructureGenerationPredicate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Source.instReprStructureGenerationPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L81-L81)
**instance
Tau.BookVI.Source.instReprStructureGenerationPredicate :Repr StructureGenerationPredicate**

Equations
- Tau.BookVI.Source.instReprStructureGenerationPredicate = { reprPrec := Tau.BookVI.Source.instReprStructureGenerationPredicate.repr }

---

### `Tau.BookVI.Source.struct_gen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L83-L85)
**def
Tau.BookVI.Source.struct_gen :StructureGenerationPredicate**

Equations
- Tau.BookVI.Source.struct_gen = { condition_count := 3, count_eq := Tau.BookVI.Source.struct_gen._proof_1 }
Instances For

---

### `Tau.BookVI.Source.generation_three_conditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L87-L89)
**theorem
Tau.BookVI.Source.generation_three_conditions :struct_gen.condition_count = 3**


---

### `Tau.BookVI.Source.generation_all_hold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L91-L95)
**theorem
Tau.BookVI.Source.generation_all_hold :struct_gen.net_production = true ∧ struct_gen.hodge_gradient_positive = true ∧ struct_gen.base_energy_input = true**


---

### `Tau.BookVI.Source.SourceProduction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L101-L111)
**structure
Tau.BookVI.Source.SourceProduction :Type**


[VI.T20] Source = π'-Fiber Production Theorem.
A source Life loop has nontrivial π'-winding on the fiber
with net positive structure generation.

- winding_pi_prime : ℕ
Winding on π' (fiber).

- pi_prime_nontrivial : self.winding_pi_prime ≥ 1
Winding is nontrivial (≥ 1).

- net_generation : Bool
Net structure generation.

Instances For

---

### `Tau.BookVI.Source.instReprSourceProduction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L111-L111)
**instance
Tau.BookVI.Source.instReprSourceProduction :Repr SourceProduction**

Equations
- Tau.BookVI.Source.instReprSourceProduction = { reprPrec := Tau.BookVI.Source.instReprSourceProduction.repr }

---

### `Tau.BookVI.Source.instReprSourceProduction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L111-L111)
**def
Tau.BookVI.Source.instReprSourceProduction.repr :SourceProduction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Source.source_prod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L113-L115)
**def
Tau.BookVI.Source.source_prod :SourceProduction**

Equations
- Tau.BookVI.Source.source_prod = { winding_pi_prime := 1, pi_prime_nontrivial := Tau.BookVI.Source.source_prod._proof_1 }
Instances For

---

### `Tau.BookVI.Source.source_is_pi_prime_production`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L117-L120)
**theorem
Tau.BookVI.Source.source_is_pi_prime_production :source_prod.winding_pi_prime ≥ 1 ∧ source_prod.net_generation = true**


---

### `Tau.BookVI.Source.CarbonFixation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L126-L138)
**structure
Tau.BookVI.Source.CarbonFixation :Type**


[VI.D38] Carbon Fixation as Canonical Source Production.
Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.
The archetypal structure generation process.

- co2_per_glucose : ℕ
CO₂ molecules fixed per glucose.

- co2_eq : self.co2_per_glucose = 6
Exactly 6.

- hodge_driven : Bool
Driven by Hodge capacity gradient.

- global_fixation_gt : ℕ
Global rate: ~120 Gt C/yr.

Instances For

---

### `Tau.BookVI.Source.instReprCarbonFixation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L138-L138)
**instance
Tau.BookVI.Source.instReprCarbonFixation :Repr CarbonFixation**

Equations
- Tau.BookVI.Source.instReprCarbonFixation = { reprPrec := Tau.BookVI.Source.instReprCarbonFixation.repr }

---

### `Tau.BookVI.Source.instReprCarbonFixation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L138-L138)
**def
Tau.BookVI.Source.instReprCarbonFixation.repr :CarbonFixation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Source.carbon_fix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L140-L142)
**def
Tau.BookVI.Source.carbon_fix :CarbonFixation**

Equations
- Tau.BookVI.Source.carbon_fix = { co2_per_glucose := 6, co2_eq := Tau.BookVI.Source.carbon_fix._proof_1 }
Instances For

---

### `Tau.BookVI.Source.FMOCoherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L148-L163)
**structure
Tau.BookVI.Source.FMOCoherence :Type**


[VI.P13] Quantum Coherence in FMO Complex (conjectural).
The Fenna-Matthews-Olson complex exploits quantum coherence for
near-unity energy transfer efficiency. Interpreted as
P vs NP force at E₂ (Book III, Part I): the complex solves
an NP-hard optimization (exciton routing) in polynomial time
by exploiting quantum superposition.

- efficiency_percent : ℕ
Transfer efficiency (percent).

- high_efficiency : self.efficiency_percent ≥ 95
Near-unity: ≥ 95%.

- p_vs_np_connection : Bool
Connected to P vs NP force (Book III, Part I).

- scope : String
Scope: conjectural.

Instances For

---

### `Tau.BookVI.Source.instReprFMOCoherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L163-L163)
**instance
Tau.BookVI.Source.instReprFMOCoherence :Repr FMOCoherence**

Equations
- Tau.BookVI.Source.instReprFMOCoherence = { reprPrec := Tau.BookVI.Source.instReprFMOCoherence.repr }

---

### `Tau.BookVI.Source.instReprFMOCoherence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L163-L163)
**def
Tau.BookVI.Source.instReprFMOCoherence.repr :FMOCoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Source.fmo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L165-L167)
**def
Tau.BookVI.Source.fmo :FMOCoherence**

Equations
- Tau.BookVI.Source.fmo = { efficiency_percent := 99, high_efficiency := Tau.BookVI.Source.fmo._proof_2 }
Instances For

---

### `Tau.BookVI.Source.fmo_quantum_coherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/SourceSector.lean#L169-L172)
**theorem
Tau.BookVI.Source.fmo_quantum_coherence :fmo.efficiency_percent ≥ 95 ∧ fmo.p_vs_np_connection = true**
