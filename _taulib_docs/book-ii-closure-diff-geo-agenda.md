---
layout: taulib-doc
title: "TauLib.BookII.Closure.DiffGeoAgenda"
permalink: /verify/taulib/docs/book-ii-closure-diff-geo-agenda/
lane: verify
module_name: "TauLib.BookII.Closure.DiffGeoAgenda"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Closure.DiffGeoAgenda


Forward declarations for differential-geometric structures that Book III
will earn. This module records the E1-layer completion and declares
placeholder structures for connections, curvature, and holonomy.

## Registry Cross-References


- [II.R21] Diff-Geo Agenda -- forward declarations

- [II.R22] Book III Prerequisites -- E1 layer completeness


## Mathematical Content


**II.R21 (Diff-Geo Agenda):** Book II earns the tau-manifold structure
(atlas + exterior derivative). Book III will earn:


- Connections: parallel transport along paths in the primorial tower

- Curvature: the obstruction to flat parallel transport

- Holonomy: the monodromy of closed paths

- Cohomology: de Rham-type cohomology via d_tau


These are NOT earned in Book II. This module provides forward declarations
with `Bool` witnesses that record they are NOT yet established.

**II.R22 (Book III Prerequisites):** The E1 layer must be complete before
Book III can begin the E2 enrichment. This module verifies E1 completeness
by delegating to e1_layer_check.

---

### `Tau.BookII.Closure.ConnectionPlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L45-L51)
**structure
Tau.BookII.Closure.ConnectionPlaceholder :Type**


[II.R21] Placeholder: connection structure (NOT earned in Book II).
The `earned` field is `false` -- this will become `true` in Book III
when parallel transport is constructed from the E2 enrichment.

- earned : Bool
- description : String
Instances For

---

### `Tau.BookII.Closure.instReprConnectionPlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L51-L51)
**instance
Tau.BookII.Closure.instReprConnectionPlaceholder :Repr ConnectionPlaceholder**

Equations
- Tau.BookII.Closure.instReprConnectionPlaceholder = { reprPrec := Tau.BookII.Closure.instReprConnectionPlaceholder.repr }

---

### `Tau.BookII.Closure.instReprConnectionPlaceholder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L51-L51)
**def
Tau.BookII.Closure.instReprConnectionPlaceholder.repr :ConnectionPlaceholder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqConnectionPlaceholder.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L51-L51)
**def
Tau.BookII.Closure.instDecidableEqConnectionPlaceholder.decEq
(x✝ x✝¹ : ConnectionPlaceholder)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqConnectionPlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L51-L51)
**instance
Tau.BookII.Closure.instDecidableEqConnectionPlaceholder :DecidableEq ConnectionPlaceholder**

Equations
- Tau.BookII.Closure.instDecidableEqConnectionPlaceholder = Tau.BookII.Closure.instDecidableEqConnectionPlaceholder.decEq

---

### `Tau.BookII.Closure.CurvaturePlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L53-L57)
**structure
Tau.BookII.Closure.CurvaturePlaceholder :Type**


[II.R21] Placeholder: curvature structure (NOT earned in Book II).

- earned : Bool
- description : String
Instances For

---

### `Tau.BookII.Closure.instReprCurvaturePlaceholder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L57-L57)
**def
Tau.BookII.Closure.instReprCurvaturePlaceholder.repr :CurvaturePlaceholder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instReprCurvaturePlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L57-L57)
**instance
Tau.BookII.Closure.instReprCurvaturePlaceholder :Repr CurvaturePlaceholder**

Equations
- Tau.BookII.Closure.instReprCurvaturePlaceholder = { reprPrec := Tau.BookII.Closure.instReprCurvaturePlaceholder.repr }

---

### `Tau.BookII.Closure.instDecidableEqCurvaturePlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L57-L57)
**instance
Tau.BookII.Closure.instDecidableEqCurvaturePlaceholder :DecidableEq CurvaturePlaceholder**

Equations
- Tau.BookII.Closure.instDecidableEqCurvaturePlaceholder = Tau.BookII.Closure.instDecidableEqCurvaturePlaceholder.decEq

---

### `Tau.BookII.Closure.instDecidableEqCurvaturePlaceholder.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L57-L57)
**def
Tau.BookII.Closure.instDecidableEqCurvaturePlaceholder.decEq
(x✝ x✝¹ : CurvaturePlaceholder)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.HolonomyPlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L59-L63)
**structure
Tau.BookII.Closure.HolonomyPlaceholder :Type**


[II.R21] Placeholder: holonomy structure (NOT earned in Book II).

- earned : Bool
- description : String
Instances For

---

### `Tau.BookII.Closure.instReprHolonomyPlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L63-L63)
**instance
Tau.BookII.Closure.instReprHolonomyPlaceholder :Repr HolonomyPlaceholder**

Equations
- Tau.BookII.Closure.instReprHolonomyPlaceholder = { reprPrec := Tau.BookII.Closure.instReprHolonomyPlaceholder.repr }

---

### `Tau.BookII.Closure.instReprHolonomyPlaceholder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L63-L63)
**def
Tau.BookII.Closure.instReprHolonomyPlaceholder.repr :HolonomyPlaceholder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqHolonomyPlaceholder.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L63-L63)
**def
Tau.BookII.Closure.instDecidableEqHolonomyPlaceholder.decEq
(x✝ x✝¹ : HolonomyPlaceholder)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqHolonomyPlaceholder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L63-L63)
**instance
Tau.BookII.Closure.instDecidableEqHolonomyPlaceholder :DecidableEq HolonomyPlaceholder**

Equations
- Tau.BookII.Closure.instDecidableEqHolonomyPlaceholder = Tau.BookII.Closure.instDecidableEqHolonomyPlaceholder.decEq

---

### `Tau.BookII.Closure.default_connection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L65-L67)
**def
Tau.BookII.Closure.default_connection :ConnectionPlaceholder**


Default connection placeholder: not earned.
Equations
- Tau.BookII.Closure.default_connection = { earned := false, description := "parallel transport on primorial tower" }
Instances For

---

### `Tau.BookII.Closure.default_curvature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L69-L71)
**def
Tau.BookII.Closure.default_curvature :CurvaturePlaceholder**


Default curvature placeholder: not earned.
Equations
- Tau.BookII.Closure.default_curvature = { earned := false, description := "obstruction to flat parallel transport" }
Instances For

---

### `Tau.BookII.Closure.default_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L73-L75)
**def
Tau.BookII.Closure.default_holonomy :HolonomyPlaceholder**


Default holonomy placeholder: not earned.
Equations
- Tau.BookII.Closure.default_holonomy = { earned := false, description := "monodromy of closed paths in tower" }
Instances For

---

### `Tau.BookII.Closure.diffgeo_not_yet_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L77-L81)
**def
Tau.BookII.Closure.diffgeo_not_yet_earned :Bool**


[II.R21] None of the diff-geo structures are earned yet.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.e1_complete_for_book3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L87-L91)
**def
Tau.BookII.Closure.e1_complete_for_book3
(bound db k_max : Denotation.TauIdx)
 :Bool**


[II.R22] E1 layer completeness check: verify that all E1 components
are present as the starting point for Book III. Delegates to
e1_layer_check from SelfDescribing.lean.
Equations
- Tau.BookII.Closure.e1_complete_for_book3 bound db k_max = Tau.BookII.Enrichment.e1_layer_check bound db k_max
Instances For

---

### `Tau.BookII.Closure.book3_prerequisites_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L93-L104)
**def
Tau.BookII.Closure.book3_prerequisites_check
(db bound k_max : Denotation.TauIdx)
 :Bool**


[II.R22] Full prerequisites check for Book III:

- E1 layer is complete

- Central Theorem verified

- Categoricity verified

- tau-manifold structure verified

- Diff-geo structures are correctly marked as NOT earned

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.diffgeo_not_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L129-L130)
**theorem
Tau.BookII.Closure.diffgeo_not_earned :diffgeo_not_yet_earned = true**


---

### `Tau.BookII.Closure.e1_complete_b3_10_3_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L133-L134)
**theorem
Tau.BookII.Closure.e1_complete_b3_10_3_3 :e1_complete_for_book3 10 3 3 = true**


---

### `Tau.BookII.Closure.book3_prereq_3_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L137-L138)
**theorem
Tau.BookII.Closure.book3_prereq_3_15_3 :book3_prerequisites_check 3 15 3 = true**


---

### `Tau.BookII.Closure.connection_not_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L144-L146)
**theorem
Tau.BookII.Closure.connection_not_earned :default_connection.earned = false**


[II.R21] Connection is not earned: the placeholder records false.

---

### `Tau.BookII.Closure.curvature_not_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L148-L150)
**theorem
Tau.BookII.Closure.curvature_not_earned :default_curvature.earned = false**


[II.R21] Curvature is not earned: the placeholder records false.

---

### `Tau.BookII.Closure.holonomy_not_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L152-L154)
**theorem
Tau.BookII.Closure.holonomy_not_earned :default_holonomy.earned = false**


[II.R21] Holonomy is not earned: the placeholder records false.

---

### `Tau.BookII.Closure.e1_includes_self_enrichment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/DiffGeoAgenda.lean#L156-L166)
**theorem
Tau.BookII.Closure.e1_includes_self_enrichment
(bound db k_max : Denotation.TauIdx)
 :Enrichment.e1_layer_check bound db k_max = true → Enrichment.e1_self_enrichment_witness bound db = true**


[II.R22] E1 completeness implies self-enrichment witness holds.
This is structural: e1_layer_check includes self-enrichment.
If the full layer check passes, then in particular the
self-enrichment component is true.
