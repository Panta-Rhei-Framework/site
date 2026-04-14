---
layout: taulib-doc
title: "TauLib.BookIII.Hinge.DependencyChain"
permalink: /verify/taulib/docs/book-iii-hinge-dependency-chain/
lane: verify
module_name: "TauLib.BookIII.Hinge.DependencyChain"
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

# TauLib.BookIII.Hinge.DependencyChain


Complete Dependency Chain from K0 through E3+: the 14-link backbone.

## Registry Cross-References


- [III.D66] Complete Dependency Chain -- `dependency_chain_check`

- [III.P29] Chain Linearity -- `chain_linearity_check`

- [III.P30] Terminal Completeness -- `terminal_completeness_check`


## Mathematical Content


**III.D66 (Complete Dependency Chain):** The 14-link dependency chain
K0 -> K1 -> ... -> K6 -> E0 -> E1 -> E1+ -> E2 -> E2+ -> E3 -> E3+
is the backbone of the entire Panta Rhei series. Each link builds on the
previous: the seven axioms (K0-K6) construct tau^3, the four enrichment
levels (E0-E3) stratify the content, and the three plus-levels (E1+, E2+,
E3+) mark the interfaces where enrichment genuinely expands.

**III.P29 (Chain Linearity):** The chain has no cycles. Each link's index
is strictly greater than the previous. This ensures the dependency is a
total order, not a lattice.

**III.P30 (Terminal Completeness):** The chain covers all enrichment levels.
E0 through E3 each appear as a link, and E3+ is the terminal node.
After E3+, the chain saturates (E4 = E3).

---

### `Tau.BookIII.Hinge.ChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L44-L63)
**inductive
Tau.BookIII.Hinge.ChainLink :Type**


A link in the 14-step dependency chain.
K0-K6 = the seven axioms (Book I construction).
E0-E3 = the four enrichment levels (Books I-VII).
E1p, E2p, E3p = the plus-interfaces (enrichment transitions).

- K0 : ChainLink
- K1 : ChainLink
- K2 : ChainLink
- K3 : ChainLink
- K4 : ChainLink
- K5 : ChainLink
- K6 : ChainLink
- E0 : ChainLink
- E1 : ChainLink
- E1p : ChainLink
- E2 : ChainLink
- E2p : ChainLink
- E3 : ChainLink
- E3p : ChainLink
Instances For

---

### `Tau.BookIII.Hinge.instReprChainLink.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**def
Tau.BookIII.Hinge.instReprChainLink.repr :ChainLink → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.instReprChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**instance
Tau.BookIII.Hinge.instReprChainLink :Repr ChainLink**

Equations
- Tau.BookIII.Hinge.instReprChainLink = { reprPrec := Tau.BookIII.Hinge.instReprChainLink.repr }

---

### `Tau.BookIII.Hinge.instDecidableEqChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**instance
Tau.BookIII.Hinge.instDecidableEqChainLink :DecidableEq ChainLink**

Equations
- Tau.BookIII.Hinge.instDecidableEqChainLink x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Hinge.instBEqChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**instance
Tau.BookIII.Hinge.instBEqChainLink :BEq ChainLink**

Equations
- Tau.BookIII.Hinge.instBEqChainLink = { beq := Tau.BookIII.Hinge.instBEqChainLink.beq }

---

### `Tau.BookIII.Hinge.instBEqChainLink.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**def
Tau.BookIII.Hinge.instBEqChainLink.beq :ChainLink → ChainLink → Bool**

Equations
- Tau.BookIII.Hinge.instBEqChainLink.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Hinge.instInhabitedChainLink.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**def
Tau.BookIII.Hinge.instInhabitedChainLink.default :ChainLink**

Equations
- Tau.BookIII.Hinge.instInhabitedChainLink.default = Tau.BookIII.Hinge.ChainLink.K0
Instances For

---

### `Tau.BookIII.Hinge.instInhabitedChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L63-L63)
**instance
Tau.BookIII.Hinge.instInhabitedChainLink :Inhabited ChainLink**

Equations
- Tau.BookIII.Hinge.instInhabitedChainLink = { default := Tau.BookIII.Hinge.instInhabitedChainLink.default }

---

### `Tau.BookIII.Hinge.ChainLink.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L65-L80)
**def
Tau.BookIII.Hinge.ChainLink.toNat :ChainLink → ℕ**


Numeric position of each link in the chain (0-indexed).
Equations
- Tau.BookIII.Hinge.ChainLink.K0.toNat = 0
- Tau.BookIII.Hinge.ChainLink.K1.toNat = 1
- Tau.BookIII.Hinge.ChainLink.K2.toNat = 2
- Tau.BookIII.Hinge.ChainLink.K3.toNat = 3
- Tau.BookIII.Hinge.ChainLink.K4.toNat = 4
- Tau.BookIII.Hinge.ChainLink.K5.toNat = 5
- Tau.BookIII.Hinge.ChainLink.K6.toNat = 6
- Tau.BookIII.Hinge.ChainLink.E0.toNat = 7
- Tau.BookIII.Hinge.ChainLink.E1.toNat = 8
- Tau.BookIII.Hinge.ChainLink.E1p.toNat = 9
- Tau.BookIII.Hinge.ChainLink.E2.toNat = 10
- Tau.BookIII.Hinge.ChainLink.E2p.toNat = 11
- Tau.BookIII.Hinge.ChainLink.E3.toNat = 12
- Tau.BookIII.Hinge.ChainLink.E3p.toNat = 13
Instances For

---

### `Tau.BookIII.Hinge.chain_links`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L82-L85)
**def
Tau.BookIII.Hinge.chain_links :List ChainLink**


The full 14-link chain as a list.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.ChainLink.toEnrLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L87-L92)
**def
Tau.BookIII.Hinge.ChainLink.toEnrLevel :ChainLink → Enrichment.EnrLevel**


Map a chain link to its enrichment level (K-links map to E0).
Equations
- Tau.BookIII.Hinge.ChainLink.K0.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.K1.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.K2.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.K3.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.K4.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.K5.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.K6.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.E0.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Hinge.ChainLink.E1.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E1
- Tau.BookIII.Hinge.ChainLink.E1p.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E1
- Tau.BookIII.Hinge.ChainLink.E2.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Hinge.ChainLink.E2p.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Hinge.ChainLink.E3.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E3
- Tau.BookIII.Hinge.ChainLink.E3p.toEnrLevel = Tau.BookIII.Enrichment.EnrLevel.E3
Instances For

---

### `Tau.BookIII.Hinge.ChainLink.succ`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L94-L109)
**def
Tau.BookIII.Hinge.ChainLink.succ :ChainLink → ChainLink**


Successor link in the chain (saturates at E3p).
Equations
- Tau.BookIII.Hinge.ChainLink.K0.succ = Tau.BookIII.Hinge.ChainLink.K1
- Tau.BookIII.Hinge.ChainLink.K1.succ = Tau.BookIII.Hinge.ChainLink.K2
- Tau.BookIII.Hinge.ChainLink.K2.succ = Tau.BookIII.Hinge.ChainLink.K3
- Tau.BookIII.Hinge.ChainLink.K3.succ = Tau.BookIII.Hinge.ChainLink.K4
- Tau.BookIII.Hinge.ChainLink.K4.succ = Tau.BookIII.Hinge.ChainLink.K5
- Tau.BookIII.Hinge.ChainLink.K5.succ = Tau.BookIII.Hinge.ChainLink.K6
- Tau.BookIII.Hinge.ChainLink.K6.succ = Tau.BookIII.Hinge.ChainLink.E0
- Tau.BookIII.Hinge.ChainLink.E0.succ = Tau.BookIII.Hinge.ChainLink.E1
- Tau.BookIII.Hinge.ChainLink.E1.succ = Tau.BookIII.Hinge.ChainLink.E1p
- Tau.BookIII.Hinge.ChainLink.E1p.succ = Tau.BookIII.Hinge.ChainLink.E2
- Tau.BookIII.Hinge.ChainLink.E2.succ = Tau.BookIII.Hinge.ChainLink.E2p
- Tau.BookIII.Hinge.ChainLink.E2p.succ = Tau.BookIII.Hinge.ChainLink.E3
- Tau.BookIII.Hinge.ChainLink.E3.succ = Tau.BookIII.Hinge.ChainLink.E3p
- Tau.BookIII.Hinge.ChainLink.E3p.succ = Tau.BookIII.Hinge.ChainLink.E3p
Instances For

---

### `Tau.BookIII.Hinge.chain_strict_order_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L115-L125)
**def
Tau.BookIII.Hinge.chain_strict_order_check :Bool**


[III.D66] Verify that the chain is strictly ordered: each link's
index is strictly less than the next link's index.
Equations
- Tau.BookIII.Hinge.chain_strict_order_check = Tau.BookIII.Hinge.chain_strict_order_check.go Tau.BookIII.Hinge.chain_links
Instances For

---

### `Tau.BookIII.Hinge.chain_strict_order_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L120-L125)
**def
Tau.BookIII.Hinge.chain_strict_order_check.go :List ChainLink → Bool**

Equations
- Tau.BookIII.Hinge.chain_strict_order_check.go [] = true
- Tau.BookIII.Hinge.chain_strict_order_check.go [head] = true
- Tau.BookIII.Hinge.chain_strict_order_check.go (a :: b :: rest) = (decide (a.toNat < b.toNat) && decide (a.succ.toNat ≤ b.toNat) && Tau.BookIII.Hinge.chain_strict_order_check.go (b :: rest))
Instances For

---

### `Tau.BookIII.Hinge.chain_layer_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L127-L141)
**def
Tau.BookIII.Hinge.chain_layer_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D66] Verify that each enrichment level's layer template is valid
at the corresponding chain link. For K-links, verify that the axiom
level infrastructure (primorial, reduce, etc.) is operational.
Equations
- Tau.BookIII.Hinge.chain_layer_check bound db = Tau.BookIII.Hinge.chain_layer_check.go Tau.BookIII.Hinge.chain_links bound db
 (Tau.BookIII.Hinge.chain_links.length + 1)
Instances For

---

### `Tau.BookIII.Hinge.chain_layer_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L133-L140)@[irreducible]

**def
Tau.BookIII.Hinge.chain_layer_check.go
(links : List ChainLink)

(bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Hinge.chain_layer_check.go [] bound db fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookIII.Hinge.chain_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L143-L149)
**def
Tau.BookIII.Hinge.chain_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D66] Verify tower coherence at each enrichment transition.
At each E-link, the tower assembly check passes.
Equations
- Tau.BookIII.Hinge.chain_tower_check bound db = (Tau.BookIII.Arithmetic.tower_strict_check && Tau.BookIII.Arithmetic.tower_assembly_check bound db)
Instances For

---

### `Tau.BookIII.Hinge.dependency_chain_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L151-L156)
**def
Tau.BookIII.Hinge.dependency_chain_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D66] Complete dependency chain check: strict order, layer validity,
and tower coherence all hold simultaneously.
Equations
- Tau.BookIII.Hinge.dependency_chain_check bound db = (Tau.BookIII.Hinge.chain_strict_order_check && Tau.BookIII.Hinge.chain_layer_check bound db && Tau.BookIII.Hinge.chain_tower_check bound db)
Instances For

---

### `Tau.BookIII.Hinge.chain_linearity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L162-L177)
**def
Tau.BookIII.Hinge.chain_linearity_check :Bool**


[III.P29] Chain linearity: the chain has no cycles.
Verification: for every pair (i, j) with i < j in the chain,
link_i.toNat < link_j.toNat (no backward edges).
Equations
- Tau.BookIII.Hinge.chain_linearity_check = Tau.BookIII.Hinge.chain_linearity_check.go Tau.BookIII.Hinge.chain_links 0 (Tau.BookIII.Hinge.chain_links.length + 1)
Instances For

---

### `Tau.BookIII.Hinge.chain_linearity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L168-L176)@[irreducible]

**def
Tau.BookIII.Hinge.chain_linearity_check.go
(links : List ChainLink)

(prev_idx fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Hinge.chain_linearity_check.go [] prev_idx fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookIII.Hinge.chain_no_duplicates_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L179-L191)
**def
Tau.BookIII.Hinge.chain_no_duplicates_check :Bool**


[III.P29] Acyclicity witness: no link appears twice in the chain.
Equations
- Tau.BookIII.Hinge.chain_no_duplicates_check = Tau.BookIII.Hinge.chain_no_duplicates_check.go Tau.BookIII.Hinge.chain_links []
 (Tau.BookIII.Hinge.chain_links.length + 1)
Instances For

---

### `Tau.BookIII.Hinge.chain_no_duplicates_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L183-L190)@[irreducible]

**def
Tau.BookIII.Hinge.chain_no_duplicates_check.go
(links : List ChainLink)

(seen : List ℕ)

(fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Hinge.chain_no_duplicates_check.go [] seen fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookIII.Hinge.chain_linearity_full_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L193-L195)
**def
Tau.BookIII.Hinge.chain_linearity_full_check :Bool**


[III.P29] Full chain linearity: strict order + no duplicates.
Equations
- Tau.BookIII.Hinge.chain_linearity_full_check = (Tau.BookIII.Hinge.chain_linearity_check && Tau.BookIII.Hinge.chain_no_duplicates_check)
Instances For

---

### `Tau.BookIII.Hinge.terminal_completeness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L201-L217)
**def
Tau.BookIII.Hinge.terminal_completeness_check :Bool**


[III.P30] Terminal completeness: the chain covers all four enrichment
levels. Accumulate which levels appear; verify all 4 are present.
Equations
- Tau.BookIII.Hinge.terminal_completeness_check = Tau.BookIII.Hinge.terminal_completeness_check.go Tau.BookIII.Hinge.chain_links false false false false
 (Tau.BookIII.Hinge.chain_links.length + 1)
Instances For

---

### `Tau.BookIII.Hinge.terminal_completeness_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L206-L216)@[irreducible]

**def
Tau.BookIII.Hinge.terminal_completeness_check.go
(links : List ChainLink)

(e0 e1 e2 e3 : Bool)

(fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Hinge.terminal_completeness_check.go [] e0 e1 e2 e3 fuel = if fuel = 0 then e0 && e1 && e2 && e3 else e0 && e1 && e2 && e3
Instances For

---

### `Tau.BookIII.Hinge.chain_length_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L219-L221)
**def
Tau.BookIII.Hinge.chain_length_check :Bool**


[III.P30] The chain has exactly 14 links.
Equations
- Tau.BookIII.Hinge.chain_length_check = (Tau.BookIII.Hinge.chain_links.length == 14)
Instances For

---

### `Tau.BookIII.Hinge.chain_terminal_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L223-L227)
**def
Tau.BookIII.Hinge.chain_terminal_check :Bool**


[III.P30] The terminal link is E3+ (saturation).
Equations
- Tau.BookIII.Hinge.chain_terminal_check = match Tau.BookIII.Hinge.chain_links.getLast? with
 | some link => link == Tau.BookIII.Hinge.ChainLink.E3p
 | none => false
Instances For

---

### `Tau.BookIII.Hinge.chain_saturation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L229-L231)
**def
Tau.BookIII.Hinge.chain_saturation_check :Bool**


[III.P30] E3+ is terminal: its successor is itself.
Equations
- Tau.BookIII.Hinge.chain_saturation_check = (Tau.BookIII.Hinge.ChainLink.E3p.succ == Tau.BookIII.Hinge.ChainLink.E3p)
Instances For

---

### `Tau.BookIII.Hinge.terminal_completeness_full_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L233-L239)
**def
Tau.BookIII.Hinge.terminal_completeness_full_check :Bool**


[III.P30] Full terminal completeness: coverage + length + terminal


- saturation.

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Hinge.dependency_chain_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L280-L281)
**theorem
Tau.BookIII.Hinge.dependency_chain_8_3 :dependency_chain_check 8 3 = true**


---

### `Tau.BookIII.Hinge.chain_strict_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L283-L284)
**theorem
Tau.BookIII.Hinge.chain_strict_order :chain_strict_order_check = true**


---

### `Tau.BookIII.Hinge.chain_layer_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L286-L287)
**theorem
Tau.BookIII.Hinge.chain_layer_8_3 :chain_layer_check 8 3 = true**


---

### `Tau.BookIII.Hinge.chain_tower_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L289-L290)
**theorem
Tau.BookIII.Hinge.chain_tower_10_3 :chain_tower_check 10 3 = true**


---

### `Tau.BookIII.Hinge.chain_linearity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L293-L294)
**theorem
Tau.BookIII.Hinge.chain_linearity :chain_linearity_check = true**


---

### `Tau.BookIII.Hinge.chain_no_duplicates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L296-L297)
**theorem
Tau.BookIII.Hinge.chain_no_duplicates :chain_no_duplicates_check = true**


---

### `Tau.BookIII.Hinge.chain_linearity_full`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L299-L300)
**theorem
Tau.BookIII.Hinge.chain_linearity_full :chain_linearity_full_check = true**


---

### `Tau.BookIII.Hinge.terminal_completeness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L303-L304)
**theorem
Tau.BookIII.Hinge.terminal_completeness :terminal_completeness_check = true**


---

### `Tau.BookIII.Hinge.chain_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L306-L307)
**theorem
Tau.BookIII.Hinge.chain_length :chain_length_check = true**


---

### `Tau.BookIII.Hinge.chain_terminal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L309-L310)
**theorem
Tau.BookIII.Hinge.chain_terminal :chain_terminal_check = true**


---

### `Tau.BookIII.Hinge.chain_saturation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L312-L313)
**theorem
Tau.BookIII.Hinge.chain_saturation :chain_saturation_check = true**


---

### `Tau.BookIII.Hinge.terminal_completeness_full`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L315-L316)
**theorem
Tau.BookIII.Hinge.terminal_completeness_full :terminal_completeness_full_check = true**


---

### `Tau.BookIII.Hinge.chain_has_14_links`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L322-L324)
**theorem
Tau.BookIII.Hinge.chain_has_14_links :chain_links.length = 14**


[III.D66] Structural: the chain has exactly 14 links.

---

### `Tau.BookIII.Hinge.k0_is_first`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L326-L327)
**theorem
Tau.BookIII.Hinge.k0_is_first :ChainLink.K0.toNat = 0**


[III.D66] Structural: K0 is the first link (index 0).

---

### `Tau.BookIII.Hinge.e3p_is_last`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L329-L330)
**theorem
Tau.BookIII.Hinge.e3p_is_last :ChainLink.E3p.toNat = 13**


[III.D66] Structural: E3p is the last link (index 13).

---

### `Tau.BookIII.Hinge.axiom_to_enrichment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L332-L334)
**theorem
Tau.BookIII.Hinge.axiom_to_enrichment :ChainLink.K6.succ = ChainLink.E0**


[III.D66] Structural: K6 -> E0 is the axiom-to-enrichment transition.

---

### `Tau.BookIII.Hinge.succ_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L336-L339)
**theorem
Tau.BookIII.Hinge.succ_monotone
(link : ChainLink)
 :link.toNat ≤ link.succ.toNat**


[III.P29] Structural: successor always increases index (except at E3p).

---

### `Tau.BookIII.Hinge.e3p_saturates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L341-L342)
**theorem
Tau.BookIII.Hinge.e3p_saturates :ChainLink.E3p.succ = ChainLink.E3p**


[III.P30] Structural: E3p.succ = E3p (terminal saturation).

---

### `Tau.BookIII.Hinge.all_links_have_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L344-L350)
**theorem
Tau.BookIII.Hinge.all_links_have_level
(link : ChainLink)
 :link.toEnrLevel = Enrichment.EnrLevel.E0 ∨ link.toEnrLevel = Enrichment.EnrLevel.E1 ∨ link.toEnrLevel = Enrichment.EnrLevel.E2 ∨ link.toEnrLevel = Enrichment.EnrLevel.E3**


[III.P30] Structural: every link maps to a valid enrichment level.

---

### `Tau.BookIII.Hinge.seven_plus_seven`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Hinge/DependencyChain.lean#L352-L354)
**theorem
Tau.BookIII.Hinge.seven_plus_seven :(List.filter (fun (l : ChainLink) => decide (l.toNat < 7)) chain_links).length = 7**


[III.D66] Structural: the chain covers 7 axiom links + 7 enrichment links.
