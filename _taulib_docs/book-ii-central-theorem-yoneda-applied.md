---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.YonedaApplied"
permalink: /verify/taulib/docs/book-ii-central-theorem-yoneda-applied/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.YonedaApplied"
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

# TauLib.BookII.CentralTheorem.YonedaApplied


Yoneda embedding applied to tau^3: omega-germ transformers are
holomorphic functions, via the pre-Yoneda embedding and Code/Decode.

## Registry Cross-References


- [II.L14] Yoneda Application -- `yoneda_application_check`, `yoneda_hom_identification_check`

- [II.T39] Omega-Germs iff Holomorphic Functions -- `omega_germs_holomorphic_check`,
`holomorphic_classification_check`, `full_yoneda_applied_check`


## Mathematical Content


**II.L14 (Yoneda Application):** The Yoneda embedding applied to tau^3
identifies elements of the internal Hom [tau^3, H_tau] with natural
transformations y(tau^3) -> y(H_tau), and then with omega-germ transformers
via probe naturality.

Concretely: the pre-Yoneda embedding preyoneda_embed(f, x, k) = f(reduce(x, k))
applied to a tower-coherent function gives a tower-coherent result, and
Code extracts the original function value.

**II.T39 (Omega-Germs iff Holomorphic Functions):** Canonical bijection
between omega-germ transformers on tau^3 and tau-holomorphic functions
tau^3 -> H_tau. The proof uses bipolar idempotents, tower coherence,
Code/Decode, and the characterization theorem (II.T33: holomorphic iff
idempotent-supported).

Every tower-coherent function (= holomorphic) determines a unique omega-germ
transformer, and conversely.

---

### `Tau.BookII.CentralTheorem.yoneda_application_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L46-L76)
**def
Tau.BookII.CentralTheorem.yoneda_application_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L14] Yoneda application check: verify that the pre-Yoneda
embedding applied to a tower-coherent function gives a tower-coherent
result, and that Code extracts the original.

For f = identity (tower-coherent by construction):

- preyoneda_embed(f, x, k) = f(reduce(x, k)) = reduce(x, k)

- code_extract(preyoneda(f), k, x) = preyoneda(f)(reduce(x, k))
= f(reduce(reduce(x, k), k)) = f(reduce(x, k))
= preyoneda(f)(x, k)


So Code applied to the pre-Yoneda image recovers the pre-Yoneda image itself.
This is the Yoneda lemma in action: representable presheaves are fully faithful.
Equations
- Tau.BookII.CentralTheorem.yoneda_application_check bound db = Tau.BookII.CentralTheorem.yoneda_application_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.yoneda_application_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L61-L75)@[irreducible]

**def
Tau.BookII.CentralTheorem.yoneda_application_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.yoneda_hom_identification_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L78-L115)
**def
Tau.BookII.CentralTheorem.yoneda_hom_identification_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L14] Yoneda hom identification check: for test functions f,
verify that the Hom-object representation (via hom_stage from pre-Yoneda)
is consistent with the Code/Decode representation.

For f = chi_plus_stage (B-sector projection):


- preyoneda gives f(reduce(x, k)) = reduce(x, k) in B, 0 in C

- Code/Decode round-trip on the B-channel recovers the same value


For f = chi_minus_stage:


- preyoneda gives 0 in B, reduce(x, k) in C

- Code/Decode round-trip on the C-channel recovers the same value

Equations
- Tau.BookII.CentralTheorem.yoneda_hom_identification_check bound db = Tau.BookII.CentralTheorem.yoneda_hom_identification_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.yoneda_hom_identification_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L92-L114)@[irreducible]

**def
Tau.BookII.CentralTheorem.yoneda_hom_identification_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.omega_germs_holomorphic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L121-L162)
**def
Tau.BookII.CentralTheorem.omega_germs_holomorphic_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T39] Omega-germs determine holomorphic functions (forward direction).

Every tower-coherent function (= holomorphic) determines a unique
omega-germ transformer. Concretely: for a tower-coherent StageFun f,
the pre-Yoneda image is tower-coherent, and the Code extraction at
each stage is well-defined.

Test: for id_stage (tower-coherent by id_coherent),


- The B/C-sector readings at stage k are reduced values

- These readings are tower-coherent: reduce(reading at k+1, k) = reading at k

- Code extraction at stage k matches the reading

Equations
- Tau.BookII.CentralTheorem.omega_germs_holomorphic_check bound db = Tau.BookII.CentralTheorem.omega_germs_holomorphic_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.omega_germs_holomorphic_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L135-L161)@[irreducible]

**def
Tau.BookII.CentralTheorem.omega_germs_holomorphic_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.holomorphic_classification_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L164-L198)
**def
Tau.BookII.CentralTheorem.holomorphic_classification_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T39] Holomorphic classification check: verify the complete chain
tower coherence ==> idempotent support ==> bipolar decomposition
==> unique omega-germ.

For each test point x at stage k:

- Tower coherence of id_stage gives reduce-compatibility

- Idempotent support: interior_bipolar decomposes into e_plus and e_minus

- Bipolar decomposition: independent B and C channels

- Unique omega-germ: Code extraction is deterministic

Equations
- Tau.BookII.CentralTheorem.holomorphic_classification_check bound db = Tau.BookII.CentralTheorem.holomorphic_classification_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.holomorphic_classification_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L176-L197)@[irreducible]

**def
Tau.BookII.CentralTheorem.holomorphic_classification_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.germ_to_holomorphic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L200-L228)
**def
Tau.BookII.CentralTheorem.germ_to_holomorphic_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T39] Reverse direction: every omega-germ transformer determines
a holomorphic function.

Given the omega-germ data (the tower of reduce values), we reconstruct
the tower-coherent function via Decode, and verify it is tower-coherent.

For input table(a) = a (identity table):


- decode_reconstruct(table, k, x) = table(reduce(x, k)) = reduce(x, k)

- This IS the identity StageFun, which is tower-coherent.

- So the omega-germ (encoded as a code table) reconstructs to a holomorphic function.

Equations
- Tau.BookII.CentralTheorem.germ_to_holomorphic_check bound db = Tau.BookII.CentralTheorem.germ_to_holomorphic_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.germ_to_holomorphic_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L213-L227)@[irreducible]

**def
Tau.BookII.CentralTheorem.germ_to_holomorphic_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.full_yoneda_applied_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L234-L244)
**def
Tau.BookII.CentralTheorem.full_yoneda_applied_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L14 + II.T39] Full Yoneda-applied verification:


- Yoneda application (pre-Yoneda + Code round-trip)

- Hom identification (chi_plus, chi_minus consistency)

- Omega-germ <-> holomorphic bijection (both directions)

- Holomorphic classification chain

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.yoneda_app_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L278-L279)
**theorem
Tau.BookII.CentralTheorem.yoneda_app_12_3 :yoneda_application_check 12 3 = true**


---

### `Tau.BookII.CentralTheorem.yoneda_hom_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L282-L283)
**theorem
Tau.BookII.CentralTheorem.yoneda_hom_12_3 :yoneda_hom_identification_check 12 3 = true**


---

### `Tau.BookII.CentralTheorem.omega_germs_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L286-L287)
**theorem
Tau.BookII.CentralTheorem.omega_germs_12_3 :omega_germs_holomorphic_check 12 3 = true**


---

### `Tau.BookII.CentralTheorem.hol_class_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L290-L291)
**theorem
Tau.BookII.CentralTheorem.hol_class_12_3 :holomorphic_classification_check 12 3 = true**


---

### `Tau.BookII.CentralTheorem.germ_hol_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L294-L295)
**theorem
Tau.BookII.CentralTheorem.germ_hol_12_3 :germ_to_holomorphic_check 12 3 = true**


---

### `Tau.BookII.CentralTheorem.full_yoneda_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L298-L299)
**theorem
Tau.BookII.CentralTheorem.full_yoneda_10_3 :full_yoneda_applied_check 10 3 = true**


---

### `Tau.BookII.CentralTheorem.yoneda_code_roundtrip`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L305-L313)
**theorem
Tau.BookII.CentralTheorem.yoneda_code_roundtrip
(x k : Denotation.TauIdx)
 :Regularity.code_extract
 (fun (n : Denotation.TauIdx) => ↑(Regularity.preyoneda_embed_nat (fun (m : Denotation.TauIdx) => m) n k)) k x = ↑(Regularity.preyoneda_embed_nat (fun (m : Denotation.TauIdx) => m) x k)**


[II.L14] Pre-Yoneda embedding of the identity is recovered by Code.
code_extract(preyoneda(id), k, x) = preyoneda(id)(x, k)
Both sides equal reduce(x, k).

---

### `Tau.BookII.CentralTheorem.omega_germ_tower_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L315-L322)
**theorem
Tau.BookII.CentralTheorem.omega_germ_tower_coherent
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (Regularity.preyoneda_embed_nat (fun (n : Denotation.TauIdx) => n) x l) k = Regularity.preyoneda_embed_nat (fun (n : Denotation.TauIdx) => n) x k**


[II.T39] Tower coherence of the pre-Yoneda identity embedding:
reduce(preyoneda(id, x, l), k) = preyoneda(id, x, k) for k <= l.
This is reduction_compat in disguise.

---

### `Tau.BookII.CentralTheorem.germ_reconstructs_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L324-L329)
**theorem
Tau.BookII.CentralTheorem.germ_reconstructs_identity
(x k : Denotation.TauIdx)
 :Regularity.decode_reconstruct (fun (a : Denotation.TauIdx) => ↑a) k x = ↑(Polarity.reduce x k)**


[II.T39] Decode of the identity code table reconstructs reduce:
decode_reconstruct(id_table, k, x) = reduce(x, k).
This is the germ-to-holomorphic direction.

---

### `Tau.BookII.CentralTheorem.germ_idempotent_supported`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L331-L339)
**theorem
Tau.BookII.CentralTheorem.germ_idempotent_supported
(p : Interior.TauAdmissiblePoint)
 :(Polarity.e_plus_sector.mul (Interior.interior_bipolar p)).add
 (Polarity.e_minus_sector.mul (Interior.interior_bipolar p)) = Interior.interior_bipolar p**


[II.T39] The identity omega-germ is idempotent-supported:
e_plus * interior_bipolar(p) + e_minus * interior_bipolar(p) = interior_bipolar(p).
This is the decompose_recovery theorem applied pointwise.
