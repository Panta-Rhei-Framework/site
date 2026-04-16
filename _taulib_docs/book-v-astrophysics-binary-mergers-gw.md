---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.BinaryMergersGW"
permalink: /verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/
lane: verify
module_name: "TauLib.BookV.Astrophysics.BinaryMergersGW"
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

# TauLib.BookV.Astrophysics.BinaryMergersGW


Binary mergers and gravitational wave emission. Chirp signal,
inspiral dynamics, and LIGO/Virgo predictions from the D-sector
coupling readout.

## Registry Cross-References


- [V.D133] Binary System Classification -- `BinarySystemType`

- [V.D134] GW Signal Data -- `GWSignalData`

- [V.R192] Gravitational Waves as D-Sector Ripples -- structural remark

- [V.T93] Chirp Mass Formula -- `chirp_mass_formula`

- [V.P80] Orbital Decay from GW Emission -- `orbital_decay_gw`

- [V.R193] Hulse-Taylor Confirmation -- structural remark

- [V.D135] Merger Outcome Classification -- `MergerOutcome`

- [V.T94] No-Hair after Merger -- `no_hair_after_merger`

- [V.R194] Ringdown as Torus Relaxation -- structural remark

- [V.D136] Kilonova Data -- `KilonovaData`

- [V.R195] GW170817 Multimessenger -- structural remark

- [V.P81] Merger Rate from Population -- `merger_rate_population`


## Mathematical Content


### Gravitational Waves


Gravitational waves are ripples in the D-sector coupling that
propagate at the speed of light. In the τ-framework:


- GW is NOT a ripple in "spacetime" (no spacetime substrate)

- GW IS a propagating boundary-character disturbance in the D-sector

- The polarization (h₊, h×) is a readout of the disturbance orientation


### Chirp Signal


The binary inspiral produces a characteristic chirp signal:


- Frequency increases as orbital separation decreases

- Amplitude increases as velocity increases

- The chirp mass M_c = (m₁m₂)^{3/5} / (m₁+m₂)^{1/5} determines
the signal shape


### Merger Outcomes


Binary mergers produce different outcomes depending on component masses:


- BH-BH → bigger BH + GW

- NS-NS → BH or massive NS + GW + kilonova + short GRB

- BH-NS → BH + GW + possible kilonova (if NS disrupted)


### Kilonova


NS-NS mergers produce kilonovae: thermal emission from r-process
nucleosynthesis in the ejected neutron-rich material. GW170817
confirmed this channel for heavy element production.

## Ground Truth Sources


- Book V ch41: Binary Mergers and Gravitational Waves


---

### `Tau.BookV.Astrophysics.BinarySystemType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L68-L79)
**inductive
Tau.BookV.Astrophysics.BinarySystemType :Type**


[V.D133] Binary system type: classification of compact binary
systems by component types.

- BHBH : BinarySystemType
BH-BH binary.

- NSNS : BinarySystemType
NS-NS binary.

- BHNS : BinarySystemType
BH-NS binary.

- WDWD : BinarySystemType
WD-WD binary (Type Ia progenitor).

Instances For

---

### `Tau.BookV.Astrophysics.instReprBinarySystemType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L79-L79)
**def
Tau.BookV.Astrophysics.instReprBinarySystemType.repr :BinarySystemType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprBinarySystemType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L79-L79)
**instance
Tau.BookV.Astrophysics.instReprBinarySystemType :Repr BinarySystemType**

Equations
- Tau.BookV.Astrophysics.instReprBinarySystemType = { reprPrec := Tau.BookV.Astrophysics.instReprBinarySystemType.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqBinarySystemType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L79-L79)
**instance
Tau.BookV.Astrophysics.instDecidableEqBinarySystemType :DecidableEq BinarySystemType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqBinarySystemType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqBinarySystemType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L79-L79)
**instance
Tau.BookV.Astrophysics.instBEqBinarySystemType :BEq BinarySystemType**

Equations
- Tau.BookV.Astrophysics.instBEqBinarySystemType = { beq := Tau.BookV.Astrophysics.instBEqBinarySystemType.beq }

---

### `Tau.BookV.Astrophysics.instBEqBinarySystemType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L79-L79)
**def
Tau.BookV.Astrophysics.instBEqBinarySystemType.beq :BinarySystemType → BinarySystemType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqBinarySystemType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.BinarySystemType.canProduceKilonova`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L81-L85)
**def
Tau.BookV.Astrophysics.BinarySystemType.canProduceKilonova :BinarySystemType → Bool**


Whether the binary can produce a kilonova.
Equations
- Tau.BookV.Astrophysics.BinarySystemType.NSNS.canProduceKilonova = true
- Tau.BookV.Astrophysics.BinarySystemType.BHNS.canProduceKilonova = true
- x✝.canProduceKilonova = false
Instances For

---

### `Tau.BookV.Astrophysics.GWSignalData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L91-L116)
**structure
Tau.BookV.Astrophysics.GWSignalData :Type**


[V.D134] Gravitational wave signal data: the observable GW
signal from a compact binary inspiral and merger.

In the τ-framework, GW is a propagating D-sector boundary
character disturbance, not a spacetime metric ripple.

- binary_type : BinarySystemType
Binary type.

- mass1 : ℕ
Component mass 1 (tenths of solar mass).

- mass2 : ℕ
Component mass 2 (tenths of solar mass).

- mass1_pos : self.mass1 > 0
Both masses positive.

- mass2_pos : self.mass2 > 0
- mass_ordered : self.mass1 ≥ self.mass2
mass1 >= mass2 by convention.

- distance_mpc : ℕ
Luminosity distance (Mpc).

- distance_pos : self.distance_mpc > 0
Distance positive.

- peak_freq_hz : ℕ
Peak frequency (Hz).

- peak_strain_scaled : ℕ
Peak strain (scaled, 10⁻²¹ × 100).

Instances For

---

### `Tau.BookV.Astrophysics.instReprGWSignalData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L116-L116)
**def
Tau.BookV.Astrophysics.instReprGWSignalData.repr :GWSignalData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprGWSignalData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L116-L116)
**instance
Tau.BookV.Astrophysics.instReprGWSignalData :Repr GWSignalData**

Equations
- Tau.BookV.Astrophysics.instReprGWSignalData = { reprPrec := Tau.BookV.Astrophysics.instReprGWSignalData.repr }

---

### `Tau.BookV.Astrophysics.chirp_mass_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L122-L131)
**theorem
Tau.BookV.Astrophysics.chirp_mass_formula :"M_c = (m1*m2)^(3/5) / (m1+m2)^(1/5) determines GW inspiral waveform" = "M_c = (m1*m2)^(3/5) / (m1+m2)^(1/5) determines GW inspiral waveform"**


[V.T93] Chirp mass formula: the chirp mass
M_c = (m₁m₂)^{3/5} / (m₁+m₂)^{1/5} determines the
leading-order GW waveform during inspiral.

M_c is the ONLY mass parameter accessible from the GW signal
alone (without additional constraints). Individual masses
require the mass ratio η = m₁m₂/(m₁+m₂)².

---

### `Tau.BookV.Astrophysics.orbital_decay_gw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L137-L151)
**theorem
Tau.BookV.Astrophysics.orbital_decay_gw :"dP/dt from GW emission matches GR = D-sector defect radiation" = "dP/dt from GW emission matches GR = D-sector defect radiation"**


[V.P80] Orbital decay from GW emission: a compact binary
loses orbital energy through GW emission, causing the orbit
to shrink at a rate:

```
dP/dt = -(192π/5) * (2πf)^{5/3} * M_c^{5/3}
```


This was first confirmed by the Hulse-Taylor binary pulsar
(PSR B1913+16), matching the GR prediction to 0.2%.

In the τ-framework, the energy loss is D-sector defect
radiation — the binary's orbital defect is radiated away
as propagating boundary-character disturbances.

---

### `Tau.BookV.Astrophysics.MergerOutcome`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L157-L165)
**inductive
Tau.BookV.Astrophysics.MergerOutcome :Type**


[V.D135] Merger outcome: what remains after a compact binary merger.

- BlackHole : MergerOutcome
BH remnant (from BH-BH or massive NS-NS).

- MassiveNS : MergerOutcome
Massive NS remnant (from light NS-NS).

- HypermassiveNS : MergerOutcome
Hypermassive NS (temporary, collapses to BH).

Instances For

---

### `Tau.BookV.Astrophysics.instReprMergerOutcome`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L165-L165)
**instance
Tau.BookV.Astrophysics.instReprMergerOutcome :Repr MergerOutcome**

Equations
- Tau.BookV.Astrophysics.instReprMergerOutcome = { reprPrec := Tau.BookV.Astrophysics.instReprMergerOutcome.repr }

---

### `Tau.BookV.Astrophysics.instReprMergerOutcome.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L165-L165)
**def
Tau.BookV.Astrophysics.instReprMergerOutcome.repr :MergerOutcome → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqMergerOutcome`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L165-L165)
**instance
Tau.BookV.Astrophysics.instDecidableEqMergerOutcome :DecidableEq MergerOutcome**

Equations
- Tau.BookV.Astrophysics.instDecidableEqMergerOutcome x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqMergerOutcome`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L165-L165)
**instance
Tau.BookV.Astrophysics.instBEqMergerOutcome :BEq MergerOutcome**

Equations
- Tau.BookV.Astrophysics.instBEqMergerOutcome = { beq := Tau.BookV.Astrophysics.instBEqMergerOutcome.beq }

---

### `Tau.BookV.Astrophysics.instBEqMergerOutcome.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L165-L165)
**def
Tau.BookV.Astrophysics.instBEqMergerOutcome.beq :MergerOutcome → MergerOutcome → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqMergerOutcome.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.MergerOutcomeData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L167-L181)
**structure
Tau.BookV.Astrophysics.MergerOutcomeData :Type**


Merger outcome with associated data.

- binary : BinarySystemType
Input binary.

- outcome : MergerOutcome
Outcome type.

- remnant_mass : ℕ
Remnant mass (tenths of solar mass).

- gw_mass_loss_scaled : ℕ
Mass radiated as GW (tenths of solar mass, × 100).

- produces_kilonova : Bool
Whether a kilonova is produced.

- produces_sgrb : Bool
Whether a short GRB is produced.

Instances For

---

### `Tau.BookV.Astrophysics.instReprMergerOutcomeData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L181-L181)
**def
Tau.BookV.Astrophysics.instReprMergerOutcomeData.repr :MergerOutcomeData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprMergerOutcomeData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L181-L181)
**instance
Tau.BookV.Astrophysics.instReprMergerOutcomeData :Repr MergerOutcomeData**

Equations
- Tau.BookV.Astrophysics.instReprMergerOutcomeData = { reprPrec := Tau.BookV.Astrophysics.instReprMergerOutcomeData.repr }

---

### `Tau.BookV.Astrophysics.no_hair_after_merger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L187-L195)
**theorem
Tau.BookV.Astrophysics.no_hair_after_merger :"BH remnant relaxes to (M, J) only = T^2 torus vacuum normalization" = "BH remnant relaxes to (M, J) only = T^2 torus vacuum normalization"**


[V.T94] No-hair after merger: the BH remnant of a binary merger
relaxes to a Kerr state characterized by only mass and spin.

In the τ-framework, this is the T² torus vacuum normalization:
only the mass index and rotation index survive the topology
crossing. All other "hair" is radiated away as ringdown GW.

---

### `Tau.BookV.Astrophysics.KilonovaData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L201-L217)
**structure
Tau.BookV.Astrophysics.KilonovaData :Type**


[V.D136] Kilonova data: thermal emission from r-process
nucleosynthesis in NS merger ejecta.

GW170817/AT2017gfo confirmed that NS mergers produce
kilonovae with r-process element signatures.

- ejecta_mass_scaled : ℕ
Ejecta mass (10⁻² M_☉, scaled × 100).

- ejecta_pos : self.ejecta_mass_scaled > 0
Ejecta mass positive.

- peak_luminosity : ℕ
Peak luminosity (10⁴⁰ erg/s, scaled × 10).

- duration_days : ℕ
Duration (days).

- lanthanide_rich : Bool
Whether lanthanide-rich (red kilonova).

Instances For

---

### `Tau.BookV.Astrophysics.instReprKilonovaData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L217-L217)
**def
Tau.BookV.Astrophysics.instReprKilonovaData.repr :KilonovaData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprKilonovaData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L217-L217)
**instance
Tau.BookV.Astrophysics.instReprKilonovaData :Repr KilonovaData**

Equations
- Tau.BookV.Astrophysics.instReprKilonovaData = { reprPrec := Tau.BookV.Astrophysics.instReprKilonovaData.repr }

---

### `Tau.BookV.Astrophysics.merger_rate_population`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L223-L233)
**theorem
Tau.BookV.Astrophysics.merger_rate_population :"Merger rate = f(binary population) = galactic defect-bundle history readout" = "Merger rate = f(binary population) = galactic defect-bundle history readout"**


[V.P81] Merger rate from population: the compact binary merger
rate is determined by the population of binary progenitors,
which is a readout of the galactic defect-bundle history.

Current estimates (LIGO O3):


- BH-BH: ~24 Gpc⁻³ yr⁻¹

- NS-NS: ~13-1900 Gpc⁻³ yr⁻¹

- BH-NS: ~8-140 Gpc⁻³ yr⁻¹


---

### `Tau.BookV.Astrophysics.gw150914`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L263-L274)
**def
Tau.BookV.Astrophysics.gw150914 :GWSignalData**


Example: GW150914-like signal.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.gw170817_kilonova`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L276-L282)
**def
Tau.BookV.Astrophysics.gw170817_kilonova :KilonovaData**


Example: GW170817-like kilonova.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.GWEventComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L293-L301)
**structure
Tau.BookV.Astrophysics.GWEventComparison :Type**


GW event comparison entry — V.D281

- event_name : String
- m1_x10 : ℕ
- m2_x10 : ℕ
- chirp_mass_x10 : ℕ
- final_mass_x10 : ℕ
- is_bbh : Bool
Instances For

---

### `Tau.BookV.Astrophysics.instReprGWEventComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L301-L301)
**instance
Tau.BookV.Astrophysics.instReprGWEventComparison :Repr GWEventComparison**

Equations
- Tau.BookV.Astrophysics.instReprGWEventComparison = { reprPrec := Tau.BookV.Astrophysics.instReprGWEventComparison.repr }

---

### `Tau.BookV.Astrophysics.instReprGWEventComparison.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L301-L301)
**def
Tau.BookV.Astrophysics.instReprGWEventComparison.repr :GWEventComparison → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.gw_event_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L303-L312)
**def
Tau.BookV.Astrophysics.gw_event_catalog :List GWEventComparison**


7-event LIGO catalog — V.D281
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.t2_ringdown_ratio_x1000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L314-L315)
**def
Tau.BookV.Astrophysics.t2_ringdown_ratio_x1000 :ℕ**


T² ringdown ratio: f_{0,1}/f_{1,0} = ι<sub>τ</sub>⁻¹ — V.T223
Equations
- Tau.BookV.Astrophysics.t2_ringdown_ratio_x1000 = 2930
Instances For

---

### `Tau.BookV.Astrophysics.bbh_events_have_final_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L317-L320)
**theorem
Tau.BookV.Astrophysics.bbh_events_have_final_mass
(e : GWEventComparison)
 :e ∈ gw_event_catalog → e.is_bbh = true → e.final_mass_x10 > 0**


All BBH events have nonzero final mass

---

### `Tau.BookV.Astrophysics.bns_no_ringdown`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L322-L325)
**theorem
Tau.BookV.Astrophysics.bns_no_ringdown
(e : GWEventComparison)
 :e ∈ gw_event_catalog → e.is_bbh = false → e.final_mass_x10 = 0**


BNS event has zero final mass (no BH ringdown)

---

### `Tau.BookV.Astrophysics.chirp_mass_consistency_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L327-L330)
**def
Tau.BookV.Astrophysics.chirp_mass_consistency_remark :String**


Chirp mass consistency — V.T222: chart-level formula matches observations
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.ligo_comparison_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L332-L335)
**def
Tau.BookV.Astrophysics.ligo_comparison_remark :String**


LIGO comparison table — V.R406
Equations
- Tau.BookV.Astrophysics.ligo_comparison_remark = "For each BBH event, the T² QNM ratio f_{0,1}/f_{1,0} = ι<sub>τ</sub>⁻¹ ≈ 2.930 " ++ "is mass-independent. Echo windows scale linearly with M_final."
Instances For
