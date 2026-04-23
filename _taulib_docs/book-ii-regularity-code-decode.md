---
layout: taulib-doc
title: "TauLib.BookII.Regularity.CodeDecode"
permalink: /verify/taulib/docs/book-ii-regularity-code-decode/
lane: verify
module_name: "TauLib.BookII.Regularity.CodeDecode"
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

# TauLib.BookII.Regularity.CodeDecode


Code/Decode bijection: CRT spectral analysis and synthesis on the primorial tower.

## Registry Cross-References


- [II.D51] Code — `code_extract`, `code_tower_check`

- [II.D52] Decode — `decode_reconstruct`, `decode_welldef_check`

- [II.T35] Code/Decode Bijection — `code_decode_inverse_check`, `full_code_decode_check`


## Mathematical Content


Code and Decode provide a CRT-based analysis/synthesis pair for functions
on the primorial tower Z/P_kZ.

**CRT Decomposition:**
Z/P_kZ ≅ Z/p_1Z × Z/p_2Z × ... × Z/p_kZ

Every element x ∈ Z/P_kZ is uniquely determined by its CRT coordinates:
(x mod p_1, x mod p_2, ..., x mod p_k)

**Code (II.D51):** Extracts the function value at a point, indexed by
its CRT coordinates. Equivalently, `code_extract(f, k, x) = f(reduce(x, k))`
for `x ∈ Z/P_kZ`. The spectral content is then read off via
`proj_coeff` from the CanonicalBasis: the projection of f onto
the cylinder generator E_{k,pi,v} gives the sum of f over the
residue class v mod p at stage k.

**Decode (II.D52):** Reconstructs the function value at x from the
CRT-indexed code. Given a table of values indexed by Z/P_kZ:
decode_reconstruct(table, k, x) = table(reduce(x, k))

In the primorial tower, the CRT preimage IS just x itself (for x < P_k),
so Decode . Code = id reduces to f(reduce(x, k)) = f(reduce(x, k)).

**Code/Decode Bijection (II.T35):**
The bijection is between:


- Functions f : Z/P_kZ → Z (the "spatial" representation)

- CRT coefficient tables a → f(a) for a ∈ Z/P_kZ


The per-prime spectral projections (proj_coeff) provide a COMPLETE
spectral decomposition: knowing all proj_coeff values determines f.

---

### `Tau.BookII.Regularity.code_extract`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L58-L65)
**def
Tau.BookII.Regularity.code_extract
(f : Denotation.TauIdx → ℤ)

(k x : Denotation.TauIdx)
 :ℤ**


[II.D51] Code: extract the function value at a given input.
code_extract(f, k, x) = f(reduce(x, k))

This is the fundamental "sampling" operation: the code of f at stage k
is the restriction of f to Z/P_kZ. The CRT coordinates of x are
(x mod p_1, ..., x mod p_k), and the code records f at each such point.
Equations
- Tau.BookII.Regularity.code_extract f k x = f (Tau.Polarity.reduce x k)
Instances For

---

### `Tau.BookII.Regularity.code_spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L67-L74)
**def
Tau.BookII.Regularity.code_spectral
(f : Denotation.TauIdx → ℤ)

(k prime_idx v : Denotation.TauIdx)
 :ℤ**


[II.D51] Per-prime spectral coefficient: the projection of f onto
the cylinder generator E_{k,pi,v}. This is proj_coeff from CanonicalBasis:
code_spectral(f, k, pi, v) = sum_{x in Z/P_kZ : x%p == v} f(x)

The spectral coefficients are the Fourier-like components of f
decomposed along individual CRT factors.
Equations
- Tau.BookII.Regularity.code_spectral f k prime_idx v = Tau.BookII.Hartogs.proj_coeff f k prime_idx v
Instances For

---

### `Tau.BookII.Regularity.code_tower_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L76-L92)
**def
Tau.BookII.Regularity.code_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D51] Code tower coherence check:
verify that code at stage k is determined by code at stage k+1.
For f = identity: reduce(reduce(x, k+1), k) = reduce(x, k).
Equations
- Tau.BookII.Regularity.code_tower_check bound db = Tau.BookII.Regularity.code_tower_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.code_tower_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L82-L91)@[irreducible]

**def
Tau.BookII.Regularity.code_tower_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_delta_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L94-L109)
**def
Tau.BookII.Regularity.code_delta_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.D51] Code extraction for the delta function:
code(delta_a, k, x) = 1 if reduce(x, k) == a, else 0.
Equations
- Tau.BookII.Regularity.code_delta_check k_max = Tau.BookII.Regularity.code_delta_check.go k_max 1 0 0 (k_max * 100 + 1)
Instances For

---

### `Tau.BookII.Regularity.code_delta_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L99-L108)@[irreducible]

**def
Tau.BookII.Regularity.code_delta_check.go
(k_max : Denotation.TauIdx)

(k a x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_constant_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L111-L129)
**def
Tau.BookII.Regularity.code_constant_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.D51] Spectral coefficient check for the constant function:
code_spectral(1, k, pi, v) = P_k / p for each residue class v.
Equations
- Tau.BookII.Regularity.code_constant_check k_max = Tau.BookII.Regularity.code_constant_check.go k_max 1 1 0 (k_max * 20 + 1)
Instances For

---

### `Tau.BookII.Regularity.code_constant_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L116-L128)@[irreducible]

**def
Tau.BookII.Regularity.code_constant_check.go
(k_max : Denotation.TauIdx)

(k pi_idx v fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.decode_reconstruct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L135-L144)
**def
Tau.BookII.Regularity.decode_reconstruct
(table : Denotation.TauIdx → ℤ)

(k x : Denotation.TauIdx)
 :ℤ**


[II.D52] Decode: reconstruct a function value from its CRT-indexed code.
Given a table of values indexed by points in Z/P_kZ, decode reads
the value at the stage-k representative of x.

decode_reconstruct(table, k, x) = table(reduce(x, k))

This is the inverse of code_extract: reading back the recorded value
at the canonical representative.
Equations
- Tau.BookII.Regularity.decode_reconstruct table k x = table (Tau.Polarity.reduce x k)
Instances For

---

### `Tau.BookII.Regularity.decode_crt_indicator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L146-L150)
**def
Tau.BookII.Regularity.decode_crt_indicator
(k x target : Denotation.TauIdx)
 :Bool**


[II.D52] CRT product indicator: returns true iff reduce(x, k) == target.
This is the product basis element
Phi_{v_1,...,v_k}(x) = prod_i E_{k,i,v_i}(x).
Equations
- Tau.BookII.Regularity.decode_crt_indicator k x target = (Tau.Polarity.reduce x k == target)
Instances For

---

### `Tau.BookII.Regularity.decode_welldef_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L152-L168)
**def
Tau.BookII.Regularity.decode_welldef_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.D52] Decode well-definedness check:
verify that decode is periodic: decode(table, k, x) = decode(table, k, x + P_k).
This follows from reduce(x + P_k, k) = reduce(x, k).
Equations
- Tau.BookII.Regularity.decode_welldef_check k_max bound = Tau.BookII.Regularity.decode_welldef_check.go k_max 1 0 (k_max * bound + k_max + bound + 1)
Instances For

---

### `Tau.BookII.Regularity.decode_welldef_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L158-L167)@[irreducible]

**def
Tau.BookII.Regularity.decode_welldef_check.go
(k_max : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.decode_uniqueness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L170-L187)
**def
Tau.BookII.Regularity.decode_uniqueness_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.D52] Decode uniqueness check:
for a != b in [0, P_k), the CRT indicators are different.
Equations
- Tau.BookII.Regularity.decode_uniqueness_check k_max = Tau.BookII.Regularity.decode_uniqueness_check.go k_max 1 0 0 (k_max * 100 + 1)
Instances For

---

### `Tau.BookII.Regularity.decode_uniqueness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L175-L186)@[irreducible]

**def
Tau.BookII.Regularity.decode_uniqueness_check.go
(k_max : Denotation.TauIdx)

(k a b fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_decode_inverse_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L193-L222)
**def
Tau.BookII.Regularity.code_decode_inverse_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T35] Code/Decode round-trip (direction 1): Decode . Code = id.
For a function f on Z/P_kZ:
decode(code(f), k, x) = code(f)(reduce(x, k))
= f(reduce(reduce(x,k), k)) = f(reduce(x,k))

For x < P_k, reduce(x, k) = x, so this gives f(x).
Equations
- Tau.BookII.Regularity.code_decode_inverse_check k_max = Tau.BookII.Regularity.code_decode_inverse_check.go_k k_max 1 (k_max * 200 + 1)
Instances For

---

### `Tau.BookII.Regularity.code_decode_inverse_check.go_k`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L202-L213)@[irreducible]

**def
Tau.BookII.Regularity.code_decode_inverse_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_decode_inverse_check.check_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L215-L221)@[irreducible]

**def
Tau.BookII.Regularity.code_decode_inverse_check.check_roundtrip
(f : Denotation.TauIdx → ℤ)

(k x fuel pk : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.decode_code_inverse_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L224-L249)
**def
Tau.BookII.Regularity.decode_code_inverse_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T35] Code/Decode round-trip (direction 2): Code . Decode = id.
For a coefficient table c : Z/P_kZ → Int:
code(decode(c), k, a) = decode(c)(reduce(a, k))
= c(reduce(reduce(a,k), k)) = c(reduce(a,k))

For a < P_k, this gives c(a).
Equations
- Tau.BookII.Regularity.decode_code_inverse_check k_max = Tau.BookII.Regularity.decode_code_inverse_check.go_k k_max 1 (k_max * 200 + 1)
Instances For

---

### `Tau.BookII.Regularity.decode_code_inverse_check.go_k`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L233-L240)@[irreducible]

**def
Tau.BookII.Regularity.decode_code_inverse_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.decode_code_inverse_check.check_inverse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L242-L248)@[irreducible]

**def
Tau.BookII.Regularity.decode_code_inverse_check.check_inverse
(table : Denotation.TauIdx → ℤ)

(k a fuel pk : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_spectral_scan_residues`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L255-L269)
**def
Tau.BookII.Regularity.code_spectral_scan_residues
(f g : Denotation.TauIdx → ℤ)

(k pi_idx : Denotation.TauIdx)
 :Bool**


Helper: scan residue classes for a given prime to find differing coefficients.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_spectral_scan_residues.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L261-L268)@[irreducible]

**def
Tau.BookII.Regularity.code_spectral_scan_residues.go
(f g : Denotation.TauIdx → ℤ)

(k pi_idx p v fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_spectral_find_separator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L271-L284)
**def
Tau.BookII.Regularity.code_spectral_find_separator
(f g : Denotation.TauIdx → ℤ)

(k : Denotation.TauIdx)
 :Bool**


Helper: search across primes for a separating spectral coefficient.
Equations
- Tau.BookII.Regularity.code_spectral_find_separator f g k = Tau.BookII.Regularity.code_spectral_find_separator.go f g k 1 (k + 1)
Instances For

---

### `Tau.BookII.Regularity.code_spectral_find_separator.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L276-L283)@[irreducible]

**def
Tau.BookII.Regularity.code_spectral_find_separator.go
(f g : Denotation.TauIdx → ℤ)

(k pi_idx fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_spectral_separation_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L286-L302)
**def
Tau.BookII.Regularity.code_spectral_separation_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T35] Spectral completeness: the per-prime projections determine f.
For distinct functions f, g on Z/P_kZ, there exists a prime p and
residue v such that code_spectral(f, k, p, v) != code_spectral(g, k, p, v).

Verified: for f = delta_0 and g = delta_1, the spectral coefficients differ.
Equations
- Tau.BookII.Regularity.code_spectral_separation_check k_max = Tau.BookII.Regularity.code_spectral_separation_check.go k_max 1 (k_max + 1)
Instances For

---

### `Tau.BookII.Regularity.code_spectral_separation_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L294-L301)@[irreducible]

**def
Tau.BookII.Regularity.code_spectral_separation_check.go
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_decode_delta_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L304-L331)
**def
Tau.BookII.Regularity.code_decode_delta_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T35] Delta function round-trip:
decode(code(delta_a)) = delta_a for all a in [0, P_k).
Equations
- Tau.BookII.Regularity.code_decode_delta_check k_max = Tau.BookII.Regularity.code_decode_delta_check.go_k k_max 1 (k_max * 200 + 1)
Instances For

---

### `Tau.BookII.Regularity.code_decode_delta_check.go_k`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L309-L315)@[irreducible]

**def
Tau.BookII.Regularity.code_decode_delta_check.go_k
(k_max : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_decode_delta_check.check_deltas`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L317-L330)@[irreducible]

**def
Tau.BookII.Regularity.code_decode_delta_check.check_deltas
(k a fuel pk : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_decode_tower_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L337-L354)
**def
Tau.BookII.Regularity.code_decode_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


Code/Decode respects tower structure:
reduce(code(id, k+1, x), k) = code(id, k, x).
For f = identity: reduce(reduce(x, k+1), k) = reduce(x, k).
Equations
- Tau.BookII.Regularity.code_decode_tower_check bound db = Tau.BookII.Regularity.code_decode_tower_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.code_decode_tower_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L343-L353)@[irreducible]

**def
Tau.BookII.Regularity.code_decode_tower_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.full_code_decode_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L360-L378)
**def
Tau.BookII.Regularity.full_code_decode_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.T35] Full Code/Decode bijection verification:


- Code extraction (delta, constant checks)

- Decode well-definedness (periodic)

- Decode uniqueness (CRT injectivity)

- Round-trip Decode . Code = id

- Round-trip Code . Decode = id

- Delta function round-trip

- Spectral separation (completeness)

- Tower compatibility

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.code_delta_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L442-L443)
**theorem
Tau.BookII.Regularity.code_delta_3 :code_delta_check 3 = true**


---

### `Tau.BookII.Regularity.code_constant_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L445-L446)
**theorem
Tau.BookII.Regularity.code_constant_3 :code_constant_check 3 = true**


---

### `Tau.BookII.Regularity.code_tower_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L448-L449)
**theorem
Tau.BookII.Regularity.code_tower_15_3 :code_tower_check 15 3 = true**


---

### `Tau.BookII.Regularity.decode_welldef_3_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L452-L453)
**theorem
Tau.BookII.Regularity.decode_welldef_3_15 :decode_welldef_check 3 15 = true**


---

### `Tau.BookII.Regularity.decode_unique_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L456-L457)
**theorem
Tau.BookII.Regularity.decode_unique_3 :decode_uniqueness_check 3 = true**


---

### `Tau.BookII.Regularity.code_decode_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L460-L461)
**theorem
Tau.BookII.Regularity.code_decode_3 :code_decode_inverse_check 3 = true**


---

### `Tau.BookII.Regularity.decode_code_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L463-L464)
**theorem
Tau.BookII.Regularity.decode_code_3 :decode_code_inverse_check 3 = true**


---

### `Tau.BookII.Regularity.code_decode_delta_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L467-L468)
**theorem
Tau.BookII.Regularity.code_decode_delta_3 :code_decode_delta_check 3 = true**


---

### `Tau.BookII.Regularity.spectral_sep_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L471-L472)
**theorem
Tau.BookII.Regularity.spectral_sep_3 :code_spectral_separation_check 3 = true**


---

### `Tau.BookII.Regularity.tower_compat_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L475-L476)
**theorem
Tau.BookII.Regularity.tower_compat_15_3 :code_decode_tower_check 15 3 = true**


---

### `Tau.BookII.Regularity.full_code_decode_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L479-L480)
**theorem
Tau.BookII.Regularity.full_code_decode_3 :full_code_decode_check 3 = true**


---

### `Tau.BookII.Regularity.code_decode_id_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L486-L493)
**theorem
Tau.BookII.Regularity.code_decode_id_roundtrip
(x k : Denotation.TauIdx)
 :decode_reconstruct (fun (a : Denotation.TauIdx) => code_extract (fun (n : Denotation.TauIdx) => ↑n) k a) k x = code_extract (fun (n : Denotation.TauIdx) => ↑n) k x**


[II.T35] Formal proof: Decode . Code = id for the identity function.
This follows from reduction idempotence: reduce(reduce(x, k), k) = reduce(x, k).

---

### `Tau.BookII.Regularity.decode_code_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/CodeDecode.lean#L495-L502)
**theorem
Tau.BookII.Regularity.decode_code_roundtrip
(table : Denotation.TauIdx → ℤ)

(a k : Denotation.TauIdx)
 :code_extract (fun (x : Denotation.TauIdx) => decode_reconstruct table k x) k a = decode_reconstruct table k a**


[II.T35] Formal proof: Code . Decode = id for any table.
This follows from reduce(reduce(a, k), k) = reduce(a, k).
