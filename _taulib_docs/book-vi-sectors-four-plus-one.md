---
layout: taulib-doc
title: "TauLib.BookVI.Sectors.FourPlusOne"
permalink: /verify/taulib/docs/book-vi-sectors-four-plus-one/
lane: verify
module_name: "TauLib.BookVI.Sectors.FourPlusOne"
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

# TauLib.BookVI.Sectors.FourPlusOne


The 4+1 life sector classification: 4 primitive + 1 mixed = 5 total.

## Registry Cross-References


- [VI.D15] Life Sector — `LifeSector`

- [VI.D16–D20] Five sectors — `persistence_sector` etc.

- [VI.T07] Generator Adequacy at E₂ — `generator_adequacy_e2`

- [VI.L05] Neutron NoDist — `neutron_nodist`


## Ground Truth Sources


- Book VI Chapter 8 (2nd Edition): Five Sectors


---

### `Tau.BookVI.FourPlusOne.LifeSector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L21-L26)
**structure
Tau.BookVI.FourPlusOne.LifeSector :Type**


[VI.D15] Life sector: pair (g, P) with generator and restriction.

- generator : String
- is_primitive : Bool
- archetype : String
Instances For

---

### `Tau.BookVI.FourPlusOne.instReprLifeSector.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L26-L26)
**def
Tau.BookVI.FourPlusOne.instReprLifeSector.repr :LifeSector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FourPlusOne.instReprLifeSector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L26-L26)
**instance
Tau.BookVI.FourPlusOne.instReprLifeSector :Repr LifeSector**

Equations
- Tau.BookVI.FourPlusOne.instReprLifeSector = { reprPrec := Tau.BookVI.FourPlusOne.instReprLifeSector.repr }

---

### `Tau.BookVI.FourPlusOne.persistence_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L28-L32)
**def
Tau.BookVI.FourPlusOne.persistence_sector :LifeSector**


[VI.D16] Persistence sector (α-base). Archetype: Archaea.
Equations
- Tau.BookVI.FourPlusOne.persistence_sector = { generator := "alpha", is_primitive := true, archetype := "Archaea" }
Instances For

---

### `Tau.BookVI.FourPlusOne.agency_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L34-L38)
**def
Tau.BookVI.FourPlusOne.agency_sector :LifeSector**


[VI.D17] Agency sector (π-base). Archetype: Bacteria.
Equations
- Tau.BookVI.FourPlusOne.agency_sector = { generator := "pi", is_primitive := true, archetype := "Bacteria" }
Instances For

---

### `Tau.BookVI.FourPlusOne.source_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L40-L44)
**def
Tau.BookVI.FourPlusOne.source_sector :LifeSector**


[VI.D18] Source sector (π'-fiber). Archetype: Plants.
Equations
- Tau.BookVI.FourPlusOne.source_sector = { generator := "pi_prime", is_primitive := true, archetype := "Plants" }
Instances For

---

### `Tau.BookVI.FourPlusOne.closure_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L46-L50)
**def
Tau.BookVI.FourPlusOne.closure_sector :LifeSector**


[VI.D19] Closure sector (π''-fiber). Archetype: Fungi.
Equations
- Tau.BookVI.FourPlusOne.closure_sector = { generator := "pi_double_prime", is_primitive := true, archetype := "Fungi" }
Instances For

---

### `Tau.BookVI.FourPlusOne.consumer_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L52-L56)
**def
Tau.BookVI.FourPlusOne.consumer_sector :LifeSector**


[VI.D20] Consumer mixed sector (π',π''). Archetype: Animals.
Equations
- Tau.BookVI.FourPlusOne.consumer_sector = { generator := "pi_prime_pi_double_prime", is_primitive := false, archetype := "Animals" }
Instances For

---

### `Tau.BookVI.FourPlusOne.all_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L58-L59)
**def
Tau.BookVI.FourPlusOne.all_sectors :List LifeSector**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FourPlusOne.sector_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L61-L61)
**theorem
Tau.BookVI.FourPlusOne.sector_count :all_sectors.length = 5**


---

### `Tau.BookVI.FourPlusOne.primitive_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L63-L64)
**def
Tau.BookVI.FourPlusOne.primitive_sectors :List LifeSector**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FourPlusOne.primitive_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L66-L66)
**theorem
Tau.BookVI.FourPlusOne.primitive_count :primitive_sectors.length = 4**


---

### `Tau.BookVI.FourPlusOne.GeneratorAdequacy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L68-L74)
**structure
Tau.BookVI.FourPlusOne.GeneratorAdequacy :Type**


[VI.T07] Generator adequacy: 5 sectors cover all Life loops disjointly.

- total_sectors : ℕ
- total_eq : self.total_sectors = 5
- disjoint : Bool
- exhaustive : Bool
Instances For

---

### `Tau.BookVI.FourPlusOne.instReprGeneratorAdequacy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L74-L74)
**instance
Tau.BookVI.FourPlusOne.instReprGeneratorAdequacy :Repr GeneratorAdequacy**

Equations
- Tau.BookVI.FourPlusOne.instReprGeneratorAdequacy = { reprPrec := Tau.BookVI.FourPlusOne.instReprGeneratorAdequacy.repr }

---

### `Tau.BookVI.FourPlusOne.instReprGeneratorAdequacy.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L74-L74)
**def
Tau.BookVI.FourPlusOne.instReprGeneratorAdequacy.repr :GeneratorAdequacy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FourPlusOne.gen_adequacy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L76-L78)
**def
Tau.BookVI.FourPlusOne.gen_adequacy :GeneratorAdequacy**

Equations
- Tau.BookVI.FourPlusOne.gen_adequacy = { total_sectors := 5, total_eq := Tau.BookVI.FourPlusOne.gen_adequacy._proof_1 }
Instances For

---

### `Tau.BookVI.FourPlusOne.generator_adequacy_e2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L80-L84)
**theorem
Tau.BookVI.FourPlusOne.generator_adequacy_e2 :gen_adequacy.total_sectors = 5 ∧ gen_adequacy.disjoint = true ∧ gen_adequacy.exhaustive = true**


---

### `Tau.BookVI.FourPlusOne.NeutronNoDist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L86-L90)
**structure
Tau.BookVI.FourPlusOne.NeutronNoDist :Type**


[VI.L05] Neutron NoDist: free neutron fails 3/5 distinction conditions.

- conditions_failed : ℕ
- failed_eq : self.conditions_failed = 3
Instances For

---

### `Tau.BookVI.FourPlusOne.instReprNeutronNoDist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L90-L90)
**instance
Tau.BookVI.FourPlusOne.instReprNeutronNoDist :Repr NeutronNoDist**

Equations
- Tau.BookVI.FourPlusOne.instReprNeutronNoDist = { reprPrec := Tau.BookVI.FourPlusOne.instReprNeutronNoDist.repr }

---

### `Tau.BookVI.FourPlusOne.instReprNeutronNoDist.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L90-L90)
**def
Tau.BookVI.FourPlusOne.instReprNeutronNoDist.repr :NeutronNoDist → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.FourPlusOne.neutron_nd`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L92-L94)
**def
Tau.BookVI.FourPlusOne.neutron_nd :NeutronNoDist**

Equations
- Tau.BookVI.FourPlusOne.neutron_nd = { conditions_failed := 3, failed_eq := Tau.BookVI.FourPlusOne.neutron_nd._proof_1 }
Instances For

---

### `Tau.BookVI.FourPlusOne.neutron_nodist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/FourPlusOne.lean#L96-L96)
**theorem
Tau.BookVI.FourPlusOne.neutron_nodist :neutron_nd.conditions_failed = 3**
