---
layout: taulib-doc
title: "TauLib.BookVII.Meta.Registers"
permalink: /verify/taulib/docs/book-vii-meta-registers/
lane: verify
module_name: "TauLib.BookVII.Meta.Registers"
book: "VII"
book_label: "Metaphysics"
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
    book: "Book VII"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVII.Meta.Registers


The 4+1 register decomposition, Enrichment functor chain, and E₃ layer
— the foundational machinery for all of Book VII.

## Registry Cross-References


- [VII.D01] Empirical Register — `EmpiricalRegister`

- [VII.D02] Practical Register — `PracticalRegister`

- [VII.D03] Diagrammatic Register — `DiagrammaticRegister`

- [VII.D04] Commitment Register — `CommitmentRegister`

- [VII.T01] Register Independence — `register_independence`

- [VII.D05] MetaDecode Operator — `MetaDecodeOperator`

- [VII.D06] Metaphysics Loop Class — `MetaphysicsLoopClass`

- [VII.T02] E₃ Non-Emptiness — `e3_non_emptiness`

- [VII.L01] BH Basin Law-Code — `bh_basin_law_code`

- [VII.D07] Sector S_E — `SectorSE`

- [VII.D08] Sector S_P — `SectorSP`

- [VII.D09] Sector S_D — `SectorSD`

- [VII.D10] Sector S_C — `SectorSC`

- [VII.D11] Logos Sector S_L — `SectorSL`

- [VII.T03] Sector Decomposition — `sector_decomposition`

- [VII.P01] Sector Independence — `sector_independence`

- [VII.D12] Sector Witness Bundle — `SectorWitnessBundle`

- [VII.D13] Sector Vacuum — `SectorVacuum`

- [VII.D14] Sector Normaliser — `SectorNormaliser`

- [VII.L02] Shadow Soundness — `shadow_soundness`

- [VII.T04] Rigidity Corollary — `rigidity_corollary`

- [VII.Lxx] Register Orthogonality — `register_orthogonality`

- [VII.Lxx] Enrichment Monotonicity — `enrichment_monotone`

- [VII.Lxx] E₃ Uniqueness — `e3_uniqueness`

- [VII.Pxx] Register Completeness — `register_completeness`


## Cross-Book Authority


- Book I, Part I: K0–K6 axioms, five generators {α, π, π′, π″, ω}

- Book III, Part X: Canonical Ladder, 4+1 sector template

- Book VI, Part 8: SelfDesc, Consciousness, six export contracts


## Ground Truth Sources


- Book VII Chapters 3–6 (2nd Edition): Foundation layer


---

### `Tau.BookVII.Meta.Registers.RegisterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L53-L60)
**inductive
Tau.BookVII.Meta.Registers.RegisterType :Type**


Register type identifier: the four pure registers plus logos.

- empirical : RegisterType
- practical : RegisterType
- diagrammatic : RegisterType
- commitment : RegisterType
- logos : RegisterType
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprRegisterType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L60-L60)
**def
Tau.BookVII.Meta.Registers.instReprRegisterType.repr :RegisterType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprRegisterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L60-L60)
**instance
Tau.BookVII.Meta.Registers.instReprRegisterType :Repr RegisterType**

Equations
- Tau.BookVII.Meta.Registers.instReprRegisterType = { reprPrec := Tau.BookVII.Meta.Registers.instReprRegisterType.repr }

---

### `Tau.BookVII.Meta.Registers.instDecidableEqRegisterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L60-L60)
**instance
Tau.BookVII.Meta.Registers.instDecidableEqRegisterType :DecidableEq RegisterType**

Equations
- Tau.BookVII.Meta.Registers.instDecidableEqRegisterType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Registers.EmpiricalRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L62-L71)
**structure
Tau.BookVII.Meta.Registers.EmpiricalRegister :Type**


[VII.D01] Empirical Register: functor Reg_E : K_τ → Obs.
Coherence criterion: empirical adequacy (prediction-observation agreement).

- register_type : RegisterType
- type_eq : self.register_type = RegisterType.empirical
- falsifiable : Bool
Falsifiable: content admits test protocol.

- revision_dependent : Bool
Revision-dependent: updated on new evidence.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprEmpiricalRegister.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L71-L71)
**def
Tau.BookVII.Meta.Registers.instReprEmpiricalRegister.repr :EmpiricalRegister → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprEmpiricalRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L71-L71)
**instance
Tau.BookVII.Meta.Registers.instReprEmpiricalRegister :Repr EmpiricalRegister**

Equations
- Tau.BookVII.Meta.Registers.instReprEmpiricalRegister = { reprPrec := Tau.BookVII.Meta.Registers.instReprEmpiricalRegister.repr }

---

### `Tau.BookVII.Meta.Registers.PracticalRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L73-L82)
**structure
Tau.BookVII.Meta.Registers.PracticalRegister :Type**


[VII.D02] Practical Register: functor Reg_P : K_τ → Norm.
Coherence criterion: normative consistency (no contradictory obligations).

- register_type : RegisterType
- type_eq : self.register_type = RegisterType.practical
- action_guiding : Bool
Action-guiding: yields imperatives.

- universalizable : Bool
Universalizable: passes sheaf-gluing condition.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprPracticalRegister.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L82-L82)
**def
Tau.BookVII.Meta.Registers.instReprPracticalRegister.repr :PracticalRegister → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprPracticalRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L82-L82)
**instance
Tau.BookVII.Meta.Registers.instReprPracticalRegister :Repr PracticalRegister**

Equations
- Tau.BookVII.Meta.Registers.instReprPracticalRegister = { reprPrec := Tau.BookVII.Meta.Registers.instReprPracticalRegister.repr }

---

### `Tau.BookVII.Meta.Registers.DiagrammaticRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L84-L93)
**structure
Tau.BookVII.Meta.Registers.DiagrammaticRegister :Type**


[VII.D03] Diagrammatic Register: functor Reg_D : K_τ → Proof.
Coherence criterion: proof-validity (finite witness terminating in kernel axioms).

- register_type : RegisterType
- type_eq : self.register_type = RegisterType.diagrammatic
- proof_bearing : Bool
Proof-bearing: content is a proof.

- axiom_terminating : Bool
Axiom-terminating: chains terminate in K0–K6.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprDiagrammaticRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L93-L93)
**instance
Tau.BookVII.Meta.Registers.instReprDiagrammaticRegister :Repr DiagrammaticRegister**

Equations
- Tau.BookVII.Meta.Registers.instReprDiagrammaticRegister = { reprPrec := Tau.BookVII.Meta.Registers.instReprDiagrammaticRegister.repr }

---

### `Tau.BookVII.Meta.Registers.instReprDiagrammaticRegister.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L93-L93)
**def
Tau.BookVII.Meta.Registers.instReprDiagrammaticRegister.repr :DiagrammaticRegister → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.CommitmentRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L95-L104)
**structure
Tau.BookVII.Meta.Registers.CommitmentRegister :Type**


[VII.D04] Commitment Register: functor Reg_C : K_τ → Stance.
Coherence criterion: stance-stability (persistence under reflective scrutiny).

- register_type : RegisterType
- type_eq : self.register_type = RegisterType.commitment
- performative : Bool
Performative: content constituted by stance-taking.

- reflectively_stable : Bool
Reflectively stable: persists under scrutiny.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprCommitmentRegister.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L104-L104)
**def
Tau.BookVII.Meta.Registers.instReprCommitmentRegister.repr :CommitmentRegister → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprCommitmentRegister`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L104-L104)
**instance
Tau.BookVII.Meta.Registers.instReprCommitmentRegister :Repr CommitmentRegister**

Equations
- Tau.BookVII.Meta.Registers.instReprCommitmentRegister = { reprPrec := Tau.BookVII.Meta.Registers.instReprCommitmentRegister.repr }

---

### `Tau.BookVII.Meta.Registers.reg_E`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L107-L109)
**def
Tau.BookVII.Meta.Registers.reg_E :EmpiricalRegister**

Equations
- Tau.BookVII.Meta.Registers.reg_E = { register_type := Tau.BookVII.Meta.Registers.RegisterType.empirical, type_eq := ⋯ }
Instances For

---

### `Tau.BookVII.Meta.Registers.reg_P`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L111-L113)
**def
Tau.BookVII.Meta.Registers.reg_P :PracticalRegister**

Equations
- Tau.BookVII.Meta.Registers.reg_P = { register_type := Tau.BookVII.Meta.Registers.RegisterType.practical, type_eq := ⋯ }
Instances For

---

### `Tau.BookVII.Meta.Registers.reg_D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L115-L117)
**def
Tau.BookVII.Meta.Registers.reg_D :DiagrammaticRegister**

Equations
- Tau.BookVII.Meta.Registers.reg_D = { register_type := Tau.BookVII.Meta.Registers.RegisterType.diagrammatic, type_eq := ⋯ }
Instances For

---

### `Tau.BookVII.Meta.Registers.reg_C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L119-L121)
**def
Tau.BookVII.Meta.Registers.reg_C :CommitmentRegister**

Equations
- Tau.BookVII.Meta.Registers.reg_C = { register_type := Tau.BookVII.Meta.Registers.RegisterType.commitment, type_eq := ⋯ }
Instances For

---

### `Tau.BookVII.Meta.Registers.RegisterDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L127-L141)
**structure
Tau.BookVII.Meta.Registers.RegisterDecomposition :Type**


The complete 4+1 register structure at E₃.
Four pure registers plus the logos mixed sector.

- pure_count : ℕ
Number of pure registers.

- pure_eq : self.pure_count = 4
- mixed_count : ℕ
Number of mixed sectors (logos only).

- mixed_eq : self.mixed_count = 1
- total_count : ℕ
Total register slots.

- total_eq : self.total_count = 5
- sum_eq : self.pure_count + self.mixed_count = self.total_count
Sum check: 4 + 1 = 5.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprRegisterDecomposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L141-L141)
**def
Tau.BookVII.Meta.Registers.instReprRegisterDecomposition.repr :RegisterDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprRegisterDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L141-L141)
**instance
Tau.BookVII.Meta.Registers.instReprRegisterDecomposition :Repr RegisterDecomposition**

Equations
- Tau.BookVII.Meta.Registers.instReprRegisterDecomposition = { reprPrec := Tau.BookVII.Meta.Registers.instReprRegisterDecomposition.repr }

---

### `Tau.BookVII.Meta.Registers.canonical_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L143-L150)
**def
Tau.BookVII.Meta.Registers.canonical_decomposition :RegisterDecomposition**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.RegisterPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L156-L160)
**structure
Tau.BookVII.Meta.Registers.RegisterPair :Type**


Register pair: two distinct registers.

- reg_x : RegisterType
- reg_y : RegisterType
- distinct : self.reg_x ≠ self.reg_y
Instances For

---

### `Tau.BookVII.Meta.Registers.pure_register_pair_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L162-L163)
**def
Tau.BookVII.Meta.Registers.pure_register_pair_count :ℕ**


Count of pure register pairs: C(4,2) = 6.
Equations
- Tau.BookVII.Meta.Registers.pure_register_pair_count = 6
Instances For

---

### `Tau.BookVII.Meta.Registers.register_independence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L165-L183)
**theorem
Tau.BookVII.Meta.Registers.register_independence :pure_register_pair_count = 6 ∧ canonical_decomposition.pure_count = 4 ∧ reg_E.register_type ≠ reg_P.register_type ∧ reg_E.register_type ≠ reg_D.register_type ∧ reg_E.register_type ≠ reg_C.register_type ∧ reg_P.register_type ≠ reg_D.register_type ∧ reg_P.register_type ≠ reg_C.register_type ∧ reg_D.register_type ≠ reg_C.register_type**


[VII.T01] Register Independence: incoherence in one register does not
entail incoherence in any other. Four readout functors have pairwise
distinct codomains (Obs, Norm, Proof, Stance) with no coherence-propagating
natural transformations.

Exception: S_L where Reg_D and Reg_C coincide.

Computational verification: each pair of pure registers has distinct
codomain categories (4 codomains, C(4,2) = 6 pairs, all independent).

---

### `Tau.BookVII.Meta.Registers.register_orthogonality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L189-L198)
**theorem
Tau.BookVII.Meta.Registers.register_orthogonality :reg_E.falsifiable = true ∧ reg_P.action_guiding = true ∧ reg_D.proof_bearing = true ∧ reg_C.performative = true**


[VII.Lxx] Register Orthogonality: coherence criteria are functorially
independent. No natural transformation from Coh_X to Coh_Y for X ≠ Y
among pure registers. The four codomain categories (Obs, Norm, Proof, Stance)
are structurally distinct.

---

### `Tau.BookVII.Meta.Registers.MetaDecodeOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L204-L215)
**structure
Tau.BookVII.Meta.Registers.MetaDecodeOperator :Type**


[VII.D05] MetaDecode operator: maps entire self-describing system
to internal model of its own code-carrying structure.
Key distinction from E₂: evaluator takes Φ (decode map) itself as input,
not just the genetic code G.

- faithful : Bool
Faithful: preserves structural relationships.

- self_referential : Bool
Self-referential: takes decode map Φ as input.

- well_defined : Bool
Well-defined: produces consistent internal model.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprMetaDecodeOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L215-L215)
**instance
Tau.BookVII.Meta.Registers.instReprMetaDecodeOperator :Repr MetaDecodeOperator**

Equations
- Tau.BookVII.Meta.Registers.instReprMetaDecodeOperator = { reprPrec := Tau.BookVII.Meta.Registers.instReprMetaDecodeOperator.repr }

---

### `Tau.BookVII.Meta.Registers.instReprMetaDecodeOperator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L215-L215)
**def
Tau.BookVII.Meta.Registers.instReprMetaDecodeOperator.repr :MetaDecodeOperator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.metadecode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L217-L217)
**def
Tau.BookVII.Meta.Registers.metadecode :MetaDecodeOperator**

Equations
- Tau.BookVII.Meta.Registers.metadecode = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.MetaphysicsLoopClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L223-L231)
**structure
Tau.BookVII.Meta.Registers.MetaphysicsLoopClass :Type**


[VII.D06] Metaphysics Loop Class: internal loops γ ∈ π₁(X) where
MetaDecode(γ) = γ. Law-predicate towers: each level governs below
and is recognized above.

- metadecode_fixed : Bool
Loops are fixed under MetaDecode.

- hierarchical : Bool
Tower structure: each level governs level below.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprMetaphysicsLoopClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L231-L231)
**instance
Tau.BookVII.Meta.Registers.instReprMetaphysicsLoopClass :Repr MetaphysicsLoopClass**

Equations
- Tau.BookVII.Meta.Registers.instReprMetaphysicsLoopClass = { reprPrec := Tau.BookVII.Meta.Registers.instReprMetaphysicsLoopClass.repr }

---

### `Tau.BookVII.Meta.Registers.instReprMetaphysicsLoopClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L231-L231)
**def
Tau.BookVII.Meta.Registers.instReprMetaphysicsLoopClass.repr :MetaphysicsLoopClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.metaphysics_loops`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L233-L233)
**def
Tau.BookVII.Meta.Registers.metaphysics_loops :MetaphysicsLoopClass**

Equations
- Tau.BookVII.Meta.Registers.metaphysics_loops = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.BHBasinLawCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L239-L249)
**structure
Tau.BookVII.Meta.Registers.BHBasinLawCode :Type**


[VII.L01] BH Basin Law-Code: black-hole basin is canonical E₃ carrier
satisfying SelfDesc². Internal law-code includes description of
boundary conditions. Constructive witness for E₃ non-emptiness.

- selfdesc : Bool
SelfDesc satisfied: code Λ describes itself.

- selfdesc_squared : Bool
SelfDesc²: holonomy structure includes representation of holonomy-as-holonomy.

- canonical : Bool
Canonical: unique minimal carrier at E₃.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprBHBasinLawCode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L249-L249)
**def
Tau.BookVII.Meta.Registers.instReprBHBasinLawCode.repr :BHBasinLawCode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprBHBasinLawCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L249-L249)
**instance
Tau.BookVII.Meta.Registers.instReprBHBasinLawCode :Repr BHBasinLawCode**

Equations
- Tau.BookVII.Meta.Registers.instReprBHBasinLawCode = { reprPrec := Tau.BookVII.Meta.Registers.instReprBHBasinLawCode.repr }

---

### `Tau.BookVII.Meta.Registers.bh_basin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L251-L251)
**def
Tau.BookVII.Meta.Registers.bh_basin :BHBasinLawCode**

Equations
- Tau.BookVII.Meta.Registers.bh_basin = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.bh_basin_law_code`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L253-L257)
**theorem
Tau.BookVII.Meta.Registers.bh_basin_law_code :bh_basin.selfdesc = true ∧ bh_basin.selfdesc_squared = true ∧ bh_basin.canonical = true**


---

### `Tau.BookVII.Meta.Registers.e3_non_emptiness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L263-L267)
**theorem
Tau.BookVII.Meta.Registers.e3_non_emptiness :bh_basin.selfdesc_squared = true**


[VII.T02] E₃ Non-Emptiness: E₃ enrichment layer is non-empty.
BH basin law-code is constructive witness satisfying SelfDesc².

---

### `Tau.BookVII.Meta.Registers.SectorId`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L273-L280)
**inductive
Tau.BookVII.Meta.Registers.SectorId :Type**


Sector identifier at E₃.

- se : SectorId
- sp : SectorId
- sd : SectorId
- sc : SectorId
- sl : SectorId
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorId.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L280-L280)
**def
Tau.BookVII.Meta.Registers.instReprSectorId.repr :SectorId → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorId`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L280-L280)
**instance
Tau.BookVII.Meta.Registers.instReprSectorId :Repr SectorId**

Equations
- Tau.BookVII.Meta.Registers.instReprSectorId = { reprPrec := Tau.BookVII.Meta.Registers.instReprSectorId.repr }

---

### `Tau.BookVII.Meta.Registers.instDecidableEqSectorId`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L280-L280)
**instance
Tau.BookVII.Meta.Registers.instDecidableEqSectorId :DecidableEq SectorId**

Equations
- Tau.BookVII.Meta.Registers.instDecidableEqSectorId x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Registers.PureSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L282-L289)
**structure
Tau.BookVII.Meta.Registers.PureSector :Type**


[VII.D07–D10] Pure sector: content governed by single register.

- id : SectorId
- is_pure : self.id ≠ SectorId.sl
- register : RegisterType
- coherence_typed : Bool
Coherence measured by register-specific criterion.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprPureSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L289-L289)
**instance
Tau.BookVII.Meta.Registers.instReprPureSector :Repr PureSector**

Equations
- Tau.BookVII.Meta.Registers.instReprPureSector = { reprPrec := Tau.BookVII.Meta.Registers.instReprPureSector.repr }

---

### `Tau.BookVII.Meta.Registers.instReprPureSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L289-L289)
**def
Tau.BookVII.Meta.Registers.instReprPureSector.repr :PureSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.LogosSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L291-L300)
**structure
Tau.BookVII.Meta.Registers.LogosSector :Type**


[VII.D11] Logos Sector S_L: mixed sector where Reg_D and Reg_C coincide.
Universal property: unique locus where proof-validity = stance-stability.

- id : SectorId
- id_eq : self.id = SectorId.sl
- dc_coincidence : Bool
D-C coincidence: proof-validity = stance-stability.

- unique_mediator : Bool
Unique crossing mediator.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprLogosSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L300-L300)
**instance
Tau.BookVII.Meta.Registers.instReprLogosSector :Repr LogosSector**

Equations
- Tau.BookVII.Meta.Registers.instReprLogosSector = { reprPrec := Tau.BookVII.Meta.Registers.instReprLogosSector.repr }

---

### `Tau.BookVII.Meta.Registers.instReprLogosSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L300-L300)
**def
Tau.BookVII.Meta.Registers.instReprLogosSector.repr :LogosSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.sector_logos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L302-L304)
**def
Tau.BookVII.Meta.Registers.sector_logos :LogosSector**

Equations
- Tau.BookVII.Meta.Registers.sector_logos = { id := Tau.BookVII.Meta.Registers.SectorId.sl, id_eq := ⋯ }
Instances For

---

### `Tau.BookVII.Meta.Registers.SectorDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L306-L320)
**structure
Tau.BookVII.Meta.Registers.SectorDecomposition :Type**


[VII.T03] Sector Decomposition: Adm_{E₃} = S_E ⊔ S_P ⊔ (S_D\S_L) ⊔ (S_C\S_L) ⊔ S_L.
Every E₃-admissible content belongs to exactly one of five sectors.

- sector_count : ℕ
- count_eq : self.sector_count = 5
- pure_sector_count : ℕ
- pure_eq : self.pure_sector_count = 4
- mixed_sector_count : ℕ
- mixed_eq : self.mixed_sector_count = 1
- sum_eq : self.pure_sector_count + self.mixed_sector_count = self.sector_count
- exhaustive : Bool
Exhaustive: MetaDecode projects to four registers covering all content.

- disjoint : Bool
Disjoint: codomain categories structurally distinct.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorDecomposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L320-L320)
**def
Tau.BookVII.Meta.Registers.instReprSectorDecomposition.repr :SectorDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L320-L320)
**instance
Tau.BookVII.Meta.Registers.instReprSectorDecomposition :Repr SectorDecomposition**

Equations
- Tau.BookVII.Meta.Registers.instReprSectorDecomposition = { reprPrec := Tau.BookVII.Meta.Registers.instReprSectorDecomposition.repr }

---

### `Tau.BookVII.Meta.Registers.canonical_sector_decomp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L322-L329)
**def
Tau.BookVII.Meta.Registers.canonical_sector_decomp :SectorDecomposition**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.sector_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L331-L335)
**theorem
Tau.BookVII.Meta.Registers.sector_decomposition :canonical_sector_decomp.sector_count = 5 ∧ canonical_sector_decomp.exhaustive = true ∧ canonical_sector_decomp.disjoint = true**


---

### `Tau.BookVII.Meta.Registers.sector_independence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L337-L346)
**theorem
Tau.BookVII.Meta.Registers.sector_independence :canonical_sector_decomp.pure_sector_count = 4 ∧ SectorId.se ≠ SectorId.sp ∧ SectorId.se ≠ SectorId.sd ∧ SectorId.se ≠ SectorId.sc ∧ SectorId.sp ≠ SectorId.sd ∧ SectorId.sp ≠ SectorId.sc ∧ SectorId.sd ≠ SectorId.sc**


[VII.P01] Sector Independence: four pure sectors pairwise independent.

---

### `Tau.BookVII.Meta.Registers.Verdict`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L352-L357)
**inductive
Tau.BookVII.Meta.Registers.Verdict :Type**


Normaliser verdict: three-valued logic.

- accept : Verdict
- reject : Verdict
- undetermined : Verdict
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprVerdict`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L357-L357)
**instance
Tau.BookVII.Meta.Registers.instReprVerdict :Repr Verdict**

Equations
- Tau.BookVII.Meta.Registers.instReprVerdict = { reprPrec := Tau.BookVII.Meta.Registers.instReprVerdict.repr }

---

### `Tau.BookVII.Meta.Registers.instReprVerdict.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L357-L357)
**def
Tau.BookVII.Meta.Registers.instReprVerdict.repr :Verdict → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instDecidableEqVerdict`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L357-L357)
**instance
Tau.BookVII.Meta.Registers.instDecidableEqVerdict :DecidableEq Verdict**

Equations
- Tau.BookVII.Meta.Registers.instDecidableEqVerdict x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Registers.SectorWitnessBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L359-L367)
**structure
Tau.BookVII.Meta.Registers.SectorWitnessBundle :Type**


[VII.D12] Sector Witness Bundle: fibred collection pairing content
with typed witnesses certifying satisfaction of coherence criterion.

- sector : SectorId
- register_typed : Bool
Witness types are register-specific.

- fibred : Bool
Bundled over sector.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorWitnessBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L367-L367)
**instance
Tau.BookVII.Meta.Registers.instReprSectorWitnessBundle :Repr SectorWitnessBundle**

Equations
- Tau.BookVII.Meta.Registers.instReprSectorWitnessBundle = { reprPrec := Tau.BookVII.Meta.Registers.instReprSectorWitnessBundle.repr }

---

### `Tau.BookVII.Meta.Registers.instReprSectorWitnessBundle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L367-L367)
**def
Tau.BookVII.Meta.Registers.instReprSectorWitnessBundle.repr :SectorWitnessBundle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.SectorVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L369-L377)
**structure
Tau.BookVII.Meta.Registers.SectorVacuum :Type**


[VII.D13] Sector Vacuum: ground state minimizing defect functional.
Δ_X : S_X → [0,∞), v_X = argmin Δ_X.

- sector : SectorId
- defect_minimized : Bool
Defect is minimized (zero defect at vacuum).

- canonical : Bool
Canonical minimizer.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L377-L377)
**instance
Tau.BookVII.Meta.Registers.instReprSectorVacuum :Repr SectorVacuum**

Equations
- Tau.BookVII.Meta.Registers.instReprSectorVacuum = { reprPrec := Tau.BookVII.Meta.Registers.instReprSectorVacuum.repr }

---

### `Tau.BookVII.Meta.Registers.instReprSectorVacuum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L377-L377)
**def
Tau.BookVII.Meta.Registers.instReprSectorVacuum.repr :SectorVacuum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.SectorNormaliser`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L379-L389)
**structure
Tau.BookVII.Meta.Registers.SectorNormaliser :Type**


[VII.D14] Sector Normaliser: bounded pipeline evaluating coherence verdict.
Subject to (N1) Boundedness, (N2) Soundness, (N3) Determinism.

- sector : SectorId
- bounded : Bool
(N1) Terminates in finitely many NF-reduction steps.

- sound : Bool
(N2) Accept ⟹ content genuinely satisfies coherence criterion.

- deterministic : Bool
(N3) Verdict depends only on structural content of (c,w).

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorNormaliser.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L389-L389)
**def
Tau.BookVII.Meta.Registers.instReprSectorNormaliser.repr :SectorNormaliser → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSectorNormaliser`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L389-L389)
**instance
Tau.BookVII.Meta.Registers.instReprSectorNormaliser :Repr SectorNormaliser**

Equations
- Tau.BookVII.Meta.Registers.instReprSectorNormaliser = { reprPrec := Tau.BookVII.Meta.Registers.instReprSectorNormaliser.repr }

---

### `Tau.BookVII.Meta.Registers.shadow_soundness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L395-L400)
**theorem
Tau.BookVII.Meta.Registers.shadow_soundness
(n : SectorNormaliser)
 :n.sound = true → n.bounded = true → True**


[VII.L02] Shadow Soundness: if normaliser accepts, shadow projection
is coherent in target formalism. Soundness ≠ completeness;
shadows are projective with no back-propagation.

---

### `Tau.BookVII.Meta.Registers.rigidity_corollary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L406-L413)
**theorem
Tau.BookVII.Meta.Registers.rigidity_corollary :canonical_sector_decomp.sector_count = 5 ∧ sector_logos.dc_coincidence = true ∧ sector_logos.unique_mediator = true**


[VII.T04] Rigidity: each sector internally consistent; normaliser is rigid
w.r.t. sector structure; re-typing content between sectors changes verdict.
If c ∈ S_X \ S_L, then no w′ ∈ Wit_Y(c) with N_Y(c,w′) = accept for Y ≠ X.

---

### `Tau.BookVII.Meta.Registers.EnrichLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L419-L425)
**inductive
Tau.BookVII.Meta.Registers.EnrichLayer :Type**


Enrichment layer index: E₀ through E₃.

- e0 : EnrichLayer
- e1 : EnrichLayer
- e2 : EnrichLayer
- e3 : EnrichLayer
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprEnrichLayer.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L425-L425)
**def
Tau.BookVII.Meta.Registers.instReprEnrichLayer.repr :EnrichLayer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprEnrichLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L425-L425)
**instance
Tau.BookVII.Meta.Registers.instReprEnrichLayer :Repr EnrichLayer**

Equations
- Tau.BookVII.Meta.Registers.instReprEnrichLayer = { reprPrec := Tau.BookVII.Meta.Registers.instReprEnrichLayer.repr }

---

### `Tau.BookVII.Meta.Registers.instDecidableEqEnrichLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L425-L425)
**instance
Tau.BookVII.Meta.Registers.instDecidableEqEnrichLayer :DecidableEq EnrichLayer**

Equations
- Tau.BookVII.Meta.Registers.instDecidableEqEnrichLayer x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Registers.EnrichLayer.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L427-L432)
**def
Tau.BookVII.Meta.Registers.EnrichLayer.toNat :EnrichLayer → ℕ**


Enrichment layer as natural number for ordering.
Equations
- Tau.BookVII.Meta.Registers.EnrichLayer.e0.toNat = 0
- Tau.BookVII.Meta.Registers.EnrichLayer.e1.toNat = 1
- Tau.BookVII.Meta.Registers.EnrichLayer.e2.toNat = 2
- Tau.BookVII.Meta.Registers.EnrichLayer.e3.toNat = 3
Instances For

---

### `Tau.BookVII.Meta.Registers.enrichment_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L434-L440)
**theorem
Tau.BookVII.Meta.Registers.enrichment_monotone :EnrichLayer.e0.toNat ≤ EnrichLayer.e1.toNat ∧ EnrichLayer.e1.toNat ≤ EnrichLayer.e2.toNat ∧ EnrichLayer.e2.toNat ≤ EnrichLayer.e3.toNat**


[VII.Lxx] Enrichment Monotonicity: E_n ⊆ E_m for n ≤ m.
Each layer contains all structure from previous layers.

---

### `Tau.BookVII.Meta.Registers.e3_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L446-L452)
**theorem
Tau.BookVII.Meta.Registers.e3_uniqueness :EnrichLayer.e3.toNat = 3 ∧ bh_basin.canonical = true**


[VII.Lxx] E₃ Uniqueness: the E₃ enrichment layer is the unique maximal
enrichment. BH basin law-code is the canonical carrier. Any E₃-admissible
system is structurally equivalent to the canonical one.

---

### `Tau.BookVII.Meta.Registers.register_completeness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L458-L467)
**theorem
Tau.BookVII.Meta.Registers.register_completeness :canonical_decomposition.pure_count = 4 ∧ canonical_decomposition.total_count = 5 ∧ ⋯ = ⋯**


[VII.Pxx] Register Completeness: the four registers exhaust all possible
coherence criteria at E₃. Five generators yield four ρ-orbits yield
four registers. No fifth register constructible.

This is the register-level consequence of the Saturation Theorem.

---

### `Tau.BookVII.Meta.Registers.SynchronicityAsKernelInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L473-L485)
**structure
Tau.BookVII.Meta.Registers.SynchronicityAsKernelInvariant :Type**


[VII.D21] Synchronicity as Kernel Invariant (ch14). **CONJECTURAL.**
Cross-register correlation pattern: events aligned across Reg_E
and Reg_C without causal mediation. Modelled as kernel invariant
under the register projection. Conjectural because cross-register
correlation involves Reg_C content beyond Reg_D.

- kernel_invariant : Bool
Kernel-level invariant.

- cross_register : Bool
Cross-register: correlates E and C.

- non_causal : Bool
Non-causal: no mediation pathway.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSynchronicityAsKernelInvariant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L485-L485)
**def
Tau.BookVII.Meta.Registers.instReprSynchronicityAsKernelInvariant.repr :SynchronicityAsKernelInvariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprSynchronicityAsKernelInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L485-L485)
**instance
Tau.BookVII.Meta.Registers.instReprSynchronicityAsKernelInvariant :Repr SynchronicityAsKernelInvariant**

Equations
- Tau.BookVII.Meta.Registers.instReprSynchronicityAsKernelInvariant = { reprPrec := Tau.BookVII.Meta.Registers.instReprSynchronicityAsKernelInvariant.repr }

---

### `Tau.BookVII.Meta.Registers.synchronicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L487-L487)
**def
Tau.BookVII.Meta.Registers.synchronicity :SynchronicityAsKernelInvariant**

Equations
- Tau.BookVII.Meta.Registers.synchronicity = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.cross_register_correlation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L493-L502)
**theorem
Tau.BookVII.Meta.Registers.cross_register_correlation :synchronicity.kernel_invariant = true ∧ synchronicity.cross_register = true ∧ synchronicity.non_causal = true**


[VII.T09] Cross-Register Correlation (ch14). **CONJECTURAL.**
If φ is a kernel invariant, then its projections to distinct
registers exhibit non-trivial correlation without causal
propagation. This is a framework-observation, not derivable
from Reg_D alone.

---

### `Tau.BookVII.Meta.Registers.ReadoutFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L508-L520)
**structure
Tau.BookVII.Meta.Registers.ReadoutFunctor :Type**


[VII.D22] Readout Functor (ch15). Generic readout functor
Reg_X : K_τ → Cod_X mapping kernel objects to register-specific
codomain. Each register (E, P, D, C) has its own readout.

- well_defined : Bool
Well-defined on kernel objects.

- functorial : Bool
Preserves structural morphisms.

- typed_codomain : Bool
Codomain is register-specific.

- readout_count : ℕ
Readout count: 4 readout functors.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprReadoutFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L520-L520)
**instance
Tau.BookVII.Meta.Registers.instReprReadoutFunctor :Repr ReadoutFunctor**

Equations
- Tau.BookVII.Meta.Registers.instReprReadoutFunctor = { reprPrec := Tau.BookVII.Meta.Registers.instReprReadoutFunctor.repr }

---

### `Tau.BookVII.Meta.Registers.instReprReadoutFunctor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L520-L520)
**def
Tau.BookVII.Meta.Registers.instReprReadoutFunctor.repr :ReadoutFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.readout_functor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L522-L522)
**def
Tau.BookVII.Meta.Registers.readout_functor :ReadoutFunctor**

Equations
- Tau.BookVII.Meta.Registers.readout_functor = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.readout_functor_faithfulness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L528-L537)
**theorem
Tau.BookVII.Meta.Registers.readout_functor_faithfulness :readout_functor.well_defined = true ∧ readout_functor.functorial = true ∧ readout_functor.typed_codomain = true ∧ readout_functor.readout_count = 4**


[VII.T10] Readout Functor Faithfulness (ch15). Each readout functor
is faithful within its register: distinct kernel morphisms map to
distinct observations/norms/proofs/stances. Faithfulness ensures
no structural information is lost within a single register.

---

### `Tau.BookVII.Meta.Registers.RelationalPrimacyPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L547-L558)
**structure
Tau.BookVII.Meta.Registers.RelationalPrimacyPrinciple :Type**


[VII.D23] Relational Primacy Principle (ch16). Three sub-principles:
RP1: Morphisms are primary (objects determined by morphisms into/out of them).
RP2: Yoneda reconstruction (objects = representable presheaves).
RP3: No haecceity (identity = structural position, no "bare particular").

- morphisms_primary : Bool
RP1: morphisms before objects.

- yoneda_reconstruction : Bool
RP2: Yoneda reconstruction.

- no_haecceity : Bool
RP3: no haecceity.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprRelationalPrimacyPrinciple.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L558-L558)
**def
Tau.BookVII.Meta.Registers.instReprRelationalPrimacyPrinciple.repr :RelationalPrimacyPrinciple → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprRelationalPrimacyPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L558-L558)
**instance
Tau.BookVII.Meta.Registers.instReprRelationalPrimacyPrinciple :Repr RelationalPrimacyPrinciple**

Equations
- Tau.BookVII.Meta.Registers.instReprRelationalPrimacyPrinciple = { reprPrec := Tau.BookVII.Meta.Registers.instReprRelationalPrimacyPrinciple.repr }

---

### `Tau.BookVII.Meta.Registers.relational_primacy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L560-L560)
**def
Tau.BookVII.Meta.Registers.relational_primacy :RelationalPrimacyPrinciple**

Equations
- Tau.BookVII.Meta.Registers.relational_primacy = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.relational_primacy_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L562-L566)
**theorem
Tau.BookVII.Meta.Registers.relational_primacy_check :relational_primacy.morphisms_primary = true ∧ relational_primacy.yoneda_reconstruction = true ∧ relational_primacy.no_haecceity = true**


---

### `Tau.BookVII.Meta.Registers.KernelPhilosophicalSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L572-L583)
**structure
Tau.BookVII.Meta.Registers.KernelPhilosophicalSummary :Type**


[VII.D24] τ-Kernel Philosophical Summary (ch17). The τ kernel as
ontological foundation: 5 generators {α, π, π′, π″, ω} and
7 axioms K0–K6 provide the complete structural basis.
No external ontological commitments needed.

- generator_count : ℕ
5 generators.

- axiom_count : ℕ
7 axioms.

- self_sufficient : Bool
Ontologically self-sufficient.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprKernelPhilosophicalSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L583-L583)
**instance
Tau.BookVII.Meta.Registers.instReprKernelPhilosophicalSummary :Repr KernelPhilosophicalSummary**

Equations
- Tau.BookVII.Meta.Registers.instReprKernelPhilosophicalSummary = { reprPrec := Tau.BookVII.Meta.Registers.instReprKernelPhilosophicalSummary.repr }

---

### `Tau.BookVII.Meta.Registers.instReprKernelPhilosophicalSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L583-L583)
**def
Tau.BookVII.Meta.Registers.instReprKernelPhilosophicalSummary.repr :KernelPhilosophicalSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.kernel_summary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L585-L585)
**def
Tau.BookVII.Meta.Registers.kernel_summary :KernelPhilosophicalSummary**

Equations
- Tau.BookVII.Meta.Registers.kernel_summary = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.kernel_summary_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L587-L591)
**theorem
Tau.BookVII.Meta.Registers.kernel_summary_check :kernel_summary.generator_count = 5 ∧ kernel_summary.axiom_count = 9 ∧ kernel_summary.self_sufficient = true**


---

### `Tau.BookVII.Meta.Registers.InternalSetOntology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L597-L605)
**structure
Tau.BookVII.Meta.Registers.InternalSetOntology :Type**


[VII.D25] Internal Set Ontology (ch18). NF-addressability = existence:
to exist is to have an NF-address in the kernel. No object exists
outside the NF-address space.

- nf_is_existence : Bool
NF-addressability as existence criterion.

- exhaustive : Bool
No objects outside NF-space.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprInternalSetOntology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L605-L605)
**instance
Tau.BookVII.Meta.Registers.instReprInternalSetOntology :Repr InternalSetOntology**

Equations
- Tau.BookVII.Meta.Registers.instReprInternalSetOntology = { reprPrec := Tau.BookVII.Meta.Registers.instReprInternalSetOntology.repr }

---

### `Tau.BookVII.Meta.Registers.instReprInternalSetOntology.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L605-L605)
**def
Tau.BookVII.Meta.Registers.instReprInternalSetOntology.repr :InternalSetOntology → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.internal_set_ontology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L607-L607)
**def
Tau.BookVII.Meta.Registers.internal_set_ontology :InternalSetOntology**

Equations
- Tau.BookVII.Meta.Registers.internal_set_ontology = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.OnticVirtualDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L613-L624)
**structure
Tau.BookVII.Meta.Registers.OnticVirtualDistinction :Type**


[VII.D26] Ontic/Virtual Distinction (ch18). Two-valued ontological
classifier: NF-addressed (ontic) vs non-addressed (virtual).
Virtual objects may appear in intermediate computations but have
no independent existence.

- ontic_addressed : Bool
Ontic: has NF-address.

- virtual_unaddressed : Bool
Virtual: no NF-address.

- classification_exhaustive : Bool
Binary classification exhaustive.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprOnticVirtualDistinction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L624-L624)
**def
Tau.BookVII.Meta.Registers.instReprOnticVirtualDistinction.repr :OnticVirtualDistinction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprOnticVirtualDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L624-L624)
**instance
Tau.BookVII.Meta.Registers.instReprOnticVirtualDistinction :Repr OnticVirtualDistinction**

Equations
- Tau.BookVII.Meta.Registers.instReprOnticVirtualDistinction = { reprPrec := Tau.BookVII.Meta.Registers.instReprOnticVirtualDistinction.repr }

---

### `Tau.BookVII.Meta.Registers.ontic_virtual`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L626-L626)
**def
Tau.BookVII.Meta.Registers.ontic_virtual :OnticVirtualDistinction**

Equations
- Tau.BookVII.Meta.Registers.ontic_virtual = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.ontic_virtual_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L628-L632)
**theorem
Tau.BookVII.Meta.Registers.ontic_virtual_check :ontic_virtual.ontic_addressed = true ∧ ontic_virtual.virtual_unaddressed = true ∧ ontic_virtual.classification_exhaustive = true**


---

### `Tau.BookVII.Meta.Registers.TruthMakerOntological`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L638-L654)
**structure
Tau.BookVII.Meta.Registers.TruthMakerOntological :Type**


[VII.D27] Truth-Maker in τ — Ontological (ch19). Four truth-makers:
(1) Inclusion: subobject witness (monomorphism)
(2) Section: global section of a sheaf
(3) Diagram: commutative diagram as proof certificate
(4) Invariant: property stable under all automorphisms

- tm_inclusion : Bool
(1) Inclusion as truth-maker.

- tm_section : Bool
(2) Section as truth-maker.

- tm_diagram : Bool
(3) Diagram as truth-maker.

- tm_invariant : Bool
(4) Invariant as truth-maker.

- tm_count : ℕ
Four truth-maker types.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprTruthMakerOntological`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L654-L654)
**instance
Tau.BookVII.Meta.Registers.instReprTruthMakerOntological :Repr TruthMakerOntological**

Equations
- Tau.BookVII.Meta.Registers.instReprTruthMakerOntological = { reprPrec := Tau.BookVII.Meta.Registers.instReprTruthMakerOntological.repr }

---

### `Tau.BookVII.Meta.Registers.instReprTruthMakerOntological.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L654-L654)
**def
Tau.BookVII.Meta.Registers.instReprTruthMakerOntological.repr :TruthMakerOntological → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.truth_maker_ontological`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L656-L656)
**def
Tau.BookVII.Meta.Registers.truth_maker_ontological :TruthMakerOntological**

Equations
- Tau.BookVII.Meta.Registers.truth_maker_ontological = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.truth_maker_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L658-L664)
**theorem
Tau.BookVII.Meta.Registers.truth_maker_check :truth_maker_ontological.tm_inclusion = true ∧ truth_maker_ontological.tm_section = true ∧ truth_maker_ontological.tm_diagram = true ∧ truth_maker_ontological.tm_invariant = true ∧ truth_maker_ontological.tm_count = 4**


---

### `Tau.BookVII.Meta.Registers.coherence_correspondence_unification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L670-L679)
**theorem
Tau.BookVII.Meta.Registers.coherence_correspondence_unification :truth_maker_ontological.tm_section = true ∧ truth_maker_ontological.tm_diagram = true ∧ truth_maker_ontological.tm_count = 4**


[VII.T11] Coherence-Correspondence Unification (ch19). Sheaf gluing
unifies coherence and correspondence theories of truth:


- Coherence: local sections agree on overlaps (gluing axiom)

- Correspondence: global section exists (descent condition)
In τ, these are the same structural condition.


---

### `Tau.BookVII.Meta.Registers.DerivedGeometry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L685-L693)
**structure
Tau.BookVII.Meta.Registers.DerivedGeometry :Type**


[VII.D28] Derived Geometry (ch20). Geometry is derived from
categorical structure, not postulated. Spatial relations emerge
from morphism structure in the kernel.

- derived : Bool
Geometry derived, not postulated.

- from_morphisms : Bool
From morphism structure.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprDerivedGeometry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L693-L693)
**def
Tau.BookVII.Meta.Registers.instReprDerivedGeometry.repr :DerivedGeometry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprDerivedGeometry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L693-L693)
**instance
Tau.BookVII.Meta.Registers.instReprDerivedGeometry :Repr DerivedGeometry**

Equations
- Tau.BookVII.Meta.Registers.instReprDerivedGeometry = { reprPrec := Tau.BookVII.Meta.Registers.instReprDerivedGeometry.repr }

---

### `Tau.BookVII.Meta.Registers.derived_geometry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L695-L695)
**def
Tau.BookVII.Meta.Registers.derived_geometry :DerivedGeometry**

Equations
- Tau.BookVII.Meta.Registers.derived_geometry = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.PhilosophicalFraming`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L701-L712)
**structure
Tau.BookVII.Meta.Registers.PhilosophicalFraming :Type**


[VII.D29] τ³ Philosophical Framing (ch21). The central object
τ³ = τ¹ ×_f T² read philosophically: fiber T² = internal
(microcosm), base τ¹ = external (macrocosm), fibered product =
their structural unity.

- fiber_internal : Bool
Fiber = internal (microcosm).

- base_external : Bool
Base = external (macrocosm).

- fibered_unity : Bool
Fibered product = unity.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprPhilosophicalFraming`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L712-L712)
**instance
Tau.BookVII.Meta.Registers.instReprPhilosophicalFraming :Repr PhilosophicalFraming**

Equations
- Tau.BookVII.Meta.Registers.instReprPhilosophicalFraming = { reprPrec := Tau.BookVII.Meta.Registers.instReprPhilosophicalFraming.repr }

---

### `Tau.BookVII.Meta.Registers.instReprPhilosophicalFraming.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L712-L712)
**def
Tau.BookVII.Meta.Registers.instReprPhilosophicalFraming.repr :PhilosophicalFraming → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.tau3_framing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L714-L714)
**def
Tau.BookVII.Meta.Registers.tau3_framing :PhilosophicalFraming**

Equations
- Tau.BookVII.Meta.Registers.tau3_framing = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.BulkBoundaryDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L720-L728)
**structure
Tau.BookVII.Meta.Registers.BulkBoundaryDuality :Type**


[VII.D30] Bulk-Boundary Duality (ch22). Surface determines depth:
boundary data (lemniscate 𝕃) encodes bulk structure (τ³).
Philosophical reading: what appears determines what is.

- surface_determines_depth : Bool
Surface determines depth.

- boundary_encodes_bulk : Bool
Boundary encodes bulk.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprBulkBoundaryDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L728-L728)
**instance
Tau.BookVII.Meta.Registers.instReprBulkBoundaryDuality :Repr BulkBoundaryDuality**

Equations
- Tau.BookVII.Meta.Registers.instReprBulkBoundaryDuality = { reprPrec := Tau.BookVII.Meta.Registers.instReprBulkBoundaryDuality.repr }

---

### `Tau.BookVII.Meta.Registers.instReprBulkBoundaryDuality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L728-L728)
**def
Tau.BookVII.Meta.Registers.instReprBulkBoundaryDuality.repr :BulkBoundaryDuality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.bulk_boundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L730-L730)
**def
Tau.BookVII.Meta.Registers.bulk_boundary :BulkBoundaryDuality**

Equations
- Tau.BookVII.Meta.Registers.bulk_boundary = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.LawAsAdmissibleContinuation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L736-L747)
**structure
Tau.BookVII.Meta.Registers.LawAsAdmissibleContinuation :Type**


[VII.D31] Law as Admissible Continuation (ch23). Laws of nature
reinterpreted as analytic continuation operators: they extend
local data to global structure. Not prescriptive rules but
structural continuation conditions.

- laws_as_continuation : Bool
Laws = continuation operators.

- non_prescriptive : Bool
Not prescriptive.

- structure_preserving : Bool
Structure-preserving.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprLawAsAdmissibleContinuation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L747-L747)
**instance
Tau.BookVII.Meta.Registers.instReprLawAsAdmissibleContinuation :Repr LawAsAdmissibleContinuation**

Equations
- Tau.BookVII.Meta.Registers.instReprLawAsAdmissibleContinuation = { reprPrec := Tau.BookVII.Meta.Registers.instReprLawAsAdmissibleContinuation.repr }

---

### `Tau.BookVII.Meta.Registers.instReprLawAsAdmissibleContinuation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L747-L747)
**def
Tau.BookVII.Meta.Registers.instReprLawAsAdmissibleContinuation.repr :LawAsAdmissibleContinuation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.law_continuation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L749-L749)
**def
Tau.BookVII.Meta.Registers.law_continuation :LawAsAdmissibleContinuation**

Equations
- Tau.BookVII.Meta.Registers.law_continuation = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.operator_realism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L755-L762)
**theorem
Tau.BookVII.Meta.Registers.operator_realism :law_continuation.laws_as_continuation = true ∧ law_continuation.structure_preserving = true**


[VII.T12] Operator Realism (ch23). Classification of operators
is a structural invariant: the operator algebra is determined by
the kernel axioms, not by convention. Laws are discovered, not
invented — because continuation operators are structurally forced.

---

### `Tau.BookVII.Meta.Registers.CausationAsConstrainedComposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L768-L777)
**structure
Tau.BookVII.Meta.Registers.CausationAsConstrainedComposition :Type**


[VII.D32] Causation as Constrained Composition (ch24). Causation =
morphism factorization: A causes B iff there exists a factorization
A → C → B through an admissible intermediate. Constraints from
kernel axioms determine which factorizations are admissible.

- factorization : Bool
Causation = morphism factorization.

- kernel_constrained : Bool
Admissibility from kernel axioms.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprCausationAsConstrainedComposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L777-L777)
**instance
Tau.BookVII.Meta.Registers.instReprCausationAsConstrainedComposition :Repr CausationAsConstrainedComposition**

Equations
- Tau.BookVII.Meta.Registers.instReprCausationAsConstrainedComposition = { reprPrec := Tau.BookVII.Meta.Registers.instReprCausationAsConstrainedComposition.repr }

---

### `Tau.BookVII.Meta.Registers.instReprCausationAsConstrainedComposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L777-L777)
**def
Tau.BookVII.Meta.Registers.instReprCausationAsConstrainedComposition.repr :CausationAsConstrainedComposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.causation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L779-L779)
**def
Tau.BookVII.Meta.Registers.causation :CausationAsConstrainedComposition**

Equations
- Tau.BookVII.Meta.Registers.causation = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.temporal_ordering_from_persistence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L785-L792)
**theorem
Tau.BookVII.Meta.Registers.temporal_ordering_from_persistence :causation.factorization = true ∧ causation.kernel_constrained = true**


[VII.P06] Temporal Ordering from Persistence (ch24). Time is not
assumed but derived: temporal ordering emerges from the persistence
of NF-addresses through morphism chains. Directed morphisms
induce a partial order = temporal sequence.

---

### `Tau.BookVII.Meta.Registers.TauModalOperators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L798-L810)
**structure
Tau.BookVII.Meta.Registers.TauModalOperators :Type**


[VII.D33] τ-Modal Operators (ch25). Box (□) and Diamond (◇)
from admissible transformations:
□φ = φ holds under all admissible transformations
◇φ = φ holds under some admissible transformation
Internal to τ: no possible-worlds machinery needed.

- has_box : Bool
Box: necessity via all admissible transformations.

- has_diamond : Bool
Diamond: possibility via some admissible transformation.

- internal : Bool
Internal: no external possible worlds.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprTauModalOperators.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L810-L810)
**def
Tau.BookVII.Meta.Registers.instReprTauModalOperators.repr :TauModalOperators → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprTauModalOperators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L810-L810)
**instance
Tau.BookVII.Meta.Registers.instReprTauModalOperators :Repr TauModalOperators**

Equations
- Tau.BookVII.Meta.Registers.instReprTauModalOperators = { reprPrec := Tau.BookVII.Meta.Registers.instReprTauModalOperators.repr }

---

### `Tau.BookVII.Meta.Registers.tau_modal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L812-L812)
**def
Tau.BookVII.Meta.Registers.tau_modal :TauModalOperators**

Equations
- Tau.BookVII.Meta.Registers.tau_modal = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.modal_logic_soundness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L818-L826)
**theorem
Tau.BookVII.Meta.Registers.modal_logic_soundness :tau_modal.has_box = true ∧ tau_modal.has_diamond = true ∧ tau_modal.internal = true**


[VII.T13] Modal Logic Soundness in τ (ch25). Internal Kripke
semantics is sound: the τ-modal operators satisfy S4 axioms
(reflexivity + transitivity of accessibility). Accessibility
relation from admissible transformations.

---

### `Tau.BookVII.Meta.Registers.IdentityAsAddressPersistence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L832-L840)
**structure
Tau.BookVII.Meta.Registers.IdentityAsAddressPersistence :Type**


[VII.D34] Identity as Address Persistence (ch26). Identity of
an object = persistence of its NF-address through transformations.
No "bare substrate" needed: identity IS the address trajectory.

- address_persistence : Bool
Identity = NF-address persistence.

- no_substrate : Bool
No bare substrate.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprIdentityAsAddressPersistence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L840-L840)
**def
Tau.BookVII.Meta.Registers.instReprIdentityAsAddressPersistence.repr :IdentityAsAddressPersistence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprIdentityAsAddressPersistence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L840-L840)
**instance
Tau.BookVII.Meta.Registers.instReprIdentityAsAddressPersistence :Repr IdentityAsAddressPersistence**

Equations
- Tau.BookVII.Meta.Registers.instReprIdentityAsAddressPersistence = { reprPrec := Tau.BookVII.Meta.Registers.instReprIdentityAsAddressPersistence.repr }

---

### `Tau.BookVII.Meta.Registers.identity_persistence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L842-L842)
**def
Tau.BookVII.Meta.Registers.identity_persistence :IdentityAsAddressPersistence**

Equations
- Tau.BookVII.Meta.Registers.identity_persistence = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.MereologicalCompositionAsColimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L848-L856)
**structure
Tau.BookVII.Meta.Registers.MereologicalCompositionAsColimit :Type**


[VII.D35] Mereological Composition as Colimit (ch27). Parts and
wholes via categorical colimits: composition of parts = colimit
of a diagram of parts. Universal property gives canonical whole.

- composition_as_colimit : Bool
Composition = colimit.

- universal_property : Bool
Universal property.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprMereologicalCompositionAsColimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L856-L856)
**instance
Tau.BookVII.Meta.Registers.instReprMereologicalCompositionAsColimit :Repr MereologicalCompositionAsColimit**

Equations
- Tau.BookVII.Meta.Registers.instReprMereologicalCompositionAsColimit = { reprPrec := Tau.BookVII.Meta.Registers.instReprMereologicalCompositionAsColimit.repr }

---

### `Tau.BookVII.Meta.Registers.instReprMereologicalCompositionAsColimit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L856-L856)
**def
Tau.BookVII.Meta.Registers.instReprMereologicalCompositionAsColimit.repr :MereologicalCompositionAsColimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.mereological_colimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L858-L858)
**def
Tau.BookVII.Meta.Registers.mereological_colimit :MereologicalCompositionAsColimit**

Equations
- Tau.BookVII.Meta.Registers.mereological_colimit = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.special_composition_answer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L864-L871)
**theorem
Tau.BookVII.Meta.Registers.special_composition_answer :mereological_colimit.composition_as_colimit = true ∧ mereological_colimit.universal_property = true**


[VII.P07] Special Composition Answer (ch27). Composition exists
when the colimit exists in the ambient category. This gives a
precise structural answer to van Inwagen's Special Composition
Question: things compose when their diagram has a colimit.

---

### `Tau.BookVII.Meta.Registers.AbstractObjectAsStructuralPosition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L877-L886)
**structure
Tau.BookVII.Meta.Registers.AbstractObjectAsStructuralPosition :Type**


[VII.D36] Abstract Object as Structural Position (ch28). Abstract
objects = positions in structures (ante rem structuralism).
Numbers, sets, categories: identified with their structural role
via Yoneda. No Platonic realm needed.

- structural_position : Bool
Position in structure.

- yoneda_identified : Bool
Yoneda identification.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprAbstractObjectAsStructuralPosition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L886-L886)
**def
Tau.BookVII.Meta.Registers.instReprAbstractObjectAsStructuralPosition.repr :AbstractObjectAsStructuralPosition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprAbstractObjectAsStructuralPosition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L886-L886)
**instance
Tau.BookVII.Meta.Registers.instReprAbstractObjectAsStructuralPosition :Repr AbstractObjectAsStructuralPosition**

Equations
- Tau.BookVII.Meta.Registers.instReprAbstractObjectAsStructuralPosition = { reprPrec := Tau.BookVII.Meta.Registers.instReprAbstractObjectAsStructuralPosition.repr }

---

### `Tau.BookVII.Meta.Registers.abstract_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L888-L888)
**def
Tau.BookVII.Meta.Registers.abstract_structural :AbstractObjectAsStructuralPosition**

Equations
- Tau.BookVII.Meta.Registers.abstract_structural = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.ProblemMapClassificationScheme`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L894-L905)
**structure
Tau.BookVII.Meta.Registers.ProblemMapClassificationScheme :Type**


[VII.D38] Problem Map Classification Scheme (ch30). 17 classical
philosophical problems classified by their register-type and
τ-resolution status: dissolved (structure reveals pseudo-problem),
resolved (τ-answer), or bounded (methodological boundary).

- problem_count : ℕ
17 problems classified.

- resolution_types : ℕ
Three resolution types: dissolved/resolved/bounded.

- structural : Bool
Classification is structural.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprProblemMapClassificationScheme.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L905-L905)
**def
Tau.BookVII.Meta.Registers.instReprProblemMapClassificationScheme.repr :ProblemMapClassificationScheme → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprProblemMapClassificationScheme`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L905-L905)
**instance
Tau.BookVII.Meta.Registers.instReprProblemMapClassificationScheme :Repr ProblemMapClassificationScheme**

Equations
- Tau.BookVII.Meta.Registers.instReprProblemMapClassificationScheme = { reprPrec := Tau.BookVII.Meta.Registers.instReprProblemMapClassificationScheme.repr }

---

### `Tau.BookVII.Meta.Registers.problem_map`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L907-L907)
**def
Tau.BookVII.Meta.Registers.problem_map :ProblemMapClassificationScheme**

Equations
- Tau.BookVII.Meta.Registers.problem_map = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.problem_map_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L909-L913)
**theorem
Tau.BookVII.Meta.Registers.problem_map_check :problem_map.problem_count = 17 ∧ problem_map.resolution_types = 3 ∧ problem_map.structural = true**


---

### `Tau.BookVII.Meta.Registers.ThreeLayerSolipsismResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L919-L933)
**structure
Tau.BookVII.Meta.Registers.ThreeLayerSolipsismResolution :Type**


[VII.D39] Three-Layer Solipsism Resolution (ch31). Solipsism
dissolved via three layers:
(1) Ontic: other minds have NF-addresses (exist structurally)
(2) Epistemic: register independence gives independent evidence
(3) Bayesian: solipsism has vanishing posterior under any prior

- ontic_layer : Bool
(1) Ontic layer: NF-addresses for other minds.

- epistemic_layer : Bool
(2) Epistemic layer: register independence.

- bayesian_layer : Bool
(3) Bayesian layer: vanishing posterior.

- layer_count : ℕ
Three layers.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprThreeLayerSolipsismResolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L933-L933)
**def
Tau.BookVII.Meta.Registers.instReprThreeLayerSolipsismResolution.repr :ThreeLayerSolipsismResolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprThreeLayerSolipsismResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L933-L933)
**instance
Tau.BookVII.Meta.Registers.instReprThreeLayerSolipsismResolution :Repr ThreeLayerSolipsismResolution**

Equations
- Tau.BookVII.Meta.Registers.instReprThreeLayerSolipsismResolution = { reprPrec := Tau.BookVII.Meta.Registers.instReprThreeLayerSolipsismResolution.repr }

---

### `Tau.BookVII.Meta.Registers.solipsism_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L935-L935)
**def
Tau.BookVII.Meta.Registers.solipsism_resolution :ThreeLayerSolipsismResolution**

Equations
- Tau.BookVII.Meta.Registers.solipsism_resolution = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.bayesian_exclusion_of_solipsism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L941-L950)
**theorem
Tau.BookVII.Meta.Registers.bayesian_exclusion_of_solipsism :solipsism_resolution.ontic_layer = true ∧ solipsism_resolution.epistemic_layer = true ∧ solipsism_resolution.bayesian_layer = true ∧ solipsism_resolution.layer_count = 3**


[VII.T15] Bayesian Exclusion of Solipsism (ch31). Information-
theoretic argument: under any reasonable prior, the posterior
probability of solipsism vanishes because it requires all
cross-register correlations to be coincidental.

---

### `Tau.BookVII.Meta.Registers.NonDualisticPlatonism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L956-L968)
**structure
Tau.BookVII.Meta.Registers.NonDualisticPlatonism :Type**


[VII.D40] Non-Dualistic Platonism (ch32). Dissolves the
Platonism-Nominalism debate: mathematical objects exist as
structural positions (not in a separate Platonic realm) but
are mind-independent (not nominalist conventions). The kernel
K_τ is the locus of mathematical existence.

- no_separate_realm : Bool
Not Platonic realm.

- mind_independent : Bool
Not nominalist convention.

- kernel_locus : Bool
Structural positions in kernel.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprNonDualisticPlatonism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L968-L968)
**def
Tau.BookVII.Meta.Registers.instReprNonDualisticPlatonism.repr :NonDualisticPlatonism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprNonDualisticPlatonism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L968-L968)
**instance
Tau.BookVII.Meta.Registers.instReprNonDualisticPlatonism :Repr NonDualisticPlatonism**

Equations
- Tau.BookVII.Meta.Registers.instReprNonDualisticPlatonism = { reprPrec := Tau.BookVII.Meta.Registers.instReprNonDualisticPlatonism.repr }

---

### `Tau.BookVII.Meta.Registers.non_dualistic_platonism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L970-L970)
**def
Tau.BookVII.Meta.Registers.non_dualistic_platonism :NonDualisticPlatonism**

Equations
- Tau.BookVII.Meta.Registers.non_dualistic_platonism = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.OmegaUniquenessPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L976-L987)
**structure
Tau.BookVII.Meta.Registers.OmegaUniquenessPrinciple :Type**


[VII.D41] ω-Uniqueness Principle (ch32). Terminal object ω is
unique up to (unique) isomorphism — standard categorical result.
Philosophical reading: the closure point of the lemniscate is
structurally determined, not chosen.

- terminal : Bool
Terminal object.

- unique_up_to_iso : Bool
Unique up to iso.

- structurally_determined : Bool
Structurally determined.

Instances For

---

### `Tau.BookVII.Meta.Registers.instReprOmegaUniquenessPrinciple.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L987-L987)
**def
Tau.BookVII.Meta.Registers.instReprOmegaUniquenessPrinciple.repr :OmegaUniquenessPrinciple → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Registers.instReprOmegaUniquenessPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L987-L987)
**instance
Tau.BookVII.Meta.Registers.instReprOmegaUniquenessPrinciple :Repr OmegaUniquenessPrinciple**

Equations
- Tau.BookVII.Meta.Registers.instReprOmegaUniquenessPrinciple = { reprPrec := Tau.BookVII.Meta.Registers.instReprOmegaUniquenessPrinciple.repr }

---

### `Tau.BookVII.Meta.Registers.omega_uniqueness_principle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L989-L989)
**def
Tau.BookVII.Meta.Registers.omega_uniqueness_principle :OmegaUniquenessPrinciple**

Equations
- Tau.BookVII.Meta.Registers.omega_uniqueness_principle = { }
Instances For

---

### `Tau.BookVII.Meta.Registers.omega_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Registers.lean#L995-L1002)
**theorem
Tau.BookVII.Meta.Registers.omega_uniqueness :omega_uniqueness_principle.terminal = true ∧ omega_uniqueness_principle.unique_up_to_iso = true ∧ omega_uniqueness_principle.structurally_determined = true**


[VII.T16] ω-Uniqueness (ch32). Categorical proof: if T₁ and T₂
are both terminal, then T₁ ≅ T₂ via unique isomorphism.
Applied to ω: the closure generator is unique.
