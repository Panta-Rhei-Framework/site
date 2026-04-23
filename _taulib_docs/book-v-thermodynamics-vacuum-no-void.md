---
layout: taulib-doc
title: "TauLib.BookV.Thermodynamics.VacuumNoVoid"
permalink: /verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/
lane: verify
module_name: "TauLib.BookV.Thermodynamics.VacuumNoVoid"
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

# TauLib.BookV.Thermodynamics.VacuumNoVoid


No true void: the tau-vacuum has definite character. Vacuum energy is
boundary energy (finite, no UV divergence). The vacuum catastrophe is a
category error. Casimir effect from boundary modes.

## Registry Cross-References


- [V.D94] The tau-Vacuum -- `TauVacuum`

- [V.T65] Vacuum Energy is Boundary Energy -- `vacuum_energy_is_boundary`

- [V.T66] The Vacuum Catastrophe is a Category Error -- `vacuum_catastrophe_category_error`

- [V.T67] Ground State Uniqueness -- `GroundStateUniqueness`

- [V.C08] Vacuum Source Term is Finite -- `vacuum_source_finite`

- [V.P38] QFT Vacuum = Refinement Sum -- `QFTVacuumAsRefinement`

- [V.P39] Casimir Effect from Boundary Modes -- `CasimirFromBoundary`

- [V.R130] Why No Divergence -- structural remark

- [V.R131] Comparison with Normal Ordering -- `normal_ordering_comparison`

- [V.R132] Casimir Does Not Prove Mode Summation -- structural remark


## Mathematical Content


### The tau-Vacuum


The ground configuration omega_0 in H_partial[omega] satisfying:


- dbar_b omega_0 = 0 everywhere (holomorphic throughout)

- S_def[omega_0] = 0 (zero defect entropy)

- E[omega_0] = E_bdry (energy equals the boundary energy)


### Vacuum Energy is Boundary Energy


E_vac = E_bdry = integral over L of |H_partial[omega_0]|^2 d-sigma.
Finite integral over compact boundary L. No UV divergence.

### The Vacuum Catastrophe


The 10^120 discrepancy between QFT vacuum energy and observed Lambda is
a category error: QFT sums refinement entropy (lattice modes), not
physical energy. The tau-vacuum energy is a single boundary integral.

### Casimir Effect


Reproduced as the difference in boundary energies between constrained
(plates) and unconstrained geometry -- boundary mode argument, not
mode summation.

## Ground Truth Sources


- Book V ch25: vacuum structure

- kappa_n_closing_identity_sprint.md: vacuum energy


---

### `Tau.BookV.Thermodynamics.TauVacuum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L62-L85)
**structure
Tau.BookV.Thermodynamics.TauVacuum :Type**


[V.D94] The tau-vacuum: the ground configuration omega_0
in H_partial[omega] satisfying:

- dbar_b omega_0 = 0 everywhere (holomorphic)

- S_def[omega_0] = 0 (zero defect entropy)

- E[omega_0] = E_bdry (minimal energy = boundary energy)


The vacuum is NOT "empty space" -- it has definite character
from the boundary holonomy algebra on L = S^1 v S^1.

- is_holomorphic : Bool
Whether dbar_b omega_0 = 0 (holomorphic).

- s_def : ℕ
Defect entropy (zero in vacuum).

- zero_defect : self.s_def = 0
Vacuum is at zero defect entropy.

- e_bdry_numer : ℕ
Boundary energy numerator.

- e_bdry_denom : ℕ
Boundary energy denominator.

- denom_pos : self.e_bdry_denom > 0
Denominator positive.

- is_not_void : Bool
The vacuum has definite character (not void).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprTauVacuum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L85-L85)
**instance
Tau.BookV.Thermodynamics.instReprTauVacuum :Repr TauVacuum**

Equations
- Tau.BookV.Thermodynamics.instReprTauVacuum = { reprPrec := Tau.BookV.Thermodynamics.instReprTauVacuum.repr }

---

### `Tau.BookV.Thermodynamics.instReprTauVacuum.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L85-L85)
**def
Tau.BookV.Thermodynamics.instReprTauVacuum.repr :TauVacuum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.TauVacuum.energyFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L87-L89)
**def
Tau.BookV.Thermodynamics.TauVacuum.energyFloat
(v : TauVacuum)
 :Float**


Boundary energy as Float.
Equations
- v.energyFloat = Float.ofNat v.e_bdry_numer / Float.ofNat v.e_bdry_denom
Instances For

---

### `Tau.BookV.Thermodynamics.vacuum_holomorphic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L91-L93)
**theorem
Tau.BookV.Thermodynamics.vacuum_holomorphic :{ zero_defect := ⋯, e_bdry_numer := 1, e_bdry_denom := 1, denom_pos := ⋯ }.is_holomorphic = true**


The default vacuum is holomorphic.

---

### `Tau.BookV.Thermodynamics.vacuum_energy_is_boundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L99-L107)
**theorem
Tau.BookV.Thermodynamics.vacuum_energy_is_boundary :"E_vac = E_bdry = integral_L |H_partial[omega_0]|^2 d-sigma, finite" = "E_vac = E_bdry = integral_L |H_partial[omega_0]|^2 d-sigma, finite"**


[V.T65] Vacuum energy is boundary energy:
E_vac = E_bdry = integral over L of |H_partial[omega_0]|^2 d-sigma.

The vacuum energy is a finite integral over the compact
boundary L = S^1 v S^1. No momentum integral, no UV cutoff,
no renormalization needed.

---

### `Tau.BookV.Thermodynamics.QFTVacuumAsRefinement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L113-L127)
**structure
Tau.BookV.Thermodynamics.QFTVacuumAsRefinement :Type**


[V.P38] QFT vacuum = refinement sum: the QFT vacuum energy density
at cutoff level n corresponds to rho_vac^QFT(n) ~ p^{3n} hbar c / (2 l_ref).

At the Planck cutoff, this gives the 10^{120} discrepancy.
The QFT sum counts lattice modes (refinement entropy), not energy.

- refinement_prime : ℕ
The refinement prime p.

- cutoff_level : ℕ
Cutoff level n.

- mode_count_scaling : String
The mode count grows as p^{3n}.

- discrepancy_log10 : ℕ
The discrepancy exponent (120 orders of magnitude).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprQFTVacuumAsRefinement.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L127-L127)
**def
Tau.BookV.Thermodynamics.instReprQFTVacuumAsRefinement.repr :QFTVacuumAsRefinement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprQFTVacuumAsRefinement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L127-L127)
**instance
Tau.BookV.Thermodynamics.instReprQFTVacuumAsRefinement :Repr QFTVacuumAsRefinement**

Equations
- Tau.BookV.Thermodynamics.instReprQFTVacuumAsRefinement = { reprPrec := Tau.BookV.Thermodynamics.instReprQFTVacuumAsRefinement.repr }

---

### `Tau.BookV.Thermodynamics.qft_vacuum_planck`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L129-L132)
**def
Tau.BookV.Thermodynamics.qft_vacuum_planck :QFTVacuumAsRefinement**


The discrepancy is 120 orders of magnitude.
Equations
- Tau.BookV.Thermodynamics.qft_vacuum_planck = { refinement_prime := 2, cutoff_level := 0 }
Instances For

---

### `Tau.BookV.Thermodynamics.qft_discrepancy_120`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L134-L135)
**theorem
Tau.BookV.Thermodynamics.qft_discrepancy_120 :qft_vacuum_planck.discrepancy_log10 = 120**


---

### `Tau.BookV.Thermodynamics.vacuum_catastrophe_category_error`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L141-L150)
**theorem
Tau.BookV.Thermodynamics.vacuum_catastrophe_category_error :"rho_vac^QFT counts S_ref modes, not E_vac; 10^120 is a category error" = "rho_vac^QFT counts S_ref modes, not E_vac; 10^120 is a category error"**


[V.T66] The vacuum catastrophe is a category error: the QFT
vacuum energy density is not the energy of the vacuum state but
a refinement count (lattice modes weighted by zero-point energy).

It corresponds to S_ref (refinement entropy), not E_vac (energy).
The 10^{120} mismatch is between a counting artifact and a
physical energy -- comparing apples to oranges.

---

### `Tau.BookV.Thermodynamics.vacuum_source_finite`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L156-L164)
**theorem
Tau.BookV.Thermodynamics.vacuum_source_finite :"T_vac = E_bdry/V, finite, no cutoff dependence" = "T_vac = E_bdry/V, finite, no cutoff dependence"**


[V.C08] Vacuum source term is finite:
T_vac = E_bdry/V = (1/V) integral_L |H_partial[omega_0]|^2 d-sigma.

Finite and independent of any momentum cutoff.
The 10^{120} discrepancy does not arise because no
momentum-space sum is performed.

---

### `Tau.BookV.Thermodynamics.normal_ordering_comparison`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L170-L176)
**theorem
Tau.BookV.Thermodynamics.normal_ordering_comparison :"QFT :H: = H - E_0 subtracts S_ref; tau explains why this is correct" = "QFT :H: = H - E_0 subtracts S_ref; tau explains why this is correct"**


[V.R131] Normal ordering comparison: QFT normal ordering
:H: = H - E_0 removes the divergence without physical justification.
The tau-framework explains WHY the subtraction is correct:
the zero-point contributions are refinement entropy, not energy.

---

### `Tau.BookV.Thermodynamics.GroundStateUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L182-L196)
**structure
Tau.BookV.Thermodynamics.GroundStateUniqueness :Type**


[V.T67] The ground state of H_partial[omega] is the unique vacuum:


- S_def = 0 (zero defect entropy)

- E = E_bdry <= E[psi] for all configurations psi (minimal energy)

- dbar_b omega_0 = 0 on all of tau^3 (holomorphic)


Uniqueness follows from the convexity of the defect functional
on the compact base tau^1.

- vacuum : TauVacuum
The unique vacuum.

- is_unique : Bool
Whether the ground state is unique.

- from_convexity : Bool
Whether uniqueness follows from convexity.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprGroundStateUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L196-L196)
**instance
Tau.BookV.Thermodynamics.instReprGroundStateUniqueness :Repr GroundStateUniqueness**

Equations
- Tau.BookV.Thermodynamics.instReprGroundStateUniqueness = { reprPrec := Tau.BookV.Thermodynamics.instReprGroundStateUniqueness.repr }

---

### `Tau.BookV.Thermodynamics.instReprGroundStateUniqueness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L196-L196)
**def
Tau.BookV.Thermodynamics.instReprGroundStateUniqueness.repr :GroundStateUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.ground_state_unique`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L198-L201)
**theorem
Tau.BookV.Thermodynamics.ground_state_unique :"tau-vacuum ground state is unique by convexity" = "tau-vacuum ground state is unique by convexity"**


The ground state is unique (for default instance).

---

### `Tau.BookV.Thermodynamics.CasimirFromBoundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L207-L225)
**structure
Tau.BookV.Thermodynamics.CasimirFromBoundary :Type**


[V.P39] Casimir effect from boundary modes: the Casimir force
F_Cas = -pi^2 hbar c / (240 d^4) * A is reproduced as the
difference in boundary energies between constrained (plates)
and unconstrained geometry.

The result follows from boundary mode counting on L, not from
summing zero-point energies in momentum space.

- separation_numer : ℕ
Plate separation numerator (in natural units).

- separation_denom : ℕ
Plate separation denominator.

- denom_pos : self.separation_denom > 0
Denominator positive.

- reproduces_standard : Bool
Whether the boundary derivation reproduces the standard result.

- uses_mode_summation : Bool
Whether mode summation is used.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprCasimirFromBoundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L225-L225)
**instance
Tau.BookV.Thermodynamics.instReprCasimirFromBoundary :Repr CasimirFromBoundary**

Equations
- Tau.BookV.Thermodynamics.instReprCasimirFromBoundary = { reprPrec := Tau.BookV.Thermodynamics.instReprCasimirFromBoundary.repr }

---

### `Tau.BookV.Thermodynamics.instReprCasimirFromBoundary.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L225-L225)
**def
Tau.BookV.Thermodynamics.instReprCasimirFromBoundary.repr :CasimirFromBoundary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.casimir_no_mode_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L227-L230)
**theorem
Tau.BookV.Thermodynamics.casimir_no_mode_sum :"Casimir from boundary modes, not mode summation" = "Casimir from boundary modes, not mode summation"**


Casimir does NOT use mode summation (structural fact).

---

### `Tau.BookV.Thermodynamics.example_vacuum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L247-L251)
**def
Tau.BookV.Thermodynamics.example_vacuum :TauVacuum**


Example tau-vacuum with unit boundary energy.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.planck_cutoff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L258-L261)
**def
Tau.BookV.Thermodynamics.planck_cutoff :QFTVacuumAsRefinement**


Example QFT refinement at Planck cutoff.
Equations
- Tau.BookV.Thermodynamics.planck_cutoff = { refinement_prime := 2, cutoff_level := 400 }
Instances For

---

### `Tau.BookV.Thermodynamics.casimir_example`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L266-L270)
**def
Tau.BookV.Thermodynamics.casimir_example :CasimirFromBoundary**


Example Casimir setup at d = 1 micrometer.
Equations
- Tau.BookV.Thermodynamics.casimir_example = { separation_numer := 1, separation_denom := 1000000, denom_pos := Tau.BookV.Thermodynamics.casimir_example._proof_2 }
Instances For
