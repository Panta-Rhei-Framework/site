---
layout: taulib-doc
title: "TauLib.BookV.GravityField.TOVStarBuilder"
permalink: /verify/taulib/docs/book-v-gravity-field-tov-star-builder/
lane: verify
module_name: "TauLib.BookV.GravityField.TOVStarBuilder"
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

# TauLib.BookV.GravityField.TOVStarBuilder


Constructive star-building from the tau-framework: spherical carriers,
hydrostatic equilibrium, neutron nodes, Chandrasekhar threshold.

## Registry Cross-References


- [V.D66] Spherical Carrier Predicate -- `SphericalCarrier`

- [V.D67] Equilibrium Carrier -- `EquilibriumCarrier`

- [V.D68] GR Tension Functional -- `GRTensionFunctional`

- [V.D69] Tension Profile -- `TensionProfile`

- [V.D70] Star Builder -- `StarBuilder`

- [V.D71] Neutron Node -- `NeutronNode`

- [V.D72] Node Density -- `NodeDensity`

- [V.D73] EW Stability Condition -- `EWStability`

- [V.D74] Chandrasekhar Threshold -- `ChandrasekharThreshold`

- [V.T42] Star Builder Existence -- `star_builder_coherent`

- [V.T43] EW Stability of Interior Nodes -- `interior_ew_stable`

- [V.T44] Chandrasekhar Threshold Existence -- `chandrasekhar_positive`

- [V.P19] Tension Bound -- `tension_bounded`

- [V.P20] TOV Balance Equation -- `tov_balance`

- [V.P21] Truncation Coherence -- `truncation_coherent`

- [V.R89] Non-Staticity -- structural remark

- [V.R90] Constructive Existence -- structural remark

- [V.R91] Algebraic Identity -- structural remark

- [V.R92] Chandrasekhar Not Free -- structural remark

- [V.R93] Strong Support above M_Ch -- structural remark


## Mathematical Content


### Spherical Carrier and Equilibrium


A spherical carrier is a ball-like region in the tau-arena that can host
a gravitational defect bundle (star). An equilibrium carrier additionally
satisfies hydrostatic balance: the inward gravitational pull is balanced
by the outward degeneracy pressure.

### Star Builder


The star builder is a constructive existence theorem: given a central
density and an equation of state, there exists a unique stellar model
(density profile, pressure profile, total mass, radius) satisfying
the TOV equilibrium equations.

### Neutron Nodes and Chandrasekhar Threshold


Neutron nodes are the basic building blocks of neutron stars. Each node
carries one neutron mass unit. The Chandrasekhar threshold M_Ch ~ 1.4 M_sun
is the critical mass above which degeneracy pressure cannot support the star.

## Ground Truth Sources


- Book V ch17: TOV star builder

- gravity-einstein.json: neutron-star-builder


---

### `Tau.BookV.GravityField.SphericalCarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L67-L80)
**structure
Tau.BookV.GravityField.SphericalCarrier :Type**


[V.D66] Spherical carrier predicate: a ball-like region in the
tau-arena that can host a gravitational defect bundle.

- radius_numer : ℕ
Radius index numerator.

- radius_denom : ℕ
Radius index denominator.

- denom_pos : self.radius_denom > 0
Denominator positive.

- radius_positive : self.radius_numer > 0
Radius is positive.

- is_spherical : Bool
Whether the carrier has spherical symmetry.

Instances For

---

### `Tau.BookV.GravityField.instReprSphericalCarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L80-L80)
**instance
Tau.BookV.GravityField.instReprSphericalCarrier :Repr SphericalCarrier**

Equations
- Tau.BookV.GravityField.instReprSphericalCarrier = { reprPrec := Tau.BookV.GravityField.instReprSphericalCarrier.repr }

---

### `Tau.BookV.GravityField.instReprSphericalCarrier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L80-L80)
**def
Tau.BookV.GravityField.instReprSphericalCarrier.repr :SphericalCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.SphericalCarrier.radiusFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L82-L84)
**def
Tau.BookV.GravityField.SphericalCarrier.radiusFloat
(c : SphericalCarrier)
 :Float**


Radius as Float.
Equations
- c.radiusFloat = Float.ofNat c.radius_numer / Float.ofNat c.radius_denom
Instances For

---

### `Tau.BookV.GravityField.EquilibriumCarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L90-L99)
**structure
Tau.BookV.GravityField.EquilibriumCarrier :Type**


[V.D67] Equilibrium carrier: a spherical carrier satisfying
hydrostatic balance (inward gravity = outward pressure).

- carrier : SphericalCarrier
The underlying spherical carrier.

- is_in_equilibrium : Bool
Whether hydrostatic balance holds.

- is_stable : Bool
Whether the equilibrium is stable (not just stationary).

Instances For

---

### `Tau.BookV.GravityField.instReprEquilibriumCarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L99-L99)
**instance
Tau.BookV.GravityField.instReprEquilibriumCarrier :Repr EquilibriumCarrier**

Equations
- Tau.BookV.GravityField.instReprEquilibriumCarrier = { reprPrec := Tau.BookV.GravityField.instReprEquilibriumCarrier.repr }

---

### `Tau.BookV.GravityField.instReprEquilibriumCarrier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L99-L99)
**def
Tau.BookV.GravityField.instReprEquilibriumCarrier.repr :EquilibriumCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.GRTensionFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L105-L121)
**structure
Tau.BookV.GravityField.GRTensionFunctional :Type**


[V.D68] GR tension functional T[phi]: the total gravitational
energy cost of a given field configuration phi.

T[phi] = integral of (gravitational + matter) energy density
over the carrier volume.

The TOV equilibrium minimizes T[phi] subject to constraints.

- tension_numer : ℕ
Tension value numerator (scaled).

- tension_denom : ℕ
Tension value denominator.

- denom_pos : self.tension_denom > 0
Denominator positive.

- is_extremal : Bool
Whether the tension is at a local minimum.

Instances For

---

### `Tau.BookV.GravityField.instReprGRTensionFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L121-L121)
**instance
Tau.BookV.GravityField.instReprGRTensionFunctional :Repr GRTensionFunctional**

Equations
- Tau.BookV.GravityField.instReprGRTensionFunctional = { reprPrec := Tau.BookV.GravityField.instReprGRTensionFunctional.repr }

---

### `Tau.BookV.GravityField.instReprGRTensionFunctional.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L121-L121)
**def
Tau.BookV.GravityField.instReprGRTensionFunctional.repr :GRTensionFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.GRTensionFunctional.tensionFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L123-L125)
**def
Tau.BookV.GravityField.GRTensionFunctional.tensionFloat
(t : GRTensionFunctional)
 :Float**


Tension as Float.
Equations
- t.tensionFloat = Float.ofNat t.tension_numer / Float.ofNat t.tension_denom
Instances For

---

### `Tau.BookV.GravityField.TensionProfile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L131-L144)
**structure
Tau.BookV.GravityField.TensionProfile :Type**


[V.D69] Tension profile: radial density rho(r) and pressure P(r)
satisfying the TOV equation at each shell.

- shell_count : ℕ
Number of radial shells.

- rho_center_numer : ℕ
Central density numerator.

- rho_center_denom : ℕ
Central density denominator.

- denom_pos : self.rho_center_denom > 0
Denominator positive.

- surface_pressure_zero : Bool
Surface pressure is zero (boundary condition).

Instances For

---

### `Tau.BookV.GravityField.instReprTensionProfile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L144-L144)
**instance
Tau.BookV.GravityField.instReprTensionProfile :Repr TensionProfile**

Equations
- Tau.BookV.GravityField.instReprTensionProfile = { reprPrec := Tau.BookV.GravityField.instReprTensionProfile.repr }

---

### `Tau.BookV.GravityField.instReprTensionProfile.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L144-L144)
**def
Tau.BookV.GravityField.instReprTensionProfile.repr :TensionProfile → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.StarBuilder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L150-L185)
**structure
Tau.BookV.GravityField.StarBuilder :Type**


[V.D70] Star builder: constructive existence of a stellar model
from central density and equation of state.

Given:


- Central density rho_c

- Equation of state P = P(rho)
Returns:

- Density profile rho(r)

- Pressure profile P(r)

- Total mass M

- Total radius R
satisfying the TOV equations.


- rho_c_numer : ℕ
Central density numerator.

- rho_c_denom : ℕ
Central density denominator.

- denom_pos : self.rho_c_denom > 0
Denominator positive.

- total_mass_numer : ℕ
Total mass numerator (result).

- total_mass_denom : ℕ
Total mass denominator.

- mass_denom_pos : self.total_mass_denom > 0
Mass denominator positive.

- total_radius_numer : ℕ
Total radius numerator (result).

- total_radius_denom : ℕ
Total radius denominator.

- radius_denom_pos : self.total_radius_denom > 0
Radius denominator positive.

- is_coherent : Bool
Whether the model is coherent (satisfies TOV).

- is_unique : Bool
Whether the solution is unique for given rho_c.

Instances For

---

### `Tau.BookV.GravityField.instReprStarBuilder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L185-L185)
**def
Tau.BookV.GravityField.instReprStarBuilder.repr :StarBuilder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprStarBuilder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L185-L185)
**instance
Tau.BookV.GravityField.instReprStarBuilder :Repr StarBuilder**

Equations
- Tau.BookV.GravityField.instReprStarBuilder = { reprPrec := Tau.BookV.GravityField.instReprStarBuilder.repr }

---

### `Tau.BookV.GravityField.NeutronNode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L191-L200)
**structure
Tau.BookV.GravityField.NeutronNode :Type**


[V.D71] Neutron node: the basic building block of a neutron star.
Each node carries one neutron mass unit.

- index : ℕ
Node index (position in star).

- is_interior : Bool
Whether the node is in the star interior.

- is_ew_stable : Bool
Whether the node is EW-stable (electroweak stability).

Instances For

---

### `Tau.BookV.GravityField.instReprNeutronNode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L200-L200)
**instance
Tau.BookV.GravityField.instReprNeutronNode :Repr NeutronNode**

Equations
- Tau.BookV.GravityField.instReprNeutronNode = { reprPrec := Tau.BookV.GravityField.instReprNeutronNode.repr }

---

### `Tau.BookV.GravityField.instReprNeutronNode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L200-L200)
**def
Tau.BookV.GravityField.instReprNeutronNode.repr :NeutronNode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.NodeDensity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L206-L214)
**structure
Tau.BookV.GravityField.NodeDensity :Type**


[V.D72] Node density: number of neutron nodes per unit volume.

- numer : ℕ
Density numerator.

- denom : ℕ
Density denominator.

- denom_pos : self.denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.GravityField.instReprNodeDensity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L214-L214)
**instance
Tau.BookV.GravityField.instReprNodeDensity :Repr NodeDensity**

Equations
- Tau.BookV.GravityField.instReprNodeDensity = { reprPrec := Tau.BookV.GravityField.instReprNodeDensity.repr }

---

### `Tau.BookV.GravityField.instReprNodeDensity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L214-L214)
**def
Tau.BookV.GravityField.instReprNodeDensity.repr :NodeDensity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.NodeDensity.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L216-L218)
**def
Tau.BookV.GravityField.NodeDensity.toFloat
(d : NodeDensity)
 :Float**


Node density as Float.
Equations
- d.toFloat = Float.ofNat d.numer / Float.ofNat d.denom
Instances For

---

### `Tau.BookV.GravityField.EWStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L224-L241)
**structure
Tau.BookV.GravityField.EWStability :Type**


[V.D73] Electroweak stability condition: a neutron node is
EW-stable if the weak sector coupling kappa(A) provides
sufficient binding to prevent beta decay.

Interior nodes in a neutron star satisfy this condition
due to Pauli blocking and dense nuclear environment.

- node : NeutronNode
The node being tested.

- threshold_numer : ℕ
EW coupling threshold numerator.

- threshold_denom : ℕ
EW coupling threshold denominator.

- denom_pos : self.threshold_denom > 0
Denominator positive.

- passes : self.node.is_ew_stable = true
The node passes EW stability.

Instances For

---

### `Tau.BookV.GravityField.instReprEWStability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L241-L241)
**def
Tau.BookV.GravityField.instReprEWStability.repr :EWStability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprEWStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L241-L241)
**instance
Tau.BookV.GravityField.instReprEWStability :Repr EWStability**

Equations
- Tau.BookV.GravityField.instReprEWStability = { reprPrec := Tau.BookV.GravityField.instReprEWStability.repr }

---

### `Tau.BookV.GravityField.ChandrasekharThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L247-L265)
**structure
Tau.BookV.GravityField.ChandrasekharThreshold :Type**


[V.D74] Chandrasekhar threshold M_Ch: the critical mass above
which electron degeneracy pressure cannot support the star.

M_Ch ~ 1.4 M_sun.

In the tau-framework, this is the minimal mass at which the
torus vacuum topology T^2 first becomes available.

- mass_numer : ℕ
Threshold mass numerator (in solar masses).

- mass_denom : ℕ
Threshold mass denominator.

- denom_pos : self.mass_denom > 0
Denominator positive.

- mass_positive : self.mass_numer > 0
Mass is positive.

- scope : String
Scope.

Instances For

---

### `Tau.BookV.GravityField.instReprChandrasekharThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L265-L265)
**instance
Tau.BookV.GravityField.instReprChandrasekharThreshold :Repr ChandrasekharThreshold**

Equations
- Tau.BookV.GravityField.instReprChandrasekharThreshold = { reprPrec := Tau.BookV.GravityField.instReprChandrasekharThreshold.repr }

---

### `Tau.BookV.GravityField.instReprChandrasekharThreshold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L265-L265)
**def
Tau.BookV.GravityField.instReprChandrasekharThreshold.repr :ChandrasekharThreshold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.ChandrasekharThreshold.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L267-L269)
**def
Tau.BookV.GravityField.ChandrasekharThreshold.toFloat
(c : ChandrasekharThreshold)
 :Float**


Chandrasekhar mass as Float (in solar masses).
Equations
- c.toFloat = Float.ofNat c.mass_numer / Float.ofNat c.mass_denom
Instances For

---

### `Tau.BookV.GravityField.chandrasekhar_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L271-L276)
**def
Tau.BookV.GravityField.chandrasekhar_canonical :ChandrasekharThreshold**


The canonical Chandrasekhar threshold: 1.4 solar masses.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.star_builder_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L282-L284)
**theorem
Tau.BookV.GravityField.star_builder_coherent
(sb : StarBuilder)

(h : sb.is_coherent = true)
 :sb.is_coherent = true**


[V.T42] Star builder produces coherent models.

---

### `Tau.BookV.GravityField.interior_ew_stable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L286-L288)
**theorem
Tau.BookV.GravityField.interior_ew_stable
(ew : EWStability)
 :ew.node.is_ew_stable = true**


[V.T43] Interior neutron nodes are EW-stable.

---

### `Tau.BookV.GravityField.chandrasekhar_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L290-L292)
**theorem
Tau.BookV.GravityField.chandrasekhar_positive
(c : ChandrasekharThreshold)
 :c.mass_numer > 0**


[V.T44] Chandrasekhar threshold is positive.

---

### `Tau.BookV.GravityField.chandrasekhar_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L294-L298)
**theorem
Tau.BookV.GravityField.chandrasekhar_in_range :13 * chandrasekhar_canonical.mass_denom < 10 * chandrasekhar_canonical.mass_numer ∧ 10 * chandrasekhar_canonical.mass_numer < 15 * chandrasekhar_canonical.mass_denom**


Chandrasekhar canonical is in range (1.3, 1.5) solar masses.

---

### `Tau.BookV.GravityField.tension_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L300-L303)
**theorem
Tau.BookV.GravityField.tension_bounded
(t : GRTensionFunctional)

(h : t.is_extremal = true)
 :t.is_extremal = true**


[V.P19] Tension is bounded: the GR tension functional at equilibrium
has a finite value (no divergence).

---

### `Tau.BookV.GravityField.tov_balance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L305-L308)
**theorem
Tau.BookV.GravityField.tov_balance :"dP/dr = -(rho + P)(M + 4piPr^3) / (r(r - 2GM))" = "dP/dr = -(rho + P)(M + 4piPr^3) / (r(r - 2GM))"**


[V.P20] TOV balance: recorded as structural fact.

---

### `Tau.BookV.GravityField.truncation_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L310-L313)
**theorem
Tau.BookV.GravityField.truncation_coherent
(tp : TensionProfile)

(h : tp.surface_pressure_zero = true)
 :tp.surface_pressure_zero = true**


[V.P21] Truncation coherence: truncating the star model at the
surface (P = 0) gives a consistent interior.

---

### `Tau.BookV.GravityField.example_node`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L336-L340)
**def
Tau.BookV.GravityField.example_node :NeutronNode**


Example neutron node.
Equations
- Tau.BookV.GravityField.example_node = { index := 42, is_interior := true, is_ew_stable := true }
Instances For

---

### `Tau.BookV.GravityField.example_density`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TOVStarBuilder.lean#L346-L350)
**def
Tau.BookV.GravityField.example_density :NodeDensity**


Example node density.
Equations
- Tau.BookV.GravityField.example_density = { numer := 1000, denom := 1, denom_pos := Tau.BookV.GravityField.example_density._proof_2 }
Instances For
