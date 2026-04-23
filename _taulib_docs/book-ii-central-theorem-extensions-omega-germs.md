---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms"
permalink: /verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms"
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

# TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms


Stagewise naturality of Hartogs extensions and the theorem that
extensions are omega-germ transformers.

## Registry Cross-References


- [II.L13] Stagewise Naturality -- `stagewise_naturality_check`

- [II.T38] Extensions Are Omega-Germ Transformers -- `omega_germ_transformer_check`, `extension_germ_roundtrip_check`


## Mathematical Content


**II.L13 (Stagewise Naturality):** The Hartogs extension respects CRT
reduction maps at every stage:

reduce(ext(x, k+1), k) = ext(x, k)

Since the extension is BndLift (bndlift(x, k) = reduce(x, k+1)),
this becomes:

reduce(bndlift(x, k+1), k) = bndlift(x, k)
i.e. reduce(reduce(x, k+2), k) = reduce(x, k+1)

This follows from reduction_compat: since k <= k+2, we have
reduce(reduce(x, k+2), k) = reduce(x, k). But we need the stronger
statement with k+1 on the right. Since bndlift(x,k) = reduce(x,k+1),
we equivalently check: reduce(reduce(x,k+2), k+1) = reduce(x,k+1),
which is reduction_compat with k+1 <= k+2.

This is the key link: extensions are NATURAL TRANSFORMATIONS on the
primorial inverse system.

**II.T38 (Extensions Are Omega-Germ Transformers):** Every Hartogs
extension determines a unique omega-germ transformer. The extension at
stage k defines a map on Z/P_kZ, and the tower coherence makes these
maps into a coherent system = omega-germ transformer.

The extension-germ roundtrip: extracting the omega-germ from an extension
(via Code) and reconstructing the extension from the germ (via Decode)
give the same result. This uses the Code/Decode bijection (II.T35).

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L56-L92)
**def
Tau.BookII.CentralTheorem.stagewise_naturality_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L13] Stagewise naturality check: verify that the bndlift
extension is stage-compatible:

reduce(bndlift(x, k+1), k) = bndlift(x, k)

Equivalently: reduce(reduce(x, k+2), k+1) = reduce(x, k+1).

This is exactly reduction_compat with k+1 <= k+2.
This is the naturality condition making the extension a natural
transformation on the primorial inverse system.
Equations
- Tau.BookII.CentralTheorem.stagewise_naturality_check bound db = Tau.BookII.CentralTheorem.stagewise_naturality_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L69-L91)@[irreducible]

**def
Tau.BookII.CentralTheorem.stagewise_naturality_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_strong_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L94-L113)
**def
Tau.BookII.CentralTheorem.stagewise_naturality_strong_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L13] Stronger naturality: bndlift at successive stages
is coherent: reduce(bndlift(x, k+1), k+1) = bndlift(x, k).
This is: reduce(reduce(x, k+2), k+1) = reduce(x, k+1),
which follows from reduction_compat since k+1 <= k+2.
Equations
- Tau.BookII.CentralTheorem.stagewise_naturality_strong_check bound db = Tau.BookII.CentralTheorem.stagewise_naturality_strong_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_strong_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L101-L112)@[irreducible]

**def
Tau.BookII.CentralTheorem.stagewise_naturality_strong_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_multi_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L115-L131)
**def
Tau.BookII.CentralTheorem.stagewise_naturality_multi_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L13] Multi-step naturality: reducing a bndlift extension
across multiple stages is consistent.
reduce(bndlift(x, k+m), k) = reduce(x, k) for any m >= 0.
Equations
- Tau.BookII.CentralTheorem.stagewise_naturality_multi_check bound db = Tau.BookII.CentralTheorem.stagewise_naturality_multi_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_multi_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L121-L130)@[irreducible]

**def
Tau.BookII.CentralTheorem.stagewise_naturality_multi_check.go
(bound db : Denotation.TauIdx)

(x k m fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.omega_germ_transformer_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L137-L160)
**def
Tau.BookII.CentralTheorem.omega_germ_transformer_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T38] An omega-germ transformer from the bndlift extension:
at each stage k, the extension defines a map
f_k : Z/P_kZ -> Z/P_{k+1}Z given by f_k(x) = bndlift(x, k).

Tower coherence of this family: reduce(f_{k+1}(x), k+1) = f_k(x).
This is: reduce(bndlift(x, k+1), k+1) = bndlift(x, k)
= reduce(x, k+1), which is reduction_compat (k+1 <= k+2).
Equations
- Tau.BookII.CentralTheorem.omega_germ_transformer_check bound db = Tau.BookII.CentralTheorem.omega_germ_transformer_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.omega_germ_transformer_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L147-L159)@[irreducible]

**def
Tau.BookII.CentralTheorem.omega_germ_transformer_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.bndlift_stagefun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L162-L169)
**def
Tau.BookII.CentralTheorem.bndlift_stagefun :Holomorphy.StageFun**


[II.T38] The bndlift family gives a StageFun (omega-germ transformer):
B-sector: (x, k) -> B-coord of from_tau_idx(bndlift(x, k))
C-sector: (x, k) -> C-coord of from_tau_idx(bndlift(x, k))

This StageFun is tower-coherent by stagewise naturality.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.bndlift_stagefun_coherent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L171-L194)
**def
Tau.BookII.CentralTheorem.bndlift_stagefun_coherent_check
(bound db : Denotation.TauIdx)
 :Bool**


Tower coherence check for the bndlift StageFun:
reduce(bndlift(x, l), k) = reduce(x, k) means the ABCD chart
at stage k is determined by reduce(x, k), regardless of l >= k.
So the B and C coordinates of from_tau_idx(reduce(bndlift(x,l), k))
match those of from_tau_idx(reduce(x, k)).
Equations
- Tau.BookII.CentralTheorem.bndlift_stagefun_coherent_check bound db = Tau.BookII.CentralTheorem.bndlift_stagefun_coherent_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.bndlift_stagefun_coherent_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L179-L193)@[irreducible]

**def
Tau.BookII.CentralTheorem.bndlift_stagefun_coherent_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.extension_germ_roundtrip_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L200-L237)
**def
Tau.BookII.CentralTheorem.extension_germ_roundtrip_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T38] Extension-germ roundtrip: extracting the omega-germ from
an extension and reconstructing the extension from the germ give
the same result.

Step 1 (Code direction): Given bndlift extension, extract the
Code at stage k: code_extract(bndlift_fn, k, x) = bndlift(reduce(x, k), k-1)
for the bndlift "function" viewed as a map on stage-k inputs.

Step 2 (Decode direction): Reconstruct from the coded values:
decode_reconstruct(coded_table, k, x) should give back the
original bndlift value.

The roundtrip works because Code/Decode is a bijection (II.T35)
and bndlift is well-defined on residue classes (depends only on
reduce(x, k)).
Equations
- Tau.BookII.CentralTheorem.extension_germ_roundtrip_check bound db = Tau.BookII.CentralTheorem.extension_germ_roundtrip_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.extension_germ_roundtrip_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L218-L236)@[irreducible]

**def
Tau.BookII.CentralTheorem.extension_germ_roundtrip_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.extension_sector_roundtrip_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L239-L260)
**def
Tau.BookII.CentralTheorem.extension_sector_roundtrip_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T38] Full roundtrip including the SectorPair decomposition:
the bndlift extension, coded as a StageFun, can be recovered from
its Code/Decode representation.
Equations
- Tau.BookII.CentralTheorem.extension_sector_roundtrip_check bound db = Tau.BookII.CentralTheorem.extension_sector_roundtrip_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.extension_sector_roundtrip_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L245-L259)@[irreducible]

**def
Tau.BookII.CentralTheorem.extension_sector_roundtrip_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.full_extensions_omega_germs_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L266-L281)
**def
Tau.BookII.CentralTheorem.full_extensions_omega_germs_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L13 + II.T38] Complete verification:


- Stagewise naturality (II.L13)

- Strong naturality (II.L13)

- Multi-step naturality (II.L13)

- Omega-germ transformer (II.T38)

- BndLift StageFun coherence (II.T38)

- Extension-germ roundtrip (II.T38)

- Extension sector roundtrip (II.T38)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.stagewise_naturality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L287-L294)
**theorem
Tau.BookII.CentralTheorem.stagewise_naturality
(x k : Denotation.TauIdx)
 :Polarity.reduce (Hartogs.bndlift x (k + 1)) k = Polarity.reduce x k**


[II.L13] Stagewise naturality (structural): reduce(bndlift(x, k+1), k) = reduce(x, k).
Since bndlift(x, k+1) = reduce(x, k+2) and k <= k+2, this follows
from reduction_compat.

---

### `Tau.BookII.CentralTheorem.stagewise_naturality_strong`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L296-L302)
**theorem
Tau.BookII.CentralTheorem.stagewise_naturality_strong
(x k : Denotation.TauIdx)
 :Polarity.reduce (Hartogs.bndlift x (k + 1)) (k + 1) = Hartogs.bndlift x k**


[II.L13] Strong naturality (structural): reduce(bndlift(x, k+1), k+1) = bndlift(x, k).
This is: reduce(reduce(x, k+2), k+1) = reduce(x, k+1),
which follows from reduction_compat since k+1 <= k+2.

---

### `Tau.BookII.CentralTheorem.bndlift_reduce_invariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L304-L311)
**theorem
Tau.BookII.CentralTheorem.bndlift_reduce_invariant
(x k : Denotation.TauIdx)
 :Hartogs.bndlift (Polarity.reduce x (k + 1)) k = Hartogs.bndlift x k**


[II.T38] The bndlift extension at stage k depends only on reduce(x, k+1).
bndlift(x, k) = bndlift(reduce(x, k+1), k).
This is: reduce(x, k+1) = reduce(reduce(x, k+1), k+1),
which is reduction idempotence.

---

### `Tau.BookII.CentralTheorem.bndlift_stagefun_welldef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L313-L320)
**theorem
Tau.BookII.CentralTheorem.bndlift_stagefun_welldef
(x k : Denotation.TauIdx)
 :Hartogs.bndlift (Polarity.reduce x (k + 1)) k = Hartogs.bndlift x k**


[II.T38] Tower coherence of bndlift StageFun inputs:
the ABCD chart at stage k is determined by reduce(x, k).
For the bndlift StageFun, from_tau_idx(bndlift(x, k)) =
from_tau_idx(bndlift(reduce(x, k+1), k)) =
from_tau_idx(bndlift(x, k)) by bndlift_reduce_invariant.

---

### `Tau.BookII.CentralTheorem.reduction_gives_naturality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L322-L327)
**theorem
Tau.BookII.CentralTheorem.reduction_gives_naturality
(x : Denotation.TauIdx)

{j k : Denotation.TauIdx}

(h : j ≤ k)
 :Polarity.reduce (Hartogs.bndlift x k) j = Polarity.reduce x j**


[II.L13] Reduction compatibility directly implies stagewise naturality.
This is the structural heart of the module.

---

### `Tau.BookII.CentralTheorem.nat_check_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L365-L366)
**theorem
Tau.BookII.CentralTheorem.nat_check_20_4 :stagewise_naturality_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.nat_strong_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L368-L369)
**theorem
Tau.BookII.CentralTheorem.nat_strong_20_4 :stagewise_naturality_strong_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.nat_multi_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L371-L372)
**theorem
Tau.BookII.CentralTheorem.nat_multi_15_4 :stagewise_naturality_multi_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.ogt_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L375-L376)
**theorem
Tau.BookII.CentralTheorem.ogt_15_4 :omega_germ_transformer_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.bsf_coh_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L379-L380)
**theorem
Tau.BookII.CentralTheorem.bsf_coh_15_4 :bndlift_stagefun_coherent_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.egr_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L383-L384)
**theorem
Tau.BookII.CentralTheorem.egr_15_4 :extension_germ_roundtrip_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.esr_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L386-L387)
**theorem
Tau.BookII.CentralTheorem.esr_15_4 :extension_sector_roundtrip_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.full_eog_12_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L390-L391)
**theorem
Tau.BookII.CentralTheorem.full_eog_12_3 :full_extensions_omega_germs_check 12 3 = true**
