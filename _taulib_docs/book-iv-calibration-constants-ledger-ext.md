---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.ConstantsLedgerExt"
permalink: /verify/taulib/docs/book-iv-calibration-constants-ledger-ext/
lane: verify
module_name: "TauLib.BookIV.Calibration.ConstantsLedgerExt"
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

# TauLib.BookIV.Calibration.ConstantsLedgerExt


Extended constants ledger: coupling table, fundamental scales,
particle masses, and structural constants — the Ch15 export contract.

## Registry Cross-References


- [IV.D305] Coupling Constants Table — `CouplingTable`

- [IV.R283] Lean verification — (structural remark)

- [IV.D306] Fundamental Scales Table — `FundamentalScalesTable`

- [IV.D307] Particle Mass Table — `ParticleMassTable`

- [IV.R285] Honest deviations — (structural remark)

- [IV.D308] Structural Constants Table — `StructuralConstantsTable`

- [IV.R286] 5, 4, 3, 2, 1 — (structural remark)

- [IV.R287] Honest fraction — (structural remark)


## Ground Truth Sources


- Chapter 15 of Book IV (2nd Edition)


---

### `Tau.BookIV.Calibration.CouplingTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L33-L45)
**structure
Tau.BookIV.Calibration.CouplingTable :Type**


[IV.D305] The complete coupling constants table:
10 entries (5 self + 5 cross), all rational functions of ι<sub>τ</sub>.

- self_count : ℕ
Self-coupling count.

- self_eq : self.self_count = 5
- cross_count : ℕ
Cross-coupling count.

- cross_eq : self.cross_count = 5
- total : ℕ
Total.

- total_eq : self.total = self.self_count + self.cross_count
Instances For

---

### `Tau.BookIV.Calibration.instReprCouplingTable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L45-L45)
**def
Tau.BookIV.Calibration.instReprCouplingTable.repr :CouplingTable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprCouplingTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L45-L45)
**instance
Tau.BookIV.Calibration.instReprCouplingTable :Repr CouplingTable**

Equations
- Tau.BookIV.Calibration.instReprCouplingTable = { reprPrec := Tau.BookIV.Calibration.instReprCouplingTable.repr }

---

### `Tau.BookIV.Calibration.coupling_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L47-L54)
**def
Tau.BookIV.Calibration.coupling_table :CouplingTable**


The canonical coupling table.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.FundamentalScalesTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L63-L73)
**structure
Tau.BookIV.Calibration.FundamentalScalesTable :Type**


[IV.D306] Fundamental scales table: dimensional constants as products
of relational units M, L, H, Q and ι<sub>τ</sub>.

- entry_count : ℕ
Number of fundamental scale entries.

- entry_eq : self.entry_count = 5
Entries: c, h, k_e, ε₀, μ₀ = 5 dimensional formulas.

- planck_derived : ℕ
Plus Planck units derived from them.

- planck_eq : self.planck_derived = 3
Instances For

---

### `Tau.BookIV.Calibration.instReprFundamentalScalesTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L73-L73)
**instance
Tau.BookIV.Calibration.instReprFundamentalScalesTable :Repr FundamentalScalesTable**

Equations
- Tau.BookIV.Calibration.instReprFundamentalScalesTable = { reprPrec := Tau.BookIV.Calibration.instReprFundamentalScalesTable.repr }

---

### `Tau.BookIV.Calibration.instReprFundamentalScalesTable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L73-L73)
**def
Tau.BookIV.Calibration.instReprFundamentalScalesTable.repr :FundamentalScalesTable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.fundamental_scales`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L75-L80)
**def
Tau.BookIV.Calibration.fundamental_scales :FundamentalScalesTable**


The canonical fundamental scales table.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.ParticleMassTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L86-L96)
**structure
Tau.BookIV.Calibration.ParticleMassTable :Type**


[IV.D307] Particle mass table: predicted masses as functions
of ι<sub>τ</sub> and m_n, compared to experiment.

- entry_count : ℕ
Number of mass predictions.

- entry_eq : self.entry_count = 6
Entries: m_e, m_p, m_W, m_Z, m_H, m_ν.

- best_ppm_times_1000 : ℕ
Best precision achieved (m_e: 0.025 ppm).

- best_eq : self.best_ppm_times_1000 = 25
Instances For

---

### `Tau.BookIV.Calibration.instReprParticleMassTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L96-L96)
**instance
Tau.BookIV.Calibration.instReprParticleMassTable :Repr ParticleMassTable**

Equations
- Tau.BookIV.Calibration.instReprParticleMassTable = { reprPrec := Tau.BookIV.Calibration.instReprParticleMassTable.repr }

---

### `Tau.BookIV.Calibration.instReprParticleMassTable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L96-L96)
**def
Tau.BookIV.Calibration.instReprParticleMassTable.repr :ParticleMassTable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.particle_mass_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L98-L103)
**def
Tau.BookIV.Calibration.particle_mass_table :ParticleMassTable**


The canonical particle mass table.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.StructuralConstantsTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L113-L131)
**structure
Tau.BookIV.Calibration.StructuralConstantsTable :Type**


[IV.D308] Structural constants: dimensionless integers determined
by kernel axioms K0-K6.

- generators : ℕ
5 generators.

- gen_eq : self.generators = 5
- arena_dim : ℕ
4 arena dimensions.

- dim_eq : self.arena_dim = 4
- spatial : ℕ
3 spatial dimensions (fiber).

- spatial_eq : self.spatial = 3
- lobes : ℕ
2 lobes (lemniscate).

- lobes_eq : self.lobes = 2
- constants : ℕ
1 master constant.

- const_eq : self.constants = 1
Instances For

---

### `Tau.BookIV.Calibration.instReprStructuralConstantsTable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L131-L131)
**def
Tau.BookIV.Calibration.instReprStructuralConstantsTable.repr :StructuralConstantsTable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprStructuralConstantsTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L131-L131)
**instance
Tau.BookIV.Calibration.instReprStructuralConstantsTable :Repr StructuralConstantsTable**

Equations
- Tau.BookIV.Calibration.instReprStructuralConstantsTable = { reprPrec := Tau.BookIV.Calibration.instReprStructuralConstantsTable.repr }

---

### `Tau.BookIV.Calibration.structural_constants`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L133-L144)
**def
Tau.BookIV.Calibration.structural_constants :StructuralConstantsTable**


The canonical structural constants.
Equations
- One or more equations did not get rendered due to their size.
Instances For
