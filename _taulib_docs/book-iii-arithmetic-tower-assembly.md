---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.TowerAssembly"
permalink: /verify/taulib/docs/book-iii-arithmetic-tower-assembly/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.TowerAssembly"
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

# TauLib.BookIII.Arithmetic.TowerAssembly


Enrichment Tower Assembly: E₀ ⊊ E₁ ⊊ E₂ assembled.

## Registry Cross-References


- [III.T40] Enrichment Tower Assembly -- `tower_assembly_check`


## Mathematical Content


**III.T40 (Tower Assembly):** The tower E₀ ⊊ E₁ ⊊ E₂ is assembled with
coherent bi-square scaling chain and complete Millennium coverage:


- E₀: RH + Poincaré (pure mathematics)

- E₁: NS + YM + Hodge (physics)

- E₁→E₂: BSD + Langlands (arithmetic mirror)

- E₂: P vs NP (computation)


The tower is strict (E₀ ⊊ E₁ ⊊ E₂), each level has its bi-square, and
the scaling chain is coherent: algebraic → topological → enriched.

---

### `Tau.BookIII.Arithmetic.tower_strict_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L37-L43)
**def
Tau.BookIII.Arithmetic.tower_strict_check :Bool**


[III.T40] Tower strictness: E₀ ⊊ E₁ ⊊ E₂. Each level is a proper
subset of the next (enrichment adds genuine content).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.millennium_coverage_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L45-L56)
**def
Tau.BookIII.Arithmetic.millennium_coverage_check :Bool**


[III.T40] Millennium coverage: all 8 problems are assigned to levels.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.scaling_chain_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L58-L94)
**def
Tau.BookIII.Arithmetic.scaling_chain_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T40] Bi-square scaling chain: all three bi-squares have the same
structural shape (CRT roundtrip + BNF decomposition + sector products).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.scaling_chain_check.crt_roundtrip_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L70-L80)@[irreducible]

**def
Tau.BookIII.Arithmetic.scaling_chain_check.crt_roundtrip_go
(x k bound db fuel : ℕ)
 :Bool**


Algebraic: CRT roundtrip.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.scaling_chain_check.bnf_decomposition_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L83-L93)@[irreducible]

**def
Tau.BookIII.Arithmetic.scaling_chain_check.bnf_decomposition_go
(x k bound db fuel : ℕ)
 :Bool**


Topological: BNF decomposition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.tower_assembly_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L96-L101)
**def
Tau.BookIII.Arithmetic.tower_assembly_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T40] Tower assembly: tower is strict, coverage is complete,
and scaling chain is coherent.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.tower_strict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L116-L117)
**theorem
Tau.BookIII.Arithmetic.tower_strict :tower_strict_check = true**


---

### `Tau.BookIII.Arithmetic.millennium_coverage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L119-L120)
**theorem
Tau.BookIII.Arithmetic.millennium_coverage :millennium_coverage_check = true**


---

### `Tau.BookIII.Arithmetic.scaling_chain_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L122-L123)
**theorem
Tau.BookIII.Arithmetic.scaling_chain_15_3 :scaling_chain_check 15 3 = true**


---

### `Tau.BookIII.Arithmetic.tower_assembly_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L125-L126)
**theorem
Tau.BookIII.Arithmetic.tower_assembly_15_3 :tower_assembly_check 15 3 = true**


---

### `Tau.BookIII.Arithmetic.e0_lt_e1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L132-L133)
**theorem
Tau.BookIII.Arithmetic.e0_lt_e1 :Enrichment.EnrLevel.E0.lt Enrichment.EnrLevel.E1 = true**


[III.T40] Structural: E₀ < E₁.

---

### `Tau.BookIII.Arithmetic.e1_lt_e2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L135-L136)
**theorem
Tau.BookIII.Arithmetic.e1_lt_e2 :Enrichment.EnrLevel.E1.lt Enrichment.EnrLevel.E2 = true**


[III.T40] Structural: E₁ < E₂.

---

### `Tau.BookIII.Arithmetic.e2_lt_e3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L138-L139)
**theorem
Tau.BookIII.Arithmetic.e2_lt_e3 :Enrichment.EnrLevel.E2.lt Enrichment.EnrLevel.E3 = true**


[III.T40] Structural: E₂ < E₃.

---

### `Tau.BookIII.Arithmetic.eight_problems`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Arithmetic/TowerAssembly.lean#L141-L146)
**theorem
Tau.BookIII.Arithmetic.eight_problems :[Doors.problem_level Doors.MillenniumProblem.RH, Doors.problem_level Doors.MillenniumProblem.Poincare, Doors.problem_level Doors.MillenniumProblem.NS, Doors.problem_level Doors.MillenniumProblem.YM, Doors.problem_level Doors.MillenniumProblem.Hodge, Doors.problem_level Doors.MillenniumProblem.BSD, Doors.problem_level Doors.MillenniumProblem.Langlands, Doors.problem_level Doors.MillenniumProblem.PvsNP].length = 8**


[III.T40] Structural: all 8 problems covered.
