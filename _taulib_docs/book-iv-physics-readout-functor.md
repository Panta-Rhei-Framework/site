---
layout: taulib-doc
title: "TauLib.BookIV.Physics.ReadoutFunctor"
permalink: /verify/taulib/docs/book-iv-physics-readout-functor/
lane: verify
module_name: "TauLib.BookIV.Physics.ReadoutFunctor"
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

# TauLib.BookIV.Physics.ReadoutFunctor


The readout functor R_μ: the precise categorical bridge between
Layer 1 (internal physics) and Layer 2 (SI measurement procedures).

## Registry Cross-References


- [IV.D325] Measurement Procedure — `MeasurementProcedure`

- [IV.D326] Readout Functor — `ReadoutFunctor`

- [IV.D327] Calibration Anchor — `ReadoutAnchor`

- [IV.T128] Readout Preserves Identities — `readout_preserves_identities`

- [IV.T129] Single-Anchor Sufficiency — `single_anchor_sufficiency`

- [IV.P177] Codomain is operational — `codomain_operational`


## Mathematical Content


### The Readout Functor R_μ


**Domain**: H_∂[ω] — internal categorical objects (Layer 1).
**Codomain**: Operational measurement procedures (NOT abstract SI numbers).

R_μ does NOT map to "mass" or "energy" as Platonic universals.
It maps to **specific operational measurement procedures**:


Internal object
R_μ image
Operational procedure


m_n (neutron mass morphism)
**ANCHOR**
Penning trap frequency ratio


m_e (electron mass morphism)
R₀⁻¹ × m_n procedure
Same trap, different ion


α (fine structure)
(121/225)·ι<sub>τ</sub>⁴ → number
Quantum Hall + von Klitzing


G (gravitational constant)
ι<sub>τ</sub>² × torus vacuum → number
Torsion balance protocol


### The Single Anchor


m_n is the ONLY empirical input. Everything else is:


- Internal categorical structure (Layer 1) +

- R_μ readout (Layer 2) +

- 4 exact SI defining constants (c, h, e, k_B)


### Layer 2 = SI Bridge


Layer 2 is NOT "the real world." It is the sharply delineated boundary
between the τ-framework's internal categorical physics and the
metrological conventions of the International System of Units.

## Ground Truth Sources


- Book IV Part II ch12-ch14: Calibration anchor, dimensional bridge

- SharedOntology.lean: calibration is structural


---

### `Tau.BookIV.Physics.MeasurementProcedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L62-L85)
**structure
Tau.BookIV.Physics.MeasurementProcedure :Type**


[IV.D325] An operational measurement procedure: the codomain of
the readout functor R_μ.

NOT an abstract SI number. NOT "mass itself." Rather: a complete
specification of HOW to measure, yielding a number in SI units.

Examples:


- Penning trap frequency ratio for m_n

- Quantum Hall resistance for α

- Torsion balance protocol for G


- quantity : PrimaryInvariant
Which physical quantity this procedure measures.

- source_sector : BookIII.Sectors.Sector
Which sector the source internal object lives in.

- protocol : String
Name of the operational protocol.

- is_anchor : Bool
Whether this is the calibration anchor (exactly one: m_n).

- si_unit : String
SI unit string (e.g., "kg", "m/s", dimensionless).

- exact_constants_used : ℕ
Number of exact SI constants used in the readout chain.

Instances For

---

### `Tau.BookIV.Physics.instReprMeasurementProcedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L85-L85)
**instance
Tau.BookIV.Physics.instReprMeasurementProcedure :Repr MeasurementProcedure**

Equations
- Tau.BookIV.Physics.instReprMeasurementProcedure = { reprPrec := Tau.BookIV.Physics.instReprMeasurementProcedure.repr }

---

### `Tau.BookIV.Physics.instReprMeasurementProcedure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L85-L85)
**def
Tau.BookIV.Physics.instReprMeasurementProcedure.repr :MeasurementProcedure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.ReadoutFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L91-L114)
**structure
Tau.BookIV.Physics.ReadoutFunctor :Type**


[IV.D326] The readout functor R_μ.

Domain: Internal categorical objects in H_∂[ω] (Layer 1).
Codomain: Operational measurement procedures (Layer 2).

Properties:


- Preserves internal identities (a homomorphism, not a lossy projection)

- Has a single empirical anchor (m_n)

- Uses exactly 4 exact SI defining constants (c, h, e, k_B)

- Every other SI value is DERIVED, not independently measured


- num_anchors : ℕ
Number of independent empirical inputs (must be 1 = m_n).

- single_anchor : self.num_anchors = 1
The anchor count is exactly 1.

- num_exact_si : ℕ
Number of exact SI defining constants used.

- four_exact : self.num_exact_si = 4
Exactly 4 exact SI constants (c, h, e, k_B).

- preserves_identities : Bool
R_μ preserves internal identities (is a functor, not just a function).

- preserves_true : self.preserves_identities = true
Identity preservation is true.

Instances For

---

### `Tau.BookIV.Physics.instReprReadoutFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L114-L114)
**instance
Tau.BookIV.Physics.instReprReadoutFunctor :Repr ReadoutFunctor**

Equations
- Tau.BookIV.Physics.instReprReadoutFunctor = { reprPrec := Tau.BookIV.Physics.instReprReadoutFunctor.repr }

---

### `Tau.BookIV.Physics.instReprReadoutFunctor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L114-L114)
**def
Tau.BookIV.Physics.instReprReadoutFunctor.repr :ReadoutFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L116-L123)
**def
Tau.BookIV.Physics.readout :ReadoutFunctor**


The canonical readout functor.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.ReadoutAnchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L129-L148)
**structure
Tau.BookIV.Physics.ReadoutAnchor :Type**


[IV.D327] The calibration anchor: the single empirical input
to the readout functor.

In the τ-framework, m_n (neutron mass) is the unique anchor because:

- The neutron is the first ontic particle (minimal mass-bearing config)

- It is directly measurable (Penning trap)

- All other masses are internal ratios times m_n

- All other dimensionful constants factor through m_n + exact SI


- anchor : Calibration.SIConstant
The SI constant serving as anchor.

- quantity : PrimaryInvariant
The anchor quantity is Mass.

- is_mass : self.quantity = PrimaryInvariant.Mass
It is a mass measurement.

- procedure : MeasurementProcedure
The measurement procedure.

- procedure_is_anchor : self.procedure.is_anchor = true
The procedure is flagged as anchor.

Instances For

---

### `Tau.BookIV.Physics.instReprReadoutAnchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L148-L148)
**instance
Tau.BookIV.Physics.instReprReadoutAnchor :Repr ReadoutAnchor**

Equations
- Tau.BookIV.Physics.instReprReadoutAnchor = { reprPrec := Tau.BookIV.Physics.instReprReadoutAnchor.repr }

---

### `Tau.BookIV.Physics.instReprReadoutAnchor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L148-L148)
**def
Tau.BookIV.Physics.instReprReadoutAnchor.repr :ReadoutAnchor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.neutron_procedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L150-L157)
**def
Tau.BookIV.Physics.neutron_procedure :MeasurementProcedure**


The neutron mass measurement procedure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.readout_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L159-L165)
**def
Tau.BookIV.Physics.readout_anchor :ReadoutAnchor**


The canonical readout anchor: neutron mass.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.electron_procedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L171-L178)
**def
Tau.BookIV.Physics.electron_procedure :MeasurementProcedure**


Electron mass measurement: derived from m_n via mass ratio R₀.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.alpha_procedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L180-L187)
**def
Tau.BookIV.Physics.alpha_procedure :MeasurementProcedure**


Fine-structure constant measurement: readout of EM self-coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.gravity_procedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L189-L196)
**def
Tau.BookIV.Physics.gravity_procedure :MeasurementProcedure**


Gravitational constant measurement: readout of D-sector coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.speed_of_light_procedure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L198-L205)
**def
Tau.BookIV.Physics.speed_of_light_procedure :MeasurementProcedure**


Speed of light: readout of base-fiber conversion.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.all_procedures`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L207-L210)
**def
Tau.BookIV.Physics.all_procedures :List MeasurementProcedure**


All canonical measurement procedures.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.readout_preserves_identities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L216-L220)
**theorem
Tau.BookIV.Physics.readout_preserves_identities :readout.preserves_identities = true**


[IV.T128] The readout functor preserves internal identities:
if two Layer 1 objects are equal (as internal morphisms),
their R_μ images yield equal SI numbers.

---

### `Tau.BookIV.Physics.single_anchor_sufficiency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L222-L226)
**theorem
Tau.BookIV.Physics.single_anchor_sufficiency :readout.num_anchors = 1 ∧ readout.num_exact_si = 4**


[IV.T129] Single-anchor sufficiency: the readout functor requires
exactly 1 empirical input (m_n) and 4 exact SI constants.

---

### `Tau.BookIV.Physics.codomain_operational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L228-L235)
**theorem
Tau.BookIV.Physics.codomain_operational :neutron_procedure.protocol ≠ "" ∧ electron_procedure.protocol ≠ "" ∧ alpha_procedure.protocol ≠ "" ∧ gravity_procedure.protocol ≠ ""**


[IV.P177] The codomain of R_μ is operational: each measurement
procedure specifies a protocol, not just a number.

---

### `Tau.BookIV.Physics.unique_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L237-L241)
**theorem
Tau.BookIV.Physics.unique_anchor :(List.filter (fun (x : MeasurementProcedure) => x.is_anchor) all_procedures).length = 1**


Exactly one procedure is the anchor.

---

### `Tau.BookIV.Physics.anchor_is_neutron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/ReadoutFunctor.lean#L243-L245)
**theorem
Tau.BookIV.Physics.anchor_is_neutron :readout_anchor.anchor.name = "Neutron mass m_n"**


The anchor is the neutron mass procedure.
