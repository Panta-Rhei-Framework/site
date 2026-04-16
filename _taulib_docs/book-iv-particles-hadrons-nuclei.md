---
layout: taulib-doc
title: "TauLib.BookIV.Particles.HadronsNuclei"
permalink: /verify/taulib/docs/book-iv-particles-hadrons-nuclei/
lane: verify
module_name: "TauLib.BookIV.Particles.HadronsNuclei"
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

# TauLib.BookIV.Particles.HadronsNuclei


Hadron structure (baryons, mesons), quark confinement in hadrons,
nucleon mass decomposition, nuclear binding from strong+EM balance,
nuclear shell model, magic numbers, iron peak, and decay channels
from sector admissibility.

## Registry Cross-References


- [IV.D200] Meson Classification — `MesonClassification`

- [IV.D201] Glueball — `GlueballDef`

- [IV.D202] Nuclear Force — `NuclearForce`

- [IV.P128] Nucleon Mass Decomposition — `nucleon_mass_decomposition`

- [IV.P129] Nuclear Force Saturation — `nuclear_force_saturation`

- [IV.P130] Nuclear Shell Structure — `nuclear_shell_structure`

- [IV.P131] Iron Peak from Competing Sectors — `iron_peak`

- [IV.P132] Decay Channels from Sector Admissibility — `decay_channels`

- [IV.R128] Eta-eta' Splitting — `eta_eta_prime` (conjectural)

- [IV.R129] Glueballs and the Mass Gap — `glueballs_mass_gap`

- [IV.R130] Mass from Nothing — comment-only (not_applicable)

- [IV.R131] Isospin Splitting from Polarity — `isospin_splitting`

- [IV.R132] Proton Lighter but Ontologically Later — comment-only (not_applicable)

- [IV.R133] Deuteron Binding in tau-language — `deuteron_binding`

- [IV.R134] Spin-orbit from omega-sector — comment-only (not_applicable)

- [IV.R135] Why He-4 is Tightly Bound — `helium4_tightly_bound`

- [IV.R136] Nucleosynthesis Forward to Book V — `nucleosynthesis_forward`

- [IV.R137] Alpha-decay as Mode Cluster Ejection — `alpha_decay_mode`

- [IV.R138] Neutron Stability inside Nuclei — `neutron_stability_nuclear`

- [IV.R139] Gamma-decay as Mode Transition — `gamma_decay_mode`


## Mathematical Content


Hadrons are color-neutral composites: mesons (qq̄, B = 0) and baryons
(qqq, B = 1). The nucleon mass is 99% vacuum + kinetic energy from
confinement, only 1% from quark rest masses. Nuclear binding comes from
residual C-sector interaction, with shell structure producing magic
numbers (2, 8, 20, 28, 50, 82, 126). The iron peak (A ≈ 56) results
from optimal C-sector binding vs B-sector Coulomb repulsion balance.

## Ground Truth Sources


- Chapter 48 of Book IV (2nd Edition)


---

### `Tau.BookIV.Particles.BaryonNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L55-L61)
**inductive
Tau.BookIV.Particles.BaryonNumber :Type**


Hadron baryon number.

- zero : BaryonNumber
Meson: B = 0 (quark-antiquark).

- one : BaryonNumber
Baryon: B = 1 (three quarks).

Instances For

---

### `Tau.BookIV.Particles.instReprBaryonNumber.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L61-L61)
**def
Tau.BookIV.Particles.instReprBaryonNumber.repr :BaryonNumber → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprBaryonNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L61-L61)
**instance
Tau.BookIV.Particles.instReprBaryonNumber :Repr BaryonNumber**

Equations
- Tau.BookIV.Particles.instReprBaryonNumber = { reprPrec := Tau.BookIV.Particles.instReprBaryonNumber.repr }

---

### `Tau.BookIV.Particles.instDecidableEqBaryonNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L61-L61)
**instance
Tau.BookIV.Particles.instDecidableEqBaryonNumber :DecidableEq BaryonNumber**

Equations
- Tau.BookIV.Particles.instDecidableEqBaryonNumber x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Particles.instBEqBaryonNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L61-L61)
**instance
Tau.BookIV.Particles.instBEqBaryonNumber :BEq BaryonNumber**

Equations
- Tau.BookIV.Particles.instBEqBaryonNumber = { beq := Tau.BookIV.Particles.instBEqBaryonNumber.beq }

---

### `Tau.BookIV.Particles.instBEqBaryonNumber.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L61-L61)
**def
Tau.BookIV.Particles.instBEqBaryonNumber.beq :BaryonNumber → BaryonNumber → Bool**

Equations
- Tau.BookIV.Particles.instBEqBaryonNumber.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Particles.MesonClassification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L63-L81)
**structure
Tau.BookIV.Particles.MesonClassification :Type**


[IV.D200] A meson |q_i q̄_j⟩ classified by:

- Flavor content (quark flavors from {u,d,s,c,b,t})

- Spin-parity J^PC (angular momentum + spin)

- Generation class (lemniscate mode classes of constituents)


Pseudoscalar (J=0): anti-aligned spins.
Vector (J=1): aligned spins.

- name : String
Name.

- quark : String
Quark content.

- antiquark : String
Antiquark content.

- spin : ℕ
Spin J.

- mass_mev : ℕ
Approximate mass (MeV).

Instances For

---

### `Tau.BookIV.Particles.instReprMesonClassification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L81-L81)
**def
Tau.BookIV.Particles.instReprMesonClassification.repr :MesonClassification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprMesonClassification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L81-L81)
**instance
Tau.BookIV.Particles.instReprMesonClassification :Repr MesonClassification**

Equations
- Tau.BookIV.Particles.instReprMesonClassification = { reprPrec := Tau.BookIV.Particles.instReprMesonClassification.repr }

---

### `Tau.BookIV.Particles.pion_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L83-L85)
**def
Tau.BookIV.Particles.pion_plus :MesonClassification**


Canonical mesons.
Equations
- Tau.BookIV.Particles.pion_plus = { name := "pi+", quark := "u", antiquark := "d_bar", spin := 0, mass_mev := 140 }
Instances For

---

### `Tau.BookIV.Particles.kaon_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L87-L88)
**def
Tau.BookIV.Particles.kaon_plus :MesonClassification**

Equations
- Tau.BookIV.Particles.kaon_plus = { name := "K+", quark := "u", antiquark := "s_bar", spin := 0, mass_mev := 494 }
Instances For

---

### `Tau.BookIV.Particles.rho_meson`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L90-L91)
**def
Tau.BookIV.Particles.rho_meson :MesonClassification**

Equations
- Tau.BookIV.Particles.rho_meson = { name := "rho", quark := "u", antiquark := "d_bar", spin := 1, mass_mev := 775 }
Instances For

---

### `Tau.BookIV.Particles.EtaEtaPrime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L97-L107)
**structure
Tau.BookIV.Particles.EtaEtaPrime :Type**


[IV.R128] The η-η' mass splitting (~410 MeV) exceeds quark mass
predictions alone: the resolution is the axial anomaly breaking
U(1)_A symmetry via quantum effects. Conjectural scope.

- splitting_mev : ℕ
Splitting in MeV.

- mechanism : String
Mechanism.

- scope : String
Scope.

Instances For

---

### `Tau.BookIV.Particles.instReprEtaEtaPrime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L107-L107)
**instance
Tau.BookIV.Particles.instReprEtaEtaPrime :Repr EtaEtaPrime**

Equations
- Tau.BookIV.Particles.instReprEtaEtaPrime = { reprPrec := Tau.BookIV.Particles.instReprEtaEtaPrime.repr }

---

### `Tau.BookIV.Particles.instReprEtaEtaPrime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L107-L107)
**def
Tau.BookIV.Particles.instReprEtaEtaPrime.repr :EtaEtaPrime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.eta_eta_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L109-L109)
**def
Tau.BookIV.Particles.eta_eta_prime :EtaEtaPrime**

Equations
- Tau.BookIV.Particles.eta_eta_prime = { }
Instances For

---

### `Tau.BookIV.Particles.GlueballDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L115-L129)
**structure
Tau.BookIV.Particles.GlueballDef :Type**


[IV.D201] A glueball is a bound state of the strong vacuum field
Γ_s* with no quark content: a color-neutral excitation of the
su(3) connection field above the vacuum minimum.

Predicted by lattice QCD at ~1.5-1.7 GeV for J^PC = 0^++.

- quark_content : ℕ
Quark content: none.

- mass_low_mev : ℕ
Predicted mass range low (MeV).

- mass_high_mev : ℕ
Predicted mass range high (MeV).

- jpc : String
Quantum numbers J^PC.

Instances For

---

### `Tau.BookIV.Particles.instReprGlueballDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L129-L129)
**instance
Tau.BookIV.Particles.instReprGlueballDef :Repr GlueballDef**

Equations
- Tau.BookIV.Particles.instReprGlueballDef = { reprPrec := Tau.BookIV.Particles.instReprGlueballDef.repr }

---

### `Tau.BookIV.Particles.instReprGlueballDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L129-L129)
**def
Tau.BookIV.Particles.instReprGlueballDef.repr :GlueballDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.glueball_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L131-L131)
**def
Tau.BookIV.Particles.glueball_def :GlueballDef**

Equations
- Tau.BookIV.Particles.glueball_def = { }
Instances For

---

### `Tau.BookIV.Particles.glueball_no_quarks`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L133-L133)
**theorem
Tau.BookIV.Particles.glueball_no_quarks :glueball_def.quark_content = 0**


---

### `Tau.BookIV.Particles.glueballs_mass_gap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L139-L143)
**def
Tau.BookIV.Particles.glueballs_mass_gap :String**


[IV.R129] Glueball existence is a direct consequence of the mass gap:
confinement ensures every excitation above vacuum carries positive mass.
m_gb ≈ 2π/σ_τ^(1/2) ≈ 1.5 GeV.
Equations
- Tau.BookIV.Particles.glueballs_mass_gap = "Glueball existence: structural consequence of mass gap (confinement)"
Instances For

---

### `Tau.BookIV.Particles.NucleonMassDecomp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L149-L170)
**structure
Tau.BookIV.Particles.NucleonMassDecomp :Type**


[IV.P128] m_N = E_vac + E_kin + Σm_qi


- C-sector vacuum energy: ~400 MeV (42%)

- Quark kinetic energy: ~500 MeV (53%)

- Bare quark rest masses: ~12 MeV (1%)

- Trace anomaly + sigma terms: ~27 MeV (3%)


Vacuum + kinetic ≈ 99% of nucleon mass.
All energies in MeV.

- e_vac_mev : ℕ
Vacuum energy (MeV).

- e_kin_mev : ℕ
Kinetic energy (MeV).

- e_quark_mev : ℕ
Quark rest masses (MeV).

- e_other_mev : ℕ
Other (trace anomaly, sigma).

- total_mev : ℕ
Total nucleon mass (MeV, approximate).

- nonquark_pct : ℕ
Percentage from non-quark-mass sources.

Instances For

---

### `Tau.BookIV.Particles.instReprNucleonMassDecomp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L170-L170)
**instance
Tau.BookIV.Particles.instReprNucleonMassDecomp :Repr NucleonMassDecomp**

Equations
- Tau.BookIV.Particles.instReprNucleonMassDecomp = { reprPrec := Tau.BookIV.Particles.instReprNucleonMassDecomp.repr }

---

### `Tau.BookIV.Particles.instReprNucleonMassDecomp.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L170-L170)
**def
Tau.BookIV.Particles.instReprNucleonMassDecomp.repr :NucleonMassDecomp → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.nucleon_mass_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L172-L172)
**def
Tau.BookIV.Particles.nucleon_mass_decomposition :NucleonMassDecomp**

Equations
- Tau.BookIV.Particles.nucleon_mass_decomposition = { }
Instances For

---

### `Tau.BookIV.Particles.nucleon_99pct_nonquark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L174-L175)
**theorem
Tau.BookIV.Particles.nucleon_99pct_nonquark :nucleon_mass_decomposition.nonquark_pct = 99**


---

### `Tau.BookIV.Particles.nucleon_decomp_sums`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L177-L183)
**theorem
Tau.BookIV.Particles.nucleon_decomp_sums :nucleon_mass_decomposition.e_vac_mev + nucleon_mass_decomposition.e_kin_mev + nucleon_mass_decomposition.e_quark_mev + nucleon_mass_decomposition.e_other_mev = nucleon_mass_decomposition.total_mev**


Decomposition sums to approximately the nucleon mass.

---

### `Tau.BookIV.Particles.IsospinSplitting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L189-L201)
**structure
Tau.BookIV.Particles.IsospinSplitting :Type**


[IV.R131] m_d > m_u has structural origin: the d-quark has
η-winding n ≡ 1 mod 3 (χ₋-dominant), while u-quark has
n ≡ 2 mod 3 (complement class). δ_A ≈ 1.293 MeV.

- d_winding_mod3 : ℕ
d-quark winding class mod 3.

- u_winding_mod3 : ℕ
u-quark winding class mod 3.

- delta_A_keV : ℕ
Mass splitting (keV).

- d_heavier : Bool
d heavier than u.

Instances For

---

### `Tau.BookIV.Particles.instReprIsospinSplitting.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L201-L201)
**def
Tau.BookIV.Particles.instReprIsospinSplitting.repr :IsospinSplitting → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprIsospinSplitting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L201-L201)
**instance
Tau.BookIV.Particles.instReprIsospinSplitting :Repr IsospinSplitting**

Equations
- Tau.BookIV.Particles.instReprIsospinSplitting = { reprPrec := Tau.BookIV.Particles.instReprIsospinSplitting.repr }

---

### `Tau.BookIV.Particles.isospin_splitting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L203-L203)
**def
Tau.BookIV.Particles.isospin_splitting :IsospinSplitting**

Equations
- Tau.BookIV.Particles.isospin_splitting = { }
Instances For

---

### `Tau.BookIV.Particles.NuclearForce`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L209-L220)
**structure
Tau.BookIV.Particles.NuclearForce :Type**


[IV.D202] The nuclear force is the residual C-sector interaction
from partial overlap of nucleon color fields at ~1 fm.
Mediated by virtual meson exchange, principally the pion
(range ≈ ℏ/m_π c ≈ 1.4 fm).

- range_fm_x10 : ℕ
Range (fm ×10).

- mediator : String
Mediator.

- mechanism : String
Mechanism.

Instances For

---

### `Tau.BookIV.Particles.instReprNuclearForce`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L220-L220)
**instance
Tau.BookIV.Particles.instReprNuclearForce :Repr NuclearForce**

Equations
- Tau.BookIV.Particles.instReprNuclearForce = { reprPrec := Tau.BookIV.Particles.instReprNuclearForce.repr }

---

### `Tau.BookIV.Particles.instReprNuclearForce.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L220-L220)
**def
Tau.BookIV.Particles.instReprNuclearForce.repr :NuclearForce → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.nuclear_force`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L222-L222)
**def
Tau.BookIV.Particles.nuclear_force :NuclearForce**

Equations
- Tau.BookIV.Particles.nuclear_force = { }
Instances For

---

### `Tau.BookIV.Particles.DeuteronBinding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L228-L238)
**structure
Tau.BookIV.Particles.DeuteronBinding :Type**


[IV.R133] The deuteron is the minimal two-nucleon winding
configuration on T². Binding energy B_d ≈ 2.224 MeV from
η-holonomy field overlap.

- nucleon_count : ℕ
Number of nucleons.

- binding_keV : ℕ
Binding energy (keV).

- minimal : Bool
Minimal configuration.

Instances For

---

### `Tau.BookIV.Particles.instReprDeuteronBinding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L238-L238)
**instance
Tau.BookIV.Particles.instReprDeuteronBinding :Repr DeuteronBinding**

Equations
- Tau.BookIV.Particles.instReprDeuteronBinding = { reprPrec := Tau.BookIV.Particles.instReprDeuteronBinding.repr }

---

### `Tau.BookIV.Particles.instReprDeuteronBinding.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L238-L238)
**def
Tau.BookIV.Particles.instReprDeuteronBinding.repr :DeuteronBinding → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.deuteron_binding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L240-L240)
**def
Tau.BookIV.Particles.deuteron_binding :DeuteronBinding**

Equations
- Tau.BookIV.Particles.deuteron_binding = { }
Instances For

---

### `Tau.BookIV.Particles.NuclearSaturation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L246-L256)
**structure
Tau.BookIV.Particles.NuclearSaturation :Type**


[IV.P129] Each nucleon's defect bundle has finite angular extent
Δθ ≈ ι<sub>τ</sub> on the η-circle, so only ~12 nearest neighbors interact.
Binding energy per nucleon B/A plateaus near 8.8 MeV for large A.

- max_neighbors : ℕ
Max neighbors interacting.

- ba_plateau_mev_x10 : ℕ
B/A plateau (MeV ×10).

- angular_extent : Bool
Angular extent determines saturation.

Instances For

---

### `Tau.BookIV.Particles.instReprNuclearSaturation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L256-L256)
**def
Tau.BookIV.Particles.instReprNuclearSaturation.repr :NuclearSaturation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNuclearSaturation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L256-L256)
**instance
Tau.BookIV.Particles.instReprNuclearSaturation :Repr NuclearSaturation**

Equations
- Tau.BookIV.Particles.instReprNuclearSaturation = { reprPrec := Tau.BookIV.Particles.instReprNuclearSaturation.repr }

---

### `Tau.BookIV.Particles.nuclear_force_saturation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L258-L258)
**def
Tau.BookIV.Particles.nuclear_force_saturation :NuclearSaturation**

Equations
- Tau.BookIV.Particles.nuclear_force_saturation = { }
Instances For

---

### `Tau.BookIV.Particles.NuclearShellStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L264-L272)
**structure
Tau.BookIV.Particles.NuclearShellStructure :Type**


[IV.P130] T²-winding modes for nucleons organize into shells.
Cumulative counts at shell closures produce the magic numbers:
2, 8, 20, 28, 50, 82, 126.

- magic_numbers : List ℕ
Magic numbers.

- origin : String
Origin: T²-winding shell closures.

Instances For

---

### `Tau.BookIV.Particles.instReprNuclearShellStructure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L272-L272)
**def
Tau.BookIV.Particles.instReprNuclearShellStructure.repr :NuclearShellStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNuclearShellStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L272-L272)
**instance
Tau.BookIV.Particles.instReprNuclearShellStructure :Repr NuclearShellStructure**

Equations
- Tau.BookIV.Particles.instReprNuclearShellStructure = { reprPrec := Tau.BookIV.Particles.instReprNuclearShellStructure.repr }

---

### `Tau.BookIV.Particles.nuclear_shell_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L274-L274)
**def
Tau.BookIV.Particles.nuclear_shell_structure :NuclearShellStructure**

Equations
- Tau.BookIV.Particles.nuclear_shell_structure = { }
Instances For

---

### `Tau.BookIV.Particles.seven_magic_numbers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L276-L277)
**theorem
Tau.BookIV.Particles.seven_magic_numbers :nuclear_shell_structure.magic_numbers.length = 7**


---

### `Tau.BookIV.Particles.Helium4Bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L283-L297)
**structure
Tau.BookIV.Particles.Helium4Bound :Type**


[IV.R135] He-4 (Z=N=2) is the first doubly magic nucleus.
B/A ≈ 7.1 MeV, preferred alpha-decay product.
Completely fills lowest winding mode (0,0) with all four slots.

- z : ℕ
Atomic number Z.

- n : ℕ
Neutron number N.

- ba_mev_x10 : ℕ
Binding per nucleon (MeV ×10).

- doubly_magic : Bool
Doubly magic.

- slots_filled : ℕ
Number of nucleon slots filled.

Instances For

---

### `Tau.BookIV.Particles.instReprHelium4Bound.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L297-L297)
**def
Tau.BookIV.Particles.instReprHelium4Bound.repr :Helium4Bound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprHelium4Bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L297-L297)
**instance
Tau.BookIV.Particles.instReprHelium4Bound :Repr Helium4Bound**

Equations
- Tau.BookIV.Particles.instReprHelium4Bound = { reprPrec := Tau.BookIV.Particles.instReprHelium4Bound.repr }

---

### `Tau.BookIV.Particles.helium4_tightly_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L299-L299)
**def
Tau.BookIV.Particles.helium4_tightly_bound :Helium4Bound**

Equations
- Tau.BookIV.Particles.helium4_tightly_bound = { }
Instances For

---

### `Tau.BookIV.Particles.helium4_doubly_magic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L301-L302)
**theorem
Tau.BookIV.Particles.helium4_doubly_magic :helium4_tightly_bound.doubly_magic = true**


---

### `Tau.BookIV.Particles.IronPeak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L308-L323)
**structure
Tau.BookIV.Particles.IronPeak :Type**


[IV.P131] The binding energy maximum at A ≈ 56 (iron peak) results
from optimal balance between:


- C-sector (strong) binding per nucleon (saturating)

- B-sector (EM) repulsion per nucleon (growing as Z²/A^(1/3))


Crossover near iron-56 where Coulomb cost exceeds marginal binding.

- peak_A : ℕ
Peak mass number.

- binding_sector : BookIII.Sectors.Sector
Binding sector.

- repulsion_sector : BookIII.Sectors.Sector
Repulsion sector.

- ba_peak_mev_x100 : ℕ
B/A at peak (MeV ×100).

Instances For

---

### `Tau.BookIV.Particles.instReprIronPeak.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L323-L323)
**def
Tau.BookIV.Particles.instReprIronPeak.repr :IronPeak → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprIronPeak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L323-L323)
**instance
Tau.BookIV.Particles.instReprIronPeak :Repr IronPeak**

Equations
- Tau.BookIV.Particles.instReprIronPeak = { reprPrec := Tau.BookIV.Particles.instReprIronPeak.repr }

---

### `Tau.BookIV.Particles.iron_peak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L325-L325)
**def
Tau.BookIV.Particles.iron_peak :IronPeak**

Equations
- Tau.BookIV.Particles.iron_peak = { }
Instances For

---

### `Tau.BookIV.Particles.iron_at_56`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L327-L327)
**theorem
Tau.BookIV.Particles.iron_at_56 :iron_peak.peak_A = 56**


---

### `Tau.BookIV.Particles.nucleosynthesis_forward`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L333-L337)
**def
Tau.BookIV.Particles.nucleosynthesis_forward :String**


[IV.R136] Fusion releases energy below iron peak (A < 56),
fission above it (A > 56). Astrophysical consequences deferred
to Book V.
Equations
- Tau.BookIV.Particles.nucleosynthesis_forward = "Fusion (A<56) and fission (A>56) consequences deferred to Book V"
Instances For

---

### `Tau.BookIV.Particles.alpha_decay_mode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L343-L347)
**def
Tau.BookIV.Particles.alpha_decay_mode :String**


[IV.R137] Alpha-decay: ejection of a completely filled lowest-winding-mode
cluster (4 nucleons) from the parent nucleus, tunneling through the
Coulomb barrier.
Equations
- Tau.BookIV.Particles.alpha_decay_mode = "Alpha-decay: 4-nucleon cluster ejection, lowest winding mode, Coulomb tunneling"
Instances For

---

### `Tau.BookIV.Particles.NeutronStabilityNuclear`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L353-L363)
**structure
Tau.BookIV.Particles.NeutronStabilityNuclear :Type**


[IV.R138] Free neutrons decay in ~10 min, but bound neutrons are stable
because nuclear binding makes Q_β < 0 (energetically forbidden).
This is a readout-level phenomenon; the ontic neutron is unchanged.

- free_lifetime_min : ℕ
Free lifetime (minutes, approx).

- stable_in_nuclei : Bool
Stable in nuclei.

- mechanism : String
Mechanism: Q_β < 0.

Instances For

---

### `Tau.BookIV.Particles.instReprNeutronStabilityNuclear.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L363-L363)
**def
Tau.BookIV.Particles.instReprNeutronStabilityNuclear.repr :NeutronStabilityNuclear → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNeutronStabilityNuclear`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L363-L363)
**instance
Tau.BookIV.Particles.instReprNeutronStabilityNuclear :Repr NeutronStabilityNuclear**

Equations
- Tau.BookIV.Particles.instReprNeutronStabilityNuclear = { reprPrec := Tau.BookIV.Particles.instReprNeutronStabilityNuclear.repr }

---

### `Tau.BookIV.Particles.neutron_stability_nuclear`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L365-L365)
**def
Tau.BookIV.Particles.neutron_stability_nuclear :NeutronStabilityNuclear**

Equations
- Tau.BookIV.Particles.neutron_stability_nuclear = { }
Instances For

---

### `Tau.BookIV.Particles.gamma_decay_mode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L371-L375)
**def
Tau.BookIV.Particles.gamma_decay_mode :String**


[IV.R139] Gamma-decay is the same mechanism as atomic spectral lines:
a T²-winding mode transition with energy carried by a B-sector photon.
Only difference: scale (MeV nuclear vs eV atomic).
Equations
- Tau.BookIV.Particles.gamma_decay_mode = "Gamma-decay: T^2 mode transition at MeV scale (same mechanism as atomic lines)"
Instances For

---

### `Tau.BookIV.Particles.DecayChannels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L381-L395)
**structure
Tau.BookIV.Particles.DecayChannels :Type**


[IV.P132] Every radioactive decay satisfies sector admissibility:


- Color neutrality (η-holonomy trivial mod 3)

- Baryon number conserved

- Electric charge conserved (γ-holonomy)

- Energy-momentum conserved


Each decay type corresponds to a specific sector-transition pattern.

- conservation_laws : ℕ
Number of conservation laws.

- types : List String
Decay types.

- all_admissible : Bool
All satisfy sector admissibility.

Instances For

---

### `Tau.BookIV.Particles.instReprDecayChannels.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L395-L395)
**def
Tau.BookIV.Particles.instReprDecayChannels.repr :DecayChannels → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprDecayChannels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L395-L395)
**instance
Tau.BookIV.Particles.instReprDecayChannels :Repr DecayChannels**

Equations
- Tau.BookIV.Particles.instReprDecayChannels = { reprPrec := Tau.BookIV.Particles.instReprDecayChannels.repr }

---

### `Tau.BookIV.Particles.decay_channels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L397-L397)
**def
Tau.BookIV.Particles.decay_channels :DecayChannels**

Equations
- Tau.BookIV.Particles.decay_channels = { }
Instances For

---

### `Tau.BookIV.Particles.three_decay_types`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L399-L399)
**theorem
Tau.BookIV.Particles.three_decay_types :decay_channels.types.length = 3**


---

### `Tau.BookIV.Particles.four_conservation_laws`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/HadronsNuclei.lean#L400-L400)
**theorem
Tau.BookIV.Particles.four_conservation_laws :decay_channels.conservation_laws = 4**
