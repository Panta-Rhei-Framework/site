---
layout: taulib-doc
title: "TauLib.BookII.Domains.HolImpliesCont"
permalink: /verify/taulib/docs/book-ii-domains-hol-implies-cont/
lane: verify
module_name: "TauLib.BookII.Domains.HolImpliesCont"
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

# TauLib.BookII.Domains.HolImpliesCont


The key inversion of Book II: holomorphic ⟹ continuous.

## Registry Cross-References


- [II.L01] Cylinder Compatibility Lemma — `cyl_compat_check`

- [II.T06] Hol ⟹ Cont — `hol_cont_check`


## Mathematical Content


II.L01 (Cylinder Compatibility):
If f is a stage-local StageFun (f_k depends only on π_k),
then f maps cylinders to cylinders:
π_k(x) = π_k(y) ⟹ f_k(x) = f_k(y)

II.T06 (Hol ⟹ Cont):
Every τ-holomorphic function is 1-Lipschitz:
δ(f(x), f(y)) ≥ δ(x, y)
i.e., holomorphic functions are uniformly continuous.

This INVERTS the classical order: in standard complex analysis,
holomorphy is defined via topology (continuity + Cauchy–Riemann).
Here, holomorphy = algebraic tower coherence, and continuity follows.

---

### `Tau.BookII.Domains.stage_local_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L39-L51)
**def
Tau.BookII.Domains.stage_local_check
(sf : Holomorphy.StageFun)

(k bound : Denotation.TauIdx)
 :Bool**


A StageFun is stage-local if f_k(n) depends only on π_k(n).
Check: f_k(n) = f_k(reduce(n, k)) for all n in [2, bound].
Equations
- Tau.BookII.Domains.stage_local_check sf k bound = Tau.BookII.Domains.stage_local_check.go sf k bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Domains.stage_local_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L44-L50)@[irreducible]

**def
Tau.BookII.Domains.stage_local_check.go
(sf : Holomorphy.StageFun)

(k bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.stage_local_batch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L53-L61)
**def
Tau.BookII.Domains.stage_local_batch
(sf : Holomorphy.StageFun)

(k_max bound : Denotation.TauIdx)
 :Bool**


Batch stage locality across stages 1..k_max.
Equations
- Tau.BookII.Domains.stage_local_batch sf k_max bound = Tau.BookII.Domains.stage_local_batch.go sf k_max bound 1 (k_max + 1)
Instances For

---

### `Tau.BookII.Domains.stage_local_batch.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L57-L60)@[irreducible]

**def
Tau.BookII.Domains.stage_local_batch.go
(sf : Holomorphy.StageFun)

(k_max bound : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.cyl_compat_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L67-L82)
**def
Tau.BookII.Domains.cyl_compat_check
(sf : Holomorphy.StageFun)

(k bound : Denotation.TauIdx)
 :Bool**


[II.L01] Cylinder compatibility: stage-local functions map
cylinders to cylinders.
Check: cylinder_mem k x y → f_k(x) = f_k(y).
Flat double loop with single fuel counter.
Equations
- Tau.BookII.Domains.cyl_compat_check sf k bound = Tau.BookII.Domains.cyl_compat_check.go sf k bound 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Domains.cyl_compat_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L74-L81)@[irreducible]

**def
Tau.BookII.Domains.cyl_compat_check.go
(sf : Holomorphy.StageFun)

(k bound : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.check_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L88-L99)
**def
Tau.BookII.Domains.check_depth
(sf : Holomorphy.StageFun)

(x y depth k_max : Denotation.TauIdx)
 :Bool**


Check output agreement at all stages up to a given depth.
Equations
- Tau.BookII.Domains.check_depth sf x y depth k_max = Tau.BookII.Domains.check_depth.go sf x y depth k_max 1 (min depth k_max + 1)
Instances For

---

### `Tau.BookII.Domains.check_depth.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L93-L98)@[irreducible]

**def
Tau.BookII.Domains.check_depth.go
(sf : Holomorphy.StageFun)

(x y depth k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.hol_cont_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L101-L116)
**def
Tau.BookII.Domains.hol_cont_check
(sf : Holomorphy.StageFun)

(k_max bound : Denotation.TauIdx)
 :Bool**


[II.T06] Hol ⟹ Cont: stage-local functions preserve
agreement depth (1-Lipschitz in the ultrametric).
If x,y agree at stage k, then f(x),f(y) agree at stage k.
Flat double loop with single fuel counter.
Equations
- Tau.BookII.Domains.hol_cont_check sf k_max bound = Tau.BookII.Domains.hol_cont_check.go sf k_max bound 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Domains.hol_cont_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L108-L115)@[irreducible]

**def
Tau.BookII.Domains.hol_cont_check.go
(sf : Holomorphy.StageFun)

(k_max bound : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Domains.chi_plus_local`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L139-L139)
**theorem
Tau.BookII.Domains.chi_plus_local :stage_local_batch Holomorphy.chi_plus_stage 4 20 = true**


---

### `Tau.BookII.Domains.chi_minus_local`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L140-L140)
**theorem
Tau.BookII.Domains.chi_minus_local :stage_local_batch Holomorphy.chi_minus_stage 4 20 = true**


---

### `Tau.BookII.Domains.id_local`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L141-L141)
**theorem
Tau.BookII.Domains.id_local :stage_local_batch Holomorphy.id_stage 4 20 = true**


---

### `Tau.BookII.Domains.chi_plus_compat_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L143-L143)
**theorem
Tau.BookII.Domains.chi_plus_compat_k1 :cyl_compat_check Holomorphy.chi_plus_stage 1 20 = true**


---

### `Tau.BookII.Domains.chi_plus_compat_k2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L144-L144)
**theorem
Tau.BookII.Domains.chi_plus_compat_k2 :cyl_compat_check Holomorphy.chi_plus_stage 2 20 = true**


---

### `Tau.BookII.Domains.chi_minus_compat_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L145-L145)
**theorem
Tau.BookII.Domains.chi_minus_compat_k1 :cyl_compat_check Holomorphy.chi_minus_stage 1 20 = true**


---

### `Tau.BookII.Domains.id_compat_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L146-L146)
**theorem
Tau.BookII.Domains.id_compat_k1 :cyl_compat_check Holomorphy.id_stage 1 20 = true**


---

### `Tau.BookII.Domains.chi_plus_cont`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L148-L148)
**theorem
Tau.BookII.Domains.chi_plus_cont :hol_cont_check Holomorphy.chi_plus_stage 4 15 = true**


---

### `Tau.BookII.Domains.chi_minus_cont`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L149-L149)
**theorem
Tau.BookII.Domains.chi_minus_cont :hol_cont_check Holomorphy.chi_minus_stage 4 15 = true**


---

### `Tau.BookII.Domains.id_cont`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Domains/HolImpliesCont.lean#L150-L150)
**theorem
Tau.BookII.Domains.id_cont :hol_cont_check Holomorphy.id_stage 4 15 = true**
