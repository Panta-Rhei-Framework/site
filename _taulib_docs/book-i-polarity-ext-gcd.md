---
layout: taulib-doc
title: "TauLib.BookI.Polarity.ExtGCD"
permalink: /verify/taulib/docs/book-i-polarity-ext-gcd/
lane: verify
module_name: "TauLib.BookI.Polarity.ExtGCD"
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

# TauLib.Polarity.ExtGCD


Extended GCD algorithm, Bézout identity, and modular inverse existence.

## Main Results


- `ext_gcd`: Extended GCD returning (gcd, s, t) with Int Bézout coefficients

- `ext_gcd_bezout`: Bézout identity: ↑a * s + ↑b * t = ↑(gcd a b)

- `mod_inv_exists`: For coprime a, m with m > 1, a modular inverse exists


---

### `Tau.Polarity.ext_gcd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ExtGCD.lean#L25-L33)@[irreducible]

**def
Tau.Polarity.ext_gcd
(a b : ℕ)
 :ℕ × ℤ × ℤ**


Extended GCD: returns (gcd, s, t) with gcd = Nat.gcd a b
and ↑a * s + ↑b * t = ↑gcd (Int coefficients).
Equations
- Tau.Polarity.ext_gcd a b = if b = 0 then (a, 1, 0)
 else have r := Tau.Polarity.ext_gcd b (a % b);
 (r.1, r.2.2, r.2.1 - ↑(a / b) * r.2.2)
Instances For

---

### `Tau.Polarity.ext_gcd_fst`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ExtGCD.lean#L39-L53)
**theorem
Tau.Polarity.ext_gcd_fst
(a b : ℕ)
 :(ext_gcd a b).1 = a.gcd b**


ext_gcd computes the GCD.

---

### `Tau.Polarity.ext_gcd_bezout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ExtGCD.lean#L55-L78)
**theorem
Tau.Polarity.ext_gcd_bezout
(a b : ℕ)
 :↑a * (ext_gcd a b).2.1 + ↑b * (ext_gcd a b).2.2 = ↑(ext_gcd a b).1**


Bézout identity: ↑a * s + ↑b * t = ↑(ext_gcd a b).1.

---

### `Tau.Polarity.ext_gcd_spec`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ExtGCD.lean#L80-L84)
**theorem
Tau.Polarity.ext_gcd_spec
(a b : ℕ)
 :↑a * (ext_gcd a b).2.1 + ↑b * (ext_gcd a b).2.2 = ↑(a.gcd b)**


Combined: ext_gcd gives Bézout coefficients for gcd.

---

### `Tau.Polarity.mod_inv_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ExtGCD.lean#L90-L130)
**theorem
Tau.Polarity.mod_inv_exists
(a m : ℕ)

(hcop : a.Coprime m)

(hm : m > 1)
 :∃ (x : ℕ), x < m ∧ a * x % m = 1**


If gcd(a, m) = 1 and m > 1, there exists x < m with (a*x) % m = 1.
