---
layout: taulib-doc
title: "TauLib.BookV.Gravity.EinsteinEquation"
permalink: /verify/taulib/docs/book-v-gravity-einstein-equation/
lane: verify
module_name: "TauLib.BookV.Gravity.EinsteinEquation"
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

# TauLib.BookV.Gravity.EinsteinEquation


The tau-Einstein equation as boundary-character identity.

## Registry Cross-References


- [V.D03] Matter Character — `MatterCharacter`

- [V.D04] Curvature Character — `CurvatureCharacter`

- [V.D05] GR Coupling — `GRCoupling`

- [V.D06] Tau-Einstein Equation — `TauEinstein`

- [V.T02] κ_τ uniqueness — `kappa_unique`

- [V.R01] Einstein as boundary identity — structural remark


## Mathematical Content


### Tau-Einstein Equation


The central equation of τ-gravity is a **boundary-character identity**:

```
G_ω(x) = κ_τ · T^mat_ω(x) in H_∂[ω]
```


This is NOT a nonlinear PDE but an algebraic identity in the boundary
holonomy algebra.

### Matter Character


T^mat_n(x) := η_n(T^EM_n(x) ⊕ T^wk_n(x) ⊕ T^s_n(x))

= direct sum of EM, weak, and strong sector boundary projections
embedded into H_∂[n]. Forms truncation-coherent ω-germ.

### Curvature Character


G_n(x) := η_n(T^GR_n(x))

where T^GR_n(x) = minimal GR budget = smallest α-Idx value t such that
∃ GR-frame holonomy witness ∇_n(x;t).

### GR Coupling κ_τ


κ_τ is the **unique unpolarized coupling** (σ-fixed, crossing-point mediator):


- Uniqueness by field cancellation: any two couplings agree at x* with T^mat ≠ 0

- κ_τ is σ-equivariant (unpolarized)

- Equality holds as boundary-character identity


### Orthodox Shadow


Via the chart readout homomorphism Φ_p : H_∂[ω] → Jet_p[ω]:

```
G_ω = κ_τ · T^mat → G_μν = (8πG/c⁴) T_μν
```


The orthodox Einstein field equations are the chart-projected shadow
of the tau-Einstein boundary identity.

### Conservation (Tau-Bianchi)


∇ · G = ∇ · (κ_τ · T^mat) as a COROLLARY (not extra axiom).
Backreaction is automatic: matter modifies admissible transport and defect cost.
Geometry is never "bent" — holonomy defects and admissibility change, not metric.

## Ground Truth Sources


- gravity-einstein.json: tau-einstein-equation, matter-character, curvature-character

- gravity-einstein.json: chart-readout-homomorphism, tau-bianchi


---

### `Tau.BookV.Gravity.MatterCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L78-L97)
**structure
Tau.BookV.Gravity.MatterCharacter :Type**


[V.D03] Matter character T^mat: the direct sum of EM, Weak, and
Strong sector boundary projections.

T^mat_n(x) = η_n(T^EM_n(x) ⊕ T^wk_n(x) ⊕ T^s_n(x))

The matter character includes exactly the three spatial sectors
(B, A, C) but NOT gravity (D). Gravity appears on the LHS
of the Einstein equation as curvature.

- em_numer : ℕ
EM sector contribution T^EM (B-sector).

- weak_numer : ℕ
Weak sector contribution T^wk (A-sector).

- strong_numer : ℕ
Strong sector contribution T^s (C-sector).

- denom : ℕ
Common denominator for all three.

- denom_pos : self.denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Gravity.instReprMatterCharacter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L97-L97)
**def
Tau.BookV.Gravity.instReprMatterCharacter.repr :MatterCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprMatterCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L97-L97)
**instance
Tau.BookV.Gravity.instReprMatterCharacter :Repr MatterCharacter**

Equations
- Tau.BookV.Gravity.instReprMatterCharacter = { reprPrec := Tau.BookV.Gravity.instReprMatterCharacter.repr }

---

### `Tau.BookV.Gravity.MatterCharacter.total_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L99-L101)
**def
Tau.BookV.Gravity.MatterCharacter.total_numer
(m : MatterCharacter)
 :ℕ**


Total matter character as sum of three sectors.
Equations
- m.total_numer = m.em_numer + m.weak_numer + m.strong_numer
Instances For

---

### `Tau.BookV.Gravity.MatterCharacter.totalFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L103-L105)
**def
Tau.BookV.Gravity.MatterCharacter.totalFloat
(m : MatterCharacter)
 :Float**


Matter character total as Float.
Equations
- m.totalFloat = Float.ofNat m.total_numer / Float.ofNat m.denom
Instances For

---

### `Tau.BookV.Gravity.CurvatureCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L111-L126)
**structure
Tau.BookV.Gravity.CurvatureCharacter :Type**


[V.D04] Curvature character G: the GR-sector boundary projection.

G_n(x) = η_n(T^GR_n(x))

where T^GR_n(x) = minimal GR budget = smallest α-Idx value t
such that ∃ GR-frame holonomy witness ∇_n(x;t).

This is the curvature-side of the Einstein equation.

- numer : ℕ
Curvature numerator (GR-sector boundary projection).

- denom : ℕ
Curvature denominator.

- denom_pos : self.denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Gravity.instReprCurvatureCharacter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L126-L126)
**def
Tau.BookV.Gravity.instReprCurvatureCharacter.repr :CurvatureCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprCurvatureCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L126-L126)
**instance
Tau.BookV.Gravity.instReprCurvatureCharacter :Repr CurvatureCharacter**

Equations
- Tau.BookV.Gravity.instReprCurvatureCharacter = { reprPrec := Tau.BookV.Gravity.instReprCurvatureCharacter.repr }

---

### `Tau.BookV.Gravity.CurvatureCharacter.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L128-L130)
**def
Tau.BookV.Gravity.CurvatureCharacter.toFloat
(c : CurvatureCharacter)
 :Float**


Curvature character as Float.
Equations
- c.toFloat = Float.ofNat c.numer / Float.ofNat c.denom
Instances For

---

### `Tau.BookV.Gravity.GRCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L136-L158)
**structure
Tau.BookV.Gravity.GRCoupling :Type**


[V.D05] GR coupling κ_τ: the unique unpolarized coupling constant
in the tau-Einstein equation.

Properties:


- σ-fixed (unpolarized, crossing-point mediator)

- Unique by field cancellation at canonical carrier x*

- Determined entirely by ι<sub>τ</sub> (No Knobs)


The gravity sector self-coupling κ(D;1) = 1 − ι<sub>τ</sub> is the
sector-level expression. The Einstein coupling κ_τ relates
curvature to total matter character.

- kappa_numer : ℕ
κ_τ numerator.

- kappa_denom : ℕ
κ_τ denominator.

- denom_pos : self.kappa_denom > 0
Denominator positive.

- sigma_fixed : Bool
κ_τ is σ-fixed (unpolarized).

- is_unique : Bool
κ_τ is unique (no other coupling satisfies the universal property).

Instances For

---

### `Tau.BookV.Gravity.instReprGRCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L158-L158)
**def
Tau.BookV.Gravity.instReprGRCoupling.repr :GRCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprGRCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L158-L158)
**instance
Tau.BookV.Gravity.instReprGRCoupling :Repr GRCoupling**

Equations
- Tau.BookV.Gravity.instReprGRCoupling = { reprPrec := Tau.BookV.Gravity.instReprGRCoupling.repr }

---

### `Tau.BookV.Gravity.GRCoupling.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L160-L162)
**def
Tau.BookV.Gravity.GRCoupling.toFloat
(g : GRCoupling)
 :Float**


Float display for GR coupling.
Equations
- g.toFloat = Float.ofNat g.kappa_numer / Float.ofNat g.kappa_denom
Instances For

---

### `Tau.BookV.Gravity.canonical_gr_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L168-L173)
**def
Tau.BookV.Gravity.canonical_gr_coupling :GRCoupling**


The canonical GR coupling: κ_τ = κ(D;1) = 1 − ι<sub>τ</sub>.
This is the gravity sector self-coupling from Book IV Part I.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.TauEinstein`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L179-L205)
**structure
Tau.BookV.Gravity.TauEinstein :Type**


[V.D06] Tau-Einstein equation: G_ω(x) = κ_τ · T^mat_ω(x).

This is a **boundary-character identity** in H_∂[ω], NOT a
nonlinear PDE. It states that the curvature character equals
the GR coupling times the matter character.

Key distinctions from orthodox GR:

- Algebraic identity, not differential equation

- Boundary determines interior (Hartogs principle)

- Unique solution by τ-NF minimization (no gauge freedom)

- Backreaction automatic (not extra axiom)


The structural relation (cross-multiplied):
curvature_numer · kappa_denom · matter_denom =
kappa_numer · matter_total · curvature_denom

- kappa : GRCoupling
The GR coupling constant κ_τ.

- matter : MatterCharacter
The matter character T^mat (3 sector contributions).

- curvature : CurvatureCharacter
The curvature character G.

- einstein_identity : self.curvature.numer * self.kappa.kappa_denom * self.matter.denom = self.kappa.kappa_numer * self.matter.total_numer * self.curvature.denom
The Einstein identity: G = κ_τ · T^mat (cross-multiplied).

Instances For

---

### `Tau.BookV.Gravity.instReprTauEinstein.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L205-L205)
**def
Tau.BookV.Gravity.instReprTauEinstein.repr :TauEinstein → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprTauEinstein`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L205-L205)
**instance
Tau.BookV.Gravity.instReprTauEinstein :Repr TauEinstein**

Equations
- Tau.BookV.Gravity.instReprTauEinstein = { reprPrec := Tau.BookV.Gravity.instReprTauEinstein.repr }

---

### `Tau.BookV.Gravity.TauBianchi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L211-L226)
**structure
Tau.BookV.Gravity.TauBianchi :Type**


[V.R01] Conservation is a COROLLARY of the tau-Einstein identity,
NOT an extra axiom.

∇ · G = ∇ · (κ_τ · T^mat)

No admissible refinement can change matter-character without
compensating curvature change. Backreaction is automatic.

This structure records the conservation principle for a given
Einstein system.

- einstein : TauEinstein
The underlying Einstein system.

- is_derived : Bool
Conservation is derived (not postulated).

Instances For

---

### `Tau.BookV.Gravity.instReprTauBianchi.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L226-L226)
**def
Tau.BookV.Gravity.instReprTauBianchi.repr :TauBianchi → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprTauBianchi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L226-L226)
**instance
Tau.BookV.Gravity.instReprTauBianchi :Repr TauBianchi**

Equations
- Tau.BookV.Gravity.instReprTauBianchi = { reprPrec := Tau.BookV.Gravity.instReprTauBianchi.repr }

---

### `Tau.BookV.Gravity.kappa_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L232-L235)
**theorem
Tau.BookV.Gravity.kappa_unique
(g : GRCoupling)

(h : g.is_unique = true)
 :g.is_unique = true**


[V.T02] κ_τ is unique: encoded as a field constraint.
Any GRCoupling with is_unique = true satisfies uniqueness.

---

### `Tau.BookV.Gravity.kappa_sigma_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L237-L239)
**theorem
Tau.BookV.Gravity.kappa_sigma_fixed :canonical_gr_coupling.sigma_fixed = true**


κ_τ is σ-fixed (unpolarized).

---

### `Tau.BookV.Gravity.kappa_is_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L241-L243)
**theorem
Tau.BookV.Gravity.kappa_is_unique :canonical_gr_coupling.is_unique = true**


κ_τ is unique.

---

### `Tau.BookV.Gravity.matter_three_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L245-L249)
**theorem
Tau.BookV.Gravity.matter_three_sectors
(m : MatterCharacter)
 :m.total_numer = m.em_numer + m.weak_numer + m.strong_numer**


The matter character has exactly 3 sector components (EM, Weak, Strong).
Gravity (D) is NOT part of the matter character — it appears
on the curvature side.

---

### `Tau.BookV.Gravity.canonical_coupling_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L251-L255)
**theorem
Tau.BookV.Gravity.canonical_coupling_value :canonical_gr_coupling.kappa_numer = BookIV.Sectors.iotaD - BookIV.Sectors.iota ∧ canonical_gr_coupling.kappa_denom = BookIV.Sectors.iotaD**


The canonical GR coupling uses the gravity self-coupling value.

---

### `Tau.BookV.Gravity.bianchi_is_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/EinsteinEquation.lean#L257-L259)
**theorem
Tau.BookV.Gravity.bianchi_is_derived
(b : TauBianchi)
 :b.is_derived = true → b.is_derived = true**


Conservation in the tau-Bianchi is derived, not postulated.
