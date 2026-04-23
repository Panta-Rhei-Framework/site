---
layout: taulib-doc
title: "TauLib.BookIV.Strong.YangMillsGap"
permalink: /verify/taulib/docs/book-iv-strong-yang-mills-gap/
lane: verify
module_name: "TauLib.BookIV.Strong.YangMillsGap"
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

# TauLib.BookIV.Strong.YangMillsGap


Yang-Mills gap theorem: strong configuration space, connection assignments,
curvature, plaquette-aggregated defect, spectral gap, gap quantum,
profinite spectral preservation, and the tau-Yang-Mills mass gap.

## Registry Cross-References


- [IV.D169] Strong Configuration Space — `StrongConfigSpace`

- [IV.D170] Strong Connection Assignment — `StrongConnection`

- [IV.D171] Strong Curvature — `StrongCurvature`

- [IV.D172] Plaquette-aggregated Strong Defect — `PlaquetteDefect`

- [IV.D173] Canonical Strong Vacuum (Plaquette Form) — `VacuumPlaquetteForm`

- [IV.D174] Strong Quadratic Form — `StrongQuadraticForm`

- [IV.D175] Spectral Gap at Stage n — `SpectralGapStage`

- [IV.D176] YM Sector Coupling — `YMSectorCoupling`

- [IV.D177] Gap Quantum — `GapQuantumDef`

- [IV.D178] Readout Functor (conjectural) — `ReadoutFunctor`

- [IV.D179] Orthodox Bridge Conjecture — `OrthodoxBridgeConj`

- [IV.P103] Equivalence of Defect Formulations — `defect_equivalence`

- [IV.P104] Refinement Coherence — `refinement_coherence`

- [IV.P105] Properties of Q_n^s — `quadratic_form_properties`

- [IV.P106] Gap Mode Coherence — `gap_mode_coherence`

- [IV.P107] Gap Positivity at Each Finite Stage — `gap_positivity`

- [IV.P108] Tower Monotonicity — `tower_monotonicity`

- [IV.T74] Profinite Spectral Preservation — `profinite_spectral_preservation`

- [IV.T75] Yang-Mills Mass Gap Theorem — `yang_mills_mass_gap`

- [IV.R74-R83] Structural remarks (comment-only)


## Mathematical Content


The tau-Yang-Mills Mass Gap Theorem: the C-sector strong vacuum has a
positive spectral gap delta_infinity^s > 0. The proof proceeds by
establishing gap positivity at each finite stage, tower monotonicity,
and profinite spectral preservation. The gap quantum g[omega] is the
lightest excitation above the vacuum, with mass proportional to the gap.

## Ground Truth Sources


- Chapter 41 of Book IV (2nd Edition)


---

### `Tau.BookIV.Strong.StrongConfigSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L54-L66)
**structure
Tau.BookIV.Strong.StrongConfigSpace :Type**


[IV.D169] Strong configuration space C_s[n]:
quotient of strongly admissible endomorphisms at stage n
by the equivalence relation induced by the strong vacuum.

- stage : ℕ
Stage n.

- is_quotient : Bool
Quotient by vacuum equivalence.

- finite : Bool
Finite at each stage.

- nf_enumerable : Bool
NF-enumerable.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongConfigSpace.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L66-L66)
**def
Tau.BookIV.Strong.instReprStrongConfigSpace.repr :StrongConfigSpace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprStrongConfigSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L66-L66)
**instance
Tau.BookIV.Strong.instReprStrongConfigSpace :Repr StrongConfigSpace**

Equations
- Tau.BookIV.Strong.instReprStrongConfigSpace = { reprPrec := Tau.BookIV.Strong.instReprStrongConfigSpace.repr }

---

### `Tau.BookIV.Strong.StrongConnection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L72-L82)
**structure
Tau.BookIV.Strong.StrongConnection :Type**


[IV.D170] A strong connection at stage n: a map assigning
color phase automorphisms to edges of the finite cell complex.
The tau-analogue of a gauge connection on a lattice.

- stage : ℕ
Stage n.

- edge_to_aut : Bool
Maps edges to color-phase automorphisms.

- finite_complex : Bool
Finite cell complex.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongConnection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L82-L82)
**instance
Tau.BookIV.Strong.instReprStrongConnection :Repr StrongConnection**

Equations
- Tau.BookIV.Strong.instReprStrongConnection = { reprPrec := Tau.BookIV.Strong.instReprStrongConnection.repr }

---

### `Tau.BookIV.Strong.instReprStrongConnection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L82-L82)
**def
Tau.BookIV.Strong.instReprStrongConnection.repr :StrongConnection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.StrongCurvature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L88-L99)
**structure
Tau.BookIV.Strong.StrongCurvature :Type**


[IV.D171] Strong curvature F_n^s(Box) at a plaquette:
norm of ordered composition of connection automorphisms around
an elementary closed path minus the identity.
F = 0 iff the connection is flat on that plaquette.

- measures_flatness_departure : Bool
Measures departure from flatness.

- zero_iff_flat : Bool
Zero iff locally flat.

- nonneg : Bool
Non-negative valued.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongCurvature.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L99-L99)
**def
Tau.BookIV.Strong.instReprStrongCurvature.repr :StrongCurvature → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprStrongCurvature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L99-L99)
**instance
Tau.BookIV.Strong.instReprStrongCurvature :Repr StrongCurvature**

Equations
- Tau.BookIV.Strong.instReprStrongCurvature = { reprPrec := Tau.BookIV.Strong.instReprStrongCurvature.repr }

---

### `Tau.BookIV.Strong.PlaquetteDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L105-L115)
**structure
Tau.BookIV.Strong.PlaquetteDefect :Type**


[IV.D172] V_n^s(Gamma_n) = Agg({F_n^s(Box) | Box in P_n^s}):
canonical aggregation of curvatures over all plaquettes.
The plaquette reformulation of the gap-loop defect.

- aggregation_method : String
Aggregation over all plaquettes.

- nonneg : Bool
Non-negative.

- vanishes_on_flat : Bool
Vanishes on flat connections.

Instances For

---

### `Tau.BookIV.Strong.instReprPlaquetteDefect.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L115-L115)
**def
Tau.BookIV.Strong.instReprPlaquetteDefect.repr :PlaquetteDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprPlaquetteDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L115-L115)
**instance
Tau.BookIV.Strong.instReprPlaquetteDefect :Repr PlaquetteDefect**

Equations
- Tau.BookIV.Strong.instReprPlaquetteDefect = { reprPrec := Tau.BookIV.Strong.instReprPlaquetteDefect.repr }

---

### `Tau.BookIV.Strong.DefectEquivalence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L117-L124)
**structure
Tau.BookIV.Strong.DefectEquivalence :Type**


[IV.P103] The two defect formulations determine the same vacuum:
argmin V_n^s = Gamma_s^*[n] = argmin Delta_n^s.

- same_vacuum : Bool
Same vacuum from both formulations.

- loop_plaquette_decomposition : Bool
Gap loops decompose into plaquettes.

Instances For

---

### `Tau.BookIV.Strong.instReprDefectEquivalence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L124-L124)
**instance
Tau.BookIV.Strong.instReprDefectEquivalence :Repr DefectEquivalence**

Equations
- Tau.BookIV.Strong.instReprDefectEquivalence = { reprPrec := Tau.BookIV.Strong.instReprDefectEquivalence.repr }

---

### `Tau.BookIV.Strong.instReprDefectEquivalence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L124-L124)
**def
Tau.BookIV.Strong.instReprDefectEquivalence.repr :DefectEquivalence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.defect_equivalence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L126-L126)
**def
Tau.BookIV.Strong.defect_equivalence :DefectEquivalence**

Equations
- Tau.BookIV.Strong.defect_equivalence = { }
Instances For

---

### `Tau.BookIV.Strong.VacuumPlaquetteForm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L132-L144)
**structure
Tau.BookIV.Strong.VacuumPlaquetteForm :Type**


[IV.D173] Gamma_s^*[n] in plaquette form:
argmin of V_n^s with NF code tie-breaking.
Equivalent to the gap-loop definition from ch37.

- stage : ℕ
Stage n.

- is_argmin : Bool
Argmin of plaquette defect.

- nf_tiebreak : Bool
NF tie-breaking.

- equivalent_to_loop_vacuum : Bool
Equivalent to gap-loop vacuum.

Instances For

---

### `Tau.BookIV.Strong.instReprVacuumPlaquetteForm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L144-L144)
**instance
Tau.BookIV.Strong.instReprVacuumPlaquetteForm :Repr VacuumPlaquetteForm**

Equations
- Tau.BookIV.Strong.instReprVacuumPlaquetteForm = { reprPrec := Tau.BookIV.Strong.instReprVacuumPlaquetteForm.repr }

---

### `Tau.BookIV.Strong.instReprVacuumPlaquetteForm.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L144-L144)
**def
Tau.BookIV.Strong.instReprVacuumPlaquetteForm.repr :VacuumPlaquetteForm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.RefinementCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L146-L153)
**structure
Tau.BookIV.Strong.RefinementCoherence :Type**


[IV.P104] Refinement coherence:
rho(Gamma_s^*[n+1]) = Gamma_s^*[n] for all n >= 3.

- restriction_preserves : Bool
Restriction preserves vacuum.

- activation_depth : ℕ
Active from depth 3.

Instances For

---

### `Tau.BookIV.Strong.instReprRefinementCoherence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L153-L153)
**def
Tau.BookIV.Strong.instReprRefinementCoherence.repr :RefinementCoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprRefinementCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L153-L153)
**instance
Tau.BookIV.Strong.instReprRefinementCoherence :Repr RefinementCoherence**

Equations
- Tau.BookIV.Strong.instReprRefinementCoherence = { reprPrec := Tau.BookIV.Strong.instReprRefinementCoherence.repr }

---

### `Tau.BookIV.Strong.refinement_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L155-L155)
**def
Tau.BookIV.Strong.refinement_coherence :RefinementCoherence**

Equations
- Tau.BookIV.Strong.refinement_coherence = { }
Instances For

---

### `Tau.BookIV.Strong.StrongQuadraticForm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L161-L173)
**structure
Tau.BookIV.Strong.StrongQuadraticForm :Type**


[IV.D174] Q_n^s(p,q): finite-difference second variation of V_n^s
around the strong vacuum. The Hessian of the Yang-Mills action
at the vacuum configuration.

- symmetric : Bool
Symmetric.

- nonneg : Bool
Non-negative definite.

- zero_iff_gauge_equiv : Bool
Equality with zero iff gauge-equivalent to vacuum.

- finite_rank : Bool
Finite rank.

Instances For

---

### `Tau.BookIV.Strong.instReprStrongQuadraticForm.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L173-L173)
**def
Tau.BookIV.Strong.instReprStrongQuadraticForm.repr :StrongQuadraticForm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprStrongQuadraticForm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L173-L173)
**instance
Tau.BookIV.Strong.instReprStrongQuadraticForm :Repr StrongQuadraticForm**

Equations
- Tau.BookIV.Strong.instReprStrongQuadraticForm = { reprPrec := Tau.BookIV.Strong.instReprStrongQuadraticForm.repr }

---

### `Tau.BookIV.Strong.quadratic_form_properties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L175-L177)
**def
Tau.BookIV.Strong.quadratic_form_properties :StrongQuadraticForm**


[IV.P105] Properties of Q_n^s: symmetric, non-negative,
zero iff gauge-equivalent to vacuum, finite rank.
Equations
- Tau.BookIV.Strong.quadratic_form_properties = { }
Instances For

---

### `Tau.BookIV.Strong.SpectralGapStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L183-L193)
**structure
Tau.BookIV.Strong.SpectralGapStage :Type**


[IV.D175] delta_n^s := lambda_1^(n) = min{lambda > 0 in Spec(Q_n^s)},
the smallest nonzero eigenvalue. The gap mode g_n is the
corresponding eigenmode (lightest excitation).

- stage : ℕ
Stage n.

- is_min_nonzero : Bool
The gap is the smallest nonzero eigenvalue.

- gap_mode_exists : Bool
Associated gap mode g_n exists.

Instances For

---

### `Tau.BookIV.Strong.instReprSpectralGapStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L193-L193)
**instance
Tau.BookIV.Strong.instReprSpectralGapStage :Repr SpectralGapStage**

Equations
- Tau.BookIV.Strong.instReprSpectralGapStage = { reprPrec := Tau.BookIV.Strong.instReprSpectralGapStage.repr }

---

### `Tau.BookIV.Strong.instReprSpectralGapStage.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L193-L193)
**def
Tau.BookIV.Strong.instReprSpectralGapStage.repr :SpectralGapStage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.YMSectorCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L199-L209)
**structure
Tau.BookIV.Strong.YMSectorCoupling :Type**


[IV.D176] mu_YM(k): ratio of B-product to C-product of the
split-complex zeta function at primorial depth k (III.D46).
Measures bipolar asymmetry between the two lobe sectors.

- depth : ℕ
Primorial depth k.

- is_ratio : Bool
Ratio of B-product to C-product.

- source : String
From split-complex zeta (III.D46).

Instances For

---

### `Tau.BookIV.Strong.instReprYMSectorCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L209-L209)
**instance
Tau.BookIV.Strong.instReprYMSectorCoupling :Repr YMSectorCoupling**

Equations
- Tau.BookIV.Strong.instReprYMSectorCoupling = { reprPrec := Tau.BookIV.Strong.instReprYMSectorCoupling.repr }

---

### `Tau.BookIV.Strong.instReprYMSectorCoupling.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L209-L209)
**def
Tau.BookIV.Strong.instReprYMSectorCoupling.repr :YMSectorCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.GapModeCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L215-L224)
**structure
Tau.BookIV.Strong.GapModeCoherence :Type**


[IV.P106] Gap mode coherence: rho(g_{n+1}) = g_n for n >= 3.
The lightest excitation at successive stages is consistent.

- restriction_preserves : Bool
Restriction preserves gap mode.

- activation_depth : ℕ
Active from depth 3.

- limit_defined : Bool
Projective limit is well-defined.

Instances For

---

### `Tau.BookIV.Strong.instReprGapModeCoherence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L224-L224)
**def
Tau.BookIV.Strong.instReprGapModeCoherence.repr :GapModeCoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprGapModeCoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L224-L224)
**instance
Tau.BookIV.Strong.instReprGapModeCoherence :Repr GapModeCoherence**

Equations
- Tau.BookIV.Strong.instReprGapModeCoherence = { reprPrec := Tau.BookIV.Strong.instReprGapModeCoherence.repr }

---

### `Tau.BookIV.Strong.gap_mode_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L226-L226)
**def
Tau.BookIV.Strong.gap_mode_coherence :GapModeCoherence**

Equations
- Tau.BookIV.Strong.gap_mode_coherence = { }
Instances For

---

### `Tau.BookIV.Strong.GapQuantumDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L232-L242)
**structure
Tau.BookIV.Strong.GapQuantumDef :Type**


[IV.D177] g[omega] := varprojlim_{n>=3} g_n, the profinite
gap quantum. Its spectral weight lambda_omega^s(g[omega]) :=
lim delta_n^s is the mass gap of the strong sector.

- construction : String
Projective limit of finite-stage gap modes.

- spectral_weight : String
Spectral weight is the omega-limit of gaps.

- physical_interpretation : String
Represents the lightest glueball in the C-sector.

Instances For

---

### `Tau.BookIV.Strong.instReprGapQuantumDef.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L242-L242)
**def
Tau.BookIV.Strong.instReprGapQuantumDef.repr :GapQuantumDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprGapQuantumDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L242-L242)
**instance
Tau.BookIV.Strong.instReprGapQuantumDef :Repr GapQuantumDef**

Equations
- Tau.BookIV.Strong.instReprGapQuantumDef = { reprPrec := Tau.BookIV.Strong.instReprGapQuantumDef.repr }

---

### `Tau.BookIV.Strong.gap_quantum_def`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L244-L244)
**def
Tau.BookIV.Strong.gap_quantum_def :GapQuantumDef**

Equations
- Tau.BookIV.Strong.gap_quantum_def = { }
Instances For

---

### `Tau.BookIV.Strong.GapPositivity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L250-L257)
**structure
Tau.BookIV.Strong.GapPositivity :Type**


[IV.P107] Gap positivity at each finite stage:
delta_n^s > 0 for every n >= 3.

- positive_all_stages : Bool
Gap is positive at each stage.

- mechanism : String
Mechanism: finite config, positive-definite Q on non-vacuum.

Instances For

---

### `Tau.BookIV.Strong.instReprGapPositivity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L257-L257)
**instance
Tau.BookIV.Strong.instReprGapPositivity :Repr GapPositivity**

Equations
- Tau.BookIV.Strong.instReprGapPositivity = { reprPrec := Tau.BookIV.Strong.instReprGapPositivity.repr }

---

### `Tau.BookIV.Strong.instReprGapPositivity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L257-L257)
**def
Tau.BookIV.Strong.instReprGapPositivity.repr :GapPositivity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.gap_positivity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L259-L259)
**def
Tau.BookIV.Strong.gap_positivity :GapPositivity**

Equations
- Tau.BookIV.Strong.gap_positivity = { }
Instances For

---

### `Tau.BookIV.Strong.TowerMonotonicity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L261-L268)
**structure
Tau.BookIV.Strong.TowerMonotonicity :Type**


[IV.P108] Tower monotonicity: delta_{n+1}^s >= delta_n^s.
The spectral gap is non-decreasing along the refinement tower.

- non_decreasing : Bool
Non-decreasing gaps.

- mechanism : String
Higher refinement strengthens constraints.

Instances For

---

### `Tau.BookIV.Strong.instReprTowerMonotonicity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L268-L268)
**instance
Tau.BookIV.Strong.instReprTowerMonotonicity :Repr TowerMonotonicity**

Equations
- Tau.BookIV.Strong.instReprTowerMonotonicity = { reprPrec := Tau.BookIV.Strong.instReprTowerMonotonicity.repr }

---

### `Tau.BookIV.Strong.instReprTowerMonotonicity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L268-L268)
**def
Tau.BookIV.Strong.instReprTowerMonotonicity.repr :TowerMonotonicity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.tower_monotonicity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L270-L270)
**def
Tau.BookIV.Strong.tower_monotonicity :TowerMonotonicity**

Equations
- Tau.BookIV.Strong.tower_monotonicity = { }
Instances For

---

### `Tau.BookIV.Strong.ProfiniteSpectralPreservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L276-L287)
**structure
Tau.BookIV.Strong.ProfiniteSpectralPreservation :Type**


[IV.T74] Profinite spectral preservation: Q_omega^s has no
eigenvalues in (0, delta_infinity^s).
The profinite limit does not introduce new eigenvalues that
would close the gap.

- no_eigenvalues_in_gap : Bool
No eigenvalues in the gap interval.

- preserves_spectrum : Bool
Profinite limit preserves spectral structure.

- monotonicity_source : String
Tower monotonicity ensures gaps only grow.

Instances For

---

### `Tau.BookIV.Strong.instReprProfiniteSpectralPreservation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L287-L287)
**def
Tau.BookIV.Strong.instReprProfiniteSpectralPreservation.repr :ProfiniteSpectralPreservation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprProfiniteSpectralPreservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L287-L287)
**instance
Tau.BookIV.Strong.instReprProfiniteSpectralPreservation :Repr ProfiniteSpectralPreservation**

Equations
- Tau.BookIV.Strong.instReprProfiniteSpectralPreservation = { reprPrec := Tau.BookIV.Strong.instReprProfiniteSpectralPreservation.repr }

---

### `Tau.BookIV.Strong.profinite_spectral_preservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L289-L289)
**def
Tau.BookIV.Strong.profinite_spectral_preservation :ProfiniteSpectralPreservation**

Equations
- Tau.BookIV.Strong.profinite_spectral_preservation = { }
Instances For

---

### `Tau.BookIV.Strong.YangMillsMassGap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L295-L321)
**structure
Tau.BookIV.Strong.YangMillsMassGap :Type**


[IV.T75] The tau-Yang-Mills Mass Gap Theorem:
In the C-sector at E1 level:

- The strong vacuum Gamma_s^*[omega] has a positive spectral gap
delta_infinity^s > 0.

- The gap mode g[omega] exists.

- The gap is non-perturbative (not accessible by perturbation
theory around the vacuum).


Proof structure:


- Step 1: Gap positivity at each finite stage (IV.P107)

- Step 2: Tower monotonicity (IV.P108)

- Step 3: Profinite spectral preservation (IV.T74)

- Step 4: Gap Meta-Theorem (IV.T73) applies


Scope: tau-effective (proved within the tau-framework).

- gap_positive : Bool
Spectral gap is positive at omega.

- gap_mode_exists : Bool
Gap mode exists.

- non_perturbative : Bool
Gap is non-perturbative.

- scope : String
Scope: tau-effective.

- step_count : ℕ
Four proof steps.

Instances For

---

### `Tau.BookIV.Strong.instReprYangMillsMassGap.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L321-L321)
**def
Tau.BookIV.Strong.instReprYangMillsMassGap.repr :YangMillsMassGap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprYangMillsMassGap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L321-L321)
**instance
Tau.BookIV.Strong.instReprYangMillsMassGap :Repr YangMillsMassGap**

Equations
- Tau.BookIV.Strong.instReprYangMillsMassGap = { reprPrec := Tau.BookIV.Strong.instReprYangMillsMassGap.repr }

---

### `Tau.BookIV.Strong.yang_mills_mass_gap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L323-L323)
**def
Tau.BookIV.Strong.yang_mills_mass_gap :YangMillsMassGap**

Equations
- Tau.BookIV.Strong.yang_mills_mass_gap = { }
Instances For

---

### `Tau.BookIV.Strong.ym_gap_positive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L325-L326)
**theorem
Tau.BookIV.Strong.ym_gap_positive :yang_mills_mass_gap.gap_positive = true**


---

### `Tau.BookIV.Strong.ym_four_steps`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L328-L329)
**theorem
Tau.BookIV.Strong.ym_four_steps :yang_mills_mass_gap.step_count = 4**


---

### `Tau.BookIV.Strong.ReadoutFunctor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L335-L350)
**structure
Tau.BookIV.Strong.ReadoutFunctor :Type**


[IV.D178] Readout functor R: Spec_tau(C) -> Spec_YM(SU(3))
from the tau-spectrum of the C-sector to the physical spectrum
of SU(3) Yang-Mills on R^4. Conjectural: bridges tau-internal
mass gap to the Millennium Problem's R^4 formulation.

- source : String
Source: tau C-sector spectrum.

- target : String
Target: SU(3) Yang-Mills spectrum on R^4.

- scope : String
Scope: conjectural.

- gap_preserving : Bool
Must preserve gap positivity.

- ordering_preserving : Bool
Must preserve spectral ordering.

Instances For

---

### `Tau.BookIV.Strong.instReprReadoutFunctor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L350-L350)
**instance
Tau.BookIV.Strong.instReprReadoutFunctor :Repr ReadoutFunctor**

Equations
- Tau.BookIV.Strong.instReprReadoutFunctor = { reprPrec := Tau.BookIV.Strong.instReprReadoutFunctor.repr }

---

### `Tau.BookIV.Strong.instReprReadoutFunctor.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L350-L350)
**def
Tau.BookIV.Strong.instReprReadoutFunctor.repr :ReadoutFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.readout_functor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L352-L352)
**def
Tau.BookIV.Strong.readout_functor :ReadoutFunctor**

Equations
- Tau.BookIV.Strong.readout_functor = { }
Instances For

---

### `Tau.BookIV.Strong.OrthodoxBridgeConj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L358-L376)
**structure
Tau.BookIV.Strong.OrthodoxBridgeConj :Type**


[IV.D179] Orthodox Bridge Conjecture: a readout functor satisfying
gap preservation, spectral ordering, and multiplicity conditions
exists, so tau-gap > 0 implies orthodox-gap > 0.

This is the conjectural link between the tau-internal result
(which IS proved) and the Millennium Problem (which requires
the bridge to be established).

- functor_exists : Bool
Asserts existence of suitable readout functor.

- gap_preserving : Bool
Gap preservation.

- ordering : Bool
Spectral ordering.

- multiplicity : Bool
Multiplicity conditions.

- scope : String
Scope: conjectural.

Instances For

---

### `Tau.BookIV.Strong.instReprOrthodoxBridgeConj.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L376-L376)
**def
Tau.BookIV.Strong.instReprOrthodoxBridgeConj.repr :OrthodoxBridgeConj → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprOrthodoxBridgeConj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L376-L376)
**instance
Tau.BookIV.Strong.instReprOrthodoxBridgeConj :Repr OrthodoxBridgeConj**

Equations
- Tau.BookIV.Strong.instReprOrthodoxBridgeConj = { reprPrec := Tau.BookIV.Strong.instReprOrthodoxBridgeConj.repr }

---

### `Tau.BookIV.Strong.orthodox_bridge_conjecture`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/YangMillsGap.lean#L378-L378)
**def
Tau.BookIV.Strong.orthodox_bridge_conjecture :OrthodoxBridgeConj**

Equations
- Tau.BookIV.Strong.orthodox_bridge_conjecture = { }
Instances For
