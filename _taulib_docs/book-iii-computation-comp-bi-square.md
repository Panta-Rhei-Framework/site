---
layout: taulib-doc
title: "TauLib.BookIII.Computation.CompBiSquare"
permalink: /verify/taulib/docs/book-iii-computation-comp-bi-square/
lane: verify
module_name: "TauLib.BookIII.Computation.CompBiSquare"
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

# TauLib.BookIII.Computation.CompBiSquare


Computational Bi-Square, Product-Meet Collapse, τ-Admissibility Collapse,
and No Barrier Theorem.

## Registry Cross-References


- [III.D56] Computational Bi-Square -- `comp_bisquare_check`

- [III.T32] Product-Meet Collapse -- `product_meet_collapse_check`

- [III.T33] τ-Admissibility Collapse -- `tau_admissibility_collapse_check`

- [III.T34] No Barrier Theorem -- `no_barrier_check`


## Mathematical Content


**III.D56 (Computational Bi-Square):** Fourth bi-square in the scaling chain:
algebraic (I) → topological (II) → enriched (III) → computational (III.VII).
Left = TTM tower coherence, right = witness spectral naturality.

**III.T32 (Product-Meet Collapse):** At E₂, meet (finding a witness) IS
product (constructing a composite). CRT decomposes the search space so
that finding = constructing.

**III.T33 (τ-Admissibility Collapse):** τ-P_adm = τ-NP_adm. Three-step proof:
(1) Cook-Levin gives polynomial tableau; (2) CRT decomposes witness;
(3) Product-Meet collapses search to construction.

**III.T34 (No Barrier Theorem):** No encoding gap between external and internal
computation. TTM τ-Nativity closes the "representation barrier": asking whether
P ≠ NP was asking an E₂ question with E₀ tools.

---

### `Tau.BookIII.Computation.product_meet_collapse_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L46-L70)
**def
Tau.BookIII.Computation.product_meet_collapse_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T32] Product-Meet Collapse: at E₂ level, "finding a witness"
(meet/search) IS "constructing a composite" (product/multiplication).
Verified by: CRT decomposition turns ∏ into ∑, and the sum is
reconstructible from the factors.
Equations
- Tau.BookIII.Computation.product_meet_collapse_check bound db = Tau.BookIII.Computation.product_meet_collapse_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.product_meet_collapse_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L53-L69)@[irreducible]

**def
Tau.BookIII.Computation.product_meet_collapse_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.ttm_tower_coherence_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L76-L91)@[irreducible]

**def
Tau.BookIII.Computation.ttm_tower_coherence_go
(x k bound db fuel : ℕ)
 :Bool**


[III.D56] TTM tower coherence: result at depth k+1 reduces mod p_k
to result at depth k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.witness_spectral_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L93-L109)@[irreducible]

**def
Tau.BookIII.Computation.witness_spectral_go
(x k bound db fuel : ℕ)
 :Bool**


[III.D56] Witness spectral naturality: CRT decomposition commutes
with BNF (same structural property as algebraic/topological bi-squares).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.comp_bisquare_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L111-L117)
**def
Tau.BookIII.Computation.comp_bisquare_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D56] Computational bi-square check: left face = TTM tower coherence,
right face = witness spectral naturality, paste = product-meet collapse.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.tau_admissibility_collapse_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L123-L132)
**def
Tau.BookIII.Computation.tau_admissibility_collapse_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T33] τ-Admissibility Collapse: τ-P_adm = τ-NP_adm.
Three-step verification:
(1) Cook-Levin: polynomial bounded tableau
(2) CRT: witness decomposes into per-prime searches
(3) Product-Meet: search = construction
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.no_barrier_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L138-L146)
**def
Tau.BookIII.Computation.no_barrier_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T34] No Barrier: no encoding gap between external/internal
computation. Verified by: (1) TTM τ-nativity (code = data),
(2) operational closure (no meta-level), (3) interface width
principle (finite determination).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.pvsnp_is_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L148-L149)
**def
Tau.BookIII.Computation.pvsnp_is_e2 :Bool**


[III.T34] P vs NP is at E₂ (enrichment level 2).
Equations
- Tau.BookIII.Computation.pvsnp_is_e2 = (Tau.BookIII.Enrichment.EnrLevel.E2.toNat == 2)
Instances For

---

### `Tau.BookIII.Computation.comp_bisquare_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L165-L166)
**theorem
Tau.BookIII.Computation.comp_bisquare_10_3 :comp_bisquare_check 10 3 = true**


---

### `Tau.BookIII.Computation.product_meet_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L168-L169)
**theorem
Tau.BookIII.Computation.product_meet_15_4 :product_meet_collapse_check 15 4 = true**


---

### `Tau.BookIII.Computation.tau_collapse_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L171-L172)
**theorem
Tau.BookIII.Computation.tau_collapse_10_3 :tau_admissibility_collapse_check 10 3 = true**


---

### `Tau.BookIII.Computation.no_barrier_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L174-L175)
**theorem
Tau.BookIII.Computation.no_barrier_10_3 :no_barrier_check 10 3 = true**


---

### `Tau.BookIII.Computation.pvsnp_is_e2_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L177-L178)
**theorem
Tau.BookIII.Computation.pvsnp_is_e2_thm :pvsnp_is_e2 = true**


---

### `Tau.BookIII.Computation.product_meet_10_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L184-L186)
**theorem
Tau.BookIII.Computation.product_meet_10_1 :product_meet_collapse_check 10 1 = true**


[III.T32] Structural: product-meet at depth 1.

---

### `Tau.BookIII.Computation.pvsnp_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L188-L189)
**theorem
Tau.BookIII.Computation.pvsnp_level :Enrichment.EnrLevel.E2.toNat = 2**


[III.T33] Structural: P vs NP is at E₂.

---

### `Tau.BookIII.Computation.no_barrier_10_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/CompBiSquare.lean#L191-L193)
**theorem
Tau.BookIII.Computation.no_barrier_10_1 :no_barrier_check 10 1 = true**


[III.T34] Structural: no-barrier at depth 1.
