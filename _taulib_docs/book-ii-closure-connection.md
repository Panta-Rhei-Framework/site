---
layout: taulib-doc
title: "TauLib.BookII.Closure.Connection"
permalink: /verify/taulib/docs/book-ii-closure-connection/
lane: verify
module_name: "TauLib.BookII.Closure.Connection"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Closure.Connection


τ-connections on the primorial tower: parallel transport, holonomy,
and curvature via finite differences on Z/M_k Z.

## Registry Cross-References


- [II.D78] τ-Connection — `TauConnection`, `connection_check`

- [II.D79] Parallel Transport — `parallel_transport`, `transport_check`

- [II.T50] Flat Connection Existence — `flat_connection_check`

- [II.P16] Holonomy Triviality — `holonomy_trivial_check`


## Mathematical Content


**II.D78 (τ-Connection):** A connection on the primorial tower assigns to
each stage k a "transport operator" Γ_k : Z/M_k Z × Z/M_k Z → Z/M_k Z
that lifts the identity to a parallel transport rule. The natural connection
uses the additive structure: Γ_k(x, v) = reduce(x + v, k).

The key constraint is tower compatibility: transporting at stage k+1 and
then reducing must equal reducing and then transporting at stage k.

**II.D79 (Parallel Transport):** Given a connection Γ and a path
γ = (x₀, x₁, ..., x_n) in Z/M_k Z, parallel transport along γ is the
sequential composition Γ_k(x₀, x₁-x₀) ∘ Γ_k(x₁, x₂-x₁) ∘ ...

**II.T50 (Flat Connection Existence):** The additive connection Γ_k(x,v) =
(x+v) mod M_k is flat: parallel transport around any closed loop returns
to the starting point. This is because Z/M_k Z is a group and addition is
associative.

**II.P16 (Holonomy Triviality):** At each finite stage, the holonomy group
of the flat connection is trivial. This is the categorical analogue of
"simply connected at each stage" — the profinite limit may acquire
nontrivial holonomy (from the lemniscate fundamental group).

---

### `Tau.BookII.Closure.TauConnection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L52-L55)
**structure
Tau.BookII.Closure.TauConnection :Type**


[II.D78] A τ-connection at stage k: a transport function
Γ(x, v) that moves from x in direction v within Z/M_k Z.

- transport : ℕ → ℕ → ℕ → ℕ
Instances For

---

### `Tau.BookII.Closure.flat_connection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L57-L59)
**def
Tau.BookII.Closure.flat_connection :TauConnection**


[II.D78] The canonical flat connection: additive transport.
Equations
- Tau.BookII.Closure.flat_connection = { transport := fun (k x v : ℕ) => (x + v) % Tau.Polarity.primorial k }
Instances For

---

### `Tau.BookII.Closure.connection_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L61-L79)
**def
Tau.BookII.Closure.connection_tower_check
(conn : TauConnection)

(k : ℕ)
 :Bool**


[II.D78] Connection tower compatibility check: transport at stage k+1
composed with reduction equals reduction composed with transport at
stage k. Formally: reduce(Γ_{k+1}(x,v), k) = Γ_k(reduce(x,k), reduce(v,k)).
Equations
- Tau.BookII.Closure.connection_tower_check conn k = Tau.BookII.Closure.connection_tower_check.go conn k 0 (Tau.Polarity.primorial (k + 1)) 0
Instances For

---

### `Tau.BookII.Closure.connection_tower_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L67-L71)@[irreducible]

**def
Tau.BookII.Closure.connection_tower_check.go
(conn : TauConnection)

(k x pk1 v_fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.connection_tower_check.go_v`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L73-L78)@[irreducible]

**def
Tau.BookII.Closure.connection_tower_check.go_v
(conn : TauConnection)

(k x pk pk1 v v_fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.connection_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L81-L89)
**def
Tau.BookII.Closure.connection_check
(conn : TauConnection)

(db : ℕ)
 :Bool**


[II.D78] Full connection check for stages 1..db.
Equations
- Tau.BookII.Closure.connection_check conn db = Tau.BookII.Closure.connection_check.go conn db 1 (db + 1)
Instances For

---

### `Tau.BookII.Closure.connection_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L85-L88)@[irreducible]

**def
Tau.BookII.Closure.connection_check.go
(conn : TauConnection)

(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.parallel_transport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L95-L99)
**def
Tau.BookII.Closure.parallel_transport
(conn : TauConnection)

(k x : ℕ)

(path : List ℕ)
 :ℕ**


[II.D79] Transport a value x along a path (list of direction vectors)
at stage k.
Equations
- Tau.BookII.Closure.parallel_transport conn k x path = List.foldl (fun (pos v : ℕ) => conn.transport k pos v) x path
Instances For

---

### `Tau.BookII.Closure.transport_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L101-L106)
**def
Tau.BookII.Closure.transport_in_range
(conn : TauConnection)

(k x : ℕ)

(path : List ℕ)
 :Bool**


[II.D79] Transport check: verify that transport along a path
at stage k stays within Z/M_k Z.
Equations
- Tau.BookII.Closure.transport_in_range conn k x path = decide (Tau.BookII.Closure.parallel_transport conn k x path < Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.flatness_check_loop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L112-L117)
**def
Tau.BookII.Closure.flatness_check_loop
(conn : TauConnection)

(k x : ℕ)

(loop : List ℕ)
 :Bool**


[II.T50] Flatness check: parallel transport around a closed loop
(path where sum of directions = 0 mod M_k) returns to start.
Equations
- Tau.BookII.Closure.flatness_check_loop conn k x loop = (Tau.BookII.Closure.parallel_transport conn k x loop == x)
Instances For

---

### `Tau.BookII.Closure.flat_connection_check_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L119-L139)
**def
Tau.BookII.Closure.flat_connection_check_stage
(k : ℕ)
 :Bool**


[II.T50] Check flatness of the flat connection for small loops at stage k.
Tests all triangular loops (v, w, -(v+w)) for v, w in [0, M_k).
Equations
- Tau.BookII.Closure.flat_connection_check_stage k = Tau.BookII.Closure.flat_connection_check_stage.go k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.flat_connection_check_stage.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L125-L129)@[irreducible]

**def
Tau.BookII.Closure.flat_connection_check_stage.go
(k v pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.flat_connection_check_stage.go_w`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L131-L138)@[irreducible]

**def
Tau.BookII.Closure.flat_connection_check_stage.go_w
(k v w pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.flat_connection_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L141-L149)
**def
Tau.BookII.Closure.flat_connection_check
(db : ℕ)
 :Bool**


[II.T50] Flat connection check for stages 1..db.
Equations
- Tau.BookII.Closure.flat_connection_check db = Tau.BookII.Closure.flat_connection_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.Closure.flat_connection_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L145-L148)@[irreducible]

**def
Tau.BookII.Closure.flat_connection_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.holonomy_trivial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L155-L178)
**def
Tau.BookII.Closure.holonomy_trivial_check
(k : ℕ)
 :Bool**


[II.P16] Holonomy check: for every starting point and every closed
loop of length ≤ 3, the flat connection returns to the origin.
Tests at stage k with small loops.
Equations
- Tau.BookII.Closure.holonomy_trivial_check k = Tau.BookII.Closure.holonomy_trivial_check.go k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Closure.holonomy_trivial_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L164-L169)@[irreducible]

**def
Tau.BookII.Closure.holonomy_trivial_check.go
(k x pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.holonomy_trivial_check.go_loop`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L171-L177)@[irreducible]

**def
Tau.BookII.Closure.holonomy_trivial_check.go_loop
(k x v pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.flat_connection_compatible_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L184-L186)
**theorem
Tau.BookII.Closure.flat_connection_compatible_2 :connection_check flat_connection 2 = true**


[II.D78] Flat connection is tower-compatible at stages 1-2.

---

### `Tau.BookII.Closure.flat_connection_flat_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L188-L190)
**theorem
Tau.BookII.Closure.flat_connection_flat_2 :flat_connection_check 2 = true**


[II.T50] Flat connection is flat at stages 1-2.

---

### `Tau.BookII.Closure.holonomy_trivial_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L192-L194)
**theorem
Tau.BookII.Closure.holonomy_trivial_1 :holonomy_trivial_check 1 = true**


[II.P16] Holonomy is trivial at stage 1.

---

### `Tau.BookII.Closure.holonomy_trivial_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L196-L198)
**theorem
Tau.BookII.Closure.holonomy_trivial_2 :holonomy_trivial_check 2 = true**


[II.P16] Holonomy is trivial at stage 2.

---

### `Tau.BookII.Closure.transport_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L200-L203)
**theorem
Tau.BookII.Closure.transport_zero
(k x : ℕ)
 :flat_connection.transport k x 0 = x % Polarity.primorial k**


Transport by 0 is identity.

---

### `Tau.BookII.Closure.transport_empty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/Connection.lean#L205-L208)
**theorem
Tau.BookII.Closure.transport_empty
(k x : ℕ)
 :parallel_transport flat_connection k x [] = x**


Parallel transport along empty path is identity.
