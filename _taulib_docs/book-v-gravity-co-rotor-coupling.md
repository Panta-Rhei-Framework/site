---
layout: taulib-doc
title: "TauLib.BookV.Gravity.CoRotorCoupling"
permalink: /verify/taulib/docs/book-v-gravity-co-rotor-coupling/
lane: verify
module_name: "TauLib.BookV.Gravity.CoRotorCoupling"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Gravity.CoRotorCoupling


The co-rotor coupling distance κ_n on T² at the lemniscate crossing.

## Registry Cross-References


- [V.D10] Co-Rotor Coupling — `CoRotorCoupling`

- [V.D11] Gravitational Closing Identity — `canonical_coupling`

- [V.T04] κ_n Required Value — `kn_required_range`

- [V.T05] c₁ = 3/π Identification — `c1_matches_three_over_pi`

- [V.P02] Tree-Level Range — `kn_tree_in_range`

- [V.R03] R Formula Independence — `deficit_positive`


## Mathematical Content


### The Co-Rotor Coupling Distance


On T² with shape ratio r/R = ι<sub>τ</sub>, two co-rotating loops (toroidal and
poloidal circles) interact at the lemniscate crossing L = S¹ ∨ S¹.
The spectral coupling distance combines:


- √3 from the three-fold sector structure: |1 - ω| = √3 where
ω = e^{2πi/3} (Eisenstein cube root, see IV.T11)

- Factor 2 from two independent rotation axes (b₁(T²) = 2)


Tree-level result: κ_n^{tree} = 2√3 = 3.4641...

### The α-Order Correction


The physical coupling distance receives a first-order EM correction:

```
χ·κ_n/2 = √3 · (1 - c₁·α)
```


Sprint 4 numerical laboratory (224 candidates tested) identified:

```
c₁ = 3/π = 0.95493...
```


matching the required value 0.95453 to 0.04% (G deviation: 0.0003%).

Physical interpretation: three lemniscate sectors each contribute
1/π holonomy units to the correction, giving c₁ = 3 × (1/π) = 3/π.

### Closing Identity


The gravitational fine-structure constant satisfies:

```
α_G = α¹⁸ · (χ·κ_n/2) = α¹⁸ · √3 · (1 - (3/π)·α)
```


This is the closing identity from Sprint 3 (SS1-SS6) with the
correction identified in Sprint 4 (SS17).

## Scope


- The tree-level κ_n = 2√3 is **conjectural**

- The correction c₁ = 3/π is **conjectural** (0.04% match)

- The closing identity structure is **tau-effective**

- The required value κ_n = 3.44 is **established** (CODATA arithmetic)


## Ground Truth Sources


- kappa_n_geometric_derivation_sprint.md (Sprint 4)

- kappa_n_closing_identity_sprint.md (Sprint 3)

- electron_mass_first_principles.md §28


---

### `Tau.BookV.Gravity.CoRotorCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L78-L103)
**structure
Tau.BookV.Gravity.CoRotorCoupling :Type**


[V.D10] Co-rotor coupling structure on T².

Encodes the tree-level coupling distance κ_n^{tree} = 2√3
and the α-order correction coefficient c₁.

The physical κ_n = κ_n^{tree} × (1 - c₁·α):


- tree_factor = 2 (from b₁(T²) = 2, two rotation axes)

- spectral_distance_sq = 3 (from |1-ω|² = 3, three-fold lemniscate)

- correction_c1_numer/denom ≈ 3/π ≈ 0.95493


With these values and CODATA α:
κ_n ≈ 2√3 × (1 - (3/π)·α) ≈ 3.4400 (0.0003% from CODATA G).

- tree_factor : ℕ
Tree-level factor (number of rotation axes on T²).

- spectral_distance_sq : ℕ
Spectral distance squared |1-ω|² at the crossing.

- correction_c1_numer : ℕ
c₁ numerator (rational approximation of 3/π).

- correction_c1_denom : ℕ
c₁ denominator.

- denom_pos : self.correction_c1_denom > 0
Denominator positive.

- scope : String
Scope label.

Instances For

---

### `Tau.BookV.Gravity.instReprCoRotorCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L103-L103)
**def
Tau.BookV.Gravity.instReprCoRotorCoupling.repr :CoRotorCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprCoRotorCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L103-L103)
**instance
Tau.BookV.Gravity.instReprCoRotorCoupling :Repr CoRotorCoupling**

Equations
- Tau.BookV.Gravity.instReprCoRotorCoupling = { reprPrec := Tau.BookV.Gravity.instReprCoRotorCoupling.repr }

---

### `Tau.BookV.Gravity.c1_three_over_pi_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L109-L114)
**def
Tau.BookV.Gravity.c1_three_over_pi_numer :ℕ**


3/π rational approximation (7 significant digits).
3/π = 0.9549296585... ≈ 9549297/10000000

Quality: 9549297 × π_denom ≈ 3 × 10000000 × π_denom
(verified by range bounds below).
Equations
- Tau.BookV.Gravity.c1_three_over_pi_numer = 9549297
Instances For

---

### `Tau.BookV.Gravity.c1_three_over_pi_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L115-L115)
**def
Tau.BookV.Gravity.c1_three_over_pi_denom :ℕ**

Equations
- Tau.BookV.Gravity.c1_three_over_pi_denom = 10000000
Instances For

---

### `Tau.BookV.Gravity.canonical_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L117-L123)
**def
Tau.BookV.Gravity.canonical_coupling :CoRotorCoupling**


The canonical co-rotor coupling with c₁ = 3/π.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.kn_required_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L129-L134)
**def
Tau.BookV.Gravity.kn_required_numer :ℕ**


κ_n required value from the closing identity (rational approximation).

κ_n = 2 · α_G / α¹⁸ = 3.4399723239...

Using 8-digit approximation: 34399723/10000000.
Equations
- Tau.BookV.Gravity.kn_required_numer = 34399723
Instances For

---

### `Tau.BookV.Gravity.kn_required_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L135-L135)
**def
Tau.BookV.Gravity.kn_required_denom :ℕ**

Equations
- Tau.BookV.Gravity.kn_required_denom = 10000000
Instances For

---

### `Tau.BookV.Gravity.kn_required_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L137-L146)
**theorem
Tau.BookV.Gravity.kn_required_range :3439 * kn_required_denom < 1000 * kn_required_numer ∧ 1000 * kn_required_numer < 3441 * kn_required_denom**


[V.T04] κ_n is in the range (3.439, 3.441).

This range is established by CODATA arithmetic:
κ_n = 2 · G · m_n² / (α¹⁸ · ℏc) is fixed by measured constants.

34399 × 10000 < 10000 × 34399723 < 34410 × 10000.

---

### `Tau.BookV.Gravity.kn_tree_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L152-L154)
**def
Tau.BookV.Gravity.kn_tree_numer :ℕ**


κ_n^{tree} = 2√3 rational approximation.
2√3 = 3.4641016... ≈ 2 × 17320508/10000000.
Equations
- Tau.BookV.Gravity.kn_tree_numer = 2 * Tau.BookIV.Physics.sqrt3_numer
Instances For

---

### `Tau.BookV.Gravity.kn_tree_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L155-L155)
**def
Tau.BookV.Gravity.kn_tree_denom :ℕ**

Equations
- Tau.BookV.Gravity.kn_tree_denom = Tau.BookIV.Physics.sqrt3_denom
Instances For

---

### `Tau.BookV.Gravity.kn_tree_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L157-L161)
**theorem
Tau.BookV.Gravity.kn_tree_in_range :3464 * kn_tree_denom < 1000 * kn_tree_numer ∧ 1000 * kn_tree_numer < 3465 * kn_tree_denom**


[V.P02] The tree-level κ_n = 2√3 is in range (3.464, 3.465).

---

### `Tau.BookV.Gravity.tree_exceeds_required`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L163-L168)
**theorem
Tau.BookV.Gravity.tree_exceeds_required :kn_tree_numer * kn_required_denom > kn_required_numer * kn_tree_denom**


Tree level exceeds required value.
2√3 > κ_n(required), confirming the correction is negative.

---

### `Tau.BookV.Gravity.c1_target_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L174-L176)
**def
Tau.BookV.Gravity.c1_target_numer :ℕ**


The c₁ target from the deficit analysis (rational approximation).
c₁ = (√3 - χκ_n/2) / (α·√3) = 0.9545278697... ≈ 9545279/10000000.
Equations
- Tau.BookV.Gravity.c1_target_numer = 9545279
Instances For

---

### `Tau.BookV.Gravity.c1_target_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L177-L177)
**def
Tau.BookV.Gravity.c1_target_denom :ℕ**

Equations
- Tau.BookV.Gravity.c1_target_denom = 10000000
Instances For

---

### `Tau.BookV.Gravity.c1_matches_three_over_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L179-L188)
**theorem
Tau.BookV.Gravity.c1_matches_three_over_pi :c1_three_over_pi_numer < c1_target_numer + 5000 ∧ c1_target_numer < c1_three_over_pi_numer + 5000**


[V.T05] c₁ = 3/π matches the target to better than 0.05%.

|c₁(3/π) - c₁(target)| < 5000/10000000 = 0.0005

Verified: |9549297 - 9545279| = 4018 < 5000.
Relative error: 4018/9545279 ≈ 0.042% < 0.05%.

---

### `Tau.BookV.Gravity.c1_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L190-L194)
**theorem
Tau.BookV.Gravity.c1_in_range :954 * c1_three_over_pi_denom < 1000 * c1_three_over_pi_numer ∧ 1000 * c1_three_over_pi_numer < 956 * c1_three_over_pi_denom**


c₁ = 3/π is in range (0.954, 0.956).

---

### `Tau.BookV.Gravity.canonical_spectral_distance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L200-L202)
**theorem
Tau.BookV.Gravity.canonical_spectral_distance :canonical_coupling.spectral_distance_sq = 3**


The tree-level coupling has spectral distance² = 3 (from |1-ω|² = 3).

---

### `Tau.BookV.Gravity.canonical_tree_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L204-L206)
**theorem
Tau.BookV.Gravity.canonical_tree_factor :canonical_coupling.tree_factor = 2**


The tree-level coupling has factor 2 (from b₁(T²) = 2).

---

### `Tau.BookV.Gravity.canonical_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L208-L211)
**theorem
Tau.BookV.Gravity.canonical_denom_pos :canonical_coupling.correction_c1_denom > 0**


The correction denominator is positive.

---

### `Tau.BookV.Gravity.deficit_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/CoRotorCoupling.lean#L213-L217)
**theorem
Tau.BookV.Gravity.deficit_positive :kn_tree_numer * kn_required_denom > kn_required_numer * kn_tree_denom**


The deficit is positive: 2√3 > κ_n(required), so the correction
reduces the tree-level value.
