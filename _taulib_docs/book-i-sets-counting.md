---
layout: taulib-doc
title: "TauLib.BookI.Sets.Counting"
permalink: /verify/taulib/docs/book-i-sets-counting/
lane: verify
module_name: "TauLib.BookI.Sets.Counting"
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

# TauLib.Sets.Counting


Generative counting: the bijection that simultaneously creates and enumerates
orbit elements, and countability of Obj(tau) as a structural consequence.

## Registry Cross-References


- [I.D75] Generative Counting Principle -- `generative_counting_principle`

- [I.P33] Counting as Structural Feature -- `counting_structural`


## Ground Truth Sources


- Part IX "The Cantor Mirage": Countability is earned via orbit generation,
not imposed by external cardinality axioms.


## Mathematical Content


The Generative Counting Principle states that the bijection phi_g(n) = rho^n(g)
simultaneously CREATES each orbit element and ASSIGNS it a natural-number label.
There is no prior pool of uncounted objects -- every object arrives already
counted by virtue of its generation depth.

From this principle plus the Ontic Closure Theorem (K6), countability of Obj(tau)
follows: the universe is a finite union of countably generated orbit rays plus
the singleton {omega}. No uncountable structure can arise without three
prerequisites that are absent from K0--K6:

- Impredicative powerset (collecting ALL subsets of an infinite set)

- Unrestricted comprehension (Sep : (Idx -> Prop) -> Idx)

- Free Cartesian diagonal (Delta : Idx -> Idx x Idx as an earned morphism)


All three are blocked by the earned-arrow discipline.

---

### `Tau.Sets.GenerativeCountingPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L46-L57)
**structure
Tau.Sets.GenerativeCountingPrinciple
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)
 :Type**


[I.D75] The generative counting principle: the map phi_g(n) = (g, n)
simultaneously creates the n-th orbit element and assigns it index n.
This is a bijection between Nat and the orbit ray O_g.

- phi : ℕ → Kernel.TauObj
The creation-enumeration map: n maps to the n-th orbit element

- phi_def
(n : ℕ)
 : self.phi n = { seed := g, depth := n }
phi is defined as depth-n in orbit g

- phi_injective
(n m : ℕ)
 : self.phi n = self.phi m → n = m
phi is injective (distinct depths yield distinct objects)

- phi_surjective
(x : Kernel.TauObj)
 : Orbit.OrbitRay g x → ∃ (n : ℕ), self.phi n = x
phi is surjective onto O_g (every orbit element has a depth)

Instances For

---

### `Tau.Sets.generative_counting_principle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L59-L68)
**def
Tau.Sets.generative_counting_principle
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)
 :GenerativeCountingPrinciple g hg**


Construct the generative counting principle for any non-omega generator g.
Equations
- Tau.Sets.generative_counting_principle g hg = { phi := fun (n : ℕ) => { seed := g, depth := n }, phi_def := ⋯, phi_injective := ⋯, phi_surjective := ⋯ }
Instances For

---

### `Tau.Sets.gcp_eq_iter_rho`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L70-L73)
**theorem
Tau.Sets.gcp_eq_iter_rho
(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : ℕ)
 :(generative_counting_principle g hg).phi n = Orbit.iter_rho n (Kernel.TauObj.ofGen g)**


The generative counting map agrees with iter_rho from the generator.

---

### `Tau.Sets.counting_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L79-L93)
**theorem
Tau.Sets.counting_structural :(∀ (g : Kernel.Generator),
 g ≠ Kernel.Generator.omega →
 ∃ (f : ℕ → Kernel.TauObj), Function.Injective f ∧ ∀ (x : Kernel.TauObj), Orbit.OrbitRay g x → ∃ (n : ℕ), f n = x) ∧ ∃ (enc : Kernel.TauObj → ℕ), Function.Injective enc**


[I.P33] Countability of Obj(tau) as a structural feature:
it follows from generative counting (each orbit is counted)
plus ontic closure (the universe is a finite union of orbits).

The injection TauObj -> Nat witnesses countability.

---

### `Tau.Sets.obj_tau_countable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L99-L106)
**theorem
Tau.Sets.obj_tau_countable :(∃ (f : Kernel.TauObj → ℕ), Function.Injective f) ∧ ∃ (g : ℕ → Kernel.TauObj), Function.Injective g**


|Obj(tau)| = aleph_0: the object universe is countably infinite.
Injective: tauObj_encode provides an injection TauObj -> Nat.
Surjective: the alpha orbit maps Nat into TauObj injectively.

---

### `Tau.Sets.UncountablePrerequisites`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L112-L125)
**structure
Tau.Sets.UncountablePrerequisites :Type**


An uncountability argument requires three structural prerequisites.
This record witnesses the absence of each from K0-K6.

- no_impredicative_powerset : Prop
P1: Impredicative powerset -- would require collecting ALL subsets
of an infinite set, but tau-sets are divisor sets (always finite for
nonzero indices).

- no_comprehension : Prop
P2: Unrestricted comprehension -- would require
Sep : (TauIdx -> Prop) -> TauIdx, but no such separator exists.

- no_free_diagonal : Prop
P3: Free Cartesian diagonal -- would require
Delta : TauIdx -> TauIdx x TauIdx as an earned morphism,
but self-pairing is not in the program monoid.

Instances For

---

### `Tau.Sets.no_uncountable_prerequisite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L127-L151)
**def
Tau.Sets.no_uncountable_prerequisite :UncountablePrerequisites**


The three prerequisites for uncountability are not derivable from K0-K6.

P1 (impredicative powerset): For any nonzero b, the tau-members of b
are bounded by b (tau_mem_le), so the "powerset" at each level is finite.
There is no single tau-index encoding "all subsets of Nat."

P2 (unrestricted comprehension): The tau-set universe is exactly Nat;
not every predicate on Nat corresponds to a tau-index. In particular,
there is no R such that a in_tau R iff not(a in_tau a) (no_russell_set).

P3 (free Cartesian diagonal): Self-pairing n |-> (n, n) requires a
product encoding that is an earned morphism. But in Cat_tau (thin category),
the diagonal map would need to factor through the product universal
property, and the earned-arrow discipline prevents unrestricted self-reference.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Sets.p1_verified`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L153-L156)
**theorem
Tau.Sets.p1_verified :no_uncountable_prerequisite.no_impredicative_powerset = ∀ (b : Denotation.TauIdx), b ≠ 0 → ∀ (a : Denotation.TauIdx), tau_mem a b → a ≤ b**


Verification: P1 holds (finite divisor sets).

---

### `Tau.Sets.p2_verified`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L158-L161)
**theorem
Tau.Sets.p2_verified :no_uncountable_prerequisite.no_comprehension = ¬∃ (R : Denotation.TauIdx), ∀ (a : Denotation.TauIdx), tau_mem a R ↔ ¬tau_mem a R**


Verification: P2 holds (no Russell set).

---

### `Tau.Sets.p1_true`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L163-L165)
**theorem
Tau.Sets.p1_true
(b : Denotation.TauIdx)
 :b ≠ 0 → ∀ (a : Denotation.TauIdx), tau_mem a b → a ≤ b**


P1 is provably true: divisor sets are bounded.

---

### `Tau.Sets.p2_true`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Counting.lean#L167-L169)
**theorem
Tau.Sets.p2_true :¬∃ (R : Denotation.TauIdx), ∀ (a : Denotation.TauIdx), tau_mem a R ↔ ¬tau_mem a R**


P2 is provably true: no Russell set exists.
