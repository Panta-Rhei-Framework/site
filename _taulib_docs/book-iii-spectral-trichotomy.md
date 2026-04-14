---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.Trichotomy"
permalink: /verify/taulib/docs/book-iii-spectral-trichotomy/
lane: verify
module_name: "TauLib.BookIII.Spectral.Trichotomy"
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

# TauLib.BookIII.Spectral.Trichotomy


Spectral Trichotomy Lemma, Boundary Normal Form, and B/C Non-Collapse Theorem.

## Registry Cross-References


- [III.T14] Spectral Trichotomy Lemma -- `trichotomy_check`

- [III.D24] Boundary Normal Form -- `boundary_normal_form`, `bnf_check`

- [III.T15] B/C Non-Collapse Theorem -- `bc_non_collapse_check`


## Mathematical Content


**III.T14 (Spectral Trichotomy):** Every boundary character at level n
decomposes uniquely into B-supported, C-supported, and X-mixing
components. The decomposition is exact, orthogonal, and functorial.

**III.D24 (Boundary Normal Form):** Every element of ℤ/Prim(k)ℤ[j] has
unique normal form a·e₊ + b·e₋ where a is B-supported and b is C-supported.

**III.T15 (B/C Non-Collapse):** B-sector and C-sector are genuinely distinct:
no tower-compatible isomorphism between B-supported and C-supported
subrings exists. Growth-rate asymmetry creates inescapable coherence obstruction.

---

### `Tau.BookIII.Spectral.trichotomy_decompose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L38-L55)
**def
Tau.BookIII.Spectral.trichotomy_decompose
(residues : List Denotation.TauIdx)

(k : Denotation.TauIdx)
 :List Denotation.TauIdx × List Denotation.TauIdx × List Denotation.TauIdx**


[III.T14] Decompose a CRT residue tuple into B-supported,
C-supported, and X-supported components.
Uses label_direct to classify each prime.
Equations
- Tau.BookIII.Spectral.trichotomy_decompose residues k = Tau.BookIII.Spectral.trichotomy_decompose.go residues 0 k [] [] []
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_decompose.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L45-L55)@[irreducible]

**def
Tau.BookIII.Spectral.trichotomy_decompose.go
(res : List Denotation.TauIdx)

(i k : ℕ)

(b_acc c_acc x_acc : List Denotation.TauIdx)
 :List Denotation.TauIdx × List Denotation.TauIdx × List Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L57-L90)
**def
Tau.BookIII.Spectral.trichotomy_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T14] Spectral trichotomy check: verify that the B+C+X decomposition
is exact (sums back to original) and orthogonal (cross-terms zero).
Equations
- Tau.BookIII.Spectral.trichotomy_check bound db = Tau.BookIII.Spectral.trichotomy_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L62-L73)@[irreducible]

**def
Tau.BookIII.Spectral.trichotomy_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_check.check_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L75-L83)@[irreducible]

**def
Tau.BookIII.Spectral.trichotomy_check.check_exact
(orig b_part c_part x_part : List Denotation.TauIdx)

(i k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_check.check_ortho`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L84-L90)@[irreducible]

**def
Tau.BookIII.Spectral.trichotomy_check.check_ortho
(b_part c_part : List Denotation.TauIdx)

(i k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_functorial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L92-L115)
**def
Tau.BookIII.Spectral.trichotomy_functorial_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T14] Trichotomy functoriality: the decomposition commutes
with level change (reduction from k+1 to k).
Equations
- Tau.BookIII.Spectral.trichotomy_functorial_check bound db = Tau.BookIII.Spectral.trichotomy_functorial_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_functorial_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L97-L110)@[irreducible]

**def
Tau.BookIII.Spectral.trichotomy_functorial_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_functorial_check.check_prefix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L112-L115)@[irreducible]

**def
Tau.BookIII.Spectral.trichotomy_functorial_check.check_prefix
(high low : List Denotation.TauIdx)

(i k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.BoundaryNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L121-L129)
**structure
Tau.BookIII.Spectral.BoundaryNF :Type**


[III.D24] Boundary normal form: decompose x into (a, b) where
a is B-supported and b is C-supported. The X-component goes to
whichever has a larger contribution (tie → B).

- b_part : Denotation.TauIdx
- c_part : Denotation.TauIdx
- x_part : Denotation.TauIdx
- depth : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Spectral.instReprBoundaryNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L129-L129)
**instance
Tau.BookIII.Spectral.instReprBoundaryNF :Repr BoundaryNF**

Equations
- Tau.BookIII.Spectral.instReprBoundaryNF = { reprPrec := Tau.BookIII.Spectral.instReprBoundaryNF.repr }

---

### `Tau.BookIII.Spectral.instReprBoundaryNF.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L129-L129)
**def
Tau.BookIII.Spectral.instReprBoundaryNF.repr :BoundaryNF → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instDecidableEqBoundaryNF.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L129-L129)
**def
Tau.BookIII.Spectral.instDecidableEqBoundaryNF.decEq
(x✝ x✝¹ : BoundaryNF)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instDecidableEqBoundaryNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L129-L129)
**instance
Tau.BookIII.Spectral.instDecidableEqBoundaryNF :DecidableEq BoundaryNF**

Equations
- Tau.BookIII.Spectral.instDecidableEqBoundaryNF = Tau.BookIII.Spectral.instDecidableEqBoundaryNF.decEq

---

### `Tau.BookIII.Spectral.instBEqBoundaryNF.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L129-L129)
**def
Tau.BookIII.Spectral.instBEqBoundaryNF.beq :BoundaryNF → BoundaryNF → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Spectral.instBEqBoundaryNF.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Spectral.instBEqBoundaryNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L129-L129)
**instance
Tau.BookIII.Spectral.instBEqBoundaryNF :BEq BoundaryNF**

Equations
- Tau.BookIII.Spectral.instBEqBoundaryNF = { beq := Tau.BookIII.Spectral.instBEqBoundaryNF.beq }

---

### `Tau.BookIII.Spectral.boundary_normal_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L131-L138)
**def
Tau.BookIII.Spectral.boundary_normal_form
(x k : Denotation.TauIdx)
 :BoundaryNF**


[III.D24] Compute boundary normal form from a value at depth k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.bnf_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L140-L158)
**def
Tau.BookIII.Spectral.bnf_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D24] BNF check: verify that the normal form decomposes correctly.
b_part + c_part + x_part ≡ x mod Prim(k).
Equations
- Tau.BookIII.Spectral.bnf_check bound db = Tau.BookIII.Spectral.bnf_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.bnf_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L145-L157)@[irreducible]

**def
Tau.BookIII.Spectral.bnf_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.bnf_uniqueness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L160-L183)
**def
Tau.BookIII.Spectral.bnf_uniqueness_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D24] BNF uniqueness: the decomposition is unique.
Equations
- Tau.BookIII.Spectral.bnf_uniqueness_check bound db = Tau.BookIII.Spectral.bnf_uniqueness_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.bnf_uniqueness_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L164-L182)@[irreducible]

**def
Tau.BookIII.Spectral.bnf_uniqueness_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.compute_label_product`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L189-L201)
**def
Tau.BookIII.Spectral.compute_label_product
(label : PrimeLabel)

(k : Denotation.TauIdx)
 :Denotation.TauIdx**


Helper: compute product of primes with given label up to depth k.
Equations
- Tau.BookIII.Spectral.compute_label_product label k = Tau.BookIII.Spectral.compute_label_product.go label k 1 1 (k + 1)
Instances For

---

### `Tau.BookIII.Spectral.compute_label_product.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L193-L200)@[irreducible]

**def
Tau.BookIII.Spectral.compute_label_product.go
(label : PrimeLabel)

(k : Denotation.TauIdx)

(i acc fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.bc_non_collapse_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L203-L223)
**def
Tau.BookIII.Spectral.bc_non_collapse_check
(_bound db : Denotation.TauIdx)
 :Bool**


[III.T15] B/C non-collapse: verify that B-supported and C-supported
subrings are genuinely distinct. No isomorphism preserving
the tower structure exists between them.
Criterion: B-type primes and C-type primes have different growth
behavior (B = exponent-type, C = tetration-type).
Equations
- Tau.BookIII.Spectral.bc_non_collapse_check _bound db = Tau.BookIII.Spectral.bc_non_collapse_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.bc_non_collapse_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L211-L222)@[irreducible]

**def
Tau.BookIII.Spectral.bc_non_collapse_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.bc_coprime_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L225-L240)
**def
Tau.BookIII.Spectral.bc_coprime_check
(db : Denotation.TauIdx)
 :Bool**


[III.T15] B/C asymmetry: the B-product and C-product at depth k
are coprime (no shared prime factors).
Equations
- Tau.BookIII.Spectral.bc_coprime_check db = Tau.BookIII.Spectral.bc_coprime_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.bc_coprime_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L230-L239)@[irreducible]

**def
Tau.BookIII.Spectral.bc_coprime_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.trichotomy_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L271-L272)
**theorem
Tau.BookIII.Spectral.trichotomy_15_4 :trichotomy_check 15 4 = true**


---

### `Tau.BookIII.Spectral.trichotomy_func_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L275-L276)
**theorem
Tau.BookIII.Spectral.trichotomy_func_15_3 :trichotomy_functorial_check 15 3 = true**


---

### `Tau.BookIII.Spectral.bnf_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L279-L280)
**theorem
Tau.BookIII.Spectral.bnf_15_4 :bnf_check 15 4 = true**


---

### `Tau.BookIII.Spectral.bnf_unique_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L283-L284)
**theorem
Tau.BookIII.Spectral.bnf_unique_10_3 :bnf_uniqueness_check 10 3 = true**


---

### `Tau.BookIII.Spectral.bc_non_collapse_10_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L287-L288)
**theorem
Tau.BookIII.Spectral.bc_non_collapse_10_5 :bc_non_collapse_check 10 5 = true**


---

### `Tau.BookIII.Spectral.bc_coprime_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L291-L292)
**theorem
Tau.BookIII.Spectral.bc_coprime_5 :bc_coprime_check 5 = true**


---

### `Tau.BookIII.Spectral.trichotomy_depth_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L298-L301)
**theorem
Tau.BookIII.Spectral.trichotomy_depth_1 :(trichotomy_decompose [1] 1).1 = [0]**


[III.T14] Structural: trichotomy at depth 1 has only X-component
(only prime is 2, which is X-type).

---

### `Tau.BookIII.Spectral.bnf_zero_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L303-L307)
**theorem
Tau.BookIII.Spectral.bnf_zero_3 :(boundary_normal_form 0 3).b_part = 0 ∧ (boundary_normal_form 0 3).c_part = 0 ∧ (boundary_normal_form 0 3).x_part = 0**


[III.D24] Structural: BNF of 0 is all zeros.

---

### `Tau.BookIII.Spectral.bc_coprime_at_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L309-L313)
**theorem
Tau.BookIII.Spectral.bc_coprime_at_3 :Nat.gcd (compute_label_product PrimeLabel.B 3) (compute_label_product PrimeLabel.C 3) = 1**


[III.T15] Structural: B-product and C-product at depth 3 are
coprime (they share no prime factors).

---

### `Tau.BookIII.Spectral.bc_distinct_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/Trichotomy.lean#L315-L317)
**theorem
Tau.BookIII.Spectral.bc_distinct_3 :compute_label_product PrimeLabel.B 3 ≠ compute_label_product PrimeLabel.C 3**


[III.T15] Structural: B-product ≠ C-product at depth 3.
