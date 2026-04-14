---
layout: taulib-doc
title: "TauLib.BookI.Sets.Operations"
permalink: /verify/taulib/docs/book-i-sets-operations/
lane: verify
module_name: "TauLib.BookI.Sets.Operations"
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

# TauLib.Sets.Operations


τ-Set operations: union (lcm), intersection (gcd), and their lattice laws.

## Registry Cross-References


- [I.D32] Set Operations — `tau_union`, `tau_inter`

- [I.P11] Distributive Lattice — `tau_inter_distrib_union`


## Ground Truth Sources


- chunk_0355_M003041: gcd/lcm as meet/join in the divisibility lattice


## Mathematical Content


Under the τ-membership encoding (a ∈_τ b iff a | b):


- Intersection = gcd: d ∈_τ gcd(a,b) iff d ∈_τ a and d ∈_τ b

- Union = lcm: d ∈_τ lcm(a,b) iff d ∈_τ a or d ∈_τ b (up to closure)


The divisibility poset (Nat, |) forms a DISTRIBUTIVE LATTICE with
gcd as meet and lcm as join. The distributivity identity
gcd(a, lcm(b,c)) = lcm(gcd(a,b), gcd(a,c)) is proved in full
via a coprime decomposition argument.

---

### `Tau.Sets.tau_union`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L38-L39)
**def
Tau.Sets.tau_union
(a b : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D32] τ-union: lcm encodes set union under divisibility membership.
Equations
- Tau.Sets.tau_union a b = Nat.lcm a b
Instances For

---

### `Tau.Sets.tau_inter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L41-L42)
**def
Tau.Sets.tau_inter
(a b : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D32] τ-intersection: gcd encodes set intersection under divisibility membership.
Equations
- Tau.Sets.tau_inter a b = Tau.Coordinates.idx_gcd a b
Instances For

---

### `Tau.Sets.tau_union_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L48-L49)
**theorem
Tau.Sets.tau_union_comm
(a b : Denotation.TauIdx)
 :tau_union a b = tau_union b a**


---

### `Tau.Sets.tau_inter_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L51-L52)
**theorem
Tau.Sets.tau_inter_comm
(a b : Denotation.TauIdx)
 :tau_inter a b = tau_inter b a**


---

### `Tau.Sets.tau_union_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L58-L60)
**theorem
Tau.Sets.tau_union_assoc
(a b c : Denotation.TauIdx)
 :tau_union (tau_union a b) c = tau_union a (tau_union b c)**


---

### `Tau.Sets.tau_inter_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L62-L64)
**theorem
Tau.Sets.tau_inter_assoc
(a b c : Denotation.TauIdx)
 :tau_inter (tau_inter a b) c = tau_inter a (tau_inter b c)**


---

### `Tau.Sets.tau_union_self`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L70-L75)
**theorem
Tau.Sets.tau_union_self
(a : Denotation.TauIdx)
 :tau_union a a = a**


---

### `Tau.Sets.tau_inter_self`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L77-L78)
**theorem
Tau.Sets.tau_inter_self
(a : Denotation.TauIdx)
 :tau_inter a a = a**


---

### `Tau.Sets.tau_union_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L84-L85)
**theorem
Tau.Sets.tau_union_one
(a : Denotation.TauIdx)
 :tau_union 1 a = a**


---

### `Tau.Sets.tau_inter_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L92-L93)
**theorem
Tau.Sets.tau_inter_zero
(a : Denotation.TauIdx)
 :tau_inter 0 a = a**


---

### `Tau.Sets.tau_union_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L95-L96)
**theorem
Tau.Sets.tau_union_zero
(a : Denotation.TauIdx)
 :tau_union 0 a = 0**


---

### `Tau.Sets.tau_inter_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L98-L99)
**theorem
Tau.Sets.tau_inter_one
(a : Denotation.TauIdx)
 :tau_inter 1 a = 1**


---

### `Tau.Sets.tau_mem_union_left`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L105-L106)
**theorem
Tau.Sets.tau_mem_union_left
(a b : Denotation.TauIdx)
 :tau_mem a (tau_union a b)**


---

### `Tau.Sets.tau_mem_union_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L108-L109)
**theorem
Tau.Sets.tau_mem_union_right
(a b : Denotation.TauIdx)
 :tau_mem b (tau_union a b)**


---

### `Tau.Sets.tau_mem_inter_left`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L111-L112)
**theorem
Tau.Sets.tau_mem_inter_left
(a b : Denotation.TauIdx)
 :tau_mem (tau_inter a b) a**


---

### `Tau.Sets.tau_mem_inter_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L114-L115)
**theorem
Tau.Sets.tau_mem_inter_right
(a b : Denotation.TauIdx)
 :tau_mem (tau_inter a b) b**


---

### `Tau.Sets.tau_union_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L117-L120)
**theorem
Tau.Sets.tau_union_dvd
{a b c : Denotation.TauIdx}

(ha : tau_mem a c)

(hb : tau_mem b c)
 :tau_mem (tau_union a b) c**


---

### `Tau.Sets.tau_inter_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L122-L125)
**theorem
Tau.Sets.tau_inter_dvd
{a b c : Denotation.TauIdx}

(ha : tau_mem c a)

(hb : tau_mem c b)
 :tau_mem c (tau_inter a b)**


---

### `Tau.Sets.tau_union_inter_absorb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L131-L134)
**theorem
Tau.Sets.tau_union_inter_absorb
(a b : Denotation.TauIdx)
 :tau_union a (tau_inter a b) = a**


---

### `Tau.Sets.tau_inter_union_absorb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L136-L139)
**theorem
Tau.Sets.tau_inter_union_absorb
(a b : Denotation.TauIdx)
 :tau_inter a (tau_union a b) = a**


---

### `Tau.Sets.tau_inter_distrib_union`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L287-L292)
**theorem
Tau.Sets.tau_inter_distrib_union
(a b c : Denotation.TauIdx)
 :tau_inter a (tau_union b c) = tau_union (tau_inter a b) (tau_inter a c)**


[I.P11] Distributive Lattice: gcd distributes over lcm.
gcd(a, lcm(b,c)) = lcm(gcd(a,b), gcd(a,c)).

---

### `Tau.Sets.tau_union_distrib_inter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Sets/Operations.lean#L298-L325)
**theorem
Tau.Sets.tau_union_distrib_inter
(a b c : Denotation.TauIdx)
 :tau_union a (tau_inter b c) = tau_inter (tau_union a b) (tau_union a c)**


Dual distributivity: lcm distributes over gcd.
lcm(a, gcd(b,c)) = gcd(lcm(a,b), lcm(a,c)).
