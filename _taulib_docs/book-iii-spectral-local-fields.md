---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.LocalFields"
permalink: /verify/taulib/docs/book-iii-spectral-local-fields/
lane: verify
module_name: "TauLib.BookIII.Spectral.LocalFields"
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

# TauLib.BookIII.Spectral.LocalFields


τ-Native Local Fields and Completeness Without Topology.

## Registry Cross-References


- [III.D21] τ-Native Local Field -- `LocalField`, `local_field_check`

- [III.P06] Completeness Without Topology -- `completeness_check`


## Mathematical Content


**III.D21 (τ-Native Local Field):** ℤ_p^τ = lim← ℤ/p^n ℤ as inverse
limit within τ. The p-adic integers are a τ-object with NF address.
p-adic valuation v_p = D-coordinate restricted to p-primary component.

**III.P06 (Completeness Without Topology):** ℤ_p^τ is complete in the τ
sense: every tower-coherent sequence has unique limit. This is Global
Hartogs restricted to the p-primary tower. No metric, no Cauchy sequences.

---

### `Tau.BookIII.Spectral.LocalFieldElt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L34-L40)
**structure
Tau.BookIII.Spectral.LocalFieldElt :Type**


[III.D21] A τ-native local field element at finite depth.
Represents an element of ℤ_p^τ = lim← ℤ/p^nℤ at depth d.

- prime : Denotation.TauIdx
- depth : Denotation.TauIdx
- value : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Spectral.instReprLocalFieldElt.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L40-L40)
**def
Tau.BookIII.Spectral.instReprLocalFieldElt.repr :LocalFieldElt → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instReprLocalFieldElt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L40-L40)
**instance
Tau.BookIII.Spectral.instReprLocalFieldElt :Repr LocalFieldElt**

Equations
- Tau.BookIII.Spectral.instReprLocalFieldElt = { reprPrec := Tau.BookIII.Spectral.instReprLocalFieldElt.repr }

---

### `Tau.BookIII.Spectral.instDecidableEqLocalFieldElt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L40-L40)
**instance
Tau.BookIII.Spectral.instDecidableEqLocalFieldElt :DecidableEq LocalFieldElt**

Equations
- Tau.BookIII.Spectral.instDecidableEqLocalFieldElt = Tau.BookIII.Spectral.instDecidableEqLocalFieldElt.decEq

---

### `Tau.BookIII.Spectral.instDecidableEqLocalFieldElt.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L40-L40)
**def
Tau.BookIII.Spectral.instDecidableEqLocalFieldElt.decEq
(x✝ x✝¹ : LocalFieldElt)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instBEqLocalFieldElt.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L40-L40)
**def
Tau.BookIII.Spectral.instBEqLocalFieldElt.beq :LocalFieldElt → LocalFieldElt → Bool**

Equations
- Tau.BookIII.Spectral.instBEqLocalFieldElt.beq { prime := a, depth := a_1, value := a_2 }
 { prime := b, depth := b_1, value := b_2 } = (a == b && (a_1 == b_1 && a_2 == b_2))
- Tau.BookIII.Spectral.instBEqLocalFieldElt.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Spectral.instBEqLocalFieldElt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L40-L40)
**instance
Tau.BookIII.Spectral.instBEqLocalFieldElt :BEq LocalFieldElt**

Equations
- Tau.BookIII.Spectral.instBEqLocalFieldElt = { beq := Tau.BookIII.Spectral.instBEqLocalFieldElt.beq }

---

### `Tau.BookIII.Spectral.to_local`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L42-L45)
**def
Tau.BookIII.Spectral.to_local
(x p d : Denotation.TauIdx)
 :LocalFieldElt**


[III.D21] Build a local field element from a global τ-value.
Equations
- Tau.BookIII.Spectral.to_local x p d = { prime := p, depth := d, value := if p ^ d > 0 then x % p ^ d else 0 }
Instances For

---

### `Tau.BookIII.Spectral.padic_val`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L47-L57)
**def
Tau.BookIII.Spectral.padic_val
(x p : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D21] p-adic valuation: largest k such that p^k | x.
Returns 0 if x = 0 or p < 2.
Equations
- Tau.BookIII.Spectral.padic_val x p = if (x == 0 || decide (p < 2)) = true then 0 else Tau.BookIII.Spectral.padic_val.go x p 0 x
Instances For

---

### `Tau.BookIII.Spectral.padic_val.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L53-L56)@[irreducible]

**def
Tau.BookIII.Spectral.padic_val.go
(x p acc fuel : ℕ)
 :Denotation.TauIdx**

Equations
- Tau.BookIII.Spectral.padic_val.go x p acc fuel = if fuel = 0 then acc
 else if (x % p != 0) = true then acc else Tau.BookIII.Spectral.padic_val.go (x / p) p (acc + 1) (fuel - 1)
Instances For

---

### `Tau.BookIII.Spectral.local_field_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L59-L80)
**def
Tau.BookIII.Spectral.local_field_check
(bound depth : Denotation.TauIdx)
 :Bool**


[III.D21] Local field check: verify inverse system property.
For each p and depth d: reduce from p^(d+1) to p^d is coherent.
Equations
- Tau.BookIII.Spectral.local_field_check bound depth = Tau.BookIII.Spectral.local_field_check.go bound depth 0 1 1 ((bound + 1) * (depth + 1) * 5)
Instances For

---

### `Tau.BookIII.Spectral.local_field_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L64-L79)@[irreducible]

**def
Tau.BookIII.Spectral.local_field_check.go
(bound depth : Denotation.TauIdx)

(x p_idx d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.local_ring_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L82-L105)
**def
Tau.BookIII.Spectral.local_ring_check
(bound depth : Denotation.TauIdx)
 :Bool**


[III.D21] Local field ring operations: addition and multiplication
are well-defined on ℤ/p^dℤ.
Equations
- Tau.BookIII.Spectral.local_ring_check bound depth = Tau.BookIII.Spectral.local_ring_check.go bound depth 0 0 1 ((bound + 1) * (bound + 1) * (depth + 1))
Instances For

---

### `Tau.BookIII.Spectral.local_ring_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L87-L104)@[irreducible]

**def
Tau.BookIII.Spectral.local_ring_check.go
(bound depth : Denotation.TauIdx)

(x y d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.completeness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L111-L139)
**def
Tau.BookIII.Spectral.completeness_check
(bound depth : Denotation.TauIdx)
 :Bool**


[III.P06] Completeness check: every tower-coherent sequence has
unique limit. A sequence (a_1, a_2, ...) with a_{n+1} ≡ a_n mod p^n
determines a unique element of ℤ_p^τ.
We verify: if we build a coherent tower from x, the limit = x mod p^d.
Equations
- Tau.BookIII.Spectral.completeness_check bound depth = Tau.BookIII.Spectral.completeness_check.go bound depth 0 1 ((bound + 1) * 3)
Instances For

---

### `Tau.BookIII.Spectral.completeness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L118-L128)@[irreducible]

**def
Tau.BookIII.Spectral.completeness_check.go
(bound depth : Denotation.TauIdx)

(x p_idx fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.completeness_check.check_tower`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L130-L138)@[irreducible]

**def
Tau.BookIII.Spectral.completeness_check.check_tower
(depth : Denotation.TauIdx)

(x p d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.limit_uniqueness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L141-L168)
**def
Tau.BookIII.Spectral.limit_uniqueness_check
(bound depth : Denotation.TauIdx)
 :Bool**


[III.P06] Uniqueness of limit: two tower-coherent sequences that
agree at all levels are equal (= same element of ℤ_p^τ).
Equations
- Tau.BookIII.Spectral.limit_uniqueness_check bound depth = Tau.BookIII.Spectral.limit_uniqueness_check.go bound depth 0 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Spectral.limit_uniqueness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L146-L158)@[irreducible]

**def
Tau.BookIII.Spectral.limit_uniqueness_check.go
(bound depth : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.limit_uniqueness_check.check_agreement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L160-L167)@[irreducible]

**def
Tau.BookIII.Spectral.limit_uniqueness_check.check_agreement
(depth : Denotation.TauIdx)

(x y p d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.local_field_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L196-L197)
**theorem
Tau.BookIII.Spectral.local_field_15_4 :local_field_check 15 4 = true**


---

### `Tau.BookIII.Spectral.local_ring_10_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L200-L201)
**theorem
Tau.BookIII.Spectral.local_ring_10_4 :local_ring_check 10 4 = true**


---

### `Tau.BookIII.Spectral.completeness_20_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L204-L205)
**theorem
Tau.BookIII.Spectral.completeness_20_5 :completeness_check 20 5 = true**


---

### `Tau.BookIII.Spectral.limit_unique_10_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L208-L209)
**theorem
Tau.BookIII.Spectral.limit_unique_10_4 :limit_uniqueness_check 10 4 = true**


---

### `Tau.BookIII.Spectral.val_p_is_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L215-L216)
**theorem
Tau.BookIII.Spectral.val_p_is_1 :padic_val 3 3 = 1**


[III.D21] Structural: p-adic valuation of p is 1.

---

### `Tau.BookIII.Spectral.val_p_is_1'`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L217-L217)
**theorem
Tau.BookIII.Spectral.val_p_is_1' :padic_val 5 5 = 1**


---

### `Tau.BookIII.Spectral.val_p2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L219-L220)
**theorem
Tau.BookIII.Spectral.val_p2 :padic_val 9 3 = 2**


[III.D21] Structural: p-adic valuation of p^k is k.

---

### `Tau.BookIII.Spectral.val_p3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L221-L221)
**theorem
Tau.BookIII.Spectral.val_p3 :padic_val 27 3 = 3**


---

### `Tau.BookIII.Spectral.val_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L223-L224)
**theorem
Tau.BookIII.Spectral.val_zero :padic_val 0 3 = 0**


[III.D21] Structural: p-adic valuation of 0 is 0 (convention).

---

### `Tau.BookIII.Spectral.tower_42_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/LocalFields.lean#L226-L228)
**theorem
Tau.BookIII.Spectral.tower_42_3 :42 % 3 ^ 3 % 3 ^ 2 = 42 % 3 ^ 2**


[III.P06] Structural: tower coherence at p=3, x=42.
