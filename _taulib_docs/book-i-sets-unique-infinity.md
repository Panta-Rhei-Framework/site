---
layout: taulib-doc
title: "TauLib.BookI.Sets.UniqueInfinity"
permalink: /verify/taulib/docs/book-i-sets-unique-infinity/
lane: verify
module_name: "TauLib.BookI.Sets.UniqueInfinity"
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

# TauLib.Sets.UniqueInfinity


The Unique Infinity Object theorem: omega is the sole infinity, and
omega-germs with their ultrametric structure replace the cardinality hierarchy.

## Registry Cross-References


- [I.D76] Omega-Germ Approach -- `OmegaGermApproach`

- [I.T36] Unique Infinity Object -- `unique_infinity`

- [I.P37] Ultrametric Replaces Cardinality -- `ultrametric_replaces_card`


## Ground Truth Sources


- Part IX "The Cantor Mirage": With the diagonal argument blocked,
the cardinality hierarchy collapses to a single infinity.


## Mathematical Content


In ZF set theory, the Axiom of Infinity produces aleph_0, and then the
powerset axiom + diagonal argument produce aleph_1, aleph_2, ... --
an infinite hierarchy of cardinals.

In Category tau:


- K2 (omega fixed point) provides exactly ONE infinity object: omega

- K5 (beacon non-successor) makes omega unreachable from any orbit ray

- K6 (object closure) seals the universe: Obj(tau) = 4 orbits + {omega}

- The diagonal argument is inapplicable (I.T35)


Therefore: omega is the UNIQUE infinity object. There is no second
infinity, no aleph_1, no continuum hypothesis. The cardinality hierarchy
is replaced by a METRIC structure: the divergence ultrametric on
omega-germs (compatible towers on the primorial ladder).

Omega-germs form an inverse limit of finite rings Z/M_kZ. The
convergence mechanism is: a sequence of naturals (n_i) converges if
their omega-tails agree to ever-deeper depths. This is NOT a cardinality
notion but a proximity notion -- qualitative, not quantitative.

---

### `Tau.Sets.OmegaGermApproach`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L51-L68)
**structure
Tau.Sets.OmegaGermApproach :Prop**


[I.D76] The Omega-Germ Approach: omega-germs are compatible towers
on the primorial ladder, equipped with the divergence ultrametric.
This replaces "set of all reals" with "inverse limit of finite rings."

The approach has three components:

- The primorial ladder M_1 | M_2 | M_3 | ... provides the tower

- Reduction maps pi_{l->k} : Z/M_l -> Z/M_k give compatibility

- The divergence ultrametric measures agreement depth


- ladder_positive
(k : Denotation.TauIdx)
 : Polarity.primorial k > 0
The primorial ladder is well-defined: M_k > 0 for all k

- ladder_divisible
(k l : Denotation.TauIdx)
 : k ≤ l → Polarity.primorial k ∣ Polarity.primorial l
The ladder is divisible: M_k | M_l for k <= l

- reduction_compatible
(x k l : Denotation.TauIdx)
 : k ≤ l → Polarity.reduce (Polarity.reduce x l) k = Polarity.reduce x k
Reduction maps compose: (x mod M_l) mod M_k = x mod M_k for k <= l

- ultra_sym
(t1 t2 : Polarity.OmegaTail)
 : Polarity.ultra_dist t1 t2 = Polarity.ultra_dist t2 t1
The ultrametric is symmetric

Instances For

---

### `Tau.Sets.omega_germ_approach`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L70-L75)
**def
Tau.Sets.omega_germ_approach :OmegaGermApproach**


Construct the omega-germ approach from established lemmas.
Equations
- Tau.Sets.omega_germ_approach = ⋯
Instances For

---

### `Tau.Sets.InfinityObject`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L81-L89)
**structure
Tau.Sets.InfinityObject
(x : Kernel.TauObj)
 :Prop**


An "infinity object" in tau is an object that is a fixed point
of rho (absorbs iteration) and is unreachable from orbit rays.
These are precisely the defining properties of omega (K2 + K5).

- rho_fixed : Kernel.rho x = x
Fixed under rho: rho(x) = x

- unreachable
(g : Kernel.Generator)
 : g ≠ Kernel.Generator.omega → ∀ (n : ℕ), Orbit.iter_rho n (Kernel.TauObj.ofGen g) ≠ x
Unreachable from every non-omega orbit

Instances For

---

### `Tau.Sets.omega_rho_fixed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L91-L93)
**theorem
Tau.Sets.omega_rho_fixed
(d : ℕ)
 :Kernel.rho { seed := Kernel.Generator.omega, depth := d } = { seed := Kernel.Generator.omega, depth := d }**


Omega (with any depth) is a fixed point of rho.

---

### `Tau.Sets.omega_is_infinity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L95-L101)
**def
Tau.Sets.omega_is_infinity :InfinityObject Orbit.omega_obj**


The canonical omega object is an infinity object.
Equations
- Tau.Sets.omega_is_infinity = ⋯
Instances For

---

### `Tau.Sets.unique_infinity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L103-L140)
**theorem
Tau.Sets.unique_infinity
(x : Kernel.TauObj)

(hx : InfinityObject x)
 :x.seed = Kernel.Generator.omega**


[I.T36] Unique Infinity Object: omega is the ONLY infinity object
in Category tau.

Proof: Let x be any infinity object. Since rho(x) = x and x is
unreachable from orbit rays, x must have seed = omega (by K6
object closure, the only objects not in orbit rays have seed omega).
Then x = (omega, d) for some d. Since rho(omega, d) = (omega, d)
(K2), ANY omega-seeded object is rho-fixed.

But the uniqueness is stronger: all (omega, d) are rho-equivalent
(they all satisfy rho(x) = x), so up to rho-equivalence there is
exactly one infinity object.

---

### `Tau.Sets.infinity_in_omega_fiber`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L142-L145)
**theorem
Tau.Sets.infinity_in_omega_fiber
(x : Kernel.TauObj)

(hx : InfinityObject x)
 :Orbit.OmegaFiber x**


Corollary: every infinity object is in the omega fiber.

---

### `Tau.Sets.no_orbit_infinity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L147-L153)
**theorem
Tau.Sets.no_orbit_infinity
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : ℕ)
 :¬InfinityObject { seed := g, depth := n }**


Corollary: no non-omega generator produces an infinity object.

---

### `Tau.Sets.ultrametric_replaces_card`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L159-L187)
**theorem
Tau.Sets.ultrametric_replaces_card :(∀ (t1 t2 : Polarity.OmegaTail), Polarity.ultra_dist t1 t2 = Polarity.ultra_dist t2 t1) ∧ (∀ (t1 t2 t3 : Polarity.OmegaTail),
 t1.depth = t2.depth →
 t1.depth = t3.depth →
 Polarity.ultra_dist t1 t3 = 0 ∨ Polarity.ultra_dist t1 t3 ≥ Nat.min (Polarity.ultra_dist t1 t2) (Polarity.ultra_dist t2 t3)) ∧ ∀ (x : Kernel.TauObj), InfinityObject x → x.seed = Kernel.Generator.omega**


[I.P37] Ultrametric structure replaces cardinality hierarchy.

In ZF, the chain aleph_0 < aleph_1 < aleph_2 < ... measures
"how many" elements a set has. In tau, this hierarchy collapses:
there is only one infinity (omega), and the notion of "size" is
replaced by PROXIMITY in the divergence ultrametric.

Two omega-tails are "close" if they agree to deep primorial depth,
and "far" if they diverge early. This is an ultrametric (satisfies
the strong triangle inequality), providing a finer structure than
cardinality.

The replacement has three pillars:

- The ultrametric exists (from OmegaGerms)

- It satisfies the strong triangle inequality (ultra_triangle)

- There is no second infinity to compare against (unique_infinity)


We package these as a single theorem.

---

### `Tau.Sets.GermConvergence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L193-L199)
**def
Tau.Sets.GermConvergence
(seq : ℕ → Denotation.TauIdx)

(d : ℕ)
 :Prop**


Germ convergence: a sequence (n_i) of naturals "converges" if
their omega-tails agree to ever-deeper primorial depths.
Formally: for every depth d, there exists N such that for all
i, j >= N, the tails of n_i and n_j at depth d are identical.
Equations
- Tau.Sets.GermConvergence seq d = ∃ (N : ℕ), ∀ (i j : ℕ),
 i ≥ N → j ≥ N → ∀ (k : ℕ), k < d → Tau.Polarity.reduce (seq i) (k + 1) = Tau.Polarity.reduce (seq j) (k + 1)
Instances For

---

### `Tau.Sets.const_seq_converges`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L201-L204)
**theorem
Tau.Sets.const_seq_converges
(c : Denotation.TauIdx)

(d : ℕ)
 :GermConvergence (fun (x : ℕ) => c) d**


Constant sequences converge at every depth.

---

### `Tau.Sets.germ_convergence_via_reduction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L206-L221)
**theorem
Tau.Sets.germ_convergence_via_reduction
(seq : ℕ → Denotation.TauIdx)

(d : ℕ)

(_hd : d ≥ 1)

(h : ∃ (N : ℕ), ∀ (i j : ℕ), i ≥ N → j ≥ N → Polarity.reduce (seq i) d = Polarity.reduce (seq j) d)
 :GermConvergence seq d**


The convergence mechanism is via primorial reduction maps:
convergence at depth d means agreement modulo M_d.

---

### `Tau.Sets.cardinality_hierarchy_collapse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Sets/UniqueInfinity.lean#L227-L240)
**theorem
Tau.Sets.cardinality_hierarchy_collapse :(∀ (x y : Kernel.TauObj), InfinityObject x → InfinityObject y → x.seed = y.seed) ∧ (∃ (f : Kernel.TauObj → ℕ), Function.Injective f) ∧ ¬∃ (x : CantorDiagonalApparatus), True**


The cardinality hierarchy collapses: since omega is the unique infinity
and the diagonal argument is inapplicable, there is exactly one
infinite cardinal in tau (witnessed by the countable object set).
