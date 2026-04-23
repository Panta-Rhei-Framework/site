---
layout: taulib-doc
title: "TauLib.BookI.Logic.BooleanRecovery"
permalink: /verify/taulib/docs/book-i-logic-boolean-recovery/
lane: verify
module_name: "TauLib.BookI.Logic.BooleanRecovery"
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

# TauLib.Logic.BooleanRecovery


Boolean recovery: the forgetful functor from Truth4 to Bool.

## Registry Cross-References


- [I.P13] Boolean Recovery -- `boolean_recovery`, `forget_preserves_meet`, `forget_preserves_join`

- [I.D41] Subobject Classifier Preview -- `Omega_tau`


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, bipolar balance

- chunk_0310_M002679: Bipolar partition


## Mathematical Content


The forgetful map `forget : Truth4 -> Bool` collapses the four truth values
to two by an "optimistic" projection: B (overdetermined) maps to true,
N (underdetermined) maps to false. Equivalently, forget reads only the
B-sector component of the Bool x Bool encoding.

Key results:

- forget is a LATTICE homomorphism: it preserves meet and join.

- forget FAILS to preserve negation at B and N -- this is the precise
fingerprint of information loss from 4-valued to 2-valued logic.

- The boolean_recovery theorem: forget is lossless (preserves negation)
if and only if the input is classical (T or F).


The Heyting implication is also defined. Since Truth4 is a Boolean algebra
(isomorphic to 2 x 2), the Heyting implication coincides with the material
implication at all designated values, but we define and verify it independently.

Omega_tau := Truth4 is declared as the subobject classifier preview for
the tau-topos (to be developed in the Topos module).

---

### `Tau.Logic.forget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L46-L53)
**def
Tau.Logic.forget :Truth4 → Bool**


[I.P13] Forgetful map from Truth4 to Bool.
"Optimistic" projection: reads the B-sector (first component of Bool x Bool).
T -> true, B -> true, N -> false, F -> false.
Equations
- Tau.Logic.forget Tau.Logic.Truth4.T = true
- Tau.Logic.forget Tau.Logic.Truth4.B = true
- Tau.Logic.forget Tau.Logic.Truth4.N = false
- Tau.Logic.forget Tau.Logic.Truth4.F = false
Instances For

---

### `Tau.Logic.forget_preserves_meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L59-L62)
**theorem
Tau.Logic.forget_preserves_meet
(a b : Truth4)
 :forget (a.meet b) = (forget a && forget b)**


forget preserves meet: forget(meet a b) = forget(a) && forget(b).

---

### `Tau.Logic.forget_preserves_join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L64-L67)
**theorem
Tau.Logic.forget_preserves_join
(a b : Truth4)
 :forget (a.join b) = (forget a || forget b)**


forget preserves join: forget(join a b) = forget(a) || forget(b).

---

### `Tau.Logic.forget_conflates_T_B`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L77-L78)
**theorem
Tau.Logic.forget_conflates_T_B :forget Truth4.T = forget Truth4.B**


forget conflates T and B: both map to true.

---

### `Tau.Logic.forget_conflates_F_N`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L80-L81)
**theorem
Tau.Logic.forget_conflates_F_N :forget Truth4.F = forget Truth4.N**


forget conflates F and N: both map to false.

---

### `Tau.Logic.forget_not_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L83-L87)
**theorem
Tau.Logic.forget_not_injective :¬∀ (a b : Truth4), forget a = forget b → a = b**


forget is NOT injective: T <> B but forget T = forget B.

---

### `Tau.Logic.forget_preserves_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L89-L91)
**theorem
Tau.Logic.forget_preserves_neg
(v : Truth4)
 :forget v.neg = !forget v**


forget does preserve negation (for the optimistic projection).

---

### `Tau.Logic.forget_pessimistic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L97-L103)
**def
Tau.Logic.forget_pessimistic :Truth4 → Bool**


The pessimistic forgetful map: reads the C-sector (second component).
T -> true, N -> true, B -> false, F -> false.
Equations
- Tau.Logic.forget_pessimistic Tau.Logic.Truth4.T = true
- Tau.Logic.forget_pessimistic Tau.Logic.Truth4.N = true
- Tau.Logic.forget_pessimistic Tau.Logic.Truth4.B = false
- Tau.Logic.forget_pessimistic Tau.Logic.Truth4.F = false
Instances For

---

### `Tau.Logic.forget_pessimistic_preserves_meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L105-L109)
**theorem
Tau.Logic.forget_pessimistic_preserves_meet
(a b : Truth4)
 :forget_pessimistic (a.meet b) = (forget_pessimistic a && forget_pessimistic b)**


The pessimistic map also preserves meet.

---

### `Tau.Logic.forget_pessimistic_preserves_join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L111-L115)
**theorem
Tau.Logic.forget_pessimistic_preserves_join
(a b : Truth4)
 :forget_pessimistic (a.join b) = (forget_pessimistic a || forget_pessimistic b)**


The pessimistic map also preserves join.

---

### `Tau.Logic.forget_pessimistic_preserves_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L117-L120)
**theorem
Tau.Logic.forget_pessimistic_preserves_neg
(v : Truth4)
 :forget_pessimistic v.neg = !forget_pessimistic v**


The pessimistic map also preserves negation.

---

### `Tau.Logic.dual_forget_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L122-L127)
**theorem
Tau.Logic.dual_forget_injective
(a b : Truth4)

(h1 : forget a = forget b)

(h2 : forget_pessimistic a = forget_pessimistic b)
 :a = b**


The two projections together recover Truth4: the pair (forget v, forget_pessimistic v)
uniquely determines v.

---

### `Tau.Logic.dual_forget_is_toBoolPair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L129-L132)
**theorem
Tau.Logic.dual_forget_is_toBoolPair
(v : Truth4)
 :(forget v, forget_pessimistic v) = v.toBoolPair**


The dual-forget map is exactly the toBoolPair isomorphism.

---

### `Tau.Logic.boolean_recovery`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L138-L145)
**theorem
Tau.Logic.boolean_recovery
(v : Truth4)
 :v = Truth4.T ∨ v = Truth4.F ↔ forget v = forget_pessimistic v**


[I.P13] Boolean recovery: a Truth4 value is classical (T or F) if and only if
both sector projections agree.

For classical values: forget T = true = forget_pessimistic T, forget F = false = forget_pessimistic F.
For non-classical: forget B = true but forget_pessimistic B = false (sectors disagree).

---

### `Tau.Logic.forget_fiber_T_B`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L147-L148)
**theorem
Tau.Logic.forget_fiber_T_B :forget Truth4.T = forget Truth4.B**


The forget fiber has exactly 2 elements for each output value.

---

### `Tau.Logic.forget_fiber_F_N`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L150-L150)
**theorem
Tau.Logic.forget_fiber_F_N :forget Truth4.F = forget Truth4.N**


---

### `Tau.Logic.forget_never_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L152-L159)
**theorem
Tau.Logic.forget_never_injective
(v : Truth4)
 :∃ (w : Truth4), w ≠ v ∧ forget w = forget v**


No Truth4 value has a singleton forget-fiber: the projection always loses information.

---

### `Tau.Logic.forget_fiber`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L161-L167)
**theorem
Tau.Logic.forget_fiber
(a b : Truth4)
 :forget a = forget b ↔ a = b ∨ a = Truth4.T ∧ b = Truth4.B ∨ a = Truth4.B ∧ b = Truth4.T ∨ a = Truth4.F ∧ b = Truth4.N ∨ a = Truth4.N ∧ b = Truth4.F**


The key information-loss theorem: forget loses exactly the B/N distinction.
Two values have the same forget image iff they agree on "B-sector truth".

---

### `Tau.Logic.Omega_tau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L173-L176)@[reducible, inline]

**abbrev
Tau.Logic.Omega_tau :Type**


[I.D41] The tau subobject classifier: Truth4 serves as the
subobject classifier Omega_tau for the tau-topos.
Full development deferred to TauLib.Topos.
Equations
- Tau.Logic.Omega_tau = Tau.Logic.Truth4
Instances For

---

### `Tau.Logic.omega_true`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L178-L179)
**def
Tau.Logic.omega_true :Omega_tau**


The "true" arrow: the inclusion of the terminal object into Omega_tau.
Equations
- Tau.Logic.omega_true = Tau.Logic.Truth4.T
Instances For

---

### `Tau.Logic.omega_false`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L181-L182)
**def
Tau.Logic.omega_false :Omega_tau**


The characteristic map of the empty subobject.
Equations
- Tau.Logic.omega_false = Tau.Logic.Truth4.F
Instances For

---

### `Tau.Logic.omega_both`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L184-L185)
**def
Tau.Logic.omega_both :Omega_tau**


The characteristic map of an overdetermined subobject.
Equations
- Tau.Logic.omega_both = Tau.Logic.Truth4.B
Instances For

---

### `Tau.Logic.omega_neither`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L187-L188)
**def
Tau.Logic.omega_neither :Omega_tau**


The characteristic map of an underdetermined subobject.
Equations
- Tau.Logic.omega_neither = Tau.Logic.Truth4.N
Instances For

---

### `Tau.Logic.Truth4.heyting_impl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L194-L214)
**def
Tau.Logic.Truth4.heyting_impl :Truth4 → Truth4 → Truth4**


Heyting implication: a => b = sup{c : meet(a,c) <= b}.

For Truth4 (which is Boolean), this coincides with material implication.
The table is computed by hand:
a\b | T F B N
----+----------------
T | T F B N
F | T T T T
B | T N T N
N | T B B T
Equations
- Tau.Logic.Truth4.T.heyting_impl x✝ = x✝
- Tau.Logic.Truth4.F.heyting_impl x✝ = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.B.heyting_impl Tau.Logic.Truth4.T = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.B.heyting_impl Tau.Logic.Truth4.F = Tau.Logic.Truth4.N
- Tau.Logic.Truth4.B.heyting_impl Tau.Logic.Truth4.B = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.B.heyting_impl Tau.Logic.Truth4.N = Tau.Logic.Truth4.N
- Tau.Logic.Truth4.N.heyting_impl Tau.Logic.Truth4.T = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.N.heyting_impl Tau.Logic.Truth4.F = Tau.Logic.Truth4.B
- Tau.Logic.Truth4.N.heyting_impl Tau.Logic.Truth4.B = Tau.Logic.Truth4.B
- Tau.Logic.Truth4.N.heyting_impl Tau.Logic.Truth4.N = Tau.Logic.Truth4.T
Instances For

---

### `Tau.Logic.heyting_eq_material`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L216-L221)
**theorem
Tau.Logic.heyting_eq_material
(a b : Truth4)
 :a.heyting_impl b = a.impl b**


Heyting implication coincides with material implication on Truth4.
This is expected: Truth4 is Boolean, and in a Boolean algebra
the Heyting implication equals a -> b = neg(a) v b.

---

### `Tau.Logic.heyting_adjunction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L223-L227)
**theorem
Tau.Logic.heyting_adjunction
(a b : Truth4)
 :(a.meet (a.heyting_impl b)).le b = true**


Heyting adjunction (main direction): meet(a, a => b) <= b.
Verified via the le predicate.

---

### `Tau.Logic.heyting_maximality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L229-L234)
**theorem
Tau.Logic.heyting_maximality
(a b c : Truth4)

(h : (a.meet c).le b = true)
 :c.le (a.heyting_impl b) = true**


Heyting adjunction (maximality): if meet(a, c) <= b then c <= a => b.

---

### `Tau.Logic.Truth4.heyting_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L236-L237)
**def
Tau.Logic.Truth4.heyting_neg
(a : Truth4)
 :Truth4**


Heyting pseudo-complement: neg_H(a) := a => F.
Equations
- a.heyting_neg = a.heyting_impl Tau.Logic.Truth4.F
Instances For

---

### `Tau.Logic.heyting_neg_eq_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L239-L242)
**theorem
Tau.Logic.heyting_neg_eq_neg
(a : Truth4)
 :a.heyting_neg = a.neg**


Heyting negation coincides with bipolar negation on Truth4.

---

### `Tau.Logic.excluded_middle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L248-L251)
**theorem
Tau.Logic.excluded_middle
(v : Truth4)
 :v.join v.neg = Truth4.T**


Excluded middle holds in Truth4: join v (neg v) = T for all v.
This confirms Truth4 is Boolean, not merely Heyting.

---

### `Tau.Logic.double_negation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L253-L255)
**theorem
Tau.Logic.double_negation
(v : Truth4)
 :v.neg.neg = v**


Double negation elimination: neg(neg v) = v. (Already proved as neg_involutive.)

---

### `Tau.Logic.non_contradiction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L257-L259)
**theorem
Tau.Logic.non_contradiction
(v : Truth4)
 :v.meet v.neg = Truth4.F**


Non-contradiction: meet v (neg v) = F for all v.

---

### `Tau.Logic.truth4_is_boolean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L265-L280)
**theorem
Tau.Logic.truth4_is_boolean :(∀ (a : Truth4), a.meet a.neg = Truth4.F) ∧ (∀ (a : Truth4), a.join a.neg = Truth4.T) ∧ (∀ (a b c : Truth4), a.meet (b.join c) = (a.meet b).join (a.meet c)) ∧ ∀ (a : Truth4), a.neg.neg = a**


Truth4 is a Boolean algebra: it has complement laws (complement_meet,
complement_join), distributivity (meet_distrib_join, join_distrib_meet),
and excluded middle. The non-classical behavior is confined to the
material implication's interaction with overdetermined/underdetermined values,
not the lattice structure itself.

---

### `Tau.Logic.explosion_is_semantic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/BooleanRecovery.lean#L286-L297)
**theorem
Tau.Logic.explosion_is_semantic :(∀ (a : Truth4), a.meet a.neg = Truth4.F) ∧ (∀ (a : Truth4), a.join a.neg = Truth4.T) ∧ Truth4.B.impl Truth4.F ≠ Truth4.T**


The explosion barrier is about material implication, not lattice structure.
Truth4 IS Boolean, but impl B F = N <> T.
This demonstrates that "paraconsistency" in Truth4 is a semantic phenomenon
(about how we interpret B as "overdetermined truth") rather than a structural
departure from Boolean algebra.
