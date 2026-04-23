---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Cyclotomic"
permalink: /verify/taulib/docs/book-i-boundary-cyclotomic/
lane: verify
module_name: "TauLib.BookI.Boundary.Cyclotomic"
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

# TauLib.Boundary.Cyclotomic


Cyclotomic fields and roots of unity, connecting to the CRT decomposition.

## Registry Cross-References


- [I.D88] CyclotomicField — Roots of unity in modular arithmetic

- [I.T45] Roots of Unity — Basic structure theorems

- [I.R23] Galois Preview — Galois action on roots of unity


## Mathematical Content


Roots of unity are defined modularly over TauIdx: z is an nth root of unity
mod m when z^n ≡ 1 (mod m). Primitive roots require minimality.

The key structural result is the CRT connection: roots of unity mod coprime
moduli decompose as products via the Chinese Remainder Theorem. This connects
the cyclotomic structure to the primorial ladder from Polarity.ChineseRemainder.

The Galois action σ_k : ζ_n ↦ ζ_n^k (for gcd(k,n)=1) preserves the root
of unity property, previewing the structure Gal(Q(ζ_n)/Q) ≅ (Z/nZ)×.

---

### `Tau.Boundary.IsRootOfUnity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L40-L42)
**def
Tau.Boundary.IsRootOfUnity
(n : ℕ)

(z m : Denotation.TauIdx)
 :Prop**


[I.D88] z is an nth root of unity modulo m: z^n ≡ 1 (mod m).
Equations
- Tau.Boundary.IsRootOfUnity n z m = (z ^ n % m = 1 % m)
Instances For

---

### `Tau.Boundary.instDecidableIsRootOfUnity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L44-L46)
**instance
Tau.Boundary.instDecidableIsRootOfUnity
(n : ℕ)

(z m : Denotation.TauIdx)
 :Decidable (IsRootOfUnity n z m)**


IsRootOfUnity is decidable (Nat equality is decidable).
Equations
- Tau.Boundary.instDecidableIsRootOfUnity n z m = inferInstanceAs (Decidable (z ^ n % m = 1 % m))

---

### `Tau.Boundary.IsPrimitiveRoot`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L48-L51)
**def
Tau.Boundary.IsPrimitiveRoot
(n : ℕ)

(z m : Denotation.TauIdx)
 :Prop**


z is a primitive nth root of unity mod m: z^n ≡ 1 and z^k ≢ 1
for all 0 < k < n.
Equations
- Tau.Boundary.IsPrimitiveRoot n z m = (Tau.Boundary.IsRootOfUnity n z m ∧ ∀ (k : ℕ), 0 < k → k < n → ¬Tau.Boundary.IsRootOfUnity k z m)
Instances For

---

### `Tau.Boundary.root_of_unity_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L57-L59)
**theorem
Tau.Boundary.root_of_unity_one
(n m : Denotation.TauIdx)
 :IsRootOfUnity n 1 m**


[I.T45] 1 is always an nth root of unity mod any m.

---

### `Tau.Boundary.root_of_unity_pow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L61-L68)
**theorem
Tau.Boundary.root_of_unity_pow
(n : ℕ)

(z m : Denotation.TauIdx)

(k : ℕ)

(hz : IsRootOfUnity n z m)
 :IsRootOfUnity (k * n) z m**


If z^n ≡ 1 (mod m) then z^(k*n) ≡ 1 (mod m).

---

### `Tau.Boundary.CyclotomicRoot`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L70-L74)
**def
Tau.Boundary.CyclotomicRoot
(n : ℕ)

(z m : Denotation.TauIdx)
 :Prop**


The nth cyclotomic polynomial's roots divide x^n - 1.
We capture the key property: if z is a primitive nth root
then z^d ≢ 1 for proper divisors d of n.
Equations
- Tau.Boundary.CyclotomicRoot n z m = Tau.Boundary.IsPrimitiveRoot n z m
Instances For

---

### `Tau.Boundary.root_divides_power`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L76-L80)
**theorem
Tau.Boundary.root_divides_power
(n : ℕ)

(z m : Denotation.TauIdx)

(k : ℕ)

(hk : k > 0)

(hz : IsRootOfUnity n z m)
 :IsRootOfUnity (n * k) z m**


Any root of unity of order n is also a root of order n*k.

---

### `Tau.Boundary.root_of_unity_factor_left`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L86-L97)
**theorem
Tau.Boundary.root_of_unity_factor_left
(n : ℕ)

(z m1 m2 : Denotation.TauIdx)

(hz : IsRootOfUnity n z (m1 * m2))
 :IsRootOfUnity n z m1**


Factor left: a root mod m1*m2 is a root mod m1.

---

### `Tau.Boundary.root_of_unity_factor_right`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L99-L103)
**theorem
Tau.Boundary.root_of_unity_factor_right
(n : ℕ)

(z m1 m2 : Denotation.TauIdx)

(hz : IsRootOfUnity n z (m1 * m2))
 :IsRootOfUnity n z m2**


Factor right: a root mod m1*m2 is a root mod m2.

---

### `Tau.Boundary.euler_totient`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L109-L111)
**def
Tau.Boundary.euler_totient
(n : ℕ)
 :ℕ**


Euler's totient function: φ(n) = #{k : 1 ≤ k ≤ n, gcd(k,n) = 1}.
Equations
- Tau.Boundary.euler_totient n = (List.filter (fun (k : ℕ) => decide (n.Coprime (k + 1))) (List.range n)).length
Instances For

---

### `Tau.Boundary.euler_totient_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L113-L114)
**theorem
Tau.Boundary.euler_totient_one :euler_totient 1 = 1**


φ(1) = 1.

---

### `Tau.Boundary.euler_totient_two`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L116-L117)
**theorem
Tau.Boundary.euler_totient_two :euler_totient 2 = 1**


φ(2) = 1.

---

### `Tau.Boundary.euler_totient_three`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L119-L120)
**theorem
Tau.Boundary.euler_totient_three :euler_totient 3 = 2**


φ(p) = p - 1 for small primes.

---

### `Tau.Boundary.euler_totient_five`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L121-L121)
**theorem
Tau.Boundary.euler_totient_five :euler_totient 5 = 4**


---

### `Tau.Boundary.euler_totient_seven`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L122-L122)
**theorem
Tau.Boundary.euler_totient_seven :euler_totient 7 = 6**


---

### `Tau.Boundary.galois_action`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L128-L137)
**theorem
Tau.Boundary.galois_action
(n k : ℕ)

(z m : Denotation.TauIdx)

(_hk : k.Coprime n)

(hz : IsRootOfUnity n z m)
 :IsRootOfUnity n (z ^ k % m) m**


The Galois action σ_k maps an nth root of unity z to z^k.
When gcd(k, n) = 1, this preserves the root of unity property.
This previews Gal(Q(ζ_n)/Q) ≅ (Z/nZ)×.

---

### `Tau.Boundary.galois_action_comp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Cyclotomic.lean#L139-L143)
**theorem
Tau.Boundary.galois_action_comp
(n j k : ℕ)

(z m : Denotation.TauIdx)

(_hm : m > 0)

(_hz : IsRootOfUnity n z m)
 :(z ^ j % m) ^ k % m = z ^ (j * k) % m**


Composing Galois actions: σ_k ∘ σ_j = σ_{kj}.
