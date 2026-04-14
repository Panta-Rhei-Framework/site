---
layout: taulib-doc
title: "TauLib.BookI.Polarity.PrimeBridge"
permalink: /verify/taulib/docs/book-i-polarity-prime-bridge/
lane: verify
module_name: "TauLib.BookI.Polarity.PrimeBridge"
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

# TauLib.Polarity.PrimeBridge


Reflection lemma: `is_prime_bool p = true ↔ idx_prime p`.

Bridges computable Boolean primality (`is_prime_bool`) to the propositional
definition (`idx_prime`). This is the foundational link needed for the CRT
formal proof chain.

## Main Results


- `no_factor_below_true_imp`: forward correctness of trial division

- `no_factor_below_of_spec`: backward correctness of trial division

- `is_prime_bool_iff`: the reflection lemma


---

### `Tau.Polarity.no_factor_below_true_imp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/PrimeBridge.lean#L66-L70)
**theorem
Tau.Polarity.no_factor_below_true_imp
(n d : Denotation.TauIdx)

(hn : n ≥ 2)

(hd : d ≥ 2)

(h : Coordinates.no_factor_below n d = true)

(k : Denotation.TauIdx)
 :k ≥ d → k * k ≤ n → n % k ≠ 0**


If no_factor_below n d = true, then no k in [d, √n] divides n.

---

### `Tau.Polarity.no_factor_below_of_spec`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/PrimeBridge.lean#L104-L108)
**theorem
Tau.Polarity.no_factor_below_of_spec
(n d : Denotation.TauIdx)

(hn : n ≥ 2)

(hd : d ≥ 2)

(hspec : ∀ (k : Denotation.TauIdx), k ≥ d → k * k ≤ n → n % k ≠ 0)
 :Coordinates.no_factor_below n d = true**


If no k in [d, √n] divides n, then no_factor_below n d = true.

---

### `Tau.Polarity.is_prime_of_bool`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/PrimeBridge.lean#L114-L159)
**theorem
Tau.Polarity.is_prime_of_bool
(p : Denotation.TauIdx)

(h : Coordinates.is_prime_bool p = true)
 :Coordinates.idx_prime p**


Forward: is_prime_bool p = true → idx_prime p.

---

### `Tau.Polarity.bool_of_is_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/PrimeBridge.lean#L165-L179)
**theorem
Tau.Polarity.bool_of_is_prime
(p : Denotation.TauIdx)

(h : Coordinates.idx_prime p)
 :Coordinates.is_prime_bool p = true**


Backward: idx_prime p → is_prime_bool p = true.

---

### `Tau.Polarity.is_prime_bool_iff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/PrimeBridge.lean#L185-L187)
**theorem
Tau.Polarity.is_prime_bool_iff
(p : Denotation.TauIdx)
 :Coordinates.is_prime_bool p = true ↔ Coordinates.idx_prime p**


Boolean primality reflects propositional primality.
