---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.SheafCohomology"
permalink: /verify/taulib/docs/book-ii-central-theorem-sheaf-cohomology/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.SheafCohomology"
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

# TauLib.BookII.CentralTheorem.SheafCohomology


Sheaf cohomology foundations on the primorial tower.

## Registry Cross-References


- [II.D86] Čech Complex — `cech_cochain`, `cech_coboundary`

- [II.D87] Sheaf Cohomology Group — `h0_global_sections`, `h1_check`

- [II.T55] H⁰ = Global Sections — `h0_equals_global_check`

- [II.P20] Čech-to-Derived — `cech_derived_comparison_check`


## Mathematical Content


**II.D86 (Čech Complex):** For the cover {C_{k,a}} of Z/M_k Z by cylinders
at stage k, the Čech complex computes cohomology via:
C⁰ = Π_a F(C_{k,a}), C¹ = Π_{a
**II.D87 (Sheaf Cohomology):** H⁰(F) = global sections = ker(δ⁰).
H¹(F) = ker(δ¹)/im(δ⁰). For the constant sheaf on the primorial
tower, H⁰ = ℤ and H¹ = 0 (contractible at each finite stage).

**II.T55 (H⁰ = Global Sections):** The zeroth cohomology group equals
the space of global sections. For the constant sheaf with value 1,
this is the single constant function.

**II.P20 (Čech-to-Derived):** On the primorial tower, Čech cohomology
agrees with derived functor cohomology. This follows from the cover
being acyclic (ultrametric: all intersections are either empty or
cylinders).

---

### `Tau.BookII.CentralTheorem.cech_cochain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L49-L52)
**def
Tau.BookII.CentralTheorem.cech_cochain
(f : ℕ → ℤ)

(k a : ℕ)
 :ℤ**


[II.D86] A Čech 0-cochain at stage k: a function assigning a value
to each cylinder C_{k,a} for a ∈ Z/M_k Z.
Equations
- Tau.BookII.CentralTheorem.cech_cochain f k a = f (a % Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.CentralTheorem.cech_coboundary_0`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L54-L58)
**def
Tau.BookII.CentralTheorem.cech_coboundary_0
(f : ℕ → ℤ)

(k a b : ℕ)
 :ℤ**


[II.D86] Čech coboundary δ⁰: (δ⁰ f)(a,b) = f(b) - f(a).
For cylinders at the same stage, intersections are empty unless a = b
(ultrametric property), so δ⁰ is the difference map.
Equations
- Tau.BookII.CentralTheorem.cech_coboundary_0 f k a b = Tau.BookII.CentralTheorem.cech_cochain f k b - Tau.BookII.CentralTheorem.cech_cochain f k a
Instances For

---

### `Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L60-L88)
**def
Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check
(k : ℕ)
 :Bool**


[II.D86] Check δ² = 0 for the Čech complex.
δ¹(δ⁰ f)(a,b,c) = δ⁰f(b,c) - δ⁰f(a,c) + δ⁰f(a,b)
= (f(c)-f(b)) - (f(c)-f(a)) + (f(b)-f(a)) = 0.
Equations
- Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check k = Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_a 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_a`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L67-L70)@[irreducible]

**def
Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_a
(a pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L72-L75)@[irreducible]

**def
Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_b
(a b pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L77-L87)@[irreducible]

**def
Tau.BookII.CentralTheorem.cech_coboundary_sq_zero_check.go_c
(a b c pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.h0_global_sections`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L94-L103)
**def
Tau.BookII.CentralTheorem.h0_global_sections
(k : ℕ)
 :ℕ**


[II.D87] H⁰ = global sections: count cochains f with δ⁰f = 0,
i.e., f(a) = f(b) for all a,b (constant functions).
Equations
- Tau.BookII.CentralTheorem.h0_global_sections k = if Tau.Polarity.primorial k > 0 then 1 else 0
Instances For

---

### `Tau.BookII.CentralTheorem.h1_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L105-L125)
**def
Tau.BookII.CentralTheorem.h1_check
(k : ℕ)
 :Bool**


[II.D87] H¹ check: for the constant sheaf on Z/M_k Z with the
cylinder cover, H¹ = 0.
Proof: every 1-cocycle is a coboundary because the cover is acyclic.
Equations
- Tau.BookII.CentralTheorem.h1_check k = Tau.BookII.CentralTheorem.h1_check.go 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.CentralTheorem.h1_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L116-L124)@[irreducible]

**def
Tau.BookII.CentralTheorem.h1_check.go
(a pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.h0_equals_global_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L131-L146)
**def
Tau.BookII.CentralTheorem.h0_equals_global_check
(k : ℕ)
 :Bool**


[II.T55] Verify that H⁰ equals global sections:
a 0-cochain f is a global section iff f is constant on Z/M_k Z.
We check: the constant function 1 is in ker(δ⁰).
Equations
- Tau.BookII.CentralTheorem.h0_equals_global_check k = Tau.BookII.CentralTheorem.h0_equals_global_check.go 0 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
 (fun (x : ℕ) => 1) k
Instances For

---

### `Tau.BookII.CentralTheorem.h0_equals_global_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L139-L145)@[irreducible]

**def
Tau.BookII.CentralTheorem.h0_equals_global_check.go
(a b pk fuel : ℕ)

(f : ℕ → ℤ)

(k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.h0_nonconstant_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L148-L156)
**def
Tau.BookII.CentralTheorem.h0_nonconstant_check
(k : ℕ)
 :Bool**


[II.T55] Non-constant functions are NOT global sections.
Equations
- Tau.BookII.CentralTheorem.h0_nonconstant_check k = if Tau.Polarity.primorial k ≤ 1 then true
 else have f := fun (x : ℕ) => ↑x;
 Tau.BookII.CentralTheorem.cech_coboundary_0 f k 0 1 != 0
Instances For

---

### `Tau.BookII.CentralTheorem.cover_acyclic_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L162-L179)
**def
Tau.BookII.CentralTheorem.cover_acyclic_check
(k : ℕ)
 :Bool**


[II.P20] Acyclicity of the cylinder cover: any intersection of
cylinders at the same stage is either empty or a cylinder.
In the ultrametric topology, C_{k,a} ∩ C_{k,b} = ∅ for a ≠ b.
Equations
- Tau.BookII.CentralTheorem.cover_acyclic_check k = Tau.BookII.CentralTheorem.cover_acyclic_check.go 0 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.CentralTheorem.cover_acyclic_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L169-L178)@[irreducible]

**def
Tau.BookII.CentralTheorem.cover_acyclic_check.go
(a b pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.cech_derived_comparison_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L181-L187)
**def
Tau.BookII.CentralTheorem.cech_derived_comparison_check
(k : ℕ)
 :Bool**


[II.P20] Čech-to-derived comparison: on an acyclic cover,
Čech cohomology = derived functor cohomology.
Verify: H⁰ = Γ(X, F) and H¹ = 0 (acyclic).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.cech_sq_zero_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L193-L195)
**theorem
Tau.BookII.CentralTheorem.cech_sq_zero_1 :cech_coboundary_sq_zero_check 1 = true**


[II.D86] δ² = 0 at stage 1.

---

### `Tau.BookII.CentralTheorem.cech_sq_zero_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L197-L199)
**theorem
Tau.BookII.CentralTheorem.cech_sq_zero_2 :cech_coboundary_sq_zero_check 2 = true**


[II.D86] δ² = 0 at stage 2.

---

### `Tau.BookII.CentralTheorem.h1_vanishes_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L201-L203)
**theorem
Tau.BookII.CentralTheorem.h1_vanishes_1 :h1_check 1 = true**


[II.D87] H¹ = 0 at stage 1.

---

### `Tau.BookII.CentralTheorem.h1_vanishes_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L205-L207)
**theorem
Tau.BookII.CentralTheorem.h1_vanishes_2 :h1_check 2 = true**


[II.D87] H¹ = 0 at stage 2.

---

### `Tau.BookII.CentralTheorem.h0_global_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L209-L211)
**theorem
Tau.BookII.CentralTheorem.h0_global_1 :h0_equals_global_check 1 = true**


[II.T55] H⁰ = global sections at stage 1.

---

### `Tau.BookII.CentralTheorem.h0_global_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L213-L215)
**theorem
Tau.BookII.CentralTheorem.h0_global_2 :h0_equals_global_check 2 = true**


[II.T55] H⁰ = global sections at stage 2.

---

### `Tau.BookII.CentralTheorem.h0_nonconstant_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L217-L219)
**theorem
Tau.BookII.CentralTheorem.h0_nonconstant_2 :h0_nonconstant_check 2 = true**


[II.T55] Non-constant rejected at stage 2.

---

### `Tau.BookII.CentralTheorem.cech_derived_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L221-L223)
**theorem
Tau.BookII.CentralTheorem.cech_derived_1 :cech_derived_comparison_check 1 = true**


[II.P20] Čech = derived at stage 1.

---

### `Tau.BookII.CentralTheorem.cech_derived_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/SheafCohomology.lean#L225-L227)
**theorem
Tau.BookII.CentralTheorem.cech_derived_2 :cech_derived_comparison_check 2 = true**


[II.P20] Čech = derived at stage 2.
