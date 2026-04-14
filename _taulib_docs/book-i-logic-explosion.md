---
layout: taulib-doc
title: "TauLib.BookI.Logic.Explosion"
permalink: /verify/taulib/docs/book-i-logic-explosion/
lane: verify
module_name: "TauLib.BookI.Logic.Explosion"
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

# TauLib.Logic.Explosion


The explosion barrier: paraconsistent behavior of Truth4 material implication.

## Registry Cross-References


- [I.T13] Explosion Barrier -- `explosion_barrier`, `explosion_exists_counterexample`


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, bipolar balance

- chunk_0310_M002679: Bipolar partition and sector orthogonality


## Mathematical Content


In classical logic, from a contradiction P and not-P one can derive any
proposition Q (ex falso quodlibet / principle of explosion). In Truth4,
this fails for the overdetermined value B.

The explosion barrier theorem: impl B F = N, not T. That is, from an
overdetermined truth value, one cannot derive arbitrary falsehood via
material implication.

Key insight: Truth4 IS a Boolean algebra (it is isomorphic to Bool x Bool),
so the "non-classical" behavior is not about the lattice structure. Rather,
the explosion barrier concerns MATERIAL IMPLICATION (impl a b := join(neg a, b)):
evaluating impl at B does not yield T for all targets.

The spectral interpretation: the explosion barrier mirrors the orthogonality
of the sector idempotents e+ * e- = 0. The B value (= e+) and its negation
N (= e-) live in orthogonal sectors; their interaction annihilates rather
than propagating.

---

### `Tau.Logic.explosion_barrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L45-L52)
**theorem
Tau.Logic.explosion_barrier :Truth4.B.impl Truth4.F ≠ Truth4.T**


[I.T13] The explosion barrier: B does not imply everything.
Specifically, impl B F = N, not T.
This is the central paraconsistent feature of Truth4.

Calculation: impl B F = join (neg B) F = join N F = N.
Since N <> T, the implication B -> F is not "true".

---

### `Tau.Logic.explosion_exists_counterexample`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L54-L57)
**theorem
Tau.Logic.explosion_exists_counterexample :∃ (Q : Truth4), Truth4.B.impl Q ≠ Truth4.T**


Existential form: there exists a target Q such that impl B Q <> T.

---

### `Tau.Logic.impl_B_not_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L59-L65)
**theorem
Tau.Logic.impl_B_not_constant :¬∀ (Q : Truth4), Truth4.B.impl Q = Truth4.T**


Full tabulation: impl B is not constantly T.
impl B T = T, impl B F = N, impl B B = T, impl B N = T.

---

### `Tau.Logic.classical_explosion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L71-L74)
**theorem
Tau.Logic.classical_explosion
(Q : Truth4)
 :Truth4.F.impl Q = Truth4.T**


Classical explosion is preserved: from F (genuinely false), everything follows.
impl F Q = join (neg F) Q = join T Q = T.

---

### `Tau.Logic.classical_chain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L76-L81)
**theorem
Tau.Logic.classical_chain
(a Q : Truth4)
 :(a.meet a.neg).impl Q = Truth4.T**


The classical path: meet a (neg a) = F, and impl F Q = T.
So the two-step chain "from a and neg a deduce F, then from F deduce Q"
still works. The explosion barrier blocks the ONE-STEP path at B.

---

### `Tau.Logic.B_meet_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L87-L88)
**theorem
Tau.Logic.B_meet_B :Truth4.B.meet Truth4.B = Truth4.B**


B is idempotent under meet.

---

### `Tau.Logic.B_join_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L90-L91)
**theorem
Tau.Logic.B_join_B :Truth4.B.join Truth4.B = Truth4.B**


B is idempotent under join.

---

### `Tau.Logic.neg_B_eq_N`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L93-L94)
**theorem
Tau.Logic.neg_B_eq_N :Truth4.B.neg = Truth4.N**


neg B = N.

---

### `Tau.Logic.neg_N_eq_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L96-L97)
**theorem
Tau.Logic.neg_N_eq_B :Truth4.N.neg = Truth4.B**


neg N = B.

---

### `Tau.Logic.B_impl_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L99-L101)
**theorem
Tau.Logic.B_impl_B :Truth4.B.impl Truth4.B = Truth4.T**


B implies itself: impl B B = T.

---

### `Tau.Logic.B_meet_T`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L103-L104)
**theorem
Tau.Logic.B_meet_T :Truth4.B.meet Truth4.T = Truth4.B**


B infects conjunction with T: meet B T = B.

---

### `Tau.Logic.B_join_T`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L106-L107)
**theorem
Tau.Logic.B_join_T :Truth4.B.join Truth4.T = Truth4.T**


B absorbed by disjunction with T: join B T = T.

---

### `Tau.Logic.N_explosion_barrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L109-L111)
**theorem
Tau.Logic.N_explosion_barrier :Truth4.N.impl Truth4.F ≠ Truth4.T**


Symmetrically, N propagation: impl N F = B, not T.

---

### `Tau.Logic.impl_T`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L117-L119)
**theorem
Tau.Logic.impl_T
(a : Truth4)
 :Truth4.T.impl a = a**


impl T a = a (modus ponens compatible).

---

### `Tau.Logic.impl_T_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L121-L123)
**theorem
Tau.Logic.impl_T_right
(a : Truth4)
 :a.impl Truth4.T = Truth4.T**


impl a T = T (T is always implied).

---

### `Tau.Logic.impl_refl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L125-L127)
**theorem
Tau.Logic.impl_refl
(a : Truth4)
 :a.impl a = Truth4.T**


impl a a = join(neg a, a) = T for all a (reflexivity of implication).

---

### `Tau.Logic.impl_table_T_row`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L129-L132)
**theorem
Tau.Logic.impl_table_T_row :Truth4.T.impl Truth4.T = Truth4.T ∧ Truth4.T.impl Truth4.F = Truth4.F ∧ Truth4.T.impl Truth4.B = Truth4.B ∧ Truth4.T.impl Truth4.N = Truth4.N**


The full impl table as a computable function, verified against the definition.

---

### `Tau.Logic.impl_table_F_row`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L134-L136)
**theorem
Tau.Logic.impl_table_F_row :Truth4.F.impl Truth4.T = Truth4.T ∧ Truth4.F.impl Truth4.F = Truth4.T ∧ Truth4.F.impl Truth4.B = Truth4.T ∧ Truth4.F.impl Truth4.N = Truth4.T**


---

### `Tau.Logic.impl_table_B_row`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L138-L140)
**theorem
Tau.Logic.impl_table_B_row :Truth4.B.impl Truth4.T = Truth4.T ∧ Truth4.B.impl Truth4.F = Truth4.N ∧ Truth4.B.impl Truth4.B = Truth4.T ∧ Truth4.B.impl Truth4.N = Truth4.N**


---

### `Tau.Logic.impl_table_N_row`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L142-L144)
**theorem
Tau.Logic.impl_table_N_row :Truth4.N.impl Truth4.T = Truth4.T ∧ Truth4.N.impl Truth4.F = Truth4.B ∧ Truth4.N.impl Truth4.B = Truth4.B ∧ Truth4.N.impl Truth4.N = Truth4.T**


---

### `Tau.Logic.spectral_bridge_orthogonality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L150-L165)
**theorem
Tau.Logic.spectral_bridge_orthogonality :Truth4.B.toSectorPair.mul Truth4.N.toSectorPair = { b_sector := 0, c_sector := 0 }**


The spectral bridge: the explosion barrier corresponds to
sector orthogonality e+ * e- = 0.

Truth4.B maps to e_plus_sector = (1,0).
Truth4.N maps to e_minus_sector = (0,1).
Their product e+ * e- = (0,0), the zero sector pair.

The explosion barrier (impl B F = N, not T) mirrors the fact that
B and its negation N live in orthogonal spectral sectors that cannot
"communicate" to produce the top element T = (1,1).

---

### `Tau.Logic.spectral_bridge_B_idem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L167-L173)
**theorem
Tau.Logic.spectral_bridge_B_idem :Truth4.B.toSectorPair.mul Truth4.B.toSectorPair = Truth4.B.toSectorPair**


The sector product of B with itself is B (idempotent), matching e+^2 = e+.

---

### `Tau.Logic.spectral_bridge_N_idem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L175-L181)
**theorem
Tau.Logic.spectral_bridge_N_idem :Truth4.N.toSectorPair.mul Truth4.N.toSectorPair = Truth4.N.toSectorPair**


The sector product of N with itself is N (idempotent), matching e-^2 = e-.

---

### `Tau.Logic.spectral_bridge_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L183-L189)
**theorem
Tau.Logic.spectral_bridge_partition :Truth4.B.toSectorPair.add Truth4.N.toSectorPair = Truth4.T.toSectorPair**


Sector partition of unity: e+ + e- = (1,1) = T.

---

### `Tau.Logic.contraposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L195-L198)
**theorem
Tau.Logic.contraposition
(a b : Truth4)
 :a.impl b = b.neg.impl a.neg**


Contraposition holds: impl a b = impl (neg b) (neg a).

---

### `Tau.Logic.modus_ponens`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Logic/Explosion.lean#L200-L205)
**theorem
Tau.Logic.modus_ponens
(a b : Truth4)

(h_impl : a.impl b = Truth4.T)

(h_a : a = Truth4.T)
 :b = Truth4.T**


Modus ponens: if impl a b = T and a = T, then b = T.
