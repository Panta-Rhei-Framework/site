---
layout: taulib-doc
title: "TauLib.BookIII.Physics.Hodge"
permalink: /verify/taulib/docs/book-iii-physics-hodge/
lane: verify
module_name: "TauLib.BookIII.Physics.Hodge"
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

# TauLib.BookIII.Physics.Hodge


σ-Fixed Characters, Sector Addressability, NF-Addressability Theorem,
Hodge Filtration, and Spectral-Hodge Compatibility.

## Registry Cross-References


- [III.D47] σ-Fixed Characters -- `sigma_fixed_check`

- [III.D48] Sector Addressability -- `sector_addressability_check`

- [III.P18] Character-Sector Correspondence -- `char_sector_check`

- [III.T28] NF-Addressability Theorem -- `nf_addressability_check`

- [III.P19] Hodge Filtration -- `hodge_filtration_check`

- [III.P20] Spectral-Hodge Compatibility -- `spectral_hodge_check`


## Mathematical Content


**III.D47 (σ-Fixed Characters):** A boundary character χ is σ-fixed if
polarity_swap(BNF(χ)) = BNF(χ). These are the self-dual characters that
live on the crossing locus of L = S¹ ∨ S¹.

**III.D48 (Sector Addressability):** Every cylinder at every primorial level
is uniquely addressable by its B/C/X coordinates. The address is the triple
(b_part, c_part, x_part) in the BNF.

**III.P18 (Character-Sector Correspondence):** Each character maps to exactly
one sector, and each sector is non-empty at sufficiently high depth.

**III.T28 (NF-Addressability):** Every element of ℤ/Prim(k)ℤ is uniquely
addressable by its BNF. Combined with sector addressability, this gives
a complete addressing scheme for the spectral algebra.

**III.P19 (Hodge Filtration):** The BNF decomposition induces a filtration
B ⊂ B+X ⊂ B+C+X = ℤ/Prim(k)ℤ. This is the τ-analog of the Hodge filtration.

**III.P20 (Spectral-Hodge Compatibility):** The Hodge filtration is compatible
with the spectral decomposition: the B-step of the filtration corresponds
to B-type eigenvalues of H_L, and similarly for C and X.

---

### `Tau.BookIII.Physics.is_sigma_fixed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L54-L57)
**def
Tau.BookIII.Physics.is_sigma_fixed
(nf : Spectral.BoundaryNF)
 :Bool**


[III.D47] A BNF is σ-fixed if polarity swap leaves it unchanged:
b_part = c_part. These are the self-dual elements.
Equations
- Tau.BookIII.Physics.is_sigma_fixed nf = (nf.b_part == nf.c_part)
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L59-L81)
**def
Tau.BookIII.Physics.sigma_fixed_check
(db : Denotation.TauIdx)
 :Bool**


[III.D47] σ-fixed character check: count and verify σ-fixed elements
at each primorial level.
Equations
- Tau.BookIII.Physics.sigma_fixed_check db = Tau.BookIII.Physics.sigma_fixed_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L64-L74)@[irreducible]

**def
Tau.BookIII.Physics.sigma_fixed_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_check.count_fixed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L76-L81)@[irreducible]

**def
Tau.BookIII.Physics.sigma_fixed_check.count_fixed
(x pk k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_closed_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L83-L107)
**def
Tau.BookIII.Physics.sigma_fixed_closed_check
(db : Denotation.TauIdx)
 :Bool**


[III.D47] σ-fixed involution: the set of σ-fixed elements is closed
under BNF operations.
Equations
- Tau.BookIII.Physics.sigma_fixed_closed_check db = Tau.BookIII.Physics.sigma_fixed_closed_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_closed_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L88-L95)@[irreducible]

**def
Tau.BookIII.Physics.sigma_fixed_closed_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_closed_check.check_closed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L97-L107)@[irreducible]

**def
Tau.BookIII.Physics.sigma_fixed_closed_check.check_closed
(x pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.sector_addressability_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L113-L130)
**def
Tau.BookIII.Physics.sector_addressability_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D48] Sector addressability: every cylinder has a unique triple
(b, c, x) address via its BNF.
Equations
- Tau.BookIII.Physics.sector_addressability_check bound db = Tau.BookIII.Physics.sector_addressability_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.sector_addressability_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L118-L129)@[irreducible]

**def
Tau.BookIII.Physics.sector_addressability_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.char_sector_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L136-L156)
**def
Tau.BookIII.Physics.char_sector_check
(db : Denotation.TauIdx)
 :Bool**


[III.P18] Character-sector correspondence: each non-zero element at
level k has at least one non-zero component (lives in some sector).
Equations
- Tau.BookIII.Physics.char_sector_check db = Tau.BookIII.Physics.char_sector_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.char_sector_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L141-L148)@[irreducible]

**def
Tau.BookIII.Physics.char_sector_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.char_sector_check.check_nonzero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L150-L156)@[irreducible]

**def
Tau.BookIII.Physics.char_sector_check.check_nonzero
(x pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.nf_addressability_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L162-L170)
**def
Tau.BookIII.Physics.nf_addressability_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T28] NF-addressability: every element of ℤ/Prim(k)ℤ is uniquely
determined by its BNF triple. Combines BNF injectivity (from III.P16)
and sector addressability (from III.D48).
Equations
- Tau.BookIII.Physics.nf_addressability_check bound db = (Tau.BookIII.Physics.sector_addressability_check bound db && Tau.BookIII.Physics.nf_discreteness_check db)
Instances For

---

### `Tau.BookIII.Physics.hodge_filtration_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L176-L205)
**def
Tau.BookIII.Physics.hodge_filtration_check
(db : Denotation.TauIdx)
 :Bool**


[III.P19] Hodge filtration at level k: B-part ⊂ B+X ⊂ B+C+X.
Check that the filtration steps are nested.
Equations
- Tau.BookIII.Physics.hodge_filtration_check db = Tau.BookIII.Physics.hodge_filtration_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.hodge_filtration_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L181-L188)@[irreducible]

**def
Tau.BookIII.Physics.hodge_filtration_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.hodge_filtration_check.check_filtration`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L190-L205)@[irreducible]

**def
Tau.BookIII.Physics.hodge_filtration_check.check_filtration
(x pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.spectral_hodge_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L211-L233)
**def
Tau.BookIII.Physics.spectral_hodge_check
(db : Denotation.TauIdx)
 :Bool**


[III.P20] Spectral-Hodge compatibility: the Hodge filtration is
compatible with the label-based spectral decomposition.
B-filtration step ↔ B-type primes, C-step ↔ C-type primes.
Equations
- Tau.BookIII.Physics.spectral_hodge_check db = Tau.BookIII.Physics.spectral_hodge_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.spectral_hodge_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L217-L232)@[irreducible]

**def
Tau.BookIII.Physics.spectral_hodge_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.sigma_fixed_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L251-L252)
**theorem
Tau.BookIII.Physics.sigma_fixed_4 :sigma_fixed_check 4 = true**


---

### `Tau.BookIII.Physics.sigma_fixed_closed_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L254-L255)
**theorem
Tau.BookIII.Physics.sigma_fixed_closed_4 :sigma_fixed_closed_check 4 = true**


---

### `Tau.BookIII.Physics.sector_addr_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L257-L258)
**theorem
Tau.BookIII.Physics.sector_addr_15_4 :sector_addressability_check 15 4 = true**


---

### `Tau.BookIII.Physics.char_sector_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L260-L261)
**theorem
Tau.BookIII.Physics.char_sector_4 :char_sector_check 4 = true**


---

### `Tau.BookIII.Physics.nf_addr_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L263-L264)
**theorem
Tau.BookIII.Physics.nf_addr_15_3 :nf_addressability_check 15 3 = true**


---

### `Tau.BookIII.Physics.hodge_filt_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L266-L267)
**theorem
Tau.BookIII.Physics.hodge_filt_4 :hodge_filtration_check 4 = true**


---

### `Tau.BookIII.Physics.spectral_hodge_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L269-L270)
**theorem
Tau.BookIII.Physics.spectral_hodge_5 :spectral_hodge_check 5 = true**


---

### `Tau.BookIII.Physics.zero_is_sigma_fixed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L276-L278)
**theorem
Tau.BookIII.Physics.zero_is_sigma_fixed :is_sigma_fixed { b_part := 0, c_part := 0, x_part := 0, depth := 3 } = true**


[III.D47] Structural: zero BNF is always σ-fixed.

---

### `Tau.BookIII.Physics.sigma_fixed_swap_id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L280-L283)
**theorem
Tau.BookIII.Physics.sigma_fixed_swap_id
(nf : Spectral.BoundaryNF)

(h : nf.b_part = nf.c_part)
 :polarity_swap nf = nf**


[III.D47] Structural: polarity swap of σ-fixed is identity.

---

### `Tau.BookIII.Physics.addr_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L285-L287)
**theorem
Tau.BookIII.Physics.addr_10_1 :sector_addressability_check 10 1 = true**


[III.D48] Structural: addressability at depth 1.

---

### `Tau.BookIII.Physics.nf_addr_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Physics/Hodge.lean#L289-L291)
**theorem
Tau.BookIII.Physics.nf_addr_10_1 :nf_addressability_check 10 1 = true**


[III.T28] Structural: NF-addressability at depth 1.
