---
layout: taulib-doc
title: "TauLib.BookII.Closure.ForwardBook3"
permalink: /verify/taulib/docs/book-ii-closure-forward-book3/
lane: verify
module_name: "TauLib.BookII.Closure.ForwardBook3"
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

# TauLib.BookII.Closure.ForwardBook3


E1 Export Package: the complete set of data that Book II exports to Book III.

## Registry Cross-References


- [II.D66] E1 Export Package -- `E1ExportPackage`, `compute_e1_export`,
`full_export_check`


## Mathematical Content


**II.D66 (E1 Export Package):** The E1 Export Package bundles all verified
results from Book II into a single structure that Book III can import.
The package contains:

- **E1 Layer Completeness**: self-enrichment, Yoneda, 2-categories,
Code/Decode bijection (from Part VIII).

- **Central Theorem Verification**: O(tau^3) = A_spec(L) (from Part IX).

- **Categoricity**: tau^3 is unique up to canonical isomorphism (Part IX).

- **Enrichment Ladder**: E0 -> E1 transition verified (Part VIII).

- **tau-Manifold Structure**: atlas, transitions, d^2 = 0 (Part X).

- **Proto-Rationality**: finite-stage-determined points exist (Part X).


Book III will use this package as its starting point:


- E2 enrichment builds on E1 completeness

- Spectral forces act on the tau-manifold

- The 8 Millennium Problems connect to proto-rationality and the
enrichment ladder


---

### `Tau.BookII.Closure.E1ExportPackage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L46-L56)
**structure
Tau.BookII.Closure.E1ExportPackage :Type**


[II.D66] The E1 Export Package: all verified Book II results
bundled for Book III. Each field records a boolean witness
of the corresponding verification.

- e1_layer_complete : Bool
- central_theorem_verified : Bool
- categoricity_verified : Bool
- enrichment_ladder_verified : Bool
- tau_manifold_verified : Bool
- proto_rationality_verified : Bool
Instances For

---

### `Tau.BookII.Closure.instReprE1ExportPackage.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L56-L56)
**def
Tau.BookII.Closure.instReprE1ExportPackage.repr :E1ExportPackage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instReprE1ExportPackage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L56-L56)
**instance
Tau.BookII.Closure.instReprE1ExportPackage :Repr E1ExportPackage**

Equations
- Tau.BookII.Closure.instReprE1ExportPackage = { reprPrec := Tau.BookII.Closure.instReprE1ExportPackage.repr }

---

### `Tau.BookII.Closure.instDecidableEqE1ExportPackage.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L56-L56)
**def
Tau.BookII.Closure.instDecidableEqE1ExportPackage.decEq
(x✝ x✝¹ : E1ExportPackage)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqE1ExportPackage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L56-L56)
**instance
Tau.BookII.Closure.instDecidableEqE1ExportPackage :DecidableEq E1ExportPackage**

Equations
- Tau.BookII.Closure.instDecidableEqE1ExportPackage = Tau.BookII.Closure.instDecidableEqE1ExportPackage.decEq

---

### `Tau.BookII.Closure.compute_e1_export`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L58-L70)
**def
Tau.BookII.Closure.compute_e1_export
(db bound k_max : Denotation.TauIdx)
 :E1ExportPackage**


[II.D66] Compute the E1 Export Package by evaluating all components.
Parameters control the verification depth:


- db: max stage depth for tower checks

- bound: max input value for range checks

- k_max: max stage for Code/Decode checks

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.export_package_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L72-L80)
**def
Tau.BookII.Closure.export_package_complete
(pkg : E1ExportPackage)
 :Bool**


[II.D66] Check that all components of the export package are present.
This is the single-point verification that Book II is complete.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.full_export_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L82-L84)
**def
Tau.BookII.Closure.full_export_check
(db bound k_max : Denotation.TauIdx)
 :Bool**


[II.D66] Full export check: compute and verify the entire package.
Equations
- Tau.BookII.Closure.full_export_check db bound k_max = Tau.BookII.Closure.export_package_complete (Tau.BookII.Closure.compute_e1_export db bound k_max)
Instances For

---

### `Tau.BookII.Closure.export_component_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L90-L97)
**def
Tau.BookII.Closure.export_component_count
(pkg : E1ExportPackage)
 :ℕ**


Summary: count how many components are verified (out of 6).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.export_all_six`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L99-L101)
**def
Tau.BookII.Closure.export_all_six
(db bound k_max : Denotation.TauIdx)
 :Bool**


A complete export package has all 6 components.
Equations
- Tau.BookII.Closure.export_all_six db bound k_max = (Tau.BookII.Closure.export_component_count (Tau.BookII.Closure.compute_e1_export db bound k_max) == 6)
Instances For

---

### `Tau.BookII.Closure.book3_entry_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L107-L113)
**def
Tau.BookII.Closure.book3_entry_level
(db bound k_max : Denotation.TauIdx)
 :Option Enrichment.EnrichmentLevel**


[II.D66] The entry point for Book III: verify that Book II is complete
and return the enrichment level (E1) that Book III starts from.
Equations
- Tau.BookII.Closure.book3_entry_level db bound k_max = if Tau.BookII.Closure.full_export_check db bound k_max = true then some Tau.BookII.Enrichment.EnrichmentLevel.E1
 else none
Instances For

---

### `Tau.BookII.Closure.book3_starts_at_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L115-L117)
**def
Tau.BookII.Closure.book3_starts_at_e1
(db bound k_max : Denotation.TauIdx)
 :Bool**


Verify that Book III starts at E1, not E0.
Equations
- Tau.BookII.Closure.book3_starts_at_e1 db bound k_max = (Tau.BookII.Closure.book3_entry_level db bound k_max == some Tau.BookII.Enrichment.EnrichmentLevel.E1)
Instances For

---

### `Tau.BookII.Closure.full_export_3_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L156-L157)
**theorem
Tau.BookII.Closure.full_export_3_15_3 :full_export_check 3 15 3 = true**


---

### `Tau.BookII.Closure.all_six_3_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L160-L161)
**theorem
Tau.BookII.Closure.all_six_3_15_3 :export_all_six 3 15 3 = true**


---

### `Tau.BookII.Closure.book3_e1_3_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L164-L165)
**theorem
Tau.BookII.Closure.book3_e1_3_15_3 :book3_starts_at_e1 3 15 3 = true**


---

### `Tau.BookII.Closure.export_e1_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L168-L169)
**theorem
Tau.BookII.Closure.export_e1_layer :(compute_e1_export 3 15 3).e1_layer_complete = true**


---

### `Tau.BookII.Closure.export_central`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L171-L172)
**theorem
Tau.BookII.Closure.export_central :(compute_e1_export 3 15 3).central_theorem_verified = true**


---

### `Tau.BookII.Closure.export_categoricity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L174-L175)
**theorem
Tau.BookII.Closure.export_categoricity :(compute_e1_export 3 15 3).categoricity_verified = true**


---

### `Tau.BookII.Closure.export_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L177-L178)
**theorem
Tau.BookII.Closure.export_ladder :(compute_e1_export 3 15 3).enrichment_ladder_verified = true**


---

### `Tau.BookII.Closure.export_manifold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L180-L181)
**theorem
Tau.BookII.Closure.export_manifold :(compute_e1_export 3 15 3).tau_manifold_verified = true**


---

### `Tau.BookII.Closure.export_proto`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L183-L184)
**theorem
Tau.BookII.Closure.export_proto :(compute_e1_export 3 15 3).proto_rationality_verified = true**


---

### `Tau.BookII.Closure.complete_means_six`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L190-L205)
**theorem
Tau.BookII.Closure.complete_means_six
(pkg : E1ExportPackage)
 :export_package_complete pkg = true → export_component_count pkg = 6**


[II.D66] A complete export package has all 6 components.
This is the structural statement that completeness implies count = 6.

---

### `Tau.BookII.Closure.export_implies_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L207-L215)
**theorem
Tau.BookII.Closure.export_implies_e1
(db bound k_max : Denotation.TauIdx)
 :full_export_check db bound k_max = true → Enrichment.e1_layer_check bound db k_max = true**


[II.D66] The export package is self-consistent: if the full check passes,
then each component individually passes.

---

### `Tau.BookII.Closure.export_implies_central`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L217-L225)
**theorem
Tau.BookII.Closure.export_implies_central
(db bound k_max : Denotation.TauIdx)
 :full_export_check db bound k_max = true → CentralTheorem.central_theorem_check db bound = true**


[II.D66] The export package is self-consistent: full check implies
Central Theorem verified.

---

### `Tau.BookII.Closure.e1_gt_e0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/ForwardBook3.lean#L227-L230)
**theorem
Tau.BookII.Closure.e1_gt_e0 :Enrichment.EnrichmentLevel.E0 ≠ Enrichment.EnrichmentLevel.E1**


[II.D66] E0 and E1 are distinct enrichment levels.
Book III starts at E1, not E0.
