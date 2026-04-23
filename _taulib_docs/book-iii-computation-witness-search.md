---
layout: taulib-doc
title: "TauLib.BookIII.Computation.WitnessSearch"
permalink: /verify/taulib/docs/book-iii-computation-witness-search/
lane: verify
module_name: "TauLib.BookIII.Computation.WitnessSearch"
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

# TauLib.BookIII.Computation.WitnessSearch


NP Witness as Canonical Address, CRT Witness Decomposition,
and Polynomial Refinement.

## Registry Cross-References


- [III.D55] NP Witness as Canonical Address -- `WitnessAddress`, `witness_check`

- [III.P22] CRT Witness Decomposition -- `crt_witness_check`

- [III.P23] Polynomial Refinement -- `polynomial_refinement_check`


## Mathematical Content


**III.D55 (NP Witness):** An NP witness is a τ-address with unique BNF
decomposition (A, B, C, D). The witness carries its own verification:
the BNF components encode the proof structure.

**III.P22 (CRT Witness Decomposition):** The witness search over
ℤ/Prim(k)ℤ decomposes via CRT into independent per-prime searches:
W(x, Prim(k)) ≅ ∏ W(x, p_i). Total search = sum of per-prime searches.

**III.P23 (Polynomial Refinement):** |W(x, p_i)| ≤ p_i for each prime.
Total search cost: O(∑ p_i) = O(k² log k) by PNT.

---

### `Tau.BookIII.Computation.WitnessAddress`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L40-L48)
**structure
Tau.BookIII.Computation.WitnessAddress :Type**


[III.D55] Witness address: a τ-address with its BNF decomposition.
The witness is self-verifying: BNF components encode the proof.

- value : Denotation.TauIdx
- depth : Denotation.TauIdx
- b_part : Denotation.TauIdx
- c_part : Denotation.TauIdx
- x_part : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Computation.instReprWitnessAddress.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L48-L48)
**def
Tau.BookIII.Computation.instReprWitnessAddress.repr :WitnessAddress → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.instReprWitnessAddress`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L48-L48)
**instance
Tau.BookIII.Computation.instReprWitnessAddress :Repr WitnessAddress**

Equations
- Tau.BookIII.Computation.instReprWitnessAddress = { reprPrec := Tau.BookIII.Computation.instReprWitnessAddress.repr }

---

### `Tau.BookIII.Computation.instDecidableEqWitnessAddress`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L48-L48)
**instance
Tau.BookIII.Computation.instDecidableEqWitnessAddress :DecidableEq WitnessAddress**

Equations
- Tau.BookIII.Computation.instDecidableEqWitnessAddress = Tau.BookIII.Computation.instDecidableEqWitnessAddress.decEq

---

### `Tau.BookIII.Computation.instDecidableEqWitnessAddress.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L48-L48)
**def
Tau.BookIII.Computation.instDecidableEqWitnessAddress.decEq
(x✝ x✝¹ : WitnessAddress)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.instBEqWitnessAddress.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L48-L48)
**def
Tau.BookIII.Computation.instBEqWitnessAddress.beq :WitnessAddress → WitnessAddress → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Computation.instBEqWitnessAddress.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Computation.instBEqWitnessAddress`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L48-L48)
**instance
Tau.BookIII.Computation.instBEqWitnessAddress :BEq WitnessAddress**

Equations
- Tau.BookIII.Computation.instBEqWitnessAddress = { beq := Tau.BookIII.Computation.instBEqWitnessAddress.beq }

---

### `Tau.BookIII.Computation.make_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L50-L56)
**def
Tau.BookIII.Computation.make_witness
(x k : Denotation.TauIdx)
 :WitnessAddress**


[III.D55] Construct a witness from a value and depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.witness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L58-L76)
**def
Tau.BookIII.Computation.witness_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D55] Witness validity: the BNF components sum to the value.
Equations
- Tau.BookIII.Computation.witness_check bound db = Tau.BookIII.Computation.witness_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.witness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L62-L75)@[irreducible]

**def
Tau.BookIII.Computation.witness_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.crt_witness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L82-L103)
**def
Tau.BookIII.Computation.crt_witness_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P22] CRT witness decomposition: witness search at Prim(k)
decomposes into independent per-prime searches. Each prime p_i
contributes a search space of size p_i.
Equations
- Tau.BookIII.Computation.crt_witness_check bound db = Tau.BookIII.Computation.crt_witness_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.crt_witness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L88-L102)@[irreducible]

**def
Tau.BookIII.Computation.crt_witness_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.search_space_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L105-L124)
**def
Tau.BookIII.Computation.search_space_check
(db : Denotation.TauIdx)
 :Bool**


[III.P22] Per-prime search space: the number of candidates at each
prime is exactly p_i. Total = ∑ p_i (not ∏ p_i).
Equations
- Tau.BookIII.Computation.search_space_check db = Tau.BookIII.Computation.search_space_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Computation.search_space_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L110-L119)@[irreducible]

**def
Tau.BookIII.Computation.search_space_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.search_space_check.sum_of_primes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L121-L123)@[irreducible]

**def
Tau.BookIII.Computation.search_space_check.sum_of_primes
(i k acc : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Computation.search_space_check.sum_of_primes i k acc = if i > k then acc
 else Tau.BookIII.Computation.search_space_check.sum_of_primes (i + 1) k (acc + Tau.Polarity.nth_prime i)
Instances For

---

### `Tau.BookIII.Computation.polynomial_refinement_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L130-L154)
**def
Tau.BookIII.Computation.polynomial_refinement_check
(db : Denotation.TauIdx)
 :Bool**


[III.P23] Polynomial refinement: each per-prime search space has
size at most p_i. The total cost ∑ p_i grows polynomially in k
(O(k² log k) by PNT).
Equations
- Tau.BookIII.Computation.polynomial_refinement_check db = Tau.BookIII.Computation.polynomial_refinement_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Computation.polynomial_refinement_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L136-L143)@[irreducible]

**def
Tau.BookIII.Computation.polynomial_refinement_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.polynomial_refinement_check.check_per_prime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L145-L153)@[irreducible]

**def
Tau.BookIII.Computation.polynomial_refinement_check.check_per_prime
(i k prev : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.complexity_comparison`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L156-L165)
**def
Tau.BookIII.Computation.complexity_comparison
(k : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx**


[III.P23] Complexity comparison: sum of primes vs primorial at each depth.
Equations
- Tau.BookIII.Computation.complexity_comparison k = (Tau.BookIII.Computation.complexity_comparison.sum_primes 1 k 0, Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookIII.Computation.complexity_comparison.sum_primes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L162-L164)@[irreducible]

**def
Tau.BookIII.Computation.complexity_comparison.sum_primes
(i k acc : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Computation.complexity_comparison.sum_primes i k acc = if i > k then acc
 else Tau.BookIII.Computation.complexity_comparison.sum_primes (i + 1) k (acc + Tau.Polarity.nth_prime i)
Instances For

---

### `Tau.BookIII.Computation.witness_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L182-L183)
**theorem
Tau.BookIII.Computation.witness_15_4 :witness_check 15 4 = true**


---

### `Tau.BookIII.Computation.crt_witness_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L185-L186)
**theorem
Tau.BookIII.Computation.crt_witness_15_4 :crt_witness_check 15 4 = true**


---

### `Tau.BookIII.Computation.search_space_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L188-L189)
**theorem
Tau.BookIII.Computation.search_space_5 :search_space_check 5 = true**


---

### `Tau.BookIII.Computation.polynomial_refinement_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L191-L192)
**theorem
Tau.BookIII.Computation.polynomial_refinement_5 :polynomial_refinement_check 5 = true**


---

### `Tau.BookIII.Computation.witness_zero_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L198-L200)
**theorem
Tau.BookIII.Computation.witness_zero_3 :make_witness 0 3 = { value := 0, depth := 3, b_part := 0, c_part := 0, x_part := 0 }**


[III.D55] Structural: witness of 0 has zero components.

---

### `Tau.BookIII.Computation.crt_faithful_42_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L202-L205)
**theorem
Tau.BookIII.Computation.crt_faithful_42_3 :Polarity.crt_reconstruct (Polarity.crt_decompose 42 3) 3 = 42 % Polarity.primorial 3**


[III.P22] Structural: CRT decomposition at depth 3 is faithful.

---

### `Tau.BookIII.Computation.sum_less_prod_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/WitnessSearch.lean#L207-L210)
**theorem
Tau.BookIII.Computation.sum_less_prod_3 :(complexity_comparison 3).1 < (complexity_comparison 3).2**


[III.P23] Structural: sum of first 3 primes < primorial 3.
