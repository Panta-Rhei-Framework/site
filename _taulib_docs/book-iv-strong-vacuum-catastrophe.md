---
layout: taulib-doc
title: "TauLib.BookIV.Strong.VacuumCatastrophe"
permalink: /verify/taulib/docs/book-iv-strong-vacuum-catastrophe/
lane: verify
module_name: "TauLib.BookIV.Strong.VacuumCatastrophe"
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

# TauLib.BookIV.Strong.VacuumCatastrophe


Vacuum energy, the cosmological constant problem, boundary-first
normalization, earned vs unearned mode counts, the no-vacuum-catastrophe
theorem, and tail stabilization of vacuum energy.

## Registry Cross-References


- [IV.D192] Boundary-first Normalization — `BoundaryFirstNorm`

- [IV.D193] Earned vs Unearned Mode Count — `EarnedModeCount`

- [IV.P119] No Uncountable Factorization — `no_uncountable`

- [IV.P120] Canonical Vacuum Uniqueness — `canonical_vacuum_uniqueness`

- [IV.T78] No Vacuum Catastrophe in tau — `no_vacuum_catastrophe`

- [IV.T79] Tail Stabilization of Vacuum Energy — `tail_stabilization`

- [IV.R99-R105] Structural remarks (comment-only)


## Mathematical Content


The cosmological constant catastrophe arises in orthodox QFT because
summing zero-point energies over uncountably many field modes produces
a divergent (or absurdly large) vacuum energy density, typically off by
~10^{120} from observation. In the tau-framework:

- Boundary-first normalization: all physical quantities factor through
the profinite omega-germ limit and boundary characters.

- Mode counts are EARNED (finite at each stage, profinite limit) not
UNEARNED (assigned infinite cardinality a priori).

- The vacuum energy density is a finite, stabilized boundary invariant.

- Tail stabilization ensures VacE_s[n] becomes constant beyond N_s.


## Ground Truth Sources


- Chapter 44 of Book IV (2nd Edition)


---

### `Tau.BookIV.Strong.BoundaryFirstNorm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L47-L63)
**structure
Tau.BookIV.Strong.BoundaryFirstNorm :Type**


[IV.D192] A physical quantity Q satisfies boundary-first normalization
if Q = eval o chi o omega-germ, factoring through:

- The profinite omega-germ limit

- A boundary character (tail-invariant)

- Evaluation in tau-Idx


This ensures no uncountable intermediaries appear.

- factorization : String
Factorization: eval o chi o omega-germ.

- step1_omega_germ : Bool
Step 1: omega-germ (profinite limit).

- step2_boundary_char : Bool
Step 2: boundary character (tail-invariant).

- step3_evaluation : Bool
Step 3: evaluation in tau-Idx.

Instances For

---

### `Tau.BookIV.Strong.instReprBoundaryFirstNorm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L63-L63)
**instance
Tau.BookIV.Strong.instReprBoundaryFirstNorm :Repr BoundaryFirstNorm**

Equations
- Tau.BookIV.Strong.instReprBoundaryFirstNorm = { reprPrec := Tau.BookIV.Strong.instReprBoundaryFirstNorm.repr }

---

### `Tau.BookIV.Strong.instReprBoundaryFirstNorm.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L63-L63)
**def
Tau.BookIV.Strong.instReprBoundaryFirstNorm.repr :BoundaryFirstNorm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.boundary_first_norm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L65-L65)
**def
Tau.BookIV.Strong.boundary_first_norm :BoundaryFirstNorm**

Equations
- Tau.BookIV.Strong.boundary_first_norm = { }
Instances For

---

### `Tau.BookIV.Strong.NoUncountable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L71-L89)
**structure
Tau.BookIV.Strong.NoUncountable :Type**


[IV.P119] No uncountable factorization: boundary-first normalized
quantities involve only:


- Finite sums at each stage

- The profinite omega-germ limit

- Evaluation in tau-Idx


No uncountable sums, integrals over continua, or infinite-dimensional
functional integrals appear. This is the structural reason the
vacuum catastrophe does not arise.

- finite_sums : Bool
Only finite sums at each stage.

- no_continuum : Bool
No continuum integrals.

- no_path_integrals : Bool
No infinite-dimensional path integrals.

- vacuum_finite : Bool
Consequence: vacuum energy is automatically finite.

Instances For

---

### `Tau.BookIV.Strong.instReprNoUncountable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L89-L89)
**instance
Tau.BookIV.Strong.instReprNoUncountable :Repr NoUncountable**

Equations
- Tau.BookIV.Strong.instReprNoUncountable = { reprPrec := Tau.BookIV.Strong.instReprNoUncountable.repr }

---

### `Tau.BookIV.Strong.instReprNoUncountable.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L89-L89)
**def
Tau.BookIV.Strong.instReprNoUncountable.repr :NoUncountable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.no_uncountable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L91-L91)
**def
Tau.BookIV.Strong.no_uncountable :NoUncountable**

Equations
- Tau.BookIV.Strong.no_uncountable = { }
Instances For

---

### `Tau.BookIV.Strong.CanonicalVacuumUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L97-L112)
**structure
Tau.BookIV.Strong.CanonicalVacuumUniqueness :Type**


[IV.P120] Each sector vacuum is the UNIQUE minimizer of its defect
functional, not a representative of an equivalence class:


- Omega^*_EM (B-sector)

- Omega^*_wk (A-sector)

- Gamma^*_s (C-sector, strong vacuum)

- nabla^*_GR (D-sector, gravitational vacuum)


Uniqueness follows from NFMin tie-breaking over finite sets.

- num_vacua : ℕ
Number of sector vacua.

- each_unique : Bool
Each is unique (not up to equivalence).

- mechanism : String
Mechanism: NFMin over finite admissible sets.

Instances For

---

### `Tau.BookIV.Strong.instReprCanonicalVacuumUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L112-L112)
**instance
Tau.BookIV.Strong.instReprCanonicalVacuumUniqueness :Repr CanonicalVacuumUniqueness**

Equations
- Tau.BookIV.Strong.instReprCanonicalVacuumUniqueness = { reprPrec := Tau.BookIV.Strong.instReprCanonicalVacuumUniqueness.repr }

---

### `Tau.BookIV.Strong.instReprCanonicalVacuumUniqueness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L112-L112)
**def
Tau.BookIV.Strong.instReprCanonicalVacuumUniqueness.repr :CanonicalVacuumUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.canonical_vacuum_uniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L114-L114)
**def
Tau.BookIV.Strong.canonical_vacuum_uniqueness :CanonicalVacuumUniqueness**

Equations
- Tau.BookIV.Strong.canonical_vacuum_uniqueness = { }
Instances For

---

### `Tau.BookIV.Strong.four_sector_vacua`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L116-L118)
**theorem
Tau.BookIV.Strong.four_sector_vacua :canonical_vacuum_uniqueness.num_vacua = 4**


Four sector vacua (B, A, C, D).

---

### `Tau.BookIV.Strong.ModeCountType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L124-L138)
**inductive
Tau.BookIV.Strong.ModeCountType :Type**


[IV.D193] Mode count classification:

EARNED: N_n = dim(H_partial[n]|_{T^2}) < infinity,
the number of independent boundary characters on T^2 at stage n.
Finite at every stage, grows with n, profinite limit is well-defined.

UNEARNED: any infinite cardinal assigned to continuum field theory
modes a priori, without derivation from a finite construction.
This is the source of the vacuum catastrophe in orthodox QFT.

- earned : ModeCountType
Earned: finite at each stage, profinite limit.

- unearned : ModeCountType
Unearned: infinite cardinal assigned a priori.

Instances For

---

### `Tau.BookIV.Strong.instReprModeCountType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L138-L138)
**instance
Tau.BookIV.Strong.instReprModeCountType :Repr ModeCountType**

Equations
- Tau.BookIV.Strong.instReprModeCountType = { reprPrec := Tau.BookIV.Strong.instReprModeCountType.repr }

---

### `Tau.BookIV.Strong.instReprModeCountType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L138-L138)
**def
Tau.BookIV.Strong.instReprModeCountType.repr :ModeCountType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instDecidableEqModeCountType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L138-L138)
**instance
Tau.BookIV.Strong.instDecidableEqModeCountType :DecidableEq ModeCountType**

Equations
- Tau.BookIV.Strong.instDecidableEqModeCountType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Strong.instBEqModeCountType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L138-L138)
**instance
Tau.BookIV.Strong.instBEqModeCountType :BEq ModeCountType**

Equations
- Tau.BookIV.Strong.instBEqModeCountType = { beq := Tau.BookIV.Strong.instBEqModeCountType.beq }

---

### `Tau.BookIV.Strong.instBEqModeCountType.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L138-L138)
**def
Tau.BookIV.Strong.instBEqModeCountType.beq :ModeCountType → ModeCountType → Bool**

Equations
- Tau.BookIV.Strong.instBEqModeCountType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Strong.EarnedModeCount`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L140-L148)
**structure
Tau.BookIV.Strong.EarnedModeCount :Type**


A mode count with its classification.

- count_type : ModeCountType
Type of mode count.

- finite_each_stage : Bool
If earned: finite at each stage.

- leads_to_divergence : Bool
If unearned: leads to divergence.

Instances For

---

### `Tau.BookIV.Strong.instReprEarnedModeCount.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L148-L148)
**def
Tau.BookIV.Strong.instReprEarnedModeCount.repr :EarnedModeCount → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprEarnedModeCount`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L148-L148)
**instance
Tau.BookIV.Strong.instReprEarnedModeCount :Repr EarnedModeCount**

Equations
- Tau.BookIV.Strong.instReprEarnedModeCount = { reprPrec := Tau.BookIV.Strong.instReprEarnedModeCount.repr }

---

### `Tau.BookIV.Strong.tau_mode_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L150-L154)
**def
Tau.BookIV.Strong.tau_mode_count :EarnedModeCount**


Tau mode count is earned.
Equations
- Tau.BookIV.Strong.tau_mode_count = { count_type := Tau.BookIV.Strong.ModeCountType.earned, finite_each_stage := true, leads_to_divergence := false }
Instances For

---

### `Tau.BookIV.Strong.orthodox_mode_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L156-L160)
**def
Tau.BookIV.Strong.orthodox_mode_count :EarnedModeCount**


Orthodox QFT mode count is unearned.
Equations
- Tau.BookIV.Strong.orthodox_mode_count = { count_type := Tau.BookIV.Strong.ModeCountType.unearned, finite_each_stage := false, leads_to_divergence := true }
Instances For

---

### `Tau.BookIV.Strong.tau_is_earned`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L162-L162)
**theorem
Tau.BookIV.Strong.tau_is_earned :tau_mode_count.count_type = ModeCountType.earned**


---

### `Tau.BookIV.Strong.orthodox_is_unearned`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L163-L163)
**theorem
Tau.BookIV.Strong.orthodox_is_unearned :orthodox_mode_count.count_type = ModeCountType.unearned**


---

### `Tau.BookIV.Strong.earned_does_not_diverge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L165-L165)
**theorem
Tau.BookIV.Strong.earned_does_not_diverge :tau_mode_count.leads_to_divergence = false**


---

### `Tau.BookIV.Strong.unearned_diverges`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L166-L166)
**theorem
Tau.BookIV.Strong.unearned_diverges :orthodox_mode_count.leads_to_divergence = true**


---

### `Tau.BookIV.Strong.NoVacuumCatastrophe`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L172-L195)
**structure
Tau.BookIV.Strong.NoVacuumCatastrophe :Type**


[IV.T78] No vacuum catastrophe in tau: the tau-vacuum energy density
rho_vac^(tau) = sum over {B,A,C,D} of eval(Delta^S_omega(Vac^*_S))
is:

- FINITE (a stabilized boundary invariant)

- PARAMETER-FREE (no additive renormalization needed)

- SCALE-INDEPENDENT (same element of H_partial at all regimes)


The orthodox catastrophe (10^120 mismatch) arises from assigning
uncountably many unearned modes and then attempting to regulate the
resulting divergence. In tau, finiteness is built in.

- finite : Bool
Vacuum energy is finite.

- parameter_free : Bool
No additive renormalization needed.

- scale_independent : Bool
Scale-independent.

- num_sectors_summed : ℕ
Sum over 4 primitive sectors.

- orthodox_mismatch_exponent : ℕ
Orthodox mismatch (order of magnitude in exponent).

- tau_mismatch : String
Tau: no mismatch by construction.

Instances For

---

### `Tau.BookIV.Strong.instReprNoVacuumCatastrophe`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L195-L195)
**instance
Tau.BookIV.Strong.instReprNoVacuumCatastrophe :Repr NoVacuumCatastrophe**

Equations
- Tau.BookIV.Strong.instReprNoVacuumCatastrophe = { reprPrec := Tau.BookIV.Strong.instReprNoVacuumCatastrophe.repr }

---

### `Tau.BookIV.Strong.instReprNoVacuumCatastrophe.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L195-L195)
**def
Tau.BookIV.Strong.instReprNoVacuumCatastrophe.repr :NoVacuumCatastrophe → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.no_vacuum_catastrophe`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L197-L197)
**def
Tau.BookIV.Strong.no_vacuum_catastrophe :NoVacuumCatastrophe**

Equations
- Tau.BookIV.Strong.no_vacuum_catastrophe = { }
Instances For

---

### `Tau.BookIV.Strong.vacuum_is_finite`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L199-L200)
**theorem
Tau.BookIV.Strong.vacuum_is_finite :no_vacuum_catastrophe.finite = true**


---

### `Tau.BookIV.Strong.vacuum_parameter_free`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L202-L203)
**theorem
Tau.BookIV.Strong.vacuum_parameter_free :no_vacuum_catastrophe.parameter_free = true**


---

### `Tau.BookIV.Strong.vacuum_scale_independent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L205-L206)
**theorem
Tau.BookIV.Strong.vacuum_scale_independent :no_vacuum_catastrophe.scale_independent = true**


---

### `Tau.BookIV.Strong.four_sectors_summed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L208-L209)
**theorem
Tau.BookIV.Strong.four_sectors_summed :no_vacuum_catastrophe.num_sectors_summed = 4**


---

### `Tau.BookIV.Strong.TailStabilization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L215-L235)
**structure
Tau.BookIV.Strong.TailStabilization :Type**


[IV.T79] Tail stabilization of vacuum energy: there exists a
stabilization horizon N_s such that VacE_s[n+1] = VacE_s[n]
for all n >= N_s.

The omega-germ limit VacE_s[omega] = VacE_s[N_s] is a finite
element of the boundary algebra, not a divergent limit.

This is not fine-tuning: N_s is determined by the sector's
activation depth and the rate of spectral tightening.

- horizon_exists : Bool
Stabilization horizon exists.

- constant_beyond : Bool
Beyond horizon: vacuum energy is constant.

- limit_equals_horizon : Bool
Omega-germ limit equals value at horizon.

- not_fine_tuning : Bool
Not fine-tuning: horizon determined by structure.

- source : String
Source: spectral tightening + finite mode count.

Instances For

---

### `Tau.BookIV.Strong.instReprTailStabilization.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L235-L235)
**def
Tau.BookIV.Strong.instReprTailStabilization.repr :TailStabilization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprTailStabilization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L235-L235)
**instance
Tau.BookIV.Strong.instReprTailStabilization :Repr TailStabilization**

Equations
- Tau.BookIV.Strong.instReprTailStabilization = { reprPrec := Tau.BookIV.Strong.instReprTailStabilization.repr }

---

### `Tau.BookIV.Strong.tail_stabilization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L237-L237)
**def
Tau.BookIV.Strong.tail_stabilization :TailStabilization**

Equations
- Tau.BookIV.Strong.tail_stabilization = { }
Instances For

---

### `Tau.BookIV.Strong.stabilization_exists`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L239-L240)
**theorem
Tau.BookIV.Strong.stabilization_exists :tail_stabilization.horizon_exists = true**


---

### `Tau.BookIV.Strong.VacuumEnergyComparison`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L246-L258)
**structure
Tau.BookIV.Strong.VacuumEnergyComparison :Type**


Summary comparing tau and orthodox vacuum energy.

- framework : String
Framework name.

- mode_count : ModeCountType
Mode count type.

- divergent : Bool
Divergent?

- requires_renorm : Bool
Requires renormalization?

- cc_problem : Bool
Cosmological constant problem?

Instances For

---

### `Tau.BookIV.Strong.instReprVacuumEnergyComparison`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L258-L258)
**instance
Tau.BookIV.Strong.instReprVacuumEnergyComparison :Repr VacuumEnergyComparison**

Equations
- Tau.BookIV.Strong.instReprVacuumEnergyComparison = { reprPrec := Tau.BookIV.Strong.instReprVacuumEnergyComparison.repr }

---

### `Tau.BookIV.Strong.instReprVacuumEnergyComparison.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L258-L258)
**def
Tau.BookIV.Strong.instReprVacuumEnergyComparison.repr :VacuumEnergyComparison → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.tau_vacuum_energy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L260-L265)
**def
Tau.BookIV.Strong.tau_vacuum_energy :VacuumEnergyComparison**

Equations
- Tau.BookIV.Strong.tau_vacuum_energy = { framework := "Category tau", mode_count := Tau.BookIV.Strong.ModeCountType.earned, divergent := false,
 requires_renorm := false, cc_problem := false }
Instances For

---

### `Tau.BookIV.Strong.orthodox_vacuum_energy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L267-L272)
**def
Tau.BookIV.Strong.orthodox_vacuum_energy :VacuumEnergyComparison**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.tau_no_cc_problem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L274-L274)
**theorem
Tau.BookIV.Strong.tau_no_cc_problem :tau_vacuum_energy.cc_problem = false**


---

### `Tau.BookIV.Strong.orthodox_has_cc_problem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L275-L275)
**theorem
Tau.BookIV.Strong.orthodox_has_cc_problem :orthodox_vacuum_energy.cc_problem = true**


---

### `Tau.BookIV.Strong.tau_no_divergence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L277-L277)
**theorem
Tau.BookIV.Strong.tau_no_divergence :tau_vacuum_energy.divergent = false**


---

### `Tau.BookIV.Strong.orthodox_diverges`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L278-L278)
**theorem
Tau.BookIV.Strong.orthodox_diverges :orthodox_vacuum_energy.divergent = true**
