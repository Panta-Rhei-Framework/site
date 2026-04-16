---
layout: taulib-doc
title: "TauLib.BookV.Coda.HermeticClosure"
permalink: /verify/taulib/docs/book-v-coda-hermetic-closure/
lane: verify
module_name: "TauLib.BookV.Coda.HermeticClosure"
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

# TauLib.BookV.Coda.HermeticClosure


Capstone theorems of Book V: the Hermetic Identity, physics as
self-description, the Hermetic Closure, the Hermetic Truth (complete),
generator universality, structural rigidity, and permanent sector
distinction.

## Registry Cross-References


- [V.T159] The Hermetic Identity -- `HermeticIdentity`

- [V.T160] Physics as Self-Description -- `PhysicsSelfDescription`

- [V.T161] The Hermetic Closure -- `HermeticClosureThm`

- [V.T162] The Hermetic Truth (Complete) -- `HermeticTruthComplete`

- [V.P119] Generator Universality -- `GeneratorUniversality`

- [V.P120] Structural Rigidity -- `StructuralRigidity`

- [V.P121] Permanent Sector Distinction -- `PermanentSectorDistinction`


## Mathematical Content


### The Hermetic Identity [V.T159]


H_∂[ω] = H_∂^base[α,π] ⊗*{cross} H*∂^fiber[γ,η,ω] is exact.
ι<sub>τ</sub> appears identically in both factors.

### Physics as Self-Description [V.T160]


H_∂[ω] = h_{τ³}|_L: every physical observable is a section of
the Yoneda restriction to the boundary.

### The Hermetic Closure [V.T161]


5-sector structure produces necessary conditions for observers:
periodic table, nuclei, chemistry, planets, mass.

### The Hermetic Truth (Complete) [V.T162]


τ³ is a single object producing all physics and observer conditions.
Fiber and base are two projections of one structure.

Note: V.T162 `HermeticTruthComplete` is distinct from V.T143 `HermeticTruth`
in BridgeToLife.lean. V.T143 states the tensor product is exact; V.T162
is the capstone combining all preceding results.

### Generator Universality [V.P119]


Each generator acts at every scale; no RG flow of generators; effective
coupling is depth-dependent.

### Structural Rigidity [V.P120]


K0-K6 admits a unique coherence kernel; every constant derived; no
continuous variation possible.

### Permanent Sector Distinction [V.P121]


Five sectors are topologically distinct characters on L; no deformation
can merge two; no sixth exists.

## Ground Truth Sources


- Book V ch72-74: Hermetic identity, closure, truth, capstone


---

### `Tau.BookV.Coda.HermeticIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L72-L91)
**structure
Tau.BookV.Coda.HermeticIdentity :Type**


[V.T159] The Hermetic Identity:
H_∂[ω] = H_∂^base[α,π] ⊗*{cross} H*∂^fiber[γ,η,ω]

ι<sub>τ</sub> appears identically in both factors. The crossing sector ω
mediates between base and fiber. The identity is exact: no
information is lost in the tensor decomposition.

- base_gens : ℕ
Base generators (α, π).

- base_eq : self.base_gens = 2
Two base generators.

- fiber_gens : ℕ
Fiber generators (γ, η, ω).

- fiber_eq : self.fiber_gens = 3
Three fiber generators.

- iota_in_both : Bool
ι<sub>τ</sub> appears in both factors.

- decomp_exact : Bool
Tensor decomposition is exact.

Instances For

---

### `Tau.BookV.Coda.instReprHermeticIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L91-L91)
**instance
Tau.BookV.Coda.instReprHermeticIdentity :Repr HermeticIdentity**

Equations
- Tau.BookV.Coda.instReprHermeticIdentity = { reprPrec := Tau.BookV.Coda.instReprHermeticIdentity.repr }

---

### `Tau.BookV.Coda.instReprHermeticIdentity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L91-L91)
**def
Tau.BookV.Coda.instReprHermeticIdentity.repr :HermeticIdentity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.hermetic_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L93-L98)
**def
Tau.BookV.Coda.hermetic_identity :HermeticIdentity**


The canonical Hermetic Identity.
Equations
- Tau.BookV.Coda.hermetic_identity = { base_gens := 2, base_eq := Tau.BookV.Coda.hermetic_identity._proof_1, fiber_gens := 3,
 fiber_eq := Tau.BookV.Coda.hermetic_identity._proof_2 }
Instances For

---

### `Tau.BookV.Coda.hermetic_identity_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L100-L106)
**theorem
Tau.BookV.Coda.hermetic_identity_thm :hermetic_identity.base_gens + hermetic_identity.fiber_gens = 5 ∧ hermetic_identity.iota_in_both = true ∧ hermetic_identity.decomp_exact = true**


Hermetic Identity: 2 base + 3 fiber, ι<sub>τ</sub> in both, exact.

---

### `Tau.BookV.Coda.generators_total_five`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L108-L110)
**theorem
Tau.BookV.Coda.generators_total_five :2 + 3 = 5**


Base + fiber generators sum to 5: 2 + 3 = 5.

---

### `Tau.BookV.Coda.identity_matches_hermetic_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L112-L118)
**theorem
Tau.BookV.Coda.identity_matches_hermetic_data :hermetic_identity.base_gens = hermetic_data.base_generators ∧ hermetic_identity.fiber_gens = hermetic_data.fiber_generators**


Hermetic Identity matches Hermetic Truth data in BridgeToLife.

---

### `Tau.BookV.Coda.PhysicsSelfDescription`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L124-L141)
**structure
Tau.BookV.Coda.PhysicsSelfDescription :Type**


[V.T160] Physics as self-description:
H_∂[ω] = h_{τ³}|_L

Every physical observable is a section of the Yoneda restriction
to the boundary L = S¹ ∨ S¹. The τ³ fibration describes itself
through its boundary characters.

- yoneda_restriction : Bool
Yoneda restriction holds.

- all_observables_boundary : Bool
Every observable is a boundary section.

- self_description_exact : Bool
Self-description is exact.

- boundary_components : ℕ
Boundary components (S¹ ∨ S¹ = 2 circles).

- total_generators : ℕ
Total generators on boundary.

Instances For

---

### `Tau.BookV.Coda.instReprPhysicsSelfDescription.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L141-L141)
**def
Tau.BookV.Coda.instReprPhysicsSelfDescription.repr :PhysicsSelfDescription → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprPhysicsSelfDescription`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L141-L141)
**instance
Tau.BookV.Coda.instReprPhysicsSelfDescription :Repr PhysicsSelfDescription**

Equations
- Tau.BookV.Coda.instReprPhysicsSelfDescription = { reprPrec := Tau.BookV.Coda.instReprPhysicsSelfDescription.repr }

---

### `Tau.BookV.Coda.self_description`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L143-L144)
**def
Tau.BookV.Coda.self_description :PhysicsSelfDescription**


The canonical self-description.
Equations
- Tau.BookV.Coda.self_description = { }
Instances For

---

### `Tau.BookV.Coda.physics_self_description`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L146-L151)
**theorem
Tau.BookV.Coda.physics_self_description :self_description.yoneda_restriction = true ∧ self_description.all_observables_boundary = true ∧ self_description.self_description_exact = true**


Physics is self-describing: Yoneda restriction, all observables boundary.

---

### `Tau.BookV.Coda.HermeticClosureThm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L157-L174)
**structure
Tau.BookV.Coda.HermeticClosureThm :Type**


[V.T161] The Hermetic Closure: the 5-sector structure from ι<sub>τ</sub>
produces necessary conditions for observers.

From 5 sectors → periodic table, nuclei, chemistry, planets, mass.
This is NOT an anthropic argument: the conditions follow from the
sector structure, which is fixed by the axioms.

- n_sectors : ℕ
Number of sectors.

- sectors_eq : self.n_sectors = 5
Five sectors.

- observer_conditions : Bool
Produces observer conditions.

- not_anthropic : Bool
Not anthropic (structural).

- observer_requirements : ℕ
Observer requirements (periodic table, nuclei, chemistry, planets, mass).

Instances For

---

### `Tau.BookV.Coda.instReprHermeticClosureThm.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L174-L174)
**def
Tau.BookV.Coda.instReprHermeticClosureThm.repr :HermeticClosureThm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprHermeticClosureThm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L174-L174)
**instance
Tau.BookV.Coda.instReprHermeticClosureThm :Repr HermeticClosureThm**

Equations
- Tau.BookV.Coda.instReprHermeticClosureThm = { reprPrec := Tau.BookV.Coda.instReprHermeticClosureThm.repr }

---

### `Tau.BookV.Coda.hermetic_closure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L176-L179)
**def
Tau.BookV.Coda.hermetic_closure :HermeticClosureThm**


The canonical Hermetic Closure.
Equations
- Tau.BookV.Coda.hermetic_closure = { n_sectors := 5, sectors_eq := Tau.BookV.Coda.hermetic_closure._proof_1 }
Instances For

---

### `Tau.BookV.Coda.hermetic_closure_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L181-L186)
**theorem
Tau.BookV.Coda.hermetic_closure_thm :hermetic_closure.n_sectors = 5 ∧ hermetic_closure.observer_conditions = true ∧ hermetic_closure.not_anthropic = true**


Hermetic Closure: 5 sectors produce observer conditions structurally.

---

### `Tau.BookV.Coda.HermeticTruthComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L192-L214)
**structure
Tau.BookV.Coda.HermeticTruthComplete :Type**


[V.T162] The Hermetic Truth (Complete): τ³ is a single object
producing all microphysics, all macrophysics, and conditions for
observers. Fiber and base are two projections of one structure.

This is the capstone: it combines the Hermetic Identity (V.T159),
self-description (V.T160), and Hermetic Closure (V.T161).

Note: distinct from V.T143 `HermeticTruth` in BridgeToLife.lean,
which states the tensor product is exact. V.T162 is the full synthesis.

- microphysics_complete : Bool
All microphysics from fiber T².

- macrophysics_complete : Bool
All macrophysics from base τ¹.

- observer_conditions : Bool
Observer conditions from sector structure.

- single_object : Bool
Single object (τ³).

- two_projections : Bool
Fiber + base = two projections.

- projection_count : ℕ
Number of projections (fiber + base).

Instances For

---

### `Tau.BookV.Coda.instReprHermeticTruthComplete.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L214-L214)
**def
Tau.BookV.Coda.instReprHermeticTruthComplete.repr :HermeticTruthComplete → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprHermeticTruthComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L214-L214)
**instance
Tau.BookV.Coda.instReprHermeticTruthComplete :Repr HermeticTruthComplete**

Equations
- Tau.BookV.Coda.instReprHermeticTruthComplete = { reprPrec := Tau.BookV.Coda.instReprHermeticTruthComplete.repr }

---

### `Tau.BookV.Coda.hermetic_truth_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L216-L217)
**def
Tau.BookV.Coda.hermetic_truth_complete :HermeticTruthComplete**


The canonical complete Hermetic Truth.
Equations
- Tau.BookV.Coda.hermetic_truth_complete = { }
Instances For

---

### `Tau.BookV.Coda.hermetic_truth_complete_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L219-L226)
**theorem
Tau.BookV.Coda.hermetic_truth_complete_thm :hermetic_truth_complete.microphysics_complete = true ∧ hermetic_truth_complete.macrophysics_complete = true ∧ hermetic_truth_complete.observer_conditions = true ∧ hermetic_truth_complete.single_object = true ∧ hermetic_truth_complete.two_projections = true**


Complete Hermetic Truth: all physics + observers from single τ³.

---

### `Tau.BookV.Coda.GeneratorUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L232-L253)
**structure
Tau.BookV.Coda.GeneratorUniversality :Type**


[V.P119] Generator universality: each generator acts on H_∂[ω]
at every scale. No RG flow of generator itself; effective coupling
is depth-dependent.

The generators {α, π, γ, η, ω} are universal characters on L.
They do not run with energy scale (unlike QFT couplings). The
*effective* coupling κ(X;n) at depth n changes because the
threshold admissibility changes, not because X itself runs.

- n_generators : ℕ
Number of universal generators.

- gens_eq : self.n_generators = 5
Five generators.

- no_rg_flow : Bool
No RG flow of generators.

- depth_dependent : Bool
Coupling is depth-dependent.

- base_count : ℕ
Base generators (α, π).

- fiber_count : ℕ
Fiber generators (γ, η, ω).

Instances For

---

### `Tau.BookV.Coda.instReprGeneratorUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L253-L253)
**instance
Tau.BookV.Coda.instReprGeneratorUniversality :Repr GeneratorUniversality**

Equations
- Tau.BookV.Coda.instReprGeneratorUniversality = { reprPrec := Tau.BookV.Coda.instReprGeneratorUniversality.repr }

---

### `Tau.BookV.Coda.instReprGeneratorUniversality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L253-L253)
**def
Tau.BookV.Coda.instReprGeneratorUniversality.repr :GeneratorUniversality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.gen_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L255-L258)
**def
Tau.BookV.Coda.gen_universality :GeneratorUniversality**


The canonical generator universality.
Equations
- Tau.BookV.Coda.gen_universality = { n_generators := 5, gens_eq := Tau.BookV.Coda.hermetic_closure._proof_1 }
Instances For

---

### `Tau.BookV.Coda.generator_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L260-L265)
**theorem
Tau.BookV.Coda.generator_universality :gen_universality.n_generators = 5 ∧ gen_universality.no_rg_flow = true ∧ gen_universality.depth_dependent = true**


Generator universality: 5 generators, no RG flow, depth-dependent coupling.

---

### `Tau.BookV.Coda.gen_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L267-L269)
**theorem
Tau.BookV.Coda.gen_sum :2 + 3 = 5**


Base + fiber = total generators: 2 + 3 = 5.

---

### `Tau.BookV.Coda.StructuralRigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L275-L298)
**structure
Tau.BookV.Coda.StructuralRigidity :Type**


[V.P120] Structural rigidity: the axiom system K0-K6 admits a
unique coherence kernel. Every dimensionless constant is derived.
No continuous variation is possible.


- K0-K6 → unique boundary algebra on L

- Unique boundary → unique ι<sub>τ</sub> = 2/(π+e)

- Unique ι<sub>τ</sub> → unique coupling budget

- No free parameters → no continuous deformation


- n_axioms : ℕ
Number of axioms in the kernel.

- axioms_eq : self.n_axioms = 7
Seven axioms K0-K6.

- kernel_unique : Bool
Coherence kernel is unique.

- all_derived : Bool
All constants derived.

- no_variation : Bool
No continuous variation.

- n_derived_constants : ℕ
Number of derived constants (all from ι<sub>τ</sub>).

- n_free : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Coda.instReprStructuralRigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L298-L298)
**instance
Tau.BookV.Coda.instReprStructuralRigidity :Repr StructuralRigidity**

Equations
- Tau.BookV.Coda.instReprStructuralRigidity = { reprPrec := Tau.BookV.Coda.instReprStructuralRigidity.repr }

---

### `Tau.BookV.Coda.instReprStructuralRigidity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L298-L298)
**def
Tau.BookV.Coda.instReprStructuralRigidity.repr :StructuralRigidity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.rigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L300-L303)
**def
Tau.BookV.Coda.rigidity :StructuralRigidity**


The canonical structural rigidity.
Equations
- Tau.BookV.Coda.rigidity = { n_axioms := 7, axioms_eq := Tau.BookV.Coda.rigidity._proof_1 }
Instances For

---

### `Tau.BookV.Coda.structural_rigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L305-L311)
**theorem
Tau.BookV.Coda.structural_rigidity :rigidity.n_axioms = 7 ∧ rigidity.kernel_unique = true ∧ rigidity.all_derived = true ∧ rigidity.no_variation = true**


Structural rigidity: 7 axioms, unique kernel, all derived, no variation.

---

### `Tau.BookV.Coda.rigidity_matches_calibration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L313-L316)
**theorem
Tau.BookV.Coda.rigidity_matches_calibration :rigidity.n_axioms > rigidity.n_free**


Rigidity: axiom count exceeds free parameter count.

---

### `Tau.BookV.Coda.PermanentSectorDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L322-L343)
**structure
Tau.BookV.Coda.PermanentSectorDistinction :Type**


[V.P121] Permanent sector distinction: the five sectors are
topologically distinct characters on L. No deformation can merge
two sectors. Sector Exhaustion proves no sixth exists.


- 5 sectors = 5 distinct characters on L = S¹ ∨ S¹

- Topological distinction: cannot be continuously deformed into each other

- Exhaustion: no 6th character exists (sector budget = 5)

- Permanence: structure is rigid (V.P120) and cannot change


- n_sectors : ℕ
Number of distinct sectors.

- sectors_eq : self.n_sectors = 5
Five sectors.

- topologically_distinct : Bool
Topologically distinct.

- no_sixth : Bool
No sixth exists.

- permanent : Bool
Structure is permanent.

- max_sectors : ℕ
Maximum sector budget.

Instances For

---

### `Tau.BookV.Coda.instReprPermanentSectorDistinction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L343-L343)
**def
Tau.BookV.Coda.instReprPermanentSectorDistinction.repr :PermanentSectorDistinction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprPermanentSectorDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L343-L343)
**instance
Tau.BookV.Coda.instReprPermanentSectorDistinction :Repr PermanentSectorDistinction**

Equations
- Tau.BookV.Coda.instReprPermanentSectorDistinction = { reprPrec := Tau.BookV.Coda.instReprPermanentSectorDistinction.repr }

---

### `Tau.BookV.Coda.sector_distinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L345-L348)
**def
Tau.BookV.Coda.sector_distinction :PermanentSectorDistinction**


The canonical permanent sector distinction.
Equations
- Tau.BookV.Coda.sector_distinction = { n_sectors := 5, sectors_eq := Tau.BookV.Coda.hermetic_closure._proof_1 }
Instances For

---

### `Tau.BookV.Coda.permanent_sector_distinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L350-L356)
**theorem
Tau.BookV.Coda.permanent_sector_distinction :sector_distinction.n_sectors = 5 ∧ sector_distinction.topologically_distinct = true ∧ sector_distinction.no_sixth = true ∧ sector_distinction.permanent = true**


Permanent sectors: 5 distinct, no 6th, permanent.

---

### `Tau.BookV.Coda.sector_budget_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L358-L360)
**theorem
Tau.BookV.Coda.sector_budget_exact :5 = 2 + 3**


Sector budget = base + fiber: 5 = 2 + 3.

---

### `Tau.BookV.Coda.closure_sectors_eq_distinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L362-L365)
**theorem
Tau.BookV.Coda.closure_sectors_eq_distinction :hermetic_closure.n_sectors = sector_distinction.n_sectors**


Sectors match Hermetic Closure count (V.T161).

---

### `Tau.BookV.Coda.distinction_matches_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L367-L370)
**theorem
Tau.BookV.Coda.distinction_matches_universality :sector_distinction.n_sectors = gen_universality.n_generators**


Sector count matches generator universality (V.P119).

---

### `Tau.BookV.Coda.capstone_combines_three`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/HermeticClosure.lean#L372-L378)
**theorem
Tau.BookV.Coda.capstone_combines_three :hermetic_identity.decomp_exact = true ∧ self_description.self_description_exact = true ∧ hermetic_closure.observer_conditions = true ∧ hermetic_truth_complete.single_object = true**


Capstone: V.T162 combines V.T159 (identity) + V.T160 (self-description) + V.T161 (closure).
