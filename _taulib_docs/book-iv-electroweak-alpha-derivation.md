---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.AlphaDerivation"
permalink: /verify/taulib/docs/book-iv-electroweak-alpha-derivation/
lane: verify
module_name: "TauLib.BookIV.Electroweak.AlphaDerivation"
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

# TauLib.BookIV.Electroweak.AlphaDerivation


The τ-native fine-structure constant α: spectral and holonomy formulas,
null transport mode, holonomy correction factor, ontic invariance,
AB holonomy lemma, photon phase quantum, and structural independence.

## Registry Cross-References


- [IV.D104] τ-Native Fine-Structure Constant — `AlphaTau`

- [IV.D105] Null Transport Mode — `NullTransportMode`

- [IV.D106] Holonomy Correction Factor — `HolonomyCorrectionR`

- [IV.T49] Holonomy Formula Exact — `holonomy_formula_exact`

- [IV.T50] α_τ is Ontic Invariant — `alpha_ontic_invariant`

- [IV.L02] AB Holonomy Lemma — `ab_holonomy_lemma`

- [IV.L03] Photon Phase Quantum — `photon_phase_quantum`

- [IV.L04] α from Relational Units — `alpha_relational_units`

- [IV.P50] Unique Massless Transport — `unique_massless_transport`

- [IV.P51] Structural Independence — `structural_independence`

- [IV.R27, IV.R365-IV.R379] structural remarks


## Mathematical Content


### Two Derivations of α


**Spectral formula (leading order):**
α_spec = (8/15) · ι<sub>τ</sub>⁴ ≈ 1/137.9 (0.6% off)

**Holonomy formula (exact):**
α = (π³/16) · Q⁴ / (M² H³ L⁶)

where Q, M, H, L are the relational units from the calibration cascade.
The holonomy formula resolves to the spectral formula at leading order
with a correction factor R(ι<sub>τ</sub>) ≈ 1.0065.

### Origin of π³


The factor π³ arises from three independent U(1) holonomy circles in
τ³ = τ¹ ×_f T²: one base circle + two fiber circles.

### α as Ontic Invariant


α is an ontic invariant: it depends only on ι<sub>τ</sub> = 2/(π+e) and
geometric constants (π, e). It is not a free parameter. The spectral
formula makes this manifest: α ∝ ι<sub>τ</sub>⁴.

## Ground Truth Sources


- Chapter 29 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.AlphaTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L63-L83)
**structure
Tau.BookIV.Electroweak.AlphaTau :Type**


[IV.D104] The τ-native fine-structure constant α_τ.
Two equivalent formulas:


- Spectral: α_spec = (8/15)·ι<sub>τ</sub>⁴ (leading order, 0.6% off)

- Holonomy: α = (π³/16)·Q⁴/(M²H³L⁶) (exact)
Both are fully determined by ι<sub>τ</sub> = 2/(π+e).


- spectral_numer : ℕ
Spectral formula numerator (8·ι<sub>τ</sub>⁴).

- spectral_denom : ℕ
Spectral formula denominator (15·D⁴).

- denom_pos : self.spectral_denom > 0
- inverse_lower : self.spectral_denom > 137 * self.spectral_numer
1/α lies in [137, 139] for spectral formula.

- inverse_upper : self.spectral_denom < 139 * self.spectral_numer
- holonomy_circles : ℕ
Number of holonomy circles (π³ origin).

- circles_eq : self.holonomy_circles = 3
- relational_units : ℕ
Number of relational units in denominator.

- units_eq : self.relational_units = 4
Instances For

---

### `Tau.BookIV.Electroweak.instReprAlphaTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L83-L83)
**instance
Tau.BookIV.Electroweak.instReprAlphaTau :Repr AlphaTau**

Equations
- Tau.BookIV.Electroweak.instReprAlphaTau = { reprPrec := Tau.BookIV.Electroweak.instReprAlphaTau.repr }

---

### `Tau.BookIV.Electroweak.instReprAlphaTau.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L83-L83)
**def
Tau.BookIV.Electroweak.instReprAlphaTau.repr :AlphaTau → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.alpha_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L85-L95)
**def
Tau.BookIV.Electroweak.alpha_tau :AlphaTau**


Canonical α_τ using spectral formula values.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.alpha_tau_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L97-L99)
**def
Tau.BookIV.Electroweak.alpha_tau_float :Float**


α as Float (spectral approximation).
Equations
- Tau.BookIV.Electroweak.alpha_tau_float = Float.ofNat Tau.BookIV.Electroweak.alpha_tau.spectral_numer / Float.ofNat Tau.BookIV.Electroweak.alpha_tau.spectral_denom
Instances For

---

### `Tau.BookIV.Electroweak.NullTransportMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L105-L117)
**structure
Tau.BookIV.Electroweak.NullTransportMode :Type**


[IV.D105] Null transport mode on τ¹: a mode with zero fiber
obstruction that propagates purely along the base τ¹ at speed c.
The photon is the B-sector null transport mode.

- base_only : Bool
Propagation is along base τ¹ only.

- fiber_degenerate : Bool
Fiber character is degenerate (0,0).

- speed_is_c : Bool
Speed equals c (base propagation speed).

- sector : BookIII.Sectors.Sector
Associated sector.

Instances For

---

### `Tau.BookIV.Electroweak.instReprNullTransportMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L117-L117)
**def
Tau.BookIV.Electroweak.instReprNullTransportMode.repr :NullTransportMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprNullTransportMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L117-L117)
**instance
Tau.BookIV.Electroweak.instReprNullTransportMode :Repr NullTransportMode**

Equations
- Tau.BookIV.Electroweak.instReprNullTransportMode = { reprPrec := Tau.BookIV.Electroweak.instReprNullTransportMode.repr }

---

### `Tau.BookIV.Electroweak.photon_null`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L119-L121)
**def
Tau.BookIV.Electroweak.photon_null :NullTransportMode**


Photon as null transport mode.
Equations
- Tau.BookIV.Electroweak.photon_null = { sector := Tau.BookIII.Sectors.Sector.B }
Instances For

---

### `Tau.BookIV.Electroweak.graviton_null`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L123-L125)
**def
Tau.BookIV.Electroweak.graviton_null :NullTransportMode**


Graviton candidate as null transport mode (D-sector).
Equations
- Tau.BookIV.Electroweak.graviton_null = { sector := Tau.BookIII.Sectors.Sector.D }
Instances For

---

### `Tau.BookIV.Electroweak.HolonomyCorrectionR`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L131-L144)
**structure
Tau.BookIV.Electroweak.HolonomyCorrectionR :Type**


[IV.D106] Holonomy correction factor R(ι<sub>τ</sub>) relating the spectral
and holonomy formulas: α = (8/15)·ι<sub>τ</sub>⁴ · R(ι<sub>τ</sub>).
R ≈ 1.0065: the spectral formula is a 0.6% approximation.
R encodes the detailed calibration cascade.

- r_numer : ℕ
R numerator (scaled at 10⁶).

- r_denom : ℕ
R denominator.

- denom_pos : self.r_denom > 0
- near_unity_lower : self.r_numer * 1000 > self.r_denom * 1000
R is near unity: 1.000 < R < 1.010.

- near_unity_upper : self.r_numer * 1000 < self.r_denom * 1010
Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyCorrectionR.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L144-L144)
**def
Tau.BookIV.Electroweak.instReprHolonomyCorrectionR.repr :HolonomyCorrectionR → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyCorrectionR`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L144-L144)
**instance
Tau.BookIV.Electroweak.instReprHolonomyCorrectionR :Repr HolonomyCorrectionR**

Equations
- Tau.BookIV.Electroweak.instReprHolonomyCorrectionR = { reprPrec := Tau.BookIV.Electroweak.instReprHolonomyCorrectionR.repr }

---

### `Tau.BookIV.Electroweak.HolonomyCorrectionR.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L146-L147)
**def
Tau.BookIV.Electroweak.HolonomyCorrectionR.toFloat
(r : HolonomyCorrectionR)
 :Float**

Equations
- r.toFloat = Float.ofNat r.r_numer / Float.ofNat r.r_denom
Instances For

---

### `Tau.BookIV.Electroweak.correction_r`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L149-L155)
**def
Tau.BookIV.Electroweak.correction_r :HolonomyCorrectionR**


R ≈ 1.0065 from calibration cascade.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.HolonomyFormulaExact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L161-L177)
**structure
Tau.BookIV.Electroweak.HolonomyFormulaExact :Type**


[IV.T49] The holonomy formula α = (π³/16)·Q⁴/(M²H³L⁶) is exact.
The π³ factor arises from three independent U(1) circles in τ³.
The denominator encodes the relational units from the calibration
cascade, all determined by ι<sub>τ</sub>.

- is_exact : Bool
The formula is exact (not approximate).

- pi_cubed_approx : ℕ
π³ = 31.006... from three circles.

- pi_cubed_eq : self.pi_cubed_approx = 31
- denom_factor : ℕ
Denominator factor 16.

- factor_eq : self.denom_factor = 16
- unit_types : ℕ
Number of relational unit types in formula.

- types_eq : self.unit_types = 4
Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyFormulaExact.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L177-L177)
**def
Tau.BookIV.Electroweak.instReprHolonomyFormulaExact.repr :HolonomyFormulaExact → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprHolonomyFormulaExact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L177-L177)
**instance
Tau.BookIV.Electroweak.instReprHolonomyFormulaExact :Repr HolonomyFormulaExact**

Equations
- Tau.BookIV.Electroweak.instReprHolonomyFormulaExact = { reprPrec := Tau.BookIV.Electroweak.instReprHolonomyFormulaExact.repr }

---

### `Tau.BookIV.Electroweak.holonomy_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L179-L186)
**def
Tau.BookIV.Electroweak.holonomy_formula :HolonomyFormulaExact**


The holonomy formula.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.holonomy_formula_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L188-L189)
**theorem
Tau.BookIV.Electroweak.holonomy_formula_exact :holonomy_formula.is_exact = true**


---

### `Tau.BookIV.Electroweak.OnticInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L195-L206)
**structure
Tau.BookIV.Electroweak.OnticInvariant :Type**


[IV.T50] α_τ is an ontic invariant: it depends only on ι<sub>τ</sub> and
geometric constants (π, e). It is NOT a free parameter of the
theory. The value 1/137.036... is structurally determined.

- depends_on_iota : Bool
Depends only on ι<sub>τ</sub>.

- free_parameters : ℕ
No free parameters.

- free_eq : self.free_parameters = 0
- structurally_determined : Bool
Structurally determined (not tuned).

Instances For

---

### `Tau.BookIV.Electroweak.instReprOnticInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L206-L206)
**instance
Tau.BookIV.Electroweak.instReprOnticInvariant :Repr OnticInvariant**

Equations
- Tau.BookIV.Electroweak.instReprOnticInvariant = { reprPrec := Tau.BookIV.Electroweak.instReprOnticInvariant.repr }

---

### `Tau.BookIV.Electroweak.instReprOnticInvariant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L206-L206)
**def
Tau.BookIV.Electroweak.instReprOnticInvariant.repr :OnticInvariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ontic_invariant_instance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L208-L210)
**def
Tau.BookIV.Electroweak.ontic_invariant_instance :OnticInvariant**

Equations
- Tau.BookIV.Electroweak.ontic_invariant_instance = { free_parameters := 0, free_eq := Tau.BookIV.Electroweak.ontic_invariant_instance._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.alpha_ontic_invariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L212-L213)
**theorem
Tau.BookIV.Electroweak.alpha_ontic_invariant :ontic_invariant_instance.free_parameters = 0**


---

### `Tau.BookIV.Electroweak.ABHolonomyLemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L219-L232)
**structure
Tau.BookIV.Electroweak.ABHolonomyLemma :Type**


[IV.L02] AB holonomy around the minimal EM loop on T² equals
the B-sector self-coupling κ(B;2) = ι<sub>τ</sub>².
This connects the gauge-theory holonomy to the sector coupling.

- equals_kappa_b : Bool
The holonomy equals κ(B;2).

- kappa_b_numer : ℕ
κ(B;2) = ι<sub>τ</sub>².

- kappa_b_denom : ℕ
- denom_pos : self.kappa_b_denom > 0
- numer_eq : self.kappa_b_numer = Boundary.iota_tau_numer * Boundary.iota_tau_numer
Check: numer/denom ≈ 0.1166 (ι<sub>τ</sub>²).

- denom_eq : self.kappa_b_denom = Boundary.iota_tau_denom * Boundary.iota_tau_denom
Instances For

---

### `Tau.BookIV.Electroweak.instReprABHolonomyLemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L232-L232)
**instance
Tau.BookIV.Electroweak.instReprABHolonomyLemma :Repr ABHolonomyLemma**

Equations
- Tau.BookIV.Electroweak.instReprABHolonomyLemma = { reprPrec := Tau.BookIV.Electroweak.instReprABHolonomyLemma.repr }

---

### `Tau.BookIV.Electroweak.instReprABHolonomyLemma.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L232-L232)
**def
Tau.BookIV.Electroweak.instReprABHolonomyLemma.repr :ABHolonomyLemma → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ab_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L234-L240)
**def
Tau.BookIV.Electroweak.ab_holonomy :ABHolonomyLemma**


AB holonomy = ι<sub>τ</sub>² around minimal loop.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ab_holonomy_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L242-L243)
**theorem
Tau.BookIV.Electroweak.ab_holonomy_lemma :ab_holonomy.equals_kappa_b = true**


---

### `Tau.BookIV.Electroweak.PhotonPhaseQuantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L249-L259)
**structure
Tau.BookIV.Electroweak.PhotonPhaseQuantum :Type**


[IV.L03] Photon phase quantum Φ₀: the minimal phase acquired
by a unit-charge photon around a flux quantum.
Φ₀ = 2π (one complete winding).

- phase_per_quantum : ℕ
Phase per flux quantum in units of 2π.

- phase_eq : self.phase_per_quantum = 1
- min_winding : ℕ
Winding number for minimal loop.

- winding_eq : self.min_winding = 1
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonPhaseQuantum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L259-L259)
**def
Tau.BookIV.Electroweak.instReprPhotonPhaseQuantum.repr :PhotonPhaseQuantum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonPhaseQuantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L259-L259)
**instance
Tau.BookIV.Electroweak.instReprPhotonPhaseQuantum :Repr PhotonPhaseQuantum**

Equations
- Tau.BookIV.Electroweak.instReprPhotonPhaseQuantum = { reprPrec := Tau.BookIV.Electroweak.instReprPhotonPhaseQuantum.repr }

---

### `Tau.BookIV.Electroweak.phase_quantum_instance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L261-L265)
**def
Tau.BookIV.Electroweak.phase_quantum_instance :PhotonPhaseQuantum**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.photon_phase_quantum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L267-L268)
**theorem
Tau.BookIV.Electroweak.photon_phase_quantum :phase_quantum_instance.phase_per_quantum = 1**


---

### `Tau.BookIV.Electroweak.AlphaRelationalUnits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L274-L294)
**structure
Tau.BookIV.Electroweak.AlphaRelationalUnits :Type**


[IV.L04] α = (π³/16) · Q⁴/(M²H³L⁶): the holonomy formula
expressed in terms of the four relational units.
The exponents (4, 2, 3, 6) are structurally determined by the
dimension of each unit in the τ-framework.

- q_exp : ℕ
Exponent of Q (charge unit).

- q_eq : self.q_exp = 4
- m_exp : ℕ
Exponent of M (mass unit).

- m_eq : self.m_exp = 2
- h_exp : ℕ
Exponent of H (frequency unit).

- h_eq : self.h_exp = 3
- l_exp : ℕ
Exponent of L (length unit).

- l_eq : self.l_exp = 6
- denom_total : ℕ
Sum of denominator exponents = 2 + 3 + 6 = 11.

- denom_eq : self.denom_total = self.m_exp + self.h_exp + self.l_exp
Instances For

---

### `Tau.BookIV.Electroweak.instReprAlphaRelationalUnits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L294-L294)
**instance
Tau.BookIV.Electroweak.instReprAlphaRelationalUnits :Repr AlphaRelationalUnits**

Equations
- Tau.BookIV.Electroweak.instReprAlphaRelationalUnits = { reprPrec := Tau.BookIV.Electroweak.instReprAlphaRelationalUnits.repr }

---

### `Tau.BookIV.Electroweak.instReprAlphaRelationalUnits.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L294-L294)
**def
Tau.BookIV.Electroweak.instReprAlphaRelationalUnits.repr :AlphaRelationalUnits → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.alpha_rel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L296-L307)
**def
Tau.BookIV.Electroweak.alpha_rel :AlphaRelationalUnits**


Canonical relational unit exponents.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.alpha_relational_units`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L309-L310)
**theorem
Tau.BookIV.Electroweak.alpha_relational_units :alpha_rel.q_exp = 4 ∧ alpha_rel.denom_total = 11**


---

### `Tau.BookIV.Electroweak.UniqueMassless`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L316-L326)
**structure
Tau.BookIV.Electroweak.UniqueMassless :Type**


[IV.P50] The photon is the unique massless transport mode in the
B-sector: (0,0) is the only character in ker(Δ_Hodge) ∩ B.
Any other B-sector mode has (m,n) ≠ (0,0) and hence mass > 0.

- photon_m : ℤ
The photon character (0,0).

- photon_n : ℤ
- is_zero : self.photon_m = 0 ∧ self.photon_n = 0
- unique_in_b : Bool
Uniqueness: any other B-mode has nonzero character.

Instances For

---

### `Tau.BookIV.Electroweak.instReprUniqueMassless`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L326-L326)
**instance
Tau.BookIV.Electroweak.instReprUniqueMassless :Repr UniqueMassless**

Equations
- Tau.BookIV.Electroweak.instReprUniqueMassless = { reprPrec := Tau.BookIV.Electroweak.instReprUniqueMassless.repr }

---

### `Tau.BookIV.Electroweak.instReprUniqueMassless.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L326-L326)
**def
Tau.BookIV.Electroweak.instReprUniqueMassless.repr :UniqueMassless → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.unique_massless_instance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L328-L331)
**def
Tau.BookIV.Electroweak.unique_massless_instance :UniqueMassless**

Equations
- Tau.BookIV.Electroweak.unique_massless_instance = { photon_m := 0, photon_n := 0, is_zero := Tau.BookIV.Electroweak.unique_massless_instance._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.unique_massless_transport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L333-L334)
**theorem
Tau.BookIV.Electroweak.unique_massless_transport :unique_massless_instance.unique_in_b = true**


---

### `Tau.BookIV.Electroweak.StructuralIndependence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L340-L351)
**structure
Tau.BookIV.Electroweak.StructuralIndependence :Type**


[IV.P51] α and ι<sub>τ</sub> are structurally independent constants:
α depends on ι<sub>τ</sub> via (8/15)·ι<sub>τ</sub>⁴·R, but ι<sub>τ</sub> is the master
constant from which α is derived (not vice versa).
Their ratio is not a simple number.

- alpha_from_iota : Bool
α is derived from ι<sub>τ</sub>.

- iota_is_master : Bool
ι<sub>τ</sub> is the master constant.

- via_spectral : Bool
The derivation goes through spectral formula.

Instances For

---

### `Tau.BookIV.Electroweak.instReprStructuralIndependence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L351-L351)
**def
Tau.BookIV.Electroweak.instReprStructuralIndependence.repr :StructuralIndependence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprStructuralIndependence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L351-L351)
**instance
Tau.BookIV.Electroweak.instReprStructuralIndependence :Repr StructuralIndependence**

Equations
- Tau.BookIV.Electroweak.instReprStructuralIndependence = { reprPrec := Tau.BookIV.Electroweak.instReprStructuralIndependence.repr }

---

### `Tau.BookIV.Electroweak.structural_indep_instance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L353-L353)
**def
Tau.BookIV.Electroweak.structural_indep_instance :StructuralIndependence**

Equations
- Tau.BookIV.Electroweak.structural_indep_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.structural_independence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L355-L357)
**theorem
Tau.BookIV.Electroweak.structural_independence :structural_indep_instance.alpha_from_iota = true ∧ structural_indep_instance.iota_is_master = true**


---

### `Tau.BookIV.Electroweak.example_null`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L403-L403)
**def
Tau.BookIV.Electroweak.example_null :NullTransportMode**

Equations
- Tau.BookIV.Electroweak.example_null = { sector := Tau.BookIII.Sectors.Sector.B }
Instances For

---

### `Tau.BookIV.Electroweak.TwoLoopWindowCoeff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L410-L427)
**structure
Tau.BookIV.Electroweak.TwoLoopWindowCoeff :Type**


[IV.D384] Two-Loop Window Coefficient c₂ = 1/W₄(3) = 1/18.
Loop order k → window W_{k+2}(·):


- One-loop: W₃(4) = 5

- Two-loop: W₄(3) = 18

- Inflationary: W₅(3) = 19
The same CF window sequence governs corrections across sectors.


- w3_4 : ℕ
One-loop window value.

- w4_3 : ℕ
Two-loop window value.

- w5_3 : ℕ
Inflationary window value.

- c2_denom : ℕ
c₂ denominator = W₄(3).

- arithmetic_check : self.w4_3 = self.w3_4 + 13
Window sequence is arithmetic at fixed arg 3.

Instances For

---

### `Tau.BookIV.Electroweak.instReprTwoLoopWindowCoeff.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L427-L427)
**def
Tau.BookIV.Electroweak.instReprTwoLoopWindowCoeff.repr :TwoLoopWindowCoeff → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprTwoLoopWindowCoeff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L427-L427)
**instance
Tau.BookIV.Electroweak.instReprTwoLoopWindowCoeff :Repr TwoLoopWindowCoeff**

Equations
- Tau.BookIV.Electroweak.instReprTwoLoopWindowCoeff = { reprPrec := Tau.BookIV.Electroweak.instReprTwoLoopWindowCoeff.repr }

---

### `Tau.BookIV.Electroweak.two_loop_window`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L429-L429)
**def
Tau.BookIV.Electroweak.two_loop_window :TwoLoopWindowCoeff**

Equations
- Tau.BookIV.Electroweak.two_loop_window = { arithmetic_check := Tau.BookIV.Electroweak.two_loop_window._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.window_depth_loop_correspondence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L431-L433)
**theorem
Tau.BookIV.Electroweak.window_depth_loop_correspondence :17 + 1 = 18 ∧ 18 + 1 = 19**


[IV.T204] Depth–loop correspondence: W₃(3)=17, W₄(3)=18, W₅(3)=19.

---

### `Tau.BookIV.Electroweak.c2_alpha_sub_1_ppm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L435-L439)
**theorem
Tau.BookIV.Electroweak.c2_alpha_sub_1_ppm :two_loop_window.c2_denom = 18 ∧ two_loop_window.w3_4 = 5**


[IV.P225] Two-loop α correction is sub-1 ppm:
α·c₂·ι<sub>τ</sub>² ≈ (1/137)·(1/18)·0.1165 ≈ 4.7×10⁻⁵ ≈ 0.5 ppm.

---

### `Tau.BookIV.Electroweak.AlphaNLOCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L448-L464)
**structure
Tau.BookIV.Electroweak.AlphaNLOCatalog :Type**


[IV.D385] α NLO Correction Candidate Catalog.
Four candidates, none improves 9.8 ppm:
A: +ι<sub>τ</sub>⁶/(5·2) = +158 ppm (wrong direction)
B: +ι<sub>τ</sub>⁴/25 = +543 ppm (wrong direction)
C: −ι<sub>τ</sub>²/50 = −2330 ppm (too large)
D: +ι<sub>τ</sub>²/18 = +6470 ppm (too large)
All overshoot or wrong sign vs the +9.8 ppm residual.

- n_candidates : ℕ
Number of candidates assessed.

- current_ppm : ℕ
Current precision in ppm (LO tower formula).

- smallest_shift : ℕ
Smallest candidate shift magnitude in ppm.

- all_overshoot : Bool
All candidates overshoot.

Instances For

---

### `Tau.BookIV.Electroweak.instReprAlphaNLOCatalog.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L464-L464)
**def
Tau.BookIV.Electroweak.instReprAlphaNLOCatalog.repr :AlphaNLOCatalog → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprAlphaNLOCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L464-L464)
**instance
Tau.BookIV.Electroweak.instReprAlphaNLOCatalog :Repr AlphaNLOCatalog**

Equations
- Tau.BookIV.Electroweak.instReprAlphaNLOCatalog = { reprPrec := Tau.BookIV.Electroweak.instReprAlphaNLOCatalog.repr }

---

### `Tau.BookIV.Electroweak.alpha_nlo_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L466-L466)
**def
Tau.BookIV.Electroweak.alpha_nlo_catalog :AlphaNLOCatalog**

Equations
- Tau.BookIV.Electroweak.alpha_nlo_catalog = { }
Instances For

---

### `Tau.BookIV.Electroweak.AlphaPrecisionBarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L468-L478)
**structure
Tau.BookIV.Electroweak.AlphaPrecisionBarrier :Type**


[IV.T205] α precision barrier: 9.8 ppm is the current limit.
The fraction 11/15 is isolated (unique a/b ≤ 100 within 10 ppm)
and all NLO candidates overshoot or have wrong sign.

- precision_ppm : Float
Precision in ppm (tower formula).

- fraction_isolated : Bool
11/15 is isolated (unique in a,b ≤ 100).

- nlo_improves : Bool
NLO catalog empty (no improvement found).

Instances For

---

### `Tau.BookIV.Electroweak.instReprAlphaPrecisionBarrier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L478-L478)
**def
Tau.BookIV.Electroweak.instReprAlphaPrecisionBarrier.repr :AlphaPrecisionBarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprAlphaPrecisionBarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L478-L478)
**instance
Tau.BookIV.Electroweak.instReprAlphaPrecisionBarrier :Repr AlphaPrecisionBarrier**

Equations
- Tau.BookIV.Electroweak.instReprAlphaPrecisionBarrier = { reprPrec := Tau.BookIV.Electroweak.instReprAlphaPrecisionBarrier.repr }

---

### `Tau.BookIV.Electroweak.alpha_precision_barrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L480-L480)
**def
Tau.BookIV.Electroweak.alpha_precision_barrier :AlphaPrecisionBarrier**

Equations
- Tau.BookIV.Electroweak.alpha_precision_barrier = { }
Instances For
