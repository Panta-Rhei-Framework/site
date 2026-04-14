---
layout: taulib-doc
title: "TauLib.BookII.Domains.Cylinders"
permalink: /verify/taulib/docs/book-ii-domains-cylinders/
lane: verify
module_name: "TauLib.BookII.Domains.Cylinders"
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

# TauLib.BookII.Domains.Cylinders


Stage-k cylinders and clopen basis for the profinite topology on Ẑ_τ.

## Registry Cross-References


- [II.D09] Stage-k Cylinder — `cylinder_mem`, `cylinder_count`

- [II.D10] Cylinder Domain — `CylinderDomain`, `eval_domain`

- [II.D11] Clopen Basis — `cylinder_clopen`

- [II.T04] Cylinder Basis Theorem — `nesting_check`, `stage_zero_check`, `partition_check`


## Mathematical Content


C_k(x) = { y ∈ Ẑ_τ : π_k(y) = π_k(x) } where π_k = reduce(·, k).

Properties:

- Nesting: C_{k+1}(x) ⊆ C_k(x) (finer stages refine)

- Trivial: C_0(x) = Ẑ_τ (primorial 0 = 1)

- Separating: for x ≠ y, ∃k such that C_k(x) ∩ C_k(y) = ∅

- Partition: at each k, cylinders partition ℤ/M_kℤ


---

### `Tau.BookII.Domains.cylinder_mem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L34-L37)
**def
Tau.BookII.Domains.cylinder_mem
(k center y : Denotation.TauIdx)
 :Bool**


[II.D09] Stage-k cylinder membership:
y ∈ C_k(x) iff π_k(y) = π_k(x), i.e., y ≡ x (mod M_k).
Equations
- Tau.BookII.Domains.cylinder_mem k center y = decide (Tau.Polarity.reduce y k = Tau.Polarity.reduce center k)
Instances For

---

### `Tau.BookII.Domains.cylinder_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L39-L47)
**def
Tau.BookII.Domains.cylinder_count
(k center bound : Denotation.TauIdx)
 :Nat**


Count members of C_k(center) in [2, bound].
Equations
- Tau.BookII.Domains.cylinder_count k center bound = Tau.BookII.Domains.cylinder_count.go k center bound 2 (bound + 1) 0
Instances For

---

### `Tau.BookII.Domains.cylinder_count.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L43-L46)@[irreducible]

**def
Tau.BookII.Domains.cylinder_count.go
(k center bound : Denotation.TauIdx)

(y fuel acc : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.CylinderDomain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L53-L58)
**inductive
Tau.BookII.Domains.CylinderDomain :Type**


[II.D10] Cylinder domain: finite Boolean combination of cylinders.

- basic : Denotation.TauIdx → Denotation.TauIdx → CylinderDomain
- inter : CylinderDomain → CylinderDomain → CylinderDomain
- union : CylinderDomain → CylinderDomain → CylinderDomain
- compl : CylinderDomain → CylinderDomain
Instances For

---

### `Tau.BookII.Domains.eval_domain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L60-L66)
**def
Tau.BookII.Domains.eval_domain
(d : CylinderDomain)

(y : Denotation.TauIdx)
 :Bool**


Evaluate membership in a cylinder domain.
Equations
- Tau.BookII.Domains.eval_domain (Tau.BookII.Domains.CylinderDomain.basic k c) y = Tau.BookII.Domains.cylinder_mem k c y
- Tau.BookII.Domains.eval_domain (a.inter b) y = (Tau.BookII.Domains.eval_domain a y && Tau.BookII.Domains.eval_domain b y)
- Tau.BookII.Domains.eval_domain (a.union b) y = (Tau.BookII.Domains.eval_domain a y || Tau.BookII.Domains.eval_domain b y)
- Tau.BookII.Domains.eval_domain a.compl y = !Tau.BookII.Domains.eval_domain a y
Instances For

---

### `Tau.BookII.Domains.cylinder_clopen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L72-L80)
**def
Tau.BookII.Domains.cylinder_clopen :CylinderDomain → Bool**


[II.D11] Every cylinder domain is clopen by construction.
Basic cylinders: defined by finitely many modular conditions (open)
and complement is a finite union of cylinders (closed).
Boolean operations preserve clopenness.
Equations
- Tau.BookII.Domains.cylinder_clopen (Tau.BookII.Domains.CylinderDomain.basic k c) = (decide (Tau.Polarity.primorial k > 0) && decide (Tau.Polarity.reduce c k < Tau.Polarity.primorial k))
- Tau.BookII.Domains.cylinder_clopen (a.inter b) = (Tau.BookII.Domains.cylinder_clopen a && Tau.BookII.Domains.cylinder_clopen b)
- Tau.BookII.Domains.cylinder_clopen (a.union b) = (Tau.BookII.Domains.cylinder_clopen a && Tau.BookII.Domains.cylinder_clopen b)
- Tau.BookII.Domains.cylinder_clopen a.compl = Tau.BookII.Domains.cylinder_clopen a
Instances For

---

### `Tau.BookII.Domains.nesting_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L86-L96)
**def
Tau.BookII.Domains.nesting_check
(x k bound : Denotation.TauIdx)
 :Bool**


[II.T04, clause 1] Nesting: C_{k+1}(x) ⊆ C_k(x).
If y ≡ x mod M_{k+1} then y ≡ x mod M_k (since M_k | M_{k+1}).
Equations
- Tau.BookII.Domains.nesting_check x k bound = Tau.BookII.Domains.nesting_check.go x k bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Domains.nesting_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L91-L95)@[irreducible]

**def
Tau.BookII.Domains.nesting_check.go
(x k bound : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.stage_zero_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L98-L107)
**def
Tau.BookII.Domains.stage_zero_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T04, clause 2] Stage 0: C_0(x) = everything.
primorial 0 = 1, so reduce y 0 = 0 for all y.
Equations
- Tau.BookII.Domains.stage_zero_check bound = Tau.BookII.Domains.stage_zero_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Domains.stage_zero_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L103-L106)@[irreducible]

**def
Tau.BookII.Domains.stage_zero_check.go
(bound : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.partition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L109-L126)
**def
Tau.BookII.Domains.partition_check
(k : Denotation.TauIdx)
 :Bool**


[II.T04, clause 3] Partition: residue classes at stage k partition.
Every y ∈ [0, M_k) satisfies y ∈ C_k(y).
Equations
- Tau.BookII.Domains.partition_check k = if Tau.Polarity.primorial k ≤ 1 then true else Tau.BookII.Domains.partition_check.go k 0 (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Domains.partition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L116-L125)@[irreducible]

**def
Tau.BookII.Domains.partition_check.go
(k : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.separation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L128-L138)
**def
Tau.BookII.Domains.separation_check
(x y : Denotation.TauIdx)
 :Bool**


[II.T04, clause 4] Separation: distinct elements eventually separate.
For x ≠ y, ∃ k such that ¬ cylinder_mem k x y.
Equations
- Tau.BookII.Domains.separation_check x y = if (x == y) = true then true else Tau.BookII.Domains.separation_check.go x y 1 20
Instances For

---

### `Tau.BookII.Domains.separation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L134-L137)@[irreducible]

**def
Tau.BookII.Domains.separation_check.go
(x y : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.nesting_7_1_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L166-L166)
**theorem
Tau.BookII.Domains.nesting_7_1_50 :nesting_check 7 1 50 = true**


---

### `Tau.BookII.Domains.nesting_7_2_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L167-L167)
**theorem
Tau.BookII.Domains.nesting_7_2_50 :nesting_check 7 2 50 = true**


---

### `Tau.BookII.Domains.stage_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L168-L168)
**theorem
Tau.BookII.Domains.stage_zero :stage_zero_check 50 = true**


---

### `Tau.BookII.Domains.partition_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L169-L169)
**theorem
Tau.BookII.Domains.partition_1 :partition_check 1 = true**


---

### `Tau.BookII.Domains.partition_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L170-L170)
**theorem
Tau.BookII.Domains.partition_2 :partition_check 2 = true**


---

### `Tau.BookII.Domains.partition_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L171-L171)
**theorem
Tau.BookII.Domains.partition_3 :partition_check 3 = true**


---

### `Tau.BookII.Domains.sep_3_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L172-L172)
**theorem
Tau.BookII.Domains.sep_3_5 :separation_check 3 5 = true**


---

### `Tau.BookII.Domains.sep_7_13`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/Cylinders.lean#L173-L173)
**theorem
Tau.BookII.Domains.sep_7_13 :separation_check 7 13 = true**
