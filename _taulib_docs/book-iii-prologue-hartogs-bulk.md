---
layout: taulib-doc
title: "TauLib.BookIII.Prologue.HartogsBulk"
permalink: /verify/taulib/docs/book-iii-prologue-hartogs-bulk/
lane: verify
module_name: "TauLib.BookIII.Prologue.HartogsBulk"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Prologue.HartogsBulk


Hartogs Bulk Projection and E₁ as Gluing Principle.

## Registry Cross-References


- [III.D01] Hartogs Bulk Projection -- `HartogsBulk`, `hartogs_bulk_check`

- [III.D03] E₁ as Gluing Principle -- `e1_gluing_check`


## Mathematical Content


**III.D01 (Hartogs Bulk Projection):** 3D Cartesian space = Hartogs-projected
bulk of the local T² fiber at each worldline point. Solenoidal surface
coordinates (γ, η) carry boundary data; Hartogs extension fills the interior
with genuine linear coordinates.

**III.D03 (E₁ as Gluing Principle):** Self-enrichment (E₁) is precisely the
statement that local Hartogs bulk projections glue globally. Morphisms between
local patches carry the same split-complex bipolar structure as the patches
themselves. Physics IS E₁.

Book III starts at E₁ (verified by ForwardBook3.lean). These two definitions
set the stage: Hartogs bulk = local spatial structure, E₁ gluing = global
coherence.

---

### `Tau.BookIII.Prologue.HartogsBulk`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L39-L52)
**structure
Tau.BookIII.Prologue.HartogsBulk :Type**


[III.D01] Hartogs Bulk Projection: at each stage k, the bulk coordinate
is the interior value obtained by Hartogs extension from boundary data.
Concretely: given boundary values at stage k (the reduce-compatible map),
the bulk value is the unique Hartogs extension = reduce(x, k).

The "3D space" perceived at a point is the Hartogs-filled interior of
the local T² fiber. We model this as: for each pair (boundary_val, stage),
the bulk projection is the reduce of their sum (combining solenoidal
coordinates into a single interior coordinate).

- boundary_b : Denotation.TauIdx
- boundary_c : Denotation.TauIdx
- stage : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Prologue.instReprHartogsBulk`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L52-L52)
**instance
Tau.BookIII.Prologue.instReprHartogsBulk :Repr HartogsBulk**

Equations
- Tau.BookIII.Prologue.instReprHartogsBulk = { reprPrec := Tau.BookIII.Prologue.instReprHartogsBulk.repr }

---

### `Tau.BookIII.Prologue.instReprHartogsBulk.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L52-L52)
**def
Tau.BookIII.Prologue.instReprHartogsBulk.repr :HartogsBulk → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Prologue.instDecidableEqHartogsBulk.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L52-L52)
**def
Tau.BookIII.Prologue.instDecidableEqHartogsBulk.decEq
(x✝ x✝¹ : HartogsBulk)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Prologue.instDecidableEqHartogsBulk`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L52-L52)
**instance
Tau.BookIII.Prologue.instDecidableEqHartogsBulk :DecidableEq HartogsBulk**

Equations
- Tau.BookIII.Prologue.instDecidableEqHartogsBulk = Tau.BookIII.Prologue.instDecidableEqHartogsBulk.decEq

---

### `Tau.BookIII.Prologue.bulk_coordinate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L54-L58)
**def
Tau.BookIII.Prologue.bulk_coordinate
(hb : HartogsBulk)
 :Denotation.TauIdx**


[III.D01] Compute the bulk coordinate from boundary data.
The bulk projection combines two boundary channels via addition
mod primorial (Hartogs fill = summation of boundary contributions).
Equations
- Tau.BookIII.Prologue.bulk_coordinate hb = Tau.Polarity.reduce (hb.boundary_b + hb.boundary_c) hb.stage
Instances For

---

### `Tau.BookIII.Prologue.hartogs_bulk_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L60-L69)
**def
Tau.BookIII.Prologue.hartogs_bulk_coherent
(hb : HartogsBulk)

(k : Denotation.TauIdx)
 :Bool**


[III.D01] Hartogs bulk coherence: the bulk coordinate at stage k+1
projects correctly to stage k. This is the local version of tower
coherence applied to the spatial (Hartogs-filled) interior.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Prologue.hartogs_bulk_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L71-L84)
**def
Tau.BookIII.Prologue.hartogs_bulk_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D01] Full Hartogs bulk check: for all boundary pairs in range,
verify tower coherence of the bulk projection.
Equations
- Tau.BookIII.Prologue.hartogs_bulk_check bound db = Tau.BookIII.Prologue.hartogs_bulk_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Prologue.hartogs_bulk_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L76-L83)@[irreducible]

**def
Tau.BookIII.Prologue.hartogs_bulk_check.go
(bound db : Denotation.TauIdx)

(b c k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Prologue.e1_gluing_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L90-L97)
**def
Tau.BookIII.Prologue.e1_gluing_check
(bound db k_max : Denotation.TauIdx)
 :Bool**


[III.D03] E₁ gluing check: verify that Book II is complete (all 6
export components verified) and that the Hartogs bulk projection
is tower-coherent. E₁ = "local patches glue" = "physics exists".

This combines the ForwardBook3 export with local Hartogs coherence.
Equations
- Tau.BookIII.Prologue.e1_gluing_check bound db k_max = (Tau.BookII.Closure.full_export_check db bound k_max && Tau.BookIII.Prologue.hartogs_bulk_check bound db)
Instances For

---

### `Tau.BookIII.Prologue.book3_e1_established`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L99-L102)
**def
Tau.BookIII.Prologue.book3_e1_established
(bound db k_max : Denotation.TauIdx)
 :Bool**


[III.D03] The entry point for Book III: E₁ is established.
Book III begins at E₁ and constructs the full enrichment ladder.
Equations
- Tau.BookIII.Prologue.book3_e1_established bound db k_max = (Tau.BookII.Closure.book3_starts_at_e1 db bound k_max && Tau.BookIII.Prologue.e1_gluing_check bound db k_max)
Instances For

---

### `Tau.BookIII.Prologue.hartogs_bulk_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L131-L132)
**theorem
Tau.BookIII.Prologue.hartogs_bulk_8_3 :hartogs_bulk_check 8 3 = true**


---

### `Tau.BookIII.Prologue.e1_gluing_8_3_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L135-L136)
**theorem
Tau.BookIII.Prologue.e1_gluing_8_3_3 :e1_gluing_check 8 3 3 = true**


---

### `Tau.BookIII.Prologue.book3_entry_8_3_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L139-L140)
**theorem
Tau.BookIII.Prologue.book3_entry_8_3_3 :book3_e1_established 8 3 3 = true**


---

### `Tau.BookIII.Prologue.bulk_tower_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L146-L151)
**theorem
Tau.BookIII.Prologue.bulk_tower_coherent
(b c : Denotation.TauIdx)

{k stage : Denotation.TauIdx}

(h : k ≤ stage)
 :Polarity.reduce (Polarity.reduce (b + c) stage) k = Polarity.reduce (b + c) k**


[III.D01] Structural proof: Hartogs bulk projection is tower-coherent.
reduce(reduce(b + c, stage), k) = reduce(b + c, k) for k ≤ stage.
This is reduction_compat from Book I.

---

### `Tau.BookIII.Prologue.bulk_reduce_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Prologue/HartogsBulk.lean#L153-L158)
**theorem
Tau.BookIII.Prologue.bulk_reduce_stable
(hb : HartogsBulk)
 :Polarity.reduce (bulk_coordinate hb) hb.stage = bulk_coordinate hb**


[III.D01] Bulk projection is reduce-stable:
reduce(bulk_coordinate(hb), hb.stage) = bulk_coordinate(hb).
