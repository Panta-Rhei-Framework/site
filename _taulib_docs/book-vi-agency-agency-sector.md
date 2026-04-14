---
layout: taulib-doc
title: "TauLib.BookVI.Agency.AgencySector"
permalink: /verify/taulib/docs/book-vi-agency-agency-sector/
lane: verify
module_name: "TauLib.BookVI.Agency.AgencySector"
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

# TauLib.BookVI.Agency.AgencySector


Agency sector (Part 3): π-sector spatial motility on base.
Archetype: Bacteria. Dominant forces: Navier–Stokes + Poincaré.

## Registry Cross-References


- [VI.D29] Agency Sector — `AgencySectorDef`

- [VI.D30] Spatial Motility Predicate — `SpatialMotilityPredicate`

- [VI.T18] Agency = π-Base Extension — `agency_is_pi_extension`

- [VI.D31] Chemotaxis Functor — `ChemotaxisFunctor`


## Cross-Book Authority


- Book I, Part I: π generator (solenoidal, base circle τ¹)

- Book III, Part VII: Navier–Stokes force (fluid dynamics)

- Book III, Part II: Poincaré force (circulation)


## Ground Truth Sources


- Book VI Chapter 17 (2nd Edition): The Agency Sector

- Book VI Chapter 18 (2nd Edition): Bacteria


---

### `Tau.BookVI.Agency.AgencySectorDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L35-L50)
**structure
Tau.BookVI.Agency.AgencySectorDef :Type**


[VI.D29] Agency Sector: π-sector on base circle τ¹.
Life Loop extended with spatial displacement on base.
Generator: π (solenoidal, Book I Part I).
Dominant forces: Navier–Stokes + Poincaré (Book III, Parts VII, II).

- generator : String
Generator is pi (base).

- is_primitive : Bool
Sector is primitive (single generator).

- archetype : String
Archetype organism.

- dominant_navier_stokes : Bool
Dominant force 1: Navier–Stokes (motility, fluid dynamics).

- dominant_poincare : Bool
Dominant force 2: Poincaré (circulation).

Instances For

---

### `Tau.BookVI.Agency.instReprAgencySectorDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L50-L50)
**instance
Tau.BookVI.Agency.instReprAgencySectorDef :Repr AgencySectorDef**

Equations
- Tau.BookVI.Agency.instReprAgencySectorDef = { reprPrec := Tau.BookVI.Agency.instReprAgencySectorDef.repr }

---

### `Tau.BookVI.Agency.instReprAgencySectorDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L50-L50)
**def
Tau.BookVI.Agency.instReprAgencySectorDef.repr :AgencySectorDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Agency.agency_def`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L52-L52)
**def
Tau.BookVI.Agency.agency_def :AgencySectorDef**

Equations
- Tau.BookVI.Agency.agency_def = { }
Instances For

---

### `Tau.BookVI.Agency.agency_generator_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L54-L57)
**theorem
Tau.BookVI.Agency.agency_generator_match :agency_def.generator = FourPlusOne.agency_sector.generator**


Agency sector matches the FourPlusOne agency_sector definition.

---

### `Tau.BookVI.Agency.SpatialMotilityPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L63-L78)
**structure
Tau.BookVI.Agency.SpatialMotilityPredicate :Type**


[VI.D30] Spatial Motility Predicate: 3 conditions for agency.
(i) Displacement on base τ¹ within one Life Loop cycle
(ii) Displacement is distinction-preserving (carrier boundary intact)
(iii) Energy cost bounded by metabolic budget

- condition_count : ℕ
Number of conditions.

- count_eq : self.condition_count = 3
Exactly 3 conditions.

- base_displacement : Bool
(i) Displacement on base.

- distinction_preserving : Bool
(ii) Distinction-preserving.

- energy_bounded : Bool
(iii) Energy-bounded.

Instances For

---

### `Tau.BookVI.Agency.instReprSpatialMotilityPredicate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L78-L78)
**def
Tau.BookVI.Agency.instReprSpatialMotilityPredicate.repr :SpatialMotilityPredicate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Agency.instReprSpatialMotilityPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L78-L78)
**instance
Tau.BookVI.Agency.instReprSpatialMotilityPredicate :Repr SpatialMotilityPredicate**

Equations
- Tau.BookVI.Agency.instReprSpatialMotilityPredicate = { reprPrec := Tau.BookVI.Agency.instReprSpatialMotilityPredicate.repr }

---

### `Tau.BookVI.Agency.spatial_motility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L80-L82)
**def
Tau.BookVI.Agency.spatial_motility :SpatialMotilityPredicate**

Equations
- Tau.BookVI.Agency.spatial_motility = { condition_count := 3, count_eq := Tau.BookVI.Agency.spatial_motility._proof_1 }
Instances For

---

### `Tau.BookVI.Agency.motility_three_conditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L84-L86)
**theorem
Tau.BookVI.Agency.motility_three_conditions :spatial_motility.condition_count = 3**


---

### `Tau.BookVI.Agency.motility_all_hold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L88-L92)
**theorem
Tau.BookVI.Agency.motility_all_hold :spatial_motility.base_displacement = true ∧ spatial_motility.distinction_preserving = true ∧ spatial_motility.energy_bounded = true**


---

### `Tau.BookVI.Agency.AgencyExtension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L98-L110)
**structure
Tau.BookVI.Agency.AgencyExtension :Type**


[VI.T18] Agency = π-Base Extension Theorem.
An agency Life loop is a persistence loop extended by
nontrivial π-winding on the base.

- winding_alpha : ℕ
Winding number on alpha (temporal).

- winding_pi : ℕ
Winding number on pi (spatial).

- pi_nontrivial : self.winding_pi ≥ 1
Pi-winding is nontrivial (≥ 1).

- extends_persistence : Bool
Extends persistence.

Instances For

---

### `Tau.BookVI.Agency.instReprAgencyExtension.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L110-L110)
**def
Tau.BookVI.Agency.instReprAgencyExtension.repr :AgencyExtension → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Agency.instReprAgencyExtension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L110-L110)
**instance
Tau.BookVI.Agency.instReprAgencyExtension :Repr AgencyExtension**

Equations
- Tau.BookVI.Agency.instReprAgencyExtension = { reprPrec := Tau.BookVI.Agency.instReprAgencyExtension.repr }

---

### `Tau.BookVI.Agency.agency_ext`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L112-L114)
**def
Tau.BookVI.Agency.agency_ext :AgencyExtension**

Equations
- Tau.BookVI.Agency.agency_ext = { winding_pi := 1, pi_nontrivial := Tau.BookVI.Agency.agency_ext._proof_1 }
Instances For

---

### `Tau.BookVI.Agency.agency_is_pi_extension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L116-L120)
**theorem
Tau.BookVI.Agency.agency_is_pi_extension :agency_ext.winding_alpha = 1 ∧ agency_ext.winding_pi ≥ 1 ∧ agency_ext.extends_persistence = true**


---

### `Tau.BookVI.Agency.ChemotaxisFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L126-L138)
**structure
Tau.BookVI.Agency.ChemotaxisFunctor :Type**


[VI.D31] Chemotaxis Functor: directed spatial agency.
Maps chemical gradient to motility direction.
The simplest Agency instantiation: bacterium swimming up gradient.

- input_type : String
Input: chemical gradient signal.

- output_type : String
Output: motility direction.

- preserves_distinction : Bool
Preserves distinction (carrier boundary intact during motion).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Agency.instReprChemotaxisFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L138-L138)
**instance
Tau.BookVI.Agency.instReprChemotaxisFunctor :Repr ChemotaxisFunctor**

Equations
- Tau.BookVI.Agency.instReprChemotaxisFunctor = { reprPrec := Tau.BookVI.Agency.instReprChemotaxisFunctor.repr }

---

### `Tau.BookVI.Agency.instReprChemotaxisFunctor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L138-L138)
**def
Tau.BookVI.Agency.instReprChemotaxisFunctor.repr :ChemotaxisFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Agency.chemotaxis`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L140-L140)
**def
Tau.BookVI.Agency.chemotaxis :ChemotaxisFunctor**

Equations
- Tau.BookVI.Agency.chemotaxis = { }
Instances For

---

### `Tau.BookVI.Agency.chemotaxis_preserves_distinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Agency/AgencySector.lean#L142-L143)
**theorem
Tau.BookVI.Agency.chemotaxis_preserves_distinction :chemotaxis.preserves_distinction = true**
