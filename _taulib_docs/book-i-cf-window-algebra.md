---
layout: taulib-doc
title: "TauLib.BookI.CF.WindowAlgebra"
permalink: /verify/taulib/docs/book-i-cf-window-algebra/
lane: verify
module_name: "TauLib.BookI.CF.WindowAlgebra"
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

# TauLib.CF.WindowAlgebra


Window algebra on the continued fraction head of ι<sub>τ</sub> = 2/(π+e).

## Registry Cross-References


- [CF.01] CF Head — `cf_head`

- [CF.05] 17 = a₃+a₄+a₅ — `w3_at_3`

- [CF.06] 5/7 symmetric recipe — `symmetric_recipe`

- [CF.09] Window Algebra — `windowSum`, key identities


## Mathematical Content


The continued fraction CF[ι<sub>τ</sub>] = [0; 2, 1, 13, 3, 1, 1, 1, 42, ...] encodes
electroweak physics through width-3 sliding window sums W₃(j) = a_j + a_{j+1} + a_{j+2}.

Key values:


- W₃(3) = 13+3+1 = 17 (g_A NLO denominator: 8/17)

- W₃(4) = 3+1+1 = 5 (sin²θ_W NLO numerator)

- W₃(5) = 1+1+1 = 3 (= |solenoidal triple|)


The symmetric 5/7 identity:
5/7 = W₃(4) / (W₃(3) − 2·W₃(4))
Both numerator and denominator use the same W₃ family.

The 17/5 quotient:
M_W/m_n = (17/5)·ι⁻³ = W₃(3)/W₃(4) · ι⁻³

Width 3 = |{π, γ, η}| = cardinality of solenoidal triple = number of
generators winding through the fiber T².

---

### `Tau.CF.cf_head`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L44-L47)
**def
Tau.CF.cf_head :List Nat**


The first 14 partial quotients of CF[ι<sub>τ</sub>] = CF[2/(π+e)].
Index 0 = floor part (0), indices 1..13 = partial quotients a₁..a₁₃.
Sufficient for all known physics encodings.
Equations
- Tau.CF.cf_head = [0, 2, 1, 13, 3, 1, 1, 1, 42, 1, 2, 1, 5, 5]
Instances For

---

### `Tau.CF.cf_head_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L49-L49)
**theorem
Tau.CF.cf_head_length :cf_head.length = 14**


---

### `Tau.CF.windowSum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L55-L59)
**def
Tau.CF.windowSum
(cf : List Nat)

(width start : Nat)
 :Nat**


Window sum W_k(j): sum of `width` consecutive CF terms starting at position `start`.
Returns 0 if any index is out of bounds.
Equations
- Tau.CF.windowSum cf width start = List.foldl (fun (acc i : Nat) => acc + cf.getD (start + i) 0) 0 (List.range width)
Instances For

---

### `Tau.CF.w3_at_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L65-L67)
**theorem
Tau.CF.w3_at_3 :windowSum cf_head 3 3 = 17**


[CF.05] W₃(3) = a₃ + a₄ + a₅ = 13 + 3 + 1 = 17.
The g_A NLO denominator: δ_A = (8/17)·ι².

---

### `Tau.CF.w3_at_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L69-L71)
**theorem
Tau.CF.w3_at_4 :windowSum cf_head 3 4 = 5**


[CF.06] W₃(4) = a₄ + a₅ + a₆ = 3 + 1 + 1 = 5.
The sin²θ_W NLO numerator.

---

### `Tau.CF.w3_at_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L73-L75)
**theorem
Tau.CF.w3_at_5 :windowSum cf_head 3 5 = 3**


W₃(5) = a₅ + a₆ + a₇ = 1 + 1 + 1 = 3.
Equals the cardinality of the solenoidal triple {π, γ, η}.

---

### `Tau.CF.w3_at_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L77-L78)
**theorem
Tau.CF.w3_at_1 :windowSum cf_head 3 1 = 16**


W₃(1) = a₁ + a₂ + a₃ = 2 + 1 + 13 = 16.

---

### `Tau.CF.w3_at_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L80-L81)
**theorem
Tau.CF.w3_at_2 :windowSum cf_head 3 2 = 17**


W₃(2) = a₂ + a₃ + a₄ = 1 + 13 + 3 = 17.

---

### `Tau.CF.symmetric_recipe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L87-L94)
**theorem
Tau.CF.symmetric_recipe :have w34 := windowSum cf_head 3 4;
have denom := windowSum cf_head 3 3 - 2 * windowSum cf_head 3 4;
w34 = 5 ∧ denom = 7**


[CF.06] The symmetric recipe for 5/7:
numerator = W₃(4) = 5, denominator = W₃(3) − 2·W₃(4) = 17 − 10 = 7.
Both sides use the same W₃ window family.

---

### `Tau.CF.symmetric_product`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L96-L99)
**theorem
Tau.CF.symmetric_product :windowSum cf_head 3 4 * (windowSum cf_head 3 3 - 2 * windowSum cf_head 3 4) = 35**


The product 5 × 7 = 35 from the symmetric recipe.

---

### `Tau.CF.mw_window_quotient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L105-L109)
**theorem
Tau.CF.mw_window_quotient :windowSum cf_head 3 3 = 17 ∧ windowSum cf_head 3 4 = 5**


[CF.06] The 17/5 quotient: W₃(3)/W₃(4) = 17/5.
This is the coefficient in M_W/m_n = (17/5)·ι⁻³.

---

### `Tau.CF.window_width_is_solenoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L115-L121)
**theorem
Tau.CF.window_width_is_solenoidal :3 = Kernel.solenoidalGenerators.length**


The window width 3 equals the number of solenoidal generators.
This is the structural reason WHY width-3 windows encode physics:
each W₃ window sum "reads out" one complete fiber period
through the three generators {π, γ, η} winding through T².

---

### `Tau.CF.w3_at_5_eq_solenoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L123-L126)
**theorem
Tau.CF.w3_at_5_eq_solenoidal :windowSum cf_head 3 5 = Kernel.solenoidalGenerators.length**


W₃(5) = 3 = |solenoidal|: the third window echoes the width itself.

---

### `Tau.CF.a3_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L132-L133)
**theorem
Tau.CF.a3_eq :cf_head.getD 3 0 = 13**


a₃ = 13 (the CF hub, anomalously large).

---

### `Tau.CF.a4_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L135-L136)
**theorem
Tau.CF.a4_eq :cf_head.getD 4 0 = 3**


a₄ = 3 = dim(τ³) = window width.

---

### `Tau.CF.a8_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L138-L139)
**theorem
Tau.CF.a8_eq :cf_head.getD 8 0 = 42**


a₈ = 42 (the "dark number", highest information content).

---

### `Tau.CF.EWCrossWeb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L145-L156)
**structure
Tau.CF.EWCrossWeb :Type**


The electroweak cross-web: all three EW observables (g_A, sin²θ_W, M_W/m_n)
are determined by two adjacent W₃ windows at positions 3 and 4.


- g_A NLO: 8/W₃(3) = 8/17

- sin²θ_W NLO: W₃(4)/(W₃(3)−2·W₃(4)) = 5/7

- M_W/m_n: W₃(3)/W₃(4) = 17/5
This structure packages 3 from the 17 that is expressible as a sum of
sums from two overlapping W₃ windows.


- w3_3 : Nat
- w3_4 : Nat
- hw3 : self.w3_3 = windowSum cf_head 3 3
- hw4 : self.w3_4 = windowSum cf_head 3 4
Instances For

---

### `Tau.CF.ewCrossWeb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/CF/WindowAlgebra.lean#L158-L159)
**def
Tau.CF.ewCrossWeb :EWCrossWeb**


The canonical EW cross-web instance.
Equations
- Tau.CF.ewCrossWeb = { w3_3 := 17, w3_4 := 5, hw3 := Tau.CF.ewCrossWeb._proof_1, hw4 := Tau.CF.ewCrossWeb._proof_2 }
Instances For
