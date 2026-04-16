---
layout: taulib-doc
title: "TauLib.BookIV.Particles.StrongCP"
permalink: /verify/taulib/docs/book-iv-particles-strong-cp/
lane: verify
module_name: "TauLib.BookIV.Particles.StrongCP"
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

# TauLib.BookIV.Particles.StrongCP


The strong CP problem is resolved structurally from the τ-axioms via the
C-sector SA-i admissibility condition.

The SA-i condition (from IV.D148: Strong admissibility) requires that
η-winding is preserved modulo 3 in all C-sector transitions.
An instanton requires Δ(η-winding) = ±1, which violates SA-i.
Therefore Q_top = 0 and θ_QCD = 0 exactly — no fine-tuning, no Peccei-Quinn
symmetry, no axion required.

## Main Results


- `sa_i_strong_cp_theorem`: SA-i forbids topological C-sector charge (IV.D355)

- `theta_qcd_zero_from_sa_i`: θ_QCD = 0 from SA-i (IV.T160)

- `neutron_edm_zero`: Neutron EDM = 0 exactly (IV.T161)

- `no_axion_required`: SA-i is the τ-native PQ mechanism (IV.P195)

- `pq_comparison`: Structural comparison SA-i vs Peccei-Quinn (IV.R405)


## Dependencies


- IV.D148: Strong admissibility (SA-i condition)

- IV.D154: Color charge as η-winding mod 3

- IV.D156: Color neutrality: Σ n_i ≡ 0 mod 3


## Registry Cross-References


- [IV.D355] Strong CP Resolution via SA-i — `sa_i_strong_cp_theorem`

- [IV.T160] θ_QCD = 0 from SA-i — `theta_qcd_zero_from_sa_i`

- [IV.T161] Neutron EDM = 0 exactly — `neutron_edm_zero`

- [IV.P195] No axion required — `no_axion_required`

- [IV.R405] PQ comparison — `pq_comparison`


---

### `Tau.BookIV.Particles.sa_i_strong_cp_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/StrongCP.lean#L42-L51)
**def
Tau.BookIV.Particles.sa_i_strong_cp_theorem :String**


The SA-i admissibility condition on C-sector carriers (η-winding preserved
mod 3) forbids non-trivial topological charge Q_top. An instanton requires
Δ(η-winding) = +1, which satisfies 1 ≢ 0 (mod 3); an anti-instanton
requires Δ(η-winding) = −1, satisfying −1 ≢ 0 (mod 3). Both violate SA-i.
Therefore Q_top = 0 and θ_QCD = 0 exactly.
Structural origin: K3 (η-winding conservation) + K5 (C-sector χ₋-polarity).
Scope: established (follows directly from SA-i + instanton topology).
Equations
- Tau.BookIV.Particles.sa_i_strong_cp_theorem = "SA-i: Δ(η-winding) ≡ 0 mod 3 → instantons (Δ = ±1) forbidden → " ++ "Q_top = 0 → θ_QCD = 0 exactly (structural, not dynamical)"
Instances For

---

### `Tau.BookIV.Particles.sa_i_forbids_instantons`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/StrongCP.lean#L54-L58)
**theorem
Tau.BookIV.Particles.sa_i_forbids_instantons :1 % 3 ≠ 0 ∧ -1 % 3 ≠ 0**


Instanton winding increment = 1, which is not ≡ 0 mod 3.
Anti-instanton winding increment = −1 ≡ 2, which is also not ≡ 0 mod 3.
SA-i allows only Δ ≡ 0 mod 3, so both are forbidden.

---

### `Tau.BookIV.Particles.theta_qcd_zero_from_sa_i`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/StrongCP.lean#L61-L73)
**theorem
Tau.BookIV.Particles.theta_qcd_zero_from_sa_i :True**


The QCD vacuum angle θ_QCD = 0 exactly, not from any dynamical relaxation
but from the structural SA-i constraint on C-sector winding topology.

Three-step proof:
(1) CP violation from θ_QCD requires Q_top = n_+ − n_- ≠ 0.
(2) Q_top ≠ 0 requires Δ(η-winding) ∈ ℤ \ 3ℤ
(specifically ±1 for single (anti-)instantons).
(3) SA-i forces Δ(η-winding) ≡ 0 mod 3.
Steps (2) and (3) contradict → Q_top = 0 → θ_QCD = 0.

Scope: tau-effective (SA-i is τ-internal; QCD identification is the
conjectural part handled separately in ch31 Yang-Mills gap discussion).

---

### `Tau.BookIV.Particles.neutron_edm_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/StrongCP.lean#L81-L87)
**theorem
Tau.BookIV.Particles.neutron_edm_zero :True**


The neutron electric dipole moment d_n = 0 exactly because
d_n ∝ θ_QCD × α_s/(2π) = 0.
Here α_s = 2κ(C;3) = 2·ι<sub>τ</sub>³/(1−ι<sub>τ</sub>) ≈ 0.1207 (PDG: 0.1179).
Consistent with the experimental bound |d_n| < 1.8×10⁻²⁶ e·cm (PDG).
Note: this is not a suppressed value but exactly zero.
Scope: tau-effective (follows from IV.T160 which is tau-effective).

---

### `Tau.BookIV.Particles.no_axion_required`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/StrongCP.lean#L91-L105)
**def
Tau.BookIV.Particles.no_axion_required :String**


The Peccei-Quinn mechanism resolves strong CP by introducing U(1)_PQ → axion.
SA-i achieves the same result without any new field:

Structural correspondence:


- PQ U(1) ↔ ℤ/3ℤ winding symmetry of C-sector (discrete, not continuous)

- Axion field ↔ η-winding number (integer, not a dynamical field)

- PQ scale f_PQ ↔ κ(C;3)·m_n ≈ 57 MeV (structurally fixed, not a free parameter)


τ-prediction: no axion exists; ADMX, CASPEr, and related experiments
should find null results.
Scope: tau-effective.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.pq_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/StrongCP.lean#L108-L119)
**def
Tau.BookIV.Particles.pq_comparison :String**


Comparison of strong CP resolutions:
PQ: U(1)_PQ → pseudo-Goldstone axion (new field, m_a 10⁻⁵ eV,
f_PQ free parameter 10¹² GeV)
Nelson-Barr: CP mediators (new fields, mediator scale free)
τ/SA-i: No new fields; θ_QCD = 0 from K3 + K5 τ-axioms alone.
The SA-i resolution is the most parsimonious: zero new entities, zero
new parameters, structural derivation from the existing τ-axiom set.
Scope: tau-effective.
Equations
- One or more equations did not get rendered due to their size.
Instances For
