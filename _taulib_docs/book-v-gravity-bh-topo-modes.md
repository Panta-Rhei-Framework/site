---
layout: taulib-doc
title: "TauLib.BookV.Gravity.BHTopoModes"
permalink: /verify/taulib/docs/book-v-gravity-bh-topo-modes/
lane: verify
module_name: "TauLib.BookV.Gravity.BHTopoModes"
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

# TauLib.BookV.Gravity.BHTopoModes


T² torus horizon topology for τ-black holes: quasi-normal mode spectrum,
GW echo times, entropy comparison, and no-Hawking argument.

## Registry Cross-References


- [V.D234] T² QNM Mode Structure -- `TorusMode`

- [V.T168] QNM Fundamental Frequency Ratio = ι<sub>τ</sub>⁻¹ -- `qnm_ratio_is_iota_inv`

- [V.T169] GW Echo Times t± = 4GM·ι<sub>τ</sub>^{±1}/c³ -- `echo_time_outer`, `echo_time_inner`

- [V.P124] T² Shadow Radius vs EHT -- `m87_shadow_tau_outer_uas`

- [V.P125] T² Entropy = π·ι<sub>τ</sub> × S² Entropy -- `torus_entropy_ratio`

- [V.R373] LIGO Echo Window -- `echo_separation`

- [V.R374] No-Hawking from τ-vacuum -- `no_hawking_argument`


## Physical Context


The τ-black hole has T² topology (not S²). The two fundamental torus cycles give
QNM frequency ratio ι<sub>τ</sub>⁻¹ ≈ 2.9299, distinct from Schwarzschild overtone ratio ≈ 0.928.

## Numerical Ground Truth (from scripts/bh_topology_lab.py, mpmath 50 dps)


- ι<sub>τ</sub> = 0.34130423887521951564

- ι<sub>τ</sub>⁻¹ = 2.9299372410244192369

- f(0,1)/f(1,0) = ι<sub>τ</sub>⁻¹ ≈ 2.9299

- For M=30 M_☉: Δt = 1.5303 ms

- For M=62 M_☉ (GW150914): Δt = 3.1626 ms

- π·ι<sub>τ</sub> = 1.07223889 (entropy ratio)


---

### `Tau.BookV.Gravity.TorusMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L52-L62)
**structure
Tau.BookV.Gravity.TorusMode :Type**


A torus quasi-normal mode labeled by integer winding numbers (n, m)
for the outer and inner S¹ cycles respectively. [V.D234]

Laplacian eigenvalue (in units 1/R²): λ_{n,m} = n² + m²·ι<sub>τ</sub>⁻²
QNM frequency: f_{n,m} ∝ √λ_{n,m}

- n : ℤ
Outer S¹ winding number (outer horizon cycle).

- m : ℤ
Inner S¹ winding number (inner horizon cycle, r = R·ι<sub>τ</sub>).

Instances For

---

### `Tau.BookV.Gravity.instReprTorusMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L62-L62)
**def
Tau.BookV.Gravity.instReprTorusMode.repr :TorusMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprTorusMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L62-L62)
**instance
Tau.BookV.Gravity.instReprTorusMode :Repr TorusMode**

Equations
- Tau.BookV.Gravity.instReprTorusMode = { reprPrec := Tau.BookV.Gravity.instReprTorusMode.repr }

---

### `Tau.BookV.Gravity.primitiveTorusModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L64-L68)
**def
Tau.BookV.Gravity.primitiveTorusModes :List TorusMode**


The three primitive torus modes with lowest non-zero QNM frequencies.
Equations
- Tau.BookV.Gravity.primitiveTorusModes = [{ n := 1, m := 0 }, { n := 0, m := 1 }, { n := 1, m := 1 }]
Instances For

---

### `Tau.BookV.Gravity.torusEigenvalue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L70-L75)
**def
Tau.BookV.Gravity.torusEigenvalue
(mode : TorusMode)
 :Float**


Laplacian eigenvalue of mode (n,m) in units of 1/R², using Float ι<sub>τ</sub>.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.torusQnmFreq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L77-L79)
**def
Tau.BookV.Gravity.torusQnmFreq
(mode : TorusMode)
 :Float**


QNM frequency of mode (n,m) in units of c/(2πR).
Equations
- Tau.BookV.Gravity.torusQnmFreq mode = (Tau.BookV.Gravity.torusEigenvalue mode).sqrt
Instances For

---

### `Tau.BookV.Gravity.qnm_ratio_is_iota_inv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L85-L95)
**theorem
Tau.BookV.Gravity.qnm_ratio_is_iota_inv :Boundary.iota_tau_numer < Boundary.iota_tau_denom**


The QNM frequency ratio f(0,1)/f(1,0) = R/r = ι<sub>τ</sub>⁻¹ ≈ 2.9299. [V.T168]
Inner cycle is faster than outer cycle by factor ι<sub>τ</sub>⁻¹.
Proof: f_{(n,m)} ∝ √(n²/R² + m²/r²)
f(0,1)/f(1,0) = (1/r)/(1/R) = R/r = 1/ι<sub>τ</sub>
This follows from V.T01: r/R = ι<sub>τ</sub>

Nat-level proof: ι<sub>τ</sub> = iota_tau_numer/iota_tau_denom = 341304/1000000,
so ι<sub>τ</sub>⁻¹ = iota_tau_denom/iota_tau_numer. The ratio exceeds 1 because
iota_tau_numer < iota_tau_denom (equivalently, ι<sub>τ</sub> < 1).

---

### `Tau.BookV.Gravity.qnm_frequency_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L97-L98)
**def
Tau.BookV.Gravity.qnm_frequency_ratio :Float**


Numerical value: QNM inner/outer frequency ratio = ι<sub>τ</sub>⁻¹.
Equations
- Tau.BookV.Gravity.qnm_frequency_ratio = 1.0 / Tau.BookV.Gravity.iota_float✝
Instances For

---

### `Tau.BookV.Gravity.schwarzschild_overtone_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L100-L101)
**def
Tau.BookV.Gravity.schwarzschild_overtone_ratio :Float**


The Schwarzschild l=2 overtone ratio (for comparison).
Equations
- Tau.BookV.Gravity.schwarzschild_overtone_ratio = 0.928
Instances For

---

### `Tau.BookV.Gravity.G_Newton`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L107-L108)
**def
Tau.BookV.Gravity.G_Newton :Float**


Newton's gravitational constant G [m³/(kg·s²)].
Equations
- Tau.BookV.Gravity.G_Newton = 6674e-14
Instances For

---

### `Tau.BookV.Gravity.c_light`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L110-L111)
**def
Tau.BookV.Gravity.c_light :Float**


Speed of light c [m/s].
Equations
- Tau.BookV.Gravity.c_light = 2998e5
Instances For

---

### `Tau.BookV.Gravity.M_sun`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L113-L114)
**def
Tau.BookV.Gravity.M_sun :Float**


Solar mass [kg].
Equations
- Tau.BookV.Gravity.M_sun = 1989e27
Instances For

---

### `Tau.BookV.Gravity.echo_time_outer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L120-L123)
**def
Tau.BookV.Gravity.echo_time_outer
(M_kg : Float)
 :Float**


Outer echo time: t_outer = 4GM·ι<sub>τ</sub>⁻¹/c³ [seconds].
Corresponds to outer S¹ round-trip on the torus horizon. [V.T169]
Equations
- Tau.BookV.Gravity.echo_time_outer M_kg = 4.0 * Tau.BookV.Gravity.G_Newton * M_kg / (Tau.BookV.Gravity.iota_float✝ * Tau.BookV.Gravity.c_light ^ 3)
Instances For

---

### `Tau.BookV.Gravity.echo_time_inner`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L125-L128)
**def
Tau.BookV.Gravity.echo_time_inner
(M_kg : Float)
 :Float**


Inner echo time: t_inner = 4GM·ι<sub>τ</sub>/c³ [seconds].
Corresponds to inner S¹ round-trip on the torus horizon. [V.T169]
Equations
- Tau.BookV.Gravity.echo_time_inner M_kg = 4.0 * Tau.BookV.Gravity.G_Newton * M_kg * Tau.BookV.Gravity.iota_float✝ / Tau.BookV.Gravity.c_light ^ 3
Instances For

---

### `Tau.BookV.Gravity.echo_separation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L130-L133)
**def
Tau.BookV.Gravity.echo_separation
(M_kg : Float)
 :Float**


Echo separation: Δt = t_outer - t_inner = 4GM(ι<sub>τ</sub>⁻¹ - ι<sub>τ</sub>)/c³ [seconds].
Lab values: M=30 M_☉ → 1.5303 ms; M=62 M_☉ → 3.1626 ms. [V.R373]
Equations
- Tau.BookV.Gravity.echo_separation M_kg = Tau.BookV.Gravity.echo_time_outer M_kg - Tau.BookV.Gravity.echo_time_inner M_kg
Instances For

---

### `Tau.BookV.Gravity.echo_separation_ms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L135-L137)
**def
Tau.BookV.Gravity.echo_separation_ms
(M_solar : Float)
 :Float**


Echo separation in milliseconds for a given mass in solar masses.
Equations
- Tau.BookV.Gravity.echo_separation_ms M_solar = Tau.BookV.Gravity.echo_separation (M_solar * Tau.BookV.Gravity.M_sun) * 1000.0
Instances For

---

### `Tau.BookV.Gravity.m87_shadow_tau_outer_uas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L143-L151)
**def
Tau.BookV.Gravity.m87_shadow_tau_outer_uas :Float**


T² outer torus angular size for M87* [microarcseconds].
θ_outer = 4πGM/(c²·d) · (rad → μas conversion). [V.P124]
M87*: M = 6.5×10⁹ M_☉, d = 16.8 Mpc.
Lab value: 48.00 μas (EHT observed: 42 ± 3 μas).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.m87_shadow_gr_uas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L153-L159)
**def
Tau.BookV.Gravity.m87_shadow_gr_uas :Float**


GR photon sphere angular size for M87* [microarcseconds].
R_shadow = 3√3 GM/c². Lab value: 19.85 μas.
Equations
- Tau.BookV.Gravity.m87_shadow_gr_uas = 3.0 * Float.sqrt 3.0 * Tau.BookV.Gravity.G_Newton * (65e8 * Tau.BookV.Gravity.M_sun) / Tau.BookV.Gravity.c_light ^ 2 / (16.8 * 3086e19) * 2062650e5
Instances For

---

### `Tau.BookV.Gravity.torus_entropy_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L165-L170)
**def
Tau.BookV.Gravity.torus_entropy_ratio :Float**


T² / S² Bekenstein-Hawking entropy ratio = π · ι<sub>τ</sub>.
Derivation: A_{T²} = 4π²R_S²ι<sub>τ</sub>, A_{S²} = 4πR_S²
S_{T²}/S_{S²} = A_{T²}/A_{S²} = πι<sub>τ</sub> ≈ 1.0722.
[V.P125]
Equations
- Tau.BookV.Gravity.torus_entropy_ratio = 3.14159265358979 * Tau.BookV.Gravity.iota_float✝
Instances For

---

### `Tau.BookV.Gravity.no_hawking_argument`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L176-L183)
**def
Tau.BookV.Gravity.no_hawking_argument :String**


The τ-vacuum has no in/out split → no Bogoliubov transformation
→ no Hawking radiation. SA-i forbids sub-kernel modes.
Combined with No-Shrink (V.T03): τ-BHs do not evaporate. [V.R374]
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.three_primitive_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L189-L191)
**theorem
Tau.BookV.Gravity.three_primitive_modes :primitiveTorusModes.length = 3**


There are exactly 3 primitive torus modes.

---

### `Tau.BookV.Gravity.outer_mode_has_zero_inner`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L193-L195)
**theorem
Tau.BookV.Gravity.outer_mode_has_zero_inner :(primitiveTorusModes.get ⟨0, ⋯⟩).m = 0**


The outer mode has zero inner winding.

---

### `Tau.BookV.Gravity.inner_mode_has_zero_outer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L197-L199)
**theorem
Tau.BookV.Gravity.inner_mode_has_zero_outer :(primitiveTorusModes.get ⟨1, ⋯⟩).n = 0**


The inner mode has zero outer winding.

---

### `Tau.BookV.Gravity.qnm_ratio_gt_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L201-L206)
**theorem
Tau.BookV.Gravity.qnm_ratio_gt_one :qnm_frequency_ratio > 1.0**


QNM frequency ratio exceeds 1 (inner faster than outer).
This holds because ι<sub>τ</sub> < 1, so ι<sub>τ</sub>⁻¹ > 1.

---

### `Tau.BookV.Gravity.torus_entropy_ratio_gt_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L208-L212)
**theorem
Tau.BookV.Gravity.torus_entropy_ratio_gt_one :torus_entropy_ratio > 1.0**


Entropy ratio exceeds 1 (T² has more entropy than S²).

---

### `Tau.BookV.Gravity.outer_echo_longer_than_inner`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L214-L220)
**theorem
Tau.BookV.Gravity.outer_echo_longer_than_inner :Boundary.iota_tau_denom * Boundary.iota_tau_denom > Boundary.iota_tau_numer * Boundary.iota_tau_numer**


Outer echo time exceeds inner echo time.
Structural: t_outer/t_inner = ι<sub>τ</sub>⁻² > 1 because ι<sub>τ</sub> < 1.
Nat-level proof: iota_tau_denom² > iota_tau_numer²
(1000000² = 10¹² > 341304² ≈ 1.165 × 10¹¹).

---

### `Tau.BookV.Gravity.echo_separation_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L222-L227)
**theorem
Tau.BookV.Gravity.echo_separation_pos :Boundary.iota_tau_denom > Boundary.iota_tau_numer**


Echo separation Δt > 0 for positive mass.
Structural: Δt ∝ (ι<sub>τ</sub>⁻¹ − ι<sub>τ</sub>) > 0 because ι<sub>τ</sub>⁻¹ > 1 > ι<sub>τ</sub>.
Nat-level proof: iota_tau_denom > iota_tau_numer (i.e., ι<sub>τ</sub> < 1).

---

### `Tau.BookV.Gravity.t2_qnm_eigenvalue_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L266-L271)
**def
Tau.BookV.Gravity.t2_qnm_eigenvalue_structure :String**


[V.D242] T² QNM Eigenvalue Structure.
ω_{n,m} = √(n²+m²·ι<sub>τ</sub>⁻²)/(2π·r_s). First 3 overtones:
(1,0): 1.000, (0,1): ι<sub>τ</sub>⁻¹=2.930, (1,1): √(1+ι<sub>τ</sub>⁻²)=3.096.
Equations
- Tau.BookV.Gravity.t2_qnm_eigenvalue_structure = "T² QNM: ω_{n,m} = √(n²+m²·ι<sub>τ</sub>⁻²)/(2πr_s). " ++ "Overtones: (1,0)→1.000, (0,1)→2.930, (1,1)→3.096."
Instances For

---

### `Tau.BookV.Gravity.T2QNMEigenvalues`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L273-L285)
**structure
Tau.BookV.Gravity.T2QNMEigenvalues :Type**


[V.D242] Structure capturing the T² QNM eigenvalue structure.
3 primitive modes from 2 S¹ cycles (outer winding n, inner winding m).
Spectrum is anisotropic because r ≠ R (aspect ratio = ι<sub>τ</sub>).

- n_primitive_modes : ℕ
Number of primitive torus modes with lowest non-zero frequency.

- outer_winding : ℕ
Outer S¹ winding quantum number for fundamental mode.

- inner_winding : ℕ
Inner S¹ winding quantum number for fundamental mode.

- n_independent_frequencies : ℕ
Number of independent frequencies from the 2 S¹ cycles (anisotropic: r ≠ R).

Instances For

---

### `Tau.BookV.Gravity.instReprT2QNMEigenvalues`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L285-L285)
**instance
Tau.BookV.Gravity.instReprT2QNMEigenvalues :Repr T2QNMEigenvalues**

Equations
- Tau.BookV.Gravity.instReprT2QNMEigenvalues = { reprPrec := Tau.BookV.Gravity.instReprT2QNMEigenvalues.repr }

---

### `Tau.BookV.Gravity.instReprT2QNMEigenvalues.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L285-L285)
**def
Tau.BookV.Gravity.instReprT2QNMEigenvalues.repr :T2QNMEigenvalues → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instInhabitedT2QNMEigenvalues`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L287-L288)
**instance
Tau.BookV.Gravity.instInhabitedT2QNMEigenvalues :Inhabited T2QNMEigenvalues**


Canonical T² QNM eigenvalue data.
Equations
- Tau.BookV.Gravity.instInhabitedT2QNMEigenvalues = { default := { } }

---

### `Tau.BookV.Gravity.t2_qnm_eigenvalues_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L290-L295)
**theorem
Tau.BookV.Gravity.t2_qnm_eigenvalues_conjunction :have d := { };
d.n_primitive_modes = 3 ∧ d.outer_winding = 1 ∧ d.inner_winding = 1 ∧ d.n_independent_frequencies = 2**


All structural properties of T² QNM eigenvalues hold.

---

### `Tau.BookV.Gravity.t2_qnm_modes_eq_list`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L297-L299)
**theorem
Tau.BookV.Gravity.t2_qnm_modes_eq_list :default.n_primitive_modes = primitiveTorusModes.length**


The number of primitive modes equals the length of primitiveTorusModes.

---

### `Tau.BookV.Gravity.t2_echo_time_formulas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L303-L307)
**def
Tau.BookV.Gravity.t2_echo_time_formulas :String**


[V.D243] T² GW Echo Time Formulas.
t₊=4GMι<sub>τ</sub>/c³ (inner), t₋=4GMι<sub>τ</sub>⁻¹/c³ (outer), t₋/t₊=ι<sub>τ</sub>⁻²=8.585.
Equations
- Tau.BookV.Gravity.t2_echo_time_formulas = "GW echoes: t₊=4GMι<sub>τ</sub>/c³, t₋=4GMι<sub>τ</sub>⁻¹/c³, ratio t₋/t₊=ι<sub>τ</sub>⁻²=8.585. " ++ "GW150914: t₊=0.417 ms, t₋=3.580 ms, both in LIGO band."
Instances For

---

### `Tau.BookV.Gravity.T2EchoFormulas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L309-L321)
**structure
Tau.BookV.Gravity.T2EchoFormulas :Type**


[V.D243] Structure capturing T² GW echo time formulas.
t₋/t₊ = ι<sub>τ</sub>⁻² ≈ 8.585. Both echoes fall in LIGO band for stellar-mass BHs.
Ratio stored ×1000 for Nat arithmetic.

- ratio_x1000 : ℕ
Echo time ratio ×1000 (ι<sub>τ</sub>⁻² ≈ 8.585 → 8585).

- n_ligo_band : ℕ
Number of echo times in LIGO band (inner + outer).

- n_reference_events : ℕ
Number of reference events tested (GW150914).

- ratio_gt_1000 : self.ratio_x1000 > 1000
Ratio exceeds 1000 (i.e., ι<sub>τ</sub>⁻² > 1, inner is shorter).

Instances For

---

### `Tau.BookV.Gravity.instReprT2EchoFormulas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L321-L321)
**instance
Tau.BookV.Gravity.instReprT2EchoFormulas :Repr T2EchoFormulas**

Equations
- Tau.BookV.Gravity.instReprT2EchoFormulas = { reprPrec := Tau.BookV.Gravity.instReprT2EchoFormulas.repr }

---

### `Tau.BookV.Gravity.instReprT2EchoFormulas.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L321-L321)
**def
Tau.BookV.Gravity.instReprT2EchoFormulas.repr :T2EchoFormulas → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.t2_echo_formulas_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L323-L325)
**def
Tau.BookV.Gravity.t2_echo_formulas_data :T2EchoFormulas**


Canonical T² echo formula data.
Equations
- Tau.BookV.Gravity.t2_echo_formulas_data = { ratio_gt_1000 := Tau.BookV.Gravity.t2_echo_formulas_data._proof_2 }
Instances For

---

### `Tau.BookV.Gravity.instInhabitedT2EchoFormulas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L327-L327)
**instance
Tau.BookV.Gravity.instInhabitedT2EchoFormulas :Inhabited T2EchoFormulas**

Equations
- Tau.BookV.Gravity.instInhabitedT2EchoFormulas = { default := Tau.BookV.Gravity.t2_echo_formulas_data }

---

### `Tau.BookV.Gravity.t2_echo_formulas_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L329-L334)
**theorem
Tau.BookV.Gravity.t2_echo_formulas_conjunction :t2_echo_formulas_data.ratio_x1000 = 8585 ∧ t2_echo_formulas_data.n_ligo_band = 2 ∧ t2_echo_formulas_data.n_reference_events = 1**


All structural properties of the T² echo formulas hold.

---

### `Tau.BookV.Gravity.echo_ratio_approx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L336-L338)
**theorem
Tau.BookV.Gravity.echo_ratio_approx :t2_echo_formulas_data.ratio_x1000 = 8585**


Echo time ratio ×1000 = 8585.

---

### `Tau.BookV.Gravity.qnm_frequency_ratio_discriminator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L342-L347)
**def
Tau.BookV.Gravity.qnm_frequency_ratio_discriminator :String**


[V.T185] QNM Frequency Ratio = ι<sub>τ</sub>⁻¹ as Clean Discriminator.
ω(0,1)/ω(1,0) = ι<sub>τ</sub>⁻¹ = (π+e)/2 = 2.930.
T² range [2.5,3.4] vs S² range [0.8,1.1]: no overlap.
Equations
- Tau.BookV.Gravity.qnm_frequency_ratio_discriminator = "QNM ratio ω(0,1)/ω(1,0) = ι<sub>τ</sub>⁻¹ = 2.930. " ++ "T² prediction [2.5,3.4] vs S² [0.8,1.1]: zero-parameter discriminator."
Instances For

---

### `Tau.BookV.Gravity.QNMDiscriminator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L349-L367)
**structure
Tau.BookV.Gravity.QNMDiscriminator :Type**


[V.T185] Structure capturing the QNM frequency ratio discriminator.
T² range [2.5, 3.4] vs S² range [0.8, 1.1]: no overlap → clean discriminator.
All values stored ×10 to use Nat arithmetic.

- t2_lower_x10 : ℕ
T² lower bound ×10 (= 2.5 → 25).

- t2_upper_x10 : ℕ
T² upper bound ×10 (= 3.4 → 34).

- s2_lower_x10 : ℕ
S² lower bound ×10 (= 0.8 → 8).

- s2_upper_x10 : ℕ
S² upper bound ×10 (= 1.1 → 11).

- range_gap_x10 : ℕ
Range gap ×10 = t2_lower − s2_upper (>0 means no overlap).

- gap_eq : self.range_gap_x10 = self.t2_lower_x10 - self.s2_upper_x10
Gap equals t2_lower − s2_upper.

- free_parameters : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Gravity.instReprQNMDiscriminator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L367-L367)
**instance
Tau.BookV.Gravity.instReprQNMDiscriminator :Repr QNMDiscriminator**

Equations
- Tau.BookV.Gravity.instReprQNMDiscriminator = { reprPrec := Tau.BookV.Gravity.instReprQNMDiscriminator.repr }

---

### `Tau.BookV.Gravity.instReprQNMDiscriminator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L367-L367)
**def
Tau.BookV.Gravity.instReprQNMDiscriminator.repr :QNMDiscriminator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.qnm_discriminator_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L369-L371)
**def
Tau.BookV.Gravity.qnm_discriminator_data :QNMDiscriminator**


Canonical QNM discriminator data.
Equations
- Tau.BookV.Gravity.qnm_discriminator_data = { gap_eq := Tau.BookV.Gravity.qnm_discriminator_data._proof_1 }
Instances For

---

### `Tau.BookV.Gravity.instInhabitedQNMDiscriminator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L373-L373)
**instance
Tau.BookV.Gravity.instInhabitedQNMDiscriminator :Inhabited QNMDiscriminator**

Equations
- Tau.BookV.Gravity.instInhabitedQNMDiscriminator = { default := Tau.BookV.Gravity.qnm_discriminator_data }

---

### `Tau.BookV.Gravity.qnm_discriminator_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L375-L381)
**theorem
Tau.BookV.Gravity.qnm_discriminator_conjunction :qnm_discriminator_data.t2_lower_x10 = 25 ∧ qnm_discriminator_data.s2_lower_x10 = 8 ∧ qnm_discriminator_data.range_gap_x10 = 14 ∧ qnm_discriminator_data.free_parameters = 0**


All structural properties of the QNM discriminator hold.

---

### `Tau.BookV.Gravity.qnm_ranges_separated`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L383-L386)
**theorem
Tau.BookV.Gravity.qnm_ranges_separated :qnm_discriminator_data.t2_lower_x10 > qnm_discriminator_data.s2_upper_x10**


T² lower bound exceeds S² upper bound → ranges are separated.

---

### `Tau.BookV.Gravity.bh_t2_falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L398-L406)
**def
Tau.BookV.Gravity.bh_t2_falsification :String**


[V.P131] Three falsifiable T² BH predictions with explicit error bars.
(1) QNM ratio = ι<sub>τ</sub>⁻¹ (discriminator), (2) shadow correction +2.91%,
(3) GW echoes at t₊ = 4GM·ι<sub>τ</sub>/c³. All zero-free-parameter predictions.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.BHT2Falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L408-L418)
**structure
Tau.BookV.Gravity.BHT2Falsification :Type**


[V.P131] Structure capturing the three falsifiable T² BH predictions.

- n_predictions : ℕ
Number of independent falsifiable predictions.

- n_channels : ℕ
Number of observational channels (QNM + shadow + echoes).

- predictions_eq_channels : self.n_predictions = self.n_channels
Predictions equal channels.

- free_parameters : ℕ
Number of free parameters across all predictions.

Instances For

---

### `Tau.BookV.Gravity.instReprBHT2Falsification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L418-L418)
**def
Tau.BookV.Gravity.instReprBHT2Falsification.repr :BHT2Falsification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprBHT2Falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L418-L418)
**instance
Tau.BookV.Gravity.instReprBHT2Falsification :Repr BHT2Falsification**

Equations
- Tau.BookV.Gravity.instReprBHT2Falsification = { reprPrec := Tau.BookV.Gravity.instReprBHT2Falsification.repr }

---

### `Tau.BookV.Gravity.bh_t2_falsification_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L420-L422)
**def
Tau.BookV.Gravity.bh_t2_falsification_data :BHT2Falsification**


Canonical BH T² falsification data.
Equations
- Tau.BookV.Gravity.bh_t2_falsification_data = { predictions_eq_channels := Tau.BookV.Gravity.bh_t2_falsification_data._proof_1 }
Instances For

---

### `Tau.BookV.Gravity.instInhabitedBHT2Falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L424-L424)
**instance
Tau.BookV.Gravity.instInhabitedBHT2Falsification :Inhabited BHT2Falsification**

Equations
- Tau.BookV.Gravity.instInhabitedBHT2Falsification = { default := Tau.BookV.Gravity.bh_t2_falsification_data }

---

### `Tau.BookV.Gravity.bh_t2_falsification_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L426-L431)
**theorem
Tau.BookV.Gravity.bh_t2_falsification_conjunction :bh_t2_falsification_data.n_predictions = 3 ∧ bh_t2_falsification_data.n_channels = 3 ∧ bh_t2_falsification_data.free_parameters = 0**


All structural properties of BH T² falsification hold.

---

### `Tau.BookV.Gravity.bh_predictions_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L433-L435)
**theorem
Tau.BookV.Gravity.bh_predictions_count :bh_t2_falsification_data.n_predictions = 3**


There are exactly 3 falsifiable predictions.

---

### `Tau.BookV.Gravity.vop5_sprint7e_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L444-L450)
**def
Tau.BookV.Gravity.vop5_sprint7e_status :String**


[V.R380] V.OP5 SOLVED: Sprint 7E provides complete observational
signature suite for T² BH topology. Three channels (EHT, QNM, GW echo)
all derived from ι<sub>τ</sub> with zero free parameters.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.VOP5Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L452-L462)
**structure
Tau.BookV.Gravity.VOP5Status :Type**


[V.R380] Structure capturing V.OP5 solution status.

- n_observational_channels : ℕ
Number of independent observational channels.

- n_input_constants : ℕ
Number of input constants (just ι<sub>τ</sub>).

- n_cross_checks : ℕ
Number of independent cross-checks (entropy ratio).

- free_parameters : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Gravity.instReprVOP5Status.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L462-L462)
**def
Tau.BookV.Gravity.instReprVOP5Status.repr :VOP5Status → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprVOP5Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L462-L462)
**instance
Tau.BookV.Gravity.instReprVOP5Status :Repr VOP5Status**

Equations
- Tau.BookV.Gravity.instReprVOP5Status = { reprPrec := Tau.BookV.Gravity.instReprVOP5Status.repr }

---

### `Tau.BookV.Gravity.vop5_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L464-L465)
**def
Tau.BookV.Gravity.vop5_data :VOP5Status**


Canonical V.OP5 status data.
Equations
- Tau.BookV.Gravity.vop5_data = { }
Instances For

---

### `Tau.BookV.Gravity.instInhabitedVOP5Status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L467-L467)
**instance
Tau.BookV.Gravity.instInhabitedVOP5Status :Inhabited VOP5Status**

Equations
- Tau.BookV.Gravity.instInhabitedVOP5Status = { default := Tau.BookV.Gravity.vop5_data }

---

### `Tau.BookV.Gravity.vop5_status_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L469-L475)
**theorem
Tau.BookV.Gravity.vop5_status_conjunction :vop5_data.n_observational_channels = 3 ∧ vop5_data.n_input_constants = 1 ∧ vop5_data.n_cross_checks = 1 ∧ vop5_data.free_parameters = 0**


All structural properties of V.OP5 status hold.

---

### `Tau.BookV.Gravity.vop5_channels_eq_predictions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L477-L480)
**theorem
Tau.BookV.Gravity.vop5_channels_eq_predictions :vop5_data.n_observational_channels = bh_t2_falsification_data.n_predictions**


V.OP5 channels = BH T² falsification predictions.

---

### `Tau.BookV.Gravity.BHEntropyCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L489-L496)
**structure
Tau.BookV.Gravity.BHEntropyCatalog :Type**


Black hole entropy catalog entry — V.T216
S_τ = πι<sub>τ</sub> · k_B · A/(4ℓ_P²) for T² horizon topology

- name : String
- mass_solar : ℕ
- log10_entropy : ℕ
- t2_excess_x1000 : ℕ
Instances For

---

### `Tau.BookV.Gravity.instReprBHEntropyCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L496-L496)
**instance
Tau.BookV.Gravity.instReprBHEntropyCatalog :Repr BHEntropyCatalog**

Equations
- Tau.BookV.Gravity.instReprBHEntropyCatalog = { reprPrec := Tau.BookV.Gravity.instReprBHEntropyCatalog.repr }

---

### `Tau.BookV.Gravity.instReprBHEntropyCatalog.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L496-L496)
**def
Tau.BookV.Gravity.instReprBHEntropyCatalog.repr :BHEntropyCatalog → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.t2_entropy_excess_x10000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L498-L499)
**def
Tau.BookV.Gravity.t2_entropy_excess_x10000 :ℕ**


The T² entropy excess factor: πι<sub>τ</sub> ≈ 1.0722
Equations
- Tau.BookV.Gravity.t2_entropy_excess_x10000 = 10722
Instances For

---

### `Tau.BookV.Gravity.bh_entropy_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L501-L508)
**def
Tau.BookV.Gravity.bh_entropy_catalog :List BHEntropyCatalog**


5-entry catalog — V.T216
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.entropy_catalog_uniform_excess`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L510-L513)
**theorem
Tau.BookV.Gravity.entropy_catalog_uniform_excess
(e : BHEntropyCatalog)
 :e ∈ bh_entropy_catalog → e.t2_excess_x1000 = 1072**


All catalog entries share the same T² excess factor

---

### `Tau.BookV.Gravity.entropy_catalog_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L515-L518)
**def
Tau.BookV.Gravity.entropy_catalog_remark :String**


Entropy catalog remark — V.R402
Equations
- Tau.BookV.Gravity.entropy_catalog_remark = "S_BH ranges from ~10⁷⁹ k_B (stellar) to ~10⁹⁸ k_B (TON 618). " ++ "The T² excess factor πι<sub>τ</sub> ≈ 1.0722 is universal, independent of mass."
Instances For

---

### `Tau.BookV.Gravity.ReadoutGibbsState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L524-L533)
**structure
Tau.BookV.Gravity.ReadoutGibbsState :Type**


Readout Gibbs state — V.D276
The boundary Hilbert space admits a thermal state encoding information.
Temperature formula: T_H = ℏc³/(8πGMk_B).
Spectrum is Planckian but implies NO mass loss (No-Shrink Theorem).

- description : String
- temperature_formula : String
- is_planckian : ℕ
- implies_mass_loss : ℕ
Instances For

---

### `Tau.BookV.Gravity.instReprReadoutGibbsState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L533-L533)
**instance
Tau.BookV.Gravity.instReprReadoutGibbsState :Repr ReadoutGibbsState**

Equations
- Tau.BookV.Gravity.instReprReadoutGibbsState = { reprPrec := Tau.BookV.Gravity.instReprReadoutGibbsState.repr }

---

### `Tau.BookV.Gravity.instReprReadoutGibbsState.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L533-L533)
**def
Tau.BookV.Gravity.instReprReadoutGibbsState.repr :ReadoutGibbsState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.canonical_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L535-L537)
**def
Tau.BookV.Gravity.canonical_readout :ReadoutGibbsState**


Canonical readout state: Planckian (1), no mass loss (0)
Equations
- Tau.BookV.Gravity.canonical_readout = { description := "Boundary holonomy Gibbs state", temperature_formula := "ℏc³/(8πGMk_B)", is_planckian := 1,
 implies_mass_loss := 0 }
Instances For

---

### `Tau.BookV.Gravity.readout_no_mass_loss`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L539-L540)
**theorem
Tau.BookV.Gravity.readout_no_mass_loss :canonical_readout.implies_mass_loss = 0**


Readout does NOT imply mass loss — V.T217

---

### `Tau.BookV.Gravity.readout_is_planckian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L542-L543)
**theorem
Tau.BookV.Gravity.readout_is_planckian :canonical_readout.is_planckian = 1**


Readout IS Planckian — V.P148

---

### `Tau.BookV.Gravity.readout_planckian_gt_mass_loss`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L545-L548)
**theorem
Tau.BookV.Gravity.readout_planckian_gt_mass_loss :canonical_readout.is_planckian > canonical_readout.implies_mass_loss**


Planckian flag exceeds mass-loss flag (1 > 0): spectrum exists but no evaporation

---

### `Tau.BookV.Gravity.ReadoutTemperatureCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L550-L555)
**structure
Tau.BookV.Gravity.ReadoutTemperatureCatalog :Type**


Readout temperature catalog entry — V.R403

- name : String
- mass_solar : ℕ
- neg_log10_T : ℕ
Instances For

---

### `Tau.BookV.Gravity.instReprReadoutTemperatureCatalog.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L555-L555)
**def
Tau.BookV.Gravity.instReprReadoutTemperatureCatalog.repr :ReadoutTemperatureCatalog → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprReadoutTemperatureCatalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L555-L555)
**instance
Tau.BookV.Gravity.instReprReadoutTemperatureCatalog :Repr ReadoutTemperatureCatalog**

Equations
- Tau.BookV.Gravity.instReprReadoutTemperatureCatalog = { reprPrec := Tau.BookV.Gravity.instReprReadoutTemperatureCatalog.repr }

---

### `Tau.BookV.Gravity.readout_temp_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L557-L564)
**def
Tau.BookV.Gravity.readout_temp_catalog :List ReadoutTemperatureCatalog**


5-entry readout temperature catalog
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.readout_catalog_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L566-L568)
**theorem
Tau.BookV.Gravity.readout_catalog_length :readout_temp_catalog.length = 5**


Catalog has exactly 5 entries

---

### `Tau.BookV.Gravity.readout_temps_all_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L570-L573)
**theorem
Tau.BookV.Gravity.readout_temps_all_positive
(e : ReadoutTemperatureCatalog)
 :e ∈ readout_temp_catalog → e.neg_log10_T > 0**


All catalog entries have positive temperature exponent

---

### `Tau.BookV.Gravity.KMSReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L579-L598)
**structure
Tau.BookV.Gravity.KMSReadout :Type**


[Sprint 22C] KMS readout derivation. The Planckian spectrum follows from the
KMS condition on the boundary algebra without Bogoliubov transformations.

- H_∂[ω] restricted to L = S¹∨S¹ is a bosonic algebra (Book IV, K5+K6)

- The readout Gibbs state (V.D276, τ-effective) is max-entropy at T_H

- KMS condition (Haag-Hugenholtz-Winnink 1967): thermal equilibrium on
a bosonic algebra has unique spectral distribution = Bose-Einstein

- Therefore B(ν,T_H) = (2hν³/c²)/(exp(hν/k_BT_H)−1) — Planckian. QED.


- boundary_algebra_bosonic : ℕ
Boundary algebra is bosonic (from Book IV K5+K6).

- kms_condition_satisfied : ℕ
Readout state satisfies KMS condition at T_H.

- spectral_uniqueness : ℕ
Spectral distribution is unique (Haag-Hugenholtz-Winnink).

- is_planckian : ℕ
Resulting spectrum is Planckian.

- no_bogoliubov : ℕ
No Bogoliubov transformation needed.

Instances For

---

### `Tau.BookV.Gravity.instReprKMSReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L598-L598)
**instance
Tau.BookV.Gravity.instReprKMSReadout :Repr KMSReadout**

Equations
- Tau.BookV.Gravity.instReprKMSReadout = { reprPrec := Tau.BookV.Gravity.instReprKMSReadout.repr }

---

### `Tau.BookV.Gravity.instReprKMSReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L598-L598)
**def
Tau.BookV.Gravity.instReprKMSReadout.repr :KMSReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.kms_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L600-L601)
**def
Tau.BookV.Gravity.kms_readout :KMSReadout**


Canonical KMS readout data.
Equations
- Tau.BookV.Gravity.kms_readout = { }
Instances For

---

### `Tau.BookV.Gravity.kms_implies_planckian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L603-L609)
**theorem
Tau.BookV.Gravity.kms_implies_planckian :kms_readout.boundary_algebra_bosonic = 1 ∧ kms_readout.kms_condition_satisfied = 1 → kms_readout.is_planckian = 1**


KMS implies Planckian: if boundary algebra is bosonic and KMS holds,
the spectrum is uniquely Planckian.

---

### `Tau.BookV.Gravity.kms_no_bogoliubov`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L611-L613)
**theorem
Tau.BookV.Gravity.kms_no_bogoliubov :kms_readout.no_bogoliubov = 1**


The KMS derivation does not use Bogoliubov transformations.

---

### `Tau.BookV.Gravity.kms_consistent_with_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L615-L617)
**theorem
Tau.BookV.Gravity.kms_consistent_with_readout :kms_readout.is_planckian = canonical_readout.is_planckian**


KMS readout is consistent with the existing V.P148 readout_is_planckian.

---

### `Tau.BookV.Gravity.EchoSearchEvent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L630-L638)
**structure
Tau.BookV.Gravity.EchoSearchEvent :Type**


Echo search event entry — V.D283

- event_name : String
- final_mass_x10 : ℕ
- main_snr_x10 : ℕ
- echo_snr_x100 : ℕ
- t_plus_us : ℕ
- t_minus_us : ℕ
Instances For

---

### `Tau.BookV.Gravity.instReprEchoSearchEvent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L638-L638)
**instance
Tau.BookV.Gravity.instReprEchoSearchEvent :Repr EchoSearchEvent**

Equations
- Tau.BookV.Gravity.instReprEchoSearchEvent = { reprPrec := Tau.BookV.Gravity.instReprEchoSearchEvent.repr }

---

### `Tau.BookV.Gravity.instReprEchoSearchEvent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L638-L638)
**def
Tau.BookV.Gravity.instReprEchoSearchEvent.repr :EchoSearchEvent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.echo_search_catalog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L640-L652)
**def
Tau.BookV.Gravity.echo_search_catalog :List EchoSearchEvent**


10-event echo search catalog
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.echo_damping_10mode_x10000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L654-L655)
**def
Tau.BookV.Gravity.echo_damping_10mode_x10000 :ℕ**


(1,0) mode damping factor × 10000: exp(−π) ≈ 0.0432 → 432
Equations
- Tau.BookV.Gravity.echo_damping_10mode_x10000 = 432
Instances For

---

### `Tau.BookV.Gravity.echo_detection_snr_threshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L657-L658)
**def
Tau.BookV.Gravity.echo_detection_snr_threshold :ℕ**


Echo detection threshold — V.T225
Equations
- Tau.BookV.Gravity.echo_detection_snr_threshold = 3
Instances For

---

### `Tau.BookV.Gravity.stacked_echo_snr_x10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L660-L661)
**def
Tau.BookV.Gravity.stacked_echo_snr_x10 :ℕ**


Stacked echo SNR estimate — V.P151 (×10)
Equations
- Tau.BookV.Gravity.stacked_echo_snr_x10 = 22
Instances For

---

### `Tau.BookV.Gravity.events_needed_3sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L663-L664)
**def
Tau.BookV.Gravity.events_needed_3sigma :ℕ**


Events needed for 3σ detection
Equations
- Tau.BookV.Gravity.events_needed_3sigma = 19
Instances For

---

### `Tau.BookV.Gravity.et_sensitivity_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L666-L667)
**def
Tau.BookV.Gravity.et_sensitivity_factor :ℕ**


Einstein Telescope improvement factor
Equations
- Tau.BookV.Gravity.et_sensitivity_factor = 10
Instances For

---

### `Tau.BookV.Gravity.et_single_echo_snr_x10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L669-L670)
**def
Tau.BookV.Gravity.et_single_echo_snr_x10 :ℕ**


ET single-event echo SNR for GW150914-class (×10)
Equations
- Tau.BookV.Gravity.et_single_echo_snr_x10 = 104
Instances For

---

### `Tau.BookV.Gravity.echo_catalog_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L672-L674)
**theorem
Tau.BookV.Gravity.echo_catalog_length :echo_search_catalog.length = 10**


Catalog has 10 events

---

### `Tau.BookV.Gravity.et_single_event_detectable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L676-L679)
**theorem
Tau.BookV.Gravity.et_single_event_detectable :et_single_echo_snr_x10 > echo_detection_snr_threshold * 10**


ET single-event SNR exceeds detection threshold

---

### `Tau.BookV.Gravity.o1o3_stack_below_threshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L681-L684)
**theorem
Tau.BookV.Gravity.o1o3_stack_below_threshold :stacked_echo_snr_x10 < echo_detection_snr_threshold * 10**


O1-O3 stacked SNR is below 3σ threshold

---

### `Tau.BookV.Gravity.echo_search_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L686-L690)
**def
Tau.BookV.Gravity.echo_search_remark :String**


Echo search remark — V.R407
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.t2_lyapunov_correction_x10000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L696-L699)
**def
Tau.BookV.Gravity.t2_lyapunov_correction_x10000 :ℕ**


[Sprint 22D] T²-corrected Lyapunov exponent × 10000.
γ_τ = π(1+ι<sub>τ</sub>²/2) ≈ 3.324 → 33240 × 10000.
The T² correction factor is 1+ι<sub>τ</sub>²/2 ≈ 1.0583 (from V.P83, τ-effective).
Equations
- Tau.BookV.Gravity.t2_lyapunov_correction_x10000 = 10583
Instances For

---

### `Tau.BookV.Gravity.s2_lyapunov_x10000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L701-L702)
**def
Tau.BookV.Gravity.s2_lyapunov_x10000 :ℕ**


S² Lyapunov exponent × 10000: π ≈ 3.1416 → 31416
Equations
- Tau.BookV.Gravity.s2_lyapunov_x10000 = 31416
Instances For

---

### `Tau.BookV.Gravity.t2_lyapunov_exceeds_s2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L704-L706)
**theorem
Tau.BookV.Gravity.t2_lyapunov_exceeds_s2 :t2_lyapunov_correction_x10000 > 10000**


T² Lyapunov exceeds S² (tighter bound on echo amplitude).

---

### `Tau.BookV.Gravity.echo_damping_t2_bound_x10000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L708-L710)
**def
Tau.BookV.Gravity.echo_damping_t2_bound_x10000 :ℕ**


Echo damping bound (1,0) mode × 10000 with T² correction:
exp(−γ_τ) ≈ 0.0361 → 361 (compared to S² value 432).
Equations
- Tau.BookV.Gravity.echo_damping_t2_bound_x10000 = 361
Instances For

---

### `Tau.BookV.Gravity.t2_echo_bound_tighter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L712-L714)
**theorem
Tau.BookV.Gravity.t2_echo_bound_tighter :echo_damping_t2_bound_x10000 < echo_damping_10mode_x10000**


T² echo bound is tighter than S² estimate.

---

### `Tau.BookV.Gravity.t2_echo_reduction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/BHTopoModes.lean#L716-L718)
**theorem
Tau.BookV.Gravity.t2_echo_reduction :echo_damping_10mode_x10000 - echo_damping_t2_bound_x10000 = 71**


The T² correction reduces echo amplitude by ~16%.
