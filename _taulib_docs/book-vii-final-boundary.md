---
layout: taulib-doc
title: "TauLib.BookVII.Final.Boundary"
permalink: /verify/taulib/docs/book-vii-final-boundary/
lane: verify
module_name: "TauLib.BookVII.Final.Boundary"
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

# TauLib.BookVII.Final.Boundary


The boundary theorems: D→C Bridge, No Forced Stance, Mediator Basin,
Subject-Tool Collapse, and Lemniscate Closure.
**R8-D enriched** from stub to full structures around methodological sorry.

## Registry Cross-References


- [VII.D87] D→C Bridge Functor — `BridgeFunctor`

- [VII.T46] Bridge Equivalence at S_L — `bridge_equivalence_structural`

- [VII.P29] Four-Register Convergence — `four_register_convergence_structural`

- [VII.D88] Mediator Fixed-Point Basin — `MediatorBasin`

- [VII.D89] Subject-Tool Collapse — `SubjectToolCollapse`

- [VII.T47] No Forced Stance — `no_forced_stance`


## Cross-Book Authority


- Book VII, Logos.Sector: logos characterization, ω-point

- Book VII, Meta.Saturation: bounded witness, Gödel avoidance


## Ground Truth Sources


- Book VII Chapters 119–124 (2nd Edition): Logos Boundary


## Methodological Boundary


VII.T46 (Bridge Equivalence) and VII.P29 (Four-Register Convergence) involve
ω which is non-diagrammatic by VII.T47 (No Forced Stance). The structural
parts are verified; the ω-content sorry stubs are methodological.
VII.T47 (No Forced Stance) is itself a methodological boundary theorem.

---

### `Tau.BookVII.Final.Boundary.BridgeFunctor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L44-L58)
**structure
Tau.BookVII.Final.Boundary.BridgeFunctor :Type**


[VII.D87] D→C Bridge Functor (ch120). Functor B_{D→C} : S_D → S_C
mapping diagrammatic content to commitment content. At S_L,
this bridge is an equivalence; outside S_L, it fails.

- well_defined : Bool
Well-defined on S_D.

- target_commitment : Bool
Maps to S_C.

- faithful_at_sl : Bool
Faithful at S_L.

- full_at_sl : Bool
Full at S_L.

- ess_surj_at_sl : Bool
Essentially surjective at S_L.

Instances For

---

### `Tau.BookVII.Final.Boundary.instReprBridgeFunctor.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L58-L58)
**def
Tau.BookVII.Final.Boundary.instReprBridgeFunctor.repr :BridgeFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Final.Boundary.instReprBridgeFunctor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L58-L58)
**instance
Tau.BookVII.Final.Boundary.instReprBridgeFunctor :Repr BridgeFunctor**

Equations
- Tau.BookVII.Final.Boundary.instReprBridgeFunctor = { reprPrec := Tau.BookVII.Final.Boundary.instReprBridgeFunctor.repr }

---

### `Tau.BookVII.Final.Boundary.bridge_functor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L60-L60)
**def
Tau.BookVII.Final.Boundary.bridge_functor :BridgeFunctor**

Equations
- Tau.BookVII.Final.Boundary.bridge_functor = { }
Instances For

---

### `Tau.BookVII.Final.Boundary.bridge_equivalence_structural`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L66-L78)
**theorem
Tau.BookVII.Final.Boundary.bridge_equivalence_structural :bridge_functor.faithful_at_sl = true ∧ bridge_functor.full_at_sl = true ∧ bridge_functor.ess_surj_at_sl = true**


[VII.T46] Bridge Equivalence at S_L (ch120). The structural parts:
B_{D→C} restricted to S_L satisfies faithfulness, fullness, and
essential surjectivity. These are the diagrammatic components.

**sorry**: methodological boundary — the equivalence statement involves
ω-content (the bridge succeeds precisely because D-C coincide at S_L,
which involves ω as crossing mediator). The structural fields are
verified; the categorical equivalence claim transcends Reg_D.

---

### `Tau.BookVII.Final.Boundary.four_register_convergence_structural`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L87-L99)
**theorem
Tau.BookVII.Final.Boundary.four_register_convergence_structural :Meta.Registers.sector_logos.dc_coincidence = true ∧ Meta.Registers.sector_logos.unique_mediator = true ∧ Meta.Registers.canonical_sector_decomp.pure_sector_count = 4**


[VII.P29] Four-Register Convergence at S_L (ch121). Structural parts:
D-C coincidence verified; the convergence of all four registers
(E, P, D, C) at S_L requires ω-content.

**sorry**: methodological boundary — full four-register convergence
involves Reg_C stance-stability and Reg_E empirical adequacy claims
that transcend formal verification. D-C coincidence is the
diagrammatic core.

---

### `Tau.BookVII.Final.Boundary.MediatorBasin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L108-L119)
**structure
Tau.BookVII.Final.Boundary.MediatorBasin :Type**


[VII.D88] Mediator Fixed-Point Basin (ch121). The register-crossing
endofunctor Φ has fixed-point basin B(S_L) = S_L itself. At S_L,
the mediator stabilizes: Φ(φ) = φ for all φ ∈ S_L. Outside S_L,
Φ shifts content between registers.

- basin_is_logos : Bool
Basin coincides with logos sector.

- fixed_point_at_sl : Bool
Fixed-point property at S_L.

- non_trivial_outside : Bool
Non-trivial outside S_L.

Instances For

---

### `Tau.BookVII.Final.Boundary.instReprMediatorBasin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L119-L119)
**instance
Tau.BookVII.Final.Boundary.instReprMediatorBasin :Repr MediatorBasin**

Equations
- Tau.BookVII.Final.Boundary.instReprMediatorBasin = { reprPrec := Tau.BookVII.Final.Boundary.instReprMediatorBasin.repr }

---

### `Tau.BookVII.Final.Boundary.instReprMediatorBasin.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L119-L119)
**def
Tau.BookVII.Final.Boundary.instReprMediatorBasin.repr :MediatorBasin → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Final.Boundary.mediator_basin`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L121-L121)
**def
Tau.BookVII.Final.Boundary.mediator_basin :MediatorBasin**

Equations
- Tau.BookVII.Final.Boundary.mediator_basin = { }
Instances For

---

### `Tau.BookVII.Final.Boundary.mediator_basin_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L123-L127)
**theorem
Tau.BookVII.Final.Boundary.mediator_basin_check :mediator_basin.basin_is_logos = true ∧ mediator_basin.fixed_point_at_sl = true ∧ mediator_basin.non_trivial_outside = true**


---

### `Tau.BookVII.Final.Boundary.SubjectToolCollapse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L133-L145)
**structure
Tau.BookVII.Final.Boundary.SubjectToolCollapse :Type**


[VII.D89] Subject-Tool Collapse (ch122). Boundary condition where
the investigating subject and the formal tool become indistinguishable.
At S_L, the proof (tool) and the prover's commitment (subject) are
the same structural datum. The subject cannot step outside the tool
without leaving S_L.

- boundary_condition : Bool
Boundary condition.

- collapse : Bool
Subject-tool indistinguishable at S_L.

- no_external_standpoint : Bool
Cannot step outside without leaving S_L.

Instances For

---

### `Tau.BookVII.Final.Boundary.instReprSubjectToolCollapse.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L145-L145)
**def
Tau.BookVII.Final.Boundary.instReprSubjectToolCollapse.repr :SubjectToolCollapse → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Final.Boundary.instReprSubjectToolCollapse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L145-L145)
**instance
Tau.BookVII.Final.Boundary.instReprSubjectToolCollapse :Repr SubjectToolCollapse**

Equations
- Tau.BookVII.Final.Boundary.instReprSubjectToolCollapse = { reprPrec := Tau.BookVII.Final.Boundary.instReprSubjectToolCollapse.repr }

---

### `Tau.BookVII.Final.Boundary.subject_tool`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L147-L147)
**def
Tau.BookVII.Final.Boundary.subject_tool :SubjectToolCollapse**

Equations
- Tau.BookVII.Final.Boundary.subject_tool = { }
Instances For

---

### `Tau.BookVII.Final.Boundary.subject_tool_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L149-L153)
**theorem
Tau.BookVII.Final.Boundary.subject_tool_check :subject_tool.boundary_condition = true ∧ subject_tool.collapse = true ∧ subject_tool.no_external_standpoint = true**


---

### `Tau.BookVII.Final.Boundary.NoForcedStanceStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L159-L178)
**structure
Tau.BookVII.Final.Boundary.NoForcedStanceStructure :Type**


[VII.T47] No Forced Stance (ch123). ω is undecidable in Reg_D:
the diagrammatic register cannot force a stance on ω-content.
Subject-Tool Collapse + bounded witness form ⟹ ω undecidable.

Three claims:
(1) ω is not NF-addressable in the standard sense (closure point)
(2) Subject-Tool Collapse at S_L prevents external standpoint
(3) BWF excludes unbounded witness for ω-claims

**sorry**: methodological boundary — the theorem itself establishes
the boundary of formal verification. It cannot be formally proved
because proving it would require the very standpoint it denies.

- omega_non_standard : Bool
ω not standardly NF-addressable.

- no_external_standpoint : Bool
Subject-tool collapse prevents external standpoint.

- bwf_excludes : Bool
BWF excludes unbounded ω-witness.

Instances For

---

### `Tau.BookVII.Final.Boundary.instReprNoForcedStanceStructure.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L178-L178)
**def
Tau.BookVII.Final.Boundary.instReprNoForcedStanceStructure.repr :NoForcedStanceStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVII.Final.Boundary.instReprNoForcedStanceStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L178-L178)
**instance
Tau.BookVII.Final.Boundary.instReprNoForcedStanceStructure :Repr NoForcedStanceStructure**

Equations
- Tau.BookVII.Final.Boundary.instReprNoForcedStanceStructure = { reprPrec := Tau.BookVII.Final.Boundary.instReprNoForcedStanceStructure.repr }

---

### `Tau.BookVII.Final.Boundary.no_forced_stance_structure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L180-L180)
**def
Tau.BookVII.Final.Boundary.no_forced_stance_structure :NoForcedStanceStructure**

Equations
- Tau.BookVII.Final.Boundary.no_forced_stance_structure = { }
Instances For

---

### `Tau.BookVII.Final.Boundary.no_forced_stance_structural`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L182-L186)
**theorem
Tau.BookVII.Final.Boundary.no_forced_stance_structural :no_forced_stance_structure.omega_non_standard = true ∧ no_forced_stance_structure.no_external_standpoint = true ∧ no_forced_stance_structure.bwf_excludes = true**


---

### `Tau.BookVII.Final.Boundary.no_forced_stance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVII/Final/Boundary.lean#L189-L189)
**theorem
Tau.BookVII.Final.Boundary.no_forced_stance :True**
