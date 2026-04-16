---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.ConstantsLedger"
permalink: /verify/taulib/docs/book-iv-calibration-constants-ledger/
lane: verify
module_name: "TauLib.BookIV.Calibration.ConstantsLedger"
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

# TauLib.BookIV.Calibration.ConstantsLedger


Master synthesis table of all constants with scope labels — the "export contract"
for Parts III–X of Book IV.

## Registry Cross-References


- [IV.D38] Ledger Entry — `LedgerEntry`, `LedgerScope`

- [IV.D39] Complete Constants Ledger — `complete_ledger`

- [IV.T09] Ledger Count — `ledger_count`

- [IV.R09] Self-Assessment — scope distribution theorem


## Mathematical Content


### The Constants Ledger


Part II's output is a master table of every constant derived or compared.
Each entry carries an explicit scope label from the 4-tier system:


- **Established**: Lean-proved structural identities (temporal complement, etc.)

- **Tau-effective**: Derived within the τ-framework, internally verified
(dimensional bridge formulas, Maxwell relation)

- **Conjectural**: Comparisons with experiment, not yet formally proved
(all numerical near-matches with SI)

- **Metaphorical**: Conceptual analogies (none in Part II)


### Categories


- **Couplings** (10 entries): The complete coupling ledger from ι<sub>τ</sub>

- **Dimensional formulas** (5 entries): c, h, k_e, ε₀, μ₀ derivation chain

- **Structural identities** (2 entries): Maxwell relation, Coulomb-permittivity

- **Dimensionless near-matches** (3 entries): α, sin²θ_W, α_s

- **Anchor and framework** (3 entries): m_n anchor, 5→1 collapse, G frontier


### Export Contract


Parts III–X may import any entry from this ledger. The scope label
determines how the entry may be used:


- Established/Tau-effective entries may serve as premises in proofs

- Conjectural entries may only be used as comparison targets


## Ground Truth Sources


- Book IV Part II ch15 (Constants Ledger)


---

### `Tau.BookIV.Calibration.LedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L58-L64)
**inductive
Tau.BookIV.Calibration.LedgerScope :Type**


[IV.D38] Four-tier scope classification for ledger entries.

- Established : LedgerScope
- TauEffective : LedgerScope
- Conjectural : LedgerScope
- Metaphorical : LedgerScope
Instances For

---

### `Tau.BookIV.Calibration.instReprLedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L64-L64)
**instance
Tau.BookIV.Calibration.instReprLedgerScope :Repr LedgerScope**

Equations
- Tau.BookIV.Calibration.instReprLedgerScope = { reprPrec := Tau.BookIV.Calibration.instReprLedgerScope.repr }

---

### `Tau.BookIV.Calibration.instReprLedgerScope.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L64-L64)
**def
Tau.BookIV.Calibration.instReprLedgerScope.repr :LedgerScope → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqLedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L64-L64)
**instance
Tau.BookIV.Calibration.instDecidableEqLedgerScope :DecidableEq LedgerScope**

Equations
- Tau.BookIV.Calibration.instDecidableEqLedgerScope x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Calibration.LedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L70-L80)
**structure
Tau.BookIV.Calibration.LedgerEntry :Type**


[IV.D38] A single entry in the constants ledger.

- id : String
Registry ID (e.g., "IV.T01").

- name : String
Display name.

- category : String
Category: coupling, formula, identity, near-match, framework.

- scope : LedgerScope
Scope label.

Instances For

---

### `Tau.BookIV.Calibration.instReprLedgerEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L80-L80)
**def
Tau.BookIV.Calibration.instReprLedgerEntry.repr :LedgerEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprLedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L80-L80)
**instance
Tau.BookIV.Calibration.instReprLedgerEntry :Repr LedgerEntry**

Equations
- Tau.BookIV.Calibration.instReprLedgerEntry = { reprPrec := Tau.BookIV.Calibration.instReprLedgerEntry.repr }

---

### `Tau.BookIV.Calibration.coupling_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L86-L98)
**def
Tau.BookIV.Calibration.coupling_ledger :List LedgerEntry**


The 10 coupling constants from ι<sub>τ</sub>.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.formula_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L104-L111)
**def
Tau.BookIV.Calibration.formula_ledger :List LedgerEntry**


The 5 dimensional bridge formulas.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.identity_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L117-L121)
**def
Tau.BookIV.Calibration.identity_ledger :List LedgerEntry**


The 2 structural identities proved algebraically.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.near_match_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L127-L132)
**def
Tau.BookIV.Calibration.near_match_ledger :List LedgerEntry**


The 3 dimensionless near-matches with experiment.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.framework_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L138-L143)
**def
Tau.BookIV.Calibration.framework_ledger :List LedgerEntry**


The anchor, collapse, and frontier entries.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.complete_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L149-L152)
**def
Tau.BookIV.Calibration.complete_ledger :List LedgerEntry**


[IV.D39] The complete constants ledger: all Part II outputs.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.ledger_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L158-L159)
**theorem
Tau.BookIV.Calibration.ledger_count :complete_ledger.length = 23**


[IV.T09] The ledger has exactly 23 entries.

---

### `Tau.BookIV.Calibration.ledger_breakdown`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L161-L168)
**theorem
Tau.BookIV.Calibration.ledger_breakdown :coupling_ledger.length = 10 ∧ formula_ledger.length = 5 ∧ identity_ledger.length = 2 ∧ near_match_ledger.length = 3 ∧ framework_ledger.length = 3**


10 coupling + 5 formula + 2 identity + 3 near-match + 3 framework = 23.

---

### `Tau.BookIV.Calibration.scope_distribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L174-L183)
**theorem
Tau.BookIV.Calibration.scope_distribution :(List.filter (fun (x : LedgerEntry) => x.scope == LedgerScope.Established) complete_ledger).length = 12 ∧ (List.filter (fun (x : LedgerEntry) => x.scope == LedgerScope.TauEffective) complete_ledger).length = 7 ∧ (List.filter (fun (x : LedgerEntry) => x.scope == LedgerScope.Conjectural) complete_ledger).length = 4 ∧ (List.filter (fun (x : LedgerEntry) => x.scope == LedgerScope.Metaphorical) complete_ledger).length = 0**


[IV.R09] Self-assessment: scope distribution across the ledger.


- Established: 12 (10 couplings + 2 identities)

- Tau-effective: 7 (5 formulas + 2 framework)

- Conjectural: 4 (3 near-matches + 1 G frontier)

- Metaphorical: 0


---

### `Tau.BookIV.Calibration.no_metaphorical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L185-L188)
**theorem
Tau.BookIV.Calibration.no_metaphorical :(List.filter (fun (x : LedgerEntry) => x.scope == LedgerScope.Metaphorical) complete_ledger).length = 0**


No metaphorical entries in Part II.

---

### `Tau.BookIV.Calibration.all_have_ids`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L194-L196)
**theorem
Tau.BookIV.Calibration.all_have_ids :(complete_ledger.all fun (e : LedgerEntry) => decide (e.id.length > 0)) = true**


Every entry has a non-empty registry ID.

---

### `Tau.BookIV.Calibration.all_have_names`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/ConstantsLedger.lean#L198-L200)
**theorem
Tau.BookIV.Calibration.all_have_names :(complete_ledger.all fun (e : LedgerEntry) => decide (e.name.length > 0)) = true**


Every entry has a non-empty name.
