---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.BndLift"
permalink: /verify/taulib/docs/book-ii-hartogs-bnd-lift/
lane: verify
module_name: "TauLib.BookII.Hartogs.BndLift"
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

# TauLib.BookII.Hartogs.BndLift


The BndLift construction: promoting boundary data at stage n to
interior data at stage n+1 via CRT decomposition.

## Registry Cross-References


- [II.D36] BndLift Construction — `bndlift`, `bndlift_value`

- [II.T26] BndLift Existence — `bndlift_existence_check`

- [II.P08] Bipolar Channel Independence — `bipolar_channel_independence`


## Mathematical Content


BndLift_n promotes a function defined on Z/P_n Z to a function on
Z/P_{n+1} Z. The mechanism is the Chinese Remainder Theorem:

Z/P_{n+1} Z ≅ Z/P_n Z × Z/p_{n+1} Z

since P_{n+1} = P_n · p_{n+1} and gcd(P_n, p_{n+1}) = 1.

Given stage-n data f_n : Z/P_n Z → H_τ, the lift produces
stage-(n+1) data f_{n+1} : Z/P_{n+1} Z → H_τ by:

f_{n+1}(x) = f_n(x mod P_n) + extension(x mod p_{n+1})

The extension decomposes into two independent channels via e₊, e₋:


- B-channel extension depends only on the γ-orbit (π-calibrated)

- C-channel extension depends only on the η-orbit (e-calibrated)


Tower coherence requires: reduce(f_{n+1}(x), n) = f_n(reduce(x, n)).
In our model, this is: reduce(x, n+1) reduced to stage n equals reduce(x, n),
which is exactly the reduction compatibility theorem from ModArith.

## Key Insight


BndLift at the TauIdx level is essentially the reduce map viewed
from one stage higher:

bndlift(x, n) = reduce(x, n+1)

This "knows" about stage n+1 because P_{n+1} = P_n · p_{n+1}, and the
CRT decomposition gives the new prime factor. Tower coherence then
follows directly from reduction_compat.

---

### `Tau.BookII.Hartogs.crt_decompose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L58-L64)
**def
Tau.BookII.Hartogs.crt_decompose
(x stage : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx**


CRT decomposition of x ∈ Z/P_{n+1}Z into (a, b) where
a = x mod P_n (stage-n projection) and b = x mod p_{n+1} (new factor).
This witnesses: Z/P_{n+1}Z ≅ Z/P_nZ × Z/p_{n+1}Z.
Equations
- Tau.BookII.Hartogs.crt_decompose x stage = (x % Tau.Polarity.primorial stage, x % Tau.Polarity.nth_prime (stage + 1))
Instances For

---

### `Tau.BookII.Hartogs.crt_unique_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L66-L83)
**def
Tau.BookII.Hartogs.crt_unique_check
(stage : Denotation.TauIdx)
 :Bool**


CRT check: a and b uniquely determine x mod P_{n+1}.
For all x in [0, P_{n+1}), the pair (x mod P_n, x mod p_{n+1})
is unique. Verify by checking no collisions in range.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_unique_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L74-L82)@[irreducible]

**def
Tau.BookII.Hartogs.crt_unique_check.go
(stage : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_coverage_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L85-L102)
**def
Tau.BookII.Hartogs.crt_coverage_check
(stage : Denotation.TauIdx)
 :Bool**


CRT coverage: every pair (a, b) with 0 ≤ a < P_n and 0 ≤ b < p_{n+1}
is hit by some x in [0, P_{n+1}).
Check: the number of distinct CRT pairs equals P_n × p_{n+1} = P_{n+1}.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_coverage_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L98-L101)@[irreducible]

**def
Tau.BookII.Hartogs.crt_coverage_check.go
(stage : Denotation.TauIdx)

(x fuel acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bndlift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L108-L119)
**def
Tau.BookII.Hartogs.bndlift
(x stage : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D36] BndLift: promote stage-n data to stage-(n+1) data.

At the TauIdx level, the lift of x to stage (n+1) is simply
reduce(x, n+1): we read off the residue modulo P_{n+1}.

This is the key observation: the BndLift construction at the
level of the inverse system IS the reduction map, viewed from
one stage higher. The new information at stage n+1 is the
residue mod p_{n+1}, which CRT decomposes into a separate
independent coordinate.
Equations
- Tau.BookII.Hartogs.bndlift x stage = Tau.Polarity.reduce x (stage + 1)
Instances For

---

### `Tau.BookII.Hartogs.bndlift_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L121-L127)
**def
Tau.BookII.Hartogs.bndlift_value
(x stage : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx**


Explicit BndLift value showing CRT structure:
bndlift_value(x, n) = reduce(x, n+1), and we can decompose
this into its stage-n part and its new-prime part.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bndlift_coherent_pointwise`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L129-L133)
**def
Tau.BookII.Hartogs.bndlift_coherent_pointwise
(x stage : Denotation.TauIdx)
 :Bool**


The stage-n part of the lift equals the stage-n reduction.
This is the core tower coherence property:
reduce(bndlift(x, n), n) = reduce(x, n).
Equations
- Tau.BookII.Hartogs.bndlift_coherent_pointwise x stage = (Tau.Polarity.reduce (Tau.BookII.Hartogs.bndlift x stage) stage == Tau.Polarity.reduce x stage)
Instances For

---

### `Tau.BookII.Hartogs.bndlift_existence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L139-L156)
**def
Tau.BookII.Hartogs.bndlift_existence_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.T26] BndLift existence theorem (tower coherence).
For all x in [2, bound] and stages in [1, k_max]:
reduce(bndlift(x, n), n) = reduce(x, n).

This is a direct consequence of reduction_compat: since
bndlift(x, n) = reduce(x, n+1), we have
reduce(reduce(x, n+1), n) = reduce(x, n) because n ≤ n+1.
Equations
- Tau.BookII.Hartogs.bndlift_existence_check k_max bound = Tau.BookII.Hartogs.bndlift_existence_check.go k_max bound 1 2 (k_max * bound + k_max + bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.bndlift_existence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L149-L155)@[irreducible]

**def
Tau.BookII.Hartogs.bndlift_existence_check.go
(k_max bound : Denotation.TauIdx)

(stage x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.tower_coherence_multi`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L158-L173)
**def
Tau.BookII.Hartogs.tower_coherence_multi
(k_max bound : Denotation.TauIdx)
 :Bool**


Tower coherence across multiple levels: reducing a lift at stage n+2
back to stage n should equal the direct stage-n reduction.
reduce(bndlift(bndlift(x, n), n+1), n) = reduce(x, n).
Equations
- Tau.BookII.Hartogs.tower_coherence_multi k_max bound = Tau.BookII.Hartogs.tower_coherence_multi.go k_max bound 1 2 (k_max * bound + k_max + bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.tower_coherence_multi.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L164-L172)@[irreducible]

**def
Tau.BookII.Hartogs.tower_coherence_multi.go
(k_max bound : Denotation.TauIdx)

(stage x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.lift_information_gain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L175-L187)
**def
Tau.BookII.Hartogs.lift_information_gain
(k_max : Denotation.TauIdx)
 :Bool**


Lift monotonicity: at stage n+1, the lifted value carries
strictly more information than the stage-n projection.
Evidence: P_{n+1} > P_n, so more residue classes are distinguished.
Equations
- Tau.BookII.Hartogs.lift_information_gain k_max = Tau.BookII.Hartogs.lift_information_gain.go k_max 1 (k_max + 1)
Instances For

---

### `Tau.BookII.Hartogs.lift_information_gain.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L181-L186)@[irreducible]

**def
Tau.BookII.Hartogs.lift_information_gain.go
(k_max : Denotation.TauIdx)

(stage fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_independence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L193-L215)
**def
Tau.BookII.Hartogs.crt_independence_check
(stage bound : Denotation.TauIdx)
 :Bool**


The new prime at stage n+1 provides an independent coordinate.
For x, y with same stage-n projection but different stage-(n+1) projections,
they must differ in the new prime factor.
Evidence: find pairs (x, y) with reduce(x,n) = reduce(y,n) but
reduce(x,n+1) ≠ reduce(y,n+1), and check their p_{n+1}-residues differ.
Equations
- Tau.BookII.Hartogs.crt_independence_check stage bound = Tau.BookII.Hartogs.crt_independence_check.go stage bound 2 3 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.crt_independence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L201-L214)@[irreducible]

**def
Tau.BookII.Hartogs.crt_independence_check.go
(stage bound : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bipolar_channel_independence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L221-L250)
**def
Tau.BookII.Hartogs.bipolar_channel_independence
(bound : Denotation.TauIdx)
 :Bool**


[II.P08] Bipolar channel independence under BndLift.

The B-component and C-component of the lifted value are independent:
varying B (exponent) while fixing C (tetration) produces independent
effects on the lifted value, and vice versa.

Evidence: for pairs of τ-admissible points that differ ONLY in B
(or only in C), the lifted ABCD charts show independent variation
in the corresponding sector.

We test this by examining how the ABCD decomposition of the lifted
value responds to B-only and C-only changes in the input.
Equations
- Tau.BookII.Hartogs.bipolar_channel_independence bound = Tau.BookII.Hartogs.bipolar_channel_independence.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.bipolar_channel_independence.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L236-L249)@[irreducible]

**def
Tau.BookII.Hartogs.bipolar_channel_independence.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.channel_decoupling_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L252-L285)
**def
Tau.BookII.Hartogs.channel_decoupling_check
(stage bound : Denotation.TauIdx)
 :Bool**


Stronger channel independence: under the BndLift, the B and C
coordinates of the ABCD chart evolve independently.
For x and x + P_n (same stage-n, different stage-(n+1)):
the B-change and C-change are decoupled.

Evidence: at representative indices, the B-sector and C-sector
projections of the bipolar decomposition remain orthogonal after lift.
Equations
- Tau.BookII.Hartogs.channel_decoupling_check stage bound = Tau.BookII.Hartogs.channel_decoupling_check.go stage bound 2 (bound + 1) (Tau.Polarity.primorial stage)
Instances For

---

### `Tau.BookII.Hartogs.channel_decoupling_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L263-L284)@[irreducible]

**def
Tau.BookII.Hartogs.channel_decoupling_check.go
(stage bound : Denotation.TauIdx)

(x fuel pn : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.lift_sector_preservation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L287-L305)
**def
Tau.BookII.Hartogs.lift_sector_preservation
(stage bound : Denotation.TauIdx)
 :Bool**


The lift preserves the sector structure: for any x, the bipolar
decomposition of the lifted value decomposes into independent
B-sector and C-sector contributions that sum to the full value.
Equations
- Tau.BookII.Hartogs.lift_sector_preservation stage bound = Tau.BookII.Hartogs.lift_sector_preservation.go stage bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.lift_sector_preservation.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L293-L304)@[irreducible]

**def
Tau.BookII.Hartogs.lift_sector_preservation.go
(stage bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.extension_determinacy_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L311-L327)
**def
Tau.BookII.Hartogs.extension_determinacy_check
(stage : Denotation.TauIdx)
 :Bool**


The BndLift extension is determined by the CRT structure.
For all x in [0, P_{n+1}), the lifted value equals x itself
(since reduce(x, n+1) = x for x < P_{n+1}).
This shows the lift is surjective onto the stage-(n+1) residues.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.extension_determinacy_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L320-L326)@[irreducible]

**def
Tau.BookII.Hartogs.extension_determinacy_check.go
(stage : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.splitting_count_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L329-L352)
**def
Tau.BookII.Hartogs.splitting_count_check
(stage : Denotation.TauIdx)
 :Bool**


Each residue class at stage n splits into exactly p_{n+1}
residue classes at stage n+1.
Evidence: for a fixed r < P_n, count elements in [0, P_{n+1})
with reduce(x, n) = r. Should equal p_{n+1}.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.splitting_count_check.go_r`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L339-L346)@[irreducible]

**def
Tau.BookII.Hartogs.splitting_count_check.go_r
(stage : Denotation.TauIdx)

(r fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.splitting_count_check.count_x`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L348-L351)@[irreducible]

**def
Tau.BookII.Hartogs.splitting_count_check.count_x
(stage : Denotation.TauIdx)

(x fuel acc r : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_bndlift_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L358-L380)
**def
Tau.BookII.Hartogs.full_bndlift_check :Bool**


[II.D36 + II.T26 + II.P08] Complete BndLift verification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.crt_unique_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L447-L447)
**theorem
Tau.BookII.Hartogs.crt_unique_1 :crt_unique_check 1 = true**


---

### `Tau.BookII.Hartogs.crt_unique_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L448-L448)
**theorem
Tau.BookII.Hartogs.crt_unique_2 :crt_unique_check 2 = true**


---

### `Tau.BookII.Hartogs.crt_cover_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L449-L449)
**theorem
Tau.BookII.Hartogs.crt_cover_1 :crt_coverage_check 1 = true**


---

### `Tau.BookII.Hartogs.crt_cover_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L450-L450)
**theorem
Tau.BookII.Hartogs.crt_cover_2 :crt_coverage_check 2 = true**


---

### `Tau.BookII.Hartogs.bndlift_exist_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L453-L453)
**theorem
Tau.BookII.Hartogs.bndlift_exist_3_30 :bndlift_existence_check 3 30 = true**


---

### `Tau.BookII.Hartogs.tower_multi_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L454-L454)
**theorem
Tau.BookII.Hartogs.tower_multi_3_30 :tower_coherence_multi 3 30 = true**


---

### `Tau.BookII.Hartogs.info_gain_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L455-L455)
**theorem
Tau.BookII.Hartogs.info_gain_4 :lift_information_gain 4 = true**


---

### `Tau.BookII.Hartogs.crt_indep_1_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L458-L458)
**theorem
Tau.BookII.Hartogs.crt_indep_1_20 :crt_independence_check 1 20 = true**


---

### `Tau.BookII.Hartogs.crt_indep_2_40`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L459-L459)
**theorem
Tau.BookII.Hartogs.crt_indep_2_40 :crt_independence_check 2 40 = true**


---

### `Tau.BookII.Hartogs.bipolar_indep_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L462-L462)
**theorem
Tau.BookII.Hartogs.bipolar_indep_30 :bipolar_channel_independence 30 = true**


---

### `Tau.BookII.Hartogs.decoupling_1_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L463-L463)
**theorem
Tau.BookII.Hartogs.decoupling_1_20 :channel_decoupling_check 1 20 = true**


---

### `Tau.BookII.Hartogs.sector_pres_2_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L464-L464)
**theorem
Tau.BookII.Hartogs.sector_pres_2_30 :lift_sector_preservation 2 30 = true**


---

### `Tau.BookII.Hartogs.ext_det_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L467-L467)
**theorem
Tau.BookII.Hartogs.ext_det_1 :extension_determinacy_check 1 = true**


---

### `Tau.BookII.Hartogs.ext_det_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L468-L468)
**theorem
Tau.BookII.Hartogs.ext_det_2 :extension_determinacy_check 2 = true**


---

### `Tau.BookII.Hartogs.split_count_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L469-L469)
**theorem
Tau.BookII.Hartogs.split_count_1 :splitting_count_check 1 = true**


---

### `Tau.BookII.Hartogs.split_count_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L470-L470)
**theorem
Tau.BookII.Hartogs.split_count_2 :splitting_count_check 2 = true**


---

### `Tau.BookII.Hartogs.full_bndlift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/BndLift.lean#L473-L473)
**theorem
Tau.BookII.Hartogs.full_bndlift :full_bndlift_check = true**
