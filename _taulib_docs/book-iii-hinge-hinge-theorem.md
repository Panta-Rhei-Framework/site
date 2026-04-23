---
layout: taulib-doc
title: "TauLib.BookIII.Hinge.HingeTheorem"
permalink: /verify/taulib/docs/book-iii-hinge-hinge-theorem/
lane: verify
module_name: "TauLib.BookIII.Hinge.HingeTheorem"
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

# TauLib.BookIII.Hinge.HingeTheorem


Hinge Theorem and No-Knobs Theorem: the capstone results of Book III Part VIII.

## Registry Cross-References


- [III.T41] Hinge Theorem -- `hinge_theorem_check`

- [III.T42] No-Knobs Theorem -- `no_knobs_check`


## Mathematical Content


**III.T41 (Hinge Theorem):** Every result in Books IV-VII is a sector
instantiation of a Book III structure. The enrichment tower E0 -> E1 -> E2 -> E3
acts as a hinge: Book III provides the universal template, and each subsequent
book instantiates the template at the appropriate enrichment level with sector
products determined by the dependency chain.

At finite level: for each enrichment level E_k and each sector S in {D, A, B, C, Omega},
the sector product at E_k is determined by the tower coherence checks at that level.
The hinge ensures that the 14-link chain controls all downstream content.

**III.T42 (No-Knobs Theorem):** All coupling constants and sector products
are determined by a single parameter: iota_tau = 2/(pi + e) ~ 0.341304.
No free parameters remain after the enrichment tower is assembled.
The rational approximation 341304/1000000 determines all finite-level
sector products via the primorial tower.

The No-Knobs Theorem is the philosophical capstone: Category tau has
no adjustable parameters. Everything flows from the seven axioms.

---

### `Tau.BookIII.Hinge.sector_product`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L47-L60)
**def
Tau.BookIII.Hinge.sector_product
(s : Sectors.Sector)

(k : Denotation.TauIdx)
 :Denotation.TauIdx**


Sector product at a given enrichment level and depth k.
Each sector contributes a factor to the primorial decomposition:


- D: radial (trivial character contribution = 1)

- A: balanced (equal m,n contribution)

- B: B-lobe product (split_zeta_b)

- C: C-lobe product (split_zeta_c)

- Omega: crossing product (split_zeta_x)

Equations
- Tau.BookIII.Hinge.sector_product Tau.BookIII.Sectors.Sector.D k = 1
- Tau.BookIII.Hinge.sector_product Tau.BookIII.Sectors.Sector.A k = if (k == 0) = true then 1 else 2
- Tau.BookIII.Hinge.sector_product Tau.BookIII.Sectors.Sector.B k = Tau.BookIII.Doors.split_zeta_b k
- Tau.BookIII.Hinge.sector_product Tau.BookIII.Sectors.Sector.C k = Tau.BookIII.Doors.split_zeta_c k
- Tau.BookIII.Hinge.sector_product Tau.BookIII.Sectors.Sector.Omega k = Tau.BookIII.Doors.split_zeta_x k
Instances For

---

### `Tau.BookIII.Hinge.total_sector_product`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L62-L69)
**def
Tau.BookIII.Hinge.total_sector_product
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


Total sector product: D * A * B * C * Omega should recover a
function of Prim(k) at each depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.sector_product_at_level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L71-L78)
**def
Tau.BookIII.Hinge.sector_product_at_level
(lev : Enrichment.EnrLevel)

(k : Denotation.TauIdx)
 :Denotation.TauIdx**


Sector product at an enrichment level: the layer template determines
which sectors are active at each level.
Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Hinge.sector_product_at_level Tau.BookIII.Enrichment.EnrLevel.E3 k = 1
Instances For

---

### `Tau.BookIII.Hinge.sector_instantiation_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L84-L117)
**def
Tau.BookIII.Hinge.sector_instantiation_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T41] Sector instantiation check: at each enrichment level,
the sector products are determined by the tower coherence.
For k in 1..db: BNF at k decomposes into sector products,
and these products are compatible across levels.
Equations
- Tau.BookIII.Hinge.sector_instantiation_check bound db = Tau.BookIII.Hinge.sector_instantiation_check.go bound 1 db (db + 1)
Instances For

---

### `Tau.BookIII.Hinge.sector_instantiation_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L91-L102)@[irreducible]

**def
Tau.BookIII.Hinge.sector_instantiation_check.go
(bound : Denotation.TauIdx)

(k db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.sector_instantiation_check.bnf_check_at`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L105-L106)
**def
Tau.BookIII.Hinge.sector_instantiation_check.bnf_check_at
(bound k : ℕ)
 :Bool**


Check BNF at a single depth.
Equations
- Tau.BookIII.Hinge.sector_instantiation_check.bnf_check_at bound k = Tau.BookIII.Hinge.sector_instantiation_check.bnf_at_go 0 bound k (bound + 1)
Instances For

---

### `Tau.BookIII.Hinge.sector_instantiation_check.bnf_at_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L107-L116)@[irreducible]

**def
Tau.BookIII.Hinge.sector_instantiation_check.bnf_at_go
(x bound k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.level_coherence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L119-L136)
**def
Tau.BookIII.Hinge.level_coherence_check
(db : Denotation.TauIdx)
 :Bool**


[III.T41] Level coherence check: sector products at level k+1
extend those at level k (divisibility).
Equations
- Tau.BookIII.Hinge.level_coherence_check db = Tau.BookIII.Hinge.level_coherence_check.go 1 db (db + 1)
Instances For

---

### `Tau.BookIII.Hinge.level_coherence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L124-L135)@[irreducible]

**def
Tau.BookIII.Hinge.level_coherence_check.go
(k db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Hinge.enrichment_determines_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L144-L171)
**def
Tau.BookIII.Hinge.enrichment_determines_sectors
(bound db : Denotation.TauIdx)
 :Bool**


[III.T41] Enrichment determines sectors: at each level, the layer
template's predicate selects exactly the admissible sector products.
Equations
- Tau.BookIII.Hinge.enrichment_determines_sectors bound db = Tau.BookIII.Hinge.enrichment_determines_sectors.go 0 1 bound db ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Hinge.enrichment_determines_sectors.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L149-L170)@[irreducible]

**def
Tau.BookIII.Hinge.enrichment_determines_sectors.go
(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.hinge_theorem_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L173-L183)
**def
Tau.BookIII.Hinge.hinge_theorem_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T41] Hinge theorem check: sector instantiation + level coherence +
enrichment determines sectors + dependency chain valid.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.iota_numer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L189-L190)
**def
Tau.BookIII.Hinge.iota_numer :ℕ**


The iota_tau rational approximation: 341304/1000000.
Equations
- Tau.BookIII.Hinge.iota_numer = 341304
Instances For

---

### `Tau.BookIII.Hinge.iota_denom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L191-L191)
**def
Tau.BookIII.Hinge.iota_denom :ℕ**

Equations
- Tau.BookIII.Hinge.iota_denom = 1000000
Instances For

---

### `Tau.BookIII.Hinge.iota_determines_ratio`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L193-L214)
**def
Tau.BookIII.Hinge.iota_determines_ratio
(db : Denotation.TauIdx)
 :Bool**


[III.T42] iota_tau determines B/C ratio: at each depth k,
the ratio B-product / C-product is governed by iota_tau.
In scaled arithmetic: B * iota_denom vs C * iota_numer
should be in the correct ordering.
Equations
- Tau.BookIII.Hinge.iota_determines_ratio db = Tau.BookIII.Hinge.iota_determines_ratio.go 3 db (db + 1)
Instances For

---

### `Tau.BookIII.Hinge.iota_determines_ratio.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L200-L213)@[irreducible]

**def
Tau.BookIII.Hinge.iota_determines_ratio.go
(k db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.no_free_parameters_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L216-L243)
**def
Tau.BookIII.Hinge.no_free_parameters_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T42] No free parameters: all sector products are derivable from
the primorial tower, which is itself uniquely determined by the primes.
The primes are fixed by K0-K6. Hence: no knobs.
Equations
- Tau.BookIII.Hinge.no_free_parameters_check bound db = Tau.BookIII.Hinge.no_free_parameters_check.go 0 1 bound db ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Hinge.no_free_parameters_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L222-L242)@[irreducible]

**def
Tau.BookIII.Hinge.no_free_parameters_check.go
(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.coupling_uniqueness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L245-L255)
**def
Tau.BookIII.Hinge.coupling_uniqueness_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T42] Coupling uniqueness: at each enrichment level, the layer
template's invariant is uniquely determined (no choice involved).
E0: holomorphic (reduce-idempotent).
E1: orthogonal (e+ * e- = 0).
E2: self-correcting (triple-reduce stable).
E3: self-model (fixed point).
Equations
- Tau.BookIII.Hinge.coupling_uniqueness_check bound db = (Tau.BookIII.Enrichment.all_layers_valid bound db && Tau.BookIII.Arithmetic.tower_assembly_check bound db)
Instances For

---

### `Tau.BookIII.Hinge.no_knobs_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L257-L263)
**def
Tau.BookIII.Hinge.no_knobs_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T42] No-knobs check: iota_tau determines ratio + no free parameters


- coupling uniqueness. The single constant 341304/1000000 controls
everything downstream of the seven axioms.

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.hinge_assembly_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L269-L274)
**def
Tau.BookIII.Hinge.hinge_assembly_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T41 + III.T42] Full hinge assembly: hinge theorem + no-knobs
theorem + terminal completeness of the chain.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.hinge_theorem_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L317-L318)
**theorem
Tau.BookIII.Hinge.hinge_theorem_8_3 :hinge_theorem_check 8 3 = true**


---

### `Tau.BookIII.Hinge.sector_instantiation_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L320-L321)
**theorem
Tau.BookIII.Hinge.sector_instantiation_10_3 :sector_instantiation_check 10 3 = true**


---

### `Tau.BookIII.Hinge.level_coherence_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L323-L324)
**theorem
Tau.BookIII.Hinge.level_coherence_4 :level_coherence_check 4 = true**


---

### `Tau.BookIII.Hinge.enrichment_determines_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L326-L327)
**theorem
Tau.BookIII.Hinge.enrichment_determines_10_3 :enrichment_determines_sectors 10 3 = true**


---

### `Tau.BookIII.Hinge.no_knobs_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L330-L331)
**theorem
Tau.BookIII.Hinge.no_knobs_8_3 :no_knobs_check 8 3 = true**


---

### `Tau.BookIII.Hinge.iota_determines_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L333-L334)
**theorem
Tau.BookIII.Hinge.iota_determines_5 :iota_determines_ratio 5 = true**


---

### `Tau.BookIII.Hinge.no_free_params_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L336-L337)
**theorem
Tau.BookIII.Hinge.no_free_params_10_3 :no_free_parameters_check 10 3 = true**


---

### `Tau.BookIII.Hinge.coupling_uniqueness_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L339-L340)
**theorem
Tau.BookIII.Hinge.coupling_uniqueness_8_3 :coupling_uniqueness_check 8 3 = true**


---

### `Tau.BookIII.Hinge.hinge_assembly_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L343-L344)
**theorem
Tau.BookIII.Hinge.hinge_assembly_8_3 :hinge_assembly_check 8 3 = true**


---

### `Tau.BookIII.Hinge.hinge_chain_length`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L350-L352)
**theorem
Tau.BookIII.Hinge.hinge_chain_length :chain_links.length = 14**


[III.T41] Structural: the hinge chain has 14 links.

---

### `Tau.BookIII.Hinge.sector_product_depth_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L354-L357)
**theorem
Tau.BookIII.Hinge.sector_product_depth_3 :Doors.split_zeta_b 3 * Doors.split_zeta_c 3 * Doors.split_zeta_x 3 = Polarity.primorial 3**


[III.T41] Structural: B * C * X = Prim(3) = 30 at depth 3.

---

### `Tau.BookIII.Hinge.enrichment_strict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L359-L364)
**theorem
Tau.BookIII.Hinge.enrichment_strict :Enrichment.EnrLevel.E0.lt Enrichment.EnrLevel.E1 = true ∧ Enrichment.EnrLevel.E1.lt Enrichment.EnrLevel.E2 = true ∧ Enrichment.EnrLevel.E2.lt Enrichment.EnrLevel.E3 = true**


[III.T41] Structural: enrichment level ordering is strict.

---

### `Tau.BookIII.Hinge.iota_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L366-L368)
**theorem
Tau.BookIII.Hinge.iota_value :iota_numer = 341304 ∧ iota_denom = 1000000**


[III.T42] Structural: iota_tau approximation is 341304/1000000.

---

### `Tau.BookIII.Hinge.iota_lt_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L370-L371)
**theorem
Tau.BookIII.Hinge.iota_lt_one :iota_numer < iota_denom**


[III.T42] Structural: iota_tau < 1 (B is the minority channel).

---

### `Tau.BookIII.Hinge.iota_pos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L373-L374)
**theorem
Tau.BookIII.Hinge.iota_pos :iota_numer > 0**


[III.T42] Structural: iota_tau > 0 (master constant is positive).

---

### `Tau.BookIII.Hinge.iota_ratio_depth_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L376-L380)
**theorem
Tau.BookIII.Hinge.iota_ratio_depth_3 :sector_product Sectors.Sector.B 3 * iota_denom > sector_product Sectors.Sector.C 3 * iota_numer**


[III.T42] Structural: at depth 3, B/C > iota_tau (convergence not yet reached).
B*denom = 5*1000000 = 5000000 > C*numer = 3*341304 = 1023912.

---

### `Tau.BookIII.Hinge.iota_ratio_depth_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L382-L386)
**theorem
Tau.BookIII.Hinge.iota_ratio_depth_4 :sector_product Sectors.Sector.B 4 * iota_denom < sector_product Sectors.Sector.C 4 * iota_numer**


[III.T42] Structural: at depth 4, B/C < iota_tau (crossover).
B*denom = 5*1000000 = 5000000 < C*numer = 21*341304 = 7167384.

---

### `Tau.BookIII.Hinge.five_sectors_exhaustive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L388-L391)
**theorem
Tau.BookIII.Hinge.five_sectors_exhaustive
(s : Sectors.Sector)
 :s = Sectors.Sector.D ∨ s = Sectors.Sector.A ∨ s = Sectors.Sector.B ∨ s = Sectors.Sector.C ∨ s = Sectors.Sector.Omega**


[III.T42] Structural: the five sectors are exhaustive.

---

### `Tau.BookIII.Hinge.no_knobs_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L393-L398)
**theorem
Tau.BookIII.Hinge.no_knobs_witness :sector_product Sectors.Sector.B 3 = 5 ∧ sector_product Sectors.Sector.C 3 = 3 ∧ sector_product Sectors.Sector.Omega 3 = 2**


[III.T42] Structural: no-knobs means sector products are derivable.
At depth 3: B=5, C=3, X=2, and 5*3*2 = 30 = Prim(3).

---

### `Tau.BookIII.Hinge.hinge_point`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Hinge/HingeTheorem.lean#L400-L405)
**theorem
Tau.BookIII.Hinge.hinge_point :ChainLink.K6.succ = ChainLink.E0 ∧ ChainLink.E0.toEnrLevel = Enrichment.EnrLevel.E0**


[III.T41] Structural: the axiom-to-enrichment transition at K6 -> E0
is the hinge point where Books I-II feed into Book III.
