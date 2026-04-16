---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.Supernovae"
permalink: /verify/taulib/docs/book-v-astrophysics-supernovae/
lane: verify
module_name: "TauLib.BookV.Astrophysics.Supernovae"
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

# TauLib.BookV.Astrophysics.Supernovae


Supernovae from coherence horizon crossing. Core collapse, Type Ia
thermonuclear explosions, nucleosynthesis, and the role of supernovae
as distance indicators — all as τ-readouts.

## Registry Cross-References


- [V.D126] Supernova Classification -- `SupernovaType`

- [V.T89] Core Collapse as Topology Transition -- `core_collapse_topology`

- [V.R181] Iron Core Threshold -- structural remark

- [V.D127] Core Collapse Mechanism -- `CoreCollapseMechanism`

- [V.P73] Neutrino Burst from Defect Release -- `neutrino_from_defect`

- [V.R182] SN 1987A Neutrinos Consistent -- structural remark

- [V.P74] Type Ia as Chandrasekhar Crossing -- `type_ia_chandrasekhar`

- [V.D128] Nucleosynthesis Products -- `NucleosynthesisProducts`

- [V.R183] r-Process from Neutron Star Mergers -- structural remark

- [V.P75] Standardizable Candle from Fixed Physics -- `standardizable_candle`

- [V.P76] SN Rate from Star Formation History -- `sn_rate_sfh`

- [V.R184] Supernova Remnants as Boundary Imprints -- structural remark


## Mathematical Content


### Core Collapse Mechanism


When a massive star's iron core exceeds the Chandrasekhar mass,
electron degeneracy can no longer support the S² boundary topology.
The core undergoes a topology transition:

- Inner core collapses to nuclear density (~10¹⁴ g/cm³)

- Bounce creates an outward-propagating shock

- Neutrino heating revives the shock (delayed mechanism)

- Envelope is expelled; remnant is NS or BH


In the τ-framework, the collapse is a defect-cascade event:
the stored compression defect is released explosively when the
boundary topology can no longer be maintained.

### Type Ia Supernovae


Type Ia SNe are thermonuclear explosions of white dwarfs that
accrete mass to the Chandrasekhar limit. The standardizable-candle
property arises because the explosion is triggered at a FIXED
mass threshold — the same Chandrasekhar limit in every case.

### Nucleosynthesis


Supernova explosions create heavy elements:


- Core collapse SNe: elements up to Ni/Fe plus r-process

- Type Ia: mainly Fe-group elements

- NS mergers (Book V ch41): r-process heavy elements (Au, Pt, U)


## Ground Truth Sources


- Book V ch39: Supernovae


---

### `Tau.BookV.Astrophysics.SupernovaType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L68-L78)
**inductive
Tau.BookV.Astrophysics.SupernovaType :Type**


[V.D126] Supernova type classification.

- TypeIa : SupernovaType
Type Ia: thermonuclear white dwarf explosion.

- TypeII : SupernovaType
Type II: core collapse of massive star with H envelope.

- TypeIb : SupernovaType
Type Ib: core collapse, H-stripped.

- TypeIc : SupernovaType
Type Ic: core collapse, H and He stripped.

Instances For

---

### `Tau.BookV.Astrophysics.instReprSupernovaType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L78-L78)
**def
Tau.BookV.Astrophysics.instReprSupernovaType.repr :SupernovaType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprSupernovaType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L78-L78)
**instance
Tau.BookV.Astrophysics.instReprSupernovaType :Repr SupernovaType**

Equations
- Tau.BookV.Astrophysics.instReprSupernovaType = { reprPrec := Tau.BookV.Astrophysics.instReprSupernovaType.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqSupernovaType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L78-L78)
**instance
Tau.BookV.Astrophysics.instDecidableEqSupernovaType :DecidableEq SupernovaType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqSupernovaType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqSupernovaType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L78-L78)
**instance
Tau.BookV.Astrophysics.instBEqSupernovaType :BEq SupernovaType**

Equations
- Tau.BookV.Astrophysics.instBEqSupernovaType = { beq := Tau.BookV.Astrophysics.instBEqSupernovaType.beq }

---

### `Tau.BookV.Astrophysics.instBEqSupernovaType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L78-L78)
**def
Tau.BookV.Astrophysics.instBEqSupernovaType.beq :SupernovaType → SupernovaType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqSupernovaType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.SupernovaType.isCoreCollapse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L80-L85)
**def
Tau.BookV.Astrophysics.SupernovaType.isCoreCollapse :SupernovaType → Bool**


Whether the SN is a core-collapse type.
Equations
- Tau.BookV.Astrophysics.SupernovaType.TypeIa.isCoreCollapse = false
- Tau.BookV.Astrophysics.SupernovaType.TypeII.isCoreCollapse = true
- Tau.BookV.Astrophysics.SupernovaType.TypeIb.isCoreCollapse = true
- Tau.BookV.Astrophysics.SupernovaType.TypeIc.isCoreCollapse = true
Instances For

---

### `Tau.BookV.Astrophysics.SupernovaType.isThermonuclear`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L87-L90)
**def
Tau.BookV.Astrophysics.SupernovaType.isThermonuclear :SupernovaType → Bool**


Whether the SN is thermonuclear (Type Ia).
Equations
- Tau.BookV.Astrophysics.SupernovaType.TypeIa.isThermonuclear = true
- x✝.isThermonuclear = false
Instances For

---

### `Tau.BookV.Astrophysics.core_collapse_topology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L96-L104)
**theorem
Tau.BookV.Astrophysics.core_collapse_topology
(sn : SupernovaType)

(hcc : sn.isCoreCollapse = true)
 :sn.isCoreCollapse = true**


[V.T89] Core collapse as topology transition: when the iron
core exceeds M_Ch, the S² boundary topology fails and the
defect cascade produces a supernova explosion.

The core collapse is the stellar-mass analog of the coherence
horizon crossing discussed in TOVPhaseBoundary.

---

### `Tau.BookV.Astrophysics.CollapsePhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L110-L124)
**inductive
Tau.BookV.Astrophysics.CollapsePhase :Type**


Core collapse phase.

- IronCoreGrowth : CollapsePhase
Iron core growth to M_Ch.

- ElectronCapture : CollapsePhase
Electron capture and core collapse.

- Bounce : CollapsePhase
Bounce at nuclear density.

- ShockRevival : CollapsePhase
Shock revival by neutrino heating.

- EnvelopeEjection : CollapsePhase
Envelope ejection.

- RemnantFormation : CollapsePhase
Remnant formation (NS or BH).

Instances For

---

### `Tau.BookV.Astrophysics.instReprCollapsePhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L124-L124)
**instance
Tau.BookV.Astrophysics.instReprCollapsePhase :Repr CollapsePhase**

Equations
- Tau.BookV.Astrophysics.instReprCollapsePhase = { reprPrec := Tau.BookV.Astrophysics.instReprCollapsePhase.repr }

---

### `Tau.BookV.Astrophysics.instReprCollapsePhase.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L124-L124)
**def
Tau.BookV.Astrophysics.instReprCollapsePhase.repr :CollapsePhase → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqCollapsePhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L124-L124)
**instance
Tau.BookV.Astrophysics.instDecidableEqCollapsePhase :DecidableEq CollapsePhase**

Equations
- Tau.BookV.Astrophysics.instDecidableEqCollapsePhase x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqCollapsePhase.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L124-L124)
**def
Tau.BookV.Astrophysics.instBEqCollapsePhase.beq :CollapsePhase → CollapsePhase → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqCollapsePhase.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqCollapsePhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L124-L124)
**instance
Tau.BookV.Astrophysics.instBEqCollapsePhase :BEq CollapsePhase**

Equations
- Tau.BookV.Astrophysics.instBEqCollapsePhase = { beq := Tau.BookV.Astrophysics.instBEqCollapsePhase.beq }

---

### `Tau.BookV.Astrophysics.CoreCollapseMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L126-L142)
**structure
Tau.BookV.Astrophysics.CoreCollapseMechanism :Type**


[V.D127] Core collapse mechanism: the sequence of events in a
core-collapse supernova, modeled as a defect cascade in the
τ-framework.

- progenitor_mass : ℕ
Progenitor mass (tenths of solar mass).

- massive_enough : self.progenitor_mass > 80
Progenitor is massive enough (> 8 M_☉).

- core_mass : ℕ
Iron core mass at collapse (tenths of solar mass).

- exceeds_chandrasekhar : self.core_mass ≥ chandrasekhar_mass_limit
Core exceeds Chandrasekhar.

- remnant : CompactObjectType
Remnant type.

- energy_released : ℕ
Energy released (10⁵¹ erg, scaled × 10).

Instances For

---

### `Tau.BookV.Astrophysics.instReprCoreCollapseMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L142-L142)
**instance
Tau.BookV.Astrophysics.instReprCoreCollapseMechanism :Repr CoreCollapseMechanism**

Equations
- Tau.BookV.Astrophysics.instReprCoreCollapseMechanism = { reprPrec := Tau.BookV.Astrophysics.instReprCoreCollapseMechanism.repr }

---

### `Tau.BookV.Astrophysics.instReprCoreCollapseMechanism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L142-L142)
**def
Tau.BookV.Astrophysics.instReprCoreCollapseMechanism.repr :CoreCollapseMechanism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.collapse_phases_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L144-L149)
**theorem
Tau.BookV.Astrophysics.collapse_phases_complete :[CollapsePhase.IronCoreGrowth, CollapsePhase.ElectronCapture, CollapsePhase.Bounce, CollapsePhase.ShockRevival, CollapsePhase.EnvelopeEjection, CollapsePhase.RemnantFormation].length = 6**


All collapse phases form a complete sequence.

---

### `Tau.BookV.Astrophysics.neutrino_from_defect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L155-L164)
**theorem
Tau.BookV.Astrophysics.neutrino_from_defect :"99% of binding energy released as neutrinos = defect energy release" = "99% of binding energy released as neutrinos = defect energy release"**


[V.P73] Neutrino burst from defect release: ~99% of the
gravitational binding energy (~3 × 10⁵³ erg) is released as
neutrinos during core collapse.

In the τ-framework, the neutrinos carry away the defect energy
that was stored in the compression component of the iron core's
defect tuple.

---

### `Tau.BookV.Astrophysics.type_ia_chandrasekhar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L170-L178)
**theorem
Tau.BookV.Astrophysics.type_ia_chandrasekhar :"Type Ia trigger at M_Ch = fixed mass threshold from iota_tau" = "Type Ia trigger at M_Ch = fixed mass threshold from iota_tau"**


[V.P74] Type Ia as Chandrasekhar crossing: the Type Ia SN is
triggered when the white dwarf accretes mass to reach M_Ch.

The standardizable-candle property follows from the FIXED
trigger mass (M_Ch is determined by fundamental constants
→ by ι<sub>τ</sub> in the τ-framework).

---

### `Tau.BookV.Astrophysics.ElementGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L184-L194)
**inductive
Tau.BookV.Astrophysics.ElementGroup :Type**


Element group produced in supernovae.

- Alpha : ElementGroup
Alpha elements (O, Ne, Mg, Si, S).

- IronPeak : ElementGroup
Iron peak (Cr, Mn, Fe, Co, Ni).

- RProcess : ElementGroup
r-Process (heavy elements beyond Fe).

- SProcess : ElementGroup
s-Process (slow neutron capture, AGB stars).

Instances For

---

### `Tau.BookV.Astrophysics.instReprElementGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L194-L194)
**instance
Tau.BookV.Astrophysics.instReprElementGroup :Repr ElementGroup**

Equations
- Tau.BookV.Astrophysics.instReprElementGroup = { reprPrec := Tau.BookV.Astrophysics.instReprElementGroup.repr }

---

### `Tau.BookV.Astrophysics.instReprElementGroup.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L194-L194)
**def
Tau.BookV.Astrophysics.instReprElementGroup.repr :ElementGroup → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqElementGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L194-L194)
**instance
Tau.BookV.Astrophysics.instDecidableEqElementGroup :DecidableEq ElementGroup**

Equations
- Tau.BookV.Astrophysics.instDecidableEqElementGroup x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqElementGroup.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L194-L194)
**def
Tau.BookV.Astrophysics.instBEqElementGroup.beq :ElementGroup → ElementGroup → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqElementGroup.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqElementGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L194-L194)
**instance
Tau.BookV.Astrophysics.instBEqElementGroup :BEq ElementGroup**

Equations
- Tau.BookV.Astrophysics.instBEqElementGroup = { beq := Tau.BookV.Astrophysics.instBEqElementGroup.beq }

---

### `Tau.BookV.Astrophysics.NucleosynthesisProducts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L196-L209)
**structure
Tau.BookV.Astrophysics.NucleosynthesisProducts :Type**


[V.D128] Nucleosynthesis products: the element groups produced
by different supernova types.

In the τ-framework, nucleosynthesis is a readout of the
C-sector (strong nuclear) coupling at high temperatures
where fusion reactions are defect-budget favorable.

- sn_type : SupernovaType
Supernova type.

- primary_products : List ElementGroup
Primary element groups produced.

- products_nonempty : self.primary_products.length > 0
Products are non-empty.

Instances For

---

### `Tau.BookV.Astrophysics.instReprNucleosynthesisProducts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L209-L209)
**instance
Tau.BookV.Astrophysics.instReprNucleosynthesisProducts :Repr NucleosynthesisProducts**

Equations
- Tau.BookV.Astrophysics.instReprNucleosynthesisProducts = { reprPrec := Tau.BookV.Astrophysics.instReprNucleosynthesisProducts.repr }

---

### `Tau.BookV.Astrophysics.instReprNucleosynthesisProducts.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L209-L209)
**def
Tau.BookV.Astrophysics.instReprNucleosynthesisProducts.repr :NucleosynthesisProducts → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.cc_sn_products`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L211-L215)
**def
Tau.BookV.Astrophysics.cc_sn_products :NucleosynthesisProducts**


Core-collapse SNe produce alpha + iron-peak + some r-process.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.ia_sn_products`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L217-L221)
**def
Tau.BookV.Astrophysics.ia_sn_products :NucleosynthesisProducts**


Type Ia SNe mainly produce iron-peak elements.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.standardizable_candle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L227-L235)
**theorem
Tau.BookV.Astrophysics.standardizable_candle :"Type Ia standardizable because M_Ch fixed by iota_tau" = "Type Ia standardizable because M_Ch fixed by iota_tau"**


[V.P75] Standardizable candle from fixed physics: Type Ia SNe
are standardizable candles because the trigger mass (M_Ch) is
fixed by fundamental physics (ultimately by ι<sub>τ</sub>).

The Phillips relation (brighter → slower decline) provides
the standardization correction.

---

### `Tau.BookV.Astrophysics.sn_rate_sfh`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L241-L246)
**theorem
Tau.BookV.Astrophysics.sn_rate_sfh :"SN rate = f(star formation history) = D-sector galactic readout" = "SN rate = f(star formation history) = D-sector galactic readout"**


[V.P76] SN rate from star formation history: the supernova rate
in a galaxy is determined by its star formation history, which
is a D-sector readout of the galactic defect bundle.

---

### `Tau.BookV.Astrophysics.example_cc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/Supernovae.lean#L276-L283)
**def
Tau.BookV.Astrophysics.example_cc :CoreCollapseMechanism**


Example: 20 M_☉ progenitor core collapse.
Equations
- One or more equations did not get rendered due to their size.
Instances For
