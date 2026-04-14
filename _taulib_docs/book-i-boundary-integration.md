---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Integration"
permalink: /verify/taulib/docs/book-i-boundary-integration/
lane: verify
module_name: "TauLib.BookI.Boundary.Integration"
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

# TauLib.Boundary.Integration


Constructive integration on the primorial tower.

## Registry Cross-References


- [I.D99] τ-Integral — `tau_integral`, `integral_check`

- [I.T51] Linearity of Integration — `integral_linearity_check`

- [I.P45] Monotone Convergence — `monotone_convergence_check`


## Mathematical Content


**I.D99 (τ-Integral):** The integral of a function f: Z/M_k Z → ℤ at stage k
is the normalized sum: ∫*k f = (1/M_k) Σ*{x=0}^{M_k-1} f(x). This is the
expectation under the counting measure μ_k.

**I.T51 (Linearity):** ∫_k (af + bg) = a ∫_k f + b ∫_k g. Verified as an
equality of rational pairs (numerator/denominator).

**I.P45 (Monotone Convergence):** For a tower-compatible family of functions
f_k: Z/M_k Z → ℤ with f_k ≤ f_{k+1} (appropriately defined), the integrals
∫_k f_k form a non-decreasing sequence.

---

### `Tau.Boundary.stage_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L38-L45)
**def
Tau.Boundary.stage_sum
(f : ℕ → ℤ)

(k : ℕ)
 :ℤ**


[I.D99] Sum a function over Z/M_k Z.
Equations
- Tau.Boundary.stage_sum f k = Tau.Boundary.stage_sum.go f 0 (Tau.Polarity.primorial k) 0
Instances For

---

### `Tau.Boundary.stage_sum.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L42-L44)@[irreducible]

**def
Tau.Boundary.stage_sum.go
(f : ℕ → ℤ)

(x bound : ℕ)

(acc : ℤ)
 :ℤ**

Equations
- Tau.Boundary.stage_sum.go f x bound acc = if x ≥ bound then acc else Tau.Boundary.stage_sum.go f (x + 1) bound (acc + f x)
Instances For

---

### `Tau.Boundary.TauIntegral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L47-L52)
**structure
Tau.Boundary.TauIntegral :Type**


[I.D99] The τ-integral as a rational pair:
∫_k f = (Σ f(x), M_k).

- numerator : ℤ
- denominator : ℕ
Instances For

---

### `Tau.Boundary.instReprTauIntegral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L52-L52)
**instance
Tau.Boundary.instReprTauIntegral :Repr TauIntegral**

Equations
- Tau.Boundary.instReprTauIntegral = { reprPrec := Tau.Boundary.instReprTauIntegral.repr }

---

### `Tau.Boundary.instReprTauIntegral.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L52-L52)
**def
Tau.Boundary.instReprTauIntegral.repr :TauIntegral → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.tau_integral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L54-L57)
**def
Tau.Boundary.tau_integral
(f : ℕ → ℤ)

(k : ℕ)
 :TauIntegral**


[I.D99] Compute the integral of f at stage k.
Equations
- Tau.Boundary.tau_integral f k = { numerator := Tau.Boundary.stage_sum f k, denominator := Tau.Polarity.primorial k }
Instances For

---

### `Tau.Boundary.integral_equiv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L59-L62)
**def
Tau.Boundary.integral_equiv
(i j : TauIntegral)
 :Bool**


[I.D99] Two integrals are equivalent (same rational value):
a/b = c/d iff a*d = c*b.
Equations
- Tau.Boundary.integral_equiv i j = (i.numerator * ↑j.denominator == j.numerator * ↑i.denominator)
Instances For

---

### `Tau.Boundary.integral_linearity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L68-L77)
**def
Tau.Boundary.integral_linearity_check
(a b : ℤ)

(f g : ℕ → ℤ)

(k : ℕ)
 :Bool**


[I.T51] Check linearity: ∫(af + bg) = a∫f + b∫g at stage k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.monotone_convergence_check_step`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L83-L91)
**def
Tau.Boundary.monotone_convergence_check_step
(f : ℕ → ℕ → ℤ)

(k : ℕ)
 :Bool**


[I.P45] Check that integrals increase from stage k to stage k+1
for a given function family.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.const_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L97-L98)
**def
Tau.Boundary.const_one :ℕ → ℤ**


The constant function f(x) = 1.
Equations
- Tau.Boundary.const_one x✝ = 1
Instances For

---

### `Tau.Boundary.ident_fn`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L100-L101)
**def
Tau.Boundary.ident_fn :ℕ → ℤ**


The identity function f(x) = x.
Equations
- Tau.Boundary.ident_fn x = ↑x
Instances For

---

### `Tau.Boundary.even_indicator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L103-L104)
**def
Tau.Boundary.even_indicator :ℕ → ℤ**


The indicator of even numbers.
Equations
- Tau.Boundary.even_indicator x = if (x % 2 == 0) = true then 1 else 0
Instances For

---

### `Tau.Boundary.integral_const_one_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L110-L112)
**theorem
Tau.Boundary.integral_const_one_3 :(tau_integral const_one 3).numerator = 30**


[I.D99] Integral of constant 1 at stage 3: ∫_3 1 = 30/30 = 1.

---

### `Tau.Boundary.linearity_2f_3g_stage2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L114-L116)
**theorem
Tau.Boundary.linearity_2f_3g_stage2 :integral_linearity_check 2 3 ident_fn const_one 2 = true**


[I.T51] Linearity for (2f + 3g) at stage 2.

---

### `Tau.Boundary.linearity_identity_stage2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L118-L120)
**theorem
Tau.Boundary.linearity_identity_stage2 :integral_linearity_check 1 0 ident_fn const_one 2 = true**


[I.T51] Linearity for (1f + 0g) at stage 2 (identity).

---

### `Tau.Boundary.integral_even_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Integration.lean#L122-L124)
**theorem
Tau.Boundary.integral_even_2 :(tau_integral even_indicator 2).numerator = 3**


[I.D99] Integral of even indicator at stage 2: 3/6 = 1/2.
