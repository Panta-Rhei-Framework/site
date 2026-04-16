---
layout: taulib-doc
title: "TauLib.BookIV.Sectors.SectorParameters"
permalink: /verify/taulib/docs/book-iv-sectors-sector-parameters/
lane: verify
module_name: "TauLib.BookIV.Sectors.SectorParameters"
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

# TauLib.BookIV.Sectors.SectorParameters


Sector Physics Template: the 4 defining parameters for each of the 5 sectors
at the E₁ (physics) enrichment level.

## Registry Cross-References


- [IV.D01] Sector Physics Template — `SectorPhysics`, `PolaritySign`

- [IV.D02] EM Sector at E₁ — `em_sector`

- [IV.D03] Strong Sector at E₁ — `strong_sector`

- [IV.D04] Higgs Sector at E₁ — `higgs_sector`

- [IV.D05] Gravity Sector at E₁ — `gravity_sector`

- [IV.D06] Weak Sector at E₁ — `weak_sector`


## Mathematical Content


Book III established the abstract 4+1 sector template (III.D13) via character-lattice
counting. Book IV instantiates each sector with its **four defining parameters**:

- **Self-coupling κ(S;d)** — rational function of ι<sub>τ</sub> at primorial depth d

- **Polarity signature** — χ₊-dominant, balanced, χ₋-dominant, or crossing

- **Primorial depth** — the level d ∈ {1, 2, 3} at which the coupling operates

- **Physical force** — the E₁ incarnation of the sector


The five generators split into temporal (base τ¹) and spatial (fiber T²):


Sector
Gen
ABCD
Carrier
κ(S;d)
Polarity
Depth


B (EM)
γ
B
Fiber T²
ι<sub>τ</sub>²
χ₊-dom
2


C (Strong)
η
C
Fiber T²
ι<sub>τ</sub>³/(1−ι<sub>τ</sub>)
χ₋-dom
3


ω (Higgs)
γ∩η
B∩C
Fiber T²
ι<sub>τ</sub>³/(1+ι<sub>τ</sub>)
crossing
3


D (Gravity)
α
D
Base τ¹
1−ι<sub>τ</sub>
χ₊-dom
1


A (Weak)
π
A
Base τ¹
ι<sub>τ</sub>
balanced
1


All couplings are determined by ι<sub>τ</sub> = 2/(π+e) ≈ 0.341304 (No Knobs, III.T08).

## Ground Truth Sources


- physics_layer_sector_instantiation.md §4: 4+1 sector template at E₁

- temporal_spatial_decomposition.md: generator-carrier correspondence

- Book III editorial logbook Decision #31: canonical force mapping (LOCKED)


---

### `Tau.BookIV.Sectors.PolaritySign`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L55-L66)
**inductive
Tau.BookIV.Sectors.PolaritySign :Type**


[IV.D01] Spectral polarity signature of a sector.
Determines which boundary characters dominate the sector's physics.

- ChiPlus : PolaritySign
χ₊-dominant: multiplicative/spreading characters dominate.

- Balanced : PolaritySign
Balanced: equal χ₊ and χ₋ content (pol = 1).

- ChiMinus : PolaritySign
χ₋-dominant: additive/tightening characters dominate.

- Crossing : PolaritySign
Crossing: both lobes active simultaneously (ω-sector only).

Instances For

---

### `Tau.BookIV.Sectors.instReprPolaritySign`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L66-L66)
**instance
Tau.BookIV.Sectors.instReprPolaritySign :Repr PolaritySign**

Equations
- Tau.BookIV.Sectors.instReprPolaritySign = { reprPrec := Tau.BookIV.Sectors.instReprPolaritySign.repr }

---

### `Tau.BookIV.Sectors.instReprPolaritySign.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L66-L66)
**def
Tau.BookIV.Sectors.instReprPolaritySign.repr :PolaritySign → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.instDecidableEqPolaritySign`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L66-L66)
**instance
Tau.BookIV.Sectors.instDecidableEqPolaritySign :DecidableEq PolaritySign**

Equations
- Tau.BookIV.Sectors.instDecidableEqPolaritySign x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Sectors.instBEqPolaritySign`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L66-L66)
**instance
Tau.BookIV.Sectors.instBEqPolaritySign :BEq PolaritySign**

Equations
- Tau.BookIV.Sectors.instBEqPolaritySign = { beq := Tau.BookIV.Sectors.instBEqPolaritySign.beq }

---

### `Tau.BookIV.Sectors.instBEqPolaritySign.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L66-L66)
**def
Tau.BookIV.Sectors.instBEqPolaritySign.beq :PolaritySign → PolaritySign → Bool**

Equations
- Tau.BookIV.Sectors.instBEqPolaritySign.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Sectors.SectorPhysics`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L72-L90)
**structure
Tau.BookIV.Sectors.SectorPhysics :Type**


[IV.D01] The four defining parameters of a sector at E₁.
Every sector is completely characterized by these four values.
All couplings are rational functions of ι<sub>τ</sub>.

- sector : BookIII.Sectors.Sector
The abstract sector (from Book III Decomposition).

- generator : Kernel.Generator
The kernel generator seeding this sector.

- depth : Denotation.TauIdx
Primorial depth at which the coupling operates.

- polarity : PolaritySign
Spectral polarity signature.

- coupling_numer : ℕ
Self-coupling numerator (scaled by coupling_denom).

- coupling_denom : ℕ
Self-coupling denominator (common scale).

- denom_pos : self.coupling_denom > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Sectors.instReprSectorPhysics`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L90-L90)
**instance
Tau.BookIV.Sectors.instReprSectorPhysics :Repr SectorPhysics**

Equations
- Tau.BookIV.Sectors.instReprSectorPhysics = { reprPrec := Tau.BookIV.Sectors.instReprSectorPhysics.repr }

---

### `Tau.BookIV.Sectors.instReprSectorPhysics.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L90-L90)
**def
Tau.BookIV.Sectors.instReprSectorPhysics.repr :SectorPhysics → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.CouplingScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L96-L98)@[reducible, inline]

**abbrev
Tau.BookIV.Sectors.CouplingScale :ℕ**


The common denominator for coupling computations.
We use 10¹² to preserve precision through multiplication.
Equations
- Tau.BookIV.Sectors.CouplingScale = 1000000000000
Instances For

---

### `Tau.BookIV.Sectors.iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L100-L101)@[reducible, inline]

**abbrev
Tau.BookIV.Sectors.iota :ℕ**


ι<sub>τ</sub> numerator at scale 10⁶ (from Iota.lean).
Equations
- Tau.BookIV.Sectors.iota = Tau.Boundary.iota_tau_numer
Instances For

---

### `Tau.BookIV.Sectors.iotaD`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L103-L104)@[reducible, inline]

**abbrev
Tau.BookIV.Sectors.iotaD :ℕ**


ι<sub>τ</sub> denominator at scale 10⁶ (from Iota.lean).
Equations
- Tau.BookIV.Sectors.iotaD = Tau.Boundary.iota_tau_denom
Instances For

---

### `Tau.BookIV.Sectors.iota_sq_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L106-L107)
**def
Tau.BookIV.Sectors.iota_sq_numer :ℕ**


ι<sub>τ</sub>² numerator: iota² = 341304² = 116,594,274,681.
Equations
- Tau.BookIV.Sectors.iota_sq_numer = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Sectors.iota_sq_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L109-L110)
**def
Tau.BookIV.Sectors.iota_sq_denom :ℕ**


ι<sub>τ</sub>² denominator: 10¹².
Equations
- Tau.BookIV.Sectors.iota_sq_denom = Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookIV.Sectors.iota_cu_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L112-L113)
**def
Tau.BookIV.Sectors.iota_cu_numer :ℕ**


ι<sub>τ</sub>³ numerator: iota³.
Equations
- Tau.BookIV.Sectors.iota_cu_numer = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Sectors.iota_cu_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L115-L116)
**def
Tau.BookIV.Sectors.iota_cu_denom :ℕ**


ι<sub>τ</sub>³ denominator: 10¹⁸.
Equations
- Tau.BookIV.Sectors.iota_cu_denom = Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookIV.Sectors.em_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L122-L134)
**def
Tau.BookIV.Sectors.em_sector :SectorPhysics**


[IV.D02] **EM Sector (B)**: γ-generator, electromagnetic force.
Self-coupling κ(B;2) = ι<sub>τ</sub>².
Polarity: χ₊-dominant (spreading/multiplicative).
Depth: 2 (second primorial level).
Physical: photon transport, Maxwell equations, fine structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.strong_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L135-L151)
**def
Tau.BookIV.Sectors.strong_sector :SectorPhysics**


[IV.D03] **Strong Sector (C)**: η-generator, strong force.
Self-coupling κ(C;3) = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>).
Polarity: χ₋-dominant (tightening/additive).
Depth: 3 (third primorial level).
Physical: color holonomy, confinement, mass gap.
The (1−ι<sub>τ</sub>) denominator is the structural signature of confinement.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.higgs_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L152-L166)
**def
Tau.BookIV.Sectors.higgs_sector :SectorPhysics**


[IV.D04] **Higgs Sector (ω)**: γ∩η crossing, Higgs/mass mechanism.
Self-coupling κ(B,C) = ι<sub>τ</sub>³/(1+ι<sub>τ</sub>).
Polarity: crossing (both lobes active simultaneously).
Depth: 3 (third primorial level).
Physical: mass generation, dense spatial occupancy.
The unique +1 derived sector from the lemniscate crossing.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.gravity_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L167-L179)
**def
Tau.BookIV.Sectors.gravity_sector :SectorPhysics**


[IV.D05] **Gravity Sector (D)**: α-generator, gravitational force.
Self-coupling κ(D;1) = 1−ι<sub>τ</sub>.
Polarity: χ₊-dominant.
Depth: 1 (first primorial level).
Physical: frame holonomy, temporal flow, G = (c³/ℏ)·ι<sub>τ</sub>².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.weak_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L180-L193)
**def
Tau.BookIV.Sectors.weak_sector :SectorPhysics**


[IV.D06] **Weak Sector (A)**: π-generator, weak force.
Self-coupling κ(A;1) = ι<sub>τ</sub>.
Polarity: balanced (unique sector with pol = 1).
Depth: 1 (first primorial level).
Physical: temporal arrow, parity violation, beta decay.
The master constant ι<sub>τ</sub> itself IS the weak self-coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.all_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L198-L200)
**def
Tau.BookIV.Sectors.all_sectors :List SectorPhysics**


All five sector instantiations as a list.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.sector_physics`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L202-L209)
**def
Tau.BookIV.Sectors.sector_physics
(s : BookIII.Sectors.Sector)
 :SectorPhysics**


Lookup sector physics by abstract sector.
Equations
- Tau.BookIV.Sectors.sector_physics Tau.BookIII.Sectors.Sector.D = Tau.BookIV.Sectors.gravity_sector
- Tau.BookIV.Sectors.sector_physics Tau.BookIII.Sectors.Sector.A = Tau.BookIV.Sectors.weak_sector
- Tau.BookIV.Sectors.sector_physics Tau.BookIII.Sectors.Sector.B = Tau.BookIV.Sectors.em_sector
- Tau.BookIV.Sectors.sector_physics Tau.BookIII.Sectors.Sector.C = Tau.BookIV.Sectors.strong_sector
- Tau.BookIV.Sectors.sector_physics Tau.BookIII.Sectors.Sector.Omega = Tau.BookIV.Sectors.higgs_sector
Instances For

---

### `Tau.BookIV.Sectors.gen_sector_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L215-L220)
**theorem
Tau.BookIV.Sectors.gen_sector_injective :gravity_sector.generator ≠ weak_sector.generator ∧ weak_sector.generator ≠ em_sector.generator ∧ em_sector.generator ≠ strong_sector.generator**


Generator-sector correspondence is injective on primitive sectors.

---

### `Tau.BookIV.Sectors.all_couplings_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L222-L230)
**theorem
Tau.BookIV.Sectors.all_couplings_pos :gravity_sector.coupling_numer > 0 ∧ weak_sector.coupling_numer > 0 ∧ em_sector.coupling_numer > 0 ∧ strong_sector.coupling_numer > 0 ∧ higgs_sector.coupling_numer > 0**


Every sector has a positive coupling.

---

### `Tau.BookIV.Sectors.temporal_depth_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L232-L235)
**theorem
Tau.BookIV.Sectors.temporal_depth_one :gravity_sector.depth = 1 ∧ weak_sector.depth = 1**


Temporal sectors have depth 1; spatial sectors have depth ≥ 2.

---

### `Tau.BookIV.Sectors.spatial_depth_ge_two`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L237-L239)
**theorem
Tau.BookIV.Sectors.spatial_depth_ge_two :em_sector.depth ≥ 2 ∧ strong_sector.depth ≥ 2 ∧ higgs_sector.depth ≥ 2**


---

### `Tau.BookIV.Sectors.weak_unique_balanced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L241-L248)
**theorem
Tau.BookIV.Sectors.weak_unique_balanced :weak_sector.polarity = PolaritySign.Balanced ∧ gravity_sector.polarity ≠ PolaritySign.Balanced ∧ em_sector.polarity ≠ PolaritySign.Balanced ∧ strong_sector.polarity ≠ PolaritySign.Balanced ∧ higgs_sector.polarity ≠ PolaritySign.Balanced**


The weak sector is the unique balanced sector.

---

### `Tau.BookIV.Sectors.SectorPhysics.coupling_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SectorParameters.lean#L254-L256)
**def
Tau.BookIV.Sectors.SectorPhysics.coupling_float
(s : SectorPhysics)
 :Float**


Coupling as a Float (for display purposes).
Equations
- s.coupling_float = Float.ofNat s.coupling_numer / Float.ofNat s.coupling_denom
Instances For
