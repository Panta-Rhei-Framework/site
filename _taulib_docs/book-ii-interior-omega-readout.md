---
layout: taulib-doc
title: "TauLib.BookII.Interior.OmegaReadout"
permalink: /verify/taulib/docs/book-ii-interior-omega-readout/
lane: verify
module_name: "TauLib.BookII.Interior.OmegaReadout"
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

# TauLib.BookII.Interior.OmegaReadout


The omega readout: how ABCD coordinates behave as paths approach ω.

## Registry Cross-References


- [II.D04] Omega Readout — `FiberDominance`, `classify_dominance`

- [II.T02] Fiber Degeneration at Omega — `fiber_degeneration_primorial`

- [II.P01] Lemniscate as Coordinate Limit — `lemniscate_coordinate_limit`


## Mathematical Content


As objects approach ω along the primorial tower P_k = p₁·...·p_k:


- Base (D, A): both components → ∞ (universal collapse to Ω)

- Fiber (B, C): locked by B/C competition into bipolar structure


Three fiber limit types:


- B-dominant (B ≫ C): maps to e₊-lobe of ℒ

- C-dominant (C ≫ B): maps to e₋-lobe of ℒ

- Balanced (B ≈ C): maps to crossing point (node of ℒ)


The lemniscate ℒ ≅ pr_fiber(Φ_ω): fiber limits at ω reproduce
the algebraic lemniscate from Book I (I.D18).

---

### `Tau.BookII.Interior.FiberDominance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L38-L44)
**inductive
Tau.BookII.Interior.FiberDominance :Type**


[II.D04] Classification of fiber (B,C) behavior at ω-limit.
Determines which lobe of the lemniscate ℒ a path approaches.

- b_dominant : FiberDominance
- c_dominant : FiberDominance
- balanced : FiberDominance
Instances For

---

### `Tau.BookII.Interior.instReprFiberDominance.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L44-L44)
**def
Tau.BookII.Interior.instReprFiberDominance.repr :FiberDominance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.instReprFiberDominance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L44-L44)
**instance
Tau.BookII.Interior.instReprFiberDominance :Repr FiberDominance**

Equations
- Tau.BookII.Interior.instReprFiberDominance = { reprPrec := Tau.BookII.Interior.instReprFiberDominance.repr }

---

### `Tau.BookII.Interior.instDecidableEqFiberDominance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L44-L44)
**instance
Tau.BookII.Interior.instDecidableEqFiberDominance :DecidableEq FiberDominance**

Equations
- Tau.BookII.Interior.instDecidableEqFiberDominance x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Interior.classify_dominance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L46-L50)
**def
Tau.BookII.Interior.classify_dominance
(b c : Denotation.TauIdx)
 :FiberDominance**


Classify fiber dominance from (B, C) coordinates.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.TauAdmissiblePoint.fiber_dominance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L52-L54)
**def
Tau.BookII.Interior.TauAdmissiblePoint.fiber_dominance
(p : TauAdmissiblePoint)
 :FiberDominance**


Classify an admissible point's fiber dominance.
Equations
- p.fiber_dominance = Tau.BookII.Interior.classify_dominance p.b p.c
Instances For

---

### `Tau.BookII.Interior.omega_readout`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L60-L65)
**def
Tau.BookII.Interior.omega_readout
(p : TauAdmissiblePoint)
 :Denotation.TauIdx × Denotation.TauIdx × FiberDominance**


[II.D04] Omega readout of an admissible point.
Returns (base_A, base_D, fiber_dominance).
At ω-limit: base → (Ω,Ω), fiber → lobe of ℒ.
Equations
- Tau.BookII.Interior.omega_readout p = (p.a, p.d, p.fiber_dominance)
Instances For

---

### `Tau.BookII.Interior.dominance_to_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L67-L73)
**def
Tau.BookII.Interior.dominance_to_sector
(fd : FiberDominance)
 :Polarity.SectorPair**


Sector assignment from fiber dominance:
B-dominant → e₊-sector, C-dominant → e₋-sector, balanced → both.
Equations
- Tau.BookII.Interior.dominance_to_sector Tau.BookII.Interior.FiberDominance.b_dominant = Tau.Polarity.e_plus_sector
- Tau.BookII.Interior.dominance_to_sector Tau.BookII.Interior.FiberDominance.c_dominant = Tau.Polarity.e_minus_sector
- Tau.BookII.Interior.dominance_to_sector Tau.BookII.Interior.FiberDominance.balanced = { b_sector := 1, c_sector := 1 }
Instances For

---

### `Tau.BookII.Interior.primorial_fiber_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L79-L82)
**def
Tau.BookII.Interior.primorial_fiber_check :Bool**


[II.T02] Primorial path fiber degeneration.
Along the primorial tower, B = C = 1 always: balanced (crossing point).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_base_diverges`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L84-L92)
**def
Tau.BookII.Interior.primorial_base_diverges :Bool**


[II.T02] Primorial base readout: A-values exhaust primes.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_base_diverges.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L90-L92)
**def
Tau.BookII.Interior.primorial_base_diverges.go :List Denotation.TauIdx → Bool**

Equations
- Tau.BookII.Interior.primorial_base_diverges.go [] = true
- Tau.BookII.Interior.primorial_base_diverges.go [head] = true
- Tau.BookII.Interior.primorial_base_diverges.go (x_1 :: y :: rest) = (decide (x_1 < y) && Tau.BookII.Interior.primorial_base_diverges.go (y :: rest))
Instances For

---

### `Tau.BookII.Interior.tower_path_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L94-L97)
**def
Tau.BookII.Interior.tower_path_check :Bool**


[II.T02] Tower path (X_n = 2^n) is B-dominant.
Equations
- Tau.BookII.Interior.tower_path_check = (List.map Tau.BookII.Interior.from_tau_idx [4, 8, 16, 32, 64, 128, 256]).all
 fun (p : Tau.BookII.Interior.TauAdmissiblePoint) => decide (p.b > p.c)
Instances For

---

### `Tau.BookII.Interior.base_collapse_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L99-L107)
**def
Tau.BookII.Interior.base_collapse_check :Bool**


[II.T02, clause 1] Base collapse: both A and D grow along primorials.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.base_collapse_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L105-L107)
**def
Tau.BookII.Interior.base_collapse_check.go :List (Denotation.TauIdx × Denotation.TauIdx) → Bool**

Equations
- Tau.BookII.Interior.base_collapse_check.go [] = true
- Tau.BookII.Interior.base_collapse_check.go [head] = true
- Tau.BookII.Interior.base_collapse_check.go ((a₁, d₁) :: (a₂, d₂) :: rest) = (decide (a₁ < a₂) && decide (d₁ < d₂) && Tau.BookII.Interior.base_collapse_check.go ((a₂, d₂) :: rest))
Instances For

---

### `Tau.BookII.Interior.lemniscate_sector_idem_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L113-L132)
**def
Tau.BookII.Interior.lemniscate_sector_idem_check :Bool**


[II.P01] The three fiber limit types correspond to the algebraic
lemniscate structure:


- B-dominant → e₊-lobe (I.D21 e₊ idempotent)

- C-dominant → e₋-lobe (I.D21 e₋ idempotent)

- Balanced → crossing point (node where both sectors active)


Verification: sector assignment is idempotent-compatible.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_balanced`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L162-L162)
**theorem
Tau.BookII.Interior.primorial_balanced :primorial_fiber_check = true**


---

### `Tau.BookII.Interior.base_diverges`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L163-L163)
**theorem
Tau.BookII.Interior.base_diverges :primorial_base_diverges = true**


---

### `Tau.BookII.Interior.lemniscate_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/OmegaReadout.lean#L164-L164)
**theorem
Tau.BookII.Interior.lemniscate_compat :lemniscate_sector_idem_check = true**
