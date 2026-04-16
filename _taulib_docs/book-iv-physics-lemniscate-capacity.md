---
layout: taulib-doc
title: "TauLib.BookIV.Physics.LemniscateCapacity"
permalink: /verify/taulib/docs/book-iv-physics-lemniscate-capacity/
lane: verify
module_name: "TauLib.BookIV.Physics.LemniscateCapacity"
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

# TauLib.BookIV.Physics.LemniscateCapacity


The √3 spectral distance from the lemniscate three-fold structure.

## Registry Cross-References


- [IV.D42] Lemniscate Three-Fold — `LemniscateThreeFold`, `three_fold`

- [IV.D43] Spectral Distance √3 — `sqrt3_numer`, `sqrt3_denom`

- [IV.T11] Three-Fold Distance Squared — `threefold_distance_sq`

- [IV.P06] √3 Approximation Quality — `sqrt3_approx_quality`

- [IV.R11] √3 Triad — structural remark


## Mathematical Content


### The Lemniscate Three-Fold


The boundary L = S¹ ∨ S¹ (wedge of two circles) has three distinguished
supports visible to spectral analysis:

- **Lobe₁**: the first S¹ component (χ₊-sector)

- **Lobe₂**: the second S¹ component (χ₋-sector)

- **Crossing**: the wedge point where the lobes meet


These three supports form a regular simplex in the spectral metric,
with pairwise distance √3.

### The Cube Root Mechanism


The distance √3 arises from the cube roots of unity:


- ω = e^{2πi/3} is the primitive third root

- |1 - ω|² = |1 - (-1/2 + i√3/2)|² = (3/2)² + (√3/2)² = 9/4 + 3/4 = 3

- Therefore |1 - ω| = √3


### The √3 Triad


The same √3 appears in three independent formulas:

- **R correction**: R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2) (mass ratio)

- **δ_A**: δ_A/m_n = (√3/2)·ι<sub>τ</sub>⁶ (proton-neutron mass difference)

- **α_G**: α_G = α¹⁸·√3·κ (gravity-EM hierarchy, if κ_n = 2√3)


All three are different readouts of the same geometric fact:
|1 - ω| = √3 on the three-fold lemniscate.

## Scope


- The three-fold structure is **tau-effective** (earned from L = S¹∨S¹)

- The √3 triad universality is **conjectural** (the δ_A and α_G applications
are partially verified numerically but not yet formally derived)


## Ground Truth Sources


- sqrt3_derivation_sprint.md §11-§15

- holonomy_correction_sprint.md §12-§16 (√3 triad)

- electron_mass_first_principles.md §28


---

### `Tau.BookIV.Physics.LemniscateSupport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L68-L73)
**inductive
Tau.BookIV.Physics.LemniscateSupport :Type**


[IV.D42] The three distinguished supports on L = S¹ ∨ S¹.

- Lobe1 : LemniscateSupport
- Lobe2 : LemniscateSupport
- Crossing : LemniscateSupport
Instances For

---

### `Tau.BookIV.Physics.instReprLemniscateSupport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L73-L73)
**instance
Tau.BookIV.Physics.instReprLemniscateSupport :Repr LemniscateSupport**

Equations
- Tau.BookIV.Physics.instReprLemniscateSupport = { reprPrec := Tau.BookIV.Physics.instReprLemniscateSupport.repr }

---

### `Tau.BookIV.Physics.instReprLemniscateSupport.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L73-L73)
**def
Tau.BookIV.Physics.instReprLemniscateSupport.repr :LemniscateSupport → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqLemniscateSupport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L73-L73)
**instance
Tau.BookIV.Physics.instDecidableEqLemniscateSupport :DecidableEq LemniscateSupport**

Equations
- Tau.BookIV.Physics.instDecidableEqLemniscateSupport x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.LemniscateThreeFold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L75-L83)
**structure
Tau.BookIV.Physics.LemniscateThreeFold :Type**


The three-fold structure: 3 supports with pairwise spectral distance √3.

- supports : List LemniscateSupport
The three supports.

- count : self.supports.length = 3
Exactly three supports.

- distance_sq : ℕ
Pairwise distance squared = 3 (i.e., distance = √3).

Instances For

---

### `Tau.BookIV.Physics.instReprLemniscateThreeFold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L83-L83)
**def
Tau.BookIV.Physics.instReprLemniscateThreeFold.repr :LemniscateThreeFold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprLemniscateThreeFold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L83-L83)
**instance
Tau.BookIV.Physics.instReprLemniscateThreeFold :Repr LemniscateThreeFold**

Equations
- Tau.BookIV.Physics.instReprLemniscateThreeFold = { reprPrec := Tau.BookIV.Physics.instReprLemniscateThreeFold.repr }

---

### `Tau.BookIV.Physics.three_fold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L85-L88)
**def
Tau.BookIV.Physics.three_fold :LemniscateThreeFold**


The canonical three-fold on L.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.supports_distinct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L90-L95)
**theorem
Tau.BookIV.Physics.supports_distinct :LemniscateSupport.Lobe1 ≠ LemniscateSupport.Lobe2 ∧ LemniscateSupport.Lobe2 ≠ LemniscateSupport.Crossing ∧ LemniscateSupport.Lobe1 ≠ LemniscateSupport.Crossing**


All three support types are distinct.

|1 - ω|² components for the cube root of unity ω = e^{2πi/3}.

```
ω = -1/2 + i(√3/2), so:
- (1 - ω_re)² = (1 - (-1/2))² = (3/2)² = 9/4
- (ω_im)² = (√3/2)² = 3/4
- |1 - ω|² = 9/4 + 3/4 = 12/4 = 3 
```


---

### `Tau.BookIV.Physics.omega_real_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L108-L109)
**def
Tau.BookIV.Physics.omega_real_sq :ℕ**


(1 - Re(ω))² numerator: (3/2)² has numerator 9.
Equations
- Tau.BookIV.Physics.omega_real_sq = 9
Instances For

---

### `Tau.BookIV.Physics.omega_imag_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L111-L112)
**def
Tau.BookIV.Physics.omega_imag_sq :ℕ**


Im(ω)² numerator: (√3/2)² has numerator 3.
Equations
- Tau.BookIV.Physics.omega_imag_sq = 3
Instances For

---

### `Tau.BookIV.Physics.omega_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L114-L115)
**def
Tau.BookIV.Physics.omega_denom :ℕ**


Common denominator for both squared components: 4.
Equations
- Tau.BookIV.Physics.omega_denom = 4
Instances For

---

### `Tau.BookIV.Physics.threefold_distance_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L117-L129)
**theorem
Tau.BookIV.Physics.threefold_distance_sq :omega_real_sq + omega_imag_sq = 3 * omega_denom**


[IV.T11] |1 - ω|² = 3.

Proof: |1 - ω|² = (3/2)² + (√3/2)² = 9/4 + 3/4 = 12/4 = 3.

In integer arithmetic:


- Numerator sum: 9 + 3 = 12

- Denominator: 4

- Quotient: 12 / 4 = 3


This is the origin of √3 in the mass ratio formula.

---

### `Tau.BookIV.Physics.distance_numerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L131-L134)
**theorem
Tau.BookIV.Physics.distance_numerator :omega_real_sq + omega_imag_sq = 12**


The numerator sum is 12.

---

### `Tau.BookIV.Physics.distance_denominator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L136-L138)
**theorem
Tau.BookIV.Physics.distance_denominator :omega_denom = 4**


The denominator is 4.

---

### `Tau.BookIV.Physics.sqrt3_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L144-L150)
**def
Tau.BookIV.Physics.sqrt3_numer :ℕ**


[IV.D43] √3 rational approximation (7 significant digits).
√3 = 1.7320508... ≈ 17320508/10000000

Quality: (17320508)² = 299,999,982,338,064
3 × (10000000)² = 300,000,000,000,000
Relative error: ~5.9 × 10⁻⁸
Equations
- Tau.BookIV.Physics.sqrt3_numer = 17320508
Instances For

---

### `Tau.BookIV.Physics.sqrt3_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L151-L151)
**def
Tau.BookIV.Physics.sqrt3_denom :ℕ**

Equations
- Tau.BookIV.Physics.sqrt3_denom = 10000000
Instances For

---

### `Tau.BookIV.Physics.sqrt3_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L153-L155)
**theorem
Tau.BookIV.Physics.sqrt3_denom_pos :sqrt3_denom > 0**


√3 denominator is positive.

---

### `Tau.BookIV.Physics.sqrt3_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L157-L159)
**def
Tau.BookIV.Physics.sqrt3_float :Float**


√3 as Float (for display).
Equations
- Tau.BookIV.Physics.sqrt3_float = Float.ofNat Tau.BookIV.Physics.sqrt3_numer / Float.ofNat Tau.BookIV.Physics.sqrt3_denom
Instances For

---

### `Tau.BookIV.Physics.sqrt3_approx_undershoots`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L161-L164)
**theorem
Tau.BookIV.Physics.sqrt3_approx_undershoots :sqrt3_numer * sqrt3_numer < 3 * sqrt3_denom * sqrt3_denom**


[IV.P06] The √3 approximation satisfies (√3_approx)² < 3 (undershoots).
17320508² < 3 × 10000000².

---

### `Tau.BookIV.Physics.sqrt3_approx_quality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L166-L169)
**theorem
Tau.BookIV.Physics.sqrt3_approx_quality :sqrt3_numer * sqrt3_numer * 100000 > 299999 * sqrt3_denom * sqrt3_denom**


The √3 approximation is close: (√3_approx)² > 2.99999.
17320508² × 100000 > 299999 × 10000000².

---

### `Tau.BookIV.Physics.sqrt3_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L171-L176)
**theorem
Tau.BookIV.Physics.sqrt3_in_range :173 * sqrt3_denom < 100 * sqrt3_numer ∧ 100 * sqrt3_numer < 174 * sqrt3_denom**


√3 is between 1.73 and 1.74.
173 × sqrt3_denom < 100 × sqrt3_numer < 174 × sqrt3_denom.

---

### `Tau.BookIV.Physics.Sqrt3Triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L182-L198)
**structure
Tau.BookIV.Physics.Sqrt3Triad :Type**


[IV.R11] The √3 triad: three independent physical formulas
sharing the same √3 from the lemniscate three-fold.

- R correction: R₀ = ι<sub>τ</sub>^(-7) − √3·ι<sub>τ</sub>^(-2)

- δ_A: δ_A/m_n = (√3/2)·ι<sub>τ</sub>⁶

- α_G: α_G = α¹⁸·√3·κ (if κ_n = 2√3)


This universality is CONJECTURAL: the R correction √3 is
tau-effective (Sprint 1), but δ_A and α_G await full derivation.

- name : String
Name of the formula.

- role : String
Where √3 appears.

- scope : String
Scope: tau-effective or conjectural.

Instances For

---

### `Tau.BookIV.Physics.instReprSqrt3Triad.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L198-L198)
**def
Tau.BookIV.Physics.instReprSqrt3Triad.repr :Sqrt3Triad → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprSqrt3Triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L198-L198)
**instance
Tau.BookIV.Physics.instReprSqrt3Triad :Repr Sqrt3Triad**

Equations
- Tau.BookIV.Physics.instReprSqrt3Triad = { reprPrec := Tau.BookIV.Physics.instReprSqrt3Triad.repr }

---

### `Tau.BookIV.Physics.sqrt3_triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L200-L205)
**def
Tau.BookIV.Physics.sqrt3_triad :List Sqrt3Triad**


The three members of the √3 triad.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.triad_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L207-L208)
**theorem
Tau.BookIV.Physics.triad_count :sqrt3_triad.length = 3**


Three triad members.

---

### `Tau.BookIV.Physics.CapacityIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L214-L228)
**structure
Tau.BookIV.Physics.CapacityIdentity :Type**


The capacity identity: √3·ι<sub>τ</sub>^(-2) = 4π√3 × X_E^(nat)
where X_E^(nat) = 1/(4π·ι<sub>τ</sub>²) is the natural electrostatic capacity
of the torus T² with shape ι<sub>τ</sub>.

This gives the correction term a clean physical interpretation:
it is the lemniscate-corrected universal capacity of T².

- coeff_numer : ℕ
The correction coefficient.

- coeff_denom : ℕ
- iota_power : ℕ
The ι<sub>τ</sub> power in the denominator.

- interpretation : String
Physical interpretation.

Instances For

---

### `Tau.BookIV.Physics.instReprCapacityIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L228-L228)
**instance
Tau.BookIV.Physics.instReprCapacityIdentity :Repr CapacityIdentity**

Equations
- Tau.BookIV.Physics.instReprCapacityIdentity = { reprPrec := Tau.BookIV.Physics.instReprCapacityIdentity.repr }

---

### `Tau.BookIV.Physics.instReprCapacityIdentity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/LemniscateCapacity.lean#L228-L228)
**def
Tau.BookIV.Physics.instReprCapacityIdentity.repr :CapacityIdentity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For
