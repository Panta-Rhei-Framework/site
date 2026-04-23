---
layout: taulib-doc
title: "TauLib.BookVI.Sectors.Absence"
permalink: /verify/taulib/docs/book-vi-sectors-absence/
lane: verify
module_name: "TauLib.BookVI.Sectors.Absence"
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

# TauLib.BookVI.Sectors.Absence


Failure modes: NoDist and NoSelfDesc. Virus, neutron, NS counterexamples.

## Registry Cross-References


- [VI.D21] NoDist — `NoDist`

- [VI.D22] NoSelfDesc — `NoSelfDesc`

- [VI.T15] Virus NoDist — `virus_nodist`

- [VI.L06] NS-NoSelfDesc — `ns_noselfdesc`

- [VI.L07] Consumer Bridge to E₃ — `consumer_bridge_e3`

- [VI.P09] Circadian 24h = τ¹ Rotation — `circadian_rotation`


## Ground Truth Sources


- Book VI Chapter 10 (2nd Edition): Predictions by Absence


---

### `Tau.BookVI.Absence.NoDist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L23-L27)
**structure
Tau.BookVI.Absence.NoDist :Type**


[VI.D21] NoDist: system fails τ-Distinction.

- conditions_failed : ℕ
- at_least_one : self.conditions_failed ≥ 1
Instances For

---

### `Tau.BookVI.Absence.instReprNoDist.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L27-L27)
**def
Tau.BookVI.Absence.instReprNoDist.repr :NoDist → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Absence.instReprNoDist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L27-L27)
**instance
Tau.BookVI.Absence.instReprNoDist :Repr NoDist**

Equations
- Tau.BookVI.Absence.instReprNoDist = { reprPrec := Tau.BookVI.Absence.instReprNoDist.repr }

---

### `Tau.BookVI.Absence.NoSelfDesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L29-L34)
**structure
Tau.BookVI.Absence.NoSelfDesc :Type**


[VI.D22] NoSelfDesc: has Distinction but fails SelfDesc.

- has_distinction : Bool
- selfdesc_fails : Bool
- failure_reason : String
Instances For

---

### `Tau.BookVI.Absence.instReprNoSelfDesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L34-L34)
**instance
Tau.BookVI.Absence.instReprNoSelfDesc :Repr NoSelfDesc**

Equations
- Tau.BookVI.Absence.instReprNoSelfDesc = { reprPrec := Tau.BookVI.Absence.instReprNoSelfDesc.repr }

---

### `Tau.BookVI.Absence.instReprNoSelfDesc.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L34-L34)
**def
Tau.BookVI.Absence.instReprNoSelfDesc.repr :NoSelfDesc → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Absence.VirusNoDist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L36-L41)
**structure
Tau.BookVI.Absence.VirusNoDist :Type**


[VI.T15] Virus NoDist: fails 3/5 distinction conditions outside host.

- conditions_failed : ℕ
- three_fail : self.conditions_failed = 3
- host_dependent : Bool
Instances For

---

### `Tau.BookVI.Absence.instReprVirusNoDist.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L41-L41)
**def
Tau.BookVI.Absence.instReprVirusNoDist.repr :VirusNoDist → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Absence.instReprVirusNoDist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L41-L41)
**instance
Tau.BookVI.Absence.instReprVirusNoDist :Repr VirusNoDist**

Equations
- Tau.BookVI.Absence.instReprVirusNoDist = { reprPrec := Tau.BookVI.Absence.instReprVirusNoDist.repr }

---

### `Tau.BookVI.Absence.virus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L43-L45)
**def
Tau.BookVI.Absence.virus :VirusNoDist**

Equations
- Tau.BookVI.Absence.virus = { conditions_failed := 3, three_fail := Tau.BookVI.Absence.virus._proof_1 }
Instances For

---

### `Tau.BookVI.Absence.virus_nodist`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L47-L50)
**theorem
Tau.BookVI.Absence.virus_nodist :virus.conditions_failed = 3 ∧ virus.host_dependent = true**


---

### `Tau.BookVI.Absence.NSNoSelfDesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L52-L57)
**structure
Tau.BookVI.Absence.NSNoSelfDesc :Type**


[VI.L06] NS-NoSelfDesc: 5/5 distinction, fails SelfDesc.

- distinction_passed : ℕ
- all_five : self.distinction_passed = 5
- selfdesc_fails : Bool
Instances For

---

### `Tau.BookVI.Absence.instReprNSNoSelfDesc.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L57-L57)
**def
Tau.BookVI.Absence.instReprNSNoSelfDesc.repr :NSNoSelfDesc → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Absence.instReprNSNoSelfDesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L57-L57)
**instance
Tau.BookVI.Absence.instReprNSNoSelfDesc :Repr NSNoSelfDesc**

Equations
- Tau.BookVI.Absence.instReprNSNoSelfDesc = { reprPrec := Tau.BookVI.Absence.instReprNSNoSelfDesc.repr }

---

### `Tau.BookVI.Absence.ns_nosd`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L59-L61)
**def
Tau.BookVI.Absence.ns_nosd :NSNoSelfDesc**

Equations
- Tau.BookVI.Absence.ns_nosd = { distinction_passed := 5, all_five := Tau.BookVI.Absence.ns_nosd._proof_1 }
Instances For

---

### `Tau.BookVI.Absence.ns_noselfdesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L63-L66)
**theorem
Tau.BookVI.Absence.ns_noselfdesc :ns_nosd.distinction_passed = 5 ∧ ns_nosd.selfdesc_fails = true**


---

### `Tau.BookVI.Absence.ConsumerBridgeE3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L68-L72)
**structure
Tau.BookVI.Absence.ConsumerBridgeE3 :Type**


[VI.L07] Consumer sector is unique bridge-head to E₃.

- has_eval_squared : Bool
- consumer_only : Bool
Instances For

---

### `Tau.BookVI.Absence.instReprConsumerBridgeE3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L72-L72)
**instance
Tau.BookVI.Absence.instReprConsumerBridgeE3 :Repr ConsumerBridgeE3**

Equations
- Tau.BookVI.Absence.instReprConsumerBridgeE3 = { reprPrec := Tau.BookVI.Absence.instReprConsumerBridgeE3.repr }

---

### `Tau.BookVI.Absence.instReprConsumerBridgeE3.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L72-L72)
**def
Tau.BookVI.Absence.instReprConsumerBridgeE3.repr :ConsumerBridgeE3 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Absence.consumer_bridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L74-L74)
**def
Tau.BookVI.Absence.consumer_bridge :ConsumerBridgeE3**

Equations
- Tau.BookVI.Absence.consumer_bridge = { }
Instances For

---

### `Tau.BookVI.Absence.consumer_bridge_e3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L76-L79)
**theorem
Tau.BookVI.Absence.consumer_bridge_e3 :consumer_bridge.has_eval_squared = true ∧ consumer_bridge.consumer_only = true**


---

### `Tau.BookVI.Absence.CircadianRotation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L81-L85)
**structure
Tau.BookVI.Absence.CircadianRotation :Type**


[VI.P09] Circadian 24h = one full α-rotation on τ¹.

- period_hours : ℕ
- winding_number : ℕ
Instances For

---

### `Tau.BookVI.Absence.instReprCircadianRotation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L85-L85)
**def
Tau.BookVI.Absence.instReprCircadianRotation.repr :CircadianRotation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Absence.instReprCircadianRotation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L85-L85)
**instance
Tau.BookVI.Absence.instReprCircadianRotation :Repr CircadianRotation**

Equations
- Tau.BookVI.Absence.instReprCircadianRotation = { reprPrec := Tau.BookVI.Absence.instReprCircadianRotation.repr }

---

### `Tau.BookVI.Absence.circadian`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L87-L87)
**def
Tau.BookVI.Absence.circadian :CircadianRotation**

Equations
- Tau.BookVI.Absence.circadian = { }
Instances For

---

### `Tau.BookVI.Absence.circadian_rotation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Sectors/Absence.lean#L89-L92)
**theorem
Tau.BookVI.Absence.circadian_rotation :circadian.period_hours = 24 ∧ circadian.winding_number = 1**
