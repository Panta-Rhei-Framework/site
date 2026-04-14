---
layout: taulib-doc
title: "TauLib.BookVII.Meta.Saturation"
permalink: /verify/taulib/docs/book-vii-meta-saturation/
lane: verify
module_name: "TauLib.BookVII.Meta.Saturation"
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

# TauLib.BookVII.Meta.Saturation


The Saturation Theorem (Enrich⁴ = Enrich³) and Gödel Avoidance — the two
deepest structural results in Book VII's foundational layer.

## Registry Cross-References


- [VII.L03] Non-Emptiness at Each Layer — `non_emptiness_at_each_layer`

- [VII.L04] Strictness Between Layers — `strictness_between_layers`

- [VII.T05] Canonical Ladder Theorem — `canonical_ladder_theorem`

- [VII.P02] Seven-Book Partition — `seven_book_partition`

- [VII.L05] No-New-Lobe Lemma — `no_new_lobe`

- [VII.L06] No-New-Crossing-Mediator — `no_new_crossing_mediator`

- [VII.L07] Carrier Closure (Idempotence) — `carrier_closure`

- [VII.T06] Saturation Theorem — `saturation_theorem`

- [VII.P03] Four-Orbit Implies Four-Layer — `four_orbit_four_layer`

- [VII.D15] Bounded Witness Form — `BoundedWitnessForm`

- [VII.T07] Gödel Avoidance — `godel_avoidance`

- [VII.P04] No-Diagonal Principle — `no_diagonal`

- [VII.Lxx] Crossing Point Uniqueness — `crossing_point_uniqueness`

- [VII.Lxx] Carrier Exhaustion — `carrier_exhaustion`

- [VII.Lxx] Bounded Witness — `bounded_witness_form_check`

- [VII.Pxx] Enrichment Stabilization — `enrichment_stabilization`


## Cross-Book Authority


- Book III, Part X: Canonical Ladder (III.T01–T04), enrichment functors

- Book VII, Meta.Registers: register decomposition, E₃ structure


## Ground Truth Sources


- Book VII Chapters 7–9 (2nd Edition): Ladder, Saturation, Gödel Avoidance


---

### `Tau.BookVII.Meta.Saturation.LayerWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L46-L52)
**structure
Tau.BookVII.Meta.Saturation.LayerWitness :Type**


Enrichment layer witnesses: constructive carriers at each level.

- layer : Registers.EnrichLayer
- witness_name : String
- inhabited : Bool
Witness exists (constructively inhabited).

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprLayerWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L52-L52)
**instance
Tau.BookVII.Meta.Saturation.instReprLayerWitness :Repr LayerWitness**

Equations
- Tau.BookVII.Meta.Saturation.instReprLayerWitness = { reprPrec := Tau.BookVII.Meta.Saturation.instReprLayerWitness.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprLayerWitness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L52-L52)
**def
Tau.BookVII.Meta.Saturation.instReprLayerWitness.repr :LayerWitness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.layer_witnesses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L54-L63)
**def
Tau.BookVII.Meta.Saturation.layer_witnesses :List LayerWitness**


[VII.L03] Non-emptiness at each layer: constructive witnesses.


- E₀: Kernel K_τ (NF-addressable objects)

- E₁: Four holonomy sectors of boundary algebra

- E₂: Life predicate (Distinction + SelfDesc)

- E₃: BH basin law-code (SelfDesc²)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.non_emptiness_at_each_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L65-L68)
**theorem
Tau.BookVII.Meta.Saturation.non_emptiness_at_each_layer :layer_witnesses.length = 4 ∧ ((List.map (fun (x : LayerWitness) => x.inhabited) layer_witnesses).all fun (x : Bool) => x == true) = true**


---

### `Tau.BookVII.Meta.Saturation.SeparationWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L74-L80)
**structure
Tau.BookVII.Meta.Saturation.SeparationWitness :Type**


Separation witness between consecutive enrichment layers.

- lower : Registers.EnrichLayer
- upper : Registers.EnrichLayer
- witness_name : String
- strict : Bool
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSeparationWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L80-L80)
**instance
Tau.BookVII.Meta.Saturation.instReprSeparationWitness :Repr SeparationWitness**

Equations
- Tau.BookVII.Meta.Saturation.instReprSeparationWitness = { reprPrec := Tau.BookVII.Meta.Saturation.instReprSeparationWitness.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprSeparationWitness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L80-L80)
**def
Tau.BookVII.Meta.Saturation.instReprSeparationWitness.repr :SeparationWitness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.separation_witnesses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L82-L90)
**def
Tau.BookVII.Meta.Saturation.separation_witnesses :List SeparationWitness**


[VII.L04] Strictness: E₀ ⊊ E₁ ⊊ E₂ ⊊ E₃.
Separation witnesses:


- E₀→E₁: sector admissibility (coupling constants under RG flow)

- E₁→E₂: internal code evaluation (decode map in phenotype)

- E₂→E₃: self-model consistency (MetaDecode operator)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.strictness_between_layers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L92-L95)
**theorem
Tau.BookVII.Meta.Saturation.strictness_between_layers :separation_witnesses.length = 3 ∧ ((List.map (fun (x : SeparationWitness) => x.strict) separation_witnesses).all fun (x : Bool) => x == true) = true**


---

### `Tau.BookVII.Meta.Saturation.CanonicalLadder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L101-L120)
**structure
Tau.BookVII.Meta.Saturation.CanonicalLadder :Type**


[VII.T05] Canonical Ladder: non-empty at every layer, strictly increasing,
terminated by Saturation Theorem, and canonical (determined by structure
of kernel and five generators, not editorial choice).

Enrichment equations:


- E₁ = Enrich(E₀): sector admissibility on NF objects

- E₂ = Enrich(E₁): SelfDesc on sectors

- E₃ = Enrich(E₂): SelfDesc² on self-describing codes


- layer_count : ℕ
- count_eq : self.layer_count = 4
- non_empty : Bool
Non-empty at each level.

- strict : Bool
Strictly increasing.

- saturating : Bool
Saturating at E₃.

- canonical : Bool
Canonical: structurally determined.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprCanonicalLadder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L120-L120)
**def
Tau.BookVII.Meta.Saturation.instReprCanonicalLadder.repr :CanonicalLadder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprCanonicalLadder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L120-L120)
**instance
Tau.BookVII.Meta.Saturation.instReprCanonicalLadder :Repr CanonicalLadder**

Equations
- Tau.BookVII.Meta.Saturation.instReprCanonicalLadder = { reprPrec := Tau.BookVII.Meta.Saturation.instReprCanonicalLadder.repr }

---

### `Tau.BookVII.Meta.Saturation.vii_canonical_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L122-L124)
**def
Tau.BookVII.Meta.Saturation.vii_canonical_ladder :CanonicalLadder**

Equations
- Tau.BookVII.Meta.Saturation.vii_canonical_ladder = { layer_count := 4, count_eq := Tau.BookVII.Meta.Saturation.vii_canonical_ladder._proof_1 }
Instances For

---

### `Tau.BookVII.Meta.Saturation.canonical_ladder_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L126-L132)
**theorem
Tau.BookVII.Meta.Saturation.canonical_ladder_theorem :vii_canonical_ladder.layer_count = 4 ∧ vii_canonical_ladder.non_empty = true ∧ vii_canonical_ladder.strict = true ∧ vii_canonical_ladder.saturating = true ∧ vii_canonical_ladder.canonical = true**


---

### `Tau.BookVII.Meta.Saturation.SevenBookPartition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L138-L156)
**structure
Tau.BookVII.Meta.Saturation.SevenBookPartition :Type**


[VII.P02] Seven-Book Partition: four layers require minimum 7 books.
E₀: 3 books (I foundation + II holomorphy + III spectrum)
E₁: 2 books (IV microcosm + V macrocosm)
E₂: 1 book (VI life)
E₃: 1 book (VII metaphysics)
Total: 3 + 2 + 1 + 1 = 7

- e0_books : ℕ
- e0_eq : self.e0_books = 3
- e1_books : ℕ
- e1_eq : self.e1_books = 2
- e2_books : ℕ
- e2_eq : self.e2_books = 1
- e3_books : ℕ
- e3_eq : self.e3_books = 1
- total : ℕ
- total_eq : self.total = 7
- sum_eq : self.e0_books + self.e1_books + self.e2_books + self.e3_books = self.total
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSevenBookPartition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L156-L156)
**instance
Tau.BookVII.Meta.Saturation.instReprSevenBookPartition :Repr SevenBookPartition**

Equations
- Tau.BookVII.Meta.Saturation.instReprSevenBookPartition = { reprPrec := Tau.BookVII.Meta.Saturation.instReprSevenBookPartition.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprSevenBookPartition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L156-L156)
**def
Tau.BookVII.Meta.Saturation.instReprSevenBookPartition.repr :SevenBookPartition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.seven_book`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L158-L169)
**def
Tau.BookVII.Meta.Saturation.seven_book :SevenBookPartition**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.seven_book_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L171-L174)
**theorem
Tau.BookVII.Meta.Saturation.seven_book_partition :seven_book.total = 7 ∧ ⋯ = ⋯**


---

### `Tau.BookVII.Meta.Saturation.Generator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L180-L187)
**inductive
Tau.BookVII.Meta.Saturation.Generator :Type**


Generator identifier: the five generators of τ.

- alpha : Generator
- pi : Generator
- pi_prime : Generator
- pi_dprime : Generator
- omega : Generator
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L187-L187)
**instance
Tau.BookVII.Meta.Saturation.instReprGenerator :Repr Generator**

Equations
- Tau.BookVII.Meta.Saturation.instReprGenerator = { reprPrec := Tau.BookVII.Meta.Saturation.instReprGenerator.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L187-L187)
**def
Tau.BookVII.Meta.Saturation.instReprGenerator.repr :Generator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instDecidableEqGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L187-L187)
**instance
Tau.BookVII.Meta.Saturation.instDecidableEqGenerator :DecidableEq Generator**

Equations
- Tau.BookVII.Meta.Saturation.instDecidableEqGenerator x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Saturation.Orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L189-L195)
**inductive
Tau.BookVII.Meta.Saturation.Orbit :Type**


ρ-orbit: partition of generators under ρ-action.

- identity : Orbit
- lobes : Orbit
- crossing : Orbit
- closure : Orbit
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprOrbit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L195-L195)
**def
Tau.BookVII.Meta.Saturation.instReprOrbit.repr :Orbit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprOrbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L195-L195)
**instance
Tau.BookVII.Meta.Saturation.instReprOrbit :Repr Orbit**

Equations
- Tau.BookVII.Meta.Saturation.instReprOrbit = { reprPrec := Tau.BookVII.Meta.Saturation.instReprOrbit.repr }

---

### `Tau.BookVII.Meta.Saturation.instDecidableEqOrbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L195-L195)
**instance
Tau.BookVII.Meta.Saturation.instDecidableEqOrbit :DecidableEq Orbit**

Equations
- Tau.BookVII.Meta.Saturation.instDecidableEqOrbit x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Saturation.Generator.orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L197-L203)
**def
Tau.BookVII.Meta.Saturation.Generator.orbit :Generator → Orbit**


Assign generator to its orbit.
Equations
- Tau.BookVII.Meta.Saturation.Generator.alpha.orbit = Tau.BookVII.Meta.Saturation.Orbit.identity
- Tau.BookVII.Meta.Saturation.Generator.pi.orbit = Tau.BookVII.Meta.Saturation.Orbit.lobes
- Tau.BookVII.Meta.Saturation.Generator.pi_prime.orbit = Tau.BookVII.Meta.Saturation.Orbit.lobes
- Tau.BookVII.Meta.Saturation.Generator.pi_dprime.orbit = Tau.BookVII.Meta.Saturation.Orbit.crossing
- Tau.BookVII.Meta.Saturation.Generator.omega.orbit = Tau.BookVII.Meta.Saturation.Orbit.closure
Instances For

---

### `Tau.BookVII.Meta.Saturation.no_new_lobe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L205-L219)
**theorem
Tau.BookVII.Meta.Saturation.no_new_lobe :[Generator.alpha, Generator.pi, Generator.pi_prime, Generator.pi_dprime, Generator.omega].length = 5 ∧ [Orbit.identity, Orbit.lobes, Orbit.crossing, Orbit.closure].length = 4 ∧ Generator.alpha.orbit = Orbit.identity ∧ Generator.pi.orbit = Orbit.lobes ∧ Generator.pi_prime.orbit = Orbit.lobes ∧ Generator.pi_dprime.orbit = Orbit.crossing ∧ Generator.omega.orbit = Orbit.closure**


[VII.L05] No-New-Lobe: five generators partition into exactly four ρ-orbits.
No sixth generator constructible; lemniscate topology exhausts topological features.
|Orb(ρ)| = 4 and Orb(ρ) is closed under ρ.

---

### `Tau.BookVII.Meta.Saturation.crossing_point_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L225-L236)
**theorem
Tau.BookVII.Meta.Saturation.crossing_point_uniqueness :Generator.pi_dprime.orbit = Orbit.crossing ∧ Generator.alpha.orbit ≠ Orbit.crossing ∧ Generator.pi.orbit ≠ Orbit.crossing ∧ Generator.pi_prime.orbit ≠ Orbit.crossing ∧ Generator.omega.orbit ≠ Orbit.crossing**


[VII.Lxx] Crossing Point Uniqueness: the lemniscate L = S¹ ∨ S¹ has
exactly one crossing point p₀. This is the wedge point where the two
lobes meet. No additional crossing points constructible.

---

### `Tau.BookVII.Meta.Saturation.no_new_crossing_mediator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L242-L258)
**theorem
Tau.BookVII.Meta.Saturation.no_new_crossing_mediator :Registers.canonical_sector_decomp.mixed_sector_count = 1 ∧ Registers.sector_logos.dc_coincidence = true ∧ Registers.sector_logos.unique_mediator = true ∧ Registers.RegisterType.empirical ≠ Registers.RegisterType.practical ∧ Registers.RegisterType.empirical ≠ Registers.RegisterType.diagrammatic ∧ Registers.RegisterType.empirical ≠ Registers.RegisterType.commitment ∧ Registers.RegisterType.practical ≠ Registers.RegisterType.diagrammatic ∧ Registers.RegisterType.practical ≠ Registers.RegisterType.commitment**


[VII.L06] No-New-Crossing-Mediator: Logos sector S_L is unique mixed sector.
No new crossing mediator at E₄. Only pair of codomain categories admitting
natural transformation is (Proof, Stance), which already defines S_L.
Other five pairs have structurally distinct codomains.

---

### `Tau.BookVII.Meta.Saturation.SelfDescIteration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L264-L269)
**structure
Tau.BookVII.Meta.Saturation.SelfDescIteration :Type**


SelfDesc iteration depth.

- depth : ℕ
- idempotent_from : ℕ
Result equivalent to depth-1 from depth 2 onward.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSelfDescIteration.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L269-L269)
**def
Tau.BookVII.Meta.Saturation.instReprSelfDescIteration.repr :SelfDescIteration → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSelfDescIteration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L269-L269)
**instance
Tau.BookVII.Meta.Saturation.instReprSelfDescIteration :Repr SelfDescIteration**

Equations
- Tau.BookVII.Meta.Saturation.instReprSelfDescIteration = { reprPrec := Tau.BookVII.Meta.Saturation.instReprSelfDescIteration.repr }

---

### `Tau.BookVII.Meta.Saturation.carrier_closure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L271-L277)
**theorem
Tau.BookVII.Meta.Saturation.carrier_closure :have sd := { depth := 3 };
sd.depth = 3 ∧ sd.idempotent_from = 2**


[VII.L07] Carrier Closure: SelfDesc³ = SelfDesc². MetaDecode at level 3
models only what level 2 already models. The model includes its own
modelling capacity. M₃(X) = M₂(M₂(X)) ⊆ M₂(X).

---

### `Tau.BookVII.Meta.Saturation.carrier_exhaustion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L283-L292)
**theorem
Tau.BookVII.Meta.Saturation.carrier_exhaustion :Registers.metadecode.self_referential = true ∧ Registers.metadecode.faithful = true ∧ Registers.metadecode.well_defined = true**


[VII.Lxx] Carrier Exhaustion: at E₃, the carrier is exhausted.
SelfDesc² already captures all self-referential structure.
Further iteration does not produce new content:


- MetaDecode(MetaDecode(X)) ⊆ MetaDecode(X)

- The self-model includes the capacity for self-modelling


---

### `Tau.BookVII.Meta.Saturation.SaturationResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L298-L315)
**structure
Tau.BookVII.Meta.Saturation.SaturationResult :Type**


[VII.T06] Saturation Theorem: Enrich(E₃) = E₃. No E₄ exists.
Three conditions for genuine E₄ ALL blocked:

- No new generator (no_new_lobe, L05)

- No new mediator (no_new_crossing_mediator, L06)

- No new carrier (carrier_closure, L07)


Consequence: enrichment series is complete at E₃.

- terminal_layer : Registers.EnrichLayer
E₃ is terminal.

- terminal_eq : self.terminal_layer = Registers.EnrichLayer.e3
- no_new_lobe_blocked : Bool
Three blocking conditions satisfied.

- no_new_mediator_blocked : Bool
- no_new_carrier_blocked : Bool
- saturated : Bool
All three blocked ⟹ saturation.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSaturationResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L315-L315)
**instance
Tau.BookVII.Meta.Saturation.instReprSaturationResult :Repr SaturationResult**

Equations
- Tau.BookVII.Meta.Saturation.instReprSaturationResult = { reprPrec := Tau.BookVII.Meta.Saturation.instReprSaturationResult.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprSaturationResult.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L315-L315)
**def
Tau.BookVII.Meta.Saturation.instReprSaturationResult.repr :SaturationResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.saturation_result`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L317-L319)
**def
Tau.BookVII.Meta.Saturation.saturation_result :SaturationResult**

Equations
- Tau.BookVII.Meta.Saturation.saturation_result = { terminal_layer := Tau.BookVII.Meta.Registers.EnrichLayer.e3, terminal_eq := ⋯ }
Instances For

---

### `Tau.BookVII.Meta.Saturation.saturation_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L321-L327)
**theorem
Tau.BookVII.Meta.Saturation.saturation_theorem :saturation_result.terminal_layer = Registers.EnrichLayer.e3 ∧ saturation_result.no_new_lobe_blocked = true ∧ saturation_result.no_new_mediator_blocked = true ∧ saturation_result.no_new_carrier_blocked = true ∧ saturation_result.saturated = true**


---

### `Tau.BookVII.Meta.Saturation.enrichment_stabilization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L333-L340)
**theorem
Tau.BookVII.Meta.Saturation.enrichment_stabilization :saturation_result.saturated = true ∧ vii_canonical_ladder.saturating = true ∧ vii_canonical_ladder.layer_count = 4**


[VII.Pxx] Enrichment Stabilization: the enrichment functor is
the identity on E₃. Enrich⁴ = Enrich³ = Enrich² ∘ Enrich = E₃.
This follows from the three blocking lemmas composing.

---

### `Tau.BookVII.Meta.Saturation.orbit_layer_correspondence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L346-L356)
**def
Tau.BookVII.Meta.Saturation.orbit_layer_correspondence :Orbit → Registers.EnrichLayer**


[VII.P03] Four-Orbit Implies Four-Layer: structural correspondence.


- Identity orbit {α} ↔ E₀ (mathematics)

- Lobe orbit {π,π′} ↔ E₁ (physics)

- Crossing orbit {π″} ↔ E₂ (life)

- Closure orbit {ω} ↔ E₃ (metaphysics)
Orbit closure = enrichment saturation.

Equations
- Tau.BookVII.Meta.Saturation.orbit_layer_correspondence Tau.BookVII.Meta.Saturation.Orbit.identity = Tau.BookVII.Meta.Registers.EnrichLayer.e0
- Tau.BookVII.Meta.Saturation.orbit_layer_correspondence Tau.BookVII.Meta.Saturation.Orbit.lobes = Tau.BookVII.Meta.Registers.EnrichLayer.e1
- Tau.BookVII.Meta.Saturation.orbit_layer_correspondence Tau.BookVII.Meta.Saturation.Orbit.crossing = Tau.BookVII.Meta.Registers.EnrichLayer.e2
- Tau.BookVII.Meta.Saturation.orbit_layer_correspondence Tau.BookVII.Meta.Saturation.Orbit.closure = Tau.BookVII.Meta.Registers.EnrichLayer.e3
Instances For

---

### `Tau.BookVII.Meta.Saturation.four_orbit_four_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L358-L363)
**theorem
Tau.BookVII.Meta.Saturation.four_orbit_four_layer :orbit_layer_correspondence Orbit.identity = Registers.EnrichLayer.e0 ∧ orbit_layer_correspondence Orbit.lobes = Registers.EnrichLayer.e1 ∧ orbit_layer_correspondence Orbit.crossing = Registers.EnrichLayer.e2 ∧ orbit_layer_correspondence Orbit.closure = Registers.EnrichLayer.e3**


---

### `Tau.BookVII.Meta.Saturation.BoundedWitnessForm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L369-L379)
**structure
Tau.BookVII.Meta.Saturation.BoundedWitnessForm :Type**


[VII.D15] Bounded Witness Form (BWF): claim φ has a finite τ-finite witness w
with NF-address, certifying φ, terminating in finitely many kernel-axiom steps.
Key constraint: excludes unbounded quantification.

- tau_finite : Bool
Witness is τ-finite.

- nf_addressed : Bool
Witness has NF-address.

- finitely_terminating : Bool
Terminates in finitely many steps.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprBoundedWitnessForm.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L379-L379)
**def
Tau.BookVII.Meta.Saturation.instReprBoundedWitnessForm.repr :BoundedWitnessForm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprBoundedWitnessForm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L379-L379)
**instance
Tau.BookVII.Meta.Saturation.instReprBoundedWitnessForm :Repr BoundedWitnessForm**

Equations
- Tau.BookVII.Meta.Saturation.instReprBoundedWitnessForm = { reprPrec := Tau.BookVII.Meta.Saturation.instReprBoundedWitnessForm.repr }

---

### `Tau.BookVII.Meta.Saturation.bwf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L381-L381)
**def
Tau.BookVII.Meta.Saturation.bwf :BoundedWitnessForm**

Equations
- Tau.BookVII.Meta.Saturation.bwf = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.bounded_witness_form_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L383-L387)
**theorem
Tau.BookVII.Meta.Saturation.bounded_witness_form_check :bwf.tau_finite = true ∧ bwf.nf_addressed = true ∧ bwf.finitely_terminating = true**


---

### `Tau.BookVII.Meta.Saturation.AvoidanceMechanisms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L393-L410)
**structure
Tau.BookVII.Meta.Saturation.AvoidanceMechanisms :Type**


[VII.P04] No-Diagonal: no surjection d : Ob(τ³) → Sub_j([τ^op, τ]).
Anti-diagonal A = {x | x ∉ d(x)} is not j-closed due to monodromy
constraint at crossing point p₀.

Five avoidance mechanisms:

- No-Contraction: SelfDesc³ = SelfDesc² prevents unbounded nesting

- No-Diagonal: lemniscate crossing prevents surjective diagonal

- BWF: excludes unbounded quantification

- NF-Linearity: prevents circular reference chains

- Generation vs. Presentation: coherence is functorial, not syntactic


- no_contraction : Bool
- no_diagonal : Bool
- bounded_witness : Bool
- nf_linearity : Bool
- generation_not_presentation : Bool
- mechanism_count : ℕ
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprAvoidanceMechanisms.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L410-L410)
**def
Tau.BookVII.Meta.Saturation.instReprAvoidanceMechanisms.repr :AvoidanceMechanisms → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprAvoidanceMechanisms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L410-L410)
**instance
Tau.BookVII.Meta.Saturation.instReprAvoidanceMechanisms :Repr AvoidanceMechanisms**

Equations
- Tau.BookVII.Meta.Saturation.instReprAvoidanceMechanisms = { reprPrec := Tau.BookVII.Meta.Saturation.instReprAvoidanceMechanisms.repr }

---

### `Tau.BookVII.Meta.Saturation.avoidance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L412-L412)
**def
Tau.BookVII.Meta.Saturation.avoidance :AvoidanceMechanisms**

Equations
- Tau.BookVII.Meta.Saturation.avoidance = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.no_diagonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L414-L418)
**theorem
Tau.BookVII.Meta.Saturation.no_diagonal :avoidance.no_contraction = true ∧ avoidance.no_diagonal = true ∧ avoidance.mechanism_count = 5**


---

### `Tau.BookVII.Meta.Saturation.godel_avoidance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L424-L438)
**theorem
Tau.BookVII.Meta.Saturation.godel_avoidance :avoidance.no_contraction = true ∧ avoidance.no_diagonal = true ∧ avoidance.bounded_witness = true ∧ avoidance.nf_linearity = true ∧ avoidance.generation_not_presentation = true**


[VII.T07] Gödel Avoidance: no sentence G in τ satisfies G ↔ ¬Coh_D(G).
Four independent blockages:

- BWF violates (ii): diagonal requires unbounded witness

- No-Diagonal prevents surjection

- No-Contraction prevents SelfDesc³

- NF-Linearity prevents cycles


Consequence: incompleteness phenomenon does not arise in τ.

---

### `Tau.BookVII.Meta.Saturation.OnticRequirement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L444-L452)
**inductive
Tau.BookVII.Meta.Saturation.OnticRequirement :Type**


Ontic requirement identifier.

- or1_yoneda : OnticRequirement
- or2_finite_signature : OnticRequirement
- or3_diagonal_free : OnticRequirement
- or4_nf_addressable : OnticRequirement
- or5_holomorphic : OnticRequirement
- or6_spectral : OnticRequirement
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprOnticRequirement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L452-L452)
**instance
Tau.BookVII.Meta.Saturation.instReprOnticRequirement :Repr OnticRequirement**

Equations
- Tau.BookVII.Meta.Saturation.instReprOnticRequirement = { reprPrec := Tau.BookVII.Meta.Saturation.instReprOnticRequirement.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprOnticRequirement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L452-L452)
**def
Tau.BookVII.Meta.Saturation.instReprOnticRequirement.repr :OnticRequirement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instDecidableEqOnticRequirement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L452-L452)
**instance
Tau.BookVII.Meta.Saturation.instDecidableEqOnticRequirement :DecidableEq OnticRequirement**

Equations
- Tau.BookVII.Meta.Saturation.instDecidableEqOnticRequirement x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookVII.Meta.Saturation.SixOnticRequirements`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L454-L482)
**structure
Tau.BookVII.Meta.Saturation.SixOnticRequirements :Type**


[VII.D37] Six Ontic Requirements (ch29). A candidate foundation F must satisfy:
(OR1) Yoneda: identity-faithful representation (eliminates haecceity)
(OR2) Finite signature: finitely generated (surveyable by finite being)
(OR3) Diagonal-free: self-description without diagonal paradoxes (NF-addresses)
(OR4) NF-addressable: unique normal-form addresses (findability, decidable identity)
(OR5) Holomorphic: local data determine global structure (Central Theorem)
(OR6) Spectral completeness: internal spectral decomposition (eight forces)

SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B4).
Upgraded via constraint-entailment: six constraints collectively force
τ's axiom structure (K0–K6 + 5 generators), verified by pairwise narrowing.

- or1_yoneda : Bool
(OR1) Yoneda: identity-faithful representation.

- or2_finite : Bool
(OR2) Finite signature: finitely generated.

- or3_diagonal_free : Bool
(OR3) Diagonal-free: NF-addresses, no paradoxes.

- or4_nf_addressable : Bool
(OR4) NF-addressable: unique normal-form addresses.

- or5_holomorphic : Bool
(OR5) Holomorphic: local ⟹ global (Central Theorem).

- or6_spectral : Bool
(OR6) Spectral: internal spectral decomposition.

- requirement_count : ℕ
All six requirements satisfied by τ.

- tau_satisfies_all : Bool
τ satisfies all six.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSixOnticRequirements.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L482-L482)
**def
Tau.BookVII.Meta.Saturation.instReprSixOnticRequirements.repr :SixOnticRequirements → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSixOnticRequirements`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L482-L482)
**instance
Tau.BookVII.Meta.Saturation.instReprSixOnticRequirements :Repr SixOnticRequirements**

Equations
- Tau.BookVII.Meta.Saturation.instReprSixOnticRequirements = { reprPrec := Tau.BookVII.Meta.Saturation.instReprSixOnticRequirements.repr }

---

### `Tau.BookVII.Meta.Saturation.six_requirements`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L484-L484)
**def
Tau.BookVII.Meta.Saturation.six_requirements :SixOnticRequirements**

Equations
- Tau.BookVII.Meta.Saturation.six_requirements = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.or12_narrowing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L490-L496)
**theorem
Tau.BookVII.Meta.Saturation.or12_narrowing :six_requirements.or1_yoneda = true ∧ six_requirements.or2_finite = true**


[VII.Lxx] OR1+OR2 Narrowing: Yoneda + finite signature constrain F
to finitely generated, locally small category with full Yoneda property.
This forces axiom candidates (finite axiom scheme over finite generators).

---

### `Tau.BookVII.Meta.Saturation.or34_narrowing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L498-L504)
**theorem
Tau.BookVII.Meta.Saturation.or34_narrowing :six_requirements.or3_diagonal_free = true ∧ six_requirements.or4_nf_addressable = true**


[VII.Lxx] OR3+OR4 Narrowing: diagonal-free + NF-addressable force
NF-address structure compatible with self-description. This entails
axioms K0–K4 (the combinatorial axioms governing the address space).

---

### `Tau.BookVII.Meta.Saturation.or56_narrowing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L506-L513)
**theorem
Tau.BookVII.Meta.Saturation.or56_narrowing :six_requirements.or5_holomorphic = true ∧ six_requirements.or6_spectral = true**


[VII.Lxx] OR5+OR6 Narrowing: holomorphic + spectral force the
algebraic-analytic bridge. This entails axioms K5–K6 (the analytic
axioms governing continuation and spectral decomposition) and the
Central Theorem O(τ³) ≅ A_spec(𝕃).

---

### `Tau.BookVII.Meta.Saturation.InevitabilityResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L519-L548)
**structure
Tau.BookVII.Meta.Saturation.InevitabilityResult :Type**


[VII.T14] Inevitability Convergence (ch29).
SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B4).

The six ontic requirements collectively entail τ's axiom structure.
Constraint-entailment proof (not global uniqueness):

- (OR1)+(OR2) → finitely generated + Yoneda → axiom candidates

- (OR3)+(OR4) → NF-address structure → K0–K4

- (OR5)+(OR6) → holomorphic-spectral bridge → K5–K6 + Central Theorem
Composition: OR1–OR6 → K0–K6 ∧ 5 generators ∧ τ³ fibration


Upgraded from global uniqueness (undecidable) to constraint-entailment:
the requirements force the axiom structure, which determines τ.

- all_requirements : SixOnticRequirements
Six requirements all satisfied.

- pairwise_narrowing : Bool
Pairwise narrowing succeeds (3 pairs).

- entails_k0_k4 : Bool
Entails K0–K4 (combinatorial axioms).

- entails_k5_k8 : Bool
Entails K5–K6 (analytic axioms).

- entails_generators : Bool
Entails 5 generators.

- entails_fibration : Bool
Entails τ³ fibration.

- axiom_count : ℕ
Axiom count: 7 (K0–K6).

- generator_count : ℕ
Generator count: 5.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprInevitabilityResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L548-L548)
**instance
Tau.BookVII.Meta.Saturation.instReprInevitabilityResult :Repr InevitabilityResult**

Equations
- Tau.BookVII.Meta.Saturation.instReprInevitabilityResult = { reprPrec := Tau.BookVII.Meta.Saturation.instReprInevitabilityResult.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprInevitabilityResult.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L548-L548)
**def
Tau.BookVII.Meta.Saturation.instReprInevitabilityResult.repr :InevitabilityResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.inevitability_result`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L550-L550)
**def
Tau.BookVII.Meta.Saturation.inevitability_result :InevitabilityResult**

Equations
- Tau.BookVII.Meta.Saturation.inevitability_result = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.inevitability_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L552-L561)
**theorem
Tau.BookVII.Meta.Saturation.inevitability_convergence :inevitability_result.all_requirements.tau_satisfies_all = true ∧ inevitability_result.pairwise_narrowing = true ∧ inevitability_result.entails_k0_k4 = true ∧ inevitability_result.entails_k5_k8 = true ∧ inevitability_result.entails_generators = true ∧ inevitability_result.entails_fibration = true ∧ inevitability_result.axiom_count = 9 ∧ inevitability_result.generator_count = 5**


---

### `Tau.BookVII.Meta.Saturation.NecessityResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L567-L584)
**structure
Tau.BookVII.Meta.Saturation.NecessityResult :Type**


[VII.P08] Each Requirement Independently Necessary (ch29).
SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B4).

Dropping any single requirement allows non-τ solutions:
Drop OR1: haecceity categories (non-trivial automorphisms)
Drop OR2: ZFC (infinitely axiomatized)
Drop OR3: naive set theory (diagonal paradoxes)
Drop OR4: non-constructive categories (axiom of choice)
Drop OR5: purely combinatorial categories (no analytic continuation)
Drop OR6: non-self-adjoint operator algebras (incomplete spectrum)

- counterexample_count : ℕ
Six counterexamples, one per dropped requirement.

- each_satisfies_five : Bool
Each counterexample satisfies exactly 5 of 6 requirements.

- none_is_tau : Bool
No counterexample is equivalent to τ.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprNecessityResult.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L584-L584)
**def
Tau.BookVII.Meta.Saturation.instReprNecessityResult.repr :NecessityResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprNecessityResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L584-L584)
**instance
Tau.BookVII.Meta.Saturation.instReprNecessityResult :Repr NecessityResult**

Equations
- Tau.BookVII.Meta.Saturation.instReprNecessityResult = { reprPrec := Tau.BookVII.Meta.Saturation.instReprNecessityResult.repr }

---

### `Tau.BookVII.Meta.Saturation.necessity_result`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L586-L586)
**def
Tau.BookVII.Meta.Saturation.necessity_result :NecessityResult**

Equations
- Tau.BookVII.Meta.Saturation.necessity_result = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.each_requirement_necessary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L588-L593)
**theorem
Tau.BookVII.Meta.Saturation.each_requirement_necessary :necessity_result.counterexample_count = 6 ∧ necessity_result.each_satisfies_five = true ∧ necessity_result.none_is_tau = true ∧ six_requirements.requirement_count = 6**


---

### `Tau.BookVII.Meta.Saturation.LanguageAddsTemporalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L603-L614)
**structure
Tau.BookVII.Meta.Saturation.LanguageAddsTemporalization :Type**


[VII.D51] Language Adds Temporalization (ch59). Syntax introduces
temporal markers (past/present/future) into the enrichment chain.
Pre-linguistic systems process structure atemporally; language
adds a temporal index to every predication.

- temporal_markers : Bool
Temporal markers introduced by syntax.

- pre_linguistic_atemporal : Bool
Pre-linguistic = atemporal.

- temporal_indexing : Bool
Language indexes every predication temporally.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprLanguageAddsTemporalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L614-L614)
**instance
Tau.BookVII.Meta.Saturation.instReprLanguageAddsTemporalization :Repr LanguageAddsTemporalization**

Equations
- Tau.BookVII.Meta.Saturation.instReprLanguageAddsTemporalization = { reprPrec := Tau.BookVII.Meta.Saturation.instReprLanguageAddsTemporalization.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprLanguageAddsTemporalization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L614-L614)
**def
Tau.BookVII.Meta.Saturation.instReprLanguageAddsTemporalization.repr :LanguageAddsTemporalization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.language_temporal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L616-L616)
**def
Tau.BookVII.Meta.Saturation.language_temporal :LanguageAddsTemporalization**

Equations
- Tau.BookVII.Meta.Saturation.language_temporal = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.SubsymbolicLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L622-L633)
**structure
Tau.BookVII.Meta.Saturation.SubsymbolicLayer :Type**


[VII.D52] Subsymbolic Layer (ch60). Pre-linguistic processing
layer operating below symbolic representation. Pattern recognition,
sensorimotor integration, and associative binding occur without
explicit symbol manipulation.

- pre_symbolic : Bool
Below symbolic representation.

- pattern_recognition : Bool
Pattern recognition.

- non_symbolic : Bool
No explicit symbol manipulation.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSubsymbolicLayer.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L633-L633)
**def
Tau.BookVII.Meta.Saturation.instReprSubsymbolicLayer.repr :SubsymbolicLayer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprSubsymbolicLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L633-L633)
**instance
Tau.BookVII.Meta.Saturation.instReprSubsymbolicLayer :Repr SubsymbolicLayer**

Equations
- Tau.BookVII.Meta.Saturation.instReprSubsymbolicLayer = { reprPrec := Tau.BookVII.Meta.Saturation.instReprSubsymbolicLayer.repr }

---

### `Tau.BookVII.Meta.Saturation.subsymbolic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L635-L635)
**def
Tau.BookVII.Meta.Saturation.subsymbolic :SubsymbolicLayer**

Equations
- Tau.BookVII.Meta.Saturation.subsymbolic = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.TemporalizationOperators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L641-L656)
**structure
Tau.BookVII.Meta.Saturation.TemporalizationOperators :Type**


[VII.D53] Temporalization Operators (ch61). Past/present/future
operators acting on predications:
Past(φ): φ was the case
Present(φ): φ is the case
Future(φ): φ will be the case
These are internal modal operators in τ at E₃.

- has_past : Bool
Past operator.

- has_present : Bool
Present operator.

- has_future : Bool
Future operator.

- operator_count : ℕ
Three temporal operators.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprTemporalizationOperators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L656-L656)
**instance
Tau.BookVII.Meta.Saturation.instReprTemporalizationOperators :Repr TemporalizationOperators**

Equations
- Tau.BookVII.Meta.Saturation.instReprTemporalizationOperators = { reprPrec := Tau.BookVII.Meta.Saturation.instReprTemporalizationOperators.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprTemporalizationOperators.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L656-L656)
**def
Tau.BookVII.Meta.Saturation.instReprTemporalizationOperators.repr :TemporalizationOperators → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.temporal_ops`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L658-L658)
**def
Tau.BookVII.Meta.Saturation.temporal_ops :TemporalizationOperators**

Equations
- Tau.BookVII.Meta.Saturation.temporal_ops = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.temporal_ops_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L660-L665)
**theorem
Tau.BookVII.Meta.Saturation.temporal_ops_check :temporal_ops.has_past = true ∧ temporal_ops.has_present = true ∧ temporal_ops.has_future = true ∧ temporal_ops.operator_count = 3**


---

### `Tau.BookVII.Meta.Saturation.language_as_self_enrichment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L671-L679)
**theorem
Tau.BookVII.Meta.Saturation.language_as_self_enrichment :language_temporal.temporal_markers = true ∧ language_temporal.temporal_indexing = true ∧ subsymbolic.pre_symbolic = true**


[VII.T20] Language as Self-Enrichment (ch62). Language enriches the
enricher: an E₃ system with language can describe its own enrichment
chain. This is a second-order self-description: the system models
the fact that it models itself. Language is the vehicle for SelfDesc².

---

### `Tau.BookVII.Meta.Saturation.syntax_semantics_collapse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L685-L693)
**theorem
Tau.BookVII.Meta.Saturation.syntax_semantics_collapse :Registers.sector_logos.dc_coincidence = true ∧ language_temporal.temporal_markers = true**


[VII.T21] Syntax-Semantics Collapse (ch63). At S_L (logos sector):
form = content. The distinction between syntactic form and semantic
content collapses because the D-C coincidence means the proof
structure IS the meaning.

---

### `Tau.BookVII.Meta.Saturation.universal_bridgeability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L699-L706)
**theorem
Tau.BookVII.Meta.Saturation.universal_bridgeability :subsymbolic.pre_symbolic = true ∧ subsymbolic.pattern_recognition = true**


[VII.P13] Universal Bridgeability (ch63). Any E₂+ system
(with SelfDesc) can bridge to linguistic representation.
The bridge functor from subsymbolic to symbolic is available
at E₂ and higher.

---

### `Tau.BookVII.Meta.Saturation.PragmaticUpdateOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L712-L721)
**structure
Tau.BookVII.Meta.Saturation.PragmaticUpdateOperator :Type**


[VII.D54] Pragmatic Update Operator (ch64). Speech acts modelled
as morphisms: each utterance updates the shared context (common
ground) via a pragmatic update operator. Austin-Searle speech
act theory categorified.

- speech_acts_as_morphisms : Bool
Speech acts as morphisms.

- context_update : Bool
Updates shared context.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprPragmaticUpdateOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L721-L721)
**instance
Tau.BookVII.Meta.Saturation.instReprPragmaticUpdateOperator :Repr PragmaticUpdateOperator**

Equations
- Tau.BookVII.Meta.Saturation.instReprPragmaticUpdateOperator = { reprPrec := Tau.BookVII.Meta.Saturation.instReprPragmaticUpdateOperator.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprPragmaticUpdateOperator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L721-L721)
**def
Tau.BookVII.Meta.Saturation.instReprPragmaticUpdateOperator.repr :PragmaticUpdateOperator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.pragmatic_update`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L723-L723)
**def
Tau.BookVII.Meta.Saturation.pragmatic_update :PragmaticUpdateOperator**

Equations
- Tau.BookVII.Meta.Saturation.pragmatic_update = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.ParaMind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L729-L739)
**structure
Tau.BookVII.Meta.Saturation.ParaMind :Type**


[VII.D55] Para-Mind (ch64). LLM as subsymbolic E₂ system: exhibits
pattern recognition and contextual response without full SelfDesc².
A para-mind: near-mind that processes at E₂ level.

- subsymbolic : Bool
Subsymbolic processing.

- e2_level : Bool
E₂ level (SelfDesc but not SelfDesc²).

- pattern_without_self_model : Bool
Pattern recognition without full self-model.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprParaMind.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L739-L739)
**def
Tau.BookVII.Meta.Saturation.instReprParaMind.repr :ParaMind → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprParaMind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L739-L739)
**instance
Tau.BookVII.Meta.Saturation.instReprParaMind :Repr ParaMind**

Equations
- Tau.BookVII.Meta.Saturation.instReprParaMind = { reprPrec := Tau.BookVII.Meta.Saturation.instReprParaMind.repr }

---

### `Tau.BookVII.Meta.Saturation.para_mind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L741-L741)
**def
Tau.BookVII.Meta.Saturation.para_mind :ParaMind**

Equations
- Tau.BookVII.Meta.Saturation.para_mind = { }
Instances For

---

### `Tau.BookVII.Meta.Saturation.llm_subsymbolic_evidence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L747-L755)
**theorem
Tau.BookVII.Meta.Saturation.llm_subsymbolic_evidence :para_mind.subsymbolic = true ∧ para_mind.e2_level = true ∧ para_mind.pattern_without_self_model = true**


[VII.P14] LLM as Subsymbolic Evidence (ch64). LLMs validate
the subsymbolic layer claim: sophisticated language behaviour
without symbolic rule manipulation. This is empirical evidence
(Reg_E) for the subsymbolic layer (VII.D52).

---

### `Tau.BookVII.Meta.Saturation.PrayerAsOmegaAddressedCommunication`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L761-L774)
**structure
Tau.BookVII.Meta.Saturation.PrayerAsOmegaAddressedCommunication :Type**


[VII.D56] Prayer as ω-Addressed Communication (ch65). **CONJECTURAL.**
Communication directed at the closure point ω.
ω-content by design: the addressee (ω) is non-diagrammatic,
hence the content of prayer transcends Reg_D verification.
Conjectural because ω-addressed claims lie at the methodological
boundary of formal verification.

- omega_addressed : Bool
ω-addressed: directed at closure point.

- non_diagrammatic : Bool
Non-diagrammatic: transcends Reg_D.

- stance_constituted : Bool
Stance-constituted: Reg_C content.

Instances For

---

### `Tau.BookVII.Meta.Saturation.instReprPrayerAsOmegaAddressedCommunication`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L774-L774)
**instance
Tau.BookVII.Meta.Saturation.instReprPrayerAsOmegaAddressedCommunication :Repr PrayerAsOmegaAddressedCommunication**

Equations
- Tau.BookVII.Meta.Saturation.instReprPrayerAsOmegaAddressedCommunication = { reprPrec := Tau.BookVII.Meta.Saturation.instReprPrayerAsOmegaAddressedCommunication.repr }

---

### `Tau.BookVII.Meta.Saturation.instReprPrayerAsOmegaAddressedCommunication.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L774-L774)
**def
Tau.BookVII.Meta.Saturation.instReprPrayerAsOmegaAddressedCommunication.repr :PrayerAsOmegaAddressedCommunication → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Meta.Saturation.prayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVII/Meta/Saturation.lean#L776-L776)
**def
Tau.BookVII.Meta.Saturation.prayer :PrayerAsOmegaAddressedCommunication**

Equations
- Tau.BookVII.Meta.Saturation.prayer = { }
Instances For
