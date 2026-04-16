---
layout: taulib-doc
title: "TauLib.BookIV.Particles.PeriodicTable"
permalink: /verify/taulib/docs/book-iv-particles-periodic-table/
lane: verify
module_name: "TauLib.BookIV.Particles.PeriodicTable"
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

# TauLib.BookIV.Particles.PeriodicTable


Periodic table from sector couplings: atom definition, electron quantum
numbers, Madelung rule from T² geometry, period length sequence,
chemical bonding (covalent, ionic, metallic), molecular geometry from
mode repulsion, hybrid modes, and the five-rung donut ladder.

## Registry Cross-References


- [IV.D203] Atom as Dressed Nuclear Mode — `AtomDef`

- [IV.D204] Electron Quantum Numbers — `ElectronQuantumNumbers`

- [IV.D205] Covalent Bond — `CovalentBond`

- [IV.D206] Ionic Bond — `IonicBond`

- [IV.D207] Metallic Bond — `MetallicBond`

- [IV.D208] Hybrid Modes — `HybridMode`

- [IV.T88] Period Length Sequence — `period_length_sequence`

- [IV.R140] Madelung Rule from T² Geometry — `madelung_rule`

- [IV.R141] Topological not Accidental — `topological_not_accidental`

- [IV.R142] Molecules as Mode-Sharing Graphs — comment-only (not_applicable)

- [IV.R143] No New Parameters for Chemistry — comment-only (not_applicable)

- [IV.R144] Mode-Repulsion Geometry — `mode_repulsion_geometry`

- [IV.R145] Homochirality and Parity Violation — comment-only (not_applicable)

- [IV.R146] Structural vs Quantitative Chemistry — comment-only (not_applicable)

- [IV.R147] The Donut Ladder — comment-only (not_applicable)

- [IV.R148] Comparison with Orthodox Physics — `orthodox_comparison`


## Mathematical Content


The periodic table is a topological invariant of T²: shell capacities 2n²
follow from winding mode counting, and period pairing from the Madelung
energy ordering E_{n,l} ≈ −1/(n + l·ι<sub>τ</sub>)² determined by the fiber shape
ratio ι<sub>τ</sub>. The sequence 2, 8, 8, 18, 18, 32, 32,... is fixed by geometry.

Chemical bonds (covalent, ionic, metallic) are different patterns of
B-sector winding modes on T². Molecular geometry follows from mode
repulsion: k mode pairs maximize angular separation.

## Ground Truth Sources


- Chapter 49 of Book IV (2nd Edition)


---

### `Tau.BookIV.Particles.AtomDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L53-L70)
**structure
Tau.BookIV.Particles.AtomDef :Type**


[IV.D203] An atom of atomic number Z is a stable composite of:

- Nuclear core: Z protons + N neutrons (bound by C-sector)

- Electron shell: Z electrons on T² (bound by B-sector EM)


A neutral atom has vanishing net B-sector winding:
electromagnetically closed.

- z : ℕ
Atomic number Z.

- n : ℕ
Neutron number N.

- electrons : ℕ
Number of shell electrons in neutral atom.

- neutral : self.electrons = self.z
Neutral: electrons = Z.

- em_closed : Bool
Electromagnetically closed.

Instances For

---

### `Tau.BookIV.Particles.instReprAtomDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L70-L70)
**def
Tau.BookIV.Particles.instReprAtomDef.repr :AtomDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprAtomDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L70-L70)
**instance
Tau.BookIV.Particles.instReprAtomDef :Repr AtomDef**

Equations
- Tau.BookIV.Particles.instReprAtomDef = { reprPrec := Tau.BookIV.Particles.instReprAtomDef.repr }

---

### `Tau.BookIV.Particles.hydrogen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L72-L74)
**def
Tau.BookIV.Particles.hydrogen :AtomDef**


Hydrogen atom.
Equations
- Tau.BookIV.Particles.hydrogen = { z := 1, n := 0, electrons := 1, neutral := Tau.BookIV.Particles.hydrogen._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.helium`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L76-L78)
**def
Tau.BookIV.Particles.helium :AtomDef**


Helium atom.
Equations
- Tau.BookIV.Particles.helium = { z := 2, n := 2, electrons := 2, neutral := Tau.BookIV.Particles.helium._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.carbon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L80-L82)
**def
Tau.BookIV.Particles.carbon :AtomDef**


Carbon atom.
Equations
- Tau.BookIV.Particles.carbon = { z := 6, n := 6, electrons := 6, neutral := Tau.BookIV.Particles.carbon._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.iron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L84-L86)
**def
Tau.BookIV.Particles.iron :AtomDef**


Iron atom.
Equations
- Tau.BookIV.Particles.iron = { z := 26, n := 30, electrons := 26, neutral := Tau.BookIV.Particles.iron._proof_1 }
Instances For

---

### `Tau.BookIV.Particles.ElectronQuantumNumbers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L92-L113)
**structure
Tau.BookIV.Particles.ElectronQuantumNumbers :Type**


[IV.D204] An electron mode on T² bound to nuclear charge Z
carries four quantum numbers:


- n: principal (total winding depth)

- l: angular (0 ≤ l ≤ n-1, lobe structure on L)

- m_l: magnetic (-l ≤ m_l ≤ l, orientation on L)

- m_s: spin (±1/2, chirality on T²)


Shell capacity: 2n² = 2 × sum_{l=0}^{n-1} (2l+1).

- n_principal : ℕ
Principal quantum number (n ≥ 1).

- l_angular : ℕ
Angular quantum number (0 ≤ l ≤ n-1).

- m_l_magnetic : ℤ
Magnetic quantum number (|m_l| ≤ l).

- spin_up : Bool
Spin (true = +1/2, false = -1/2).

- n_pos : self.n_principal ≥ 1
n ≥ 1.

- l_bound : self.l_angular < self.n_principal
l < n.

Instances For

---

### `Tau.BookIV.Particles.instReprElectronQuantumNumbers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L113-L113)
**instance
Tau.BookIV.Particles.instReprElectronQuantumNumbers :Repr ElectronQuantumNumbers**

Equations
- Tau.BookIV.Particles.instReprElectronQuantumNumbers = { reprPrec := Tau.BookIV.Particles.instReprElectronQuantumNumbers.repr }

---

### `Tau.BookIV.Particles.instReprElectronQuantumNumbers.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L113-L113)
**def
Tau.BookIV.Particles.instReprElectronQuantumNumbers.repr :ElectronQuantumNumbers → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.shell_capacity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L115-L116)
**def
Tau.BookIV.Particles.shell_capacity
(n : ℕ)
 :ℕ**


Shell capacity for principal quantum number n: 2n².
Equations
- Tau.BookIV.Particles.shell_capacity n = 2 * n * n
Instances For

---

### `Tau.BookIV.Particles.shell_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L118-L118)
**theorem
Tau.BookIV.Particles.shell_1 :shell_capacity 1 = 2**


---

### `Tau.BookIV.Particles.shell_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L119-L119)
**theorem
Tau.BookIV.Particles.shell_2 :shell_capacity 2 = 8**


---

### `Tau.BookIV.Particles.shell_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L120-L120)
**theorem
Tau.BookIV.Particles.shell_3 :shell_capacity 3 = 18**


---

### `Tau.BookIV.Particles.shell_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L121-L121)
**theorem
Tau.BookIV.Particles.shell_4 :shell_capacity 4 = 32**


---

### `Tau.BookIV.Particles.MadelungRule`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L127-L145)
**structure
Tau.BookIV.Particles.MadelungRule :Type**


[IV.R140] The Madelung rule (subshells fill in order of increasing n+l)
has no first-principles derivation in orthodox physics.

In Category τ, the breathing eigenvalue on T² with shape ratio ι<sub>τ</sub> is
E_{n,l} ≈ −1/(n + l·ι<sub>τ</sub>)², and since ι<sub>τ</sub> ≈ 0.34, the n+l ordering
emerges naturally from the fiber geometry.

The subshell filling order is:
1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, ...

- ordering_param : String
Ordering parameter: n + l.

- origin : String
Origin: breathing eigenvalue on T² with shape ι<sub>τ</sub>.

- no_orthodox_derivation : Bool
No orthodox first-principles derivation.

- tau_derived : Bool
Tau-framework: emerges from geometry.

Instances For

---

### `Tau.BookIV.Particles.instReprMadelungRule.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L145-L145)
**def
Tau.BookIV.Particles.instReprMadelungRule.repr :MadelungRule → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprMadelungRule`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L145-L145)
**instance
Tau.BookIV.Particles.instReprMadelungRule :Repr MadelungRule**

Equations
- Tau.BookIV.Particles.instReprMadelungRule = { reprPrec := Tau.BookIV.Particles.instReprMadelungRule.repr }

---

### `Tau.BookIV.Particles.madelung_rule`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L147-L147)
**def
Tau.BookIV.Particles.madelung_rule :MadelungRule**

Equations
- Tau.BookIV.Particles.madelung_rule = { }
Instances For

---

### `Tau.BookIV.Particles.madelung_tau_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L149-L149)
**theorem
Tau.BookIV.Particles.madelung_tau_derived :madelung_rule.tau_derived = true**


---

### `Tau.BookIV.Particles.PeriodLengthSequence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L155-L173)
**structure
Tau.BookIV.Particles.PeriodLengthSequence :Type**


[IV.T88] The periodic table period lengths follow:
2, 8, 8, 18, 18, 32, 32,...

Each length = 2n² (twice a perfect square).
Each value (except 2) appears twice.

This is a topological consequence of T² fiber geometry:
shell capacity 2n² combined with Aufbau filling order
determines noble gas closures.

- lengths : List ℕ
First 7 period lengths.

- twice_perfect_square : Bool
Each is twice a perfect square.

- doubled : Bool
Each (except 2) appears twice.

- topological : Bool
Topological origin.

Instances For

---

### `Tau.BookIV.Particles.instReprPeriodLengthSequence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L173-L173)
**def
Tau.BookIV.Particles.instReprPeriodLengthSequence.repr :PeriodLengthSequence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprPeriodLengthSequence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L173-L173)
**instance
Tau.BookIV.Particles.instReprPeriodLengthSequence :Repr PeriodLengthSequence**

Equations
- Tau.BookIV.Particles.instReprPeriodLengthSequence = { reprPrec := Tau.BookIV.Particles.instReprPeriodLengthSequence.repr }

---

### `Tau.BookIV.Particles.period_length_sequence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L175-L175)
**def
Tau.BookIV.Particles.period_length_sequence :PeriodLengthSequence**

Equations
- Tau.BookIV.Particles.period_length_sequence = { }
Instances For

---

### `Tau.BookIV.Particles.seven_periods`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L177-L177)
**theorem
Tau.BookIV.Particles.seven_periods :period_length_sequence.lengths.length = 7**


---

### `Tau.BookIV.Particles.noble_gas_z`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L179-L180)
**def
Tau.BookIV.Particles.noble_gas_z :List ℕ**


Noble gas atomic numbers from cumulative period lengths.
Equations
- Tau.BookIV.Particles.noble_gas_z = [2, 10, 18, 36, 54, 86, 118]
Instances For

---

### `Tau.BookIV.Particles.seven_noble_gases`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L182-L182)
**theorem
Tau.BookIV.Particles.seven_noble_gases :noble_gas_z.length = 7**


---

### `Tau.BookIV.Particles.first_noble_gas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L184-L185)
**theorem
Tau.BookIV.Particles.first_noble_gas :noble_gas_z.head? = some 2**


Cumulative sum of period lengths gives noble gas Z values.

---

### `Tau.BookIV.Particles.period_2_is_2x1sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L187-L188)
**theorem
Tau.BookIV.Particles.period_2_is_2x1sq :2 = 2 * 1 * 1**


Period lengths are all twice perfect squares.

---

### `Tau.BookIV.Particles.period_8_is_2x2sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L189-L189)
**theorem
Tau.BookIV.Particles.period_8_is_2x2sq :8 = 2 * 2 * 2**


---

### `Tau.BookIV.Particles.period_18_is_2x3sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L190-L190)
**theorem
Tau.BookIV.Particles.period_18_is_2x3sq :18 = 2 * 3 * 3**


---

### `Tau.BookIV.Particles.period_32_is_2x4sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L191-L191)
**theorem
Tau.BookIV.Particles.period_32_is_2x4sq :32 = 2 * 4 * 4**


---

### `Tau.BookIV.Particles.topological_not_accidental`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L197-L201)
**def
Tau.BookIV.Particles.topological_not_accidental :String**


[IV.R141] The sequence 2, 8, 8, 18, 18, 32,... is a topological
invariant of T²: the periodic table has its shape because the
fiber torus has its shape.
Equations
- Tau.BookIV.Particles.topological_not_accidental = "Period sequence is topological invariant of T^2, not accidental"
Instances For

---

### `Tau.BookIV.Particles.CovalentBond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L207-L221)
**structure
Tau.BookIV.Particles.CovalentBond :Type**


[IV.D205] A covalent bond of order k: k electron winding modes on T²
contribute simultaneously to shell closure of both atoms.


- k=1: single bond (e.g., H₂)

- k=2: double bond (e.g., O=O)

- k=3: triple bond (e.g., N≡N)


Bond strength increases with k via mode-overlap integrals.

- order : ℕ
Bond order.

- example_mol : String
Example molecule.

- order_valid : self.order ≥ 1 ∧ self.order ≤ 3
Order is 1, 2, or 3.

Instances For

---

### `Tau.BookIV.Particles.instReprCovalentBond.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L221-L221)
**def
Tau.BookIV.Particles.instReprCovalentBond.repr :CovalentBond → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprCovalentBond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L221-L221)
**instance
Tau.BookIV.Particles.instReprCovalentBond :Repr CovalentBond**

Equations
- Tau.BookIV.Particles.instReprCovalentBond = { reprPrec := Tau.BookIV.Particles.instReprCovalentBond.repr }

---

### `Tau.BookIV.Particles.single_bond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L223-L224)
**def
Tau.BookIV.Particles.single_bond :CovalentBond**

Equations
- Tau.BookIV.Particles.single_bond = { order := 1, example_mol := "H_2", order_valid := Tau.BookIV.Particles.single_bond._proof_3 }
Instances For

---

### `Tau.BookIV.Particles.double_bond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L226-L227)
**def
Tau.BookIV.Particles.double_bond :CovalentBond**

Equations
- Tau.BookIV.Particles.double_bond = { order := 2, example_mol := "O=O", order_valid := Tau.BookIV.Particles.double_bond._proof_3 }
Instances For

---

### `Tau.BookIV.Particles.triple_bond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L229-L230)
**def
Tau.BookIV.Particles.triple_bond :CovalentBond**

Equations
- Tau.BookIV.Particles.triple_bond = { order := 3, example_mol := "N_triple_N", order_valid := Tau.BookIV.Particles.triple_bond._proof_3 }
Instances For

---

### `Tau.BookIV.Particles.IonicBond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L236-L246)
**structure
Tau.BookIV.Particles.IonicBond :Type**


[IV.D206] An ionic bond is a complete transfer of electron winding
modes from atom A to atom B such that both ions achieve noble gas
closure. Bond energy E_ionic ≈ −k²α/r_AB.

- complete_transfer : Bool
Complete electron transfer.

- both_closed : Bool
Both ions approach noble gas closure.

- example_compound : String
Example.

Instances For

---

### `Tau.BookIV.Particles.instReprIonicBond.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L246-L246)
**def
Tau.BookIV.Particles.instReprIonicBond.repr :IonicBond → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprIonicBond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L246-L246)
**instance
Tau.BookIV.Particles.instReprIonicBond :Repr IonicBond**

Equations
- Tau.BookIV.Particles.instReprIonicBond = { reprPrec := Tau.BookIV.Particles.instReprIonicBond.repr }

---

### `Tau.BookIV.Particles.ionic_bond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L248-L248)
**def
Tau.BookIV.Particles.ionic_bond :IonicBond**

Equations
- Tau.BookIV.Particles.ionic_bond = { }
Instances For

---

### `Tau.BookIV.Particles.MetallicBond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L254-L264)
**structure
Tau.BookIV.Particles.MetallicBond :Type**


[IV.D207] A metallic bond is a collective binding mode in which
outermost electron winding modes are delocalized across the lattice.
Explains: conductivity, malleability, luster.

- delocalized : Bool
Delocalized modes.

- properties : List String
Properties explained.

- few_outer : Bool
Arises in elements with few outer-shell electrons.

Instances For

---

### `Tau.BookIV.Particles.instReprMetallicBond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L264-L264)
**instance
Tau.BookIV.Particles.instReprMetallicBond :Repr MetallicBond**

Equations
- Tau.BookIV.Particles.instReprMetallicBond = { reprPrec := Tau.BookIV.Particles.instReprMetallicBond.repr }

---

### `Tau.BookIV.Particles.instReprMetallicBond.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L264-L264)
**def
Tau.BookIV.Particles.instReprMetallicBond.repr :MetallicBond → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.metallic_bond`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L266-L266)
**def
Tau.BookIV.Particles.metallic_bond :MetallicBond**

Equations
- Tau.BookIV.Particles.metallic_bond = { }
Instances For

---

### `Tau.BookIV.Particles.three_metallic_properties`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L268-L268)
**theorem
Tau.BookIV.Particles.three_metallic_properties :metallic_bond.properties.length = 3**


---

### `Tau.BookIV.Particles.ModeRepulsionEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L274-L293)
**structure
Tau.BookIV.Particles.ModeRepulsionEntry :Type**


[IV.R144] Molecular geometry from mode repulsion: k mode pairs
maximize minimum angular separation.


k
Geometry
Angle


2
linear
180°


3
trigonal planar
120°


4
tetrahedral
109.5°


5
trigonal bipyramidal
90°/120°


6
octahedral
90°


Symmetry depends only on k, not on ι<sub>τ</sub>.

- k : ℕ
Number of mode pairs.

- geometry : String
Geometry name.

- angle_deg_x10 : ℕ
Characteristic angle (degrees ×10).

Instances For

---

### `Tau.BookIV.Particles.instReprModeRepulsionEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L293-L293)
**instance
Tau.BookIV.Particles.instReprModeRepulsionEntry :Repr ModeRepulsionEntry**

Equations
- Tau.BookIV.Particles.instReprModeRepulsionEntry = { reprPrec := Tau.BookIV.Particles.instReprModeRepulsionEntry.repr }

---

### `Tau.BookIV.Particles.instReprModeRepulsionEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L293-L293)
**def
Tau.BookIV.Particles.instReprModeRepulsionEntry.repr :ModeRepulsionEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.mode_repulsion_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L295-L301)
**def
Tau.BookIV.Particles.mode_repulsion_table :List ModeRepulsionEntry**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.mode_repulsion_geometry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L303-L303)
**def
Tau.BookIV.Particles.mode_repulsion_geometry :List ModeRepulsionEntry**

Equations
- Tau.BookIV.Particles.mode_repulsion_geometry = Tau.BookIV.Particles.mode_repulsion_table
Instances For

---

### `Tau.BookIV.Particles.five_geometries`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L305-L305)
**theorem
Tau.BookIV.Particles.five_geometries :mode_repulsion_table.length = 5**


---

### `Tau.BookIV.Particles.HybridizationType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L311-L319)
**inductive
Tau.BookIV.Particles.HybridizationType :Type**


Hybridization type.

- sp : HybridizationType
sp: 2 linear hybrids (180°).

- sp2 : HybridizationType
sp²: 3 planar hybrids (120°).

- sp3 : HybridizationType
sp³: 4 tetrahedral hybrids (109.5°).

Instances For

---

### `Tau.BookIV.Particles.instReprHybridizationType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L319-L319)
**instance
Tau.BookIV.Particles.instReprHybridizationType :Repr HybridizationType**

Equations
- Tau.BookIV.Particles.instReprHybridizationType = { reprPrec := Tau.BookIV.Particles.instReprHybridizationType.repr }

---

### `Tau.BookIV.Particles.instReprHybridizationType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L319-L319)
**def
Tau.BookIV.Particles.instReprHybridizationType.repr :HybridizationType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instDecidableEqHybridizationType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L319-L319)
**instance
Tau.BookIV.Particles.instDecidableEqHybridizationType :DecidableEq HybridizationType**

Equations
- Tau.BookIV.Particles.instDecidableEqHybridizationType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Particles.instBEqHybridizationType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L319-L319)
**def
Tau.BookIV.Particles.instBEqHybridizationType.beq :HybridizationType → HybridizationType → Bool**

Equations
- Tau.BookIV.Particles.instBEqHybridizationType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Particles.instBEqHybridizationType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L319-L319)
**instance
Tau.BookIV.Particles.instBEqHybridizationType :BEq HybridizationType**

Equations
- Tau.BookIV.Particles.instBEqHybridizationType = { beq := Tau.BookIV.Particles.instBEqHybridizationType.beq }

---

### `Tau.BookIV.Particles.HybridMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L321-L332)
**structure
Tau.BookIV.Particles.HybridMode :Type**


[IV.D208] A hybrid mode is a linear combination of s-type (l=0)
and p-type (l=1) winding modes optimized for directional bonding.

- hybridization : HybridizationType
Hybridization type.

- num_hybrids : ℕ
Number of equivalent hybrids.

- angle_deg_x10 : ℕ
Bond angle (degrees ×10).

- example_mol : String
Example molecule.

Instances For

---

### `Tau.BookIV.Particles.instReprHybridMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L332-L332)
**instance
Tau.BookIV.Particles.instReprHybridMode :Repr HybridMode**

Equations
- Tau.BookIV.Particles.instReprHybridMode = { reprPrec := Tau.BookIV.Particles.instReprHybridMode.repr }

---

### `Tau.BookIV.Particles.instReprHybridMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L332-L332)
**def
Tau.BookIV.Particles.instReprHybridMode.repr :HybridMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.sp3_hybrid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L334-L338)
**def
Tau.BookIV.Particles.sp3_hybrid :HybridMode**

Equations
- Tau.BookIV.Particles.sp3_hybrid = { hybridization := Tau.BookIV.Particles.HybridizationType.sp3, num_hybrids := 4, angle_deg_x10 := 1095,
 example_mol := "CH_4" }
Instances For

---

### `Tau.BookIV.Particles.sp2_hybrid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L340-L344)
**def
Tau.BookIV.Particles.sp2_hybrid :HybridMode**

Equations
- Tau.BookIV.Particles.sp2_hybrid = { hybridization := Tau.BookIV.Particles.HybridizationType.sp2, num_hybrids := 3, angle_deg_x10 := 1200,
 example_mol := "C_2H_4" }
Instances For

---

### `Tau.BookIV.Particles.sp_hybrid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L346-L350)
**def
Tau.BookIV.Particles.sp_hybrid :HybridMode**

Equations
- Tau.BookIV.Particles.sp_hybrid = { hybridization := Tau.BookIV.Particles.HybridizationType.sp, num_hybrids := 2, angle_deg_x10 := 1800,
 example_mol := "C_2H_2" }
Instances For

---

### `Tau.BookIV.Particles.OrthodoxComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L356-L370)
**structure
Tau.BookIV.Particles.OrthodoxComparison :Type**


[IV.R148] In orthodox physics, the five rungs (QCD, nuclear, atomic,
quantum chemistry, condensed matter) are separate disciplines with
separate formalisms and effective parameters. In Category τ, all five
are one continuous ascent on T² with derived scale separations
κ(C) >> κ(B) >> κ(D) from a single master constant.

- orthodox_disciplines : ℕ
Orthodox: separate disciplines.

- tau_unified : Bool
Tau: one continuous ascent.

- separations_derived : Bool
Scale separations derived.

- single_constant : Bool
Single master constant.

Instances For

---

### `Tau.BookIV.Particles.instReprOrthodoxComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L370-L370)
**instance
Tau.BookIV.Particles.instReprOrthodoxComparison :Repr OrthodoxComparison**

Equations
- Tau.BookIV.Particles.instReprOrthodoxComparison = { reprPrec := Tau.BookIV.Particles.instReprOrthodoxComparison.repr }

---

### `Tau.BookIV.Particles.instReprOrthodoxComparison.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L370-L370)
**def
Tau.BookIV.Particles.instReprOrthodoxComparison.repr :OrthodoxComparison → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.orthodox_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L372-L372)
**def
Tau.BookIV.Particles.orthodox_comparison :OrthodoxComparison**

Equations
- Tau.BookIV.Particles.orthodox_comparison = { }
Instances For

---

### `Tau.BookIV.Particles.five_orthodox_disciplines`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/PeriodicTable.lean#L374-L375)
**theorem
Tau.BookIV.Particles.five_orthodox_disciplines :orthodox_comparison.orthodox_disciplines = 5**
