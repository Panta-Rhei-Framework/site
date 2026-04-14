---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.ZFCasVM"
permalink: /verify/taulib/docs/book-iii-bridge-zf-cas-vm/
lane: verify
module_name: "TauLib.BookIII.Bridge.ZFCasVM"
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

# TauLib.BookIII.Bridge.ZFCasVM


ZFC as an E2 Virtual Machine: modeling ZFC axioms within the layer template.

## Registry Cross-References


- [III.D67] ZFC as E2 VM -- `ZFCAxiom`, `zfc_vm_check`

- [III.D68] ZFC Axiom Encoding -- `axiom_encoding_check`

- [III.D70] Set-Theoretic Universe -- `set_universe_check`


## Mathematical Content


**III.D67 (ZFC as E2 VM):** ZFC characterised as an E2 virtual machine using
the Layer Template: Carrier = formal sentences, Predicate = derivability,
Decoder = Godel numbering, Invariant = consistency. ZFC cannot live at E0
(no execution) or E1 (no codes). tau and ZFC are two different E2 VMs.

**III.D68 (Godel Numbering as NF Address):** Each ZFC axiom encoded as a
BNF operation on tau-addresses. Godel numbering is the NF-address system
of the ZFC-VM's code space: injective, primitive-recursive decoder,
self-referential via the diagonal lemma.

**III.D70 (Host-Level Property):** A host-level property quantifies over the
totality of a VM's execution histories. Consistency, halting, and completeness
are host-level. The cumulative hierarchy V_alpha as a tower of primorial levels:
at each primorial depth k, the "sets of rank <= k" are tau-addresses < Prim(k).

---

### `Tau.BookIII.Bridge.ZFCAxiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L43-L55)
**inductive
Tau.BookIII.Bridge.ZFCAxiom :Type**


[III.D67] The ZFC axioms modeled as operations on tau-addresses.
Each axiom corresponds to a modular operation at primorial level k.

- extensionality : ZFCAxiom
- pairing : ZFCAxiom
- union : ZFCAxiom
- powerset : ZFCAxiom
- infinity : ZFCAxiom
- separation : ZFCAxiom
- replacement : ZFCAxiom
- foundation : ZFCAxiom
- choice : ZFCAxiom
Instances For

---

### `Tau.BookIII.Bridge.instReprZFCAxiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L55-L55)
**instance
Tau.BookIII.Bridge.instReprZFCAxiom :Repr ZFCAxiom**

Equations
- Tau.BookIII.Bridge.instReprZFCAxiom = { reprPrec := Tau.BookIII.Bridge.instReprZFCAxiom.repr }

---

### `Tau.BookIII.Bridge.instReprZFCAxiom.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L55-L55)
**def
Tau.BookIII.Bridge.instReprZFCAxiom.repr :ZFCAxiom → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instDecidableEqZFCAxiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L55-L55)
**instance
Tau.BookIII.Bridge.instDecidableEqZFCAxiom :DecidableEq ZFCAxiom**

Equations
- Tau.BookIII.Bridge.instDecidableEqZFCAxiom x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqZFCAxiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L55-L55)
**instance
Tau.BookIII.Bridge.instBEqZFCAxiom :BEq ZFCAxiom**

Equations
- Tau.BookIII.Bridge.instBEqZFCAxiom = { beq := Tau.BookIII.Bridge.instBEqZFCAxiom.beq }

---

### `Tau.BookIII.Bridge.instBEqZFCAxiom.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L55-L55)
**def
Tau.BookIII.Bridge.instBEqZFCAxiom.beq :ZFCAxiom → ZFCAxiom → Bool**

Equations
- Tau.BookIII.Bridge.instBEqZFCAxiom.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.zfc_axiom_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L57-L58)
**def
Tau.BookIII.Bridge.zfc_axiom_count :ℕ**


Number of ZFC axioms.
Equations
- Tau.BookIII.Bridge.zfc_axiom_count = 9
Instances For

---

### `Tau.BookIII.Bridge.axiom_min_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L60-L71)
**def
Tau.BookIII.Bridge.axiom_min_depth :ZFCAxiom → ℕ**


[III.D68] Each axiom has a primorial depth requirement: the minimum
depth k at which the axiom's operation is expressible.
Equations
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.extensionality = 1
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.pairing = 1
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.union = 2
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.powerset = 2
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.infinity = 3
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.separation = 1
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.replacement = 2
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.foundation = 1
- Tau.BookIII.Bridge.axiom_min_depth Tau.BookIII.Bridge.ZFCAxiom.choice = 2
Instances For

---

### `Tau.BookIII.Bridge.axiom_operation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L73-L99)
**def
Tau.BookIII.Bridge.axiom_operation
(ax : ZFCAxiom)

(a b k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D68] Encoding of a ZFC axiom as a tau-address operation.
Each axiom maps (a, b) to a result at primorial depth k.
Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Bridge.axiom_operation Tau.BookIII.Bridge.ZFCAxiom.union a b k = if (Tau.Polarity.primorial k == 0) = true then 0 else (a + b) % Tau.Polarity.primorial k
- Tau.BookIII.Bridge.axiom_operation Tau.BookIII.Bridge.ZFCAxiom.powerset a b k = if (Tau.Polarity.primorial k == 0) = true then 0 else a * a % Tau.Polarity.primorial k
- Tau.BookIII.Bridge.axiom_operation Tau.BookIII.Bridge.ZFCAxiom.infinity a b k = if (Tau.Polarity.primorial k == 0) = true then 0 else (a + 1) % Tau.Polarity.primorial k
- Tau.BookIII.Bridge.axiom_operation Tau.BookIII.Bridge.ZFCAxiom.replacement a b k = if (Tau.Polarity.primorial k == 0) = true then 0 else a * (b + 1) % Tau.Polarity.primorial k
- Tau.BookIII.Bridge.axiom_operation Tau.BookIII.Bridge.ZFCAxiom.foundation a b k = if (Tau.Polarity.primorial k == 0) = true then 0 else a % Tau.Polarity.primorial k / 2
Instances For

---

### `Tau.BookIII.Bridge.zfc_vm_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L101-L116)
**def
Tau.BookIII.Bridge.zfc_vm_layer
(bound db : Denotation.TauIdx)
 :Enrichment.LayerTemplate**


[III.D67] ZFC VM layer template: the four-component template specialized
for the ZFC virtual machine at E2.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.zfc_vm_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L118-L147)
**def
Tau.BookIII.Bridge.zfc_vm_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D67] ZFC VM check: verify that the ZFC layer template is valid at E2.
Each axiom operation produces a valid tau-address within primorial range.
Equations
- Tau.BookIII.Bridge.zfc_vm_check bound db = Tau.BookIII.Bridge.zfc_vm_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.zfc_vm_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L123-L146)@[irreducible]

**def
Tau.BookIII.Bridge.zfc_vm_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.axiom_encoding_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L153-L186)
**def
Tau.BookIII.Bridge.axiom_encoding_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D68] Axiom encoding check: verify that each axiom is expressible
at its minimum depth and all depths above it.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.axiom_encoding_check.next_axiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L159-L169)
**def
Tau.BookIII.Bridge.axiom_encoding_check.next_axiom
(ax : ZFCAxiom)
 :Option ZFCAxiom**


All axioms to check.
Equations
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.extensionality = some Tau.BookIII.Bridge.ZFCAxiom.pairing
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.pairing = some Tau.BookIII.Bridge.ZFCAxiom.union
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.union = some Tau.BookIII.Bridge.ZFCAxiom.powerset
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.powerset = some Tau.BookIII.Bridge.ZFCAxiom.infinity
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.infinity = some Tau.BookIII.Bridge.ZFCAxiom.separation
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.separation = some Tau.BookIII.Bridge.ZFCAxiom.replacement
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.replacement = some Tau.BookIII.Bridge.ZFCAxiom.foundation
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.foundation = some Tau.BookIII.Bridge.ZFCAxiom.choice
- Tau.BookIII.Bridge.axiom_encoding_check.next_axiom Tau.BookIII.Bridge.ZFCAxiom.choice = none
Instances For

---

### `Tau.BookIII.Bridge.axiom_encoding_check.go_ax`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L170-L185)@[irreducible]

**def
Tau.BookIII.Bridge.axiom_encoding_check.go_ax
(bound db : Denotation.TauIdx)

(ax : ZFCAxiom)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.universe_rank`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L192-L194)
**def
Tau.BookIII.Bridge.universe_rank
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D70] Cumulative hierarchy V_k: sets of rank <= k are
tau-addresses x < Prim(k). The universe grows strictly with k.
Equations
- Tau.BookIII.Bridge.universe_rank k = Tau.Polarity.primorial k
Instances For

---

### `Tau.BookIII.Bridge.set_universe_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L196-L215)
**def
Tau.BookIII.Bridge.set_universe_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D70] Set-theoretic universe check: the cumulative hierarchy
V_0 subset V_1 subset ... is modeled by the primorial tower.
Equations
- Tau.BookIII.Bridge.set_universe_check bound db = Tau.BookIII.Bridge.set_universe_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.set_universe_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L201-L214)@[irreducible]

**def
Tau.BookIII.Bridge.set_universe_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.host_level_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L217-L235)
**def
Tau.BookIII.Bridge.host_level_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D70] Host-level property: a property that quantifies over the
entire code space. Consistency is the paradigmatic host-level property.
Modeled as: for all codes, no code crashes the VM (reduce is total).
Equations
- Tau.BookIII.Bridge.host_level_check bound db = Tau.BookIII.Bridge.host_level_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.host_level_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L223-L234)@[irreducible]

**def
Tau.BookIII.Bridge.host_level_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.zfc_vm_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L263-L264)
**theorem
Tau.BookIII.Bridge.zfc_vm_8_3 :zfc_vm_check 8 3 = true**


---

### `Tau.BookIII.Bridge.axiom_encoding_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L267-L268)
**theorem
Tau.BookIII.Bridge.axiom_encoding_8_3 :axiom_encoding_check 8 3 = true**


---

### `Tau.BookIII.Bridge.set_universe_10_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L271-L272)
**theorem
Tau.BookIII.Bridge.set_universe_10_4 :set_universe_check 10 4 = true**


---

### `Tau.BookIII.Bridge.host_level_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L275-L276)
**theorem
Tau.BookIII.Bridge.host_level_10_3 :host_level_check 10 3 = true**


---

### `Tau.BookIII.Bridge.zfc_has_9_axioms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L282-L283)
**theorem
Tau.BookIII.Bridge.zfc_has_9_axioms :zfc_axiom_count = 9**


[III.D67] Structural: ZFC has exactly 9 axioms.

---

### `Tau.BookIII.Bridge.zfc_is_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L285-L286)
**theorem
Tau.BookIII.Bridge.zfc_is_e2 :Enrichment.EnrLevel.E2.toNat = 2**


[III.D67] Structural: ZFC is at E2 (not E0 or E1).

---

### `Tau.BookIII.Bridge.ext_min_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L288-L289)
**theorem
Tau.BookIII.Bridge.ext_min_depth :axiom_min_depth ZFCAxiom.extensionality = 1**


[III.D68] Structural: extensionality needs depth >= 1.

---

### `Tau.BookIII.Bridge.inf_min_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L291-L292)
**theorem
Tau.BookIII.Bridge.inf_min_depth :axiom_min_depth ZFCAxiom.infinity = 3**


[III.D68] Structural: infinity needs depth >= 3.

---

### `Tau.BookIII.Bridge.universe_rank_0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L294-L295)
**theorem
Tau.BookIII.Bridge.universe_rank_0 :universe_rank 0 = 1**


[III.D70] Structural: V_0 = Prim(0) = 1 (singleton universe).

---

### `Tau.BookIII.Bridge.universe_rank_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L297-L298)
**theorem
Tau.BookIII.Bridge.universe_rank_3 :universe_rank 3 = 30**


[III.D70] Structural: V_3 = 30 (primorial 3).

---

### `Tau.BookIII.Bridge.pairing_valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L300-L302)
**theorem
Tau.BookIII.Bridge.pairing_valid :axiom_operation ZFCAxiom.pairing 3 5 3 < 30**


[III.D67] Structural: pairing at depth 3 produces valid result.

---

### `Tau.BookIII.Bridge.ext_detects_equal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L304-L306)
**theorem
Tau.BookIII.Bridge.ext_detects_equal :axiom_operation ZFCAxiom.extensionality 3 3 3 = 1**


[III.D67] Structural: extensionality detects equality.

---

### `Tau.BookIII.Bridge.ext_detects_unequal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ZFCasVM.lean#L308-L310)
**theorem
Tau.BookIII.Bridge.ext_detects_unequal :axiom_operation ZFCAxiom.extensionality 3 5 3 = 0**


[III.D67] Structural: extensionality detects inequality.
