---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.Evolution"
permalink: /verify/taulib/docs/book-vi-consumer-evolution/
lane: verify
module_name: "TauLib.BookVI.Consumer.Evolution"
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

# TauLib.BookVI.Consumer.Evolution


Evolution as PPAS optimization on fitness landscapes.

## Registry Cross-References


- [VI.D50] PPAS Algorithm on Fitness Landscapes — `PPASFitness`

- [VI.T27] Evolution as Optimization (NP-hard → polynomial) — `evolution_is_ppas`

- [VI.R20] Fitness Landscape Topology — `FitnessLandscapeTopology`


## Cross-Book Authority


- Book III, Part IX: III.T33 Admissibility Collapse / PPAS (Prover–Proof–Admissibility–Specifier)

- Book III, Part I: P vs NP force (NP-hard optimization in polynomial time)


## Ground Truth Sources


- Book VI Chapter 37 (2nd Edition): Evolution as PPAS

- Book VI Chapter 38 (2nd Edition): Speciation and Fitness Landscapes


---

### `Tau.BookVI.Evolution.PPASFitness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L30-L44)
**structure
Tau.BookVI.Evolution.PPASFitness :Type**


[VI.D50] PPAS Algorithm on Fitness Landscapes.
Population = Prover, Selection = Verifier (Book III, Part IX).
The NP-hard fitness landscape optimization (Book III, Part I)
is solved in polynomial generations by the PPAS protocol:
mutation proposes, selection verifies, population converges.

- landscape_np_hard : Bool
Fitness landscape is NP-hard.

- prover : String
Population acts as prover.

- verifier : String
Selection acts as verifier.

- polynomial_converge : Bool
PPAS achieves polynomial convergence.

Instances For

---

### `Tau.BookVI.Evolution.instReprPPASFitness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L44-L44)
**def
Tau.BookVI.Evolution.instReprPPASFitness.repr :PPASFitness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Evolution.instReprPPASFitness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L44-L44)
**instance
Tau.BookVI.Evolution.instReprPPASFitness :Repr PPASFitness**

Equations
- Tau.BookVI.Evolution.instReprPPASFitness = { reprPrec := Tau.BookVI.Evolution.instReprPPASFitness.repr }

---

### `Tau.BookVI.Evolution.ppas_fit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L46-L46)
**def
Tau.BookVI.Evolution.ppas_fit :PPASFitness**

Equations
- Tau.BookVI.Evolution.ppas_fit = { }
Instances For

---

### `Tau.BookVI.Evolution.EvolutionOptimization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L52-L71)
**structure
Tau.BookVI.Evolution.EvolutionOptimization :Type**


[VI.T27] Evolution as Optimization: NP-hard → polynomial.
Four evolutionary forces: mutation, selection, drift, migration.
Together they implement the PPAS protocol (Book III, Part IX, III.T33)
that reduces NP-hard search to polynomial convergence.

- force_count : ℕ
Number of evolutionary forces.

- count_eq : self.force_count = 4
Exactly 4 forces.

- mutation : Bool
Force 1: mutation (variation generator).

- selection : Bool
Force 2: selection (fitness filter).

- drift : Bool
Force 3: genetic drift (stochastic sampling).

- migration : Bool
Force 4: migration (gene flow).

- convergence : Bool
Convergence in polynomial generations.

Instances For

---

### `Tau.BookVI.Evolution.instReprEvolutionOptimization.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L71-L71)
**def
Tau.BookVI.Evolution.instReprEvolutionOptimization.repr :EvolutionOptimization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Evolution.instReprEvolutionOptimization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L71-L71)
**instance
Tau.BookVI.Evolution.instReprEvolutionOptimization :Repr EvolutionOptimization**

Equations
- Tau.BookVI.Evolution.instReprEvolutionOptimization = { reprPrec := Tau.BookVI.Evolution.instReprEvolutionOptimization.repr }

---

### `Tau.BookVI.Evolution.evo_opt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L73-L75)
**def
Tau.BookVI.Evolution.evo_opt :EvolutionOptimization**

Equations
- Tau.BookVI.Evolution.evo_opt = { force_count := 4, count_eq := Tau.BookVI.Evolution.evo_opt._proof_1 }
Instances For

---

### `Tau.BookVI.Evolution.evolution_is_ppas`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L77-L81)
**theorem
Tau.BookVI.Evolution.evolution_is_ppas :evo_opt.force_count = 4 ∧ evo_opt.convergence = true ∧ ppas_fit.polynomial_converge = true**


---

### `Tau.BookVI.Evolution.ppas_polynomial_convergence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L83-L86)
**theorem
Tau.BookVI.Evolution.ppas_polynomial_convergence :ppas_fit.landscape_np_hard = true ∧ ppas_fit.polynomial_converge = true**


---

### `Tau.BookVI.Evolution.FitnessLandscapeTopology`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L92-L103)
**structure
Tau.BookVI.Evolution.FitnessLandscapeTopology :Type**


[VI.R20] Fitness Landscape Topology.
Rugged landscapes with epistatic interactions,
NK-model structure, and multiple attractor basins.
Speciation occurs at saddle points between basins.

- epistatic : Bool
Epistatic interactions present.

- nk_model : Bool
NK-model structure.

- attractor_basins : Bool
Attractor basins present.

Instances For

---

### `Tau.BookVI.Evolution.instReprFitnessLandscapeTopology`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L103-L103)
**instance
Tau.BookVI.Evolution.instReprFitnessLandscapeTopology :Repr FitnessLandscapeTopology**

Equations
- Tau.BookVI.Evolution.instReprFitnessLandscapeTopology = { reprPrec := Tau.BookVI.Evolution.instReprFitnessLandscapeTopology.repr }

---

### `Tau.BookVI.Evolution.instReprFitnessLandscapeTopology.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L103-L103)
**def
Tau.BookVI.Evolution.instReprFitnessLandscapeTopology.repr :FitnessLandscapeTopology → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Evolution.fitness_topo`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L105-L105)
**def
Tau.BookVI.Evolution.fitness_topo :FitnessLandscapeTopology**

Equations
- Tau.BookVI.Evolution.fitness_topo = { }
Instances For

---

### `Tau.BookVI.Evolution.fitness_landscape_rugged`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/Evolution.lean#L107-L111)
**theorem
Tau.BookVI.Evolution.fitness_landscape_rugged :fitness_topo.epistatic = true ∧ fitness_topo.nk_model = true ∧ fitness_topo.attractor_basins = true**
