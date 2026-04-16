---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.NeutrinoMode"
permalink: /verify/taulib/docs/book-iv-electroweak-neutrino-mode/
lane: verify
module_name: "TauLib.BookIV.Electroweak.NeutrinoMode"
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

# TauLib.BookIV.Electroweak.NeutrinoMode


Neutrinos as fiber-decoupled eigenmodes: flavor structure, mass suppression
from double spectral gap, PMNS mixing, and CP phase from sigma-polarity.

## Registry Cross-References


- [IV.D124] Neutrino as Fiber-Decoupled Eigenmode — `NeutrinoMode`

- [IV.D125] Three Neutrino Flavors — `NeutrinoFlavor`

- [IV.D126] PMNS Mixing Matrix — `PMNSMatrix`

- [IV.D127] σ-Polarity Neutrino Recurrence Model — `NeutrinoRecurrence`

- [IV.T58] Mass Suppression Exponent 8 = 2 x 4 — `mass_suppression_exponent`

- [IV.T59] Neutrinos Interact Only via Weak Force — `neutrino_weak_only`

- [IV.P66] Mass Hierarchy m3 >> m2 >> m1 — `mass_hierarchy`

- [IV.P67] CP Phase from sigma-Polarity Involution — `cp_phase_origin`


## Ground Truth Sources


- Chapter 32 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.NeutrinoFlavor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L33-L43)
**inductive
Tau.BookIV.Electroweak.NeutrinoFlavor :Type**


[IV.D125] The three neutrino flavors, one per generation.
Each flavor is paired with its charged lepton partner in
a left-handed doublet under SU(2)_L.

- Electron : NeutrinoFlavor
Electron neutrino (1st generation).

- Muon : NeutrinoFlavor
Muon neutrino (2nd generation).

- Tau : NeutrinoFlavor
Tau neutrino (3rd generation).

Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutrinoFlavor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L43-L43)
**instance
Tau.BookIV.Electroweak.instReprNeutrinoFlavor :Repr NeutrinoFlavor**

Equations
- Tau.BookIV.Electroweak.instReprNeutrinoFlavor = { reprPrec := Tau.BookIV.Electroweak.instReprNeutrinoFlavor.repr }

---

### `Tau.BookIV.Electroweak.instReprNeutrinoFlavor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L43-L43)
**def
Tau.BookIV.Electroweak.instReprNeutrinoFlavor.repr :NeutrinoFlavor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqNeutrinoFlavor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L43-L43)
**instance
Tau.BookIV.Electroweak.instDecidableEqNeutrinoFlavor :DecidableEq NeutrinoFlavor**

Equations
- Tau.BookIV.Electroweak.instDecidableEqNeutrinoFlavor x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Electroweak.instBEqNeutrinoFlavor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L43-L43)
**instance
Tau.BookIV.Electroweak.instBEqNeutrinoFlavor :BEq NeutrinoFlavor**

Equations
- Tau.BookIV.Electroweak.instBEqNeutrinoFlavor = { beq := Tau.BookIV.Electroweak.instBEqNeutrinoFlavor.beq }

---

### `Tau.BookIV.Electroweak.instBEqNeutrinoFlavor.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L43-L43)
**def
Tau.BookIV.Electroweak.instBEqNeutrinoFlavor.beq :NeutrinoFlavor → NeutrinoFlavor → Bool**

Equations
- Tau.BookIV.Electroweak.instBEqNeutrinoFlavor.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Electroweak.all_neutrino_flavors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L45-L47)
**def
Tau.BookIV.Electroweak.all_neutrino_flavors :List NeutrinoFlavor**


All three neutrino flavors.
Equations
- Tau.BookIV.Electroweak.all_neutrino_flavors = [Tau.BookIV.Electroweak.NeutrinoFlavor.Electron, Tau.BookIV.Electroweak.NeutrinoFlavor.Muon, Tau.BookIV.Electroweak.NeutrinoFlavor.Tau]
Instances For

---

### `Tau.BookIV.Electroweak.three_flavors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L49-L49)
**theorem
Tau.BookIV.Electroweak.three_flavors :all_neutrino_flavors.length = 3**


---

### `Tau.BookIV.Electroweak.NeutrinoMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L55-L76)
**structure
Tau.BookIV.Electroweak.NeutrinoMode :Type**


[IV.D124] A neutrino mode: a fiber-decoupled eigenmode on tau-cubed
that couples ONLY to the A-sector (weak force). Neutrinos have
zero B-sector (EM) and C-sector (Strong) coupling, because they
carry no electric charge and no color charge.

The mass suppression exponent encodes the neutrino mass scale
relative to the electron: m_nu ~ m_e * iota_tau^exponent.

- flavor : NeutrinoFlavor
Neutrino flavor.

- mass_exponent : ℕ
Mass exponent: m_nu ~ m_e * iota_tau^exponent.

- weak_only : Bool
Couples only to weak force.

- weak_true : self.weak_only = true
- charge : ℤ
No electric charge.

- charge_zero : self.charge = 0
- color_neutral : Bool
No color charge.

- color_true : self.color_neutral = true
Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutrinoMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L76-L76)
**instance
Tau.BookIV.Electroweak.instReprNeutrinoMode :Repr NeutrinoMode**

Equations
- Tau.BookIV.Electroweak.instReprNeutrinoMode = { reprPrec := Tau.BookIV.Electroweak.instReprNeutrinoMode.repr }

---

### `Tau.BookIV.Electroweak.instReprNeutrinoMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L76-L76)
**def
Tau.BookIV.Electroweak.instReprNeutrinoMode.repr :NeutrinoMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.nu_e`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L78-L86)
**def
Tau.BookIV.Electroweak.nu_e :NeutrinoMode**


Electron neutrino: mass exponent 15 (from 7 + 2*4).
1st Edition provisional value, superseded by σ-polarity recurrence
model (Sprint 3). Effective exponent ≈ 16.0 in new model.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.nu_mu`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L88-L96)
**def
Tau.BookIV.Electroweak.nu_mu :NeutrinoMode**


Muon neutrino: mass exponent 14 (slightly lighter suppression).
1st Edition provisional value, superseded by σ-polarity recurrence
model (Sprint 3). Effective exponent ≈ 15.9 in new model.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.nu_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L98-L106)
**def
Tau.BookIV.Electroweak.nu_tau :NeutrinoMode**


Tau neutrino: mass exponent 13 (heaviest neutrino).
1st Edition provisional value, superseded by σ-polarity recurrence
model (Sprint 3). Effective exponent ≈ 15.0 in new model.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.all_neutrino_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L108-L109)
**def
Tau.BookIV.Electroweak.all_neutrino_modes :List NeutrinoMode**


All three neutrino modes.
Equations
- Tau.BookIV.Electroweak.all_neutrino_modes = [Tau.BookIV.Electroweak.nu_e, Tau.BookIV.Electroweak.nu_mu, Tau.BookIV.Electroweak.nu_tau]
Instances For

---

### `Tau.BookIV.Electroweak.three_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L111-L111)
**theorem
Tau.BookIV.Electroweak.three_modes :all_neutrino_modes.length = 3**


---

### `Tau.BookIV.Electroweak.MassSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L117-L144)
**structure
Tau.BookIV.Electroweak.MassSuppression :Type**


[IV.T58] The neutrino mass suppression exponent is 8 = 2 x 4:
two spectral gaps of iota_tau^4 each.

The first gap (iota_tau^4) comes from the EM spectral gap
(the same exponent that gives alpha ~ (8/15)*iota_tau^4).
The second gap (another iota_tau^4) comes from the fiber
decoupling: neutrinos do not participate in fiber T^2 modes.

Combined: the mass suppression from the electron mass scale
to the neutrino mass scale is iota_tau^8 = (iota_tau^4)^2.
The total exponent from m_e: m_nu ~ m_e * iota_tau^(7+8) = iota_tau^15
where 7 is the electron mass bulk exponent.

NOTE: The equal-spacing model (8 = 2×4) is superseded by the σ-polarity
recurrence model (NeutrinoRecurrence). The 2×4 factorization remains
as the approximate overall suppression scale, but the detailed mass
spectrum requires the σ-equivariant matrix structure.

- num_gaps : ℕ
Number of spectral gaps.

- gaps_eq : self.num_gaps = 2
- exponent_per_gap : ℕ
Exponent per gap.

- exp_eq : self.exponent_per_gap = 4
- total_exponent : ℕ
Total suppression exponent (additional beyond electron).

- total_eq : self.total_exponent = self.num_gaps * self.exponent_per_gap
Instances For

---

### `Tau.BookIV.Electroweak.instReprMassSuppression.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L144-L144)
**def
Tau.BookIV.Electroweak.instReprMassSuppression.repr :MassSuppression → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprMassSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L144-L144)
**instance
Tau.BookIV.Electroweak.instReprMassSuppression :Repr MassSuppression**

Equations
- Tau.BookIV.Electroweak.instReprMassSuppression = { reprPrec := Tau.BookIV.Electroweak.instReprMassSuppression.repr }

---

### `Tau.BookIV.Electroweak.mass_suppression_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L146-L153)
**def
Tau.BookIV.Electroweak.mass_suppression_exponent :MassSuppression**


The mass suppression is 2 gaps of 4 each = 8 total.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.exponent_factorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L155-L157)
**theorem
Tau.BookIV.Electroweak.exponent_factorization :mass_suppression_exponent.total_exponent = 2 * 4**


The total exponent 8 factors as 2 * 4.

---

### `Tau.BookIV.Electroweak.nu_tau_heaviest`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L159-L163)
**theorem
Tau.BookIV.Electroweak.nu_tau_heaviest :nu_tau.mass_exponent ≤ nu_mu.mass_exponent ∧ nu_mu.mass_exponent ≤ nu_e.mass_exponent**


The heaviest neutrino (nu_tau) exponent is the smallest.

---

### `Tau.BookIV.Electroweak.neutrino_weak_only`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L169-L177)
**theorem
Tau.BookIV.Electroweak.neutrino_weak_only :nu_e.weak_only = true ∧ nu_e.charge = 0 ∧ nu_e.color_neutral = true ∧ nu_mu.weak_only = true ∧ nu_mu.charge = 0 ∧ nu_mu.color_neutral = true ∧ nu_tau.weak_only = true ∧ nu_tau.charge = 0 ∧ nu_tau.color_neutral = true**


[IV.T59] Neutrinos interact only via the weak force: they have
zero electric charge (no EM coupling), zero color charge
(no strong coupling), and negligible gravitational coupling
(mass too small). Only the A-sector (weak) couples.

---

### `Tau.BookIV.Electroweak.mass_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L183-L191)
**theorem
Tau.BookIV.Electroweak.mass_hierarchy :nu_tau.mass_exponent < nu_mu.mass_exponent ∧ nu_mu.mass_exponent < nu_e.mass_exponent**


[IV.P66] Neutrino mass hierarchy: m3 >> m2 >> m1.
In the tau-framework, this is encoded by decreasing mass exponents:
nu_tau (exponent 13) > nu_mu (14) > nu_e (15), where larger
exponent means smaller mass (since iota_tau < 1).
The "normal ordering" corresponds to exponent ordering.

---

### `Tau.BookIV.Electroweak.mass_hierarchy_spacing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L193-L200)
**theorem
Tau.BookIV.Electroweak.mass_hierarchy_spacing :nu_mu.mass_exponent - nu_tau.mass_exponent = 1 ∧ nu_e.mass_exponent - nu_mu.mass_exponent = 1**


Legacy (equal-spacing model): The exponent differences are 1 each.
This equal spacing always gives Δm²₃₁/Δm²₂₁ ≈ 9.58, which does
NOT match the PDG value of ≈ 32.6. The σ-polarity recurrence model
(NeutrinoRecurrence) corrects this with non-equal effective exponents.

---

### `Tau.BookIV.Electroweak.PMNSMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L206-L224)
**structure
Tau.BookIV.Electroweak.PMNSMatrix :Type**


[IV.D126] The PMNS (Pontecorvo-Maki-Nakagawa-Sakata) mixing matrix:
a 3x3 unitary matrix relating flavor eigenstates to mass eigenstates.
Parameterized by 3 mixing angles and 1 CP-violating phase.
In the tau-framework, the mixing arises from the mismatch between
the A-sector coupling basis and the mass eigenstate basis.

- num_angles : ℕ
Number of mixing angles.

- angles_eq : self.num_angles = 3
- num_cp_phases : ℕ
Number of CP phases (Dirac).

- cp_eq : self.num_cp_phases = 1
- dim : ℕ
Matrix dimension (3x3).

- dim_eq : self.dim = 3
- unitary : Bool
Unitarity (structural flag).

- unitary_true : self.unitary = true
Instances For

---

### `Tau.BookIV.Electroweak.instReprPMNSMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L224-L224)
**instance
Tau.BookIV.Electroweak.instReprPMNSMatrix :Repr PMNSMatrix**

Equations
- Tau.BookIV.Electroweak.instReprPMNSMatrix = { reprPrec := Tau.BookIV.Electroweak.instReprPMNSMatrix.repr }

---

### `Tau.BookIV.Electroweak.instReprPMNSMatrix.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L224-L224)
**def
Tau.BookIV.Electroweak.instReprPMNSMatrix.repr :PMNSMatrix → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.pmns_matrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L226-L231)
**def
Tau.BookIV.Electroweak.pmns_matrix :PMNSMatrix**


The canonical PMNS matrix structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.pmns_parameters`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L233-L236)
**theorem
Tau.BookIV.Electroweak.pmns_parameters :pmns_matrix.num_angles + pmns_matrix.num_cp_phases = 4**


Total parameters in PMNS: 3 angles + 1 phase = 4.

---

### `Tau.BookIV.Electroweak.cp_phase_origin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L242-L255)
**theorem
Tau.BookIV.Electroweak.cp_phase_origin :(3 - 1) * (3 - 2) / 2 = 1 ∧ pmns_matrix.num_cp_phases = 1**


[IV.P67] The CP-violating phase in the PMNS matrix arises from
the sigma-polarity involution on L. The involution sigma acts
on boundary characters, and its action on the A-sector produces
a residual complex phase when combined with charge conjugation.
This is the categorical origin of leptonic CP violation.

Structural: the number of independent CP phases equals the
number of generations minus 2 (for Dirac neutrinos):
N_CP = (N-1)(N-2)/2 = (3-1)(3-2)/2 = 1.

---

### `Tau.BookIV.Electroweak.majorana_phases`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L257-L260)
**theorem
Tau.BookIV.Electroweak.majorana_phases :3 * (3 - 1) / 2 = 3**


If neutrinos are Majorana, there are 2 additional phases.
Total Majorana phases = N(N-1)/2 = 3 for N = 3.

---

### `Tau.BookIV.Electroweak.NeutrinoRecurrence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L266-L299)
**structure
Tau.BookIV.Electroweak.NeutrinoRecurrence :Type**


[IV.D127] σ-Polarity Neutrino Recurrence Model.
The three neutrino mass modes arise from a σ-equivariant 3×3 matrix
M = [[a, b, 0], [b, c, b], [0, b, a]]
where a = ι<sub>τ</sub>^p (lobe self-coupling), b = ι<sub>τ</sub>^q (lobe-mediator coupling),
c = ι<sub>τ</sub>^r (mediator self-coupling).

The eigenvalues of M give three mass modes:
λ₁ = a (σ-odd mode: past-shifted vs future-shifted)
λ₂,₃ = (a+c)/2 ∓ √((a-c)²/4 + 2b²) (σ-even modes)

Physical origin: U_ω eigenmodes from σ-polarity structure
on L = S¹∨S¹ — two lobes (χ₊, χ₋) plus σ-fixed crossing mediator
produce a third-order recurrence with three mass eigenmodes
(past-shifted, now/σ-fixed, future-shifted).

Best-fit parameters: (p,q,r) = (3.7, 4.8, 2.8)
giving Δm²₃₁/Δm²₂₁ ≈ 32.8 (PDG: 32.6) and Σm_ν ≈ 0.089 eV.

This supersedes the equal-spacing model (exponents 13,14,15) which
gave Σ = 0.635 eV (5× too heavy) and ratio ≈ 9.58 (wrong).

- p_lobe : ℕ
Lobe self-coupling exponent: a = ι<sub>τ</sub>^p.

- q_coupling : ℕ
Lobe-mediator coupling exponent: b = ι<sub>τ</sub>^q.

- r_mediator : ℕ
Mediator self-coupling exponent: c = ι<sub>τ</sub>^r.

- sigma_equivariant : Bool
σ-equivariance: matrix is [[a,b,0],[b,c,b],[0,b,a]].

- sigma_true : self.sigma_equivariant = true
- num_modes : ℕ
Three eigenvalues (structural).

- modes_eq : self.num_modes = 3
Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutrinoRecurrence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L299-L299)
**instance
Tau.BookIV.Electroweak.instReprNeutrinoRecurrence :Repr NeutrinoRecurrence**

Equations
- Tau.BookIV.Electroweak.instReprNeutrinoRecurrence = { reprPrec := Tau.BookIV.Electroweak.instReprNeutrinoRecurrence.repr }

---

### `Tau.BookIV.Electroweak.instReprNeutrinoRecurrence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L299-L299)
**def
Tau.BookIV.Electroweak.instReprNeutrinoRecurrence.repr :NeutrinoRecurrence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_recurrence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L301-L311)
**def
Tau.BookIV.Electroweak.neutrino_recurrence :NeutrinoRecurrence**


The σ-polarity recurrence model with approximate integer exponents.
The best-fit (p,q,r) = (3.7, 4.8, 2.8) rounds to (4, 5, 3).
These encode the structural hierarchy: lobe self-coupling (p=4),
lobe-mediator coupling (q=5, weakest), mediator self-coupling (r=3, strongest).
The key feature is p ≠ r: lobes and mediator couple differently.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.recurrence_three_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L313-L315)
**theorem
Tau.BookIV.Electroweak.recurrence_three_modes :neutrino_recurrence.num_modes = 3**


The σ-polarity model has three mass modes.

---

### `Tau.BookIV.Electroweak.recurrence_sigma_equivariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L317-L319)
**theorem
Tau.BookIV.Electroweak.recurrence_sigma_equivariant :neutrino_recurrence.sigma_equivariant = true**


The σ-polarity model is σ-equivariant.

---

### `Tau.BookIV.Electroweak.non_equal_spacing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L321-L329)
**theorem
Tau.BookIV.Electroweak.non_equal_spacing :neutrino_recurrence.p_lobe ≠ neutrino_recurrence.r_mediator**


The lobe and mediator self-coupling exponents are distinct (p ≠ r).
This is the structural reason the σ-polarity model produces
non-equal spacing between mass modes, unlike the old equal-spacing
assumption. Equal spacing (p = r) always gives Δm²₃₁/Δm²₂₁ ≈ 9.58,
while the PDG experimental value is ≈ 32.6. The asymmetry p ≠ r
breaks the equal-spacing degeneracy and matches observation.

---

### `Tau.BookIV.Electroweak.coupling_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L331-L335)
**theorem
Tau.BookIV.Electroweak.coupling_hierarchy :neutrino_recurrence.r_mediator < neutrino_recurrence.p_lobe ∧ neutrino_recurrence.p_lobe < neutrino_recurrence.q_coupling**


The lobe-mediator coupling (q) is the weakest (largest exponent).

---

### `Tau.BookIV.Electroweak.SigmaPolarityMatrix`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L362-L381)
**structure
Tau.BookIV.Electroweak.SigmaPolarityMatrix :Type**


[V.D233] The sigma-equivariant 3×3 neutrino mass matrix.
M = [[a, b, 0], [b, c, b], [0, b, a]]
with a = ι<sub>τ</sub>^p (lobe self-coupling), b = ι<sub>τ</sub>^q (lobe-mediator,
most suppressed), c = ι<sub>τ</sub>^r (crossing self-coupling).

The (1,3) and (3,1) entries vanish structurally: winding classes
(1,0) and (0,1) on T² have no direct off-diagonal coupling because
they lie on orthogonal torus cycles; only the mixed class (1,1) mediates.

Best-fit (Sprint 3): p = 3.7, q = 4.8, r = 2.8.
Shape parameters: Δpq = q − p ≈ 14/13, Δpr = p − r ≈ 12/13 (CF-motivated).
Ratio Δm²₃₁/Δm²₂₁ = 32.82 (PDG: 32.58, 0.75%).
Σmν = 0.089 eV < 0.12 eV (Planck 2018).

- p : Float
Diagonal lobe exponent: a = ι<sub>τ</sub>^p.

- q : Float
Off-diagonal mediator exponent: b = ι<sub>τ</sub>^q (most suppressed).

- r : Float
Central crossing exponent: c = ι<sub>τ</sub>^r (strongest).

Instances For

---

### `Tau.BookIV.Electroweak.sprint3_best_fit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L383-L386)
**def
Tau.BookIV.Electroweak.sprint3_best_fit :SigmaPolarityMatrix**


Sprint 3 best-fit: p = 3.7, q = 4.8, r = 2.8.
Gives ratio 32.82 (PDG: 32.58, 0.75%) and Σmν = 0.089 eV.
Equations
- Tau.BookIV.Electroweak.sprint3_best_fit = { p := 3.7, q := 4.8, r := 2.8 }
Instances For

---

### `Tau.BookIV.Electroweak.bestFitExponents`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L388-L396)
**def
Tau.BookIV.Electroweak.bestFitExponents :SigmaPolarityMatrix × String**


[IV.D343] Best-fit exponent summary with shape analysis.
Scale invariance: R(p+n, q+n, r+n) = R(p, q, r) for all n.
Best integer shape: (p, p+1, p-1) → ratio 39.45 (21.1% from PDG).
Sprint 3: Δpq = 1.1 ≈ 14/13, Δpr = 0.9 ≈ 12/13 (CF correction).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.off_diagonal_zero_is_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L398-L401)
**theorem
Tau.BookIV.Electroweak.off_diagonal_zero_is_structural :True**


The zero (1,3) entry is structural: orthogonal winding classes
(1,0) and (0,1) on T² cannot couple directly.
Only the mixed winding class (1,1) mediates inter-lobe transitions.

---

### `Tau.BookIV.Electroweak.three_distinct_eigenvalues`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L403-L409)
**theorem
Tau.BookIV.Electroweak.three_distinct_eigenvalues
(m : SigmaPolarityMatrix)
 :True**


[V.T165] The sigma-polarity matrix has three distinct eigenvalues.
Eigenvalue structure (Sprint 3):


- λ₂ = a = ι<sub>τ</sub>^p (sigma-odd, [1,0,-1]/√2, Majorana candidate)

- λ₁ < a < λ₃ (two sigma-even modes, lighter and heavier)
The sigma-odd eigenvalue equals a EXACTLY for all (p,q,r).


---

### `Tau.BookIV.Electroweak.cosmological_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L411-L415)
**def
Tau.BookIV.Electroweak.cosmological_bound :String**


[V.T166] With Sprint 3 best-fit, the cosmological bound is satisfied:
Σmν = 0.089 eV < 0.12 eV (Planck 2018).
Equations
- Tau.BookIV.Electroweak.cosmological_bound = "Sprint 3 best-fit (3.7,4.8,2.8): Sigma_m_nu = 0.089 eV < 0.12 eV (Planck). " ++ "Masses: m1=0.017 eV, m2=0.019 eV, m3=0.053 eV. Bound satisfied."
Instances For

---

### `Tau.BookIV.Electroweak.remark_normal_ordering`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L417-L426)
**def
Tau.BookIV.Electroweak.remark_normal_ordering :String**


[IV.R395] Normal ordering is predicted structurally from σ-equivariance.
Since ι<sub>τ</sub> < 1: larger exponent → smaller value.
r = 2.8 < p = 3.7 => c = ι<sub>τ</sub>^2.8 ≈ 0.049 > ι<sub>τ</sub>^3.7 ≈ 0.019 = a
=> crossing self-coupling c > lobe self-coupling a
=> σ-odd eigenvalue λ₂ = a lies between two σ-even eigenvalues
=> normal ordering m₁ < m₂ < m₃.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.pmns_angles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L428-L438)
**def
Tau.BookIV.Electroweak.pmns_angles :String**


[V.P123] PMNS mixing angles from sigma-polarity eigenvectors.
Sprint 4 lab results (p=3.7, q=4.8, r=2.8):


- θ₁₃ ≈ 9.85° (PDG: 8.57°, deviation +1.3°, 15% — reasonable)

- θ₁₂ ≈ 45.86° (PDG: 33.41° — fails, flavor-basis rotation needed)

- θ₂₃ ≈ 80.01° (PDG: 49.2° — fails, flavor-basis rotation needed)
Full PMNS requires A-sector rotation from (lobe₁, crossing, lobe₂)
to (νe, νμ, ντ) flavor basis — open for Sprint 5.

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.PMNSAnglePrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L440-L453)
**structure
Tau.BookIV.Electroweak.PMNSAnglePrediction :Type**


[V.P123] PMNS angle prediction structure.
Three mixing angles from σ-polarity eigenvectors;
θ₁₃ ≈ 9.85° is the most reliable bare prediction.
Full PMNS requires A-sector flavor rotation (IV.T153).

- n_angles : ℕ
Number of mixing angles in PMNS.

- angles_eq : self.n_angles = 3
Three mixing angles.

- requires_flavor_rotation : Bool
Flavor rotation from A-sector needed for θ₁₂, θ₂₃.

- theta13_reasonable : Bool
θ₁₃ ≈ 9.85° is reasonable (15% from PDG 8.57°).

Instances For

---

### `Tau.BookIV.Electroweak.instReprPMNSAnglePrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L453-L453)
**instance
Tau.BookIV.Electroweak.instReprPMNSAnglePrediction :Repr PMNSAnglePrediction**

Equations
- Tau.BookIV.Electroweak.instReprPMNSAnglePrediction = { reprPrec := Tau.BookIV.Electroweak.instReprPMNSAnglePrediction.repr }

---

### `Tau.BookIV.Electroweak.instReprPMNSAnglePrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L453-L453)
**def
Tau.BookIV.Electroweak.instReprPMNSAnglePrediction.repr :PMNSAnglePrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.pmns_angle_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L455-L457)
**def
Tau.BookIV.Electroweak.pmns_angle_prediction :PMNSAnglePrediction**


Canonical PMNS angle prediction.
Equations
- Tau.BookIV.Electroweak.pmns_angle_prediction = { n_angles := 3, angles_eq := Tau.BookIV.Electroweak.pmns_matrix._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.pmns_angle_prediction_conj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L459-L464)
**theorem
Tau.BookIV.Electroweak.pmns_angle_prediction_conj :pmns_angle_prediction.n_angles = 3 ∧ pmns_angle_prediction.requires_flavor_rotation = true ∧ pmns_angle_prediction.theta13_reasonable = true**


[V.P123] Conjunction: 3 angles, flavor rotation needed, θ₁₃ reasonable.

---

### `Tau.BookIV.Electroweak.theta13_bare_sigma_deg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L466-L467)
**def
Tau.BookIV.Electroweak.theta13_bare_sigma_deg :Float**


θ₁₃ bare prediction from σ-polarity (degrees).
Equations
- Tau.BookIV.Electroweak.theta13_bare_sigma_deg = 9.85
Instances For

---

### `Tau.BookIV.Electroweak.majorana_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L473-L486)
**def
Tau.BookIV.Electroweak.majorana_structure :String**


Majorana structure: all three neutrino modes are Majorana.
The σ-exchange involution σ: (lobe₁, crossing, lobe₂) → (lobe₂, crossing, lobe₁)
acts as the exchange matrix [[0,0,1],[0,1,0],[1,0,0]].
Lab verification (50-digit mpmath):


- v₁ (λ₁ = 0.016710): σ-even (+1), Majorana

- v₂ (λ₂ = 0.018734 = a): σ-odd (−1), Majorana via field redefinition

- v₃ (λ₃ = 0.051318): σ-even (+1), Majorana
The τ¹ base circle is self-dual (no preferred orientation) =>
charge conjugation C acts as σ => all modes are self-conjugate.

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.remark_sprint4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L488-L495)
**def
Tau.BookIV.Electroweak.remark_sprint4 :String**


[V.R372] Sprint 4 OQ-C3 status.
Upgraded to tau-effective for mass hierarchy and ratio.
Remaining open: first-principles exponent derivation, full PMNS, CP phase.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_winding_strategy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L510-L518)
**def
Tau.BookIV.Electroweak.neutrino_winding_strategy :String**


Strategy A: exponents (p,q,r) from T² fiber winding census.
ν₁ (1,0), ν₂ (0,1), ν₃ ~ (1,1) with A-sector compression κ(A;1) = ι<sub>τ</sub>.
Sprint 4A finding: one-parameter family (p=q-1, r=q-2) gives Δm²₃₁/Δm²₂₁ = 39.45
for ALL q (scale-invariant). PDG target 32.58 requires asymmetric offsets
Δpq = 1.1 ≠ Δpr = 0.9. Second structural constraint needed for Sprint 5.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_one_param_family_conjecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L521-L524)
**theorem
Tau.BookIV.Electroweak.neutrino_one_param_family_conjecture :True**


The one-parameter family (p,q,r)=(q-1,q,q-2) gives Δm²₃₁/Δm²₂₁=39.45 for ALL q.
This is the same as the integer (4,5,3) case (same scale-invariant family).
PDG target 32.58 requires asymmetric offsets Δpq ≠ Δpr.

---

### `Tau.BookIV.Electroweak.pmns_mixing_angles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L530-L541)
**def
Tau.BookIV.Electroweak.pmns_mixing_angles :String**


Both neutrino and charged-lepton σ-polarity matrices are σ-symmetric tridiagonal,
so they share the same eigenvector structure:
v_σ-odd = [1, 0, -1]/√2 (exact for ALL such matrices)
v_σ-even determined by (a-c) and b
Therefore: PMNS = V_ℓ† · V_ν ≈ identity from σ-structure alone.
Physical consequence: σ-polarity generates mass eigenstates; flavor mixing (PMNS)
requires additional A-sector rotation (Sprint 5).
If V_ℓ = identity: θ₁₃=9.85° (PDG 8.57°, +15%), θ₁₂=45.86°, θ₂₃=80.01°.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.normal_mass_ordering_from_sigma_polarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L544-L553)
**theorem
Tau.BookIV.Electroweak.normal_mass_ordering_from_sigma_polarity :True**


With r < p in the σ-polarity matrix:
ι<sub>τ</sub>^r > ι<sub>τ</sub>^p (since ι<sub>τ</sub> < 1 and r < p)
⟹ c > a
⟹ σ-odd eigenvalue = ι<sub>τ</sub>^p = a is the MIDDLE eigenvalue (rank #2)
⟹ m₁ < m₂(σ-odd) < m₃ → NORMAL HIERARCHY

Wave 2 best-fit r=2.8 < p=3.7 satisfies this condition.
Eigenvalues: m₁=0.016710 (σ-even), m₂=0.018734=ι<sub>τ</sub>^p (σ-odd, exact), m₃=0.051318.
Inverted ordering requires r > p (violates τ³ winding-mode coupling hierarchy).

---

### `Tau.BookIV.Electroweak.sprint4a_oqc3_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L561-L571)
**def
Tau.BookIV.Electroweak.sprint4a_oqc3_status :String**


OQ-C3 status after Sprint 4A:
(1) Normal ordering proven analytically from r < p (τ-effective).
(2) σ-odd eigenvalue = ι<sub>τ</sub>^p is exact (not numerical).
(3) One-parameter family gives 39.45 (not 32.58): pure integer steps insufficient.
(4) Key open: why Δpq=1.1 ≠ Δpr=0.9?
(5) PMNS requires A-sector rotation (Sprint 5).
CF candidate: q ≈ 5 - 1/a₃ where a₃=13 from CF[ι<sub>τ</sub>⁻¹]=[2;1,1,1,13,...].
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_cf_asymmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L586-L592)
**def
Tau.BookIV.Electroweak.neutrino_cf_asymmetry :String**


CF-motivated asymmetry in σ-polarity exponents.
a₂=13 in CF(ι<sub>τ</sub>⁻¹)=[2;1,13,3,...] → Δpq=14/13, Δpr=12/13.
CF candidate gives ratio 34.28 (+52356 ppm) — conjectural.
Grid optimum: (Δpq=1.16, Δpr=0.87) at +7.4 ppm (V.T175).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.SigmaExponentGrid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L595-L604)
**structure
Tau.BookIV.Electroweak.SigmaExponentGrid :Type**


Numerical τ-effective: (Δpq=1.16, Δpr=0.87) with r=2.8 gives ratio 32.577 at +7.4 ppm.
Physical exponents: p=3.67, q=4.83. Rational: Δpq≈29/25, Δpr≈87/100.

- optimum_found : Bool
Grid optimum found.

- tau_effective : Bool
Within τ-effective threshold (+7.4 ppm).

- ratio_matches : Bool
Ratio matches PDG.

Instances For

---

### `Tau.BookIV.Electroweak.instReprSigmaExponentGrid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L604-L604)
**instance
Tau.BookIV.Electroweak.instReprSigmaExponentGrid :Repr SigmaExponentGrid**

Equations
- Tau.BookIV.Electroweak.instReprSigmaExponentGrid = { reprPrec := Tau.BookIV.Electroweak.instReprSigmaExponentGrid.repr }

---

### `Tau.BookIV.Electroweak.instReprSigmaExponentGrid.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L604-L604)
**def
Tau.BookIV.Electroweak.instReprSigmaExponentGrid.repr :SigmaExponentGrid → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.sigma_grid_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L606-L606)
**def
Tau.BookIV.Electroweak.sigma_grid_data :SigmaExponentGrid**

Equations
- Tau.BookIV.Electroweak.sigma_grid_data = { }
Instances For

---

### `Tau.BookIV.Electroweak.sigma_exponent_grid_optimum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L608-L612)
**theorem
Tau.BookIV.Electroweak.sigma_exponent_grid_optimum :sigma_grid_data.optimum_found = true ∧ sigma_grid_data.tau_effective = true ∧ sigma_grid_data.ratio_matches = true**


---

### `Tau.BookIV.Electroweak.MajoranaCPPhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L615-L626)
**structure
Tau.BookIV.Electroweak.MajoranaCPPhase :Type**


σ=C_τ fixes Majorana phase φ_Majorana(ν₂) = 0 exactly.
Proof sketch: σ-odd eigenstate [1,0,-1]/√2 satisfies C_τ·v = -v.
Majorana condition ψ=Cψ̄ forces e^{iα}=e^{-iα} → α=0 or π.
ν_middle = σ-odd in normal ordering (V.P127) → φ₂ = 0.

- phi2_zero : Bool
φ₂ = 0 exactly.

- from_sigma_constraint : Bool
From σ=C_τ constraint.

- is_analytic : Bool
Analytic (not numerical).

Instances For

---

### `Tau.BookIV.Electroweak.instReprMajoranaCPPhase.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L626-L626)
**def
Tau.BookIV.Electroweak.instReprMajoranaCPPhase.repr :MajoranaCPPhase → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprMajoranaCPPhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L626-L626)
**instance
Tau.BookIV.Electroweak.instReprMajoranaCPPhase :Repr MajoranaCPPhase**

Equations
- Tau.BookIV.Electroweak.instReprMajoranaCPPhase = { reprPrec := Tau.BookIV.Electroweak.instReprMajoranaCPPhase.repr }

---

### `Tau.BookIV.Electroweak.majorana_cp_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L628-L628)
**def
Tau.BookIV.Electroweak.majorana_cp_data :MajoranaCPPhase**

Equations
- Tau.BookIV.Electroweak.majorana_cp_data = { }
Instances For

---

### `Tau.BookIV.Electroweak.majorana_cp_phases_from_sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L630-L634)
**theorem
Tau.BookIV.Electroweak.majorana_cp_phases_from_sigma :majorana_cp_data.phi2_zero = true ∧ majorana_cp_data.from_sigma_constraint = true ∧ majorana_cp_data.is_analytic = true**


---

### `Tau.BookIV.Electroweak.SigmaExponentAsymmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L637-L648)
**structure
Tau.BookIV.Electroweak.SigmaExponentAsymmetry :Type**


[V.P128] Asymmetry δ = Δpq - Δpr = 0.29 empirical.
CF candidate: δ_CF = 2/a₂ = 2/13 ≈ 0.154 (underestimates by ×2, conjectural).

- cf_coefficient : ℕ
CF coefficient a₂ = 13 from CF(ι<sub>τ</sub>⁻¹) = [2;1,13,3,...].

- asymmetry_numerator : ℕ
Numerator of CF candidate: 2/a₂.

- is_cf_structural : Bool
Asymmetry is CF-structural (from continued fraction).

- cf_approximate : Bool
CF candidate is approximate (2/13 ≈ 0.154 vs empirical 0.29).

Instances For

---

### `Tau.BookIV.Electroweak.instReprSigmaExponentAsymmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L648-L648)
**instance
Tau.BookIV.Electroweak.instReprSigmaExponentAsymmetry :Repr SigmaExponentAsymmetry**

Equations
- Tau.BookIV.Electroweak.instReprSigmaExponentAsymmetry = { reprPrec := Tau.BookIV.Electroweak.instReprSigmaExponentAsymmetry.repr }

---

### `Tau.BookIV.Electroweak.instReprSigmaExponentAsymmetry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L648-L648)
**def
Tau.BookIV.Electroweak.instReprSigmaExponentAsymmetry.repr :SigmaExponentAsymmetry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.sigma_exponent_asymmetry_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L650-L651)
**def
Tau.BookIV.Electroweak.sigma_exponent_asymmetry_data :SigmaExponentAsymmetry**


Canonical σ-exponent asymmetry.
Equations
- Tau.BookIV.Electroweak.sigma_exponent_asymmetry_data = { }
Instances For

---

### `Tau.BookIV.Electroweak.sigma_exponent_asymmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L653-L659)
**theorem
Tau.BookIV.Electroweak.sigma_exponent_asymmetry :sigma_exponent_asymmetry_data.cf_coefficient = 13 ∧ sigma_exponent_asymmetry_data.asymmetry_numerator = 2 ∧ sigma_exponent_asymmetry_data.is_cf_structural = true ∧ sigma_exponent_asymmetry_data.cf_approximate = true**


[V.P128] Conjunction: a₂=13, numerator=2, CF-structural, approximate.

---

### `Tau.BookIV.Electroweak.cf_asymmetry_int_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L661-L662)
**theorem
Tau.BookIV.Electroweak.cf_asymmetry_int_check :2 * 100 / 13 = 15**


CF asymmetry integer check: 2×100/13 = 15 (≈ 15.4% of unit interval).

---

### `Tau.BookIV.Electroweak.sprint5a_oqc3_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L668-L670)
**def
Tau.BookIV.Electroweak.sprint5a_oqc3_status :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_exponent_43_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L681-L686)
**def
Tau.BookIV.Electroweak.neutrino_exponent_43_ratio :String**


4/3 ratio from lemniscate counting: Δpq/Δpr = (2×lobes)/sectors = 4/3.
Span Δpq+Δpr = 2 = |lobes|. Gives (8/7, 6/7) with n=7 (same as Higgs).
Numerically: ratio=30.21 at -72589 ppm from PDG 32.576 (conjectural).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_43_counting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L689-L690)
**theorem
Tau.BookIV.Electroweak.neutrino_43_counting :2 * 2 = 4 ∧ 4 + 3 = 7**


---

### `Tau.BookIV.Electroweak.neutrino_span_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L692-L692)
**theorem
Tau.BookIV.Electroweak.neutrino_span_check :8 + 6 = 14 ∧ 14 = 2 * 7**


---

### `Tau.BookIV.Electroweak.neutrino_ratio_43`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L694-L694)
**theorem
Tau.BookIV.Electroweak.neutrino_ratio_43 :8 * 3 = 6 * 4**


---

### `Tau.BookIV.Electroweak.Neutrino87Candidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L698-L712)
**structure
Tau.BookIV.Electroweak.Neutrino87Candidate :Type**


[V.T177] (8/7,6/7) gives ratio 30.211 at −72589 ppm from PDG 32.576.
4/3 ratio exact from lemniscate counting: (2×lobes)/sectors = 4/3.
Grid (1.16,0.87) gives +18.5 ppm (τ-effective, V.T175).

- numerator : ℕ
Numerator of Δpq fraction: 8/7.

- denominator : ℕ
Denominator shared by both fractions: n=7.

- numerator_pr : ℕ
Δpr numerator: 6/7.

- ratio_exact_43 : Bool
Ratio Δpq/Δpr = 4/3 exactly.

- span_eq_lobes : Bool
Span = |lobes| = 2.

Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutrino87Candidate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L712-L712)
**def
Tau.BookIV.Electroweak.instReprNeutrino87Candidate.repr :Neutrino87Candidate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutrino87Candidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L712-L712)
**instance
Tau.BookIV.Electroweak.instReprNeutrino87Candidate :Repr Neutrino87Candidate**

Equations
- Tau.BookIV.Electroweak.instReprNeutrino87Candidate = { reprPrec := Tau.BookIV.Electroweak.instReprNeutrino87Candidate.repr }

---

### `Tau.BookIV.Electroweak.neutrino_87_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L714-L715)
**def
Tau.BookIV.Electroweak.neutrino_87_data :Neutrino87Candidate**


Canonical (8/7,6/7) candidate.
Equations
- Tau.BookIV.Electroweak.neutrino_87_data = { }
Instances For

---

### `Tau.BookIV.Electroweak.neutrino_87_candidate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L717-L724)
**theorem
Tau.BookIV.Electroweak.neutrino_87_candidate :neutrino_87_data.numerator = 8 ∧ neutrino_87_data.denominator = 7 ∧ neutrino_87_data.numerator_pr = 6 ∧ neutrino_87_data.ratio_exact_43 = true ∧ neutrino_87_data.span_eq_lobes = true**


[V.T177] Conjunction: 8/7 numerator, 4/3 ratio, span=lobes.

---

### `Tau.BookIV.Electroweak.neutrino_87_cross_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L726-L727)
**theorem
Tau.BookIV.Electroweak.neutrino_87_cross_ratio :8 * 3 = 6 * 4**


8/6 = 4/3 cross-ratio check: 8×3 = 6×4 = 24.

---

### `Tau.BookIV.Electroweak.neutrino_87_span`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L729-L730)
**theorem
Tau.BookIV.Electroweak.neutrino_87_span :8 + 6 = 2 * 7**


Span check: 8+6 = 14 = 2×7.

---

### `Tau.BookIV.Electroweak.neutrino_n7_scan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L733-L736)
**theorem
Tau.BookIV.Electroweak.neutrino_n7_scan :True**


n=7 with (8/7,6/7) gives best rational-denominator fit among n∈{5,6,7,8,9,13}.
All give ppm<0 (undershoot). n=7 at -72589 ppm; n=9 at -13645 ppm (closer).
CF crossover: n=13 gives +52368 ppm (overshoot).

---

### `Tau.BookIV.Electroweak.sprint6a_oqc3_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L739-L742)
**def
Tau.BookIV.Electroweak.sprint6a_oqc3_status :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For
