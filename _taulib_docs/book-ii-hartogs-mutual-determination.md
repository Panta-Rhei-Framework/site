---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.MutualDetermination"
permalink: /verify/taulib/docs/book-ii-hartogs-mutual-determination/
lane: verify
module_name: "TauLib.BookII.Hartogs.MutualDetermination"
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

# TauLib.BookII.Hartogs.MutualDetermination


The five equivalent descriptions of holomorphic data and the Mutual
Determination theorem.

## Registry Cross-References


- [II.L02] Refinement-Spectral Equivalence -- `refine_spectral_check`

- [II.L03] Spectral-Germ Equivalence -- `spectral_germ_check`

- [II.L04] Germ-Character Equivalence -- `germ_character_check`

- [II.L05] Character-Hartogs Equivalence -- `character_hartogs_check`

- [II.T27] Mutual Determination Theorem -- `mutual_determination_check`


## Mathematical Content


There are five equivalent descriptions of holomorphic data at a point x:

**(R) Refinement tail**: a tower-coherent sequence (f_k) with
reduce(f_{k+1}, k) = f_k. The primorial ladder projections interleave.

**(S) Spectral tail**: decomposition into boundary characters chi_plus and
chi_minus with finite spectral support at each stage. The B and C
coordinates of from_tau_idx determine the spectral components.

**(G) Omega-germ**: equivalence class at the profinite limit. Two points
that agree on all sufficiently deep stages are equivalent.

**(C) Boundary character**: ring homomorphism R_tau -> H_tau. The B and C
components of from_tau_idx determine the character data.

**(H) Hartogs continuation**: extension from boundary to interior via
BndLift. Tower coherence ensures reduce(bndlift(x, k+1), k) = reduce(x, k).

The Mutual Determination Theorem (II.T27): all five descriptions carry the
same information. The bipolar idempotent decomposition e_plus, e_minus
makes all five equivalent because the B-channel and C-channel separate
completely (orthogonality e_plus * e_minus = 0), and they recombine
completely (completeness e_plus + e_minus = 1).

---

### `Tau.BookII.Hartogs.refinement_tail_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L55-L70)
**def
Tau.BookII.Hartogs.refinement_tail_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L02, clause R] Tower coherence for reduction maps:
reduce(x, k) = reduce(reduce(x, k+1), k) for all k <= db.
This is the fundamental compatibility of the primorial inverse system:
projecting from a finer stage to a coarser stage is consistent
with direct projection.
Equations
- Tau.BookII.Hartogs.refinement_tail_check bound db = Tau.BookII.Hartogs.refinement_tail_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.refinement_tail_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L63-L69)@[irreducible]

**def
Tau.BookII.Hartogs.refinement_tail_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.spectral_tail_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L76-L109)
**def
Tau.BookII.Hartogs.spectral_tail_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L02-L03, clause S] Spectral stabilization check:
the B and C coordinates from from_tau_idx determine the spectral
decomposition. At each stage k, the spectral content is determined
by reduce(x, k), and once k is large enough, the B and C
coordinates of from_tau_idx(reduce(x, k)) stabilize.

We verify that the B-coordinate and C-coordinate of from_tau_idx
applied to the stage-k reduction are well-defined and consistent:
if reduce(x, k) = reduce(y, k), then the ABCD charts agree on
the B and C coordinates at that resolution.
Equations
- Tau.BookII.Hartogs.spectral_tail_check bound db = Tau.BookII.Hartogs.spectral_tail_check.go bound db 2 2 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.spectral_tail_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L89-L108)@[irreducible]

**def
Tau.BookII.Hartogs.spectral_tail_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.exists_separator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L115-L124)
**def
Tau.BookII.Hartogs.exists_separator
(x y db : ℕ)
 :Bool**


Helper: check if there exists a stage k <= db where x and y disagree.
Equations
- Tau.BookII.Hartogs.exists_separator x y db = Tau.BookII.Hartogs.exists_separator.go db x y 1 (db + 1)
Instances For

---

### `Tau.BookII.Hartogs.exists_separator.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L119-L123)@[irreducible]

**def
Tau.BookII.Hartogs.exists_separator.go
(db x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.omega_germ_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L126-L144)
**def
Tau.BookII.Hartogs.omega_germ_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L03, clause G] Omega-germ equivalence:
two points that agree on all stages k <= db are equal
(within the finite range [2, bound]).

This is the finite-range shadow of the profinite separation property:
if reduce(x, k) = reduce(y, k) for all k, then x = y in Z-hat_tau.
Equations
- Tau.BookII.Hartogs.omega_germ_check bound db = Tau.BookII.Hartogs.omega_germ_check.go bound db 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.omega_germ_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L135-L143)@[irreducible]

**def
Tau.BookII.Hartogs.omega_germ_check.go
(bound db : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.boundary_character_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L150-L174)
**def
Tau.BookII.Hartogs.boundary_character_check
(bound _db : Denotation.TauIdx)
 :Bool**


[II.L04, clause C] Boundary character determined by B/C data:
the B and C components of from_tau_idx encode the bipolar character
assignment. The character is determined by the idempotent decomposition:
e_plus projects onto the B-sector, e_minus onto the C-sector.

We verify: the sector pair (B, C) is consistent with the idempotent
decomposition — applying e_plus projects to (B, 0) and e_minus to (0, C),
and their sum recovers (B, C).
Equations
- Tau.BookII.Hartogs.boundary_character_check bound _db = Tau.BookII.Hartogs.boundary_character_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.boundary_character_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L161-L173)@[irreducible]

**def
Tau.BookII.Hartogs.boundary_character_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.hartogs_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L180-L199)
**def
Tau.BookII.Hartogs.hartogs_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L05, clause H] Hartogs continuation check:
BndLift produces extensions that are tower-coherent.
reduce(bndlift(x, k+1), k) = reduce(x, k) for all x, k.

This is the "Hartogs direction": boundary data determines interior
extension, and the extension is compatible with the tower structure.
Equations
- Tau.BookII.Hartogs.hartogs_check bound db = Tau.BookII.Hartogs.hartogs_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.hartogs_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L189-L198)@[irreducible]

**def
Tau.BookII.Hartogs.hartogs_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.refine_spectral_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L205-L211)
**def
Tau.BookII.Hartogs.refine_spectral_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L02] Refinement <-> Spectral:
Refinement coherence implies spectral stability and vice versa.
The tower coherence condition reduce(f_{k+1}, k) = f_k ensures
that the spectral (B, C) components at stage k are determined by
those at stage k+1.
Equations
- Tau.BookII.Hartogs.refine_spectral_check bound db = (Tau.BookII.Hartogs.refinement_tail_check bound db && Tau.BookII.Hartogs.spectral_tail_check bound db)
Instances For

---

### `Tau.BookII.Hartogs.spectral_germ_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L213-L218)
**def
Tau.BookII.Hartogs.spectral_germ_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L03] Spectral <-> Omega-germ:
Spectral stability implies germ equivalence. If the spectral
decomposition at each stage is determined by the reduction map,
then the profinite limit (omega-germ) is determined.
Equations
- Tau.BookII.Hartogs.spectral_germ_check bound db = (Tau.BookII.Hartogs.spectral_tail_check bound db && Tau.BookII.Hartogs.omega_germ_check bound db)
Instances For

---

### `Tau.BookII.Hartogs.germ_character_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L220-L225)
**def
Tau.BookII.Hartogs.germ_character_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L04] Omega-germ <-> Character:
Germ data determines character data. The omega-germ carries
the full profinite element, and the boundary character is
extracted via the bipolar idempotent decomposition.
Equations
- Tau.BookII.Hartogs.germ_character_check bound db = (Tau.BookII.Hartogs.omega_germ_check bound db && Tau.BookII.Hartogs.boundary_character_check bound db)
Instances For

---

### `Tau.BookII.Hartogs.character_hartogs_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L227-L231)
**def
Tau.BookII.Hartogs.character_hartogs_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L05] Character <-> Hartogs:
Character data determines Hartogs extension. The bipolar character
assignment determines BndLift, and BndLift is tower-coherent.
Equations
- Tau.BookII.Hartogs.character_hartogs_check bound db = (Tau.BookII.Hartogs.boundary_character_check bound db && Tau.BookII.Hartogs.hartogs_check bound db)
Instances For

---

### `Tau.BookII.Hartogs.mutual_determination_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L237-L257)
**def
Tau.BookII.Hartogs.mutual_determination_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T27] The Mutual Determination Theorem:
All five descriptions of holomorphic data at a point agree.

(R) Refinement tail <-> (S) Spectral tail <-> (G) Omega-germ
<-> (C) Boundary character <-> (H) Hartogs continuation

The equivalence chain is:


- L02: (R) <-> (S) [refinement coherence = spectral stability]

- L03: (S) <-> (G) [spectral stability = germ equivalence]

- L04: (G) <-> (C) [germ data = character data]

- L05: (C) <-> (H) [character data = Hartogs extension]


The mechanism: the bipolar idempotent decomposition e_plus, e_minus
ensures that the B-channel and C-channel carry independent, complete
information (orthogonality + partition of unity).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.idempotent_mechanism_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L263-L271)
**def
Tau.BookII.Hartogs.idempotent_mechanism_check :Bool**


The mechanism behind mutual determination: bipolar idempotents
provide orthogonal, complete decomposition.
e_plus^2 = e_plus, e_minus^2 = e_minus, e_plus * e_minus = 0,
e_plus + e_minus = (1, 1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_mutual_determination_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L273-L276)
**def
Tau.BookII.Hartogs.full_mutual_determination_check
(bound db : Denotation.TauIdx)
 :Bool**


Full mutual determination with mechanism: the five descriptions
agree AND the mechanism (bipolar idempotents) is sound.
Equations
- Tau.BookII.Hartogs.full_mutual_determination_check bound db = (Tau.BookII.Hartogs.mutual_determination_check bound db && Tau.BookII.Hartogs.idempotent_mechanism_check)
Instances For

---

### `Tau.BookII.Hartogs.bndlift_coherent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L282-L288)
**theorem
Tau.BookII.Hartogs.bndlift_coherent
(x : Denotation.TauIdx)

{j k : Denotation.TauIdx}

(hjk : j ≤ k)
 :Polarity.reduce (bndlift x k) j = Polarity.reduce x j**


BndLift tower coherence: reduce(bndlift(x, k), j) = reduce(x, j)
for j <= k. This follows from reduction compatibility.

---

### `Tau.BookII.Hartogs.bndlift_at_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L290-L293)
**theorem
Tau.BookII.Hartogs.bndlift_at_stage
(x k : Denotation.TauIdx)
 :Polarity.reduce (bndlift x k) k = Polarity.reduce x k**


BndLift at the same stage: reduce(bndlift(x, k), k) = reduce(x, k).

---

### `Tau.BookII.Hartogs.bndlift_exists_4_12`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L343-L344)
**theorem
Tau.BookII.Hartogs.bndlift_exists_4_12 :bndlift_existence_check 4 12 = true**


---

### `Tau.BookII.Hartogs.refine_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L347-L348)
**theorem
Tau.BookII.Hartogs.refine_12_4 :refinement_tail_check 12 4 = true**


---

### `Tau.BookII.Hartogs.spectral_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L351-L352)
**theorem
Tau.BookII.Hartogs.spectral_8_3 :spectral_tail_check 8 3 = true**


---

### `Tau.BookII.Hartogs.germ_10_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L355-L356)
**theorem
Tau.BookII.Hartogs.germ_10_4 :omega_germ_check 10 4 = true**


---

### `Tau.BookII.Hartogs.character_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L359-L360)
**theorem
Tau.BookII.Hartogs.character_12_4 :boundary_character_check 12 4 = true**


---

### `Tau.BookII.Hartogs.hartogs_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L363-L364)
**theorem
Tau.BookII.Hartogs.hartogs_12_4 :hartogs_check 12 4 = true**


---

### `Tau.BookII.Hartogs.l02_refine_spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L367-L368)
**theorem
Tau.BookII.Hartogs.l02_refine_spectral :refine_spectral_check 10 4 = true**


---

### `Tau.BookII.Hartogs.l03_spectral_germ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L370-L371)
**theorem
Tau.BookII.Hartogs.l03_spectral_germ :spectral_germ_check 8 3 = true**


---

### `Tau.BookII.Hartogs.l04_germ_character`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L373-L374)
**theorem
Tau.BookII.Hartogs.l04_germ_character :germ_character_check 10 4 = true**


---

### `Tau.BookII.Hartogs.l05_character_hartogs`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L376-L377)
**theorem
Tau.BookII.Hartogs.l05_character_hartogs :character_hartogs_check 10 4 = true**


---

### `Tau.BookII.Hartogs.mutual_determination`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L380-L381)
**theorem
Tau.BookII.Hartogs.mutual_determination :mutual_determination_check 10 4 = true**


---

### `Tau.BookII.Hartogs.idem_mechanism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L384-L385)
**theorem
Tau.BookII.Hartogs.idem_mechanism :idempotent_mechanism_check = true**


---

### `Tau.BookII.Hartogs.full_mutual_determination`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/MutualDetermination.lean#L388-L389)
**theorem
Tau.BookII.Hartogs.full_mutual_determination :full_mutual_determination_check 10 4 = true**
