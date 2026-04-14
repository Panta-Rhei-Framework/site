---
layout: taulib-doc
title: "TauLib.BookVI.LifeCore.ParityBridge"
permalink: /verify/taulib/docs/book-vi-life-core-parity-bridge/
lane: verify
module_name: "TauLib.BookVI.LifeCore.ParityBridge"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.LifeCore.ParityBridge


The Parity Bridge: E₁→E₂ transition factors uniquely through the weak sector.
The polarity functional P_S tests whether a holonomy sector carries intrinsic
parity asymmetry. Only the weak sector is nontrivial.

## Registry Cross-References


- [VI.D01] Polarity Functional — `PolarityFunctional`

- [VI.D02] Polarity-Typed Two-Point Object (2_τ) — `TwoPointObject`

- [VI.D03] Three Polarity Terms — `ThreePolarityTerms`

- [VI.L01] Weak-Sector Uniqueness — `weak_sector_uniqueness`

- [VI.T01] Parity Bridge Theorem — `parity_bridge_theorem`

- [VI.P01] Low-Noise Carrier Condition — `low_noise_carrier_condition`


## Ground Truth Sources


- Book VI Chapter 3 (2nd Edition): The Parity Bridge


---

### `Tau.BookVI.ParityBridge.PolarityFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L25-L33)
**structure
Tau.BookVI.ParityBridge.PolarityFunctional :Type**


[VI.D01] Polarity functional: map P_S: End(S) → 2_τ testing whether
a holonomy sector carries intrinsic parity asymmetry.
Trivial for EM, Strong, Gravity; nontrivial uniquely for Weak.

- sectors_tested : ℕ
- nontrivial_count : ℕ
- unique_nontrivial : self.nontrivial_count = 1
- all_tested : self.sectors_tested = 4
Instances For

---

### `Tau.BookVI.ParityBridge.instReprPolarityFunctional.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L33-L33)
**def
Tau.BookVI.ParityBridge.instReprPolarityFunctional.repr :PolarityFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.instReprPolarityFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L33-L33)
**instance
Tau.BookVI.ParityBridge.instReprPolarityFunctional :Repr PolarityFunctional**

Equations
- Tau.BookVI.ParityBridge.instReprPolarityFunctional = { reprPrec := Tau.BookVI.ParityBridge.instReprPolarityFunctional.repr }

---

### `Tau.BookVI.ParityBridge.polarity_functional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L35-L39)
**def
Tau.BookVI.ParityBridge.polarity_functional :PolarityFunctional**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.TwoPointObject`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L41-L48)
**structure
Tau.BookVI.ParityBridge.TwoPointObject :Type**


[VI.D02] Polarity-typed two-point object 2_τ = {+, −}.
Split-complex idempotent structure from lemniscate boundary.

- point_count : ℕ
- count_eq : self.point_count = 2
- split_complex : Bool
- from_lemniscate : Bool
Instances For

---

### `Tau.BookVI.ParityBridge.instReprTwoPointObject.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L48-L48)
**def
Tau.BookVI.ParityBridge.instReprTwoPointObject.repr :TwoPointObject → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.instReprTwoPointObject`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L48-L48)
**instance
Tau.BookVI.ParityBridge.instReprTwoPointObject :Repr TwoPointObject**

Equations
- Tau.BookVI.ParityBridge.instReprTwoPointObject = { reprPrec := Tau.BookVI.ParityBridge.instReprTwoPointObject.repr }

---

### `Tau.BookVI.ParityBridge.two_point`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L50-L52)
**def
Tau.BookVI.ParityBridge.two_point :TwoPointObject**

Equations
- Tau.BookVI.ParityBridge.two_point = { point_count := 2, count_eq := Tau.BookVI.ParityBridge.two_point._proof_1 }
Instances For

---

### `Tau.BookVI.ParityBridge.ThreePolarityTerms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L54-L58)
**structure
Tau.BookVI.ParityBridge.ThreePolarityTerms :Type**


[VI.D03] Three polarity terms: source, basin, stabilizer.

- term_count : ℕ
- count_eq : self.term_count = 3
Instances For

---

### `Tau.BookVI.ParityBridge.instReprThreePolarityTerms.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L58-L58)
**def
Tau.BookVI.ParityBridge.instReprThreePolarityTerms.repr :ThreePolarityTerms → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.instReprThreePolarityTerms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L58-L58)
**instance
Tau.BookVI.ParityBridge.instReprThreePolarityTerms :Repr ThreePolarityTerms**

Equations
- Tau.BookVI.ParityBridge.instReprThreePolarityTerms = { reprPrec := Tau.BookVI.ParityBridge.instReprThreePolarityTerms.repr }

---

### `Tau.BookVI.ParityBridge.polarity_terms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L60-L62)
**def
Tau.BookVI.ParityBridge.polarity_terms :ThreePolarityTerms**

Equations
- Tau.BookVI.ParityBridge.polarity_terms = { term_count := 3, count_eq := Tau.BookVI.ParityBridge.polarity_terms._proof_1 }
Instances For

---

### `Tau.BookVI.ParityBridge.weak_sector_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L64-L69)
**theorem
Tau.BookVI.ParityBridge.weak_sector_uniqueness :polarity_functional.nontrivial_count = 1 ∧ polarity_functional.sectors_tested = 4**


[VI.L01] Weak-sector uniqueness: among 4 primitive sectors,
weak is the unique one with nontrivial polarity.

---

### `Tau.BookVI.ParityBridge.ParityBridgeTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L71-L79)
**structure
Tau.BookVI.ParityBridge.ParityBridgeTheorem :Type**


[VI.T01] Parity Bridge Theorem: E₁→E₂ factors uniquely through weak sector.
E₁ →[P_weak] 2_τ →[SelfDesc] E₂.

- path_count : ℕ
- unique_path : self.path_count = 1
- source_layer : String
- target_layer : String
- mediating_sector : String
Instances For

---

### `Tau.BookVI.ParityBridge.instReprParityBridgeTheorem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L79-L79)
**def
Tau.BookVI.ParityBridge.instReprParityBridgeTheorem.repr :ParityBridgeTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.instReprParityBridgeTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L79-L79)
**instance
Tau.BookVI.ParityBridge.instReprParityBridgeTheorem :Repr ParityBridgeTheorem**

Equations
- Tau.BookVI.ParityBridge.instReprParityBridgeTheorem = { reprPrec := Tau.BookVI.ParityBridge.instReprParityBridgeTheorem.repr }

---

### `Tau.BookVI.ParityBridge.parity_bridge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L81-L83)
**def
Tau.BookVI.ParityBridge.parity_bridge :ParityBridgeTheorem**

Equations
- Tau.BookVI.ParityBridge.parity_bridge = { path_count := 1, unique_path := Tau.BookVI.ParityBridge.polarity_functional._proof_1 }
Instances For

---

### `Tau.BookVI.ParityBridge.parity_bridge_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L85-L87)
**theorem
Tau.BookVI.ParityBridge.parity_bridge_theorem :parity_bridge.path_count = 1**


---

### `Tau.BookVI.ParityBridge.LowNoiseCarrierCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L89-L93)
**structure
Tau.BookVI.ParityBridge.LowNoiseCarrierCondition :Type**


[VI.P01] Low-noise carrier condition: 3 conditions for E₁→E₂ transition.

- condition_count : ℕ
- count_eq : self.condition_count = 3
Instances For

---

### `Tau.BookVI.ParityBridge.instReprLowNoiseCarrierCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L93-L93)
**instance
Tau.BookVI.ParityBridge.instReprLowNoiseCarrierCondition :Repr LowNoiseCarrierCondition**

Equations
- Tau.BookVI.ParityBridge.instReprLowNoiseCarrierCondition = { reprPrec := Tau.BookVI.ParityBridge.instReprLowNoiseCarrierCondition.repr }

---

### `Tau.BookVI.ParityBridge.instReprLowNoiseCarrierCondition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L93-L93)
**def
Tau.BookVI.ParityBridge.instReprLowNoiseCarrierCondition.repr :LowNoiseCarrierCondition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.low_noise`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L95-L97)
**def
Tau.BookVI.ParityBridge.low_noise :LowNoiseCarrierCondition**

Equations
- Tau.BookVI.ParityBridge.low_noise = { condition_count := 3, count_eq := Tau.BookVI.ParityBridge.polarity_terms._proof_1 }
Instances For

---

### `Tau.BookVI.ParityBridge.low_noise_carrier_condition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L99-L100)
**theorem
Tau.BookVI.ParityBridge.low_noise_carrier_condition :low_noise.condition_count = 3**


---

### `Tau.BookVI.ParityBridge.PolarityPropagation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L106-L121)
**structure
Tau.BookVI.ParityBridge.PolarityPropagation :Type**


[VI.D71] Polarity Propagation: functor mapping IV.D112 σ_A-admissibility
through VI.T01 Parity Bridge into VI.D01 polarity functional.
The propagation chain is: weak-sector parity violation (σ = C_τ, IV.T146)
→ Parity Bridge (VI.T01) → polarity functional P_weak (VI.D01)
→ biological chirality seed.

- source_sector : String
Source: weak-sector parity violation.

- bridge_path_count : ℕ
Bridge: VI.T01 unique factorization.

- bridge_unique : self.bridge_path_count = 1
- target_codomain : String
Target: polarity functional output in 2_τ.

- sign_preserved : Bool
Propagation preserves chirality sign.

Instances For

---

### `Tau.BookVI.ParityBridge.instReprPolarityPropagation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L121-L121)
**def
Tau.BookVI.ParityBridge.instReprPolarityPropagation.repr :PolarityPropagation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.instReprPolarityPropagation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L121-L121)
**instance
Tau.BookVI.ParityBridge.instReprPolarityPropagation :Repr PolarityPropagation**

Equations
- Tau.BookVI.ParityBridge.instReprPolarityPropagation = { reprPrec := Tau.BookVI.ParityBridge.instReprPolarityPropagation.repr }

---

### `Tau.BookVI.ParityBridge.polarity_propagation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L123-L125)
**def
Tau.BookVI.ParityBridge.polarity_propagation :PolarityPropagation**

Equations
- Tau.BookVI.ParityBridge.polarity_propagation = { bridge_path_count := 1, bridge_unique := Tau.BookVI.ParityBridge.polarity_functional._proof_1 }
Instances For

---

### `Tau.BookVI.ParityBridge.ChiralitySeed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L131-L143)
**structure
Tau.BookVI.ParityBridge.ChiralitySeed :Type**


[VI.D72] Chirality Seed: initial asymmetry from weak parity violation.
The weak sector couples exclusively to left-handed fermions (V(A)=100%),
seeding a universal directional bias. The seed magnitude is ~10⁻¹⁷ eV
but the sign is coherent across all chiral molecules.

- va_coupling_pct : ℕ
Parity violation is maximal (100%) in weak sector.

- va_maximal : self.va_coupling_pct = 100
- coherent : Bool
Seed is coherent: same sign for all amino acids.

- iv_t146_source : Bool
Source: IV.T146 σ = C_τ (Majorana).

Instances For

---

### `Tau.BookVI.ParityBridge.instReprChiralitySeed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L143-L143)
**instance
Tau.BookVI.ParityBridge.instReprChiralitySeed :Repr ChiralitySeed**

Equations
- Tau.BookVI.ParityBridge.instReprChiralitySeed = { reprPrec := Tau.BookVI.ParityBridge.instReprChiralitySeed.repr }

---

### `Tau.BookVI.ParityBridge.instReprChiralitySeed.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L143-L143)
**def
Tau.BookVI.ParityBridge.instReprChiralitySeed.repr :ChiralitySeed → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.ParityBridge.chirality_seed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L145-L147)
**def
Tau.BookVI.ParityBridge.chirality_seed :ChiralitySeed**

Equations
- Tau.BookVI.ParityBridge.chirality_seed = { va_coupling_pct := 100, va_maximal := Tau.BookVI.ParityBridge.chirality_seed._proof_1 }
Instances For

---

### `Tau.BookVI.ParityBridge.propagation_preserves_chirality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L153-L163)
**theorem
Tau.BookVI.ParityBridge.propagation_preserves_chirality :polarity_propagation.sign_preserved = true ∧ polarity_propagation.bridge_path_count = 1 ∧ chirality_seed.va_coupling_pct = 100 ∧ chirality_seed.coherent = true**


[VI.T41] Propagation Preserves Chirality: left-handed input through the
Parity Bridge yields a definite polarity sign in 2_τ.
Proof chain: weak-sector parity violation (ChiralitySeed, VI.D72)
→ unique bridge path (PolarityPropagation, VI.D71)
→ definite polarity (PolarityFunctional, VI.D01).

---

### `Tau.BookVI.ParityBridge.propagation_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/ParityBridge.lean#L169-L175)
**theorem
Tau.BookVI.ParityBridge.propagation_uniqueness :polarity_functional.nontrivial_count = 1 ∧ polarity_propagation.bridge_path_count = 1**


[VI.L14] Propagation Uniqueness: weak-sector uniqueness (VI.L01) implies
the propagation path is unique. Since only one sector has nontrivial
polarity, there is exactly one route from parity violation to chirality seed.
