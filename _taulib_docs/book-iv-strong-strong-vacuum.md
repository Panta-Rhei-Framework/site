---
layout: taulib-doc
title: "TauLib.BookIV.Strong.StrongVacuum"
permalink: /verify/taulib/docs/book-iv-strong-strong-vacuum/
lane: verify
module_name: "TauLib.BookIV.Strong.StrongVacuum"
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

# TauLib.BookIV.Strong.StrongVacuum


The C-sector architecture: strong defect functional, strong admissibility,
finite-stage strong vacuum as argmin, profinite limit, truncation coherence,
HolEnd_tau(s), Fix(s), and the canonical strong lift.

## Registry Cross-References


- [IV.D144] The C-sector — `CSectorDef`

- [IV.D145] Strong Loop Class — `StrongLoopClass`

- [IV.D146] Strong Holonomy Defect — `StrongHolonomyDefect`

- [IV.D147] Strong Defect Functional — `StrongDefectFunctional`

- [IV.D148] Strong Admissibility — `StrongAdmissibility`

- [IV.D149] Finite-stage Strong Vacuum — `FiniteStageStrongVacuum`

- [IV.D150] Strong Vacuum (profinite limit) — `StrongVacuumDef`

- [IV.D151] HolEnd_tau(s) — `HolEndStrong`

- [IV.D152] Fix(s) — `FixStrong`

- [IV.D153] Canonical Strong Lift — `CanonicalStrongLift`

- [IV.P80] Spectral Tightening — `spectral_tightening`

- [IV.P81] Finiteness and Decidability — `finiteness_decidability`

- [IV.P82] Loop Class Inclusion — `loop_class_inclusion`

- [IV.P83] Properties of Delta_n^s — `defect_properties`

- [IV.P84] Nonemptiness of Adm_s[n] — `adm_nonempty`

- [IV.P85] Existence and Uniqueness — `vacuum_existence_uniqueness`

- [IV.P86] Structure of Fix(s) — `fix_structure`

- [IV.P87] Properties of Canonical Strong Lift — `lift_properties`

- [IV.T68] Truncation Coherence — `truncation_coherence`

- [IV.R46-R52] Structural remarks (comment-only)


## Mathematical Content


The C-sector is the eta-generator sector at primorial depth d=3 with
chi_minus-dominant polarity and self-coupling kappa(C;3) = iota_tau^3/(1-iota_tau).
The strong defect functional Delta_n^s measures minimal holonomy distortion over
gap loops. The strong vacuum Gamma_s^* is the profinite limit of finite-stage
argmin vacua, with truncation coherence ensuring consistency.

## Ground Truth Sources


- Chapter 37 of Book IV (2nd Edition)

- Book IV registry entries IV.D144-IV.D153, IV.P80-IV.P87, IV.T68


---

### `Tau.BookIV.Strong.CSectorDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L55-L72)
**structure
Tau.BookIV.Strong.CSectorDef :Type**


[IV.D144] The C-sector: E1 instantiation of the eta-generator.
Primorial depth d=3, chi_minus-dominant polarity, fiber T^2 carrier,
self-coupling kappa(C;3) = iota_tau^3/(1-iota_tau).
The (1-iota_tau) denominator is the structural signature of confinement.

- gen : Kernel.Generator
Generator: eta.

- sector : BookIII.Sectors.Sector
Abstract sector label.

- depth : ℕ
Primorial activation depth.

- polarity : Sectors.PolaritySign
Chi-minus dominant polarity.

- coupling_numer : ℕ
Coupling numerator (iota^3 * 10^6, common denom with (10^6 - iota)).

- coupling_denom : ℕ
Coupling denominator (iota_cu_denom * (10^6 - iota)).

Instances For

---

### `Tau.BookIV.Strong.instReprCSectorDef.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L72-L72)
**def
Tau.BookIV.Strong.instReprCSectorDef.repr :CSectorDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprCSectorDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L72-L72)
**instance
Tau.BookIV.Strong.instReprCSectorDef :Repr CSectorDef**

Equations
- Tau.BookIV.Strong.instReprCSectorDef = { reprPrec := Tau.BookIV.Strong.instReprCSectorDef.repr }

---

### `Tau.BookIV.Strong.c_sector_def`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L74-L74)
**def
Tau.BookIV.Strong.c_sector_def :CSectorDef**

Equations
- Tau.BookIV.Strong.c_sector_def = { }
Instances For

---

### `Tau.BookIV.Strong.c_sector_gen`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L76-L77)
**theorem
Tau.BookIV.Strong.c_sector_gen :c_sector_def.gen = Kernel.Generator.eta**


The C-sector has eta generator.

---

### `Tau.BookIV.Strong.c_sector_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L79-L80)
**theorem
Tau.BookIV.Strong.c_sector_depth :c_sector_def.depth = 3**


The C-sector has depth 3.

---

### `Tau.BookIV.Strong.c_sector_polarity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L82-L83)
**theorem
Tau.BookIV.Strong.c_sector_polarity :c_sector_def.polarity = Sectors.PolaritySign.ChiMinus**


The C-sector is chi-minus dominant.

---

### `Tau.BookIV.Strong.SpectralTightening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L89-L102)
**structure
Tau.BookIV.Strong.SpectralTightening :Type**


[IV.P80] Spectral tightening in the C-sector: under refinement rho,
the support of chi_minus-dominant characters shrinks strictly
Supp_{n+1}(chi_minus) subset Supp_n(chi_minus) beyond depth d=3.

This is the structural mechanism that drives confinement:
as refinement proceeds, fewer modes survive chi_minus dominance.

- activation_depth : ℕ
Activation depth beyond which tightening occurs.

- strict_decrease : Bool
Support is strictly decreasing.

- mechanism : String
Tightening is inherited from chi_minus dominance.

Instances For

---

### `Tau.BookIV.Strong.instReprSpectralTightening.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L102-L102)
**def
Tau.BookIV.Strong.instReprSpectralTightening.repr :SpectralTightening → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprSpectralTightening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L102-L102)
**instance
Tau.BookIV.Strong.instReprSpectralTightening :Repr SpectralTightening**

Equations
- Tau.BookIV.Strong.instReprSpectralTightening = { reprPrec := Tau.BookIV.Strong.instReprSpectralTightening.repr }

---

### `Tau.BookIV.Strong.spectral_tightening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L104-L104)
**def
Tau.BookIV.Strong.spectral_tightening :SpectralTightening**

Equations
- Tau.BookIV.Strong.spectral_tightening = { }
Instances For

---

### `Tau.BookIV.Strong.tightening_active_at_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L106-L107)
**theorem
Tau.BookIV.Strong.tightening_active_at_3 :spectral_tightening.activation_depth = 3**


---

### `Tau.BookIV.Strong.StrongLoopClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L113-L127)
**structure
Tau.BookIV.Strong.StrongLoopClass :Type**


[IV.D145] The strong loop class L_s[n] at primorial stage n:
the subset of loops in H_partial[n] satisfying eta-support,
gap-class membership, and nonzero contraction defect conditions.

- stage : ℕ
Primorial stage.

- min_stage : ℕ
Minimum stage for nonemptiness.

- loop_count : ℕ
Number of loops (finite at each stage).

- eta_supported : Bool
Loops have eta-support.

- gap_class : Bool
Loops are gap-class members.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongLoopClass.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L127-L127)
**def
Tau.BookIV.Strong.instReprStrongLoopClass.repr :StrongLoopClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprStrongLoopClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L127-L127)
**instance
Tau.BookIV.Strong.instReprStrongLoopClass :Repr StrongLoopClass**

Equations
- Tau.BookIV.Strong.instReprStrongLoopClass = { reprPrec := Tau.BookIV.Strong.instReprStrongLoopClass.repr }

---

### `Tau.BookIV.Strong.FinitenessDecidability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L129-L138)
**structure
Tau.BookIV.Strong.FinitenessDecidability :Type**


[IV.P81] For each n >= 3, L_s[n] is finite and membership
is decidable from the boundary holonomy data.

- finite_all_stages : Bool
Finiteness holds at all stages >= 3.

- decidable : Bool
Membership is decidable.

- source : String
Source: inherited from finite-dimensionality of H_partial[n].

Instances For

---

### `Tau.BookIV.Strong.instReprFinitenessDecidability.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L138-L138)
**def
Tau.BookIV.Strong.instReprFinitenessDecidability.repr :FinitenessDecidability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprFinitenessDecidability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L138-L138)
**instance
Tau.BookIV.Strong.instReprFinitenessDecidability :Repr FinitenessDecidability**

Equations
- Tau.BookIV.Strong.instReprFinitenessDecidability = { reprPrec := Tau.BookIV.Strong.instReprFinitenessDecidability.repr }

---

### `Tau.BookIV.Strong.finiteness_decidability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L140-L140)
**def
Tau.BookIV.Strong.finiteness_decidability :FinitenessDecidability**

Equations
- Tau.BookIV.Strong.finiteness_decidability = { }
Instances For

---

### `Tau.BookIV.Strong.LoopClassInclusion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L142-L150)
**structure
Tau.BookIV.Strong.LoopClassInclusion :Type**


[IV.P82] Refinement embedding induces injection L_s[n] into L_s[n+1].

- injective : Bool
Injection under refinement.

- no_disappearance : Bool
No loops disappear.

- new_loops_possible : Bool
New loops may appear.

Instances For

---

### `Tau.BookIV.Strong.instReprLoopClassInclusion.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L150-L150)
**def
Tau.BookIV.Strong.instReprLoopClassInclusion.repr :LoopClassInclusion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprLoopClassInclusion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L150-L150)
**instance
Tau.BookIV.Strong.instReprLoopClassInclusion :Repr LoopClassInclusion**

Equations
- Tau.BookIV.Strong.instReprLoopClassInclusion = { reprPrec := Tau.BookIV.Strong.instReprLoopClassInclusion.repr }

---

### `Tau.BookIV.Strong.loop_class_inclusion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L152-L152)
**def
Tau.BookIV.Strong.loop_class_inclusion :LoopClassInclusion**

Equations
- Tau.BookIV.Strong.loop_class_inclusion = { }
Instances For

---

### `Tau.BookIV.Strong.StrongHolonomyDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L158-L168)
**structure
Tau.BookIV.Strong.StrongHolonomyDefect :Type**


[IV.D146] The strong holonomy defect HolDef_{s,n}(f; ell)
measures the norm difference between holonomy of f composed
with a gap loop ell and holonomy of ell alone.

- stage : ℕ
Stage n.

- nonneg : Bool
The defect is non-negative.

- vanishes_on_preservation : Bool
Vanishes when f preserves the gap loop holonomy exactly.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongHolonomyDefect.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L168-L168)
**def
Tau.BookIV.Strong.instReprStrongHolonomyDefect.repr :StrongHolonomyDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprStrongHolonomyDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L168-L168)
**instance
Tau.BookIV.Strong.instReprStrongHolonomyDefect :Repr StrongHolonomyDefect**

Equations
- Tau.BookIV.Strong.instReprStrongHolonomyDefect = { reprPrec := Tau.BookIV.Strong.instReprStrongHolonomyDefect.repr }

---

### `Tau.BookIV.Strong.StrongDefectFunctional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L174-L187)
**structure
Tau.BookIV.Strong.StrongDefectFunctional :Type**


[IV.D147] The strong defect functional Delta_n^s(f):
NFMin-aggregated minimum of holonomy defects over all gap loops.

- stage : ℕ
Stage n.

- aggregation : String
Aggregation method: NFMin.

- nonneg : Bool
Non-negative valued.

- vanishes_on_id : Bool
Vanishes on identity.

- refinement_monotone : Bool
Refinement monotone.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongDefectFunctional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L187-L187)
**instance
Tau.BookIV.Strong.instReprStrongDefectFunctional :Repr StrongDefectFunctional**

Equations
- Tau.BookIV.Strong.instReprStrongDefectFunctional = { reprPrec := Tau.BookIV.Strong.instReprStrongDefectFunctional.repr }

---

### `Tau.BookIV.Strong.instReprStrongDefectFunctional.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L187-L187)
**def
Tau.BookIV.Strong.instReprStrongDefectFunctional.repr :StrongDefectFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.DefectProperties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L189-L196)
**structure
Tau.BookIV.Strong.DefectProperties :Type**


[IV.P83] Properties of Delta_n^s: non-negative, vanishes on id,
finite-valued, refinement-monotone.

- nonneg : Bool
- vanishes_on_id : Bool
- finite_valued : Bool
- refinement_monotone : Bool
Instances For

---

### `Tau.BookIV.Strong.instReprDefectProperties.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L196-L196)
**def
Tau.BookIV.Strong.instReprDefectProperties.repr :DefectProperties → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprDefectProperties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L196-L196)
**instance
Tau.BookIV.Strong.instReprDefectProperties :Repr DefectProperties**

Equations
- Tau.BookIV.Strong.instReprDefectProperties = { reprPrec := Tau.BookIV.Strong.instReprDefectProperties.repr }

---

### `Tau.BookIV.Strong.defect_properties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L198-L198)
**def
Tau.BookIV.Strong.defect_properties :DefectProperties**

Equations
- Tau.BookIV.Strong.defect_properties = { }
Instances For

---

### `Tau.BookIV.Strong.StrongAdmissibility`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L204-L215)
**structure
Tau.BookIV.Strong.StrongAdmissibility :Type**


[IV.D148] Strong admissibility: f in S_n is strongly admissible if
(SA-i) preserves eta-sector chi_minus decomposition,
(SA-ii) respects gap-class loops,
(SA-iii) is boundary-coherent with the refinement tower.

- preserves_chi_minus : Bool
(SA-i) Preserves chi_minus decomposition.

- respects_gap_class : Bool
(SA-ii) Respects gap-class loops.

- boundary_coherent : Bool
(SA-iii) Boundary-coherent with refinement.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongAdmissibility`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L215-L215)
**instance
Tau.BookIV.Strong.instReprStrongAdmissibility :Repr StrongAdmissibility**

Equations
- Tau.BookIV.Strong.instReprStrongAdmissibility = { reprPrec := Tau.BookIV.Strong.instReprStrongAdmissibility.repr }

---

### `Tau.BookIV.Strong.instReprStrongAdmissibility.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L215-L215)
**def
Tau.BookIV.Strong.instReprStrongAdmissibility.repr :StrongAdmissibility → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.AdmNonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L217-L224)
**structure
Tau.BookIV.Strong.AdmNonempty :Type**


[IV.P84] Adm_s[n] is nonempty for every n >= 3:
the identity endomorphism trivially satisfies all conditions.

- witness : String
Witness: identity endomorphism.

- all_stages : Bool
All stages >= 3 have nonempty admissible set.

Instances For

---

### `Tau.BookIV.Strong.instReprAdmNonempty.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L224-L224)
**def
Tau.BookIV.Strong.instReprAdmNonempty.repr :AdmNonempty → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprAdmNonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L224-L224)
**instance
Tau.BookIV.Strong.instReprAdmNonempty :Repr AdmNonempty**

Equations
- Tau.BookIV.Strong.instReprAdmNonempty = { reprPrec := Tau.BookIV.Strong.instReprAdmNonempty.repr }

---

### `Tau.BookIV.Strong.adm_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L226-L226)
**def
Tau.BookIV.Strong.adm_nonempty :AdmNonempty**

Equations
- Tau.BookIV.Strong.adm_nonempty = { }
Instances For

---

### `Tau.BookIV.Strong.FiniteStageStrongVacuum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L232-L243)
**structure
Tau.BookIV.Strong.FiniteStageStrongVacuum :Type**


[IV.D149] The finite-stage strong vacuum Gamma_s^*[n]:
argmin of Delta_n^s over Adm_s[n] with NFMin tie-breaking.

- stage : ℕ
Stage n.

- is_argmin : Bool
Minimizes defect functional.

- nfmin_tiebreak : Bool
NFMin tie-breaking among minimizers.

- unique : Bool
Unique after tie-breaking.

Instances For

---

### `Tau.BookIV.Strong.instReprFiniteStageStrongVacuum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L243-L243)
**instance
Tau.BookIV.Strong.instReprFiniteStageStrongVacuum :Repr FiniteStageStrongVacuum**

Equations
- Tau.BookIV.Strong.instReprFiniteStageStrongVacuum = { reprPrec := Tau.BookIV.Strong.instReprFiniteStageStrongVacuum.repr }

---

### `Tau.BookIV.Strong.instReprFiniteStageStrongVacuum.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L243-L243)
**def
Tau.BookIV.Strong.instReprFiniteStageStrongVacuum.repr :FiniteStageStrongVacuum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.VacuumExistenceUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L245-L254)
**structure
Tau.BookIV.Strong.VacuumExistenceUniqueness :Type**


[IV.P85] Existence and uniqueness at each stage:
exists (finite nonempty domain), unique (NFMin), computable.

- exists_ : Bool
Existence from finiteness + nonemptiness.

- unique : Bool
Uniqueness from NFMin tie-breaking.

- computable : Bool
Computable from boundary holonomy data.

Instances For

---

### `Tau.BookIV.Strong.instReprVacuumExistenceUniqueness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L254-L254)
**def
Tau.BookIV.Strong.instReprVacuumExistenceUniqueness.repr :VacuumExistenceUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprVacuumExistenceUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L254-L254)
**instance
Tau.BookIV.Strong.instReprVacuumExistenceUniqueness :Repr VacuumExistenceUniqueness**

Equations
- Tau.BookIV.Strong.instReprVacuumExistenceUniqueness = { reprPrec := Tau.BookIV.Strong.instReprVacuumExistenceUniqueness.repr }

---

### `Tau.BookIV.Strong.vacuum_existence_uniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L256-L256)
**def
Tau.BookIV.Strong.vacuum_existence_uniqueness :VacuumExistenceUniqueness**

Equations
- Tau.BookIV.Strong.vacuum_existence_uniqueness = { }
Instances For

---

### `Tau.BookIV.Strong.StrongVacuumDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L262-L273)
**structure
Tau.BookIV.Strong.StrongVacuumDef :Type**


[IV.D150] The strong vacuum Gamma_s^*: omega-limit (projective limit)
of finite-stage vacua over n >= 3, in pro-objects of H_partial.

- construction : String
Construction: projective limit.

- category : String
Category: pro-objects of boundary holonomy algebra.

- activation_depth : ℕ
Activation depth.

- well_defined : Bool
Well-defined by truncation coherence.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongVacuumDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L273-L273)
**instance
Tau.BookIV.Strong.instReprStrongVacuumDef :Repr StrongVacuumDef**

Equations
- Tau.BookIV.Strong.instReprStrongVacuumDef = { reprPrec := Tau.BookIV.Strong.instReprStrongVacuumDef.repr }

---

### `Tau.BookIV.Strong.instReprStrongVacuumDef.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L273-L273)
**def
Tau.BookIV.Strong.instReprStrongVacuumDef.repr :StrongVacuumDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.strong_vacuum_def`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L275-L275)
**def
Tau.BookIV.Strong.strong_vacuum_def :StrongVacuumDef**

Equations
- Tau.BookIV.Strong.strong_vacuum_def = { }
Instances For

---

### `Tau.BookIV.Strong.TruncationCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L281-L293)
**structure
Tau.BookIV.Strong.TruncationCoherence :Type**


[IV.T68] Truncation coherence: for all n >= 3, the restriction
of the strong vacuum at stage n+1 to stage n recovers the
strong vacuum at stage n: Gamma_s^*[n+1]|_n = Gamma_s^*[n].

This ensures the projective limit is well-defined.

- activation_depth : ℕ
Coherence holds for all n >= activation_depth.

- restriction_preserves : Bool
Restriction of (n+1)-vacuum equals n-vacuum.

- mechanism : String
Mechanism: argmin + NFMin commute with restriction.

Instances For

---

### `Tau.BookIV.Strong.instReprTruncationCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L293-L293)
**instance
Tau.BookIV.Strong.instReprTruncationCoherence :Repr TruncationCoherence**

Equations
- Tau.BookIV.Strong.instReprTruncationCoherence = { reprPrec := Tau.BookIV.Strong.instReprTruncationCoherence.repr }

---

### `Tau.BookIV.Strong.instReprTruncationCoherence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L293-L293)
**def
Tau.BookIV.Strong.instReprTruncationCoherence.repr :TruncationCoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.truncation_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L295-L295)
**def
Tau.BookIV.Strong.truncation_coherence :TruncationCoherence**

Equations
- Tau.BookIV.Strong.truncation_coherence = { }
Instances For

---

### `Tau.BookIV.Strong.truncation_active_at_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L297-L298)
**theorem
Tau.BookIV.Strong.truncation_active_at_3 :truncation_coherence.activation_depth = 3**


---

### `Tau.BookIV.Strong.HolEndStrong`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L304-L316)
**structure
Tau.BookIV.Strong.HolEndStrong :Type**


[IV.D151] HolEnd_tau(s)[n]: space of strong-admissible boundary
endomorphisms satisfying vacuum preservation (H-i),
holonomy compatibility (H-ii), boundary coherence (H-iii).

- stage : ℕ
Stage n.

- vacuum_preserving : Bool
(H-i) Vacuum preservation.

- holonomy_compatible : Bool
(H-ii) Holonomy compatibility.

- boundary_coherent : Bool
(H-iii) Boundary coherence.

Instances For

---

### `Tau.BookIV.Strong.instReprHolEndStrong.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L316-L316)
**def
Tau.BookIV.Strong.instReprHolEndStrong.repr :HolEndStrong → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprHolEndStrong`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L316-L316)
**instance
Tau.BookIV.Strong.instReprHolEndStrong :Repr HolEndStrong**

Equations
- Tau.BookIV.Strong.instReprHolEndStrong = { reprPrec := Tau.BookIV.Strong.instReprHolEndStrong.repr }

---

### `Tau.BookIV.Strong.FixStrong`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L322-L333)
**structure
Tau.BookIV.Strong.FixStrong :Type**


[IV.D152] Fix(s)[n]: fixed-point subobject of HolEnd_tau(s)[n]
consisting of endomorphisms commuting with the strong vacuum.

- stage : ℕ
Stage n.

- commutes_with_vacuum : Bool
Commutes with strong vacuum.

- contains_id : Bool
Contains the identity.

- is_subalgebra : Bool
Is a subalgebra.

Instances For

---

### `Tau.BookIV.Strong.instReprFixStrong`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L333-L333)
**instance
Tau.BookIV.Strong.instReprFixStrong :Repr FixStrong**

Equations
- Tau.BookIV.Strong.instReprFixStrong = { reprPrec := Tau.BookIV.Strong.instReprFixStrong.repr }

---

### `Tau.BookIV.Strong.instReprFixStrong.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L333-L333)
**def
Tau.BookIV.Strong.instReprFixStrong.repr :FixStrong → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.FixStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L335-L346)
**structure
Tau.BookIV.Strong.FixStructure :Type**


[IV.P86] Fix(s)[n] is a subalgebra containing the identity;
its omega-limit Fix(s) is a well-defined pro-algebra.

- subalgebra : Bool
Subalgebra of End(H_partial[n])_eta.

- contains_id : Bool
Contains identity.

- omega_limit_defined : Bool
Omega-limit is well-defined.

- symmetry_role : String
Encodes symmetries commuting with strong vacuum.

Instances For

---

### `Tau.BookIV.Strong.instReprFixStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L346-L346)
**instance
Tau.BookIV.Strong.instReprFixStructure :Repr FixStructure**

Equations
- Tau.BookIV.Strong.instReprFixStructure = { reprPrec := Tau.BookIV.Strong.instReprFixStructure.repr }

---

### `Tau.BookIV.Strong.instReprFixStructure.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L346-L346)
**def
Tau.BookIV.Strong.instReprFixStructure.repr :FixStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.fix_structure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L348-L348)
**def
Tau.BookIV.Strong.fix_structure :FixStructure**

Equations
- Tau.BookIV.Strong.fix_structure = { }
Instances For

---

### `Tau.BookIV.Strong.CanonicalStrongLift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L354-L367)
**structure
Tau.BookIV.Strong.CanonicalStrongLift :Type**


[IV.D153] Canonical strong lift Lift_{s,n}: NFMin-minimal element
of HolEnd_tau(s)[n] achieving the same defect as the vacuum.
Omega-limit Lift_s = varprojlim Lift_{s,n} is the simplest
endomorphism preserving the strong vacuum.

- stage : ℕ
Stage n.

- achieves_vacuum_defect : Bool
Achieves vacuum defect value.

- nfmin_minimal : Bool
NFMin-minimal among candidates.

- truncation_coherent : Bool
Truncation coherent.

Instances For

---

### `Tau.BookIV.Strong.instReprCanonicalStrongLift.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L367-L367)
**def
Tau.BookIV.Strong.instReprCanonicalStrongLift.repr :CanonicalStrongLift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprCanonicalStrongLift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L367-L367)
**instance
Tau.BookIV.Strong.instReprCanonicalStrongLift :Repr CanonicalStrongLift**

Equations
- Tau.BookIV.Strong.instReprCanonicalStrongLift = { reprPrec := Tau.BookIV.Strong.instReprCanonicalStrongLift.repr }

---

### `Tau.BookIV.Strong.LiftProperties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L369-L380)
**structure
Tau.BookIV.Strong.LiftProperties :Type**


[IV.P87] Properties of the canonical strong lift:
exists for all n >= 3, unique, truncation coherent, computable.

- exists_all_stages : Bool
Exists for all stages >= 3.

- unique : Bool
Unique after NF tie-breaking.

- truncation_coherent : Bool
Truncation coherent: Lift_{s,n+1}|*n = Lift*{s,n}.

- computable : Bool
Computable from boundary holonomy data.

Instances For

---

### `Tau.BookIV.Strong.instReprLiftProperties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L380-L380)
**instance
Tau.BookIV.Strong.instReprLiftProperties :Repr LiftProperties**

Equations
- Tau.BookIV.Strong.instReprLiftProperties = { reprPrec := Tau.BookIV.Strong.instReprLiftProperties.repr }

---

### `Tau.BookIV.Strong.instReprLiftProperties.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L380-L380)
**def
Tau.BookIV.Strong.instReprLiftProperties.repr :LiftProperties → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.lift_properties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L382-L382)
**def
Tau.BookIV.Strong.lift_properties :LiftProperties**

Equations
- Tau.BookIV.Strong.lift_properties = { }
Instances For

---

### `Tau.BookIV.Strong.kappa_C_matches_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L394-L397)
**theorem
Tau.BookIV.Strong.kappa_C_matches_sector :Sectors.strong_sector.coupling_numer = Tau.BookIV.Strong.kappa_C_numer✝ ∧ Sectors.strong_sector.coupling_denom = Tau.BookIV.Strong.kappa_C_denom✝**


---

### `Tau.BookIV.Strong.kappa_C_positive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L399-L402)
**theorem
Tau.BookIV.Strong.kappa_C_positive :Tau.BookIV.Strong.kappa_C_numer✝ > 0**


kappa(C;3) > 0.

---

### `Tau.BookIV.Strong.opposite_denom_contrast`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongVacuum.lean#L404-L412)
**theorem
Tau.BookIV.Strong.opposite_denom_contrast :Sectors.strong_sector.coupling_numer = Sectors.higgs_sector.coupling_numer ∧ Sectors.strong_sector.coupling_denom ≠ Sectors.higgs_sector.coupling_denom**


The omega-sector coupling has the same numerator but different denominator.
kappa(omega) = iota^3/(1+iota) vs kappa(C) = iota^3/(1-iota).
The (1-iota) vs (1+iota) produces confinement vs stabilization.
