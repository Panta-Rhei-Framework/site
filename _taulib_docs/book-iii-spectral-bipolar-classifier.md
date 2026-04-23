---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.BipolarClassifier"
permalink: /verify/taulib/docs/book-iii-spectral-bipolar-classifier/
lane: verify
module_name: "TauLib.BookIII.Spectral.BipolarClassifier"
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

# TauLib.BookIII.Spectral.BipolarClassifier


Internal Bipolar Classifier (Label_n), Label Convergence,
and Label-Idempotent Compatibility.

## Registry Cross-References


- [III.D23] Internal Bipolar Classifier -- `PrimeLabel`, `label_at_depth`, `classifier_check`

- [III.T13] Label Convergence -- `label_convergence_check`

- [III.P08] Label-Idempotent Compatibility -- `label_idem_check`


## Mathematical Content


**III.D23 (Internal Bipolar Classifier):** Label_n: computable classifier
mapping primes ≤ p_n to {B, C, X}. B-type = exponent/χ₊-dominant,
C-type = tetration/χ₋-dominant, X-type = balanced.

**III.T13 (Label Convergence):** Label_n stabilizes: for each prime p,
there exists n₀ such that Label_n(p) is constant for n ≥ n₀.

**III.P08 (Label-Idempotent Compatibility):** B-type primes correspond
to e₊-dominant spectral coefficients, C-type to e₋-dominant.

---

### `Tau.BookIII.Spectral.PrimeLabel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L38-L44)
**inductive
Tau.BookIII.Spectral.PrimeLabel :Type**


[III.D23] Prime labels: B-type (multiplicative/Galois dominant),
C-type (additive/automorphic dominant), X-type (balanced).

- B : PrimeLabel
- C : PrimeLabel
- X : PrimeLabel
Instances For

---

### `Tau.BookIII.Spectral.instReprPrimeLabel.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**def
Tau.BookIII.Spectral.instReprPrimeLabel.repr :PrimeLabel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instReprPrimeLabel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**instance
Tau.BookIII.Spectral.instReprPrimeLabel :Repr PrimeLabel**

Equations
- Tau.BookIII.Spectral.instReprPrimeLabel = { reprPrec := Tau.BookIII.Spectral.instReprPrimeLabel.repr }

---

### `Tau.BookIII.Spectral.instDecidableEqPrimeLabel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**instance
Tau.BookIII.Spectral.instDecidableEqPrimeLabel :DecidableEq PrimeLabel**

Equations
- Tau.BookIII.Spectral.instDecidableEqPrimeLabel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Spectral.instBEqPrimeLabel.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**def
Tau.BookIII.Spectral.instBEqPrimeLabel.beq :PrimeLabel → PrimeLabel → Bool**

Equations
- Tau.BookIII.Spectral.instBEqPrimeLabel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Spectral.instBEqPrimeLabel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**instance
Tau.BookIII.Spectral.instBEqPrimeLabel :BEq PrimeLabel**

Equations
- Tau.BookIII.Spectral.instBEqPrimeLabel = { beq := Tau.BookIII.Spectral.instBEqPrimeLabel.beq }

---

### `Tau.BookIII.Spectral.instInhabitedPrimeLabel.default`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**def
Tau.BookIII.Spectral.instInhabitedPrimeLabel.default :PrimeLabel**

Equations
- Tau.BookIII.Spectral.instInhabitedPrimeLabel.default = Tau.BookIII.Spectral.PrimeLabel.B
Instances For

---

### `Tau.BookIII.Spectral.instInhabitedPrimeLabel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L44-L44)
**instance
Tau.BookIII.Spectral.instInhabitedPrimeLabel :Inhabited PrimeLabel**

Equations
- Tau.BookIII.Spectral.instInhabitedPrimeLabel = { default := Tau.BookIII.Spectral.instInhabitedPrimeLabel.default }

---

### `Tau.BookIII.Spectral.label_at_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L46-L70)
**def
Tau.BookIII.Spectral.label_at_depth
(p_idx n : Denotation.TauIdx)
 :PrimeLabel**


[III.D23] Classify a prime by its spectral behavior at depth n.
Uses the CRT basis element e_i at depth n to determine the
dominant channel of p_{i+1}:


- B-type if CRT basis projects primarily to B-sector

- C-type if CRT basis projects primarily to C-sector

- X-type if balanced


Concrete criterion: compare p mod 4.
p ≡ 1 mod 4: B-type (quadratic residue structure, multiplicative)
p ≡ 3 mod 4: C-type (non-residue structure, additive)
p = 2: X-type (balanced, the crossing prime)
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.label_direct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L72-L78)
**def
Tau.BookIII.Spectral.label_direct
(p : Denotation.TauIdx)
 :PrimeLabel**


[III.D23] Direct label based on the prime's residue mod 4.
This is the stable classifier (does not depend on depth).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.label_counts`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L80-L93)
**def
Tau.BookIII.Spectral.label_counts
(k : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx**


[III.D23] Count B, C, X primes up to depth k.
Equations
- Tau.BookIII.Spectral.label_counts k = Tau.BookIII.Spectral.label_counts.go k 1 0 0 0 (k + 1)
Instances For

---

### `Tau.BookIII.Spectral.label_counts.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L84-L92)@[irreducible]

**def
Tau.BookIII.Spectral.label_counts.go
(k : Denotation.TauIdx)

(i b_ct c_ct x_ct fuel : ℕ)
 :Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.classifier_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L95-L112)
**def
Tau.BookIII.Spectral.classifier_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D23] Classifier check: verify label assignment is consistent
across methods for all primes up to bound.
Equations
- Tau.BookIII.Spectral.classifier_check bound = Tau.BookIII.Spectral.classifier_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.classifier_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L100-L111)@[irreducible]

**def
Tau.BookIII.Spectral.classifier_check.go
(bound : Denotation.TauIdx)

(i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.label_convergence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L118-L141)
**def
Tau.BookIII.Spectral.label_convergence_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T13] Label convergence: label_direct is depth-independent,
so it trivially stabilizes. Verify that label_at_depth agrees
with label_direct for all primes at sufficient depth.
Equations
- Tau.BookIII.Spectral.label_convergence_check bound = Tau.BookIII.Spectral.label_convergence_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.label_convergence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L126-L140)@[irreducible]

**def
Tau.BookIII.Spectral.label_convergence_check.go
(bound : Denotation.TauIdx)

(i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.bc_balance_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L143-L147)
**def
Tau.BookIII.Spectral.bc_balance_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T13] B-C balance: both B-type and C-type primes exist
in every sufficiently large range.
Equations
- Tau.BookIII.Spectral.bc_balance_check bound = match Tau.BookIII.Spectral.label_counts bound with
 | (b, c, _x) => decide (b > 0) && decide (c > 0)
Instances For

---

### `Tau.BookIII.Spectral.label_idem_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L153-L181)
**def
Tau.BookIII.Spectral.label_idem_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P08] Label-idempotent compatibility: B-type primes have
e₊-dominant CRT basis, C-type have e₋-dominant.
Verification via the bipolar decomposition of CRT basis elements.
Equations
- Tau.BookIII.Spectral.label_idem_check bound db = Tau.BookIII.Spectral.label_idem_check.go bound db 1 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Spectral.label_idem_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L159-L180)@[irreducible]

**def
Tau.BookIII.Spectral.label_idem_check.go
(bound db : Denotation.TauIdx)

(i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.split_complex_label_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L183-L207)
**def
Tau.BookIII.Spectral.split_complex_label_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P08] Split-complex decomposition respects labels:
B-type primes have CRT basis elements with b-dominant interior,
C-type have c-dominant interior.
Equations
- Tau.BookIII.Spectral.split_complex_label_check bound db = Tau.BookIII.Spectral.split_complex_label_check.go bound db 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.split_complex_label_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L189-L206)@[irreducible]

**def
Tau.BookIII.Spectral.split_complex_label_check.go
(bound db : Denotation.TauIdx)

(i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.classifier_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L235-L236)
**theorem
Tau.BookIII.Spectral.classifier_20 :classifier_check 20 = true**


---

### `Tau.BookIII.Spectral.label_conv_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L239-L240)
**theorem
Tau.BookIII.Spectral.label_conv_20 :label_convergence_check 20 = true**


---

### `Tau.BookIII.Spectral.bc_balance_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L243-L244)
**theorem
Tau.BookIII.Spectral.bc_balance_5 :bc_balance_check 5 = true**


---

### `Tau.BookIII.Spectral.label_idem_10_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L247-L248)
**theorem
Tau.BookIII.Spectral.label_idem_10_4 :label_idem_check 10 4 = true**


---

### `Tau.BookIII.Spectral.split_label_10_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L251-L252)
**theorem
Tau.BookIII.Spectral.split_label_10_4 :split_complex_label_check 10 4 = true**


---

### `Tau.BookIII.Spectral.two_is_x`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L258-L259)
**theorem
Tau.BookIII.Spectral.two_is_x :label_direct 2 = PrimeLabel.X**


[III.D23] Structural: 2 is the unique X-type prime.

---

### `Tau.BookIII.Spectral.five_is_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L261-L262)
**theorem
Tau.BookIII.Spectral.five_is_b :label_direct 5 = PrimeLabel.B**


[III.D23] Structural: 5 is B-type (5 mod 4 = 1).

---

### `Tau.BookIII.Spectral.three_is_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L264-L265)
**theorem
Tau.BookIII.Spectral.three_is_c :label_direct 3 = PrimeLabel.C**


[III.D23] Structural: 3 is C-type (3 mod 4 = 3).

---

### `Tau.BookIII.Spectral.bc_exist_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/BipolarClassifier.lean#L267-L268)
**theorem
Tau.BookIII.Spectral.bc_exist_3 :bc_balance_check 3 = true**


[III.T13] Structural: both B and C labels exist for first 3 primes.
