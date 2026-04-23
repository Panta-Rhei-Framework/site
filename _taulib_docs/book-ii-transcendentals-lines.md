---
layout: taulib-doc
title: "TauLib.BookII.Transcendentals.Lines"
permalink: /verify/taulib/docs/book-ii-transcendentals-lines/
lane: verify
module_name: "TauLib.BookII.Transcendentals.Lines"
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

# TauLib.BookII.Transcendentals.Lines


Alpha-ray lines and the real line as an inverse limit.

## Registry Cross-References


- [II.D24] Alpha-Ray Line -- `alpha_ray_member`

- [II.D25] Level Circle -- `level_circle_mem`

- [II.T20] R as Inverse Limit -- `real_inverse_limit_check`


## Mathematical Content


The alpha-ray is the canonical radial sequence: points with D-coordinate
varying while A is fixed and B = C = 1. At each stage k, the D-coordinate
ranges over residues mod P_k, and as k -> infinity the inverse limit
recovers the real line R.

Level circles: points sharing the same D-residue mod P_k at stage k.

---

### `Tau.BookII.Transcendentals.alpha_ray_member`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L33-L38)
**def
Tau.BookII.Transcendentals.alpha_ray_member
(x a : Denotation.TauIdx)
 :Bool**


[II.D24] Alpha-ray membership: x belongs to the alpha-ray with
prime direction a iff its ABCD chart has A = a, B = 1, C = 1.
The D-coordinate varies freely (subject to constraint C3).
Equations
- Tau.BookII.Transcendentals.alpha_ray_member x a = ((Tau.BookII.Interior.from_tau_idx x).a == a && (Tau.BookII.Interior.from_tau_idx x).b == 1 && (Tau.BookII.Interior.from_tau_idx x).c == 1)
Instances For

---

### `Tau.BookII.Transcendentals.alpha_ray_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L40-L48)
**def
Tau.BookII.Transcendentals.alpha_ray_count
(a bound : Denotation.TauIdx)
 :Nat**


Count alpha-ray members in [2, bound] for a given prime a.
Equations
- Tau.BookII.Transcendentals.alpha_ray_count a bound = Tau.BookII.Transcendentals.alpha_ray_count.go a bound 2 (bound + 1) 0
Instances For

---

### `Tau.BookII.Transcendentals.alpha_ray_count.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L44-L47)@[irreducible]

**def
Tau.BookII.Transcendentals.alpha_ray_count.go
(a bound : Denotation.TauIdx)

(x fuel acc : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.level_circle_mem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L54-L57)
**def
Tau.BookII.Transcendentals.level_circle_mem
(x y k : Denotation.TauIdx)
 :Bool**


[II.D25] Level circle at stage k: two points share the same
D-residue mod primorial(k).
Equations
- Tau.BookII.Transcendentals.level_circle_mem x y k = ((Tau.BookII.Interior.from_tau_idx x).d % Tau.Polarity.primorial k == (Tau.BookII.Interior.from_tau_idx y).d % Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Transcendentals.level_nesting_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L59-L70)
**def
Tau.BookII.Transcendentals.level_nesting_check
(bound : Denotation.TauIdx)
 :Bool**


Level circles refine: agreement at stage k+1 implies agreement at stage k.
Equations
- Tau.BookII.Transcendentals.level_nesting_check bound = Tau.BookII.Transcendentals.level_nesting_check.go bound 2 2 1 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Transcendentals.level_nesting_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L63-L69)@[irreducible]

**def
Tau.BookII.Transcendentals.level_nesting_check.go
(bound : Denotation.TauIdx)

(x y k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.count_d_residues`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L76-L86)
**def
Tau.BookII.Transcendentals.count_d_residues
(a k bound : Denotation.TauIdx)
 :Nat**


Collect distinct D-residues mod primorial(k) among alpha-ray members in [2, bound].
Equations
- Tau.BookII.Transcendentals.count_d_residues a k bound = Tau.BookII.Transcendentals.count_d_residues.go a k bound 2 (bound + 1) []
Instances For

---

### `Tau.BookII.Transcendentals.count_d_residues.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L80-L85)@[irreducible]

**def
Tau.BookII.Transcendentals.count_d_residues.go
(a k bound : Denotation.TauIdx)

(x fuel : Nat)

(acc : List Denotation.TauIdx)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.real_inverse_limit_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L88-L102)
**def
Tau.BookII.Transcendentals.real_inverse_limit_check
(a bound stages : Denotation.TauIdx)
 :Bool**


[II.T20] R as inverse limit: at each stage k, the number of distinct
D-residues is positive and bounded by primorial(k).
The D-residue space grows with the primorial, witnessing the inverse
limit structure lim Z/P_k Z = Z_hat -> R.
Equations
- Tau.BookII.Transcendentals.real_inverse_limit_check a bound stages = Tau.BookII.Transcendentals.real_inverse_limit_check.go a bound stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Transcendentals.real_inverse_limit_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L95-L101)@[irreducible]

**def
Tau.BookII.Transcendentals.real_inverse_limit_check.go
(a bound stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.alpha_ray_growth_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L104-L115)
**def
Tau.BookII.Transcendentals.alpha_ray_growth_check
(a bound stages : Denotation.TauIdx)
 :Bool**


Alpha-ray growth: more D-residues appear at higher stages.
count_d_residues(k) <= count_d_residues(k+1) (monotone refinement).
Equations
- Tau.BookII.Transcendentals.alpha_ray_growth_check a bound stages = Tau.BookII.Transcendentals.alpha_ray_growth_check.go a bound stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Transcendentals.alpha_ray_growth_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L109-L114)@[irreducible]

**def
Tau.BookII.Transcendentals.alpha_ray_growth_check.go
(a bound stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.alpha_ray_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L145-L145)
**theorem
Tau.BookII.Transcendentals.alpha_ray_2 :alpha_ray_member 2 2 = true**


---

### `Tau.BookII.Transcendentals.alpha_ray_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L146-L146)
**theorem
Tau.BookII.Transcendentals.alpha_ray_3 :alpha_ray_member 3 3 = true**


---

### `Tau.BookII.Transcendentals.alpha_ray_12`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L147-L147)
**theorem
Tau.BookII.Transcendentals.alpha_ray_12 :alpha_ray_member 12 3 = true**


---

### `Tau.BookII.Transcendentals.alpha_ray_not_8`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L148-L148)
**theorem
Tau.BookII.Transcendentals.alpha_ray_not_8 :alpha_ray_member 8 2 = false**


---

### `Tau.BookII.Transcendentals.alpha_ray_not_64`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L149-L149)
**theorem
Tau.BookII.Transcendentals.alpha_ray_not_64 :alpha_ray_member 64 2 = false**


---

### `Tau.BookII.Transcendentals.level_nest_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L151-L151)
**theorem
Tau.BookII.Transcendentals.level_nest_20 :level_nesting_check 20 = true**


---

### `Tau.BookII.Transcendentals.inv_lim_2_50_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L152-L152)
**theorem
Tau.BookII.Transcendentals.inv_lim_2_50_3 :real_inverse_limit_check 2 50 3 = true**


---

### `Tau.BookII.Transcendentals.growth_2_50_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Transcendentals/Lines.lean#L153-L153)
**theorem
Tau.BookII.Transcendentals.growth_2_50_3 :alpha_ray_growth_check 2 50 3 = true**
