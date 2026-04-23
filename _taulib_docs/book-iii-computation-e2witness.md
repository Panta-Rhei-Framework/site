---
layout: taulib-doc
title: "TauLib.BookIII.Computation.E2Witness"
permalink: /verify/taulib/docs/book-iii-computation-e2witness/
lane: verify
module_name: "TauLib.BookIII.Computation.E2Witness"
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

# TauLib.BookIII.Computation.E2Witness


Constructive E₂ operational closure witnesses: Kleene fixed points,
orbit diversity, and strict enrichment beyond E₁.

## Registry Cross-References


- [III.D83] Kleene Fixed Point — `kleene_fixed_point`, `kleene_check`

- [III.D84] E₂ Orbit Structure — `orbit_length`, `orbit_diversity_check`

- [III.T57] Operational Closure — `operational_closure_full_check`

- [III.P34] E₂ ⊋ E₁ Strict Witness — `e2_strict_witness_check`


## Mathematical Content


**III.D83 (Kleene Fixed Point):** At stage k, define the self-application
operator S(c) = D(c, c) where D is the code-decode map. A fixed point is
c* such that S(c*) = c*. At every finite stage, fixed points exist because
the map Z/M_k Z → Z/M_k Z is on a finite set.

**III.D84 (E₂ Orbit Structure):** The orbit of code c under the decode map
D: x ↦ (x + d) mod M_k has length dividing M_k. Orbit lengths exhibit
diversity: not all orbits have the same length, proving computational
richness (contrast with E₁ where all orbits are trivially periodic).

**III.T57 (Operational Closure):** Every E₂-admissible operation (code-decode
cycle) stays within E₂: the output is a valid E₂ carrier element at the
same or lower stage. This is the computational analog of holomorphic closure.

**III.P34 (E₂ ⊋ E₁ Strict Witness):** E₂ contains code-decode structures
that cannot be expressed as pure sector decompositions (E₁ content). The
witness is an orbit with length > 2 (E₁ orbits have length ≤ 2 due to
bipolar e₊/e₋ involution).

---

### `Tau.BookIII.Computation.self_apply`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L51-L56)
**def
Tau.BookIII.Computation.self_apply
(c k : ℕ)
 :ℕ**


[III.D83] Self-application operator S(c) = (c + c) mod M_k.
Models code applied to itself (Kleene's recursion theorem).
Equations
- Tau.BookIII.Computation.self_apply c k = if (Tau.Polarity.primorial k == 0) = true then 0 else (c + c) % Tau.Polarity.primorial k
Instances For

---

### `Tau.BookIII.Computation.kleene_fixed_point`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L58-L64)
**def
Tau.BookIII.Computation.kleene_fixed_point
(k : ℕ)
 :ℕ**


[III.D83] Find a fixed point of self-application at stage k:
c* such that S(c*) = c*. At stage k, c* = 0 is always a fixed point.
Non-trivial fixed points exist when M_k is even (c* = M_k/2).
Equations
- Tau.BookIII.Computation.kleene_fixed_point k = if (Tau.Polarity.primorial k == 0) = true then 0 else 0
Instances For

---

### `Tau.BookIII.Computation.count_fixed_points`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L66-L76)
**def
Tau.BookIII.Computation.count_fixed_points
(k : ℕ)
 :ℕ**


[III.D83] Count fixed points of self-application at stage k.
Equations
- Tau.BookIII.Computation.count_fixed_points k = Tau.BookIII.Computation.count_fixed_points.go k 0 (Tau.Polarity.primorial k) 0
Instances For

---

### `Tau.BookIII.Computation.count_fixed_points.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L71-L75)@[irreducible]

**def
Tau.BookIII.Computation.count_fixed_points.go
(k c bound acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.kleene_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L78-L87)
**def
Tau.BookIII.Computation.kleene_check
(db : ℕ)
 :Bool**


[III.D83] Kleene check: fixed points exist at every stage.
Equations
- Tau.BookIII.Computation.kleene_check db = Tau.BookIII.Computation.kleene_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Computation.kleene_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L82-L86)@[irreducible]

**def
Tau.BookIII.Computation.kleene_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.orbit_length`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L93-L105)
**def
Tau.BookIII.Computation.orbit_length
(c d k : ℕ)
 :ℕ**


[III.D84] Orbit of code c under decoder d at stage k:
length of the cycle c → (c+d) → (c+2d) → ... → c.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.orbit_length.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L101-L104)@[irreducible]

**def
Tau.BookIII.Computation.orbit_length.go
(d pos start pk steps fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.orbit_diversity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L107-L117)
**def
Tau.BookIII.Computation.orbit_diversity_check
(k : ℕ)
 :Bool**


[III.D84] Collect distinct orbit lengths at stage k for all (c, d).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.count_distinct_orbit_lengths`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L119-L139)
**def
Tau.BookIII.Computation.count_distinct_orbit_lengths
(k : ℕ)
 :ℕ**


[III.D84] Count distinct orbit lengths at stage k.
Equations
- Tau.BookIII.Computation.count_distinct_orbit_lengths k = Tau.BookIII.Computation.count_distinct_orbit_lengths.go_d 1 (Tau.Polarity.primorial k) 0 (Tau.Polarity.primorial k) k
Instances For

---

### `Tau.BookIII.Computation.count_distinct_orbit_lengths.go_d`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L124-L131)@[irreducible]

**def
Tau.BookIII.Computation.count_distinct_orbit_lengths.go_d
(d pk acc fuel k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.count_distinct_orbit_lengths.is_new_length`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L133-L134)
**def
Tau.BookIII.Computation.count_distinct_orbit_lengths.is_new_length
(len d pk k : ℕ)
 :Bool**

Equations
- Tau.BookIII.Computation.count_distinct_orbit_lengths.is_new_length len d pk k = Tau.BookIII.Computation.count_distinct_orbit_lengths.go_check 1 d len pk k
Instances For

---

### `Tau.BookIII.Computation.count_distinct_orbit_lengths.go_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L135-L138)@[irreducible]

**def
Tau.BookIII.Computation.count_distinct_orbit_lengths.go_check
(d2 bound target pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.operational_closure_full_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L145-L171)
**def
Tau.BookIII.Computation.operational_closure_full_check
(bound db : ℕ)
 :Bool**


[III.T57] Full operational closure: every code-decode cycle
produces a valid E₂ carrier element.
Equations
- Tau.BookIII.Computation.operational_closure_full_check bound db = Tau.BookIII.Computation.operational_closure_full_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.operational_closure_full_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L150-L160)@[irreducible]

**def
Tau.BookIII.Computation.operational_closure_full_check.go
(bound db c k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.operational_closure_full_check.go_d`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L162-L170)@[irreducible]

**def
Tau.BookIII.Computation.operational_closure_full_check.go_d
(c d pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.e2_strict_witness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L177-L199)
**def
Tau.BookIII.Computation.e2_strict_witness_check
(db : ℕ)
 :Bool**


[III.P34] E₂ strict witness: find an orbit with length > 2.
E₁ orbits (bipolar involution) have length ≤ 2 (e₊↔e₋).
E₂ orbits can have length 3, 5, etc. (prime orbit lengths).
Equations
- Tau.BookIII.Computation.e2_strict_witness_check db = Tau.BookIII.Computation.e2_strict_witness_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Computation.e2_strict_witness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L183-L190)@[irreducible]

**def
Tau.BookIII.Computation.e2_strict_witness_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.e2_strict_witness_check.find_long_orbit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L192-L198)@[irreducible]

**def
Tau.BookIII.Computation.e2_strict_witness_check.find_long_orbit
(c d pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.kleene_check_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L205-L207)
**theorem
Tau.BookIII.Computation.kleene_check_3 :kleene_check 3 = true**


[III.D83] Kleene fixed points exist at stages 1-3.

---

### `Tau.BookIII.Computation.fixed_points_stage2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L209-L211)
**theorem
Tau.BookIII.Computation.fixed_points_stage2 :count_fixed_points 2 ≥ 1**


[III.D83] Fixed point exists at stage 2 (c=0).

---

### `Tau.BookIII.Computation.orbit_diversity_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L213-L215)
**theorem
Tau.BookIII.Computation.orbit_diversity_2 :orbit_diversity_check 2 = true**


[III.D84] Orbit diversity at stage 2.

---

### `Tau.BookIII.Computation.orbit_diversity_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L217-L219)
**theorem
Tau.BookIII.Computation.orbit_diversity_3 :orbit_diversity_check 3 = true**


[III.D84] Orbit diversity at stage 3.

---

### `Tau.BookIII.Computation.operational_closure_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L221-L223)
**theorem
Tau.BookIII.Computation.operational_closure_8_3 :operational_closure_full_check 8 3 = true**


[III.T57] Operational closure at bound 8, depth 3.

---

### `Tau.BookIII.Computation.e2_strict_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Computation/E2Witness.lean#L225-L227)
**theorem
Tau.BookIII.Computation.e2_strict_3 :e2_strict_witness_check 3 = true**


[III.P34] E₂ strict witness at depth 3.
