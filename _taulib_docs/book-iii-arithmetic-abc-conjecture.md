---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.ABCConjecture"
permalink: /verify/taulib/docs/book-iii-arithmetic-abc-conjecture/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.ABCConjecture"
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

# TauLib.BookIII.Arithmetic.ABCConjecture


ABC conjecture formulation on the primorial tower: radical function,
quality measure, and ABC inequality verification at finite stages.

## Registry Cross-References


- [III.D97] Radical Function — `radical`, `radical_check`

- [III.D98] ABC Quality — `abc_quality`, `abc_quality_bound_check`

- [III.T65] ABC at Primorial Levels — `abc_primorial_check`

- [III.P41] Radical-Primorial Identity — `radical_primorial_check`


## Mathematical Content


**III.D97 (Radical Function):** For n ∈ ℕ, rad(n) = product of distinct
prime divisors of n. On the primorial tower, rad(M_k) = M_k (since M_k
is squarefree by construction). This is the key structural advantage of
the primorial tower for ABC.

**III.D98 (ABC Quality):** For a triple (a, b, c) with a + b = c and
gcd(a,b) = 1, the quality q = log(c)/log(rad(abc)). The ABC conjecture
asserts q < 1 + ε for all but finitely many triples. At primorial
levels, we compute q for structured triples.

**III.T65 (ABC at Primorial Levels):** At primorial level k, every
coprime triple (a, b, a+b) with a, b < M_k satisfies the ABC inequality
c < rad(abc)^2. This is a finite verification of ABC for small values.

**III.P41 (Radical-Primorial Identity):** rad(M_k) = M_k for all k.
The primorial tower consists entirely of squarefree numbers, making
it the natural domain for ABC. The ABCD coordinate system decomposes
each integer via the tower, and the radical inherits this decomposition.

---

### `Tau.BookIII.Arithmetic.radical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L63-L85)
**def
Tau.BookIII.Arithmetic.radical
(n : ℕ)
 :ℕ**


[III.D97] Radical of n: product of distinct prime divisors.
rad(1) = 1, rad(p^k) = p, rad(p·q) = p·q.
Equations
- Tau.BookIII.Arithmetic.radical n = if n ≤ 1 then 1 else Tau.BookIII.Arithmetic.radical.go 2 n 1 (n + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.radical.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L69-L76)@[irreducible]

**def
Tau.BookIII.Arithmetic.radical.go
(d n acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.radical.strip`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L78-L80)
**def
Tau.BookIII.Arithmetic.radical.strip
(d n : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Arithmetic.radical.strip d n = if (decide (d ≤ 1) || n == 0) = true then n else Tau.BookIII.Arithmetic.radical.go_strip d n (n + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.radical.go_strip`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L81-L84)@[irreducible]

**def
Tau.BookIII.Arithmetic.radical.go_strip
(d n fuel : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Arithmetic.radical.go_strip d n fuel = if fuel = 0 then n
 else if (n % d == 0) = true then Tau.BookIII.Arithmetic.radical.go_strip d (n / d) (fuel - 1) else n
Instances For

---

### `Tau.BookIII.Arithmetic.radical_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L87-L102)
**def
Tau.BookIII.Arithmetic.radical_check
(bound : ℕ)
 :Bool**


[III.D97] Radical check: verify rad(n) divides n and rad(rad(n)) = rad(n)
(idempotence) for all n up to bound.
Equations
- Tau.BookIII.Arithmetic.radical_check bound = Tau.BookIII.Arithmetic.radical_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.radical_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L92-L101)@[irreducible]

**def
Tau.BookIII.Arithmetic.radical_check.go
(bound n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.abc_triple_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L108-L121)
**def
Tau.BookIII.Arithmetic.abc_triple_check
(a b : ℕ)
 :Bool**


[III.D98] ABC quality check for a triple (a, b, c=a+b):
verify c < rad(a·b·c)^2. This is a weak form of ABC (ε=1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.abc_quality_bound_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L123-L134)
**def
Tau.BookIII.Arithmetic.abc_quality_bound_check
(bound : ℕ)
 :Bool**


[III.D98] ABC quality bound check: for all coprime pairs (a,b) with
a, b ≤ bound, verify c < rad(abc)^2.
Equations
- Tau.BookIII.Arithmetic.abc_quality_bound_check bound = Tau.BookIII.Arithmetic.abc_quality_bound_check.go bound 1 1 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.abc_quality_bound_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L128-L133)@[irreducible]

**def
Tau.BookIII.Arithmetic.abc_quality_bound_check.go
(bound a b fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.abc_primorial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L140-L152)
**def
Tau.BookIII.Arithmetic.abc_primorial_check
(db : ℕ)
 :Bool**


[III.T65] ABC at primorial levels: for each stage k, check ABC for
coprime pairs (a, b) with a, b < min(M_k, 20).
Equations
- Tau.BookIII.Arithmetic.abc_primorial_check db = Tau.BookIII.Arithmetic.abc_primorial_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.abc_primorial_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L145-L151)@[irreducible]

**def
Tau.BookIII.Arithmetic.abc_primorial_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.radical_primorial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L158-L169)
**def
Tau.BookIII.Arithmetic.radical_primorial_check
(db : ℕ)
 :Bool**


[III.P41] Radical-primorial identity: rad(M_k) = M_k.
Primorials are squarefree (product of distinct primes).
Equations
- Tau.BookIII.Arithmetic.radical_primorial_check db = Tau.BookIII.Arithmetic.radical_primorial_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.radical_primorial_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L163-L168)@[irreducible]

**def
Tau.BookIII.Arithmetic.radical_primorial_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.radical_le_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L171-L182)
**def
Tau.BookIII.Arithmetic.radical_le_check
(bound : ℕ)
 :Bool**


[III.P41] Extended: rad(n) ≤ n for all n, with equality iff n is
squarefree. At primorial levels, equality holds.
Equations
- Tau.BookIII.Arithmetic.radical_le_check bound = Tau.BookIII.Arithmetic.radical_le_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.radical_le_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L176-L181)@[irreducible]

**def
Tau.BookIII.Arithmetic.radical_le_check.go
(bound n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.radical_check_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L188-L190)
**theorem
Tau.BookIII.Arithmetic.radical_check_30 :radical_check 30 = true**


[III.D97] Radical is well-defined and idempotent up to 30.

---

### `Tau.BookIII.Arithmetic.abc_quality_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L192-L194)
**theorem
Tau.BookIII.Arithmetic.abc_quality_15 :abc_quality_bound_check 15 = true**


[III.D98] ABC quality holds for coprime pairs up to 15.

---

### `Tau.BookIII.Arithmetic.abc_primorial_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L196-L198)
**theorem
Tau.BookIII.Arithmetic.abc_primorial_3 :abc_primorial_check 3 = true**


[III.T65] ABC at primorial levels up to depth 3.

---

### `Tau.BookIII.Arithmetic.radical_primorial_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L200-L202)
**theorem
Tau.BookIII.Arithmetic.radical_primorial_4 :radical_primorial_check 4 = true**


[III.P41] Radical-primorial identity up to depth 4.

---

### `Tau.BookIII.Arithmetic.radical_le_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L204-L206)
**theorem
Tau.BookIII.Arithmetic.radical_le_30 :radical_le_check 30 = true**


[III.P41] Radical ≤ n for all n up to 30.
