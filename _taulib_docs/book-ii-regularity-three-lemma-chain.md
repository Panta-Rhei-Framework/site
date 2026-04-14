---
layout: taulib-doc
title: "TauLib.BookII.Regularity.ThreeLemmaChain"
permalink: /verify/taulib/docs/book-ii-regularity-three-lemma-chain/
lane: verify
module_name: "TauLib.BookII.Regularity.ThreeLemmaChain"
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

# TauLib.BookII.Regularity.ThreeLemmaChain


The three-lemma chain: Branch Factorization, Prime-Split Support,
and Polarity Symmetry — culminating in the Holomorphic iff
Idempotent-Supported characterization theorem.

## Registry Cross-References


- [II.L08] Branch Factorization — `branch_factorization_check`

- [II.L09] Prime-Split Support — `prime_split_support_check`

- [II.L10] Polarity Symmetry — `polarity_symmetry_check`

- [II.T33] Holomorphic iff Idempotent-Supported — `hol_iff_is_check`


## Mathematical Content


**L08 (Branch Factorization):** Every omega-germ transformer G factors
as G = G₊ + G₋ via the idempotent decomposition. The factorization
is verified on the evolution operator output: applying the idempotent
decomposition to evolution_op(x, n, m) yields two independent branches.

**L09 (Prime-Split Support):** The B-channel component G₊ has support
on B-channel primes and the C-channel component G₋ has support on
C-channel primes. The support pattern is determined by the ABCD chart:


- B-coordinate (exponent/gamma-orbit) is the B-channel signal

- C-coordinate (tetration height/eta-orbit) is the C-channel signal


**L10 (Polarity Symmetry):** The j-involution sigma_j swaps channels:
sigma_j(e₊) = e₋ and sigma_j(e₋) = e₊. In SplitComplex: multiplication
by j swaps re and im, which transposes the sector decomposition.
In sector coordinates: sigma_j(B, C) = (C, B).

**T33 (Holomorphic iff Idempotent-Supported):** A stagewise function f
is holomorphic if and only if it satisfies four conditions:


- IS1: bipolar decomposition exists (decompose recovery)

- IS2: stagewise naturality (tower coherence of components)

- IS3: channel support (B on B-sector, C on C-sector)

- IS4: polarity symmetry (j-swap gives valid decomposition)


---

### `Tau.BookII.Regularity.branch_factorization_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L52-L79)
**def
Tau.BookII.Regularity.branch_factorization_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L08] Branch factorization of the evolution operator output.
For each point x and stages n, m: the evolution_op output decomposes
via the idempotent decomposition into independent B and C branches.

Specifically: the SectorPair formed from the ABCD chart of the
evolved point decomposes as e₊ · sp + e₋ · sp = sp.
Equations
- Tau.BookII.Regularity.branch_factorization_check bound db = Tau.BookII.Regularity.branch_factorization_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.branch_factorization_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L61-L78)@[irreducible]

**def
Tau.BookII.Regularity.branch_factorization_check.go
(bound db : Denotation.TauIdx)

(x n m fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.branch_factorization_bndlift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L81-L98)
**def
Tau.BookII.Regularity.branch_factorization_bndlift
(bound db : Denotation.TauIdx)
 :Bool**


Branch factorization applied to BndLift output: the lifted value
also factors into independent B and C branches.
Equations
- Tau.BookII.Regularity.branch_factorization_bndlift bound db = Tau.BookII.Regularity.branch_factorization_bndlift.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.branch_factorization_bndlift.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L86-L97)@[irreducible]

**def
Tau.BookII.Regularity.branch_factorization_bndlift.go
(bound db : Denotation.TauIdx)

(x stage fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.prime_split_support_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L104-L136)
**def
Tau.BookII.Regularity.prime_split_support_check
(bound : Denotation.TauIdx)
 :Bool**


[II.L09] Prime-split support check.

The B-channel component has its signal concentrated in the B-sector
(the b_sector field of the SectorPair), and the C-channel component
has its signal in the C-sector.

Specifically, for each tau-admissible point:


- G₊ = (B, 0): B-sector carries the exponent data, C-sector is zero

- G₋ = (0, C): B-sector is zero, C-sector carries the tetration data


This is the prime-split support property: the two channels have
disjoint support in the spectral decomposition.
Equations
- Tau.BookII.Regularity.prime_split_support_check bound = Tau.BookII.Regularity.prime_split_support_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.prime_split_support_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L119-L135)@[irreducible]

**def
Tau.BookII.Regularity.prime_split_support_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.prime_split_stagewise`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L138-L156)
**def
Tau.BookII.Regularity.prime_split_stagewise
(bound db : Denotation.TauIdx)
 :Bool**


[II.L09] Stage-level prime-split: at each primorial stage k,
the B-channel and C-channel of the reduced value maintain
disjoint support after reduction.
Equations
- Tau.BookII.Regularity.prime_split_stagewise bound db = Tau.BookII.Regularity.prime_split_stagewise.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.prime_split_stagewise.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L144-L155)@[irreducible]

**def
Tau.BookII.Regularity.prime_split_stagewise.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.j_swap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L162-L166)
**def
Tau.BookII.Regularity.j_swap
(sp : Polarity.SectorPair)
 :Polarity.SectorPair**


The j-involution on SectorPairs: swaps B and C sectors.
In SplitComplex terms, multiplication by j swaps re <-> im,
which in sector coordinates becomes (B, C) -> (C, B).
Equations
- Tau.BookII.Regularity.j_swap sp = { b_sector := sp.c_sector, c_sector := sp.b_sector }
Instances For

---

### `Tau.BookII.Regularity.polarity_symmetry_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L168-L199)
**def
Tau.BookII.Regularity.polarity_symmetry_check
(bound : Denotation.TauIdx)
 :Bool**


[II.L10] Polarity symmetry check:
the j-involution swaps the two channels.

sigma_j(e₊ · bp) = e₋ · sigma_j(bp)
sigma_j(e₋ · bp) = e₊ · sigma_j(bp)

In sector coordinates: j-swapping (B, 0) gives (0, B),
and j-swapping (0, C) gives (C, 0).
Equations
- Tau.BookII.Regularity.polarity_symmetry_check bound = Tau.BookII.Regularity.polarity_symmetry_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.polarity_symmetry_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L179-L198)@[irreducible]

**def
Tau.BookII.Regularity.polarity_symmetry_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.j_swap_involution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L201-L204)
**theorem
Tau.BookII.Regularity.j_swap_involution
(sp : Polarity.SectorPair)
 :j_swap (j_swap sp) = sp**


j-swap is an involution: j_swap(j_swap(sp)) = sp.

---

### `Tau.BookII.Regularity.j_swap_proj_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L206-L209)
**theorem
Tau.BookII.Regularity.j_swap_proj_plus
(bp : Polarity.SectorPair)
 :j_swap (proj_plus bp) = proj_minus (j_swap bp)**


j-swap swaps the idempotent projections (formal).

---

### `Tau.BookII.Regularity.j_swap_proj_minus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L211-L213)
**theorem
Tau.BookII.Regularity.j_swap_proj_minus
(bp : Polarity.SectorPair)
 :j_swap (proj_minus bp) = proj_plus (j_swap bp)**


---

### `Tau.BookII.Regularity.j_swap_recovery`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L215-L219)
**theorem
Tau.BookII.Regularity.j_swap_recovery
(bp : Polarity.SectorPair)
 :(j_swap (proj_plus bp)).add (j_swap (proj_minus bp)) = j_swap bp**


j-swap preserves decomposition recovery.

---

### `Tau.BookII.Regularity.sc_j_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L225-L228)
**def
Tau.BookII.Regularity.sc_j_mul
(z : Polarity.SplitComplex)
 :Polarity.SplitComplex**


SplitComplex j-multiplication: z -> j * z swaps re and im.
This is the algebraic basis for the polarity symmetry.
Equations
- Tau.BookII.Regularity.sc_j_mul z = Tau.Polarity.SplitComplex.j.mul z
Instances For

---

### `Tau.BookII.Regularity.sc_j_swaps`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L230-L233)
**theorem
Tau.BookII.Regularity.sc_j_swaps
(z : Polarity.SplitComplex)
 :(sc_j_mul z).re = z.im ∧ (sc_j_mul z).im = z.re**


j-multiplication swaps re and im (formal).

---

### `Tau.BookII.Regularity.j_swaps_idempotents_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L235-L240)
**def
Tau.BookII.Regularity.j_swaps_idempotents_check :Bool**


Computational check: j * e₊ = e₋ in sector coordinates.
In SC: j * ((1+j)/2) maps to the complementary idempotent.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.is1_decomposition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L246-L261)
**def
Tau.BookII.Regularity.is1_decomposition_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T33, IS1] Bipolar decomposition exists: the function
admits an idempotent decomposition with recovery property.
Equations
- Tau.BookII.Regularity.is1_decomposition_check bound db = Tau.BookII.Regularity.is1_decomposition_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.is1_decomposition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L251-L260)@[irreducible]

**def
Tau.BookII.Regularity.is1_decomposition_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.is2_naturality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L263-L287)
**def
Tau.BookII.Regularity.is2_naturality_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T33, IS2] Stagewise naturality: tower coherence of B and C
components individually. Reducing the B-channel at a finer stage
to a coarser stage gives the B-channel at the coarser stage.
Equations
- Tau.BookII.Regularity.is2_naturality_check bound db = Tau.BookII.Regularity.is2_naturality_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.is2_naturality_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L269-L286)@[irreducible]

**def
Tau.BookII.Regularity.is2_naturality_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.is3_channel_support_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L289-L291)
**def
Tau.BookII.Regularity.is3_channel_support_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T33, IS3] Channel support: B on B-sector, C on C-sector.
Equations
- Tau.BookII.Regularity.is3_channel_support_check bound = Tau.BookII.Regularity.prime_split_support_check bound
Instances For

---

### `Tau.BookII.Regularity.is4_polarity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L293-L295)
**def
Tau.BookII.Regularity.is4_polarity_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T33, IS4] Polarity symmetry.
Equations
- Tau.BookII.Regularity.is4_polarity_check bound = Tau.BookII.Regularity.polarity_symmetry_check bound
Instances For

---

### `Tau.BookII.Regularity.hol_iff_is_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L297-L303)
**def
Tau.BookII.Regularity.hol_iff_is_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T33] Holomorphic iff Idempotent-Supported: the full characterization.
A stagewise function is holomorphic iff it satisfies IS1-IS4.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.full_three_lemma_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L309-L317)
**def
Tau.BookII.Regularity.full_three_lemma_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L08 + II.L09 + II.L10 + II.T33] Complete three-lemma verification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.branch_fact_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L358-L359)
**theorem
Tau.BookII.Regularity.branch_fact_12_3 :branch_factorization_check 12 3 = true**


---

### `Tau.BookII.Regularity.branch_bndlift_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L361-L362)
**theorem
Tau.BookII.Regularity.branch_bndlift_12_3 :branch_factorization_bndlift 12 3 = true**


---

### `Tau.BookII.Regularity.prime_split_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L365-L366)
**theorem
Tau.BookII.Regularity.prime_split_30 :prime_split_support_check 30 = true**


---

### `Tau.BookII.Regularity.prime_split_stage_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L368-L369)
**theorem
Tau.BookII.Regularity.prime_split_stage_12_3 :prime_split_stagewise 12 3 = true**


---

### `Tau.BookII.Regularity.polarity_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L372-L373)
**theorem
Tau.BookII.Regularity.polarity_30 :polarity_symmetry_check 30 = true**


---

### `Tau.BookII.Regularity.j_idem_swap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L375-L376)
**theorem
Tau.BookII.Regularity.j_idem_swap :j_swaps_idempotents_check = true**


---

### `Tau.BookII.Regularity.is1_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L379-L380)
**theorem
Tau.BookII.Regularity.is1_12_3 :is1_decomposition_check 12 3 = true**


---

### `Tau.BookII.Regularity.is2_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L382-L383)
**theorem
Tau.BookII.Regularity.is2_12_3 :is2_naturality_check 12 3 = true**


---

### `Tau.BookII.Regularity.is3_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L385-L386)
**theorem
Tau.BookII.Regularity.is3_30 :is3_channel_support_check 30 = true**


---

### `Tau.BookII.Regularity.is4_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L388-L389)
**theorem
Tau.BookII.Regularity.is4_30 :is4_polarity_check 30 = true**


---

### `Tau.BookII.Regularity.hol_iff_is_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L392-L393)
**theorem
Tau.BookII.Regularity.hol_iff_is_12_3 :hol_iff_is_check 12 3 = true**


---

### `Tau.BookII.Regularity.full_three_lemma_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L396-L397)
**theorem
Tau.BookII.Regularity.full_three_lemma_12_3 :full_three_lemma_check 12 3 = true**
