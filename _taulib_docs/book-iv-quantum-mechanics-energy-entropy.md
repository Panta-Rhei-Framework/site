---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.EnergyEntropy"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.EnergyEntropy"
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

# TauLib.BookIV.QuantumMechanics.EnergyEntropy


Energy, entropy, arrow of time, and the dual reading of eigenvalues.

## Registry Cross-References


- [IV.D76] Holomorphic Tension Energy — `HolomorphicTension`

- [IV.D77] Graph Energy Density — `GraphEnergyDensity`

- [IV.P29] Localization Costs Energy — `localization_energy_bound`

- [IV.D78] Mass from Eigenvalue — `MassFromEigenvalue`

- [IV.D79] Frequency from Eigenvalue — `FrequencyFromEigenvalue`

- [IV.T29] Dual Reading — `dual_reading`

- [IV.T30] Energy Conservation — `energy_conservation`

- [IV.D80] CR-Entropy — `CREntropy`

- [IV.P30] Entropy Bound — `entropy_bound`

- [IV.D81] Temporal Direction — `TemporalDirection`

- [IV.T31] Entropy Non-Decreasing — `entropy_nondecreasing`

- [IV.T32] Arrow of Time — `arrow_of_time`

- [IV.P31] Within vs Between — `within_vs_between`

- [IV.R21, IV.R22, IV.R328, IV.R330, IV.R332, IV.R333] structural remarks


## Ground Truth Sources


- Book IV Part III ch20-ch22


---

### `Tau.BookIV.QuantumMechanics.HolomorphicTension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L38-L43)
**structure
Tau.BookIV.QuantumMechanics.HolomorphicTension :Type**


[IV.D76] Energy E[f] = holomorphic tension integral on T².

- energy_numer : ℕ
- energy_denom : ℕ
- denom_pos : self.energy_denom > 0
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHolomorphicTension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L43-L43)
**instance
Tau.BookIV.QuantumMechanics.instReprHolomorphicTension :Repr HolomorphicTension**

Equations
- Tau.BookIV.QuantumMechanics.instReprHolomorphicTension = { reprPrec := Tau.BookIV.QuantumMechanics.instReprHolomorphicTension.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprHolomorphicTension.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L43-L43)
**def
Tau.BookIV.QuantumMechanics.instReprHolomorphicTension.repr :HolomorphicTension → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.HolomorphicTension.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L45-L46)
**def
Tau.BookIV.QuantumMechanics.HolomorphicTension.toFloat
(e : HolomorphicTension)
 :Float**

Equations
- e.toFloat = Float.ofNat e.energy_numer / Float.ofNat e.energy_denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.GraphEnergyDensity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L52-L58)
**structure
Tau.BookIV.QuantumMechanics.GraphEnergyDensity :Type**


[IV.D77] Graph energy density ρ_E(n): energy per mode at depth n.

- density_numer : ℕ
- density_denom : ℕ
- denom_pos : self.density_denom > 0
- depth : ℕ
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprGraphEnergyDensity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L58-L58)
**def
Tau.BookIV.QuantumMechanics.instReprGraphEnergyDensity.repr :GraphEnergyDensity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprGraphEnergyDensity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L58-L58)
**instance
Tau.BookIV.QuantumMechanics.instReprGraphEnergyDensity :Repr GraphEnergyDensity**

Equations
- Tau.BookIV.QuantumMechanics.instReprGraphEnergyDensity = { reprPrec := Tau.BookIV.QuantumMechanics.instReprGraphEnergyDensity.repr }

---

### `Tau.BookIV.QuantumMechanics.GraphEnergyDensity.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L60-L61)
**def
Tau.BookIV.QuantumMechanics.GraphEnergyDensity.toFloat
(d : GraphEnergyDensity)
 :Float**

Equations
- d.toFloat = Float.ofNat d.density_numer / Float.ofNat d.density_denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.LocalizationBound`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L67-L75)
**structure
Tau.BookIV.QuantumMechanics.LocalizationBound :Type**


[IV.P29] E[ψ] ≥ E_vac + ℏ_τ²/(2(Δx)²): localization costs energy.

- e_vac_numer : ℕ
- e_vac_denom : ℕ
- hbar_sq_numer : ℕ
- hbar_sq_denom : ℕ
- vac_denom_pos : self.e_vac_denom > 0
- hbar_denom_pos : self.hbar_sq_denom > 0
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprLocalizationBound`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L75-L75)
**instance
Tau.BookIV.QuantumMechanics.instReprLocalizationBound :Repr LocalizationBound**

Equations
- Tau.BookIV.QuantumMechanics.instReprLocalizationBound = { reprPrec := Tau.BookIV.QuantumMechanics.instReprLocalizationBound.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprLocalizationBound.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L75-L75)
**def
Tau.BookIV.QuantumMechanics.instReprLocalizationBound.repr :LocalizationBound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.localization_energy_bound`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L77-L78)
**theorem
Tau.BookIV.QuantumMechanics.localization_energy_bound
(b : LocalizationBound)
 :b.e_vac_numer ≥ 0**


---

### `Tau.BookIV.QuantumMechanics.MassFromEigenvalue`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L84-L90)
**structure
Tau.BookIV.QuantumMechanics.MassFromEigenvalue :Type**


[IV.D78] Mass from H_∞ eigenvalue via fiber curvature: m_k = λ_k / c²_τ.

- mode_index : ℕ
- mass_numer : ℕ
- mass_denom : ℕ
- denom_pos : self.mass_denom > 0
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprMassFromEigenvalue.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L90-L90)
**def
Tau.BookIV.QuantumMechanics.instReprMassFromEigenvalue.repr :MassFromEigenvalue → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprMassFromEigenvalue`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L90-L90)
**instance
Tau.BookIV.QuantumMechanics.instReprMassFromEigenvalue :Repr MassFromEigenvalue**

Equations
- Tau.BookIV.QuantumMechanics.instReprMassFromEigenvalue = { reprPrec := Tau.BookIV.QuantumMechanics.instReprMassFromEigenvalue.repr }

---

### `Tau.BookIV.QuantumMechanics.FrequencyFromEigenvalue`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L92-L98)
**structure
Tau.BookIV.QuantumMechanics.FrequencyFromEigenvalue :Type**


[IV.D79] Frequency from H_∞ eigenvalue via base evolution: ω_k = λ_k / ℏ_τ.

- mode_index : ℕ
- freq_numer : ℕ
- freq_denom : ℕ
- denom_pos : self.freq_denom > 0
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprFrequencyFromEigenvalue.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L98-L98)
**def
Tau.BookIV.QuantumMechanics.instReprFrequencyFromEigenvalue.repr :FrequencyFromEigenvalue → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprFrequencyFromEigenvalue`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L98-L98)
**instance
Tau.BookIV.QuantumMechanics.instReprFrequencyFromEigenvalue :Repr FrequencyFromEigenvalue**

Equations
- Tau.BookIV.QuantumMechanics.instReprFrequencyFromEigenvalue = { reprPrec := Tau.BookIV.QuantumMechanics.instReprFrequencyFromEigenvalue.repr }

---

### `Tau.BookIV.QuantumMechanics.DualReading`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L104-L113)
**structure
Tau.BookIV.QuantumMechanics.DualReading :Type**


[IV.T29] E_k = m_k c²_τ = ℏ_τ ω_k: one eigenvalue, two readings.
Mass (fiber) and frequency (base) are the SAME eigenvalue read
through different functors, not equated by postulate.

- mode_index : ℕ
- mass : MassFromEigenvalue
- freq : FrequencyFromEigenvalue
- same_mode : self.mass.mode_index = self.freq.mode_index
- index_match : self.mass.mode_index = self.mode_index
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprDualReading`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L113-L113)
**instance
Tau.BookIV.QuantumMechanics.instReprDualReading :Repr DualReading**

Equations
- Tau.BookIV.QuantumMechanics.instReprDualReading = { reprPrec := Tau.BookIV.QuantumMechanics.instReprDualReading.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprDualReading.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L113-L113)
**def
Tau.BookIV.QuantumMechanics.instReprDualReading.repr :DualReading → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.dual_reading`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L115-L116)
**theorem
Tau.BookIV.QuantumMechanics.dual_reading
(d : DualReading)
 :d.mass.mode_index = d.freq.mode_index**


---

### `Tau.BookIV.QuantumMechanics.EnergyConservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L122-L130)
**structure
Tau.BookIV.QuantumMechanics.EnergyConservation :Type**


[IV.T30] Total energy conserved under α-orbit evolution.

- e_initial_numer : ℕ
- e_initial_denom : ℕ
- e_final_numer : ℕ
- e_final_denom : ℕ
- conserved : self.e_initial_numer * self.e_final_denom = self.e_final_numer * self.e_initial_denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEnergyConservation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L130-L130)
**def
Tau.BookIV.QuantumMechanics.instReprEnergyConservation.repr :EnergyConservation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEnergyConservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L130-L130)
**instance
Tau.BookIV.QuantumMechanics.instReprEnergyConservation :Repr EnergyConservation**

Equations
- Tau.BookIV.QuantumMechanics.instReprEnergyConservation = { reprPrec := Tau.BookIV.QuantumMechanics.instReprEnergyConservation.repr }

---

### `Tau.BookIV.QuantumMechanics.energy_conservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L132-L134)
**theorem
Tau.BookIV.QuantumMechanics.energy_conservation
(c : EnergyConservation)
 :c.e_initial_numer * c.e_final_denom = c.e_final_numer * c.e_initial_denom**


---

### `Tau.BookIV.QuantumMechanics.CREntropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L140-L147)
**structure
Tau.BookIV.QuantumMechanics.CREntropy :Type**


[IV.D80] CR-Entropy S(n) = log(# admissible CR-addresses at depth n).
Combinatorial entropy on the finite lattice; grows monotonically.

- entropy_numer : ℕ
- entropy_denom : ℕ
- denom_pos : self.entropy_denom > 0
- depth : ℕ
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCREntropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L147-L147)
**instance
Tau.BookIV.QuantumMechanics.instReprCREntropy :Repr CREntropy**

Equations
- Tau.BookIV.QuantumMechanics.instReprCREntropy = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCREntropy.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCREntropy.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L147-L147)
**def
Tau.BookIV.QuantumMechanics.instReprCREntropy.repr :CREntropy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.CREntropy.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L149-L150)
**def
Tau.BookIV.QuantumMechanics.CREntropy.toFloat
(e : CREntropy)
 :Float**

Equations
- e.toFloat = Float.ofNat e.entropy_numer / Float.ofNat e.entropy_denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.EntropyBoundData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L156-L161)
**structure
Tau.BookIV.QuantumMechanics.EntropyBoundData :Type**


[IV.P30] S[ψ] ≤ ln|A| where A = support of ψ.

- entropy : CREntropy
- support_size : ℕ
- support_pos : self.support_size > 0
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEntropyBoundData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L161-L161)
**def
Tau.BookIV.QuantumMechanics.instReprEntropyBoundData.repr :EntropyBoundData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEntropyBoundData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L161-L161)
**instance
Tau.BookIV.QuantumMechanics.instReprEntropyBoundData :Repr EntropyBoundData**

Equations
- Tau.BookIV.QuantumMechanics.instReprEntropyBoundData = { reprPrec := Tau.BookIV.QuantumMechanics.instReprEntropyBoundData.repr }

---

### `Tau.BookIV.QuantumMechanics.entropy_bound`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L163-L164)
**theorem
Tau.BookIV.QuantumMechanics.entropy_bound
(b : EntropyBoundData)
 :b.support_size > 0**


---

### `Tau.BookIV.QuantumMechanics.TemporalDirection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L170-L175)
**structure
Tau.BookIV.QuantumMechanics.TemporalDirection :Type**


[IV.D81] Temporal direction = increasing refinement.

- depth_before : ℕ
- depth_after : ℕ
- increasing : self.depth_after > self.depth_before
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprTemporalDirection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L175-L175)
**instance
Tau.BookIV.QuantumMechanics.instReprTemporalDirection :Repr TemporalDirection**

Equations
- Tau.BookIV.QuantumMechanics.instReprTemporalDirection = { reprPrec := Tau.BookIV.QuantumMechanics.instReprTemporalDirection.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprTemporalDirection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L175-L175)
**def
Tau.BookIV.QuantumMechanics.instReprTemporalDirection.repr :TemporalDirection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.EntropyMonotonicity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L177-L184)
**structure
Tau.BookIV.QuantumMechanics.EntropyMonotonicity :Type**


[IV.T31] Entropy non-decreasing along the α-orbit.

- s_before : CREntropy
- s_after : CREntropy
- depth_order : self.s_after.depth > self.s_before.depth
- nondecreasing : self.s_after.entropy_numer * self.s_before.entropy_denom ≥ self.s_before.entropy_numer * self.s_after.entropy_denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEntropyMonotonicity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L184-L184)
**instance
Tau.BookIV.QuantumMechanics.instReprEntropyMonotonicity :Repr EntropyMonotonicity**

Equations
- Tau.BookIV.QuantumMechanics.instReprEntropyMonotonicity = { reprPrec := Tau.BookIV.QuantumMechanics.instReprEntropyMonotonicity.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprEntropyMonotonicity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L184-L184)
**def
Tau.BookIV.QuantumMechanics.instReprEntropyMonotonicity.repr :EntropyMonotonicity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.entropy_nondecreasing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L186-L189)
**theorem
Tau.BookIV.QuantumMechanics.entropy_nondecreasing
(m : EntropyMonotonicity)
 :m.s_after.entropy_numer * m.s_before.entropy_denom ≥ m.s_before.entropy_numer * m.s_after.entropy_denom**


---

### `Tau.BookIV.QuantumMechanics.ArrowOfTime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L191-L198)
**structure
Tau.BookIV.QuantumMechanics.ArrowOfTime :Type**


[IV.T32] Arrow of time = direction of increasing refinement + entropy.

- direction : TemporalDirection
- entropy_witness : EntropyMonotonicity
- depth_consistent : self.direction.depth_before = self.entropy_witness.s_before.depth ∧ self.direction.depth_after = self.entropy_witness.s_after.depth
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprArrowOfTime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L198-L198)
**instance
Tau.BookIV.QuantumMechanics.instReprArrowOfTime :Repr ArrowOfTime**

Equations
- Tau.BookIV.QuantumMechanics.instReprArrowOfTime = { reprPrec := Tau.BookIV.QuantumMechanics.instReprArrowOfTime.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprArrowOfTime.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L198-L198)
**def
Tau.BookIV.QuantumMechanics.instReprArrowOfTime.repr :ArrowOfTime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.arrow_of_time`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L200-L202)
**theorem
Tau.BookIV.QuantumMechanics.arrow_of_time
(a : ArrowOfTime)
 :a.direction.depth_after > a.direction.depth_before**


---

### `Tau.BookIV.QuantumMechanics.WithinBetweenLevels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L208-L213)
**structure
Tau.BookIV.QuantumMechanics.WithinBetweenLevels :Type**


[IV.P31] Schrodinger reversible within level; thermodynamics
irreversible between levels. Resolves the paradox of irreversibility.

- within_reversible : Bool
- between_irreversible : Bool
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprWithinBetweenLevels.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L213-L213)
**def
Tau.BookIV.QuantumMechanics.instReprWithinBetweenLevels.repr :WithinBetweenLevels → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprWithinBetweenLevels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L213-L213)
**instance
Tau.BookIV.QuantumMechanics.instReprWithinBetweenLevels :Repr WithinBetweenLevels**

Equations
- Tau.BookIV.QuantumMechanics.instReprWithinBetweenLevels = { reprPrec := Tau.BookIV.QuantumMechanics.instReprWithinBetweenLevels.repr }

---

### `Tau.BookIV.QuantumMechanics.within_vs_between`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L215-L219)
**theorem
Tau.BookIV.QuantumMechanics.within_vs_between
(w : WithinBetweenLevels)

(h1 : w.within_reversible = true)

(h2 : w.between_irreversible = true)
 :w.within_reversible = true ∧ w.between_irreversible = true**


---

### `Tau.BookIV.QuantumMechanics.example_within_between`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean#L231-L231)
**def
Tau.BookIV.QuantumMechanics.example_within_between :WithinBetweenLevels**

Equations
- Tau.BookIV.QuantumMechanics.example_within_between = { }
Instances For
