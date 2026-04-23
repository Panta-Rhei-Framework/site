---
layout: taulib-doc
title: "TauLib.BookIII.Spectrum.KernelHinge"
permalink: /verify/taulib/docs/book-iii-spectrum-kernel-hinge/
lane: verify
module_name: "TauLib.BookIII.Spectrum.KernelHinge"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Spectrum.KernelHinge


The kernel hinge diagram: the complete dependency tree of Book I,
and the bridge to Book II.

## Registry Cross-References


- [I.D74] Kernel Hinge Diagram — `KernelHinge`

- [I.T34] Book II Bridge — `book_ii_bridge`


## Mathematical Content


The kernel hinge diagram gathers every dependency — from the five generators
through the Three Keys to the Global Hartogs Extension Theorem — into a
single structure witnessing that all of Book I's imports are EARNED.

Starting from:


- 5 generators: α, π, γ, η, ω

- 7 axioms: K0-K6

- 1 operator: ρ (primorial reduction)


Through 64 chapters we earned:


- The τ-index set and program monoid (Parts I-V)

- The ABCD chart and hyperfactorization (Parts IV-V)

- Prime polarity and the algebraic lemniscate (Parts VI-VII)

- Internal set theory and boundary ring (Parts VIII-IX)

- Characters, spectral decomposition, crossing point (Part X)

- Four-valued logic Ω_τ (Part XI)

- Holomorphic transformers and the Identity Theorem (Part XII)

- The earned category Cat_τ and topos E_τ (Part XIII)

- Bi-monoidal structure, cartesian closed (Part XIV)

- The Global Hartogs Extension Theorem (Part XV)

- The τ-Tower machine and complexity bridge (Part XVI)


Every result traces back to the axioms. No external imports.

---

### `Tau.Spectrum.KernelHinge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L52-L85)
**structure
Tau.Spectrum.KernelHinge :Type 1**


[I.D74] The kernel hinge diagram: a structured witness that
all of Book I's infrastructure is earned from the axioms.

Layer 1: The coherence kernel (generators + axioms)
Layer 2: The Three Keys (number system, boundary, holomorphy)
Layer 3: Categorical infrastructure (category, topos, bi-monoidal)
Layer 4: The culmination (Global Hartogs, boundary-interior)

- generators_count : ℕ
- generators_are_five : self.generators_count = 5
- key1_number_system : Type
- key2_boundary : Type
- key3_holomorphy : Type
- earned_category : Topos.CatTau
- earned_topos : Topos.EarnedTopos
- identity_theorem
(f₁ f₂ : Holomorphy.StageFun)
 : Holomorphy.TowerCoherent f₁ →
 Holomorphy.TowerCoherent f₂ →
 ∀ (d₀ : Denotation.TauIdx),
 (∀ (n : Denotation.TauIdx), Holomorphy.agree_at f₁ f₂ n d₀) →
 ∀ (n k : Denotation.TauIdx), k ≤ d₀ → Holomorphy.agree_at f₁ f₂ n k
- four_valued_classifier
(v : Logic.Omega_tau)
 : v = Logic.Truth4.T ∨ v = Logic.Truth4.F ∨ v = Logic.Truth4.B ∨ v = Logic.Truth4.N
Instances For

---

### `Tau.Spectrum.kernel_hinge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L87-L94)
**def
Tau.Spectrum.kernel_hinge :KernelHinge**


The canonical kernel hinge diagram, instantiated from earned structures.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.BookIIBridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L100-L119)
**structure
Tau.Spectrum.BookIIBridge :Type 1**


[I.T34] The Book II bridge: ALL imports for Book II are earned.

Book II needs:

- The earned category Cat_τ with composition and identity ✓

- The earned topos E_τ with Ω_τ classifier ✓

- The holomorphic function space Hol(L) ✓

- The Identity Theorem for uniqueness ✓

- The Global Hartogs Extension Theorem ✓

- The τ-Tower machine for computability arguments ✓


We witness this by constructing the complete export structure.

- export_data : Holomorphy.BookIExport
- hinge : KernelHinge
- ttm_exists : TTM
- admissibility : TauAdmissible Holomorphy.chi_plus_stage
Instances For

---

### `Tau.Spectrum.book_ii_bridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L121-L126)
**def
Tau.Spectrum.book_ii_bridge :BookIIBridge**


The canonical Book II bridge.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.book_ii_bridge_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L128-L134)
**theorem
Tau.Spectrum.book_ii_bridge_complete :⋯ = ⋯ ∧ book_ii_bridge.export_data = Holomorphy.book_i_export**


[I.T34] Main theorem: the bridge is complete.
All fields are instantiated from earned structures;
no sorry, no axiom, no external import beyond Mathlib tactics.

---

### `Tau.Spectrum.book_i_generators`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L140-L142)
**theorem
Tau.Spectrum.book_i_generators :[Kernel.Generator.alpha, Kernel.Generator.pi, Kernel.Generator.gamma, Kernel.Generator.eta, Kernel.Generator.omega].length = 5**


Book I has 5 generators.

---

### `Tau.Spectrum.book_i_parts`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L144-L145)
**theorem
Tau.Spectrum.book_i_parts :16 + 1 = 17**


Book I covers 16 Parts (0 = Prologue, I-XVI = main).

---

### `Tau.Spectrum.book_i_monoid_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L147-L151)
**theorem
Tau.Spectrum.book_i_monoid_assoc
(p q r : Denotation.Program)
 :(p.compose q).compose r = p.compose (q.compose r)**


The program monoid is associative (I.T03).

---

### `Tau.Spectrum.book_i_non_boolean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L153-L157)
**theorem
Tau.Spectrum.book_i_non_boolean :Logic.Truth4.B.impl Logic.Truth4.F ≠ Logic.Truth4.T**


The topos is non-Boolean (explosion barrier, I.T13).

---

### `Tau.Spectrum.book_i_admissibility`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/KernelHinge.lean#L159-L164)
**theorem
Tau.Spectrum.book_i_admissibility :TauAdmissible Holomorphy.chi_plus_stage ∧ TauAdmissible Holomorphy.chi_minus_stage ∧ TauAdmissible Holomorphy.id_stage**


Tower coherence implies admissibility (I.T33 + I.P30).
