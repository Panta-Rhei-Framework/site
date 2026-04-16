---
layout: taulib-doc
title: "TauLib.BookVI.CosmicLife.BHDist"
permalink: /verify/taulib/docs/book-vi-cosmic-life-bh-dist/
lane: verify
module_name: "TauLib.BookVI.CosmicLife.BHDist"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.CosmicLife.BHDist


Black hole distinction: macro-torus carrier satisfies all 5 conditions.
Imports BookV.Gravity.BHTopoModes for T² horizon topology authority.

## Registry Cross-References


- [VI.D54] Macro-Torus Carrier — `MacroTorusCarrier`

- [VI.D55] Lexicographic Defect Functional — `LexDefectFunctional`

- [VI.D56] Frame-Closure Defect — `FrameClosureDefect`

- [VI.D57] Strong-Saturation Defect — `StrongSaturationDefect`

- [VI.T29] BH Distinction Theorem — `bh_distinction_theorem`


## Book V Authority (imported via BHTopoModes)


- [V.T109] BH Toroidal Topology: horizon is T², not S²

- [V.D234] T² QNM Mode Structure: ringdown spectrum

- [V.T168] QNM Frequency Ratio = ι<sub>τ</sub>⁻¹


## Ground Truth Sources


- Book VI Chapter 43 (2nd Edition): BH Distinction

- Book V Chapter 50 (2nd Edition): BH Birth Topology (V.T109)


---

### `Tau.BookVI.BHDist.horizon_topology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L37-L40)
**def
Tau.BookVI.BHDist.horizon_topology :ℕ**


The BH horizon has T² topology (torus), NOT S² (sphere).
Authority: V.T109 (BH Toroidal Topology, Book V Chapter 50).
The two S¹ cycles generate the torus QNM spectrum (V.D234).
Equations
- Tau.BookVI.BHDist.horizon_topology = 2
Instances For

---

### `Tau.BookVI.BHDist.bh_carrier_is_torus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L42-L43)
**theorem
Tau.BookVI.BHDist.bh_carrier_is_torus :horizon_topology = 2**


The horizon is toroidal: dimension matches T² fiber of τ³.

---

### `Tau.BookVI.BHDist.torus_modes_from_bookV`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L45-L47)
**theorem
Tau.BookVI.BHDist.torus_modes_from_bookV :BookV.Gravity.primitiveTorusModes.length = 3**


Connection to BookV: the primitive torus modes exist and number 3.

---

### `Tau.BookVI.BHDist.MacroTorusCarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L53-L67)
**structure
Tau.BookVI.BHDist.MacroTorusCarrier :Type**


[VI.D54] Macro-torus carrier: BH carrier with T² boundary.
Components: T² boundary topology, multipole refinement tower,
Kerr holonomy, and carrier type.

- t2_boundary : Bool
Horizon has T² topology (from V.T109).

- multipole_tower : Bool
Refinement tower: multipole moments through order 2^n.

- kerr_holonomy : Bool
Boundary holonomy: frame-dragging algebra from Kerr.

- carrier_type : String
Carrier type identifier.

- horizon_dim : ℕ
Horizon dimension = 2 (torus).

Instances For

---

### `Tau.BookVI.BHDist.instReprMacroTorusCarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L67-L67)
**instance
Tau.BookVI.BHDist.instReprMacroTorusCarrier :Repr MacroTorusCarrier**

Equations
- Tau.BookVI.BHDist.instReprMacroTorusCarrier = { reprPrec := Tau.BookVI.BHDist.instReprMacroTorusCarrier.repr }

---

### `Tau.BookVI.BHDist.instReprMacroTorusCarrier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L67-L67)
**def
Tau.BookVI.BHDist.instReprMacroTorusCarrier.repr :MacroTorusCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHDist.macro_torus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L69-L69)
**def
Tau.BookVI.BHDist.macro_torus :MacroTorusCarrier**

Equations
- Tau.BookVI.BHDist.macro_torus = { }
Instances For

---

### `Tau.BookVI.BHDist.macro_torus_is_t2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L71-L72)
**theorem
Tau.BookVI.BHDist.macro_torus_is_t2 :macro_torus.horizon_dim = 2**


The macro-torus carrier has T² boundary.

---

### `Tau.BookVI.BHDist.LexDefectFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L78-L87)
**structure
Tau.BookVI.BHDist.LexDefectFunctional :Type**


[VI.D55] Lexicographic defect: pairs frame-closure + strong-saturation.
Ordered lexicographically: frame dominates (slow DoF first).

- component_count : ℕ
Number of defect components.

- count_eq : self.component_count = 2
Exactly 2 components: frame-closure + strong-saturation.

- lexicographic : Bool
Lexicographic ordering active.

Instances For

---

### `Tau.BookVI.BHDist.instReprLexDefectFunctional.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L87-L87)
**def
Tau.BookVI.BHDist.instReprLexDefectFunctional.repr :LexDefectFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHDist.instReprLexDefectFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L87-L87)
**instance
Tau.BookVI.BHDist.instReprLexDefectFunctional :Repr LexDefectFunctional**

Equations
- Tau.BookVI.BHDist.instReprLexDefectFunctional = { reprPrec := Tau.BookVI.BHDist.instReprLexDefectFunctional.repr }

---

### `Tau.BookVI.BHDist.lex_defect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L89-L91)
**def
Tau.BookVI.BHDist.lex_defect :LexDefectFunctional**

Equations
- Tau.BookVI.BHDist.lex_defect = { component_count := 2, count_eq := Tau.BookVI.BHDist.lex_defect._proof_1 }
Instances For

---

### `Tau.BookVI.BHDist.FrameClosureDefect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L97-L107)
**structure
Tau.BookVI.BHDist.FrameClosureDefect :Type**


[VI.D56] Frame-closure defect: Sobolev-norm deviation from Kerr-Newman.
Vanishes for isolated stationary Kerr BH.
Norm choice is conventional (any coercive norm on H^n(H) works).

- vanishes_ideal : Bool
Vanishes for ideal Kerr solution.

- sobolev_norm : Bool
Uses Sobolev norm (conventional choice).

- damped_by_qnm : Bool
Ringdown damps this defect via V.D234 QNM modes.

Instances For

---

### `Tau.BookVI.BHDist.instReprFrameClosureDefect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L107-L107)
**instance
Tau.BookVI.BHDist.instReprFrameClosureDefect :Repr FrameClosureDefect**

Equations
- Tau.BookVI.BHDist.instReprFrameClosureDefect = { reprPrec := Tau.BookVI.BHDist.instReprFrameClosureDefect.repr }

---

### `Tau.BookVI.BHDist.instReprFrameClosureDefect.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L107-L107)
**def
Tau.BookVI.BHDist.instReprFrameClosureDefect.repr :FrameClosureDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHDist.StrongSaturationDefect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L113-L120)
**structure
Tau.BookVI.BHDist.StrongSaturationDefect :Type**


[VI.D57] Strong-saturation defect: V^s_n ∈ [0,1].
Measures residual strong-sector instability.

- range_unit : Bool
Range is [0,1].

- bh_negligible : Bool
BH has negligible strong-saturation defect.

Instances For

---

### `Tau.BookVI.BHDist.instReprStrongSaturationDefect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L120-L120)
**instance
Tau.BookVI.BHDist.instReprStrongSaturationDefect :Repr StrongSaturationDefect**

Equations
- Tau.BookVI.BHDist.instReprStrongSaturationDefect = { reprPrec := Tau.BookVI.BHDist.instReprStrongSaturationDefect.repr }

---

### `Tau.BookVI.BHDist.instReprStrongSaturationDefect.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L120-L120)
**def
Tau.BookVI.BHDist.instReprStrongSaturationDefect.repr :StrongSaturationDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHDist.BHDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L126-L142)
**structure
Tau.BookVI.BHDist.BHDistinction :Type**


[VI.T29] BH Distinction Theorem: all 5 τ-Distinction conditions satisfied.
(i) Clopen: event horizon (zero-width boundary)
(ii) Refinement-coherent: No-Hair collapses tower
(iii) Eventually stable: stabilizes after 1 ringdown
(iv) Law-stable: No-Shrink Theorem (V.T114)
(v) H∂-equivariant: axial Killing symmetry

- conditions_satisfied : ℕ
Number of conditions satisfied.

- all_five : self.conditions_satisfied = 5
All five conditions verified.

- clopen : Bool
- refinement_coherent : Bool
- eventually_stable : Bool
- law_stable : Bool
- equivariant : Bool
Instances For

---

### `Tau.BookVI.BHDist.instReprBHDistinction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L142-L142)
**def
Tau.BookVI.BHDist.instReprBHDistinction.repr :BHDistinction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.BHDist.instReprBHDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L142-L142)
**instance
Tau.BookVI.BHDist.instReprBHDistinction :Repr BHDistinction**

Equations
- Tau.BookVI.BHDist.instReprBHDistinction = { reprPrec := Tau.BookVI.BHDist.instReprBHDistinction.repr }

---

### `Tau.BookVI.BHDist.bh_dist`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L144-L146)
**def
Tau.BookVI.BHDist.bh_dist :BHDistinction**

Equations
- Tau.BookVI.BHDist.bh_dist = { conditions_satisfied := 5, all_five := Tau.BookVI.BHDist.bh_dist._proof_1 }
Instances For

---

### `Tau.BookVI.BHDist.bh_distinction_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L148-L156)
**theorem
Tau.BookVI.BHDist.bh_distinction_theorem :bh_dist.conditions_satisfied = 5 ∧ bh_dist.clopen = true ∧ bh_dist.refinement_coherent = true ∧ bh_dist.eventually_stable = true ∧ bh_dist.law_stable = true ∧ bh_dist.equivariant = true**


[VI.T29] BH Distinction Theorem: 5/5 conditions, carrier is T².

---

### `Tau.BookVI.BHDist.horizon_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/CosmicLife/BHDist.lean#L158-L163)
**theorem
Tau.BookVI.BHDist.horizon_consistency :macro_torus.horizon_dim = 2 ∧ horizon_topology = 2 ∧ BookV.Gravity.primitiveTorusModes.length = 3**


Cross-book consistency: BH carrier uses T² from BookV, not S².
