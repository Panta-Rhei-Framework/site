---
layout: taulib-doc
title: "TauLib.BookV.Temporal.CosmicAPI"
permalink: /verify/taulib/docs/book-v-temporal-cosmic-api/
lane: verify
module_name: "TauLib.BookV.Temporal.CosmicAPI"
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

# TauLib.BookV.Temporal.CosmicAPI


The Cosmic Stack API: formal interface between Part I and Parts II–VIII.

## Registry Cross-References


- [V.D40] Cosmic Stack API — `CosmicStackAPI`, `cosmic_stack_api`

- [V.R52] Scope Census — `api_scope_distribution`


## Mathematical Content


### The Cosmic Stack API


Part I establishes the complete conceptual foundation for macroscopic physics.
The Cosmic Stack API is the formal interface listing all outputs:

**Fixed Inputs (from Part I):**

- Arc-length time on τ¹

- Three temporal epochs (opening, temporal, closing)

- Initial conditions (opening regime)

- Photon ontology (null intertwiner)

- Redshift-depth relation

- Distance readout functor R_d

- CMB constraint surface Σ_CMB

- CνB echo surface Σ_{CνB}

- Hubble readout parameter H(n)

- 5-sector coupling table
... (21 total items)


Each subsequent Part (II–VIII) has required outputs and scope targets.

### Scope Census


Of the 21 Part I entries in the vocabulary table:


- 19 are **τ-effective** (derived from base circle and sector couplings)

- 2 are **conjectural** (readout curvature κ_R(n) and dark energy artifact)


No entries are established (these are physics, not pure algebra) or
metaphorical (no analogies in Part I).

## Ground Truth Sources


- Book V Part I ch10 (Cosmic Stack API chapter)

- book5_registry.jsonl: V.D40, V.R52


---

### `Tau.BookV.Temporal.APIScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L55-L59)
**inductive
Tau.BookV.Temporal.APIScope :Type**


Scope of an API item (simplified for Part I).

- TauEffective : APIScope
- Conjectural : APIScope
Instances For

---

### `Tau.BookV.Temporal.instReprAPIScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L59-L59)
**instance
Tau.BookV.Temporal.instReprAPIScope :Repr APIScope**

Equations
- Tau.BookV.Temporal.instReprAPIScope = { reprPrec := Tau.BookV.Temporal.instReprAPIScope.repr }

---

### `Tau.BookV.Temporal.instReprAPIScope.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L59-L59)
**def
Tau.BookV.Temporal.instReprAPIScope.repr :APIScope → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instDecidableEqAPIScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L59-L59)
**instance
Tau.BookV.Temporal.instDecidableEqAPIScope :DecidableEq APIScope**

Equations
- Tau.BookV.Temporal.instDecidableEqAPIScope x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Temporal.instBEqAPIScope.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L59-L59)
**def
Tau.BookV.Temporal.instBEqAPIScope.beq :APIScope → APIScope → Bool**

Equations
- Tau.BookV.Temporal.instBEqAPIScope.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Temporal.instBEqAPIScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L59-L59)
**instance
Tau.BookV.Temporal.instBEqAPIScope :BEq APIScope**

Equations
- Tau.BookV.Temporal.instBEqAPIScope = { beq := Tau.BookV.Temporal.instBEqAPIScope.beq }

---

### `Tau.BookV.Temporal.APIItem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L65-L73)
**structure
Tau.BookV.Temporal.APIItem :Type**


A single item in the Cosmic Stack API.

- id : String
Registry ID (e.g., "V.D15").

- name : String
Display name.

- scope : APIScope
Scope label.

Instances For

---

### `Tau.BookV.Temporal.instReprAPIItem.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L73-L73)
**def
Tau.BookV.Temporal.instReprAPIItem.repr :APIItem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprAPIItem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L73-L73)
**instance
Tau.BookV.Temporal.instReprAPIItem :Repr APIItem**

Equations
- Tau.BookV.Temporal.instReprAPIItem = { reprPrec := Tau.BookV.Temporal.instReprAPIItem.repr }

---

### `Tau.BookV.Temporal.cosmic_stack_api`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L79-L118)
**def
Tau.BookV.Temporal.cosmic_stack_api :List APIItem**


[V.D40] The Cosmic Stack API: all 21 Part I outputs listed
as the formal interface for Parts II–VIII.

Categories:


- Temporal base (6 items): base circle, alpha-tick, proper time,
causal ordering, geodesic duration, three epochs

- Photon & readout (5 items): null intertwiner, operational distance,
refinement drift, readout expansion, Hubble readout

- Distance ladder (5 items): readout functor, Cepheid calibrator,
BAO ruler, readout curvature, dark energy artifact

- Boundary data (3 items): recombination, CMB surface, CνB surface

- Sector interface (2 items): 5-sector coupling table, opening regime

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.CosmicStackAPI`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L124-L135)
**structure
Tau.BookV.Temporal.CosmicStackAPI :Type**


[V.D40] Cosmic Stack API summary: counts of total items,
τ-effective items, and conjectural items.

- total_count : ℕ
Total number of API items.

- tau_effective_count : ℕ
Number of τ-effective items.

- conjectural_count : ℕ
Number of conjectural items.

- scope_partition : self.tau_effective_count + self.conjectural_count = self.total_count
Scope partition: τ-effective + conjectural = total.

Instances For

---

### `Tau.BookV.Temporal.instReprCosmicStackAPI`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L135-L135)
**instance
Tau.BookV.Temporal.instReprCosmicStackAPI :Repr CosmicStackAPI**

Equations
- Tau.BookV.Temporal.instReprCosmicStackAPI = { reprPrec := Tau.BookV.Temporal.instReprCosmicStackAPI.repr }

---

### `Tau.BookV.Temporal.instReprCosmicStackAPI.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L135-L135)
**def
Tau.BookV.Temporal.instReprCosmicStackAPI.repr :CosmicStackAPI → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.cosmic_stack_summary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L137-L142)
**def
Tau.BookV.Temporal.cosmic_stack_summary :CosmicStackAPI**


The canonical Cosmic Stack API summary.
Equations
- Tau.BookV.Temporal.cosmic_stack_summary = { total_count := 21, tau_effective_count := 19, conjectural_count := 2,
 scope_partition := Tau.BookV.Temporal.cosmic_stack_summary._proof_2 }
Instances For

---

### `Tau.BookV.Temporal.api_item_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L148-L149)
**theorem
Tau.BookV.Temporal.api_item_count :cosmic_stack_api.length = 21**


[V.D40] The API has exactly 21 items.

---

### `Tau.BookV.Temporal.api_scope_distribution`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L151-L155)
**theorem
Tau.BookV.Temporal.api_scope_distribution :(List.filter (fun (x : APIItem) => x.scope == APIScope.TauEffective) cosmic_stack_api).length = 19 ∧ (List.filter (fun (x : APIItem) => x.scope == APIScope.Conjectural) cosmic_stack_api).length = 2**


[V.R52] Scope distribution: 19 τ-effective, 2 conjectural.

---

### `Tau.BookV.Temporal.api_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L157-L162)
**theorem
Tau.BookV.Temporal.api_complete :cosmic_stack_summary.tau_effective_count + cosmic_stack_summary.conjectural_count = cosmic_stack_summary.total_count**


[V.D40 + V.R52] API complete: 19 + 2 = 21.

---

### `Tau.BookV.Temporal.summary_matches_list`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L164-L166)
**theorem
Tau.BookV.Temporal.summary_matches_list :cosmic_stack_summary.total_count = cosmic_stack_api.length**


The summary matches the actual list length.

---

### `Tau.BookV.Temporal.all_items_have_ids`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L168-L170)
**theorem
Tau.BookV.Temporal.all_items_have_ids :(cosmic_stack_api.all fun (item : APIItem) => decide (item.id.length > 0)) = true**


All API items have non-empty IDs.

---

### `Tau.BookV.Temporal.all_items_have_names`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L172-L174)
**theorem
Tau.BookV.Temporal.all_items_have_names :(cosmic_stack_api.all fun (item : APIItem) => decide (item.name.length > 0)) = true**


All API items have non-empty names.

---

### `Tau.BookV.Temporal.conjectural_items_identified`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L176-L179)
**theorem
Tau.BookV.Temporal.conjectural_items_identified :(List.filter (fun (x : APIItem) => x.scope == APIScope.Conjectural) cosmic_stack_api).length = 2**


The two conjectural items are readout curvature and dark energy.

---

### `Tau.BookV.Temporal.minimum_id_length`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/CosmicAPI.lean#L181-L183)
**theorem
Tau.BookV.Temporal.minimum_id_length :(cosmic_stack_api.all fun (item : APIItem) => decide (item.id.length ≥ 5)) = true**


No item has an empty ID (stronger: minimum ID length is 5).
