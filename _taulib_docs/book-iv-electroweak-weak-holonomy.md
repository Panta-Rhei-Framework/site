---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.WeakHolonomy"
permalink: /verify/taulib/docs/book-iv-electroweak-weak-holonomy/
lane: verify
module_name: "TauLib.BookIV.Electroweak.WeakHolonomy"
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

# TauLib.BookIV.Electroweak.WeakHolonomy


SU(2) gauge structure of the weak sector: generators, left-handed
doublets, holonomy loops, W boson mass, and coupling hierarchy.

## Registry Cross-References


- [IV.D115] Crossing-Point Action Space — `CrossingActionSpace`

- [IV.D116] SU(2) Generators (Pauli Matrices) — `SU2Generator`

- [IV.D117] Left-Handed Doublets — `LeftHandedDoublet`

- [IV.D118] Adjoint Representation — `AdjointRep`

- [IV.D119] Holonomy Loop in A-Sector — `WeakHolonomyLoop`

- [IV.D120] W Boson Observed Mass — `w_mass_mev`

- [IV.T52] Weak Gauge Group Is SU(2)_L — `weak_gauge_su2`

- [IV.T53] Weak Fine-Structure Constant alpha_wk — `alpha_weak`

- [IV.T54] W Mass from Coherence-Fixing Scale — `w_mass_from_coherence`

- [IV.P56] W± and W3 from SU(2) Generators — `w_from_su2_generators`

- [IV.P57] Fermi Constant from W Propagator — `fermi_from_w`

- [IV.P58] Weak > EM Coupling — `weak_gt_em`

- [IV.P59] W As Crossing Amplitude — `w_as_crossing`


## Ground Truth Sources


- Chapter 31 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.CrossingActionSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L38-L49)
**structure
Tau.BookIV.Electroweak.CrossingActionSpace :Type**


[IV.D115] The crossing-point action space: the tangent space at
the omega-crossing of L (lemniscate), where the A-sector holonomy
is concentrated. The crossing point is where both lobes meet,
giving SU(2) its non-abelian structure.

- real_dim : ℕ
Real dimension of the tangent space at crossing.

- dim_eq : self.real_dim = 3
- both_lobes : Bool
The crossing is where both lobes are simultaneously active.

- both_true : self.both_lobes = true
Instances For

---

### `Tau.BookIV.Electroweak.instReprCrossingActionSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L49-L49)
**instance
Tau.BookIV.Electroweak.instReprCrossingActionSpace :Repr CrossingActionSpace**

Equations
- Tau.BookIV.Electroweak.instReprCrossingActionSpace = { reprPrec := Tau.BookIV.Electroweak.instReprCrossingActionSpace.repr }

---

### `Tau.BookIV.Electroweak.instReprCrossingActionSpace.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L49-L49)
**def
Tau.BookIV.Electroweak.instReprCrossingActionSpace.repr :CrossingActionSpace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.crossing_action`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L51-L56)
**def
Tau.BookIV.Electroweak.crossing_action :CrossingActionSpace**


The canonical crossing-point action space.
Equations
- Tau.BookIV.Electroweak.crossing_action = { real_dim := 3, dim_eq := Tau.BookIV.Electroweak.crossing_action._proof_1, both_lobes := true, both_true := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.SU2Generator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L62-L73)
**structure
Tau.BookIV.Electroweak.SU2Generator :Type**


[IV.D116] The three SU(2) generators (Pauli matrices sigma_1, sigma_2, sigma_3).
Each generator is a 2x2 traceless Hermitian matrix.
In the tau-framework, these arise as the tangent directions
at the crossing point of L.

- index : Fin 3
Generator index: 1, 2, or 3.

- name : String
Name label.

- boson : String
Physical boson association.

Instances For

---

### `Tau.BookIV.Electroweak.instReprSU2Generator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L73-L73)
**instance
Tau.BookIV.Electroweak.instReprSU2Generator :Repr SU2Generator**

Equations
- Tau.BookIV.Electroweak.instReprSU2Generator = { reprPrec := Tau.BookIV.Electroweak.instReprSU2Generator.repr }

---

### `Tau.BookIV.Electroweak.instReprSU2Generator.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L73-L73)
**def
Tau.BookIV.Electroweak.instReprSU2Generator.repr :SU2Generator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.sigma_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L75-L76)
**def
Tau.BookIV.Electroweak.sigma_1 :SU2Generator**


sigma_1: associated with W+ and W-.
Equations
- Tau.BookIV.Electroweak.sigma_1 = { index := 0, name := "sigma_1", boson := "W+/W-" }
Instances For

---

### `Tau.BookIV.Electroweak.sigma_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L77-L78)
**def
Tau.BookIV.Electroweak.sigma_2 :SU2Generator**


sigma_2: associated with W+ and W-.
Equations
- Tau.BookIV.Electroweak.sigma_2 = { index := 1, name := "sigma_2", boson := "W+/W-" }
Instances For

---

### `Tau.BookIV.Electroweak.sigma_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L79-L80)
**def
Tau.BookIV.Electroweak.sigma_3 :SU2Generator**


sigma_3: associated with W3 (neutral).
Equations
- Tau.BookIV.Electroweak.sigma_3 = { index := 2, name := "sigma_3", boson := "W3" }
Instances For

---

### `Tau.BookIV.Electroweak.su2_generators`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L82-L83)
**def
Tau.BookIV.Electroweak.su2_generators :List SU2Generator**


All three generators.
Equations
- Tau.BookIV.Electroweak.su2_generators = [Tau.BookIV.Electroweak.sigma_1, Tau.BookIV.Electroweak.sigma_2, Tau.BookIV.Electroweak.sigma_3]
Instances For

---

### `Tau.BookIV.Electroweak.LeftHandedDoublet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L89-L102)
**structure
Tau.BookIV.Electroweak.LeftHandedDoublet :Type**


[IV.D117] A left-handed doublet: the fundamental representation
of SU(2)_L. Pairs an "up-type" and a "down-type" fermion,
both left-handed. The weak interaction rotates within doublets.

- generation : Fin 3
Generation number (1, 2, or 3).

- up_type : String
Up-type particle name.

- down_type : String
Down-type particle name.

- chirality : ChiralityType
Both components are left-handed.

- chirality_left : self.chirality = ChiralityType.Left
Instances For

---

### `Tau.BookIV.Electroweak.instReprLeftHandedDoublet.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L102-L102)
**def
Tau.BookIV.Electroweak.instReprLeftHandedDoublet.repr :LeftHandedDoublet → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprLeftHandedDoublet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L102-L102)
**instance
Tau.BookIV.Electroweak.instReprLeftHandedDoublet :Repr LeftHandedDoublet**

Equations
- Tau.BookIV.Electroweak.instReprLeftHandedDoublet = { reprPrec := Tau.BookIV.Electroweak.instReprLeftHandedDoublet.repr }

---

### `Tau.BookIV.Electroweak.doublet_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L104-L107)
**def
Tau.BookIV.Electroweak.doublet_1 :LeftHandedDoublet**


First generation: (electron neutrino, electron).
Equations
- Tau.BookIV.Electroweak.doublet_1 = { generation := 0, up_type := "nu_e", down_type := "e", chirality := Tau.BookIV.Electroweak.ChiralityType.Left,
 chirality_left := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.doublet_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L109-L112)
**def
Tau.BookIV.Electroweak.doublet_2 :LeftHandedDoublet**


Second generation: (muon neutrino, muon).
Equations
- Tau.BookIV.Electroweak.doublet_2 = { generation := 1, up_type := "nu_mu", down_type := "mu", chirality := Tau.BookIV.Electroweak.ChiralityType.Left,
 chirality_left := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.doublet_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L114-L117)
**def
Tau.BookIV.Electroweak.doublet_3 :LeftHandedDoublet**


Third generation: (tau neutrino, tau).
Equations
- Tau.BookIV.Electroweak.doublet_3 = { generation := 2, up_type := "nu_tau", down_type := "tau", chirality := Tau.BookIV.Electroweak.ChiralityType.Left,
 chirality_left := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.lepton_doublets`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L119-L120)
**def
Tau.BookIV.Electroweak.lepton_doublets :List LeftHandedDoublet**


All three lepton doublets.
Equations
- Tau.BookIV.Electroweak.lepton_doublets = [Tau.BookIV.Electroweak.doublet_1, Tau.BookIV.Electroweak.doublet_2, Tau.BookIV.Electroweak.doublet_3]
Instances For

---

### `Tau.BookIV.Electroweak.three_generations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L122-L122)
**theorem
Tau.BookIV.Electroweak.three_generations :lepton_doublets.length = 3**


---

### `Tau.BookIV.Electroweak.AdjointRep`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L128-L138)
**structure
Tau.BookIV.Electroweak.AdjointRep :Type**


[IV.D118] The adjoint representation of SU(2): the 3-dimensional
representation in which the gauge bosons (W+, W-, W3) live.
dim(adjoint) = dim(SU(2)) = 3.

- adj_dim : ℕ
Dimension of the adjoint representation.

- adj_eq : self.adj_dim = 3
- num_bosons : ℕ
Number of gauge bosons in the adjoint.

- bosons_eq : self.num_bosons = 3
Instances For

---

### `Tau.BookIV.Electroweak.instReprAdjointRep.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L138-L138)
**def
Tau.BookIV.Electroweak.instReprAdjointRep.repr :AdjointRep → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprAdjointRep`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L138-L138)
**instance
Tau.BookIV.Electroweak.instReprAdjointRep :Repr AdjointRep**

Equations
- Tau.BookIV.Electroweak.instReprAdjointRep = { reprPrec := Tau.BookIV.Electroweak.instReprAdjointRep.repr }

---

### `Tau.BookIV.Electroweak.adjoint_su2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L140-L143)
**def
Tau.BookIV.Electroweak.adjoint_su2 :AdjointRep**


The canonical adjoint representation.
Equations
- Tau.BookIV.Electroweak.adjoint_su2 = { adj_dim := 3, adj_eq := Tau.BookIV.Electroweak.crossing_action._proof_1, num_bosons := 3,
 bosons_eq := Tau.BookIV.Electroweak.crossing_action._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.WeakHolonomyLoop`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L149-L162)
**structure
Tau.BookIV.Electroweak.WeakHolonomyLoop :Type**


[IV.D119] A holonomy loop in the A-sector: parallel transport
around a closed path in the weak sector produces a non-trivial
SU(2) rotation. The non-abelian nature comes from the crossing
point where both lobes interact.

- winding : ℕ
Winding number around the crossing.

- non_abelian : Bool
Non-abelian holonomy: rotation angle depends on path.

- non_abelian_true : self.non_abelian = true
- group_dim : ℕ
The holonomy group is SU(2).

- group_eq : self.group_dim = 3
Instances For

---

### `Tau.BookIV.Electroweak.instReprWeakHolonomyLoop.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L162-L162)
**def
Tau.BookIV.Electroweak.instReprWeakHolonomyLoop.repr :WeakHolonomyLoop → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprWeakHolonomyLoop`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L162-L162)
**instance
Tau.BookIV.Electroweak.instReprWeakHolonomyLoop :Repr WeakHolonomyLoop**

Equations
- Tau.BookIV.Electroweak.instReprWeakHolonomyLoop = { reprPrec := Tau.BookIV.Electroweak.instReprWeakHolonomyLoop.repr }

---

### `Tau.BookIV.Electroweak.weak_holonomy_single`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L164-L170)
**def
Tau.BookIV.Electroweak.weak_holonomy_single :WeakHolonomyLoop**


Single-winding holonomy loop.
Equations
- Tau.BookIV.Electroweak.weak_holonomy_single = { winding := 1, non_abelian := true, non_abelian_true := ⋯, group_dim := 3,
 group_eq := Tau.BookIV.Electroweak.crossing_action._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.ObservedMass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L176-L186)
**structure
Tau.BookIV.Electroweak.ObservedMass :Type**


[IV.D120] W boson observed mass: M_W = 80379 MeV (PDG 2022).
Encoded as a rational pair (numer/denom) in MeV.

- name : String
Particle name.

- mass_numer : ℕ
Mass numerator in MeV.

- mass_denom : ℕ
Mass denominator (for sub-MeV precision).

- denom_pos : self.mass_denom > 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprObservedMass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L186-L186)
**instance
Tau.BookIV.Electroweak.instReprObservedMass :Repr ObservedMass**

Equations
- Tau.BookIV.Electroweak.instReprObservedMass = { reprPrec := Tau.BookIV.Electroweak.instReprObservedMass.repr }

---

### `Tau.BookIV.Electroweak.instReprObservedMass.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L186-L186)
**def
Tau.BookIV.Electroweak.instReprObservedMass.repr :ObservedMass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.w_mass_mev`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L188-L190)
**def
Tau.BookIV.Electroweak.w_mass_mev :ObservedMass**


W boson mass: 80379 MeV.
Equations
- Tau.BookIV.Electroweak.w_mass_mev = { name := "W", mass_numer := 80379, mass_denom := 1, denom_pos := Tau.BookIV.Electroweak.w_mass_mev._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.w_mass_float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L192-L193)
**def
Tau.BookIV.Electroweak.w_mass_float :Float**


W mass as Float.
Equations
- Tau.BookIV.Electroweak.w_mass_float = Float.ofNat Tau.BookIV.Electroweak.w_mass_mev.mass_numer / Float.ofNat Tau.BookIV.Electroweak.w_mass_mev.mass_denom
Instances For

---

### `Tau.BookIV.Electroweak.weak_gauge_su2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L199-L208)
**theorem
Tau.BookIV.Electroweak.weak_gauge_su2 :crossing_action.real_dim = 3 ∧ weak_holonomy_single.non_abelian = true ∧ su2l_identification.chirality = ChiralityType.Left**


[IV.T52] The weak gauge group is SU(2)_L: this follows from
(1) the crossing-point action space has dim = 3,
(2) the holonomy is non-abelian,
(3) only left-handed states participate.
The subscript L denotes left-handed chirality selection.

---

### `Tau.BookIV.Electroweak.WeakFineStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L214-L224)
**structure
Tau.BookIV.Electroweak.WeakFineStructure :Type**


[IV.T53] Weak fine-structure constant alpha_wk: the A-sector
self-coupling kappa(A;1) = iota_tau determines the weak coupling.
alpha_wk = kappa(A;1)^2 / (4*pi) at leading order.
We record alpha_wk as a scaled rational.

- numer : ℕ
Numerator (iota_tau squared, scaled).

- denom : ℕ
Denominator (4*pi*denom^2, approximated).

- denom_pos : self.denom > 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprWeakFineStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L224-L224)
**instance
Tau.BookIV.Electroweak.instReprWeakFineStructure :Repr WeakFineStructure**

Equations
- Tau.BookIV.Electroweak.instReprWeakFineStructure = { reprPrec := Tau.BookIV.Electroweak.instReprWeakFineStructure.repr }

---

### `Tau.BookIV.Electroweak.instReprWeakFineStructure.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L224-L224)
**def
Tau.BookIV.Electroweak.instReprWeakFineStructure.repr :WeakFineStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.alpha_weak`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L226-L233)
**def
Tau.BookIV.Electroweak.alpha_weak :WeakFineStructure**


alpha_wk approximation: iota^2 / (4*pi) where iota = 341304/10^6.
iota^2 = 116594274681 / 10^12.
4*pi 12566/1000. So alpha_wk 116594274681*1000 / (10^12 * 12566).
We simplify: numer = iota^2 = 116594274681, denom = 12566 * 10^6.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.w_mass_from_coherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L239-L244)
**theorem
Tau.BookIV.Electroweak.w_mass_from_coherence :w_mass_mev.mass_numer > 0**


[IV.T54] W mass from coherence-fixing scale: the omega-crossing
singularity fixes a coherence scale Lambda_EW. The W mass is
M_W = g_wk * Lambda_EW / 2, where g_wk is the weak coupling.
Structural: the mass is nonzero because Lambda_EW > 0.

---

### `Tau.BookIV.Electroweak.w_from_su2_generators`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L250-L256)
**theorem
Tau.BookIV.Electroweak.w_from_su2_generators :su2_generators.length = 3 ∧ adjoint_su2.num_bosons = 3**


[IV.P56] The physical W+, W-, W3 bosons arise from the 3 SU(2)
generators: W± from (sigma_1 ± i·sigma_2)/√2,
W3 = sigma_3. There are exactly 3 gauge bosons.

---

### `Tau.BookIV.Electroweak.FermiConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L262-L272)
**structure
Tau.BookIV.Electroweak.FermiConstant :Type**


[IV.P57] The Fermi constant G_F arises from W exchange at low energy:
G_F / sqrt(2) = g_wk^2 / (8 * M_W^2).
G_F = 1.1663788 * 10^-5 GeV^-2.
Encoded as scaled Nat pair.

- numer : ℕ
G_F numerator (scaled to 10^11).

- denom : ℕ
G_F denominator.

- denom_pos : self.denom > 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprFermiConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L272-L272)
**instance
Tau.BookIV.Electroweak.instReprFermiConstant :Repr FermiConstant**

Equations
- Tau.BookIV.Electroweak.instReprFermiConstant = { reprPrec := Tau.BookIV.Electroweak.instReprFermiConstant.repr }

---

### `Tau.BookIV.Electroweak.instReprFermiConstant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L272-L272)
**def
Tau.BookIV.Electroweak.instReprFermiConstant.repr :FermiConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.fermi_from_w`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L274-L278)
**def
Tau.BookIV.Electroweak.fermi_from_w :FermiConstant**


G_F = 11664 / 10^9 GeV^-2 (approximate).
Equations
- Tau.BookIV.Electroweak.fermi_from_w = { numer := 11664, denom := 1000000000, denom_pos := Tau.BookIV.Electroweak.fermi_from_w._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.weak_gt_em`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L284-L291)
**theorem
Tau.BookIV.Electroweak.weak_gt_em :Sectors.kappa_AA.numer * Sectors.kappa_BB.denom > Sectors.kappa_BB.numer * Sectors.kappa_AA.denom**


[IV.P58] The weak self-coupling exceeds the EM self-coupling:
kappa(A;1) = iota_tau > iota_tau^2 = kappa(B;2).
Since 0 < iota_tau < 1, iota > iota^2.
Proven via the coupling formula definitions.

---

### `Tau.BookIV.Electroweak.w_as_crossing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L297-L304)
**theorem
Tau.BookIV.Electroweak.w_as_crossing :w_plus.charge ≠ 0 ∧ w_plus.massive = true ∧ w_minus.charge ≠ 0 ∧ w_minus.massive = true**


[IV.P59] The W boson is the crossing amplitude: it is the transport
mode that connects the two lobes of L at the omega-crossing.
Structural: W carries charge (switches polarity) and is massive
(coherence scale from crossing).
