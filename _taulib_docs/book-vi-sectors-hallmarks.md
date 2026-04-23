---
layout: taulib-doc
title: "TauLib.BookVI.Sectors.Hallmarks"
permalink: /verify/taulib/docs/book-vi-sectors-hallmarks/
lane: verify
module_name: "TauLib.BookVI.Sectors.Hallmarks"
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

# TauLib.BookVI.Sectors.Hallmarks


Seven hallmarks of life derived from Distinction + SelfDesc.

## Registry Cross-References


- [VI.T08–T14] Seven hallmarks — `organization` through `evolution`

- [VI.P08] Thermodynamic Inevitability — `thermodynamic_inevitability`


## Ground Truth Sources


- Book VI Chapter 9 (2nd Edition): Seven Hallmarks


---

### `Tau.BookVI.Hallmarks.Hallmark`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L19-L22)
**structure
Tau.BookVI.Hallmarks.Hallmark :Type**


- classical : String
- formal : String
Instances For

---

### `Tau.BookVI.Hallmarks.instReprHallmark`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L22-L22)
**instance
Tau.BookVI.Hallmarks.instReprHallmark :Repr Hallmark**

Equations
- Tau.BookVI.Hallmarks.instReprHallmark = { reprPrec := Tau.BookVI.Hallmarks.instReprHallmark.repr }

---

### `Tau.BookVI.Hallmarks.instReprHallmark.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L22-L22)
**def
Tau.BookVI.Hallmarks.instReprHallmark.repr :Hallmark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Hallmarks.organization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L24-L27)
**def
Tau.BookVI.Hallmarks.organization :Hallmark**


[VI.T08] Organization = Distinction Structure.
Equations
- Tau.BookVI.Hallmarks.organization = { classical := "organization", formal := "distinction-structure" }
Instances For

---

### `Tau.BookVI.Hallmarks.metabolism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L29-L32)
**def
Tau.BookVI.Hallmarks.metabolism :Hallmark**


[VI.T09] Metabolism = Life Loop Class.
Equations
- Tau.BookVI.Hallmarks.metabolism = { classical := "metabolism", formal := "life-loop-class" }
Instances For

---

### `Tau.BookVI.Hallmarks.homeostasis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L34-L37)
**def
Tau.BookVI.Hallmarks.homeostasis :Hallmark**


[VI.T10] Homeostasis = Basin Stability.
Equations
- Tau.BookVI.Hallmarks.homeostasis = { classical := "homeostasis", formal := "basin-stability" }
Instances For

---

### `Tau.BookVI.Hallmarks.growth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L39-L42)
**def
Tau.BookVI.Hallmarks.growth :Hallmark**


[VI.T11] Growth = Carrier Refinement.
Equations
- Tau.BookVI.Hallmarks.growth = { classical := "growth", formal := "carrier-refinement" }
Instances For

---

### `Tau.BookVI.Hallmarks.reproduction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L44-L47)
**def
Tau.BookVI.Hallmarks.reproduction :Hallmark**


[VI.T12] Reproduction = Blueprint Propagation.
Equations
- Tau.BookVI.Hallmarks.reproduction = { classical := "reproduction", formal := "blueprint-propagation" }
Instances For

---

### `Tau.BookVI.Hallmarks.response`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L49-L52)
**def
Tau.BookVI.Hallmarks.response :Hallmark**


[VI.T13] Response = SelfDesc Adjustment.
Equations
- Tau.BookVI.Hallmarks.response = { classical := "response", formal := "selfdesc-adjustment" }
Instances For

---

### `Tau.BookVI.Hallmarks.evolution`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L54-L57)
**def
Tau.BookVI.Hallmarks.evolution :Hallmark**


[VI.T14] Evolution = PPAS Optimization.
Equations
- Tau.BookVI.Hallmarks.evolution = { classical := "evolution", formal := "ppas-optimization" }
Instances For

---

### `Tau.BookVI.Hallmarks.all_hallmarks`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L59-L60)
**def
Tau.BookVI.Hallmarks.all_hallmarks :List Hallmark**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Hallmarks.hallmark_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L62-L62)
**theorem
Tau.BookVI.Hallmarks.hallmark_count :all_hallmarks.length = 7**


---

### `Tau.BookVI.Hallmarks.ThermodynamicInevitability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L64-L69)
**structure
Tau.BookVI.Hallmarks.ThermodynamicInevitability :Type**


[VI.P08] Thermodynamic inevitability (conjectural).

- is_attractor : Bool
- positive_measure : Bool
- scope : String
Instances For

---

### `Tau.BookVI.Hallmarks.instReprThermodynamicInevitability.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L69-L69)
**def
Tau.BookVI.Hallmarks.instReprThermodynamicInevitability.repr :ThermodynamicInevitability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Hallmarks.instReprThermodynamicInevitability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L69-L69)
**instance
Tau.BookVI.Hallmarks.instReprThermodynamicInevitability :Repr ThermodynamicInevitability**

Equations
- Tau.BookVI.Hallmarks.instReprThermodynamicInevitability = { reprPrec := Tau.BookVI.Hallmarks.instReprThermodynamicInevitability.repr }

---

### `Tau.BookVI.Hallmarks.thermo_inev`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L71-L71)
**def
Tau.BookVI.Hallmarks.thermo_inev :ThermodynamicInevitability**

Equations
- Tau.BookVI.Hallmarks.thermo_inev = { }
Instances For

---

### `Tau.BookVI.Hallmarks.thermodynamic_inevitability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Hallmarks.lean#L73-L76)
**theorem
Tau.BookVI.Hallmarks.thermodynamic_inevitability :thermo_inev.is_attractor = true ∧ thermo_inev.scope = "conjectural"**
