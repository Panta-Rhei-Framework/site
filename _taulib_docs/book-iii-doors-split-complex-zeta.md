---
layout: taulib-doc
title: "TauLib.BookIII.Doors.SplitComplexZeta"
permalink: /verify/taulib/docs/book-iii-doors-split-complex-zeta/
lane: verify
module_name: "TauLib.BookIII.Doors.SplitComplexZeta"
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

# TauLib.BookIII.Doors.SplitComplexZeta


Split-Complex Zeta Function, Functional Equation Involution, and Bipolar Euler Product.

## Registry Cross-References


- [III.D26] Split-Complex Zeta ζ_τ -- `split_zeta_b`, `split_zeta_c`, `split_zeta_check`

- [III.D27] Functional Equation Involution J -- `fe_involution`, `fe_involution_check`

- [III.T16] Bipolar Euler Product -- `bipolar_euler_check`


## Mathematical Content


**III.D26 (Split-Complex Zeta):** ζ_τ(s) = e₊·ζ_B(s) + e₋·ζ_C(s), encoding
the Riemann zeta in split-complex coordinates. B-lobe = B-type primes,
C-lobe = C-type primes.

**III.D27 (Functional Equation Involution):** J exchanges B-lobe and C-lobe
components: J(b, c, x) = (c, b, x). J² = id.

**III.T16 (Bipolar Euler Product):** ζ_τ(s) = ∏_p (1 - Label(p)·p^{-s})^{-1}.
CRT decomposition at each primorial level recovers the partial products.

---

### `Tau.BookIII.Doors.split_zeta_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L38-L40)
**def
Tau.BookIII.Doors.split_zeta_b
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D26] B-lobe partial zeta: product of B-type primes up to depth k.
Delegates to the label product from Trichotomy.
Equations
- Tau.BookIII.Doors.split_zeta_b k = Tau.BookIII.Spectral.compute_label_product Tau.BookIII.Spectral.PrimeLabel.B k
Instances For

---

### `Tau.BookIII.Doors.split_zeta_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L42-L43)
**def
Tau.BookIII.Doors.split_zeta_c
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D26] C-lobe partial zeta: product of C-type primes up to depth k.
Equations
- Tau.BookIII.Doors.split_zeta_c k = Tau.BookIII.Spectral.compute_label_product Tau.BookIII.Spectral.PrimeLabel.C k
Instances For

---

### `Tau.BookIII.Doors.split_zeta_x`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L45-L46)
**def
Tau.BookIII.Doors.split_zeta_x
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D26] X-type partial product (crossing prime contribution).
Equations
- Tau.BookIII.Doors.split_zeta_x k = Tau.BookIII.Spectral.compute_label_product Tau.BookIII.Spectral.PrimeLabel.X k
Instances For

---

### `Tau.BookIII.Doors.split_zeta_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L48-L63)
**def
Tau.BookIII.Doors.split_zeta_check
(db : Denotation.TauIdx)
 :Bool**


[III.D26] Split-complex zeta check: B · C · X = Prim(k).
The three label products account for all primes in the primorial.
Equations
- Tau.BookIII.Doors.split_zeta_check db = Tau.BookIII.Doors.split_zeta_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.split_zeta_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L53-L62)@[irreducible]

**def
Tau.BookIII.Doors.split_zeta_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.fe_involution`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L69-L72)
**def
Tau.BookIII.Doors.fe_involution
(nf : Spectral.BoundaryNF)
 :Spectral.BoundaryNF**


[III.D27] Functional equation involution: exchanges B-lobe and C-lobe
components of a boundary normal form. J(b, c, x) = (c, b, x).
Equations
- Tau.BookIII.Doors.fe_involution nf = { b_part := nf.c_part, c_part := nf.b_part, x_part := nf.x_part, depth := nf.depth }
Instances For

---

### `Tau.BookIII.Doors.fe_involution_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L74-L89)
**def
Tau.BookIII.Doors.fe_involution_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D27] Involution check: J² = identity for all BNFs in range.
Equations
- Tau.BookIII.Doors.fe_involution_check bound db = Tau.BookIII.Doors.fe_involution_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.fe_involution_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L78-L88)@[irreducible]

**def
Tau.BookIII.Doors.fe_involution_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.fe_swap_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L91-L105)
**def
Tau.BookIII.Doors.fe_swap_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D27] J swaps B and C but fixes X.
Equations
- Tau.BookIII.Doors.fe_swap_check bound db = Tau.BookIII.Doors.fe_swap_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.fe_swap_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L95-L104)@[irreducible]

**def
Tau.BookIII.Doors.fe_swap_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.bipolar_euler_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L111-L126)
**def
Tau.BookIII.Doors.bipolar_euler_check
(db : Denotation.TauIdx)
 :Bool**


[III.T16] Bipolar Euler product: B · C · X = Prim(k) and B, C coprime.
Equations
- Tau.BookIII.Doors.bipolar_euler_check db = Tau.BookIII.Doors.bipolar_euler_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.bipolar_euler_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L115-L125)@[irreducible]

**def
Tau.BookIII.Doors.bipolar_euler_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.euler_tower_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L128-L143)
**def
Tau.BookIII.Doors.euler_tower_check
(db : Denotation.TauIdx)
 :Bool**


[III.T16] Tower coherence: products at depth k+1 extend depth k.
Equations
- Tau.BookIII.Doors.euler_tower_check db = Tau.BookIII.Doors.euler_tower_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.euler_tower_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L132-L142)@[irreducible]

**def
Tau.BookIII.Doors.euler_tower_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.split_zeta_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L162-L163)
**theorem
Tau.BookIII.Doors.split_zeta_5 :split_zeta_check 5 = true**


---

### `Tau.BookIII.Doors.fe_involution_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L165-L166)
**theorem
Tau.BookIII.Doors.fe_involution_15_4 :fe_involution_check 15 4 = true**


---

### `Tau.BookIII.Doors.fe_swap_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L168-L169)
**theorem
Tau.BookIII.Doors.fe_swap_15_4 :fe_swap_check 15 4 = true**


---

### `Tau.BookIII.Doors.bipolar_euler_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L171-L172)
**theorem
Tau.BookIII.Doors.bipolar_euler_5 :bipolar_euler_check 5 = true**


---

### `Tau.BookIII.Doors.euler_tower_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L174-L175)
**theorem
Tau.BookIII.Doors.euler_tower_4 :euler_tower_check 4 = true**


---

### `Tau.BookIII.Doors.b_zeta_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L181-L182)
**theorem
Tau.BookIII.Doors.b_zeta_3 :split_zeta_b 3 = 5**


[III.D26] Structural: B-zeta at depth 3 = 5 (only B-type prime ≤ p₃).

---

### `Tau.BookIII.Doors.c_zeta_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L184-L185)
**theorem
Tau.BookIII.Doors.c_zeta_3 :split_zeta_c 3 = 3**


[III.D26] Structural: C-zeta at depth 3 = 3 (only C-type prime ≤ p₃).

---

### `Tau.BookIII.Doors.fe_involution_involutive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L187-L190)
**theorem
Tau.BookIII.Doors.fe_involution_involutive
(nf : Spectral.BoundaryNF)
 :fe_involution (fe_involution nf) = nf**


[III.D27] Structural: involution is own inverse.

---

### `Tau.BookIII.Doors.euler_product_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/SplitComplexZeta.lean#L192-L195)
**theorem
Tau.BookIII.Doors.euler_product_3 :split_zeta_b 3 * split_zeta_c 3 * split_zeta_x 3 = Polarity.primorial 3**


[III.T16] Structural: B · C · X = Prim(3) at depth 3.
