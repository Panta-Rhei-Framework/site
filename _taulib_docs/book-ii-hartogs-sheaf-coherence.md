---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.SheafCoherence"
permalink: /verify/taulib/docs/book-ii-hartogs-sheaf-coherence/
lane: verify
module_name: "TauLib.BookII.Hartogs.SheafCoherence"
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

# TauLib.BookII.Hartogs.SheafCoherence


Holomorphic presheaf and sheaf axioms on the cylinder topology.

## Registry Cross-References


- [II.D47] Holomorphic Presheaf — `presheaf_assign`, `presheaf_restriction_check`

- [II.L06] Gluing Lemma — `overlap_check`, `gluing_lemma_check`

- [II.T32] Sheaf Axioms — `locality_check`, `gluing_axiom_check`, `sheaf_axioms_check`


## Mathematical Content


The holomorphic presheaf O_τ assigns to each cylinder domain C_{k,a}
the space of tower-coherent, sector-independent functions on that domain.

**Cylinder domain:** C_{k,a} = { x ∈ Z/P_kZ | reduce(x, k) == a } for
0 ≤ a < P_k. At each stage k, the cylinders C_{k,0}, ..., C_{k,P_k-1}
partition Z/P_kZ into disjoint sets.

**Presheaf structure (II.D47):**


- To each cylinder (k, a), assign the set of reduce-compatible values.

- Restriction: from stage l to stage k (k ≤ l) is the reduce map.

- Functoriality: restriction is transitive (tower coherence).


**Ultrametric advantage:** Cylinders at the same stage are disjoint.
This makes the sheaf axioms trivially satisfied:

**Gluing Lemma (II.L06):**


- Same-stage overlap: C_{k,a} ∩ C_{k,b} = ∅ when a ≠ b.

- Cross-stage containment: C_{l,a} ⊆ C_{k, reduce(a,k)} when k ≤ l.

- Gluing is concatenation (no smoothing needed).


**Sheaf Axioms (II.T32):**


- (S1) Locality: if f restricts to 0 on every cylinder in a cover, then f = 0.

- (S2) Gluing: if local sections agree on (trivial) overlaps, they paste.


Both axioms are verified computationally for representative stages.

---

### `Tau.BookII.Hartogs.presheaf_assign`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L52-L59)
**def
Tau.BookII.Hartogs.presheaf_assign
(k a x : Denotation.TauIdx)
 :Bool**


[II.D47] Cylinder membership predicate:
presheaf_assign(k, a, x) is true iff x belongs to cylinder C_{k,a},
i.e., reduce(x, k) == a.

The cylinder C_{k,a} consists of all x ∈ Z/P_kZ with x mod P_k == a.
In the full primorial tower, it consists of all x with reduce(x,k) == a.
Equations
- Tau.BookII.Hartogs.presheaf_assign k a x = (Tau.Polarity.reduce x k == a)
Instances For

---

### `Tau.BookII.Hartogs.cylinder_partition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L61-L88)
**def
Tau.BookII.Hartogs.cylinder_partition_check
(k : Denotation.TauIdx)
 :Bool**


Cylinder partition check: at stage k, every x in [0, P_k) belongs
to exactly one cylinder C_{k,a}. The cylinders partition Z/P_kZ.
Equations
- Tau.BookII.Hartogs.cylinder_partition_check k = if (Tau.Polarity.primorial k == 0) = true then true
 else Tau.BookII.Hartogs.cylinder_partition_check.go 0 (Tau.Polarity.primorial k) k
Instances For

---

### `Tau.BookII.Hartogs.cylinder_partition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L68-L78)@[irreducible]

**def
Tau.BookII.Hartogs.cylinder_partition_check.go
(x fuel k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.cylinder_partition_check.check_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L80-L87)@[irreducible]

**def
Tau.BookII.Hartogs.cylinder_partition_check.check_unique
(x b k target fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.presheaf_restrict`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L94-L100)
**def
Tau.BookII.Hartogs.presheaf_restrict
(a l k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D47] Presheaf restriction map: from cylinder at stage l to
cylinder at stage k (for k ≤ l).

The restriction of a value a at stage l to stage k is reduce(a, k).
This is the canonical projection Z/P_lZ → Z/P_kZ.
Equations
- Tau.BookII.Hartogs.presheaf_restrict a l k = if k ≤ l then Tau.Polarity.reduce a k else a
Instances For

---

### `Tau.BookII.Hartogs.presheaf_restriction_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L102-L122)
**def
Tau.BookII.Hartogs.presheaf_restriction_check
(k_max bound : Denotation.TauIdx)
 :Bool**


Restriction compatibility: restricting from stage l to k and then
from k to j equals restricting directly from l to j.
This is tower coherence applied to the restriction maps.
Equations
- Tau.BookII.Hartogs.presheaf_restriction_check k_max bound = Tau.BookII.Hartogs.presheaf_restriction_check.go k_max bound 0 1 1 ((k_max + 1) * (k_max + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.presheaf_restriction_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L108-L121)@[irreducible]

**def
Tau.BookII.Hartogs.presheaf_restriction_check.go
(k_max bound : Denotation.TauIdx)

(a j k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.restriction_identity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L124-L140)
**def
Tau.BookII.Hartogs.restriction_identity_check
(k_max bound : Denotation.TauIdx)
 :Bool**


Restriction identity: restricting at the same stage is the identity
(modulo reduce idempotence).
Equations
- Tau.BookII.Hartogs.restriction_identity_check k_max bound = Tau.BookII.Hartogs.restriction_identity_check.go k_max bound 0 1 ((bound + 1) * (k_max + 1))
Instances For

---

### `Tau.BookII.Hartogs.restriction_identity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L129-L139)@[irreducible]

**def
Tau.BookII.Hartogs.restriction_identity_check.go
(k_max bound : Denotation.TauIdx)

(a k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.overlap_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L146-L163)
**def
Tau.BookII.Hartogs.overlap_check
(k a b : Denotation.TauIdx)
 :Bool**


[II.L06] Same-stage overlap check:
For a ≠ b, the cylinders C_{k,a} and C_{k,b} are disjoint.
This is the ultrametric property: same-stage cylinders do not overlap.

Returns true iff no x in [0, P_k) belongs to both C_{k,a} and C_{k,b}.
Equations
- Tau.BookII.Hartogs.overlap_check k a b = if (a == b) = true then true else Tau.BookII.Hartogs.overlap_check.go 0 (Tau.Polarity.primorial k) k a b
Instances For

---

### `Tau.BookII.Hartogs.overlap_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L155-L162)@[irreducible]

**def
Tau.BookII.Hartogs.overlap_check.go
(x fuel k a b : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.batch_disjoint_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L165-L179)
**def
Tau.BookII.Hartogs.batch_disjoint_check
(k : Denotation.TauIdx)
 :Bool**


Batch disjointness: all distinct same-stage cylinders are disjoint.
Equations
- Tau.BookII.Hartogs.batch_disjoint_check k = Tau.BookII.Hartogs.batch_disjoint_check.go 0 0
 (Tau.Polarity.primorial k * Tau.Polarity.primorial k + Tau.Polarity.primorial k + 1) k
Instances For

---

### `Tau.BookII.Hartogs.batch_disjoint_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L170-L178)@[irreducible]

**def
Tau.BookII.Hartogs.batch_disjoint_check.go
(a b fuel k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.containment_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L185-L201)
**def
Tau.BookII.Hartogs.containment_check
(k_max bound : Denotation.TauIdx)
 :Bool**


Cross-stage containment: for k ≤ l, every cylinder C_{l,a} at the
finer stage is contained in a unique cylinder C_{k, reduce(a,k)} at
the coarser stage.

Verify: for all x in C_{l,a}, we have reduce(x, k) == reduce(a, k).
Equations
- Tau.BookII.Hartogs.containment_check k_max bound = Tau.BookII.Hartogs.containment_check.go k_max 1 0 ((k_max + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.containment_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L193-L200)@[irreducible]

**def
Tau.BookII.Hartogs.containment_check.go
(k_max : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.gluing_lemma_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L207-L240)
**def
Tau.BookII.Hartogs.gluing_lemma_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.L06] Gluing Lemma: local functions on disjoint cylinders paste
to a global function.

In the ultrametric setting, same-stage cylinders are disjoint, so
gluing is simply concatenation. We verify: given a family of values
(one per cylinder at stage k), the "pasted" function f(x) = val(a)
where a = reduce(x,k) is well-defined and restricts correctly.

The test uses f(x) = reduce(x, k) as the "local section" for cylinder
C_{k, reduce(x,k)}, and checks that the pasted function equals the
global reduce.
Equations
- Tau.BookII.Hartogs.gluing_lemma_check k_max = Tau.BookII.Hartogs.gluing_lemma_check.go_k k_max 1 (k_max * 300 + 1)
Instances For

---

### `Tau.BookII.Hartogs.gluing_lemma_check.go_k`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L221-L231)@[irreducible]

**def
Tau.BookII.Hartogs.gluing_lemma_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.gluing_lemma_check.check_paste`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L233-L239)@[irreducible]

**def
Tau.BookII.Hartogs.gluing_lemma_check.check_paste
(x fuel k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.locality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L246-L274)
**def
Tau.BookII.Hartogs.locality_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T32, S1] Locality axiom:
If f restricts to 0 on every cylinder in a covering of Z/P_kZ,
then f = 0.

In our setting, the cover is the partition { C_{k,a} | 0 ≤ a < P_k }.
If f(x) = 0 for all x in each C_{k,a}, then f(x) = 0 for all x.
This is trivially true because the cylinders cover Z/P_kZ.

We verify: the cylinders C_{k,0}, ..., C_{k,P_k-1} cover [0, P_k).
Equations
- Tau.BookII.Hartogs.locality_check k_max = Tau.BookII.Hartogs.locality_check.go_k k_max 1 (k_max * 300 + 1)
Instances For

---

### `Tau.BookII.Hartogs.locality_check.go_k`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L258-L264)@[irreducible]

**def
Tau.BookII.Hartogs.locality_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.locality_check.check_cover`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L266-L273)@[irreducible]

**def
Tau.BookII.Hartogs.locality_check.check_cover
(x fuel k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.gluing_axiom_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L276-L309)
**def
Tau.BookII.Hartogs.gluing_axiom_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T32, S2] Gluing axiom:
If local sections {f_a : C_{k,a} → Z} agree on overlaps, they paste
to a global section.

In the ultrametric cylinder topology, same-stage overlaps are empty
(disjoint partition), so the agreement condition is vacuously true.
Gluing is simply: f(x) = f_{reduce(x,k)}(x).

We verify: the pasted function is well-defined and consistent with
the local sections. Test with f_a(x) = a (constant on each cylinder).
The pasted function is f(x) = reduce(x, k).
Equations
- Tau.BookII.Hartogs.gluing_axiom_check k_max = Tau.BookII.Hartogs.gluing_axiom_check.go_k k_max 1 (k_max * 300 + 1)
Instances For

---

### `Tau.BookII.Hartogs.gluing_axiom_check.go_k`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L290-L298)@[irreducible]

**def
Tau.BookII.Hartogs.gluing_axiom_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.gluing_axiom_check.check_sections`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L300-L308)@[irreducible]

**def
Tau.BookII.Hartogs.gluing_axiom_check.check_sections
(x fuel k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.sheaf_axioms_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L311-L313)
**def
Tau.BookII.Hartogs.sheaf_axioms_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T32] Full sheaf axioms check: both locality and gluing.
Equations
- Tau.BookII.Hartogs.sheaf_axioms_check k_max = (Tau.BookII.Hartogs.locality_check k_max && Tau.BookII.Hartogs.gluing_axiom_check k_max)
Instances For

---

### `Tau.BookII.Hartogs.functoriality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L319-L329)
**def
Tau.BookII.Hartogs.functoriality_check
(k_max bound : Denotation.TauIdx)
 :Bool**


Presheaf functoriality: the restriction maps form a functor from
the cylinder poset to Sets.

Axioms:

- restrict(a, k, k) = reduce(a, k) (identity morphism)

- restrict(restrict(a, l, k), k, j) = restrict(a, l, j) (composition)


These follow from tower coherence (reduction compatibility).
Equations
- Tau.BookII.Hartogs.functoriality_check k_max bound = (Tau.BookII.Hartogs.presheaf_restriction_check k_max bound && Tau.BookII.Hartogs.restriction_identity_check k_max bound)
Instances For

---

### `Tau.BookII.Hartogs.section_compatibility_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L335-L363)
**def
Tau.BookII.Hartogs.section_compatibility_check
(k_max : Denotation.TauIdx)
 :Bool**


Sections are reduce-compatible: if f is a section on C_{l,a} and
we restrict to C_{k, reduce(a,k)}, the restriction equals
reduce(f(x), k) for all x in C_{l,a}.

In the primorial tower, "section" = "reduce-compatible value assignment,"
so this is automatic. We verify the key case: the canonical section
f(x) = x on [0, P_l) restricts to reduce(x, k) on the coarser cylinder.
Equations
- Tau.BookII.Hartogs.section_compatibility_check k_max = Tau.BookII.Hartogs.section_compatibility_check.go_k k_max 1 (k_max * 300 + 1)
Instances For

---

### `Tau.BookII.Hartogs.section_compatibility_check.go_k`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L345-L351)@[irreducible]

**def
Tau.BookII.Hartogs.section_compatibility_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.section_compatibility_check.check_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L353-L362)@[irreducible]

**def
Tau.BookII.Hartogs.section_compatibility_check.check_compat
(x fuel k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_sheaf_coherence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L369-L387)
**def
Tau.BookII.Hartogs.full_sheaf_coherence_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.D47 + II.L06 + II.T32] Complete sheaf coherence verification:
presheaf structure, gluing, sheaf axioms, and functoriality.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.partition_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L452-L453)
**theorem
Tau.BookII.Hartogs.partition_1 :cylinder_partition_check 1 = true**


---

### `Tau.BookII.Hartogs.partition_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L455-L456)
**theorem
Tau.BookII.Hartogs.partition_2 :cylinder_partition_check 2 = true**


---

### `Tau.BookII.Hartogs.disjoint_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L459-L460)
**theorem
Tau.BookII.Hartogs.disjoint_1 :batch_disjoint_check 1 = true**


---

### `Tau.BookII.Hartogs.disjoint_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L462-L463)
**theorem
Tau.BookII.Hartogs.disjoint_2 :batch_disjoint_check 2 = true**


---

### `Tau.BookII.Hartogs.containment_3_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L466-L467)
**theorem
Tau.BookII.Hartogs.containment_3_30 :containment_check 3 30 = true**


---

### `Tau.BookII.Hartogs.gluing_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L470-L471)
**theorem
Tau.BookII.Hartogs.gluing_3 :gluing_lemma_check 3 = true**


---

### `Tau.BookII.Hartogs.locality_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L474-L475)
**theorem
Tau.BookII.Hartogs.locality_3 :locality_check 3 = true**


---

### `Tau.BookII.Hartogs.gluing_axiom_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L478-L479)
**theorem
Tau.BookII.Hartogs.gluing_axiom_3 :gluing_axiom_check 3 = true**


---

### `Tau.BookII.Hartogs.sheaf_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L482-L483)
**theorem
Tau.BookII.Hartogs.sheaf_3 :sheaf_axioms_check 3 = true**


---

### `Tau.BookII.Hartogs.funct_3_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L486-L487)
**theorem
Tau.BookII.Hartogs.funct_3_30 :functoriality_check 3 30 = true**


---

### `Tau.BookII.Hartogs.sect_compat_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L490-L491)
**theorem
Tau.BookII.Hartogs.sect_compat_3 :section_compatibility_check 3 = true**


---

### `Tau.BookII.Hartogs.full_sheaf_3_20`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/SheafCoherence.lean#L494-L495)
**theorem
Tau.BookII.Hartogs.full_sheaf_3_20 :full_sheaf_coherence_check 3 20 = true**
