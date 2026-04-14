---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.WeakChirality"
permalink: /verify/taulib/docs/book-iv-electroweak-weak-chirality/
lane: verify
module_name: "TauLib.BookIV.Electroweak.WeakChirality"
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

# TauLib.BookIV.Electroweak.WeakChirality


Polarity indices, parity operations, chirality, and the structural
origin of maximal parity violation in the weak (A) sector.

## Registry Cross-References


- [IV.D107] Polarity Index chi(X) — `PolarityIndex`

- [IV.D108] Parity-Preserving Interaction — `ParityPreserving`

- [IV.D109] W Boson as Polarity-Switching Transport — `WBosonMode`

- [IV.D110] Z Boson as Neutral Weak Transport — `ZBosonMode`

- [IV.D111] Chirality (Left/Right-Handedness) — `ChiralityType`

- [IV.D112] sigma_A-Admissibility (Left-Handed Only) — `sigma_a_admissible`

- [IV.D113] Parity Transformation — `ParityTransformation`

- [IV.D114] Parity Violation Measure — `ParityViolation`

- [IV.L05] sigma_A-Admissible iff Left-Handed — `sigma_a_iff_left`

- [IV.T51] Weak Interaction Maximally Violates Parity — `weak_max_parity_violation`

- [IV.P52] Polarity Signatures of All Sectors — `all_sector_polarities`

- [IV.P53] W/Z Massive Because omega Is Conical Singularity — `wz_massive_from_omega`


## Ground Truth Sources


- Chapter 30 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.PolarityIndex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L37-L49)
**structure
Tau.BookIV.Electroweak.PolarityIndex :Type**


[IV.D107] Polarity index chi(X) for a sector X: the pair (chi_plus, chi_minus)
encoding the relative weight of multiplicative vs additive
boundary characters. Values scaled to denom = 100.

- sector : BookIII.Sectors.Sector
The sector.

- chi_plus : ℕ
chi_plus weight (scaled, 0-100).

- chi_minus : ℕ
chi_minus weight (scaled, 0-100).

- sum_eq : self.chi_plus + self.chi_minus = 100
Weights sum to 100 (full allocation).

Instances For

---

### `Tau.BookIV.Electroweak.instReprPolarityIndex.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L49-L49)
**def
Tau.BookIV.Electroweak.instReprPolarityIndex.repr :PolarityIndex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPolarityIndex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L49-L49)
**instance
Tau.BookIV.Electroweak.instReprPolarityIndex :Repr PolarityIndex**

Equations
- Tau.BookIV.Electroweak.instReprPolarityIndex = { reprPrec := Tau.BookIV.Electroweak.instReprPolarityIndex.repr }

---

### `Tau.BookIV.Electroweak.pol_D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L51-L53)
**def
Tau.BookIV.Electroweak.pol_D :PolarityIndex**


Polarity index for D (Gravity): chi_plus-dominant.
Equations
- Tau.BookIV.Electroweak.pol_D = { sector := Tau.BookIII.Sectors.Sector.D, chi_plus := 66, chi_minus := 34,
 sum_eq := Tau.BookIV.Electroweak.pol_D._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pol_A`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L55-L57)
**def
Tau.BookIV.Electroweak.pol_A :PolarityIndex**


Polarity index for A (Weak): balanced (50/50).
Equations
- Tau.BookIV.Electroweak.pol_A = { sector := Tau.BookIII.Sectors.Sector.A, chi_plus := 50, chi_minus := 50,
 sum_eq := Tau.BookIV.Electroweak.pol_A._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pol_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L59-L61)
**def
Tau.BookIV.Electroweak.pol_B :PolarityIndex**


Polarity index for B (EM): chi_plus-dominant.
Equations
- Tau.BookIV.Electroweak.pol_B = { sector := Tau.BookIII.Sectors.Sector.B, chi_plus := 66, chi_minus := 34,
 sum_eq := Tau.BookIV.Electroweak.pol_D._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pol_C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L63-L65)
**def
Tau.BookIV.Electroweak.pol_C :PolarityIndex**


Polarity index for C (Strong): chi_minus-dominant.
Equations
- Tau.BookIV.Electroweak.pol_C = { sector := Tau.BookIII.Sectors.Sector.C, chi_plus := 34, chi_minus := 66,
 sum_eq := Tau.BookIV.Electroweak.pol_C._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pol_Omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L67-L69)
**def
Tau.BookIV.Electroweak.pol_Omega :PolarityIndex**


Polarity index for omega (Higgs): crossing (both active).
Equations
- Tau.BookIV.Electroweak.pol_Omega = { sector := Tau.BookIII.Sectors.Sector.Omega, chi_plus := 50, chi_minus := 50,
 sum_eq := Tau.BookIV.Electroweak.pol_A._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.all_sector_polarities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L71-L73)
**def
Tau.BookIV.Electroweak.all_sector_polarities :List PolarityIndex**


[IV.P52] Polarity signatures of all 5 sectors at E1.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.all_sector_polarities_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L75-L75)
**theorem
Tau.BookIV.Electroweak.all_sector_polarities_count :all_sector_polarities.length = 5**


---

### `Tau.BookIV.Electroweak.ParityPreserving`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L81-L89)
**structure
Tau.BookIV.Electroweak.ParityPreserving :Type**


[IV.D108] An interaction is parity-preserving if it does not
distinguish left from right chirality. EM, Strong, and Gravity
are parity-preserving; Weak is not.

- sector : BookIII.Sectors.Sector
The sector.

- preserves : Bool
Whether the sector preserves parity.

Instances For

---

### `Tau.BookIV.Electroweak.instReprParityPreserving.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L89-L89)
**def
Tau.BookIV.Electroweak.instReprParityPreserving.repr :ParityPreserving → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprParityPreserving`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L89-L89)
**instance
Tau.BookIV.Electroweak.instReprParityPreserving :Repr ParityPreserving**

Equations
- Tau.BookIV.Electroweak.instReprParityPreserving = { reprPrec := Tau.BookIV.Electroweak.instReprParityPreserving.repr }

---

### `Tau.BookIV.Electroweak.parity_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L91-L92)
**def
Tau.BookIV.Electroweak.parity_em :ParityPreserving**


EM preserves parity.
Equations
- Tau.BookIV.Electroweak.parity_em = { sector := Tau.BookIII.Sectors.Sector.B, preserves := true }
Instances For

---

### `Tau.BookIV.Electroweak.parity_strong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L93-L94)
**def
Tau.BookIV.Electroweak.parity_strong :ParityPreserving**


Strong preserves parity.
Equations
- Tau.BookIV.Electroweak.parity_strong = { sector := Tau.BookIII.Sectors.Sector.C, preserves := true }
Instances For

---

### `Tau.BookIV.Electroweak.parity_gravity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L95-L96)
**def
Tau.BookIV.Electroweak.parity_gravity :ParityPreserving**


Gravity preserves parity.
Equations
- Tau.BookIV.Electroweak.parity_gravity = { sector := Tau.BookIII.Sectors.Sector.D, preserves := true }
Instances For

---

### `Tau.BookIV.Electroweak.parity_weak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L97-L98)
**def
Tau.BookIV.Electroweak.parity_weak :ParityPreserving**


Weak VIOLATES parity.
Equations
- Tau.BookIV.Electroweak.parity_weak = { sector := Tau.BookIII.Sectors.Sector.A, preserves := false }
Instances For

---

### `Tau.BookIV.Electroweak.parity_higgs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L99-L100)
**def
Tau.BookIV.Electroweak.parity_higgs :ParityPreserving**


Higgs preserves parity (scalar).
Equations
- Tau.BookIV.Electroweak.parity_higgs = { sector := Tau.BookIII.Sectors.Sector.Omega, preserves := true }
Instances For

---

### `Tau.BookIV.Electroweak.ChiralityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L106-L114)
**inductive
Tau.BookIV.Electroweak.ChiralityType :Type**


[IV.D111] Chirality: left- or right-handedness of a fermion state.
In the tau-framework, chirality is a boundary-character property:
left-handed = sigma_A-admissible, right-handed = sigma_A-inadmissible.

- Left : ChiralityType
Left-handed: participates in weak interaction.

- Right : ChiralityType
Right-handed: invisible to weak force.

Instances For

---

### `Tau.BookIV.Electroweak.instReprChiralityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L114-L114)
**instance
Tau.BookIV.Electroweak.instReprChiralityType :Repr ChiralityType**

Equations
- Tau.BookIV.Electroweak.instReprChiralityType = { reprPrec := Tau.BookIV.Electroweak.instReprChiralityType.repr }

---

### `Tau.BookIV.Electroweak.instReprChiralityType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L114-L114)
**def
Tau.BookIV.Electroweak.instReprChiralityType.repr :ChiralityType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqChiralityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L114-L114)
**instance
Tau.BookIV.Electroweak.instDecidableEqChiralityType :DecidableEq ChiralityType**

Equations
- Tau.BookIV.Electroweak.instDecidableEqChiralityType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Electroweak.instBEqChiralityType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L114-L114)
**def
Tau.BookIV.Electroweak.instBEqChiralityType.beq :ChiralityType → ChiralityType → Bool**

Equations
- Tau.BookIV.Electroweak.instBEqChiralityType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Electroweak.instBEqChiralityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L114-L114)
**instance
Tau.BookIV.Electroweak.instBEqChiralityType :BEq ChiralityType**

Equations
- Tau.BookIV.Electroweak.instBEqChiralityType = { beq := Tau.BookIV.Electroweak.instBEqChiralityType.beq }

---

### `Tau.BookIV.Electroweak.sigma_a_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L120-L126)
**def
Tau.BookIV.Electroweak.sigma_a_admissible
(c : ChiralityType)
 :Bool**


[IV.D112] sigma_A-admissibility: a fermion state is sigma_A-admissible iff
it is left-handed. The weak sector involution sigma_A acts only on
the left-handed projection.
Equations
- Tau.BookIV.Electroweak.sigma_a_admissible Tau.BookIV.Electroweak.ChiralityType.Left = true
- Tau.BookIV.Electroweak.sigma_a_admissible Tau.BookIV.Electroweak.ChiralityType.Right = false
Instances For

---

### `Tau.BookIV.Electroweak.sigma_a_iff_left`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L128-L131)
**theorem
Tau.BookIV.Electroweak.sigma_a_iff_left
(c : ChiralityType)
 :sigma_a_admissible c = true ↔ c = ChiralityType.Left**


[IV.L05] sigma_A-admissible if and only if left-handed.

---

### `Tau.BookIV.Electroweak.WBosonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L137-L150)
**structure
Tau.BookIV.Electroweak.WBosonMode :Type**


[IV.D109] W boson: the polarity-switching transport mode in the
A-sector. Carries charge and mediates charged-current weak
interactions. W is massive because omega (lemniscate crossing)
provides a conical singularity that fixes the coherence scale.

- name : String
Name identifier.

- charge : ℤ
Electric charge (in units of e): +1, -1, or 0.

- massive : Bool
Massive (true) or massless (false).

- left_only : Bool
Chirality coupling: left-only.

Instances For

---

### `Tau.BookIV.Electroweak.instReprWBosonMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L150-L150)
**def
Tau.BookIV.Electroweak.instReprWBosonMode.repr :WBosonMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprWBosonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L150-L150)
**instance
Tau.BookIV.Electroweak.instReprWBosonMode :Repr WBosonMode**

Equations
- Tau.BookIV.Electroweak.instReprWBosonMode = { reprPrec := Tau.BookIV.Electroweak.instReprWBosonMode.repr }

---

### `Tau.BookIV.Electroweak.w_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L152-L153)
**def
Tau.BookIV.Electroweak.w_plus :WBosonMode**


W-plus boson.
Equations
- Tau.BookIV.Electroweak.w_plus = { name := "W+", charge := 1, massive := true, left_only := true }
Instances For

---

### `Tau.BookIV.Electroweak.w_minus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L154-L155)
**def
Tau.BookIV.Electroweak.w_minus :WBosonMode**


W-minus boson.
Equations
- Tau.BookIV.Electroweak.w_minus = { name := "W-", charge := -1, massive := true, left_only := true }
Instances For

---

### `Tau.BookIV.Electroweak.ZBosonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L161-L172)
**structure
Tau.BookIV.Electroweak.ZBosonMode :Type**


[IV.D110] Z boson: the neutral weak transport mode. Mediates
neutral-current weak interactions. Also massive via omega-coupling.

- name : String
Name identifier.

- charge : ℤ
Electric charge: always 0.

- charge_zero : self.charge = 0
- massive : Bool
Massive.

- massive_true : self.massive = true
Instances For

---

### `Tau.BookIV.Electroweak.instReprZBosonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L172-L172)
**instance
Tau.BookIV.Electroweak.instReprZBosonMode :Repr ZBosonMode**

Equations
- Tau.BookIV.Electroweak.instReprZBosonMode = { reprPrec := Tau.BookIV.Electroweak.instReprZBosonMode.repr }

---

### `Tau.BookIV.Electroweak.instReprZBosonMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L172-L172)
**def
Tau.BookIV.Electroweak.instReprZBosonMode.repr :ZBosonMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.z_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L174-L180)
**def
Tau.BookIV.Electroweak.z_zero :ZBosonMode**


Z-zero boson.
Equations
- Tau.BookIV.Electroweak.z_zero = { name := "Z0", charge := 0, charge_zero := Tau.BookIV.Electroweak.z_zero._proof_1, massive := true,
 massive_true := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.ParityTransformation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L186-L196)
**structure
Tau.BookIV.Electroweak.ParityTransformation :Type**


[IV.D113] Parity transformation P: spatial inversion x to -x.
In the tau-framework, P is the sigma-involution restricted to spatial
coordinates (fiber T-squared). It swaps chi_plus and chi_minus on the fiber.

- spatial_dims : ℕ
Spatial dimension count affected.

- spatial_eq : self.spatial_dims = 3
- det_sign : ℤ
Determinant of P: det(P) = (-1)^d = -1 for d = 3.

- det_eq : self.det_sign = -1
Instances For

---

### `Tau.BookIV.Electroweak.instReprParityTransformation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L196-L196)
**def
Tau.BookIV.Electroweak.instReprParityTransformation.repr :ParityTransformation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprParityTransformation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L196-L196)
**instance
Tau.BookIV.Electroweak.instReprParityTransformation :Repr ParityTransformation**

Equations
- Tau.BookIV.Electroweak.instReprParityTransformation = { reprPrec := Tau.BookIV.Electroweak.instReprParityTransformation.repr }

---

### `Tau.BookIV.Electroweak.parity_3d`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L198-L203)
**def
Tau.BookIV.Electroweak.parity_3d :ParityTransformation**


Canonical parity transformation in 3+1 dimensions.
Equations
- Tau.BookIV.Electroweak.parity_3d = { spatial_dims := 3, spatial_eq := Tau.BookIV.Electroweak.parity_3d._proof_1, det_sign := -1,
 det_eq := Tau.BookIV.Electroweak.parity_3d._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.ParityViolation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L209-L219)
**structure
Tau.BookIV.Electroweak.ParityViolation :Type**


[IV.D114] Parity violation measure V(S) for sector S:
V = 0 for parity-preserving, V = 100 for maximal violation.
The weak sector has V = 100 (couples only to left-handed fermions).

- sector : BookIII.Sectors.Sector
Sector.

- violation : ℕ
Violation measure: 0 (preserving) or 100 (maximal), scaled.

- bounded : self.violation ≤ 100
Bounded by 100.

Instances For

---

### `Tau.BookIV.Electroweak.instReprParityViolation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L219-L219)
**def
Tau.BookIV.Electroweak.instReprParityViolation.repr :ParityViolation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprParityViolation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L219-L219)
**instance
Tau.BookIV.Electroweak.instReprParityViolation :Repr ParityViolation**

Equations
- Tau.BookIV.Electroweak.instReprParityViolation = { reprPrec := Tau.BookIV.Electroweak.instReprParityViolation.repr }

---

### `Tau.BookIV.Electroweak.pv_gravity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L221-L222)
**def
Tau.BookIV.Electroweak.pv_gravity :ParityViolation**


Parity violation for each sector.
Equations
- Tau.BookIV.Electroweak.pv_gravity = { sector := Tau.BookIII.Sectors.Sector.D, violation := 0, bounded := Tau.BookIV.Electroweak.pv_gravity._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pv_weak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L223-L223)
**def
Tau.BookIV.Electroweak.pv_weak :ParityViolation**

Equations
- Tau.BookIV.Electroweak.pv_weak = { sector := Tau.BookIII.Sectors.Sector.A, violation := 100, bounded := Tau.BookIV.Electroweak.pv_weak._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pv_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L224-L224)
**def
Tau.BookIV.Electroweak.pv_em :ParityViolation**

Equations
- Tau.BookIV.Electroweak.pv_em = { sector := Tau.BookIII.Sectors.Sector.B, violation := 0, bounded := Tau.BookIV.Electroweak.pv_gravity._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pv_strong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L225-L225)
**def
Tau.BookIV.Electroweak.pv_strong :ParityViolation**

Equations
- Tau.BookIV.Electroweak.pv_strong = { sector := Tau.BookIII.Sectors.Sector.C, violation := 0, bounded := Tau.BookIV.Electroweak.pv_gravity._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.pv_higgs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L226-L226)
**def
Tau.BookIV.Electroweak.pv_higgs :ParityViolation**

Equations
- Tau.BookIV.Electroweak.pv_higgs = { sector := Tau.BookIII.Sectors.Sector.Omega, violation := 0, bounded := Tau.BookIV.Electroweak.pv_gravity._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.weak_max_parity_violation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L232-L242)
**theorem
Tau.BookIV.Electroweak.weak_max_parity_violation :pv_weak.violation = 100 ∧ pv_gravity.violation = 0 ∧ pv_em.violation = 0 ∧ pv_strong.violation = 0 ∧ pv_higgs.violation = 0**


[IV.T51] The weak interaction maximally violates parity:
V(A) = 100 (maximal) while V(D) = V(B) = V(C) = V(omega) = 0.
This is structural: the A-sector balanced polarity (pol = 1)
means sigma_A acts non-trivially, selecting one chirality.

---

### `Tau.BookIV.Electroweak.weak_unique_violator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L244-L251)
**theorem
Tau.BookIV.Electroweak.weak_unique_violator :pv_weak.violation > 0 ∧ pv_gravity.violation = 0 ∧ pv_em.violation = 0 ∧ pv_strong.violation = 0 ∧ pv_higgs.violation = 0**


Only the weak sector has nonzero parity violation.

---

### `Tau.BookIV.Electroweak.wz_massive_from_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L257-L265)
**theorem
Tau.BookIV.Electroweak.wz_massive_from_omega :w_plus.massive = true ∧ w_minus.massive = true ∧ z_zero.massive = true**


[IV.P53] W and Z bosons are massive because omega is the conical
singularity of L (lemniscate crossing point). The crossing fixes
a coherence scale, breaking the would-be massless gauge symmetry.
Structural: massive = true for both W and Z.

---

### `Tau.BookIV.Electroweak.w_left_only`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality.lean#L267-L270)
**theorem
Tau.BookIV.Electroweak.w_left_only :w_plus.left_only = true ∧ w_minus.left_only = true**


W bosons couple only to left-handed fermions.
