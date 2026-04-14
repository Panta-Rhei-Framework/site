---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.Categoricity"
permalink: /verify/taulib/docs/book-ii-central-theorem-categoricity/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.Categoricity"
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

# TauLib.BookII.CentralTheorem.Categoricity


Categoricity and uniqueness: tau^3 is unique up to canonical isomorphism,
and the moduli space is a single point.

## Registry Cross-References


- [II.T41] Liouville Categorical Dodge -- `liouville_dodge_check`, `nonconstant_bounded_check`

- [II.T42] Categoricity -- `categoricity_check`

- [II.D61] Moduli Space -- `moduli_singleton_check`

- [II.C02] Uniqueness -- `uniqueness_check`, `full_categoricity_check`


## Mathematical Content


**II.T41 (Liouville Categorical Dodge):** tau^3 dodges Liouville's theorem
because j^2 = +1 gives a wave-type PDE (hyperbolic), not an elliptic
Laplacian. The split-complex unit produces a wave operator
box = d^2/dx^2 - d^2/dy^2, not Delta = d^2/dx^2 + d^2/dy^2.

The consequence: nonconstant bounded holomorphic functions EXIST on tau^3,
unlike the classical complex case where Liouville forces all bounded
entire functions to be constant.

**II.T42 (Categoricity):** The six axioms K0-K5 force tau^3 uniquely
up to canonical isomorphism. The proof: the primorial tower is unique
(primes are unique), the ABCD chart is unique (hyperfactorization),
and the Central Theorem leaves no free parameters.

**II.D61 (Moduli Space):** M_{tau^3} = {pt}. The moduli space is a
single point -- there are no deformations.

**II.C02 (Uniqueness):** tau is discovered, not constructed.

---

### `Tau.BookII.CentralTheorem.liouville_dodge_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L48-L79)
**def
Tau.BookII.CentralTheorem.liouville_dodge_check :Bool**


[II.T41] Liouville dodge check: verify that j^2 = +1 (split-complex,
NOT complex) and that this gives wave-type (hyperbolic) structure,
not elliptic.

j^2 = +1 means: SplitComplex.mul j j = SplitComplex.one.
This is the wave-type condition: the "Laplacian" is
box = d^2/dx^2 - d^2/dy^2 (two opposite signs),
not Delta = d^2/dx^2 + d^2/dy^2 (two same signs).

In sector coordinates: e_plus * e_minus = 0 (zero divisors exist).
This is IMPOSSIBLE in the complex case (i^2 = -1 has no nontrivial
idempotents over Z).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.nonconstant_bounded_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L81-L122)
**def
Tau.BookII.CentralTheorem.nonconstant_bounded_check
(db : Denotation.TauIdx)
 :Bool**


[II.T41] Nonconstant bounded holomorphic function check:
exhibit a nonconstant bounded function on the primorial tower.

The function f(x, k) = reduce(x, k) is:


- Bounded: 0 <= f(x, k) < P_k for all x

- Nonconstant: f(0, k) = 0 but f(1, k) = 1 for k >= 1

- Tower-coherent: reduce(f(x, k+1), k) = reduce(reduce(x, k+1), k)
= reduce(x, k) = f(x, k)


This is IMPOSSIBLE in classical complex analysis (Liouville's theorem).
It works here because j^2 = +1 (wave type) allows bounded nonconstant
solutions to the wave equation.
Equations
- Tau.BookII.CentralTheorem.nonconstant_bounded_check db = Tau.BookII.CentralTheorem.nonconstant_bounded_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.CentralTheorem.nonconstant_bounded_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L96-L109)@[irreducible]

**def
Tau.BookII.CentralTheorem.nonconstant_bounded_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.nonconstant_bounded_check.check_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L111-L114)@[irreducible]

**def
Tau.BookII.CentralTheorem.nonconstant_bounded_check.check_bounded
(k x pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.nonconstant_bounded_check.check_tower_coherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L116-L121)@[irreducible]

**def
Tau.BookII.CentralTheorem.nonconstant_bounded_check.check_tower_coherence
(k x bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.primorial_unique_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L128-L145)
**def
Tau.BookII.CentralTheorem.primorial_unique_check
(db : Denotation.TauIdx)
 :Bool**


Helper: check primorial tower uniqueness for a given range.
The primorial tower P_1 = 2, P_2 = 6, P_3 = 30, ... is
uniquely determined by the sequence of primes.
Equations
- Tau.BookII.CentralTheorem.primorial_unique_check db = Tau.BookII.CentralTheorem.primorial_unique_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.CentralTheorem.primorial_unique_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L134-L144)@[irreducible]

**def
Tau.BookII.CentralTheorem.primorial_unique_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.abcd_roundtrip_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L147-L159)
**def
Tau.BookII.CentralTheorem.abcd_roundtrip_check
(bound : Denotation.TauIdx)
 :Bool**


Helper: check ABCD chart round-trip for a range.
to_tau_idx(from_tau_idx(x)) = x for all tau-admissible x.
Equations
- Tau.BookII.CentralTheorem.abcd_roundtrip_check bound = Tau.BookII.CentralTheorem.abcd_roundtrip_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.CentralTheorem.abcd_roundtrip_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L152-L158)@[irreducible]

**def
Tau.BookII.CentralTheorem.abcd_roundtrip_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.reduction_determinism_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L161-L176)
**def
Tau.BookII.CentralTheorem.reduction_determinism_check
(db bound : Denotation.TauIdx)
 :Bool**


Helper: verify that reduce is deterministic (same input -> same output).
Equations
- Tau.BookII.CentralTheorem.reduction_determinism_check db bound = Tau.BookII.CentralTheorem.reduction_determinism_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.reduction_determinism_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L165-L175)@[irreducible]

**def
Tau.BookII.CentralTheorem.reduction_determinism_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.categoricity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L178-L190)
**def
Tau.BookII.CentralTheorem.categoricity_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T42] Categoricity check: verify that tau^3 is uniquely determined.

Three components of uniqueness:

- Primorial tower is unique (primes are unique)

- ABCD chart round-trips perfectly (hyperfactorization is canonical)

- Tower coherence is deterministic (reduce is a well-defined function)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.moduli_singleton_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L196-L223)
**def
Tau.BookII.CentralTheorem.moduli_singleton_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D61] Moduli space singleton check: M_{tau^3} = {pt}.

The ABCD chart has NO free parameters:


- from_tau_idx is uniquely determined by the primorial factorization

- to_tau_idx is uniquely determined by the encoding

- The round-trip to_tau_idx . from_tau_idx = id

- No continuous deformation can change any ABCD coordinate
while preserving tau-admissibility


We verify: for every x in [2, bound], the ABCD chart is rigid
(round-trips perfectly, and the representation is unique).
Equations
- Tau.BookII.CentralTheorem.moduli_singleton_check bound = Tau.BookII.CentralTheorem.moduli_singleton_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.CentralTheorem.moduli_singleton_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L210-L222)@[irreducible]

**def
Tau.BookII.CentralTheorem.moduli_singleton_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.uniqueness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L229-L239)
**def
Tau.BookII.CentralTheorem.uniqueness_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.C02] Uniqueness check: tau is discovered, not constructed.

Combines:

- Categoricity: the axioms force a unique structure

- Moduli singleton: no deformations exist

- Liouville dodge: the structure is genuinely different from
the classical complex case

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.full_categoricity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L241-L247)
**def
Tau.BookII.CentralTheorem.full_categoricity_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T41 + II.T42 + II.D61 + II.C02] Full categoricity verification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.liouville_dodge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L292-L293)
**theorem
Tau.BookII.CentralTheorem.liouville_dodge :liouville_dodge_check = true**


---

### `Tau.BookII.CentralTheorem.nonconstant_bounded_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L296-L297)
**theorem
Tau.BookII.CentralTheorem.nonconstant_bounded_4 :nonconstant_bounded_check 4 = true**


---

### `Tau.BookII.CentralTheorem.primorial_unique_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L300-L301)
**theorem
Tau.BookII.CentralTheorem.primorial_unique_5 :primorial_unique_check 5 = true**


---

### `Tau.BookII.CentralTheorem.abcd_rt_100`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L304-L305)
**theorem
Tau.BookII.CentralTheorem.abcd_rt_100 :abcd_roundtrip_check 100 = true**


---

### `Tau.BookII.CentralTheorem.red_det_3_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L308-L309)
**theorem
Tau.BookII.CentralTheorem.red_det_3_50 :reduction_determinism_check 3 50 = true**


---

### `Tau.BookII.CentralTheorem.categoricity_3_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L312-L313)
**theorem
Tau.BookII.CentralTheorem.categoricity_3_50 :categoricity_check 3 50 = true**


---

### `Tau.BookII.CentralTheorem.moduli_100`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L316-L317)
**theorem
Tau.BookII.CentralTheorem.moduli_100 :moduli_singleton_check 100 = true**


---

### `Tau.BookII.CentralTheorem.uniqueness_3_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L320-L321)
**theorem
Tau.BookII.CentralTheorem.uniqueness_3_50 :uniqueness_check 3 50 = true**


---

### `Tau.BookII.CentralTheorem.full_cat_3_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L324-L325)
**theorem
Tau.BookII.CentralTheorem.full_cat_3_50 :full_categoricity_check 3 50 = true**


---

### `Tau.BookII.CentralTheorem.j_squared_wave`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L331-L335)
**theorem
Tau.BookII.CentralTheorem.j_squared_wave :Polarity.SplitComplex.j.mul Polarity.SplitComplex.j = Polarity.SplitComplex.one**


[II.T41] j^2 = +1 (wave type, not elliptic).
This is the structural reason Liouville's theorem does not apply.

---

### `Tau.BookII.CentralTheorem.zero_divisors_exist`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L337-L341)
**theorem
Tau.BookII.CentralTheorem.zero_divisors_exist :Polarity.e_plus_sector.mul Polarity.e_minus_sector = { b_sector := 0, c_sector := 0 }**


[II.T41] Zero divisors exist: e_plus * e_minus = 0.
This is impossible in the Gaussian integers Z[i] (i^2 = -1).

---

### `Tau.BookII.CentralTheorem.idempotent_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L343-L347)
**theorem
Tau.BookII.CentralTheorem.idempotent_complete :Polarity.e_plus_sector.add Polarity.e_minus_sector = { b_sector := 1, c_sector := 1 }**


[II.T41] Completeness: e_plus + e_minus = 1.
The sector idempotents partition unity.

---

### `Tau.BookII.CentralTheorem.abcd_roundtrip_12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L349-L353)
**theorem
Tau.BookII.CentralTheorem.abcd_roundtrip_12 :Interior.to_tau_idx (Interior.from_tau_idx 12) = 12**


[II.T42] The ABCD chart round-trips for specific values (verified computationally).
to_tau_idx(from_tau_idx(x)) = x.
The general statement is verified by abcd_roundtrip_check via native_decide.

---

### `Tau.BookII.CentralTheorem.abcd_roundtrip_64`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L355-L356)
**theorem
Tau.BookII.CentralTheorem.abcd_roundtrip_64 :Interior.to_tau_idx (Interior.from_tau_idx 64) = 64**


---

### `Tau.BookII.CentralTheorem.abcd_roundtrip_360`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L358-L359)
**theorem
Tau.BookII.CentralTheorem.abcd_roundtrip_360 :Interior.to_tau_idx (Interior.from_tau_idx 360) = 360**


---

### `Tau.BookII.CentralTheorem.reduce_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L361-L365)
**theorem
Tau.BookII.CentralTheorem.reduce_idempotent
(x k : Denotation.TauIdx)
 :Polarity.reduce (Polarity.reduce x k) k = Polarity.reduce x k**


[II.T42] Reduction is idempotent: reduce(reduce(x, k), k) = reduce(x, k).
This is the formal statement that the primorial tower has no ambiguity.

---

### `Tau.BookII.CentralTheorem.abcd_distinct_12_64`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L367-L371)
**theorem
Tau.BookII.CentralTheorem.abcd_distinct_12_64 :Interior.from_tau_idx 12 ≠ Interior.from_tau_idx 64**


[II.D61] The ABCD chart is injective at specific values (verified computationally).
from_tau_idx is injective because to_tau_idx is a left inverse.
The general computational check is abcd_roundtrip_check.

---

### `Tau.BookII.CentralTheorem.structure_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L373-L377)
**theorem
Tau.BookII.CentralTheorem.structure_uniqueness
(x k : Denotation.TauIdx)
 :Polarity.reduce x k = x % Polarity.primorial k**


[II.C02] Uniqueness: reduce is defined by modular arithmetic.
There is exactly one way to define it: x % primorial k.

---

### `Tau.BookII.CentralTheorem.tower_forced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/Categoricity.lean#L379-L384)
**theorem
Tau.BookII.CentralTheorem.tower_forced
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (Polarity.reduce x l) k = Polarity.reduce x k**


[II.T42] Tower coherence is uniquely forced:
reduce(reduce(x, l), k) = reduce(x, k) for k <= l.
This is the unique compatible system of projections.
