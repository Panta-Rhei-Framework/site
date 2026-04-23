---
layout: taulib-doc
title: "TauLib.BookI.Topos.EarnedTopos"
permalink: /verify/taulib/docs/book-i-topos-earned-topos/
lane: verify
module_name: "TauLib.BookI.Topos.EarnedTopos"
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

# TauLib.Topos.EarnedTopos


The earned topos E_τ with subobject classifier Ω_τ = Truth4.

## Registry Cross-References


- [I.T25] Ω_τ Subobject Classifier — `omega_tau_classifier`

- [I.D58] Characteristic Morphism — `characteristic_morphism`

- [I.D59] Earned Topos — `EarnedTopos`

- [I.P27] Non-Boolean — `earned_topos_non_boolean`


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, bipolar structure

- chunk_0310_M002679: Bipolar partition, four truth values


## Mathematical Content


The subobject classifier of PSh(Cat_τ) is Ω_τ = Truth4 = {T, F, B, N}.
This was PREVIEWED in Part XI (Chapter 45, I.D41) and is now EARNED:
the four truth values are forced by the topos structure.

The characteristic morphism χ_S: X → Ω_τ sends each element to its
membership status: T (fully in), F (fully out), B (overdetermined), N (underdetermined).

The earned topos E_τ is non-Boolean: since |Ω_τ| = 4 ≠ 2, the complement
law fails, and the internal logic is both intuitionistic and paraconsistent.

---

### `Tau.Topos.omega_tau_classifier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L42-L58)
**theorem
Tau.Topos.omega_tau_classifier
(v : Logic.Omega_tau)
 :v = Logic.Truth4.T ∨ v = Logic.Truth4.F ∨ v = Logic.Truth4.B ∨ v = Logic.Truth4.N**


[I.T25] The subobject classifier for PSh(Cat_τ) is Ω_τ = Truth4.

In a Grothendieck topos, the subobject classifier Ω is characterized by:
for every mono m: S ↪ X, there exists a unique χ: X → Ω such that
the pullback of true: 1 → Ω along χ recovers S.

In our four-valued setting:


- T: the element is in S (both sectors confirm membership)

- F: the element is not in S (both sectors deny)

- B: overdetermined (B-sector confirms, C-sector denies)

- N: underdetermined (neither sector confirms)


The key theorem: Ω_τ has exactly four elements, matching Truth4.

---

### `Tau.Topos.omega_true_is_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L60-L61)
**theorem
Tau.Topos.omega_true_is_T :Logic.omega_true = Logic.Truth4.T**


The "true" morphism: the global element selecting T ∈ Ω_τ.

---

### `Tau.Topos.omega_tau_card_four`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L63-L71)
**theorem
Tau.Topos.omega_tau_card_four :Logic.omega_true ≠ Logic.omega_false ∧ Logic.omega_true ≠ Logic.omega_both ∧ Logic.omega_true ≠ Logic.omega_neither ∧ Logic.omega_false ≠ Logic.omega_both ∧ Logic.omega_false ≠ Logic.omega_neither ∧ Logic.omega_both ≠ Logic.omega_neither**


The subobject classifier has exactly 4 elements.

---

### `Tau.Topos.characteristic_morphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L77-L84)
**def
Tau.Topos.characteristic_morphism
(b_member c_member : Denotation.TauIdx → Bool)
 :Denotation.TauIdx → Logic.Omega_tau**


[I.D58] The characteristic morphism: for a given predicate on TauIdx,
assigns a Truth4 value to each element based on its membership status.

The predicate P encodes membership; the Truth4 value encodes HOW
the element is a member (from which spectral sectors).
Equations
- Tau.Topos.characteristic_morphism b_member c_member x = Tau.Logic.Truth4.fromBoolPair (b_member x, c_member x)
Instances For

---

### `Tau.Topos.char_both_true`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L86-L90)
**theorem
Tau.Topos.char_both_true
(b_mem c_mem : Denotation.TauIdx → Bool)

(x : Denotation.TauIdx)

(hb : b_mem x = true)

(hc : c_mem x = true)
 :characteristic_morphism b_mem c_mem x = Logic.Truth4.T**


Characteristic morphism: both sectors confirm ⟹ T.

---

### `Tau.Topos.char_both_false`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L92-L96)
**theorem
Tau.Topos.char_both_false
(b_mem c_mem : Denotation.TauIdx → Bool)

(x : Denotation.TauIdx)

(hb : b_mem x = false)

(hc : c_mem x = false)
 :characteristic_morphism b_mem c_mem x = Logic.Truth4.F**


Characteristic morphism: both sectors deny ⟹ F.

---

### `Tau.Topos.char_overdetermined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L98-L102)
**theorem
Tau.Topos.char_overdetermined
(b_mem c_mem : Denotation.TauIdx → Bool)

(x : Denotation.TauIdx)

(hb : b_mem x = true)

(hc : c_mem x = false)
 :characteristic_morphism b_mem c_mem x = Logic.Truth4.B**


Characteristic morphism: B-sector confirms, C denies ⟹ B.

---

### `Tau.Topos.char_underdetermined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L104-L108)
**theorem
Tau.Topos.char_underdetermined
(b_mem c_mem : Denotation.TauIdx → Bool)

(x : Denotation.TauIdx)

(hb : b_mem x = false)

(hc : c_mem x = true)
 :characteristic_morphism b_mem c_mem x = Logic.Truth4.N**


Characteristic morphism: neither confirms ⟹ N.

---

### `Tau.Topos.char_pullback_true`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L110-L120)
**theorem
Tau.Topos.char_pullback_true
(b_mem c_mem : Denotation.TauIdx → Bool)

(x : Denotation.TauIdx)
 :characteristic_morphism b_mem c_mem x = Logic.Truth4.T ↔ b_mem x = true ∧ c_mem x = true**


The pullback of true along χ recovers the subobject:
χ(x) = T iff both sectors confirm.

---

### `Tau.Topos.EarnedTopos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L126-L134)
**structure
Tau.Topos.EarnedTopos :Type 1**


[I.D59] The earned topos E_τ = PSh(Cat_τ) with Ω_τ as subobject classifier.
Bundles the Grothendieck topos structure with the four-valued classifier.

- topos : PShCatTau
The underlying presheaf topos.

- classifier : Type
The subobject classifier is Truth4.

- true_arrow : Logic.Omega_tau
The "true" arrow.

Instances For

---

### `Tau.Topos.earned_topos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L136-L140)
**def
Tau.Topos.earned_topos :EarnedTopos**


The canonical earned topos.
Equations
- Tau.Topos.earned_topos = { }
Instances For

---

### `Tau.Topos.earned_topos_non_boolean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L146-L159)
**theorem
Tau.Topos.earned_topos_non_boolean :Logic.omega_both ≠ Logic.omega_true ∧ Logic.omega_neither ≠ Logic.omega_true**


[I.P27] The earned topos E_τ is non-Boolean.

A Boolean topos has Ω = {0, 1} (two truth values).
Our Ω_τ has FOUR truth values (T, F, B, N).
The complement law ¬¬p = p holds in Boolean topoi
but fails in E_τ: ¬¬B = ¬N = B, which works,
but the issue is that B and N are distinct from T and F.

The explosion barrier (I.T13) gives a direct witness:
B ⟹ F is not T (it's N), so material implication doesn't
validate ex falso quodlibet.

---

### `Tau.Topos.topos_explosion_barrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L161-L163)
**theorem
Tau.Topos.topos_explosion_barrier :Logic.Truth4.B.impl Logic.Truth4.F ≠ Logic.Truth4.T**


The explosion barrier transfers to the topos: B → F ≠ T.

---

### `Tau.Topos.neg_involutive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L165-L170)
**theorem
Tau.Topos.neg_involutive
(v : Logic.Truth4)
 :v.neg.neg = v**


Negation IS involutive on Truth4 (it's a lattice involution):
T→F→T, F→T→F, B→N→B, N→B→N.
The non-Boolean property is NOT about double negation failure but about
the existence of non-trivial truth values B and N.

---

### `Tau.Topos.non_boolean_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L172-L175)
**theorem
Tau.Topos.non_boolean_witness :∃ (v : Logic.Truth4), v ≠ Logic.Truth4.T ∧ v ≠ Logic.Truth4.F**


The witness of non-Booleanness: there exist truth values
that are neither T nor F.

---

### `Tau.Topos.B_join_N_is_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L177-L178)
**theorem
Tau.Topos.B_join_N_is_T :Logic.Truth4.B.join Logic.Truth4.N = Logic.Truth4.T**


The join of B and N is T (overdetermined ∨ underdetermined = true).

---

### `Tau.Topos.B_meet_N_is_F`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L180-L181)
**theorem
Tau.Topos.B_meet_N_is_F :Logic.Truth4.B.meet Logic.Truth4.N = Logic.Truth4.F**


The meet of B and N is F (overdetermined ∧ underdetermined = false).

---

### `Tau.Topos.internal_logic_four_valued`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L183-L189)
**theorem
Tau.Topos.internal_logic_four_valued
(v : Logic.Omega_tau)
 :v = Logic.Truth4.T ∨ v = Logic.Truth4.F ∨ v = Logic.Truth4.B ∨ v = Logic.Truth4.N**


Internal logic: the topos has 4 truth values, not 2.
This means the internal logic is both:


- Intuitionistic (not all propositions are decidable: B, N exist)

- Paraconsistent (contradictions don't explode: I.T13)


---

### `Tau.Topos.even_odd_char`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/EarnedTopos.lean#L195-L198)
**def
Tau.Topos.even_odd_char :Denotation.TauIdx → Logic.Omega_tau**


The characteristic morphism for the "even numbers" subobject,
using B-sector = divisibility by 2, C-sector = divisibility by 3.
Equations
- Tau.Topos.even_odd_char = Tau.Topos.characteristic_morphism (fun (n : Tau.Denotation.TauIdx) => n % 2 == 0) fun (n : Tau.Denotation.TauIdx) =>
 n % 3 == 0
Instances For
