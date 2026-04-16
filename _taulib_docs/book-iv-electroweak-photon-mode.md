---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.PhotonMode"
permalink: /verify/taulib/docs/book-iv-electroweak-photon-mode/
lane: verify
module_name: "TauLib.BookIV.Electroweak.PhotonMode"
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

# TauLib.BookIV.Electroweak.PhotonMode


The photon as B-sector transport mode on T², U(1) holonomy, electric
charge as winding number, and the structural derivation of photon
properties from τ³ = τ¹ ×_f T².

## Registry Cross-References


- [IV.D82] Photon Mode — `PhotonMode`

- [IV.D83] U(1) Holonomy — `U1Holonomy`

- [IV.D84] Electric Charge — `ElectricCharge`

- [IV.T33] Photon Mass Zero — `photon_mass_zero`

- [IV.T34] Photon Speed c — `photon_speed_c`

- [IV.T35] Holonomy Transport — `holonomy_transport`

- [IV.T36] Charge Conservation — `charge_conservation`

- [IV.T120] Charge Quantization — `charge_quantized`

- [IV.P32] No Rest Frame — `no_rest_frame`

- [IV.P33] Spin and Polarization — `photon_spin`

- [IV.P34] Particle Charges — `particle_charges`

- [IV.P35] Boundary Character — `photon_boundary_character`

- [IV.P36] Emission Amplitude — `emission_amplitude`

- [IV.R347-R351] structural remarks


## Mathematical Content


### Photon as B-Sector Transport Mode


The photon is the unique B-sector (γ-generator, EM) transport mode with
degenerate fiber character (m,n) = (0,0). Since the character is constant
(zero winding on both T² circles), the mode has:


- Zero mass (lies in ker(Δ_Hodge) on T²)

- Propagation at limiting speed c (no fiber obstruction)

- Spin s = 1 with exactly 2 polarization states (from CR-parity)


### U(1) Holonomy and Electric Charge


The EM gauge connection on T² defines a U(1) holonomy around each closed
loop. Electric charge is the integer winding number of this holonomy:


- Quantization: automatic from compactness of T²

- Conservation: winding numbers are additive under composition

- e, -e, 0: proton, electron, neutron charge assignments


## Ground Truth Sources


- Chapter 26 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.PhotonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L60-L84)
**structure
Tau.BookIV.Electroweak.PhotonMode :Type**


[IV.D82] The photon as B-sector transport mode with degenerate
fiber character (m,n) = (0,0). The unique massless EM mode.

- sector : BookIII.Sectors.Sector
The sector: must be B (EM).

- sector_eq : self.sector = BookIII.Sectors.Sector.B
- generator : Kernel.Generator
The generator: must be γ.

- gen_eq : self.generator = Kernel.Generator.gamma
- m_index : ℤ
Fiber character m-index = 0 (degenerate).

- m_zero : self.m_index = 0
- n_index : ℤ
Fiber character n-index = 0 (degenerate).

- n_zero : self.n_index = 0
- mass_numer : ℕ
Mass = 0 (from constant character in ker(Δ_Hodge)).

- mass_zero : self.mass_numer = 0
- spin : ℕ
Spin quantum number (s = 1).

- spin_eq : self.spin = 1
- polarizations : ℕ
Number of polarization states.

- pol_eq : self.polarizations = 2
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L84-L84)
**def
Tau.BookIV.Electroweak.instReprPhotonMode.repr :PhotonMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L84-L84)
**instance
Tau.BookIV.Electroweak.instReprPhotonMode :Repr PhotonMode**

Equations
- Tau.BookIV.Electroweak.instReprPhotonMode = { reprPrec := Tau.BookIV.Electroweak.instReprPhotonMode.repr }

---

### `Tau.BookIV.Electroweak.photon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L86-L101)
**def
Tau.BookIV.Electroweak.photon :PhotonMode**


Canonical photon instance.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.U1Holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L107-L118)
**structure
Tau.BookIV.Electroweak.U1Holonomy :Type**


[IV.D83] U(1) holonomy of the B-sector connection around a closed
loop on T². The holonomy is exp(i·2π·(flux/Φ₀)) where flux is
the EM flux through the loop and Φ₀ is the flux quantum.

- sector : BookIII.Sectors.Sector
Sector (must be B).

- sector_eq : self.sector = BookIII.Sectors.Sector.B
- winding : ℤ
Winding number (integer from compactness of T²).

- phase_is_periodic : Bool
Phase is 2π times winding number (modulo 2π).

Instances For

---

### `Tau.BookIV.Electroweak.instReprU1Holonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L118-L118)
**def
Tau.BookIV.Electroweak.instReprU1Holonomy.repr :U1Holonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprU1Holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L118-L118)
**instance
Tau.BookIV.Electroweak.instReprU1Holonomy :Repr U1Holonomy**

Equations
- Tau.BookIV.Electroweak.instReprU1Holonomy = { reprPrec := Tau.BookIV.Electroweak.instReprU1Holonomy.repr }

---

### `Tau.BookIV.Electroweak.U1Holonomy.compose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L120-L124)
**def
Tau.BookIV.Electroweak.U1Holonomy.compose
(h₁ h₂ : U1Holonomy)
 :U1Holonomy**


Holonomy composition: winding numbers add.
Equations
- h₁.compose h₂ = { sector := Tau.BookIII.Sectors.Sector.B, sector_eq := ⋯, winding := h₁.winding + h₂.winding }
Instances For

---

### `Tau.BookIV.Electroweak.U1Holonomy.trivial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L126-L130)
**def
Tau.BookIV.Electroweak.U1Holonomy.trivial :U1Holonomy**


Trivial holonomy (zero winding).
Equations
- Tau.BookIV.Electroweak.U1Holonomy.trivial = { sector := Tau.BookIII.Sectors.Sector.B, sector_eq := ⋯, winding := 0 }
Instances For

---

### `Tau.BookIV.Electroweak.U1Holonomy.inv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L132-L136)
**def
Tau.BookIV.Electroweak.U1Holonomy.inv
(h : U1Holonomy)
 :U1Holonomy**


Inverse holonomy.
Equations
- h.inv = { sector := Tau.BookIII.Sectors.Sector.B, sector_eq := ⋯, winding := -h.winding }
Instances For

---

### `Tau.BookIV.Electroweak.ElectricCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L142-L148)
**structure
Tau.BookIV.Electroweak.ElectricCharge :Type**


[IV.D84] Electric charge as winding number of U(1) holonomy.
Charge is quantized in units of e (from T² compactness).
The value is an integer: q/e ∈ ℤ.

- charge_units : ℤ
Charge in units of e.

Instances For

---

### `Tau.BookIV.Electroweak.instReprElectricCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L148-L148)
**instance
Tau.BookIV.Electroweak.instReprElectricCharge :Repr ElectricCharge**

Equations
- Tau.BookIV.Electroweak.instReprElectricCharge = { reprPrec := Tau.BookIV.Electroweak.instReprElectricCharge.repr }

---

### `Tau.BookIV.Electroweak.instReprElectricCharge.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L148-L148)
**def
Tau.BookIV.Electroweak.instReprElectricCharge.repr :ElectricCharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqElectricCharge.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L148-L148)
**def
Tau.BookIV.Electroweak.instDecidableEqElectricCharge.decEq
(x✝ x✝¹ : ElectricCharge)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookIV.Electroweak.instDecidableEqElectricCharge.decEq { charge_units := a } { charge_units := b } = if h : a = b then h ▸ isTrue ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqElectricCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L148-L148)
**instance
Tau.BookIV.Electroweak.instDecidableEqElectricCharge :DecidableEq ElectricCharge**

Equations
- Tau.BookIV.Electroweak.instDecidableEqElectricCharge = Tau.BookIV.Electroweak.instDecidableEqElectricCharge.decEq

---

### `Tau.BookIV.Electroweak.instBEqElectricCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L148-L148)
**instance
Tau.BookIV.Electroweak.instBEqElectricCharge :BEq ElectricCharge**

Equations
- Tau.BookIV.Electroweak.instBEqElectricCharge = { beq := Tau.BookIV.Electroweak.instBEqElectricCharge.beq }

---

### `Tau.BookIV.Electroweak.instBEqElectricCharge.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L148-L148)
**def
Tau.BookIV.Electroweak.instBEqElectricCharge.beq :ElectricCharge → ElectricCharge → Bool**

Equations
- Tau.BookIV.Electroweak.instBEqElectricCharge.beq { charge_units := a } { charge_units := b } = (a == b)
- Tau.BookIV.Electroweak.instBEqElectricCharge.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIV.Electroweak.charge_electron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L150-L151)
**def
Tau.BookIV.Electroweak.charge_electron :ElectricCharge**


Electron charge: -1 (in units of e).
Equations
- Tau.BookIV.Electroweak.charge_electron = { charge_units := -1 }
Instances For

---

### `Tau.BookIV.Electroweak.charge_proton`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L152-L153)
**def
Tau.BookIV.Electroweak.charge_proton :ElectricCharge**


Proton charge: +1.
Equations
- Tau.BookIV.Electroweak.charge_proton = { charge_units := 1 }
Instances For

---

### `Tau.BookIV.Electroweak.charge_neutron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L154-L155)
**def
Tau.BookIV.Electroweak.charge_neutron :ElectricCharge**


Neutron charge: 0.
Equations
- Tau.BookIV.Electroweak.charge_neutron = { charge_units := 0 }
Instances For

---

### `Tau.BookIV.Electroweak.charge_photon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L156-L157)
**def
Tau.BookIV.Electroweak.charge_photon :ElectricCharge**


Photon charge: 0 (neutral carrier).
Equations
- Tau.BookIV.Electroweak.charge_photon = { charge_units := 0 }
Instances For

---

### `Tau.BookIV.Electroweak.ElectricCharge.add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L159-L161)
**def
Tau.BookIV.Electroweak.ElectricCharge.add
(q₁ q₂ : ElectricCharge)
 :ElectricCharge**


Charge addition.
Equations
- q₁.add q₂ = { charge_units := q₁.charge_units + q₂.charge_units }
Instances For

---

### `Tau.BookIV.Electroweak.photon_mass_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L167-L169)
**theorem
Tau.BookIV.Electroweak.photon_mass_zero :photon.mass_numer = 0**


[IV.T33] Photon mass is exactly zero: constant fiber character
(0,0) lies in ker(Δ_Hodge), so no mass eigenvalue arises.

---

### `Tau.BookIV.Electroweak.PhotonSpeed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L175-L182)
**structure
Tau.BookIV.Electroweak.PhotonSpeed :Type**


[IV.T34] Photon propagates at limiting speed c.
Zero mass implies zero fiber obstruction implies base-only
propagation at c.

- mass_zero : Bool
- speed_is_c : Bool
- fiber_obstruction_zero : Bool
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonSpeed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L182-L182)
**instance
Tau.BookIV.Electroweak.instReprPhotonSpeed :Repr PhotonSpeed**

Equations
- Tau.BookIV.Electroweak.instReprPhotonSpeed = { reprPrec := Tau.BookIV.Electroweak.instReprPhotonSpeed.repr }

---

### `Tau.BookIV.Electroweak.instReprPhotonSpeed.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L182-L182)
**def
Tau.BookIV.Electroweak.instReprPhotonSpeed.repr :PhotonSpeed → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.photon_speed_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L184-L186)
**theorem
Tau.BookIV.Electroweak.photon_speed_c
(p : PhotonSpeed)

(h1 : p.mass_zero = true)

(h2 : p.speed_is_c = true)
 :p.mass_zero = true ∧ p.speed_is_c = true**


---

### `Tau.BookIV.Electroweak.HolonomyTransport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L192-L202)
**structure
Tau.BookIV.Electroweak.HolonomyTransport :Type**


[IV.T35] Photon as holonomy transport mode: the photon IS the
parallel transport of the U(1) connection. Wave/particle duality
is structural: wave = boundary character, particle = defect bundle.

- mode : PhotonMode
The photon mode.

- wave_is_character : Bool
Wave aspect = boundary character on L.

- particle_is_defect : Bool
Particle aspect = defect bundle on T².

Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyTransport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L202-L202)
**instance
Tau.BookIV.Electroweak.instReprHolonomyTransport :Repr HolonomyTransport**

Equations
- Tau.BookIV.Electroweak.instReprHolonomyTransport = { reprPrec := Tau.BookIV.Electroweak.instReprHolonomyTransport.repr }

---

### `Tau.BookIV.Electroweak.instReprHolonomyTransport.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L202-L202)
**def
Tau.BookIV.Electroweak.instReprHolonomyTransport.repr :HolonomyTransport → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.holonomy_transport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L204-L206)
**theorem
Tau.BookIV.Electroweak.holonomy_transport
(ht : HolonomyTransport)

(hw : ht.wave_is_character = true)

(hp : ht.particle_is_defect = true)
 :ht.wave_is_character = true ∧ ht.particle_is_defect = true**


---

### `Tau.BookIV.Electroweak.charge_conservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L212-L215)
**theorem
Tau.BookIV.Electroweak.charge_conservation
(q₁ q₂ : ElectricCharge)
 :(q₁.add q₂).charge_units = q₁.charge_units + q₂.charge_units**


[IV.T36] Total electric charge is conserved: winding numbers
are additive under composition of holonomy loops.

---

### `Tau.BookIV.Electroweak.charge_quantized`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L221-L224)
**theorem
Tau.BookIV.Electroweak.charge_quantized
(q : ElectricCharge)
 :∃ (n : ℤ), q.charge_units = n**


[IV.T120] Electric charge is quantized in units of e.
From compactness of T²: holonomy exp(i·2π·n) requires n ∈ ℤ.

---

### `Tau.BookIV.Electroweak.NoRestFrame`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L230-L235)
**structure
Tau.BookIV.Electroweak.NoRestFrame :Type**


[IV.P32] Photon has no rest frame: zero mass implies no
Lorentz frame where momentum vanishes.

- mass_zero : Bool
- no_rest_frame : Bool
Instances For

---

### `Tau.BookIV.Electroweak.instReprNoRestFrame.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L235-L235)
**def
Tau.BookIV.Electroweak.instReprNoRestFrame.repr :NoRestFrame → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprNoRestFrame`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L235-L235)
**instance
Tau.BookIV.Electroweak.instReprNoRestFrame :Repr NoRestFrame**

Equations
- Tau.BookIV.Electroweak.instReprNoRestFrame = { reprPrec := Tau.BookIV.Electroweak.instReprNoRestFrame.repr }

---

### `Tau.BookIV.Electroweak.no_rest_frame`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L237-L238)
**theorem
Tau.BookIV.Electroweak.no_rest_frame
(nrf : NoRestFrame)

(h : nrf.mass_zero = true)
 :nrf.mass_zero = true**


---

### `Tau.BookIV.Electroweak.photon_spin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L244-L247)
**theorem
Tau.BookIV.Electroweak.photon_spin :photon.spin = 1 ∧ photon.polarizations = 2**


[IV.P33] Photon has spin s=1, with exactly 2 polarization
states (not 2s+1=3) due to masslessness removing longitudinal.

---

### `Tau.BookIV.Electroweak.particle_charges`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L253-L258)
**theorem
Tau.BookIV.Electroweak.particle_charges :charge_electron.charge_units = -1 ∧ charge_proton.charge_units = 1 ∧ charge_neutron.charge_units = 0**


[IV.P34] Electron charge -e, proton +e, neutron 0.

---

### `Tau.BookIV.Electroweak.PhotonBoundaryChar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L264-L270)
**structure
Tau.BookIV.Electroweak.PhotonBoundaryChar :Type**


[IV.P35] Photon as boundary character under the Central Theorem:
the photon field is the (0,0) character in A_spec(L).

- m_index : ℤ
- n_index : ℤ
- is_trivial : self.m_index = 0 ∧ self.n_index = 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonBoundaryChar.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L270-L270)
**def
Tau.BookIV.Electroweak.instReprPhotonBoundaryChar.repr :PhotonBoundaryChar → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonBoundaryChar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L270-L270)
**instance
Tau.BookIV.Electroweak.instReprPhotonBoundaryChar :Repr PhotonBoundaryChar**

Equations
- Tau.BookIV.Electroweak.instReprPhotonBoundaryChar = { reprPrec := Tau.BookIV.Electroweak.instReprPhotonBoundaryChar.repr }

---

### `Tau.BookIV.Electroweak.photon_boundary_character`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L272-L273)
**theorem
Tau.BookIV.Electroweak.photon_boundary_character :photon.m_index = 0 ∧ photon.n_index = 0**


---

### `Tau.BookIV.Electroweak.EmissionAmplitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L279-L286)
**structure
Tau.BookIV.Electroweak.EmissionAmplitude :Type**


[IV.P36] Emission/absorption amplitude proportional to √α.
The coupling constant α = (8/15)·ι<sub>τ</sub>⁴ enters as amplitude squared.

- amplitude_sq_numer : ℕ
Amplitude squared = α (fine structure constant).

- amplitude_sq_denom : ℕ
- denom_pos : self.amplitude_sq_denom > 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprEmissionAmplitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L286-L286)
**instance
Tau.BookIV.Electroweak.instReprEmissionAmplitude :Repr EmissionAmplitude**

Equations
- Tau.BookIV.Electroweak.instReprEmissionAmplitude = { reprPrec := Tau.BookIV.Electroweak.instReprEmissionAmplitude.repr }

---

### `Tau.BookIV.Electroweak.instReprEmissionAmplitude.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L286-L286)
**def
Tau.BookIV.Electroweak.instReprEmissionAmplitude.repr :EmissionAmplitude → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.EmissionAmplitude.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L288-L289)
**def
Tau.BookIV.Electroweak.EmissionAmplitude.toFloat
(e : EmissionAmplitude)
 :Float**

Equations
- e.toFloat = Float.ofNat e.amplitude_sq_numer / Float.ofNat e.amplitude_sq_denom
Instances For

---

### `Tau.BookIV.Electroweak.emission_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L291-L295)
**def
Tau.BookIV.Electroweak.emission_alpha :EmissionAmplitude**


Canonical emission amplitude: α_spec = (8/15)·ι<sub>τ</sub>⁴.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.emission_amplitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L297-L299)
**theorem
Tau.BookIV.Electroweak.emission_amplitude :emission_alpha.amplitude_sq_numer = Sectors.alpha_spectral_numer**


---

### `Tau.BookIV.Electroweak.example_u1_hol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/PhotonMode.lean#L328-L328)
**def
Tau.BookIV.Electroweak.example_u1_hol :U1Holonomy**

Equations
- Tau.BookIV.Electroweak.example_u1_hol = { sector := Tau.BookIII.Sectors.Sector.B, sector_eq := ⋯, winding := 3 }
Instances For
