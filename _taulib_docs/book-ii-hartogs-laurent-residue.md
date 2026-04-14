---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.LaurentResidue"
permalink: /verify/taulib/docs/book-ii-hartogs-laurent-residue/
lane: verify
module_name: "TauLib.BookII.Hartogs.LaurentResidue"
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

# TauLib.BookII.Hartogs.LaurentResidue


Laurent expansion, residue, and meromorphic functions in the tau-setting.

## Registry Cross-References


- [II.D42] Laurent Expansion -- `laurent_coeff`, `laurent_expansion_check`

- [II.D43] Residue -- `tau_residue`, `residue_determines_check`

- [II.D44] Meromorphic Function -- `MeromorphicFun`, `meromorphic_check`

- [II.T30] Residue Theorem -- `residue_reconstruction_check`, `crt_residue_thm`


## Mathematical Content


At each stage k, a point x in Z/M_k Z decomposes via CRT into residues
at the k individual prime factors p_1, ..., p_k:

x mod M_k <--> (x mod p_1, x mod p_2, ..., x mod p_k)

This CRT decomposition IS the Laurent expansion in the tau-setting:
each "Laurent coefficient" at prime p_i is the residue x mod p_i.

**Laurent expansion (II.D42):** The i-th Laurent coefficient of x at
stage k is x mod p_i (the projection onto the i-th CRT factor).

**Residue (II.D43):** The residue at prime p_i is laurent_coeff(x, k, i)
= x mod p_i. The residues determine x mod M_k via CRT.

**Meromorphic function (II.D44):** A function that is holomorphic (tower-
coherent) except at finitely many exceptional stages. In the tau-setting,
all tower-coherent functions on the primorial ladder are meromorphic
(there are no "essential singularities" in the finite cyclic world).

**Residue theorem (II.T30):** The CRT residues at each prime factor
completely determine the function value at that stage. This is the
tau-analog of the classical residue theorem: the sum of residues
(in the CRT sense) recovers the original function value.

The reconstruction works because M_k = p_1 * ... * p_k and all p_i
are pairwise coprime, so CRT gives a unique element of Z/M_k Z from
the tuple (x mod p_1, ..., x mod p_k).

---

### `Tau.BookII.Hartogs.laurent_coeff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L55-L65)
**def
Tau.BookII.Hartogs.laurent_coeff
(x k prime_idx : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D42] The i-th Laurent coefficient of x at stage k:
the residue of x modulo the i-th prime p_i.

In the CRT decomposition of Z/M_k Z = Z/p_1 Z x ... x Z/p_k Z,
the i-th component is x mod p_i. This is the tau-analog of the
i-th Laurent coefficient in the expansion around the i-th prime.

Returns 0 if prime_idx = 0 or prime_idx > k (out of range).
Equations
- Tau.BookII.Hartogs.laurent_coeff x k prime_idx = if (prime_idx == 0 || decide (prime_idx > k)) = true then 0 else x % Tau.Polarity.nth_prime prime_idx
Instances For

---

### `Tau.BookII.Hartogs.laurent_expansion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L67-L75)
**def
Tau.BookII.Hartogs.laurent_expansion
(x k : Denotation.TauIdx)
 :List Denotation.TauIdx**


The full Laurent expansion at stage k: the tuple of all k residues.
Returns a list of length k: [x mod p_1, x mod p_2, ..., x mod p_k].
Equations
- Tau.BookII.Hartogs.laurent_expansion x k = Tau.BookII.Hartogs.laurent_expansion.go x k 1 k []
Instances For

---

### `Tau.BookII.Hartogs.laurent_expansion.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L72-L74)@[irreducible]

**def
Tau.BookII.Hartogs.laurent_expansion.go
(x k : Denotation.TauIdx)

(i remaining : ℕ)

(acc : List Denotation.TauIdx)
 :List Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.laurent_range_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L77-L92)
**def
Tau.BookII.Hartogs.laurent_range_check
(bound db : Denotation.TauIdx)
 :Bool**


Laurent expansion is well-defined: each coefficient is in the correct range.
For 1 <= i <= k: 0 <= laurent_coeff(x, k, i) < p_i.
Equations
- Tau.BookII.Hartogs.laurent_range_check bound db = Tau.BookII.Hartogs.laurent_range_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.laurent_range_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L82-L91)@[irreducible]

**def
Tau.BookII.Hartogs.laurent_range_check.go
(bound db : Denotation.TauIdx)

(x k i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.laurent_stability_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L94-L111)
**def
Tau.BookII.Hartogs.laurent_stability_check
(bound db : Denotation.TauIdx)
 :Bool**


Laurent expansion stability: reducing x to stage k does not change
the Laurent coefficients at primes <= k.
laurent_coeff(x, k, i) = laurent_coeff(reduce(x, k), k, i)
for 1 <= i <= k.
Equations
- Tau.BookII.Hartogs.laurent_stability_check bound db = Tau.BookII.Hartogs.laurent_stability_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.laurent_stability_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L101-L110)@[irreducible]

**def
Tau.BookII.Hartogs.laurent_stability_check.go
(bound db : Denotation.TauIdx)

(x k i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.tau_residue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L117-L125)
**def
Tau.BookII.Hartogs.tau_residue
(x i : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D43] The residue of x at prime index i:
tau_residue(x, i) = x mod p_i.

This is the stage-independent version: the residue at a prime
does not depend on which stage k we compute at (as long as k >= i),
because p_i divides M_k for k >= i.
Equations
- Tau.BookII.Hartogs.tau_residue x i = if (i == 0) = true then 0 else x % Tau.Polarity.nth_prime i
Instances For

---

### `Tau.BookII.Hartogs.residue_stage_independence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L127-L143)
**def
Tau.BookII.Hartogs.residue_stage_independence_check
(bound db : Denotation.TauIdx)
 :Bool**


Residue independence of stage: for k >= i,
tau_residue(x, i) = tau_residue(reduce(x, k), i).
The residue at p_i is the same whether we compute on x or x mod M_k.
Equations
- Tau.BookII.Hartogs.residue_stage_independence_check bound db = Tau.BookII.Hartogs.residue_stage_independence_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.residue_stage_independence_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L133-L142)@[irreducible]

**def
Tau.BookII.Hartogs.residue_stage_independence_check.go
(bound db : Denotation.TauIdx)

(x k i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.all_residues_agree`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L145-L153)
**def
Tau.BookII.Hartogs.all_residues_agree
(x y k : Denotation.TauIdx)
 :Bool**


Helper: check if all residues of x and y agree for primes 1..k.
Equations
- Tau.BookII.Hartogs.all_residues_agree x y k = Tau.BookII.Hartogs.all_residues_agree.go x y k 1 (k + 1)
Instances For

---

### `Tau.BookII.Hartogs.all_residues_agree.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L149-L152)@[irreducible]

**def
Tau.BookII.Hartogs.all_residues_agree.go
(x y k : Denotation.TauIdx)

(i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.residue_determines_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L155-L172)
**def
Tau.BookII.Hartogs.residue_determines_check
(bound db : Denotation.TauIdx)
 :Bool**


Residues determine the point: if tau_residue(x, i) = tau_residue(y, i)
for all 1 <= i <= k, then reduce(x, k) = reduce(y, k).
This is the CRT uniqueness theorem.
Equations
- Tau.BookII.Hartogs.residue_determines_check bound db = Tau.BookII.Hartogs.residue_determines_check.go bound db 2 2 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.residue_determines_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L161-L171)@[irreducible]

**def
Tau.BookII.Hartogs.residue_determines_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_reconstruct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L178-L198)
**def
Tau.BookII.Hartogs.crt_reconstruct
(residues : List Denotation.TauIdx)

(k : Denotation.TauIdx)
 :Denotation.TauIdx**


CRT reconstruction: given residues (r_1, ..., r_k), find x in [0, M_k)
such that x mod p_i = r_i for all i.

Implemented by brute-force search over [0, M_k). This is computable
for small k since M_k grows relatively slowly (M_4 = 210).
Equations
- Tau.BookII.Hartogs.crt_reconstruct residues k = Tau.BookII.Hartogs.crt_reconstruct.go 0 (Tau.Polarity.primorial k) residues k
Instances For

---

### `Tau.BookII.Hartogs.crt_reconstruct.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L187-L191)@[irreducible]

**def
Tau.BookII.Hartogs.crt_reconstruct.go
(x fuel : ℕ)

(residues : List Denotation.TauIdx)

(k : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_reconstruct.matches_all`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L193-L198)
**def
Tau.BookII.Hartogs.crt_reconstruct.matches_all
(x : ℕ)

(residues : List Denotation.TauIdx)

(i k : ℕ)
 :Bool**

Equations
- Tau.BookII.Hartogs.crt_reconstruct.matches_all x [] i k = true
- Tau.BookII.Hartogs.crt_reconstruct.matches_all x (r :: rs) i k = if i > k then true
 else x % Tau.Polarity.nth_prime i == r && Tau.BookII.Hartogs.crt_reconstruct.matches_all x rs (i + 1) k
Instances For

---

### `Tau.BookII.Hartogs.crt_roundtrip_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L200-L222)
**def
Tau.BookII.Hartogs.crt_roundtrip_check
(db : Denotation.TauIdx)
 :Bool**


CRT reconstruction round-trip check: for each x in [0, M_k),
reconstruct from Laurent coefficients and verify recovery.

Given x, compute (x%p_1, ..., x%p_k), then reconstruct y from these
residues, and verify y = x.
Equations
- Tau.BookII.Hartogs.crt_roundtrip_check db = Tau.BookII.Hartogs.crt_roundtrip_check.go_k db 1 (db + 1)
Instances For

---

### `Tau.BookII.Hartogs.crt_roundtrip_check.go_k`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L208-L213)@[irreducible]

**def
Tau.BookII.Hartogs.crt_roundtrip_check.go_k
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_roundtrip_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L215-L221)@[irreducible]

**def
Tau.BookII.Hartogs.crt_roundtrip_check.go_x
(x mk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.residue_reconstruction_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L228-L253)
**def
Tau.BookII.Hartogs.residue_reconstruction_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T30] Residue theorem: the CRT residues at stage k completely
determine the function value.

For each x in [2, bound] and stage k in [1, db]:


- Compute the Laurent expansion (all residues)

- Reconstruct via CRT

- Verify the reconstruction equals reduce(x, k)


This is the tau-analog of the classical residue theorem:
"the sum of all residues recovers the function value."
In our setting: "the tuple of all prime residues recovers the
stage-k projection via CRT."
Equations
- Tau.BookII.Hartogs.residue_reconstruction_check bound db = Tau.BookII.Hartogs.residue_reconstruction_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.residue_reconstruction_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L243-L252)@[irreducible]

**def
Tau.BookII.Hartogs.residue_reconstruction_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_residue_thm_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L255-L262)
**def
Tau.BookII.Hartogs.crt_residue_thm_check
(db : Denotation.TauIdx)
 :Bool**


[II.T30] Formal residue theorem for a specific stage:
CRT reconstruction from Laurent coefficients at stage k
is the identity on [0, M_k).

Verified computationally for stages 1-3 (M_1=2, M_2=6, M_3=30).
Equations
- Tau.BookII.Hartogs.crt_residue_thm_check db = (Tau.BookII.Hartogs.crt_roundtrip_check db && Tau.BookII.Hartogs.residue_reconstruction_check (Tau.Polarity.primorial db) db)
Instances For

---

### `Tau.BookII.Hartogs.MeromorphicFun`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L268-L282)
**structure
Tau.BookII.Hartogs.MeromorphicFun :Type**


[II.D44] A meromorphic function in the tau-setting:
a tower-coherent map that is well-defined (holomorphic) at all but
finitely many exceptional stages.

In the finite cyclic primorial world, every tower-coherent function
is automatically meromorphic (there are no essential singularities).
The "exceptional stages" are stages where the function has special
behavior (e.g., the output is 0, or the function is not injective).

We model this as a function f together with a list of exceptional stages.

- f : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx
The underlying function: (input, stage) -> output.

- poles : List Denotation.TauIdx
Exceptional stages (poles).

Instances For

---

### `Tau.BookII.Hartogs.mk_meromorphic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L284-L287)
**def
Tau.BookII.Hartogs.mk_meromorphic
(f : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(poles : List Denotation.TauIdx)
 :MeromorphicFun**


Construct a meromorphic function from a tower-coherent map.
Equations
- Tau.BookII.Hartogs.mk_meromorphic f poles = { f := f, poles := poles }
Instances For

---

### `Tau.BookII.Hartogs.mero_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L289-L291)
**def
Tau.BookII.Hartogs.mero_id :MeromorphicFun**


The identity is meromorphic with no poles.
Equations
- Tau.BookII.Hartogs.mero_id = Tau.BookII.Hartogs.mk_meromorphic Tau.BookII.Hartogs.hol_id []
Instances For

---

### `Tau.BookII.Hartogs.mero_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L293-L295)
**def
Tau.BookII.Hartogs.mero_sq :MeromorphicFun**


The squaring map is meromorphic with no poles.
Equations
- Tau.BookII.Hartogs.mero_sq = Tau.BookII.Hartogs.mk_meromorphic Tau.BookII.Hartogs.hol_sq []
Instances For

---

### `Tau.BookII.Hartogs.mero_partial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L297-L300)
**def
Tau.BookII.Hartogs.mero_partial
(n k : Denotation.TauIdx)
 :Denotation.TauIdx**


A "partial" endomorphism: holomorphic except at stage 1 where p_1=2
collapses everything to 0. This is meromorphic with pole at stage 1.
Equations
- Tau.BookII.Hartogs.mero_partial n k = if (k == 1) = true then 0 else Tau.Polarity.reduce (n * n + 1) k
Instances For

---

### `Tau.BookII.Hartogs.mero_partial_fun`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L302-L303)
**def
Tau.BookII.Hartogs.mero_partial_fun :MeromorphicFun**

Equations
- Tau.BookII.Hartogs.mero_partial_fun = Tau.BookII.Hartogs.mk_meromorphic Tau.BookII.Hartogs.mero_partial [1]
Instances For

---

### `Tau.BookII.Hartogs.meromorphic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L305-L320)
**def
Tau.BookII.Hartogs.meromorphic_check
(mf : MeromorphicFun)

(bound db : Denotation.TauIdx)
 :Bool**


Meromorphic check: the function is tower-coherent at all non-pole stages.
For stages k not in the pole list: reduce(f(x, l), k) = f(x, k) for k <= l.
Equations
- Tau.BookII.Hartogs.meromorphic_check mf bound db = Tau.BookII.Hartogs.meromorphic_check.go mf bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.meromorphic_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L310-L319)@[irreducible]

**def
Tau.BookII.Hartogs.meromorphic_check.go
(mf : MeromorphicFun)

(bound db : Denotation.TauIdx)

(x k l fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.hol_is_mero_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L322-L325)
**def
Tau.BookII.Hartogs.hol_is_mero_check
(bound db : Denotation.TauIdx)
 :Bool**


Every holomorphic endomorphism is meromorphic (with empty pole list).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.laurent_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L331-L340)
**def
Tau.BookII.Hartogs.laurent_sum
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


Sum of all Laurent coefficients at stage k.
This is a weak analog of "sum of residues": the arithmetic sum
of the CRT components.
Equations
- Tau.BookII.Hartogs.laurent_sum x k = Tau.BookII.Hartogs.laurent_sum.go x k 1 k 0
Instances For

---

### `Tau.BookII.Hartogs.laurent_sum.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L337-L339)@[irreducible]

**def
Tau.BookII.Hartogs.laurent_sum.go
(x k : Denotation.TauIdx)

(i remaining acc : ℕ)
 :Denotation.TauIdx**

Equations
- Tau.BookII.Hartogs.laurent_sum.go x k i remaining acc = if remaining = 0 then acc
 else Tau.BookII.Hartogs.laurent_sum.go x k (i + 1) (remaining - 1) (acc + Tau.BookII.Hartogs.laurent_coeff x k i)
Instances For

---

### `Tau.BookII.Hartogs.laurent_sum_bounded_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L342-L360)
**def
Tau.BookII.Hartogs.laurent_sum_bounded_check
(bound db : Denotation.TauIdx)
 :Bool**


The Laurent sum is bounded: sum of residues <= sum of (p_i - 1) for i=1..k.
Each coefficient < p_i, so the sum < p_1 + p_2 + ... + p_k.
Equations
- Tau.BookII.Hartogs.laurent_sum_bounded_check bound db = Tau.BookII.Hartogs.laurent_sum_bounded_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.laurent_sum_bounded_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L347-L355)@[irreducible]

**def
Tau.BookII.Hartogs.laurent_sum_bounded_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.laurent_sum_bounded_check.sum_primes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L357-L359)@[irreducible]

**def
Tau.BookII.Hartogs.laurent_sum_bounded_check.sum_primes
(i remaining acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.residue_evolution_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L366-L381)
**def
Tau.BookII.Hartogs.residue_evolution_check
(bound db : Denotation.TauIdx)
 :Bool**


Residues are compatible with the evolution operator:
tau_residue(evolution_op(x, n, m), i) = tau_residue(reduce(x, m), i)
for i <= m. The evolution operator preserves residue structure.
Equations
- Tau.BookII.Hartogs.residue_evolution_check bound db = Tau.BookII.Hartogs.residue_evolution_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.residue_evolution_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L372-L380)@[irreducible]

**def
Tau.BookII.Hartogs.residue_evolution_check.go
(bound db : Denotation.TauIdx)

(x m i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_laurent_residue_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L387-L402)
**def
Tau.BookII.Hartogs.full_laurent_residue_check
(bound db : Denotation.TauIdx)
 :Bool**


Complete Laurent-Residue verification:

- Laurent expansion well-defined and stable

- Residues determine points (CRT uniqueness)

- CRT reconstruction round-trip

- Residue theorem (reconstruction = original)

- Meromorphic structure

- Residue-evolution compatibility

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.laurent_range_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L469-L470)
**theorem
Tau.BookII.Hartogs.laurent_range_12_4 :laurent_range_check 12 4 = true**


---

### `Tau.BookII.Hartogs.laurent_stability_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L472-L473)
**theorem
Tau.BookII.Hartogs.laurent_stability_12_4 :laurent_stability_check 12 4 = true**


---

### `Tau.BookII.Hartogs.residue_stage_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L476-L477)
**theorem
Tau.BookII.Hartogs.residue_stage_10_3 :residue_stage_independence_check 10 3 = true**


---

### `Tau.BookII.Hartogs.residue_determines_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L479-L480)
**theorem
Tau.BookII.Hartogs.residue_determines_10_3 :residue_determines_check 10 3 = true**


---

### `Tau.BookII.Hartogs.crt_roundtrip_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L483-L484)
**theorem
Tau.BookII.Hartogs.crt_roundtrip_3 :crt_roundtrip_check 3 = true**


---

### `Tau.BookII.Hartogs.residue_recon_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L487-L488)
**theorem
Tau.BookII.Hartogs.residue_recon_12_3 :residue_reconstruction_check 12 3 = true**


---

### `Tau.BookII.Hartogs.crt_residue_thm_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L490-L491)
**theorem
Tau.BookII.Hartogs.crt_residue_thm_3 :crt_residue_thm_check 3 = true**


---

### `Tau.BookII.Hartogs.mero_id_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L494-L495)
**theorem
Tau.BookII.Hartogs.mero_id_12_4 :meromorphic_check mero_id 12 4 = true**


---

### `Tau.BookII.Hartogs.mero_sq_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L497-L498)
**theorem
Tau.BookII.Hartogs.mero_sq_12_4 :meromorphic_check mero_sq 12 4 = true**


---

### `Tau.BookII.Hartogs.laurent_sum_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L501-L502)
**theorem
Tau.BookII.Hartogs.laurent_sum_12_4 :laurent_sum_bounded_check 12 4 = true**


---

### `Tau.BookII.Hartogs.residue_evol_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L505-L506)
**theorem
Tau.BookII.Hartogs.residue_evol_10_3 :residue_evolution_check 10 3 = true**


---

### `Tau.BookII.Hartogs.full_laurent_residue_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/LaurentResidue.lean#L509-L510)
**theorem
Tau.BookII.Hartogs.full_laurent_residue_10_3 :full_laurent_residue_check 10 3 = true**
