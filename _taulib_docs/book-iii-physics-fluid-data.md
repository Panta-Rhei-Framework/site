---
layout: taulib-doc
title: "TauLib.BookIII.Physics.FluidData"
permalink: /verify/taulib/docs/book-iii-physics-fluid-data/
lane: verify
module_name: "TauLib.BookIII.Physics.FluidData"
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

# TauLib.BookIII.Physics.FluidData


τ-Admissible Fluid Data, Cylinder Assignment, ABCD Extraction, and Defect Functional.

## Registry Cross-References


- [III.D36] τ-Admissible Fluid Data -- `FluidData`, `fluid_data_check`

- [III.D37] Cylinder Assignment -- `cylinder_assignment`, `cylinder_assignment_check`

- [III.D38] ABCD Extraction -- `abcd_extract`, `abcd_check`

- [III.D39] Defect Functional -- `defect_functional`, `defect_monotone_check`


## Mathematical Content


**III.D36 (τ-Admissible Fluid Data):** An ω-germ assignment on clopen cylinders
of ℤ̂_τ. At primorial level k, a fluid datum is a function assigning to each
cylinder [a mod Prim(k)] an ω-germ value, with ABCD extraction bounded.

**III.D37 (Cylinder Assignment):** The assignment map: each residue class
mod Prim(k) receives its boundary normal form, which carries B/C/X components.

**III.D38 (ABCD Extraction):** From a cylinder assignment, extract 4 components:
A = time-sector (primorial depth), B = B-lobe contribution, C = C-lobe contribution,
D = crossing-type contribution. Each is bounded by the primorial.

**III.D39 (Defect Functional):** Δ(f, k) = max over all cylinders at level k of
|BNF sum − original residue|. Measures deviation from canonical form. A good
fluid datum has Δ → 0 as k → ∞.

---

### `Tau.BookIII.Physics.FluidData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L44-L49)
**structure
Tau.BookIII.Physics.FluidData :Type**


[III.D36] Fluid data at primorial level k: for each cylinder [a mod Prim(k)],
we store the boundary normal form (B, C, X components).

- depth : Denotation.TauIdx
- values : List Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Physics.instReprFluidData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L49-L49)
**instance
Tau.BookIII.Physics.instReprFluidData :Repr FluidData**

Equations
- Tau.BookIII.Physics.instReprFluidData = { reprPrec := Tau.BookIII.Physics.instReprFluidData.repr }

---

### `Tau.BookIII.Physics.instReprFluidData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L49-L49)
**def
Tau.BookIII.Physics.instReprFluidData.repr :FluidData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.instDecidableEqFluidData.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L49-L49)
**def
Tau.BookIII.Physics.instDecidableEqFluidData.decEq
(x✝ x✝¹ : FluidData)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.instDecidableEqFluidData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L49-L49)
**instance
Tau.BookIII.Physics.instDecidableEqFluidData :DecidableEq FluidData**

Equations
- Tau.BookIII.Physics.instDecidableEqFluidData = Tau.BookIII.Physics.instDecidableEqFluidData.decEq

---

### `Tau.BookIII.Physics.instBEqFluidData.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L49-L49)
**def
Tau.BookIII.Physics.instBEqFluidData.beq :FluidData → FluidData → Bool**

Equations
- Tau.BookIII.Physics.instBEqFluidData.beq { depth := a, values := a_1 } { depth := b, values := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIII.Physics.instBEqFluidData.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Physics.instBEqFluidData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L49-L49)
**instance
Tau.BookIII.Physics.instBEqFluidData :BEq FluidData**

Equations
- Tau.BookIII.Physics.instBEqFluidData = { beq := Tau.BookIII.Physics.instBEqFluidData.beq }

---

### `Tau.BookIII.Physics.make_fluid_data`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L51-L56)
**def
Tau.BookIII.Physics.make_fluid_data
(k : Denotation.TauIdx)
 :FluidData**


[III.D36] Construct fluid data at depth k from bound: assigns each
residue class its own value (the canonical assignment).
Equations
- Tau.BookIII.Physics.make_fluid_data k = if (Tau.Polarity.primorial k == 0) = true then { depth := k, values := [] }
 else { depth := k, values := List.range (Tau.Polarity.primorial k) }
Instances For

---

### `Tau.BookIII.Physics.fluid_data_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L58-L79)
**def
Tau.BookIII.Physics.fluid_data_check
(db : Denotation.TauIdx)
 :Bool**


[III.D36] τ-admissibility check: each cylinder value has a valid BNF
decomposition at this depth.
Equations
- Tau.BookIII.Physics.fluid_data_check db = Tau.BookIII.Physics.fluid_data_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.fluid_data_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L63-L72)@[irreducible]

**def
Tau.BookIII.Physics.fluid_data_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.fluid_data_check.go_inner`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L74-L79)@[irreducible]

**def
Tau.BookIII.Physics.fluid_data_check.go_inner
(x pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.cylinder_assignment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L85-L90)
**def
Tau.BookIII.Physics.cylinder_assignment
(x k : Denotation.TauIdx)
 :Spectral.BoundaryNF**


[III.D37] Cylinder assignment: residue class x mod Prim(k) receives
its boundary normal form.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.cylinder_assignment_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L92-L108)
**def
Tau.BookIII.Physics.cylinder_assignment_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D37] Cylinder assignment check: every cylinder has a valid
BNF that sums correctly.
Equations
- Tau.BookIII.Physics.cylinder_assignment_check bound db = Tau.BookIII.Physics.cylinder_assignment_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.cylinder_assignment_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L97-L107)@[irreducible]

**def
Tau.BookIII.Physics.cylinder_assignment_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.ABCDComponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L114-L121)
**structure
Tau.BookIII.Physics.ABCDComponents :Type**


[III.D38] ABCD components of a fluid datum at a cylinder.
A = depth (time/scale), B = B-lobe, C = C-lobe, D = crossing.

- a_comp : Denotation.TauIdx
- b_comp : Denotation.TauIdx
- c_comp : Denotation.TauIdx
- d_comp : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Physics.instReprABCDComponents.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L121-L121)
**def
Tau.BookIII.Physics.instReprABCDComponents.repr :ABCDComponents → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.instReprABCDComponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L121-L121)
**instance
Tau.BookIII.Physics.instReprABCDComponents :Repr ABCDComponents**

Equations
- Tau.BookIII.Physics.instReprABCDComponents = { reprPrec := Tau.BookIII.Physics.instReprABCDComponents.repr }

---

### `Tau.BookIII.Physics.instDecidableEqABCDComponents.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L121-L121)
**def
Tau.BookIII.Physics.instDecidableEqABCDComponents.decEq
(x✝ x✝¹ : ABCDComponents)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.instDecidableEqABCDComponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L121-L121)
**instance
Tau.BookIII.Physics.instDecidableEqABCDComponents :DecidableEq ABCDComponents**

Equations
- Tau.BookIII.Physics.instDecidableEqABCDComponents = Tau.BookIII.Physics.instDecidableEqABCDComponents.decEq

---

### `Tau.BookIII.Physics.instBEqABCDComponents.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L121-L121)
**def
Tau.BookIII.Physics.instBEqABCDComponents.beq :ABCDComponents → ABCDComponents → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Physics.instBEqABCDComponents.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Physics.instBEqABCDComponents`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L121-L121)
**instance
Tau.BookIII.Physics.instBEqABCDComponents :BEq ABCDComponents**

Equations
- Tau.BookIII.Physics.instBEqABCDComponents = { beq := Tau.BookIII.Physics.instBEqABCDComponents.beq }

---

### `Tau.BookIII.Physics.abcd_extract`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L123-L126)
**def
Tau.BookIII.Physics.abcd_extract
(x k : Denotation.TauIdx)
 :ABCDComponents**


[III.D38] Extract ABCD components from a cylinder assignment.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.abcd_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L128-L147)
**def
Tau.BookIII.Physics.abcd_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D38] ABCD extraction check: components are bounded by primorial,
and B + C + D ≡ x (mod Prim(k)).
Equations
- Tau.BookIII.Physics.abcd_check bound db = Tau.BookIII.Physics.abcd_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.abcd_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L133-L146)@[irreducible]

**def
Tau.BookIII.Physics.abcd_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.cylinder_defect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L153-L161)
**def
Tau.BookIII.Physics.cylinder_defect
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D39] Defect at a single cylinder: |BNF sum − x| mod Prim(k).
Zero defect means the BNF decomposition is exact.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.defect_functional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L163-L175)
**def
Tau.BookIII.Physics.defect_functional
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D39] Defect functional at primorial level k: maximum defect
over all cylinders.
Equations
- Tau.BookIII.Physics.defect_functional k = if (Tau.Polarity.primorial k == 0) = true then 0
 else Tau.BookIII.Physics.defect_functional.go 0 (Tau.Polarity.primorial k) k 0
Instances For

---

### `Tau.BookIII.Physics.defect_functional.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L170-L175)@[irreducible]

**def
Tau.BookIII.Physics.defect_functional.go
(x pk k max_def : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.defect_monotone_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L177-L187)
**def
Tau.BookIII.Physics.defect_monotone_check
(db : Denotation.TauIdx)
 :Bool**


[III.D39] Defect monotonicity check: defect is zero at every level
(because BNF decomposition is exact by construction).
Equations
- Tau.BookIII.Physics.defect_monotone_check db = Tau.BookIII.Physics.defect_monotone_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.defect_monotone_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L182-L186)@[irreducible]

**def
Tau.BookIII.Physics.defect_monotone_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.fluid_data_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L205-L206)
**theorem
Tau.BookIII.Physics.fluid_data_4 :fluid_data_check 4 = true**


---

### `Tau.BookIII.Physics.cylinder_assign_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L208-L209)
**theorem
Tau.BookIII.Physics.cylinder_assign_15_4 :cylinder_assignment_check 15 4 = true**


---

### `Tau.BookIII.Physics.abcd_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L211-L212)
**theorem
Tau.BookIII.Physics.abcd_15_4 :abcd_check 15 4 = true**


---

### `Tau.BookIII.Physics.defect_zero_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L214-L215)
**theorem
Tau.BookIII.Physics.defect_zero_3 :defect_functional 3 = 0**


---

### `Tau.BookIII.Physics.defect_zero_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L217-L218)
**theorem
Tau.BookIII.Physics.defect_zero_4 :defect_functional 4 = 0**


---

### `Tau.BookIII.Physics.defect_monotone_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L220-L221)
**theorem
Tau.BookIII.Physics.defect_monotone_5 :defect_monotone_check 5 = true**


---

### `Tau.BookIII.Physics.fluid_data_depth_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L227-L229)
**theorem
Tau.BookIII.Physics.fluid_data_depth_3 :(make_fluid_data 3).values.length = 30**


[III.D36] Structural: canonical fluid data at depth 3 has 30 values.

---

### `Tau.BookIII.Physics.cylinder_assign_0`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L231-L233)
**theorem
Tau.BookIII.Physics.cylinder_assign_0 :cylinder_assignment 42 0 = { b_part := 0, c_part := 0, x_part := 0, depth := 0 }**


[III.D37] Structural: cylinder assignment at depth 0 is trivial.

---

### `Tau.BookIII.Physics.abcd_zero_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L235-L237)
**theorem
Tau.BookIII.Physics.abcd_zero_3 :abcd_extract 0 3 = { a_comp := 3, b_comp := 0, c_comp := 0, d_comp := 0 }**


[III.D38] Structural: ABCD of 0 is always zero.

---

### `Tau.BookIII.Physics.defect_zero_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/FluidData.lean#L239-L241)
**theorem
Tau.BookIII.Physics.defect_zero_1 :defect_functional 1 = 0**


[III.D39] Structural: defect at depth 1 is zero.
