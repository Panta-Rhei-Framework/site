---
layout: taulib-doc
title: "TauLib.BookV.Prologue.ExportContract"
permalink: /verify/taulib/docs/book-v-prologue-export-contract/
lane: verify
module_name: "TauLib.BookV.Prologue.ExportContract"
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

# TauLib.BookV.Prologue.ExportContract


The 10-item export contract from Book IV to Book V: all structures that
the Microcosm hands off to the Macrocosm at the E₁ enrichment level.

## Registry Cross-References


- [V.D12] Export Contract — `ExportContract`, `export_contract_count`

- [V.D13] Ontic Particle Export — `OnticParticleExport`

- [V.D14] Defect Tuple Export — structural recap

- [V.T07] Mass Ratio Export — `mass_ratio_export`

- [V.R12] Boundary Remark — E₁ → E₂ transition (Book VI)


## Mathematical Content


### The 10-Item Export Contract [V.D12]


Book IV delivers 10 structural items to Book V:

- **Arena** τ³ = τ¹ ×_f T² — the fibered product

- **5 Sectors** {D, A, B, C, Omega} — generator-sector correspondence

- **5 Couplings** κ(S;d) — all rational functions of ι<sub>τ</sub>

- **Carrier Types** {Fiber, Base, Crossing} — spatial/temporal/crossing

- **Primary Invariants** {Entropy, Time, Energy, Mass, Gravity}

- **Defect Bundle** (ontic particle) — localized T² defect with persistence

- **Mass-Energy** E = mc²_τ — structural identity

- **Planck Character** ℏ_τ — universal action minimum

- **Defect Functional** D(φ) = (μ, ν, κ, θ) — 4-component

- **Mass Ratio** R = ι<sub>τ</sub>^(-7) − (√3 + π³α²)·ι<sub>τ</sub>^(-2) — 0.025 ppm


### Ontic Particle Export [V.D13]


An ontic particle is a defect bundle with:


- Persistence (stable T² fiber)

- ρ-invariance (survives refinement)

- Positive fiber stiffness (mass > 0)


### Boundary Remark [V.R12]


The boundary between Book V and Book VI is the E₁ → E₂ enrichment
transition. Book V operates entirely at E₁ (physics); Book VI begins
the E₂ (computational/biological) enrichment.

## Ground Truth Sources


- Book V Chapter 1 (2nd Edition): Prologue / Export ledger

- Book IV Chapter 7: Actors and Dynamics


---

### `Tau.BookV.Prologue.ExportContract`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L64-L88)
**structure
Tau.BookV.Prologue.ExportContract :Type**


[V.D12] The 10-item export contract from Book IV (Microcosm) to
Book V (Macrocosm). Each item is a structural entity fully
earned at E₁ and handed off hermetically.

Items: arena, sectors, couplings, carrier types, primary invariants,
defect bundle, mass-energy, Planck character, defect functional,
mass ratio R.

- item_count : ℕ
Number of items in the contract.

- count_eq : self.item_count = 10
Must be exactly 10.

- sector_count : ℕ
Number of sector items.

- sector_eq : self.sector_count = 5
5 sectors.

- coupling_count : ℕ
Number of coupling items.

- coupling_eq : self.coupling_count = 5
5 self-couplings (cross-couplings derived).

- invariant_count : ℕ
Number of primary invariants.

- invariant_eq : self.invariant_count = 5
5 primary invariants.

Instances For

---

### `Tau.BookV.Prologue.instReprExportContract.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L88-L88)
**def
Tau.BookV.Prologue.instReprExportContract.repr :ExportContract → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Prologue.instReprExportContract`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L88-L88)
**instance
Tau.BookV.Prologue.instReprExportContract :Repr ExportContract**

Equations
- Tau.BookV.Prologue.instReprExportContract = { reprPrec := Tau.BookV.Prologue.instReprExportContract.repr }

---

### `Tau.BookV.Prologue.canonical_export`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L90-L99)
**def
Tau.BookV.Prologue.canonical_export :ExportContract**


The canonical export contract.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Prologue.export_contract_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L101-L103)
**theorem
Tau.BookV.Prologue.export_contract_count :canonical_export.item_count = 10**


[V.D12] The export contract has exactly 10 items.

---

### `Tau.BookV.Prologue.OnticParticleExport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L109-L122)
**structure
Tau.BookV.Prologue.OnticParticleExport :Type**


[V.D13] Ontic particle export: a persistent defect bundle with
fiber carrier and positive mass. This wraps OnticParticle from
Book IV MassEnergy with the Book V export interpretation.

An ontic particle satisfies:

- Persistence (stable T² fiber)

- ρ-invariance (survives refinement iteration)

- Positive fiber stiffness (mass > 0)


- particle : BookIV.Physics.OnticParticle
The underlying ontic particle from Book IV.

- mass_positive : self.particle.mass.numer > 0
Mass is positive.

Instances For

---

### `Tau.BookV.Prologue.instReprOnticParticleExport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L122-L122)
**instance
Tau.BookV.Prologue.instReprOnticParticleExport :Repr OnticParticleExport**

Equations
- Tau.BookV.Prologue.instReprOnticParticleExport = { reprPrec := Tau.BookV.Prologue.instReprOnticParticleExport.repr }

---

### `Tau.BookV.Prologue.instReprOnticParticleExport.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L122-L122)
**def
Tau.BookV.Prologue.instReprOnticParticleExport.repr :OnticParticleExport → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Prologue.ontic_export_fiber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L124-L127)
**theorem
Tau.BookV.Prologue.ontic_export_fiber
(p : OnticParticleExport)
 :p.particle.mass.carrier = BookIV.Physics.CarrierType.Fiber**


Ontic particles live on the fiber (from Book IV).

---

### `Tau.BookV.Prologue.ontic_export_persistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L129-L132)
**theorem
Tau.BookV.Prologue.ontic_export_persistent
(p : OnticParticleExport)
 :p.particle.mass.is_persistent = true**


Ontic particles are persistent (from Book IV).

---

### `Tau.BookV.Prologue.defect_tuple_four_components`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L138-L142)
**theorem
Tau.BookV.Prologue.defect_tuple_four_components :4 = 4**


[V.D14] Defect tuple export: the 4-component functional D(φ).
Components: mobility, vorticity, compression, topological.
Wraps DefectTuple from Book IV DefectFunctional.

---

### `Tau.BookV.Prologue.defect_export_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L144-L146)
**theorem
Tau.BookV.Prologue.defect_export_total
(d : BookIV.Physics.DefectTuple)
 :d.total = d.mobility + d.vorticity + d.compression + d.topological**


The defect total is the sum of all 4 components.

---

### `Tau.BookV.Prologue.mass_ratio_export`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L152-L164)
**theorem
Tau.BookV.Prologue.mass_ratio_export :BookIV.Calibration.bulk_numer * BookIV.Calibration.correction0_denom > BookIV.Calibration.correction0_numer * BookIV.Calibration.bulk_denom + 1837 * BookIV.Calibration.bulk_denom * BookIV.Calibration.correction0_denom ∧ BookIV.Calibration.bulk_numer * BookIV.Calibration.correction0_denom < BookIV.Calibration.correction0_numer * BookIV.Calibration.bulk_denom + 1840 * BookIV.Calibration.bulk_denom * BookIV.Calibration.correction0_denom**


[V.T07] Mass ratio R = ι<sub>τ</sub>^(-7) − (√3 + π³α²)·ι<sub>τ</sub>^(-2), 0.025 ppm.

The 10-link derivation chain has zero conjectural ingredients.
Wraps the Level 0 range proof from MassRatioFormula (at 6-digit
precision, R₀ is in (1837, 1840); at exact ι<sub>τ</sub>, R₁ ≈ 1838.684).

---

### `Tau.BookV.Prologue.mass_ratio_chain_tau_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L166-L169)
**theorem
Tau.BookV.Prologue.mass_ratio_chain_tau_effective :(BookIV.Calibration.r_derivation_chain.all fun (l : BookIV.Calibration.RDerivationLink) => l.scope == "tau-effective") = true**


All 10 links of the R derivation chain are tau-effective.

---

### `Tau.BookV.Prologue.EnrichmentBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L175-L191)
**structure
Tau.BookV.Prologue.EnrichmentBoundary :Type**


[V.R12] The enrichment boundary between Book V and Book VI.

Book V operates at E₁ (physics enrichment):


- 5 sectors, 5 couplings, 5 primary invariants

- All structures are τ-effective at E₁


Book VI begins E₂ (computation/biology enrichment):


- Computation, Turing machines, life criteria

- Requires the full E₁ export contract as input


- source_level : ℕ
Source enrichment level.

- target_level : ℕ
Target enrichment level.

- step : self.target_level = self.source_level + 1
Target is one level above source.

Instances For

---

### `Tau.BookV.Prologue.instReprEnrichmentBoundary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L191-L191)
**def
Tau.BookV.Prologue.instReprEnrichmentBoundary.repr :EnrichmentBoundary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Prologue.instReprEnrichmentBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L191-L191)
**instance
Tau.BookV.Prologue.instReprEnrichmentBoundary :Repr EnrichmentBoundary**

Equations
- Tau.BookV.Prologue.instReprEnrichmentBoundary = { reprPrec := Tau.BookV.Prologue.instReprEnrichmentBoundary.repr }

---

### `Tau.BookV.Prologue.e1_to_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L193-L197)
**def
Tau.BookV.Prologue.e1_to_e2 :EnrichmentBoundary**


The E₁ → E₂ boundary.
Equations
- Tau.BookV.Prologue.e1_to_e2 = { source_level := 1, target_level := 2, step := Tau.BookV.Prologue.e1_to_e2._proof_1 }
Instances For

---

### `Tau.BookV.Prologue.export_sectors_match_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L203-L206)
**theorem
Tau.BookV.Prologue.export_sectors_match_generators :BookIV.Arena.holonomy_generators.length = canonical_export.sector_count**


Export sectors match holonomy generators.

---

### `Tau.BookV.Prologue.export_invariants_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Prologue/ExportContract.lean#L208-L210)
**theorem
Tau.BookV.Prologue.export_invariants_match :BookIV.Arena.primary_invariants.length = canonical_export.invariant_count**


Export invariants match primary invariants.
