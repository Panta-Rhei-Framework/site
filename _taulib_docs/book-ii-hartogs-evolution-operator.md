---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.EvolutionOperator"
permalink: /verify/taulib/docs/book-ii-hartogs-evolution-operator/
lane: verify
module_name: "TauLib.BookII.Hartogs.EvolutionOperator"
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

# TauLib.BookII.Hartogs.EvolutionOperator


The evolution operator E_{n->m} and the causal arrow from B/C asymmetry.

## Registry Cross-References


- [II.D37] Evolution Operator -- `evolution_op`, `evolution_semigroup_check`

- [II.D38] Causal Arrow -- `causal_arrow`, `bc_asymmetry_check`

- [II.T28] Evolution Semigroup -- `evolution_semigroup_thm`


## Mathematical Content


The evolution operator E_{n->m} maps a point x at stage n to its image at
stage m by composing successive BndLifts:

E_{n->m}(x) = BndLift_{m-1} . ... . BndLift_n(x) = reduce(x, m)

This is well-defined because each BndLift is a reduction map, and their
composition telescopes to a single reduction: reduce(x, m).

**Semigroup property (II.T28):**
E_{m->l} . E_{n->m} = E_{n->l}
i.e., reduce(reduce(x, m), n) = reduce(x, n) for n <= m

This is exactly tower coherence (the inverse system compatibility condition).

**Identity property:**
E_{n->n}(x) = reduce(reduce(x, n), n) = reduce(x, n)
i.e., double reduction is idempotent.

**Causal arrow (II.D38):**
The direction of increasing stage number is physically meaningful: it
corresponds to passing from coarser to finer primorial resolution.
The B-channel (exponent, gamma-orbit) and C-channel (tetration, eta-orbit)
grow at different rates as stages increase, breaking time-reversal
symmetry and selecting a preferred direction.

This B/C asymmetry is the categorical origin of the arrow of time:
tetration (C) grows faster than exponentiation (B) for the same base,
so the C-channel eventually dominates, selecting the e_minus-lobe of
the lemniscate as the "future."

---

### `Tau.BookII.Hartogs.evolution_op`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L56-L66)
**def
Tau.BookII.Hartogs.evolution_op
(x _n m : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D37] The evolution operator E_{n->m}:
maps a point x from stage n context to stage m.
Defined as reduce(x, m), the canonical projection to Z/M_m Z.

When n <= m, this is "refinement" (going to a coarser stage).
When n >= m, this is "extension" (compatible with bndlift).

The key insight: the entire tower of BndLifts telescopes to
a single reduce.
Equations
- Tau.BookII.Hartogs.evolution_op x _n m = Tau.Polarity.reduce x m
Instances For

---

### `Tau.BookII.Hartogs.evolution_id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L68-L70)
**def
Tau.BookII.Hartogs.evolution_id
(x n : Denotation.TauIdx)
 :Denotation.TauIdx**


Evolution at the same stage: just reduce.
Equations
- Tau.BookII.Hartogs.evolution_id x n = Tau.BookII.Hartogs.evolution_op x n n
Instances For

---

### `Tau.BookII.Hartogs.evolution_semigroup_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L76-L96)
**def
Tau.BookII.Hartogs.evolution_semigroup_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T28] Evolution semigroup check:
E_{m->l} . E_{n->m} = E_{n->l}
i.e., reduce(reduce(x, m), n) = reduce(x, n) for n <= m.

This is the tower coherence condition expressed as a semigroup law.
The evolution operators form a semigroup under composition,
indexed by the primorial stage numbers.
Equations
- Tau.BookII.Hartogs.evolution_semigroup_check bound db = Tau.BookII.Hartogs.evolution_semigroup_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.evolution_semigroup_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L86-L95)@[irreducible]

**def
Tau.BookII.Hartogs.evolution_semigroup_check.go
(bound db : Denotation.TauIdx)

(x n m fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.evolution_identity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L98-L112)
**def
Tau.BookII.Hartogs.evolution_identity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T28] Evolution identity check:
E_{n->n} is idempotent: reduce(reduce(x, n), n) = reduce(x, n).
Double reduction at the same stage does not change the value.
Equations
- Tau.BookII.Hartogs.evolution_identity_check bound db = Tau.BookII.Hartogs.evolution_identity_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.evolution_identity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L104-L111)@[irreducible]

**def
Tau.BookII.Hartogs.evolution_identity_check.go
(bound db : Denotation.TauIdx)

(x n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.evolution_composition_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L114-L133)
**def
Tau.BookII.Hartogs.evolution_composition_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T28] Evolution composition check:
Composing two evolution steps equals a single evolution step.
For n <= m <= l: E_{n->m}(E_{m->l}(x)) = E_{n->l}(x).
i.e., reduce(reduce(x, l), m) = reduce(x, m) when m <= l.
Equations
- Tau.BookII.Hartogs.evolution_composition_check bound db = Tau.BookII.Hartogs.evolution_composition_check.go bound db 2 1 1 1 ((bound + 1) * (db + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.evolution_composition_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L121-L132)@[irreducible]

**def
Tau.BookII.Hartogs.evolution_composition_check.go
(bound db : Denotation.TauIdx)

(x n m l fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.evolution_semigroup_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L139-L145)
**theorem
Tau.BookII.Hartogs.evolution_semigroup_thm
(x : Denotation.TauIdx)

{n m : Denotation.TauIdx}

(h : n ≤ m)
 :evolution_op (evolution_op x m m) m n = evolution_op x m n**


[II.T28] Evolution semigroup theorem (formal):
reduce(reduce(x, m), n) = reduce(x, n) for n <= m.
This is a direct corollary of reduction_compat from ModArith.

---

### `Tau.BookII.Hartogs.evolution_identity_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L147-L151)
**theorem
Tau.BookII.Hartogs.evolution_identity_thm
(x n : Denotation.TauIdx)
 :Polarity.reduce (Polarity.reduce x n) n = Polarity.reduce x n**


Evolution identity theorem (formal):
reduce(reduce(x, n), n) = reduce(x, n).

---

### `Tau.BookII.Hartogs.evolution_composition_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L153-L158)
**theorem
Tau.BookII.Hartogs.evolution_composition_thm
(x : Denotation.TauIdx)

{m l : Denotation.TauIdx}

(h : m ≤ l)
 :Polarity.reduce (evolution_op x l l) m = evolution_op x l m**


Evolution composition theorem (formal):
For m <= l, reduce(reduce(x, l), m) = reduce(x, m).

---

### `Tau.BookII.Hartogs.causal_arrow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L164-L180)
**def
Tau.BookII.Hartogs.causal_arrow
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D38] The causal arrow: a direction determined by B/C asymmetry.

For a point x, we compare how the B-coordinate and C-coordinate
change across stages. The B-coordinate (exponent, gamma-orbit)
grows polynomially, while the C-coordinate (tetration, eta-orbit)
grows hyper-exponentially. This asymmetry selects a preferred
direction: forward = increasing stage number.

Returns:


- 1 if B grows faster at this sample (B-dominant direction)

- 2 if C grows faster at this sample (C-dominant direction)

- 0 if they grow at the same rate (balanced)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bc_asymmetry_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L186-L206)
**def
Tau.BookII.Hartogs.bc_asymmetry_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D38] B/C growth rate comparison at powers of 2.
For the canonical base a=2, compare B and C coordinates of 2^n.
As n increases, B (exponent) grows linearly while C (tetration)
stays bounded. For powers of prime: x = p^n has B = n, C = 1.

This shows: in the "exponential direction," B dominates.
The complementary "tetration direction" (a ↑↑ n) has C dominating.
The asymmetry between the two rates is fundamental.
Equations
- Tau.BookII.Hartogs.bc_asymmetry_check bound = Tau.BookII.Hartogs.bc_asymmetry_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.bc_asymmetry_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L197-L205)@[irreducible]

**def
Tau.BookII.Hartogs.bc_asymmetry_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bc_asymmetry_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L208-L219)
**def
Tau.BookII.Hartogs.bc_asymmetry_witness :Bool**


[II.D38] B/C asymmetry witness: exhibit specific points where B != C.
Greedy peel prefers tetration, so from_tau_idx 4 = (2,1,2,1):
A=2, B=1, C=2, D=1 → C-dominant.
from_tau_idx 64 = (2,3,2,1): A=2, B=3, C=2, D=1 → B-dominant.
This demonstrates that both directions (B-dominant and C-dominant) exist.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.causal_arrow_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L221-L234)
**def
Tau.BookII.Hartogs.causal_arrow_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D38] Causal arrow check: the causal arrow is well-defined
for all points in [2, bound]. Every point receives a direction.
Equations
- Tau.BookII.Hartogs.causal_arrow_check bound = Tau.BookII.Hartogs.causal_arrow_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.causal_arrow_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L226-L233)@[irreducible]

**def
Tau.BookII.Hartogs.causal_arrow_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.causal_nontrivial_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L236-L253)
**def
Tau.BookII.Hartogs.causal_nontrivial_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D38] B/C asymmetry is non-trivial: not all points are balanced.
There exist both B-dominant and C-dominant points in [2, bound].
This is the categorical origin of the arrow of time.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.causal_nontrivial_check.has_b_dom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L242-L246)@[irreducible]

**def
Tau.BookII.Hartogs.causal_nontrivial_check.has_b_dom
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.causal_nontrivial_check.has_c_dom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L248-L252)@[irreducible]

**def
Tau.BookII.Hartogs.causal_nontrivial_check.has_c_dom
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_evolution_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L259-L268)
**def
Tau.BookII.Hartogs.full_evolution_check
(bound db : Denotation.TauIdx)
 :Bool**


Combined check: evolution semigroup + causal arrow.
The evolution semigroup provides the dynamics; the causal arrow
provides the direction. Together they give the full Hartogs
evolution structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.semigroup_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L312-L313)
**theorem
Tau.BookII.Hartogs.semigroup_12_4 :evolution_semigroup_check 12 4 = true**


---

### `Tau.BookII.Hartogs.identity_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L315-L316)
**theorem
Tau.BookII.Hartogs.identity_12_4 :evolution_identity_check 12 4 = true**


---

### `Tau.BookII.Hartogs.composition_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L318-L319)
**theorem
Tau.BookII.Hartogs.composition_8_3 :evolution_composition_check 8 3 = true**


---

### `Tau.BookII.Hartogs.asymmetry_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L322-L323)
**theorem
Tau.BookII.Hartogs.asymmetry_witness :bc_asymmetry_witness = true**


---

### `Tau.BookII.Hartogs.asymmetry_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L325-L326)
**theorem
Tau.BookII.Hartogs.asymmetry_15 :bc_asymmetry_check 15 = true**


---

### `Tau.BookII.Hartogs.causal_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L328-L329)
**theorem
Tau.BookII.Hartogs.causal_15 :causal_arrow_check 15 = true**


---

### `Tau.BookII.Hartogs.causal_nontrivial_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L331-L332)
**theorem
Tau.BookII.Hartogs.causal_nontrivial_20 :causal_nontrivial_check 20 = true**


---

### `Tau.BookII.Hartogs.full_evolution_10_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/EvolutionOperator.lean#L335-L336)
**theorem
Tau.BookII.Hartogs.full_evolution_10_4 :full_evolution_check 10 4 = true**
