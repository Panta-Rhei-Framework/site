---
layout: taulib-doc
title: "TauLib.BookI.Polarity.CRTBasis"
permalink: /verify/taulib/docs/book-i-polarity-crt-basis/
lane: verify
module_name: "TauLib.BookI.Polarity.CRTBasis"
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

# TauLib.Polarity.CRTBasis


Formal proofs of CRT basis orthogonality and the CRT round-trip theorem.
All results are universal (∀ depth, ∀ inputs), parameterized by `CRTHyp k`.

## Main Results


- `coprime_product`: coprimality preserved under multiplication

- `prime_coprime_primorial`: p_{k+1} coprime to M_k

- `cofactor_coprime`: M_k/p_{i+1} coprime to p_{i+1}

- `crt_basis_diagonal`: e_i ≡ 1 (mod p_{i+1})

- `crt_basis_off_diagonal`: e_i ≡ 0 (mod p_{j+1}) for j ≠ i

- `crt_unique_mod`: CRT uniqueness direction

- `crt_roundtrip_formal`: CRT round-trip theorem


---

### `Tau.Polarity.coprime_product`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L29-L59)
**theorem
Tau.Polarity.coprime_product
{a b c : ℕ}

(hac : a.Coprime c)

(hbc : b.Coprime c)
 :(a * b).Coprime c**


coprime(a,c) ∧ coprime(b,c) → coprime(a*b,c).
Proof by prime factor contradiction using euclid_lemma.

---

### `Tau.Polarity.coprime_product_right`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L61-L65)
**theorem
Tau.Polarity.coprime_product_right
{a b c : ℕ}

(hca : c.Coprime a)

(hcb : c.Coprime b)
 :c.Coprime (a * b)**


Symmetric form: coprime(c,a) ∧ coprime(c,b) → coprime(c,a*b).

---

### `Tau.Polarity.prime_coprime_primorial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L88-L95)
**theorem
Tau.Polarity.prime_coprime_primorial
{k : Denotation.TauIdx}

(hyp : CRTHyp (k + 1))
 :Nat.Coprime (nth_prime (k + 1)) (primorial k)**


The (k+1)-th prime is coprime to the k-th primorial.

---

### `Tau.Polarity.cofactor_exact`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L101-L104)
**theorem
Tau.Polarity.cofactor_exact
{k i : Denotation.TauIdx}

(hi : i + 1 ≤ k)
 :primorial k / nth_prime (i + 1) * nth_prime (i + 1) = primorial k**


Exact division: cofactor * p_{i+1} = M_k.

---

### `Tau.Polarity.cofactor_coprime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L106-L134)
**theorem
Tau.Polarity.cofactor_coprime
{k i : Denotation.TauIdx}
 :i < k → CRTHyp k → Nat.Coprime (primorial k / nth_prime (i + 1)) (nth_prime (i + 1))**


Key induction: the primorial cofactor M_k/p_{i+1} is coprime to p_{i+1}.

---

### `Tau.Polarity.other_prime_dvd_cofactor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L140-L157)
**theorem
Tau.Polarity.other_prime_dvd_cofactor
{k i j : Denotation.TauIdx}

(hi : i < k)

(hj : j < k)

(hne : i ≠ j)

(hyp : CRTHyp k)
 :nth_prime (j + 1) ∣ primorial k / nth_prime (i + 1)**


p_{j+1} divides the cofactor M_k/p_{i+1} when j ≠ i (both < k).

---

### `Tau.Polarity.crt_basis_diagonal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L169-L180)
**theorem
Tau.Polarity.crt_basis_diagonal
{k i : Denotation.TauIdx}

(hi : i < k)

(hyp : CRTHyp k)
 :crt_basis k i % nth_prime (i + 1) = 1**


e_i ≡ 1 (mod p_{i+1}): diagonal case of CRT basis orthogonality.

---

### `Tau.Polarity.crt_basis_off_diagonal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L182-L191)
**theorem
Tau.Polarity.crt_basis_off_diagonal
{k i j : Denotation.TauIdx}

(hi : i < k)

(hj : j < k)

(hne : i ≠ j)

(hyp : CRTHyp k)
 :crt_basis k i % nth_prime (j + 1) = 0**


e_i ≡ 0 (mod p_{j+1}) for j ≠ i: off-diagonal case.

---

### `Tau.Polarity.coprime_mul_dvd`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L226-L232)
**theorem
Tau.Polarity.coprime_mul_dvd
{p q n : ℕ}

(hcop : p.Coprime q)

(hp : p ∣ n)

(hq : q ∣ n)
 :p * q ∣ n**


Coprime divisibility product: gcd(p,q)=1, p∣n, q∣n → p*q∣n.

---

### `Tau.Polarity.crt_unique_mod`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L278-L296)
**theorem
Tau.Polarity.crt_unique_mod
{k : Denotation.TauIdx}
 :CRTHyp k →
 ∀ {a b : Denotation.TauIdx},
 (∀ (l : Denotation.TauIdx), l < k → a % nth_prime (l + 1) = b % nth_prime (l + 1)) →
 a % primorial k = b % primorial k**


CRT uniqueness: pointwise agreement at each prime implies agreement
modulo the primorial.

---

### `Tau.Polarity.crt_roundtrip_formal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L430-L450)
**theorem
Tau.Polarity.crt_roundtrip_formal
{x k : Denotation.TauIdx}

(hyp : CRTHyp k)
 :crt_reconstruct (crt_decompose x k) k = x % primorial k**


CRT round-trip: reconstruct ∘ decompose = id (mod M_k).

---

### `Tau.Polarity.crt_reconstruct_mod_prime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/CRTBasis.lean#L464-L473)
**theorem
Tau.Polarity.crt_reconstruct_mod_prime
{k l : Denotation.TauIdx}

(residues : List Denotation.TauIdx)

(hl : l < k)

(hyp : CRTHyp k)
 :crt_reconstruct residues k % nth_prime (l + 1) = residues.getD l 0 % nth_prime (l + 1)**


CRT projection: crt_reconstruct residues k mod p_{l+1} = residues[l] mod p_{l+1}.
This is the key interface theorem for downstream formal proofs
(Teichmüller retraction, orthogonality, etc.).
