---
layout: taulib-doc
title: "TauLib.BookV.Gravity.GravitationalConstant"
permalink: /verify/taulib/docs/book-v-gravity-gravitational-constant/
lane: verify
module_name: "TauLib.BookV.Gravity.GravitationalConstant"
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

# TauLib.BookV.Gravity.GravitationalConstant


The gravitational constant G_τ derived from torus vacuum geometry.

## Registry Cross-References


- [V.D01] Torus Vacuum — `TorusVacuum`

- [V.D02] Gravitational Constant — `GravConstant`

- [V.T01] Vacuum Shape Ratio — `vacuum_shape_ratio_holds`

- [V.P01] G_τ well-defined — structural remark


## Mathematical Content


### Torus Vacuum Shape Ratio


Every mature black hole state is a stabilized torus vacuum with a fixed
shape ratio:

```
r_n(x) / R_n(x) = ι<sub>τ</sub> ∀ mature BH states x
```


where r_n(x) is the minor radius index and R_n(x) is the major radius index.

This ratio is **fixed by refinement coherence** beyond the maturity horizon:
ι<sub>τ</sub> is the canonical shape invariant of the mature torus vacuum.
Only the scale degree of freedom (R) remains as free parameter.

### Gravitational Constant G_τ


G_τ is defined from the minimal mature BH state:

```
G_τ := R_n(x_min) / (2 · M_n(x_min))
```


where x_min is the minimal mature BH state. This is well-defined by
refinement coherence: both R_n and M_n are readouts of a single
surviving scale parameter on the stabilized torus.

The linear coupling R = 2G_τM is the canonical invariance structure
from the τ-kernel (Schwarzschild theorem, see Schwarzschild.lean).

### Physical Interpretation


- G_τ is the τ-derived gravitational constant

- In orthodox physics: G = (c³/ℏ) · ι<sub>τ</sub>² (from sector self-coupling)

- The gravity sector self-coupling κ(D;1) = 1−ι<sub>τ</sub> determines the
gravitational coupling strength


## Ground Truth Sources


- gravity-einstein.json: torus-vacuum-shape-ratio, gravitational-constant

- holonomy-sectors.json: gr-sector-coupling


---

### `Tau.BookV.Gravity.TorusVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L64-L91)
**structure
Tau.BookV.Gravity.TorusVacuum :Type**


[V.D01] Torus vacuum: the stabilized torus configuration of a
mature black hole state.

The shape ratio r/R = ι<sub>τ</sub> is fixed by refinement coherence:


- r = minor radius index (fiber dimension)

- R = major radius index (base dimension)

- Only scale (R) remains as free parameter


The BH topology is a 2-torus T² (NOT a 3-ball). This is the
unique stabilized topology from τ-NF convergence.

- minor_numer : ℕ
Minor radius index numerator (r).

- minor_denom : ℕ
Minor radius index denominator.

- major_numer : ℕ
Major radius index numerator (R).

- major_denom : ℕ
Major radius index denominator.

- minor_denom_pos : self.minor_denom > 0
Both denominators positive.

- major_denom_pos : self.major_denom > 0
- major_positive : self.major_numer > 0
Major radius positive (physical).

- shape_ratio : self.minor_numer * self.major_denom * BookIV.Sectors.iotaD = BookIV.Sectors.iota * self.minor_denom * self.major_numer
Shape ratio r/R = ι<sub>τ</sub> = iota/iotaD (cross-multiplied).

Instances For

---

### `Tau.BookV.Gravity.instReprTorusVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L91-L91)
**instance
Tau.BookV.Gravity.instReprTorusVacuum :Repr TorusVacuum**

Equations
- Tau.BookV.Gravity.instReprTorusVacuum = { reprPrec := Tau.BookV.Gravity.instReprTorusVacuum.repr }

---

### `Tau.BookV.Gravity.instReprTorusVacuum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L91-L91)
**def
Tau.BookV.Gravity.instReprTorusVacuum.repr :TorusVacuum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.TorusVacuum.minorFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L93-L95)
**def
Tau.BookV.Gravity.TorusVacuum.minorFloat
(v : TorusVacuum)
 :Float**


Minor radius as Float.
Equations
- v.minorFloat = Float.ofNat v.minor_numer / Float.ofNat v.minor_denom
Instances For

---

### `Tau.BookV.Gravity.TorusVacuum.majorFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L97-L99)
**def
Tau.BookV.Gravity.TorusVacuum.majorFloat
(v : TorusVacuum)
 :Float**


Major radius as Float.
Equations
- v.majorFloat = Float.ofNat v.major_numer / Float.ofNat v.major_denom
Instances For

---

### `Tau.BookV.Gravity.TorusVacuum.ratioFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L101-L103)
**def
Tau.BookV.Gravity.TorusVacuum.ratioFloat
(v : TorusVacuum)
 :Float**


Shape ratio r/R as Float (should be ≈ 0.341304).
Equations
- v.ratioFloat = v.minorFloat / v.majorFloat
Instances For

---

### `Tau.BookV.Gravity.unit_torus_vacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L109-L119)
**def
Tau.BookV.Gravity.unit_torus_vacuum :TorusVacuum**


Example torus vacuum with r = ι<sub>τ</sub>, R = 1 (unit major radius).
Shape ratio: ι<sub>τ</sub>/1 = ι<sub>τ</sub>.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.GravConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L125-L147)
**structure
Tau.BookV.Gravity.GravConstant :Type**


[V.D02] Gravitational constant G_τ.

Defined from the minimal mature BH state:
G_τ := R_min / (2 · M_min)

Both R and M are readouts of a single surviving scale parameter
on the stabilized torus vacuum. The factor of 2 comes from the
canonical Schwarzschild form.

Properties:


- Well-defined by refinement coherence beyond maturity horizon

- G_τ > 0 (positive gravitational coupling)

- In orthodox units: G = (c³/ℏ) · ι<sub>τ</sub>² (sector self-coupling readout)


- g_numer : ℕ
G_τ numerator.

- g_denom : ℕ
G_τ denominator.

- denom_pos : self.g_denom > 0
Denominator positive.

- g_positive : self.g_numer > 0
G_τ is positive (gravitational attraction).

Instances For

---

### `Tau.BookV.Gravity.instReprGravConstant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L147-L147)
**def
Tau.BookV.Gravity.instReprGravConstant.repr :GravConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprGravConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L147-L147)
**instance
Tau.BookV.Gravity.instReprGravConstant :Repr GravConstant**

Equations
- Tau.BookV.Gravity.instReprGravConstant = { reprPrec := Tau.BookV.Gravity.instReprGravConstant.repr }

---

### `Tau.BookV.Gravity.GravConstant.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L149-L151)
**def
Tau.BookV.Gravity.GravConstant.toFloat
(g : GravConstant)
 :Float**


Float display for gravitational constant.
Equations
- g.toFloat = Float.ofNat g.g_numer / Float.ofNat g.g_denom
Instances For

---

### `Tau.BookV.Gravity.g_tau_iota_factor_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L157-L160)
**def
Tau.BookV.Gravity.g_tau_iota_factor_numer :ℕ**


G_τ is proportional to ι<sub>τ</sub>² (from the gravity sector self-coupling).
In orthodox units: G = (c³/ℏ) · ι<sub>τ</sub>².
Here we record the ι<sub>τ</sub>² factor as the structural core.
Equations
- Tau.BookV.Gravity.g_tau_iota_factor_numer = Tau.BookIV.Sectors.iota_sq_numer
Instances For

---

### `Tau.BookV.Gravity.g_tau_iota_factor_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L161-L161)
**def
Tau.BookV.Gravity.g_tau_iota_factor_denom :ℕ**

Equations
- Tau.BookV.Gravity.g_tau_iota_factor_denom = Tau.BookIV.Sectors.iota_sq_denom
Instances For

---

### `Tau.BookV.Gravity.gravity_self_coupling_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L163-L164)
**def
Tau.BookV.Gravity.gravity_self_coupling_numer :ℕ**


The gravity sector self-coupling κ(D;1) = 1 − ι<sub>τ</sub> connects to G_τ.
Equations
- Tau.BookV.Gravity.gravity_self_coupling_numer = Tau.BookIV.Sectors.iotaD - Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookV.Gravity.gravity_self_coupling_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L165-L165)
**def
Tau.BookV.Gravity.gravity_self_coupling_denom :ℕ**

Equations
- Tau.BookV.Gravity.gravity_self_coupling_denom = Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookV.Gravity.vacuum_shape_ratio_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L171-L176)
**theorem
Tau.BookV.Gravity.vacuum_shape_ratio_holds
(v : TorusVacuum)
 :v.minor_numer * v.major_denom * BookIV.Sectors.iotaD = BookIV.Sectors.iota * v.minor_denom * v.major_numer**


[V.T01] The torus vacuum shape ratio r/R = ι<sub>τ</sub> is encoded
in the shape_ratio field of every TorusVacuum.

---

### `Tau.BookV.Gravity.unit_torus_has_iota_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L178-L182)
**theorem
Tau.BookV.Gravity.unit_torus_has_iota_ratio :unit_torus_vacuum.minor_numer = BookIV.Sectors.iota ∧ unit_torus_vacuum.major_numer = BookIV.Sectors.iotaD**


The unit torus vacuum has shape ratio ι<sub>τ</sub>.

---

### `Tau.BookV.Gravity.g_tau_well_defined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L184-L188)
**theorem
Tau.BookV.Gravity.g_tau_well_defined
(g : GravConstant)
 :g.g_numer > 0 ∧ g.g_denom > 0**


[V.P01] G_τ is well-defined: the gravitational constant structure
requires a positive numerator and denominator.

---

### `Tau.BookV.Gravity.gravity_coupling_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L190-L193)
**theorem
Tau.BookV.Gravity.gravity_coupling_positive :gravity_self_coupling_numer > 0**


The gravity self-coupling is positive (1 − ι<sub>τ</sub> > 0 since ι<sub>τ</sub> < 1).

---

### `Tau.BookV.Gravity.g_tau_factor_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/GravitationalConstant.lean#L195-L198)
**theorem
Tau.BookV.Gravity.g_tau_factor_positive :g_tau_iota_factor_numer > 0**


The ι<sub>τ</sub>² factor for G_τ is positive.
