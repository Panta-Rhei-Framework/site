---
layout: taulib-doc
title: "TauLib.BookIV.Arena.CoherenceKernel"
permalink: /verify/taulib/docs/book-iv-arena-coherence-kernel/
lane: verify
module_name: "TauLib.BookIV.Arena.CoherenceKernel"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Arena.CoherenceKernel


The coherence kernel K: the categorical core that generates all physics.
At E₁ it manifests as the 5-generator system {α,π,γ,η,ω} with canonical
sector assignment.

## Registry Cross-References


- [IV.D246] Coherence Kernel — Physics Presentation — `CoherenceKernel`

- [IV.D247] Generator–Sector Assignment — `GenSectorAssignment`

- [IV.P146] Uniqueness of Assignment — `assignment_unique`

- [IV.D248] Ontic Minimality — `ontic_minimality`


## Mathematical Content


The coherence kernel wraps the 5 generators with their canonical sector
assignment Φ: {α,π,γ,η,ω} → {D,A,B,C,Ω}. The assignment is unique (any
polarity-preserving, depth-respecting map must agree with Φ) and ontically
minimal (no proper subset of generators spans all 5 sectors).

## Ground Truth Sources


- Chapter 2 of Book IV (2nd Edition)


---

### `Tau.BookIV.Arena.GenSectorAssignment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L37-L45)
**def
Tau.BookIV.Arena.GenSectorAssignment
(g : Kernel.Generator)
 :BookIII.Sectors.Sector**


[IV.D247] The bijective map Φ: {α,π,γ,η,ω} → {D,A,B,C,Ω}
assigning each generator to its unique sector.
Equations
- Tau.BookIV.Arena.GenSectorAssignment Tau.Kernel.Generator.alpha = Tau.BookIII.Sectors.Sector.D
- Tau.BookIV.Arena.GenSectorAssignment Tau.Kernel.Generator.pi = Tau.BookIII.Sectors.Sector.A
- Tau.BookIV.Arena.GenSectorAssignment Tau.Kernel.Generator.gamma = Tau.BookIII.Sectors.Sector.B
- Tau.BookIV.Arena.GenSectorAssignment Tau.Kernel.Generator.eta = Tau.BookIII.Sectors.Sector.C
- Tau.BookIV.Arena.GenSectorAssignment Tau.Kernel.Generator.omega = Tau.BookIII.Sectors.Sector.Omega
Instances For

---

### `Tau.BookIV.Arena.assignment_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L47-L59)
**theorem
Tau.BookIV.Arena.assignment_injective :GenSectorAssignment Kernel.Generator.alpha ≠ GenSectorAssignment Kernel.Generator.pi ∧ GenSectorAssignment Kernel.Generator.alpha ≠ GenSectorAssignment Kernel.Generator.gamma ∧ GenSectorAssignment Kernel.Generator.alpha ≠ GenSectorAssignment Kernel.Generator.eta ∧ GenSectorAssignment Kernel.Generator.alpha ≠ GenSectorAssignment Kernel.Generator.omega ∧ GenSectorAssignment Kernel.Generator.pi ≠ GenSectorAssignment Kernel.Generator.gamma ∧ GenSectorAssignment Kernel.Generator.pi ≠ GenSectorAssignment Kernel.Generator.eta ∧ GenSectorAssignment Kernel.Generator.pi ≠ GenSectorAssignment Kernel.Generator.omega ∧ GenSectorAssignment Kernel.Generator.gamma ≠ GenSectorAssignment Kernel.Generator.eta ∧ GenSectorAssignment Kernel.Generator.gamma ≠ GenSectorAssignment Kernel.Generator.omega ∧ GenSectorAssignment Kernel.Generator.eta ≠ GenSectorAssignment Kernel.Generator.omega**


Φ maps each generator to a distinct sector (injective).

---

### `Tau.BookIV.Arena.assignment_surjective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L61-L69)
**theorem
Tau.BookIV.Arena.assignment_surjective
(s : BookIII.Sectors.Sector)
 :∃ (g : Kernel.Generator), GenSectorAssignment g = s**


Φ hits all 5 sectors (surjective).

---

### `Tau.BookIV.Arena.CoherenceKernel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L75-L87)
**structure
Tau.BookIV.Arena.CoherenceKernel :Type**


[IV.D246] The coherence kernel K: the categorical core generating
all physics. At E₁, K = {α,π,γ,η,ω} with canonical sector assignment
and polarity signatures. Minimal generating set for the coupling ledger.

- gen_count : ℕ
Number of generators.

- gen_count_eq : self.gen_count = 5
- sector_count : ℕ
Number of sectors covered (= gen_count for bijective assignment).

- sector_count_eq : self.sector_count = 5
- bijective : self.gen_count = self.sector_count
Bijective (gen_count = sector_count).

Instances For

---

### `Tau.BookIV.Arena.instReprCoherenceKernel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L87-L87)
**def
Tau.BookIV.Arena.instReprCoherenceKernel.repr :CoherenceKernel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprCoherenceKernel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L87-L87)
**instance
Tau.BookIV.Arena.instReprCoherenceKernel :Repr CoherenceKernel**

Equations
- Tau.BookIV.Arena.instReprCoherenceKernel = { reprPrec := Tau.BookIV.Arena.instReprCoherenceKernel.repr }

---

### `Tau.BookIV.Arena.canonical_kernel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L89-L95)
**def
Tau.BookIV.Arena.canonical_kernel :CoherenceKernel**


The canonical coherence kernel at E₁.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.gen_polarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L101-L103)
**def
Tau.BookIV.Arena.gen_polarity
(g : Kernel.Generator)
 :Sectors.PolaritySign**


Polarity of a generator in the canonical assignment.
Equations
- Tau.BookIV.Arena.gen_polarity g = (Tau.BookIV.Sectors.sector_physics (Tau.BookIV.Arena.GenSectorAssignment g)).polarity
Instances For

---

### `Tau.BookIV.Arena.gen_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L105-L107)
**def
Tau.BookIV.Arena.gen_depth
(g : Kernel.Generator)
 :ℕ**


Depth of a generator in the canonical assignment.
Equations
- Tau.BookIV.Arena.gen_depth g = (Tau.BookIV.Sectors.sector_physics (Tau.BookIV.Arena.GenSectorAssignment g)).depth
Instances For

---

### `Tau.BookIV.Arena.assignment_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L124-L136)
**theorem
Tau.BookIV.Arena.assignment_unique
(Psi : Kernel.Generator → BookIII.Sectors.Sector)

(h_pol : ∀ (g : Kernel.Generator), (Sectors.sector_physics (Psi g)).polarity = gen_polarity g)

(h_dep : ∀ (g : Kernel.Generator), (Sectors.sector_physics (Psi g)).depth = gen_depth g)

(g : Kernel.Generator)
 :Psi g = GenSectorAssignment g**


[IV.P146] Uniqueness of generator–sector assignment:
any assignment Ψ agreeing on polarity and depth must equal Φ.
Proved by exhaustive case analysis on generator × sector.

---

### `Tau.BookIV.Arena.all_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L142-L143)
**def
Tau.BookIV.Arena.all_generators :List Kernel.Generator**


All 5 generators as a list.
Equations
- Tau.BookIV.Arena.all_generators = [Tau.Kernel.Generator.alpha, Tau.Kernel.Generator.pi, Tau.Kernel.Generator.gamma, Tau.Kernel.Generator.eta, Tau.Kernel.Generator.omega]
Instances For

---

### `Tau.BookIV.Arena.covered_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L145-L147)
**def
Tau.BookIV.Arena.covered_sectors
(gens : List Kernel.Generator)
 :List BookIII.Sectors.Sector**


Sectors covered by a list of generators.
Equations
- Tau.BookIV.Arena.covered_sectors gens = List.map Tau.BookIV.Arena.GenSectorAssignment gens
Instances For

---

### `Tau.BookIV.Arena.ontic_minimality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L149-L167)
**theorem
Tau.BookIV.Arena.ontic_minimality :GenSectorAssignment Kernel.Generator.alpha = BookIII.Sectors.Sector.D ∧ GenSectorAssignment Kernel.Generator.pi ≠ BookIII.Sectors.Sector.D ∧ GenSectorAssignment Kernel.Generator.gamma ≠ BookIII.Sectors.Sector.D ∧ GenSectorAssignment Kernel.Generator.eta ≠ BookIII.Sectors.Sector.D ∧ GenSectorAssignment Kernel.Generator.omega ≠ BookIII.Sectors.Sector.D ∧ GenSectorAssignment Kernel.Generator.pi = BookIII.Sectors.Sector.A ∧ GenSectorAssignment Kernel.Generator.alpha ≠ BookIII.Sectors.Sector.A ∧ GenSectorAssignment Kernel.Generator.gamma ≠ BookIII.Sectors.Sector.A ∧ GenSectorAssignment Kernel.Generator.eta ≠ BookIII.Sectors.Sector.A ∧ GenSectorAssignment Kernel.Generator.omega ≠ BookIII.Sectors.Sector.A ∧ GenSectorAssignment Kernel.Generator.gamma = BookIII.Sectors.Sector.B ∧ GenSectorAssignment Kernel.Generator.alpha ≠ BookIII.Sectors.Sector.B ∧ GenSectorAssignment Kernel.Generator.pi ≠ BookIII.Sectors.Sector.B ∧ GenSectorAssignment Kernel.Generator.eta ≠ BookIII.Sectors.Sector.B ∧ GenSectorAssignment Kernel.Generator.omega ≠ BookIII.Sectors.Sector.B ∧ GenSectorAssignment Kernel.Generator.eta = BookIII.Sectors.Sector.C ∧ GenSectorAssignment Kernel.Generator.alpha ≠ BookIII.Sectors.Sector.C ∧ GenSectorAssignment Kernel.Generator.pi ≠ BookIII.Sectors.Sector.C ∧ GenSectorAssignment Kernel.Generator.gamma ≠ BookIII.Sectors.Sector.C ∧ GenSectorAssignment Kernel.Generator.omega ≠ BookIII.Sectors.Sector.C ∧ GenSectorAssignment Kernel.Generator.omega = BookIII.Sectors.Sector.Omega ∧ GenSectorAssignment Kernel.Generator.alpha ≠ BookIII.Sectors.Sector.Omega ∧ GenSectorAssignment Kernel.Generator.pi ≠ BookIII.Sectors.Sector.Omega ∧ GenSectorAssignment Kernel.Generator.gamma ≠ BookIII.Sectors.Sector.Omega ∧ GenSectorAssignment Kernel.Generator.eta ≠ BookIII.Sectors.Sector.Omega**


[IV.D248] Ontic minimality: each generator is the unique preimage
of its sector under Φ, so removing any one loses a sector.

---

### `Tau.BookIV.Arena.kernel_generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L169-L169)
**theorem
Tau.BookIV.Arena.kernel_generator_count :all_generators.length = 5**


---

### `Tau.BookIV.Arena.assignment_agrees_with_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/CoherenceKernel.lean#L175-L182)
**theorem
Tau.BookIV.Arena.assignment_agrees_with_params :Sectors.gravity_sector.generator = Kernel.Generator.alpha ∧ Sectors.weak_sector.generator = Kernel.Generator.pi ∧ Sectors.em_sector.generator = Kernel.Generator.gamma ∧ Sectors.strong_sector.generator = Kernel.Generator.eta ∧ Sectors.higgs_sector.generator = Kernel.Generator.omega**


Assignment agrees with sector parameter generator fields.
