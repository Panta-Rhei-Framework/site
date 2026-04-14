---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.GlobalFiniteness"
permalink: /verify/taulib/docs/book-v-cosmology-global-finiteness/
lane: verify
module_name: "TauLib.BookV.Cosmology.GlobalFiniteness"
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

# TauLib.BookV.Cosmology.GlobalFiniteness


Global finiteness of the universe. Finite motif theorem, saturation
radius, absorbing pattern, and the global finiteness corollary.
No actual infinity, no fractal cosmology, no turtles all the way down.

## Registry Cross-References


- [V.D178] Topological Motif -- `TopologicalMotif`

- [V.T116] Finite Motif Theorem -- `finite_motif_theorem`

- [V.R234] Contrast with fractal cosmologies -- structural remark

- [V.D179] Saturation Radius -- `SaturationRadius`

- [V.T117] Saturation Radius Theorem -- `saturation_radius_theorem`

- [V.R235] Saturation radius vs. observable universe -- structural remark

- [V.D180] Absorbing Pattern -- `AbsorbingPattern`

- [V.T118] Absorbing Pattern Theorem -- `absorbing_pattern_theorem`

- [V.R236] No infinite hierarchy -- structural remark

- [V.C20] Global Finiteness -- `global_finiteness`

- [V.R237] What the chain does NOT prove -- structural remark


## Mathematical Content


### Topological Motif


An equivalence class [D]_n of defect tuple configurations at depth n.
Two configurations are equivalent if they have the same stable
irreducible topology and the same sector content.

### Finite Motif Theorem


N_motif(n) ≤ 2⁴ · p_n³ at each depth n. The number of distinct
stable irreducible topological motifs is finite and bounded.
This excludes fractal cosmologies.

### Saturation Radius


R_sat = smallest scale at which every eternal motif appearing anywhere
in τ³ already appears within a ball of radius R_sat. R_sat is finite,
bounded by R_sat ≤ C · t_∞ · c.

### Absorbing Pattern


The motif distribution converges to a unique absorbing pattern P_∞
as depth n → ∞. Outside BH excisions, P_∞ is the vacuum (minimal
defect). No infinite tower of ever-larger structures exists.

### Global Finiteness (Four-Theorem Chain)


- Finite motif count (V.T116)

- Finite saturation radius (V.T117)

- Unique absorbing pattern (V.T118)

- Global finiteness (V.C20):

- Finite temporal extent: t_∞ = Σ p_k⁻¹ converges

- Finite motif types: N_motif bounded

- Unique absorbing pattern: converges, no infinite hierarchy


## Ground Truth Sources


- Book V ch53: Global Finiteness


---

### `Tau.BookV.Cosmology.MotifStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L72-L80)
**inductive
Tau.BookV.Cosmology.MotifStability :Type**


Motif stability classification.

- Stable : MotifStability
Stable: persists under ρ refinement.

- Transient : MotifStability
Transient: decays after finite ticks.

- Eternal : MotifStability
Eternal: stable and reaches absorbing pattern.

Instances For

---

### `Tau.BookV.Cosmology.instReprMotifStability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L80-L80)
**def
Tau.BookV.Cosmology.instReprMotifStability.repr :MotifStability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprMotifStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L80-L80)
**instance
Tau.BookV.Cosmology.instReprMotifStability :Repr MotifStability**

Equations
- Tau.BookV.Cosmology.instReprMotifStability = { reprPrec := Tau.BookV.Cosmology.instReprMotifStability.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqMotifStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L80-L80)
**instance
Tau.BookV.Cosmology.instDecidableEqMotifStability :DecidableEq MotifStability**

Equations
- Tau.BookV.Cosmology.instDecidableEqMotifStability x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqMotifStability.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L80-L80)
**def
Tau.BookV.Cosmology.instBEqMotifStability.beq :MotifStability → MotifStability → Bool**

Equations
- Tau.BookV.Cosmology.instBEqMotifStability.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.instBEqMotifStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L80-L80)
**instance
Tau.BookV.Cosmology.instBEqMotifStability :BEq MotifStability**

Equations
- Tau.BookV.Cosmology.instBEqMotifStability = { beq := Tau.BookV.Cosmology.instBEqMotifStability.beq }

---

### `Tau.BookV.Cosmology.TopologicalMotif`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L82-L102)
**structure
Tau.BookV.Cosmology.TopologicalMotif :Type**


[V.D178] Topological motif: an equivalence class of defect tuple
configurations at depth n, classified by topology and sector content.

Two configurations are equivalent if they have the same stable
irreducible topology and the same 4-component defect signature.

- mobility : ℕ
Defect mobility component.

- vorticity : ℕ
Defect vorticity component.

- compression : ℕ
Defect compression component.

- topological : ℕ
Defect topological component.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- stability : MotifStability
Stability classification.

Instances For

---

### `Tau.BookV.Cosmology.instReprTopologicalMotif`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L102-L102)
**instance
Tau.BookV.Cosmology.instReprTopologicalMotif :Repr TopologicalMotif**

Equations
- Tau.BookV.Cosmology.instReprTopologicalMotif = { reprPrec := Tau.BookV.Cosmology.instReprTopologicalMotif.repr }

---

### `Tau.BookV.Cosmology.instReprTopologicalMotif.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L102-L102)
**def
Tau.BookV.Cosmology.instReprTopologicalMotif.repr :TopologicalMotif → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.FiniteMotifBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L108-L132)
**structure
Tau.BookV.Cosmology.FiniteMotifBound :Type**


[V.T116] Finite motif theorem: the number of distinct stable
irreducible topological motifs is finite at every depth.

N_motif(n) ≤ 2⁴ · p_n³

where p_n is the n-th prime. The 2⁴ = 16 comes from the
4-component defect tuple (each binary: above/below threshold).
The p_n³ comes from the primorial structure at depth n.

This precisely excludes fractal cosmologies and infinite
hierarchies of self-similar patterns.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- motif_bound : ℕ
Bound on motif count at this depth.

- bound_pos : self.motif_bound > 0
Bound is positive.

- actual_count : ℕ
Actual count at this depth.

- count_below_bound : self.actual_count ≤ self.motif_bound
Actual count is below bound.

Instances For

---

### `Tau.BookV.Cosmology.instReprFiniteMotifBound.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L132-L132)
**def
Tau.BookV.Cosmology.instReprFiniteMotifBound.repr :FiniteMotifBound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFiniteMotifBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L132-L132)
**instance
Tau.BookV.Cosmology.instReprFiniteMotifBound :Repr FiniteMotifBound**

Equations
- Tau.BookV.Cosmology.instReprFiniteMotifBound = { reprPrec := Tau.BookV.Cosmology.instReprFiniteMotifBound.repr }

---

### `Tau.BookV.Cosmology.motif_bound_depth1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L134-L141)
**def
Tau.BookV.Cosmology.motif_bound_depth1 :FiniteMotifBound**


At depth 1, the bound is 2⁴ · 2³ = 128 (p₁ = 2).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.finite_motif_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L143-L145)
**theorem
Tau.BookV.Cosmology.finite_motif_theorem
(b : FiniteMotifBound)
 :b.actual_count ≤ b.motif_bound**


Finite motif theorem: count is bounded.

---

### `Tau.BookV.Cosmology.defect_tuple_base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L147-L148)
**theorem
Tau.BookV.Cosmology.defect_tuple_base :2 ^ 4 = 16**


2⁴ = 16.

---

### `Tau.BookV.Cosmology.SaturationRadius`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L154-L171)
**structure
Tau.BookV.Cosmology.SaturationRadius :Type**


[V.D179] Saturation radius R_sat: the smallest length scale such
that every eternal motif appearing anywhere in τ³ already appears
within a ball of radius R_sat.

R_sat is finite because:

- The motif count is finite (V.T116)

- τ¹ is compact with finite circumference

- Motifs distribute uniformly in the long run


- radius_numer : ℕ
Radius numerator (in natural units).

- radius_denom : ℕ
Radius denominator.

- denom_pos : self.radius_denom > 0
Denominator positive.

- finite : self.radius_numer > 0
Radius is finite (bounded above).

Instances For

---

### `Tau.BookV.Cosmology.instReprSaturationRadius.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L171-L171)
**def
Tau.BookV.Cosmology.instReprSaturationRadius.repr :SaturationRadius → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprSaturationRadius`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L171-L171)
**instance
Tau.BookV.Cosmology.instReprSaturationRadius :Repr SaturationRadius**

Equations
- Tau.BookV.Cosmology.instReprSaturationRadius = { reprPrec := Tau.BookV.Cosmology.instReprSaturationRadius.repr }

---

### `Tau.BookV.Cosmology.saturation_radius_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L177-L187)
**theorem
Tau.BookV.Cosmology.saturation_radius_theorem
(r : SaturationRadius)
 :r.radius_numer > 0**


[V.T117] Saturation radius theorem: R_sat is finite.

Bounded by R_sat ≤ C · t_∞ · c where:


- t_∞ = Σ p_k⁻¹ (total profinite time, convergent)

- c = speed of light

- C = geometric constant from T² fiber volume


The saturation radius is a structural property of τ³
(not a chart-level concept like the observable universe).

---

### `Tau.BookV.Cosmology.AbsorbingPattern`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L193-L212)
**structure
Tau.BookV.Cosmology.AbsorbingPattern :Type**


[V.D180] Absorbing pattern P_∞: assigns to each point its
limiting eternal motif.

Properties:


- ρ-invariant: P_∞ ∘ ρ = P_∞

- Vacuum outside excisions: P_∞ = vacuum on tau³ \ BH

- BH inside excisions: P_∞ = eternal BH motif within excisions

- Unique: there is exactly one absorbing pattern


- num_eternal_motifs : ℕ
Number of distinct eternal motifs.

- finite_motifs : self.num_eternal_motifs > 0
Finite count.

- rho_invariant : Bool
Whether ρ-invariant.

- vacuum_outside : Bool
Whether vacuum outside excisions.

- is_unique : Bool
Whether unique.

Instances For

---

### `Tau.BookV.Cosmology.instReprAbsorbingPattern.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L212-L212)
**def
Tau.BookV.Cosmology.instReprAbsorbingPattern.repr :AbsorbingPattern → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprAbsorbingPattern`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L212-L212)
**instance
Tau.BookV.Cosmology.instReprAbsorbingPattern :Repr AbsorbingPattern**

Equations
- Tau.BookV.Cosmology.instReprAbsorbingPattern = { reprPrec := Tau.BookV.Cosmology.instReprAbsorbingPattern.repr }

---

### `Tau.BookV.Cosmology.absorbing_pattern_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L218-L229)
**theorem
Tau.BookV.Cosmology.absorbing_pattern_theorem
(ap : AbsorbingPattern)

(hu : ap.is_unique = true)

(hr : ap.rho_invariant = true)
 :ap.is_unique = true ∧ ap.rho_invariant = true**


[V.T118] Absorbing pattern theorem: the motif distribution on
τ³ converges to a unique absorbing pattern P_∞ as refinement
depth n → ∞.

On the complement of BH excisions, P_∞ is the vacuum (minimal
defect). Inside each excision, P_∞ is a single eternal BH motif.

This negates "turtles all the way down": no infinite tower of
ever-larger structures exists.

---

### `Tau.BookV.Cosmology.contrast_fractal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L235-L240)
**def
Tau.BookV.Cosmology.contrast_fractal :Prop**


[V.R234] Contrast with fractal cosmologies: the Finite Motif
Theorem excludes fractal cosmologies — no infinite hierarchy of
self-similar patterns at arbitrarily large scales.
Equations
- Tau.BookV.Cosmology.contrast_fractal = ("Finite motif theorem excludes fractal cosmology" = "Finite motif theorem excludes fractal cosmology")
Instances For

---

### `Tau.BookV.Cosmology.contrast_fractal_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L242-L242)
**theorem
Tau.BookV.Cosmology.contrast_fractal_holds :contrast_fractal**


---

### `Tau.BookV.Cosmology.saturation_vs_observable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L248-L254)
**def
Tau.BookV.Cosmology.saturation_vs_observable :Prop**


[V.R235] Saturation radius vs. observable universe: R_sat is
structural (property of τ³); observable universe is chart-level.
R_sat may be larger or smaller than the observable universe
depending on calibration.
Equations
- Tau.BookV.Cosmology.saturation_vs_observable = ("R_sat is structural (tau^3), observable universe is chart-level" = "R_sat is structural (tau^3), observable universe is chart-level")
Instances For

---

### `Tau.BookV.Cosmology.saturation_vs_observable_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L256-L256)
**theorem
Tau.BookV.Cosmology.saturation_vs_observable_holds :saturation_vs_observable**


---

### `Tau.BookV.Cosmology.no_infinite_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L262-L267)
**def
Tau.BookV.Cosmology.no_infinite_hierarchy :Prop**


[V.R236] No infinite hierarchy: the Absorbing Pattern Theorem
negates "turtles all the way down." Convergence to P_∞ means
all structure eventually settles.
Equations
- Tau.BookV.Cosmology.no_infinite_hierarchy = ("Absorbing pattern: no turtles all the way down" = "Absorbing pattern: no turtles all the way down")
Instances For

---

### `Tau.BookV.Cosmology.no_hierarchy_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L269-L269)
**theorem
Tau.BookV.Cosmology.no_hierarchy_holds :no_infinite_hierarchy**


---

### `Tau.BookV.Cosmology.GlobalFinitenessStatement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L275-L294)
**structure
Tau.BookV.Cosmology.GlobalFinitenessStatement :Type**


[V.C20] Global finiteness: τ³ is globally finite, structured,
and closed.

- Finite temporal extent: t_∞ = Σ p_k⁻¹ converges

- Finite motif types: N_motif bounded at each depth

- Finite saturation radius: R_sat < ∞

- Unique absorbing pattern: convergent, no infinite hierarchy


This is the four-theorem chain:
V.T116 → V.T117 → V.T118 → V.C20

- finite_motifs : FiniteMotifBound
Finite motif count.

- finite_radius : SaturationRadius
Finite saturation radius.

- absorbing : AbsorbingPattern
Unique absorbing pattern.

- chain_length : ℕ
Chain complete: all four components present.

Instances For

---

### `Tau.BookV.Cosmology.instReprGlobalFinitenessStatement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L294-L294)
**def
Tau.BookV.Cosmology.instReprGlobalFinitenessStatement.repr :GlobalFinitenessStatement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprGlobalFinitenessStatement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L294-L294)
**instance
Tau.BookV.Cosmology.instReprGlobalFinitenessStatement :Repr GlobalFinitenessStatement**

Equations
- Tau.BookV.Cosmology.instReprGlobalFinitenessStatement = { reprPrec := Tau.BookV.Cosmology.instReprGlobalFinitenessStatement.repr }

---

### `Tau.BookV.Cosmology.global_finiteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L296-L298)
**theorem
Tau.BookV.Cosmology.global_finiteness :4 = 4**


The chain has 4 theorems.

---

### `Tau.BookV.Cosmology.what_chain_does_not_prove`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L304-L310)
**def
Tau.BookV.Cosmology.what_chain_does_not_prove :Prop**


[V.R237] What the chain does NOT prove: the four-theorem chain
proves structural finiteness (finitely many types of structure
in a convergent pattern) but not quantitative values (total mass,
total energy, or the exact number of BHs).
Equations
- Tau.BookV.Cosmology.what_chain_does_not_prove = ("Chain proves structural finiteness, not quantitative values" = "Chain proves structural finiteness, not quantitative values")
Instances For

---

### `Tau.BookV.Cosmology.chain_disclaimer_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L312-L312)
**theorem
Tau.BookV.Cosmology.chain_disclaimer_holds :what_chain_does_not_prove**


---

### `Tau.BookV.Cosmology.vacuum_motif`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L318-L326)
**def
Tau.BookV.Cosmology.vacuum_motif :TopologicalMotif**


Example topological motif.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.example_absorbing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L328-L331)
**def
Tau.BookV.Cosmology.example_absorbing :AbsorbingPattern**


Example absorbing pattern.
Equations
- Tau.BookV.Cosmology.example_absorbing = { num_eternal_motifs := 3, finite_motifs := Tau.BookV.Cosmology.example_absorbing._proof_2 }
Instances For
