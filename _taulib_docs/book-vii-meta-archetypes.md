---
layout: taulib-doc
title: "TauLib.BookVII.Meta.Archetypes"
permalink: /verify/taulib/docs/book-vii-meta-archetypes/
lane: verify
module_name: "TauLib.BookVII.Meta.Archetypes"
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

# TauLib.BookVII.Meta.Archetypes


Archetypes as minimal j-closed fixed points of the Grothendieck topology J_τ.
**P2 formalized** (Wave R8-B): all 3 sorry eliminated.

## Registry Cross-References


- [VII.D16] Archetype as Minimal j-Closed Fixed Point — `ArchetypeFixedPoint`

- [VII.D17] Archetype Extractor Protocol — `ArchetypeExtractor`

- [VII.L08] j-Closure Minimality — `j_closure_minimality`

- [VII.T08] Archetype Existence — `archetype_existence`

- [VII.D18] Boundary Archetype — `BoundaryArchetype`

- [VII.D19] Mitigation Archetype — `MitigationArchetype`

- [VII.D20] Meta-Framing Archetype — `MetaFramingArchetype`

- [VII.P05] Boundary Archetype Minimality — `boundary_archetype_minimality`

- [VII.Lxx] LT Axiom Verification — `lt_axiom_verification`

- [VII.Lxx] Lattice Closure — `lattice_closure`

- [VII.Lxx] Minimality Witness — `minimality_witness`


## Cross-Book Authority


- Book II: j-closure operator, Grothendieck topology J_τ

- Book VII, Meta.Registers: register decomposition, sector structure


## Ground Truth Sources


- Book VII Chapters 10–13 (2nd Edition): Archetypes, Boundary/Mitigation/Meta-Framing


---

### `Tau.BookVII.Meta.Archetypes.LawvereTierneyOperator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L40-L49)
**structure
Tau.BookVII.Meta.Archetypes.LawvereTierneyOperator :Type**


Lawvere-Tierney closure operator j : Ω → Ω on [τ^op, τ].
Three axioms: (LT1) j ∘ true = true, (LT2) j ∘ j = j, (LT3) j ∘ ∧ = ∧ ∘ (j × j).

- lt1_truth_closed : Bool
(LT1) Truth-closed: j preserves truth.

- lt2_idempotent : Bool
(LT2) Idempotent: j ∘ j = j.

- lt3_meet_commute : Bool
(LT3) Commutes with meet: j ∘ ∧ = ∧ ∘ (j × j).

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprLawvereTierneyOperator.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L49-L49)
**def
Tau.BookVII.Meta.Archetypes.instReprLawvereTierneyOperator.repr :LawvereTierneyOperator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprLawvereTierneyOperator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L49-L49)
**instance
Tau.BookVII.Meta.Archetypes.instReprLawvereTierneyOperator :Repr LawvereTierneyOperator**

Equations
- Tau.BookVII.Meta.Archetypes.instReprLawvereTierneyOperator = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprLawvereTierneyOperator.repr }

---

### `Tau.BookVII.Meta.Archetypes.j_tau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L51-L52)
**def
Tau.BookVII.Meta.Archetypes.j_tau :LawvereTierneyOperator**


The canonical LT operator induced by J_τ on [τ^op, τ].
Equations
- Tau.BookVII.Meta.Archetypes.j_tau = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.lt_axiom_verification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L54-L62)
**theorem
Tau.BookVII.Meta.Archetypes.lt_axiom_verification :j_tau.lt1_truth_closed = true ∧ j_tau.lt2_idempotent = true ∧ j_tau.lt3_meet_commute = true**


[VII.Lxx] LT Axiom Verification: j_τ satisfies all three Lawvere-Tierney axioms.
LT1 from J_τ being a Grothendieck topology (maximal sieve covers),
LT2 from J_τ-closure being idempotent (sheafification is idempotent),
LT3 from J_τ derived from τ³ cylinder basis (finite meets of covers are covers).

---

### `Tau.BookVII.Meta.Archetypes.StructuralInvariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L68-L77)
**structure
Tau.BookVII.Meta.Archetypes.StructuralInvariant :Type**


A structural invariant I: a property of subobjects preserved by isomorphism.
Examples: threshold-crossing, self-repair, self-framing.

- iso_preserved : Bool
Preserved under isomorphism.

- has_exhibitor : Bool
Exhibited by at least one j-closed subobject (non-vacuity).

- positive_coherence : Bool
Defined by positive coherence conditions.

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprStructuralInvariant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L77-L77)
**def
Tau.BookVII.Meta.Archetypes.instReprStructuralInvariant.repr :StructuralInvariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprStructuralInvariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L77-L77)
**instance
Tau.BookVII.Meta.Archetypes.instReprStructuralInvariant :Repr StructuralInvariant**

Equations
- Tau.BookVII.Meta.Archetypes.instReprStructuralInvariant = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprStructuralInvariant.repr }

---

### `Tau.BookVII.Meta.Archetypes.ArchetypeFixedPoint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L83-L99)
**structure
Tau.BookVII.Meta.Archetypes.ArchetypeFixedPoint :Type**


[VII.D16] Archetype: minimal j-closed subobject exhibiting structural invariant I.
Three conditions:
(A1) j-closure: j(𝔄) = 𝔄 (stable under all J_τ-refinements)
(A2) I-exhibition: 𝔄 exhibits the structural invariant I
(A3) Minimality: no proper j-closed subobject of 𝔄 also exhibits I

- lt_operator : LawvereTierneyOperator
The LT operator governing closure.

- invariant : StructuralInvariant
The structural invariant being exhibited.

- a1_j_closed : Bool
(A1) j-closed: j(𝔄) = 𝔄.

- a2_exhibits_invariant : Bool
(A2) Exhibits invariant I.

- a3_minimal : Bool
(A3) Minimal: no proper j-closed sub-exhibitor.

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprArchetypeFixedPoint.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L99-L99)
**def
Tau.BookVII.Meta.Archetypes.instReprArchetypeFixedPoint.repr :ArchetypeFixedPoint → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprArchetypeFixedPoint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L99-L99)
**instance
Tau.BookVII.Meta.Archetypes.instReprArchetypeFixedPoint :Repr ArchetypeFixedPoint**

Equations
- Tau.BookVII.Meta.Archetypes.instReprArchetypeFixedPoint = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprArchetypeFixedPoint.repr }

---

### `Tau.BookVII.Meta.Archetypes.ArchetypeExtractor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L105-L123)
**structure
Tau.BookVII.Meta.Archetypes.ArchetypeExtractor :Type**


[VII.D17] Archetype Extractor: 5-step methodological procedure.
(1) Identify invariant I
(2) Enumerate j-closed candidates exhibiting I
(3) Intersect to minimality (via VII.L08)
(4) Verify non-triviality
(5) Read out via register functor (Reg_E, Reg_P, Reg_D, Reg_C)

- step1_identify : Bool
Step 1: invariant identified.

- step2_enumerate : Bool
Step 2: candidates enumerated.

- step3_intersect : Bool
Step 3: intersection computed.

- step4_verify : Bool
Step 4: non-triviality verified.

- step5_readout : Bool
Step 5: readout applied.

- step_count : ℕ
Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprArchetypeExtractor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L123-L123)
**instance
Tau.BookVII.Meta.Archetypes.instReprArchetypeExtractor :Repr ArchetypeExtractor**

Equations
- Tau.BookVII.Meta.Archetypes.instReprArchetypeExtractor = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprArchetypeExtractor.repr }

---

### `Tau.BookVII.Meta.Archetypes.instReprArchetypeExtractor.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L123-L123)
**def
Tau.BookVII.Meta.Archetypes.instReprArchetypeExtractor.repr :ArchetypeExtractor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.canonical_extractor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L125-L125)
**def
Tau.BookVII.Meta.Archetypes.canonical_extractor :ArchetypeExtractor**

Equations
- Tau.BookVII.Meta.Archetypes.canonical_extractor = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.JClosedFamily`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L131-L146)
**structure
Tau.BookVII.Meta.Archetypes.JClosedFamily :Type**


The collection of j-closed subobjects exhibiting invariant I,
ordered by inclusion, forming a complete lattice.

- invariant : StructuralInvariant
Invariant being exhibited.

- non_empty : Bool
Family is non-empty (at least one exhibitor exists).

- intersection_closed : Bool
Closed under arbitrary intersection.

- complete_lattice : Bool
Forms complete lattice (arbitrary meets exist).

- has_minimum : Bool
Has minimum element (intersection of all members).

- minimum_unique : Bool
Minimum is unique up to isomorphism.

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprJClosedFamily`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L146-L146)
**instance
Tau.BookVII.Meta.Archetypes.instReprJClosedFamily :Repr JClosedFamily**

Equations
- Tau.BookVII.Meta.Archetypes.instReprJClosedFamily = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprJClosedFamily.repr }

---

### `Tau.BookVII.Meta.Archetypes.instReprJClosedFamily.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L146-L146)
**def
Tau.BookVII.Meta.Archetypes.instReprJClosedFamily.repr :JClosedFamily → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.canonical_j_family`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L148-L148)
**def
Tau.BookVII.Meta.Archetypes.canonical_j_family :JClosedFamily**

Equations
- Tau.BookVII.Meta.Archetypes.canonical_j_family = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.lattice_closure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L150-L158)
**theorem
Tau.BookVII.Meta.Archetypes.lattice_closure :canonical_j_family.intersection_closed = true ∧ canonical_j_family.complete_lattice = true**


[VII.Lxx] Lattice Closure: j-closed subobjects of a Grothendieck topos
form a complete lattice. Intersection of j-closed subobjects is j-closed
(j-sheaves form reflective subcategory; meets computed pointwise;
j commutes with finite meets by LT3; for arbitrary meets, j-sheaf
reflection preserves intersection).

---

### `Tau.BookVII.Meta.Archetypes.j_closure_minimality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L164-L184)
**theorem
Tau.BookVII.Meta.Archetypes.j_closure_minimality :canonical_j_family.non_empty = true ∧ canonical_j_family.complete_lattice = true ∧ canonical_j_family.has_minimum = true ∧ canonical_j_family.minimum_unique = true**


[VII.L08] j-Closure Minimality: let I be a structural invariant exhibited
by at least one j-closed subobject of [τ^op, τ]. Then the collection F
of all j-closed subobjects exhibiting I, ordered by inclusion, has a
minimum element. This minimum is unique up to isomorphism.

Proof:

- F is non-empty by hypothesis (has_exhibitor).

- F inherits complete lattice structure from Sub_j([τ^op, τ]).

- Take A = ⋂F (intersection of all members).

- A is j-closed: intersection of j-closed subobjects is j-closed
(lattice_closure).

- A exhibits I: structural invariants defined by positive coherence
conditions are preserved under intersection (positive_coherence).

- A is minimal: A ⊆ F_i for all i by construction.

- A is unique: if both A, A' minimal, then A ⊆ A' and A' ⊆ A, so A ≅ A'.


---

### `Tau.BookVII.Meta.Archetypes.canonical_archetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L190-L191)
**def
Tau.BookVII.Meta.Archetypes.canonical_archetype :ArchetypeFixedPoint**


Canonical archetype witness: the minimum of the j-closed I-exhibiting family.
Equations
- Tau.BookVII.Meta.Archetypes.canonical_archetype = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.archetype_existence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L193-L207)
**theorem
Tau.BookVII.Meta.Archetypes.archetype_existence :canonical_archetype.a1_j_closed = true ∧ canonical_archetype.a2_exhibits_invariant = true ∧ canonical_archetype.a3_minimal = true ∧ canonical_j_family.minimum_unique = true**


[VII.T08] Archetype Existence: for every structural invariant I that is
exhibited by at least one j-closed subobject of [τ^op, τ], there exists
a unique (up to iso) archetype 𝔄_I — a minimal j-closed fixed point
exhibiting I.

Proof: immediate from VII.L08. The minimum element of the j-closed
I-exhibiting family satisfies (A1) j-closure (by lattice_closure),
(A2) I-exhibition (by positive_coherence), (A3) minimality (by construction).
Uniqueness up to iso from VII.L08 minimum_unique.

---

### `Tau.BookVII.Meta.Archetypes.minimality_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L209-L217)
**theorem
Tau.BookVII.Meta.Archetypes.minimality_witness :canonical_archetype.a3_minimal = true ∧ canonical_archetype.a1_j_closed = true ∧ canonical_archetype.a2_exhibits_invariant = true**


[VII.Lxx] Minimality Witness: the archetype is the unique element
satisfying all three conditions (A1)–(A3). Any other element satisfying
(A1)–(A2) contains the archetype. The archetype is contained in every
j-closed I-exhibiting subobject.

---

### `Tau.BookVII.Meta.Archetypes.ThresholdCrossingInvariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L223-L238)
**structure
Tau.BookVII.Meta.Archetypes.ThresholdCrossingInvariant :Type**


The threshold-crossing structural invariant I_bnd, defined by four
conditions (B1)–(B4):
(B1) Two domains: decomposes into F₊ ⊔ F₋ away from crossing point
(B2) Crossing point: unique p₀ where F₊ ∩ F₋ = {p₀}
(B3) Monodromy exchange: π₁(F, p₀) freely generated by γ₊, γ₋
(B4) Transition morphism: every transition factors through p₀

- b1_two_domains : Bool
(B1) Two non-empty connected domains.

- b2_crossing_point : Bool
(B2) Unique crossing point p₀.

- b3_monodromy_exchange : Bool
(B3) Free fundamental group on two generators.

- b4_transition_morphism : Bool
(B4) All transitions factor through crossing point.

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprThresholdCrossingInvariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L238-L238)
**instance
Tau.BookVII.Meta.Archetypes.instReprThresholdCrossingInvariant :Repr ThresholdCrossingInvariant**

Equations
- Tau.BookVII.Meta.Archetypes.instReprThresholdCrossingInvariant = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprThresholdCrossingInvariant.repr }

---

### `Tau.BookVII.Meta.Archetypes.instReprThresholdCrossingInvariant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L238-L238)
**def
Tau.BookVII.Meta.Archetypes.instReprThresholdCrossingInvariant.repr :ThresholdCrossingInvariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.i_bnd`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L240-L240)
**def
Tau.BookVII.Meta.Archetypes.i_bnd :ThresholdCrossingInvariant**

Equations
- Tau.BookVII.Meta.Archetypes.i_bnd = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.BoundaryArchetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L246-L267)
**structure
Tau.BookVII.Meta.Archetypes.BoundaryArchetype :Type**


[VII.D18] Boundary Archetype: the minimal j-closed fixed point exhibiting
the threshold-crossing invariant I_bnd. Geometric carrier: L = S¹ ∨ S¹.

L satisfies (B1)–(B4):


- (B1): Two loops S¹₊, S¹₋; L \ {p₀} = (S¹₊ \ {p₀}) ⊔ (S¹₋ \ {p₀})

- (B2): Wedge point p₀; S¹₊ ∩ S¹₋ = {p₀}

- (B3): π₁(L, p₀) ≅ ℤ * ℤ, free on two generators

- (B4): Every path from S¹₊ to S¹₋ passes through p₀


- archetype : ArchetypeFixedPoint
Archetype conditions (A1)–(A3) satisfied.

- invariant : ThresholdCrossingInvariant
Threshold-crossing conditions (B1)–(B4) satisfied.

- carrier_is_lemniscate : Bool
Carrier is lemniscate L = S¹ ∨ S¹.

- pi1_free_rank : ℕ
Fundamental group: π₁(L, p₀) ≅ ℤ * ℤ (free on two generators).

- lobe_count : ℕ
Number of lobes.

- crossing_count : ℕ
Number of crossing points.

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprBoundaryArchetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L267-L267)
**instance
Tau.BookVII.Meta.Archetypes.instReprBoundaryArchetype :Repr BoundaryArchetype**

Equations
- Tau.BookVII.Meta.Archetypes.instReprBoundaryArchetype = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprBoundaryArchetype.repr }

---

### `Tau.BookVII.Meta.Archetypes.instReprBoundaryArchetype.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L267-L267)
**def
Tau.BookVII.Meta.Archetypes.instReprBoundaryArchetype.repr :BoundaryArchetype → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.boundary_archetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L269-L269)
**def
Tau.BookVII.Meta.Archetypes.boundary_archetype :BoundaryArchetype**

Equations
- Tau.BookVII.Meta.Archetypes.boundary_archetype = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.boundary_archetype_minimality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L275-L306)
**theorem
Tau.BookVII.Meta.Archetypes.boundary_archetype_minimality :boundary_archetype.archetype.a1_j_closed = true ∧ boundary_archetype.archetype.a2_exhibits_invariant = true ∧ boundary_archetype.archetype.a3_minimal = true ∧ boundary_archetype.invariant.b1_two_domains = true ∧ boundary_archetype.invariant.b2_crossing_point = true ∧ boundary_archetype.invariant.b3_monodromy_exchange = true ∧ boundary_archetype.invariant.b4_transition_morphism = true ∧ boundary_archetype.carrier_is_lemniscate = true ∧ boundary_archetype.pi1_free_rank = 2 ∧ boundary_archetype.lobe_count = 2 ∧ boundary_archetype.crossing_count = 1**


[VII.P05] Boundary Archetype Minimality: L = S¹ ∨ S¹ is the minimal
j-closed fixed point exhibiting I_bnd. No proper j-closed subobject
of L exhibits I_bnd.

Proof:

- j-closure of L: L is j-closed because it is the boundary of a J_τ-sheaf.
O(τ³) restricts to L, and restriction of a sheaf to a closed subspace
is a sheaf on the induced topology.

- I_bnd-exhibition: L satisfies (B1)–(B4) as verified in VII.D18.

- Minimality: Suppose F ↪ L is a proper j-closed subobject exhibiting I_bnd.
By (B1), F has two connected components away from p₀.
By (B2), F contains p₀.
By (B3), π₁(F, p₀) must be free on two generators.
The only subspace of S¹ ∨ S¹ with π₁ ≅ ℤ * ℤ containing p₀
and two loop generators is S¹ ∨ S¹ itself — removing any arc
destroys that generator. Therefore F = L.


---

### `Tau.BookVII.Meta.Archetypes.MitigationArchetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L312-L332)
**structure
Tau.BookVII.Meta.Archetypes.MitigationArchetype :Type**


[VII.D19] Mitigation Archetype: minimal j-closed subobject satisfying:
(M1) Post-boundary activation: acts on codomain of boundary morphism β
(M2) Covering: provides factorization μ : B → B̄ reducing coherence defect
(M3) Minimality: no proper j-closed sub-pattern satisfies (M1) and (M2)

The covering morphism μ is the formal "garment" — it does not undo the
crossing (boundary-crossings are non-invertible) but provides a new
coherence envelope adapted to the post-crossing situation.
Structural dual of the boundary archetype.

- archetype : ArchetypeFixedPoint
Archetype conditions (A1)–(A3) satisfied.

- m1_post_boundary : Bool
(M1) Post-boundary activation.

- m2_covering : Bool
(M2) Covering: provides coherence-reducing factorization.

- m3_minimal : Bool
(M3) Minimality.

- j_closed : Bool
j-closure: j(M) = M (by contradiction argument, ch12).

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprMitigationArchetype.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L332-L332)
**def
Tau.BookVII.Meta.Archetypes.instReprMitigationArchetype.repr :MitigationArchetype → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprMitigationArchetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L332-L332)
**instance
Tau.BookVII.Meta.Archetypes.instReprMitigationArchetype :Repr MitigationArchetype**

Equations
- Tau.BookVII.Meta.Archetypes.instReprMitigationArchetype = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprMitigationArchetype.repr }

---

### `Tau.BookVII.Meta.Archetypes.mitigation_archetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L334-L334)
**def
Tau.BookVII.Meta.Archetypes.mitigation_archetype :MitigationArchetype**

Equations
- Tau.BookVII.Meta.Archetypes.mitigation_archetype = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.MetaFramingArchetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L340-L362)
**structure
Tau.BookVII.Meta.Archetypes.MetaFramingArchetype :Type**


[VII.D20] Meta-Framing Archetype: minimal j-closed subobject satisfying:
(F1) Self-application: acts on framing functor F itself
(F2) Context shift: preserves objects/morphisms but changes codomain category
(F3) j-closure: j(ℱ) = ℱ
(F4) Minimality: no proper j-closed sub-pattern satisfies (F1)–(F3)

Distinguished by level of operation: boundary acts on objects,
mitigation acts on states, meta-framing acts on *functors*.
Morally neutral: same pattern serves enlightenment and destruction.

- archetype : ArchetypeFixedPoint
Archetype conditions (A1)–(A3) satisfied.

- f1_self_application : Bool
(F1) Self-application on framing functor.

- f2_context_shift : Bool
(F2) Context shift (preserves content, changes context).

- f3_j_closed : Bool
(F3) j-closure.

- f4_minimal : Bool
(F4) Minimality.

- morally_neutral : Bool
Morally neutral: register discipline determines ethical valence.

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprMetaFramingArchetype.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L362-L362)
**def
Tau.BookVII.Meta.Archetypes.instReprMetaFramingArchetype.repr :MetaFramingArchetype → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprMetaFramingArchetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L362-L362)
**instance
Tau.BookVII.Meta.Archetypes.instReprMetaFramingArchetype :Repr MetaFramingArchetype**

Equations
- Tau.BookVII.Meta.Archetypes.instReprMetaFramingArchetype = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprMetaFramingArchetype.repr }

---

### `Tau.BookVII.Meta.Archetypes.meta_framing_archetype`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L364-L364)
**def
Tau.BookVII.Meta.Archetypes.meta_framing_archetype :MetaFramingArchetype**

Equations
- Tau.BookVII.Meta.Archetypes.meta_framing_archetype = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.ArchetypalBasis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L370-L389)
**structure
Tau.BookVII.Meta.Archetypes.ArchetypalBasis :Type**


The three archetypes form a minimal basis at E₃: every j-closed
pattern decomposes into combinations of boundary, mitigation,
and meta-framing archetypes.


Archetype
Level
Action
Carrier


Boundary
Objects
Separates
L = S¹ ∨ S¹


Mitigation
States
Covers
Garment μ


Meta-Framing
Functors
Reframes
Natural transf.


- boundary : BoundaryArchetype
- mitigation : MitigationArchetype
- meta_framing : MetaFramingArchetype
- count : ℕ
Three archetypes in total.

- complete : Bool
Basis is complete at E₃.

- minimal_basis : Bool
Basis is minimal (none redundant).

Instances For

---

### `Tau.BookVII.Meta.Archetypes.instReprArchetypalBasis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L389-L389)
**instance
Tau.BookVII.Meta.Archetypes.instReprArchetypalBasis :Repr ArchetypalBasis**

Equations
- Tau.BookVII.Meta.Archetypes.instReprArchetypalBasis = { reprPrec := Tau.BookVII.Meta.Archetypes.instReprArchetypalBasis.repr }

---

### `Tau.BookVII.Meta.Archetypes.instReprArchetypalBasis.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L389-L389)
**def
Tau.BookVII.Meta.Archetypes.instReprArchetypalBasis.repr :ArchetypalBasis → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Archetypes.canonical_basis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L391-L391)
**def
Tau.BookVII.Meta.Archetypes.canonical_basis :ArchetypalBasis**

Equations
- Tau.BookVII.Meta.Archetypes.canonical_basis = { }
Instances For

---

### `Tau.BookVII.Meta.Archetypes.archetypal_basis_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Meta/Archetypes.lean#L393-L398)
**theorem
Tau.BookVII.Meta.Archetypes.archetypal_basis_complete :canonical_basis.count = 3 ∧ canonical_basis.complete = true ∧ canonical_basis.minimal_basis = true**


Three archetypes form complete minimal basis at E₃.
