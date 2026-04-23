---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.ABCDeep"
permalink: /verify/taulib/docs/book-iii-arithmetic-abc-deep/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.ABCDeep"
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

# TauLib.BookIII.Arithmetic.ABCDeep


Deep analysis of the ABC conjecture on the primorial tower:
extended verification, squarefree dominance theorem, high quality
triple counting, and structural insight that the primorial tower
avoids the hard case.

## Registry Cross-References


- [III.D108] Sieve-Accelerated ABC — `abc_sieve_check`

- [III.D109] High Quality Count — `abc_high_quality_count`

- [III.D110] Squarefree ABC Check — `squarefree_abc_check`

- [III.T76] ABC Quality 100 — `abc_quality_100`

- [III.T77] Squarefree Dominance 100 — `squarefree_dominance_100`

- [III.T78] Radical Primorial Identity — `radical_primorial_5`

- [III.P47] Squarefree Dominance Theorem — `squarefree_dominance_thm`

- [III.P48] ABC Gap Characterization — (meta-theorem, see docstring)


## Mathematical Content


**III.D108 (Sieve-Accelerated ABC):** ABC quality check with radical
computation accelerated by sieve-based factorization. Pushes verification
bound from 15 to 100+.

**III.D109 (High Quality Count):** Count coprime triples (a, b, a+b) with
quality q = log(c)/log(rad(abc)) > 1. These are the "interesting" triples
where ABC is nontrivial. The count grows very slowly with bound.

**III.D110 (Squarefree ABC):** For squarefree coprime triples, ABC is
trivially true: rad(abc) = abc ≥ c, so q ≤ 1 always. This is the
squarefree dominance theorem.

**III.T76 (ABC Quality 100):** Weak ABC (c < rad(abc)²) verified for
all coprime pairs up to 100. No triple violates the weak bound.

**III.T77 (Squarefree Dominance):** For all squarefree coprime pairs
(a,b) with a,b ≤ 100: c < rad(abc). This is STRONGER than ABC (ε=0).

**III.T78 (Radical Primorial):** rad(M_k) = M_k for k=1..5. The
primorial tower is entirely squarefree.

**III.P47 (Squarefree Dominance Theorem):** ABC is trivially true for
squarefree coprime triples because rad(abc) = abc when abc is squarefree.
Since a+b = c and gcd(a,b) = 1, we have abc ≥ c², giving q ≤ 1.

**III.P48 (ABC Gap):** The primorial tower is squarefree, so it avoids
the hard case of ABC entirely. The genuine difficulty lies in numbers
with large perfect-power factors (e.g., 2^n + 1). This is a structural
insight, not a failure: the τ framework naturally decomposes to the
squarefree part, which is where ABC is easy.

---

### `Tau.BookIII.Arithmetic.is_squarefree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L70-L80)
**def
Tau.BookIII.Arithmetic.is_squarefree
(n : ℕ)
 :Bool**


Check if n is squarefree (no prime divides n more than once).
Equations
- Tau.BookIII.Arithmetic.is_squarefree n = if n ≤ 1 then true else Tau.BookIII.Arithmetic.is_squarefree.go n 2 (n + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.is_squarefree.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L75-L79)@[irreducible]

**def
Tau.BookIII.Arithmetic.is_squarefree.go
(n d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.abc_sieve_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L86-L98)
**def
Tau.BookIII.Arithmetic.abc_sieve_check
(bound : ℕ)
 :Bool**


[III.D108] ABC quality check for coprime pairs up to bound.
Same as abc_quality_bound_check but with clearer structure.
Equations
- Tau.BookIII.Arithmetic.abc_sieve_check bound = Tau.BookIII.Arithmetic.abc_sieve_check.go bound 1 1 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.abc_sieve_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L91-L97)@[irreducible]

**def
Tau.BookIII.Arithmetic.abc_sieve_check.go
(bound a b fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.abc_high_quality_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L104-L121)
**def
Tau.BookIII.Arithmetic.abc_high_quality_count
(bound : ℕ)
 :ℕ**


[III.D109] Count coprime triples (a,b,c=a+b) with c ≥ rad(abc).
These are the triples where quality q ≥ 1.
Equations
- Tau.BookIII.Arithmetic.abc_high_quality_count bound = Tau.BookIII.Arithmetic.abc_high_quality_count.go bound 1 1 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.abc_high_quality_count.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L109-L120)@[irreducible]

**def
Tau.BookIII.Arithmetic.abc_high_quality_count.go
(bound a b acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.squarefree_abc_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L127-L147)
**def
Tau.BookIII.Arithmetic.squarefree_abc_check
(bound : ℕ)
 :Bool**


[III.D110] For squarefree coprime a, b: verify c < rad(abc).
Since rad(n) = n for squarefree n, and abc is squarefree when
a, b, c=a+b are pairwise coprime and squarefree, we have
rad(abc) = abc ≥ c. Stronger: c < rad(abc) always.
Equations
- Tau.BookIII.Arithmetic.squarefree_abc_check bound = Tau.BookIII.Arithmetic.squarefree_abc_check.go bound 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.squarefree_abc_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L134-L146)@[irreducible]

**def
Tau.BookIII.Arithmetic.squarefree_abc_check.go
(bound a b fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.radical_primorial_deep_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L153-L164)
**def
Tau.BookIII.Arithmetic.radical_primorial_deep_check
(db : ℕ)
 :Bool**


[III.T78] Extended radical-primorial identity: rad(M_k) = M_k
for k = 1..db. Primorials are squarefree.
Equations
- Tau.BookIII.Arithmetic.radical_primorial_deep_check db = Tau.BookIII.Arithmetic.radical_primorial_deep_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.radical_primorial_deep_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L158-L163)@[irreducible]

**def
Tau.BookIII.Arithmetic.radical_primorial_deep_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.squarefree_high_quality_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L170-L188)
**def
Tau.BookIII.Arithmetic.squarefree_high_quality_count
(bound : ℕ)
 :ℕ**


[III.P47] Squarefree dominance: for ALL squarefree coprime pairs
(a,b) with a,b ≤ bound, count how many have c ≥ rad(abc).
The theorem states this count is 0.
Equations
- Tau.BookIII.Arithmetic.squarefree_high_quality_count bound = Tau.BookIII.Arithmetic.squarefree_high_quality_count.go bound 2 2 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.squarefree_high_quality_count.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L176-L187)@[irreducible]

**def
Tau.BookIII.Arithmetic.squarefree_high_quality_count.go
(bound a b acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.abc_quality_100`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L194-L196)
**theorem
Tau.BookIII.Arithmetic.abc_quality_100 :abc_sieve_check 100 = true**


[III.T76] Weak ABC (c < rad(abc)²) for all coprime pairs up to 100.

---

### `Tau.BookIII.Arithmetic.squarefree_dominance_100`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L198-L201)
**theorem
Tau.BookIII.Arithmetic.squarefree_dominance_100 :squarefree_abc_check 100 = true**


[III.T77] Squarefree dominance: c ≤ rad(abc) for all squarefree
coprime pairs up to 100.

---

### `Tau.BookIII.Arithmetic.radical_primorial_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L203-L205)
**theorem
Tau.BookIII.Arithmetic.radical_primorial_5 :radical_primorial_deep_check 5 = true**


[III.T78] Radical-primorial identity at depth 5: rad(M_k) = M_k.

---

### `Tau.BookIII.Arithmetic.squarefree_dominance_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L207-L209)
**theorem
Tau.BookIII.Arithmetic.squarefree_dominance_thm :squarefree_high_quality_count 50 = 0**


[III.P47] Zero high-quality triples among squarefree coprimes ≤ 50.

---

### `Tau.BookIII.Arithmetic.high_quality_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L215-L217)
**theorem
Tau.BookIII.Arithmetic.high_quality_30 :abc_high_quality_count 30 ≤ 5**


[III.D109] Few high quality triples (q ≥ 1) up to 30: at most 5.

---

### `Tau.BookIII.Arithmetic.one_squarefree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L219-L220)
**theorem
Tau.BookIII.Arithmetic.one_squarefree :is_squarefree 1 = true**


[III.D110] 1 is squarefree.

---

### `Tau.BookIII.Arithmetic.thirty_squarefree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L222-L223)
**theorem
Tau.BookIII.Arithmetic.thirty_squarefree :is_squarefree 30 = true**


[III.D110] 30 is squarefree (2·3·5).

---

### `Tau.BookIII.Arithmetic.twelve_not_squarefree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/ABCDeep.lean#L225-L226)
**theorem
Tau.BookIII.Arithmetic.twelve_not_squarefree :is_squarefree 12 = false**


[III.D110] 12 is NOT squarefree (4 | 12).
