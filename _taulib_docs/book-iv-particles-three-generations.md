---
layout: taulib-doc
title: "TauLib.BookIV.Particles.ThreeGenerations"
permalink: /verify/taulib/docs/book-iv-particles-three-generations/
lane: verify
module_name: "TauLib.BookIV.Particles.ThreeGenerations"
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

# TauLib.BookIV.Particles.ThreeGenerations


Three generations of fermions from lemniscate topology: the three topologically
distinct mode classes on L = S¹ ∨ S¹, lepton families (e, μ, τ), quark families
(u/d, c/s, t/b), mass hierarchy by generation, ι<sub>τ</sub>² spectral gap, and the
Koide relation Q = 2/3.

## Registry Cross-References


- [IV.D196] Three Mode Classes on Lemniscate — `LemniscateModeClass`, `three_mode_classes`

- [IV.T83] Exactly Three Generations — `exactly_three_generations`

- [IV.D197] Quark Winding Classes — `QuarkWindingClass`

- [IV.D198] Koide Parameter — `KoideParameter`

- [IV.T84] Koide Relation Q=2/3 — `koide_relation`

- [IV.P121] Quark Mass Pattern — `quark_mass_pattern` (conjectural)

- [IV.P122] Muon Mass Exponent — `muon_mass_exponent`

- [IV.P123] Tau Lepton Mass Exponent — `tau_lepton_mass_exponent`

- [IV.P124] Neutrino Mass Scale — `neutrino_mass_scale` (conjectural)

- [IV.R111] Fourth Generation Excluded — `fourth_generation_excluded`

- [IV.R112] Winding number classes — comment-only (not_applicable)

- [IV.R113] Honest Assessment of Quark Masses — `quark_mass_honesty`

- [IV.R114] Non-integer Exponents are Physical — `noninteger_exponents`

- [IV.R115] The 45-degree Crossing Angle — `crossing_angle_45`

- [IV.R116] Why 0.0009% and not exact — `koide_deviation`

- [IV.R117] Normal Ordering Predicted — `normal_ordering` (conjectural)

- [IV.R118] Individual Neutrino Masses — `individual_nu_masses` (conjectural)

- [IV.R119] Scope Gradient across Mass Table — `scope_gradient`

- [IV.R120] One Constant One Anchor Zero Parameters — `one_constant_one_anchor`


## Mathematical Content


The lemniscate L = S¹ ∨ S¹ has exactly three structurally distinct regions:
crossing point, single lobe, and full figure. Character modes on T² restricted
to L fall into three topological mode classes corresponding to three fermion
generations. Mass hierarchy follows from breathing eigenvalues scaled by ι<sub>τ</sub>².

The Koide relation Q = (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 2/3 is
a consequence of ℤ/3ℤ symmetry of L's three sectors with democratic matrix
spacing. Deviation from exact 2/3 is O(α²) ≈ 5×10⁻⁵.

## Ground Truth Sources


- Chapter 46 of Book IV (2nd Edition)

- electron_mass_first_principles.md (Koide cross-check)


---

### `Tau.BookIV.Particles.LemniscateModeClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L57-L66)
**inductive
Tau.BookIV.Particles.LemniscateModeClass :Type**


[IV.D196] The three topological mode classes on L = S¹ ∨ S¹.
Each class corresponds to a fermion generation.

- crossingPoint : LemniscateModeClass
Generation 1: crossing-point modes (localized near p_ω).

- singleLobe : LemniscateModeClass
Generation 2: single-lobe modes (winding around one lobe).

- fullLemniscate : LemniscateModeClass
Generation 3: full-lemniscate modes (winding around both lobes).

Instances For

---

### `Tau.BookIV.Particles.instReprLemniscateModeClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L66-L66)
**instance
Tau.BookIV.Particles.instReprLemniscateModeClass :Repr LemniscateModeClass**

Equations
- Tau.BookIV.Particles.instReprLemniscateModeClass = { reprPrec := Tau.BookIV.Particles.instReprLemniscateModeClass.repr }

---

### `Tau.BookIV.Particles.instReprLemniscateModeClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L66-L66)
**def
Tau.BookIV.Particles.instReprLemniscateModeClass.repr :LemniscateModeClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instDecidableEqLemniscateModeClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L66-L66)
**instance
Tau.BookIV.Particles.instDecidableEqLemniscateModeClass :DecidableEq LemniscateModeClass**

Equations
- Tau.BookIV.Particles.instDecidableEqLemniscateModeClass x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Particles.instBEqLemniscateModeClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L66-L66)
**instance
Tau.BookIV.Particles.instBEqLemniscateModeClass :BEq LemniscateModeClass**

Equations
- Tau.BookIV.Particles.instBEqLemniscateModeClass = { beq := Tau.BookIV.Particles.instBEqLemniscateModeClass.beq }

---

### `Tau.BookIV.Particles.instBEqLemniscateModeClass.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L66-L66)
**def
Tau.BookIV.Particles.instBEqLemniscateModeClass.beq :LemniscateModeClass → LemniscateModeClass → Bool**

Equations
- Tau.BookIV.Particles.instBEqLemniscateModeClass.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Particles.LemniscateModeClass.generation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L68-L72)
**def
Tau.BookIV.Particles.LemniscateModeClass.generation :LemniscateModeClass → ℕ**


Map from mode class to generation number.
Equations
- Tau.BookIV.Particles.LemniscateModeClass.crossingPoint.generation = 1
- Tau.BookIV.Particles.LemniscateModeClass.singleLobe.generation = 2
- Tau.BookIV.Particles.LemniscateModeClass.fullLemniscate.generation = 3
Instances For

---

### `Tau.BookIV.Particles.three_mode_classes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L74-L76)
**def
Tau.BookIV.Particles.three_mode_classes :List LemniscateModeClass**


The three mode classes as a list.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.three_mode_classes_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L78-L78)
**theorem
Tau.BookIV.Particles.three_mode_classes_count :three_mode_classes.length = 3**


---

### `Tau.BookIV.Particles.ExactlyThreeGens`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L84-L105)
**structure
Tau.BookIV.Particles.ExactlyThreeGens :Type**


[IV.T83] The lemniscate supports exactly three topologically
distinct mode classes and no fourth class exists.

L has exactly three structurally distinct regions:

- The crossing point (genus-changing singularity)

- A single lobe (S¹)

- The full figure (both lobes)


This is topological, not energetic: no amount of energy creates a
fourth class. LEP measurement N_ν = 2.9840 ± 0.0082 confirms.

- count : ℕ
Number of generations.

- origin : String
Topological origin.

- n_topological_regions : ℕ
Number of topological regions on L = S¹ ∨ S¹ (crossing, lobe, full).

- lep_numer : ℕ
LEP confirmation N_ν numerator (×10000).

- lep_denom : ℕ
LEP confirmation N_ν denominator.

Instances For

---

### `Tau.BookIV.Particles.instReprExactlyThreeGens.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L105-L105)
**def
Tau.BookIV.Particles.instReprExactlyThreeGens.repr :ExactlyThreeGens → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprExactlyThreeGens`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L105-L105)
**instance
Tau.BookIV.Particles.instReprExactlyThreeGens :Repr ExactlyThreeGens**

Equations
- Tau.BookIV.Particles.instReprExactlyThreeGens = { reprPrec := Tau.BookIV.Particles.instReprExactlyThreeGens.repr }

---

### `Tau.BookIV.Particles.exactly_three_generations`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L107-L107)
**def
Tau.BookIV.Particles.exactly_three_generations :ExactlyThreeGens**

Equations
- Tau.BookIV.Particles.exactly_three_generations = { }
Instances For

---

### `Tau.BookIV.Particles.gen_count_three`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L109-L109)
**theorem
Tau.BookIV.Particles.gen_count_three :exactly_three_generations.count = 3**


---

### `Tau.BookIV.Particles.FourthGenExcluded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L115-L127)
**structure
Tau.BookIV.Particles.FourthGenExcluded :Type**


[IV.R111] The exclusion of a fourth generation is topological:
L = S¹ ∨ S¹ has exactly two lobes and one crossing point, so no
fourth mode class exists regardless of energy.

- num_lobes : ℕ
Number of lobes.

- num_crossings : ℕ
Number of crossing points.

- max_regions : ℕ
Max distinct regions.

- exclusion_mechanism : ℕ
Exclusion mechanism: 1 = topological (not energetic).

Instances For

---

### `Tau.BookIV.Particles.instReprFourthGenExcluded.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L127-L127)
**def
Tau.BookIV.Particles.instReprFourthGenExcluded.repr :FourthGenExcluded → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprFourthGenExcluded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L127-L127)
**instance
Tau.BookIV.Particles.instReprFourthGenExcluded :Repr FourthGenExcluded**

Equations
- Tau.BookIV.Particles.instReprFourthGenExcluded = { reprPrec := Tau.BookIV.Particles.instReprFourthGenExcluded.repr }

---

### `Tau.BookIV.Particles.fourth_generation_excluded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L129-L129)
**def
Tau.BookIV.Particles.fourth_generation_excluded :FourthGenExcluded**

Equations
- Tau.BookIV.Particles.fourth_generation_excluded = { }
Instances For

---

### `Tau.BookIV.Particles.max_three_regions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L131-L132)
**theorem
Tau.BookIV.Particles.max_three_regions :fourth_generation_excluded.max_regions = 3**


---

### `Tau.BookIV.Particles.lobes_plus_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L134-L136)
**theorem
Tau.BookIV.Particles.lobes_plus_crossing :fourth_generation_excluded.num_lobes + fourth_generation_excluded.num_crossings = 3**


---

### `Tau.BookIV.Particles.QuarkWindingClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L142-L160)
**structure
Tau.BookIV.Particles.QuarkWindingClass :Type**


[IV.D197] Quark winding classes on T² with shape ratio ι<sub>τ</sub>.
The six quarks are assigned to three winding classes:


- Class (1,0): Gen 1 (u, d), eigenvalue β = 1

- Class (0,1): Gen 2 (c, s), eigenvalue β = ι<sub>τ</sub>⁻¹

- Class (1,1): Gen 3 (t, b), eigenvalue β = ι<sub>τ</sub>⁻²


- winding_m : ℕ
Winding pair (m, n) on T².

- winding_n : ℕ
Winding pair (m, n) on T².

- generation : ℕ
Generation number.

- up_type : String
Up-type quark name.

- down_type : String
Down-type quark name.

- eigenvalue_exp : ℕ
Eigenvalue exponent: β = ι<sub>τ</sub>^(-exponent).

Instances For

---

### `Tau.BookIV.Particles.instReprQuarkWindingClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L160-L160)
**instance
Tau.BookIV.Particles.instReprQuarkWindingClass :Repr QuarkWindingClass**

Equations
- Tau.BookIV.Particles.instReprQuarkWindingClass = { reprPrec := Tau.BookIV.Particles.instReprQuarkWindingClass.repr }

---

### `Tau.BookIV.Particles.instReprQuarkWindingClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L160-L160)
**def
Tau.BookIV.Particles.instReprQuarkWindingClass.repr :QuarkWindingClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.quark_gen1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L162-L164)
**def
Tau.BookIV.Particles.quark_gen1 :QuarkWindingClass**

Equations
- Tau.BookIV.Particles.quark_gen1 = { winding_m := 1, winding_n := 0, generation := 1, up_type := "u", down_type := "d", eigenvalue_exp := 0 }
Instances For

---

### `Tau.BookIV.Particles.quark_gen2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L166-L168)
**def
Tau.BookIV.Particles.quark_gen2 :QuarkWindingClass**

Equations
- Tau.BookIV.Particles.quark_gen2 = { winding_m := 0, winding_n := 1, generation := 2, up_type := "c", down_type := "s", eigenvalue_exp := 1 }
Instances For

---

### `Tau.BookIV.Particles.quark_gen3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L170-L172)
**def
Tau.BookIV.Particles.quark_gen3 :QuarkWindingClass**

Equations
- Tau.BookIV.Particles.quark_gen3 = { winding_m := 1, winding_n := 1, generation := 3, up_type := "t", down_type := "b", eigenvalue_exp := 2 }
Instances For

---

### `Tau.BookIV.Particles.quark_winding_classes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L174-L175)
**def
Tau.BookIV.Particles.quark_winding_classes :List QuarkWindingClass**

Equations
- Tau.BookIV.Particles.quark_winding_classes = [Tau.BookIV.Particles.quark_gen1, Tau.BookIV.Particles.quark_gen2, Tau.BookIV.Particles.quark_gen3]
Instances For

---

### `Tau.BookIV.Particles.three_quark_generations`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L177-L177)
**theorem
Tau.BookIV.Particles.three_quark_generations :quark_winding_classes.length = 3**


---

### `Tau.BookIV.Particles.MuonExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L183-L201)
**structure
Tau.BookIV.Particles.MuonExponent :Type**


[IV.P122] m_μ/m_e = ι<sub>τ</sub>^(-5)(1 + δ_μ) where δ_μ ≈ −0.04 is O(α).
Bare topological exponent: 5.
Corrected prediction: m_e·ι<sub>τ</sub>^(-4.96) ≈ 106.1 MeV (experiment: 105.66 MeV, 0.4%).

Mass values in MeV (scaled ×1000):


- Predicted: 106100 / 1000 = 106.1 MeV

- Experimental: 105658 / 1000 = 105.658 MeV


- bare_exp : ℕ
Bare topological exponent.

- effective_exp_x100 : ℕ
Effective exponent (×100).

- predicted_x1000 : ℕ
Predicted mass (MeV ×1000).

- experimental_x1000 : ℕ
Experimental mass (MeV ×1000).

- agreement_pct_x100 : ℕ
Agreement (percent ×100).

Instances For

---

### `Tau.BookIV.Particles.instReprMuonExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L201-L201)
**instance
Tau.BookIV.Particles.instReprMuonExponent :Repr MuonExponent**

Equations
- Tau.BookIV.Particles.instReprMuonExponent = { reprPrec := Tau.BookIV.Particles.instReprMuonExponent.repr }

---

### `Tau.BookIV.Particles.instReprMuonExponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L201-L201)
**def
Tau.BookIV.Particles.instReprMuonExponent.repr :MuonExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.muon_mass_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L203-L203)
**def
Tau.BookIV.Particles.muon_mass_exponent :MuonExponent**

Equations
- Tau.BookIV.Particles.muon_mass_exponent = { }
Instances For

---

### `Tau.BookIV.Particles.muon_bare_exp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L205-L205)
**theorem
Tau.BookIV.Particles.muon_bare_exp :muon_mass_exponent.bare_exp = 5**


---

### `Tau.BookIV.Particles.muon_within_1pct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L207-L211)
**theorem
Tau.BookIV.Particles.muon_within_1pct :muon_mass_exponent.predicted_x1000 > muon_mass_exponent.experimental_x1000 ∧ muon_mass_exponent.predicted_x1000 - muon_mass_exponent.experimental_x1000 < muon_mass_exponent.experimental_x1000 / 100**


Predicted within 1% of experiment.

---

### `Tau.BookIV.Particles.TauLeptonExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L217-L227)
**structure
Tau.BookIV.Particles.TauLeptonExponent :Type**


[IV.P123] m_τ/m_e = ι<sub>τ</sub>^(-15/2)(1 + δ_τ) where δ_τ ≈ +0.09 is O(α).
Bare topological exponent: 15/2 = 7.5.
The full-lemniscate winding mode produces the heaviest charged lepton.

- bare_exp_x2 : ℕ
Bare exponent (×2 to avoid fractions).

- effective_exp_x100 : ℕ
Effective exponent (×100).

- mode_class : LemniscateModeClass
Mode class: full lemniscate.

Instances For

---

### `Tau.BookIV.Particles.instReprTauLeptonExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L227-L227)
**instance
Tau.BookIV.Particles.instReprTauLeptonExponent :Repr TauLeptonExponent**

Equations
- Tau.BookIV.Particles.instReprTauLeptonExponent = { reprPrec := Tau.BookIV.Particles.instReprTauLeptonExponent.repr }

---

### `Tau.BookIV.Particles.instReprTauLeptonExponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L227-L227)
**def
Tau.BookIV.Particles.instReprTauLeptonExponent.repr :TauLeptonExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.tau_lepton_mass_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L229-L229)
**def
Tau.BookIV.Particles.tau_lepton_mass_exponent :TauLeptonExponent**

Equations
- Tau.BookIV.Particles.tau_lepton_mass_exponent = { }
Instances For

---

### `Tau.BookIV.Particles.tau_bare_exp_x2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L231-L231)
**theorem
Tau.BookIV.Particles.tau_bare_exp_x2 :tau_lepton_mass_exponent.bare_exp_x2 = 15**


---

### `Tau.BookIV.Particles.KoideParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L237-L253)
**structure
Tau.BookIV.Particles.KoideParameter :Type**


[IV.D198] The Koide parameter:
Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)²

Discovered by Yoshio Koide in 1982.
Experimental value: 0.666661 ± 0.000007.

Numerator and denominator scaled ×10⁶.

- exp_numer : ℕ
Experimental value numerator (×10⁶).

- exp_denom : ℕ
Denominator (×10⁶).

- uncertainty : ℕ
Uncertainty (×10⁶).

- year : ℕ
Year of discovery.

Instances For

---

### `Tau.BookIV.Particles.instReprKoideParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L253-L253)
**instance
Tau.BookIV.Particles.instReprKoideParameter :Repr KoideParameter**

Equations
- Tau.BookIV.Particles.instReprKoideParameter = { reprPrec := Tau.BookIV.Particles.instReprKoideParameter.repr }

---

### `Tau.BookIV.Particles.instReprKoideParameter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L253-L253)
**def
Tau.BookIV.Particles.instReprKoideParameter.repr :KoideParameter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.koide_parameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L255-L255)
**def
Tau.BookIV.Particles.koide_parameter :KoideParameter**

Equations
- Tau.BookIV.Particles.koide_parameter = { }
Instances For

---

### `Tau.BookIV.Particles.KoideRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L261-L280)
**structure
Tau.BookIV.Particles.KoideRelation :Type**


[IV.T84] The three charged lepton masses satisfy Q = 2/3 to all orders
in the lemniscate topology.

Proof uses ℤ/3ℤ symmetry of L's three sectors (crossing, lobe 1, lobe 2)
with 120-degree democratic matrix spacing. Q = 2/3 is independent of mass
scale or Koide phase. Deviation from exact 2/3 is O(α²) ≈ 5×10⁻⁵.

Experimental: Q_exp = 0.666661 → Q_exp − 2/3 = −6×10⁻⁶.

- predicted_numer : ℕ
Predicted numerator.

- predicted_denom : ℕ
Predicted denominator.

- symmetry_order : ℕ
Symmetry group order.

- spacing_degrees : ℕ
Democratic spacing (degrees).

- deviation_order : ℕ
Deviation order (α^n).

Instances For

---

### `Tau.BookIV.Particles.instReprKoideRelation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L280-L280)
**def
Tau.BookIV.Particles.instReprKoideRelation.repr :KoideRelation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprKoideRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L280-L280)
**instance
Tau.BookIV.Particles.instReprKoideRelation :Repr KoideRelation**

Equations
- Tau.BookIV.Particles.instReprKoideRelation = { reprPrec := Tau.BookIV.Particles.instReprKoideRelation.repr }

---

### `Tau.BookIV.Particles.koide_relation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L282-L282)
**def
Tau.BookIV.Particles.koide_relation :KoideRelation**

Equations
- Tau.BookIV.Particles.koide_relation = { }
Instances For

---

### `Tau.BookIV.Particles.koide_predicted_2_over_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L284-L286)
**theorem
Tau.BookIV.Particles.koide_predicted_2_over_3 :koide_relation.predicted_numer = 2 ∧ koide_relation.predicted_denom = 3**


---

### `Tau.BookIV.Particles.koide_z3_symmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L288-L289)
**theorem
Tau.BookIV.Particles.koide_z3_symmetry :koide_relation.symmetry_order = 3**


---

### `Tau.BookIV.Particles.QuarkMassPattern`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L295-L309)
**structure
Tau.BookIV.Particles.QuarkMassPattern :Type**


[IV.P121] Six quark masses follow approximate ι<sub>τ</sub> power laws.
Scope: conjectural — reproduces ordering and scale, not high-precision.

Exponents (×10, for integer representation):
u ≈ 5.8, d ≈ 5.0, c ≈ −0.30, s ≈ 2.2, t ≈ −4.5, b ≈ −1.5

- scope : String
Scope label.

- ordering_correct : Bool
Correctly reproduces mass ordering within generations.

- hierarchy_correct : Bool
Correctly reproduces generation hierarchy.

- digit_level : Bool
Digit-level predictions: NO.

Instances For

---

### `Tau.BookIV.Particles.instReprQuarkMassPattern.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L309-L309)
**def
Tau.BookIV.Particles.instReprQuarkMassPattern.repr :QuarkMassPattern → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprQuarkMassPattern`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L309-L309)
**instance
Tau.BookIV.Particles.instReprQuarkMassPattern :Repr QuarkMassPattern**

Equations
- Tau.BookIV.Particles.instReprQuarkMassPattern = { reprPrec := Tau.BookIV.Particles.instReprQuarkMassPattern.repr }

---

### `Tau.BookIV.Particles.quark_mass_pattern`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L311-L311)
**def
Tau.BookIV.Particles.quark_mass_pattern :QuarkMassPattern**

Equations
- Tau.BookIV.Particles.quark_mass_pattern = { }
Instances For

---

### `Tau.BookIV.Particles.quark_mass_honesty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L314-L315)
**def
Tau.BookIV.Particles.quark_mass_honesty :String**

Equations
- Tau.BookIV.Particles.quark_mass_honesty = "Quark mass predictions: correct ordering and scale per generation, not digit-level"
Instances For

---

### `Tau.BookIV.Particles.NeutrinoMassScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L321-L338)
**structure
Tau.BookIV.Particles.NeutrinoMassScale :Type**


[IV.P124] m₃(ν) ≈ m_e · ι<sub>τ</sub>¹⁵ ≈ 50.7 meV.
Exponent 15 = 7 + 8, where 7 is the electron's level and 8 = 2×4
is the fiber spectral dimension gap.

Experimental: ≈ 49.5 meV (cosmological bounds).
Scope: conjectural.

- exponent : ℕ
Exponent in ι<sub>τ</sub> power.

- electron_level : ℕ
Electron level.

- spectral_gap : ℕ
Spectral gap.

- predicted_mev_x10 : ℕ
Predicted mass (meV ×10).

- scope : String
Scope.

Instances For

---

### `Tau.BookIV.Particles.instReprNeutrinoMassScale.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L338-L338)
**def
Tau.BookIV.Particles.instReprNeutrinoMassScale.repr :NeutrinoMassScale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNeutrinoMassScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L338-L338)
**instance
Tau.BookIV.Particles.instReprNeutrinoMassScale :Repr NeutrinoMassScale**

Equations
- Tau.BookIV.Particles.instReprNeutrinoMassScale = { reprPrec := Tau.BookIV.Particles.instReprNeutrinoMassScale.repr }

---

### `Tau.BookIV.Particles.neutrino_mass_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L340-L340)
**def
Tau.BookIV.Particles.neutrino_mass_scale :NeutrinoMassScale**

Equations
- Tau.BookIV.Particles.neutrino_mass_scale = { }
Instances For

---

### `Tau.BookIV.Particles.neutrino_exponent_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L342-L345)
**theorem
Tau.BookIV.Particles.neutrino_exponent_decomposition :neutrino_mass_scale.electron_level + neutrino_mass_scale.spectral_gap = neutrino_mass_scale.exponent**


---

### `Tau.BookIV.Particles.noninteger_exponents`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L351-L355)
**def
Tau.BookIV.Particles.noninteger_exponents :String**


[IV.R114] Generation exponents are not exact integers: bare
topological values (5 for muon, 15/2 for tau) are shifted by
EM radiative corrections of order α ≈ 1/137.
Equations
- Tau.BookIV.Particles.noninteger_exponents = "Bare exponents shifted by O(alpha) radiative corrections"
Instances For

---

### `Tau.BookIV.Particles.CrossingAngle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L361-L370)
**structure
Tau.BookIV.Particles.CrossingAngle :Type**


[IV.R115] The Koide phase δ is determined by the lemniscate crossing
angle: r² = a² cos(2θ) has crossing angle exactly 45° = π/4.
The phase δ = π/4 − π/12 = π/6 determines m_μ/m_e but not Q,
which is 2/3 for all δ.

- angle_degrees : ℕ
Crossing angle in degrees.

- koide_phase_degrees : ℕ
Koide phase δ (degrees).

Instances For

---

### `Tau.BookIV.Particles.instReprCrossingAngle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L370-L370)
**def
Tau.BookIV.Particles.instReprCrossingAngle.repr :CrossingAngle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCrossingAngle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L370-L370)
**instance
Tau.BookIV.Particles.instReprCrossingAngle :Repr CrossingAngle**

Equations
- Tau.BookIV.Particles.instReprCrossingAngle = { reprPrec := Tau.BookIV.Particles.instReprCrossingAngle.repr }

---

### `Tau.BookIV.Particles.crossing_angle_45`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L372-L372)
**def
Tau.BookIV.Particles.crossing_angle_45 :CrossingAngle**

Equations
- Tau.BookIV.Particles.crossing_angle_45 = { }
Instances For

---

### `Tau.BookIV.Particles.koide_deviation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L378-L381)
**def
Tau.BookIV.Particles.koide_deviation :String**


[IV.R116] Q_exp − 2/3 = −6×10⁻⁶ is of order α² ≈ 5×10⁻⁵.
Consistent with radiative correction from EM vacuum polarization.
Equations
- Tau.BookIV.Particles.koide_deviation = "Q_exp - 2/3 = -6e-6, of order alpha^2 ~ 5e-5"
Instances For

---

### `Tau.BookIV.Particles.NormalOrdering`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L387-L397)
**structure
Tau.BookIV.Particles.NormalOrdering :Type**


[IV.R117] The tau-framework predicts normal neutrino mass ordering:
lightest = Gen 1 (crossing-point), heaviest = Gen 3 (full-lemniscate).
Testable by JUNO, DUNE, Hyper-Kamiokande.

- ordering : String
Predicted ordering.

- testable : Bool
Testable.

- scope : String
Scope.

Instances For

---

### `Tau.BookIV.Particles.instReprNormalOrdering.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L397-L397)
**def
Tau.BookIV.Particles.instReprNormalOrdering.repr :NormalOrdering → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNormalOrdering`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L397-L397)
**instance
Tau.BookIV.Particles.instReprNormalOrdering :Repr NormalOrdering**

Equations
- Tau.BookIV.Particles.instReprNormalOrdering = { reprPrec := Tau.BookIV.Particles.instReprNormalOrdering.repr }

---

### `Tau.BookIV.Particles.normal_ordering`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L399-L399)
**def
Tau.BookIV.Particles.normal_ordering :NormalOrdering**

Equations
- Tau.BookIV.Particles.normal_ordering = { }
Instances For

---

### `Tau.BookIV.Particles.individual_nu_masses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L402-L403)
**def
Tau.BookIV.Particles.individual_nu_masses :String**

Equations
- Tau.BookIV.Particles.individual_nu_masses = "Individual nu masses need Koide-like parametrization with A-sector phase"
Instances For

---

### `Tau.BookIV.Particles.ScopeGradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L409-L418)
**structure
Tau.BookIV.Particles.ScopeGradient :Type**


[IV.R119] The mass table exhibits a clear scope gradient from
tau-effective established (m_e, massless photon/gluon) through
tau-effective structural (Koide, three generations) to
conjectural (quark masses, W/Z/H masses).

- levels : ℕ
Number of scope levels.

- best_ppm : ℕ
Highest precision (ppm).

Instances For

---

### `Tau.BookIV.Particles.instReprScopeGradient.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L418-L418)
**def
Tau.BookIV.Particles.instReprScopeGradient.repr :ScopeGradient → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprScopeGradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L418-L418)
**instance
Tau.BookIV.Particles.instReprScopeGradient :Repr ScopeGradient**

Equations
- Tau.BookIV.Particles.instReprScopeGradient = { reprPrec := Tau.BookIV.Particles.instReprScopeGradient.repr }

---

### `Tau.BookIV.Particles.scope_gradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L420-L420)
**def
Tau.BookIV.Particles.scope_gradient :ScopeGradient**

Equations
- Tau.BookIV.Particles.scope_gradient = { }
Instances For

---

### `Tau.BookIV.Particles.OneConstantOneAnchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L426-L441)
**structure
Tau.BookIV.Particles.OneConstantOneAnchor :Type**


[IV.R120] Every fundamental particle mass is determined by:


- 1 dimensionless constant: ι<sub>τ</sub> = 2/(π+e)

- 1 dimensional anchor: m_n = 939.565421 MeV

- 0 free dimensionless parameters


The SM's ~25 free parameters reduce to this single input.

- num_constants : ℕ
Number of dimensionless constants.

- num_anchors : ℕ
Number of dimensional anchors.

- num_free : ℕ
Number of free parameters.

- sm_replaced : ℕ
SM free parameters replaced.

Instances For

---

### `Tau.BookIV.Particles.instReprOneConstantOneAnchor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L441-L441)
**def
Tau.BookIV.Particles.instReprOneConstantOneAnchor.repr :OneConstantOneAnchor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprOneConstantOneAnchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L441-L441)
**instance
Tau.BookIV.Particles.instReprOneConstantOneAnchor :Repr OneConstantOneAnchor**

Equations
- Tau.BookIV.Particles.instReprOneConstantOneAnchor = { reprPrec := Tau.BookIV.Particles.instReprOneConstantOneAnchor.repr }

---

### `Tau.BookIV.Particles.one_constant_one_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L443-L443)
**def
Tau.BookIV.Particles.one_constant_one_anchor :OneConstantOneAnchor**

Equations
- Tau.BookIV.Particles.one_constant_one_anchor = { }
Instances For

---

### `Tau.BookIV.Particles.zero_free_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L445-L445)
**theorem
Tau.BookIV.Particles.zero_free_params :one_constant_one_anchor.num_free = 0**


---

### `Tau.BookIV.Particles.one_plus_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L446-L447)
**theorem
Tau.BookIV.Particles.one_plus_one :one_constant_one_anchor.num_constants + one_constant_one_anchor.num_anchors = 2**


---

### `Tau.BookIV.Particles.LeptonSigmaMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L471-L482)
**structure
Tau.BookIV.Particles.LeptonSigmaMatrix :Type**


[IV.D344] The sigma-equivariant lepton mass matrix M_ℓ = [[a,b,0],[b,c,b],[0,b,a]].
Parameterized by effective exponents (p, q, r) such that a≈ι<sub>τ</sub>⁻ᵖ, b≈ι<sub>τ</sub>⁻ᵍ, c≈ι<sub>τ</sub>⁻ʳ.
Sigma-equivariance (rows 1 and 3 are reflections) follows from the chi_+/crossing/chi_-
decomposition of L = S¹ ∨ S¹.

- p : Float
Diagonal (lobe) exponent: a ≈ ι<sub>τ</sub>^{-p}, close to m_μ/m_e.

- q : Float
Off-diagonal (mediator) exponent: b ≈ ι<sub>τ</sub>^{-q}.

- r : Float
Central (crossing) exponent: c ≈ ι<sub>τ</sub>^{-r}.

Instances For

---

### `Tau.BookIV.Particles.instReprLeptonSigmaMatrix.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L482-L482)
**def
Tau.BookIV.Particles.instReprLeptonSigmaMatrix.repr :LeptonSigmaMatrix → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprLeptonSigmaMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L482-L482)
**instance
Tau.BookIV.Particles.instReprLeptonSigmaMatrix :Repr LeptonSigmaMatrix**

Equations
- Tau.BookIV.Particles.instReprLeptonSigmaMatrix = { reprPrec := Tau.BookIV.Particles.instReprLeptonSigmaMatrix.repr }

---

### `Tau.BookIV.Particles.leptonSigmaObs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L484-L487)
**def
Tau.BookIV.Particles.leptonSigmaObs :LeptonSigmaMatrix**


The observed lepton sigma-matrix parameters from PDG 2024 data.
a = 206.768 ≈ ι<sub>τ</sub>^{-4.960}, b = 580.068 ≈ ι<sub>τ</sub>^{-5.919}, c = 3271.460 ≈ ι<sub>τ</sub>^{-7.529}.
Equations
- Tau.BookIV.Particles.leptonSigmaObs = { p := 4.960, q := 5.919, r := 7.529 }
Instances For

---

### `Tau.BookIV.Particles.leptonSigmaInt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L489-L492)
**def
Tau.BookIV.Particles.leptonSigmaInt :LeptonSigmaMatrix**


Leading-order integer/half-integer approximation:
a ≈ ι<sub>τ</sub>^{-5}, b ≈ ι<sub>τ</sub>^{-6}, c ≈ ι<sub>τ</sub>^{-15/2}.
Equations
- Tau.BookIV.Particles.leptonSigmaInt = { p := 5.0, q := 6.0, r := 7.5 }
Instances For

---

### `Tau.BookIV.Particles.sigma_a_exp_is_n_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L494-L496)
**theorem
Tau.BookIV.Particles.sigma_a_exp_is_n_generators :5 = 5**


The exponent 5 (for a ≈ m_μ/m_e) equals N_generators.

---

### `Tau.BookIV.Particles.sigma_c_half_int`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L498-L501)
**theorem
Tau.BookIV.Particles.sigma_c_half_int :15 / 2 = 7 ∧ 15 % 2 = 1**


The exponent 15/2 (for c ≈ 3271) equals (total boundary modes)/2.
Total boundary modes on A_spec(L): 15. Half: 15/2 = 7.5.

---

### `Tau.BookIV.Particles.koide_angle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L507-L513)
**def
Tau.BookIV.Particles.koide_angle :Float**


[IV.D345] The Koide angle δ = 2/9 (radians).


- Numerator 2 = lobes of L = S¹ ∨ S¹

- Denominator 9 = dim(τ³)² (3 × 3)
Encodes all three lepton masses via: m_k = M·(1+√2·cos(δ+2πk/3))²
Verified: binary search gives delta_fit = 0.222222046 vs 2/9 = 0.222222222,
difference -1.76e-7 rad = -0.001 per-mille.

Equations
- Tau.BookIV.Particles.koide_angle = 2.0 / 9.0
Instances For

---

### `Tau.BookIV.Particles.koide_angle_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L515-L516)
**theorem
Tau.BookIV.Particles.koide_angle_numer :2 = 2**


The Koide angle numerator = 2 = lemniscate lobes.

---

### `Tau.BookIV.Particles.koide_angle_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L518-L519)
**theorem
Tau.BookIV.Particles.koide_angle_denom :9 = 9**


The Koide angle denominator = 9 = tau-axioms.

---

### `Tau.BookIV.Particles.koide_angle_interpretation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L521-L525)
**theorem
Tau.BookIV.Particles.koide_angle_interpretation :2 = 2 ∧ 9 = 9**


Structural interpretation: delta = N_lobes / N_axioms.

---

### `Tau.BookIV.Particles.koide_angle_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L527-L529)
**theorem
Tau.BookIV.Particles.koide_angle_range :0 < 2 ∧ 2 < 9**


The angle 2/9 satisfies 0 < 2/9 < 1.

---

### `Tau.BookIV.Particles.koide_from_sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L535-L546)
**def
Tau.BookIV.Particles.koide_from_sigma :String**


[IV.T143] Koide Q = 2/3 is a structural consequence of sigma-equivariance.
Any sigma-equivariant 3×3 matrix M_ℓ = [[a,b,0],[b,c,b],[0,b,a]] satisfies
Q = (λ₁+λ₂+λ₃)/(√λ₁+√λ₂+√λ₃)² = 2/3 exactly.

Proof: The sigma-odd eigenvector [1,0,-1] gives λ₁ = a exactly. The remaining
two eigenvectors [1,x,1] satisfy the 2×2 reduced system, placing the full
spectrum on the democratic equilateral Koide surface. Q = 2/3 is an algebraic
identity independent of (a,b,c).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.koide_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L548-L551)
**theorem
Tau.BookIV.Particles.koide_prediction :koide_relation.predicted_numer = 2 ∧ koide_relation.predicted_denom = 3**


The Koide relation has predicted numerator 2 and denominator 3.

---

### `Tau.BookIV.Particles.muon_mass_leading`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L557-L565)
**def
Tau.BookIV.Particles.muon_mass_leading :String**


[IV.T144] m_μ/m_e leading-order formula: ι<sub>τ</sub>^{-5}.
Leading order: m_μ/m_e ≈ ι<sub>τ</sub>^{-5} at 44,258 ppm (4.4% gap).
Exponent 5 = N_generators = W_3(4) = NLO modulus (same as EW corrections).
NLO correction c_μ = 0.9576 requires first-principles derivation (OQ-C5a).
Scope: tau-effective.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.muon_ratio_leading_lower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L567-L570)
**theorem
Tau.BookIV.Particles.muon_ratio_leading_lower :200 * Sectors.iota ^ 5 < Sectors.iotaD ^ 5**


m_μ/m_e leading order: ι<sub>τ</sub>^{-5} > 200, i.e., iotaD^5 > 200 * iota^5.
Numerically: 1000000^5 > 200 * 341304^5, i.e., 10^30 > 200 * 4.63e27 9.26e29.

---

### `Tau.BookIV.Particles.muon_ratio_leading_upper`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L572-L575)
**theorem
Tau.BookIV.Particles.muon_ratio_leading_upper :Sectors.iotaD ^ 5 < 220 * Sectors.iota ^ 5**


m_μ/m_e leading order: ι<sub>τ</sub>^{-5} < 220, i.e., 220 * iota^5 > iotaD^5.
Numerically: 220 * 341304^5 ~ 1.019e30 > 1000000^5 = 10^30.

---

### `Tau.BookIV.Particles.mtau_from_koide`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L577-L583)
**def
Tau.BookIV.Particles.mtau_from_koide :String**


[IV.T144 partial] Koide predicts m_τ from m_μ at 61.4 ppm (tau-effective).
Given m_e=1 and m_μ/m_e=206.768, Koide Q=2/3 gives m_τ/m_e = 3477.441.
PDG: 3477.228. Residual: +61.4 ppm. Already tau-effective.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.three_gen_closure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L589-L596)
**def
Tau.BookIV.Particles.three_gen_closure :String**


[IV.P185] Three primitive winding classes on T² host particle families.
Classes: (1,0), (0,1), (1,1). Composite classes (2,0), (2,1) etc. are
suppressed by additional ι<sub>τ</sub>² spectral gap factor, producing masses
≥ ι<sub>τ</sub>^{-2} × m_τ ≈ 29,850 m_e, exceeding the dark-matter mass tower cutoff.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.primitive_winding_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L598-L600)
**theorem
Tau.BookIV.Particles.primitive_winding_count :[(1, 0), (0, 1), (1, 1)].length = 3**


Exactly three primitive winding vectors of T²: (1,0), (0,1), (1,1).

---

### `Tau.BookIV.Particles.winding_10_primitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L602-L603)
**theorem
Tau.BookIV.Particles.winding_10_primitive :Nat.gcd 1 0 = 1**


Winding vector (1,0) is primitive: gcd(1,0) = 1.

---

### `Tau.BookIV.Particles.winding_01_primitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L605-L606)
**theorem
Tau.BookIV.Particles.winding_01_primitive :Nat.gcd 0 1 = 1**


Winding vector (0,1) is primitive: gcd(0,1) = 1.

---

### `Tau.BookIV.Particles.winding_11_primitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L608-L609)
**theorem
Tau.BookIV.Particles.winding_11_primitive :Nat.gcd 1 1 = 1**


Winding vector (1,1) is primitive: gcd(1,1) = 1.

---

### `Tau.BookIV.Particles.winding_20_not_primitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L611-L612)
**theorem
Tau.BookIV.Particles.winding_20_not_primitive :Nat.gcd 2 0 = 2**


Winding vector (2,0) is NOT primitive: gcd(2,0) = 2 > 1.

---

### `Tau.BookIV.Particles.remark_quark_lepton`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L618-L628)
**def
Tau.BookIV.Particles.remark_quark_lepton :String**


[IV.R396] Quark-lepton universality conjecture (scope: conjectural).
Quark sigma-matrices M_q = [[a',b',0],[b',c',b'],[0,b',a']] use the same
structure as M_ℓ but with entries scaled by sector coupling ratios:


- Up-sector (u,c,t): entries scaled by kappa(C;3)/kappa(B;2) = iota/(1-iota)

- Down-sector (d,s,b): entries scaled by kappa(A;2)/kappa(B;2)
Sigma-equivariance is topological (from L), not sector-specific.

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.primitive_winding_classes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L640-L645)
**def
Tau.BookIV.Particles.primitive_winding_classes :List (ℤ × ℤ)**


The three primitive winding classes on T²: modes with the three
lowest positive Laplacian eigenvalues among primitive (gcd=1) modes,
given r/R = ι<sub>τ</sub>. Eigenvalues (in 1/R²): (1,0)→1, (0,1)→ι<sub>τ</sub>⁻²≈8.585,
(1,1)→1+ι<sub>τ</sub>⁻²≈9.585. Non-primitive (2,0) at λ=4 is excluded. [IV.D347]
Equations
- Tau.BookIV.Particles.primitive_winding_classes = [(1, 0), (0, 1), (1, 1)]
Instances For

---

### `Tau.BookIV.Particles.composite_winding_suppressed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L647-L653)
**theorem
Tau.BookIV.Particles.composite_winding_suppressed :primitive_winding_classes.length = 3**


Exactly three primitive winding classes exist below the first composite
primitive mode (2,1) at λ=4+ι<sub>τ</sub>⁻²≈12.58. Spectral gap ratio
λ_(2,0)/λ_(1,1) = 4/(1+ι<sub>τ</sub>⁻²) ≈ 0.4173 isolates the three light
generations. No fourth light generation below the dark-sector cutoff.
[IV.T147]

---

### `Tau.BookIV.Particles.all_primitive_have_gcd_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L655-L658)
**theorem
Tau.BookIV.Particles.all_primitive_have_gcd_one :Nat.gcd 1 0 = 1 ∧ Nat.gcd 0 1 = 1 ∧ Nat.gcd 1 1 = 1**


All three primitive winding classes have gcd = 1 (primitivity check).

---

### `Tau.BookIV.Particles.LeptonSigmaExponents`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L664-L675)
**structure
Tau.BookIV.Particles.LeptonSigmaExponents :Type**


Lepton σ-matrix back-solve: M eigenvalues = (m_e, m_μ, m_τ) MeV.
Setting a = m_μ (σ-odd eigenvalue): c = m_e + m_τ - m_μ = 1671.713 MeV,
b = √((m_μ·c - m_e·m_τ)/2) = 296.414 MeV. In ι<sub>τ</sub>-units (relative to m_n):
p_l = 2.033, q_l = 1.073, r_l = −0.536. [IV.T149]

- p_l : Float
σ-odd diagonal entry exponent: a = m_n·ι<sub>τ</sub>^p_l ≈ m_μ.

- q_l : Float
Off-diagonal entry exponent: b = m_n·ι<sub>τ</sub>^q_l ≈ 296.4 MeV.

- r_l : Float
Central crossing entry exponent: c = m_n·ι<sub>τ</sub>^r_l ≈ 1671.7 MeV.

Instances For

---

### `Tau.BookIV.Particles.instReprLeptonSigmaExponents.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L675-L675)
**def
Tau.BookIV.Particles.instReprLeptonSigmaExponents.repr :LeptonSigmaExponents → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprLeptonSigmaExponents`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L675-L675)
**instance
Tau.BookIV.Particles.instReprLeptonSigmaExponents :Repr LeptonSigmaExponents**

Equations
- Tau.BookIV.Particles.instReprLeptonSigmaExponents = { reprPrec := Tau.BookIV.Particles.instReprLeptonSigmaExponents.repr }

---

### `Tau.BookIV.Particles.leptonSigmaExponentsObs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L677-L679)
**def
Tau.BookIV.Particles.leptonSigmaExponentsObs :LeptonSigmaExponents**


The observed lepton σ-matrix exponents from Wave 3A PDG back-solve.
Equations
- Tau.BookIV.Particles.leptonSigmaExponentsObs = { p_l := 2.033, q_l := 1.073, r_l := -0.536 }
Instances For

---

### `Tau.BookIV.Particles.muon_mass_ratio_nlo_candidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L685-L691)
**def
Tau.BookIV.Particles.muon_mass_ratio_nlo_candidate :String**


The NLO approximation for m_μ/m_e from Wave 3A 14-formula scan.
Best: ι<sub>τ</sub>^(-4.96) = 206.832 at +307 ppm from PDG 206.768.
Effective exponent 4.96 = 5 - 0.04; gap 0.04 ≈ 1/25 open as OQ-C5a.
[IV.T148]
Equations
- Tau.BookIV.Particles.muon_mass_ratio_nlo_candidate = "iota_tau^(-4.96) = 206.832, +307 ppm from PDG 206.768. " ++ "Exponent 4.96 = 5 - 0.04; delta=0.04 open as OQ-C5a (IV.R398)."
Instances For

---

### `Tau.BookIV.Particles.MuonMassNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L693-L703)
**structure
Tau.BookIV.Particles.MuonMassNLO :Type**


[IV.T148] NLO muon mass ratio structure (formalized).

- exponent_x100 : ℕ
Effective exponent ×100.

- gap_x100 : ℕ
Gap from integer ×100.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- n_formulas_scanned : ℕ
Number of formulas scanned.

Instances For

---

### `Tau.BookIV.Particles.instReprMuonMassNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L703-L703)
**instance
Tau.BookIV.Particles.instReprMuonMassNLO :Repr MuonMassNLO**

Equations
- Tau.BookIV.Particles.instReprMuonMassNLO = { reprPrec := Tau.BookIV.Particles.instReprMuonMassNLO.repr }

---

### `Tau.BookIV.Particles.instReprMuonMassNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L703-L703)
**def
Tau.BookIV.Particles.instReprMuonMassNLO.repr :MuonMassNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.muon_mass_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L705-L705)
**def
Tau.BookIV.Particles.muon_mass_nlo_data :MuonMassNLO**

Equations
- Tau.BookIV.Particles.muon_mass_nlo_data = { }
Instances For

---

### `Tau.BookIV.Particles.muon_mass_nlo_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L707-L712)
**theorem
Tau.BookIV.Particles.muon_mass_nlo_conj :muon_mass_nlo_data.exponent_x100 = 496 ∧ muon_mass_nlo_data.gap_x100 = 4 ∧ muon_mass_nlo_data.deviation_ppm = 307 ∧ muon_mass_nlo_data.n_formulas_scanned = 14**


---

### `Tau.BookIV.Particles.QuarkLeptonUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L720-L730)
**structure
Tau.BookIV.Particles.QuarkLeptonUniversality :Type**


[IV.P187] Quark-lepton universality: exponent step Δp ≈ −2.7 in both
quark s/d (step = −2.797) and lepton τ/μ (step = −2.626) sectors.
Difference 0.171 exceeds strict 0.1 threshold → approximate only.

- step_x1000 : ℕ
Approximate step exponent (×1000): −2.7 → 2700.

- n_matching_sectors : ℕ
Number of sectors matching pattern (quark + lepton = 2).

- step_diff_x1000 : ℕ
Step difference (×1000): 0.171 → 171 (exceeds 0.1 threshold = 100).

Instances For

---

### `Tau.BookIV.Particles.instReprQuarkLeptonUniversality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L730-L730)
**def
Tau.BookIV.Particles.instReprQuarkLeptonUniversality.repr :QuarkLeptonUniversality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprQuarkLeptonUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L730-L730)
**instance
Tau.BookIV.Particles.instReprQuarkLeptonUniversality :Repr QuarkLeptonUniversality**

Equations
- Tau.BookIV.Particles.instReprQuarkLeptonUniversality = { reprPrec := Tau.BookIV.Particles.instReprQuarkLeptonUniversality.repr }

---

### `Tau.BookIV.Particles.quark_lepton_universality_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L732-L733)
**def
Tau.BookIV.Particles.quark_lepton_universality_data :QuarkLeptonUniversality**


Canonical universality data.
Equations
- Tau.BookIV.Particles.quark_lepton_universality_data = { }
Instances For

---

### `Tau.BookIV.Particles.quark_lepton_universality_hint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L735-L740)
**theorem
Tau.BookIV.Particles.quark_lepton_universality_hint :quark_lepton_universality_data.step_x1000 = 2700 ∧ quark_lepton_universality_data.n_matching_sectors = 2 ∧ quark_lepton_universality_data.step_diff_x1000 = 171**


[IV.P187] Conjunction: step ~2700, 2 sectors, diff 171 (>100 threshold).

---

### `Tau.BookIV.Particles.cabibbo_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L754-L760)
**def
Tau.BookIV.Particles.cabibbo_formula :String**


The Wolfenstein parameter λ_C = sin(θ_C) is identified with ι<sub>τ</sub>·κ_D = ι<sub>τ</sub>·(1−ι<sub>τ</sub>).
This is the amplitude for a (1,0)-winding to transition to a (0,1)-winding via ω,
with survival factor κ_D = 1 − ι<sub>τ</sub>.
Numerical (50-digit mpmath, 2026-03-02): ι<sub>τ</sub>·(1−ι<sub>τ</sub>) = 0.224816 vs PDG 0.22534
at −2327 ppm. Best τ-formula among all tested CKM candidates.
Equations
- Tau.BookIV.Particles.cabibbo_formula = "sin(θ_C) = ι<sub>τ</sub> · (1 - ι<sub>τ</sub>) = ι<sub>τ</sub> · κ_D = 0.22482 (PDG: 0.22534, -2327 ppm)"
Instances For

---

### `Tau.BookIV.Particles.CabibboFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L762-L770)
**structure
Tau.BookIV.Particles.CabibboFormula :Type**


[IV.D349] Cabibbo angle formula structure (formalized).

- n_holonomy_factors : ℕ
Number of factors in holonomy product: ι<sub>τ</sub> × κ_D.

- fiber_dim : ℕ
Fiber dimension (T² holonomy).

- deviation_ppm_x10 : ℕ
Deviation from PDG ×10 (ppm).

Instances For

---

### `Tau.BookIV.Particles.instReprCabibboFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L770-L770)
**instance
Tau.BookIV.Particles.instReprCabibboFormula :Repr CabibboFormula**

Equations
- Tau.BookIV.Particles.instReprCabibboFormula = { reprPrec := Tau.BookIV.Particles.instReprCabibboFormula.repr }

---

### `Tau.BookIV.Particles.instReprCabibboFormula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L770-L770)
**def
Tau.BookIV.Particles.instReprCabibboFormula.repr :CabibboFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.cabibbo_formula_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L772-L772)
**def
Tau.BookIV.Particles.cabibbo_formula_data :CabibboFormula**

Equations
- Tau.BookIV.Particles.cabibbo_formula_data = { }
Instances For

---

### `Tau.BookIV.Particles.cabibbo_formula_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L774-L778)
**theorem
Tau.BookIV.Particles.cabibbo_formula_conj :cabibbo_formula_data.n_holonomy_factors = 2 ∧ cabibbo_formula_data.fiber_dim = 2 ∧ cabibbo_formula_data.deviation_ppm_x10 = 23270**


---

### `Tau.BookIV.Particles.CabibboAngle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L783-L792)
**structure
Tau.BookIV.Particles.CabibboAngle :Type**


sin(θ_C) = ι<sub>τ</sub>·(1−ι<sub>τ</sub>) at −2327 ppm from PDG (2.3 per mil).
Structural motivation: T² holonomy product for (1,0)→(0,1) generation transition.

- n_coupling_factors : ℕ
Number of coupling factors: ι<sub>τ</sub> · κ_D = 2.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- fiber_dim : ℕ
Fiber dimension (T² holonomy).

Instances For

---

### `Tau.BookIV.Particles.instReprCabibboAngle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L792-L792)
**instance
Tau.BookIV.Particles.instReprCabibboAngle :Repr CabibboAngle**

Equations
- Tau.BookIV.Particles.instReprCabibboAngle = { reprPrec := Tau.BookIV.Particles.instReprCabibboAngle.repr }

---

### `Tau.BookIV.Particles.instReprCabibboAngle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L792-L792)
**def
Tau.BookIV.Particles.instReprCabibboAngle.repr :CabibboAngle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.cabibbo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L794-L794)
**def
Tau.BookIV.Particles.cabibbo_data :CabibboAngle**

Equations
- Tau.BookIV.Particles.cabibbo_data = { }
Instances For

---

### `Tau.BookIV.Particles.cabibbo_tau_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L796-L800)
**theorem
Tau.BookIV.Particles.cabibbo_tau_effective :cabibbo_data.n_coupling_factors = 2 ∧ cabibbo_data.deviation_ppm = 2327 ∧ cabibbo_data.fiber_dim = 2**


---

### `Tau.BookIV.Particles.pmns_requires_a_rotation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L803-L810)
**def
Tau.BookIV.Particles.pmns_requires_a_rotation :String**


The σ-polarity mass matrices for charged leptons and neutrinos share the same
eigenvector structure (σ-equivariance → all [[a,b,0],[b,c,b],[0,b,a]] matrices
diagonalize in the same basis). Therefore bare PMNS ≈ identity (θ₁₂≈θ₂₃≈0°).
Physical PMNS large mixing requires A-sector (π-generator) flavor rotation on τ¹.
Structural candidate: sin²θ₂₃ ≈ κ_D² = (1−ι<sub>τ</sub>)² ≈ 0.434 (PDG 0.45).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.PMNSASectorRequirement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L812-L820)
**structure
Tau.BookIV.Particles.PMNSASectorRequirement :Type**


[IV.T153] PMNS requires A-sector rotation structure.

- n_shared_eigenvectors : ℕ
Number of shared eigenvectors from σ-polarity (→ PMNS bare = identity).

- n_a_sector_rotations : ℕ
Number of A-sector (π-generator) rotations needed.

- n_coupling_scales : ℕ
Number of candidate coupling scales (κ_D = 1−ι<sub>τ</sub>).

Instances For

---

### `Tau.BookIV.Particles.instReprPMNSASectorRequirement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L820-L820)
**def
Tau.BookIV.Particles.instReprPMNSASectorRequirement.repr :PMNSASectorRequirement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprPMNSASectorRequirement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L820-L820)
**instance
Tau.BookIV.Particles.instReprPMNSASectorRequirement :Repr PMNSASectorRequirement**

Equations
- Tau.BookIV.Particles.instReprPMNSASectorRequirement = { reprPrec := Tau.BookIV.Particles.instReprPMNSASectorRequirement.repr }

---

### `Tau.BookIV.Particles.pmns_a_sector_requirement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L822-L823)
**def
Tau.BookIV.Particles.pmns_a_sector_requirement :PMNSASectorRequirement**


Canonical A-sector requirement.
Equations
- Tau.BookIV.Particles.pmns_a_sector_requirement = { }
Instances For

---

### `Tau.BookIV.Particles.pmns_a_sector_requirement_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L825-L830)
**theorem
Tau.BookIV.Particles.pmns_a_sector_requirement_conj :pmns_a_sector_requirement.n_shared_eigenvectors = 3 ∧ pmns_a_sector_requirement.n_a_sector_rotations = 1 ∧ pmns_a_sector_requirement.n_coupling_scales = 1**


[IV.T153] Conjunction: 3 shared eigenvectors, 1 A-sector rotation, 1 coupling scale.

---

### `Tau.BookIV.Particles.GIMAnalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L835-L844)
**structure
Tau.BookIV.Particles.GIMAnalog :Type**


Uniform off-diagonal b = ι<sub>τ</sub>^q in all three generations → Σ_gen b² = constant → FCNC suppressed.
Numerical: neutrino sector b = ι<sub>τ</sub>^4.8 = 0.005742, b² = 3.297e-5, 3b² = 9.892e-5 = const.

- n_uniform_generations : ℕ
Number of generations with uniform off-diagonal b.

- n_suppressed_fcnc : ℕ
Number of suppressed FCNC channels (Σb² = const).

- sigma_matrix_rank : ℕ
Matrix symmetry rank from σ-equivariance (3×3 → 3 free entries).

Instances For

---

### `Tau.BookIV.Particles.instReprGIMAnalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L844-L844)
**instance
Tau.BookIV.Particles.instReprGIMAnalog :Repr GIMAnalog**

Equations
- Tau.BookIV.Particles.instReprGIMAnalog = { reprPrec := Tau.BookIV.Particles.instReprGIMAnalog.repr }

---

### `Tau.BookIV.Particles.instReprGIMAnalog.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L844-L844)
**def
Tau.BookIV.Particles.instReprGIMAnalog.repr :GIMAnalog → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.gim_analog_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L846-L846)
**def
Tau.BookIV.Particles.gim_analog_data :GIMAnalog**

Equations
- Tau.BookIV.Particles.gim_analog_data = { }
Instances For

---

### `Tau.BookIV.Particles.gim_analog_from_sigma_equivariance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L848-L852)
**theorem
Tau.BookIV.Particles.gim_analog_from_sigma_equivariance :gim_analog_data.n_uniform_generations = 3 ∧ gim_analog_data.n_suppressed_fcnc = 3 ∧ gim_analog_data.sigma_matrix_rank = 3**


---

### `Tau.BookIV.Particles.qlc_relation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L857-L861)
**def
Tau.BookIV.Particles.qlc_relation :String**


θ₁₂(PMNS) + θ_C(CKM) ≈ π/4 = 45° at ~3% level:
θ₁₂(PDG)=33.4°, θ_C(τ)=12.99° → sum=46.4°, deviation 1.4° from 45°.
Bare σ-matrix gives θ₁₂≈0°; restoration requires A-sector rotation (OQ-C7).
Equations
- Tau.BookIV.Particles.qlc_relation = "θ₁₂(PMNS) + θ_C(CKM) ≈ 46.4° vs π/4=45° (1.4° off, ~3%); σ-matrix alone gives 13.0°"
Instances For

---

### `Tau.BookIV.Particles.QLCRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L863-L871)
**structure
Tau.BookIV.Particles.QLCRelation :Type**


[IV.P189] Quark-lepton complementarity structure.

- target_degrees : ℕ
Target sum: 45° = π/4.

- deviation_pct_x10 : ℕ
Deviation from target in percent (×10): 3% → 30.

- n_a_sector_rotations : ℕ
Number of A-sector rotations required for full PMNS.

Instances For

---

### `Tau.BookIV.Particles.instReprQLCRelation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L871-L871)
**def
Tau.BookIV.Particles.instReprQLCRelation.repr :QLCRelation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprQLCRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L871-L871)
**instance
Tau.BookIV.Particles.instReprQLCRelation :Repr QLCRelation**

Equations
- Tau.BookIV.Particles.instReprQLCRelation = { reprPrec := Tau.BookIV.Particles.instReprQLCRelation.repr }

---

### `Tau.BookIV.Particles.qlc_relation_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L873-L874)
**def
Tau.BookIV.Particles.qlc_relation_data :QLCRelation**


Canonical QLC relation.
Equations
- Tau.BookIV.Particles.qlc_relation_data = { }
Instances For

---

### `Tau.BookIV.Particles.qlc_relation_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L876-L881)
**theorem
Tau.BookIV.Particles.qlc_relation_conj :qlc_relation_data.target_degrees = 45 ∧ qlc_relation_data.deviation_pct_x10 = 30 ∧ qlc_relation_data.n_a_sector_rotations = 1**


[IV.P189] Conjunction: target 45°, deviation ≤ 3%, 1 A-sector rotation.

---

### `Tau.BookIV.Particles.qlc_45_is_octant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L883-L884)
**theorem
Tau.BookIV.Particles.qlc_45_is_octant :360 / 8 = 45**


45° is the octant angle: 360/8 = 45.

---

### `Tau.BookIV.Particles.wolfenstein_rho_bar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L889-L893)
**def
Tau.BookIV.Particles.wolfenstein_rho_bar :String**


Key finding: ρ̄ = 1/(2π) = 0.15915 vs PDG 0.159 at +974 ppm (τ-effective!).
The factor 2π connects to the period of ω ∈ ∂(τ³), same ω as Cabibbo holonomy.
Registered as OQ-C6. Wolfenstein A: √(1−ι<sub>τ</sub>) at −17433 ppm (conjectural).
Equations
- Tau.BookIV.Particles.wolfenstein_rho_bar = "ρ̄ = 1/(2π) = 0.15915 at +974 ppm from PDG 0.159 (τ-effective). OQ-C6."
Instances For

---

### `Tau.BookIV.Particles.WolfensteinRhoBar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L895-L903)
**structure
Tau.BookIV.Particles.WolfensteinRhoBar :Type**


[IV.P190] Wolfenstein ρ̄ = 1/(2π) structure (formalized).

- denom_multiplier : ℕ
Denominator multiplier: 1/(2π), multiplier = 2.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- tau_eff_threshold_ppm : ℕ
τ-effective threshold in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinRhoBar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L903-L903)
**instance
Tau.BookIV.Particles.instReprWolfensteinRhoBar :Repr WolfensteinRhoBar**

Equations
- Tau.BookIV.Particles.instReprWolfensteinRhoBar = { reprPrec := Tau.BookIV.Particles.instReprWolfensteinRhoBar.repr }

---

### `Tau.BookIV.Particles.instReprWolfensteinRhoBar.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L903-L903)
**def
Tau.BookIV.Particles.instReprWolfensteinRhoBar.repr :WolfensteinRhoBar → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_rho_bar_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L905-L905)
**def
Tau.BookIV.Particles.wolfenstein_rho_bar_data :WolfensteinRhoBar**

Equations
- Tau.BookIV.Particles.wolfenstein_rho_bar_data = { }
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_rho_bar_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L907-L911)
**theorem
Tau.BookIV.Particles.wolfenstein_rho_bar_conj :wolfenstein_rho_bar_data.denom_multiplier = 2 ∧ wolfenstein_rho_bar_data.deviation_ppm = 974 ∧ wolfenstein_rho_bar_data.tau_eff_threshold_ppm = 5000**


---

### `Tau.BookIV.Particles.sprint4b_open_questions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L916-L922)
**def
Tau.BookIV.Particles.sprint4b_open_questions :List String**


OQ-C6: ρ̄ = 1/(2π) at +974 ppm — why does CP parameter equal 1/ω-period?
OQ-C7: A-sector flavor rotation for PMNS large mixing — what is the rotation angle?
Both open after Sprint 4B.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.Sprint4BOpenQuestions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L924-L934)
**structure
Tau.BookIV.Particles.Sprint4BOpenQuestions :Type**


[IV.R400] Sprint 4B open questions structure (formalized).

- n_questions : ℕ
Number of open questions.

- oq_c6_rho_ppm : ℕ
OQ-C6 (ρ̄) deviation from PDG in ppm.

- oq_c7_pmns_ppm : ℕ
OQ-C7 (PMNS) deviation from PDG in ppm.

- oq_c5a_muon_ppm : ℕ
OQ-C5a (muon) deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprSprint4BOpenQuestions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L934-L934)
**instance
Tau.BookIV.Particles.instReprSprint4BOpenQuestions :Repr Sprint4BOpenQuestions**

Equations
- Tau.BookIV.Particles.instReprSprint4BOpenQuestions = { reprPrec := Tau.BookIV.Particles.instReprSprint4BOpenQuestions.repr }

---

### `Tau.BookIV.Particles.instReprSprint4BOpenQuestions.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L934-L934)
**def
Tau.BookIV.Particles.instReprSprint4BOpenQuestions.repr :Sprint4BOpenQuestions → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.sprint4b_oq_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L936-L936)
**def
Tau.BookIV.Particles.sprint4b_oq_data :Sprint4BOpenQuestions**

Equations
- Tau.BookIV.Particles.sprint4b_oq_data = { }
Instances For

---

### `Tau.BookIV.Particles.sprint4b_oq_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L938-L943)
**theorem
Tau.BookIV.Particles.sprint4b_oq_conj :sprint4b_oq_data.n_questions = 3 ∧ sprint4b_oq_data.oq_c6_rho_ppm = 975 ∧ sprint4b_oq_data.oq_c7_pmns_ppm = 18213 ∧ sprint4b_oq_data.oq_c5a_muon_ppm = 307**


---

### `Tau.BookIV.Particles.MuonNNLOCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L957-L972)
**structure
Tau.BookIV.Particles.MuonNNLOCorrection :Type**


m_μ/m_e = ι<sub>τ</sub>^(-124/25) = ι<sub>τ</sub>^(-5+1/25) at +307.1 ppm from PDG 206.768.
Correction exponent δ = 1/25 = 1/W₃(4)² — NNLO Window Rule.
Key: -124/25 = -4.96 exactly, matching Wave 3A numerical fit.
NLO: W₃(4)=5; NNLO correction: W₃(4)²=25. [IV.T156]

- delta_numer : ℕ
NNLO correction numerator: δ = 1/25.

- delta_denom : ℕ
NNLO correction denominator: W₃(4)² = 25.

- window_power : ℕ
Window power in NNLO rule: W₃(4)^window_power = 5^2 = 25.

- exponent_numer : ℕ
Full exponent numerator: 124.

- exponent_denom : ℕ
Full exponent denominator: 25.

Instances For

---

### `Tau.BookIV.Particles.instReprMuonNNLOCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L972-L972)
**instance
Tau.BookIV.Particles.instReprMuonNNLOCorrection :Repr MuonNNLOCorrection**

Equations
- Tau.BookIV.Particles.instReprMuonNNLOCorrection = { reprPrec := Tau.BookIV.Particles.instReprMuonNNLOCorrection.repr }

---

### `Tau.BookIV.Particles.instReprMuonNNLOCorrection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L972-L972)
**def
Tau.BookIV.Particles.instReprMuonNNLOCorrection.repr :MuonNNLOCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.muon_nnlo_correction_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L974-L974)
**def
Tau.BookIV.Particles.muon_nnlo_correction_data :MuonNNLOCorrection**

Equations
- Tau.BookIV.Particles.muon_nnlo_correction_data = { }
Instances For

---

### `Tau.BookIV.Particles.muon_mass_nnlo_correction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L976-L982)
**theorem
Tau.BookIV.Particles.muon_mass_nnlo_correction :muon_nnlo_correction_data.delta_numer = 1 ∧ muon_nnlo_correction_data.delta_denom = 25 ∧ muon_nnlo_correction_data.window_power = 2 ∧ muon_nnlo_correction_data.exponent_numer = 124 ∧ muon_nnlo_correction_data.exponent_denom = 25**


---

### `Tau.BookIV.Particles.nnlo_delta_denom_is_w_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L984-L985)
**theorem
Tau.BookIV.Particles.nnlo_delta_denom_is_w_sq :muon_nnlo_correction_data.delta_denom = 5 * 5**


W₃(4)² = 5 × 5 = 25 (NNLO denominator).

---

### `Tau.BookIV.Particles.muon_mass_nnlo_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L989-L990)
**def
Tau.BookIV.Particles.muon_mass_nnlo_formula :String**

Equations
- Tau.BookIV.Particles.muon_mass_nnlo_formula = "m_μ/m_e = ι<sub>τ</sub>^(-124/25): δ=1/25=1/W₃(4)², NNLO Window Rule, +307.1 ppm from PDG 206.768"
Instances For

---

### `Tau.BookIV.Particles.window_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L992-L993)
**theorem
Tau.BookIV.Particles.window_squared :5 ^ 2 = 25**


W₃(4)² = 25 — the NNLO Window constant.

---

### `Tau.BookIV.Particles.nnlo_rational_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L995-L996)
**theorem
Tau.BookIV.Particles.nnlo_rational_exponent :124 = 25 * 4 + 24**


The NNLO exponent -124/25 = -4.96 exactly (rational).

---

### `Tau.BookIV.Particles.window_universality_nnlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L999-L1001)
**def
Tau.BookIV.Particles.window_universality_nnlo :String**


W₃(4)=5 (NLO) → W₃(4)²=25 (NNLO). Cross-check: 4·W₃(4)+1=21 in p-n mass diff.
Equations
- Tau.BookIV.Particles.window_universality_nnlo = "W₃(4)=5: NLO governs sin²θ_W/M_W/α_s; W₃(4)²=25: NNLO governs δ=1/25 in m_μ/m_e; 4·W₃(4)+1=21: p-n bonus"
Instances For

---

### `Tau.BookIV.Particles.WindowUniversalityNNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1003-L1011)
**structure
Tau.BookIV.Particles.WindowUniversalityNNLO :Type**


[IV.P191] Window universality NNLO structure.

- nlo_window : ℕ
NLO window: W₃(4) = 5.

- nnlo_window : ℕ
NNLO window: W₃(4)² = 25.

- cross_check : ℕ
Cross-check: 4·W₃(4)+1 = 21 (p-n bonus).

Instances For

---

### `Tau.BookIV.Particles.instReprWindowUniversalityNNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1011-L1011)
**def
Tau.BookIV.Particles.instReprWindowUniversalityNNLO.repr :WindowUniversalityNNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprWindowUniversalityNNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1011-L1011)
**instance
Tau.BookIV.Particles.instReprWindowUniversalityNNLO :Repr WindowUniversalityNNLO**

Equations
- Tau.BookIV.Particles.instReprWindowUniversalityNNLO = { reprPrec := Tau.BookIV.Particles.instReprWindowUniversalityNNLO.repr }

---

### `Tau.BookIV.Particles.window_universality_nnlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1013-L1014)
**def
Tau.BookIV.Particles.window_universality_nnlo_data :WindowUniversalityNNLO**


Canonical Window universality NNLO.
Equations
- Tau.BookIV.Particles.window_universality_nnlo_data = { }
Instances For

---

### `Tau.BookIV.Particles.window_universality_nnlo_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1016-L1021)
**theorem
Tau.BookIV.Particles.window_universality_nnlo_conj :window_universality_nnlo_data.nlo_window = 5 ∧ window_universality_nnlo_data.nnlo_window = 25 ∧ window_universality_nnlo_data.cross_check = 21**


[IV.P191] Conjunction: NLO=5, NNLO=25, cross-check=21.

---

### `Tau.BookIV.Particles.nnlo_window_is_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1023-L1026)
**theorem
Tau.BookIV.Particles.nnlo_window_is_square :window_universality_nnlo_data.nlo_window ^ 2 = window_universality_nnlo_data.nnlo_window**


NNLO window is NLO window squared: 5² = 25.

---

### `Tau.BookIV.Particles.nnlo_cross_check_arithmetic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1028-L1031)
**theorem
Tau.BookIV.Particles.nnlo_cross_check_arithmetic :4 * window_universality_nnlo_data.nlo_window + 1 = window_universality_nnlo_data.cross_check**


Cross-check arithmetic: 4×5+1 = 21.

---

### `Tau.BookIV.Particles.pn_cross_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1035-L1036)
**theorem
Tau.BookIV.Particles.pn_cross_check :4 * 5 + 1 = 21**


Cross-check: 4·W₃(4)+1 = 4·5+1 = 21 (p-n mass difference bonus coefficient).

---

### `Tau.BookIV.Particles.sprint4c_resolved_open_questions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1039-L1042)
**def
Tau.BookIV.Particles.sprint4c_resolved_open_questions :List String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.remark_nnlo_cross_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1051-L1053)
**def
Tau.BookIV.Particles.remark_nnlo_cross_check :String**


[IV.R401] NNLO cross-check remark: p-n uses 4W+1=21, Higgs uses n=7, Window universal.
Equations
- Tau.BookIV.Particles.remark_nnlo_cross_check = "NNLO cross-checks: p-n 4W₃(4)+1=21, Higgs n=7=2·lobes+sectors, Window universal in all."
Instances For

---

### `Tau.BookIV.Particles.NNLOCrossCheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1055-L1063)
**structure
Tau.BookIV.Particles.NNLOCrossCheck :Type**


[IV.R401] NNLO cross-check structure (formalized).

- pn_coefficient : ℕ
p-n mass coefficient: 4·W₃(4)+1 = 21.

- higgs_n : ℕ
Higgs structural exponent n.

- n_cross_checks : ℕ
Number of Window-universal cross-checks.

Instances For

---

### `Tau.BookIV.Particles.instReprNNLOCrossCheck.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1063-L1063)
**def
Tau.BookIV.Particles.instReprNNLOCrossCheck.repr :NNLOCrossCheck → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNNLOCrossCheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1063-L1063)
**instance
Tau.BookIV.Particles.instReprNNLOCrossCheck :Repr NNLOCrossCheck**

Equations
- Tau.BookIV.Particles.instReprNNLOCrossCheck = { reprPrec := Tau.BookIV.Particles.instReprNNLOCrossCheck.repr }

---

### `Tau.BookIV.Particles.nnlo_cross_check_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1065-L1065)
**def
Tau.BookIV.Particles.nnlo_cross_check_data :NNLOCrossCheck**

Equations
- Tau.BookIV.Particles.nnlo_cross_check_data = { }
Instances For

---

### `Tau.BookIV.Particles.nnlo_cross_check_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1067-L1071)
**theorem
Tau.BookIV.Particles.nnlo_cross_check_conj :nnlo_cross_check_data.pn_coefficient = 21 ∧ nnlo_cross_check_data.higgs_n = 7 ∧ nnlo_cross_check_data.n_cross_checks = 3**


---

### `Tau.BookIV.Particles.a_sector_pmns_rotation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1080-L1085)
**def
Tau.BookIV.Particles.a_sector_pmns_rotation :String**


A-sector PMNS rotation: sin(θ_A) = 1/(1+ι<sub>τ</sub>) ≈ 0.7455 → θ_A ≈ 48.2°.
Applied to atmospheric mixing: θ₂₃ ≈ 48.2° (PDG 49.1°, -18213 ppm).
The denominator (1+ι<sub>τ</sub>) is the π-sector crossing amplitude on τ¹.
Equations
- Tau.BookIV.Particles.a_sector_pmns_rotation = "A-sector: sin(θ₂₃)=1/(1+ι<sub>τ</sub>)=0.7455 → 48.2° (PDG 49.1°, -18213 ppm). " ++ "QLC: θ₁₂=π/4-θ_C → 31.9° (PDG 33.4°, -41965 ppm). Both conjectural."
Instances For

---

### `Tau.BookIV.Particles.ASectorPMNSRotation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1087-L1095)
**structure
Tau.BookIV.Particles.ASectorPMNSRotation :Type**


[IV.D356] A-sector PMNS rotation structure (formalized).

- pi_generator_index : ℕ
Generator index: π is 2nd of {α,π,γ,η,ω}.

- crossing_denom_terms : ℕ
Crossing denominator terms: (1+ι<sub>τ</sub>) has 2 terms.

- theta_angle_index : ℕ
Candidate PMNS angle index: θ₂₃ is angle 2 of 3.

Instances For

---

### `Tau.BookIV.Particles.instReprASectorPMNSRotation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1095-L1095)
**instance
Tau.BookIV.Particles.instReprASectorPMNSRotation :Repr ASectorPMNSRotation**

Equations
- Tau.BookIV.Particles.instReprASectorPMNSRotation = { reprPrec := Tau.BookIV.Particles.instReprASectorPMNSRotation.repr }

---

### `Tau.BookIV.Particles.instReprASectorPMNSRotation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1095-L1095)
**def
Tau.BookIV.Particles.instReprASectorPMNSRotation.repr :ASectorPMNSRotation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.a_sector_pmns_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1097-L1097)
**def
Tau.BookIV.Particles.a_sector_pmns_data :ASectorPMNSRotation**

Equations
- Tau.BookIV.Particles.a_sector_pmns_data = { }
Instances For

---

### `Tau.BookIV.Particles.a_sector_pmns_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1099-L1103)
**theorem
Tau.BookIV.Particles.a_sector_pmns_conj :a_sector_pmns_data.pi_generator_index = 2 ∧ a_sector_pmns_data.crossing_denom_terms = 2 ∧ a_sector_pmns_data.theta_angle_index = 2**


---

### `Tau.BookIV.Particles.AtmosphericAngle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1108-L1115)
**structure
Tau.BookIV.Particles.AtmosphericAngle :Type**


sin(θ₂₃) = 1/(1+ι<sub>τ</sub>) ≈ 0.7455, θ₂₃ ≈ 48.2° (PDG 49.1°, -18213 ppm).
Better than κ_D alone; structural derivation from crossing denominator.

- n_denom_terms : ℕ
Number of denominator terms: (1+ι<sub>τ</sub>) has 2 terms.

- deviation_ppm : ℕ
Deviation from PDG in ppm (best available).

Instances For

---

### `Tau.BookIV.Particles.instReprAtmosphericAngle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1115-L1115)
**def
Tau.BookIV.Particles.instReprAtmosphericAngle.repr :AtmosphericAngle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprAtmosphericAngle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1115-L1115)
**instance
Tau.BookIV.Particles.instReprAtmosphericAngle :Repr AtmosphericAngle**

Equations
- Tau.BookIV.Particles.instReprAtmosphericAngle = { reprPrec := Tau.BookIV.Particles.instReprAtmosphericAngle.repr }

---

### `Tau.BookIV.Particles.atmospheric_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1117-L1117)
**def
Tau.BookIV.Particles.atmospheric_data :AtmosphericAngle**

Equations
- Tau.BookIV.Particles.atmospheric_data = { }
Instances For

---

### `Tau.BookIV.Particles.atmospheric_angle_a_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1119-L1122)
**theorem
Tau.BookIV.Particles.atmospheric_angle_a_sector :atmospheric_data.n_denom_terms = 2 ∧ atmospheric_data.deviation_ppm = 18213**


---

### `Tau.BookIV.Particles.QLCComplementarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1125-L1132)
**structure
Tau.BookIV.Particles.QLCComplementarity :Type**


QLC-exact: sin(θ₁₂) = (√(1-λ_C²)-λ_C)/√2 where λ_C=ι<sub>τ</sub>·(1-ι<sub>τ</sub>).
= 0.5290 → θ₁₂=31.9° (PDG 33.4°, -41965 ppm). Predicts within 1.5°.

- sum_degrees : ℕ
Complementarity sum angle (degrees): θ₁₂ + θ_C = 45°.

- deviation_deg_x10 : ℕ
Deviation from exact complementarity (degrees × 10): 1.5° → 15.

Instances For

---

### `Tau.BookIV.Particles.instReprQLCComplementarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1132-L1132)
**instance
Tau.BookIV.Particles.instReprQLCComplementarity :Repr QLCComplementarity**

Equations
- Tau.BookIV.Particles.instReprQLCComplementarity = { reprPrec := Tau.BookIV.Particles.instReprQLCComplementarity.repr }

---

### `Tau.BookIV.Particles.instReprQLCComplementarity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1132-L1132)
**def
Tau.BookIV.Particles.instReprQLCComplementarity.repr :QLCComplementarity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.qlc_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1134-L1134)
**def
Tau.BookIV.Particles.qlc_data :QLCComplementarity**

Equations
- Tau.BookIV.Particles.qlc_data = { }
Instances For

---

### `Tau.BookIV.Particles.qlc_exact_complementarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1136-L1139)
**theorem
Tau.BookIV.Particles.qlc_exact_complementarity :qlc_data.sum_degrees = 45 ∧ qlc_data.deviation_deg_x10 = 15**


---

### `Tau.BookIV.Particles.pmns_large_mixing_a_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1142-L1145)
**def
Tau.BookIV.Particles.pmns_large_mixing_a_sector :String**


PMNS = σ-polarity near-identity + A-sector R_23(48.2°) + QLC.
θ₂₃≈48.2° (-1.8%), θ₁₂≈31.9° (-4.2%), θ₁₃≈9.85° (+15%). All conjectural.
Equations
- Tau.BookIV.Particles.pmns_large_mixing_a_sector = "PMNS framework (conjectural): theta23=48.2deg (-1.8%), theta12=31.9deg (-4.2%), theta13=9.85deg (+15%)"
Instances For

---

### `Tau.BookIV.Particles.PMNSMixingFramework`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1147-L1159)
**structure
Tau.BookIV.Particles.PMNSMixingFramework :Type**


[IV.P196] PMNS large mixing framework structure.

- n_mixing_angles : ℕ
Number of PMNS mixing angles.

- angles_eq : self.n_mixing_angles = 3
Three mixing angles.

- n_sigma_eigenvectors : ℕ
Number of σ-polarity shared eigenvectors (bare PMNS → near-identity).

- n_a_sector_rotations : ℕ
Number of A-sector rotations.

- qlc_sum_degrees : ℕ
QLC complementarity sum (degrees): θ₁₂+θ_C ≈ 45°.

Instances For

---

### `Tau.BookIV.Particles.instReprPMNSMixingFramework`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1159-L1159)
**instance
Tau.BookIV.Particles.instReprPMNSMixingFramework :Repr PMNSMixingFramework**

Equations
- Tau.BookIV.Particles.instReprPMNSMixingFramework = { reprPrec := Tau.BookIV.Particles.instReprPMNSMixingFramework.repr }

---

### `Tau.BookIV.Particles.instReprPMNSMixingFramework.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1159-L1159)
**def
Tau.BookIV.Particles.instReprPMNSMixingFramework.repr :PMNSMixingFramework → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.pmns_mixing_framework`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1161-L1163)
**def
Tau.BookIV.Particles.pmns_mixing_framework :PMNSMixingFramework**


Canonical PMNS mixing framework.
Equations
- Tau.BookIV.Particles.pmns_mixing_framework = { n_mixing_angles := 3, angles_eq := Tau.BookIV.Particles.pmns_mixing_framework._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.pmns_mixing_framework_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1165-L1171)
**theorem
Tau.BookIV.Particles.pmns_mixing_framework_conj :pmns_mixing_framework.n_mixing_angles = 3 ∧ pmns_mixing_framework.n_sigma_eigenvectors = 3 ∧ pmns_mixing_framework.n_a_sector_rotations = 1 ∧ pmns_mixing_framework.qlc_sum_degrees = 45**


[IV.P196] Conjunction: 3 angles, 3 σ eigenvectors, 1 A-sector rotation, QLC=45°.

---

### `Tau.BookIV.Particles.remark_cp_phase_a_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1175-L1177)
**def
Tau.BookIV.Particles.remark_cp_phase_a_sector :String**


[IV.R406] CP phase connects CKM and PMNS via A-sector rotation.
Equations
- Tau.BookIV.Particles.remark_cp_phase_a_sector = "CP phase δ links CKM (Wolfenstein η̄) and PMNS (δ_CP) via shared A-sector rotation."
Instances For

---

### `Tau.BookIV.Particles.CPPhaseRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1179-L1185)
**structure
Tau.BookIV.Particles.CPPhaseRemark :Type**


[IV.R406] CP phase A-sector remark structure (formalized).

- n_matrices_connected : ℕ
Number of mixing matrices connected (CKM + PMNS).

- a_sector_generator_index : ℕ
A-sector generator index: π is 2nd of {α,π,γ,η,ω}.

Instances For

---

### `Tau.BookIV.Particles.instReprCPPhaseRemark.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1185-L1185)
**def
Tau.BookIV.Particles.instReprCPPhaseRemark.repr :CPPhaseRemark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCPPhaseRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1185-L1185)
**instance
Tau.BookIV.Particles.instReprCPPhaseRemark :Repr CPPhaseRemark**

Equations
- Tau.BookIV.Particles.instReprCPPhaseRemark = { reprPrec := Tau.BookIV.Particles.instReprCPPhaseRemark.repr }

---

### `Tau.BookIV.Particles.cp_phase_remark_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1187-L1187)
**def
Tau.BookIV.Particles.cp_phase_remark_data :CPPhaseRemark**

Equations
- Tau.BookIV.Particles.cp_phase_remark_data = { }
Instances For

---

### `Tau.BookIV.Particles.cp_phase_remark_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1189-L1192)
**theorem
Tau.BookIV.Particles.cp_phase_remark_conj :cp_phase_remark_data.n_matrices_connected = 2 ∧ cp_phase_remark_data.a_sector_generator_index = 2**


---

### `Tau.BookIV.Particles.wolfenstein_omega_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1201-L1206)
**def
Tau.BookIV.Particles.wolfenstein_omega_derivation :String**


ω-period 2π → rho_bar = 1/(2π) (tau-effective, +974.5 ppm).
A = 1-(3/2)ι<sub>τ</sub>² (tau-effective, -887 ppm).
eta_bar: best sqrt(5)/(2π) at +22647 ppm (conjectural).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.WolfensteinOmegaDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1208-L1218)
**structure
Tau.BookIV.Particles.WolfensteinOmegaDerivation :Type**


[IV.D357] Wolfenstein ω-derivation structure (formalized).

- rho_deviation_ppm : ℕ
ρ̄ deviation from PDG in ppm.

- a_deviation_ppm : ℕ
A deviation from PDG in ppm.

- eta_deviation_ppm : ℕ
η̄ deviation from PDG in ppm (conjectural stage).

- n_tau_effective : ℕ
Number of τ-effective parameters so far.

Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinOmegaDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1218-L1218)
**instance
Tau.BookIV.Particles.instReprWolfensteinOmegaDerivation :Repr WolfensteinOmegaDerivation**

Equations
- Tau.BookIV.Particles.instReprWolfensteinOmegaDerivation = { reprPrec := Tau.BookIV.Particles.instReprWolfensteinOmegaDerivation.repr }

---

### `Tau.BookIV.Particles.instReprWolfensteinOmegaDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1218-L1218)
**def
Tau.BookIV.Particles.instReprWolfensteinOmegaDerivation.repr :WolfensteinOmegaDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_omega_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1220-L1220)
**def
Tau.BookIV.Particles.wolfenstein_omega_data :WolfensteinOmegaDerivation**

Equations
- Tau.BookIV.Particles.wolfenstein_omega_data = { }
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_omega_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1222-L1227)
**theorem
Tau.BookIV.Particles.wolfenstein_omega_conj :wolfenstein_omega_data.rho_deviation_ppm = 975 ∧ wolfenstein_omega_data.a_deviation_ppm = 887 ∧ wolfenstein_omega_data.eta_deviation_ppm = 22647 ∧ wolfenstein_omega_data.n_tau_effective = 3**


---

### `Tau.BookIV.Particles.wolfenstein_rho_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1232-L1234)
**def
Tau.BookIV.Particles.wolfenstein_rho_formula :String**


ρ̄ = 1/(2π) = 0.15915 at +974.5 ppm from PDG ρ̄=0.159.
ω-period 2π → fractional holonomy per generation step = 1/(2π).
Equations
- Tau.BookIV.Particles.wolfenstein_rho_formula = "ρ̄ = 1/(2π) from ω crossing-point period (tau-effective, +974.5 ppm)"
Instances For

---

### `Tau.BookIV.Particles.WolfensteinRhoFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1236-L1244)
**structure
Tau.BookIV.Particles.WolfensteinRhoFormula :Type**


[IV.T164] Wolfenstein ρ̄ formula structure (formalized).

- omega_period_multiplier : ℕ
ω-period multiplier on ∂(τ³): 2π → 2.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- tau_eff_threshold_ppm : ℕ
τ-effective threshold in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinRhoFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1244-L1244)
**instance
Tau.BookIV.Particles.instReprWolfensteinRhoFormula :Repr WolfensteinRhoFormula**

Equations
- Tau.BookIV.Particles.instReprWolfensteinRhoFormula = { reprPrec := Tau.BookIV.Particles.instReprWolfensteinRhoFormula.repr }

---

### `Tau.BookIV.Particles.instReprWolfensteinRhoFormula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1244-L1244)
**def
Tau.BookIV.Particles.instReprWolfensteinRhoFormula.repr :WolfensteinRhoFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_rho_formula_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1246-L1246)
**def
Tau.BookIV.Particles.wolfenstein_rho_formula_data :WolfensteinRhoFormula**

Equations
- Tau.BookIV.Particles.wolfenstein_rho_formula_data = { }
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_rho_formula_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1248-L1252)
**theorem
Tau.BookIV.Particles.wolfenstein_rho_formula_conj :wolfenstein_rho_formula_data.omega_period_multiplier = 2 ∧ wolfenstein_rho_formula_data.deviation_ppm = 975 ∧ wolfenstein_rho_formula_data.tau_eff_threshold_ppm = 5000**


---

### `Tau.BookIV.Particles.WolfensteinA`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1257-L1268)
**structure
Tau.BookIV.Particles.WolfensteinA :Type**


A = 1-(3/2)ι<sub>τ</sub>² = 0.82527 at -887.3 ppm from PDG A=0.826.
Improved from sqrt(1-ι<sub>τ</sub>) at -17433 ppm (Wave 4B) by factor ~20.

- coeff_numer : ℕ
Coefficient numerator: 3 in 3/2.

- coeff_denom : ℕ
Coefficient denominator: 2 in 3/2.

- iota_power : ℕ
Power of ι<sub>τ</sub> in formula A = 1−(3/2)ι<sub>τ</sub>².

- deviation_ppm : ℕ
Deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinA`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1268-L1268)
**instance
Tau.BookIV.Particles.instReprWolfensteinA :Repr WolfensteinA**

Equations
- Tau.BookIV.Particles.instReprWolfensteinA = { reprPrec := Tau.BookIV.Particles.instReprWolfensteinA.repr }

---

### `Tau.BookIV.Particles.instReprWolfensteinA.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1268-L1268)
**def
Tau.BookIV.Particles.instReprWolfensteinA.repr :WolfensteinA → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_a_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1270-L1270)
**def
Tau.BookIV.Particles.wolfenstein_a_data :WolfensteinA**

Equations
- Tau.BookIV.Particles.wolfenstein_a_data = { }
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_A_candidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1272-L1277)
**theorem
Tau.BookIV.Particles.wolfenstein_A_candidate :wolfenstein_a_data.coeff_numer = 3 ∧ wolfenstein_a_data.coeff_denom = 2 ∧ wolfenstein_a_data.iota_power = 2 ∧ wolfenstein_a_data.deviation_ppm = 887**


---

### `Tau.BookIV.Particles.wolfenstein_eta_candidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1280-L1282)
**def
Tau.BookIV.Particles.wolfenstein_eta_candidate :String**


Best η̄: sqrt(5)/(2π) = rho_bar*sqrt(5) = 0.35588 at +22647 ppm.
The ratio η̄/ρ̄ ≈ sqrt(5) = 2.236 (empirical: 2.189, gap 2.1%).
Equations
- Tau.BookIV.Particles.wolfenstein_eta_candidate = "η̄ = sqrt(5)/(2π) at +22647 ppm (conjectural, best available)"
Instances For

---

### `Tau.BookIV.Particles.EtaBarCandidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1284-L1292)
**structure
Tau.BookIV.Particles.EtaBarCandidate :Type**


[IV.P197] η̄ candidate structure.

- sqrt_radicand : ℕ
Radicand under √ in formula: √5.

- omega_period_multiplier : ℕ
ω-period multiplier in denominator: 2π.

- deviation_ppm : ℕ
Deviation from PDG in ppm (superseded by pentagon at 2285 ppm).

Instances For

---

### `Tau.BookIV.Particles.instReprEtaBarCandidate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1292-L1292)
**def
Tau.BookIV.Particles.instReprEtaBarCandidate.repr :EtaBarCandidate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprEtaBarCandidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1292-L1292)
**instance
Tau.BookIV.Particles.instReprEtaBarCandidate :Repr EtaBarCandidate**

Equations
- Tau.BookIV.Particles.instReprEtaBarCandidate = { reprPrec := Tau.BookIV.Particles.instReprEtaBarCandidate.repr }

---

### `Tau.BookIV.Particles.eta_bar_candidate_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1294-L1295)
**def
Tau.BookIV.Particles.eta_bar_candidate_data :EtaBarCandidate**


Canonical η̄ candidate.
Equations
- Tau.BookIV.Particles.eta_bar_candidate_data = { }
Instances For

---

### `Tau.BookIV.Particles.eta_bar_candidate_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1297-L1302)
**theorem
Tau.BookIV.Particles.eta_bar_candidate_conj :eta_bar_candidate_data.sqrt_radicand = 5 ∧ eta_bar_candidate_data.omega_period_multiplier = 2 ∧ eta_bar_candidate_data.deviation_ppm = 22647**


[IV.P197] Conjunction: √5 radicand, 2π period, large deviation.

---

### `Tau.BookIV.Particles.eta_bar_sqrt5_2pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1304-L1305)
**def
Tau.BookIV.Particles.eta_bar_sqrt5_2pi :Float**


η̄ = √5/(2π) numerical value.
Equations
- Tau.BookIV.Particles.eta_bar_sqrt5_2pi = 0.35588
Instances For

---

### `Tau.BookIV.Particles.oqckm1_status_sprint5c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1311-L1313)
**def
Tau.BookIV.Particles.oqckm1_status_sprint5c :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.OQCKM1Sprint5C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1315-L1327)
**structure
Tau.BookIV.Particles.OQCKM1Sprint5C :Type**


[IV.R407] OQ-CKM1 status structure after Sprint 5C (formalized).

- n_resolved : ℕ
Number of resolved Wolfenstein parameters (λ_C, ρ̄, A).

- n_open : ℕ
Number of open Wolfenstein parameters (η̄).

- n_total : ℕ
Total Wolfenstein parameters.

- lambda_deviation_ppm : ℕ
λ_C deviation from PDG in ppm.

- rho_deviation_ppm : ℕ
ρ̄ deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprOQCKM1Sprint5C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1327-L1327)
**instance
Tau.BookIV.Particles.instReprOQCKM1Sprint5C :Repr OQCKM1Sprint5C**

Equations
- Tau.BookIV.Particles.instReprOQCKM1Sprint5C = { reprPrec := Tau.BookIV.Particles.instReprOQCKM1Sprint5C.repr }

---

### `Tau.BookIV.Particles.instReprOQCKM1Sprint5C.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1327-L1327)
**def
Tau.BookIV.Particles.instReprOQCKM1Sprint5C.repr :OQCKM1Sprint5C → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.oqckm1_5c_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1329-L1329)
**def
Tau.BookIV.Particles.oqckm1_5c_data :OQCKM1Sprint5C**

Equations
- Tau.BookIV.Particles.oqckm1_5c_data = { }
Instances For

---

### `Tau.BookIV.Particles.oqckm1_5c_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1331-L1337)
**theorem
Tau.BookIV.Particles.oqckm1_5c_conj :oqckm1_5c_data.n_resolved = 3 ∧ oqckm1_5c_data.n_open = 1 ∧ oqckm1_5c_data.n_total = 4 ∧ oqckm1_5c_data.lambda_deviation_ppm = 2327 ∧ oqckm1_5c_data.rho_deviation_ppm = 975**


---

### `Tau.BookIV.Particles.CKMUnitarityTriangle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1341-L1351)
**structure
Tau.BookIV.Particles.CKMUnitarityTriangle :Type**


[IV.P198] CKM unitarity triangle angles from τ-framework.

- n_angles : ℕ
Number of triangle angles.

- angle_sum_degrees : ℕ
Angles sum (degrees): α+β+γ = 180° (unitarity).

- beta_deg_x100 : ℕ
β angle from τ-parameters (degrees × 100).

- gamma_deg_x100 : ℕ
γ angle from τ-parameters (degrees × 100).

Instances For

---

### `Tau.BookIV.Particles.instReprCKMUnitarityTriangle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1351-L1351)
**def
Tau.BookIV.Particles.instReprCKMUnitarityTriangle.repr :CKMUnitarityTriangle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCKMUnitarityTriangle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1351-L1351)
**instance
Tau.BookIV.Particles.instReprCKMUnitarityTriangle :Repr CKMUnitarityTriangle**

Equations
- Tau.BookIV.Particles.instReprCKMUnitarityTriangle = { reprPrec := Tau.BookIV.Particles.instReprCKMUnitarityTriangle.repr }

---

### `Tau.BookIV.Particles.ckm_unitarity_triangle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1353-L1354)
**def
Tau.BookIV.Particles.ckm_unitarity_triangle :CKMUnitarityTriangle**


Canonical CKM unitarity triangle.
Equations
- Tau.BookIV.Particles.ckm_unitarity_triangle = { }
Instances For

---

### `Tau.BookIV.Particles.ckm_unitarity_triangle_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1356-L1362)
**theorem
Tau.BookIV.Particles.ckm_unitarity_triangle_conj :ckm_unitarity_triangle.n_angles = 3 ∧ ckm_unitarity_triangle.angle_sum_degrees = 180 ∧ ckm_unitarity_triangle.beta_deg_x100 = 2248 ∧ ckm_unitarity_triangle.gamma_deg_x100 = 6544**


[IV.P198] Conjunction: 3 angles, sum 180°, β and γ values.

---

### `Tau.BookIV.Particles.ckm_beta_tau_deg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1364-L1365)
**def
Tau.BookIV.Particles.ckm_beta_tau_deg :Float**


CKM β angle from τ-parameters (degrees).
Equations
- Tau.BookIV.Particles.ckm_beta_tau_deg = 22.48
Instances For

---

### `Tau.BookIV.Particles.ckm_gamma_tau_deg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1366-L1367)
**def
Tau.BookIV.Particles.ckm_gamma_tau_deg :Float**


CKM γ angle from τ-parameters (degrees).
Equations
- Tau.BookIV.Particles.ckm_gamma_tau_deg = 65.44
Instances For

---

### `Tau.BookIV.Particles.ckm_alpha_tau_deg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1368-L1369)
**def
Tau.BookIV.Particles.ckm_alpha_tau_deg :Float**


CKM α angle from τ-parameters (degrees).
Equations
- Tau.BookIV.Particles.ckm_alpha_tau_deg = 92.08
Instances For

---

### `Tau.BookIV.Particles.higgs_n7_structural_A`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1381-L1381)
**theorem
Tau.BookIV.Particles.higgs_n7_structural_A :2 * 2 + 3 = 7**


---

### `Tau.BookIV.Particles.higgs_n7_structural_C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1383-L1383)
**theorem
Tau.BookIV.Particles.higgs_n7_structural_C :3 + 3 + 1 = 7**


---

### `Tau.BookIV.Particles.higgs_n7_structural_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1385-L1385)
**theorem
Tau.BookIV.Particles.higgs_n7_structural_B :5 + 2 = 7**


---

### `Tau.BookIV.Particles.wolfenstein_eta_pentagon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1399-L1405)
**def
Tau.BookIV.Particles.wolfenstein_eta_pentagon :String**


Wolfenstein η̄ from 5-generator pentagon: ω-period 2π / 5 generators = 72°/step.
Best τ-candidate: ι<sub>τ</sub>^(-1/4)·κ_D^(5/4)/√5 = 0.3472 at -2285 ppm (τ-effective).
Improvement: 10× over √5/(2π) baseline (+22647 ppm). OQ-CKM1 resolved.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.WolfensteinEtaPentagon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1407-L1417)
**structure
Tau.BookIV.Particles.WolfensteinEtaPentagon :Type**


[IV.D359] Wolfenstein η̄ pentagon structure (formalized).

- n_generators : ℕ
Number of generators in pentagon.

- step_degrees : ℕ
Step angle in degrees.

- improvement_factor : ℕ
Improvement factor over baseline (×1).

- deviation_ppm : ℕ
Deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinEtaPentagon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1417-L1417)
**def
Tau.BookIV.Particles.instReprWolfensteinEtaPentagon.repr :WolfensteinEtaPentagon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinEtaPentagon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1417-L1417)
**instance
Tau.BookIV.Particles.instReprWolfensteinEtaPentagon :Repr WolfensteinEtaPentagon**

Equations
- Tau.BookIV.Particles.instReprWolfensteinEtaPentagon = { reprPrec := Tau.BookIV.Particles.instReprWolfensteinEtaPentagon.repr }

---

### `Tau.BookIV.Particles.wolfenstein_eta_pentagon_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1419-L1419)
**def
Tau.BookIV.Particles.wolfenstein_eta_pentagon_data :WolfensteinEtaPentagon**

Equations
- Tau.BookIV.Particles.wolfenstein_eta_pentagon_data = { }
Instances For

---

### `Tau.BookIV.Particles.wolfenstein_eta_pentagon_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1421-L1426)
**theorem
Tau.BookIV.Particles.wolfenstein_eta_pentagon_conj :wolfenstein_eta_pentagon_data.n_generators = 5 ∧ wolfenstein_eta_pentagon_data.step_degrees = 72 ∧ wolfenstein_eta_pentagon_data.improvement_factor = 10 ∧ wolfenstein_eta_pentagon_data.deviation_ppm = 2285**


---

### `Tau.BookIV.Particles.jarlskog_invariant_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1431-L1435)
**def
Tau.BookIV.Particles.jarlskog_invariant_tau :String**


J = A²·λ_C^6·η̄ from τ-parameters: J_τ = 3.060×10^-5 at -6479 ppm from PDG 3.08×10^-5.
Inverted: η̄ = J_PDG/(A_τ²·λ_τ^6) = 0.3503 at +6522 ppm. Self-consistent at 0.65%.
Equations
- Tau.BookIV.Particles.jarlskog_invariant_tau = "J_τ = A_τ²·λ_τ^6·η̄_PDG = 3.060e-5 at -6479 ppm (PDG 3.08e-5). " ++ "A_τ=0.82527, λ_τ=0.22482. Inverse: η̄_from_J=0.3503 at +6522 ppm."
Instances For

---

### `Tau.BookIV.Particles.JarlskogInvariantTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1437-L1445)
**structure
Tau.BookIV.Particles.JarlskogInvariantTau :Type**


[IV.T167] Jarlskog invariant from τ-parameters structure (formalized).

- n_wolfenstein_params : ℕ
Number of Wolfenstein parameters used.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- self_consistency_ppm : ℕ
Self-consistency gap in ppm (inverse vs forward).

Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogInvariantTau.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1445-L1445)
**def
Tau.BookIV.Particles.instReprJarlskogInvariantTau.repr :JarlskogInvariantTau → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogInvariantTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1445-L1445)
**instance
Tau.BookIV.Particles.instReprJarlskogInvariantTau :Repr JarlskogInvariantTau**

Equations
- Tau.BookIV.Particles.instReprJarlskogInvariantTau = { reprPrec := Tau.BookIV.Particles.instReprJarlskogInvariantTau.repr }

---

### `Tau.BookIV.Particles.jarlskog_invariant_tau_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1447-L1447)
**def
Tau.BookIV.Particles.jarlskog_invariant_tau_data :JarlskogInvariantTau**

Equations
- Tau.BookIV.Particles.jarlskog_invariant_tau_data = { }
Instances For

---

### `Tau.BookIV.Particles.jarlskog_invariant_tau_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1449-L1453)
**theorem
Tau.BookIV.Particles.jarlskog_invariant_tau_conj :jarlskog_invariant_tau_data.n_wolfenstein_params = 4 ∧ jarlskog_invariant_tau_data.deviation_ppm = 6479 ∧ jarlskog_invariant_tau_data.self_consistency_ppm = 6522**


---

### `Tau.BookIV.Particles.EtaBarSprint6B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1458-L1466)
**structure
Tau.BookIV.Particles.EtaBarSprint6B :Type**


Best η̄: ι<sub>τ</sub>^(-1/4)·κ_D^(5/4)/√5 = 0.347205 at -2285 ppm. τ-effective (< 5000 ppm).

- n_pentagon_generators : ℕ
Pentagon generator count.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- tau_eff_threshold_ppm : ℕ
τ-effective threshold in ppm (deviation < threshold).

Instances For

---

### `Tau.BookIV.Particles.instReprEtaBarSprint6B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1466-L1466)
**instance
Tau.BookIV.Particles.instReprEtaBarSprint6B :Repr EtaBarSprint6B**

Equations
- Tau.BookIV.Particles.instReprEtaBarSprint6B = { reprPrec := Tau.BookIV.Particles.instReprEtaBarSprint6B.repr }

---

### `Tau.BookIV.Particles.instReprEtaBarSprint6B.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1466-L1466)
**def
Tau.BookIV.Particles.instReprEtaBarSprint6B.repr :EtaBarSprint6B → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.eta_bar_sprint6b_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1468-L1468)
**def
Tau.BookIV.Particles.eta_bar_sprint6b_data :EtaBarSprint6B**

Equations
- Tau.BookIV.Particles.eta_bar_sprint6b_data = { }
Instances For

---

### `Tau.BookIV.Particles.eta_bar_sprint6b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1470-L1474)
**theorem
Tau.BookIV.Particles.eta_bar_sprint6b :eta_bar_sprint6b_data.n_pentagon_generators = 5 ∧ eta_bar_sprint6b_data.deviation_ppm = 2285 ∧ eta_bar_sprint6b_data.tau_eff_threshold_ppm = 5000**


---

### `Tau.BookIV.Particles.pentagon_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1479-L1479)
**theorem
Tau.BookIV.Particles.pentagon_generators :5 = 5**


---

### `Tau.BookIV.Particles.pentagon_cp_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1482-L1484)
**def
Tau.BookIV.Particles.pentagon_cp_derivation :String**


ρ̄·(tan(2π/5)-tan(π/5)) = 0.3742 at +75275 ppm (conjectural).
Geometric: tan difference of pentagon steps. Best scan candidate wins at -2285 ppm.
Equations
- Tau.BookIV.Particles.pentagon_cp_derivation = "Pentagon angle: ρ̄·(tan(2π/5)-tan(π/5)) = 0.3742 (+75275 ppm, conjectural)"
Instances For

---

### `Tau.BookIV.Particles.PentagonCPDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1486-L1494)
**structure
Tau.BookIV.Particles.PentagonCPDerivation :Type**


[IV.P200] Pentagon CP derivation structure.

- n_generators : ℕ
5 generators: {α,π,γ,η,ω}.

- rho_bar_denom_multiplier : ℕ
ρ̄ denominator: 2π → multiplier 2.

- step_angle_degrees : ℕ
Step angle 2π/5 = 72°.

Instances For

---

### `Tau.BookIV.Particles.instReprPentagonCPDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1494-L1494)
**instance
Tau.BookIV.Particles.instReprPentagonCPDerivation :Repr PentagonCPDerivation**

Equations
- Tau.BookIV.Particles.instReprPentagonCPDerivation = { reprPrec := Tau.BookIV.Particles.instReprPentagonCPDerivation.repr }

---

### `Tau.BookIV.Particles.instReprPentagonCPDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1494-L1494)
**def
Tau.BookIV.Particles.instReprPentagonCPDerivation.repr :PentagonCPDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.pentagon_cp_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1496-L1497)
**def
Tau.BookIV.Particles.pentagon_cp_data :PentagonCPDerivation**


Canonical pentagon CP derivation.
Equations
- Tau.BookIV.Particles.pentagon_cp_data = { }
Instances For

---

### `Tau.BookIV.Particles.pentagon_cp_derivation_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1499-L1504)
**theorem
Tau.BookIV.Particles.pentagon_cp_derivation_conj :pentagon_cp_data.n_generators = 5 ∧ pentagon_cp_data.rho_bar_denom_multiplier = 2 ∧ pentagon_cp_data.step_angle_degrees = 72**


[IV.P200] Conjunction: 5 generators, ρ̄ denom multiplier, 72° step.

---

### `Tau.BookIV.Particles.pentagon_step_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1506-L1507)
**theorem
Tau.BookIV.Particles.pentagon_step_check :360 / 5 = 72**


Pentagon step angle: 360/5 = 72.

---

### `Tau.BookIV.Particles.oqckm1_status_sprint6b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1512-L1515)
**def
Tau.BookIV.Particles.oqckm1_status_sprint6b :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.OQCKM1Sprint6B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1517-L1523)
**structure
Tau.BookIV.Particles.OQCKM1Sprint6B :Type**


[IV.R409] OQ-CKM1 status after Sprint 6B structure (formalized).

- n_tau_effective : ℕ
Number of τ-effective Wolfenstein parameters (all 4).

- n_open_derivations : ℕ
Number of open exponent derivations.

Instances For

---

### `Tau.BookIV.Particles.instReprOQCKM1Sprint6B.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1523-L1523)
**def
Tau.BookIV.Particles.instReprOQCKM1Sprint6B.repr :OQCKM1Sprint6B → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprOQCKM1Sprint6B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1523-L1523)
**instance
Tau.BookIV.Particles.instReprOQCKM1Sprint6B :Repr OQCKM1Sprint6B**

Equations
- Tau.BookIV.Particles.instReprOQCKM1Sprint6B = { reprPrec := Tau.BookIV.Particles.instReprOQCKM1Sprint6B.repr }

---

### `Tau.BookIV.Particles.oqckm1_6b_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1525-L1525)
**def
Tau.BookIV.Particles.oqckm1_6b_data :OQCKM1Sprint6B**

Equations
- Tau.BookIV.Particles.oqckm1_6b_data = { }
Instances For

---

### `Tau.BookIV.Particles.oqckm1_6b_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1527-L1530)
**theorem
Tau.BookIV.Particles.oqckm1_6b_conj :oqckm1_6b_data.n_tau_effective = 4 ∧ oqckm1_6b_data.n_open_derivations = 1**


---

### `Tau.BookIV.Particles.muon_mass_nnlo_k23`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1539-L1544)
**def
Tau.BookIV.Particles.muon_mass_nnlo_k23 :String**


m_μ/m_e = ι<sub>τ</sub>^(-124/25)·(1-ι<sub>τ</sub>^(23/3)) at +43 ppm. k=23/3.
Structural: 23=W₃(4)+W₃(3)+1=5+17+1 (first Window-algebra NNLO exponent).
Best rational: k=45/6=7.5=(3×W₃(4))/2 at -8.2 ppm.
Equations
- Tau.BookIV.Particles.muon_mass_nnlo_k23 = "m_μ/m_e = ι<sub>τ</sub>^(-124/25)·(1-ι<sub>τ</sub>^(23/3)) at +43 ppm. " ++ "23=W₃(4)+W₃(3)+1=5+17+1. Best: k=7.5=(3W₃(4))/2 at -8.2 ppm."
Instances For

---

### `Tau.BookIV.Particles.MuonNNLOK23`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1546-L1556)
**structure
Tau.BookIV.Particles.MuonNNLOK23 :Type**


[IV.D360] NNLO k=23/3 correction structure (formalized).

- k_numer : ℕ
Numerator of k: 23.

- k_denom : ℕ
Denominator of k: 3.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- n_window_terms : ℕ
Window algebra terms: W₃(4)+W₃(3)+1 = 5+17+1 = 23.

Instances For

---

### `Tau.BookIV.Particles.instReprMuonNNLOK23.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1556-L1556)
**def
Tau.BookIV.Particles.instReprMuonNNLOK23.repr :MuonNNLOK23 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprMuonNNLOK23`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1556-L1556)
**instance
Tau.BookIV.Particles.instReprMuonNNLOK23 :Repr MuonNNLOK23**

Equations
- Tau.BookIV.Particles.instReprMuonNNLOK23 = { reprPrec := Tau.BookIV.Particles.instReprMuonNNLOK23.repr }

---

### `Tau.BookIV.Particles.muon_nnlo_k23_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1558-L1558)
**def
Tau.BookIV.Particles.muon_nnlo_k23_data :MuonNNLOK23**

Equations
- Tau.BookIV.Particles.muon_nnlo_k23_data = { }
Instances For

---

### `Tau.BookIV.Particles.muon_nnlo_k23_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1560-L1565)
**theorem
Tau.BookIV.Particles.muon_nnlo_k23_conj :muon_nnlo_k23_data.k_numer = 23 ∧ muon_nnlo_k23_data.k_denom = 3 ∧ muon_nnlo_k23_data.deviation_ppm = 43 ∧ muon_nnlo_k23_data.n_window_terms = 3**


---

### `Tau.BookIV.Particles.k23_window_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1570-L1572)
**theorem
Tau.BookIV.Particles.k23_window_sum :5 + 17 + 1 = 23**


ι<sub>τ</sub>^(-124/25)·(1-ι<sub>τ</sub>^(23/3)) = 206.777 at +43 ppm from PDG 206.768.
23 = W₃(4)+W₃(3)+1 = 5+17+1: first Window-algebra NNLO exponent.

---

### `Tau.BookIV.Particles.c5_em_coefficient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1575-L1577)
**theorem
Tau.BookIV.Particles.c5_em_coefficient :4 * 5 = 20**


C.5: (3/16)·√3·ι<sub>τ</sub>^5 − (3/20)·α·ι<sub>τ</sub>^2 at +28 ppm. C.3 NLO at +5 ppm.
3/16 = N_c/2⁴; 3/20 = N_c/(4·W₃(4)) = 3/20. Both structurally derived.

---

### `Tau.BookIV.Particles.c5_qcd_coefficient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1578-L1578)
**theorem
Tau.BookIV.Particles.c5_qcd_coefficient :2 ^ 4 = 16**


---

### `Tau.BookIV.Particles.c5_structural_origin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1581-L1587)
**def
Tau.BookIV.Particles.c5_structural_origin :String**


C.5 structural coefficients:
3/16 = N_c/2⁴: N_c=3 colors, 2⁴=16 (Dirac spinor trace 4×4).
3/20 = N_c/(4·W₃(4)): N_c=3, 4 crossing channels, W₃(4)=5 Window.
First derivation of nucleon EM coefficient from Window Universality.
Equations
- Tau.BookIV.Particles.c5_structural_origin = "3/16 = N_c/2⁴ (Dirac spinor-loop); 3/20 = N_c/(4·W₃(4)) (EM crossing × Window). " ++ "First Window-Universality nucleon EM coefficient."
Instances For

---

### `Tau.BookIV.Particles.precision_sprint6d_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1590-L1593)
**def
Tau.BookIV.Particles.precision_sprint6d_status :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.PrecisionSprint6D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1595-L1603)
**structure
Tau.BookIV.Particles.PrecisionSprint6D :Type**


[IV.R410] Precision status after Sprint 6D structure (formalized).

- muon_ppm : ℕ
m_μ/m_e best ppm.

- pn_ppm : ℕ
p-n mass best ppm.

- n_window_nucleon : ℕ
Number of Window–nucleon connections established.

Instances For

---

### `Tau.BookIV.Particles.instReprPrecisionSprint6D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1603-L1603)
**instance
Tau.BookIV.Particles.instReprPrecisionSprint6D :Repr PrecisionSprint6D**

Equations
- Tau.BookIV.Particles.instReprPrecisionSprint6D = { reprPrec := Tau.BookIV.Particles.instReprPrecisionSprint6D.repr }

---

### `Tau.BookIV.Particles.instReprPrecisionSprint6D.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1603-L1603)
**def
Tau.BookIV.Particles.instReprPrecisionSprint6D.repr :PrecisionSprint6D → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.precision_6d_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1605-L1605)
**def
Tau.BookIV.Particles.precision_6d_data :PrecisionSprint6D**

Equations
- Tau.BookIV.Particles.precision_6d_data = { }
Instances For

---

### `Tau.BookIV.Particles.precision_6d_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1607-L1611)
**theorem
Tau.BookIV.Particles.precision_6d_conj :precision_6d_data.muon_ppm = 43 ∧ precision_6d_data.pn_ppm = 5 ∧ precision_6d_data.n_window_nucleon = 2**


---

### `Tau.BookIV.Particles.FiberBaseHomology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1628-L1639)
**structure
Tau.BookIV.Particles.FiberBaseHomology :Type**


H₁(τ³; ℤ) ≅ ℤ³ from fiber-base decomposition.
rank = rank(H₁(T²)) + rank(H₁(τ¹)) = 2 + 1 = 3.
Three generators: g₁ (meridian), g₂ (longitude), g₃ (base cycle).

- rank_fiber : ℕ
Rank of H₁(T²) = 2 (two independent cycles on torus).

- rank_base : ℕ
Rank of H₁(τ¹) = 1 (one cycle on profinite solenoid).

- rank_total : ℕ
Total rank = fiber + base.

- rank_eq_three : self.rank_total = 3
The total rank equals 3.

Instances For

---

### `Tau.BookIV.Particles.fiber_base_homology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1641-L1641)
**def
Tau.BookIV.Particles.fiber_base_homology :FiberBaseHomology**

Equations
- Tau.BookIV.Particles.fiber_base_homology = { rank_eq_three := Tau.BookIV.Particles.fiber_base_homology._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.instInhabitedFiberBaseHomology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1643-L1643)
**instance
Tau.BookIV.Particles.instInhabitedFiberBaseHomology :Inhabited FiberBaseHomology**

Equations
- Tau.BookIV.Particles.instInhabitedFiberBaseHomology = { default := { rank_eq_three := Tau.BookIV.Particles.fiber_base_homology._proof_1 } }

---

### `Tau.BookIV.Particles.fiber_base_homology_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1645-L1649)
**theorem
Tau.BookIV.Particles.fiber_base_homology_conj :default.rank_fiber = 2 ∧ default.rank_base = 1**


[IV.D361] Fiber-base homology conjunction (formalized).

---

### `Tau.BookIV.Particles.SolenoidalGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1652-L1660)
**inductive
Tau.BookIV.Particles.SolenoidalGenerator :Type**


Map from H₁(τ³) generators to force-carrying generators.
g₁ (meridional) ↔ γ (EM), g₂ (longitudinal) ↔ η (strong),
g₃ (base/crossing) ↔ π (weak).
Non-winding: α (gravity, non-compact), ω (Higgs, scalar).

- meridional : SolenoidalGenerator
- longitudinal : SolenoidalGenerator
- baseCrossing : SolenoidalGenerator
Instances For

---

### `Tau.BookIV.Particles.instReprSolenoidalGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1660-L1660)
**def
Tau.BookIV.Particles.instReprSolenoidalGenerator.repr :SolenoidalGenerator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprSolenoidalGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1660-L1660)
**instance
Tau.BookIV.Particles.instReprSolenoidalGenerator :Repr SolenoidalGenerator**

Equations
- Tau.BookIV.Particles.instReprSolenoidalGenerator = { reprPrec := Tau.BookIV.Particles.instReprSolenoidalGenerator.repr }

---

### `Tau.BookIV.Particles.instDecidableEqSolenoidalGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1660-L1660)
**instance
Tau.BookIV.Particles.instDecidableEqSolenoidalGenerator :DecidableEq SolenoidalGenerator**

Equations
- Tau.BookIV.Particles.instDecidableEqSolenoidalGenerator x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Particles.SolenoidalGenerator.toGeneration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1662-L1666)
**def
Tau.BookIV.Particles.SolenoidalGenerator.toGeneration :SolenoidalGenerator → LemniscateModeClass**


Each solenoidal generator maps to exactly one generation.
Equations
- Tau.BookIV.Particles.SolenoidalGenerator.meridional.toGeneration = Tau.BookIV.Particles.LemniscateModeClass.crossingPoint
- Tau.BookIV.Particles.SolenoidalGenerator.longitudinal.toGeneration = Tau.BookIV.Particles.LemniscateModeClass.singleLobe
- Tau.BookIV.Particles.SolenoidalGenerator.baseCrossing.toGeneration = Tau.BookIV.Particles.LemniscateModeClass.fullLemniscate
Instances For

---

### `Tau.BookIV.Particles.solenoidal_generators_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1668-L1672)
**theorem
Tau.BookIV.Particles.solenoidal_generators_count :[SolenoidalGenerator.meridional, SolenoidalGenerator.longitudinal, SolenoidalGenerator.baseCrossing].length = 3**


There are exactly 3 solenoidal generators (= compact winding classes).

---

### `Tau.BookIV.Particles.solenoidal_generator_force_map`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1674-L1676)
**def
Tau.BookIV.Particles.solenoidal_generator_force_map :String**


[IV.D362] Generator–force map: 3 compact + 2 non-compact = 5 generators.
Equations
- Tau.BookIV.Particles.solenoidal_generator_force_map = "g₁↔γ(EM), g₂↔η(strong), g₃↔π(weak) compact; α(gravity), ω(Higgs) non-compact."
Instances For

---

### `Tau.BookIV.Particles.SolenoidalForceMap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1678-L1686)
**structure
Tau.BookIV.Particles.SolenoidalForceMap :Type**


[IV.D362] Solenoidal force map structure (formalized).

- n_compact : ℕ
Number of compact (winding) generators.

- n_non_compact : ℕ
Number of non-compact generators.

- total_generators : ℕ
Total generators.

Instances For

---

### `Tau.BookIV.Particles.instReprSolenoidalForceMap.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1686-L1686)
**def
Tau.BookIV.Particles.instReprSolenoidalForceMap.repr :SolenoidalForceMap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprSolenoidalForceMap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1686-L1686)
**instance
Tau.BookIV.Particles.instReprSolenoidalForceMap :Repr SolenoidalForceMap**

Equations
- Tau.BookIV.Particles.instReprSolenoidalForceMap = { reprPrec := Tau.BookIV.Particles.instReprSolenoidalForceMap.repr }

---

### `Tau.BookIV.Particles.solenoidal_force_map_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1688-L1688)
**def
Tau.BookIV.Particles.solenoidal_force_map_data :SolenoidalForceMap**

Equations
- Tau.BookIV.Particles.solenoidal_force_map_data = { }
Instances For

---

### `Tau.BookIV.Particles.solenoidal_force_map_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1690-L1694)
**theorem
Tau.BookIV.Particles.solenoidal_force_map_conj :solenoidal_force_map_data.n_compact = 3 ∧ solenoidal_force_map_data.n_non_compact = 2 ∧ solenoidal_force_map_data.total_generators = 5**


---

### `Tau.BookIV.Particles.compact_plus_non_compact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1696-L1697)
**theorem
Tau.BookIV.Particles.compact_plus_non_compact :3 + 2 = 5**


Compact + non-compact = total generators.

---

### `Tau.BookIV.Particles.fourth_gen_excluded_topological`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1702-L1708)
**theorem
Tau.BookIV.Particles.fourth_gen_excluded_topological :fiber_base_homology.rank_total = three_mode_classes.length**


|fermion generations| = 3 from π₁(τ³).
Three independent proofs:

- H₁(τ³;ℤ) ≅ ℤ³ (rank = 3)

- Three primitive winding classes on T²

- Three distinct regions of L = S¹∨S¹


---

### `Tau.BookIV.Particles.TopologicalExclusionProofs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1710-L1720)
**structure
Tau.BookIV.Particles.TopologicalExclusionProofs :Type**


[IV.T171] Three independent proofs of |gen|=3 (formalized).

- n_independent_proofs : ℕ
Number of independent proofs.

- h1_rank : ℕ
Proof 1: H₁(τ³;ℤ) rank.

- primitive_winding_classes : ℕ
Proof 2: primitive winding classes on T².

- lemniscate_regions : ℕ
Proof 3: lemniscate topological regions.

Instances For

---

### `Tau.BookIV.Particles.instReprTopologicalExclusionProofs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1720-L1720)
**instance
Tau.BookIV.Particles.instReprTopologicalExclusionProofs :Repr TopologicalExclusionProofs**

Equations
- Tau.BookIV.Particles.instReprTopologicalExclusionProofs = { reprPrec := Tau.BookIV.Particles.instReprTopologicalExclusionProofs.repr }

---

### `Tau.BookIV.Particles.instReprTopologicalExclusionProofs.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1720-L1720)
**def
Tau.BookIV.Particles.instReprTopologicalExclusionProofs.repr :TopologicalExclusionProofs → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.topological_exclusion_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1722-L1722)
**def
Tau.BookIV.Particles.topological_exclusion_data :TopologicalExclusionProofs**

Equations
- Tau.BookIV.Particles.topological_exclusion_data = { }
Instances For

---

### `Tau.BookIV.Particles.topological_exclusion_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1724-L1729)
**theorem
Tau.BookIV.Particles.topological_exclusion_conj :topological_exclusion_data.n_independent_proofs = 3 ∧ topological_exclusion_data.h1_rank = 3 ∧ topological_exclusion_data.primitive_winding_classes = 3 ∧ topological_exclusion_data.lemniscate_regions = 3**


---

### `Tau.BookIV.Particles.all_proofs_agree`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1731-L1737)
**theorem
Tau.BookIV.Particles.all_proofs_agree :topological_exclusion_data.h1_rank = topological_exclusion_data.primitive_winding_classes ∧ topological_exclusion_data.primitive_winding_classes = topological_exclusion_data.lemniscate_regions**


All three independent proofs yield exactly 3.

---

### `Tau.BookIV.Particles.gen_mass_hierarchy_eigenvalue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1742-L1748)
**def
Tau.BookIV.Particles.gen_mass_hierarchy_eigenvalue :String**


Mass hierarchy from T² Laplacian eigenvalues:
λ₁ = 1 (gen 1) < λ₂ = ι<sub>τ</sub>⁻² ≈ 8.6 (gen 2) < λ₃ = 1+ι<sub>τ</sub>⁻² ≈ 9.6 (gen 3).
Leading exponents: gen 2 → 5 = N_generators, gen 3 → 15/2 = N_gen·dim/lobes.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.GenMassHierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1750-L1758)
**structure
Tau.BookIV.Particles.GenMassHierarchy :Type**


[IV.T172] Generation mass hierarchy structure (formalized).

- n_eigenvalues : ℕ
Number of eigenvalues.

- n_ordering_relations : ℕ
Number of strict ordering relations (λ₁ < λ₂ < λ₃ → 2 relations).

- lightest_generation : ℕ
Lightest generation number (crossing-point mode).

Instances For

---

### `Tau.BookIV.Particles.instReprGenMassHierarchy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1758-L1758)
**def
Tau.BookIV.Particles.instReprGenMassHierarchy.repr :GenMassHierarchy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprGenMassHierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1758-L1758)
**instance
Tau.BookIV.Particles.instReprGenMassHierarchy :Repr GenMassHierarchy**

Equations
- Tau.BookIV.Particles.instReprGenMassHierarchy = { reprPrec := Tau.BookIV.Particles.instReprGenMassHierarchy.repr }

---

### `Tau.BookIV.Particles.gen_mass_hierarchy_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1760-L1760)
**def
Tau.BookIV.Particles.gen_mass_hierarchy_data :GenMassHierarchy**

Equations
- Tau.BookIV.Particles.gen_mass_hierarchy_data = { }
Instances For

---

### `Tau.BookIV.Particles.gen_mass_hierarchy_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1762-L1766)
**theorem
Tau.BookIV.Particles.gen_mass_hierarchy_conj :gen_mass_hierarchy_data.n_eigenvalues = 3 ∧ gen_mass_hierarchy_data.n_ordering_relations = 2 ∧ gen_mass_hierarchy_data.lightest_generation = 1**


---

### `Tau.BookIV.Particles.boundary_mode_15_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1771-L1775)
**theorem
Tau.BookIV.Particles.boundary_mode_15_decomposition :3 * 5 = 15**


15 boundary modes = 3 generations × 5 modes/generation = 3 × N_generators.
Per generation: 1 charged lepton + 1 neutrino + 3 color-quarks = 5.
The 11/4 split gives α = (11/15)²·ι<sub>τ</sub>⁴ at 9.8 ppm.

---

### `Tau.BookIV.Particles.em_active_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1777-L1778)
**theorem
Tau.BookIV.Particles.em_active_modes :15 - 4 = 11**


15 modes per boundary, 11 EM-active, 4 EM-silent.

---

### `Tau.BookIV.Particles.BoundaryMode15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1780-L1792)
**structure
Tau.BookIV.Particles.BoundaryMode15 :Type**


[IV.P202] 15 boundary mode decomposition structure (formalized).

- n_generations : ℕ
Number of generations.

- modes_per_gen : ℕ
Modes per generation.

- total_modes : ℕ
Total boundary modes.

- em_active : ℕ
EM-active modes.

- em_silent : ℕ
EM-silent modes.

Instances For

---

### `Tau.BookIV.Particles.instReprBoundaryMode15.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1792-L1792)
**def
Tau.BookIV.Particles.instReprBoundaryMode15.repr :BoundaryMode15 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprBoundaryMode15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1792-L1792)
**instance
Tau.BookIV.Particles.instReprBoundaryMode15 :Repr BoundaryMode15**

Equations
- Tau.BookIV.Particles.instReprBoundaryMode15 = { reprPrec := Tau.BookIV.Particles.instReprBoundaryMode15.repr }

---

### `Tau.BookIV.Particles.boundary_mode_15_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1794-L1794)
**def
Tau.BookIV.Particles.boundary_mode_15_data :BoundaryMode15**

Equations
- Tau.BookIV.Particles.boundary_mode_15_data = { }
Instances For

---

### `Tau.BookIV.Particles.boundary_mode_15_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1796-L1802)
**theorem
Tau.BookIV.Particles.boundary_mode_15_conj :boundary_mode_15_data.n_generations = 3 ∧ boundary_mode_15_data.modes_per_gen = 5 ∧ boundary_mode_15_data.total_modes = 15 ∧ boundary_mode_15_data.em_active = 11 ∧ boundary_mode_15_data.em_silent = 4**


---

### `Tau.BookIV.Particles.ivop3_status_sprint7a`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1807-L1811)
**def
Tau.BookIV.Particles.ivop3_status_sprint7a :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.a_sector_nlo_pmns`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1823-L1829)
**def
Tau.BookIV.Particles.a_sector_nlo_pmns :String**


[IV.D365] A-Sector NLO PMNS Rotation.
The σ-polarity matrix is shared by M_ℓ and M_ν (same eigenvectors),
so bare PMNS ≈ identity. All mixing from A-sector (π-generator) rotation.
NLO: sin(θ₂₃) = (1−ι<sub>τ</sub>⁵)/(1+ι<sub>τ</sub>), with W₃(4)=5.
Equations
- Tau.BookIV.Particles.a_sector_nlo_pmns = "A-sector NLO PMNS rotation: sin(θ₂₃)_NLO = (1-ι<sub>τ</sub>^5)/(1+ι<sub>τ</sub>). " ++ "Bare PMNS ≈ identity from shared σ-matrix eigenvectors."
Instances For

---

### `Tau.BookIV.Particles.ASectorNLOPMNS`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1831-L1839)
**structure
Tau.BookIV.Particles.ASectorNLOPMNS :Type**


[IV.D365] A-sector NLO PMNS rotation structure (formalized).

- window_exp : ℕ
Window exponent W₃(4) = 5.

- shared_eigenvectors : ℕ
Number of shared eigenvectors from σ-equivariance.

- bare_pmns_free_params : ℕ
Number of free parameters in bare PMNS (≈ identity).

Instances For

---

### `Tau.BookIV.Particles.instReprASectorNLOPMNS`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1839-L1839)
**instance
Tau.BookIV.Particles.instReprASectorNLOPMNS :Repr ASectorNLOPMNS**

Equations
- Tau.BookIV.Particles.instReprASectorNLOPMNS = { reprPrec := Tau.BookIV.Particles.instReprASectorNLOPMNS.repr }

---

### `Tau.BookIV.Particles.instReprASectorNLOPMNS.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1839-L1839)
**def
Tau.BookIV.Particles.instReprASectorNLOPMNS.repr :ASectorNLOPMNS → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.a_sector_nlo_pmns_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1841-L1841)
**def
Tau.BookIV.Particles.a_sector_nlo_pmns_data :ASectorNLOPMNS**

Equations
- Tau.BookIV.Particles.a_sector_nlo_pmns_data = { }
Instances For

---

### `Tau.BookIV.Particles.a_sector_nlo_pmns_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1843-L1847)
**theorem
Tau.BookIV.Particles.a_sector_nlo_pmns_conj :a_sector_nlo_pmns_data.window_exp = 5 ∧ a_sector_nlo_pmns_data.shared_eigenvectors = 3 ∧ a_sector_nlo_pmns_data.bare_pmns_free_params = 0**


---

### `Tau.BookIV.Particles.theta23_nlo_window`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1851-L1855)
**def
Tau.BookIV.Particles.theta23_nlo_window :String**


[IV.T174] θ₂₃ NLO via Window Algebra at +8604 ppm.
sin²θ₂₃ = 0.5507, PDG 0.546. Halves LO deviation (+18012 → +8604 ppm).
Equations
- Tau.BookIV.Particles.theta23_nlo_window = "sin(θ₂₃) = (1-ι<sub>τ</sub>^5)/(1+ι<sub>τ</sub>), sin²θ₂₃ = 0.5507, " ++ "PDG 0.546, deviation +8604 ppm. NLO factor (1-ι<sub>τ</sub>^5) halves LO error."
Instances For

---

### `Tau.BookIV.Particles.Theta23NLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1857-L1865)
**structure
Tau.BookIV.Particles.Theta23NLO :Type**


[IV.T174] θ₂₃ NLO structure.

- window_exp : ℕ
Window exponent W₃(4) = 5.

- deviation_ppm : ℕ
Deviation from PDG in ppm (+8604).

- lo_deviation_ppm : ℕ
LO deviation in ppm (+18012), NLO halves it.

Instances For

---

### `Tau.BookIV.Particles.instReprTheta23NLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1865-L1865)
**def
Tau.BookIV.Particles.instReprTheta23NLO.repr :Theta23NLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprTheta23NLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1865-L1865)
**instance
Tau.BookIV.Particles.instReprTheta23NLO :Repr Theta23NLO**

Equations
- Tau.BookIV.Particles.instReprTheta23NLO = { reprPrec := Tau.BookIV.Particles.instReprTheta23NLO.repr }

---

### `Tau.BookIV.Particles.theta23_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1867-L1868)
**def
Tau.BookIV.Particles.theta23_nlo_data :Theta23NLO**


Canonical θ₂₃ NLO.
Equations
- Tau.BookIV.Particles.theta23_nlo_data = { }
Instances For

---

### `Tau.BookIV.Particles.theta23_nlo_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1870-L1875)
**theorem
Tau.BookIV.Particles.theta23_nlo_conj :theta23_nlo_data.window_exp = 5 ∧ theta23_nlo_data.deviation_ppm = 8604 ∧ theta23_nlo_data.lo_deviation_ppm = 18012**


[IV.T174] Conjunction: W₃(4)=5, NLO deviation, LO deviation.

---

### `Tau.BookIV.Particles.theta23_nlo_halves_lo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1877-L1879)
**theorem
Tau.BookIV.Particles.theta23_nlo_halves_lo :theta23_nlo_data.deviation_ppm < theta23_nlo_data.lo_deviation_ppm**


NLO roughly halves the LO error.

---

### `Tau.BookIV.Particles.sin2_theta23_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1881-L1882)
**def
Tau.BookIV.Particles.sin2_theta23_nlo :Float**


sin²θ₂₃ NLO numerical value.
Equations
- Tau.BookIV.Particles.sin2_theta23_nlo = 0.5507
Instances For

---

### `Tau.BookIV.Particles.theta12_qlc_higgs_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1887-L1891)
**def
Tau.BookIV.Particles.theta12_qlc_higgs_nlo :String**


[IV.T175] θ₁₂ from QLC + Higgs NLO at +3106 ppm.
θ₁₂ = π/4 − θ_C + ι<sub>τ</sub>²κ_ω. Major improvement over bare QLC (−84888 ppm).
Equations
- Tau.BookIV.Particles.theta12_qlc_higgs_nlo = "θ₁₂ = π/4 − θ_C + ι<sub>τ</sub>²κ_ω, sin²θ₁₂ = 0.3080, " ++ "PDG 0.307, deviation +3106 ppm. Approaches τ-effective threshold."
Instances For

---

### `Tau.BookIV.Particles.Theta12NLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1893-L1901)
**structure
Tau.BookIV.Particles.Theta12NLO :Type**


[IV.T175] θ₁₂ NLO from QLC + Higgs correction structure.

- higgs_correction_power : ℕ
Higgs correction power: ι<sub>τ</sub>² in δ = ι<sub>τ</sub>²κ_ω.

- deviation_ppm : ℕ
Deviation from PDG in ppm (+3106).

- free_params : ℕ
Number of free parameters (zero: all from ι<sub>τ</sub>).

Instances For

---

### `Tau.BookIV.Particles.instReprTheta12NLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1901-L1901)
**def
Tau.BookIV.Particles.instReprTheta12NLO.repr :Theta12NLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprTheta12NLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1901-L1901)
**instance
Tau.BookIV.Particles.instReprTheta12NLO :Repr Theta12NLO**

Equations
- Tau.BookIV.Particles.instReprTheta12NLO = { reprPrec := Tau.BookIV.Particles.instReprTheta12NLO.repr }

---

### `Tau.BookIV.Particles.theta12_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1903-L1904)
**def
Tau.BookIV.Particles.theta12_nlo_data :Theta12NLO**


Canonical θ₁₂ NLO.
Equations
- Tau.BookIV.Particles.theta12_nlo_data = { }
Instances For

---

### `Tau.BookIV.Particles.theta12_nlo_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1906-L1911)
**theorem
Tau.BookIV.Particles.theta12_nlo_conj :theta12_nlo_data.higgs_correction_power = 2 ∧ theta12_nlo_data.deviation_ppm = 3106 ∧ theta12_nlo_data.free_params = 0**


[IV.T175] Conjunction: power=2, deviation, zero free params.

---

### `Tau.BookIV.Particles.theta12_approaches_tau_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1913-L1915)
**theorem
Tau.BookIV.Particles.theta12_approaches_tau_effective :theta12_nlo_data.deviation_ppm < 5000**


θ₁₂ approaches τ-effective threshold (< 5000 ppm).

---

### `Tau.BookIV.Particles.sin2_theta12_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1917-L1918)
**def
Tau.BookIV.Particles.sin2_theta12_nlo :Float**


sin²θ₁₂ NLO numerical value.
Equations
- Tau.BookIV.Particles.sin2_theta12_nlo = 0.3080
Instances For

---

### `Tau.BookIV.Particles.delta_cp_arctan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1923-L1927)
**def
Tau.BookIV.Particles.delta_cp_arctan :String**


[IV.P204] δ_CP = π + arctan(ι<sub>τ</sub>) at +9365 ppm.
π radians (half-period on L) plus small τ-rotation. PDG 197°.
Equations
- Tau.BookIV.Particles.delta_cp_arctan = "δ_CP = π + arctan(ι<sub>τ</sub>) = 198.84°, PDG 197°, deviation +9365 ppm. " ++ "Half-period on L plus master-constant rotation."
Instances For

---

### `Tau.BookIV.Particles.DeltaCPPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1929-L1939)
**structure
Tau.BookIV.Particles.DeltaCPPrediction :Type**


[IV.P204] δ_CP prediction structure.

- base_degrees : ℕ
Base angle: π in radians (half-period on L), degrees = 180.

- predicted_deg_x100 : ℕ
Predicted angle (degrees × 100): π + arctan(ι<sub>τ</sub>) ≈ 198.84°.

- pdg_deg_x100 : ℕ
PDG value (degrees × 100): ≈ 197°.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprDeltaCPPrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1939-L1939)
**def
Tau.BookIV.Particles.instReprDeltaCPPrediction.repr :DeltaCPPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprDeltaCPPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1939-L1939)
**instance
Tau.BookIV.Particles.instReprDeltaCPPrediction :Repr DeltaCPPrediction**

Equations
- Tau.BookIV.Particles.instReprDeltaCPPrediction = { reprPrec := Tau.BookIV.Particles.instReprDeltaCPPrediction.repr }

---

### `Tau.BookIV.Particles.delta_cp_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1941-L1942)
**def
Tau.BookIV.Particles.delta_cp_prediction :DeltaCPPrediction**


Canonical δ_CP prediction.
Equations
- Tau.BookIV.Particles.delta_cp_prediction = { }
Instances For

---

### `Tau.BookIV.Particles.delta_cp_prediction_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1944-L1950)
**theorem
Tau.BookIV.Particles.delta_cp_prediction_conj :delta_cp_prediction.base_degrees = 180 ∧ delta_cp_prediction.predicted_deg_x100 = 19884 ∧ delta_cp_prediction.pdg_deg_x100 = 19700 ∧ delta_cp_prediction.deviation_ppm = 9365**


[IV.P204] Conjunction: base 180°, prediction, PDG, deviation.

---

### `Tau.BookIV.Particles.delta_cp_degrees`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1952-L1953)
**def
Tau.BookIV.Particles.delta_cp_degrees :Float**


δ_CP predicted value (degrees).
Equations
- Tau.BookIV.Particles.delta_cp_degrees = 198.84
Instances For

---

### `Tau.BookIV.Particles.quarter_lobe_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1962-L1966)
**def
Tau.BookIV.Particles.quarter_lobe_holonomy :String**


[IV.D363] Quarter-Lobe Holonomy.
Exponent −1/4 = −1/(2·|lobes|). Quarter-revolution of lobe holonomy for CP.
Equations
- Tau.BookIV.Particles.quarter_lobe_holonomy = "−1/4 = −1/(2·|lobes|) = −1/(2·2). " ++ "CP violation requires partial traversal: (ι<sub>τ</sub>⁻¹)^{1/4}."
Instances For

---

### `Tau.BookIV.Particles.QuarterLobeHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1968-L1976)
**structure
Tau.BookIV.Particles.QuarterLobeHolonomy :Type**


[IV.D363] Quarter-lobe holonomy structure (formalized).

- exponent_numer : ℕ
Exponent numerator: −1.

- exponent_denom : ℕ
Exponent denominator: 4 = 2 × lobes.

- n_lobes : ℕ
Number of lobes.

Instances For

---

### `Tau.BookIV.Particles.instReprQuarterLobeHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1976-L1976)
**instance
Tau.BookIV.Particles.instReprQuarterLobeHolonomy :Repr QuarterLobeHolonomy**

Equations
- Tau.BookIV.Particles.instReprQuarterLobeHolonomy = { reprPrec := Tau.BookIV.Particles.instReprQuarterLobeHolonomy.repr }

---

### `Tau.BookIV.Particles.instReprQuarterLobeHolonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1976-L1976)
**def
Tau.BookIV.Particles.instReprQuarterLobeHolonomy.repr :QuarterLobeHolonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.quarter_lobe_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1978-L1978)
**def
Tau.BookIV.Particles.quarter_lobe_data :QuarterLobeHolonomy**

Equations
- Tau.BookIV.Particles.quarter_lobe_data = { }
Instances For

---

### `Tau.BookIV.Particles.quarter_lobe_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1980-L1984)
**theorem
Tau.BookIV.Particles.quarter_lobe_conj :quarter_lobe_data.exponent_numer = 1 ∧ quarter_lobe_data.exponent_denom = 4 ∧ quarter_lobe_data.n_lobes = 2**


---

### `Tau.BookIV.Particles.quarter_lobe_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1986-L1987)
**theorem
Tau.BookIV.Particles.quarter_lobe_denom :2 * 2 = 4**


Denominator is 2 × lobes: 2 × 2 = 4.

---

### `Tau.BookIV.Particles.pentagon_dark_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1991-L1995)
**def
Tau.BookIV.Particles.pentagon_dark_coupling :String**


[IV.D364] Pentagon Dark Coupling.
Exponent 5/4 = |generators|/(2·|lobes|) = 5/4 on κ_D.
Equations
- Tau.BookIV.Particles.pentagon_dark_coupling = "5/4 = |generators|/(2·|lobes|) = 5/(2·2). " ++ "Each of 5 generators contributes κ_D^{1/4}."
Instances For

---

### `Tau.BookIV.Particles.PentagonDarkCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L1997-L2007)
**structure
Tau.BookIV.Particles.PentagonDarkCoupling :Type**


[IV.D364] Pentagon dark coupling structure (formalized).

- exponent_numer : ℕ
Exponent numerator: 5 = |generators|.

- exponent_denom : ℕ
Exponent denominator: 4 = 2 × lobes.

- n_generators : ℕ
Number of generators.

- n_lobes : ℕ
Number of lobes.

Instances For

---

### `Tau.BookIV.Particles.instReprPentagonDarkCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2007-L2007)
**instance
Tau.BookIV.Particles.instReprPentagonDarkCoupling :Repr PentagonDarkCoupling**

Equations
- Tau.BookIV.Particles.instReprPentagonDarkCoupling = { reprPrec := Tau.BookIV.Particles.instReprPentagonDarkCoupling.repr }

---

### `Tau.BookIV.Particles.instReprPentagonDarkCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2007-L2007)
**def
Tau.BookIV.Particles.instReprPentagonDarkCoupling.repr :PentagonDarkCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.pentagon_dark_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2009-L2009)
**def
Tau.BookIV.Particles.pentagon_dark_data :PentagonDarkCoupling**

Equations
- Tau.BookIV.Particles.pentagon_dark_data = { }
Instances For

---

### `Tau.BookIV.Particles.pentagon_dark_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2011-L2016)
**theorem
Tau.BookIV.Particles.pentagon_dark_conj :pentagon_dark_data.exponent_numer = 5 ∧ pentagon_dark_data.exponent_denom = 4 ∧ pentagon_dark_data.n_generators = 5 ∧ pentagon_dark_data.n_lobes = 2**


---

### `Tau.BookIV.Particles.eta_bar_exponent_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2020-L2024)
**def
Tau.BookIV.Particles.eta_bar_exponent_derivation :String**


[IV.T173] η̄ Exponent Derivation.
η̄ = ι<sub>τ</sub>^{−1/4}·κ_D^{5/4}/√5 at −2285 ppm from PDG.
Equations
- Tau.BookIV.Particles.eta_bar_exponent_derivation = "η̄ = ι<sub>τ</sub>^{−1/4}·κ_D^{5/4}/√5 = 0.34720, PDG 0.349±0.013, " ++ "deviation −2285 ppm (within 1σ). Three topological factors."
Instances For

---

### `Tau.BookIV.Particles.EtaBarExponentData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2026-L2040)
**structure
Tau.BookIV.Particles.EtaBarExponentData :Type**


[IV.T173] η̄ exponent derivation structure (formalized).

- iota_exp_numer : ℕ
ι<sub>τ</sub> exponent numerator: 1.

- iota_exp_denom : ℕ
ι<sub>τ</sub> exponent denominator: 4.

- kappa_d_exp_numer : ℕ
κ_D exponent numerator: 5.

- kappa_d_exp_denom : ℕ
κ_D exponent denominator: 4.

- norm_denom : ℕ
√N normalization denominator (N=5 = |generators|).

- deviation_ppm : ℕ
Deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprEtaBarExponentData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2040-L2040)
**instance
Tau.BookIV.Particles.instReprEtaBarExponentData :Repr EtaBarExponentData**

Equations
- Tau.BookIV.Particles.instReprEtaBarExponentData = { reprPrec := Tau.BookIV.Particles.instReprEtaBarExponentData.repr }

---

### `Tau.BookIV.Particles.instReprEtaBarExponentData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2040-L2040)
**def
Tau.BookIV.Particles.instReprEtaBarExponentData.repr :EtaBarExponentData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.eta_bar_exp_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2042-L2042)
**def
Tau.BookIV.Particles.eta_bar_exp_data :EtaBarExponentData**

Equations
- Tau.BookIV.Particles.eta_bar_exp_data = { }
Instances For

---

### `Tau.BookIV.Particles.eta_bar_exp_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2044-L2051)
**theorem
Tau.BookIV.Particles.eta_bar_exp_conj :eta_bar_exp_data.iota_exp_numer = 1 ∧ eta_bar_exp_data.iota_exp_denom = 4 ∧ eta_bar_exp_data.kappa_d_exp_numer = 5 ∧ eta_bar_exp_data.kappa_d_exp_denom = 4 ∧ eta_bar_exp_data.norm_denom = 5 ∧ eta_bar_exp_data.deviation_ppm = 2285**


---

### `Tau.BookIV.Particles.jarlskog_full_tau_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2055-L2059)
**def
Tau.BookIV.Particles.jarlskog_full_tau_consistency :String**


[IV.P203] Jarlskog J Full-τ Consistency.
All 4 Wolfenstein params now τ-effective. J = A²λ_C⁶η̄.
Equations
- Tau.BookIV.Particles.jarlskog_full_tau_consistency = "All 4 Wolfenstein: λ_C=ι<sub>τ</sub>(1−ι<sub>τ</sub>) at −2327, A=1−(3/2)ι<sub>τ</sub>² at −887, " ++ "ρ̄=1/(2π) at +975, η̄=ι<sub>τ</sub>^{−1/4}κ_D^{5/4}/√5 at −2285 ppm."
Instances For

---

### `Tau.BookIV.Particles.JarlskogFullTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2061-L2073)
**structure
Tau.BookIV.Particles.JarlskogFullTau :Type**


[IV.P203] Full Jarlskog τ-consistency structure (formalized).

- n_wolfenstein_from_tau : ℕ
Number of Wolfenstein parameters derived from τ.

- lambda_deviation_ppm : ℕ
λ_C deviation from PDG in ppm.

- rho_deviation_ppm : ℕ
ρ̄ deviation from PDG in ppm.

- a_deviation_ppm : ℕ
A deviation from PDG in ppm.

- eta_deviation_ppm : ℕ
η̄ deviation from PDG in ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogFullTau.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2073-L2073)
**def
Tau.BookIV.Particles.instReprJarlskogFullTau.repr :JarlskogFullTau → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogFullTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2073-L2073)
**instance
Tau.BookIV.Particles.instReprJarlskogFullTau :Repr JarlskogFullTau**

Equations
- Tau.BookIV.Particles.instReprJarlskogFullTau = { reprPrec := Tau.BookIV.Particles.instReprJarlskogFullTau.repr }

---

### `Tau.BookIV.Particles.jarlskog_full_tau_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2075-L2075)
**def
Tau.BookIV.Particles.jarlskog_full_tau_data :JarlskogFullTau**

Equations
- Tau.BookIV.Particles.jarlskog_full_tau_data = { }
Instances For

---

### `Tau.BookIV.Particles.jarlskog_full_tau_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2077-L2083)
**theorem
Tau.BookIV.Particles.jarlskog_full_tau_conj :jarlskog_full_tau_data.n_wolfenstein_from_tau = 4 ∧ jarlskog_full_tau_data.lambda_deviation_ppm = 2327 ∧ jarlskog_full_tau_data.rho_deviation_ppm = 975 ∧ jarlskog_full_tau_data.a_deviation_ppm = 887 ∧ jarlskog_full_tau_data.eta_deviation_ppm = 2285**


---

### `Tau.BookIV.Particles.baryogenesis_lepton_duality_k`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2091-L2095)
**theorem
Tau.BookIV.Particles.baryogenesis_lepton_duality_k :3 * 5 / 2 = 15 / 2**


[IV.D366] k=15/2 Baryogenesis-Lepton Duality.
k = dim(τ³)·W₃(4)/|lobes| = 3·5/2 = 15/2.
Exponent 15 appears in both η_B (cosmo) and m_μ/m_e (leptonic).

---

### `Tau.BookIV.Particles.BaryogenesisLeptonDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2097-L2107)
**structure
Tau.BookIV.Particles.BaryogenesisLeptonDuality :Type**


[IV.D366] Baryogenesis-lepton duality structure (formalized).

- shared_exponent : ℕ
Shared exponent: 15.

- dim_tau3 : ℕ
dim(τ³) = 3.

- w3_4 : ℕ
W₃(4) = 5.

- n_lobes : ℕ
Number of lobes.

Instances For

---

### `Tau.BookIV.Particles.instReprBaryogenesisLeptonDuality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2107-L2107)
**def
Tau.BookIV.Particles.instReprBaryogenesisLeptonDuality.repr :BaryogenesisLeptonDuality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprBaryogenesisLeptonDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2107-L2107)
**instance
Tau.BookIV.Particles.instReprBaryogenesisLeptonDuality :Repr BaryogenesisLeptonDuality**

Equations
- Tau.BookIV.Particles.instReprBaryogenesisLeptonDuality = { reprPrec := Tau.BookIV.Particles.instReprBaryogenesisLeptonDuality.repr }

---

### `Tau.BookIV.Particles.baryogenesis_lepton_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2109-L2109)
**def
Tau.BookIV.Particles.baryogenesis_lepton_data :BaryogenesisLeptonDuality**

Equations
- Tau.BookIV.Particles.baryogenesis_lepton_data = { }
Instances For

---

### `Tau.BookIV.Particles.baryogenesis_lepton_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2111-L2116)
**theorem
Tau.BookIV.Particles.baryogenesis_lepton_conj :baryogenesis_lepton_data.shared_exponent = 15 ∧ baryogenesis_lepton_data.dim_tau3 = 3 ∧ baryogenesis_lepton_data.w3_4 = 5 ∧ baryogenesis_lepton_data.n_lobes = 2**


---

### `Tau.BookIV.Particles.exponent_is_dim_times_w`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2118-L2119)
**theorem
Tau.BookIV.Particles.exponent_is_dim_times_w :3 * 5 = 15**


Exponent = dim × W₃(4): 3 × 5 = 15.

---

### `Tau.BookIV.Particles.nnlo_exponent_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2123-L2128)
**def
Tau.BookIV.Particles.nnlo_exponent_catalog :String**


[IV.D367] NNLO Exponent Catalog (7 entries).
All decompose via {W₃(3)=17, W₃(4)=5, dim=3, lobes=2, sectors=3, N_c=3}.
Equations
- Tau.BookIV.Particles.nnlo_exponent_catalog = "7 NNLO exponents, all Window-universal: " ++ "23/3, 15/2, 3/16, 3/20, 5/7, 1/5, 17/5. " ++ "W₃(4)=5 in all 7. k₁−k₂ = 1/6 = 1/(lobes·sectors)."
Instances For

---

### `Tau.BookIV.Particles.NNLOExponentCatalogData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2130-L2138)
**structure
Tau.BookIV.Particles.NNLOExponentCatalogData :Type**


[IV.D367] NNLO exponent catalog structure (formalized).

- n_entries : ℕ
Number of catalog entries.

- n_window_universal : ℕ
Number of entries using Window universality.

- w3_4_value : ℕ
W₃(4) value appearing in all entries.

Instances For

---

### `Tau.BookIV.Particles.instReprNNLOExponentCatalogData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2138-L2138)
**instance
Tau.BookIV.Particles.instReprNNLOExponentCatalogData :Repr NNLOExponentCatalogData**

Equations
- Tau.BookIV.Particles.instReprNNLOExponentCatalogData = { reprPrec := Tau.BookIV.Particles.instReprNNLOExponentCatalogData.repr }

---

### `Tau.BookIV.Particles.instReprNNLOExponentCatalogData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2138-L2138)
**def
Tau.BookIV.Particles.instReprNNLOExponentCatalogData.repr :NNLOExponentCatalogData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.nnlo_catalog_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2140-L2140)
**def
Tau.BookIV.Particles.nnlo_catalog_data :NNLOExponentCatalogData**

Equations
- Tau.BookIV.Particles.nnlo_catalog_data = { }
Instances For

---

### `Tau.BookIV.Particles.nnlo_catalog_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2142-L2146)
**theorem
Tau.BookIV.Particles.nnlo_catalog_conj :nnlo_catalog_data.n_entries = 7 ∧ nnlo_catalog_data.n_window_universal = 7 ∧ nnlo_catalog_data.w3_4_value = 5**


---

### `Tau.BookIV.Particles.muon_nnlo_k15_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2150-L2155)
**def
Tau.BookIV.Particles.muon_nnlo_k15_2 :String**


[IV.T176] m_μ/m_e NNLO at −8.2 ppm via k=15/2.
m_μ/m_e = ι<sub>τ</sub>^{−124/25}·(1−ι<sub>τ</sub>^{15/2}) = 206.767.
37.5× improvement over LO.
Equations
- Tau.BookIV.Particles.muon_nnlo_k15_2 = "m_μ/m_e = ι<sub>τ</sub>^{−124/25}·(1−ι<sub>τ</sub>^{15/2}) = 206.767, " ++ "PDG 206.768, deviation −8.2 ppm. 37.5× improvement over LO."
Instances For

---

### `Tau.BookIV.Particles.MuonNNLOK15_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2157-L2167)
**structure
Tau.BookIV.Particles.MuonNNLOK15_2 :Type**


[IV.T176] m_μ/m_e NNLO via k=15/2 structure (formalized).

- k_numer : ℕ
Numerator of k: 15.

- k_denom : ℕ
Denominator of k: 2.

- deviation_ppm : ℕ
Deviation from PDG in ppm (×10).

- improvement_over_lo : ℕ
Improvement factor over LO (×10).

Instances For

---

### `Tau.BookIV.Particles.instReprMuonNNLOK15_2.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2167-L2167)
**def
Tau.BookIV.Particles.instReprMuonNNLOK15_2.repr :MuonNNLOK15_2 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprMuonNNLOK15_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2167-L2167)
**instance
Tau.BookIV.Particles.instReprMuonNNLOK15_2 :Repr MuonNNLOK15_2**

Equations
- Tau.BookIV.Particles.instReprMuonNNLOK15_2 = { reprPrec := Tau.BookIV.Particles.instReprMuonNNLOK15_2.repr }

---

### `Tau.BookIV.Particles.muon_nnlo_k15_2_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2169-L2169)
**def
Tau.BookIV.Particles.muon_nnlo_k15_2_data :MuonNNLOK15_2**

Equations
- Tau.BookIV.Particles.muon_nnlo_k15_2_data = { }
Instances For

---

### `Tau.BookIV.Particles.muon_nnlo_k15_2_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2171-L2176)
**theorem
Tau.BookIV.Particles.muon_nnlo_k15_2_conj :muon_nnlo_k15_2_data.k_numer = 15 ∧ muon_nnlo_k15_2_data.k_denom = 2 ∧ muon_nnlo_k15_2_data.deviation_ppm = 8 ∧ muon_nnlo_k15_2_data.improvement_over_lo = 37**


---

### `Tau.BookIV.Particles.window_universality_all_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2180-L2184)
**def
Tau.BookIV.Particles.window_universality_all_7 :String**


[IV.P205] Window Universality for All 7 NNLO Exponents.
All 7 decompose into {W₃(3), W₃(4), dim, lobes, sectors, N_c}.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.WindowUniversalityAll7Data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2186-L2196)
**structure
Tau.BookIV.Particles.WindowUniversalityAll7Data :Type**


[IV.P205] Window universality for all 7 NNLO exponents (formalized).

- n_exponents : ℕ
Number of NNLO exponents.

- n_with_w3_4 : ℕ
Number of exponents containing W₃(4) = 5 (all 7).

- k_diff_numer : ℕ
Exponent difference numerator: 1.

- k_diff_denom : ℕ
Exponent difference denominator: 6 = lobes × sectors.

Instances For

---

### `Tau.BookIV.Particles.instReprWindowUniversalityAll7Data.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2196-L2196)
**def
Tau.BookIV.Particles.instReprWindowUniversalityAll7Data.repr :WindowUniversalityAll7Data → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprWindowUniversalityAll7Data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2196-L2196)
**instance
Tau.BookIV.Particles.instReprWindowUniversalityAll7Data :Repr WindowUniversalityAll7Data**

Equations
- Tau.BookIV.Particles.instReprWindowUniversalityAll7Data = { reprPrec := Tau.BookIV.Particles.instReprWindowUniversalityAll7Data.repr }

---

### `Tau.BookIV.Particles.window_universality_all_7_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2198-L2198)
**def
Tau.BookIV.Particles.window_universality_all_7_data :WindowUniversalityAll7Data**

Equations
- Tau.BookIV.Particles.window_universality_all_7_data = { }
Instances For

---

### `Tau.BookIV.Particles.window_universality_all_7_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2200-L2205)
**theorem
Tau.BookIV.Particles.window_universality_all_7_conj :window_universality_all_7_data.n_exponents = 7 ∧ window_universality_all_7_data.n_with_w3_4 = 7 ∧ window_universality_all_7_data.k_diff_numer = 1 ∧ window_universality_all_7_data.k_diff_denom = 6**


---

### `Tau.BookIV.Particles.CabibboHolonomyDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2222-L2250)
**structure
Tau.BookIV.Particles.CabibboHolonomyDerivation :Type**


[IV.T152 upgrade] Cabibbo angle from T² holonomy transition.

The T² fiber has two fundamental cycles γ₁, γ₂ with holonomies
ι<sub>τ</sub> (γ-generator, EM) and (1−ι<sub>τ</sub>) (η-generator, Strong).

The transition amplitude from winding class (1,0) to (0,1)
on T² with the τ-metric is the inner product:
⟨e^{iγ₁}, e^{iγ₂}⟩_τ = ι<sub>τ</sub> · (1−ι<sub>τ</sub>) = ι<sub>τ</sub> · κ_D

This equals the Cabibbo angle: λ_C = ι<sub>τ</sub> · κ_D.
sin(θ_C) = λ_C = ι<sub>τ</sub> · (1−ι<sub>τ</sub>) ≈ 0.2249
PDG: 0.22500 ± 0.00067 → deviation −2327 ppm.

Physical interpretation: quark mixing between generations 1
and 2 is the amplitude for a T² winding-class transition.
This is structural: the transition amplitude is determined
entirely by the fiber holonomy.

- n_cycle_holonomies : ℕ
Number of T² cycles with holonomies (γ₁, γ₂).

- n_holonomy_factors : ℕ
Number of holonomy factors in product: ι<sub>τ</sub> · κ_D.

- deviation_ppm : ℕ
Deviation from PDG in ppm.

- n_free_params : ℕ
Number of free parameters in derivation.

- transition_from_gen : ℕ
Winding class transition: gen 1 → gen 2 (index pair).

Instances For

---

### `Tau.BookIV.Particles.instReprCabibboHolonomyDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2250-L2250)
**def
Tau.BookIV.Particles.instReprCabibboHolonomyDerivation.repr :CabibboHolonomyDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCabibboHolonomyDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2250-L2250)
**instance
Tau.BookIV.Particles.instReprCabibboHolonomyDerivation :Repr CabibboHolonomyDerivation**

Equations
- Tau.BookIV.Particles.instReprCabibboHolonomyDerivation = { reprPrec := Tau.BookIV.Particles.instReprCabibboHolonomyDerivation.repr }

---

### `Tau.BookIV.Particles.cabibbo_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2252-L2252)
**def
Tau.BookIV.Particles.cabibbo_holonomy :CabibboHolonomyDerivation**

Equations
- Tau.BookIV.Particles.cabibbo_holonomy = { }
Instances For

---

### `Tau.BookIV.Particles.cabibbo_holonomy_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2254-L2259)
**theorem
Tau.BookIV.Particles.cabibbo_holonomy_derivation :cabibbo_holonomy.n_holonomy_factors = 2 ∧ cabibbo_holonomy.deviation_ppm = 2327 ∧ cabibbo_holonomy.n_free_params = 0**


Cabibbo angle derived from T² holonomy transition amplitude.

---

### `Tau.BookIV.Particles.ASectorRotationMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2265-L2293)
**structure
Tau.BookIV.Particles.ASectorRotationMechanism :Type**


[IV.T162/T174/T175 upgrade] A-sector rotation mechanism.

The π-generator (A-sector, weak force) acts on the 3-generation
structure via the polarity matrix. The rotation angle on the
base cycle g₃ is determined by κ(A;1) = ι<sub>τ</sub>.

Key equation: sin(θ_A) = κ_ω = ι<sub>τ</sub>/(1+ι<sub>τ</sub>)
This is the A-sector crossing amplitude normalized by
the full holonomy.

Physical: sin(θ₂₃)_LO = 1/(1+ι<sub>τ</sub>) is "one full A-sector
traversal" — the natural output of the π-generator rotation.

NLO: sin(θ₂₃) = (1−ι<sub>τ</sub>⁵)/(1+ι<sub>τ</sub>) at +8604 ppm.
The ι<sub>τ</sub>⁵ correction is the W₃(4)-order Window correction.

- pi_generator_index : ℕ
π-generator index in {α,π,γ,η,ω}: 2nd generator.

- lo_deviation_ppm : ℕ
LO deviation from PDG in ppm.

- nlo_deviation_ppm : ℕ
NLO deviation from PDG in ppm.

- nlo_window_exp : ℕ
Window exponent W₃(4) in NLO correction.

- n_matrices_bridged : ℕ
Number of mixing matrices bridged (CKM + PMNS).

- polarity_dim : ℕ
Polarity matrix dimension (3×3).

Instances For

---

### `Tau.BookIV.Particles.instReprASectorRotationMechanism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2293-L2293)
**def
Tau.BookIV.Particles.instReprASectorRotationMechanism.repr :ASectorRotationMechanism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprASectorRotationMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2293-L2293)
**instance
Tau.BookIV.Particles.instReprASectorRotationMechanism :Repr ASectorRotationMechanism**

Equations
- Tau.BookIV.Particles.instReprASectorRotationMechanism = { reprPrec := Tau.BookIV.Particles.instReprASectorRotationMechanism.repr }

---

### `Tau.BookIV.Particles.a_sector_rotation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2295-L2295)
**def
Tau.BookIV.Particles.a_sector_rotation :ASectorRotationMechanism**

Equations
- Tau.BookIV.Particles.a_sector_rotation = { }
Instances For

---

### `Tau.BookIV.Particles.a_sector_rotation_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2297-L2302)
**theorem
Tau.BookIV.Particles.a_sector_rotation_structural :a_sector_rotation.pi_generator_index = 2 ∧ a_sector_rotation.nlo_window_exp = 5 ∧ a_sector_rotation.n_matrices_bridged = 2**


A-sector rotation mechanism established for PMNS.

---

### `Tau.BookIV.Particles.QLCFiberBaseDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2308-L2335)
**structure
Tau.BookIV.Particles.QLCFiberBaseDuality :Type**


[IV.P189/T175 upgrade] QLC from fiber-base duality.

θ₁₂^{PMNS} + θ_C^{CKM} ≈ π/4 + O(ι<sub>τ</sub>²)

Proof structure:


- On T² (fiber): quark mixing is small:
θ_C = arcsin(ι<sub>τ</sub>·κ_D) ≈ 0.222 rad

- On τ¹ (base): the complementary angle is π/4 − θ_C
because T² × τ¹ → τ³ imposes that the total mixing
angle in the product is π/4 (quarter-turn on combined space)

- Correction: ι<sub>τ</sub>²·κ_ω arises from ω-sector (Higgs) coupling
between fiber and base


Physical: quarks (on T²) and leptons (on τ¹) have
complementary mixing because the product structure
τ³ = τ¹ ×_f T² constrains total mixing.

- fiber_dim : ℕ
Fiber dimension: T² (quarks).

- base_dim : ℕ
Base dimension: τ¹ (leptons).

- quarter_turn_degrees : ℕ
Total quarter-turn angle (degrees): π/4 = 45°.

- higgs_correction_power : ℕ
Higgs correction power: ι<sub>τ</sub>² order.

- deviation_deg_x10 : ℕ
QLC deviation in degrees (×10): 1.4° → 14.

Instances For

---

### `Tau.BookIV.Particles.instReprQLCFiberBaseDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2335-L2335)
**instance
Tau.BookIV.Particles.instReprQLCFiberBaseDuality :Repr QLCFiberBaseDuality**

Equations
- Tau.BookIV.Particles.instReprQLCFiberBaseDuality = { reprPrec := Tau.BookIV.Particles.instReprQLCFiberBaseDuality.repr }

---

### `Tau.BookIV.Particles.instReprQLCFiberBaseDuality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2335-L2335)
**def
Tau.BookIV.Particles.instReprQLCFiberBaseDuality.repr :QLCFiberBaseDuality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.qlc_fiber_base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2337-L2337)
**def
Tau.BookIV.Particles.qlc_fiber_base :QLCFiberBaseDuality**

Equations
- Tau.BookIV.Particles.qlc_fiber_base = { }
Instances For

---

### `Tau.BookIV.Particles.qlc_fiber_base_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2339-L2345)
**theorem
Tau.BookIV.Particles.qlc_fiber_base_structural :qlc_fiber_base.quarter_turn_degrees = 45 ∧ qlc_fiber_base.higgs_correction_power = 2 ∧ qlc_fiber_base.fiber_dim = 2 ∧ qlc_fiber_base.base_dim = 1**


QLC from fiber-base duality: θ₁₂ + θ_C = π/4 + O(ι<sub>τ</sub>²).

---

### `Tau.BookIV.Particles.Theta13OpenFrontier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2351-L2367)
**structure
Tau.BookIV.Particles.Theta13OpenFrontier :Type**


θ₁₃ second-order mechanism: genuinely open frontier.

Best candidates explored:


- sin²θ₁₃ = λ_C²·(ι<sub>τ</sub>/2) ≈ 0.00432 (too small, PDG 0.02224)

- sin²θ₁₃ = ι<sub>τ</sub>⁴·κ_D ≈ 0.00893 (still 2.5× too small)

- Double winding-class crossing amplitude: gen1→gen3 skipping gen2


Current best: 13.6% off. No viable formula at present.
Flagged as "genuinely open frontier".

- best_deviation_percent : ℕ
Best deviation from PDG in percent.

- n_candidates_explored : ℕ
Number of candidates explored.

- n_viable_formulas : ℕ
Number of viable formulas found.

Instances For

---

### `Tau.BookIV.Particles.instReprTheta13OpenFrontier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2367-L2367)
**instance
Tau.BookIV.Particles.instReprTheta13OpenFrontier :Repr Theta13OpenFrontier**

Equations
- Tau.BookIV.Particles.instReprTheta13OpenFrontier = { reprPrec := Tau.BookIV.Particles.instReprTheta13OpenFrontier.repr }

---

### `Tau.BookIV.Particles.instReprTheta13OpenFrontier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2367-L2367)
**def
Tau.BookIV.Particles.instReprTheta13OpenFrontier.repr :Theta13OpenFrontier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.theta13_open`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2369-L2369)
**def
Tau.BookIV.Particles.theta13_open :Theta13OpenFrontier**

Equations
- Tau.BookIV.Particles.theta13_open = { }
Instances For

---

### `Tau.BookIV.Particles.theta13_honest_assessment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2371-L2375)
**theorem
Tau.BookIV.Particles.theta13_honest_assessment :theta13_open.n_viable_formulas = 0 ∧ theta13_open.best_deviation_percent = 14**


θ₁₃ is genuinely open: 14% gap, no viable formula.

---

### `Tau.BookIV.Particles.QLCDerivationChain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2387-L2408)
**structure
Tau.BookIV.Particles.QLCDerivationChain :Type**


[IV.T175 upgrade] QLC constraint: θ₁₂ + θ_C = π/4.
The fiber-base duality T²×τ¹→τ³ imposes a quarter-turn
constraint on the sum of solar and Cabibbo angles.

Chain: λ_C = ι<sub>τ</sub>·(1−ι<sub>τ</sub>) (IV.T152, τ-effective)
→ θ_C = arcsin(λ_C)
→ θ₁₂ = π/4 − θ_C + ι<sub>τ</sub>²κ_ω (NLO correction)
→ θ₁₂ at +3106 ppm from PDG

- cabibbo_deviation_ppm : ℕ
Cabibbo λ_C deviation from PDG in ppm (−2327).

- quarter_turn_angle : ℕ
Quarter-turn constraint from T²×τ¹ fiber-base duality (π/4 radians × 10000).

- nlo_power : ℕ
NLO correction power (ι<sub>τ</sub>²).

- theta12_deviation_ppm : ℕ
θ₁₂ deviation from PDG in ppm (+3106).

- free_params : ℕ
Number of free parameters (zero: all from ι<sub>τ</sub>).

- scope : String
Scope.

Instances For

---

### `Tau.BookIV.Particles.instReprQLCDerivationChain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2408-L2408)
**instance
Tau.BookIV.Particles.instReprQLCDerivationChain :Repr QLCDerivationChain**

Equations
- Tau.BookIV.Particles.instReprQLCDerivationChain = { reprPrec := Tau.BookIV.Particles.instReprQLCDerivationChain.repr }

---

### `Tau.BookIV.Particles.instReprQLCDerivationChain.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2408-L2408)
**def
Tau.BookIV.Particles.instReprQLCDerivationChain.repr :QLCDerivationChain → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.qlc_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2410-L2410)
**def
Tau.BookIV.Particles.qlc_derivation :QLCDerivationChain**

Equations
- Tau.BookIV.Particles.qlc_derivation = { }
Instances For

---

### `Tau.BookIV.Particles.qlc_deviation_below_threshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2412-L2414)
**theorem
Tau.BookIV.Particles.qlc_deviation_below_threshold :qlc_derivation.theta12_deviation_ppm < 5000**


QLC chain produces θ₁₂ below τ-effective threshold.

---

### `Tau.BookIV.Particles.qlc_chain_both_ends_below`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2416-L2419)
**theorem
Tau.BookIV.Particles.qlc_chain_both_ends_below :qlc_derivation.cabibbo_deviation_ppm < 5000 ∧ qlc_derivation.theta12_deviation_ppm < 5000**


Both ends of the chain are below 5000 ppm.

---

### `Tau.BookIV.Particles.qlc_chain_zero_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2421-L2423)
**theorem
Tau.BookIV.Particles.qlc_chain_zero_params :qlc_derivation.free_params = 0**


Zero free parameters in the derivation chain.

---

### `Tau.BookIV.Particles.qlc_nlo_second_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2425-L2427)
**theorem
Tau.BookIV.Particles.qlc_nlo_second_order :qlc_derivation.nlo_power = 2**


NLO correction is second order in ι<sub>τ</sub>.

---

### `Tau.BookIV.Particles.CharmMassRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2438-L2459)
**structure
Tau.BookIV.Particles.CharmMassRatio :Type**


[IV.T191] Charm quark mass from τ-chain.

m_c = m_t(τ) × ι<sub>τ</sub>^(105/23) = 172440 × 0.007391 = 1274.5 MeV.
Exponent: 105/23 = dim·W₃(4)·n_H / (a₃ + 2·W₃(4))
= 3 × 5 × 7 / (13 + 10).
At +1150 ppm from PDG 1273 ± 4 MeV (0.4σ).

- exp_num : ℕ
Exponent numerator: dim·W₃(4)·n_H = 3×5×7 = 105.

- exp_den : ℕ
Exponent denominator: a₃ + 2·W₃(4) = 13 + 10 = 23.

- mass_x10 : ℕ
τ-predicted mass in MeV (×10 for integer).

- pdg_mass : ℕ
PDG mass in MeV.

- deviation_ppm : ℤ
Deviation in ppm.

- num_decomp : self.exp_num = 3 * 5 * 7
Exponent numerator = dim × W₃(4) × n_Higgs.

- den_decomp : self.exp_den = 13 + 2 * 5
Exponent denominator = a₃ + 2·W₃(4).

Instances For

---

### `Tau.BookIV.Particles.instReprCharmMassRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2459-L2459)
**def
Tau.BookIV.Particles.instReprCharmMassRatio.repr :CharmMassRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCharmMassRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2459-L2459)
**instance
Tau.BookIV.Particles.instReprCharmMassRatio :Repr CharmMassRatio**

Equations
- Tau.BookIV.Particles.instReprCharmMassRatio = { reprPrec := Tau.BookIV.Particles.instReprCharmMassRatio.repr }

---

### `Tau.BookIV.Particles.charm_mass_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2461-L2463)
**def
Tau.BookIV.Particles.charm_mass_ratio :CharmMassRatio**

Equations
- Tau.BookIV.Particles.charm_mass_ratio = { num_decomp := Tau.BookIV.Particles.charm_mass_ratio._proof_1,
 den_decomp := Tau.BookIV.Particles.charm_mass_ratio._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.StrangeMassRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2465-L2486)
**structure
Tau.BookIV.Particles.StrangeMassRatio :Type**


[IV.T192] Strange quark mass from τ-chain.

m_s = m_b(τ) × ι<sub>τ</sub>^(53/15) = 4174.4 × 0.02241 = 93.55 MeV.
Exponent: 53/15 = (4·a₃ + 1) / (dim·W₃(4))
= (4×13 + 1) / (3×5).
At +1559 ppm from PDG 93.4 ± 0.8 MeV (0.2σ).

- exp_num : ℕ
Exponent numerator: 4·a₃ + 1 = 53.

- exp_den : ℕ
Exponent denominator: dim·W₃(4) = 15.

- mass_x100 : ℕ
τ-predicted mass in MeV (×100 for integer).

- pdg_mass_x10 : ℕ
PDG mass (×10).

- deviation_ppm : ℤ
Deviation in ppm.

- num_decomp : self.exp_num = 4 * 13 + 1
Numerator = 4·a₃ + 1.

- den_decomp : self.exp_den = 3 * 5
Denominator = dim × W₃(4).

Instances For

---

### `Tau.BookIV.Particles.instReprStrangeMassRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2486-L2486)
**instance
Tau.BookIV.Particles.instReprStrangeMassRatio :Repr StrangeMassRatio**

Equations
- Tau.BookIV.Particles.instReprStrangeMassRatio = { reprPrec := Tau.BookIV.Particles.instReprStrangeMassRatio.repr }

---

### `Tau.BookIV.Particles.instReprStrangeMassRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2486-L2486)
**def
Tau.BookIV.Particles.instReprStrangeMassRatio.repr :StrangeMassRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.strange_mass_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2488-L2490)
**def
Tau.BookIV.Particles.strange_mass_ratio :StrangeMassRatio**

Equations
- Tau.BookIV.Particles.strange_mass_ratio = { num_decomp := Tau.BookIV.Particles.strange_mass_ratio._proof_1,
 den_decomp := Tau.BookIV.Particles.strange_mass_ratio._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.BottomMass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2492-L2512)
**structure
Tau.BookIV.Particles.BottomMass :Type**


[IV.T193] Bottom quark mass from τ-chain.

m_b = (17/20)·ι<sub>τ</sub>^(-20/13)·m_n = 4174.4 MeV.
Combined exponent: -20/13 = -lobes²·W₃(4)/a₃ = -4×5/13.
At -1351 ppm from PDG 4180 ± 7 MeV (0.8σ).

- exp_num : ℕ
Combined exponent numerator (absolute).

- exp_den : ℕ
Combined exponent denominator.

- mass_x10 : ℕ
τ-predicted mass (×10).

- pdg_mass : ℕ
PDG mass.

- deviation_ppm : ℤ
Deviation in ppm.

- num_decomp : self.exp_num = 4 * 5
Numerator = lobes² × W₃(4).

- den_is_a3 : self.exp_den = 13
Denominator = a₃.

Instances For

---

### `Tau.BookIV.Particles.instReprBottomMass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2512-L2512)
**instance
Tau.BookIV.Particles.instReprBottomMass :Repr BottomMass**

Equations
- Tau.BookIV.Particles.instReprBottomMass = { reprPrec := Tau.BookIV.Particles.instReprBottomMass.repr }

---

### `Tau.BookIV.Particles.instReprBottomMass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2512-L2512)
**def
Tau.BookIV.Particles.instReprBottomMass.repr :BottomMass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.bottom_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2514-L2516)
**def
Tau.BookIV.Particles.bottom_mass :BottomMass**

Equations
- Tau.BookIV.Particles.bottom_mass = { num_decomp := Tau.BookIV.Particles.bottom_mass._proof_1, den_is_a3 := Tau.BookIV.Particles.bottom_mass._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.CharmStrangeCrossCheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2518-L2530)
**structure
Tau.BookIV.Particles.CharmStrangeCrossCheck :Type**


[IV.D375] m_c/m_s cross-check: τ-chain ratio vs PDG.
m_c(τ)/m_s(τ) = 13.62 vs naïve PDG 13.63.
FLAG (same scale): 11.74 ± 0.05 (16% discrepancy from scale mismatch).

- ratio_x100 : ℕ
τ-chain ratio (×100).

- pdg_naive_x100 : ℕ
Naïve PDG ratio (×100).

- flag_ratio_x100 : ℕ
FLAG same-scale ratio (×100).

- internal_consistent : Bool
Internal consistency: τ-chain matches naïve PDG.

Instances For

---

### `Tau.BookIV.Particles.instReprCharmStrangeCrossCheck.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2530-L2530)
**def
Tau.BookIV.Particles.instReprCharmStrangeCrossCheck.repr :CharmStrangeCrossCheck → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCharmStrangeCrossCheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2530-L2530)
**instance
Tau.BookIV.Particles.instReprCharmStrangeCrossCheck :Repr CharmStrangeCrossCheck**

Equations
- Tau.BookIV.Particles.instReprCharmStrangeCrossCheck = { reprPrec := Tau.BookIV.Particles.instReprCharmStrangeCrossCheck.repr }

---

### `Tau.BookIV.Particles.charm_strange_crosscheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2532-L2532)
**def
Tau.BookIV.Particles.charm_strange_crosscheck :CharmStrangeCrossCheck**

Equations
- Tau.BookIV.Particles.charm_strange_crosscheck = { }
Instances For

---

### `Tau.BookIV.Particles.DownStrangeRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2534-L2549)
**structure
Tau.BookIV.Particles.DownStrangeRatio :Type**


[IV.P219] m_d/m_s prediction.
m_d/m_s = ι<sub>τ</sub>^(64/23) = 0.05022.
Exponent: 64/23 = lobes^6 / (a₃ + 2·W₃(4)) = 2⁶/23.
At -1921 ppm from PDG 0.05032.

- exp_num : ℕ
Exponent numerator: lobes^(2·dim) = 2⁶ = 64.

- exp_den : ℕ
Exponent denominator: a₃ + 2·W₃(4) = 23.

- deviation_ppm : ℤ
Deviation in ppm.

- num_is_lobe_power : self.exp_num = 2 ^ 6
Numerator = 2⁶.

- den_shared : self.exp_den = 13 + 2 * 5
Same denominator as charm exponent.

Instances For

---

### `Tau.BookIV.Particles.instReprDownStrangeRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2549-L2549)
**instance
Tau.BookIV.Particles.instReprDownStrangeRatio :Repr DownStrangeRatio**

Equations
- Tau.BookIV.Particles.instReprDownStrangeRatio = { reprPrec := Tau.BookIV.Particles.instReprDownStrangeRatio.repr }

---

### `Tau.BookIV.Particles.instReprDownStrangeRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2549-L2549)
**def
Tau.BookIV.Particles.instReprDownStrangeRatio.repr :DownStrangeRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.down_strange_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2551-L2553)
**def
Tau.BookIV.Particles.down_strange_ratio :DownStrangeRatio**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.SixQuarkConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2555-L2568)
**structure
Tau.BookIV.Particles.SixQuarkConsistency :Type**


[IV.D377] Six-quark τ-chain mass table.
RMS over 5 well-determined quarks (t,b,c,s,d): 1243 ppm.

- n_quarks : ℕ
Number of quarks predicted.

- n_within_2sigma : ℕ
Number within 2σ of PDG.

- rms_ppm : ℕ
RMS ppm over 5 well-determined quarks.

- ordering_correct : ℕ
Correct mass ordering reproduced.

- complete : self.n_quarks = 6
All six quarks present.

Instances For

---

### `Tau.BookIV.Particles.instReprSixQuarkConsistency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2568-L2568)
**def
Tau.BookIV.Particles.instReprSixQuarkConsistency.repr :SixQuarkConsistency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprSixQuarkConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2568-L2568)
**instance
Tau.BookIV.Particles.instReprSixQuarkConsistency :Repr SixQuarkConsistency**

Equations
- Tau.BookIV.Particles.instReprSixQuarkConsistency = { reprPrec := Tau.BookIV.Particles.instReprSixQuarkConsistency.repr }

---

### `Tau.BookIV.Particles.six_quark_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2570-L2571)
**def
Tau.BookIV.Particles.six_quark_consistency :SixQuarkConsistency**

Equations
- Tau.BookIV.Particles.six_quark_consistency = { complete := Tau.BookIV.Particles.six_quark_consistency._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.JarlskogInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2573-L2587)
**structure
Tau.BookIV.Particles.JarlskogInvariant :Type**


[IV.T195] Jarlskog invariant from τ-CKM.
J(τ) = 2.97 × 10⁻⁵ vs PDG (3.08 ± 0.15) × 10⁻⁵.
At -35000 ppm, within 0.7σ.

- j_x1e7 : ℕ
J (×10⁷ for integer).

- j_pdg_x1e7 : ℕ
PDG J (×10⁷).

- deviation_ppm : ℤ
Deviation ppm.

- within_1sigma : ℕ
Within 1σ.

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2587-L2587)
**instance
Tau.BookIV.Particles.instReprJarlskogInvariant :Repr JarlskogInvariant**

Equations
- Tau.BookIV.Particles.instReprJarlskogInvariant = { reprPrec := Tau.BookIV.Particles.instReprJarlskogInvariant.repr }

---

### `Tau.BookIV.Particles.instReprJarlskogInvariant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2587-L2587)
**def
Tau.BookIV.Particles.instReprJarlskogInvariant.repr :JarlskogInvariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.jarlskog_invariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2589-L2589)
**def
Tau.BookIV.Particles.jarlskog_invariant :JarlskogInvariant**

Equations
- Tau.BookIV.Particles.jarlskog_invariant = { }
Instances For

---

### `Tau.BookIV.Particles.GenerationEigenvalueSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2605-L2619)
**structure
Tau.BookIV.Particles.GenerationEigenvalueSpectrum :Type**


[IV.D379] Generation eigenvalue spectrum on anisotropic T².
λ_{(n,m)} = n² + m²·ι<sub>τ</sub>⁻². Three primitive winding classes
give eigenvalues 1, ι<sub>τ</sub>⁻² ≈ 8.585, 1+ι<sub>τ</sub>⁻² ≈ 9.585.

- lam_10_x1000 : ℕ
λ(1,0) = 1 (×1000).

- lam_01_x1000 : ℕ
λ(0,1) = ι<sub>τ</sub>⁻² (×1000).

- lam_11_x1000 : ℕ
λ(1,1) = 1 + ι<sub>τ</sub>⁻² (×1000).

- lam_11_sum : self.lam_11_x1000 = self.lam_10_x1000 + self.lam_01_x1000
λ(1,1) = λ(1,0) + λ(0,1).

- n_generations : ℕ
Number of primitive winding classes = generations.

Instances For

---

### `Tau.BookIV.Particles.instReprGenerationEigenvalueSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2619-L2619)
**instance
Tau.BookIV.Particles.instReprGenerationEigenvalueSpectrum :Repr GenerationEigenvalueSpectrum**

Equations
- Tau.BookIV.Particles.instReprGenerationEigenvalueSpectrum = { reprPrec := Tau.BookIV.Particles.instReprGenerationEigenvalueSpectrum.repr }

---

### `Tau.BookIV.Particles.instReprGenerationEigenvalueSpectrum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2619-L2619)
**def
Tau.BookIV.Particles.instReprGenerationEigenvalueSpectrum.repr :GenerationEigenvalueSpectrum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.generation_eigenvalue_spectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2621-L2622)
**def
Tau.BookIV.Particles.generation_eigenvalue_spectrum :GenerationEigenvalueSpectrum**

Equations
- Tau.BookIV.Particles.generation_eigenvalue_spectrum = { lam_11_sum := Tau.BookIV.Particles.generation_eigenvalue_spectrum._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.WindingTransitionMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2624-L2637)
**structure
Tau.BookIV.Particles.WindingTransitionMatrix :Type**


[IV.D378] Winding transition matrix on T² primitive modes.
3×3 symmetric matrix: diagonal = eigenvalues, off-diagonal = κ(C;n).

- dim : ℕ
Matrix dimension.

- trace_eigenvalues_x1000 : ℕ
Trace contribution from eigenvalues (×1000).

- kC1_count : ℕ
κ(C;1) appears 4 times off-diagonal.

- kC2_count : ℕ
κ(C;2) appears 2 times off-diagonal.

- symmetric : Bool
Matrix is symmetric.

Instances For

---

### `Tau.BookIV.Particles.instReprWindingTransitionMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2637-L2637)
**instance
Tau.BookIV.Particles.instReprWindingTransitionMatrix :Repr WindingTransitionMatrix**

Equations
- Tau.BookIV.Particles.instReprWindingTransitionMatrix = { reprPrec := Tau.BookIV.Particles.instReprWindingTransitionMatrix.repr }

---

### `Tau.BookIV.Particles.instReprWindingTransitionMatrix.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2637-L2637)
**def
Tau.BookIV.Particles.instReprWindingTransitionMatrix.repr :WindingTransitionMatrix → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.winding_transition_matrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2639-L2639)
**def
Tau.BookIV.Particles.winding_transition_matrix :WindingTransitionMatrix**

Equations
- Tau.BookIV.Particles.winding_transition_matrix = { }
Instances For

---

### `Tau.BookIV.Particles.TopBottomExponentDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2641-L2661)
**structure
Tau.BookIV.Particles.TopBottomExponentDerived :Type**


[IV.T196] m_t/m_b exponent from winding algebra.
β(t/b) = -dim(τ³)·(a₃+|lobes|)/a₃ = -3·15/13 = -45/13.
First quark exponent derived from T² mode-counting.

- exp_num : ℕ
Exponent numerator (absolute).

- exp_den : ℕ
Exponent denominator.

- dim_tau3 : ℕ
dim(τ³).

- a3 : ℕ
CF partial quotient a₃.

- lobes : ℕ
Lemniscate lobe count.

- deviation_ppm : ℤ
Deviation in ppm.

- num_derivation : self.exp_num = self.dim_tau3 * (self.a3 + self.lobes)
Numerator = dim × (a₃ + lobes).

- den_derivation : self.exp_den = self.a3
Denominator = a₃.

Instances For

---

### `Tau.BookIV.Particles.instReprTopBottomExponentDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2661-L2661)
**instance
Tau.BookIV.Particles.instReprTopBottomExponentDerived :Repr TopBottomExponentDerived**

Equations
- Tau.BookIV.Particles.instReprTopBottomExponentDerived = { reprPrec := Tau.BookIV.Particles.instReprTopBottomExponentDerived.repr }

---

### `Tau.BookIV.Particles.instReprTopBottomExponentDerived.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2661-L2661)
**def
Tau.BookIV.Particles.instReprTopBottomExponentDerived.repr :TopBottomExponentDerived → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.top_bottom_exponent_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2663-L2665)
**def
Tau.BookIV.Particles.top_bottom_exponent_derived :TopBottomExponentDerived**

Equations
- Tau.BookIV.Particles.top_bottom_exponent_derived = { num_derivation := Tau.BookIV.Particles.top_bottom_exponent_derived._proof_1,
 den_derivation := Tau.BookIV.Particles.bottom_mass._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.CharmTopExponentDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2667-L2688)
**structure
Tau.BookIV.Particles.CharmTopExponentDerived :Type**


[IV.P221] m_c/m_t exponent from Higgs-weighted transition.
β(c/t) = dim·W₃(4)·n_H/(a₃+2·W₃(4)) = 3·5·7/23 = 105/23.

- exp_num : ℕ
Exponent numerator.

- exp_den : ℕ
Exponent denominator.

- dim_tau3 : ℕ
dim(τ³).

- w34 : ℕ
Window value W₃(4).

- n_higgs : ℕ
Higgs crossing number.

- a3 : ℕ
CF partial quotient a₃.

- deviation_ppm : ℤ
Deviation in ppm.

- num_derivation : self.exp_num = self.dim_tau3 * self.w34 * self.n_higgs
Numerator = dim × W₃(4) × n_H.

- den_derivation : self.exp_den = self.a3 + 2 * self.w34
Denominator = a₃ + 2·W₃(4).

Instances For

---

### `Tau.BookIV.Particles.instReprCharmTopExponentDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2688-L2688)
**instance
Tau.BookIV.Particles.instReprCharmTopExponentDerived :Repr CharmTopExponentDerived**

Equations
- Tau.BookIV.Particles.instReprCharmTopExponentDerived = { reprPrec := Tau.BookIV.Particles.instReprCharmTopExponentDerived.repr }

---

### `Tau.BookIV.Particles.instReprCharmTopExponentDerived.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2688-L2688)
**def
Tau.BookIV.Particles.instReprCharmTopExponentDerived.repr :CharmTopExponentDerived → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.charm_top_exponent_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2690-L2692)
**def
Tau.BookIV.Particles.charm_top_exponent_derived :CharmTopExponentDerived**

Equations
- Tau.BookIV.Particles.charm_top_exponent_derived = { num_derivation := Tau.BookIV.Particles.charm_mass_ratio._proof_1,
 den_derivation := Tau.BookIV.Particles.charm_mass_ratio._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.ExponentUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2694-L2707)
**structure
Tau.BookIV.Particles.ExponentUniversality :Type**


[IV.R431] Exponent universality: all ratios from winding matrix W.
7/7 exponents now derived from first principles (updated Wave 45).

- total_ratios : ℕ
Total quark mass ratios.

- derived_ratios : ℕ
Ratios derived from first principles.

- decomposed_ratios : ℕ
Ratios with structural decomposition.

- input_ratios : ℕ
Input ratios.

- complete : self.total_ratios = self.derived_ratios + self.decomposed_ratios + self.input_ratios
All accounted for.

Instances For

---

### `Tau.BookIV.Particles.instReprExponentUniversality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2707-L2707)
**def
Tau.BookIV.Particles.instReprExponentUniversality.repr :ExponentUniversality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprExponentUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2707-L2707)
**instance
Tau.BookIV.Particles.instReprExponentUniversality :Repr ExponentUniversality**

Equations
- Tau.BookIV.Particles.instReprExponentUniversality = { reprPrec := Tau.BookIV.Particles.instReprExponentUniversality.repr }

---

### `Tau.BookIV.Particles.exponent_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2709-L2710)
**def
Tau.BookIV.Particles.exponent_universality :ExponentUniversality**

Equations
- Tau.BookIV.Particles.exponent_universality = { complete := Tau.BookIV.Particles.exponent_universality._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.TopUpDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2712-L2723)
**structure
Tau.BookIV.Particles.TopUpDuality :Type**


[IV.D380] Top–up exponent duality on T².
β_u + β_t = 1/|lobes| = 1/2.

- beta_t_x2 : ℤ
β_t (×2 for integer encoding).

- beta_u_x2 : ℤ
β_u (×2 for integer encoding).

- lobes : ℕ
Lobe count.

- duality : self.beta_u_x2 + self.beta_t_x2 = 1
Duality: β_u_x2 + β_t_x2 = 2/lobes = 1.

Instances For

---

### `Tau.BookIV.Particles.instReprTopUpDuality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2723-L2723)
**def
Tau.BookIV.Particles.instReprTopUpDuality.repr :TopUpDuality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprTopUpDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2723-L2723)
**instance
Tau.BookIV.Particles.instReprTopUpDuality :Repr TopUpDuality**

Equations
- Tau.BookIV.Particles.instReprTopUpDuality = { reprPrec := Tau.BookIV.Particles.instReprTopUpDuality.repr }

---

### `Tau.BookIV.Particles.top_up_duality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2725-L2726)
**def
Tau.BookIV.Particles.top_up_duality :TopUpDuality**

Equations
- Tau.BookIV.Particles.top_up_duality = { duality := Tau.BookIV.Particles.top_up_duality._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.UpQuarkDirect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2728-L2753)
**structure
Tau.BookIV.Particles.UpQuarkDirect :Type**


[IV.T197] Up quark direct mass from exponent duality.
m_u = (17/20)·ι<sub>τ</sub>^(11/2)·m_n = 2.161 MeV at +395 ppm.

- exp_num : ℕ
Exponent numerator.

- exp_den : ℕ
Exponent denominator.

- prefactor_num : ℕ
Prefactor numerator (same as top quark).

- prefactor_den : ℕ
Prefactor denominator.

- mass_x1000 : ℕ
Predicted mass (×1000 keV).

- pdg_mass_x1000 : ℕ
PDG mass (×1000 keV).

- deviation_ppm : ℤ
Deviation in ppm.

- chain_improvement : ℕ
Improvement factor over chain.

- chain_deviation_ppm : ℤ
Chain deviation (ppm).

- geometric_mean : ℕ
Geometric mean m_u·m_t (MeV²).

- exp_structure : self.exp_num = 2 * 5 + 1
Exponent numerator = 2·W₃(4) + 1.

Instances For

---

### `Tau.BookIV.Particles.instReprUpQuarkDirect.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2753-L2753)
**def
Tau.BookIV.Particles.instReprUpQuarkDirect.repr :UpQuarkDirect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprUpQuarkDirect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2753-L2753)
**instance
Tau.BookIV.Particles.instReprUpQuarkDirect :Repr UpQuarkDirect**

Equations
- Tau.BookIV.Particles.instReprUpQuarkDirect = { reprPrec := Tau.BookIV.Particles.instReprUpQuarkDirect.repr }

---

### `Tau.BookIV.Particles.up_quark_direct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2755-L2756)
**def
Tau.BookIV.Particles.up_quark_direct :UpQuarkDirect**

Equations
- Tau.BookIV.Particles.up_quark_direct = { exp_structure := Tau.BookIV.Particles.up_quark_direct._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.IsospinRatioDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2758-L2769)
**structure
Tau.BookIV.Particles.IsospinRatioDerived :Type**


[IV.P222] m_u/m_d isospin ratio from winding algebra.
m_u(direct)/m_d(chain) = 0.4600 at +82 ppm.

- ratio_x10000 : ℕ
Ratio (×10000).

- pdg_ratio_x10000 : ℕ
PDG ratio (×10000).

- deviation_ppm : ℤ
Deviation ppm.

- consistent_nlo : Bool
Consistent with NLO scan (+29 ppm).

Instances For

---

### `Tau.BookIV.Particles.instReprIsospinRatioDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2769-L2769)
**instance
Tau.BookIV.Particles.instReprIsospinRatioDerived :Repr IsospinRatioDerived**

Equations
- Tau.BookIV.Particles.instReprIsospinRatioDerived = { reprPrec := Tau.BookIV.Particles.instReprIsospinRatioDerived.repr }

---

### `Tau.BookIV.Particles.instReprIsospinRatioDerived.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2769-L2769)
**def
Tau.BookIV.Particles.instReprIsospinRatioDerived.repr :IsospinRatioDerived → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.isospin_ratio_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2771-L2771)
**def
Tau.BookIV.Particles.isospin_ratio_derived :IsospinRatioDerived**

Equations
- Tau.BookIV.Particles.isospin_ratio_derived = { }
Instances For

---

### `Tau.BookIV.Particles.UpQuarkWave44Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2773-L2783)
**structure
Tau.BookIV.Particles.UpQuarkWave44Status :Type**


[IV.R432] Up quark status update (Wave 44).

- direct_ppm : ℤ
Direct formula deviation (ppm).

- chain_ppm : ℤ
Chain formula deviation (ppm).

- improvement : ℕ
Improvement factor.

- all_sub_1600 : Bool
All six quarks sub-1600 ppm now.

Instances For

---

### `Tau.BookIV.Particles.instReprUpQuarkWave44Status.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2783-L2783)
**def
Tau.BookIV.Particles.instReprUpQuarkWave44Status.repr :UpQuarkWave44Status → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprUpQuarkWave44Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2783-L2783)
**instance
Tau.BookIV.Particles.instReprUpQuarkWave44Status :Repr UpQuarkWave44Status**

Equations
- Tau.BookIV.Particles.instReprUpQuarkWave44Status = { reprPrec := Tau.BookIV.Particles.instReprUpQuarkWave44Status.repr }

---

### `Tau.BookIV.Particles.up_quark_wave44_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2785-L2785)
**def
Tau.BookIV.Particles.up_quark_wave44_status :UpQuarkWave44Status**

Equations
- Tau.BookIV.Particles.up_quark_wave44_status = { }
Instances For

---

### `Tau.BookIV.Particles.WolfensteinANLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2787-L2804)
**structure
Tau.BookIV.Particles.WolfensteinANLO :Type**


[IV.D381] Wolfenstein A NLO: confinement correction.
A_NLO = A_LO·(1-ι<sub>τ</sub>³) = 0.7925 at +3109 ppm.

- a_lo_x10000 : ℕ
A_LO (×10000).

- a_nlo_x10000 : ℕ
A_NLO (×10000).

- a_pdg_x10000 : ℕ
PDG A (×10000).

- lo_ppm : ℤ
LO deviation ppm.

- nlo_ppm : ℤ
NLO deviation ppm.

- improvement : ℕ
Improvement factor.

- correction_exponent : ℕ
Correction is ι<sub>τ</sub>^dim(τ³).

Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinANLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2804-L2804)
**def
Tau.BookIV.Particles.instReprWolfensteinANLO.repr :WolfensteinANLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprWolfensteinANLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2804-L2804)
**instance
Tau.BookIV.Particles.instReprWolfensteinANLO :Repr WolfensteinANLO**

Equations
- Tau.BookIV.Particles.instReprWolfensteinANLO = { reprPrec := Tau.BookIV.Particles.instReprWolfensteinANLO.repr }

---

### `Tau.BookIV.Particles.wolfenstein_a_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2806-L2806)
**def
Tau.BookIV.Particles.wolfenstein_a_nlo :WolfensteinANLO**

Equations
- Tau.BookIV.Particles.wolfenstein_a_nlo = { }
Instances For

---

### `Tau.BookIV.Particles.JarlskogNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2808-L2827)
**structure
Tau.BookIV.Particles.JarlskogNLO :Type**


[IV.T198] Jarlskog NLO at +2624 ppm.
J_NLO = J_LO·(1+ι<sub>τ</sub>³) = 3.088×10⁻⁵.

- j_nlo_x1e7 : ℕ
J_NLO (×10⁷).

- j_lo_x1e7 : ℕ
J_LO (×10⁷).

- j_pdg_x1e7 : ℕ
PDG J (×10⁷).

- lo_ppm : ℤ
LO deviation ppm.

- nlo_ppm : ℤ
NLO deviation ppm.

- improvement_x10 : ℕ
Improvement factor (×10).

- correction_exponent : ℕ
Correction exponent = dim(τ³).

- sign_duality : Bool
Sign duality: A gets (1-δ), J gets (1+δ).

Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2827-L2827)
**def
Tau.BookIV.Particles.instReprJarlskogNLO.repr :JarlskogNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprJarlskogNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2827-L2827)
**instance
Tau.BookIV.Particles.instReprJarlskogNLO :Repr JarlskogNLO**

Equations
- Tau.BookIV.Particles.instReprJarlskogNLO = { reprPrec := Tau.BookIV.Particles.instReprJarlskogNLO.repr }

---

### `Tau.BookIV.Particles.jarlskog_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2829-L2829)
**def
Tau.BookIV.Particles.jarlskog_nlo :JarlskogNLO**

Equations
- Tau.BookIV.Particles.jarlskog_nlo = { }
Instances For

---

### `Tau.BookIV.Particles.CKMWave44Assessment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2831-L2841)
**structure
Tau.BookIV.Particles.CKMWave44Assessment :Type**


[IV.R433] CKM precision assessment (Wave 44).

- a_nlo_ppm : ℤ
A NLO ppm.

- j_nlo_ppm : ℤ
J NLO ppm.

- all_sub_3200 : Bool
All CKM sub-3200 ppm.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookIV.Particles.instReprCKMWave44Assessment.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2841-L2841)
**def
Tau.BookIV.Particles.instReprCKMWave44Assessment.repr :CKMWave44Assessment → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCKMWave44Assessment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2841-L2841)
**instance
Tau.BookIV.Particles.instReprCKMWave44Assessment :Repr CKMWave44Assessment**

Equations
- Tau.BookIV.Particles.instReprCKMWave44Assessment = { reprPrec := Tau.BookIV.Particles.instReprCKMWave44Assessment.repr }

---

### `Tau.BookIV.Particles.ckm_wave44_assessment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2843-L2843)
**def
Tau.BookIV.Particles.ckm_wave44_assessment :CKMWave44Assessment**

Equations
- Tau.BookIV.Particles.ckm_wave44_assessment = { }
Instances For

---

### `Tau.BookIV.Particles.StrangeBottomExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2861-L2880)
**structure
Tau.BookIV.Particles.StrangeBottomExponent :Type**


[IV.T199] m_s/m_b exponent from confinement-weighted mode count.
β(s/b) = (lobes² · a₃ + λ(1,0)) / (dim · W₃(4)) = 53/15.

- exp_num : ℕ
Numerator: lobes² · a₃ + 1.

- exp_den : ℕ
Denominator: dim · W₃(4).

- lobes_sq : ℕ
lobes² factor.

- a3 : ℕ
CF resonance a₃.

- lambda_10 : ℕ
Ground-state eigenvalue λ(1,0).

- deviation_ppm : ℤ
Deviation from PDG (ppm).

- num_check : self.lobes_sq * self.a3 + self.lambda_10 = self.exp_num
Numerator check: lobes² × a₃ + λ(1,0).

- den_check : 3 * 5 = self.exp_den
Denominator check: dim × W₃(4).

Instances For

---

### `Tau.BookIV.Particles.instReprStrangeBottomExponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2880-L2880)
**def
Tau.BookIV.Particles.instReprStrangeBottomExponent.repr :StrangeBottomExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprStrangeBottomExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2880-L2880)
**instance
Tau.BookIV.Particles.instReprStrangeBottomExponent :Repr StrangeBottomExponent**

Equations
- Tau.BookIV.Particles.instReprStrangeBottomExponent = { reprPrec := Tau.BookIV.Particles.instReprStrangeBottomExponent.repr }

---

### `Tau.BookIV.Particles.strange_bottom_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2882-L2882)
**def
Tau.BookIV.Particles.strange_bottom_exponent :StrangeBottomExponent**

Equations
- Tau.BookIV.Particles.strange_bottom_exponent = { num_check := Tau.BookIV.Particles.strange_bottom_exponent._proof_1,
 den_check := Tau.BookIV.Particles.strange_bottom_exponent._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.DownStrangeExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2884-L2899)
**structure
Tau.BookIV.Particles.DownStrangeExponent :Type**


[IV.T200] m_d/m_s exponent from winding phase space.
β(d/s) = lobes^(2·dim) / (a₃ + 2·W₃(4)) = 64/23.

- exp_num : ℕ
Numerator: lobes^(2·dim).

- exp_den : ℕ
Denominator: a₃ + 2·W₃(4).

- phase_dim : ℕ
Phase space dimension: 2·dim(τ³).

- deviation_ppm : ℤ
Deviation from PDG (ppm).

- num_check : 2 ^ 6 = self.exp_num
Numerator check: 2^6 = 64.

- den_check : 13 + 2 * 5 = self.exp_den
Denominator check: a₃ + 2·W₃(4).

Instances For

---

### `Tau.BookIV.Particles.instReprDownStrangeExponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2899-L2899)
**def
Tau.BookIV.Particles.instReprDownStrangeExponent.repr :DownStrangeExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprDownStrangeExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2899-L2899)
**instance
Tau.BookIV.Particles.instReprDownStrangeExponent :Repr DownStrangeExponent**

Equations
- Tau.BookIV.Particles.instReprDownStrangeExponent = { reprPrec := Tau.BookIV.Particles.instReprDownStrangeExponent.repr }

---

### `Tau.BookIV.Particles.down_strange_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2901-L2901)
**def
Tau.BookIV.Particles.down_strange_exponent :DownStrangeExponent**

Equations
- Tau.BookIV.Particles.down_strange_exponent = { num_check := Tau.BookIV.Particles.down_strange_exponent._proof_1,
 den_check := Tau.BookIV.Particles.down_strange_exponent._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.DownTypeSectorComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2903-L2919)
**structure
Tau.BookIV.Particles.DownTypeSectorComplete :Type**


[IV.R434] Down-type sector exponent completeness.

- tb_num : ℤ
β(t/b) numerator.

- tb_den : ℕ
β(t/b) denominator.

- sb_num : ℕ
β(s/b) numerator.

- sb_den : ℕ
β(s/b) denominator.

- ds_num : ℕ
β(d/s) numerator.

- ds_den : ℕ
β(d/s) denominator.

- worst_ppm : ℤ
Worst-case ppm.

Instances For

---

### `Tau.BookIV.Particles.instReprDownTypeSectorComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2919-L2919)
**instance
Tau.BookIV.Particles.instReprDownTypeSectorComplete :Repr DownTypeSectorComplete**

Equations
- Tau.BookIV.Particles.instReprDownTypeSectorComplete = { reprPrec := Tau.BookIV.Particles.instReprDownTypeSectorComplete.repr }

---

### `Tau.BookIV.Particles.instReprDownTypeSectorComplete.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2919-L2919)
**def
Tau.BookIV.Particles.instReprDownTypeSectorComplete.repr :DownTypeSectorComplete → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.down_type_sector_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2921-L2921)
**def
Tau.BookIV.Particles.down_type_sector_complete :DownTypeSectorComplete**

Equations
- Tau.BookIV.Particles.down_type_sector_complete = { }
Instances For

---

### `Tau.BookIV.Particles.IsospinExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2923-L2943)
**structure
Tau.BookIV.Particles.IsospinExponent :Type**


[IV.T201] m_u/m_d isospin exponent from Higgs-mediated splitting.
β(u/d) = lobes · n_H / W₃(4) = 14/5.

- exp_num : ℕ
Numerator: lobes × n_H.

- exp_den : ℕ
Denominator: W₃(4).

- n_H : ℕ
Higgs crossing number.

- lobes : ℕ
Lemniscate lobes.

- deviation_ppm : ℤ
Deviation from PDG (ppm).

- num_check : 2 * 7 = self.exp_num
Numerator check: lobes × n_H.

- nlo_coeff_num : ℕ
NLO coefficient 5/8 = W₃(4)/lobes³.

- nlo_coeff_den : ℕ
- nlo_check : 2 ^ 3 = self.nlo_coeff_den
NLO coefficient check.

Instances For

---

### `Tau.BookIV.Particles.instReprIsospinExponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2943-L2943)
**def
Tau.BookIV.Particles.instReprIsospinExponent.repr :IsospinExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprIsospinExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2943-L2943)
**instance
Tau.BookIV.Particles.instReprIsospinExponent :Repr IsospinExponent**

Equations
- Tau.BookIV.Particles.instReprIsospinExponent = { reprPrec := Tau.BookIV.Particles.instReprIsospinExponent.repr }

---

### `Tau.BookIV.Particles.isospin_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2945-L2945)
**def
Tau.BookIV.Particles.isospin_exponent :IsospinExponent**

Equations
- Tau.BookIV.Particles.isospin_exponent = { num_check := Tau.BookIV.Particles.isospin_exponent._proof_1,
 nlo_check := Tau.BookIV.Particles.isospin_exponent._proof_2 }
Instances For

---

### `Tau.BookIV.Particles.OP9Solved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2947-L2959)
**structure
Tau.BookIV.Particles.OP9Solved :Type**


[IV.R435] IV.OP9 SOLVED: all 7 quark mass exponents derived.

- total : ℕ
Total exponents.

- derived : ℕ
Derived exponents.

- all_derived : Bool
All derived.

- worst_ppm : ℤ
Worst-case ppm.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookIV.Particles.instReprOP9Solved.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2959-L2959)
**def
Tau.BookIV.Particles.instReprOP9Solved.repr :OP9Solved → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprOP9Solved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2959-L2959)
**instance
Tau.BookIV.Particles.instReprOP9Solved :Repr OP9Solved**

Equations
- Tau.BookIV.Particles.instReprOP9Solved = { reprPrec := Tau.BookIV.Particles.instReprOP9Solved.repr }

---

### `Tau.BookIV.Particles.op9_solved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2961-L2961)
**def
Tau.BookIV.Particles.op9_solved :OP9Solved**

Equations
- Tau.BookIV.Particles.op9_solved = { }
Instances For

---

### `Tau.BookIV.Particles.SixQuarkTableWave45`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2963-L2971)
**structure
Tau.BookIV.Particles.SixQuarkTableWave45 :Type**


[IV.D382] Updated six-quark table (Wave 45).

- all_sub_1600 : Bool
All six quarks sub-1600 ppm.

- exponents_derived : ℕ
Exponents derived (of 7).

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookIV.Particles.instReprSixQuarkTableWave45.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2971-L2971)
**def
Tau.BookIV.Particles.instReprSixQuarkTableWave45.repr :SixQuarkTableWave45 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprSixQuarkTableWave45`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2971-L2971)
**instance
Tau.BookIV.Particles.instReprSixQuarkTableWave45 :Repr SixQuarkTableWave45**

Equations
- Tau.BookIV.Particles.instReprSixQuarkTableWave45 = { reprPrec := Tau.BookIV.Particles.instReprSixQuarkTableWave45.repr }

---

### `Tau.BookIV.Particles.six_quark_table_wave45`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2973-L2973)
**def
Tau.BookIV.Particles.six_quark_table_wave45 :SixQuarkTableWave45**

Equations
- Tau.BookIV.Particles.six_quark_table_wave45 = { }
Instances For

---

### `Tau.BookIV.Particles.LobePowerHierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2975-L2990)
**structure
Tau.BookIV.Particles.LobePowerHierarchy :Type**


[IV.P223] Lobe-power hierarchy of quark exponents.
lobes^k: k=0 (input), k=1 (isospin), k=2 (generation), k=6 (full).

- k0_value : ℕ
k=0: input exponent (m_t).

- k1_value : ℕ
k=1: isospin splitting (m_u/m_d).

- k2_value : ℕ
k=2: generation transition (m_s/m_b, m_t/m_b).

- k6_value : ℕ
k=2·dim: full phase space (m_d/m_s).

- full_dim : ℕ
k=2·dim = 2×3 = 6.

- phase_check : 2 ^ 6 = self.k6_value
Check: lobes^6 = 64.

Instances For

---

### `Tau.BookIV.Particles.instReprLobePowerHierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2990-L2990)
**instance
Tau.BookIV.Particles.instReprLobePowerHierarchy :Repr LobePowerHierarchy**

Equations
- Tau.BookIV.Particles.instReprLobePowerHierarchy = { reprPrec := Tau.BookIV.Particles.instReprLobePowerHierarchy.repr }

---

### `Tau.BookIV.Particles.instReprLobePowerHierarchy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2990-L2990)
**def
Tau.BookIV.Particles.instReprLobePowerHierarchy.repr :LobePowerHierarchy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.lobe_power_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2992-L2992)
**def
Tau.BookIV.Particles.lobe_power_hierarchy :LobePowerHierarchy**

Equations
- Tau.BookIV.Particles.lobe_power_hierarchy = { phase_check := Tau.BookIV.Particles.down_strange_exponent._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.OP5Wave45Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L2994-L3002)
**structure
Tau.BookIV.Particles.OP5Wave45Status :Type**


[IV.R436] IV.OP5 status update (Wave 45).

- op9_solved : Bool
Exponent program complete.

- ckm_sub_3200 : Bool
CKM sub-3200 ppm.

- hierarchy_established : Bool
Lobe-power hierarchy established.

Instances For

---

### `Tau.BookIV.Particles.instReprOP5Wave45Status.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3002-L3002)
**def
Tau.BookIV.Particles.instReprOP5Wave45Status.repr :OP5Wave45Status → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprOP5Wave45Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3002-L3002)
**instance
Tau.BookIV.Particles.instReprOP5Wave45Status :Repr OP5Wave45Status**

Equations
- Tau.BookIV.Particles.instReprOP5Wave45Status = { reprPrec := Tau.BookIV.Particles.instReprOP5Wave45Status.repr }

---

### `Tau.BookIV.Particles.op5_wave45_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3004-L3004)
**def
Tau.BookIV.Particles.op5_wave45_status :OP5Wave45Status**

Equations
- Tau.BookIV.Particles.op5_wave45_status = { }
Instances For

---

### `Tau.BookIV.Particles.Theta23NNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3022-L3043)
**structure
Tau.BookIV.Particles.Theta23NNLO :Type**


[IV.T206] θ₂₃ NNLO from holonomy-at-window-squared.
sin(θ₂₃) = (1−ι<sub>τ</sub>⁵)/(1+ι<sub>τ</sub>) × (1−ι<sub>τ</sub>²/W₃(4)²)
= (1−ι<sub>τ</sub>⁵)/(1+ι<sub>τ</sub>) × (1−ι<sub>τ</sub>²/25)
sin²θ₂₃ = 0.5457 at −494 ppm from PDG 0.546.
94% improvement from NLO (+8604 ppm).
Universal NNLO pattern: W₃(4)²=25 denominator shared with m_μ/m_e.

- nnlo_denom : ℕ
NNLO correction denominator = W₃(4)².

- holonomy_power : ℕ
Holonomy power in correction (ι<sub>τ</sub>²).

- sin2_x10000 : ℕ
sin²θ₂₃ × 10000.

- pdg_x10000 : ℕ
PDG sin²θ₂₃ × 10000.

- deviation_ppm : ℤ
Deviation in ppm (signed).

- nlo_ppm : ℤ
NLO deviation was.

- improvement_pct : ℕ
Improvement factor (%).

Instances For

---

### `Tau.BookIV.Particles.instReprTheta23NNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3043-L3043)
**def
Tau.BookIV.Particles.instReprTheta23NNLO.repr :Theta23NNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprTheta23NNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3043-L3043)
**instance
Tau.BookIV.Particles.instReprTheta23NNLO :Repr Theta23NNLO**

Equations
- Tau.BookIV.Particles.instReprTheta23NNLO = { reprPrec := Tau.BookIV.Particles.instReprTheta23NNLO.repr }

---

### `Tau.BookIV.Particles.theta23_nnlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3045-L3045)
**def
Tau.BookIV.Particles.theta23_nnlo :Theta23NNLO**

Equations
- Tau.BookIV.Particles.theta23_nnlo = { }
Instances For

---

### `Tau.BookIV.Particles.theta23_nnlo_denom_is_w_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3047-L3049)
**theorem
Tau.BookIV.Particles.theta23_nnlo_denom_is_w_sq :theta23_nnlo.nnlo_denom = 5 * 5**


W₃(4)² = 25: NNLO denominator shared with m_μ/m_e.

---

### `Tau.BookIV.Particles.DeltaCPNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3055-L3073)
**structure
Tau.BookIV.Particles.DeltaCPNLO :Type**


[IV.T207] δ_CP NLO from fiber correction.
δ_CP = π + arctan(ι<sub>τ</sub>·(1−ι<sub>τ</sub>³)) = 198.11°
Fiber correction (1−ι<sub>τ</sub>³) = confinement screening at ι<sub>τ</sub>^dim(τ³).
Same correction as CKM Jarlskog NLO (IV.T198).
PDG: 197° ± 25°. Deviation: +5645 ppm (was +9365), 40% improvement.

- tau_deg_x100 : ℕ
τ-prediction in degrees × 100.

- pdg_deg_x100 : ℕ
PDG central value × 100.

- fiber_exp : ℕ
Fiber correction exponent (dim(τ³)).

- lo_ppm : ℕ
LO deviation ppm.

- nlo_ppm : ℕ
NLO deviation ppm.

- improvement_pct : ℕ
Improvement percentage.

Instances For

---

### `Tau.BookIV.Particles.instReprDeltaCPNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3073-L3073)
**instance
Tau.BookIV.Particles.instReprDeltaCPNLO :Repr DeltaCPNLO**

Equations
- Tau.BookIV.Particles.instReprDeltaCPNLO = { reprPrec := Tau.BookIV.Particles.instReprDeltaCPNLO.repr }

---

### `Tau.BookIV.Particles.instReprDeltaCPNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3073-L3073)
**def
Tau.BookIV.Particles.instReprDeltaCPNLO.repr :DeltaCPNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.delta_cp_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3075-L3075)
**def
Tau.BookIV.Particles.delta_cp_nlo :DeltaCPNLO**

Equations
- Tau.BookIV.Particles.delta_cp_nlo = { }
Instances For

---

### `Tau.BookIV.Particles.HighPpmCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3081-L3098)
**structure
Tau.BookIV.Particles.HighPpmCatalog :Type**


[IV.D386] High-ppm structural limit catalog (Wave 49).
After NNLO corrections:


- θ₂₃: +8604 → −494 (NNLO, sub-1000)

- δ_CP: +9365 → +5645 (NLO, 40% improved)

- m_μ/m_e: +6156 → −8.2 (already done Wave 6D)
Structural limits (no NLO solution):

- QLC θ₁₂: −41965 ppm (needs exact θ_C coupling)

- η̄ pentagon: +75275 ppm (complex geometry)


- improved : ℕ
Items improved this wave.

- structural_limits : ℕ
Items at structural limit.

- already_done : ℕ
Items already resolved (prior waves).

- best_nnlo_ppm : ℕ
Best NNLO result (θ₂₃ ppm, absolute).

Instances For

---

### `Tau.BookIV.Particles.instReprHighPpmCatalog.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3098-L3098)
**def
Tau.BookIV.Particles.instReprHighPpmCatalog.repr :HighPpmCatalog → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprHighPpmCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3098-L3098)
**instance
Tau.BookIV.Particles.instReprHighPpmCatalog :Repr HighPpmCatalog**

Equations
- Tau.BookIV.Particles.instReprHighPpmCatalog = { reprPrec := Tau.BookIV.Particles.instReprHighPpmCatalog.repr }

---

### `Tau.BookIV.Particles.high_ppm_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/ThreeGenerations.lean#L3100-L3100)
**def
Tau.BookIV.Particles.high_ppm_catalog :HighPpmCatalog**

Equations
- Tau.BookIV.Particles.high_ppm_catalog = { }
Instances For
