---
layout: taulib-doc
title: "TauLib.BookIII.Physics.StrongSector"
permalink: /verify/taulib/docs/book-iii-physics-strong-sector/
lane: verify
module_name: "TauLib.BookIII.Physics.StrongSector"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Physics.StrongSector


Strong Sector at E₁, Gauge Data, and NF Discreteness.

## Registry Cross-References


- [III.D43] Strong Sector at E₁ -- `strong_sector_check`

- [III.D44] Gauge Data -- `GaugeData`, `gauge_data_check`

- [III.P16] NF Discreteness -- `nf_discreteness_check`


## Mathematical Content


**III.D43 (Strong Sector):** A sector is "strong" at E₁ if its BNF decomposition
is unambiguous, tower-stable, and carries non-trivial content. Concretely: the
B-product and C-product at each primorial level are coprime (from the trichotomy),
and the label assignment is depth-stable.

**III.D44 (Gauge Data):** At E₁ level, each sector carries "gauge data": the
label assignment of each prime, the sector coupling constants (B-product, C-product,
X-product), and the defect functional value. Gauge data is the E₁ enrichment
of the bare E₀ BNF.

**III.P16 (NF Discreteness):** The normal form is discrete: distinct cylinders have
distinct BNFs. The number of distinct BNFs at level k equals Prim(k), confirming
no information loss in the sector decomposition.

---

### `Tau.BookIII.Physics.strong_sector_at_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L42-L57)
**def
Tau.BookIII.Physics.strong_sector_at_level
(k : Denotation.TauIdx)
 :Bool**


[III.D43] Strong sector check at level k: the B/C/X decomposition is
unambiguous (coprimality), tower-stable (labels don't change with depth),
and carries non-trivial content (B and C both have primes).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.strong_sector_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L59-L68)
**def
Tau.BookIII.Physics.strong_sector_check
(db : Denotation.TauIdx)
 :Bool**


[III.D43] Strong sector check across all levels.
Equations
- Tau.BookIII.Physics.strong_sector_check db = Tau.BookIII.Physics.strong_sector_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.strong_sector_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L63-L67)@[irreducible]

**def
Tau.BookIII.Physics.strong_sector_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.label_stability_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L70-L86)
**def
Tau.BookIII.Physics.label_stability_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D43] Label stability check: each prime's label is depth-independent.
Equations
- Tau.BookIII.Physics.label_stability_check bound db = Tau.BookIII.Physics.label_stability_check.go bound db 1 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.label_stability_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L74-L85)@[irreducible]

**def
Tau.BookIII.Physics.label_stability_check.go
(bound db : Denotation.TauIdx)

(i k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.GaugeData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L92-L102)
**structure
Tau.BookIII.Physics.GaugeData :Type**


[III.D44] Gauge data at E₁ level: the enriched sector information
beyond the bare BNF.

- depth : Denotation.TauIdx
- b_product : Denotation.TauIdx
- c_product : Denotation.TauIdx
- x_product : Denotation.TauIdx
- b_count : Denotation.TauIdx
- c_count : Denotation.TauIdx
- x_count : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Physics.instReprGaugeData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L102-L102)
**def
Tau.BookIII.Physics.instReprGaugeData.repr :GaugeData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.instReprGaugeData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L102-L102)
**instance
Tau.BookIII.Physics.instReprGaugeData :Repr GaugeData**

Equations
- Tau.BookIII.Physics.instReprGaugeData = { reprPrec := Tau.BookIII.Physics.instReprGaugeData.repr }

---

### `Tau.BookIII.Physics.instDecidableEqGaugeData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L102-L102)
**instance
Tau.BookIII.Physics.instDecidableEqGaugeData :DecidableEq GaugeData**

Equations
- Tau.BookIII.Physics.instDecidableEqGaugeData = Tau.BookIII.Physics.instDecidableEqGaugeData.decEq

---

### `Tau.BookIII.Physics.instDecidableEqGaugeData.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L102-L102)
**def
Tau.BookIII.Physics.instDecidableEqGaugeData.decEq
(x✝ x✝¹ : GaugeData)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.instBEqGaugeData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L102-L102)
**instance
Tau.BookIII.Physics.instBEqGaugeData :BEq GaugeData**

Equations
- Tau.BookIII.Physics.instBEqGaugeData = { beq := Tau.BookIII.Physics.instBEqGaugeData.beq }

---

### `Tau.BookIII.Physics.instBEqGaugeData.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L102-L102)
**def
Tau.BookIII.Physics.instBEqGaugeData.beq :GaugeData → GaugeData → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Physics.instBEqGaugeData.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Physics.gauge_data_at`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L104-L107)
**def
Tau.BookIII.Physics.gauge_data_at
(k : Denotation.TauIdx)
 :GaugeData**


[III.D44] Extract gauge data at primorial level k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.gauge_data_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L109-L127)
**def
Tau.BookIII.Physics.gauge_data_check
(db : Denotation.TauIdx)
 :Bool**


[III.D44] Gauge data check: products are consistent, counts match
the number of primes, and gauge data at k is compatible with k+1.
Equations
- Tau.BookIII.Physics.gauge_data_check db = Tau.BookIII.Physics.gauge_data_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.gauge_data_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L114-L126)@[irreducible]

**def
Tau.BookIII.Physics.gauge_data_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.gauge_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L129-L149)
**def
Tau.BookIII.Physics.gauge_tower_check
(db : Denotation.TauIdx)
 :Bool**


[III.D44] Gauge tower compatibility: gauge data at k extends to k+1
(products divide).
Equations
- Tau.BookIII.Physics.gauge_tower_check db = Tau.BookIII.Physics.gauge_tower_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.gauge_tower_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L134-L148)@[irreducible]

**def
Tau.BookIII.Physics.gauge_tower_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.nf_discreteness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L155-L176)
**def
Tau.BookIII.Physics.nf_discreteness_check
(db : Denotation.TauIdx)
 :Bool**


[III.P16] NF discreteness check: distinct residues mod Prim(k) have
distinct BNFs. This means the BNF map is injective.
Equations
- Tau.BookIII.Physics.nf_discreteness_check db = Tau.BookIII.Physics.nf_discreteness_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.nf_discreteness_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L160-L167)@[irreducible]

**def
Tau.BookIII.Physics.nf_discreteness_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.nf_discreteness_check.check_inj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L169-L176)@[irreducible]

**def
Tau.BookIII.Physics.nf_discreteness_check.check_inj
(x y pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.strong_sector_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L194-L195)
**theorem
Tau.BookIII.Physics.strong_sector_5 :strong_sector_check 5 = true**


---

### `Tau.BookIII.Physics.label_stability_10_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L197-L198)
**theorem
Tau.BookIII.Physics.label_stability_10_4 :label_stability_check 10 4 = true**


---

### `Tau.BookIII.Physics.gauge_data_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L200-L201)
**theorem
Tau.BookIII.Physics.gauge_data_5 :gauge_data_check 5 = true**


---

### `Tau.BookIII.Physics.gauge_tower_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L203-L204)
**theorem
Tau.BookIII.Physics.gauge_tower_4 :gauge_tower_check 4 = true**


---

### `Tau.BookIII.Physics.nf_discrete_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L206-L207)
**theorem
Tau.BookIII.Physics.nf_discrete_3 :nf_discreteness_check 3 = true**


---

### `Tau.BookIII.Physics.strong_at_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L213-L215)
**theorem
Tau.BookIII.Physics.strong_at_1 :strong_sector_at_level 1 = true**


[III.D43] Structural: strong sector at depth 1 (only prime 2 = X).

---

### `Tau.BookIII.Physics.gauge_3_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L217-L220)
**theorem
Tau.BookIII.Physics.gauge_3_complete :(gauge_data_at 3).b_product * (gauge_data_at 3).c_product * (gauge_data_at 3).x_product = Polarity.primorial 3**


[III.D44] Structural: gauge data at depth 3 has correct products.

---

### `Tau.BookIII.Physics.gauge_3_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L222-L225)
**theorem
Tau.BookIII.Physics.gauge_3_count :(gauge_data_at 3).b_count + (gauge_data_at 3).c_count + (gauge_data_at 3).x_count = 3**


[III.D44] Structural: gauge data at depth 3 has correct counts.

---

### `Tau.BookIII.Physics.nf_zero_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/StrongSector.lean#L227-L229)
**theorem
Tau.BookIII.Physics.nf_zero_unique :Spectral.boundary_normal_form 0 3 = { b_part := 0, c_part := 0, x_part := 0, depth := 3 }**


[III.P16] Structural: BNF of 0 is unique at depth 3.
