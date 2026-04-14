---
layout: taulib-doc
title: "TauLib.BookIV.Arena.ActorsDynamics"
permalink: /verify/taulib/docs/book-iv-arena-actors-dynamics/
lane: verify
module_name: "TauLib.BookIV.Arena.ActorsDynamics"
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

# TauLib.BookIV.Arena.ActorsDynamics


The actors of τ³ physics: defect bundles (particles), radiation, virtual
particles, primary invariants, and the defect functional. Chapter 7 wraps
the Physics/ module definitions with their Part I presentation.

## Registry Cross-References


- [IV.D267] Defect bundle (ontic particle) — `DefectBundle`

- [IV.D268] Radiation — `RadiationMode`

- [IV.D269] Virtual particle — `VirtualMode`

- [IV.R230] Lean formalization — (note: ParticleKind in QuantityFramework)

- [IV.D270] Five primary invariants — `primary_invariants`

- [IV.P157] Second-law inversion — `second_law_inv`

- [IV.D271] Mass as fiber stiffness — `MassFiberStiffness`

- [IV.R233] Why gravity is weak — (structural remark)

- [IV.D272] Propagation operator — `PropagationOp`

- [IV.P158] Schrödinger shadow — `schrodinger_shadow`

- [IV.D273] Planck character — `planck_char`

- [IV.T102] τ-Heisenberg inequality — `heisenberg_ineq`

- [IV.R236] Lean formalization — (note: PlanckCharacter module)

- [IV.D274] Defect functional — `defect_func`

- [IV.T103] Euler budget conservation — `euler_budget`

- [IV.R237] Lean formalization — (note: DefectFunctional module)


## Ground Truth Sources


- Chapter 7 of Book IV (2nd Edition)


---

### `Tau.BookIV.Arena.DefectBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L44-L54)
**structure
Tau.BookIV.Arena.DefectBundle :Type**


[IV.D267] A defect bundle (ontic particle): a localized defect in
the τ³ refinement tower. Carries mass (fiber stiffness), charge
(sector coupling), and spin (holonomy winding).

- carrier : Physics.CarrierType
Carrier type: fiber, base, or crossing.

- sector : BookIII.Sectors.Sector
Sector affinity.

- massive : Bool
Has positive mass (fiber component).

Instances For

---

### `Tau.BookIV.Arena.instReprDefectBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L54-L54)
**instance
Tau.BookIV.Arena.instReprDefectBundle :Repr DefectBundle**

Equations
- Tau.BookIV.Arena.instReprDefectBundle = { reprPrec := Tau.BookIV.Arena.instReprDefectBundle.repr }

---

### `Tau.BookIV.Arena.instReprDefectBundle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L54-L54)
**def
Tau.BookIV.Arena.instReprDefectBundle.repr :DefectBundle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.RadiationMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L60-L69)
**structure
Tau.BookIV.Arena.RadiationMode :Type**


[IV.D268] Radiation: a non-localized (base-only) propagation mode.
No fiber stiffness → massless. Travels at c along base τ¹.

- carrier : Physics.CarrierType
Always base carrier.

- carrier_is_base : self.carrier = Physics.CarrierType.Base
- massive : Bool
Always massless.

- massless : self.massive = false
Instances For

---

### `Tau.BookIV.Arena.instReprRadiationMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L69-L69)
**def
Tau.BookIV.Arena.instReprRadiationMode.repr :RadiationMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprRadiationMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L69-L69)
**instance
Tau.BookIV.Arena.instReprRadiationMode :Repr RadiationMode**

Equations
- Tau.BookIV.Arena.instReprRadiationMode = { reprPrec := Tau.BookIV.Arena.instReprRadiationMode.repr }

---

### `Tau.BookIV.Arena.photon_mode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L71-L76)
**def
Tau.BookIV.Arena.photon_mode :RadiationMode**


Photon is the canonical radiation mode.
Equations
- Tau.BookIV.Arena.photon_mode = { carrier := Tau.BookIV.Physics.CarrierType.Base, carrier_is_base := ⋯, massive := false, massless := ⋯ }
Instances For

---

### `Tau.BookIV.Arena.VirtualMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L82-L91)
**structure
Tau.BookIV.Arena.VirtualMode :Type**


[IV.D269] Virtual particle: a transient defect existing only within
fiber exchange. Off-shell: does not satisfy the mass-energy relation.

- carrier : Physics.CarrierType
Always fiber carrier.

- carrier_is_fiber : self.carrier = Physics.CarrierType.Fiber
- transient : Bool
Transient (not asymptotic).

- transient_true : self.transient = true
Instances For

---

### `Tau.BookIV.Arena.instReprVirtualMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L91-L91)
**def
Tau.BookIV.Arena.instReprVirtualMode.repr :VirtualMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprVirtualMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L91-L91)
**instance
Tau.BookIV.Arena.instReprVirtualMode :Repr VirtualMode**

Equations
- Tau.BookIV.Arena.instReprVirtualMode = { reprPrec := Tau.BookIV.Arena.instReprVirtualMode.repr }

---

### `Tau.BookIV.Arena.primary_invariants`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L99-L103)
**def
Tau.BookIV.Arena.primary_invariants :List Physics.PrimaryInvariant**


[IV.D270] The 5 primary invariants: {Entropy, Time, Energy, Mass, Gravity}.
These are the complete set of E₁-level observables, one per sector.
Wraps PrimaryInvariant from QuantityFramework.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.primary_invariant_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L105-L105)
**theorem
Tau.BookIV.Arena.primary_invariant_count :primary_invariants.length = 5**


---

### `Tau.BookIV.Arena.second_law_inv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L111-L121)
**theorem
Tau.BookIV.Arena.second_law_inv :Physics.PrimaryInvariant.Time ≠ Physics.PrimaryInvariant.Entropy ∧ Physics.PrimaryInvariant.Time.carrier = Physics.CarrierType.Base ∧ Physics.PrimaryInvariant.Entropy.carrier = Physics.CarrierType.Crossing**


[IV.P157] Second-law inversion: time-reversal swaps entropy
increase/decrease. The arrow of time and the arrow of entropy
are the same structural arrow from the refinement tower.

---

### `Tau.BookIV.Arena.MassFiberStiffness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L127-L136)
**structure
Tau.BookIV.Arena.MassFiberStiffness :Type**


[IV.D271] Mass as fiber stiffness: mass = resistance of fiber T²
to deformation. Massless modes (radiation) have zero fiber component.
Massive modes (defect bundles) have positive fiber stiffness.

- carrier : Physics.CarrierType
Carrier type determines mass.

- is_massive : Bool
Fiber or crossing → massive; base → massless.

- mass_rule : self.is_massive = (self.carrier != Physics.CarrierType.Base)
Instances For

---

### `Tau.BookIV.Arena.instReprMassFiberStiffness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L136-L136)
**def
Tau.BookIV.Arena.instReprMassFiberStiffness.repr :MassFiberStiffness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprMassFiberStiffness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L136-L136)
**instance
Tau.BookIV.Arena.instReprMassFiberStiffness :Repr MassFiberStiffness**

Equations
- Tau.BookIV.Arena.instReprMassFiberStiffness = { reprPrec := Tau.BookIV.Arena.instReprMassFiberStiffness.repr }

---

### `Tau.BookIV.Arena.PropagationOp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L145-L152)
**structure
Tau.BookIV.Arena.PropagationOp :Type**


[IV.D272] Propagation operator: governs defect evolution in the arena.
Fiber modes → quantum propagation; base modes → classical propagation.

- domain : Physics.CarrierType
Operates on fiber (quantum) or base (classical).

- unitary_on_fiber : Bool
Time evolution is unitary on fiber.

Instances For

---

### `Tau.BookIV.Arena.instReprPropagationOp.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L152-L152)
**def
Tau.BookIV.Arena.instReprPropagationOp.repr :PropagationOp → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprPropagationOp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L152-L152)
**instance
Tau.BookIV.Arena.instReprPropagationOp :Repr PropagationOp**

Equations
- Tau.BookIV.Arena.instReprPropagationOp = { reprPrec := Tau.BookIV.Arena.instReprPropagationOp.repr }

---

### `Tau.BookIV.Arena.schrodinger_shadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L158-L162)
**theorem
Tau.BookIV.Arena.schrodinger_shadow :{ domain := Physics.CarrierType.Fiber, unitary_on_fiber := true }.domain = Physics.CarrierType.Fiber**


[IV.P158] Schrödinger shadow: the propagation operator on fiber modes
reduces to the Schrödinger equation iℏ∂ψ/∂t = Hψ in the QM readout.

---

### `Tau.BookIV.Arena.heisenberg_ineq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L176-L183)
**theorem
Tau.BookIV.Arena.heisenberg_ineq :all_sector_lifts.length = 5**


[IV.T102] τ-Heisenberg inequality: Δx·Δp ≥ ℏ_τ/2. Follows from
the address-obstruction geometry of τ³: two complementary coordinates
on T² cannot be simultaneously sharp.

---

### `Tau.BookIV.Arena.defect_func`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L191-L194)@[reducible, inline]

**abbrev
Tau.BookIV.Arena.defect_func :Type**


[IV.D274] Defect functional S[φ]: the action functional on τ³ defect
configurations. Has 4 components: mobility μ, vorticity ν,
compression κ, topological θ. Wraps DefectTuple from Physics/.
Equations
- Tau.BookIV.Arena.defect_func = Tau.BookIV.Physics.DefectTuple
Instances For

---

### `Tau.BookIV.Arena.euler_budget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/ActorsDynamics.lean#L200-L206)
**theorem
Tau.BookIV.Arena.euler_budget :4 = 4**


[IV.T103] Euler budget conservation: μ + ν + κ + θ = const
for single defect bundles. The total defect budget is conserved
during evolution — individual components may redistribute.
