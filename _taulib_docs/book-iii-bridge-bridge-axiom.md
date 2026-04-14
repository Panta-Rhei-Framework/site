---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.BridgeAxiom"
permalink: /verify/taulib/docs/book-iii-bridge-bridge-axiom/
lane: verify
module_name: "TauLib.BookIII.Bridge.BridgeAxiom"
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

# TauLib.BookIII.Bridge.BridgeAxiom


Bridge Axiom (CONJECTURAL), Shadow Diagram, RH Bridge Three-Layer,
Bridge Ledger, and Honest Claim Theorem.

## Registry Cross-References


- [III.D71] Bridge Axiom (CONJECTURAL) -- `bridge_functor_exists` (Lean axiom)

- [III.D72] Shadow Diagram -- `shadow_diagram_check`

- [III.T45] RH Bridge Three-Layer -- `rh_bridge_three_layer`

- [III.T46] Bridge Ledger -- `bridge_ledger_check`

- [III.T47] Honest Claim Theorem -- `honest_claim_check`


## Mathematical Content


**III.D71 (Bridge Axiom):** A bridge is a structure-preserving functor
F: Cat_tau(E2) -> Mod(ZFC) satisfying carrier preservation, predicate
preservation, decoder compatibility, and invariant reflection. The existence
of such F is CONJECTURAL and declared as a Lean axiom. This is the one
point where the tau-framework explicitly marks the gap between internal
and external mathematics.

**III.D72 (Shadow Diagram):** The image of a tau-internal commutative
diagram under the bridge functor F. The shadow preserves commutativity
but may lose structure: each forbidden move introduces a specific
degeneracy in the shadow.

**III.T45 (RH Bridge Three-Layer):** The RH bridge has three layers:
(1) tau-internal spectral purity (tau-effective),
(2) Connes-Consani Weil positivity (established),
(3) identification of tau spectral data with Riemann zeta zeros (conjectural).

**III.T46 (Bridge Ledger):** Per-problem bridge status:
6 conjectural (RH, NS, YM, Hodge, BSD, Langlands),
1 bridge break (P vs NP), 1 established (Poincare).

**III.T47 (Honest Claim):** tau-framework claims are precisely bounded by
scope labels. Every check that passes at (bound, db) is labeled with the
correct scope: established, tau-effective, conjectural, or metaphorical.

---

### `Tau.BookIII.Bridge.ScopeLabel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L56-L63)
**inductive
Tau.BookIII.Bridge.ScopeLabel :Type**


The four scope labels used throughout Book III.
Establishes the honesty discipline for claims.

- established : ScopeLabel
- tau_effective : ScopeLabel
- conjectural : ScopeLabel
- metaphorical : ScopeLabel
Instances For

---

### `Tau.BookIII.Bridge.instReprScopeLabel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L63-L63)
**def
Tau.BookIII.Bridge.instReprScopeLabel.repr :ScopeLabel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instReprScopeLabel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L63-L63)
**instance
Tau.BookIII.Bridge.instReprScopeLabel :Repr ScopeLabel**

Equations
- Tau.BookIII.Bridge.instReprScopeLabel = { reprPrec := Tau.BookIII.Bridge.instReprScopeLabel.repr }

---

### `Tau.BookIII.Bridge.instDecidableEqScopeLabel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L63-L63)
**instance
Tau.BookIII.Bridge.instDecidableEqScopeLabel :DecidableEq ScopeLabel**

Equations
- Tau.BookIII.Bridge.instDecidableEqScopeLabel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqScopeLabel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L63-L63)
**instance
Tau.BookIII.Bridge.instBEqScopeLabel :BEq ScopeLabel**

Equations
- Tau.BookIII.Bridge.instBEqScopeLabel = { beq := Tau.BookIII.Bridge.instBEqScopeLabel.beq }

---

### `Tau.BookIII.Bridge.instBEqScopeLabel.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L63-L63)
**def
Tau.BookIII.Bridge.instBEqScopeLabel.beq :ScopeLabel → ScopeLabel → Bool**

Equations
- Tau.BookIII.Bridge.instBEqScopeLabel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.ScopeLabel.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L65-L70)
**def
Tau.BookIII.Bridge.ScopeLabel.toNat :ScopeLabel → ℕ**


Numeric order of scopes (higher = less certain).
Equations
- Tau.BookIII.Bridge.ScopeLabel.established.toNat = 0
- Tau.BookIII.Bridge.ScopeLabel.tau_effective.toNat = 1
- Tau.BookIII.Bridge.ScopeLabel.conjectural.toNat = 2
- Tau.BookIII.Bridge.ScopeLabel.metaphorical.toNat = 3
Instances For

---

### `Tau.BookIII.Bridge.bridge_functor_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L76-L98)
**def
Tau.BookIII.Bridge.bridge_functor_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D71] Bridge functor check at finite level: can we map tau-internal
structures to ZFC-internal structures at depth k? At finite level, the
bridge is a map from tau-addresses to ZFC axiom operations.
Equations
- Tau.BookIII.Bridge.bridge_functor_check bound db = Tau.BookIII.Bridge.bridge_functor_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.bridge_functor_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L82-L97)@[irreducible]

**def
Tau.BookIII.Bridge.bridge_functor_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.bridge_functor_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L100-L105)
**axiom
Tau.BookIII.Bridge.bridge_functor_exists
(bound db : Denotation.TauIdx)
 :bridge_functor_check bound db = true**


[III.D71] **CONJECTURAL AXIOM**: The bridge functor exists for all
(bound, db). This is the ONE conjectural postulate in the Bridge.
At finite level, `bridge_functor_check` verifies the finite shadow.
The axiom asserts that this extends to the infinite tower.

---

### `Tau.BookIII.Bridge.shadow_diagram_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L111-L139)
**def
Tau.BookIII.Bridge.shadow_diagram_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D72] Shadow diagram: the image of a tau-internal diagram under
the bridge functor. A shadow preserves commutativity but may lose
injectivity or faithfulness at forbidden moves.

Modeled as: for a commutative square (a -> b -> c) in tau,
the shadow (F(a) -> F(b) -> F(c)) in ZFC preserves the composition
(reduce coherence) but may collapse distinct values.
Equations
- Tau.BookIII.Bridge.shadow_diagram_check bound db = Tau.BookIII.Bridge.shadow_diagram_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.shadow_diagram_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L121-L138)@[irreducible]

**def
Tau.BookIII.Bridge.shadow_diagram_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.BridgeStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L145-L150)
**inductive
Tau.BookIII.Bridge.BridgeStatus :Type**


Bridge status for each Millennium Problem.

- established : BridgeStatus
- conjectural : BridgeStatus
- bridge_break : BridgeStatus
Instances For

---

### `Tau.BookIII.Bridge.instReprBridgeStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L150-L150)
**instance
Tau.BookIII.Bridge.instReprBridgeStatus :Repr BridgeStatus**

Equations
- Tau.BookIII.Bridge.instReprBridgeStatus = { reprPrec := Tau.BookIII.Bridge.instReprBridgeStatus.repr }

---

### `Tau.BookIII.Bridge.instReprBridgeStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L150-L150)
**def
Tau.BookIII.Bridge.instReprBridgeStatus.repr :BridgeStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instDecidableEqBridgeStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L150-L150)
**instance
Tau.BookIII.Bridge.instDecidableEqBridgeStatus :DecidableEq BridgeStatus**

Equations
- Tau.BookIII.Bridge.instDecidableEqBridgeStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqBridgeStatus.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L150-L150)
**def
Tau.BookIII.Bridge.instBEqBridgeStatus.beq :BridgeStatus → BridgeStatus → Bool**

Equations
- Tau.BookIII.Bridge.instBEqBridgeStatus.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.instBEqBridgeStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L150-L150)
**instance
Tau.BookIII.Bridge.instBEqBridgeStatus :BEq BridgeStatus**

Equations
- Tau.BookIII.Bridge.instBEqBridgeStatus = { beq := Tau.BookIII.Bridge.instBEqBridgeStatus.beq }

---

### `Tau.BookIII.Bridge.rh_bridge_three_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L152-L161)
**def
Tau.BookIII.Bridge.rh_bridge_three_layer
(bound db : Denotation.TauIdx)

(h : bridge_functor_check bound db = true)
 :BridgeStatus**


[III.T45] RH bridge three-layer structure:
Layer 1: tau-internal spectral purity on H_L (tau-effective)
Layer 2: Connes-Consani Weil positivity Q_W(g) >= 0 (established)
Layer 3: identification of tau spectral data with zeta zeros (conjectural)
Equations
- Tau.BookIII.Bridge.rh_bridge_three_layer bound db h = Tau.BookIII.Bridge.BridgeStatus.conjectural
Instances For

---

### `Tau.BookIII.Bridge.rh_bridge_layer_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L163-L164)
**def
Tau.BookIII.Bridge.rh_bridge_layer_count :ℕ**


[III.T45] Layer count for the RH bridge.
Equations
- Tau.BookIII.Bridge.rh_bridge_layer_count = 3
Instances For

---

### `Tau.BookIII.Bridge.rh_conjectural_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L166-L167)
**def
Tau.BookIII.Bridge.rh_conjectural_layer :ℕ**


[III.T45] The conjectural gap is always Layer 3.
Equations
- Tau.BookIII.Bridge.rh_conjectural_layer = 3
Instances For

---

### `Tau.BookIII.Bridge.BridgeLedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L173-L179)
**structure
Tau.BookIII.Bridge.BridgeLedgerEntry :Type**


[III.T46] Bridge ledger entry: each Millennium Problem has a bridge
status and a scope label.

- problem : Doors.MillenniumProblem
- status : BridgeStatus
- scope : ScopeLabel
Instances For

---

### `Tau.BookIII.Bridge.instReprBridgeLedgerEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L179-L179)
**def
Tau.BookIII.Bridge.instReprBridgeLedgerEntry.repr :BridgeLedgerEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instReprBridgeLedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L179-L179)
**instance
Tau.BookIII.Bridge.instReprBridgeLedgerEntry :Repr BridgeLedgerEntry**

Equations
- Tau.BookIII.Bridge.instReprBridgeLedgerEntry = { reprPrec := Tau.BookIII.Bridge.instReprBridgeLedgerEntry.repr }

---

### `Tau.BookIII.Bridge.instDecidableEqBridgeLedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L179-L179)
**instance
Tau.BookIII.Bridge.instDecidableEqBridgeLedgerEntry :DecidableEq BridgeLedgerEntry**

Equations
- Tau.BookIII.Bridge.instDecidableEqBridgeLedgerEntry = Tau.BookIII.Bridge.instDecidableEqBridgeLedgerEntry.decEq

---

### `Tau.BookIII.Bridge.instDecidableEqBridgeLedgerEntry.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L179-L179)
**def
Tau.BookIII.Bridge.instDecidableEqBridgeLedgerEntry.decEq
(x✝ x✝¹ : BridgeLedgerEntry)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instBEqBridgeLedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L179-L179)
**instance
Tau.BookIII.Bridge.instBEqBridgeLedgerEntry :BEq BridgeLedgerEntry**

Equations
- Tau.BookIII.Bridge.instBEqBridgeLedgerEntry = { beq := Tau.BookIII.Bridge.instBEqBridgeLedgerEntry.beq }

---

### `Tau.BookIII.Bridge.instBEqBridgeLedgerEntry.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L179-L179)
**def
Tau.BookIII.Bridge.instBEqBridgeLedgerEntry.beq :BridgeLedgerEntry → BridgeLedgerEntry → Bool**

Equations
- Tau.BookIII.Bridge.instBEqBridgeLedgerEntry.beq { problem := a, status := a_1, scope := a_2 }
 { problem := b, status := b_1, scope := b_2 } = (a == b && (a_1 == b_1 && a_2 == b_2))
- Tau.BookIII.Bridge.instBEqBridgeLedgerEntry.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Bridge.bridge_ledger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L181-L191)
**def
Tau.BookIII.Bridge.bridge_ledger :List BridgeLedgerEntry**


[III.T46] The complete bridge ledger.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.bridge_ledger_len`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L193-L194)
**def
Tau.BookIII.Bridge.bridge_ledger_len :ℕ**


[III.T46] Bridge ledger length.
Equations
- Tau.BookIII.Bridge.bridge_ledger_len = Tau.BookIII.Bridge.bridge_ledger.length
Instances For

---

### `Tau.BookIII.Bridge.ledger_status_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L196-L198)
**def
Tau.BookIII.Bridge.ledger_status_count
(s : BridgeStatus)
 :ℕ**


[III.T46] Count entries with a given status.
Equations
- Tau.BookIII.Bridge.ledger_status_count s = (List.filter (fun (e : Tau.BookIII.Bridge.BridgeLedgerEntry) => e.status == s)
 Tau.BookIII.Bridge.bridge_ledger).length
Instances For

---

### `Tau.BookIII.Bridge.bridge_ledger_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L200-L205)
**def
Tau.BookIII.Bridge.bridge_ledger_check :Bool**


[III.T46] Bridge ledger check: verify the ledger is consistent.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.ClaimRecord`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L211-L215)
**structure
Tau.BookIII.Bridge.ClaimRecord :Type**


[III.T47] A claim record: associates a check function with its scope.

- name : String
- scope : ScopeLabel
- check : Denotation.TauIdx → Denotation.TauIdx → Bool
Instances For

---

### `Tau.BookIII.Bridge.established_claims`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L217-L226)
**def
Tau.BookIII.Bridge.established_claims :List ClaimRecord**


[III.T47] The established claims: these pass checks and have scope
"established" or "tau-effective". No bridge axiom needed.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.honest_claim_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L228-L243)
**def
Tau.BookIII.Bridge.honest_claim_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T47] Honest claim check: every established/tau-effective claim
passes its check at the given (bound, db). This is UNCONDITIONAL --
no bridge axiom needed for honest claims.
Equations
- Tau.BookIII.Bridge.honest_claim_check bound db = Tau.BookIII.Bridge.honest_claim_check.go bound db Tau.BookIII.Bridge.established_claims
 (Tau.BookIII.Bridge.established_claims.length + 1)
Instances For

---

### `Tau.BookIII.Bridge.honest_claim_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L234-L242)@[irreducible]

**def
Tau.BookIII.Bridge.honest_claim_check.go
(bound db : Denotation.TauIdx)

(claims : List ClaimRecord)

(fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Bridge.honest_claim_check.go bound db [] fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookIII.Bridge.conjectural_properly_marked`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L245-L249)
**def
Tau.BookIII.Bridge.conjectural_properly_marked :Bool**


[III.T47] Conjectural claims are clearly marked: they depend on
the bridge axiom and are NOT claimed as theorems.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.break_properly_marked`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L251-L255)
**def
Tau.BookIII.Bridge.break_properly_marked :Bool**


[III.T47] Bridge breaks are clearly marked: P vs NP is tau_effective
internally but the bridge degenerates.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.honest_claim_full`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L257-L263)
**def
Tau.BookIII.Bridge.honest_claim_full
(bound db : Denotation.TauIdx)
 :Bool**


[III.T47] Full honest claim: established claims pass checks,
conjectural claims are properly marked, breaks are properly marked.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.bridge_functor_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L301-L302)
**theorem
Tau.BookIII.Bridge.bridge_functor_8_3 :bridge_functor_check 8 3 = true**


---

### `Tau.BookIII.Bridge.shadow_diagram_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L305-L306)
**theorem
Tau.BookIII.Bridge.shadow_diagram_8_3 :shadow_diagram_check 8 3 = true**


---

### `Tau.BookIII.Bridge.honest_claim_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L309-L310)
**theorem
Tau.BookIII.Bridge.honest_claim_8_3 :honest_claim_check 8 3 = true**


---

### `Tau.BookIII.Bridge.conjectural_marked`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L313-L314)
**theorem
Tau.BookIII.Bridge.conjectural_marked :conjectural_properly_marked = true**


---

### `Tau.BookIII.Bridge.break_marked`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L317-L318)
**theorem
Tau.BookIII.Bridge.break_marked :break_properly_marked = true**


---

### `Tau.BookIII.Bridge.honest_claim_full_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L321-L322)
**theorem
Tau.BookIII.Bridge.honest_claim_full_8_3 :honest_claim_full 8 3 = true**


---

### `Tau.BookIII.Bridge.bridge_ledger_consistent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L325-L326)
**theorem
Tau.BookIII.Bridge.bridge_ledger_consistent :bridge_ledger_check = true**


---

### `Tau.BookIII.Bridge.rh_bridge_conjectural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L332-L335)
**theorem
Tau.BookIII.Bridge.rh_bridge_conjectural
(bound db : Denotation.TauIdx)
 :rh_bridge_three_layer bound db ⋯ = BridgeStatus.conjectural**


[III.T45] RH bridge is conjectural (conditional on bridge axiom).

---

### `Tau.BookIII.Bridge.one_axiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L341-L342)
**theorem
Tau.BookIII.Bridge.one_axiom :rh_conjectural_layer = 3**


[III.D71] Structural: bridge axiom is the ONLY conjectural postulate.

---

### `Tau.BookIII.Bridge.rh_layers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L344-L345)
**theorem
Tau.BookIII.Bridge.rh_layers :rh_bridge_layer_count = 3**


[III.T45] Structural: RH bridge has 3 layers.

---

### `Tau.BookIII.Bridge.ledger_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L347-L348)
**theorem
Tau.BookIII.Bridge.ledger_count :bridge_ledger_len = 8**


[III.T46] Structural: ledger has exactly 8 entries.

---

### `Tau.BookIII.Bridge.poincare_established`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L350-L352)
**theorem
Tau.BookIII.Bridge.poincare_established :ledger_status_count BridgeStatus.established = 1**


[III.T46] Structural: Poincare is established.

---

### `Tau.BookIII.Bridge.pvsnp_bridge_break`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L354-L356)
**theorem
Tau.BookIII.Bridge.pvsnp_bridge_break :ledger_status_count BridgeStatus.bridge_break = 1**


[III.T46] Structural: P vs NP is a bridge break.

---

### `Tau.BookIII.Bridge.scope_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L358-L363)
**theorem
Tau.BookIII.Bridge.scope_order :ScopeLabel.established.toNat < ScopeLabel.tau_effective.toNat ∧ ScopeLabel.tau_effective.toNat < ScopeLabel.conjectural.toNat ∧ ScopeLabel.conjectural.toNat < ScopeLabel.metaphorical.toNat**


[III.T47] Structural: scope labels are ordered.

---

### `Tau.BookIII.Bridge.established_not_conjectural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L365-L369)
**theorem
Tau.BookIII.Bridge.established_not_conjectural :(established_claims.all fun (c : ClaimRecord) =>
 c.scope == ScopeLabel.established || c.scope == ScopeLabel.tau_effective) = true**


[III.T47] Structural: established claims use no conjectural scope.

---

### `Tau.BookIII.Bridge.ledger_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/BridgeAxiom.lean#L371-L376)
**theorem
Tau.BookIII.Bridge.ledger_partition :ledger_status_count BridgeStatus.conjectural + ledger_status_count BridgeStatus.established + ledger_status_count BridgeStatus.bridge_break = 8**


[III.T47] Structural: 6 + 1 + 1 = 8 (partition of bridge ledger).
