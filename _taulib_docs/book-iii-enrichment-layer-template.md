---
layout: taulib-doc
title: "TauLib.BookIII.Enrichment.LayerTemplate"
permalink: /verify/taulib/docs/book-iii-enrichment-layer-template/
lane: verify
module_name: "TauLib.BookIII.Enrichment.LayerTemplate"
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

# TauLib.BookIII.Enrichment.LayerTemplate


The 4-level enrichment ladder and the uniform layer template.

## Registry Cross-References


- [III.D05] Layer Template -- `LayerTemplate`, `layer_template_check`

- [III.D06] E₀ Layer (Mathematics) -- `e0_layer`

- [III.D07] E₁ Layer (Physics) -- `e1_layer_book3`

- [III.D08] E₂ Layer (Computation) -- `e2_layer`

- [III.D09] E₃ Layer (Metaphysics) -- `e3_layer`


## Mathematical Content


**III.D05 (Layer Template):** Each enrichment layer E_k has a uniform
four-component structure: E_k = (Carrier_k, Predicate_k, Decoder_k,
Invariant_k). The template is preserved under enrichment: each layer's
invariant flows into the next layer's carrier.

**III.D06-D09:** Concrete instantiations at each enrichment level:


- E₀: NF-addressed τ-objects, NF-addressability, peel map Φ, holomorphic O(τ³)

- E₁: H_τ-enriched objects, sector admissibility, spectral projection, sector couplings

- E₂: Self-referential codes, operational closure, phenotype map, error-correction

- E₃: Self-modeling codes, self-model consistency, meaning assignment, self-awareness


## Architecture Decision: EnrLevel Extension


Book II defines `EnrichmentLevel` as `E0 | E1`. Book III defines a NEW
`EnrLevel` type with all four levels + coercion from Book II's type.
This avoids modifying Book II code.

---

### `Tau.BookIII.Enrichment.EnrLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L47-L54)
**inductive
Tau.BookIII.Enrichment.EnrLevel :Type**


Book III enrichment levels: E₀ through E₃.
Extends Book II's 2-level `EnrichmentLevel` to the full 4-level ladder.

- E0 : EnrLevel
- E1 : EnrLevel
- E2 : EnrLevel
- E3 : EnrLevel
Instances For

---

### `Tau.BookIII.Enrichment.instReprEnrLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**def
Tau.BookIII.Enrichment.instReprEnrLevel.repr :EnrLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.instReprEnrLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**instance
Tau.BookIII.Enrichment.instReprEnrLevel :Repr EnrLevel**

Equations
- Tau.BookIII.Enrichment.instReprEnrLevel = { reprPrec := Tau.BookIII.Enrichment.instReprEnrLevel.repr }

---

### `Tau.BookIII.Enrichment.instDecidableEqEnrLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**instance
Tau.BookIII.Enrichment.instDecidableEqEnrLevel :DecidableEq EnrLevel**

Equations
- Tau.BookIII.Enrichment.instDecidableEqEnrLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Enrichment.instBEqEnrLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**instance
Tau.BookIII.Enrichment.instBEqEnrLevel :BEq EnrLevel**

Equations
- Tau.BookIII.Enrichment.instBEqEnrLevel = { beq := Tau.BookIII.Enrichment.instBEqEnrLevel.beq }

---

### `Tau.BookIII.Enrichment.instBEqEnrLevel.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**def
Tau.BookIII.Enrichment.instBEqEnrLevel.beq :EnrLevel → EnrLevel → Bool**

Equations
- Tau.BookIII.Enrichment.instBEqEnrLevel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Enrichment.instInhabitedEnrLevel.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**def
Tau.BookIII.Enrichment.instInhabitedEnrLevel.default :EnrLevel**

Equations
- Tau.BookIII.Enrichment.instInhabitedEnrLevel.default = Tau.BookIII.Enrichment.EnrLevel.E0
Instances For

---

### `Tau.BookIII.Enrichment.instInhabitedEnrLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L54-L54)
**instance
Tau.BookIII.Enrichment.instInhabitedEnrLevel :Inhabited EnrLevel**

Equations
- Tau.BookIII.Enrichment.instInhabitedEnrLevel = { default := Tau.BookIII.Enrichment.instInhabitedEnrLevel.default }

---

### `Tau.BookIII.Enrichment.EnrLevel.ofBookII`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L56-L59)
**def
Tau.BookIII.Enrichment.EnrLevel.ofBookII :BookII.Enrichment.EnrichmentLevel → EnrLevel**


Coercion from Book II's 2-level enrichment to Book III's 4-level.
Equations
- Tau.BookIII.Enrichment.EnrLevel.ofBookII Tau.BookII.Enrichment.EnrichmentLevel.E0 = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Enrichment.EnrLevel.ofBookII Tau.BookII.Enrichment.EnrichmentLevel.E1 = Tau.BookIII.Enrichment.EnrLevel.E1
Instances For

---

### `Tau.BookIII.Enrichment.EnrLevel.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L61-L66)
**def
Tau.BookIII.Enrichment.EnrLevel.toNat :EnrLevel → ℕ**


Numeric index of an enrichment level.
Equations
- Tau.BookIII.Enrichment.EnrLevel.E0.toNat = 0
- Tau.BookIII.Enrichment.EnrLevel.E1.toNat = 1
- Tau.BookIII.Enrichment.EnrLevel.E2.toNat = 2
- Tau.BookIII.Enrichment.EnrLevel.E3.toNat = 3
Instances For

---

### `Tau.BookIII.Enrichment.EnrLevel.lt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L68-L70)
**def
Tau.BookIII.Enrichment.EnrLevel.lt
(a b : EnrLevel)
 :Bool**


Enrichment level ordering: E₀ < E₁ < E₂ < E₃.
Equations
- a.lt b = decide (a.toNat < b.toNat)
Instances For

---

### `Tau.BookIII.Enrichment.EnrLevel.le`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L72-L74)
**def
Tau.BookIII.Enrichment.EnrLevel.le
(a b : EnrLevel)
 :Bool**


Enrichment level ordering: E₀ ≤ E₁ ≤ E₂ ≤ E₃.
Equations
- a.le b = decide (a.toNat ≤ b.toNat)
Instances For

---

### `Tau.BookIII.Enrichment.EnrLevel.succ`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L76-L81)
**def
Tau.BookIII.Enrichment.EnrLevel.succ :EnrLevel → EnrLevel**


Successor enrichment level (saturates at E₃).
Equations
- Tau.BookIII.Enrichment.EnrLevel.E0.succ = Tau.BookIII.Enrichment.EnrLevel.E1
- Tau.BookIII.Enrichment.EnrLevel.E1.succ = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Enrichment.EnrLevel.E2.succ = Tau.BookIII.Enrichment.EnrLevel.E3
- Tau.BookIII.Enrichment.EnrLevel.E3.succ = Tau.BookIII.Enrichment.EnrLevel.E3
Instances For

---

### `Tau.BookIII.Enrichment.LayerTemplate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L87-L106)
**structure
Tau.BookIII.Enrichment.LayerTemplate :Type**


[III.D05] The uniform four-component layer template.
Each enrichment layer E_k instantiates this with specific
carrier, predicate, decoder, and invariant functions.

The template captures the structural pattern:


- Carrier: the objects that live at this level

- Predicate: the admissibility condition for carrier elements

- Decoder: the projection/extraction map (one level down)

- Invariant: the structure preserved at this level


Template flow: E_k.invariant → E_{k+1}.carrier

- carrier_check : Denotation.TauIdx → Denotation.TauIdx → Bool
Carrier check: is x a valid carrier element at stage k?

- predicate_check : Denotation.TauIdx → Denotation.TauIdx → Bool
Predicate check: does x satisfy the admissibility predicate?

- decoder : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx
Decoder: project x from this layer to the previous.

- invariant_check : Denotation.TauIdx → Denotation.TauIdx → Bool
Invariant check: is the layer invariant satisfied?

Instances For

---

### `Tau.BookIII.Enrichment.layer_template_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L108-L130)
**def
Tau.BookIII.Enrichment.layer_template_check
(lt : LayerTemplate)

(bound db : Denotation.TauIdx)
 :Bool**


[III.D05] Layer template completeness: all four components present
and consistent at given parameters.
Equations
- Tau.BookIII.Enrichment.layer_template_check lt bound db = Tau.BookIII.Enrichment.layer_template_check.go lt bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Enrichment.layer_template_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L113-L129)@[irreducible]

**def
Tau.BookIII.Enrichment.layer_template_check.go
(lt : LayerTemplate)

(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.e0_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L136-L151)
**def
Tau.BookIII.Enrichment.e0_layer
(bound db : Denotation.TauIdx)
 :LayerTemplate**


[III.D06] E₀ Layer: the mathematical kernel (Books I-III).


- Carrier: τ-objects with NF addressing (x < P_k)

- Predicate: NF-addressability (reduce is identity on valid elements)

- Decoder: peel map Φ — ABCD extraction

- Invariant: holomorphic structure (reduce-compatibility)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.e1_layer_book3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L157-L188)
**def
Tau.BookIII.Enrichment.e1_layer_book3
(bound db : Denotation.TauIdx)
 :LayerTemplate**


[III.D07] E₁ Layer: the physics layer (Books IV-V).


- Carrier: H_τ-enriched objects (hom-stage well-defined)

- Predicate: sector admissibility (bipolar decomposition exists)

- Decoder: spectral projection (e₊/e₋ decomposition)

- Invariant: sector coupling canonicality


This EXTENDS Book II's E1Layer with sector structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.e2_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L194-L218)
**def
Tau.BookIII.Enrichment.e2_layer
(bound db : Denotation.TauIdx)
 :LayerTemplate**


[III.D08] E₂ Layer: the computation layer (Book VI).


- Carrier: self-referential codes (address = program)

- Predicate: operational closure (D(C) produces another code)

- Decoder: phenotype map (code → observable behavior)

- Invariant: error-correction capacity


At E₂, the code IS a τ-address. The τ-Tower Machine (TTM)
from Book I is the structural template.
Equations
- One or more equations did not get rendered due to their size.
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Enrichment.e3_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L230-L267)
**def
Tau.BookIII.Enrichment.e3_layer
(bound db : Denotation.TauIdx)
 :LayerTemplate**


[III.D09] E₃ Layer: the metaphysics layer (Book VII).


- Carrier: self-modeling codes (model their own observation)

- Predicate: self-model consistency

- Decoder: meaning/interpretation assignment

- Invariant: self-awareness capacity


At E₃, the code models its own modeling process.
E₃ is terminal: E₄ = E₃ (self-modeling of self-modeling
is still self-modeling).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.layer_of`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L273-L279)
**def
Tau.BookIII.Enrichment.layer_of
(lev : EnrLevel)

(bound db : Denotation.TauIdx)
 :LayerTemplate**


Get the layer template for a given enrichment level.
Equations
- Tau.BookIII.Enrichment.layer_of Tau.BookIII.Enrichment.EnrLevel.E0 bound db = Tau.BookIII.Enrichment.e0_layer bound db
- Tau.BookIII.Enrichment.layer_of Tau.BookIII.Enrichment.EnrLevel.E1 bound db = Tau.BookIII.Enrichment.e1_layer_book3 bound db
- Tau.BookIII.Enrichment.layer_of Tau.BookIII.Enrichment.EnrLevel.E2 bound db = Tau.BookIII.Enrichment.e2_layer bound db
- Tau.BookIII.Enrichment.layer_of Tau.BookIII.Enrichment.EnrLevel.E3 bound db = Tau.BookIII.Enrichment.e3_layer bound db
Instances For

---

### `Tau.BookIII.Enrichment.layer_valid_at`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L281-L283)
**def
Tau.BookIII.Enrichment.layer_valid_at
(lev : EnrLevel)

(bound db : Denotation.TauIdx)
 :Bool**


Check that the layer template is valid at a given enrichment level.
Equations
- Tau.BookIII.Enrichment.layer_valid_at lev bound db = Tau.BookIII.Enrichment.layer_template_check (Tau.BookIII.Enrichment.layer_of lev bound db) bound db
Instances For

---

### `Tau.BookIII.Enrichment.all_layers_valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L285-L290)
**def
Tau.BookIII.Enrichment.all_layers_valid
(bound db : Denotation.TauIdx)
 :Bool**


Check all four layers are valid.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.e0_layer_valid_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L338-L339)
**theorem
Tau.BookIII.Enrichment.e0_layer_valid_8_3 :layer_valid_at EnrLevel.E0 8 3 = true**


---

### `Tau.BookIII.Enrichment.e1_layer_valid_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L342-L343)
**theorem
Tau.BookIII.Enrichment.e1_layer_valid_8_3 :layer_valid_at EnrLevel.E1 8 3 = true**


---

### `Tau.BookIII.Enrichment.e2_layer_valid_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L346-L347)
**theorem
Tau.BookIII.Enrichment.e2_layer_valid_8_3 :layer_valid_at EnrLevel.E2 8 3 = true**


---

### `Tau.BookIII.Enrichment.e3_layer_valid_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L350-L351)
**theorem
Tau.BookIII.Enrichment.e3_layer_valid_8_3 :layer_valid_at EnrLevel.E3 8 3 = true**


---

### `Tau.BookIII.Enrichment.all_layers_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L354-L355)
**theorem
Tau.BookIII.Enrichment.all_layers_8_3 :all_layers_valid 8 3 = true**


---

### `Tau.BookIII.Enrichment.enr_le_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L361-L364)
**theorem
Tau.BookIII.Enrichment.enr_le_total
(a b : EnrLevel)
 :a.le b = true ∨ b.le a = true**


EnrLevel ordering is total: for any two levels, one ≤ the other.

---

### `Tau.BookIII.Enrichment.e3_saturates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L366-L367)
**theorem
Tau.BookIII.Enrichment.e3_saturates :EnrLevel.E3.succ = EnrLevel.E3**


E₃ is maximal: E₃.succ = E₃ (saturation).

---

### `Tau.BookIII.Enrichment.e0_ne_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L369-L370)
**theorem
Tau.BookIII.Enrichment.e0_ne_e1 :EnrLevel.E0 ≠ EnrLevel.E1**


Enrichment levels are distinct.

---

### `Tau.BookIII.Enrichment.e1_ne_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L371-L371)
**theorem
Tau.BookIII.Enrichment.e1_ne_e2 :EnrLevel.E1 ≠ EnrLevel.E2**


---

### `Tau.BookIII.Enrichment.e2_ne_e3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L372-L372)
**theorem
Tau.BookIII.Enrichment.e2_ne_e3 :EnrLevel.E2 ≠ EnrLevel.E3**


---

### `Tau.BookIII.Enrichment.coercion_preserves_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L374-L377)
**theorem
Tau.BookIII.Enrichment.coercion_preserves_order :(EnrLevel.ofBookII BookII.Enrichment.EnrichmentLevel.E0).lt (EnrLevel.ofBookII BookII.Enrichment.EnrichmentLevel.E1) = true**


Coercion preserves order: if E0 < E1 in Book II, then ofBookII preserves this.

---

### `Tau.BookIII.Enrichment.e0_carrier_small`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/LayerTemplate.lean#L379-L383)
**theorem
Tau.BookIII.Enrichment.e0_carrier_small
(x k : Denotation.TauIdx)

(h : x < Polarity.primorial k)
 :(e0_layer 10 3).carrier_check x k = true**


The layer template at E₀ has a total carrier for small values.
