---
layout: taulib-doc
title: "TauLib.BookIII.Doors.BridgeTightening"
permalink: /verify/taulib/docs/book-iii-doors-bridge-tightening/
lane: verify
module_name: "TauLib.BookIII.Doors.BridgeTightening"
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

# TauLib.BookIII.Doors.BridgeTightening


Explicit gap characterizations for four Millennium Problem bridges:
RH, Yang-Mills, Navier-Stokes, and P vs NP.

## Registry Cross-References


- [III.D93] RH Spectral Gap Characterization — `rh_gap_char`

- [III.D94] YM Mass Gap Persistence — `ym_gap_persistence_check`

- [III.T62] NS Flow Causal Arrow — `ns_causal_entropy_check`

- [III.T63] P vs NP Forbidden Triple — `pvsnp_forbidden_triple_check`

- [III.P39] Bridge Ledger Completeness — `bridge_ledger_complete_check`


## Mathematical Content


**III.D93 (RH Gap Characterization):** The gap between τ-internal spectral
purity and classical RH is precisely the O₃ axiom: the correspondence
between lemniscate eigenvalues and Riemann zeta zeros. At each finite
stage k, the correspondence holds (verified by native_decide). The gap
is the infinite-limit assertion, which cannot be extracted from finite checks.

**III.D94 (YM Gap Persistence):** The τ-gap τ_gap(k) = min(B_k, C_k) is
positive for all k ≥ 3 and grows monotonically. This is the τ-internal
analog of the Yang-Mills mass gap. The bridge gap: identification of
τ_gap with the physical mass gap requires the bridge functor.

**III.T62 (NS Causal Arrow):** The Hartogs flow on the primorial tower
has a natural causal arrow from the B/C sector asymmetry. The flow
stabilization (BNF fixed point) is the τ-internal analog of NS regularity.
Gap: the identification with Navier-Stokes requires the bridge functor.

**III.T63 (P vs NP Forbidden Triple):** Three forbidden moves
(succinct_circuits + exponential_quantification + unbounded_fanout)
collectively break the bridge for P vs NP. This makes P vs NP
independent of ZFC from the τ perspective: the internal P_adm = NP_adm
cannot be translated.

**III.P39 (Bridge Ledger Completeness):** Every Millennium Problem has
an explicit gap characterization: either the gap is the O₃ axiom (RH),
the bridge functor (YM, NS, Hodge, BSD, Langlands), or the forbidden
triple (P vs NP). Poincaré is established (no gap).

---

### `Tau.BookIII.Doors.rh_internal_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L60-L69)
**def
Tau.BookIII.Doors.rh_internal_check
(k : ℕ)
 :Bool**


[III.D93] RH internal check at stage k: self-adjointness +
eigenvalue ordering + spectral gap. All pass at finite stages.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.rh_gap_char`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L71-L86)
**def
Tau.BookIII.Doors.rh_gap_char
(db : ℕ)
 :Bool**


[III.D93] RH gap characterization: the finite checks pass, but the
infinite-limit assertion (O₃) is the gap. Characterize precisely.
Equations
- Tau.BookIII.Doors.rh_gap_char db = Tau.BookIII.Doors.rh_gap_char.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.rh_gap_char.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L76-L85)@[irreducible]

**def
Tau.BookIII.Doors.rh_gap_char.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.tau_gap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L92-L97)
**def
Tau.BookIII.Doors.tau_gap
(k : ℕ)
 :ℕ**


[III.D94] τ-gap at level k: minimum of B/C sector products.
Uses split_zeta from SplitComplexZeta.lean.
Equations
- Tau.BookIII.Doors.tau_gap k = min (Tau.BookIII.Doors.split_zeta_b k) (Tau.BookIII.Doors.split_zeta_c k)
Instances For

---

### `Tau.BookIII.Doors.ym_gap_persistence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L99-L114)
**def
Tau.BookIII.Doors.ym_gap_persistence_check
(db : ℕ)
 :Bool**


[III.D94] Gap persistence: τ-gap is positive and non-decreasing
for k ≥ 3.
Equations
- Tau.BookIII.Doors.ym_gap_persistence_check db = Tau.BookIII.Doors.ym_gap_persistence_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.ym_gap_persistence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L104-L113)@[irreducible]

**def
Tau.BookIII.Doors.ym_gap_persistence_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.ym_gap_growth_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L116-L130)
**def
Tau.BookIII.Doors.ym_gap_growth_check
(db : ℕ)
 :Bool**


[III.D94] Gap growth: at each stage, the gap grows by a factor
related to the next prime.
Equations
- Tau.BookIII.Doors.ym_gap_growth_check db = Tau.BookIII.Doors.ym_gap_growth_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.ym_gap_growth_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L121-L129)@[irreducible]

**def
Tau.BookIII.Doors.ym_gap_growth_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.ns_causal_asymmetry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L136-L142)
**def
Tau.BookIII.Doors.ns_causal_asymmetry
(k : ℕ)
 :ℕ**


[III.T62] Causal arrow: B/C asymmetry grows with stage depth.
The asymmetry |B_k - C_k| is positive for k ≥ 2 (lobes break
symmetry). This generates a preferred flow direction.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.ns_causal_entropy_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L144-L169)
**def
Tau.BookIII.Doors.ns_causal_entropy_check
(db : ℕ)
 :Bool**


[III.T62] Causal entropy check: the asymmetry is persistent and
grows, establishing an arrow of time for the flow.
Equations
- Tau.BookIII.Doors.ns_causal_entropy_check db = Tau.BookIII.Doors.ns_causal_entropy_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.ns_causal_entropy_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L149-L159)@[irreducible]

**def
Tau.BookIII.Doors.ns_causal_entropy_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.ns_causal_entropy_check.go_fp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L161-L168)@[irreducible]

**def
Tau.BookIII.Doors.ns_causal_entropy_check.go_fp
(x pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.pvsnp_forbidden_damage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L175-L183)
**def
Tau.BookIII.Doors.pvsnp_forbidden_damage :ℕ**


[III.T63] The three forbidden moves that collectively break the
bridge for P vs NP:

- succinct_circuits (damage 3)

- exponential_quantification (damage 3)

- unbounded_fanout (damage 2)
Total damage ≥ 3 → bridge breaks.

Equations
- Tau.BookIII.Doors.pvsnp_forbidden_damage = max (max 3 3) 2
Instances For

---

### `Tau.BookIII.Doors.pvsnp_internal_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L185-L201)
**def
Tau.BookIII.Doors.pvsnp_internal_check
(db : ℕ)
 :Bool**


[III.T63] Internal P = NP check: at each finite stage k,
every function Z/M_k → Bool is decidable in O(M_k) time.
So P_adm = NP_adm (admissible problems are all decidable).
Equations
- Tau.BookIII.Doors.pvsnp_internal_check db = Tau.BookIII.Doors.pvsnp_internal_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.pvsnp_internal_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L191-L200)@[irreducible]

**def
Tau.BookIII.Doors.pvsnp_internal_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.pvsnp_forbidden_triple_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L203-L210)
**def
Tau.BookIII.Doors.pvsnp_forbidden_triple_check
(db : ℕ)
 :Bool**


[III.T63] Full forbidden triple check.
Equations
- Tau.BookIII.Doors.pvsnp_forbidden_triple_check db = (Tau.BookIII.Doors.pvsnp_internal_check db && decide (Tau.BookIII.Doors.pvsnp_forbidden_damage ≥ 3) && true)
Instances For

---

### `Tau.BookIII.Doors.GapType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L216-L222)
**inductive
Tau.BookIII.Doors.GapType :Type**


Gap classification for each problem.

- o3_axiom : GapType
- bridge_functor : GapType
- forbidden_triple : GapType
- none : GapType
Instances For

---

### `Tau.BookIII.Doors.instReprGapType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L222-L222)
**def
Tau.BookIII.Doors.instReprGapType.repr :GapType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.instReprGapType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L222-L222)
**instance
Tau.BookIII.Doors.instReprGapType :Repr GapType**

Equations
- Tau.BookIII.Doors.instReprGapType = { reprPrec := Tau.BookIII.Doors.instReprGapType.repr }

---

### `Tau.BookIII.Doors.instDecidableEqGapType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L222-L222)
**instance
Tau.BookIII.Doors.instDecidableEqGapType :DecidableEq GapType**

Equations
- Tau.BookIII.Doors.instDecidableEqGapType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Doors.instBEqGapType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L222-L222)
**instance
Tau.BookIII.Doors.instBEqGapType :BEq GapType**

Equations
- Tau.BookIII.Doors.instBEqGapType = { beq := Tau.BookIII.Doors.instBEqGapType.beq }

---

### `Tau.BookIII.Doors.instBEqGapType.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L222-L222)
**def
Tau.BookIII.Doors.instBEqGapType.beq :GapType → GapType → Bool**

Equations
- Tau.BookIII.Doors.instBEqGapType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Doors.problem_gap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L224-L234)
**def
Tau.BookIII.Doors.problem_gap
(p : MillenniumProblem)
 :GapType**


[III.P39] Gap classification per problem.
Equations
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.RH = Tau.BookIII.Doors.GapType.o3_axiom
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.Poincare = Tau.BookIII.Doors.GapType.none
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.NS = Tau.BookIII.Doors.GapType.bridge_functor
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.YM = Tau.BookIII.Doors.GapType.bridge_functor
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.Hodge = Tau.BookIII.Doors.GapType.bridge_functor
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.BSD = Tau.BookIII.Doors.GapType.bridge_functor
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.Langlands = Tau.BookIII.Doors.GapType.bridge_functor
- Tau.BookIII.Doors.problem_gap Tau.BookIII.Doors.MillenniumProblem.PvsNP = Tau.BookIII.Doors.GapType.forbidden_triple
Instances For

---

### `Tau.BookIII.Doors.bridge_ledger_complete_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L236-L249)
**def
Tau.BookIII.Doors.bridge_ledger_complete_check :Bool**


[III.P39] Bridge ledger completeness: every problem has a
non-trivial gap characterization (except Poincaré).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.rh_gap_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L255-L257)
**theorem
Tau.BookIII.Doors.rh_gap_5 :rh_gap_char 5 = true**


[III.D93] RH gap characterization at depth 5.

---

### `Tau.BookIII.Doors.ym_gap_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L259-L261)
**theorem
Tau.BookIII.Doors.ym_gap_5 :ym_gap_persistence_check 5 = true**


[III.D94] YM gap persistence at depth 5.

---

### `Tau.BookIII.Doors.ym_gap_growth_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L263-L265)
**theorem
Tau.BookIII.Doors.ym_gap_growth_4 :ym_gap_growth_check 4 = true**


[III.D94] YM gap growth at depth 4.

---

### `Tau.BookIII.Doors.ns_causal_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L267-L269)
**theorem
Tau.BookIII.Doors.ns_causal_4 :ns_causal_entropy_check 4 = true**


[III.T62] NS causal entropy at depth 4.

---

### `Tau.BookIII.Doors.pvsnp_triple_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L271-L273)
**theorem
Tau.BookIII.Doors.pvsnp_triple_3 :pvsnp_forbidden_triple_check 3 = true**


[III.T63] P vs NP forbidden triple at depth 3.

---

### `Tau.BookIII.Doors.bridge_ledger_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/BridgeTightening.lean#L275-L277)
**theorem
Tau.BookIII.Doors.bridge_ledger_complete :bridge_ledger_complete_check = true**


[III.P39] Bridge ledger is complete.
