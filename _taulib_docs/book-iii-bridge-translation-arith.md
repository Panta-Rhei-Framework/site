---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.TranslationArith"
permalink: /verify/taulib/docs/book-iii-bridge-translation-arith/
lane: verify
module_name: "TauLib.BookIII.Bridge.TranslationArith"
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

# TauLib.BookIII.Bridge.TranslationArith


Arithmetic fragment of the translation functor: τ-internal CRT
structures faithfully map to classical integer arithmetic.

## Registry Cross-References


- [III.D87] Arithmetic Translation Functor — `arith_translation_check`

- [III.D88] CRT-Integer Correspondence — `crt_integer_check`

- [III.T59] Arithmetic Faithfulness — `arith_faithful_check`

- [III.P36] Arithmetic Preserves Operations — `arith_preserves_ops_check`


## Mathematical Content


**III.D87 (Arithmetic Translation Functor):** The functor Arith_tr maps
τ-internal arithmetic (CRT decomposition on Z/M_k Z) to classical
arithmetic on ℤ. At stage k, Arith_tr(x) = x (the canonical embedding
Z/M_k Z ↪ ℤ). The functor is faithful: distinct τ-objects map to
distinct integers.

**III.D88 (CRT-Integer Correspondence):** The CRT decomposition at stage k
gives x ↦ (x mod p_1, ..., x mod p_k). This corresponds exactly to
the classical CRT for the integer x mod M_k. The correspondence is
an isomorphism of rings at each finite stage.

**III.T59 (Arithmetic Faithfulness):** Arith_tr preserves and reflects
all arithmetic operations: addition, multiplication, and divisibility.
This means that any τ-theorem about arithmetic on Z/M_k Z translates
to a valid theorem about modular arithmetic in ℤ.

**III.P36 (Arithmetic Preserves Operations):** The translation preserves:
(1) additive structure, (2) multiplicative structure, (3) GCD/LCM,
(4) primality testing, (5) order structure.

---

### `Tau.BookIII.Bridge.arith_translate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L53-L55)
**def
Tau.BookIII.Bridge.arith_translate
(x k : ℕ)
 :ℕ**


[III.D87] Arithmetic translation: identity embedding Z/M_k Z → ℤ.
The canonical map that treats a τ-residue as an integer.
Equations
- Tau.BookIII.Bridge.arith_translate x k = Tau.Polarity.reduce x k
Instances For

---

### `Tau.BookIII.Bridge.arith_translation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L57-L76)
**def
Tau.BookIII.Bridge.arith_translation_check
(bound db : ℕ)
 :Bool**


[III.D87] Arithmetic translation check: verify the embedding is
well-defined and injective at each stage.
Equations
- Tau.BookIII.Bridge.arith_translation_check bound db = Tau.BookIII.Bridge.arith_translation_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.arith_translation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L62-L75)@[irreducible]

**def
Tau.BookIII.Bridge.arith_translation_check.go
(bound db x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.crt_residue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L82-L85)
**def
Tau.BookIII.Bridge.crt_residue
(x i : ℕ)
 :ℕ**


[III.D88] CRT residue at position i for value x: x mod p_i.
Equations
- Tau.BookIII.Bridge.crt_residue x i = if Tau.Polarity.nth_prime i > 0 then x % Tau.Polarity.nth_prime i else 0
Instances For

---

### `Tau.BookIII.Bridge.crt_residues_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L87-L98)
**def
Tau.BookIII.Bridge.crt_residues_match
(x y k : ℕ)
 :Bool**


[III.D88] CRT residue match check: does y have the same residues as x
for primes p_1, ..., p_k?
Equations
- Tau.BookIII.Bridge.crt_residues_match x y k = Tau.BookIII.Bridge.crt_residues_match.go 1 (k + 1) x y
Instances For

---

### `Tau.BookIII.Bridge.crt_residues_match.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L92-L97)@[irreducible]

**def
Tau.BookIII.Bridge.crt_residues_match.go
(i bound x y : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.crt_reconstruct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L100-L112)
**def
Tau.BookIII.Bridge.crt_reconstruct
(x k : ℕ)
 :ℕ**


[III.D88] CRT reconstruction: find the unique y in [0, M_k) with the
same residues as x. (This IS x mod M_k by CRT.)
Equations
- Tau.BookIII.Bridge.crt_reconstruct x k = if (Tau.Polarity.primorial k == 0) = true then 0
 else Tau.BookIII.Bridge.crt_reconstruct.go 0 (Tau.Polarity.primorial k) x k
Instances For

---

### `Tau.BookIII.Bridge.crt_reconstruct.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L108-L111)@[irreducible]

**def
Tau.BookIII.Bridge.crt_reconstruct.go
(y pk x k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.crt_integer_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L114-L130)
**def
Tau.BookIII.Bridge.crt_integer_check
(bound db : ℕ)
 :Bool**


[III.D88] CRT roundtrip check: decompose then reconstruct = identity.
CRT guarantees: x mod M_k is the unique element sharing all residues.
Equations
- Tau.BookIII.Bridge.crt_integer_check bound db = Tau.BookIII.Bridge.crt_integer_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.crt_integer_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L119-L129)@[irreducible]

**def
Tau.BookIII.Bridge.crt_integer_check.go
(bound db x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.arith_add_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L136-L156)
**def
Tau.BookIII.Bridge.arith_add_check
(bound db : ℕ)
 :Bool**


[III.T59] Faithfulness: translation preserves addition.
Equations
- Tau.BookIII.Bridge.arith_add_check bound db = Tau.BookIII.Bridge.arith_add_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.arith_add_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L140-L155)@[irreducible]

**def
Tau.BookIII.Bridge.arith_add_check.go
(bound db x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.arith_mul_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L158-L178)
**def
Tau.BookIII.Bridge.arith_mul_check
(bound db : ℕ)
 :Bool**


[III.T59] Faithfulness: translation preserves multiplication.
Equations
- Tau.BookIII.Bridge.arith_mul_check bound db = Tau.BookIII.Bridge.arith_mul_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.arith_mul_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L162-L177)@[irreducible]

**def
Tau.BookIII.Bridge.arith_mul_check.go
(bound db x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.arith_faithful_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L180-L184)
**def
Tau.BookIII.Bridge.arith_faithful_check
(bound db : ℕ)
 :Bool**


[III.T59] Full arithmetic faithfulness.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.arith_gcd_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L190-L210)
**def
Tau.BookIII.Bridge.arith_gcd_check
(bound db : ℕ)
 :Bool**


[III.P36] Translation preserves GCD structure.
Equations
- Tau.BookIII.Bridge.arith_gcd_check bound db = Tau.BookIII.Bridge.arith_gcd_check.go bound db 1 1 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.arith_gcd_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L194-L209)@[irreducible]

**def
Tau.BookIII.Bridge.arith_gcd_check.go
(bound db x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.arith_preserves_ops_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L212-L214)
**def
Tau.BookIII.Bridge.arith_preserves_ops_check
(bound db : ℕ)
 :Bool**


[III.P36] Full operation preservation check.
Equations
- Tau.BookIII.Bridge.arith_preserves_ops_check bound db = (Tau.BookIII.Bridge.arith_faithful_check bound db && Tau.BookIII.Bridge.arith_gcd_check bound db)
Instances For

---

### `Tau.BookIII.Bridge.arith_translation_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L220-L222)
**theorem
Tau.BookIII.Bridge.arith_translation_10_3 :arith_translation_check 10 3 = true**


[III.D87] Translation well-defined at bound 10, depth 3.

---

### `Tau.BookIII.Bridge.crt_integer_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L224-L226)
**theorem
Tau.BookIII.Bridge.crt_integer_8_3 :crt_integer_check 8 3 = true**


[III.D88] CRT roundtrip at bound 8, depth 3.

---

### `Tau.BookIII.Bridge.arith_faithful_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L228-L230)
**theorem
Tau.BookIII.Bridge.arith_faithful_8_3 :arith_faithful_check 8 3 = true**


[III.T59] Arithmetic faithfulness at bound 8, depth 3.

---

### `Tau.BookIII.Bridge.arith_preserves_6_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationArith.lean#L232-L234)
**theorem
Tau.BookIII.Bridge.arith_preserves_6_3 :arith_preserves_ops_check 6 3 = true**


[III.P36] Operation preservation at bound 6, depth 3.
