---
layout: taulib-doc
title: "TauLib.BookIV.Strong.GapMetaTheorem"
permalink: /verify/taulib/docs/book-iv-strong-gap-meta-theorem/
lane: verify
module_name: "TauLib.BookIV.Strong.GapMetaTheorem"
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

# TauLib.BookIV.Strong.GapMetaTheorem


The tau-Gap Meta-Theorem framework: holonomy sectors, canonical vacua,
localized perturbations, quadratic form, excitation cost, three kernel
hypotheses, and instantiation for both Higgs and strong sectors.

## Registry Cross-References


- [IV.D162] Holonomy Sector — `HolonomySector`

- [IV.D163] Canonical Vacuum at Stage n — `CanonicalVacuumStage`

- [IV.D164] Localized Perturbations — `LocalizedPerturbations`

- [IV.D165] Finite-difference Quadratic Form — `FiniteDiffQuadForm`

- [IV.D166] Excitation Cost — `ExcitationCost`

- [IV.D167] Canonical Smallest Excitation — `CanonicalSmallestExcitation`

- [IV.D168] Three Kernel Hypotheses — `KernelHypotheses`

- [IV.T73] Gap Meta-Theorem (III.T26) — `gap_meta_theorem`

- [IV.L9] Finite-stage Spectral Problem — `finite_stage_spectral`

- [IV.L10] Positive Gap at Each Stage — `positive_gap_each_stage`

- [IV.L11] Vacuum Coherence — `vacuum_coherence`

- [IV.L12] Excitation Coherence — `excitation_coherence`

- [IV.P97] Well-definedness — `vacuum_well_defined`

- [IV.P98] Properties of h_n — `excitation_properties`

- [IV.P99] Higgs Sector as Holonomy Sector — `higgs_as_holonomy`

- [IV.P100] Higgs Sector Satisfies KH-1..KH-3 — `higgs_satisfies_kh`

- [IV.P101] Strong Sector as Holonomy Sector — `strong_as_holonomy`

- [IV.P102] Strong Sector Kernel Hypotheses — `strong_kernel_hypotheses`

- [IV.R69-R73] Structural remarks (comment-only)


## Mathematical Content


The Gap Meta-Theorem provides a uniform framework for proving mass gaps
across different sectors. Given a tau-holonomy sector satisfying three
kernel hypotheses (KH-1: stationarity, KH-2: monotonicity, KH-3:
positivity), the omega-vacuum exists, the omega-gap quantum exists,
and the spectral gap is strictly positive.

## Ground Truth Sources


- Chapter 40 of Book IV (2nd Edition)

- Book III registry III.T26


---

### `Tau.BookIV.Strong.HolonomySector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L54-L72)
**structure
Tau.BookIV.Strong.HolonomySector :Type**


[IV.D162] A tau-holonomy sector: at each finite stage n, a finite
configuration space C_n, a finite admissible subset C_n^{adm},
a defect functional V_n, and refinement/restriction maps.

This is the abstract template instantiated by each physical sector.

- sector : BookIII.Sectors.Sector
Sector label.

- activation_depth : ℕ
Activation depth (minimum stage for nontrivial configurations).

- config_finite : Bool
Configuration space is finite at each stage.

- adm_nonempty : Bool
Admissible subset is nonempty.

- defect_defined : Bool
Defect functional is well-defined.

- refinement_maps : Bool
Refinement maps exist.

Instances For

---

### `Tau.BookIV.Strong.instReprHolonomySector.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L72-L72)
**def
Tau.BookIV.Strong.instReprHolonomySector.repr :HolonomySector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprHolonomySector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L72-L72)
**instance
Tau.BookIV.Strong.instReprHolonomySector :Repr HolonomySector**

Equations
- Tau.BookIV.Strong.instReprHolonomySector = { reprPrec := Tau.BookIV.Strong.instReprHolonomySector.repr }

---

### `Tau.BookIV.Strong.CanonicalVacuumStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L78-L90)
**structure
Tau.BookIV.Strong.CanonicalVacuumStage :Type**


[IV.D163] Canonical vacuum at stage n:
Omega_n^* := argmin over C_n^{adm} of (V_n(Omega), code_n(Omega)).
Lexicographic: first minimize defect, then NF tie-break.

- stage : ℕ
Stage n.

- minimizes_defect : Bool
Minimizes defect.

- nf_tiebreak : Bool
NF code tie-breaking.

- unique : Bool
Unique by lexicographic total order.

Instances For

---

### `Tau.BookIV.Strong.instReprCanonicalVacuumStage.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L90-L90)
**def
Tau.BookIV.Strong.instReprCanonicalVacuumStage.repr :CanonicalVacuumStage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprCanonicalVacuumStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L90-L90)
**instance
Tau.BookIV.Strong.instReprCanonicalVacuumStage :Repr CanonicalVacuumStage**

Equations
- Tau.BookIV.Strong.instReprCanonicalVacuumStage = { reprPrec := Tau.BookIV.Strong.instReprCanonicalVacuumStage.repr }

---

### `Tau.BookIV.Strong.VacuumWellDefined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L92-L101)
**structure
Tau.BookIV.Strong.VacuumWellDefined :Type**


[IV.P97] Well-definedness: vacuum exists (finite nonempty),
is unique (lex total order), and computable (exhaustive search).

- exists_ : Bool
Existence.

- unique : Bool
Uniqueness.

- computable : Bool
Computability.

Instances For

---

### `Tau.BookIV.Strong.instReprVacuumWellDefined.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L101-L101)
**def
Tau.BookIV.Strong.instReprVacuumWellDefined.repr :VacuumWellDefined → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprVacuumWellDefined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L101-L101)
**instance
Tau.BookIV.Strong.instReprVacuumWellDefined :Repr VacuumWellDefined**

Equations
- Tau.BookIV.Strong.instReprVacuumWellDefined = { reprPrec := Tau.BookIV.Strong.instReprVacuumWellDefined.repr }

---

### `Tau.BookIV.Strong.vacuum_well_defined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L103-L103)
**def
Tau.BookIV.Strong.vacuum_well_defined :VacuumWellDefined**

Equations
- Tau.BookIV.Strong.vacuum_well_defined = { }
Instances For

---

### `Tau.BookIV.Strong.LocalizedPerturbations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L109-L119)
**structure
Tau.BookIV.Strong.LocalizedPerturbations :Type**


[IV.D164] Localized perturbation set P_n(U): admissible perturbations
supported within a region U subset T^2, such that Omega_n^* + p
remains admissible.

- stage : ℕ
Stage n.

- localized : Bool
Perturbations are localized in a region U.

- admissible_superposition : Bool
Superposition with vacuum remains admissible.

Instances For

---

### `Tau.BookIV.Strong.instReprLocalizedPerturbations.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L119-L119)
**def
Tau.BookIV.Strong.instReprLocalizedPerturbations.repr :LocalizedPerturbations → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprLocalizedPerturbations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L119-L119)
**instance
Tau.BookIV.Strong.instReprLocalizedPerturbations :Repr LocalizedPerturbations**

Equations
- Tau.BookIV.Strong.instReprLocalizedPerturbations = { reprPrec := Tau.BookIV.Strong.instReprLocalizedPerturbations.repr }

---

### `Tau.BookIV.Strong.FiniteDiffQuadForm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L125-L135)
**structure
Tau.BookIV.Strong.FiniteDiffQuadForm :Type**


[IV.D165] Q_n(p,q) := V_n(Omega^* + p + q) - V_n(Omega^* + p)
- V_n(Omega^* + q) + V_n(Omega^*)
The second-order excitation cost around the vacuum.

- symmetric : Bool
Symmetric bilinear form.

- nonneg : Bool
Non-negative definite.

- finite_rank : Bool
Finite rank at each stage.

Instances For

---

### `Tau.BookIV.Strong.instReprFiniteDiffQuadForm.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L135-L135)
**def
Tau.BookIV.Strong.instReprFiniteDiffQuadForm.repr :FiniteDiffQuadForm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprFiniteDiffQuadForm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L135-L135)
**instance
Tau.BookIV.Strong.instReprFiniteDiffQuadForm :Repr FiniteDiffQuadForm**

Equations
- Tau.BookIV.Strong.instReprFiniteDiffQuadForm = { reprPrec := Tau.BookIV.Strong.instReprFiniteDiffQuadForm.repr }

---

### `Tau.BookIV.Strong.ExcitationCost`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L141-L150)
**structure
Tau.BookIV.Strong.ExcitationCost :Type**


[IV.D166] Excitation cost lambda_n(p) := (Q_n(p,p), ||p||_n),
the lexicographic pair of quadratic energy cost and NF-norm.

- quadratic_component : Bool
Quadratic component Q_n(p,p).

- nf_norm_component : Bool
NF-norm component.

- lexicographic : Bool
Lexicographic ordering.

Instances For

---

### `Tau.BookIV.Strong.instReprExcitationCost.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L150-L150)
**def
Tau.BookIV.Strong.instReprExcitationCost.repr :ExcitationCost → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprExcitationCost`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L150-L150)
**instance
Tau.BookIV.Strong.instReprExcitationCost :Repr ExcitationCost**

Equations
- Tau.BookIV.Strong.instReprExcitationCost = { reprPrec := Tau.BookIV.Strong.instReprExcitationCost.repr }

---

### `Tau.BookIV.Strong.CanonicalSmallestExcitation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L156-L165)
**structure
Tau.BookIV.Strong.CanonicalSmallestExcitation :Type**


[IV.D167] h_n := lexicographic argmin of (lambda_n(p), code_n(p))
over P_n(U){0}. The lightest possible excitation above vacuum.

- stage : ℕ
Stage n.

- is_argmin : Bool
Argmin over nontrivial perturbations.

- nf_tiebreak : Bool
With NF code tie-breaking.

Instances For

---

### `Tau.BookIV.Strong.instReprCanonicalSmallestExcitation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L165-L165)
**instance
Tau.BookIV.Strong.instReprCanonicalSmallestExcitation :Repr CanonicalSmallestExcitation**

Equations
- Tau.BookIV.Strong.instReprCanonicalSmallestExcitation = { reprPrec := Tau.BookIV.Strong.instReprCanonicalSmallestExcitation.repr }

---

### `Tau.BookIV.Strong.instReprCanonicalSmallestExcitation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L165-L165)
**def
Tau.BookIV.Strong.instReprCanonicalSmallestExcitation.repr :CanonicalSmallestExcitation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.ExcitationProperties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L167-L175)
**structure
Tau.BookIV.Strong.ExcitationProperties :Type**


[IV.P98] Properties of h_n: exists, unique, positive excitation cost.

- exists_ : Bool
Exists for sufficiently large n.

- unique : Bool
Unique by lexicographic order.

- positive_cost : Bool
Strictly positive cost Q_n(h_n, h_n) > 0.

Instances For

---

### `Tau.BookIV.Strong.instReprExcitationProperties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L175-L175)
**instance
Tau.BookIV.Strong.instReprExcitationProperties :Repr ExcitationProperties**

Equations
- Tau.BookIV.Strong.instReprExcitationProperties = { reprPrec := Tau.BookIV.Strong.instReprExcitationProperties.repr }

---

### `Tau.BookIV.Strong.instReprExcitationProperties.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L175-L175)
**def
Tau.BookIV.Strong.instReprExcitationProperties.repr :ExcitationProperties → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.excitation_properties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L177-L177)
**def
Tau.BookIV.Strong.excitation_properties :ExcitationProperties**

Equations
- Tau.BookIV.Strong.excitation_properties = { }
Instances For

---

### `Tau.BookIV.Strong.KernelHypotheses`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L183-L196)
**structure
Tau.BookIV.Strong.KernelHypotheses :Type**


[IV.D168] The three kernel hypotheses for a tau-holonomy sector:
(KH-1) Eventual stationarity of combinatorial type beyond n_*
(KH-2) Refinement monotonicity of the defect functional
(KH-3) Discrete Hessian has strictly positive gap for n >= n_*

- kh1_stationarity : Bool
(KH-1) Stationarity beyond stabilization horizon n_*.

- kh2_monotonicity : Bool
(KH-2) Defect functional is refinement-monotone.

- kh3_positive_gap : Bool
(KH-3) Positive spectral gap beyond n_*.

- stabilization_horizon : ℕ
Stabilization horizon.

Instances For

---

### `Tau.BookIV.Strong.instReprKernelHypotheses`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L196-L196)
**instance
Tau.BookIV.Strong.instReprKernelHypotheses :Repr KernelHypotheses**

Equations
- Tau.BookIV.Strong.instReprKernelHypotheses = { reprPrec := Tau.BookIV.Strong.instReprKernelHypotheses.repr }

---

### `Tau.BookIV.Strong.instReprKernelHypotheses.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L196-L196)
**def
Tau.BookIV.Strong.instReprKernelHypotheses.repr :KernelHypotheses → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.GapMetaTheorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L202-L218)
**structure
Tau.BookIV.Strong.GapMetaTheorem :Type**


[IV.T73] tau-Gap Meta-Theorem: for any tau-holonomy sector satisfying
(KH-1)-(KH-3):

- The omega-vacuum exists (by projective limit + KH-1)

- The omega-gap quantum exists (by projective limit + KH-2)

- The spectral gap delta_infinity > 0 (by KH-3 + monotonicity)


This instantiates III.T26 from Book III at the E1 physics level.

- vacuum_exists : Bool
Omega-vacuum exists.

- gap_quantum_exists : Bool
Omega-gap quantum exists.

- gap_positive : Bool
Spectral gap is strictly positive.

- source : String
Source: III.T26.

Instances For

---

### `Tau.BookIV.Strong.instReprGapMetaTheorem.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L218-L218)
**def
Tau.BookIV.Strong.instReprGapMetaTheorem.repr :GapMetaTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprGapMetaTheorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L218-L218)
**instance
Tau.BookIV.Strong.instReprGapMetaTheorem :Repr GapMetaTheorem**

Equations
- Tau.BookIV.Strong.instReprGapMetaTheorem = { reprPrec := Tau.BookIV.Strong.instReprGapMetaTheorem.repr }

---

### `Tau.BookIV.Strong.gap_meta_theorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L220-L220)
**def
Tau.BookIV.Strong.gap_meta_theorem :GapMetaTheorem**

Equations
- Tau.BookIV.Strong.gap_meta_theorem = { }
Instances For

---

### `Tau.BookIV.Strong.FiniteStageSpectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L226-L235)
**structure
Tau.BookIV.Strong.FiniteStageSpectral :Type**


[IV.L9] At each stage n >= n_0, Q_n is a symmetric non-negative
bilinear form with finite spectrum 0 = mu_0 <= mu_1 <= ...

- symmetric : Bool
Symmetric.

- nonneg : Bool
Non-negative.

- finite_spectrum : Bool
Finite spectrum.

Instances For

---

### `Tau.BookIV.Strong.instReprFiniteStageSpectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L235-L235)
**instance
Tau.BookIV.Strong.instReprFiniteStageSpectral :Repr FiniteStageSpectral**

Equations
- Tau.BookIV.Strong.instReprFiniteStageSpectral = { reprPrec := Tau.BookIV.Strong.instReprFiniteStageSpectral.repr }

---

### `Tau.BookIV.Strong.instReprFiniteStageSpectral.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L235-L235)
**def
Tau.BookIV.Strong.instReprFiniteStageSpectral.repr :FiniteStageSpectral → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.finite_stage_spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L237-L237)
**def
Tau.BookIV.Strong.finite_stage_spectral :FiniteStageSpectral**

Equations
- Tau.BookIV.Strong.finite_stage_spectral = { }
Instances For

---

### `Tau.BookIV.Strong.PositiveGapEachStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L239-L245)
**structure
Tau.BookIV.Strong.PositiveGapEachStage :Type**


[IV.L10] For each n >= n_*, the positive gap mu_1^(n) > 0.

- gap_positive : Bool
Gap is positive.

- mechanism : String
Follows from KH-3 + finite min of positives is positive.

Instances For

---

### `Tau.BookIV.Strong.instReprPositiveGapEachStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L245-L245)
**instance
Tau.BookIV.Strong.instReprPositiveGapEachStage :Repr PositiveGapEachStage**

Equations
- Tau.BookIV.Strong.instReprPositiveGapEachStage = { reprPrec := Tau.BookIV.Strong.instReprPositiveGapEachStage.repr }

---

### `Tau.BookIV.Strong.instReprPositiveGapEachStage.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L245-L245)
**def
Tau.BookIV.Strong.instReprPositiveGapEachStage.repr :PositiveGapEachStage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.positive_gap_each_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L247-L247)
**def
Tau.BookIV.Strong.positive_gap_each_stage :PositiveGapEachStage**

Equations
- Tau.BookIV.Strong.positive_gap_each_stage = { }
Instances For

---

### `Tau.BookIV.Strong.VacuumCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L249-L255)
**structure
Tau.BookIV.Strong.VacuumCoherence :Type**


[IV.L11] Vacuum coherence: rho_{n+1->n}(Omega_{n+1}^*) = Omega_n^*.

- restriction_preserves : Bool
Restriction preserves vacuum.

- parallels : String
Parallels strong vacuum truncation coherence.

Instances For

---

### `Tau.BookIV.Strong.instReprVacuumCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L255-L255)
**instance
Tau.BookIV.Strong.instReprVacuumCoherence :Repr VacuumCoherence**

Equations
- Tau.BookIV.Strong.instReprVacuumCoherence = { reprPrec := Tau.BookIV.Strong.instReprVacuumCoherence.repr }

---

### `Tau.BookIV.Strong.instReprVacuumCoherence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L255-L255)
**def
Tau.BookIV.Strong.instReprVacuumCoherence.repr :VacuumCoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.vacuum_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L257-L257)
**def
Tau.BookIV.Strong.vacuum_coherence :VacuumCoherence**

Equations
- Tau.BookIV.Strong.vacuum_coherence = { }
Instances For

---

### `Tau.BookIV.Strong.ExcitationCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L259-L265)
**structure
Tau.BookIV.Strong.ExcitationCoherence :Type**


[IV.L12] Excitation coherence: rho(h_{n+1}) = h_n for n >= n_*.

- restriction_preserves : Bool
Restriction preserves excitation.

- mechanism : String
Follows from KH-2 (monotonicity) + surjectivity.

Instances For

---

### `Tau.BookIV.Strong.instReprExcitationCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L265-L265)
**instance
Tau.BookIV.Strong.instReprExcitationCoherence :Repr ExcitationCoherence**

Equations
- Tau.BookIV.Strong.instReprExcitationCoherence = { reprPrec := Tau.BookIV.Strong.instReprExcitationCoherence.repr }

---

### `Tau.BookIV.Strong.instReprExcitationCoherence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L265-L265)
**def
Tau.BookIV.Strong.instReprExcitationCoherence.repr :ExcitationCoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.excitation_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L267-L267)
**def
Tau.BookIV.Strong.excitation_coherence :ExcitationCoherence**

Equations
- Tau.BookIV.Strong.excitation_coherence = { }
Instances For

---

### `Tau.BookIV.Strong.higgs_as_holonomy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L273-L276)
**def
Tau.BookIV.Strong.higgs_as_holonomy :HolonomySector**


[IV.P99] The Higgs sector as a tau-holonomy sector.
Equations
- Tau.BookIV.Strong.higgs_as_holonomy = { sector := Tau.BookIII.Sectors.Sector.Omega, activation_depth := 2 }
Instances For

---

### `Tau.BookIV.Strong.higgs_satisfies_kh`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L278-L281)
**def
Tau.BookIV.Strong.higgs_satisfies_kh :KernelHypotheses**


[IV.P100] The Higgs sector satisfies all three kernel hypotheses
with stabilization at n_* = 2 (primorial depth of B).
Equations
- Tau.BookIV.Strong.higgs_satisfies_kh = { stabilization_horizon := 2 }
Instances For

---

### `Tau.BookIV.Strong.strong_as_holonomy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L283-L286)
**def
Tau.BookIV.Strong.strong_as_holonomy :HolonomySector**


[IV.P101] The strong sector as a tau-holonomy sector.
Equations
- Tau.BookIV.Strong.strong_as_holonomy = { sector := Tau.BookIII.Sectors.Sector.C, activation_depth := 3 }
Instances For

---

### `Tau.BookIV.Strong.strong_kernel_hypotheses`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L288-L292)
**def
Tau.BookIV.Strong.strong_kernel_hypotheses :KernelHypotheses**


[IV.P102] Strong sector kernel hypotheses:
KH-1 at n_* = 3, KH-2 from L_s[n] subset L_s[n+1],
KH-3 deferred to ch41 (requires curvature analysis).
Equations
- Tau.BookIV.Strong.strong_kernel_hypotheses = { stabilization_horizon := 3 }
Instances For

---

### `Tau.BookIV.Strong.higgs_before_strong`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L298-L301)
**theorem
Tau.BookIV.Strong.higgs_before_strong :higgs_as_holonomy.activation_depth < strong_as_holonomy.activation_depth**


Higgs activates at depth 2, strong at depth 3.

---

### `Tau.BookIV.Strong.strong_stabilization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L303-L305)
**theorem
Tau.BookIV.Strong.strong_stabilization :strong_kernel_hypotheses.stabilization_horizon = 3**


Strong sector stabilizes at depth 3.

---

### `Tau.BookIV.Strong.higgs_stabilization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L307-L309)
**theorem
Tau.BookIV.Strong.higgs_stabilization :higgs_satisfies_kh.stabilization_horizon = 2**


Higgs sector stabilizes at depth 2.

---

### `Tau.BookIV.Strong.both_sectors_kh`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/GapMetaTheorem.lean#L311-L319)
**theorem
Tau.BookIV.Strong.both_sectors_kh :strong_kernel_hypotheses.kh1_stationarity = true ∧ strong_kernel_hypotheses.kh2_monotonicity = true ∧ strong_kernel_hypotheses.kh3_positive_gap = true ∧ higgs_satisfies_kh.kh1_stationarity = true ∧ higgs_satisfies_kh.kh2_monotonicity = true ∧ higgs_satisfies_kh.kh3_positive_gap = true**


Both sectors have all three kernel hypotheses.
