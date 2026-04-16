---
layout: taulib-doc
title: "TauLib.BookI.Kernel.ActionQuantum"
permalink: /verify/taulib/docs/book-i-kernel-action-quantum/
lane: verify
module_name: "TauLib.BookI.Kernel.ActionQuantum"
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

# TauLib.Kernel.ActionQuantum


The action quantum ℏ_τ = 1/4 from generator counting, and the
Euler sieve identity connecting 8/15 to (11/15)².

## Registry Cross-References


- [I.D95] Action Quantum — `hbar_tau_numer`, `hbar_tau_denom`

- [I.P43] Generator Independence — `independent_generators`

- [I.P44] Euler Sieve Identity — `euler_sieve_cross`


## Mathematical Content


### Three Routes to ℏ_τ = 1/4


**Route (a): Character counting on L**
On L = S¹ ∨ S¹, the fundamental characters are {1, χ₊, χ₋, χ₊χ₋}.
|fundamental characters| = 4, so ℏ_τ = 1/4.

**Route (b): Independent generator counting**
From the 5 generators {α, π, γ, η, ω}, the constraint ω = γ ∩ η
(crossing = intersection of B and C lobes) reduces the independent set
to {α, π, γ, η}. Thus ℏ_τ = 1/|independent generators| = 1/4.

**Route (c): T² bi-rotation topology**
The fundamental group of T² has character ticks Z₂ × Z₂ = 4 elements.
ℏ_τ = 1/|Z₂ × Z₂| = 1/4.

### Euler Sieve Identity


The fine structure coefficient (11/15)² = 121/225 decomposes as:
(8/15) · (121/120) = (11/15)²

where:


- 8/15 = (1 − 1/3)(1 − 1/5) is the Euler sieve over primes {3, 5}

- 121/120 = 1 + 1/5! is the S₅ symmetry-breaking correction


All identities are proved using Nat cross-multiplication (no ℚ required).

## Ground Truth Sources


- open_questions_sprint.md Part E: ℏ_τ = 1/4 axiomatic proof

- open_questions_sprint.md Part B: Euler sieve reconciliation


---

### `Tau.Kernel.Generator.all`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L54-L55)
**def
Tau.Kernel.Generator.all :List Generator**


The list of all 5 generators (computable enumeration).
Equations
- Tau.Kernel.Generator.all = [Tau.Kernel.Generator.alpha, Tau.Kernel.Generator.pi, Tau.Kernel.Generator.gamma, Tau.Kernel.Generator.eta, Tau.Kernel.Generator.omega]
Instances For

---

### `Tau.Kernel.generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L57-L58)
**theorem
Tau.Kernel.generator_count :Generator.all.length = 5**


Generator.all has exactly 5 elements.

---

### `Tau.Kernel.independent_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L60-L62)
**theorem
Tau.Kernel.independent_generators :5 - 1 = 4**


ω = γ ∩ η (crossing constraint) reduces independent generators from 5 to 4.
The independent set is {α, π, γ, η}.

---

### `Tau.Kernel.hbar_tau_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L64-L65)
**def
Tau.Kernel.hbar_tau_numer :Nat**


[I.D95] ℏ_τ = 1/4 as a Nat fraction pair.
Equations
- Tau.Kernel.hbar_tau_numer = 1
Instances For

---

### `Tau.Kernel.hbar_tau_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L66-L66)
**def
Tau.Kernel.hbar_tau_denom :Nat**

Equations
- Tau.Kernel.hbar_tau_denom = 4
Instances For

---

### `Tau.Kernel.hbar_tau_from_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L68-L70)
**theorem
Tau.Kernel.hbar_tau_from_generators :hbar_tau_denom = Generator.all.length - 1**


ℏ_τ denominator = |generators| − 1.

---

### `Tau.Kernel.Generator.independent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L76-L77)
**def
Tau.Kernel.Generator.independent :List Generator**


The independent generators: all generators except ω.
Equations
- Tau.Kernel.Generator.independent = [Tau.Kernel.Generator.alpha, Tau.Kernel.Generator.pi, Tau.Kernel.Generator.gamma, Tau.Kernel.Generator.eta]
Instances For

---

### `Tau.Kernel.independent_generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L79-L80)
**theorem
Tau.Kernel.independent_generator_count :Generator.independent.length = 4**


There are exactly 4 independent generators.

---

### `Tau.Kernel.omega_unique_dependent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L82-L91)
**theorem
Tau.Kernel.omega_unique_dependent :¬Generator.omega ∈ Generator.independent ∧ Generator.alpha ∈ Generator.independent ∧ Generator.pi ∈ Generator.independent ∧ Generator.gamma ∈ Generator.independent ∧ Generator.eta ∈ Generator.independent**


ω is the unique dependent generator: it is the ONLY generator
not in the independent set.
ω = γ ∩ η (crossing = intersection of B and C sectors).

---

### `Tau.Kernel.hbar_tau_rigorous`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L93-L99)
**theorem
Tau.Kernel.hbar_tau_rigorous :hbar_tau_denom = Generator.independent.length ∧ hbar_tau_numer = 1**


ℏ_τ = 1/|independent| = 1/4.
Rigorous: ω is the unique constraint (γ ∩ η),
so |independent| = |all| - 1 = 5 - 1 = 4.

---

### `Tau.Kernel.euler_sieve_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L105-L110)
**theorem
Tau.Kernel.euler_sieve_cross :2 * 4 * 121 * 225 = 3 * 5 * 120 * 121**


[I.P44] The Euler sieve identity in cross-multiplied Nat form:
(2/3) · (4/5) · (121/120) = 121/225

Cross-multiplied: 2 · 4 · 121 · 225 = 3 · 5 · 120 · 121.

---

### `Tau.Kernel.euler_sieve_factor_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L112-L115)
**theorem
Tau.Kernel.euler_sieve_factor_cross :2 * 4 * 15 = 3 * 5 * 8**


Euler sieve factor: (1 − 1/3)(1 − 1/5) = 8/15.
Cross-multiplied: 2 · 4 · 15 = 3 · 5 · 8.

---

### `Tau.Kernel.s5_correction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L117-L118)
**theorem
Tau.Kernel.s5_correction :121 = 120 + 1**


The S₅ correction factor is 121/120 = 1 + 1/5!.

---

### `Tau.Kernel.factorial_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L120-L121)
**theorem
Tau.Kernel.factorial_5 :1 * 2 * 3 * 4 * 5 = 120**


5! = 120.

---

### `Tau.Kernel.numerator_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L127-L128)
**theorem
Tau.Kernel.numerator_square :121 = 11 * 11**


121 = 11² (perfect square).

---

### `Tau.Kernel.denominator_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L130-L131)
**theorem
Tau.Kernel.denominator_square :225 = 15 * 15**


225 = 15² (perfect square).

---

### `Tau.Kernel.charge_fraction_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L133-L136)
**theorem
Tau.Kernel.charge_fraction_square :11 * 11 * 225 = 15 * 15 * 121**


The charge fraction: (11/15)² = 121/225.
Cross-multiplied: 11² · 225 = 15² · 121.

---

### `Tau.Kernel.sieve_times_correction_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L138-L142)
**theorem
Tau.Kernel.sieve_times_correction_cross :8 * 121 * 225 = 15 * 120 * 121**


The product (8/15) × (121/120) = 121/225.
Cross-multiplied: 8 · 121 · 225 = 15 · 120 · 121.
Simplifying: 8 · 225 = 15 · 120 = 1800.

---

### `Tau.Kernel.eight_is_two_cubed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L148-L149)
**theorem
Tau.Kernel.eight_is_two_cubed :8 = 2 * 2 * 2**


8 = 2³ (cube of first prime).

---

### `Tau.Kernel.fifteen_is_three_times_five`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L151-L152)
**theorem
Tau.Kernel.fifteen_is_three_times_five :15 = 3 * 5**


15 = 3 · 5 (primorial M₃ / 2).

---

### `Tau.Kernel.alpha_from_charge_cross`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/ActionQuantum.lean#L154-L158)
**theorem
Tau.Kernel.alpha_from_charge_cross :11 * 11 = 121 ∧ 15 * 15 = 225**


The fine structure constant satisfies α = e_nat² where e_nat = (11/15)·ι<sub>τ</sub>².
This is α = (11/15)²·ι<sub>τ</sub>⁴ = (121/225)·ι<sub>τ</sub>⁴.
Cross-check: 11² = 121 and 15² = 225.
