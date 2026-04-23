---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.EnrichedBiSquare"
permalink: /verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.EnrichedBiSquare"
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

# TauLib.BookIII.Arithmetic.EnrichedBiSquare


Enriched Bi-Square at E₁⁺, Finite Factorization Pasting,
and Enriched Bi-Square Comparison.

## Registry Cross-References


- [III.D65] Enriched Bi-Square at E₁⁺ -- `enriched_bisquare_check`

- [III.T38] Finite Factorization Pasting -- `finite_factorization_check`

- [III.T39] Enriched Bi-Square Comparison -- `bisquare_comparison_check`


## Mathematical Content


**III.D65 (Enriched Bi-Square):** Third bi-square in the scaling chain:
algebraic (I.T41) → topological (II.T49) → enriched (III.D65).
Left = sector-coupled tower coherence, right = Langlands functoriality.

**III.T38 (Finite Factorization Pasting):** Every E₁ object factors through
finitely many primitive sector components. The E₁ content of
α_p ∧ α_q = α_{p×q} (CRT = finite factorization).

**III.T39 (Enriched Bi-Square Comparison):** The enriched bi-square has
identical shape and structural maps as the algebraic and topological bi-squares.

---

### `Tau.BookIII.Arithmetic.finite_factorization_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L41-L66)
**def
Tau.BookIII.Arithmetic.finite_factorization_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T38] Finite factorization: every element decomposes via CRT into
per-prime factors, and this decomposition is the bi-square pasting map.
α_p ∧ α_q = α_{p×q} at the sector level.
Equations
- Tau.BookIII.Arithmetic.finite_factorization_check bound db = Tau.BookIII.Arithmetic.finite_factorization_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.finite_factorization_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L47-L65)@[irreducible]

**def
Tau.BookIII.Arithmetic.finite_factorization_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.enriched_bisquare_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L72-L100)
**def
Tau.BookIII.Arithmetic.enriched_bisquare_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D65] Enriched bi-square check: left face = sector-coupled tower
coherence (BNF at k+1 projects to BNF at k), right face = Langlands
functoriality (sector morphisms commute with spectral decomposition).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.enriched_bisquare_check.tower_sector_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L85-L99)@[irreducible]

**def
Tau.BookIII.Arithmetic.enriched_bisquare_check.tower_sector_go
(x k bound db fuel : ℕ)
 :Bool**


Left face: BNF tower coherence with sector products.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bisquare_comparison_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L106-L135)
**def
Tau.BookIII.Arithmetic.bisquare_comparison_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T39] Bi-square comparison: the enriched bi-square (this) has the
same shape as the algebraic (Book I) and topological (Book II) bi-squares.
Shape = (left: tower coherence) × (right: spectral decomposition) with
CRT pasting. Verified: all three check the same structural properties.
Equations
- Tau.BookIII.Arithmetic.bisquare_comparison_check bound db = Tau.BookIII.Arithmetic.bisquare_comparison_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.bisquare_comparison_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L113-L134)@[irreducible]

**def
Tau.BookIII.Arithmetic.bisquare_comparison_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.enriched_bisquare_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L149-L150)
**theorem
Tau.BookIII.Arithmetic.enriched_bisquare_10_3 :enriched_bisquare_check 10 3 = true**


---

### `Tau.BookIII.Arithmetic.finite_factorization_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L152-L153)
**theorem
Tau.BookIII.Arithmetic.finite_factorization_15_4 :finite_factorization_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.bisquare_comparison_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L155-L156)
**theorem
Tau.BookIII.Arithmetic.bisquare_comparison_15_4 :bisquare_comparison_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.enriched_bs_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L162-L164)
**theorem
Tau.BookIII.Arithmetic.enriched_bs_10_1 :enriched_bisquare_check 10 1 = true**


[III.D65] Structural: enriched bi-square at depth 1.

---

### `Tau.BookIII.Arithmetic.factorization_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L166-L168)
**theorem
Tau.BookIII.Arithmetic.factorization_10_1 :finite_factorization_check 10 1 = true**


[III.T38] Structural: factorization at depth 1.

---

### `Tau.BookIII.Arithmetic.comparison_10_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L170-L172)
**theorem
Tau.BookIII.Arithmetic.comparison_10_1 :bisquare_comparison_check 10 1 = true**


[III.T39] Structural: comparison at depth 1.
