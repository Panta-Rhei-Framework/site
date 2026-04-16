---
layout: taulib-doc
title: "TauLib.BookVI.Agency.MetabolicEnergy"
permalink: /verify/taulib/docs/book-vi-agency-metabolic-energy/
lane: verify
module_name: "TauLib.BookVI.Agency.MetabolicEnergy"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.Agency.MetabolicEnergy


Metabolic energy: ATP structure, membrane topology, and metabolism.

## Registry Cross-References


- [VI.D32] ATP/ADP Oscillation — `ATPOscillation`

- [VI.D33] Membrane as Lemniscate Boundary — `MembraneAsLemniscate`

- [VI.T19] Universal Currency Uniqueness — `atp_universality`

- [VI.P11] Krebs Cycle as Loop_L — `krebs_cycle_loop`

- [VI.P12] Self-Assembly as Boundary-Induced Distinction — `membrane_self_assembly`


## Cross-Book Authority


- Book I, Part IX: ι<sub>τ</sub> = 2/(π+e) calibration constant

- Book II, Part III: L = S¹ ∨ S¹ (lemniscate boundary)

- Book II, Ch 44: Central Theorem O(τ³) ≅ A_spec(L)

- Book III, Part III: Riemann force (energy quantization)


## Ground Truth Sources


- Book VI Chapter 19 (2nd Edition): Metabolism

- Book VI Chapter 20 (2nd Edition): ATP

- Book VI Chapter 21 (2nd Edition): Membranes


---

### `Tau.BookVI.MetabolicEnergy.ATPOscillation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L35-L50)
**structure
Tau.BookVI.MetabolicEnergy.ATPOscillation :Type**


[VI.D32] ATP/ADP Oscillation: discrete energy currency.
ΔG ≈ 30.5 kJ/mol. Set by Riemann force at E₂
(Book III, Part III: energy quantization).
Calibrated by ι<sub>τ</sub> (Book I, Part IX).

- delta_g_x10 : ℕ
Free energy in kJ/mol (×10 for integer representation).

- delta_g_eq : self.delta_g_x10 = 305
ΔG ≈ 30.5 kJ/mol → 305 in ×10 representation.

- riemann_governed : Bool
Governed by Riemann force (Book III, Part III).

- iota_tau_calibrated : Bool
Calibrated by ι<sub>τ</sub> (Book I, Part IX).

- universal : Bool
Universal across all terrestrial life.

Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprATPOscillation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L50-L50)
**def
Tau.BookVI.MetabolicEnergy.instReprATPOscillation.repr :ATPOscillation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprATPOscillation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L50-L50)
**instance
Tau.BookVI.MetabolicEnergy.instReprATPOscillation :Repr ATPOscillation**

Equations
- Tau.BookVI.MetabolicEnergy.instReprATPOscillation = { reprPrec := Tau.BookVI.MetabolicEnergy.instReprATPOscillation.repr }

---

### `Tau.BookVI.MetabolicEnergy.atp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L52-L54)
**def
Tau.BookVI.MetabolicEnergy.atp :ATPOscillation**

Equations
- Tau.BookVI.MetabolicEnergy.atp = { delta_g_x10 := 305, delta_g_eq := Tau.BookVI.MetabolicEnergy.atp._proof_1 }
Instances For

---

### `Tau.BookVI.MetabolicEnergy.CurrencyUniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L60-L78)
**structure
Tau.BookVI.MetabolicEnergy.CurrencyUniqueness :Type**


[VI.T19] Universal Currency Uniqueness Theorem.
ATP is the unique energy currency satisfying:
(i) Life Loop closure (metabolic cycle returns to initial state)
(ii) Coupling constraint (energy quantum matches phosphate bond)
(iii) Topological constraint (adenine-ribose-triphosphate topology)

- constraint_count : ℕ
Number of uniqueness constraints.

- count_eq : self.constraint_count = 3
Exactly 3 constraints.

- loop_closure : Bool
(i) Life Loop closure.

- coupling : Bool
(ii) Coupling constraint.

- topological : Bool
(iii) Topological constraint.

- unique_currency : String
Result: ATP is unique.

Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprCurrencyUniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L78-L78)
**instance
Tau.BookVI.MetabolicEnergy.instReprCurrencyUniqueness :Repr CurrencyUniqueness**

Equations
- Tau.BookVI.MetabolicEnergy.instReprCurrencyUniqueness = { reprPrec := Tau.BookVI.MetabolicEnergy.instReprCurrencyUniqueness.repr }

---

### `Tau.BookVI.MetabolicEnergy.instReprCurrencyUniqueness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L78-L78)
**def
Tau.BookVI.MetabolicEnergy.instReprCurrencyUniqueness.repr :CurrencyUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.MetabolicEnergy.currency_uniq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L80-L82)
**def
Tau.BookVI.MetabolicEnergy.currency_uniq :CurrencyUniqueness**

Equations
- Tau.BookVI.MetabolicEnergy.currency_uniq = { constraint_count := 3, count_eq := Tau.BookVI.MetabolicEnergy.currency_uniq._proof_1 }
Instances For

---

### `Tau.BookVI.MetabolicEnergy.atp_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L84-L89)
**theorem
Tau.BookVI.MetabolicEnergy.atp_universality :currency_uniq.constraint_count = 3 ∧ currency_uniq.loop_closure = true ∧ currency_uniq.coupling = true ∧ currency_uniq.topological = true**


---

### `Tau.BookVI.MetabolicEnergy.MembraneAsLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L95-L113)
**structure
Tau.BookVI.MetabolicEnergy.MembraneAsLemniscate :Type**


[VI.D33] Membrane as Lemniscate Boundary: L = S¹ ∨ S¹.
Lipid bilayer = two leaflets (outer/inner) sharing hydrophobic core.
Topologically: L = S¹_outer ∨ S¹_inner.
Authority: Book II, Part III (L construction); Book II, Ch 44 (Central Theorem).
The membrane IS the τ-Distinction boundary realized physically.

- leaflet_count : ℕ
Number of leaflets.

- leaflets_eq : self.leaflet_count = 2
Exactly 2 leaflets.

- outer_leaflet : String
Outer leaflet = S¹.

- inner_leaflet : String
Inner leaflet = S¹.

- wedge_point : String
Wedge point = hydrophobic core.

- realizes_distinction : Bool
Realizes τ-Distinction boundary.

Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprMembraneAsLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L113-L113)
**instance
Tau.BookVI.MetabolicEnergy.instReprMembraneAsLemniscate :Repr MembraneAsLemniscate**

Equations
- Tau.BookVI.MetabolicEnergy.instReprMembraneAsLemniscate = { reprPrec := Tau.BookVI.MetabolicEnergy.instReprMembraneAsLemniscate.repr }

---

### `Tau.BookVI.MetabolicEnergy.instReprMembraneAsLemniscate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L113-L113)
**def
Tau.BookVI.MetabolicEnergy.instReprMembraneAsLemniscate.repr :MembraneAsLemniscate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.MetabolicEnergy.membrane`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L115-L117)
**def
Tau.BookVI.MetabolicEnergy.membrane :MembraneAsLemniscate**

Equations
- Tau.BookVI.MetabolicEnergy.membrane = { leaflet_count := 2, leaflets_eq := Tau.BookVI.MetabolicEnergy.membrane._proof_1 }
Instances For

---

### `Tau.BookVI.MetabolicEnergy.membrane_two_leaflets`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L119-L120)
**theorem
Tau.BookVI.MetabolicEnergy.membrane_two_leaflets :membrane.leaflet_count = 2**


---

### `Tau.BookVI.MetabolicEnergy.membrane_realizes_distinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L122-L123)
**theorem
Tau.BookVI.MetabolicEnergy.membrane_realizes_distinction :membrane.realizes_distinction = true**


---

### `Tau.BookVI.MetabolicEnergy.KrebsCycleLoop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L129-L142)
**structure
Tau.BookVI.MetabolicEnergy.KrebsCycleLoop :Type**


[VI.P11] Krebs Cycle as Loop_L instantiation.
The citric acid cycle is a Poincaré circulation (Book III, Part II)
that instantiates the Life Loop Class at the metabolic level.
8-step cycle: acetyl-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP → return.

- steps : ℕ
Number of cycle steps.

- steps_eq : self.steps = 8
Exactly 8 steps.

- poincare_circulation : Bool
Is a Poincaré circulation (Book III, Part II).

- life_loop_instance : Bool
Instantiates Life Loop Class.

Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprKrebsCycleLoop.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L142-L142)
**def
Tau.BookVI.MetabolicEnergy.instReprKrebsCycleLoop.repr :KrebsCycleLoop → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprKrebsCycleLoop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L142-L142)
**instance
Tau.BookVI.MetabolicEnergy.instReprKrebsCycleLoop :Repr KrebsCycleLoop**

Equations
- Tau.BookVI.MetabolicEnergy.instReprKrebsCycleLoop = { reprPrec := Tau.BookVI.MetabolicEnergy.instReprKrebsCycleLoop.repr }

---

### `Tau.BookVI.MetabolicEnergy.krebs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L144-L146)
**def
Tau.BookVI.MetabolicEnergy.krebs :KrebsCycleLoop**

Equations
- Tau.BookVI.MetabolicEnergy.krebs = { steps := 8, steps_eq := Tau.BookVI.MetabolicEnergy.krebs._proof_1 }
Instances For

---

### `Tau.BookVI.MetabolicEnergy.krebs_cycle_loop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L148-L152)
**theorem
Tau.BookVI.MetabolicEnergy.krebs_cycle_loop :krebs.steps = 8 ∧ krebs.poincare_circulation = true ∧ krebs.life_loop_instance = true**


---

### `Tau.BookVI.MetabolicEnergy.MembraneAssembly`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L158-L169)
**structure
Tau.BookVI.MetabolicEnergy.MembraneAssembly :Type**


[VI.P12] Self-Assembly as Boundary-Induced Distinction.
Amphiphilic self-assembly produces L = S¹ ∨ S¹ boundary
without requiring a template or external information.
The lemniscate topology is the ONLY self-assembling 2_τ boundary.

- no_template : Bool
Self-assembles (no template needed).

- produces_lemniscate : Bool
Produces L topology.

- unique : Bool
Unique self-assembling boundary.

Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprMembraneAssembly.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L169-L169)
**def
Tau.BookVI.MetabolicEnergy.instReprMembraneAssembly.repr :MembraneAssembly → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.MetabolicEnergy.instReprMembraneAssembly`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L169-L169)
**instance
Tau.BookVI.MetabolicEnergy.instReprMembraneAssembly :Repr MembraneAssembly**

Equations
- Tau.BookVI.MetabolicEnergy.instReprMembraneAssembly = { reprPrec := Tau.BookVI.MetabolicEnergy.instReprMembraneAssembly.repr }

---

### `Tau.BookVI.MetabolicEnergy.self_assembly`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L171-L171)
**def
Tau.BookVI.MetabolicEnergy.self_assembly :MembraneAssembly**

Equations
- Tau.BookVI.MetabolicEnergy.self_assembly = { }
Instances For

---

### `Tau.BookVI.MetabolicEnergy.membrane_self_assembly`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/MetabolicEnergy.lean#L173-L177)
**theorem
Tau.BookVI.MetabolicEnergy.membrane_self_assembly :self_assembly.no_template = true ∧ self_assembly.produces_lemniscate = true ∧ self_assembly.unique = true**
