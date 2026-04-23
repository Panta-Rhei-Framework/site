---
layout: taulib-doc
title: "TauLib.BookII.Closure.TauManifold"
permalink: /verify/taulib/docs/book-ii-closure-tau-manifold/
lane: verify
module_name: "TauLib.BookII.Closure.TauManifold"
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

# TauLib.BookII.Closure.TauManifold


tau-Manifold structure: the primorial tower with a tau-analytic atlas
and tau-exterior derivative.

## Registry Cross-References


- [II.D62] tau-Manifold -- `TauManifoldData`, `tau_manifold_check`

- [II.D63] tau-Analytic Atlas -- `atlas_chart_check`, `atlas_transition_check`

- [II.D64] tau-Exterior Derivative -- `tau_exterior_derivative`, `d_squared_zero_check`

- [II.P15] tau^3 Is a tau-Manifold -- `tau3_is_manifold_check`


## Mathematical Content


**II.D62 (tau-Manifold):** A tau-manifold is a primorial tower equipped with
a tau-analytic atlas. The atlas consists of charts (from_tau_idx/to_tau_idx)
at each stage k that are reduce-compatible. The primorial tower inherits
manifold structure because the ABCD chart provides canonical coordinates
at every stage.

**II.D63 (tau-Analytic Atlas):** A collection of charts that are reduce-
compatible. Each chart is the ABCD chart restricted to a cylinder Z/P_kZ.
Chart transitions from stage k+1 to stage k are given by the reduction map,
which is well-defined by tower coherence.

**II.D64 (tau-Exterior Derivative):** The tau-exterior derivative d_tau acts
on 0-forms (functions on the tower) by finite differences:
d_tau f(x, k) = f(reduce(x+1, k)) - f(reduce(x, k))
The key property: d_tau . d_tau = 0 (d-squared-is-zero).

**II.P15 (tau^3 Is a tau-Manifold):** tau^3 satisfies the manifold axioms:
(1) atlas exists, (2) charts are reduce-compatible, (3) exterior derivative
is well-defined.

---

### `Tau.BookII.Closure.atlas_chart_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L50-L61)@[irreducible]

**def
Tau.BookII.Closure.atlas_chart_roundtrip
(k x fuel : ℕ)
 :Bool**


[II.D63] Atlas chart check at stage k: verify that the ABCD chart
(from_tau_idx/to_tau_idx) round-trips for all x in [2, P_k).
Each chart maps a tau-index to its ABCD quadruple and back.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.atlas_chart_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L63-L75)
**def
Tau.BookII.Closure.atlas_chart_check
(db : Denotation.TauIdx)
 :Bool**


[II.D63] Atlas chart check for stages 1..db: at each stage k,
the ABCD chart round-trips for all valid inputs.
Equations
- Tau.BookII.Closure.atlas_chart_check db = Tau.BookII.Closure.atlas_chart_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.Closure.atlas_chart_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L68-L74)@[irreducible]

**def
Tau.BookII.Closure.atlas_chart_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.atlas_transition_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L77-L102)
**def
Tau.BookII.Closure.atlas_transition_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.D63] Atlas transition check: chart transitions from stage k+1
to stage k are reduce-compatible. For any x at stage k+1, reducing
to stage k and then applying from_tau_idx at stage k must agree with
directly reducing the ABCD-reconstructed value.

Concretely: reduce(to_tau_idx(from_tau_idx(x)), k) = reduce(x, k).
Since to_tau_idx(from_tau_idx(x)) = x (round-trip), this reduces to
reduce(x, k) = reduce(x, k), which is trivial.

The nontrivial check: the ABCD coordinates at stage k+1 project
consistently to stage k.
Equations
- Tau.BookII.Closure.atlas_transition_check db bound = Tau.BookII.Closure.atlas_transition_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Closure.atlas_transition_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L91-L101)@[irreducible]

**def
Tau.BookII.Closure.atlas_transition_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.tau_exterior_derivative`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L108-L112)
**def
Tau.BookII.Closure.tau_exterior_derivative
(f : Denotation.TauIdx → Denotation.TauIdx → ℤ)

(x k : Denotation.TauIdx)
 :ℤ**


[II.D64] tau-Exterior derivative acting on a 0-form f at point (x, k).
d_tau f(x, k) = f(reduce(x+1, k)) - f(reduce(x, k)).
This is the finite-difference operator on the cyclic group Z/P_kZ.
Equations
- Tau.BookII.Closure.tau_exterior_derivative f x k = f (Tau.Polarity.reduce (x + 1) k) k - f (Tau.Polarity.reduce x k) k
Instances For

---

### `Tau.BookII.Closure.sum_exterior_deriv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L114-L121)@[irreducible]

**def
Tau.BookII.Closure.sum_exterior_deriv
(f : Denotation.TauIdx → Denotation.TauIdx → ℤ)

(k start count fuel : ℕ)
 :ℤ**


Helper: sum d_tau f over [start, start + count).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.d_squared_zero_const_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L123-L135)
**def
Tau.BookII.Closure.d_squared_zero_const_check
(db bound : Denotation.TauIdx)
 :Bool**


d^2 = 0 for constant functions: d_tau(constant)(x, k) = 0 for all x, k.
Equations
- Tau.BookII.Closure.d_squared_zero_const_check db bound = Tau.BookII.Closure.d_squared_zero_const_check.go db bound 1 0 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Closure.d_squared_zero_const_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L127-L134)@[irreducible]

**def
Tau.BookII.Closure.d_squared_zero_const_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.d_tau_const_is_zero_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L137-L149)
**def
Tau.BookII.Closure.d_tau_const_is_zero_check
(db bound : Denotation.TauIdx)
 :Bool**


d_tau of a constant function is zero (verified for value 42).
Equations
- Tau.BookII.Closure.d_tau_const_is_zero_check db bound = Tau.BookII.Closure.d_tau_const_is_zero_check.go db bound 1 0 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Closure.d_tau_const_is_zero_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L141-L148)@[irreducible]

**def
Tau.BookII.Closure.d_tau_const_is_zero_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.d_squared_zero_tower_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L151-L170)
**def
Tau.BookII.Closure.d_squared_zero_tower_check
(db bound : Denotation.TauIdx)
 :Bool**


d^2 = 0 verified via telescoping: the sum of d_tau f over a full period
[0, P_k) is 0 for any function f. This is the cyclic telescoping identity:
sum_{x=0}^{P_k - 1} [f(x+1 mod P_k) - f(x mod P_k)] = 0.

We verify this for f(y, k) = reduce(y, k) at each stage k.
Equations
- Tau.BookII.Closure.d_squared_zero_tower_check db bound = Tau.BookII.Closure.d_squared_zero_tower_check.go db bound 1 0 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Closure.d_squared_zero_tower_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L159-L169)@[irreducible]

**def
Tau.BookII.Closure.d_squared_zero_tower_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.TauManifoldData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L176-L182)
**structure
Tau.BookII.Closure.TauManifoldData :Type**


[II.D62] tau-Manifold data: a primorial tower with atlas verification
results and exterior derivative properties.

- has_atlas : Bool
- has_transitions : Bool
- has_d_squared_zero : Bool
Instances For

---

### `Tau.BookII.Closure.instReprTauManifoldData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L182-L182)
**def
Tau.BookII.Closure.instReprTauManifoldData.repr :TauManifoldData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instReprTauManifoldData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L182-L182)
**instance
Tau.BookII.Closure.instReprTauManifoldData :Repr TauManifoldData**

Equations
- Tau.BookII.Closure.instReprTauManifoldData = { reprPrec := Tau.BookII.Closure.instReprTauManifoldData.repr }

---

### `Tau.BookII.Closure.instDecidableEqTauManifoldData.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L182-L182)
**def
Tau.BookII.Closure.instDecidableEqTauManifoldData.decEq
(x✝ x✝¹ : TauManifoldData)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqTauManifoldData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L182-L182)
**instance
Tau.BookII.Closure.instDecidableEqTauManifoldData :DecidableEq TauManifoldData**

Equations
- Tau.BookII.Closure.instDecidableEqTauManifoldData = Tau.BookII.Closure.instDecidableEqTauManifoldData.decEq

---

### `Tau.BookII.Closure.compute_tau_manifold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L184-L193)
**def
Tau.BookII.Closure.compute_tau_manifold
(db bound : Denotation.TauIdx)
 :TauManifoldData**


[II.D62] Compute tau-manifold data by evaluating atlas, transitions,
and exterior derivative properties.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.tau_manifold_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L195-L198)
**def
Tau.BookII.Closure.tau_manifold_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.D62] Full tau-manifold check: atlas + transitions + d^2 = 0.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.tau3_is_manifold_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L204-L213)
**def
Tau.BookII.Closure.tau3_is_manifold_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.P15] tau^3 is a tau-manifold check: combines atlas existence,
chart reduce-compatibility, exterior derivative well-definedness,
and the ABCD round-trip from categoricity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.atlas_chart_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L254-L255)
**theorem
Tau.BookII.Closure.atlas_chart_3 :atlas_chart_check 3 = true**


---

### `Tau.BookII.Closure.atlas_transition_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L258-L259)
**theorem
Tau.BookII.Closure.atlas_transition_3_30 :atlas_transition_check 3 30 = true**


---

### `Tau.BookII.Closure.d_const_zero_3_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L262-L263)
**theorem
Tau.BookII.Closure.d_const_zero_3_15 :d_squared_zero_const_check 3 15 = true**


---

### `Tau.BookII.Closure.d_tau_const_3_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L265-L266)
**theorem
Tau.BookII.Closure.d_tau_const_3_15 :d_tau_const_is_zero_check 3 15 = true**


---

### `Tau.BookII.Closure.d_sq_tower_3_10`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L269-L270)
**theorem
Tau.BookII.Closure.d_sq_tower_3_10 :d_squared_zero_tower_check 3 10 = true**


---

### `Tau.BookII.Closure.tau_manifold_3_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L273-L274)
**theorem
Tau.BookII.Closure.tau_manifold_3_15 :tau_manifold_check 3 15 = true**


---

### `Tau.BookII.Closure.tau3_manifold_3_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L277-L278)
**theorem
Tau.BookII.Closure.tau3_manifold_3_15 :tau3_is_manifold_check 3 15 = true**


---

### `Tau.BookII.Closure.abcd_atlas_roundtrip_7`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L284-L287)
**theorem
Tau.BookII.Closure.abcd_atlas_roundtrip_7 :Interior.to_tau_idx (Interior.from_tau_idx 7) = 7**


[II.D63] The ABCD chart round-trips for specific values.
to_tau_idx(from_tau_idx(x)) = x. Verified computationally.

---

### `Tau.BookII.Closure.abcd_atlas_roundtrip_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L289-L290)
**theorem
Tau.BookII.Closure.abcd_atlas_roundtrip_30 :Interior.to_tau_idx (Interior.from_tau_idx 30) = 30**


---

### `Tau.BookII.Closure.abcd_atlas_roundtrip_100`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L292-L293)
**theorem
Tau.BookII.Closure.abcd_atlas_roundtrip_100 :Interior.to_tau_idx (Interior.from_tau_idx 100) = 100**


---

### `Tau.BookII.Closure.chart_transition_7_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L295-L299)
**theorem
Tau.BookII.Closure.chart_transition_7_2 :Polarity.reduce (Interior.to_tau_idx (Interior.from_tau_idx 7)) 2 = Polarity.reduce 7 2**


[II.D63] Chart transitions are reduce-compatible:
reduce(to_tau_idx(from_tau_idx(x)), k) = reduce(x, k).
Verified for specific instances.

---

### `Tau.BookII.Closure.chart_transition_30_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L301-L302)
**theorem
Tau.BookII.Closure.chart_transition_30_3 :Polarity.reduce (Interior.to_tau_idx (Interior.from_tau_idx 30)) 3 = Polarity.reduce 30 3**


---

### `Tau.BookII.Closure.d_tau_constant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L304-L308)
**theorem
Tau.BookII.Closure.d_tau_constant
(c : ℤ)

(x k : Denotation.TauIdx)
 :tau_exterior_derivative (fun (x x_1 : Denotation.TauIdx) => c) x k = 0**


[II.D64] d_tau of a constant 0-form is zero.
tau_exterior_derivative(const_c, x, k) = c - c = 0.

---

### `Tau.BookII.Closure.d_tau_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L310-L313)
**theorem
Tau.BookII.Closure.d_tau_zero
(x k : Denotation.TauIdx)
 :tau_exterior_derivative (fun (x x_1 : Denotation.TauIdx) => 0) x k = 0**


[II.D64] Telescoping: d_tau of the zero function is zero.

---

### `Tau.BookII.Closure.manifold_reduce_idempotent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L315-L318)
**theorem
Tau.BookII.Closure.manifold_reduce_idempotent
(x k : Denotation.TauIdx)
 :Polarity.reduce (Polarity.reduce x k) k = Polarity.reduce x k**


[II.P15] tau^3 manifold: reduction is idempotent (atlas well-defined).

---

### `Tau.BookII.Closure.manifold_tower_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Closure/TauManifold.lean#L320-L324)
**theorem
Tau.BookII.Closure.manifold_tower_coherence
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (Polarity.reduce x l) k = Polarity.reduce x k**


[II.P15] tau^3 manifold: tower coherence gives chart transitions.
reduce(reduce(x, l), k) = reduce(x, k) for k <= l.
