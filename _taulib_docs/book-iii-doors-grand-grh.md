---
layout: taulib-doc
title: "TauLib.BookIII.Doors.GrandGRH"
permalink: /verify/taulib/docs/book-iii-doors-grand-grh/
lane: verify
module_name: "TauLib.BookIII.Doors.GrandGRH"
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

# TauLib.BookIII.Doors.GrandGRH


Grand GRH (Generalized Riemann Hypothesis), Prime Polarity Scaling, and
L-Functions as Spectral Determinants.

## Registry Cross-References


- [III.D31] Grand GRH (τ-effective) -- `grand_grh_finite_check` [AXIOM at adelic level]

- [III.T20] Prime Polarity Scaling Theorem -- `prime_polarity_scaling_check`

- [III.D32] L-Function as Spectral Determinant -- `l_function_spectral_check`


## Mathematical Content


**III.D31 (Grand GRH):** At adelic level: for all boundary characters on 𝔸_τ,
the corresponding L-function has all non-trivial zeros on Re(s) = ½.
CONJECTURAL at the adelic extension beyond finite primorial cutoff.

**III.T20 (Prime Polarity Scaling):** The GRH at each primorial depth
decomposes into three independent statements via Label_n: purity of
B-sector zeros, purity of C-sector zeros, and balance of X-sector zeros.

**III.D32 (L-Function as Spectral Determinant):** All L-functions as spectral
determinants of the universal operator at finite cutoff.

---

### `Tau.BookIII.Doors.grand_grh_finite_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L40-L62)
**def
Tau.BookIII.Doors.grand_grh_finite_check
(db : Denotation.TauIdx)
 :Bool**


[III.D31] Grand GRH at finite primorial level k: the finite Euler
product decomposes correctly via B/C/X labels, and each sector
has the correct zero structure at this level.
Equations
- Tau.BookIII.Doors.grand_grh_finite_check db = Tau.BookIII.Doors.grand_grh_finite_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.grand_grh_finite_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L46-L61)@[irreducible]

**def
Tau.BookIII.Doors.grand_grh_finite_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.grand_grh_adelic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L64-L68)
**axiom
Tau.BookIII.Doors.grand_grh_adelic
(k : ℕ)
 :grand_grh_finite_check k = true**


[III.D31] **Grand GRH Axiom**: the adelic extension of GRH beyond
finite primorial cutoff. CONJECTURAL SCOPE.
All finite checks pass; the axiom asserts the infinite/adelic limit.

---

### `Tau.BookIII.Doors.prime_polarity_scaling_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L74-L100)
**def
Tau.BookIII.Doors.prime_polarity_scaling_check
(db : Denotation.TauIdx)
 :Bool**


[III.T20] Prime polarity scaling: the GRH decomposition into B/C/X
sectors is compatible across primorial levels. Scaling from level k
to k+1 preserves polarity type of each prime.
Equations
- Tau.BookIII.Doors.prime_polarity_scaling_check db = Tau.BookIII.Doors.prime_polarity_scaling_check.go db 1 1 ((db + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.prime_polarity_scaling_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L80-L99)@[irreducible]

**def
Tau.BookIII.Doors.prime_polarity_scaling_check.go
(db : Denotation.TauIdx)

(i k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.sector_growth_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L102-L117)
**def
Tau.BookIII.Doors.sector_growth_check
(db : Denotation.TauIdx)
 :Bool**


[III.T20] Sector growth rates: B-product and C-product grow at
different rates (B = multiplicative/exponent, C = additive/tetration).
Equations
- Tau.BookIII.Doors.sector_growth_check db = Tau.BookIII.Doors.sector_growth_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.sector_growth_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L107-L116)@[irreducible]

**def
Tau.BookIII.Doors.sector_growth_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.l_function_spectral_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L123-L146)
**def
Tau.BookIII.Doors.l_function_spectral_check
(db : Denotation.TauIdx)
 :Bool**


[III.D32] L-function as spectral determinant at finite level:
L_{≤k}(s) = ∏_{p ≤ p_k} (1 - p^{-s})^{-1}.
At τ-level: the finite Euler product equals the primorial when
all factors are included, and decomposes via the B/C/X labels.
Equations
- Tau.BookIII.Doors.l_function_spectral_check db = Tau.BookIII.Doors.l_function_spectral_check.go db 1 1 ((db + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.l_function_spectral_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L130-L145)@[irreducible]

**def
Tau.BookIII.Doors.l_function_spectral_check.go
(db : Denotation.TauIdx)

(i k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.grand_grh_finite_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L161-L162)
**theorem
Tau.BookIII.Doors.grand_grh_finite_5 :grand_grh_finite_check 5 = true**


---

### `Tau.BookIII.Doors.prime_polarity_scaling_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L164-L165)
**theorem
Tau.BookIII.Doors.prime_polarity_scaling_5 :prime_polarity_scaling_check 5 = true**


---

### `Tau.BookIII.Doors.sector_growth_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L167-L168)
**theorem
Tau.BookIII.Doors.sector_growth_5 :sector_growth_check 5 = true**


---

### `Tau.BookIII.Doors.l_function_spectral_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L170-L171)
**theorem
Tau.BookIII.Doors.l_function_spectral_5 :l_function_spectral_check 5 = true**


---

### `Tau.BookIII.Doors.grand_grh_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L177-L179)
**theorem
Tau.BookIII.Doors.grand_grh_3 :grand_grh_finite_check 3 = true**


[III.D31] Structural: Grand GRH finite check at depth 3.

---

### `Tau.BookIII.Doors.label_5_is_B`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L181-L182)
**theorem
Tau.BookIII.Doors.label_5_is_B :Spectral.label_direct 5 = Spectral.PrimeLabel.B**


[III.T20] Structural: label classification of prime 5 (5 ≡ 1 mod 4 → B).

---

### `Tau.BookIII.Doors.label_3_is_C`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L183-L184)
**theorem
Tau.BookIII.Doors.label_3_is_C :Spectral.label_direct 3 = Spectral.PrimeLabel.C**


[III.T20] Structural: label classification of prime 3 (3 ≡ 3 mod 4 → C).

---

### `Tau.BookIII.Doors.l_function_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L186-L189)
**theorem
Tau.BookIII.Doors.l_function_3 :split_zeta_b 3 * split_zeta_c 3 * split_zeta_x 3 = Polarity.primorial 3**


[III.D32] Structural: L-function at depth 3 = Prim(3).

---

### `Tau.BookIII.Doors.grand_grh_from_axiom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/GrandGRH.lean#L191-L194)
**theorem
Tau.BookIII.Doors.grand_grh_from_axiom
(k : ℕ)
 :grand_grh_finite_check k = true**


[III.D31] Structural: Grand GRH from axiom.
