---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.WeakChirality2"
permalink: /verify/taulib/docs/book-iv-electroweak-weak-chirality2/
lane: verify
module_name: "TauLib.BookIV.Electroweak.WeakChirality2"
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

# TauLib.BookIV.Electroweak.WeakChirality2


Chirality selection theorem, parity bridge recall, polarity-switching
suppression, SU(2)_L identification, and structural remarks on
right-handed invisibility and parity preservation.

## Registry Cross-References


- [IV.C01] Right-Handed Configurations Invisible — `right_handed_invisible`

- [IV.D319] Polarity-Switching Transition in A-Sector — `PolaritySwitching`

- [IV.T122] Parity Bridge Recall (III.T07) — `parity_bridge_recall`

- [IV.T123] Chirality Selection Theorem — `chirality_selection`

- [IV.P54] EM, Strong, Gravity Are Parity-Preserving — `non_weak_parity_preserving`

- [IV.P55] SU(2)_L As Automorphism Group — `su2l_identification`

- [IV.P174] Polarity-Switching Suppressed by exp(-pol(X)) — `switching_suppression`

- [IV.R28] Chirality is boundary-character property — (structural remark)

- [IV.R380] Parity violation is a tau-effective prediction — (structural remark)

- [IV.R382] No right-handed neutrinos in minimal tau — (structural remark)

- [IV.R383] CP violation from sigma-polarity involution — (structural remark)


## Ground Truth Sources


- Chapter 30 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.right_handed_invisible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L37-L42)
**theorem
Tau.BookIV.Electroweak.right_handed_invisible :sigma_a_admissible ChiralityType.Right = false**


[IV.C01] Right-handed fermion configurations are invisible to the
weak force. This is a structural consequence: sigma_A-inadmissible
states do not couple to A-sector transport modes.
Formalized as: sigma_a_admissible Right = false.

---

### `Tau.BookIV.Electroweak.right_handed_no_weak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L44-L48)
**theorem
Tau.BookIV.Electroweak.right_handed_no_weak :sigma_a_admissible ChiralityType.Right = false ∧ sigma_a_admissible ChiralityType.Left = true**


Right-handed states have zero weak coupling.

---

### `Tau.BookIV.Electroweak.PolaritySwitching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L54-L69)
**structure
Tau.BookIV.Electroweak.PolaritySwitching :Type**


[IV.D319] A polarity-switching transition in the A-sector: a process
that changes the chi_plus/chi_minus composition of a state.
The W boson mediates such transitions (e.g., up-quark to down-quark).
The transition amplitude depends on the sector polarity measure.

- source : ChiralityType
Source chirality.

- target : ChiralityType
Target chirality.

- source_left : self.source = ChiralityType.Left
Source must be left-handed (sigma_A-admissible).

- target_left : self.target = ChiralityType.Left
Target must be left-handed.

- mediator : String
The mediating boson name.

Instances For

---

### `Tau.BookIV.Electroweak.instReprPolaritySwitching.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L69-L69)
**def
Tau.BookIV.Electroweak.instReprPolaritySwitching.repr :PolaritySwitching → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPolaritySwitching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L69-L69)
**instance
Tau.BookIV.Electroweak.instReprPolaritySwitching :Repr PolaritySwitching**

Equations
- Tau.BookIV.Electroweak.instReprPolaritySwitching = { reprPrec := Tau.BookIV.Electroweak.instReprPolaritySwitching.repr }

---

### `Tau.BookIV.Electroweak.w_transition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L71-L77)
**def
Tau.BookIV.Electroweak.w_transition :PolaritySwitching**


Canonical polarity-switching transition via W boson.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ParityBridgeRecall`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L83-L94)
**structure
Tau.BookIV.Electroweak.ParityBridgeRecall :Prop**


[IV.T122] Parity Bridge Recall (III.T07): the A-sector is the unique
sector where the sigma-involution acts non-trivially on chirality.
This is the physical consequence of the Parity Bridge theorem
from Book III. The balanced polarity (chi_plus = chi_minus = 50)
implies maximal parity violation.

- a_balanced : pol_A.chi_plus = pol_A.chi_minus
The A-sector has balanced polarity.

- d_not_balanced : pol_D.chi_plus ≠ pol_D.chi_minus
Only A is balanced among primitive sectors.

- b_not_balanced : pol_B.chi_plus ≠ pol_B.chi_minus
- c_not_balanced : pol_C.chi_plus ≠ pol_C.chi_minus
Instances For

---

### `Tau.BookIV.Electroweak.parity_bridge_recall`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L96-L101)
**def
Tau.BookIV.Electroweak.parity_bridge_recall :ParityBridgeRecall**


The parity bridge recall is verified by computation.
Equations
- Tau.BookIV.Electroweak.parity_bridge_recall = ⋯
Instances For

---

### `Tau.BookIV.Electroweak.chirality_selection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L107-L116)
**theorem
Tau.BookIV.Electroweak.chirality_selection
(c : ChiralityType)
 :sigma_a_admissible c = true ↔ c = ChiralityType.Left**


[IV.T123] Chirality Selection Theorem: the weak interaction selects
exactly the left-handed projection. This follows from:
(1) A-sector has balanced polarity (Parity Bridge),
(2) sigma_A acts non-trivially (flips chirality),
(3) only sigma_A-admissible states couple to W/Z.

Formally: for all chirality types c, c couples to weak iff c = Left.

---

### `Tau.BookIV.Electroweak.chirality_selection_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L118-L120)
**theorem
Tau.BookIV.Electroweak.chirality_selection_complete :sigma_a_admissible ChiralityType.Left = true**


The selection is complete: every left-handed state couples.

---

### `Tau.BookIV.Electroweak.chirality_selection_exclusive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L122-L124)
**theorem
Tau.BookIV.Electroweak.chirality_selection_exclusive :sigma_a_admissible ChiralityType.Right = false**


The selection is exclusive: no right-handed state couples.

---

### `Tau.BookIV.Electroweak.non_weak_parity_preserving`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L130-L137)
**theorem
Tau.BookIV.Electroweak.non_weak_parity_preserving :parity_em.preserves = true ∧ parity_strong.preserves = true ∧ parity_gravity.preserves = true**


[IV.P54] EM, Strong, and Gravity are parity-preserving:
they do not distinguish chirality. Their parity violation
measure is zero.

---

### `Tau.BookIV.Electroweak.weak_unique_non_preserving`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L139-L146)
**theorem
Tau.BookIV.Electroweak.weak_unique_non_preserving :parity_weak.preserves = false ∧ parity_em.preserves = true ∧ parity_strong.preserves = true ∧ parity_gravity.preserves = true ∧ parity_higgs.preserves = true**


Weak is the unique non-preserving sector.

---

### `Tau.BookIV.Electroweak.SU2LIdentification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L152-L168)
**structure
Tau.BookIV.Electroweak.SU2LIdentification :Type**


[IV.P55] SU(2)_L as the automorphism group of the A-sector
left-handed doublet structure. The subscript L means "left":
only left-handed fermions transform under SU(2)_L.

Structural encoding: gauge_group_dim = 3 (dim of SU(2)),
chirality = Left (only left-handed transforms).

- gauge_dim : ℕ
Gauge group dimension: dim SU(2) = 3.

- gauge_dim_eq : self.gauge_dim = 3
- num_generators : ℕ
Number of generators = 3 (Pauli matrices).

- num_gen_eq : self.num_generators = 3
- chirality : ChiralityType
Only left-handed chirality.

- chirality_left : self.chirality = ChiralityType.Left
Instances For

---

### `Tau.BookIV.Electroweak.instReprSU2LIdentification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L168-L168)
**def
Tau.BookIV.Electroweak.instReprSU2LIdentification.repr :SU2LIdentification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprSU2LIdentification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L168-L168)
**instance
Tau.BookIV.Electroweak.instReprSU2LIdentification :Repr SU2LIdentification**

Equations
- Tau.BookIV.Electroweak.instReprSU2LIdentification = { reprPrec := Tau.BookIV.Electroweak.instReprSU2LIdentification.repr }

---

### `Tau.BookIV.Electroweak.su2l_identification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L170-L177)
**def
Tau.BookIV.Electroweak.su2l_identification :SU2LIdentification**


The canonical SU(2)_L identification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.polarity_difference`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L183-L191)
**def
Tau.BookIV.Electroweak.polarity_difference
(p : PolarityIndex)
 :ℤ**


[IV.P174] Polarity-switching transitions are suppressed in sectors
with unbalanced polarity. The suppression factor is exp(-|pol(X)|)
where pol(X) = chi_plus - chi_minus. For unbalanced sectors,
|pol| > 0, so transitions are exponentially suppressed.
For the balanced A-sector, |pol| = 0 and there is no suppression.

Structural: we verify that only A has pol = 0.
Equations
- Tau.BookIV.Electroweak.polarity_difference p = Int.ofNat p.chi_plus - Int.ofNat p.chi_minus
Instances For

---

### `Tau.BookIV.Electroweak.switching_suppression_a_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L193-L195)
**theorem
Tau.BookIV.Electroweak.switching_suppression_a_zero :polarity_difference pol_A = 0**


---

### `Tau.BookIV.Electroweak.switching_suppression_d_nonzero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L197-L199)
**theorem
Tau.BookIV.Electroweak.switching_suppression_d_nonzero :polarity_difference pol_D ≠ 0**


---

### `Tau.BookIV.Electroweak.switching_suppression_b_nonzero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L201-L203)
**theorem
Tau.BookIV.Electroweak.switching_suppression_b_nonzero :polarity_difference pol_B ≠ 0**


---

### `Tau.BookIV.Electroweak.switching_suppression_c_nonzero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeakChirality2.lean#L205-L207)
**theorem
Tau.BookIV.Electroweak.switching_suppression_c_nonzero :polarity_difference pol_C ≠ 0**
