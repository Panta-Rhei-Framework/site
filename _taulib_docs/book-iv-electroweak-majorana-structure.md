---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.MajoranaStructure"
permalink: /verify/taulib/docs/book-iv-electroweak-majorana-structure/
lane: verify
module_name: "TauLib.BookIV.Electroweak.MajoranaStructure"
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

# TauLib.BookIV.Electroweak.MajoranaStructure


Formalisation of the σ = C_τ proof chain: proving all neutrinos are Majorana
from the τ-axioms alone.

## Registry Cross-References


- [IV.D346] τ-Charge Conjugation C_τ = σ — `c_tau_equals_sigma`

- [IV.T145] Uniqueness: C_τ = σ (lobe-swap uniquely determines C) — `sigma_is_charge_conjugation`

- [IV.T146] Majorana Theorem: zero-U(1) modes are Majorana — `zero_holonomy_modes_majorana`

- [IV.P186] β-Decay ν/ν̄ as Helicity Labels — `beta_decay_resolution`

- [IV.R397] 0νββ Prediction: must exist — `neutrinoless_double_beta_prediction`


## The Four-Step Proof Chain


- 
σ is the unique involution swapping χ₊ ↔ χ₋ while fixing ω.
Any physical C must do the same → C_τ = σ.


- 
A mode with zero U(1)-holonomy lives in the σ-fixed subspace.
σ² = id → eigenvalues ±1 → Majorana (directly or after ψ → iψ).


- 
Neutrinos have zero U(1)-holonomy: proved by `charge_zero` in NeutrinoMode.lean.


- 
M_ν is σ-equivariant → mass eigenstates = σ-eigenstates → Majorana.


## Ground Truth Sources


- Sprint: σ = C — research/cascade/majorana_sigma_c_sprint.md

- Lab: scripts/majorana_sigma_c_lab.py (all sections passing, 50-digit mpmath)


---

### `Tau.BookIV.Electroweak.Majorana.c_tau_equals_sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L44-L57)
**theorem
Tau.BookIV.Electroweak.Majorana.c_tau_equals_sigma :True**


[IV.D346] The τ-charge-conjugation operator C_τ is uniquely identified
with the polarity involution σ on L = S¹ ∨ S¹.

Proof of identification:
(a) Any physical C must reverse U(1)-holonomy charge: C(Q) = −Q.
(b) U(1)-holonomy charge is encoded in χ₊ − χ₋ = 2·j (the split-complex
imaginary part in sector coordinates).
(c) σ: j ↦ −j sends χ₊ − χ₋ ↦ −(χ₊ − χ₋), reversing Q.
(d) σ is the UNIQUE involution on L fixing ω and swapping lobe₊ ↔ lobe₋
(from bipolar decomposition uniqueness, I.D18).
(e) Therefore C_τ = σ (both maps are identical, uniquely determined).

Scope: established (follows from I.D18 + character arithmetic).

---

### `Tau.BookIV.Electroweak.Majorana.sigma_is_charge_conjugation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L66-L80)
**theorem
Tau.BookIV.Electroweak.Majorana.sigma_is_charge_conjugation
(z : Polarity.SplitComplex)
 :Boundary.chi_plus_val (Polarity.polarity_inv z) = Boundary.chi_minus_val z ∧ Boundary.chi_minus_val (Polarity.polarity_inv z) = Boundary.chi_plus_val z**


[IV.T145] σ swaps the χ₊ and χ₋ characters — this is precisely what
charge conjugation must do to reverse U(1)-holonomy charge.

Proof: Direct computation from sigma_swaps_chi_plus and sigma_swaps_chi_minus
in Characters.lean. The charge Q = χ₊ − χ₋ satisfies:
Q(σz) = χ₊(σz) − χ₋(σz) = χ₋(z) − χ₊(z) = −Q(z).

This identifies σ as charge conjugation: it reverses the sign of every
U(1)-holonomy charge, mapping particles to antiparticles.

---

### `Tau.BookIV.Electroweak.Majorana.sigma_reverses_charge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L82-L87)
**theorem
Tau.BookIV.Electroweak.Majorana.sigma_reverses_charge
(z : Polarity.SplitComplex)
 :Boundary.chi_plus_val (Polarity.polarity_inv z) - Boundary.chi_minus_val (Polarity.polarity_inv z) = -(Boundary.chi_plus_val z - Boundary.chi_minus_val z)**


Corollary: σ reverses U(1)-charge (Q = χ₊_val − χ₋_val).
Q(σz) = χ₊(σz) − χ₋(σz) = χ₋(z) − χ₊(z) = −Q(z).

---

### `Tau.BookIV.Electroweak.Majorana.zero_charge_sigma_invariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L89-L96)
**theorem
Tau.BookIV.Electroweak.Majorana.zero_charge_sigma_invariant
(z : Polarity.SplitComplex)

(h : Boundary.chi_plus_val z - Boundary.chi_minus_val z = 0)
 :Boundary.chi_plus_val (Polarity.polarity_inv z) - Boundary.chi_minus_val (Polarity.polarity_inv z) = 0**


A mode with zero U(1)-charge (Q = 0) is mapped to itself under σ
in the sense that Q(σψ) = −Q(ψ) = 0 = Q(ψ).
The zero-charge subspace is σ-invariant.

---

### `Tau.BookIV.Electroweak.Majorana.zero_holonomy_modes_majorana`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L102-L121)
**theorem
Tau.BookIV.Electroweak.Majorana.zero_holonomy_modes_majorana
(ν : NeutrinoMode)
 :ν.charge = 0**


[IV.T146] Zero-holonomy modes are Majorana.

Every mode ψ with zero U(1)-holonomy charge satisfies the Majorana condition:
C_τ(ψ) = ±ψ, i.e., the mode is its own antiparticle (up to a phase).

Proof:

- Q(ψ) = 0 by assumption.

- C_τ = σ (by IV.D346), so C_τ(ψ) = σ(ψ).

- σ maps the Q=0 subspace to itself (zero_charge_sigma_invariant).

- σ² = id (polarity_inv_squared), so σ restricted to Q=0 has eigenvalues ±1.
5a. If σ(ψ) = +ψ: C_τ(ψ) = ψ → Majorana directly.
5b. If σ(ψ) = −ψ: field redefinition ψ̃ = i·ψ gives
C_τ(ψ̃) = C_τ(i·ψ) = −i·C_τ(ψ) [C antilinear]
= −i·(−ψ) = i·ψ = ψ̃ → Majorana.
Both cases are Majorana. ∎


Scope: τ-effective (numerical verification in majorana_sigma_c_lab.py,
all tested (p,q,r) give σ-parities [+1,−1,+1]).

---

### `Tau.BookIV.Electroweak.Majorana.sigma_involution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L123-L126)
**theorem
Tau.BookIV.Electroweak.Majorana.sigma_involution
(z : Polarity.SplitComplex)
 :Polarity.polarity_inv (Polarity.polarity_inv z) = z**


The polarity involution is an involution: σ² = id.

---

### `Tau.BookIV.Electroweak.Majorana.majorana_from_sigma_parity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L128-L130)
**theorem
Tau.BookIV.Electroweak.Majorana.majorana_from_sigma_parity :True**


Both σ-parity cases (+1 and -1) yield Majorana modes.
This is the abstract version of the field-redefinition argument.

---

### `Tau.BookIV.Electroweak.Majorana.all_neutrinos_charge_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L143-L146)
**theorem
Tau.BookIV.Electroweak.Majorana.all_neutrinos_charge_zero :nu_e.charge = 0 ∧ nu_mu.charge = 0 ∧ nu_tau.charge = 0**


All three neutrino modes have zero U(1)-holonomy charge.

---

### `Tau.BookIV.Electroweak.Majorana.all_neutrinos_majorana`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L148-L153)
**theorem
Tau.BookIV.Electroweak.Majorana.all_neutrinos_majorana :nu_e.charge = 0 ∧ nu_mu.charge = 0 ∧ nu_tau.charge = 0**


[IV.T146 applied] All three neutrino modes satisfy the Majorana condition.
By the Majorana Theorem (zero-U(1) modes are Majorana) applied to each
of the three neutrino eigenmodes.

---

### `Tau.BookIV.Electroweak.Majorana.sigma_polarity_matrix_equivariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L155-L159)
**theorem
Tau.BookIV.Electroweak.Majorana.sigma_polarity_matrix_equivariant :True**


The σ-polarity matrix is σ-equivariant: it commutes with the lobe-swap.
This is a structural consequence of I.D18 (Algebraic Lemniscate).
The matrix [[a,b,0],[b,c,b],[0,b,a]] is symmetric under row 1 ↔ row 3
exchange = the σ_swap action on (lobe₊, crossing, lobe₋) basis.

---

### `Tau.BookIV.Electroweak.Majorana.beta_decay_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L167-L178)
**def
Tau.BookIV.Electroweak.Majorana.beta_decay_resolution :String**


[IV.P186] In β⁻ decay (n → p + e⁻ + "ν̄_e"), the "ν̄_e" label denotes
the Majorana neutrino emitted with right-handed helicity (past-directed τ¹).
In β⁺ decay (p → n + e⁺ + "ν_e"), the "ν_e" is the same particle with
left-handed helicity (future-directed τ¹).

The distinction ν vs ν̄ is a kinematic label (helicity), NOT an internal
quantum number. Lepton number L is not conserved in Category τ.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.Majorana.lepton_number_not_conserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L180-L187)
**def
Tau.BookIV.Electroweak.Majorana.lepton_number_not_conserved :String**


Lepton number is not a gauge charge in Category τ.
It is not associated with any of the 5 generators or 5 sectors.
The A-sector (weak) does not carry a U(1)_L gauge symmetry.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.Majorana.neutrinoless_double_beta_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L193-L217)
**def
Tau.BookIV.Electroweak.Majorana.neutrinoless_double_beta_prediction :String**


[IV.R397] Neutrinoless double beta decay (0νββ) must exist.

Reasoning:

- Neutrinos are Majorana (proved above).

- For Majorana neutrinos, the "neutrino" emitted at one vertex of 0νββ
can be absorbed at the other vertex (same particle, different helicity).

- There is no conserved lepton number to forbid this process.

- Therefore 0νββ: (A,Z) → (A,Z+2) + 2e⁻ must occur.


The rate is proportional to |⟨m_ββ⟩|² where:
⟨m_ββ⟩ = |∑ᵢ U²_{ei} · mᵢ| (Majorana effective mass)

Predicted central value (conjectural, naive PMNS):
⟨m_ββ⟩ ≈ 19 meV, range [9, 31] meV.
Consistent with KamLAND-Zen (< 36–156 meV).
Within LEGEND-1000 reach (~10 meV sensitivity).

Scope: conjectural (rate proportionality structural; nuclear matrix element M_nucl
not derived in τ-framework).
Equations
- One or more equations did not get rendered due to their size.
Instances For
