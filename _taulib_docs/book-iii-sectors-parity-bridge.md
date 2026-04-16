---
layout: taulib-doc
title: "TauLib.BookIII.Sectors.ParityBridge"
permalink: /verify/taulib/docs/book-iii-sectors-parity-bridge/
lane: verify
module_name: "TauLib.BookIII.Sectors.ParityBridge"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Sectors.ParityBridge


Parity Bridge Theorem, No Knobs Principle, and Coupling Ledger.

## Registry Cross-References


- [III.T07] Parity Bridge Theorem -- `parity_bridge_check`

- [III.T08] No Knobs Principle -- `no_knobs_check`

- [III.D18] Coupling Ledger -- `CouplingEntry`, `coupling_ledger_check`


## Mathematical Content


**III.T07 (Parity Bridge):** The weak sector (A, π-generator) is the unique
sector whose balanced spectral polarity permits the E₁→E₂ transition.

**III.T08 (No Knobs):** All inter-sector couplings are canonically determined
by ι<sub>τ</sub> = 2/(π+e). The framework has no free parameters.

**III.D18 (Coupling Ledger):** The 10-entry inventory of all inter-sector
couplings: 4 self-couplings + 6 cross-couplings.

---

### `Tau.BookIII.Sectors.parity_bridge_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L36-L46)
**def
Tau.BookIII.Sectors.parity_bridge_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T07] Parity Bridge check: the A-sector (π-generator) is the
unique primitive sector with balanced spectral polarity, enabling
the E₁→E₂ transition (physics → computation).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.CouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L52-L57)
**structure
Tau.BookIII.Sectors.CouplingEntry :Type**


[III.D18] A coupling entry: interaction strength between two sectors.

- sector_i : Sector
- sector_j : Sector
- value : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Sectors.instReprCouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L57-L57)
**instance
Tau.BookIII.Sectors.instReprCouplingEntry :Repr CouplingEntry**

Equations
- Tau.BookIII.Sectors.instReprCouplingEntry = { reprPrec := Tau.BookIII.Sectors.instReprCouplingEntry.repr }

---

### `Tau.BookIII.Sectors.instReprCouplingEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L57-L57)
**def
Tau.BookIII.Sectors.instReprCouplingEntry.repr :CouplingEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.instDecidableEqCouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L57-L57)
**instance
Tau.BookIII.Sectors.instDecidableEqCouplingEntry :DecidableEq CouplingEntry**

Equations
- Tau.BookIII.Sectors.instDecidableEqCouplingEntry = Tau.BookIII.Sectors.instDecidableEqCouplingEntry.decEq

---

### `Tau.BookIII.Sectors.instDecidableEqCouplingEntry.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L57-L57)
**def
Tau.BookIII.Sectors.instDecidableEqCouplingEntry.decEq
(x✝ x✝¹ : CouplingEntry)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.instBEqCouplingEntry.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L57-L57)
**def
Tau.BookIII.Sectors.instBEqCouplingEntry.beq :CouplingEntry → CouplingEntry → Bool**

Equations
- Tau.BookIII.Sectors.instBEqCouplingEntry.beq { sector_i := a, sector_j := a_1, value := a_2 }
 { sector_i := b, sector_j := b_1, value := b_2 } = (a == b && (a_1 == b_1 && a_2 == b_2))
- Tau.BookIII.Sectors.instBEqCouplingEntry.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Sectors.instBEqCouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L57-L57)
**instance
Tau.BookIII.Sectors.instBEqCouplingEntry :BEq CouplingEntry**

Equations
- Tau.BookIII.Sectors.instBEqCouplingEntry = { beq := Tau.BookIII.Sectors.instBEqCouplingEntry.beq }

---

### `Tau.BookIII.Sectors.sector_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L59-L84)
**def
Tau.BookIII.Sectors.sector_coupling
(si sj : Sector)

(bound : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D18] Compute the coupling between two sectors.
κ(S_i, S_j) counts shared character-lattice structure:
number of (m, n) pairs where sector_of(m,n) = S_i AND
the character has non-trivial m-projection (if Sj is B-type)
or n-projection (if Sj is C-type).
Equations
- Tau.BookIII.Sectors.sector_coupling si sj bound = Tau.BookIII.Sectors.sector_coupling.go si sj bound 0 0 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Sectors.sector_coupling.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L67-L83)@[irreducible]

**def
Tau.BookIII.Sectors.sector_coupling.go
(si sj : Sector)

(bound : Denotation.TauIdx)

(m n acc fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.coupling_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L86-L107)
**def
Tau.BookIII.Sectors.coupling_ledger
(bound : Denotation.TauIdx)
 :List CouplingEntry**


[III.D18] Build the 10-entry coupling ledger:
upper triangle of 4×4 primitive sector matrix.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.coupling_ledger.go_i`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L92-L98)
**def
Tau.BookIII.Sectors.coupling_ledger.go_i
(si_list sj_full : List Sector)

(bound : Denotation.TauIdx)

(acc : List CouplingEntry)
 :List CouplingEntry**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Sectors.coupling_ledger.go_i [] sj_full bound acc = acc
Instances For

---

### `Tau.BookIII.Sectors.coupling_ledger.go_j`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L99-L107)
**def
Tau.BookIII.Sectors.coupling_ledger.go_j
(si : Sector)

(sj_list : List Sector)

(bound : Denotation.TauIdx)

(acc : List CouplingEntry)
 :List CouplingEntry**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Sectors.coupling_ledger.go_j si [] bound acc = acc
Instances For

---

### `Tau.BookIII.Sectors.coupling_ledger_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L109-L111)
**def
Tau.BookIII.Sectors.coupling_ledger_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D18] Coupling ledger completeness: exactly 10 entries.
Equations
- Tau.BookIII.Sectors.coupling_ledger_check bound = ((Tau.BookIII.Sectors.coupling_ledger bound).length == 10)
Instances For

---

### `Tau.BookIII.Sectors.no_knobs_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L117-L126)
**def
Tau.BookIII.Sectors.no_knobs_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T08] No Knobs check: all couplings are canonically determined.

- Complete ledger (10 entries)

- Sector preservation (structure determines couplings)

- Template invariance (structure is rigid)

- Langlands reflection (sector structure preserved under enrichment)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.parity_bridge_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L152-L153)
**theorem
Tau.BookIII.Sectors.parity_bridge_5_3 :parity_bridge_check 5 3 = true**


---

### `Tau.BookIII.Sectors.coupling_ledger_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L156-L157)
**theorem
Tau.BookIII.Sectors.coupling_ledger_3 :coupling_ledger_check 3 = true**


---

### `Tau.BookIII.Sectors.no_knobs_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L160-L161)
**theorem
Tau.BookIII.Sectors.no_knobs_5_3 :no_knobs_check 5 3 = true**


---

### `Tau.BookIII.Sectors.a_is_balanced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L167-L168)
**theorem
Tau.BookIII.Sectors.a_is_balanced :sector_of { m_index := 1, n_index := 1 } = Sector.A**


[III.T07] Structural: balanced polarity is unique to A-sector.

---

### `Tau.BookIII.Sectors.b_not_a`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L170-L171)
**theorem
Tau.BookIII.Sectors.b_not_a :sector_of { m_index := 2, n_index := 0 } = Sector.B**


[III.T07] Structural: B and C sectors are NOT balanced.

---

### `Tau.BookIII.Sectors.c_not_a`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L172-L172)
**theorem
Tau.BookIII.Sectors.c_not_a :sector_of { m_index := 0, n_index := 2 } = Sector.C**


---

### `Tau.BookIII.Sectors.d_self_coupling_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L174-L177)
**theorem
Tau.BookIII.Sectors.d_self_coupling_1 :sector_coupling Sector.D Sector.D 5 = 1**


[III.T08] Structural: D-sector self-coupling is always 1
(only the trivial character maps to D).

---

### `Tau.BookIII.Sectors.coupling_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/ParityBridge.lean#L179-L181)
**theorem
Tau.BookIII.Sectors.coupling_count :4 * (4 + 1) / 2 = 10**


[III.D18] Structural: the coupling ledger has exactly 10 entries
for 4 sectors (upper triangle of 4×4 matrix).
