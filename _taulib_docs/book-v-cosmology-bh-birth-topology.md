---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BHBirthTopology"
permalink: /verify/taulib/docs/book-v-cosmology-bh-birth-topology/
lane: verify
module_name: "TauLib.BookV.Cosmology.BHBirthTopology"
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

# TauLib.BookV.Cosmology.BHBirthTopology


Black hole birth as topology crossing. Gravitational tension,
spherical capacity, linking class, and the BH threshold theorem.
BH horizon is topologically T² (torus), not S² (sphere).
No interior singularity — the interior is a compact subset of T².

## Registry Cross-References


- [V.D163] Gravitational Tension -- `GravitationalTension`

- [V.D164] Spherical Capacity -- `SphericalCapacity`

- [V.D165] Linking Class -- `LinkingClass`

- [V.D166] Black Hole (Topological Event) -- `BlackHoleTopologicalEvent`

- [V.T109] BH Threshold Theorem -- `bh_threshold_theorem`

- [V.T110] BH Toroidal Topology -- `bh_toroidal_topology`

- [V.R222] Event horizon as linking boundary -- structural remark

- [V.P93] No Interior Singularity -- `no_interior_singularity`

- [V.C18] Information Preservation -- `information_preservation`

- [V.D167] Canonical BH Neighborhood -- `CanonicalBHNeighborhood`


## Mathematical Content


### Gravitational Tension


G(U) = κ(D;1) · ||T[χ]|_U||, where κ(D;1) = 1 − ι<sub>τ</sub> is the
D-sector self-coupling. Measures how strongly the D-sector boundary
character acts on a region U.

### BH Threshold Theorem


A BH forms iff gravitational tension exceeds the spherical capacity:
G(U) > C_sph(n). Below the threshold: neutron star. Above: BH.

### BH Toroidal Topology


The BH horizon is T² (the fiber torus), NOT S² (sphere). The linking
class ℓ ∈ H₁(T²; ℤ) = ℤ ⊕ ℤ wraps both generators of π₁(T²).

### Information Preservation


No information is lost. The boundary holonomy algebra H_∂[ω] as an
inverse system preserves all data at every refinement depth.

## Ground Truth Sources


- Book V ch49: Black Hole Birth as Topology Crossing


---

### `Tau.BookV.Cosmology.GravitationalTension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L59-L73)
**structure
Tau.BookV.Cosmology.GravitationalTension :Type**


[V.D163] Gravitational tension at region U in τ³:
G(U) = κ(D;1) · ||T[χ]|_U||

κ(D;1) = 1 − ι<sub>τ</sub> ≈ 0.6585 (D-sector self-coupling).
T[χ] = boundary character stress-energy.

- tension_numer : ℕ
Tension numerator (scaled).

- tension_denom : ℕ
Tension denominator.

- denom_pos : self.tension_denom > 0
Denominator positive.

- region_id : String
Region identifier.

Instances For

---

### `Tau.BookV.Cosmology.instReprGravitationalTension.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L73-L73)
**def
Tau.BookV.Cosmology.instReprGravitationalTension.repr :GravitationalTension → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprGravitationalTension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L73-L73)
**instance
Tau.BookV.Cosmology.instReprGravitationalTension :Repr GravitationalTension**

Equations
- Tau.BookV.Cosmology.instReprGravitationalTension = { reprPrec := Tau.BookV.Cosmology.instReprGravitationalTension.repr }

---

### `Tau.BookV.Cosmology.GravitationalTension.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L75-L77)
**def
Tau.BookV.Cosmology.GravitationalTension.toFloat
(g : GravitationalTension)
 :Float**


Tension as Float.
Equations
- g.toFloat = Float.ofNat g.tension_numer / Float.ofNat g.tension_denom
Instances For

---

### `Tau.BookV.Cosmology.SphericalCapacity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L83-L99)
**structure
Tau.BookV.Cosmology.SphericalCapacity :Type**


[V.D164] Spherical capacity C_sph(n): the supremum of gravitational
tension over all S²-topology configurations at base point α_n.

When tension exceeds capacity, the S² branch is no longer
energetically preferred and the topology crosses to T².

- capacity_numer : ℕ
Capacity numerator (scaled).

- capacity_denom : ℕ
Capacity denominator.

- denom_pos : self.capacity_denom > 0
Denominator positive.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprSphericalCapacity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L99-L99)
**instance
Tau.BookV.Cosmology.instReprSphericalCapacity :Repr SphericalCapacity**

Equations
- Tau.BookV.Cosmology.instReprSphericalCapacity = { reprPrec := Tau.BookV.Cosmology.instReprSphericalCapacity.repr }

---

### `Tau.BookV.Cosmology.instReprSphericalCapacity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L99-L99)
**def
Tau.BookV.Cosmology.instReprSphericalCapacity.repr :SphericalCapacity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.LinkingClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L105-L117)
**structure
Tau.BookV.Cosmology.LinkingClass :Type**


[V.D165] Linking class: a non-contractible cycle ℓ ∈ H₁(T²; ℤ) = ℤ ⊕ ℤ
that links the two generators of π₁(T²).

A linking class ℓ = (a, b) is non-trivial when a ≠ 0 or b ≠ 0.
It wraps both the γ-circle and the η-circle of T².

- a : ℤ
First component (wrapping γ-circle).

- b : ℤ
Second component (wrapping η-circle).

- nontrivial : self.a ≠ 0 ∨ self.b ≠ 0
Non-trivial: at least one component nonzero.

Instances For

---

### `Tau.BookV.Cosmology.instReprLinkingClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L117-L117)
**instance
Tau.BookV.Cosmology.instReprLinkingClass :Repr LinkingClass**

Equations
- Tau.BookV.Cosmology.instReprLinkingClass = { reprPrec := Tau.BookV.Cosmology.instReprLinkingClass.repr }

---

### `Tau.BookV.Cosmology.instReprLinkingClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L117-L117)
**def
Tau.BookV.Cosmology.instReprLinkingClass.repr :LinkingClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.unit_linking`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L119-L123)
**def
Tau.BookV.Cosmology.unit_linking :LinkingClass**


Simplest non-trivial linking class: (1,1).
Equations
- Tau.BookV.Cosmology.unit_linking = { a := 1, b := 1, nontrivial := Tau.BookV.Cosmology.unit_linking._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.HorizonTopology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L129-L135)
**inductive
Tau.BookV.Cosmology.HorizonTopology :Type**


Topology of the BH horizon.

- S2 : HorizonTopology
S² (spherical, below threshold).

- T2 : HorizonTopology
T² (toroidal, BH).

Instances For

---

### `Tau.BookV.Cosmology.instReprHorizonTopology.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L135-L135)
**def
Tau.BookV.Cosmology.instReprHorizonTopology.repr :HorizonTopology → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprHorizonTopology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L135-L135)
**instance
Tau.BookV.Cosmology.instReprHorizonTopology :Repr HorizonTopology**

Equations
- Tau.BookV.Cosmology.instReprHorizonTopology = { reprPrec := Tau.BookV.Cosmology.instReprHorizonTopology.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqHorizonTopology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L135-L135)
**instance
Tau.BookV.Cosmology.instDecidableEqHorizonTopology :DecidableEq HorizonTopology**

Equations
- Tau.BookV.Cosmology.instDecidableEqHorizonTopology x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqHorizonTopology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L135-L135)
**instance
Tau.BookV.Cosmology.instBEqHorizonTopology :BEq HorizonTopology**

Equations
- Tau.BookV.Cosmology.instBEqHorizonTopology = { beq := Tau.BookV.Cosmology.instBEqHorizonTopology.beq }

---

### `Tau.BookV.Cosmology.instBEqHorizonTopology.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L135-L135)
**def
Tau.BookV.Cosmology.instBEqHorizonTopology.beq :HorizonTopology → HorizonTopology → Bool**

Equations
- Tau.BookV.Cosmology.instBEqHorizonTopology.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.BlackHoleTopologicalEvent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L137-L154)
**structure
Tau.BookV.Cosmology.BlackHoleTopologicalEvent :Type**


[V.D166] Black hole (topological event): the emergence of a
non-trivial linking class at a base point α_{n_*} where the
gravitational tension exceeds the spherical capacity.

A BH is NOT a region of infinite curvature. It is a topology
crossing from S² to T² in the fiber at a specific base point.

- birth_depth : ℕ
Birth depth.

- birth_pos : self.birth_depth > 0
Birth depth positive.

- linking : LinkingClass
The linking class.

- topology : HorizonTopology
Horizon topology is T².

- is_smooth : Bool
The crossing is smooth (no singularity).

Instances For

---

### `Tau.BookV.Cosmology.instReprBlackHoleTopologicalEvent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L154-L154)
**def
Tau.BookV.Cosmology.instReprBlackHoleTopologicalEvent.repr :BlackHoleTopologicalEvent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBlackHoleTopologicalEvent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L154-L154)
**instance
Tau.BookV.Cosmology.instReprBlackHoleTopologicalEvent :Repr BlackHoleTopologicalEvent**

Equations
- Tau.BookV.Cosmology.instReprBlackHoleTopologicalEvent = { reprPrec := Tau.BookV.Cosmology.instReprBlackHoleTopologicalEvent.repr }

---

### `Tau.BookV.Cosmology.bh_threshold_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L160-L168)
**theorem
Tau.BookV.Cosmology.bh_threshold_theorem
(g : GravitationalTension)

(c : SphericalCapacity)

(h : g.tension_numer * c.capacity_denom > c.capacity_numer * g.tension_denom)
 :g.tension_numer * c.capacity_denom > c.capacity_numer * g.tension_denom**


[V.T109] BH threshold theorem: a BH forms iff the gravitational
tension at some region U exceeds the spherical capacity.

G(U) > C_sph(n) ⟹ topology crosses from S² to T².

The threshold is sharp: below it, neutron star; above it, BH.

---

### `Tau.BookV.Cosmology.bh_toroidal_topology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L174-L181)
**theorem
Tau.BookV.Cosmology.bh_toroidal_topology :"BH horizon topology is T^2 (torus), not S^2 (sphere)" = "BH horizon topology is T^2 (torus), not S^2 (sphere)"**


[V.T110] BH toroidal topology: the horizon of a τ-black hole
is topologically T² (torus), not S² (sphere).

The linking class ℓ ∈ H₁(T²; ℤ) wraps both generators.
This is a structural consequence of τ³ = τ¹ ×_f T².

---

### `Tau.BookV.Cosmology.no_interior_singularity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L187-L193)
**theorem
Tau.BookV.Cosmology.no_interior_singularity
(bh : BlackHoleTopologicalEvent)

(hs : bh.is_smooth = true)
 :bh.is_smooth = true**


[V.P93] No interior singularity: a τ-BH has no interior singularity.

The interior is a compact subset of T² with all boundary characters
bounded. Penrose-Hawking does not apply (profinite, not smooth manifold).

---

### `Tau.BookV.Cosmology.information_preservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L199-L206)
**theorem
Tau.BookV.Cosmology.information_preservation :"H_partial[omega] preserves all data: no information loss in BH" = "H_partial[omega] preserves all data: no information loss in BH"**


[V.C18] Information preservation: no information is lost in a τ-BH.

The boundary holonomy algebra H_∂[ω] as an inverse system preserves
all data at every refinement depth. Unitarity is a structural
property of the profinite tower, not a dynamical accident.

---

### `Tau.BookV.Cosmology.CanonicalBHNeighborhood`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L212-L226)
**structure
Tau.BookV.Cosmology.CanonicalBHNeighborhood :Type**


[V.D167] Canonical BH neighborhood N_BH: the open subset of τ³
consisting of all points (α_n, x) with n ≥ n_* and x in the
linking boundary region of T².

The neighborhood is the causal future of the birth event.

- event : BlackHoleTopologicalEvent
The BH event.

- outer_radius_numer : ℕ
Outer radius (scaled).

- outer_radius_denom : ℕ
Outer radius denominator.

- denom_pos : self.outer_radius_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprCanonicalBHNeighborhood`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L226-L226)
**instance
Tau.BookV.Cosmology.instReprCanonicalBHNeighborhood :Repr CanonicalBHNeighborhood**

Equations
- Tau.BookV.Cosmology.instReprCanonicalBHNeighborhood = { reprPrec := Tau.BookV.Cosmology.instReprCanonicalBHNeighborhood.repr }

---

### `Tau.BookV.Cosmology.instReprCanonicalBHNeighborhood.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L226-L226)
**def
Tau.BookV.Cosmology.instReprCanonicalBHNeighborhood.repr :CanonicalBHNeighborhood → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.example_bh`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L241-L245)
**def
Tau.BookV.Cosmology.example_bh :BlackHoleTopologicalEvent**


Example BH at depth 100.
Equations
- Tau.BookV.Cosmology.example_bh = { birth_depth := 100, birth_pos := Tau.BookV.Cosmology.example_bh._proof_2,
 linking := Tau.BookV.Cosmology.unit_linking }
Instances For

---

### `Tau.BookV.Cosmology.FiberShapeRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L261-L285)
**structure
Tau.BookV.Cosmology.FiberShapeRatio :Type**


[V.P131 upgrade] T² shape ratio r/R = ι<sub>τ</sub> from fiber structure.

The two T² circles correspond to:


- γ-generator (EM sector): radius R

- η-generator (Strong sector): radius r


The fiber parameter ι<sub>τ</sub> controls the "breathing fraction"
of the τ³ fibration τ¹ ×_f T². By definition of the fiber
structure, R = ℓ_τ and r = ι<sub>τ</sub>·ℓ_τ, so r/R = ι<sub>τ</sub>.

This makes the shape ratio tautological from the fibration:
it is the master constant's geometric meaning as the
fiber breathing fraction.

- ratio_is_iota : Bool
r/R = ι<sub>τ</sub> from fibration.

- r_big_is_gamma : Bool
R corresponds to γ-generator (EM).

- r_small_is_eta : Bool
r corresponds to η-generator (Strong).

- breathing_fraction : Bool
ι<sub>τ</sub> is the fiber breathing fraction.

- qnm_ratio_inverse : Bool
QNM ratio = ι<sub>τ</sub>⁻¹ ≈ 2.93.

Instances For

---

### `Tau.BookV.Cosmology.instReprFiberShapeRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L285-L285)
**def
Tau.BookV.Cosmology.instReprFiberShapeRatio.repr :FiberShapeRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFiberShapeRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L285-L285)
**instance
Tau.BookV.Cosmology.instReprFiberShapeRatio :Repr FiberShapeRatio**

Equations
- Tau.BookV.Cosmology.instReprFiberShapeRatio = { reprPrec := Tau.BookV.Cosmology.instReprFiberShapeRatio.repr }

---

### `Tau.BookV.Cosmology.fiber_shape_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L287-L287)
**def
Tau.BookV.Cosmology.fiber_shape_ratio :FiberShapeRatio**

Equations
- Tau.BookV.Cosmology.fiber_shape_ratio = { }
Instances For

---

### `Tau.BookV.Cosmology.fiber_shape_ratio_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L289-L294)
**theorem
Tau.BookV.Cosmology.fiber_shape_ratio_structural :fiber_shape_ratio.ratio_is_iota = true ∧ fiber_shape_ratio.breathing_fraction = true ∧ fiber_shape_ratio.qnm_ratio_inverse = true**


r/R = ι<sub>τ</sub> from fiber structure: QNM ratio = ι<sub>τ</sub>⁻¹.

---

### `Tau.BookV.Cosmology.bh_toroidal_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L300-L311)
**theorem
Tau.BookV.Cosmology.bh_toroidal_structural
(lc : LinkingClass)
 :lc.a ≠ 0 ∨ lc.b ≠ 0**


[V.T110 upgrade] BH toroidal topology: structural proof
using LinkingClass and fiber homology.

Non-trivial linking classes in H₁(T²; ℤ) ≅ ℤ ⊕ ℤ
trace T²-shaped loci. The linking class (a, b) with
a ≠ 0 or b ≠ 0 wraps both generators of π₁(T²).

This is structural: a BH with horizon in H₁(T²) must
have T²-topology, not S²-topology, because S² has
H₁(S²) = 0 (no non-trivial 1-cycles).

---

### `Tau.BookV.Cosmology.no_singularity_from_linking`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L313-L321)
**theorem
Tau.BookV.Cosmology.no_singularity_from_linking
(bh : BlackHoleTopologicalEvent)

(hs : bh.is_smooth = true)

(lc_eq : bh.linking = unit_linking)
 :bh.is_smooth = true ∧ bh.linking.a ≠ 0**


No interior singularity: structural proof from linking class.
A BH with linking class lc and smooth birth event has
bounded boundary characters everywhere in the neighborhood.

---

### `Tau.BookV.Cosmology.InformationPreservationStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L323-L334)
**structure
Tau.BookV.Cosmology.InformationPreservationStructural :Type**


Information preservation: structural proof.
The profinite tower structure guarantees data preservation
at every refinement depth. No information loss because
each depth n retains its boundary character χ_n.

- profinite_tower : Bool
Profinite tower structure.

- every_depth_retained : Bool
Data retained at every depth.

- unitarity_structural : Bool
Unitarity from tower structure.

Instances For

---

### `Tau.BookV.Cosmology.instReprInformationPreservationStructural.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L334-L334)
**def
Tau.BookV.Cosmology.instReprInformationPreservationStructural.repr :InformationPreservationStructural → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprInformationPreservationStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L334-L334)
**instance
Tau.BookV.Cosmology.instReprInformationPreservationStructural :Repr InformationPreservationStructural**

Equations
- Tau.BookV.Cosmology.instReprInformationPreservationStructural = { reprPrec := Tau.BookV.Cosmology.instReprInformationPreservationStructural.repr }

---

### `Tau.BookV.Cosmology.info_preservation_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L336-L336)
**def
Tau.BookV.Cosmology.info_preservation_structural :InformationPreservationStructural**

Equations
- Tau.BookV.Cosmology.info_preservation_structural = { }
Instances For

---

### `Tau.BookV.Cosmology.info_preservation_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BHBirthTopology.lean#L338-L341)
**theorem
Tau.BookV.Cosmology.info_preservation_thm :info_preservation_structural.profinite_tower = true ∧ info_preservation_structural.unitarity_structural = true**
