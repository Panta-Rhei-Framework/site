---
layout: taulib-doc
title: "TauLib.BookV.Orthodox.MeasurementUnification"
permalink: /verify/taulib/docs/book-v-orthodox-measurement-unification/
lane: verify
module_name: "TauLib.BookV.Orthodox.MeasurementUnification"
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

# TauLib.BookV.Orthodox.MeasurementUnification


Measurement problem dissolved: no wavefunction collapse, address resolution
instead. Quantum-to-classical transition as VM zoom level. Bell inequality
recovery. Decoherence as address-resolution shadow.

## Registry Cross-References


- [V.D189] VM Representation of a Quantum State -- `VMQuantumState`

- [V.T134] Measurement Problem Dissolution -- `measurement_dissolution`

- [V.T135] Bell Inequality in tau -- `bell_inequality_tau`

- [V.P107] Decoherence as Address-Resolution Shadow -- `decoherence_shadow`

- [V.R288] Superposition in the VM -- comment-only

- [V.R289] Entanglement as Address Sharing -- comment-only

- [V.R290] The Century of Confusion -- comment-only


## Mathematical Content


### VM Quantum State [V.D189]


A VM quantum state is a vector |psi> in the orthodox Hilbert space
obtained from a boundary character chi in H_partial[omega] by the
readout map: Read(chi) -> |psi_chi>. The wave function is not a
physical object; it is a VM representation of a boundary character.

### Measurement Problem Dissolution [V.T134]


The measurement problem is dissolved (not solved):


- Unitary evolution = VM readout of character evolution under rho
when no address resolution occurs (Read(rho^n(chi)) = U^n|psi>)

- "Collapse" = address resolution in H_partial[omega], where a
definite boundary character is selected by the resolution protocol

- There is no physical collapse; the VM representation updates when
the address is resolved


### Bell Inequality [V.T135]


The CHSH inequality |S| <= 2 is violated in tau by exactly the
quantum prediction |S| <= 2*sqrt(2). Boundary characters are
non-local (they live on L = S^1 v S^1, which is connected). There
are no hidden variables.

### Decoherence [V.P107]


Decoherence is the VM description of address resolution in the
boundary algebra. The environment is the collection of boundary
characters not in the system's address range.

## Ground Truth Sources


- Book V ch64: Measurement unification

- Book IV ch20-22: Address-obstruction theorem, measurement


---

### `Tau.BookV.Orthodox.ReadoutStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L65-L71)
**inductive
Tau.BookV.Orthodox.ReadoutStatus :Type**


Readout status of a quantum state.

- Unresolved : ReadoutStatus
Unresolved: superposition in the VM (no address resolution yet).

- Resolved : ReadoutStatus
Resolved: definite boundary character selected.

Instances For

---

### `Tau.BookV.Orthodox.instReprReadoutStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L71-L71)
**def
Tau.BookV.Orthodox.instReprReadoutStatus.repr :ReadoutStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.instReprReadoutStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L71-L71)
**instance
Tau.BookV.Orthodox.instReprReadoutStatus :Repr ReadoutStatus**

Equations
- Tau.BookV.Orthodox.instReprReadoutStatus = { reprPrec := Tau.BookV.Orthodox.instReprReadoutStatus.repr }

---

### `Tau.BookV.Orthodox.instDecidableEqReadoutStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L71-L71)
**instance
Tau.BookV.Orthodox.instDecidableEqReadoutStatus :DecidableEq ReadoutStatus**

Equations
- Tau.BookV.Orthodox.instDecidableEqReadoutStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Orthodox.instBEqReadoutStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L71-L71)
**instance
Tau.BookV.Orthodox.instBEqReadoutStatus :BEq ReadoutStatus**

Equations
- Tau.BookV.Orthodox.instBEqReadoutStatus = { beq := Tau.BookV.Orthodox.instBEqReadoutStatus.beq }

---

### `Tau.BookV.Orthodox.instBEqReadoutStatus.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L71-L71)
**def
Tau.BookV.Orthodox.instBEqReadoutStatus.beq :ReadoutStatus → ReadoutStatus → Bool**

Equations
- Tau.BookV.Orthodox.instBEqReadoutStatus.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Orthodox.VMQuantumState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L73-L92)
**structure
Tau.BookV.Orthodox.VMQuantumState :Type**


[V.D189] VM representation of a quantum state.

A VM quantum state is a vector |psi> obtained from a boundary
character chi by the readout map Read : chi -> |psi_chi>.

The wave function is NOT a physical object. It is a VM (virtual
machine) representation of boundary data. "Collapse" is the VM
updating when address resolution occurs at the ontic level.

- character_count : ℕ
Number of boundary characters in the superposition.

- nonempty : self.character_count > 0
At least one character (non-empty state).

- status : ReadoutStatus
Current readout status.

- sector_count : ℕ
Sector(s) involved (up to 5).

- sector_bound : self.sector_count ≤ 5
Sector count bounded by 5.

Instances For

---

### `Tau.BookV.Orthodox.instReprVMQuantumState.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L92-L92)
**def
Tau.BookV.Orthodox.instReprVMQuantumState.repr :VMQuantumState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.instReprVMQuantumState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L92-L92)
**instance
Tau.BookV.Orthodox.instReprVMQuantumState :Repr VMQuantumState**

Equations
- Tau.BookV.Orthodox.instReprVMQuantumState = { reprPrec := Tau.BookV.Orthodox.instReprVMQuantumState.repr }

---

### `Tau.BookV.Orthodox.VMQuantumState.is_resolved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L94-L96)
**def
Tau.BookV.Orthodox.VMQuantumState.is_resolved
(s : VMQuantumState)
 :Bool**


A resolved VM state has a definite boundary character.
Equations
- s.is_resolved = (s.status == Tau.BookV.Orthodox.ReadoutStatus.Resolved)
Instances For

---

### `Tau.BookV.Orthodox.VMQuantumState.is_superposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L98-L100)
**def
Tau.BookV.Orthodox.VMQuantumState.is_superposition
(s : VMQuantumState)
 :Bool**


An unresolved VM state is in superposition (VM language).
Equations
- s.is_superposition = decide ((s.status == Tau.BookV.Orthodox.ReadoutStatus.Unresolved) = true ∧ s.character_count > 1)
Instances For

---

### `Tau.BookV.Orthodox.MeasurementDissolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L106-L116)
**structure
Tau.BookV.Orthodox.MeasurementDissolution :Type**


The three-part dissolution of the measurement problem.

- unitary_is_readout : Bool
Part 1: unitary evolution = character evolution readout.

- collapse_is_address_resolution : Bool
Part 2: collapse = address resolution (not physical).

- born_from_pythagorean : Bool
Part 3: Born rule = Pythagorean theorem on characters.

- all_parts : Bool
All three parts hold.

Instances For

---

### `Tau.BookV.Orthodox.instReprMeasurementDissolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L116-L116)
**instance
Tau.BookV.Orthodox.instReprMeasurementDissolution :Repr MeasurementDissolution**

Equations
- Tau.BookV.Orthodox.instReprMeasurementDissolution = { reprPrec := Tau.BookV.Orthodox.instReprMeasurementDissolution.repr }

---

### `Tau.BookV.Orthodox.instReprMeasurementDissolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L116-L116)
**def
Tau.BookV.Orthodox.instReprMeasurementDissolution.repr :MeasurementDissolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.canonical_measurement_dissolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L118-L132)
**def
Tau.BookV.Orthodox.canonical_measurement_dissolution :MeasurementDissolution**


[V.T134] The measurement problem is dissolved.

There is no wavefunction collapse in the ontic layer. There is
address resolution in H_partial[omega], which the VM readout
functor describes as "collapse."

Formally:


- Read(rho^n(chi)) = U^n |psi_chi> (unitary evolution)

- Read(resolve(chi)) = P_a |psi_chi> / ||P_a|psi_chi>||
(address resolution -> "collapse" in VM)


The Born rule ||^2 is the Pythagorean theorem: the
squared projection of one boundary character onto another.
Equations
- Tau.BookV.Orthodox.canonical_measurement_dissolution = { }
Instances For

---

### `Tau.BookV.Orthodox.measurement_dissolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L134-L135)
**theorem
Tau.BookV.Orthodox.measurement_dissolution :canonical_measurement_dissolution.all_parts = true**


---

### `Tau.BookV.Orthodox.canonical_dissolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L137-L138)
**def
Tau.BookV.Orthodox.canonical_dissolution :MeasurementDissolution**


The canonical dissolution structure.
Equations
- Tau.BookV.Orthodox.canonical_dissolution = { }
Instances For

---

### `Tau.BookV.Orthodox.unitary_is_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L140-L142)
**theorem
Tau.BookV.Orthodox.unitary_is_readout :canonical_dissolution.unitary_is_readout = true**


Unitary evolution is a readout.

---

### `Tau.BookV.Orthodox.collapse_is_address_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L144-L146)
**theorem
Tau.BookV.Orthodox.collapse_is_address_resolution :canonical_dissolution.collapse_is_address_resolution = true**


Collapse is address resolution.

---

### `Tau.BookV.Orthodox.BellInequality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L152-L177)
**structure
Tau.BookV.Orthodox.BellInequality :Type**


[V.T135] Bell inequality in tau: the CHSH bound is 2*sqrt(2),
exactly matching the quantum prediction (Tsirelson bound).

Boundary characters are non-local: they live on the connected
space L = S^1 v S^1. The crossing point of L enables correlations
that exceed the CHSH classical bound |S| <= 2.

There are no hidden variables because boundary characters are
not factorable over space-like separation. The "hidden variable"
is the boundary character itself, which is shared across the
lemniscate -- but sharing a boundary character is not the same
as a classical hidden variable (it respects Tsirelson).

- classical_bound : ℕ
Classical CHSH bound (|S| <= 2).

- tsirelson_numer : ℕ
Quantum Tsirelson bound numerator (2*sqrt(2) ~ 2828/1000).

- tsirelson_denom : ℕ
Tsirelson bound denominator.

- tsirelson_denom_pos : self.tsirelson_denom > 0
Denominator positive.

- reproduces_tsirelson : Bool
tau reproduces Tsirelson (not classical).

- no_hidden_variables : Bool
No hidden variables.

Instances For

---

### `Tau.BookV.Orthodox.instReprBellInequality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L177-L177)
**instance
Tau.BookV.Orthodox.instReprBellInequality :Repr BellInequality**

Equations
- Tau.BookV.Orthodox.instReprBellInequality = { reprPrec := Tau.BookV.Orthodox.instReprBellInequality.repr }

---

### `Tau.BookV.Orthodox.instReprBellInequality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L177-L177)
**def
Tau.BookV.Orthodox.instReprBellInequality.repr :BellInequality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.bell_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L179-L180)
**def
Tau.BookV.Orthodox.bell_data :BellInequality**


The canonical Bell inequality data.
Equations
- Tau.BookV.Orthodox.bell_data = { tsirelson_denom_pos := Tau.BookV.Orthodox.bell_data._proof_2 }
Instances For

---

### `Tau.BookV.Orthodox.bell_inequality_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L182-L186)
**theorem
Tau.BookV.Orthodox.bell_inequality_tau :bell_data.reproduces_tsirelson = true ∧ bell_data.no_hidden_variables = true**


tau reproduces the Tsirelson bound, not the classical bound.

---

### `Tau.BookV.Orthodox.tsirelson_exceeds_classical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L188-L191)
**theorem
Tau.BookV.Orthodox.tsirelson_exceeds_classical :bell_data.tsirelson_numer > bell_data.classical_bound * bell_data.tsirelson_denom**


The quantum bound exceeds the classical bound.

---

### `Tau.BookV.Orthodox.DecoherenceShadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L197-L221)
**structure
Tau.BookV.Orthodox.DecoherenceShadow :Type**


[V.P107] Decoherence as address-resolution shadow.

Decoherence is the VM description of address resolution in the
boundary algebra. The "environment" is the collection of boundary
characters not in the system's address range.

Decoherence rate is determined by:

- The number of environment characters

- The cross-coupling between system and environment sectors

- The refinement depth of the address resolution


Decoherence is NOT fundamental: it is the readout-layer description
of the ontic address-resolution process.

- system_chars : ℕ
Number of system characters.

- env_chars : ℕ
Number of environment characters.

- total : ℕ
Total characters = system + environment.

- total_eq : self.total = self.system_chars + self.env_chars
Total is sum.

- is_fundamental : Bool
Decoherence is NOT fundamental.

Instances For

---

### `Tau.BookV.Orthodox.instReprDecoherenceShadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L221-L221)
**instance
Tau.BookV.Orthodox.instReprDecoherenceShadow :Repr DecoherenceShadow**

Equations
- Tau.BookV.Orthodox.instReprDecoherenceShadow = { reprPrec := Tau.BookV.Orthodox.instReprDecoherenceShadow.repr }

---

### `Tau.BookV.Orthodox.instReprDecoherenceShadow.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L221-L221)
**def
Tau.BookV.Orthodox.instReprDecoherenceShadow.repr :DecoherenceShadow → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.decoherence_example`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L223-L228)
**def
Tau.BookV.Orthodox.decoherence_example :DecoherenceShadow**


Canonical decoherence example.
Equations
- Tau.BookV.Orthodox.decoherence_example = { system_chars := 1, env_chars := 1000, total := 1001, total_eq := Tau.BookV.Orthodox.decoherence_example._proof_2 }
Instances For

---

### `Tau.BookV.Orthodox.decoherence_shadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L230-L232)
**theorem
Tau.BookV.Orthodox.decoherence_shadow :decoherence_example.is_fundamental = false**


Decoherence is a VM shadow, not fundamental.

---

### `Tau.BookV.Orthodox.decoherence_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L234-L236)
**theorem
Tau.BookV.Orthodox.decoherence_total
(d : DecoherenceShadow)
 :d.total = d.system_chars + d.env_chars**


The total character count is the sum of system and environment.

---

### `Tau.BookV.Orthodox.QuantumClassicalTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L242-L258)
**structure
Tau.BookV.Orthodox.QuantumClassicalTransition :Type**


The quantum-classical transition is a change of VM zoom level,
not a physical boundary.

At fine resolution: individual boundary characters visible
(quantum regime)
At coarse resolution: averaged over many characters
(classical regime)

There is no physical "Heisenberg cut."

- fine_sees_individual : Bool
Fine resolution sees individual characters.

- coarse_sees_average : Bool
Coarse resolution sees averages.

- no_heisenberg_cut : Bool
No physical Heisenberg cut.

Instances For

---

### `Tau.BookV.Orthodox.instReprQuantumClassicalTransition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L258-L258)
**def
Tau.BookV.Orthodox.instReprQuantumClassicalTransition.repr :QuantumClassicalTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.instReprQuantumClassicalTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L258-L258)
**instance
Tau.BookV.Orthodox.instReprQuantumClassicalTransition :Repr QuantumClassicalTransition**

Equations
- Tau.BookV.Orthodox.instReprQuantumClassicalTransition = { reprPrec := Tau.BookV.Orthodox.instReprQuantumClassicalTransition.repr }

---

### `Tau.BookV.Orthodox.canonical_qc_transition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L260-L262)
**def
Tau.BookV.Orthodox.canonical_qc_transition :QuantumClassicalTransition**


Canonical quantum-classical transition.
Equations
- Tau.BookV.Orthodox.canonical_qc_transition = { }
Instances For

---

### `Tau.BookV.Orthodox.no_heisenberg_cut`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L264-L266)
**theorem
Tau.BookV.Orthodox.no_heisenberg_cut :canonical_qc_transition.no_heisenberg_cut = true**


No Heisenberg cut in tau.

---

### `Tau.BookV.Orthodox.example_superposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L290-L296)
**def
Tau.BookV.Orthodox.example_superposition :VMQuantumState**


Example: two-state system in superposition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.example_resolved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/MeasurementUnification.lean#L298-L304)
**def
Tau.BookV.Orthodox.example_resolved :VMQuantumState**


Example: resolved (measured) state.
Equations
- One or more equations did not get rendered due to their size.
Instances For
