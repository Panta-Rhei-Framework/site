---
layout: taulib-doc
title: "TauLib.BookI.Polarity.PolarizedGerms"
permalink: /verify/taulib/docs/book-i-polarity-polarized-germs/
lane: verify
module_name: "TauLib.BookI.Polarity.PolarizedGerms"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Polarity.PolarizedGerms


Polarized omega-germs: B-polarized, C-polarized, and the crossing-point germ.

## Registry Cross-References


- [I.D26] Polarized Omega-Germ — `BPolarized`, `CPolarized`, `CrossingGerm`


## Ground Truth Sources


- chunk_0123_M001424: Branch predicates ∂τ₃^B, ∂τ₃^C (lines 369-386)

- chunk_0155_M001710: Crossing-point germ, σ-fixed germ class


## Mathematical Content


Given the spectral signature σ_N(p) = (B_max, C_max), the polarity at each
primorial stage provides a sequence of B/C channel values. An omega-germ is:


- B-polarized if the C-channel eventually freezes AND the B-channel keeps refining

- C-polarized if the B-channel eventually freezes AND the C-channel keeps refining

- A crossing-point germ if neither channel freezes


The crossing-point germ corresponds to the unique element ω where both
channels continue to refine at every stage. It exists as a structural
consequence of the bipolar partition.

---

### `Tau.Polarity.b_channel_seq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L39-L40)
**def
Tau.Polarity.b_channel_seq
(p k : Denotation.TauIdx)
 :Denotation.TauIdx**


B-channel sequence at primorial stages: B_max for prime p at bound M_k.
Equations
- Tau.Polarity.b_channel_seq p k = Tau.Polarity.b_max p (Tau.Polarity.primorial k)
Instances For

---

### `Tau.Polarity.c_channel_seq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L42-L43)
**def
Tau.Polarity.c_channel_seq
(p k : Denotation.TauIdx)
 :Denotation.TauIdx**


C-channel sequence at primorial stages: C_max for prime p at bound M_k.
Equations
- Tau.Polarity.c_channel_seq p k = Tau.Polarity.c_max p (Tau.Polarity.primorial k)
Instances For

---

### `Tau.Polarity.eventually_constant_at`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L49-L52)
**def
Tau.Polarity.eventually_constant_at
(f : Nat → Nat)

(d : Nat)
 :Prop**


A sequence (represented as function Nat → Nat) is eventually constant
at depth d if f(k) = f(d) for all k ≥ d.
Equations
- Tau.Polarity.eventually_constant_at f d = ∀ (k : Nat), k ≥ d → f k = f d
Instances For

---

### `Tau.Polarity.eventually_constant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L54-L56)
**def
Tau.Polarity.eventually_constant
(f : Nat → Nat)
 :Prop**


A sequence is eventually constant if there exists such a depth.
Equations
- Tau.Polarity.eventually_constant f = ∃ (d : Nat), Tau.Polarity.eventually_constant_at f d
Instances For

---

### `Tau.Polarity.const_check_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L58-L64)@[irreducible]

**def
Tau.Polarity.const_check_go
(f : Nat → Nat)

(d0 d1 fuel : Nat)
 :Bool**


Computable check: is the sequence constant from depth d₀ to d₁?
Equations
- Tau.Polarity.const_check_go f d0 d1 fuel = if fuel = 0 then true
 else if d0 > d1 then true else f d0 == f (d0 + 1) && Tau.Polarity.const_check_go f (d0 + 1) d1 (fuel - 1)
Instances For

---

### `Tau.Polarity.const_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L66-L67)
**def
Tau.Polarity.const_check
(f : Nat → Nat)

(from_depth to_depth : Nat)
 :Bool**

Equations
- Tau.Polarity.const_check f from_depth to_depth = Tau.Polarity.const_check_go f from_depth to_depth (to_depth - from_depth + 1)
Instances For

---

### `Tau.Polarity.cofinal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L73-L76)
**def
Tau.Polarity.cofinal
(f : Nat → Nat)
 :Prop**


A sequence is cofinal if it takes nonzero values at arbitrarily large indices.
Ground truth (chunk_0123): ∀M ∃n≥M, Bₙ ≠ α₁.
Equations
- Tau.Polarity.cofinal f = ∀ (M : Nat), ∃ (k : Nat), k ≥ M ∧ f k ≠ 0
Instances For

---

### `Tau.Polarity.cofinal_check_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L78-L84)@[irreducible]

**def
Tau.Polarity.cofinal_check_go
(f : Nat → Nat)

(i to_depth fuel : Nat)
 :Bool**


Computable check: does the sequence have a nonzero value between from_depth and to_depth?
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.cofinal_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L86-L87)
**def
Tau.Polarity.cofinal_check
(f : Nat → Nat)

(from_depth to_depth : Nat)
 :Bool**

Equations
- Tau.Polarity.cofinal_check f from_depth to_depth = Tau.Polarity.cofinal_check_go f from_depth to_depth (to_depth - from_depth + 1)
Instances For

---

### `Tau.Polarity.BPolarized`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L93-L97)
**def
Tau.Polarity.BPolarized
(p : Denotation.TauIdx)
 :Prop**


[I.D26] B-polarized at a prime p: C-channel eventually freezes AND B-channel
keeps refining (cofinal). Ground truth (chunk_0123, lines 369-386):
∂τ₃^B := { [x•] | ∃N ∀n≥N, Cₙ=α₁ ∧ ∀M ∃n≥M, Bₙ≠α₁ }.
Equations
- Tau.Polarity.BPolarized p = (Tau.Polarity.eventually_constant (Tau.Polarity.c_channel_seq p) ∧ Tau.Polarity.cofinal (Tau.Polarity.b_channel_seq p))
Instances For

---

### `Tau.Polarity.CPolarized`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L99-L102)
**def
Tau.Polarity.CPolarized
(p : Denotation.TauIdx)
 :Prop**


C-polarized at a prime p: B-channel eventually freezes AND C-channel
keeps refining (cofinal). Symmetric to BPolarized.
Equations
- Tau.Polarity.CPolarized p = (Tau.Polarity.eventually_constant (Tau.Polarity.b_channel_seq p) ∧ Tau.Polarity.cofinal (Tau.Polarity.c_channel_seq p))
Instances For

---

### `Tau.Polarity.CrossingGerm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L104-L107)
**def
Tau.Polarity.CrossingGerm
(p : Denotation.TauIdx)
 :Prop**


Crossing germ at a prime p: neither channel eventually freezes.
Corresponds to the unique wedge point of the lemniscate ∂τ₃ ≅ S¹∨S¹.
Equations
- Tau.Polarity.CrossingGerm p = (¬Tau.Polarity.eventually_constant (Tau.Polarity.c_channel_seq p) ∧ ¬Tau.Polarity.eventually_constant (Tau.Polarity.b_channel_seq p))
Instances For

---

### `Tau.Polarity.b_polarized_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L113-L117)
**def
Tau.Polarity.b_polarized_check
(p d : Denotation.TauIdx)
 :Bool**


Check if prime p appears B-polarized up to primorial depth d:
C-channel constant from some point AND B-channel has nonzero values.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.c_polarized_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L119-L123)
**def
Tau.Polarity.c_polarized_check
(p d : Denotation.TauIdx)
 :Bool**


Check if prime p appears C-polarized up to primorial depth d:
B-channel constant from some point AND C-channel has nonzero values.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.germ_status`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L125-L129)
**def
Tau.Polarity.germ_status
(p d : Denotation.TauIdx)
 :String**


Polarity status string for a prime at a given primorial depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.channel_display_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L135-L144)@[irreducible]

**def
Tau.Polarity.channel_display_go
(p k d fuel : Nat)

(acc : List (Nat × Nat))
 :List (Nat × Nat)**


Display the B and C channel sequences for a prime at primorial stages 1..d.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.channel_display`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/PolarizedGerms.lean#L146-L147)
**def
Tau.Polarity.channel_display
(p d : Denotation.TauIdx)
 :List (Denotation.TauIdx × Denotation.TauIdx)**

Equations
- Tau.Polarity.channel_display p d = Tau.Polarity.channel_display_go p 1 d d []
Instances For
