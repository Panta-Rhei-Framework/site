---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.BoundaryCharacters"
permalink: /verify/taulib/docs/book-ii-central-theorem-boundary-characters/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.BoundaryCharacters"
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

# TauLib.BookII.CentralTheorem.BoundaryCharacters


Idempotent-supported boundary characters and the character algebra ring structure.

## Registry Cross-References


- [II.D59] Idempotent-Supported Character -- `IdempotentCharacter`, `idemp_character_check`

- [II.P14] Character Algebra Ring Structure -- `character_add_check`, `character_mul_check`


## Mathematical Content


A boundary character chi : Z-hat_tau -> H_tau is **idempotent-supported** if
chi = e_plus * chi_plus + e_minus * chi_minus. Every spectral character valued
in calibrated H_tau admits this unique decomposition.

In the sector-pair model, an idempotent-supported character at stage k on
input x is a SectorPair (B-component, C-component). The character is
determined by its B-channel and C-channel projections:

e_plus * (B, C) = (B, 0) -- B-channel
e_minus * (B, C) = (0, C) -- C-channel

The decomposition is unique because e_plus + e_minus = (1, 1) and
e_plus * e_minus = (0, 0).

**Character tower coherence**: reduce(chi(x, k+1), k) = chi(x, k).
This connects boundary characters to the primorial inverse system.

**Character algebra (II.P14)**: The set of idempotent-supported characters
forms a ring under pointwise operations. Addition and multiplication of
characters preserve idempotent support because the sector algebra is
closed under componentwise addition and multiplication.

---

### `Tau.BookII.CentralTheorem.IdempotentCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L48-L63)
**structure
Tau.BookII.CentralTheorem.IdempotentCharacter :Type**


[II.D59] An idempotent-supported character is a stagewise map
from (x, k) to a SectorPair, representing the B-channel and
C-channel components. The character is determined by its
idempotent projections: chi = e_plus * chi_plus + e_minus * chi_minus.

In the primorial model, the character at stage k on input x is:


- B-component: the B-coordinate of from_tau_idx(reduce(x, k))

- C-component: the C-coordinate of from_tau_idx(reduce(x, k))


This is the canonical character associated to x.

- b_ch : Denotation.TauIdx → Denotation.TauIdx → ℤ
B-channel function: (x, k) -> B-component at stage k.

- c_ch : Denotation.TauIdx → Denotation.TauIdx → ℤ
C-channel function: (x, k) -> C-component at stage k.

Instances For

---

### `Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L63-L63)
**def
Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter.default :IdempotentCharacter**

Equations
- Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter.default = { b_ch := default, c_ch := default }
Instances For

---

### `Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L63-L63)
**instance
Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter :Inhabited IdempotentCharacter**

Equations
- Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter = { default := Tau.BookII.CentralTheorem.instInhabitedIdempotentCharacter.default }

---

### `Tau.BookII.CentralTheorem.IdempotentCharacter.eval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L65-L67)
**def
Tau.BookII.CentralTheorem.IdempotentCharacter.eval
(chi : IdempotentCharacter)

(x k : Denotation.TauIdx)
 :Polarity.SectorPair**


Evaluate an idempotent character at (x, k) as a SectorPair.
Equations
- chi.eval x k = { b_sector := chi.b_ch x k, c_sector := chi.c_ch x k }
Instances For

---

### `Tau.BookII.CentralTheorem.canonical_character`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L69-L73)
**def
Tau.BookII.CentralTheorem.canonical_character :IdempotentCharacter**


The canonical idempotent character: read off B and C from the ABCD chart
of the stage-k reduction.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.chi_plus_character`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L75-L78)
**def
Tau.BookII.CentralTheorem.chi_plus_character :IdempotentCharacter**


The chi_plus character: B-channel only.
Equations
- Tau.BookII.CentralTheorem.chi_plus_character = { b_ch := fun (x k : Tau.Denotation.TauIdx) => ↑(Tau.Polarity.reduce x k),
 c_ch := fun (x x_1 : Tau.Denotation.TauIdx) => 0 }
Instances For

---

### `Tau.BookII.CentralTheorem.chi_minus_character`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L80-L83)
**def
Tau.BookII.CentralTheorem.chi_minus_character :IdempotentCharacter**


The chi_minus character: C-channel only.
Equations
- Tau.BookII.CentralTheorem.chi_minus_character = { b_ch := fun (x x_1 : Tau.Denotation.TauIdx) => 0,
 c_ch := fun (x k : Tau.Denotation.TauIdx) => ↑(Tau.Polarity.reduce x k) }
Instances For

---

### `Tau.BookII.CentralTheorem.idemp_character_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L89-L115)
**def
Tau.BookII.CentralTheorem.idemp_character_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D59] Idempotent decomposition check: for each x at stage k,
the character value (B, C) satisfies
e_plus * (B, C) + e_minus * (B, C) = (B, C).

This verifies that the character IS its own idempotent decomposition:
the B-channel and C-channel projections sum to the full character.
Equations
- Tau.BookII.CentralTheorem.idemp_character_check bound db = Tau.BookII.CentralTheorem.idemp_character_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.idemp_character_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L98-L114)@[irreducible]

**def
Tau.BookII.CentralTheorem.idemp_character_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.character_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L121-L146)
**def
Tau.BookII.CentralTheorem.character_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


Character tower coherence: reduce(chi(x, k+1), k) = chi(x, k).
For the canonical character, this means:


- B: the B-coordinate of from_tau_idx(reduce(reduce(x, k+1), k))
equals the B-coordinate of from_tau_idx(reduce(x, k))

- C: similarly for the C-coordinate


Since reduce(reduce(x, k+1), k) = reduce(x, k) by reduction_compat,
the same input to from_tau_idx yields the same ABCD chart.
Equations
- Tau.BookII.CentralTheorem.character_tower_check bound db = Tau.BookII.CentralTheorem.character_tower_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.character_tower_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L132-L145)@[irreducible]

**def
Tau.BookII.CentralTheorem.character_tower_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.IdempotentCharacter.add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L152-L155)
**def
Tau.BookII.CentralTheorem.IdempotentCharacter.add
(chi1 chi2 : IdempotentCharacter)
 :IdempotentCharacter**


Add two idempotent characters pointwise.
Equations
- chi1.add chi2 = { b_ch := fun (x k : Tau.Denotation.TauIdx) => chi1.b_ch x k + chi2.b_ch x k,
 c_ch := fun (x k : Tau.Denotation.TauIdx) => chi1.c_ch x k + chi2.c_ch x k }
Instances For

---

### `Tau.BookII.CentralTheorem.character_add_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L157-L182)
**def
Tau.BookII.CentralTheorem.character_add_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P14] Character addition preserves idempotent support:
if chi1 and chi2 are idempotent-supported, then chi1 + chi2 is also
idempotent-supported.

Proof: e_plus * (B1+B2, C1+C2) = (B1+B2, 0) and
e_minus * (B1+B2, C1+C2) = (0, C1+C2), and their sum
= (B1+B2, C1+C2) = (chi1 + chi2).
Equations
- Tau.BookII.CentralTheorem.character_add_check bound db = Tau.BookII.CentralTheorem.character_add_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.character_add_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L167-L181)@[irreducible]

**def
Tau.BookII.CentralTheorem.character_add_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.IdempotentCharacter.mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L188-L191)
**def
Tau.BookII.CentralTheorem.IdempotentCharacter.mul
(chi1 chi2 : IdempotentCharacter)
 :IdempotentCharacter**


Multiply two idempotent characters pointwise (using SectorPair.mul).
Equations
- chi1.mul chi2 = { b_ch := fun (x k : Tau.Denotation.TauIdx) => chi1.b_ch x k * chi2.b_ch x k,
 c_ch := fun (x k : Tau.Denotation.TauIdx) => chi1.c_ch x k * chi2.c_ch x k }
Instances For

---

### `Tau.BookII.CentralTheorem.character_mul_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L193-L219)
**def
Tau.BookII.CentralTheorem.character_mul_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P14] Character multiplication preserves idempotent support:
if chi1 and chi2 are idempotent-supported, then chi1 * chi2 is also
idempotent-supported.

Proof: multiplication in sector coordinates is componentwise:
(B1, C1) * (B2, C2) = (B1*B2, C1*C2).
e_plus * (B1*B2, C1*C2) = (B1*B2, 0) and
e_minus * (B1*B2, C1*C2) = (0, C1*C2).
Equations
- Tau.BookII.CentralTheorem.character_mul_check bound db = Tau.BookII.CentralTheorem.character_mul_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.character_mul_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L204-L218)@[irreducible]

**def
Tau.BookII.CentralTheorem.character_mul_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.zero_character`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L225-L227)
**def
Tau.BookII.CentralTheorem.zero_character :IdempotentCharacter**


Zero character: the additive identity.
Equations
- Tau.BookII.CentralTheorem.zero_character = { b_ch := fun (x x_1 : Tau.Denotation.TauIdx) => 0, c_ch := fun (x x_1 : Tau.Denotation.TauIdx) => 0 }
Instances For

---

### `Tau.BookII.CentralTheorem.unit_character`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L229-L231)
**def
Tau.BookII.CentralTheorem.unit_character :IdempotentCharacter**


Unit character: the multiplicative identity.
Equations
- Tau.BookII.CentralTheorem.unit_character = { b_ch := fun (x x_1 : Tau.Denotation.TauIdx) => 1, c_ch := fun (x x_1 : Tau.Denotation.TauIdx) => 1 }
Instances For

---

### `Tau.BookII.CentralTheorem.character_add_identity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L233-L246)
**def
Tau.BookII.CentralTheorem.character_add_identity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P14] Ring axiom: additive identity check.
chi + 0 = chi for the canonical character.
Equations
- Tau.BookII.CentralTheorem.character_add_identity_check bound db = Tau.BookII.CentralTheorem.character_add_identity_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.character_add_identity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L238-L245)@[irreducible]

**def
Tau.BookII.CentralTheorem.character_add_identity_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.character_mul_identity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L248-L261)
**def
Tau.BookII.CentralTheorem.character_mul_identity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P14] Ring axiom: multiplicative identity check.
chi * 1 = chi for the canonical character.
Equations
- Tau.BookII.CentralTheorem.character_mul_identity_check bound db = Tau.BookII.CentralTheorem.character_mul_identity_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.character_mul_identity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L253-L260)@[irreducible]

**def
Tau.BookII.CentralTheorem.character_mul_identity_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.character_distributive_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L263-L283)
**def
Tau.BookII.CentralTheorem.character_distributive_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P14] Ring axiom: distributivity check.
chi1 * (chi2 + chi3) = chi1*chi2 + chi1*chi3.
Equations
- Tau.BookII.CentralTheorem.character_distributive_check bound db = Tau.BookII.CentralTheorem.character_distributive_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.character_distributive_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L268-L282)@[irreducible]

**def
Tau.BookII.CentralTheorem.character_distributive_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.full_boundary_characters_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L289-L302)
**def
Tau.BookII.CentralTheorem.full_boundary_characters_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D59 + II.P14] Complete boundary character verification:


- Idempotent decomposition (II.D59)

- Tower coherence (II.D59)

- Addition preserves support (II.P14)

- Multiplication preserves support (II.P14)

- Ring axioms: additive identity, multiplicative identity, distributivity

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.idemp_decomp_recovery`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L308-L314)
**theorem
Tau.BookII.CentralTheorem.idemp_decomp_recovery
(sp : Polarity.SectorPair)
 :(Polarity.e_plus_sector.mul sp).add (Polarity.e_minus_sector.mul sp) = sp**


[II.D59] Idempotent decomposition is always valid:
e_plus * sp + e_minus * sp = sp for any SectorPair sp.
This is the algebraic core of idempotent support.

---

### `Tau.BookII.CentralTheorem.b_channel_kills_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L316-L319)
**theorem
Tau.BookII.CentralTheorem.b_channel_kills_c
(sp : Polarity.SectorPair)
 :(Polarity.e_plus_sector.mul sp).c_sector = 0**


[II.D59] The B-channel projection kills the C-sector.

---

### `Tau.BookII.CentralTheorem.c_channel_kills_b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L321-L324)
**theorem
Tau.BookII.CentralTheorem.c_channel_kills_b
(sp : Polarity.SectorPair)
 :(Polarity.e_minus_sector.mul sp).b_sector = 0**


[II.D59] The C-channel projection kills the B-sector.

---

### `Tau.BookII.CentralTheorem.character_tower_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L326-L331)
**theorem
Tau.BookII.CentralTheorem.character_tower_structural
(x : Denotation.TauIdx)

{k : Denotation.TauIdx}
 :k ≤ k + 1 → Polarity.reduce (Polarity.reduce x (k + 1)) k = Polarity.reduce x k**


[II.D59] Character tower coherence: the canonical character input
at stage k equals the stage-(k+1) input reduced.
reduce(reduce(x, k+1), k) = reduce(x, k).

---

### `Tau.BookII.CentralTheorem.character_add_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L333-L339)
**theorem
Tau.BookII.CentralTheorem.character_add_structural
(sp1 sp2 : Polarity.SectorPair)
 :(Polarity.e_plus_sector.mul (sp1.add sp2)).add (Polarity.e_minus_sector.mul (sp1.add sp2)) = sp1.add sp2**


[II.P14] Character addition preserves idempotent support (structural):
for any sp1 sp2, the sum sp1 + sp2 satisfies the decomposition.

---

### `Tau.BookII.CentralTheorem.character_mul_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L341-L347)
**theorem
Tau.BookII.CentralTheorem.character_mul_structural
(sp1 sp2 : Polarity.SectorPair)
 :(Polarity.e_plus_sector.mul (sp1.mul sp2)).add (Polarity.e_minus_sector.mul (sp1.mul sp2)) = sp1.mul sp2**


[II.P14] Character multiplication preserves idempotent support (structural):
for any sp1 sp2, the product sp1 * sp2 satisfies the decomposition.

---

### `Tau.BookII.CentralTheorem.sector_distributive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L349-L354)
**theorem
Tau.BookII.CentralTheorem.sector_distributive
(a b c : Polarity.SectorPair)
 :a.mul (b.add c) = (a.mul b).add (a.mul c)**


[II.P14] Distributivity of sector multiplication over addition.

---

### `Tau.BookII.CentralTheorem.idemp_char_20_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L390-L391)
**theorem
Tau.BookII.CentralTheorem.idemp_char_20_4 :idemp_character_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.char_tower_20_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L394-L395)
**theorem
Tau.BookII.CentralTheorem.char_tower_20_4 :character_tower_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.char_add_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L398-L399)
**theorem
Tau.BookII.CentralTheorem.char_add_15_3 :character_add_check 15 3 = true**


---

### `Tau.BookII.CentralTheorem.char_mul_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L402-L403)
**theorem
Tau.BookII.CentralTheorem.char_mul_15_3 :character_mul_check 15 3 = true**


---

### `Tau.BookII.CentralTheorem.char_add_id_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L406-L407)
**theorem
Tau.BookII.CentralTheorem.char_add_id_15_3 :character_add_identity_check 15 3 = true**


---

### `Tau.BookII.CentralTheorem.char_mul_id_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L409-L410)
**theorem
Tau.BookII.CentralTheorem.char_mul_id_15_3 :character_mul_identity_check 15 3 = true**


---

### `Tau.BookII.CentralTheorem.char_distrib_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L412-L413)
**theorem
Tau.BookII.CentralTheorem.char_distrib_15_3 :character_distributive_check 15 3 = true**


---

### `Tau.BookII.CentralTheorem.full_bnd_char_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L416-L417)
**theorem
Tau.BookII.CentralTheorem.full_bnd_char_15_3 :full_boundary_characters_check 15 3 = true**
