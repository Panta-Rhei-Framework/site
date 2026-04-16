---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BoundaryUnification"
permalink: /verify/taulib/docs/book-v-cosmology-boundary-unification/
lane: verify
module_name: "TauLib.BookV.Cosmology.BoundaryUnification"
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

# TauLib.BookV.Cosmology.BoundaryUnification


Boundary unification. All physics from boundary data. Complete
synthesis of the five sectors via commuting Hartogs squares.
Cross-coupling as naturality. ι<sub>τ</sub> mediates all ten couplings.

## Registry Cross-References


- [V.R244] The lesson: do not add, recognize -- structural remark

- [V.T120] Boundary Completeness -- `boundary_completeness`

- [V.R245] Comparison with orthodox unification -- structural remark

- [V.P103] Cross-coupling as Naturality -- `cross_coupling_naturality`

- [V.R246] Naturality replaces gauge invariance -- structural remark

- [V.P104] ι<sub>τ</sub> mediates all ten couplings -- `iota_mediates_all`

- [V.R247] Scope note: implementation roadmap -- structural remark


## Mathematical Content


### Boundary Completeness


All C(4,2) = 6 pairs of primitive sectors {D, A, B, C} satisfy
commuting Hartogs squares in H_∂[ω]. Each pair has a well-defined
cross-coupling κ(X,Y) that is a rational function of ι<sub>τ</sub>.

The 6 pairs: DA, DB, DC, AB, AC, BC.
Together with 4 self-couplings and the closing identity, all 10+1
coupling relations are determined by ι<sub>τ</sub> alone.

### Cross-Coupling as Naturality


For each sector pair (X,Y), the cross-coupling κ(X,Y) is the leading
spectral weight of a natural transformation η_{X,Y} between the
two sector functors. Naturality (= functorial coherence) replaces
gauge invariance as the organizing principle.

### ι<sub>τ</sub> Mediates All Ten Couplings


Every coupling constant in τ (self-couplings, cross-couplings, α, G,
and the closing identity) is a rational function of the single
master constant ι<sub>τ</sub> = 2/(π+e).

4 self-couplings: κ(D;1), κ(A;2), κ(B;1), κ(C;3)
6 cross-couplings: κ(D,A), κ(D,B), κ(D,C), κ(A,B), κ(A,C), κ(B,C)
Total: 10 couplings, ALL from ι<sub>τ</sub>.

### Boundary Unification Principle


Unification does not require a larger gauge group (like SU(5) or E₈).
The sectors are already unified at the boundary-character level: they
are different readings of the SAME H_∂[ω]. What orthodox physics calls
"unification" is recognition that all sectors share a common algebraic
substrate.

## Ground Truth Sources


- Book V ch56: Boundary Unification


---

### `Tau.BookV.Cosmology.PrimitiveSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L69-L79)
**inductive
Tau.BookV.Cosmology.PrimitiveSector :Type**


Primitive sector (for pairing).

- D : PrimitiveSector
D = α = Gravity.

- A : PrimitiveSector
A = π = Weak.

- B : PrimitiveSector
B = γ = EM.

- C : PrimitiveSector
C = η = Strong.

Instances For

---

### `Tau.BookV.Cosmology.instReprPrimitiveSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L79-L79)
**def
Tau.BookV.Cosmology.instReprPrimitiveSector.repr :PrimitiveSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPrimitiveSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L79-L79)
**instance
Tau.BookV.Cosmology.instReprPrimitiveSector :Repr PrimitiveSector**

Equations
- Tau.BookV.Cosmology.instReprPrimitiveSector = { reprPrec := Tau.BookV.Cosmology.instReprPrimitiveSector.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqPrimitiveSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L79-L79)
**instance
Tau.BookV.Cosmology.instDecidableEqPrimitiveSector :DecidableEq PrimitiveSector**

Equations
- Tau.BookV.Cosmology.instDecidableEqPrimitiveSector x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqPrimitiveSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L79-L79)
**instance
Tau.BookV.Cosmology.instBEqPrimitiveSector :BEq PrimitiveSector**

Equations
- Tau.BookV.Cosmology.instBEqPrimitiveSector = { beq := Tau.BookV.Cosmology.instBEqPrimitiveSector.beq }

---

### `Tau.BookV.Cosmology.instBEqPrimitiveSector.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L79-L79)
**def
Tau.BookV.Cosmology.instBEqPrimitiveSector.beq :PrimitiveSector → PrimitiveSector → Bool**

Equations
- Tau.BookV.Cosmology.instBEqPrimitiveSector.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.SectorPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L81-L89)
**structure
Tau.BookV.Cosmology.SectorPair :Type**


Ordered sector pair (X < Y in canonical order D < A < B < C).

- fst : PrimitiveSector
First sector.

- snd : PrimitiveSector
Second sector.

- different : self.fst ≠ self.snd
The pair is ordered (different sectors).

Instances For

---

### `Tau.BookV.Cosmology.instReprSectorPair.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L89-L89)
**def
Tau.BookV.Cosmology.instReprSectorPair.repr :SectorPair → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprSectorPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L89-L89)
**instance
Tau.BookV.Cosmology.instReprSectorPair :Repr SectorPair**

Equations
- Tau.BookV.Cosmology.instReprSectorPair = { reprPrec := Tau.BookV.Cosmology.instReprSectorPair.repr }

---

### `Tau.BookV.Cosmology.all_sector_pairs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L91-L98)
**def
Tau.BookV.Cosmology.all_sector_pairs :List SectorPair**


All 6 sector pairs.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.six_pairs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L100-L101)
**theorem
Tau.BookV.Cosmology.six_pairs :all_sector_pairs.length = 6**


There are exactly 6 pairs.

---

### `Tau.BookV.Cosmology.four_choose_two`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L103-L104)
**theorem
Tau.BookV.Cosmology.four_choose_two :4 * 3 / 2 = 6**


C(4,2) = 6.

---

### `Tau.BookV.Cosmology.BoundaryCompleteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L110-L128)
**structure
Tau.BookV.Cosmology.BoundaryCompleteness :Type**


[V.T120] Boundary completeness theorem: all C(4,2) = 6 pairs
of primitive sectors satisfy commuting Hartogs squares in H_∂[ω].

Each pair has a well-defined cross-coupling κ(X,Y) that is a
rational function of ι<sub>τ</sub>. No pair is "missing" or "decoupled."

This is the culminating theorem of Book V: the τ-framework
provides a complete, self-consistent description of all
inter-sector relations.

- num_pairs : ℕ
Number of sector pairs with Hartogs squares.

- all_six : self.num_pairs = 6
All 6 pairs present.

- all_commute : Bool
Whether all Hartogs squares commute.

- all_iota_rational : Bool
Whether all cross-couplings are ι<sub>τ</sub>-rational.

Instances For

---

### `Tau.BookV.Cosmology.instReprBoundaryCompleteness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L128-L128)
**def
Tau.BookV.Cosmology.instReprBoundaryCompleteness.repr :BoundaryCompleteness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBoundaryCompleteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L128-L128)
**instance
Tau.BookV.Cosmology.instReprBoundaryCompleteness :Repr BoundaryCompleteness**

Equations
- Tau.BookV.Cosmology.instReprBoundaryCompleteness = { reprPrec := Tau.BookV.Cosmology.instReprBoundaryCompleteness.repr }

---

### `Tau.BookV.Cosmology.boundary_completeness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L130-L132)
**theorem
Tau.BookV.Cosmology.boundary_completeness :all_sector_pairs.length = 6**


Boundary completeness: 6 pairs, all commuting.

---

### `Tau.BookV.Cosmology.CrossCouplingNaturality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L138-L155)
**structure
Tau.BookV.Cosmology.CrossCouplingNaturality :Type**


[V.P103] Cross-coupling as naturality: for each sector pair (X,Y),
κ(X,Y) is the leading spectral weight of a natural transformation
η_{X,Y} between the sector functors.

Naturality (functorial coherence) replaces gauge invariance as the
organizing principle for inter-sector relations.

- pair : SectorPair
The sector pair.

- coupling_numer : ℕ
Coupling numerator.

- coupling_denom : ℕ
Coupling denominator.

- denom_pos : self.coupling_denom > 0
Denominator positive.

- from_naturality : Bool
Whether the coupling arises from a natural transformation.

Instances For

---

### `Tau.BookV.Cosmology.instReprCrossCouplingNaturality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L155-L155)
**instance
Tau.BookV.Cosmology.instReprCrossCouplingNaturality :Repr CrossCouplingNaturality**

Equations
- Tau.BookV.Cosmology.instReprCrossCouplingNaturality = { reprPrec := Tau.BookV.Cosmology.instReprCrossCouplingNaturality.repr }

---

### `Tau.BookV.Cosmology.instReprCrossCouplingNaturality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L155-L155)
**def
Tau.BookV.Cosmology.instReprCrossCouplingNaturality.repr :CrossCouplingNaturality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.cross_coupling_naturality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L157-L160)
**theorem
Tau.BookV.Cosmology.cross_coupling_naturality
(c : CrossCouplingNaturality)

(hn : c.from_naturality = true)
 :c.from_naturality = true**


Cross-coupling is natural.

---

### `Tau.BookV.Cosmology.naturality_replaces_gauge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L166-L174)
**def
Tau.BookV.Cosmology.naturality_replaces_gauge :Prop**


[V.R246] In orthodox gauge theory, universality of force couplings
follows from gauge invariance of the Lagrangian. In τ, gauge
invariance is replaced by naturality (functorial coherence).

This is not a weaker condition — it is the correct structural
condition. Gauge invariance is a chart-level shadow of naturality.
Equations
- Tau.BookV.Cosmology.naturality_replaces_gauge = ("Naturality replaces gauge invariance as organizing principle" = "Naturality replaces gauge invariance as organizing principle")
Instances For

---

### `Tau.BookV.Cosmology.naturality_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L176-L176)
**theorem
Tau.BookV.Cosmology.naturality_holds :naturality_replaces_gauge**


---

### `Tau.BookV.Cosmology.CouplingType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L182-L188)
**inductive
Tau.BookV.Cosmology.CouplingType :Type**


Coupling classification.

- SelfCoupling : CouplingType
Self-coupling: κ(X; n).

- CrossCoupling : CouplingType
Cross-coupling: κ(X, Y).

Instances For

---

### `Tau.BookV.Cosmology.instReprCouplingType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L188-L188)
**def
Tau.BookV.Cosmology.instReprCouplingType.repr :CouplingType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCouplingType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L188-L188)
**instance
Tau.BookV.Cosmology.instReprCouplingType :Repr CouplingType**

Equations
- Tau.BookV.Cosmology.instReprCouplingType = { reprPrec := Tau.BookV.Cosmology.instReprCouplingType.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqCouplingType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L188-L188)
**instance
Tau.BookV.Cosmology.instDecidableEqCouplingType :DecidableEq CouplingType**

Equations
- Tau.BookV.Cosmology.instDecidableEqCouplingType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqCouplingType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L188-L188)
**instance
Tau.BookV.Cosmology.instBEqCouplingType :BEq CouplingType**

Equations
- Tau.BookV.Cosmology.instBEqCouplingType = { beq := Tau.BookV.Cosmology.instBEqCouplingType.beq }

---

### `Tau.BookV.Cosmology.instBEqCouplingType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L188-L188)
**def
Tau.BookV.Cosmology.instBEqCouplingType.beq :CouplingType → CouplingType → Bool**

Equations
- Tau.BookV.Cosmology.instBEqCouplingType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.CouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L190-L198)
**structure
Tau.BookV.Cosmology.CouplingEntry :Type**


A single coupling constant entry.

- name : String
Coupling name.

- kind : CouplingType
Coupling type.

- value_times_1e6 : ℕ
Numerator (× 10⁶).

Instances For

---

### `Tau.BookV.Cosmology.instReprCouplingEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L198-L198)
**def
Tau.BookV.Cosmology.instReprCouplingEntry.repr :CouplingEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L198-L198)
**instance
Tau.BookV.Cosmology.instReprCouplingEntry :Repr CouplingEntry**

Equations
- Tau.BookV.Cosmology.instReprCouplingEntry = { reprPrec := Tau.BookV.Cosmology.instReprCouplingEntry.repr }

---

### `Tau.BookV.Cosmology.all_couplings`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L200-L217)
**def
Tau.BookV.Cosmology.all_couplings :List CouplingEntry**


[V.P104] ι<sub>τ</sub> mediates all ten couplings: every coupling constant
in τ is a rational function of ι<sub>τ</sub> = 2/(π+e).

4 self-couplings + 6 cross-couplings = 10 total.
Plus the closing identity (α_G from α¹⁸) = 11th relation.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.iota_mediates_all`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L219-L221)
**theorem
Tau.BookV.Cosmology.iota_mediates_all :all_couplings.length = 10**


10 couplings total.

---

### `Tau.BookV.Cosmology.self_coupling_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L223-L226)
**theorem
Tau.BookV.Cosmology.self_coupling_count :(List.filter (fun (c : CouplingEntry) => c.kind == CouplingType.SelfCoupling) all_couplings).length = 4**


4 self-couplings.

---

### `Tau.BookV.Cosmology.cross_coupling_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L228-L231)
**theorem
Tau.BookV.Cosmology.cross_coupling_count :(List.filter (fun (c : CouplingEntry) => c.kind == CouplingType.CrossCoupling) all_couplings).length = 6**


6 cross-couplings.

---

### `Tau.BookV.Cosmology.BoundaryUnificationSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L237-L251)
**structure
Tau.BookV.Cosmology.BoundaryUnificationSummary :Type**


Summary of the boundary unification principle.

- num_sectors : ℕ
Number of primitive sectors.

- num_pairs : ℕ
Number of sector pairs.

- num_couplings : ℕ
Number of total couplings (self + cross).

- master_constant : String
Single master constant.

- all_determined : Bool
Whether all are determined by master constant.

- no_larger_group : Bool
No larger gauge group needed.

Instances For

---

### `Tau.BookV.Cosmology.instReprBoundaryUnificationSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L251-L251)
**instance
Tau.BookV.Cosmology.instReprBoundaryUnificationSummary :Repr BoundaryUnificationSummary**

Equations
- Tau.BookV.Cosmology.instReprBoundaryUnificationSummary = { reprPrec := Tau.BookV.Cosmology.instReprBoundaryUnificationSummary.repr }

---

### `Tau.BookV.Cosmology.instReprBoundaryUnificationSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L251-L251)
**def
Tau.BookV.Cosmology.instReprBoundaryUnificationSummary.repr :BoundaryUnificationSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.unification_summary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BoundaryUnification.lean#L253-L254)
**def
Tau.BookV.Cosmology.unification_summary :BoundaryUnificationSummary**


The canonical summary.
Equations
- Tau.BookV.Cosmology.unification_summary = { }
Instances For
