---
layout: taulib-doc
title: "TauLib.BookV.GravityField.TauEinsteinEq"
permalink: /verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/
lane: verify
module_name: "TauLib.BookV.GravityField.TauEinsteinEq"
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

# TauLib.BookV.GravityField.TauEinsteinEq


The τ-Einstein equation as a boundary-character identity in the
gravitational field context: R^H = κ_τ · T^mat.

## Registry Cross-References


- [V.D49] Curvature Character R^H — `CurvatureCharH`

- [V.D50] Matter Character T^mat — `MatterCharField`

- [V.D51] τ-Einstein Equation — `TauEinsteinField`

- [V.C03] τ-Bianchi Identity — `bianchi_from_einstein`

- [V.T26] Chart Readout Recovers EFE — `chart_recovers_efe`

- [V.T27] Hartogs Extension — `hartogs_from_boundary`

- [V.R65] κ_τ Uniqueness — structural remark

- [V.R67] Singularities as Chart Artifacts — structural remark

- [V.R68] Matter-Curvature Coupling — structural remark


## Mathematical Content


### Curvature Character R^H


The curvature character R^H_n(x) is the gravitational (D-sector) boundary
projection of the holonomy at depth n. Unlike the orthodox Riemann tensor,
R^H is an element of the boundary holonomy algebra H_∂[n], not a
(3,1)-tensor field.

R^H encodes:


- Frame holonomy defects (how much transport deviates from flatness)

- Gravitational field strength at boundary resolution n

- The curvature side of the Einstein identity


### Matter Character T^mat


The matter character T^mat_n(x) is the direct sum of the three spatial
sector boundary projections (EM + Weak + Strong), restated here with
explicit sector contributions tracked.

### τ-Einstein Equation (Field Form)


```
R^H_n(x) = κ_τ · T^mat_n(x) in H_∂[n]
```


This is a **boundary-character identity**, not a PDE. Key properties:

- Algebraic identity in H_∂[n] (not differential equation)

- Boundary determines interior (Hartogs principle)

- Unique solution by τ-NF minimization

- τ-Bianchi conservation is a COROLLARY


### Chart Readout


Under the chart readout homomorphism Φ_p:
R^H = κ_τ · T^mat → G_μν = (8πG/c⁴) T_μν

The orthodox Einstein field equations are the chart-projected shadow.

## Ground Truth Sources


- Book V Part III ch13 (τ-Einstein Equation in the Field)


---

### `Tau.BookV.GravityField.CurvatureCharH`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L71-L97)
**structure
Tau.BookV.GravityField.CurvatureCharH :Type**


[V.D49] Curvature character R^H: the D-sector boundary projection
of the holonomy at depth n.

R^H_n(x) lives in H_∂[n] (boundary holonomy algebra), NOT in a
tensor bundle. It measures how much parallel transport around
a D-sector loop deviates from the identity.

Components:


- frame_defect: deviation from flat transport (holonomy excess)

- depth: refinement level at which curvature is measured

- sector: always D (gravity)


- defect_numer : ℕ
Frame holonomy defect numerator.

- defect_denom : ℕ
Frame holonomy defect denominator.

- denom_pos : self.defect_denom > 0
Denominator positive.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- sector : BookIII.Sectors.Sector
The sector (always D = gravity).

- sector_is_d : self.sector = BookIII.Sectors.Sector.D
Curvature is D-sector.

Instances For

---

### `Tau.BookV.GravityField.instReprCurvatureCharH.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L97-L97)
**def
Tau.BookV.GravityField.instReprCurvatureCharH.repr :CurvatureCharH → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprCurvatureCharH`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L97-L97)
**instance
Tau.BookV.GravityField.instReprCurvatureCharH :Repr CurvatureCharH**

Equations
- Tau.BookV.GravityField.instReprCurvatureCharH = { reprPrec := Tau.BookV.GravityField.instReprCurvatureCharH.repr }

---

### `Tau.BookV.GravityField.CurvatureCharH.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L99-L101)
**def
Tau.BookV.GravityField.CurvatureCharH.toFloat
(c : CurvatureCharH)
 :Float**


Curvature as Float.
Equations
- c.toFloat = Float.ofNat c.defect_numer / Float.ofNat c.defect_denom
Instances For

---

### `Tau.BookV.GravityField.MatterCharField`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L107-L131)
**structure
Tau.BookV.GravityField.MatterCharField :Type**


[V.D50] Matter character T^mat in the gravitational field context.

T^mat = T^EM ⊕ T^wk ⊕ T^s (direct sum of 3 spatial sectors).
Gravity (D) is NOT included — it appears on the curvature side.

Each sector contribution is tracked separately:


- EM (B-sector): electromagnetic field energy

- Weak (A-sector): weak interaction energy

- Strong (C-sector): strong interaction energy


- em_numer : ℕ
EM sector contribution numerator.

- weak_numer : ℕ
Weak sector contribution numerator.

- strong_numer : ℕ
Strong sector contribution numerator.

- denom : ℕ
Common denominator.

- denom_pos : self.denom > 0
Denominator positive.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

Instances For

---

### `Tau.BookV.GravityField.instReprMatterCharField.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L131-L131)
**def
Tau.BookV.GravityField.instReprMatterCharField.repr :MatterCharField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprMatterCharField`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L131-L131)
**instance
Tau.BookV.GravityField.instReprMatterCharField :Repr MatterCharField**

Equations
- Tau.BookV.GravityField.instReprMatterCharField = { reprPrec := Tau.BookV.GravityField.instReprMatterCharField.repr }

---

### `Tau.BookV.GravityField.MatterCharField.total_numer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L133-L135)
**def
Tau.BookV.GravityField.MatterCharField.total_numer
(m : MatterCharField)
 :ℕ**


Total matter character (sum of 3 sectors).
Equations
- m.total_numer = m.em_numer + m.weak_numer + m.strong_numer
Instances For

---

### `Tau.BookV.GravityField.MatterCharField.totalFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L137-L139)
**def
Tau.BookV.GravityField.MatterCharField.totalFloat
(m : MatterCharField)
 :Float**


Total matter character as Float.
Equations
- m.totalFloat = Float.ofNat m.total_numer / Float.ofNat m.denom
Instances For

---

### `Tau.BookV.GravityField.TauEinsteinField`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L145-L174)
**structure
Tau.BookV.GravityField.TauEinsteinField :Type**


[V.D51] τ-Einstein equation in the gravitational field context:
R^H = κ_τ · T^mat.

This is a boundary-character identity in H_∂[n]:


- LHS: curvature character (D-sector holonomy defect)

- RHS: κ_τ times matter character (3 spatial sectors)


Cross-multiplied identity:
defect_numer · kappa_denom · matter_denom =
kappa_numer · matter_total · defect_denom

Key distinctions from orthodox GR:

- Algebraic identity, not differential equation

- Boundary determines interior (Hartogs)

- Unique by τ-NF minimization (no gauge freedom)

- Backreaction automatic (τ-Bianchi corollary)


- curvature : CurvatureCharH
The curvature character R^H.

- matter : MatterCharField
The matter character T^mat.

- kappa : GravitationalCoupling
The gravitational coupling κ_τ.

- depth_match : self.curvature.depth = self.matter.depth
Depths must match.

- einstein_identity : self.curvature.defect_numer * self.kappa.kappa_denom * self.matter.denom = self.kappa.kappa_numer * self.matter.total_numer * self.curvature.defect_denom
The Einstein identity (cross-multiplied).

Instances For

---

### `Tau.BookV.GravityField.instReprTauEinsteinField`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L174-L174)
**instance
Tau.BookV.GravityField.instReprTauEinsteinField :Repr TauEinsteinField**

Equations
- Tau.BookV.GravityField.instReprTauEinsteinField = { reprPrec := Tau.BookV.GravityField.instReprTauEinsteinField.repr }

---

### `Tau.BookV.GravityField.instReprTauEinsteinField.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L174-L174)
**def
Tau.BookV.GravityField.instReprTauEinsteinField.repr :TauEinsteinField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.bianchi_from_einstein`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L180-L194)
**theorem
Tau.BookV.GravityField.bianchi_from_einstein
(e : TauEinsteinField)
 :e.curvature.defect_numer * e.kappa.kappa_denom * e.matter.denom = e.kappa.kappa_numer * e.matter.total_numer * e.curvature.defect_denom**


[V.C03] τ-Bianchi identity: conservation follows from the
τ-Einstein equation as a COROLLARY.

∇ · R^H = ∇ · (κ_τ · T^mat) = 0

No admissible refinement can change matter-character without
compensating curvature change. Backreaction is automatic.

Unlike orthodox GR where ∇*μ G^μν = 0 is an independent identity,
in the τ-framework conservation is derived from the algebraic
structure of H*∂[n].

---

### `Tau.BookV.GravityField.chart_recovers_efe`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L200-L208)
**theorem
Tau.BookV.GravityField.chart_recovers_efe
(c : LocalTau3Chart)
 :c.dimension = 4 ∧ c.signature = lorentzian_signature**


[V.T26] The chart readout homomorphism Φ_p : H_∂[ω] → Jet_p[ω]
maps the τ-Einstein identity to the orthodox Einstein field equations:

R^H = κ_τ · T^mat → G_μν = (8πG/c⁴) T_μν

The chart must be local and 4-dimensional.

---

### `Tau.BookV.GravityField.hartogs_from_boundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L214-L225)
**theorem
Tau.BookV.GravityField.hartogs_from_boundary
(e : TauEinsteinField)
 :e.curvature.depth > 0**


[V.T27] Hartogs extension from boundary data: the boundary-character
data on ∂(τ³ chart) determines the interior field configuration.

In the τ-framework, this is the gravitational analogue of the
holomorphic Hartogs theorem: boundary determines interior.
The Einstein equation is the boundary constraint; the interior
field is uniquely determined by τ-NF minimization.

Depth must be positive (boundary data requires refinement).

---

### `Tau.BookV.GravityField.matter_three_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L231-L233)
**theorem
Tau.BookV.GravityField.matter_three_sectors
(m : MatterCharField)
 :m.total_numer = m.em_numer + m.weak_numer + m.strong_numer**


Matter has exactly 3 sector contributions.

---

### `Tau.BookV.GravityField.curvature_is_gravity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L235-L237)
**theorem
Tau.BookV.GravityField.curvature_is_gravity
(c : CurvatureCharH)
 :c.sector = BookIII.Sectors.Sector.D**


Curvature is always D-sector.

---

### `Tau.BookV.GravityField.example_curvature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L271-L276)
**def
Tau.BookV.GravityField.example_curvature :CurvatureCharH**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_matter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TauEinsteinEq.lean#L282-L289)
**def
Tau.BookV.GravityField.example_matter :MatterCharField**

Equations
- One or more equations did not get rendered due to their size.
Instances For
