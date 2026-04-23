---
layout: taulib-doc
title: "TauLib.BookI.Logic.Truth4"
permalink: /verify/taulib/docs/book-i-logic-truth4/
lane: verify
module_name: "TauLib.BookI.Logic.Truth4"
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

# TauLib.Logic.Truth4


The four-valued logic earned from bipolar prime polarity.

## Registry Cross-References


- [I.D21] Truth4 Logic -- `Truth4`, `Truth4.meet`, `Truth4.join`, `Truth4.neg`


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, bipolar balance

- chunk_0310_M002679: Bipolar partition lifts to split-complex via Chi character


## Mathematical Content


The two spectral sectors (B and C) can independently confirm or deny a predicate,
yielding four truth values: T (both confirm), F (both deny), B (overdetermined),
N (underdetermined). These form a diamond lattice T > B, N > F.

Truth4 is isomorphic to Bool x Bool via the sector encoding:
T = (true, true), F = (false, false), B = (true, false), N = (false, true).

As a lattice, Truth4 is the product 2 x 2, hence a Boolean algebra.
The non-classical behavior arises not from the lattice structure but from the
material implication (impl a b := join (neg a) b), which does not validate
all classical tautologies when evaluated at B or N.

---

### `Tau.Logic.Truth4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L36-L46)
**inductive
Tau.Logic.Truth4 :Type**


[I.D21] The four truth values from bipolar evaluation.


- T: both sectors confirm (overdetermined-true)

- F: both sectors deny (underdetermined-false)

- B: B-sector confirms, C-sector denies (overdetermined / "both")

- N: neither sector confirms (underdetermined / "neither")


- T : Truth4
- F : Truth4
- B : Truth4
- N : Truth4
Instances For

---

### `Tau.Logic.instDecidableEqTruth4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L46-L46)
**instance
Tau.Logic.instDecidableEqTruth4 :DecidableEq Truth4**

Equations
- Tau.Logic.instDecidableEqTruth4 x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.Logic.instReprTruth4.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L46-L46)
**def
Tau.Logic.instReprTruth4.repr :Truth4 → ℕ → Std.Format**

Equations
- Tau.Logic.instReprTruth4.repr Tau.Logic.Truth4.T prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Logic.Truth4.T")).group prec✝
- Tau.Logic.instReprTruth4.repr Tau.Logic.Truth4.F prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Logic.Truth4.F")).group prec✝
- Tau.Logic.instReprTruth4.repr Tau.Logic.Truth4.B prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Logic.Truth4.B")).group prec✝
- Tau.Logic.instReprTruth4.repr Tau.Logic.Truth4.N prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Logic.Truth4.N")).group prec✝
Instances For

---

### `Tau.Logic.instReprTruth4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L46-L46)
**instance
Tau.Logic.instReprTruth4 :Repr Truth4**

Equations
- Tau.Logic.instReprTruth4 = { reprPrec := Tau.Logic.instReprTruth4.repr }

---

### `Tau.Logic.instInhabitedTruth4.default`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L46-L46)
**def
Tau.Logic.instInhabitedTruth4.default :Truth4**

Equations
- Tau.Logic.instInhabitedTruth4.default = Tau.Logic.Truth4.T
Instances For

---

### `Tau.Logic.instInhabitedTruth4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L46-L46)
**instance
Tau.Logic.instInhabitedTruth4 :Inhabited Truth4**

Equations
- Tau.Logic.instInhabitedTruth4 = { default := Tau.Logic.instInhabitedTruth4.default }

---

### `Tau.Logic.Truth4.le`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L54-L61)
**def
Tau.Logic.Truth4.le :Truth4 → Truth4 → Bool**


Lattice ordering on Truth4.
Diamond: F is bottom, T is top, B and N are incomparable middle elements.
Equations
- Tau.Logic.Truth4.F.le x✝ = true
- x✝.le Tau.Logic.Truth4.T = true
- Tau.Logic.Truth4.B.le Tau.Logic.Truth4.B = true
- Tau.Logic.Truth4.N.le Tau.Logic.Truth4.N = true
- x✝¹.le x✝ = false
Instances For

---

### `Tau.Logic.Truth4.meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L67-L76)
**def
Tau.Logic.Truth4.meet :Truth4 → Truth4 → Truth4**


Meet (conjunction): greatest lower bound in the diamond lattice.
Equations
- Tau.Logic.Truth4.T.meet x✝ = x✝
- x✝.meet Tau.Logic.Truth4.T = x✝
- Tau.Logic.Truth4.F.meet x✝ = Tau.Logic.Truth4.F
- x✝.meet Tau.Logic.Truth4.F = Tau.Logic.Truth4.F
- Tau.Logic.Truth4.B.meet Tau.Logic.Truth4.B = Tau.Logic.Truth4.B
- Tau.Logic.Truth4.N.meet Tau.Logic.Truth4.N = Tau.Logic.Truth4.N
- Tau.Logic.Truth4.B.meet Tau.Logic.Truth4.N = Tau.Logic.Truth4.F
- Tau.Logic.Truth4.N.meet Tau.Logic.Truth4.B = Tau.Logic.Truth4.F
Instances For

---

### `Tau.Logic.Truth4.join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L82-L91)
**def
Tau.Logic.Truth4.join :Truth4 → Truth4 → Truth4**


Join (disjunction): least upper bound in the diamond lattice.
Equations
- Tau.Logic.Truth4.F.join x✝ = x✝
- x✝.join Tau.Logic.Truth4.F = x✝
- Tau.Logic.Truth4.T.join x✝ = Tau.Logic.Truth4.T
- x✝.join Tau.Logic.Truth4.T = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.B.join Tau.Logic.Truth4.B = Tau.Logic.Truth4.B
- Tau.Logic.Truth4.N.join Tau.Logic.Truth4.N = Tau.Logic.Truth4.N
- Tau.Logic.Truth4.B.join Tau.Logic.Truth4.N = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.N.join Tau.Logic.Truth4.B = Tau.Logic.Truth4.T
Instances For

---

### `Tau.Logic.Truth4.neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L97-L103)
**def
Tau.Logic.Truth4.neg :Truth4 → Truth4**


Negation: bipolar polarity swap. T <-> F, B <-> N.
Corresponds to the polarity involution sigma on the split-complex algebra.
Equations
- Tau.Logic.Truth4.T.neg = Tau.Logic.Truth4.F
- Tau.Logic.Truth4.F.neg = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.B.neg = Tau.Logic.Truth4.N
- Tau.Logic.Truth4.N.neg = Tau.Logic.Truth4.B
Instances For

---

### `Tau.Logic.Truth4.impl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L109-L111)
**def
Tau.Logic.Truth4.impl
(a b : Truth4)
 :Truth4**


Material implication: a -> b := join(neg a, b).
Note: this does NOT validate all classical tautologies at B and N.
Equations
- a.impl b = a.neg.join b
Instances For

---

### `Tau.Logic.Truth4.toBoolPair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L117-L122)
**def
Tau.Logic.Truth4.toBoolPair :Truth4 → Bool × Bool**


Encode Truth4 as a pair of Booleans (B-sector, C-sector).
Equations
- Tau.Logic.Truth4.T.toBoolPair = (true, true)
- Tau.Logic.Truth4.F.toBoolPair = (false, false)
- Tau.Logic.Truth4.B.toBoolPair = (true, false)
- Tau.Logic.Truth4.N.toBoolPair = (false, true)
Instances For

---

### `Tau.Logic.Truth4.fromBoolPair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L124-L129)
**def
Tau.Logic.Truth4.fromBoolPair :Bool × Bool → Truth4**


Decode a Boolean pair back to Truth4.
Equations
- Tau.Logic.Truth4.fromBoolPair (true, true) = Tau.Logic.Truth4.T
- Tau.Logic.Truth4.fromBoolPair (false, false) = Tau.Logic.Truth4.F
- Tau.Logic.Truth4.fromBoolPair (true, false) = Tau.Logic.Truth4.B
- Tau.Logic.Truth4.fromBoolPair (false, true) = Tau.Logic.Truth4.N
Instances For

---

### `Tau.Logic.Truth4.meet_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L135-L137)
**theorem
Tau.Logic.Truth4.meet_comm
(a b : Truth4)
 :a.meet b = b.meet a**


Meet is commutative.

---

### `Tau.Logic.Truth4.join_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L139-L141)
**theorem
Tau.Logic.Truth4.join_comm
(a b : Truth4)
 :a.join b = b.join a**


Join is commutative.

---

### `Tau.Logic.Truth4.meet_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L143-L146)
**theorem
Tau.Logic.Truth4.meet_assoc
(a b c : Truth4)
 :(a.meet b).meet c = a.meet (b.meet c)**


Meet is associative.

---

### `Tau.Logic.Truth4.join_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L148-L151)
**theorem
Tau.Logic.Truth4.join_assoc
(a b c : Truth4)
 :(a.join b).join c = a.join (b.join c)**


Join is associative.

---

### `Tau.Logic.Truth4.meet_idem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L153-L155)
**theorem
Tau.Logic.Truth4.meet_idem
(a : Truth4)
 :a.meet a = a**


Meet is idempotent.

---

### `Tau.Logic.Truth4.join_idem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L157-L159)
**theorem
Tau.Logic.Truth4.join_idem
(a : Truth4)
 :a.join a = a**


Join is idempotent.

---

### `Tau.Logic.Truth4.absorption_meet_join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L161-L164)
**theorem
Tau.Logic.Truth4.absorption_meet_join
(a b : Truth4)
 :a.meet (a.join b) = a**


Absorption law: meet a (join a b) = a.

---

### `Tau.Logic.Truth4.absorption_join_meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L166-L169)
**theorem
Tau.Logic.Truth4.absorption_join_meet
(a b : Truth4)
 :a.join (a.meet b) = a**


Absorption law: join a (meet a b) = a.

---

### `Tau.Logic.Truth4.meet_distrib_join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L171-L174)
**theorem
Tau.Logic.Truth4.meet_distrib_join
(a b c : Truth4)
 :a.meet (b.join c) = (a.meet b).join (a.meet c)**


Meet distributes over join.

---

### `Tau.Logic.Truth4.join_distrib_meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L176-L179)
**theorem
Tau.Logic.Truth4.join_distrib_meet
(a b c : Truth4)
 :a.join (b.meet c) = (a.join b).meet (a.join c)**


Join distributes over meet.

---

### `Tau.Logic.Truth4.meet_F`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L181-L183)
**theorem
Tau.Logic.Truth4.meet_F
(a : Truth4)
 :F.meet a = F**


F is the bottom element for meet.

---

### `Tau.Logic.Truth4.join_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L185-L187)
**theorem
Tau.Logic.Truth4.join_T
(a : Truth4)
 :T.join a = T**


T is the top element for join.

---

### `Tau.Logic.Truth4.meet_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L189-L191)
**theorem
Tau.Logic.Truth4.meet_T
(a : Truth4)
 :T.meet a = a**


T is the identity for meet.

---

### `Tau.Logic.Truth4.join_F`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L193-L195)
**theorem
Tau.Logic.Truth4.join_F
(a : Truth4)
 :F.join a = a**


F is the identity for join.

---

### `Tau.Logic.Truth4.neg_involutive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L201-L203)
**theorem
Tau.Logic.Truth4.neg_involutive
(v : Truth4)
 :v.neg.neg = v**


Negation is involutive: neg (neg v) = v.

---

### `Tau.Logic.Truth4.neg_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L205-L206)
**theorem
Tau.Logic.Truth4.neg_T :T.neg = F**


neg T = F.

---

### `Tau.Logic.Truth4.neg_F`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L208-L209)
**theorem
Tau.Logic.Truth4.neg_F :F.neg = T**


neg F = T.

---

### `Tau.Logic.Truth4.neg_B`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L211-L212)
**theorem
Tau.Logic.Truth4.neg_B :B.neg = N**


neg B = N.

---

### `Tau.Logic.Truth4.neg_N`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L214-L215)
**theorem
Tau.Logic.Truth4.neg_N :N.neg = B**


neg N = B.

---

### `Tau.Logic.Truth4.complement_meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L221-L223)
**theorem
Tau.Logic.Truth4.complement_meet
(a : Truth4)
 :a.meet a.neg = F**


Complement law: meet a (neg a) = F for all a.

---

### `Tau.Logic.Truth4.complement_join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L225-L227)
**theorem
Tau.Logic.Truth4.complement_join
(a : Truth4)
 :a.join a.neg = T**


Complement law: join a (neg a) = T for all a.

---

### `Tau.Logic.Truth4.de_morgan_meet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L233-L236)
**theorem
Tau.Logic.Truth4.de_morgan_meet
(a b : Truth4)
 :(a.meet b).neg = a.neg.join b.neg**


De Morgan: neg (meet a b) = join (neg a) (neg b).

---

### `Tau.Logic.Truth4.de_morgan_join`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L238-L241)
**theorem
Tau.Logic.Truth4.de_morgan_join
(a b : Truth4)
 :(a.join b).neg = a.neg.meet b.neg**


De Morgan: neg (join a b) = meet (neg a) (neg b).

---

### `Tau.Logic.Truth4.toBoolPair_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L247-L250)
**theorem
Tau.Logic.Truth4.toBoolPair_injective
(a b : Truth4)

(h : a.toBoolPair = b.toBoolPair)
 :a = b**


toBoolPair is injective: distinct truth values map to distinct pairs.

---

### `Tau.Logic.Truth4.fromBoolPair_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L252-L255)
**theorem
Tau.Logic.Truth4.fromBoolPair_roundtrip
(v : Truth4)
 :fromBoolPair v.toBoolPair = v**


Round-trip: fromBoolPair (toBoolPair v) = v.

---

### `Tau.Logic.Truth4.toBoolPair_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L257-L261)
**theorem
Tau.Logic.Truth4.toBoolPair_roundtrip
(p : Bool × Bool)
 :(fromBoolPair p).toBoolPair = p**


Round-trip: toBoolPair (fromBoolPair p) = p for valid pairs.

---

### `Tau.Logic.Truth4.toSectorPair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L267-L273)
**def
Tau.Logic.Truth4.toSectorPair :Truth4 → Polarity.SectorPair**


Map Truth4 to sector pairs: T = (1,1), F = (0,0), B = (1,0), N = (0,1).
Links Truth4 to the split-complex idempotent structure from BipolarAlgebra.
Equations
- Tau.Logic.Truth4.T.toSectorPair = { b_sector := 1, c_sector := 1 }
- Tau.Logic.Truth4.F.toSectorPair = { b_sector := 0, c_sector := 0 }
- Tau.Logic.Truth4.B.toSectorPair = Tau.Polarity.e_plus_sector
- Tau.Logic.Truth4.N.toSectorPair = Tau.Polarity.e_minus_sector
Instances For

---

### `Tau.Logic.Truth4.B_is_e_plus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L275-L277)
**theorem
Tau.Logic.Truth4.B_is_e_plus :B.toSectorPair = Polarity.e_plus_sector**


B maps to the B-sector idempotent e+.

---

### `Tau.Logic.Truth4.N_is_e_minus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L279-L281)
**theorem
Tau.Logic.Truth4.N_is_e_minus :N.toSectorPair = Polarity.e_minus_sector**


N maps to the C-sector idempotent e-.

---

### `Tau.Logic.Truth4.B_meet_N_spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L283-L285)
**theorem
Tau.Logic.Truth4.B_meet_N_spectral :B.meet N = F**


Spectral bridge: meet of B and N gives F, mirroring e+ * e- = 0.

---

### `Tau.Logic.Truth4.le_refl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L291-L293)
**theorem
Tau.Logic.Truth4.le_refl
(a : Truth4)
 :a.le a = true**


le is reflexive.

---

### `Tau.Logic.Truth4.le_F`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L295-L297)
**theorem
Tau.Logic.Truth4.le_F
(a : Truth4)
 :F.le a = true**


F is the bottom element.

---

### `Tau.Logic.Truth4.le_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L299-L301)
**theorem
Tau.Logic.Truth4.le_T
(a : Truth4)
 :a.le T = true**


T is the top element.

---

### `Tau.Logic.Truth4.B_not_le_N`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L303-L304)
**theorem
Tau.Logic.Truth4.B_not_le_N :B.le N = false**


B and N are incomparable (B not le N).

---

### `Tau.Logic.Truth4.N_not_le_B`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Logic/Truth4.lean#L306-L307)
**theorem
Tau.Logic.Truth4.N_not_le_B :N.le B = false**


B and N are incomparable (N not le B).
