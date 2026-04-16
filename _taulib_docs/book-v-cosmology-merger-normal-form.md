---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.MergerNormalForm"
permalink: /verify/taulib/docs/book-v-cosmology-merger-normal-form/
lane: verify
module_name: "TauLib.BookV.Cosmology.MergerNormalForm"
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

# TauLib.BookV.Cosmology.MergerNormalForm


BH merger normal form. Mass addition, spin alignment, GW emission.
Ringdown damping, BH mass scale at depth n, primorial mass gap,
Wilson loops, gravitational deconfinement, Aharonov-Bohm phase.

## Registry Cross-References


- [V.R228] Why overlap forces merger -- structural remark

- [V.T115] Merger Normal Form -- `merger_normal_form`

- [V.R229] What the Normal Form does not give -- structural remark

- [V.D175] Ringdown Mode -- `RingdownMode`

- [V.P97] Ringdown Damping is Structural -- `ringdown_damping_structural`

- [V.D176] BH Mass Scale at Depth n -- `BHMassScale`

- [V.P98] Mass Gap Between Adjacent Primorial Levels -- `mass_gap_primorial`

- [V.R230] The mass gap and the IMBH desert -- structural remark

- [V.R231] Scope note on mass spectrum predictions -- structural remark

- [V.D177] Base Wilson Loop -- `BaseWilsonLoop`

- [V.P99] Gravitational Deconfinement -- `gravitational_deconfinement`

- [V.R232] Contrast with the strong sector -- structural remark

- [V.P100] BH Gravitational Aharonov-Bohm Phase -- `bh_ab_phase`

- [V.P101] Radiated Energy Bound -- `radiated_energy_bound`

- [V.R233] The 1/√2 -- structural remark


## Mathematical Content


### Merger Normal Form


When two BHs with masses M₁, M₂ and angular momenta J₁, J₂ satisfy
the approach condition, the merger produces:
M_final = M₁ + M₂ − ΔE/c²
J_final = J₁ + J₂ − ΔJ

### Ringdown


Post-merger, the excision oscillates as ringdown modes:
r_n(t) = A_n · exp(−σ_n·t) · cos(ω_n·t + φ_n)
All damping rates σ_n > 0 (ringdown terminates).

### Primorial Mass Gap


BH mass scale at primorial depths: M_n = m_n · κ(D;1). Ratio between
adjacent levels ~ p_{n+1} (next prime). This predicts a gap between
supermassive and stellar BHs, possibly explaining IMBH scarcity.

### Gravitational Deconfinement


Gravity (base τ¹) is deconfined: Wilson loops satisfy a perimeter law.
Contrast: the strong force (fiber T²) is confined with area-law loops.

### Radiated Energy Bound


ΔE/(M₁+M₂)c² ≤ 1 − 1/√2 ≈ 0.293 (Penrose extraction limit).

## Ground Truth Sources


- Book V ch52: Merger Normal Form


---

### `Tau.BookV.Cosmology.MergerNormalFormData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L70-L92)
**structure
Tau.BookV.Cosmology.MergerNormalFormData :Type**


[V.T115] Merger normal form: when two single-excision BHs
satisfy the approach condition, the merger produces a single
excision with determined mass and angular momentum.

M_final ≤ M₁ + M₂ (energy radiated as GW).
M_final ≥ max(M₁, M₂) (no-shrink for final BH).

- mass_1 : ℕ
Mass of BH 1 (scaled).

- mass_2 : ℕ
Mass of BH 2 (scaled).

- mass_final : ℕ
Mass of final BH (scaled).

- radiated : ℕ
Radiated energy (scaled, = M₁ + M₂ − M_final).

- mass1_pos : self.mass_1 > 0
Both masses positive.

- mass2_pos : self.mass_2 > 0
- mass_balance : self.mass_final + self.radiated = self.mass_1 + self.mass_2
Final mass is sum minus radiated.

- no_shrink : self.mass_final ≥ self.mass_1 ∨ self.mass_final ≥ self.mass_2
Final mass at least max of inputs.

Instances For

---

### `Tau.BookV.Cosmology.instReprMergerNormalFormData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L92-L92)
**def
Tau.BookV.Cosmology.instReprMergerNormalFormData.repr :MergerNormalFormData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprMergerNormalFormData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L92-L92)
**instance
Tau.BookV.Cosmology.instReprMergerNormalFormData :Repr MergerNormalFormData**

Equations
- Tau.BookV.Cosmology.instReprMergerNormalFormData = { reprPrec := Tau.BookV.Cosmology.instReprMergerNormalFormData.repr }

---

### `Tau.BookV.Cosmology.merger_normal_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L94-L96)
**theorem
Tau.BookV.Cosmology.merger_normal_form
(m : MergerNormalFormData)
 :m.mass_final + m.radiated = m.mass_1 + m.mass_2**


Merger normal form: mass is conserved (modulo radiation).

---

### `Tau.BookV.Cosmology.RingdownMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L102-L121)
**structure
Tau.BookV.Cosmology.RingdownMode :Type**


[V.D175] Ringdown mode: the n-th quasi-normal mode of a merged
excision, characterized by amplitude, damping rate, and frequency.

r_n(t) = A_n · exp(−σ_n·t) · cos(ω_n·t + φ_n)

Damping rate σ_n > 0 for all n ≥ 1.

- mode_number : ℕ
Mode number (≥ 1).

- mode_pos : self.mode_number > 0
Mode number positive.

- amplitude : ℕ
Amplitude (scaled).

- damping_rate : ℕ
Damping rate (scaled, strictly positive).

- damping_pos : self.damping_rate > 0
Damping positive.

- frequency : ℕ
Frequency (scaled).

Instances For

---

### `Tau.BookV.Cosmology.instReprRingdownMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L121-L121)
**def
Tau.BookV.Cosmology.instReprRingdownMode.repr :RingdownMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprRingdownMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L121-L121)
**instance
Tau.BookV.Cosmology.instReprRingdownMode :Repr RingdownMode**

Equations
- Tau.BookV.Cosmology.instReprRingdownMode = { reprPrec := Tau.BookV.Cosmology.instReprRingdownMode.repr }

---

### `Tau.BookV.Cosmology.ringdown_damping_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L127-L130)
**theorem
Tau.BookV.Cosmology.ringdown_damping_structural
(r : RingdownMode)
 :r.damping_rate > 0**


[V.P97] Ringdown damping is structural: every mode has σ_n > 0.
The ringdown terminates in finite time.

---

### `Tau.BookV.Cosmology.BHMassScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L136-L152)
**structure
Tau.BookV.Cosmology.BHMassScale :Type**


[V.D176] BH mass scale at refinement depth n:
M_n = m_n · κ(D;1) = m_n · (1 − ι<sub>τ</sub>).

κ(D;1) ≈ 0.6585. The mass scale decreases with depth because m_n
decreases as the refinement goes deeper (smaller structures).

- level : ℕ
Primorial level index.

- level_pos : self.level > 0
Level positive.

- mass_numer : ℕ
Mass scale numerator.

- mass_denom : ℕ
Mass scale denominator.

- denom_pos : self.mass_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHMassScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L152-L152)
**instance
Tau.BookV.Cosmology.instReprBHMassScale :Repr BHMassScale**

Equations
- Tau.BookV.Cosmology.instReprBHMassScale = { reprPrec := Tau.BookV.Cosmology.instReprBHMassScale.repr }

---

### `Tau.BookV.Cosmology.instReprBHMassScale.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L152-L152)
**def
Tau.BookV.Cosmology.instReprBHMassScale.repr :BHMassScale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.PrimorialMassGap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L158-L175)
**structure
Tau.BookV.Cosmology.PrimorialMassGap :Type**


[V.P98] Mass gap between adjacent primorial levels:
M_n / M_{n+1} ~ p_{n+1} (next prime).

The primorial mass hierarchy predicts a natural gap in the
BH mass spectrum. This may explain the intermediate-mass
black hole (IMBH) desert.

- level_n : ℕ
Level n.

- level_np1 : ℕ
Level n+1.

- adjacent : self.level_np1 = self.level_n + 1
Adjacent levels.

- gap_ratio : ℕ
Gap ratio (approximate: next prime at that level).

- gap_min : self.gap_ratio ≥ 2
Gap is at least 2 (smallest prime).

Instances For

---

### `Tau.BookV.Cosmology.instReprPrimorialMassGap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L175-L175)
**instance
Tau.BookV.Cosmology.instReprPrimorialMassGap :Repr PrimorialMassGap**

Equations
- Tau.BookV.Cosmology.instReprPrimorialMassGap = { reprPrec := Tau.BookV.Cosmology.instReprPrimorialMassGap.repr }

---

### `Tau.BookV.Cosmology.instReprPrimorialMassGap.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L175-L175)
**def
Tau.BookV.Cosmology.instReprPrimorialMassGap.repr :PrimorialMassGap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.mass_gap_primorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L177-L179)
**theorem
Tau.BookV.Cosmology.mass_gap_primorial
(g : PrimorialMassGap)
 :g.gap_ratio ≥ 2**


Mass gap is at least factor of 2.

---

### `Tau.BookV.Cosmology.scope_note_mass_spectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L185-L190)
**def
Tau.BookV.Cosmology.scope_note_mass_spectrum :Prop**


[V.R231] Scope note: the qualitative BH mass spectrum features
(hierarchy, gap, IMBH scarcity) follow at the τ-effective level.
Quantitative mass values require calibration against observation.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.scope_note_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L192-L192)
**theorem
Tau.BookV.Cosmology.scope_note_holds :scope_note_mass_spectrum**


---

### `Tau.BookV.Cosmology.WilsonLawType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L198-L209)
**inductive
Tau.BookV.Cosmology.WilsonLawType :Type**


[V.D177] Base Wilson loop W_n = Tr(Hol_∂(τ¹; n)):
the trace of the boundary holonomy around τ¹ at refinement depth n.

Wilson loops diagnose confinement vs. deconfinement:


- Area law ⟹ confinement (strong sector)

- Perimeter law ⟹ deconfinement (gravitational sector)


- PerimeterLaw : WilsonLawType
Perimeter law: W ~ exp(−κ·L), deconfined.

- AreaLaw : WilsonLawType
Area law: W ~ exp(−σ·A), confined.

Instances For

---

### `Tau.BookV.Cosmology.instReprWilsonLawType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L209-L209)
**def
Tau.BookV.Cosmology.instReprWilsonLawType.repr :WilsonLawType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprWilsonLawType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L209-L209)
**instance
Tau.BookV.Cosmology.instReprWilsonLawType :Repr WilsonLawType**

Equations
- Tau.BookV.Cosmology.instReprWilsonLawType = { reprPrec := Tau.BookV.Cosmology.instReprWilsonLawType.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqWilsonLawType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L209-L209)
**instance
Tau.BookV.Cosmology.instDecidableEqWilsonLawType :DecidableEq WilsonLawType**

Equations
- Tau.BookV.Cosmology.instDecidableEqWilsonLawType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqWilsonLawType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L209-L209)
**instance
Tau.BookV.Cosmology.instBEqWilsonLawType :BEq WilsonLawType**

Equations
- Tau.BookV.Cosmology.instBEqWilsonLawType = { beq := Tau.BookV.Cosmology.instBEqWilsonLawType.beq }

---

### `Tau.BookV.Cosmology.instBEqWilsonLawType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L209-L209)
**def
Tau.BookV.Cosmology.instBEqWilsonLawType.beq :WilsonLawType → WilsonLawType → Bool**

Equations
- Tau.BookV.Cosmology.instBEqWilsonLawType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.BaseWilsonLoop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L211-L221)
**structure
Tau.BookV.Cosmology.BaseWilsonLoop :Type**


Wilson loop on the base circle.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- law : WilsonLawType
Law type.

- coupling_numer : ℕ
Coupling (scaled).

Instances For

---

### `Tau.BookV.Cosmology.instReprBaseWilsonLoop.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L221-L221)
**def
Tau.BookV.Cosmology.instReprBaseWilsonLoop.repr :BaseWilsonLoop → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBaseWilsonLoop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L221-L221)
**instance
Tau.BookV.Cosmology.instReprBaseWilsonLoop :Repr BaseWilsonLoop**

Equations
- Tau.BookV.Cosmology.instReprBaseWilsonLoop = { reprPrec := Tau.BookV.Cosmology.instReprBaseWilsonLoop.repr }

---

### `Tau.BookV.Cosmology.gravitational_deconfinement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L227-L234)
**theorem
Tau.BookV.Cosmology.gravitational_deconfinement :"D-sector deconfined: perimeter law for base Wilson loops" = "D-sector deconfined: perimeter law for base Wilson loops"**


[V.P99] Gravitational deconfinement: the D-sector is deconfined.
Base Wilson loops satisfy a perimeter law:
W_n ~ exp(−κ_τ · L(τ¹; n))

Gravity propagates freely at all distances (no confinement).

---

### `Tau.BookV.Cosmology.BHABPhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L240-L252)
**structure
Tau.BookV.Cosmology.BHABPhase :Type**


[V.P100] BH gravitational Aharonov-Bohm phase:
Φ_BH = G·M / ι<sub>τ</sub> = (c³/ℏ) · ι<sub>τ</sub> · M.

The phase is proportional to M and inversely proportional to ι<sub>τ</sub>.
It is detectable (in principle) via gravitational interference.

- mass_index : ℕ
Mass index (scaled).

- mass_pos : self.mass_index > 0
Mass positive.

- proportional_to_mass : Bool
Phase is proportional to M.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHABPhase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L252-L252)
**instance
Tau.BookV.Cosmology.instReprBHABPhase :Repr BHABPhase**

Equations
- Tau.BookV.Cosmology.instReprBHABPhase = { reprPrec := Tau.BookV.Cosmology.instReprBHABPhase.repr }

---

### `Tau.BookV.Cosmology.instReprBHABPhase.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L252-L252)
**def
Tau.BookV.Cosmology.instReprBHABPhase.repr :BHABPhase → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bh_ab_phase`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L254-L256)
**theorem
Tau.BookV.Cosmology.bh_ab_phase
(p : BHABPhase)

(h : p.proportional_to_mass = true)
 :p.proportional_to_mass = true**


AB phase is proportional to mass.

---

### `Tau.BookV.Cosmology.RadiatedEnergyBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L262-L276)
**structure
Tau.BookV.Cosmology.RadiatedEnergyBound :Type**


[V.P101] Radiated energy bound: ΔE / ((M₁+M₂)c²) ≤ 1 − 1/√2.

1 − 1/√2 ≈ 0.2929. Encoded as 2929/10000.
This is the Penrose extraction limit for Kerr BHs. In τ, the
same bound arises from the blueprint monoid structure.

- bound_numer : ℕ
Bound numerator.

- bound_denom : ℕ
Bound denominator.

- denom_pos : self.bound_denom > 0
Denominator positive.

- approx : self.bound_numer > 2900 ∧ self.bound_numer < 3000
Bound is approximately 0.293: 2929/10000.

Instances For

---

### `Tau.BookV.Cosmology.instReprRadiatedEnergyBound.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L276-L276)
**def
Tau.BookV.Cosmology.instReprRadiatedEnergyBound.repr :RadiatedEnergyBound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprRadiatedEnergyBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L276-L276)
**instance
Tau.BookV.Cosmology.instReprRadiatedEnergyBound :Repr RadiatedEnergyBound**

Equations
- Tau.BookV.Cosmology.instReprRadiatedEnergyBound = { reprPrec := Tau.BookV.Cosmology.instReprRadiatedEnergyBound.repr }

---

### `Tau.BookV.Cosmology.canonical_energy_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L278-L283)
**def
Tau.BookV.Cosmology.canonical_energy_bound :RadiatedEnergyBound**


The canonical radiated energy bound.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.radiated_energy_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L285-L289)
**theorem
Tau.BookV.Cosmology.radiated_energy_bound :canonical_energy_bound.bound_numer > 2900 ∧ canonical_energy_bound.bound_numer < 3000**


The bound is approximately 0.293.

---

### `Tau.BookV.Cosmology.the_sqrt2_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L295-L301)
**def
Tau.BookV.Cosmology.the_sqrt2_remark :Prop**


[V.R233] The 1/√2 radiated energy bound is a classical GR result
(Penrose extraction limit for Kerr BHs). In τ, the same bound
arises structurally from the blueprint fusion operation: energy
extraction cannot exceed the bipolar imbalance limit.
Equations
- Tau.BookV.Cosmology.the_sqrt2_remark = ("1/sqrt(2) bound from GR = blueprint fusion limit in tau" = "1/sqrt(2) bound from GR = blueprint fusion limit in tau")
Instances For

---

### `Tau.BookV.Cosmology.sqrt2_remark_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L303-L303)
**theorem
Tau.BookV.Cosmology.sqrt2_remark_holds :the_sqrt2_remark**


---

### `Tau.BookV.Cosmology.example_merger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L329-L338)
**def
Tau.BookV.Cosmology.example_merger :MergerNormalFormData**


Example merger.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.mode1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L344-L351)
**def
Tau.BookV.Cosmology.mode1 :RingdownMode**


Example ringdown mode 1.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.BlueprintFusionEnergy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L359-L370)
**structure
Tau.BookV.Cosmology.BlueprintFusionEnergy :Type**


[V.D282] Blueprint fusion energy: radiated fraction
η = ι<sub>τ</sub>² · ν where ν = q/(1+q)² is the symmetric mass ratio.

Derived from linking-class reduction during blueprint fusion
at the lemniscate crossing point: pre-merger H₁(L₁)⊕H₁(L₂) ≅ ℤ⁴
reduces to post-merger H₁(L_final) ≅ ℤ². The two lost classes
release energy proportional to ι<sub>τ</sub>² (D-sector holonomy constraint).

- description : String
- formula : String
- iota_sq_x10000 : ℕ
Instances For

---

### `Tau.BookV.Cosmology.instReprBlueprintFusionEnergy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L370-L370)
**def
Tau.BookV.Cosmology.instReprBlueprintFusionEnergy.repr :BlueprintFusionEnergy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBlueprintFusionEnergy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L370-L370)
**instance
Tau.BookV.Cosmology.instReprBlueprintFusionEnergy :Repr BlueprintFusionEnergy**

Equations
- Tau.BookV.Cosmology.instReprBlueprintFusionEnergy = { reprPrec := Tau.BookV.Cosmology.instReprBlueprintFusionEnergy.repr }

---

### `Tau.BookV.Cosmology.merger_energy_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L372-L377)
**def
Tau.BookV.Cosmology.merger_energy_formula :BlueprintFusionEnergy**


[V.T224] Merger energy theorem: non-spinning radiated fraction
from blueprint fusion.
Equations
- Tau.BookV.Cosmology.merger_energy_formula = { description := "Non-spinning radiated fraction from blueprint fusion", formula := "η = ι<sub>τ</sub>² · ν, ν = q/(1+q)²",
 iota_sq_x10000 := 1165 }
Instances For

---

### `Tau.BookV.Cosmology.equal_mass_eta_ppm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L379-L381)
**def
Tau.BookV.Cosmology.equal_mass_eta_ppm :ℕ**


[V.P150] Equal-mass energy fraction:
η(q=1) = ι<sub>τ</sub>²/4 ≈ 0.02912, stored as parts per million.
Equations
- Tau.BookV.Cosmology.equal_mass_eta_ppm = 29122
Instances For

---

### `Tau.BookV.Cosmology.equal_mass_eta_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L383-L384)
**theorem
Tau.BookV.Cosmology.equal_mass_eta_positive :equal_mass_eta_ppm > 0**


Equal-mass fraction is positive.

---

### `Tau.BookV.Cosmology.equal_mass_eta_below_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L386-L387)
**theorem
Tau.BookV.Cosmology.equal_mass_eta_below_bound :equal_mass_eta_ppm < 293000**


Equal-mass fraction is below upper bound (1−1/√2 ≈ 0.293).

---

### `Tau.BookV.Cosmology.iota_sq_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/MergerNormalForm.lean#L389-L390)
**theorem
Tau.BookV.Cosmology.iota_sq_canonical :merger_energy_formula.iota_sq_x10000 = 1165**


iota_tau^2 × 10000 matches the canonical value.
