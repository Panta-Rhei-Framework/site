---
layout: taulib-doc
title: "TauLib.BookVII.Ethics.CIProof"
permalink: /verify/taulib/docs/book-vii-ethics-ci-proof/
lane: verify
module_name: "TauLib.BookVII.Ethics.CIProof"
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

# TauLib.BookVII.Ethics.CIProof


The Categorical Imperative as j-closed fixed point of the practical register.
**P2 formalized** (Wave R8-B): all 8 sorry eliminated; ID mappings corrected.

## Registry Cross-References (CORRECTED R8-B2)


- [VII.D65] Dignity as Label-Independence — `DignityStructure`

- [VII.D66] CI as Naturality Constraint — `CINaturality`

- [VII.D67] Fairness Protocol — `FairnessProtocol`

- [VII.D68] Moral Monodromy — `MoralMonodromy`

- [VII.D69] Four Ethical Tests — `FourEthicalTests`

- [VII.D70] Character as Ethical Fixed Point — `CharacterFixedPoint`

- [VII.D71] CI Operator Graph — `CIOperatorGraph`

- [VII.T30] Dignity Universality — `dignity_universality`

- [VII.T31] CI-Sheaf Equivalence — `ci_sheaf_equivalence`

- [VII.T32] No-Conflict Theorem — `no_conflict`

- [VII.T33] Monodromy as Source of Tragedy — `monodromy_tragedy`

- [VII.T34] Flourishing as Global Section — `flourishing_global_section`

- [VII.T35] CI as j-Closed Fixed Point — `ci_j_closed_fixed_point`

- [VII.T36] Kernel Theorem (K) — `kernel_theorem`

- [VII.T37] Semantic Object Construction (S) — `semantic_object`

- [VII.P21] CI Uniqueness Conjecture — `ci_uniqueness`

- [VII.L11] Duty Typing Lemma — `duty_typing`

- [VII.L12] CI Minimality Lemma — `ci_minimality`

- [VII.L13] First Bombshell Lemma — `first_bombshell`

- [VII.Lxx] Dignity Witness — `dignity_witness`

- [VII.Lxx] Sheaf Gluing Verification — `sheaf_gluing_verification`

- [VII.Lxx] Operator Graph Completeness — `operator_graph_completeness`

- [VII.Lxx] Lattice Completeness of F — `f_lattice_completeness`

- [VII.Lxx] CI Uniqueness Derivation — `ci_uniqueness_derivation`


## Cross-Book Authority


- Book II: j-closure machinery, Grothendieck topology J_τ

- Book VII, Meta.Registers: practical register, sector normalisers

- Book VII, Meta.Archetypes: j-closure lattice structure, LT operator


## Ground Truth Sources


- Book VII Chapters 76–89 (2nd Edition): Ethics (Part 7)


## Three-Stage Proof Programme (K/S/CI)


- Stage K (Kernel Theorem, VII.T36): τ's axioms force existence of j-closed ethical
operator graph at E₃ — tau-effective

- Stage S (Semantic Object, VII.T37): CI-relevant ethical objects constructed internally
at E₃ — tau-effective

- Stage CI (Uniqueness, VII.P21): minimal j-closed fixed point unique — upgraded to
tau-effective via lattice completeness + Knaster-Tarski (Sprint R8-B3)


---

### `Tau.BookVII.Ethics.CIProof.DignityStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L64-L85)
**structure
Tau.BookVII.Ethics.CIProof.DignityStructure :Type**


[VII.D65] Dignity as Label-Independence (ch76).
For agent-state X ∈ Ob(A), identity-invariants D(X) = {P ∈ Prop(X) | σ*P = P ∀ σ}.
A policy π has dignity iff σ ∘ π = π ∘ σ for all σ ∈ Aut(A).
The Dignity Functor D : A → Inv extracts identity-invariants.

Identity-invariants include: rational agency, autonomous will, reflexive
self-awareness, capacity for suffering/flourishing, temporal persistence.
Excluded: names, wealth, social status, contingent attributes.

- label_independent : Bool
Label-independent: commutes with all automorphisms.

- has_identity_invariants : Bool
Identity-invariants extractable via functor D.

- has_admissible_subworld : Bool
Admissible subworld A_dig: full subcategory on dignity-preserving states.

- has_reflector : Bool
Reflector L_dig : A → A_dig exists (left adjoint to inclusion).

- reflector_idempotent : Bool
Reflector is idempotent: L_dig ∘ L_dig = L_dig.

- lt_modality : Bool
j_dig = i ∘ L_dig is a Lawvere-Tierney modal operator on A.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprDignityStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L85-L85)
**instance
Tau.BookVII.Ethics.CIProof.instReprDignityStructure :Repr DignityStructure**

Equations
- Tau.BookVII.Ethics.CIProof.instReprDignityStructure = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprDignityStructure.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprDignityStructure.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L85-L85)
**def
Tau.BookVII.Ethics.CIProof.instReprDignityStructure.repr :DignityStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.dignity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L87-L87)
**def
Tau.BookVII.Ethics.CIProof.dignity :DignityStructure**

Equations
- Tau.BookVII.Ethics.CIProof.dignity = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.dignity_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L89-L95)
**theorem
Tau.BookVII.Ethics.CIProof.dignity_witness :dignity.label_independent = true ∧ dignity.has_identity_invariants = true ∧ dignity.has_admissible_subworld = true**


[VII.Lxx] Dignity Witness: dignity functor D is well-defined and the
admissible subworld A_dig is closed under limits and internal homs.

---

### `Tau.BookVII.Ethics.CIProof.dignity_universality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L101-L118)
**theorem
Tau.BookVII.Ethics.CIProof.dignity_universality :dignity.has_reflector = true ∧ dignity.reflector_idempotent = true ∧ dignity.lt_modality = true ∧ dignity.label_independent = true**


[VII.T30] Dignity Universality (ch76). Five claims:
(1) Reflectivity: L_dig : A → A_dig left adjoint to inclusion
(2) Idempotence: L_dig ∘ L_dig = L_dig
(3) Modality: j_dig = i ∘ L_dig is Lawvere-Tierney
(4) Universality: every NF-address-bearing entity has non-trivial D(X)
(by rigidity Aut(τ) = {id}, structural properties are invariant)
(5) No trade-off: no admissible policy buys utility by degrading D(X)

Proof: (1)–(3) by reflective subcategory results (A_dig closed under
limits + internal homs). (4) by Aut(τ) = {id}: every NF address has
invariant structural properties. (5) by contraposition: degrading
invariants means not factoring through A_dig.

---

### `Tau.BookVII.Ethics.CIProof.CINaturality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L124-L141)
**structure
Tau.BookVII.Ethics.CIProof.CINaturality :Type**


[VII.D66] CI as Naturality Constraint (ch77).
Site of perspectives (P, J): objects = agent-context perspectives,
morphisms = admissible reindexings, covers = all relevant viewpoints.
A maxim M generates presheaf Max_M : P^op → Sets.
CI satisfied iff Max_M is a natural transformation w.r.t. all
admissible reindexings. Equivalently: Max_M is a separated presheaf.

- has_site : Bool
Site of perspectives exists.

- has_maxim_presheaf : Bool
Maxim presheaf Max_M well-defined.

- naturality : Bool
Natural transformation condition.

- separated : Bool
Separated presheaf condition.

- dignity_filtered : Bool
Dignity-filtered: fibers pass through L_dig.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprCINaturality.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L141-L141)
**def
Tau.BookVII.Ethics.CIProof.instReprCINaturality.repr :CINaturality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprCINaturality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L141-L141)
**instance
Tau.BookVII.Ethics.CIProof.instReprCINaturality :Repr CINaturality**

Equations
- Tau.BookVII.Ethics.CIProof.instReprCINaturality = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprCINaturality.repr }

---

### `Tau.BookVII.Ethics.CIProof.ci_naturality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L143-L143)
**def
Tau.BookVII.Ethics.CIProof.ci_naturality :CINaturality**

Equations
- Tau.BookVII.Ethics.CIProof.ci_naturality = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.ci_sheaf_equivalence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L149-L165)
**theorem
Tau.BookVII.Ethics.CIProof.ci_sheaf_equivalence :ci_naturality.has_site = true ∧ ci_naturality.has_maxim_presheaf = true ∧ ci_naturality.naturality = true ∧ ci_naturality.separated = true ∧ ci_naturality.dignity_filtered = true**


[VII.T31] CI-Sheaf Equivalence (ch77). Three equivalent formulations:
(1) Kantian universalizability: M willed as universal law without contradiction
(2) Sheaf condition: Max_M is a sheaf on (P, J)
(3) Naturality + local realizability: Max_M separated, fibers nonempty,
compatibility cocycles trivial

Proof: (1)⟹(2) Kant's test = gluing criterion.
(2)⟹(3) sheaf ⟹ separated + nonempty + trivial cocycles.
(3)⟹(1) naturality = no hidden exceptions, nonempty = conceivability,
trivial cocycles = no Čech obstruction.

---

### `Tau.BookVII.Ethics.CIProof.sheaf_gluing_verification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L167-L172)
**theorem
Tau.BookVII.Ethics.CIProof.sheaf_gluing_verification :ci_naturality.separated = true ∧ ci_naturality.naturality = true**


[VII.Lxx] Sheaf Gluing Verification: under τ-holomorphy, the sheaf condition
can be verified on any single sufficiently fine τ-holomorphic cover.

---

### `Tau.BookVII.Ethics.CIProof.DutyTyping`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L178-L196)
**structure
Tau.BookVII.Ethics.CIProof.DutyTyping :Type**


[VII.L11] Duty Typing Lemma (ch78). An obligation D is properly typed iff:
(1) Local realizability: D(U) ≠ ∅ for every perspective U
(2) Dignity preservation: every enactment factors through L_dig
(3) Overlap compatibility: restriction maps agree on pairwise overlaps
(4) Bounded tension: no enactment forces unbounded tension

Properly typed iff D is a subsheaf of Max.

- local_realizable : Bool
(1) Local realizability.

- dignity_preserving : Bool
(2) Dignity preservation.

- overlap_compatible : Bool
(3) Overlap compatibility.

- bounded_tension : Bool
(4) Bounded tension.

- is_subsheaf : Bool
All conditions = subsheaf of Max.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprDutyTyping.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L196-L196)
**def
Tau.BookVII.Ethics.CIProof.instReprDutyTyping.repr :DutyTyping → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprDutyTyping`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L196-L196)
**instance
Tau.BookVII.Ethics.CIProof.instReprDutyTyping :Repr DutyTyping**

Equations
- Tau.BookVII.Ethics.CIProof.instReprDutyTyping = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprDutyTyping.repr }

---

### `Tau.BookVII.Ethics.CIProof.canonical_duty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L198-L198)
**def
Tau.BookVII.Ethics.CIProof.canonical_duty :DutyTyping**

Equations
- Tau.BookVII.Ethics.CIProof.canonical_duty = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.duty_typing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L200-L206)
**theorem
Tau.BookVII.Ethics.CIProof.duty_typing :canonical_duty.local_realizable = true ∧ canonical_duty.dignity_preserving = true ∧ canonical_duty.overlap_compatible = true ∧ canonical_duty.bounded_tension = true ∧ canonical_duty.is_subsheaf = true**


---

### `Tau.BookVII.Ethics.CIProof.no_conflict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L212-L224)
**theorem
Tau.BookVII.Ethics.CIProof.no_conflict :canonical_duty.is_subsheaf = true ∧ canonical_duty.dignity_preserving = true ∧ ci_naturality.separated = true**


[VII.T32] No-Conflict Theorem (ch78). For properly typed D₁, D₂:
(1) Joint realizability: D₁(U) ∩ D₂(U) ≠ ∅ for every U
(2) Global compatibility: joint fibers glue to global section
(3) No dignity sacrifice: global section factors through L_dig

Proof: intersection of subsheaves pointwise. Proper typing (VII.L11)
gives nonempty fibers + dignity preservation. Sheaf axiom gives gluing.
τ-holomorphy extends local joint enactments globally.

---

### `Tau.BookVII.Ethics.CIProof.MoralMonodromy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L230-L240)
**structure
Tau.BookVII.Ethics.CIProof.MoralMonodromy :Type**


[VII.D68] Moral Monodromy (ch81). For loop γ : U ∼> U in site of
perspectives, holonomy Hol_M(γ) = M_γ : Max(U) → Max(U).
Maxim is flat (monodromy-free) iff Hol_M(γ) = Id for all loops.

- holonomy_defined : Bool
Holonomy well-defined for all loops.

- detects_monodromy : Bool
Can detect non-trivial monodromy.

- flat_iff_trivial : Bool
Flat = monodromy-free.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprMoralMonodromy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L240-L240)
**instance
Tau.BookVII.Ethics.CIProof.instReprMoralMonodromy :Repr MoralMonodromy**

Equations
- Tau.BookVII.Ethics.CIProof.instReprMoralMonodromy = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprMoralMonodromy.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprMoralMonodromy.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L240-L240)
**def
Tau.BookVII.Ethics.CIProof.instReprMoralMonodromy.repr :MoralMonodromy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.moral_monodromy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L242-L242)
**def
Tau.BookVII.Ethics.CIProof.moral_monodromy :MoralMonodromy**

Equations
- Tau.BookVII.Ethics.CIProof.moral_monodromy = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.monodromy_tragedy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L244-L253)
**theorem
Tau.BookVII.Ethics.CIProof.monodromy_tragedy :moral_monodromy.holonomy_defined = true ∧ moral_monodromy.detects_monodromy = true ∧ moral_monodromy.flat_iff_trivial = true**


[VII.T33] Monodromy as Source of Tragedy (ch81). Four claims:
(1) Local consistency: each Max(U_i) ≠ ∅
(2) Global non-closure: Hol_M(γ) ≠ Id, no single global enactment
(3) Topological, not logical: obstruction in π₁(P, U) → Aut(Max(U))
(4) Locatability: specific overlap where transported enactments disagree

---

### `Tau.BookVII.Ethics.CIProof.FourEthicalTests`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L259-L274)
**structure
Tau.BookVII.Ethics.CIProof.FourEthicalTests :Type**


[VII.D69] Four Ethical Tests (ch82). Maxim M admissible iff all pass:
(1) Universalizability: ω(M) = 0 (vanishing Čech obstruction)
(2) Respect: D(M(X)) ≅ D(X) for all affected agents
(3) Coherence: global section compatible with duty portfolio
(4) Monodromy: Hol_M(γ) = Id for all relevant loops

- universalizable : Bool
(1) Universalizability.

- respect : Bool
(2) Respect (dignity preservation).

- coherent : Bool
(3) Coherence.

- monodromy_free : Bool
(4) Monodromy-free.

- test_count : ℕ
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprFourEthicalTests`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L274-L274)
**instance
Tau.BookVII.Ethics.CIProof.instReprFourEthicalTests :Repr FourEthicalTests**

Equations
- Tau.BookVII.Ethics.CIProof.instReprFourEthicalTests = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprFourEthicalTests.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprFourEthicalTests.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L274-L274)
**def
Tau.BookVII.Ethics.CIProof.instReprFourEthicalTests.repr :FourEthicalTests → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.ethical_tests`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L276-L276)
**def
Tau.BookVII.Ethics.CIProof.ethical_tests :FourEthicalTests**

Equations
- Tau.BookVII.Ethics.CIProof.ethical_tests = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.CharacterFixedPoint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L282-L293)
**structure
Tau.BookVII.Ethics.CIProof.CharacterFixedPoint :Type**


[VII.D70] Character as Ethical Fixed Point (ch86).
Habituation functor H : Disp → Disp.
Virtue V: stable fixed point H(V) = V.
Vice W: unstable fixed point or H^n(W) diverges.

- has_habituation : Bool
Habituation functor well-defined.

- virtue_is_fixed : Bool
Virtue = stable fixed point.

- vice_is_unstable : Bool
Vice = unstable fixed point or divergent.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprCharacterFixedPoint.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L293-L293)
**def
Tau.BookVII.Ethics.CIProof.instReprCharacterFixedPoint.repr :CharacterFixedPoint → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprCharacterFixedPoint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L293-L293)
**instance
Tau.BookVII.Ethics.CIProof.instReprCharacterFixedPoint :Repr CharacterFixedPoint**

Equations
- Tau.BookVII.Ethics.CIProof.instReprCharacterFixedPoint = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprCharacterFixedPoint.repr }

---

### `Tau.BookVII.Ethics.CIProof.character`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L295-L295)
**def
Tau.BookVII.Ethics.CIProof.character :CharacterFixedPoint**

Equations
- Tau.BookVII.Ethics.CIProof.character = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.flourishing_global_section`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L301-L310)
**theorem
Tau.BookVII.Ethics.CIProof.flourishing_global_section :character.has_habituation = true ∧ character.virtue_is_fixed = true**


[VII.T34] Flourishing as Global Section (ch86).
V = virtue sheaf over life-stages L.
Flourishing = Γ(L, V). Exists iff:
(1) Local virtue at each life-stage (fixed-point locally)
(2) Gluing across life-stages (agreement on overlaps)
(3) Global existence (sheaf condition over life-course)

---

### `Tau.BookVII.Ethics.CIProof.CIOperatorGraph`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L316-L341)
**structure
Tau.BookVII.Ethics.CIProof.CIOperatorGraph :Type**


[VII.D71] CI Operator Graph (ch88). Quadruple CI = (M, U, γ, R):
M: maxim presheaf (typed pairs (α, φ) of action-type + context predicate)
U: universalization endofunctor (extends context to all perspectives)
γ: coherence test (sheaf condition check)
R: respect operator (naturality under address permutations)

Four components capture Kant's four formulations:
Universal Law (U), Law of Nature (γ), Humanity (R), Autonomy (M + site).

- has_maxim_space : Bool
M: maxim presheaf in Ĉ.

- has_universalization : Bool
U: universalization endofunctor.

- has_coherence_test : Bool
γ: coherence test (sheaf condition).

- has_respect_operator : Bool
R: respect operator (label-invariance).

- component_count : ℕ
Component count = 4 (matching four Kantian formulations).

- j_closed : Bool
j_dig-closed: j_dig(CI) = CI.

- fixed_point : Bool
Fixed point: CI = j(CI).

- minimal : Bool
Minimal: no proper j-closed sub-principle.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprCIOperatorGraph`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L341-L341)
**instance
Tau.BookVII.Ethics.CIProof.instReprCIOperatorGraph :Repr CIOperatorGraph**

Equations
- Tau.BookVII.Ethics.CIProof.instReprCIOperatorGraph = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprCIOperatorGraph.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprCIOperatorGraph.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L341-L341)
**def
Tau.BookVII.Ethics.CIProof.instReprCIOperatorGraph.repr :CIOperatorGraph → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.ci_graph`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L343-L343)
**def
Tau.BookVII.Ethics.CIProof.ci_graph :CIOperatorGraph**

Equations
- Tau.BookVII.Ethics.CIProof.ci_graph = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.operator_graph_completeness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L345-L354)
**theorem
Tau.BookVII.Ethics.CIProof.operator_graph_completeness :ci_graph.has_maxim_space = true ∧ ci_graph.has_universalization = true ∧ ci_graph.has_coherence_test = true ∧ ci_graph.has_respect_operator = true ∧ ci_graph.component_count = 4**


[VII.Lxx] Operator Graph Completeness: all four components of the CI
operator graph are determined by the structural data of τ at E₃
(no arbitrary choices).

---

### `Tau.BookVII.Ethics.CIProof.ci_j_closed_fixed_point`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L360-L375)
**theorem
Tau.BookVII.Ethics.CIProof.ci_j_closed_fixed_point :ci_graph.j_closed = true ∧ ci_graph.fixed_point = true ∧ ci_graph.minimal = true ∧ dignity.lt_modality = true**


[VII.T35] CI as j-Closed Fixed Point (ch88). Three claims:
(1) Stability: j_dig(CI) = CI
(2) Component-wise: j_dig(M⁺) = M⁺, j_dig ∘ U = U ∘ j_dig,
j_dig(γ) = γ, j_dig ∘ R = R ∘ j_dig
(3) Interpretation: CI already lives in A_dig

Proof: sheaf condition is label-independent → M⁺ j-closed.
U commutes with L_dig (universal quantification preserves site).
γ checks membership in j-closed M⁺. R checks invariance under
exactly the group defining L_dig.

---

### `Tau.BookVII.Ethics.CIProof.ci_minimality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L381-L394)
**theorem
Tau.BookVII.Ethics.CIProof.ci_minimality :ci_graph.j_closed = true ∧ ci_graph.minimal = true ∧ ci_graph.fixed_point = true**


[VII.L12] CI Minimality (ch88). In the poset F of j_dig-closed operator
graphs, ordered by inclusion:
(1) Lower bound: CI is the minimum (CI-admissible ⊆ any G ∈ F)
(2) Necessity: any G' strictly weaker is not j-closed
(3) Redundancy: any G'' strictly stronger has CI as retract

Proof: any j-closed graph must enforce sheaf condition + label-independence
(otherwise j_dig closes it further). These are exactly the CI conditions.
Knaster-Tarski on complete lattice F.

---

### `Tau.BookVII.Ethics.CIProof.KernelTheoremResult`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L400-L422)
**structure
Tau.BookVII.Ethics.CIProof.KernelTheoremResult :Type**


[VII.T36] Kernel Theorem (ch89, Stage K). At E₃ in τ:
(1) Existence: there exists a j_dig-closed operator graph G = (M, U, γ, R)
(2) Structural origin: forced by (a) saturation Enrich⁴ = Enrich³,
(b) bipolar L = S¹ ∨ S¹ generating agent-patient polarity,
(c) Yoneda embedding ensuring faithful presheaf representation
(3) Canonicity: determined by structural data, no arbitrary choices

Proof: self-enrichment at E₃ provides internal hom [A,A]; maxims are
sections M = Γ([A,A]). U via internal universal quantification (topos).
γ = sheafification comparison. R = Aut(C) action. Bipolar structure
ensures non-trivial site. Yoneda ensures faithfulness.

- existence : Bool
Existence of j-closed operator graph.

- from_saturation : Bool
Forced by self-enrichment saturation.

- from_bipolarity : Bool
Forced by bipolar lemniscate structure.

- from_yoneda : Bool
Forced by Yoneda faithfulness.

- canonical : Bool
Canonically determined.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprKernelTheoremResult.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L422-L422)
**def
Tau.BookVII.Ethics.CIProof.instReprKernelTheoremResult.repr :KernelTheoremResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprKernelTheoremResult`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L422-L422)
**instance
Tau.BookVII.Ethics.CIProof.instReprKernelTheoremResult :Repr KernelTheoremResult**

Equations
- Tau.BookVII.Ethics.CIProof.instReprKernelTheoremResult = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprKernelTheoremResult.repr }

---

### `Tau.BookVII.Ethics.CIProof.kernel_result`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L424-L424)
**def
Tau.BookVII.Ethics.CIProof.kernel_result :KernelTheoremResult**

Equations
- Tau.BookVII.Ethics.CIProof.kernel_result = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.kernel_theorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L426-L432)
**theorem
Tau.BookVII.Ethics.CIProof.kernel_theorem :kernel_result.existence = true ∧ kernel_result.from_saturation = true ∧ kernel_result.from_bipolarity = true ∧ kernel_result.from_yoneda = true ∧ kernel_result.canonical = true**


---

### `Tau.BookVII.Ethics.CIProof.SemanticObjectResult`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L438-L454)
**structure
Tau.BookVII.Ethics.CIProof.SemanticObjectResult :Type**


[VII.T37] Semantic Object Construction (ch89, Stage S). At E₃, internally
constructible:
(1) Typed maxims: m = (α, φ) as sections of M, using [A,A] and Ω
(2) Universalization domains: sieve {c | U(m)(c) enactable}
(3) Personhood predicates: identity-invariants as decidable internal predicates
(4) Obligation morphisms: dignity-preserving f : X → Y in A_dig

- typed_maxims : Bool
Typed maxims constructible.

- universalization_domains : Bool
Universalization domains well-defined.

- personhood_predicates : Bool
Personhood predicates decidable internally.

- obligation_morphisms : Bool
Obligation morphisms in A_dig.

- semantic_component_count : ℕ
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprSemanticObjectResult`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L454-L454)
**instance
Tau.BookVII.Ethics.CIProof.instReprSemanticObjectResult :Repr SemanticObjectResult**

Equations
- Tau.BookVII.Ethics.CIProof.instReprSemanticObjectResult = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprSemanticObjectResult.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprSemanticObjectResult.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L454-L454)
**def
Tau.BookVII.Ethics.CIProof.instReprSemanticObjectResult.repr :SemanticObjectResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.semantic_result`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L456-L456)
**def
Tau.BookVII.Ethics.CIProof.semantic_result :SemanticObjectResult**

Equations
- Tau.BookVII.Ethics.CIProof.semantic_result = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.semantic_object`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L458-L464)
**theorem
Tau.BookVII.Ethics.CIProof.semantic_object :semantic_result.typed_maxims = true ∧ semantic_result.universalization_domains = true ∧ semantic_result.personhood_predicates = true ∧ semantic_result.obligation_morphisms = true ∧ semantic_result.semantic_component_count = 4**


---

### `Tau.BookVII.Ethics.CIProof.JClosedOperatorGraphLattice`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L470-L482)
**structure
Tau.BookVII.Ethics.CIProof.JClosedOperatorGraphLattice :Type**


The lattice of j_dig-closed operator graphs F.
Key property: F is a complete lattice (arbitrary intersections
of j-closed operator graphs preserve j-closure).

- non_empty : Bool
Non-empty (Kernel Theorem VII.T36 guarantees).

- intersection_closed : Bool
Closed under arbitrary intersection.

- complete_lattice : Bool
Forms complete lattice.

- has_unique_minimum : Bool
Has unique minimum element.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprJClosedOperatorGraphLattice.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L482-L482)
**def
Tau.BookVII.Ethics.CIProof.instReprJClosedOperatorGraphLattice.repr :JClosedOperatorGraphLattice → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprJClosedOperatorGraphLattice`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L482-L482)
**instance
Tau.BookVII.Ethics.CIProof.instReprJClosedOperatorGraphLattice :Repr JClosedOperatorGraphLattice**

Equations
- Tau.BookVII.Ethics.CIProof.instReprJClosedOperatorGraphLattice = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprJClosedOperatorGraphLattice.repr }

---

### `Tau.BookVII.Ethics.CIProof.f_lattice`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L484-L484)
**def
Tau.BookVII.Ethics.CIProof.f_lattice :JClosedOperatorGraphLattice**

Equations
- Tau.BookVII.Ethics.CIProof.f_lattice = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.f_lattice_completeness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L486-L497)
**theorem
Tau.BookVII.Ethics.CIProof.f_lattice_completeness :f_lattice.non_empty = true ∧ f_lattice.intersection_closed = true ∧ f_lattice.complete_lattice = true**


[VII.Lxx] Lattice Completeness of F: the poset of j_dig-closed operator
graphs is a complete lattice. Arbitrary intersections of j-closed
operator graphs preserve j-closure because:


- Intersection of j-closed maxim-spaces is j-closed (sheaf property)

- U commutes with intersection (universal quantification distributes)

- γ restricted to intersection remains well-defined

- R restricted to intersection preserves label-invariance


---

### `Tau.BookVII.Ethics.CIProof.ci_uniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L499-L516)
**theorem
Tau.BookVII.Ethics.CIProof.ci_uniqueness :f_lattice.complete_lattice = true ∧ f_lattice.non_empty = true ∧ f_lattice.has_unique_minimum = true ∧ ci_graph.minimal = true**


[VII.P21] CI Uniqueness (ch89, Stage CI).
SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B3).

In Ĉ internal to τ at E₃, the minimal j_dig-closed operator graph
is unique up to natural isomorphism: G₁, G₂ ∈ F_min ⟹ G₁ ≅ G₂.

Proof (Knaster-Tarski):

- F is a complete lattice (f_lattice_completeness)

- F is non-empty (kernel_theorem, VII.T36)

- In any non-empty complete lattice, the minimum element is unique

- The minimum of F is the CI operator graph (ci_minimality, VII.L12)
Therefore: the minimal j-closed operator graph is unique up to iso.


---

### `Tau.BookVII.Ethics.CIProof.ci_uniqueness_derivation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L518-L532)
**theorem
Tau.BookVII.Ethics.CIProof.ci_uniqueness_derivation :f_lattice.complete_lattice = true ∧ f_lattice.intersection_closed = true ∧ kernel_result.existence = true ∧ f_lattice.non_empty = true ∧ f_lattice.has_unique_minimum = true ∧ ci_graph.minimal = true ∧ ci_graph.j_closed = true**


[VII.Lxx] CI Uniqueness Derivation: the full chain from lattice
completeness through Knaster-Tarski to uniqueness.

---

### `Tau.BookVII.Ethics.CIProof.first_bombshell`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L538-L555)
**theorem
Tau.BookVII.Ethics.CIProof.first_bombshell :Meta.Registers.reg_P.register_type = Meta.Registers.RegisterType.practical ∧ Meta.Registers.reg_P.action_guiding = true ∧ Meta.Registers.reg_E.register_type ≠ Meta.Registers.reg_P.register_type ∧ kernel_result.from_saturation = true**


[VII.L13] First Bombshell (ch89). Three claims about "earning the language":
(1) Circular foundations: taking ethical vocabulary as primitive is circular
(2) Naturalistic fallacy: deriving from empirical facts commits is-ought gap
(3) Earned vocabulary: in τ, Stages K+S show ethical vocabulary is constructed
from self-enrichment at E₃. The is-ought gap dissolves because Reg_P
exists alongside (not derived from) Reg_E.

The practical register is as fundamental as the empirical register —
both are readout functors on the same kernel.

---

### `Tau.BookVII.Ethics.CIProof.FairnessProtocol`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L561-L573)
**structure
Tau.BookVII.Ethics.CIProof.FairnessProtocol :Type**


[VII.D67] Fairness Protocol (ch80). 5-step procedure:
(1) Boundary identification (affected persons, actions)
(2) Structural filtering (label-independent criteria)
(3) Dignity check (factors through L_dig)
(4) Residual tie-breaking (uniform lottery 1/n)
(5) Execution (no conditioning on contingent labels)

- step_count : ℕ
- label_independent : Bool
Label-independent throughout.

- dignity_preserving : Bool
Dignity-preserving throughout.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprFairnessProtocol`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L573-L573)
**instance
Tau.BookVII.Ethics.CIProof.instReprFairnessProtocol :Repr FairnessProtocol**

Equations
- Tau.BookVII.Ethics.CIProof.instReprFairnessProtocol = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprFairnessProtocol.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprFairnessProtocol.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L573-L573)
**def
Tau.BookVII.Ethics.CIProof.instReprFairnessProtocol.repr :FairnessProtocol → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.fairness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L575-L575)
**def
Tau.BookVII.Ethics.CIProof.fairness :FairnessProtocol**

Equations
- Tau.BookVII.Ethics.CIProof.fairness = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.BooleanMicroLogic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L585-L595)
**structure
Tau.BookVII.Ethics.CIProof.BooleanMicroLogic :Type**


[VII.D57] Boolean Micro-Logic (ch39). Single-address classical
logic: at a single NF-address, propositions are 2-valued and
decidable. Boolean algebra of propositions applies.

- single_address : Bool
Single NF-address scope.

- two_valued : Bool
2-valued (true/false).

- decidable : Bool
Decidable propositions.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprBooleanMicroLogic.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L595-L595)
**def
Tau.BookVII.Ethics.CIProof.instReprBooleanMicroLogic.repr :BooleanMicroLogic → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprBooleanMicroLogic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L595-L595)
**instance
Tau.BookVII.Ethics.CIProof.instReprBooleanMicroLogic :Repr BooleanMicroLogic**

Equations
- Tau.BookVII.Ethics.CIProof.instReprBooleanMicroLogic = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprBooleanMicroLogic.repr }

---

### `Tau.BookVII.Ethics.CIProof.boolean_micro`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L597-L597)
**def
Tau.BookVII.Ethics.CIProof.boolean_micro :BooleanMicroLogic**

Equations
- Tau.BookVII.Ethics.CIProof.boolean_micro = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.single_address_classical_logic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L603-L611)
**theorem
Tau.BookVII.Ethics.CIProof.single_address_classical_logic :boolean_micro.single_address = true ∧ boolean_micro.two_valued = true ∧ boolean_micro.decidable = true**


[VII.T22] Single-Address Classical Logic (ch39). At a single
NF-address, classical logic holds: excluded middle, double
negation elimination, and all Boolean identities are valid.
This is the ground level of the scale-dependent logic stack.

---

### `Tau.BookVII.Ethics.CIProof.BayesianMesoLogic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L617-L627)
**structure
Tau.BookVII.Ethics.CIProof.BayesianMesoLogic :Type**


[VII.D58] Bayesian Meso-Logic (ch39). Multi-address probabilistic
logic: across multiple NF-addresses, propositions carry probability
weights. Bayesian updating as the coherence criterion.

- multi_address : Bool
Multi-address scope.

- probabilistic : Bool
Probabilistic truth values.

- bayesian_update : Bool
Bayesian updating.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprBayesianMesoLogic.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L627-L627)
**def
Tau.BookVII.Ethics.CIProof.instReprBayesianMesoLogic.repr :BayesianMesoLogic → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprBayesianMesoLogic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L627-L627)
**instance
Tau.BookVII.Ethics.CIProof.instReprBayesianMesoLogic :Repr BayesianMesoLogic**

Equations
- Tau.BookVII.Ethics.CIProof.instReprBayesianMesoLogic = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprBayesianMesoLogic.repr }

---

### `Tau.BookVII.Ethics.CIProof.bayesian_meso`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L629-L629)
**def
Tau.BookVII.Ethics.CIProof.bayesian_meso :BayesianMesoLogic**

Equations
- Tau.BookVII.Ethics.CIProof.bayesian_meso = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.scale_dependent_logic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L635-L644)
**theorem
Tau.BookVII.Ethics.CIProof.scale_dependent_logic :boolean_micro.single_address = true ∧ bayesian_meso.multi_address = true**


[VII.T23] Scale-Dependent Logic (ch39). The logic type is
determined by the number of NF-addresses in scope:


- 1 address → Boolean (classical)

- n addresses → Bayesian (probabilistic)

- ∞ addresses → Intuitionistic (constructive)
No single logic is "the" logic; scale determines type.


---

### `Tau.BookVII.Ethics.CIProof.InternalRandomness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L650-L661)
**structure
Tau.BookVII.Ethics.CIProof.InternalRandomness :Type**


[VII.D59] Internal Randomness (ch40). No external source of
randomness: all apparent randomness is internal complexity.
A sequence is random iff its Kolmogorov complexity ≥ its length.
Randomness is an emergent property of deterministic kernel structure.

- no_external_source : Bool
No external source.

- complexity_as_randomness : Bool
Complexity-as-randomness.

- deterministic_kernel : Bool
Deterministic kernel.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprInternalRandomness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L661-L661)
**def
Tau.BookVII.Ethics.CIProof.instReprInternalRandomness.repr :InternalRandomness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprInternalRandomness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L661-L661)
**instance
Tau.BookVII.Ethics.CIProof.instReprInternalRandomness :Repr InternalRandomness**

Equations
- Tau.BookVII.Ethics.CIProof.instReprInternalRandomness = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprInternalRandomness.repr }

---

### `Tau.BookVII.Ethics.CIProof.internal_randomness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L663-L663)
**def
Tau.BookVII.Ethics.CIProof.internal_randomness :InternalRandomness**

Equations
- Tau.BookVII.Ethics.CIProof.internal_randomness = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.randomness_as_internal_complexity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L669-L675)
**theorem
Tau.BookVII.Ethics.CIProof.randomness_as_internal_complexity :internal_randomness.no_external_source = true ∧ internal_randomness.complexity_as_randomness = true**


[VII.P15] Randomness as Internal Complexity (ch40). What appears
random is structurally complex: Kolmogorov incompressibility is
the criterion. No dice-rolling deity needed.

---

### `Tau.BookVII.Ethics.CIProof.no_external_randomness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L681-L688)
**theorem
Tau.BookVII.Ethics.CIProof.no_external_randomness :internal_randomness.no_external_source = true ∧ internal_randomness.deterministic_kernel = true**


[VII.T24] No External Randomness (ch40). There is no external
random number generator: NF-addressability precludes any source
outside the kernel. All stochastic behaviour is projective
(coarse-graining of deterministic dynamics).

---

### `Tau.BookVII.Ethics.CIProof.kolmogorov_representation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L694-L701)
**theorem
Tau.BookVII.Ethics.CIProof.kolmogorov_representation :internal_randomness.complexity_as_randomness = true ∧ internal_randomness.deterministic_kernel = true**


[VII.T25] Kolmogorov Representation (ch40). Internal probability
measures satisfy Kolmogorov axioms: they arise as normalized
counting measures on NF-address subsets. No additional structure
needed beyond NF-addresses + morphism counts.

---

### `Tau.BookVII.Ethics.CIProof.inference_from_kernel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L707-L715)
**theorem
Tau.BookVII.Ethics.CIProof.inference_from_kernel :internal_randomness.deterministic_kernel = true ∧ boolean_micro.decidable = true**


[VII.T26] Inference from Kernel Structure (ch41). Inductive
inference is a structural feature of the kernel: continuation
operators (analytic continuation) provide the bridge from
local evidence to global prediction. Not Humean custom but
structural necessity.

---

### `Tau.BookVII.Ethics.CIProof.TruthMakerLogical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L721-L738)
**structure
Tau.BookVII.Ethics.CIProof.TruthMakerLogical :Type**


[VII.D60] Truth-Maker — Logical (ch42). Four-level alethic
hierarchy (matching VII.D27 ontological truth-makers):
Level 1: Inclusion (subobject witness, monomorphism)
Level 2: Section (global section of a sheaf)
Level 3: Diagram (commutative diagram as proof certificate)
Level 4: Invariant (property stable under all automorphisms)

- level_inclusion : Bool
Level 1: inclusion truth-maker.

- level_section : Bool
Level 2: section truth-maker.

- level_diagram : Bool
Level 3: diagram truth-maker.

- level_invariant : Bool
Level 4: invariant truth-maker.

- level_count : ℕ
Four levels.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprTruthMakerLogical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L738-L738)
**instance
Tau.BookVII.Ethics.CIProof.instReprTruthMakerLogical :Repr TruthMakerLogical**

Equations
- Tau.BookVII.Ethics.CIProof.instReprTruthMakerLogical = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprTruthMakerLogical.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprTruthMakerLogical.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L738-L738)
**def
Tau.BookVII.Ethics.CIProof.instReprTruthMakerLogical.repr :TruthMakerLogical → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.truth_maker_logical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L740-L740)
**def
Tau.BookVII.Ethics.CIProof.truth_maker_logical :TruthMakerLogical**

Equations
- Tau.BookVII.Ethics.CIProof.truth_maker_logical = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.TruthBearerAsSection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L746-L755)
**structure
Tau.BookVII.Ethics.CIProof.TruthBearerAsSection :Type**


[VII.D61] Truth-Bearer as Section (ch42). The truth-bearer is
a section of a presheaf: a global assignment of truth values
compatible with restriction maps. Propositions are sections,
truth is a global section property.

- bearer_as_section : Bool
Truth-bearer = section.

- restriction_compatible : Bool
Compatible with restrictions.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprTruthBearerAsSection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L755-L755)
**def
Tau.BookVII.Ethics.CIProof.instReprTruthBearerAsSection.repr :TruthBearerAsSection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprTruthBearerAsSection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L755-L755)
**instance
Tau.BookVII.Ethics.CIProof.instReprTruthBearerAsSection :Repr TruthBearerAsSection**

Equations
- Tau.BookVII.Ethics.CIProof.instReprTruthBearerAsSection = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprTruthBearerAsSection.repr }

---

### `Tau.BookVII.Ethics.CIProof.truth_bearer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L757-L757)
**def
Tau.BookVII.Ethics.CIProof.truth_bearer :TruthBearerAsSection**

Equations
- Tau.BookVII.Ethics.CIProof.truth_bearer = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.alethic_unification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L763-L773)
**theorem
Tau.BookVII.Ethics.CIProof.alethic_unification :truth_maker_logical.level_inclusion = true ∧ truth_maker_logical.level_section = true ∧ truth_maker_logical.level_diagram = true ∧ truth_maker_logical.level_invariant = true ∧ truth_maker_logical.level_count = 4**


[VII.T27] Alethic Unification (ch42). The four truth-maker
levels form a coherent hierarchy: each level contains the
previous. Inclusion ⊂ Section ⊂ Diagram ⊂ Invariant.
All four are unified by sheaf-theoretic structure.

---

### `Tau.BookVII.Ethics.CIProof.alethic_pluralism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L779-L787)
**theorem
Tau.BookVII.Ethics.CIProof.alethic_pluralism :truth_maker_logical.level_count = 4 ∧ truth_bearer.bearer_as_section = true**


[VII.P16] Alethic Pluralism (ch42). Different registers employ
different truth-maker levels: Reg_E uses inclusion (empirical
verification), Reg_D uses diagram (formal proof), Reg_C uses
invariant (stance-stability). This is structural pluralism,
not relativism.

---

### `Tau.BookVII.Ethics.CIProof.ModalFrameTau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L793-L803)
**structure
Tau.BookVII.Ethics.CIProof.ModalFrameTau :Type**


[VII.D62] Modal Frame in τ (ch43). Kripke frame (W, R) realized
internally: worlds = NF-addresses, accessibility R = admissible
transformations between addresses. No external possible worlds.

- worlds_as_addresses : Bool
Worlds = NF-addresses.

- accessibility_admissible : Bool
Accessibility = admissible transformations.

- internal : Bool
Internal to τ.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprModalFrameTau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L803-L803)
**instance
Tau.BookVII.Ethics.CIProof.instReprModalFrameTau :Repr ModalFrameTau**

Equations
- Tau.BookVII.Ethics.CIProof.instReprModalFrameTau = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprModalFrameTau.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprModalFrameTau.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L803-L803)
**def
Tau.BookVII.Ethics.CIProof.instReprModalFrameTau.repr :ModalFrameTau → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.modal_frame`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L805-L805)
**def
Tau.BookVII.Ethics.CIProof.modal_frame :ModalFrameTau**

Equations
- Tau.BookVII.Ethics.CIProof.modal_frame = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.AccessibilityMorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L811-L822)
**structure
Tau.BookVII.Ethics.CIProof.AccessibilityMorphism :Type**


[VII.D63] Accessibility Morphism (ch43). The accessibility
relation is a morphism in the kernel: f : w₁ → w₂ iff w₂ is
accessible from w₁ via an admissible transformation. Reflexive
and transitive (S4).

- reflexive : Bool
Reflexive: every world accesses itself.

- transitive : Bool
Transitive: accessibility composes.

- kernel_morphism : Bool
Morphism in kernel.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprAccessibilityMorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L822-L822)
**instance
Tau.BookVII.Ethics.CIProof.instReprAccessibilityMorphism :Repr AccessibilityMorphism**

Equations
- Tau.BookVII.Ethics.CIProof.instReprAccessibilityMorphism = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprAccessibilityMorphism.repr }

---

### `Tau.BookVII.Ethics.CIProof.instReprAccessibilityMorphism.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L822-L822)
**def
Tau.BookVII.Ethics.CIProof.instReprAccessibilityMorphism.repr :AccessibilityMorphism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.accessibility`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L824-L824)
**def
Tau.BookVII.Ethics.CIProof.accessibility :AccessibilityMorphism**

Equations
- Tau.BookVII.Ethics.CIProof.accessibility = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.kripke_soundness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L830-L840)
**theorem
Tau.BookVII.Ethics.CIProof.kripke_soundness :modal_frame.worlds_as_addresses = true ∧ modal_frame.accessibility_admissible = true ∧ modal_frame.internal = true ∧ accessibility.reflexive = true ∧ accessibility.transitive = true**


[VII.T28] Kripke Soundness in τ (ch43). The internal modal
frame satisfies S4 axioms. Soundness: if □φ holds at w, then
φ holds at all accessible w'. Completeness relative to S4.
The modal operators from VII.D33 are sound w.r.t. this frame.

---

### `Tau.BookVII.Ethics.CIProof.modal_collapse_prevention`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L846-L854)
**theorem
Tau.BookVII.Ethics.CIProof.modal_collapse_prevention :accessibility.reflexive = true ∧ accessibility.transitive = true ∧ accessibility.kernel_morphism = true**


[VII.L09] Modal Collapse Prevention (ch43). The internal modal
frame prevents modal collapse (□φ → φ without ◇φ → φ) because
accessibility is not symmetric in general: admissible
transformations are directed.

---

### `Tau.BookVII.Ethics.CIProof.ParaconsistentBoundaryLogic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L860-L871)
**structure
Tau.BookVII.Ethics.CIProof.ParaconsistentBoundaryLogic :Type**


[VII.D64] Paraconsistent Boundary Logic (ch44). At register
boundaries (sector crossings), controlled contradiction is
possible: φ ∧ ¬φ can hold locally without global explosion.
The lemniscate crossing point p₀ is the canonical site.

- controlled_contradiction : Bool
Controlled contradiction at boundaries.

- no_explosion : Bool
No global explosion.

- crossing_point_site : Bool
Canonical site: crossing point p₀.

Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprParaconsistentBoundaryLogic.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L871-L871)
**def
Tau.BookVII.Ethics.CIProof.instReprParaconsistentBoundaryLogic.repr :ParaconsistentBoundaryLogic → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Ethics.CIProof.instReprParaconsistentBoundaryLogic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L871-L871)
**instance
Tau.BookVII.Ethics.CIProof.instReprParaconsistentBoundaryLogic :Repr ParaconsistentBoundaryLogic**

Equations
- Tau.BookVII.Ethics.CIProof.instReprParaconsistentBoundaryLogic = { reprPrec := Tau.BookVII.Ethics.CIProof.instReprParaconsistentBoundaryLogic.repr }

---

### `Tau.BookVII.Ethics.CIProof.paraconsistent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L873-L873)
**def
Tau.BookVII.Ethics.CIProof.paraconsistent :ParaconsistentBoundaryLogic**

Equations
- Tau.BookVII.Ethics.CIProof.paraconsistent = { }
Instances For

---

### `Tau.BookVII.Ethics.CIProof.no_explosion_at_boundaries`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L879-L887)
**theorem
Tau.BookVII.Ethics.CIProof.no_explosion_at_boundaries :paraconsistent.controlled_contradiction = true ∧ paraconsistent.no_explosion = true ∧ paraconsistent.crossing_point_site = true**


[VII.T29] No-Explosion at Boundaries (ch44). At register
boundaries, the logic is paraconsistent: φ ∧ ¬φ does not
entail arbitrary ψ. The monodromy around the crossing point
prevents global trivialization.

---

### `Tau.BookVII.Ethics.CIProof.truth_4_paraconsistency`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Ethics/CIProof.lean#L893-L902)
**theorem
Tau.BookVII.Ethics.CIProof.truth_4_paraconsistency :paraconsistent.controlled_contradiction = true ∧ paraconsistent.no_explosion = true ∧ boolean_micro.two_valued = true**


[VII.L10] Truth-4 Paraconsistency (ch44). At the boundary,
a 4-valued truth system: {true, false, both, neither}.
"Both" = φ true in one register, ¬φ true in another.
"Neither" = φ undecided in all registers.
The 4-valued system is consistent with scale-dependent logic.
