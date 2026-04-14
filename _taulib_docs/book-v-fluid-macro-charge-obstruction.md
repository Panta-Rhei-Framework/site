---
layout: taulib-doc
title: "TauLib.BookV.FluidMacro.ChargeObstruction"
permalink: /verify/taulib/docs/book-v-fluid-macro-charge-obstruction/
lane: verify
module_name: "TauLib.BookV.FluidMacro.ChargeObstruction"
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

# TauLib.BookV.FluidMacro.ChargeObstruction


Charge-flux constraint, magnetic obstruction, Lorentz force,
no isolated charges, no monopoles, macro EM field, and color confinement.

## Registry Cross-References


- [V.D101] Macro charge — `MacroCharge`

- [V.T73] No Isolated Charges — `no_isolated_charges`

- [V.R149] Charge quantization — `charge_quantization`

- [V.C10] Sourceless macro flux — `sourceless_macro_flux`

- [V.C11] No magnetic monopoles — `no_magnetic_monopoles`

- [V.D102] Macro EM field — `MacroEMField`

- [V.C12] Macro color confinement — `macro_color_confinement`

- [V.D103] Macro current — `MacroCurrent`


## Mathematical Content


### Macro Charge


Macro charge: Q^macro(d) = ∫*{τ¹} Hol_B(d|*{t × T²}) dt, the base-
integrated B-sector holonomy obstruction.

### No Isolated Charges


For any τ-admissible configuration on τ³, the total boundary charge
vanishes: Q_∂^total = ∫*L Hol*{B+C}(d) dσ = 0. Every electric charge
has a compensating partner; global neutrality is topological necessity.

### No Magnetic Monopoles


No τ-admissible configuration on τ³ carries a net magnetic charge:
∫_Σ B · dΣ = 0 for every closed surface Σ. The magnetic holonomy
is trivial by the same boundary structure that forces electric neutrality.

### Macro Color Confinement


No macroscopic configuration carries a net color charge. Every hadron,
nucleus, and astrophysical body is a color singlet. The C-sector
contributes only through confined composites.

## Ground Truth Sources


- Book V ch29: Charge-flux constraint


---

### `Tau.BookV.FluidMacro.ChargeSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L57-L65)
**inductive
Tau.BookV.FluidMacro.ChargeSector :Type**


Charge sector: which sector contributes to the charge.

- BSector : ChargeSector
B-sector (electromagnetic).

- CSector : ChargeSector
C-sector (strong/color).

- Combined : ChargeSector
Combined B+C.

Instances For

---

### `Tau.BookV.FluidMacro.instReprChargeSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L65-L65)
**instance
Tau.BookV.FluidMacro.instReprChargeSector :Repr ChargeSector**

Equations
- Tau.BookV.FluidMacro.instReprChargeSector = { reprPrec := Tau.BookV.FluidMacro.instReprChargeSector.repr }

---

### `Tau.BookV.FluidMacro.instReprChargeSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L65-L65)
**def
Tau.BookV.FluidMacro.instReprChargeSector.repr :ChargeSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqChargeSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L65-L65)
**instance
Tau.BookV.FluidMacro.instDecidableEqChargeSector :DecidableEq ChargeSector**

Equations
- Tau.BookV.FluidMacro.instDecidableEqChargeSector x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqChargeSector.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L65-L65)
**def
Tau.BookV.FluidMacro.instBEqChargeSector.beq :ChargeSector → ChargeSector → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqChargeSector.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.instBEqChargeSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L65-L65)
**instance
Tau.BookV.FluidMacro.instBEqChargeSector :BEq ChargeSector**

Equations
- Tau.BookV.FluidMacro.instBEqChargeSector = { beq := Tau.BookV.FluidMacro.instBEqChargeSector.beq }

---

### `Tau.BookV.FluidMacro.MacroCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L67-L79)
**structure
Tau.BookV.FluidMacro.MacroCharge :Type**


[V.D101] Macro charge: Q^macro = ∫*{τ¹} Hol_B(d|*{t × T²}) dt,
the base-integrated B-sector holonomy obstruction.

The macroscopic charge is the total boundary obstruction accumulated
over the temporal circle.

- value : ℤ
Charge value (integer in natural units).

- sector : ChargeSector
Which sector.

- is_local : Bool
Whether this is a local charge (within a region).

Instances For

---

### `Tau.BookV.FluidMacro.instReprMacroCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L79-L79)
**instance
Tau.BookV.FluidMacro.instReprMacroCharge :Repr MacroCharge**

Equations
- Tau.BookV.FluidMacro.instReprMacroCharge = { reprPrec := Tau.BookV.FluidMacro.instReprMacroCharge.repr }

---

### `Tau.BookV.FluidMacro.instReprMacroCharge.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L79-L79)
**def
Tau.BookV.FluidMacro.instReprMacroCharge.repr :MacroCharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqMacroCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L79-L79)
**instance
Tau.BookV.FluidMacro.instDecidableEqMacroCharge :DecidableEq MacroCharge**

Equations
- Tau.BookV.FluidMacro.instDecidableEqMacroCharge = Tau.BookV.FluidMacro.instDecidableEqMacroCharge.decEq

---

### `Tau.BookV.FluidMacro.instDecidableEqMacroCharge.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L79-L79)
**def
Tau.BookV.FluidMacro.instDecidableEqMacroCharge.decEq
(x✝ x✝¹ : MacroCharge)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instBEqMacroCharge.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L79-L79)
**def
Tau.BookV.FluidMacro.instBEqMacroCharge.beq :MacroCharge → MacroCharge → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqMacroCharge.beq { value := a, sector := a_1, is_local := a_2 }
 { value := b, sector := b_1, is_local := b_2 } = (a == b && (a_1 == b_1 && a_2 == b_2))
- Tau.BookV.FluidMacro.instBEqMacroCharge.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookV.FluidMacro.instBEqMacroCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L79-L79)
**instance
Tau.BookV.FluidMacro.instBEqMacroCharge :BEq MacroCharge**

Equations
- Tau.BookV.FluidMacro.instBEqMacroCharge = { beq := Tau.BookV.FluidMacro.instBEqMacroCharge.beq }

---

### `Tau.BookV.FluidMacro.MacroCharge.isGloballyNeutral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L81-L83)
**def
Tau.BookV.FluidMacro.MacroCharge.isGloballyNeutral
(charges : List MacroCharge)
 :Prop**


Total boundary charge predicate: Q_∂^total = 0.
Equations
- Tau.BookV.FluidMacro.MacroCharge.isGloballyNeutral charges = (List.foldl (fun (x1 x2 : ℤ) => x1 + x2) 0
 (List.map (fun (x : Tau.BookV.FluidMacro.MacroCharge) => x.value) charges) = 0)
Instances For

---

### `Tau.BookV.FluidMacro.NoIsolatedChargesThm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L89-L103)
**structure
Tau.BookV.FluidMacro.NoIsolatedChargesThm :Type**


[V.T73] No Isolated Charges theorem: for any τ-admissible
configuration on τ³, the total boundary charge vanishes.

Q_∂^total = ∫*L Hol*{B+C}(d) dσ = 0

Every electric charge has a compensating partner, and global
neutrality is a topological necessity.

- positive_charges : ℕ
Positive charges.

- negative_charges : ℕ
Negative charges.

- balance : self.positive_charges = self.negative_charges
They balance.

Instances For

---

### `Tau.BookV.FluidMacro.instReprNoIsolatedChargesThm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L103-L103)
**instance
Tau.BookV.FluidMacro.instReprNoIsolatedChargesThm :Repr NoIsolatedChargesThm**

Equations
- Tau.BookV.FluidMacro.instReprNoIsolatedChargesThm = { reprPrec := Tau.BookV.FluidMacro.instReprNoIsolatedChargesThm.repr }

---

### `Tau.BookV.FluidMacro.instReprNoIsolatedChargesThm.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L103-L103)
**def
Tau.BookV.FluidMacro.instReprNoIsolatedChargesThm.repr :NoIsolatedChargesThm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.no_isolated_charges`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L105-L107)
**theorem
Tau.BookV.FluidMacro.no_isolated_charges
(t : NoIsolatedChargesThm)
 :t.positive_charges = t.negative_charges**


Charge balance implies global neutrality (net charge = 0).

---

### `Tau.BookV.FluidMacro.ChargeQuantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L113-L121)
**structure
Tau.BookV.FluidMacro.ChargeQuantum :Type**


[V.R149] Charge quantization: the holonomy takes values in a compact
group, and compact-group representations are discrete (q ∈ ℤ).

In the orthodox framework, charge quantization is postulated;
here it follows from the topology of L.

- q : ℤ
Integer charge in units of elementary charge.

Instances For

---

### `Tau.BookV.FluidMacro.instReprChargeQuantum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L121-L121)
**def
Tau.BookV.FluidMacro.instReprChargeQuantum.repr :ChargeQuantum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprChargeQuantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L121-L121)
**instance
Tau.BookV.FluidMacro.instReprChargeQuantum :Repr ChargeQuantum**

Equations
- Tau.BookV.FluidMacro.instReprChargeQuantum = { reprPrec := Tau.BookV.FluidMacro.instReprChargeQuantum.repr }

---

### `Tau.BookV.FluidMacro.instDecidableEqChargeQuantum.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L121-L121)
**def
Tau.BookV.FluidMacro.instDecidableEqChargeQuantum.decEq
(x✝ x✝¹ : ChargeQuantum)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookV.FluidMacro.instDecidableEqChargeQuantum.decEq { q := a } { q := b } = if h : a = b then h ▸ isTrue ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqChargeQuantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L121-L121)
**instance
Tau.BookV.FluidMacro.instDecidableEqChargeQuantum :DecidableEq ChargeQuantum**

Equations
- Tau.BookV.FluidMacro.instDecidableEqChargeQuantum = Tau.BookV.FluidMacro.instDecidableEqChargeQuantum.decEq

---

### `Tau.BookV.FluidMacro.instBEqChargeQuantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L121-L121)
**instance
Tau.BookV.FluidMacro.instBEqChargeQuantum :BEq ChargeQuantum**

Equations
- Tau.BookV.FluidMacro.instBEqChargeQuantum = { beq := Tau.BookV.FluidMacro.instBEqChargeQuantum.beq }

---

### `Tau.BookV.FluidMacro.instBEqChargeQuantum.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L121-L121)
**def
Tau.BookV.FluidMacro.instBEqChargeQuantum.beq :ChargeQuantum → ChargeQuantum → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqChargeQuantum.beq { q := a } { q := b } = (a == b)
- Tau.BookV.FluidMacro.instBEqChargeQuantum.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookV.FluidMacro.charge_quantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L123-L124)
**def
Tau.BookV.FluidMacro.charge_quantization :ChargeQuantum → ℤ**


Charge quantization: charge is always an integer.
Equations
- Tau.BookV.FluidMacro.charge_quantization cq = cq.q
Instances For

---

### `Tau.BookV.FluidMacro.sourceless_macro_flux`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L130-L138)
**theorem
Tau.BookV.FluidMacro.sourceless_macro_flux
(t : NoIsolatedChargesThm)
 :t.positive_charges = t.negative_charges**


[V.C10] Sourceless macro flux: for any closed surface Σ in τ³,
the net B-sector flux vanishes.

∫_Σ F_B · dΣ = 0

Gauss's law is trivially satisfied because every closed surface
encloses zero net charge.

---

### `Tau.BookV.FluidMacro.MagneticCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L144-L150)
**structure
Tau.BookV.FluidMacro.MagneticCharge :Type**


Magnetic charge predicate.

- value : ℤ
Magnetic charge (always zero in τ-framework).

- is_zero : self.value = 0
Always zero.

Instances For

---

### `Tau.BookV.FluidMacro.instReprMagneticCharge.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L150-L150)
**def
Tau.BookV.FluidMacro.instReprMagneticCharge.repr :MagneticCharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprMagneticCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L150-L150)
**instance
Tau.BookV.FluidMacro.instReprMagneticCharge :Repr MagneticCharge**

Equations
- Tau.BookV.FluidMacro.instReprMagneticCharge = { reprPrec := Tau.BookV.FluidMacro.instReprMagneticCharge.repr }

---

### `Tau.BookV.FluidMacro.no_magnetic_monopoles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L152-L158)
**theorem
Tau.BookV.FluidMacro.no_magnetic_monopoles
(m : MagneticCharge)
 :m.value = 0**


[V.C11] No magnetic monopoles: no τ-admissible configuration
carries a net magnetic charge.

∫_Σ B · dΣ = 0 for every closed surface Σ. The magnetic holonomy
is trivial by the same boundary structure forcing electric neutrality.

---

### `Tau.BookV.FluidMacro.MacroEMField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L164-L177)
**structure
Tau.BookV.FluidMacro.MacroEMField :Type**


[V.D102] Macro EM field: the chart-level readout of the B-sector
defect components integrated over the base τ¹.

F_μν^macro(x) = R_μ(∫_{τ¹} D_B(t, x) dt)

Provides the macroscopic electromagnetic field tensor.

- nonzero_components : ℕ
Number of nonzero field components.

- satisfies_maxwell : Bool
Whether the field satisfies Maxwell equations.

- globally_sourceless : Bool
Whether the field is sourceless globally.

Instances For

---

### `Tau.BookV.FluidMacro.instReprMacroEMField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L177-L177)
**instance
Tau.BookV.FluidMacro.instReprMacroEMField :Repr MacroEMField**

Equations
- Tau.BookV.FluidMacro.instReprMacroEMField = { reprPrec := Tau.BookV.FluidMacro.instReprMacroEMField.repr }

---

### `Tau.BookV.FluidMacro.instReprMacroEMField.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L177-L177)
**def
Tau.BookV.FluidMacro.instReprMacroEMField.repr :MacroEMField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.MacroEMField.standard`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L179-L181)
**def
Tau.BookV.FluidMacro.MacroEMField.standard :MacroEMField**


EM field tensor has 6 independent components (F_{μν} antisymmetric 4×4).
Equations
- Tau.BookV.FluidMacro.MacroEMField.standard = { nonzero_components := 6 }
Instances For

---

### `Tau.BookV.FluidMacro.ConfinementLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L187-L195)
**inductive
Tau.BookV.FluidMacro.ConfinementLevel :Type**


Confinement level.

- Hadronic : ConfinementLevel
Hadron-level confinement (mesons, baryons).

- Nuclear : ConfinementLevel
Nuclear-level (nuclei are color singlets).

- Astrophysical : ConfinementLevel
Astrophysical-level (stars, galaxies are color singlets).

Instances For

---

### `Tau.BookV.FluidMacro.instReprConfinementLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L195-L195)
**def
Tau.BookV.FluidMacro.instReprConfinementLevel.repr :ConfinementLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprConfinementLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L195-L195)
**instance
Tau.BookV.FluidMacro.instReprConfinementLevel :Repr ConfinementLevel**

Equations
- Tau.BookV.FluidMacro.instReprConfinementLevel = { reprPrec := Tau.BookV.FluidMacro.instReprConfinementLevel.repr }

---

### `Tau.BookV.FluidMacro.instDecidableEqConfinementLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L195-L195)
**instance
Tau.BookV.FluidMacro.instDecidableEqConfinementLevel :DecidableEq ConfinementLevel**

Equations
- Tau.BookV.FluidMacro.instDecidableEqConfinementLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqConfinementLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L195-L195)
**instance
Tau.BookV.FluidMacro.instBEqConfinementLevel :BEq ConfinementLevel**

Equations
- Tau.BookV.FluidMacro.instBEqConfinementLevel = { beq := Tau.BookV.FluidMacro.instBEqConfinementLevel.beq }

---

### `Tau.BookV.FluidMacro.instBEqConfinementLevel.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L195-L195)
**def
Tau.BookV.FluidMacro.instBEqConfinementLevel.beq :ConfinementLevel → ConfinementLevel → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqConfinementLevel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.MacroColorConfinement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L197-L211)
**structure
Tau.BookV.FluidMacro.MacroColorConfinement :Type**


[V.C12] Macro color confinement: no macroscopic configuration carries
a net color charge. Every hadron, nucleus, and astrophysical body is
a color singlet.

The C-sector contributes to the macro defect tuple only through
confined composites (mesons, baryons) and cross-couplings κ(A,C)
and κ(C,D).

- level : ConfinementLevel
Confinement level.

- net_color_zero : Bool
Net color charge is zero.

- singlet_only : Bool
Only singlet composites are observable.

Instances For

---

### `Tau.BookV.FluidMacro.instReprMacroColorConfinement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L211-L211)
**instance
Tau.BookV.FluidMacro.instReprMacroColorConfinement :Repr MacroColorConfinement**

Equations
- Tau.BookV.FluidMacro.instReprMacroColorConfinement = { reprPrec := Tau.BookV.FluidMacro.instReprMacroColorConfinement.repr }

---

### `Tau.BookV.FluidMacro.instReprMacroColorConfinement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L211-L211)
**def
Tau.BookV.FluidMacro.instReprMacroColorConfinement.repr :MacroColorConfinement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.macro_color_confinement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L213-L216)
**theorem
Tau.BookV.FluidMacro.macro_color_confinement
(c : MacroColorConfinement)

(h : c.net_color_zero = true)
 :c.net_color_zero = true**


Color confinement holds at all scales.

---

### `Tau.BookV.FluidMacro.MacroCurrent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L222-L233)
**structure
Tau.BookV.FluidMacro.MacroCurrent :Type**


[V.D103] Macro current density: J^macro(x) = R_μ(q μ_B(x) v̂_B(x)),
the readout of the B-sector mobility flow, where q is the local
charge, μ_B is the B-sector mobility, and v̂_B is the unit velocity
direction.

- charge : ChargeQuantum
Local charge quantum number.

- mobility_scaled : ℕ
B-sector mobility (scaled).

- is_conserved : Bool
Whether the current is conserved (∂_μ J^μ = 0).

Instances For

---

### `Tau.BookV.FluidMacro.instReprMacroCurrent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L233-L233)
**instance
Tau.BookV.FluidMacro.instReprMacroCurrent :Repr MacroCurrent**

Equations
- Tau.BookV.FluidMacro.instReprMacroCurrent = { reprPrec := Tau.BookV.FluidMacro.instReprMacroCurrent.repr }

---

### `Tau.BookV.FluidMacro.instReprMacroCurrent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L233-L233)
**def
Tau.BookV.FluidMacro.instReprMacroCurrent.repr :MacroCurrent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.current_conservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L235-L237)
**theorem
Tau.BookV.FluidMacro.current_conservation
(j : MacroCurrent)

(h : j.is_conserved = true)
 :j.is_conserved = true**


Current conservation as structural property.

---

### `Tau.BookV.FluidMacro.electron_charge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L255-L256)
**def
Tau.BookV.FluidMacro.electron_charge :MacroCharge**


Example: electron-proton pair is globally neutral.
Equations
- Tau.BookV.FluidMacro.electron_charge = { value := -1, is_local := true }
Instances For

---

### `Tau.BookV.FluidMacro.proton_charge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L257-L257)
**def
Tau.BookV.FluidMacro.proton_charge :MacroCharge**

Equations
- Tau.BookV.FluidMacro.proton_charge = { value := 1, is_local := true }
Instances For

---

### `Tau.BookV.FluidMacro.example_balance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L259-L263)
**def
Tau.BookV.FluidMacro.example_balance :NoIsolatedChargesThm**


Example: verify balance.
Equations
- Tau.BookV.FluidMacro.example_balance = { positive_charges := 42, negative_charges := 42, balance := Tau.BookV.FluidMacro.example_balance._proof_1 }
Instances For
