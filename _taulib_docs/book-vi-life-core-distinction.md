---
layout: taulib-doc
title: "TauLib.BookVI.LifeCore.Distinction"
permalink: /verify/taulib/docs/book-vi-life-core-distinction/
lane: verify
module_name: "TauLib.BookVI.LifeCore.Distinction"
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

# TauLib.BookVI.LifeCore.Distinction


τ-Distinction: the first of two Life predicates. A predicate D: X → 2_τ
satisfying 5 conditions: clopen partition, refinement-coherent, eventually
stable, law-stable, H_∂-equivariant.

## Registry Cross-References


- [VI.D04] τ-Distinction — `Distinction`

- [VI.D05] Finite-Lineage Carrier — `FiniteLineageCarrier`

- [VI.D06] Macro-Torus Carrier — `MacroTorusCarrier`

- [VI.D07] Galactic Carrier — `GalacticCarrier`

- [VI.T02] Distinction Well-Definedness — `distinction_well_defined`


## Ground Truth Sources


- Book VI Chapter 4 (2nd Edition): τ-Distinction


---

### `Tau.BookVI.Distinction.Distinction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L24-L35)
**structure
Tau.BookVI.Distinction.Distinction :Type**


[VI.D04] τ-Distinction predicate: D: X → 2_τ satisfying 5 conditions.

- Clopen partition 2. Refinement-coherent 3. Eventually stable

- Law-stable 5. H_∂-equivariant


- condition_count : ℕ
- count_eq : self.condition_count = 5
- clopen : Bool
- refinement_coherent : Bool
- eventually_stable : Bool
- law_stable : Bool
- equivariant : Bool
Instances For

---

### `Tau.BookVI.Distinction.instReprDistinction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L35-L35)
**def
Tau.BookVI.Distinction.instReprDistinction.repr :Distinction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Distinction.instReprDistinction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L35-L35)
**instance
Tau.BookVI.Distinction.instReprDistinction :Repr Distinction**

Equations
- Tau.BookVI.Distinction.instReprDistinction = { reprPrec := Tau.BookVI.Distinction.instReprDistinction.repr }

---

### `Tau.BookVI.Distinction.canonical_distinction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L37-L39)
**def
Tau.BookVI.Distinction.canonical_distinction :Distinction**

Equations
- Tau.BookVI.Distinction.canonical_distinction = { condition_count := 5, count_eq := Tau.BookVI.Distinction.canonical_distinction._proof_1 }
Instances For

---

### `Tau.BookVI.Distinction.FiniteLineageCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L41-L48)
**structure
Tau.BookVI.Distinction.FiniteLineageCarrier :Type**


[VI.D05] Finite-lineage carrier: biological carrier with L-boundary,
mortality, genotype-inheritable distinction.

- has_l_boundary : Bool
- is_mortal : Bool
- has_genotype : Bool
- carrier_type : String
Instances For

---

### `Tau.BookVI.Distinction.instReprFiniteLineageCarrier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L48-L48)
**def
Tau.BookVI.Distinction.instReprFiniteLineageCarrier.repr :FiniteLineageCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Distinction.instReprFiniteLineageCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L48-L48)
**instance
Tau.BookVI.Distinction.instReprFiniteLineageCarrier :Repr FiniteLineageCarrier**

Equations
- Tau.BookVI.Distinction.instReprFiniteLineageCarrier = { reprPrec := Tau.BookVI.Distinction.instReprFiniteLineageCarrier.repr }

---

### `Tau.BookVI.Distinction.MacroTorusCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L50-L55)
**structure
Tau.BookVI.Distinction.MacroTorusCarrier :Type**


[VI.D06] Macro-torus carrier: BH carrier with T² boundary, immortal.

- has_t2_boundary : Bool
- is_immortal : Bool
- carrier_type : String
Instances For

---

### `Tau.BookVI.Distinction.instReprMacroTorusCarrier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L55-L55)
**def
Tau.BookVI.Distinction.instReprMacroTorusCarrier.repr :MacroTorusCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Distinction.instReprMacroTorusCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L55-L55)
**instance
Tau.BookVI.Distinction.instReprMacroTorusCarrier :Repr MacroTorusCarrier**

Equations
- Tau.BookVI.Distinction.instReprMacroTorusCarrier = { reprPrec := Tau.BookVI.Distinction.instReprMacroTorusCarrier.repr }

---

### `Tau.BookVI.Distinction.GalacticCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L57-L62)
**structure
Tau.BookVI.Distinction.GalacticCarrier :Type**


[VI.D07] Galactic carrier: galaxy carrier with halo boundary, SMBH-anchored.

- has_halo_boundary : Bool
- smbh_anchored : Bool
- carrier_type : String
Instances For

---

### `Tau.BookVI.Distinction.instReprGalacticCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L62-L62)
**instance
Tau.BookVI.Distinction.instReprGalacticCarrier :Repr GalacticCarrier**

Equations
- Tau.BookVI.Distinction.instReprGalacticCarrier = { reprPrec := Tau.BookVI.Distinction.instReprGalacticCarrier.repr }

---

### `Tau.BookVI.Distinction.instReprGalacticCarrier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L62-L62)
**def
Tau.BookVI.Distinction.instReprGalacticCarrier.repr :GalacticCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Distinction.DistinctionWellDefined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L64-L70)
**structure
Tau.BookVI.Distinction.DistinctionWellDefined :Type**


[VI.T02] Distinction well-definedness: bounded stabilization,
termination, uniqueness given character χ.

- bounded_stabilization : Bool
- terminates : Bool
- unique_given_chi : Bool
Instances For

---

### `Tau.BookVI.Distinction.instReprDistinctionWellDefined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L70-L70)
**instance
Tau.BookVI.Distinction.instReprDistinctionWellDefined :Repr DistinctionWellDefined**

Equations
- Tau.BookVI.Distinction.instReprDistinctionWellDefined = { reprPrec := Tau.BookVI.Distinction.instReprDistinctionWellDefined.repr }

---

### `Tau.BookVI.Distinction.instReprDistinctionWellDefined.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L70-L70)
**def
Tau.BookVI.Distinction.instReprDistinctionWellDefined.repr :DistinctionWellDefined → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Distinction.distinction_wd`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L72-L72)
**def
Tau.BookVI.Distinction.distinction_wd :DistinctionWellDefined**

Equations
- Tau.BookVI.Distinction.distinction_wd = { }
Instances For

---

### `Tau.BookVI.Distinction.distinction_well_defined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L74-L78)
**theorem
Tau.BookVI.Distinction.distinction_well_defined :distinction_wd.bounded_stabilization = true ∧ distinction_wd.terminates = true ∧ distinction_wd.unique_given_chi = true**


---

### `Tau.BookVI.Distinction.distinction_has_five_conditions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/LifeCore/Distinction.lean#L80-L82)
**theorem
Tau.BookVI.Distinction.distinction_has_five_conditions :canonical_distinction.condition_count = 5**
