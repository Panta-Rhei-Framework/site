---
layout: taulib-doc
title: "TauLib.BookI.Polarity.ChineseRemainder"
permalink: /verify/taulib/docs/book-i-polarity-chinese-remainder/
lane: verify
module_name: "TauLib.BookI.Polarity.ChineseRemainder"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Polarity.ChineseRemainder


Chinese Remainder Theorem decomposition and reconstruction on the primorial ladder.

## Registry Cross-References


- [I.D29] CRT Decomposition — `crt_decompose`, `crt_reconstruct`, `crt_basis`

- [I.D28] Boundary Local Ring — CRT structure of Z/M_kZ


## Ground Truth Sources


- chunk_0243_M002286: CRT chapter, constructive decomposition via coprime idempotents

- chunk_0314_M002691: Finite-stage CRT, CRT coherence with primorial reduction


## Mathematical Content


The Chinese Remainder Theorem for the primorial M_k = p₁ · p₂ · ... · p_k gives:
Z/M_kZ ≅ Z/p₁Z × Z/p₂Z × ... × Z/p_kZ

Forward map (decomposition): x ↦ (x mod p₁, ..., x mod p_k)
Inverse map (reconstruction): (r₁,...,r_k) ↦ Σ rᵢ · eᵢ mod M_k
where eᵢ = (M_k/pᵢ) · (M_k/pᵢ)⁻¹ mod M_k are coprime idempotents.

All constructions are computable. Correctness is verified by extensive native_decide.

---

### `Tau.Polarity.mod_inv_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L38-L44)@[irreducible]

**def
Tau.Polarity.mod_inv_go
(a m x fuel : ℕ)
 :ℕ**


Find modular inverse of a mod m by brute-force search.
Returns x such that (a * x) % m = 1, or 0 if not found.
Equations
- Tau.Polarity.mod_inv_go a m x fuel = if fuel = 0 then 0 else if (a * x % m == 1) = true then x else Tau.Polarity.mod_inv_go a m (x + 1) (fuel - 1)
Instances For

---

### `Tau.Polarity.mod_inv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L46-L47)
**def
Tau.Polarity.mod_inv
(a m : ℕ)
 :ℕ**


Modular inverse: a⁻¹ mod m. Correct for coprime a, m with m > 1.
Equations
- Tau.Polarity.mod_inv a m = Tau.Polarity.mod_inv_go a m 1 m
Instances For

---

### `Tau.Polarity.mod_inv_go_correct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L53-L71)
**theorem
Tau.Polarity.mod_inv_go_correct
(a m x fuel : ℕ)

(h_exists : ∃ (y : ℕ), x ≤ y ∧ y < x + fuel ∧ a * y % m = 1)
 :a * mod_inv_go a m x fuel % m = 1**


mod_inv_go finds a valid inverse when one exists in range.

---

### `Tau.Polarity.mod_inv_correct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L73-L84)
**theorem
Tau.Polarity.mod_inv_correct
(a m : ℕ)

(hcop : a.Coprime m)

(hm : m > 1)
 :a * mod_inv a m % m = 1**


mod_inv is correct for coprime inputs with m > 1.

---

### `Tau.Polarity.crt_decompose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L90-L93)
**def
Tau.Polarity.crt_decompose
(x k : Denotation.TauIdx)
 :List Denotation.TauIdx**


CRT forward map: x ↦ (x mod p₁, ..., x mod p_k).
Returns the list of residues modulo each prime.
Equations
- Tau.Polarity.crt_decompose x k = List.map (fun (i : Tau.Denotation.TauIdx) => x % Tau.Polarity.nth_prime (i + 1)) (List.range k)
Instances For

---

### `Tau.Polarity.crt_basis`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L99-L106)
**def
Tau.Polarity.crt_basis
(k i : Denotation.TauIdx)
 :Denotation.TauIdx**


CRT basis element eᵢ: the unique element of Z/M_kZ with
eᵢ ≡ 1 (mod pᵢ) and eᵢ ≡ 0 (mod pⱼ) for j ≠ i.
i is 0-indexed: crt_basis k 0 corresponds to p₁.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.crt_reconstruct_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L112-L121)@[irreducible]

**def
Tau.Polarity.crt_reconstruct_go
(residues : List Denotation.TauIdx)

(k : Denotation.TauIdx)

(i fuel : ℕ)

(acc : Denotation.TauIdx)
 :Denotation.TauIdx**


CRT reconstruction accumulator: Σ rᵢ · eᵢ mod M_k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.crt_reconstruct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L123-L125)
**def
Tau.Polarity.crt_reconstruct
(residues : List Denotation.TauIdx)

(k : Denotation.TauIdx)
 :Denotation.TauIdx**


CRT inverse map: (r₁,...,r_k) ↦ Σ rᵢ · eᵢ mod M_k.
Equations
- Tau.Polarity.crt_reconstruct residues k = Tau.Polarity.crt_reconstruct_go residues k 0 k 0
Instances For

---

### `Tau.Polarity.crt_basis_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L131-L133)
**def
Tau.Polarity.crt_basis_check
(k i j : Denotation.TauIdx)
 :Bool**


CRT basis orthogonality: eᵢ mod pⱼ = δᵢⱼ.
Equations
- Tau.Polarity.crt_basis_check k i j = (Tau.Polarity.crt_basis k i % Tau.Polarity.nth_prime (j + 1) == if (i == j) = true then 1 else 0)
Instances For

---

### `Tau.Polarity.crt_roundtrip_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L135-L137)
**def
Tau.Polarity.crt_roundtrip_check
(x k : Denotation.TauIdx)
 :Bool**


CRT round-trip: decompose ∘ reconstruct = id (mod M_k).
Equations
- Tau.Polarity.crt_roundtrip_check x k = (Tau.Polarity.crt_reconstruct (Tau.Polarity.crt_decompose x k) k == x % Tau.Polarity.primorial k)
Instances For

---

### `Tau.Polarity.crt_coherence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L139-L143)
**def
Tau.Polarity.crt_coherence_check
(x k l : Denotation.TauIdx)
 :Bool**


CRT coherence: reducing CRT output from depth l to depth k
gives the same as CRT at depth k with first k residues.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.crt_exhaustive_check_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L145-L150)@[irreducible]

**def
Tau.Polarity.crt_exhaustive_check_go
(k x : Denotation.TauIdx)

(fuel : ℕ)
 :Bool**


CRT full-range check: round-trip holds for all x in [0, M_k).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.crt_exhaustive_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L152-L153)
**def
Tau.Polarity.crt_exhaustive_check
(k : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Polarity.crt_exhaustive_check k = Tau.Polarity.crt_exhaustive_check_go k 0 (Tau.Polarity.primorial k)
Instances For

---

### `Tau.Polarity.crt_idempotent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L159-L163)
**def
Tau.Polarity.crt_idempotent_check
(k i : Denotation.TauIdx)
 :Bool**


eᵢ · eᵢ ≡ eᵢ (mod M_k): each basis element is idempotent.
Equations
- Tau.Polarity.crt_idempotent_check k i = (Tau.Polarity.crt_basis k i * Tau.Polarity.crt_basis k i % Tau.Polarity.primorial k == Tau.Polarity.crt_basis k i)
Instances For

---

### `Tau.Polarity.crt_orthogonal_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L165-L167)
**def
Tau.Polarity.crt_orthogonal_check
(k i j : Denotation.TauIdx)
 :Bool**


eᵢ · eⱼ ≡ 0 (mod M_k) for i ≠ j: distinct basis elements are orthogonal.
Equations
- Tau.Polarity.crt_orthogonal_check k i j = (i == j || Tau.Polarity.crt_basis k i * Tau.Polarity.crt_basis k j % Tau.Polarity.primorial k == 0)
Instances For

---

### `Tau.Polarity.crt_partition_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L169-L174)@[irreducible]

**def
Tau.Polarity.crt_partition_go
(k : Denotation.TauIdx)

(i fuel : ℕ)

(acc : Denotation.TauIdx)
 :Denotation.TauIdx**


Σ eᵢ ≡ 1 (mod M_k): basis elements sum to unity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.crt_partition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L176-L177)
**def
Tau.Polarity.crt_partition_check
(k : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Polarity.crt_partition_check k = (Tau.Polarity.crt_partition_go k 0 k 0 == 1 % Tau.Polarity.primorial k)
Instances For

---

### `Tau.Polarity.crt_add_hom_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L301-L307)
**def
Tau.Polarity.crt_add_hom_check
(a b k : Denotation.TauIdx)
 :Bool**


CRT is a ring homomorphism: decompose(a+b) = decompose(a) + decompose(b) mod primes.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.crt_mul_hom_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ChineseRemainder.lean#L309-L315)
**def
Tau.Polarity.crt_mul_hom_check
(a b k : Denotation.TauIdx)
 :Bool**


CRT is a ring homomorphism: decompose(a*b) = decompose(a) * decompose(b) mod primes.
Equations
- One or more equations did not get rendered due to their size.
Instances For
