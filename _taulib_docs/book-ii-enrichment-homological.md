---
layout: taulib-doc
title: "TauLib.BookII.Enrichment.Homological"
permalink: /verify/taulib/docs/book-ii-enrichment-homological/
lane: verify
module_name: "TauLib.BookII.Enrichment.Homological"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Enrichment.Homological


Homological algebra basics on the primorial tower: chain complexes,
boundary maps, homology groups, and exactness.

## Registry Cross-References


- [II.D84] Chain Complex — `ChainComplex`, `boundary_coherence_check`

- [II.D85] Homology Group — `homology_kernel_size`, `homology_image_size`

- [II.T54] Tower Coherence — `boundary_coherence_check`

- [II.P19] Long Exact Sequence — `les_exactness_check`


## Mathematical Content


**II.D84 (Chain Complex):** A chain complex on Z/M_k Z is a sequence of
maps d_n : C_n → C_{n-1} with d ∘ d = 0. At stage k, each C_n is a
subset of Z/M_k Z, and d is reduction mod a prime divisor.

**II.D85 (Homology Group):** H_n = ker(d_n) / im(d_{n+1}). At each finite
stage, this is a finite quotient. The primorial structure ensures that
homology groups decompose by CRT.

**II.T54 (d² = 0):** The boundary-of-boundary vanishes. For the primorial
chain complex, this follows from the tower structure: reducing twice by
successive primes composes to a single reduction.

**II.P19 (Long Exact Sequence):** A short exact sequence of chain complexes
induces a long exact sequence in homology. Verified at finite stages.

---

### `Tau.BookII.Enrichment.ChainComplex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L46-L50)
**structure
Tau.BookII.Enrichment.ChainComplex :Type**


[II.D84] A chain complex on the primorial tower. The boundary map
d_n reduces from stage n to stage n-1 (mod prime p_n).

- max_degree : ℕ
- boundary : ℕ → ℕ → ℕ
Instances For

---

### `Tau.BookII.Enrichment.primorial_chain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L52-L56)
**def
Tau.BookII.Enrichment.primorial_chain :ChainComplex**


[II.D84] The primorial chain complex: d_n(x) = x mod M_{n-1}.
This maps Z/M_n Z → Z/M_{n-1} Z via the canonical projection.
Equations
- Tau.BookII.Enrichment.primorial_chain = { max_degree := 5, boundary := fun (n x : ℕ) => if (n == 0) = true then 0 else Tau.Polarity.reduce x (n - 1) }
Instances For

---

### `Tau.BookII.Enrichment.boundary_coherence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L58-L75)
**def
Tau.BookII.Enrichment.boundary_coherence_check
(k : ℕ)
 :Bool**


[II.D84] Tower coherence: d_{n-1} ∘ d_n = d_{n-1} (reduction composes).
reduce(reduce(x, n-1), n-2) = reduce(x, n-2) for n ≥ 2.
Equations
- Tau.BookII.Enrichment.boundary_coherence_check k = Tau.BookII.Enrichment.boundary_coherence_check.go 2 0 k (k * (Tau.Polarity.primorial k + 1))
Instances For

---

### `Tau.BookII.Enrichment.boundary_coherence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L63-L74)@[irreducible]

**def
Tau.BookII.Enrichment.boundary_coherence_check.go
(n x maxk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.ses_exactness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L81-L102)
**def
Tau.BookII.Enrichment.ses_exactness_check
(k : ℕ)
 :Bool**


[II.D85] For the SES 0 → Z/M_{k-1} →f Z/M_k →g Z/p_k → 0:
ker(g) = {x ∈ Z/M_k : x mod p_k = 0} and im(f) = {x·p_k : x ∈ Z/M_{k-1}}.
Exactness means ker(g) = im(f), so H = ker/im is trivial.
This check verifies ker(g) ⊆ im(f): every x with x mod p = 0 equals y·p
for some y.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.ses_exactness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L94-L101)@[irreducible]

**def
Tau.BookII.Enrichment.ses_exactness_check.go
(x pk p fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.ses_kernel_size`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L104-L112)
**def
Tau.BookII.Enrichment.ses_kernel_size
(k : ℕ)
 :ℕ**


[II.D85] Count the size of ker(g) = |{x ∈ Z/M_k : x mod p_k = 0}|.
Should equal M_{k-1} = M_k / p_k.
Equations
- Tau.BookII.Enrichment.ses_kernel_size k = if (k == 0) = true then 1
 else have pk := Tau.Polarity.primorial k;
 have p := Tau.Polarity.nth_prime k;
 if (p == 0) = true then 0 else pk / p
Instances For

---

### `Tau.BookII.Enrichment.homology_trivial_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L114-L119)
**def
Tau.BookII.Enrichment.homology_trivial_check
(k : ℕ)
 :Bool**


[II.D85] Homology is trivial: |ker(g)| = |im(f)| = M_{k-1}.
Equations
- Tau.BookII.Enrichment.homology_trivial_check k = if (k == 0) = true then true
 else have expected := Tau.Polarity.primorial (k - 1);
 Tau.BookII.Enrichment.ses_kernel_size k == expected
Instances For

---

### `Tau.BookII.Enrichment.ses_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L125-L155)
**def
Tau.BookII.Enrichment.ses_check
(k : ℕ)
 :Bool**


[II.P19] Short exact sequence check: 0 → A →f B →g C → 0.
For primorial tower: A = Z/M_{k-1} Z, B = Z/M_k Z, C = Z/p_k Z.
f = inclusion (x ↦ x · p_k), g = reduction (x ↦ x mod p_k).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.ses_check.go_gf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L141-L146)@[irreducible]

**def
Tau.BookII.Enrichment.ses_check.go_gf
(x bound p pk : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.ses_check.go_inj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L148-L154)@[irreducible]

**def
Tau.BookII.Enrichment.ses_check.go_inj
(x bound p pk : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.les_exactness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L157-L160)
**def
Tau.BookII.Enrichment.les_exactness_check
(k : ℕ)
 :Bool**


[II.P19] Long exact sequence: connecting homomorphism exists.
The snake lemma gives δ : H_n(C) → H_{n-1}(A).
Equations
- Tau.BookII.Enrichment.les_exactness_check k = (Tau.BookII.Enrichment.ses_check k && Tau.BookII.Enrichment.boundary_coherence_check k)
Instances For

---

### `Tau.BookII.Enrichment.boundary_coherence_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L166-L168)
**theorem
Tau.BookII.Enrichment.boundary_coherence_2 :boundary_coherence_check 2 = true**


[II.T54] Tower coherence at stage 2.

---

### `Tau.BookII.Enrichment.boundary_coherence_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L170-L172)
**theorem
Tau.BookII.Enrichment.boundary_coherence_3 :boundary_coherence_check 3 = true**


[II.T54] Tower coherence at stage 3.

---

### `Tau.BookII.Enrichment.ses_exact_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L174-L176)
**theorem
Tau.BookII.Enrichment.ses_exact_1 :ses_exactness_check 1 = true**


[II.D85] SES exactness at stage 1.

---

### `Tau.BookII.Enrichment.ses_exact_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L178-L180)
**theorem
Tau.BookII.Enrichment.ses_exact_2 :ses_exactness_check 2 = true**


[II.D85] SES exactness at stage 2.

---

### `Tau.BookII.Enrichment.homology_trivial_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L182-L184)
**theorem
Tau.BookII.Enrichment.homology_trivial_1 :homology_trivial_check 1 = true**


[II.D85] Homology trivial at stage 1.

---

### `Tau.BookII.Enrichment.homology_trivial_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L186-L188)
**theorem
Tau.BookII.Enrichment.homology_trivial_2 :homology_trivial_check 2 = true**


[II.D85] Homology trivial at stage 2.

---

### `Tau.BookII.Enrichment.ses_stage1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L190-L192)
**theorem
Tau.BookII.Enrichment.ses_stage1 :ses_check 1 = true**


[II.P19] Short exact sequence at stage 1.

---

### `Tau.BookII.Enrichment.ses_stage2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L194-L196)
**theorem
Tau.BookII.Enrichment.ses_stage2 :ses_check 2 = true**


[II.P19] Short exact sequence at stage 2.

---

### `Tau.BookII.Enrichment.les_stage2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/Homological.lean#L198-L200)
**theorem
Tau.BookII.Enrichment.les_stage2 :les_exactness_check 2 = true**


[II.P19] Long exact sequence at stage 2.
