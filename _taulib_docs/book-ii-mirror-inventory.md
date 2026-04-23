---
layout: taulib-doc
title: "TauLib.BookII.Mirror.Inventory"
permalink: /verify/taulib/docs/book-ii-mirror-inventory/
lane: verify
module_name: "TauLib.BookII.Mirror.Inventory"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Mirror.Inventory


The rewiring table: a complete inventory of the 12 structural sign-changes
between orthodox and tau approaches.

## Registry Cross-References


- [II.D72] The Rewiring Table -- `RewiringRow`, `full_rewiring_table`,
`rewiring_table_complete`


## Mathematical Content


**II.D72 (The Rewiring Table):** The rewiring table is the definitive
inventory of Part XI. Each row records one sign level, the orthodox choice,
the tau equivalent, and the structural trade-off. The table has exactly 12
rows, one for each sign level in the classification (II.D68).

The table serves as a reading guide: for each row, the reader can trace
the change from orthodox to tau and understand the structural reason for
the switch. The trade-offs are not arbitrary -- they are forced by the
foundational choices (K0-K6 axioms, prime polarity, split-complex scalars).

Part XI summary statistics:


- 7 definitions (D68-D74)

- 4 theorems (T43-T46)

- This inventory module


---

### `Tau.BookII.Mirror.RewiringRow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L38-L45)
**structure
Tau.BookII.Mirror.RewiringRow :Type**


[II.D72] A single row of the rewiring table: one sign level,
the orthodox choice, the tau equivalent, and the trade-off.

- level : SignLevel
- orthodox : String
- tau_equiv : String
- tradeoff : String
Instances For

---

### `Tau.BookII.Mirror.instReprRewiringRow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L45-L45)
**instance
Tau.BookII.Mirror.instReprRewiringRow :Repr RewiringRow**

Equations
- Tau.BookII.Mirror.instReprRewiringRow = { reprPrec := Tau.BookII.Mirror.instReprRewiringRow.repr }

---

### `Tau.BookII.Mirror.instReprRewiringRow.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L45-L45)
**def
Tau.BookII.Mirror.instReprRewiringRow.repr :RewiringRow → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.full_rewiring_table`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L47-L96)
**def
Tau.BookII.Mirror.full_rewiring_table :List RewiringRow**


[II.D72] The full rewiring table: all 12 rows.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.rewiring_table_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L102-L104)
**theorem
Tau.BookII.Mirror.rewiring_table_complete :full_rewiring_table.length = 12**


[II.D72] The rewiring table has exactly 12 rows.

---

### `Tau.BookII.Mirror.row_orthodox_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L106-L108)
**def
Tau.BookII.Mirror.row_orthodox_nonempty
(r : RewiringRow)
 :Bool**


Each row has a nonempty orthodox description.
Equations
- Tau.BookII.Mirror.row_orthodox_nonempty r = decide (r.orthodox.length > 0)
Instances For

---

### `Tau.BookII.Mirror.row_tau_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L110-L112)
**def
Tau.BookII.Mirror.row_tau_nonempty
(r : RewiringRow)
 :Bool**


Each row has a nonempty tau description.
Equations
- Tau.BookII.Mirror.row_tau_nonempty r = decide (r.tau_equiv.length > 0)
Instances For

---

### `Tau.BookII.Mirror.row_tradeoff_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L114-L116)
**def
Tau.BookII.Mirror.row_tradeoff_nonempty
(r : RewiringRow)
 :Bool**


Each row has a nonempty trade-off description.
Equations
- Tau.BookII.Mirror.row_tradeoff_nonempty r = decide (r.tradeoff.length > 0)
Instances For

---

### `Tau.BookII.Mirror.all_orthodox_rows_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L118-L120)
**theorem
Tau.BookII.Mirror.all_orthodox_rows_nonempty :full_rewiring_table.all row_orthodox_nonempty = true**


All orthodox descriptions are nonempty.

---

### `Tau.BookII.Mirror.all_tau_rows_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L122-L124)
**theorem
Tau.BookII.Mirror.all_tau_rows_nonempty :full_rewiring_table.all row_tau_nonempty = true**


All tau descriptions are nonempty.

---

### `Tau.BookII.Mirror.all_tradeoff_rows_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L126-L128)
**theorem
Tau.BookII.Mirror.all_tradeoff_rows_nonempty :full_rewiring_table.all row_tradeoff_nonempty = true**


All trade-off descriptions are nonempty.

---

### `Tau.BookII.Mirror.table_levels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L134-L136)
**def
Tau.BookII.Mirror.table_levels :List SignLevel**


Extract the sign levels from the rewiring table.
Equations
- Tau.BookII.Mirror.table_levels = List.map Tau.BookII.Mirror.RewiringRow.level Tau.BookII.Mirror.full_rewiring_table
Instances For

---

### `Tau.BookII.Mirror.table_levels_match`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L138-L140)
**theorem
Tau.BookII.Mirror.table_levels_match :table_levels = allSignLevels**


The table levels match the canonical sign level list.

---

### `Tau.BookII.Mirror.table_covers_all_levels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L142-L144)
**theorem
Tau.BookII.Mirror.table_covers_all_levels :table_levels.length = allSignLevels.length**


The table covers all sign levels (same length and same elements).

---

### `Tau.BookII.Mirror.part_xi_definitions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L150-L151)
**def
Tau.BookII.Mirror.part_xi_definitions :ℕ**


Part XI definition count (D68-D74).
Equations
- Tau.BookII.Mirror.part_xi_definitions = 7
Instances For

---

### `Tau.BookII.Mirror.part_xi_theorems`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L153-L154)
**def
Tau.BookII.Mirror.part_xi_theorems :ℕ**


Part XI theorem count (T43-T46).
Equations
- Tau.BookII.Mirror.part_xi_theorems = 4
Instances For

---

### `Tau.BookII.Mirror.part_xi_total_entries`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L156-L157)
**def
Tau.BookII.Mirror.part_xi_total_entries :ℕ**


Part XI total formal entries.
Equations
- Tau.BookII.Mirror.part_xi_total_entries = Tau.BookII.Mirror.part_xi_definitions + Tau.BookII.Mirror.part_xi_theorems
Instances For

---

### `Tau.BookII.Mirror.part_xi_entry_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L159-L161)
**theorem
Tau.BookII.Mirror.part_xi_entry_count :part_xi_total_entries = 11**


Part XI has 11 formal entries total.

---

### `Tau.BookII.Mirror.part_xi_modules`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L163-L164)
**def
Tau.BookII.Mirror.part_xi_modules :ℕ**


Part XI module count.
Equations
- Tau.BookII.Mirror.part_xi_modules = 4
Instances For

---

### `Tau.BookII.Mirror.part_xi_module_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L166-L168)
**theorem
Tau.BookII.Mirror.part_xi_module_count :part_xi_modules = 4**


Four modules in Part XI.

---

### `Tau.BookII.Mirror.table_12`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L195-L196)
**theorem
Tau.BookII.Mirror.table_12 :full_rewiring_table.length = 12**


---

### `Tau.BookII.Mirror.rows_orthodox`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L199-L200)
**theorem
Tau.BookII.Mirror.rows_orthodox :full_rewiring_table.all row_orthodox_nonempty = true**


---

### `Tau.BookII.Mirror.rows_tau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L202-L203)
**theorem
Tau.BookII.Mirror.rows_tau :full_rewiring_table.all row_tau_nonempty = true**


---

### `Tau.BookII.Mirror.rows_tradeoff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L205-L206)
**theorem
Tau.BookII.Mirror.rows_tradeoff :full_rewiring_table.all row_tradeoff_nonempty = true**


---

### `Tau.BookII.Mirror.levels_match`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/Inventory.lean#L209-L210)
**theorem
Tau.BookII.Mirror.levels_match :table_levels = allSignLevels**
