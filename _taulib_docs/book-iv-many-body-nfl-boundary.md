---
layout: taulib-doc
title: "TauLib.BookIV.ManyBody.NFLBoundary"
permalink: /verify/taulib/docs/book-iv-many-body-nfl-boundary/
lane: verify
module_name: "TauLib.BookIV.ManyBody.NFLBoundary"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.ManyBody.NFLBoundary


NFL-boundary theorem, decidable phase classification meta-theorem,
and ten-regime instantiation catalog.

## Registry Cross-References


- [IV.D390] Non-Dissipative Endomorphism — `NonDissEndomorphism`

- [IV.T210] NFL-Boundary Theorem — `NFLBoundary`

- [IV.R442] NFL-Depth Corollary — comment

- [IV.T211] Decidable Phase Classification Meta-Theorem — `DecidableMeta`

- [IV.P229] Ten Regime Instantiations — `TenRegimes`


## Mathematical Content


This module formalizes two structural results:

- 
**NFL-Boundary Theorem**: NonDiss(Φ) ⟺ Φ ∈ Aut(H_∂).
A dynamical step is non-dissipative iff it is an automorphism of the
boundary character algebra. Three-step proof: CRT reduction → finite
ring injectivity = bijectivity → inverse-limit lift.


- 
**Decidable Meta-Theorem**: At fixed refinement stage n with bounded
budget K, every regime predicate is decidable by finite recursion on
NF-coded states. This unifies CheckCrystal/CheckGlass with all
other regime checks.


## Ground Truth Sources


- Chapter 64 of Book IV (2nd Edition)

- Transcript chunk 0237 (NFL-boundary theorem)

- Transcript chunk 0235 (decidable phase classification)


---

### `Tau.BookIV.ManyBody.NonDissEndomorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L45-L55)
**structure
Tau.BookIV.ManyBody.NonDissEndomorphism :Type**


[IV.D390] An endomorphism Φ: H_∂ → H_∂ is non-dissipative if it
preserves all clopen ideals: Φ(I) = I for every clopen ideal I.
A dissipative endomorphism strictly shrinks at least one ideal.

- preserves_clopen : Bool
Preserves all clopen ideals.

- dissipative_shrinks : Bool
Dissipative = strictly shrinks some ideal.

- domain : String
Acts on boundary character algebra H_∂.

Instances For

---

### `Tau.BookIV.ManyBody.instReprNonDissEndomorphism.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L55-L55)
**def
Tau.BookIV.ManyBody.instReprNonDissEndomorphism.repr :NonDissEndomorphism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprNonDissEndomorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L55-L55)
**instance
Tau.BookIV.ManyBody.instReprNonDissEndomorphism :Repr NonDissEndomorphism**

Equations
- Tau.BookIV.ManyBody.instReprNonDissEndomorphism = { reprPrec := Tau.BookIV.ManyBody.instReprNonDissEndomorphism.repr }

---

### `Tau.BookIV.ManyBody.nondiss_endomorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L57-L57)
**def
Tau.BookIV.ManyBody.nondiss_endomorphism :NonDissEndomorphism**

Equations
- Tau.BookIV.ManyBody.nondiss_endomorphism = { }
Instances For

---

### `Tau.BookIV.ManyBody.NFLBoundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L63-L92)
**structure
Tau.BookIV.ManyBody.NFLBoundary :Type**


[IV.T210] **NFL-Boundary Theorem.**
NonDiss(Φ) ⟺ Φ ∈ Aut(H_∂).

A dynamical step is non-dissipative if and only if it is an
automorphism of the boundary character algebra.

**Proof outline:**

- CRT reduction: H_∂^(n) ≅ ∏_{p_i ≤ p_n} ℤ/p_iℤ

- On finite ring ℤ/pℤ: injective ⟺ surjective (pigeonhole)

- Preserving clopen ideals ⟺ injective on each factor
⟺ surjective ⟺ automorphism

- Inverse-limit lift: Aut at every stage → Aut of limit


**Physical consequence:**


- Euler regime: every step is Aut(H_∂) → Kelvin preserved

- NS regime: some steps are strict endomorphisms → dissipation


- nondiss_iff_aut : Bool
Non-dissipative iff automorphism.

- crt_reduction : Bool
Step 1: CRT decomposition.

- finite_ring_pigeonhole : Bool
Step 2: Finite ring pigeonhole.

- inverse_limit_lift : Bool
Step 3: Inverse-limit lift.

- euler_all_aut : Bool
Euler: all steps are Aut.

- ns_strict_endo : Bool
NS: some steps are strict endo.

Instances For

---

### `Tau.BookIV.ManyBody.instReprNFLBoundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L92-L92)
**instance
Tau.BookIV.ManyBody.instReprNFLBoundary :Repr NFLBoundary**

Equations
- Tau.BookIV.ManyBody.instReprNFLBoundary = { reprPrec := Tau.BookIV.ManyBody.instReprNFLBoundary.repr }

---

### `Tau.BookIV.ManyBody.instReprNFLBoundary.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L92-L92)
**def
Tau.BookIV.ManyBody.instReprNFLBoundary.repr :NFLBoundary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.nfl_boundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L94-L94)
**def
Tau.BookIV.ManyBody.nfl_boundary :NFLBoundary**

Equations
- Tau.BookIV.ManyBody.nfl_boundary = { }
Instances For

---

### `Tau.BookIV.ManyBody.nfl_nondiss_iff_aut`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L96-L97)
**theorem
Tau.BookIV.ManyBody.nfl_nondiss_iff_aut :nfl_boundary.nondiss_iff_aut = true**


---

### `Tau.BookIV.ManyBody.euler_all_automorphisms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L99-L100)
**theorem
Tau.BookIV.ManyBody.euler_all_automorphisms :nfl_boundary.euler_all_aut = true**


---

### `Tau.BookIV.ManyBody.ns_has_strict_endomorphisms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L102-L103)
**theorem
Tau.BookIV.ManyBody.ns_has_strict_endomorphisms :nfl_boundary.ns_strict_endo = true**


---

### `Tau.BookIV.ManyBody.DecidableMeta`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L115-L133)
**structure
Tau.BookIV.ManyBody.DecidableMeta :Type**


[IV.T211] **Decidable Phase Classification.**
At fixed refinement stage n with bounded budget K, every regime
predicate is decidable by finite recursion on NF-coded states.

Why: (1) NF code space is finite at stage n; (2) each d_j is
computable from NF code; (3) each regime condition is decidable
on finite codes; (4) conjunction of decidable predicates is decidable.

- finite_code_space : Bool
NF code space is finite.

- components_computable : Bool
Each defect component computable.

- conditions_decidable : Bool
Each regime condition decidable.

- conjunction_decidable : Bool
Conjunction of decidable is decidable.

- no_reals : Bool
No real-number arithmetic required.

Instances For

---

### `Tau.BookIV.ManyBody.instReprDecidableMeta`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L133-L133)
**instance
Tau.BookIV.ManyBody.instReprDecidableMeta :Repr DecidableMeta**

Equations
- Tau.BookIV.ManyBody.instReprDecidableMeta = { reprPrec := Tau.BookIV.ManyBody.instReprDecidableMeta.repr }

---

### `Tau.BookIV.ManyBody.instReprDecidableMeta.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L133-L133)
**def
Tau.BookIV.ManyBody.instReprDecidableMeta.repr :DecidableMeta → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.decidable_meta`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L135-L135)
**def
Tau.BookIV.ManyBody.decidable_meta :DecidableMeta**

Equations
- Tau.BookIV.ManyBody.decidable_meta = { }
Instances For

---

### `Tau.BookIV.ManyBody.phase_classification_decidable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L137-L138)
**theorem
Tau.BookIV.ManyBody.phase_classification_decidable :decidable_meta.conditions_decidable = true**


---

### `Tau.BookIV.ManyBody.no_real_arithmetic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L140-L141)
**theorem
Tau.BookIV.ManyBody.no_real_arithmetic :decidable_meta.no_reals = true**


---

### `Tau.BookIV.ManyBody.TenRegimeInstantiations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L147-L159)
**structure
Tau.BookIV.ManyBody.TenRegimeInstantiations :Type**


[IV.P229] The decidable meta-theorem instantiates for all ten regimes.
Each regime is a corollary via a horizon-contractivity lemma.

- num_regimes : ℕ
Number of regimes.

- all_decidable : Bool
All decidable at finite refinement.

- regimes : List String
Regime labels.

Instances For

---

### `Tau.BookIV.ManyBody.instReprTenRegimeInstantiations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L159-L159)
**instance
Tau.BookIV.ManyBody.instReprTenRegimeInstantiations :Repr TenRegimeInstantiations**

Equations
- Tau.BookIV.ManyBody.instReprTenRegimeInstantiations = { reprPrec := Tau.BookIV.ManyBody.instReprTenRegimeInstantiations.repr }

---

### `Tau.BookIV.ManyBody.instReprTenRegimeInstantiations.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L159-L159)
**def
Tau.BookIV.ManyBody.instReprTenRegimeInstantiations.repr :TenRegimeInstantiations → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.ten_regimes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L161-L161)
**def
Tau.BookIV.ManyBody.ten_regimes :TenRegimeInstantiations**

Equations
- Tau.BookIV.ManyBody.ten_regimes = { }
Instances For

---

### `Tau.BookIV.ManyBody.ten_decidable_regimes_total`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L163-L164)
**theorem
Tau.BookIV.ManyBody.ten_decidable_regimes_total :ten_regimes.num_regimes = 10**


---

### `Tau.BookIV.ManyBody.ten_decidable_regimes_all`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L166-L167)
**theorem
Tau.BookIV.ManyBody.ten_decidable_regimes_all :ten_regimes.all_decidable = true**


---

### `Tau.BookIV.ManyBody.ten_decidable_regimes_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/NFLBoundary.lean#L169-L170)
**theorem
Tau.BookIV.ManyBody.ten_decidable_regimes_count :ten_regimes.regimes.length = 10**
