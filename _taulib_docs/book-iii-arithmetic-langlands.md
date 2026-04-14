---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.Langlands"
permalink: /verify/taulib/docs/book-iii-arithmetic-langlands/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.Langlands"
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

# TauLib.BookIII.Arithmetic.Langlands


Automorphic-Galois Duality, Local Langlands Instance, Duality as MD on ℤ²,
Functoriality Theorem, and Base Change-Transfer Naturality.

## Registry Cross-References


- [III.D63] Automorphic-Galois Duality -- `ag_duality_check`

- [III.D64] Local Langlands Instance -- `local_langlands_check`

- [III.P28] Duality as Mutual Determination on ℤ² -- `duality_md_check`

- [III.T36] Functoriality Theorem -- `functoriality_check`

- [III.T37] Base Change-Transfer Naturality -- `base_change_check`


## Mathematical Content


**III.D63 (Automorphic-Galois Duality):** Bidirectional correspondence between
m-axis (Galois/prime) and n-axis (automorphic/spectral) data on ℤ².

**III.D64 (Local Langlands Instance):** At each prime p, the matched pair
(Fr_p, λ_p) with Frobenius equals spectral character restricted to m-axis.

**III.P28 (Duality as MD on ℤ²):** The A-G duality IS Mutual Determination
with m-axis as boundary, n-axis as spectral, full character as interior.

**III.T36 (Functoriality):** For every sector morphism f: S₁→S₂, the induced
map on boundary characters commutes with spectral decomposition.

**III.T37 (Base Change-Transfer):** Base change and transfer are natural
transformations on the enriched bi-square.

---

### `Tau.BookIII.Arithmetic.ag_duality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L47-L71)
**def
Tau.BookIII.Arithmetic.ag_duality_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D63] Automorphic-Galois duality on ℤ² at finite level:
m-axis (Galois) = B-part of BNF, n-axis (automorphic) = C-part.
The duality maps m-data to n-data and vice versa.
Equations
- Tau.BookIII.Arithmetic.ag_duality_check bound db = Tau.BookIII.Arithmetic.ag_duality_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.ag_duality_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L53-L70)@[irreducible]

**def
Tau.BookIII.Arithmetic.ag_duality_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.local_langlands_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L77-L101)
**def
Tau.BookIII.Arithmetic.local_langlands_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D64] Local Langlands at prime p: the Frobenius at p is encoded
by the BNF component at the p-th prime position. The spectral character
restricted to the m-axis gives the Frobenius eigenvalue.
Equations
- Tau.BookIII.Arithmetic.local_langlands_check bound db = Tau.BookIII.Arithmetic.local_langlands_check.go bound db 1 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.local_langlands_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L83-L100)@[irreducible]

**def
Tau.BookIII.Arithmetic.local_langlands_check.go
(bound db : Denotation.TauIdx)

(i k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.duality_md_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L107-L129)
**def
Tau.BookIII.Arithmetic.duality_md_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P28] Duality as Mutual Determination: the A-G duality IS MD
with m-axis = boundary, n-axis = spectral, full = interior.
Equations
- Tau.BookIII.Arithmetic.duality_md_check bound db = Tau.BookIII.Arithmetic.duality_md_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.duality_md_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L112-L128)@[irreducible]

**def
Tau.BookIII.Arithmetic.duality_md_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.functoriality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L135-L157)
**def
Tau.BookIII.Arithmetic.functoriality_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T36] Functoriality: sector morphisms (BNF-preserving maps) commute
with spectral decomposition. At finite level: the polarity swap commutes
with the B/C/X decomposition.
Equations
- Tau.BookIII.Arithmetic.functoriality_check bound db = Tau.BookIII.Arithmetic.functoriality_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.functoriality_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L141-L156)@[irreducible]

**def
Tau.BookIII.Arithmetic.functoriality_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.base_change_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L163-L187)
**def
Tau.BookIII.Arithmetic.base_change_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T37] Base change-transfer naturality: the enrichment functor
Enr₀₁ on sector morphisms and the defect functional between sectors
are natural transformations. Checked by: tower projection commutes
with sector decomposition.
Equations
- Tau.BookIII.Arithmetic.base_change_check bound db = Tau.BookIII.Arithmetic.base_change_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.base_change_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L170-L186)@[irreducible]

**def
Tau.BookIII.Arithmetic.base_change_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.ag_duality_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L203-L204)
**theorem
Tau.BookIII.Arithmetic.ag_duality_15_4 :ag_duality_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.local_langlands_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L206-L207)
**theorem
Tau.BookIII.Arithmetic.local_langlands_10_3 :local_langlands_check 10 3 = true**


---

### `Tau.BookIII.Arithmetic.duality_md_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L209-L210)
**theorem
Tau.BookIII.Arithmetic.duality_md_15_4 :duality_md_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.functoriality_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L212-L213)
**theorem
Tau.BookIII.Arithmetic.functoriality_15_4 :functoriality_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.base_change_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L215-L216)
**theorem
Tau.BookIII.Arithmetic.base_change_15_3 :base_change_check 15 3 = true**


---

### `Tau.BookIII.Arithmetic.langlands_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L222-L223)
**theorem
Tau.BookIII.Arithmetic.langlands_level :Doors.problem_level Doors.MillenniumProblem.Langlands = Enrichment.EnrLevel.E2**


[III.D63] Structural: Langlands is at E₁→E₂ interface.

---

### `Tau.BookIII.Arithmetic.langlands_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L224-L224)
**theorem
Tau.BookIII.Arithmetic.langlands_part :Doors.problem_part Doors.MillenniumProblem.Langlands = 6**


---

### `Tau.BookIII.Arithmetic.func_10_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L226-L228)
**theorem
Tau.BookIII.Arithmetic.func_10_1 :functoriality_check 10 1 = true**


[III.T36] Structural: functoriality at depth 1.

---

### `Tau.BookIII.Arithmetic.base_change_10_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/Langlands.lean#L230-L232)
**theorem
Tau.BookIII.Arithmetic.base_change_10_1 :base_change_check 10 1 = true**


[III.T37] Structural: base change at depth 1.
