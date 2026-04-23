---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.CanonicalBasis"
permalink: /verify/taulib/docs/book-ii-hartogs-canonical-basis/
lane: verify
module_name: "TauLib.BookII.Hartogs.CanonicalBasis"
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

# TauLib.BookII.Hartogs.CanonicalBasis


Cylinder generators and the canonical holomorphic basis B_τ.

## Registry Cross-References


- [II.D46] Cylinder Generator — `cylinder_gen`, `cylinder_gen_indicator`

- [II.D45] Canonical Basis — `basis_orthogonality_check`, `basis_completeness_check`, `basis_independence_check`

- [II.T31] Finite Spectral Support — `finite_spectral_support_check`

- [II.P09] Projection Formula — `proj_coeff`, `projection_recovery_check`


## Mathematical Content


The canonical holomorphic basis B_τ consists of cylinder generators:

E_{k,prime_idx,v}^(sigma)(x) = 1 if reduce(x, k) mod p_i == v, else 0

where k is the stage, p_i = nth_prime(prime_idx) is a prime dividing P_k,
v is the residue class, and sigma ∈ {B, C} selects the bipolar channel.

**Key properties:**


- **Orthogonality (II.D45):** E_{k,p,v} * E_{k,p,w} = 0 for v ≠ w (same prime)

- **Completeness (II.D45):** sum_{v=0}^{p-1} E_{k,p,v}(x) = 1 for all x

- **Independence (II.D45):** generators for distinct primes are independent

- **Finite spectral support (II.T31):** at stage k, the number of nonzero
generators is at most sum of primes dividing P_k


**Projection formula (II.P09):**
proj_coeff(f, k, prime_idx, v) = sum_{x : reduce(x,k) mod p == v} f(x)

In the indicator basis, the projection of f onto E_{k,p,v} extracts the
sum of f over the residue class v mod p at stage k. The expansion
f = sum_v proj_coeff(f, k, p, v) * E_{k,p,v} recovers f on Z/P_kZ.

---

### `Tau.BookII.Hartogs.cylinder_gen`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L48-L56)
**def
Tau.BookII.Hartogs.cylinder_gen
(k prime_idx v : Denotation.TauIdx)

(_sigma : Bool)

(x : Denotation.TauIdx)
 :ℤ**


[II.D46] Cylinder generator E_{k,prime_idx,v}^(sigma)(x).

Returns 1 if x (reduced to stage k) falls in residue class v
modulo the prime p_{prime_idx}, and 0 otherwise.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.cylinder_gen_indicator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L58-L62)
**def
Tau.BookII.Hartogs.cylinder_gen_indicator
(k prime_idx v x : Denotation.TauIdx)
 :Bool**


Cylinder generator as Bool indicator (for decidable checks).
Equations
- Tau.BookII.Hartogs.cylinder_gen_indicator k prime_idx v x = (Tau.Polarity.nth_prime prime_idx != 0 && Tau.Polarity.reduce x k % Tau.Polarity.nth_prime prime_idx == v)
Instances For

---

### `Tau.BookII.Hartogs.ortho_pair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L68-L80)
**def
Tau.BookII.Hartogs.ortho_pair
(k pi_idx v w : Denotation.TauIdx)
 :Bool**


Helper: check orthogonality of generators for residue classes v, w
at stage k, prime pi_idx, for all x in [0, P_k).
Equations
- Tau.BookII.Hartogs.ortho_pair k pi_idx v w = Tau.BookII.Hartogs.ortho_pair.go k pi_idx v w 0 (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Hartogs.ortho_pair.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L73-L79)@[irreducible]

**def
Tau.BookII.Hartogs.ortho_pair.go
(k pi_idx v w : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.basis_orthogonality_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L82-L100)
**def
Tau.BookII.Hartogs.basis_orthogonality_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.D45, orthogonality] For a fixed stage k and prime p_{prime_idx},
the generators for distinct residue classes v and w are orthogonal:
E_{k,p,v}(x) * E_{k,p,w}(x) = 0 for all x when v ≠ w.
Equations
- Tau.BookII.Hartogs.basis_orthogonality_check k_max bound = Tau.BookII.Hartogs.basis_orthogonality_check.go k_max 1 1 0 0 ((k_max + 1) * (k_max + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.basis_orthogonality_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L88-L99)@[irreducible]

**def
Tau.BookII.Hartogs.basis_orthogonality_check.go
(k_max : Denotation.TauIdx)

(k pi_idx v w fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.gen_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L106-L120)
**def
Tau.BookII.Hartogs.gen_sum
(k pi_idx x : Denotation.TauIdx)
 :ℤ**


Helper: sum of cylinder generators over residue classes v=0..p-1 at
stage k, prime pi_idx, for a given x.
Equations
- Tau.BookII.Hartogs.gen_sum k pi_idx x = Tau.BookII.Hartogs.gen_sum.go k pi_idx x 0 (Tau.Polarity.nth_prime pi_idx + 1) 0
Instances For

---

### `Tau.BookII.Hartogs.gen_sum.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L112-L119)@[irreducible]

**def
Tau.BookII.Hartogs.gen_sum.go
(k pi_idx x : Denotation.TauIdx)

(v fuel : ℕ)

(acc : ℤ)
 :ℤ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.basis_completeness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L122-L135)
**def
Tau.BookII.Hartogs.basis_completeness_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.D45, completeness] For a fixed stage k and prime p_{prime_idx},
sum_{v=0}^{p-1} E_{k,p,v}(x) = 1 for all x.
Equations
- Tau.BookII.Hartogs.basis_completeness_check k_max bound = Tau.BookII.Hartogs.basis_completeness_check.go k_max 1 1 0 ((k_max + 1) * (k_max + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.basis_completeness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L127-L134)@[irreducible]

**def
Tau.BookII.Hartogs.basis_completeness_check.go
(k_max : Denotation.TauIdx)

(k pi_idx x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.indep_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L141-L153)
**def
Tau.BookII.Hartogs.indep_witness
(k pi1 pi2 : Denotation.TauIdx)
 :Bool**


Helper: find a witness x where E_{k,p1,0}(x) = 1 and E_{k,p2,0}(x) = 1.
Equations
- Tau.BookII.Hartogs.indep_witness k pi1 pi2 = Tau.BookII.Hartogs.indep_witness.go k pi1 pi2 0 (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Hartogs.indep_witness.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L145-L152)@[irreducible]

**def
Tau.BookII.Hartogs.indep_witness.go
(k pi1 pi2 : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.basis_independence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L155-L167)
**def
Tau.BookII.Hartogs.basis_independence_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.D45, independence] Generators for distinct primes at the same stage
are independent: CRT guarantees simultaneous residue solutions.
Equations
- Tau.BookII.Hartogs.basis_independence_check k_max = Tau.BookII.Hartogs.basis_independence_check.go k_max 2 1 2 (k_max * k_max * k_max + 1)
Instances For

---

### `Tau.BookII.Hartogs.basis_independence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L160-L166)@[irreducible]

**def
Tau.BookII.Hartogs.basis_independence_check.go
(k_max : Denotation.TauIdx)

(k pi1 pi2 fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.canonical_basis_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L173-L178)
**def
Tau.BookII.Hartogs.canonical_basis_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.D45] Full canonical basis verification:
orthogonality + completeness + independence.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.count_nonzero_generators`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L184-L196)
**def
Tau.BookII.Hartogs.count_nonzero_generators
(k _x : Denotation.TauIdx)
 :ℕ**


[II.T31] Count of nonzero cylinder generators at stage k for a given x.
At stage k, each prime contributes exactly 1 active residue class.
Equations
- Tau.BookII.Hartogs.count_nonzero_generators k _x = Tau.BookII.Hartogs.count_nonzero_generators.go k 1 (k + 1) 0
Instances For

---

### `Tau.BookII.Hartogs.count_nonzero_generators.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L189-L195)@[irreducible]

**def
Tau.BookII.Hartogs.count_nonzero_generators.go
(k : Denotation.TauIdx)

(pi_idx fuel acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.prime_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L198-L206)
**def
Tau.BookII.Hartogs.prime_sum
(k : Denotation.TauIdx)
 :ℕ**


Sum of primes dividing P_k: the spectral support bound.
Equations
- Tau.BookII.Hartogs.prime_sum k = Tau.BookII.Hartogs.prime_sum.go k 1 (k + 1) 0
Instances For

---

### `Tau.BookII.Hartogs.prime_sum.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L202-L205)@[irreducible]

**def
Tau.BookII.Hartogs.prime_sum.go
(k : Denotation.TauIdx)

(i fuel acc : ℕ)
 :ℕ**

Equations
- Tau.BookII.Hartogs.prime_sum.go k i fuel acc = if fuel = 0 then acc
 else if i > k then acc else Tau.BookII.Hartogs.prime_sum.go k (i + 1) (fuel - 1) (acc + Tau.Polarity.nth_prime i)
Instances For

---

### `Tau.BookII.Hartogs.finite_spectral_support_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L208-L222)
**def
Tau.BookII.Hartogs.finite_spectral_support_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.T31] Finite spectral support check:
at each stage k, the count of active generators equals k,
which is <= sum of p_i.
Equations
- Tau.BookII.Hartogs.finite_spectral_support_check k_max bound = Tau.BookII.Hartogs.finite_spectral_support_check.go k_max 1 0 ((k_max + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Hartogs.finite_spectral_support_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L214-L221)@[irreducible]

**def
Tau.BookII.Hartogs.finite_spectral_support_check.go
(k_max : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.proj_coeff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L228-L239)
**def
Tau.BookII.Hartogs.proj_coeff
(f : Denotation.TauIdx → ℤ)

(k prime_idx v : Denotation.TauIdx)
 :ℤ**


[II.P09] Spectral projection coefficient:
proj_coeff(f, k, prime_idx, v) = sum over x in Z/P_kZ of f(x) * E_{k,p,v}(x).
Equations
- Tau.BookII.Hartogs.proj_coeff f k prime_idx v = Tau.BookII.Hartogs.proj_coeff.go f k prime_idx v 0 (Tau.Polarity.primorial k) 0
Instances For

---

### `Tau.BookII.Hartogs.proj_coeff.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L233-L238)@[irreducible]

**def
Tau.BookII.Hartogs.proj_coeff.go
(f : Denotation.TauIdx → ℤ)

(k prime_idx v : Denotation.TauIdx)

(x fuel : ℕ)

(acc : ℤ)
 :ℤ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.projection_delta_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L241-L259)
**def
Tau.BookII.Hartogs.projection_delta_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.P09] Projection delta check: for delta_a(x) = (x == a ? 1 : 0),
proj_coeff(delta_a, k, pi, a mod p) = 1 for all a in [0, P_k).
Equations
- Tau.BookII.Hartogs.projection_delta_check k_max = Tau.BookII.Hartogs.projection_delta_check.go k_max 1 1 0 (k_max * k_max * 100 + 1)
Instances For

---

### `Tau.BookII.Hartogs.projection_delta_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L246-L258)@[irreducible]

**def
Tau.BookII.Hartogs.projection_delta_check.go
(k_max : Denotation.TauIdx)

(k pi_idx a fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.projection_recovery_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L261-L279)
**def
Tau.BookII.Hartogs.projection_recovery_check
(k_max : Denotation.TauIdx)
 :Bool**


[II.P09] Projection recovery check: for f(x) = 1,
proj_coeff(1, k, pi, v) = P_k / p for each v.
Equations
- Tau.BookII.Hartogs.projection_recovery_check k_max = Tau.BookII.Hartogs.projection_recovery_check.go k_max 1 1 0 (k_max * k_max * 20 + 1)
Instances For

---

### `Tau.BookII.Hartogs.projection_recovery_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L266-L278)@[irreducible]

**def
Tau.BookII.Hartogs.projection_recovery_check.go
(k_max : Denotation.TauIdx)

(k pi_idx v fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bipolar_cylinder_gen`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L285-L292)
**def
Tau.BookII.Hartogs.bipolar_cylinder_gen
(_k prime_idx v : Denotation.TauIdx)

(sigma : Bool)

(x : Denotation.TauIdx)
 :ℤ**


Bipolar cylinder generator: applied to the B or C coordinate
of the ABCD decomposition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bipolar_channel_orthogonality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L294-L309)
**def
Tau.BookII.Hartogs.bipolar_channel_orthogonality
(bound : Denotation.TauIdx)
 :Bool**


Bipolar orthogonality: B-channel and C-channel projections
have zero cross-product.
Equations
- Tau.BookII.Hartogs.bipolar_channel_orthogonality bound = Tau.BookII.Hartogs.bipolar_channel_orthogonality.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Hartogs.bipolar_channel_orthogonality.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L299-L308)@[irreducible]

**def
Tau.BookII.Hartogs.bipolar_channel_orthogonality.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_canonical_basis_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L315-L322)
**def
Tau.BookII.Hartogs.full_canonical_basis_check
(k_max bound : Denotation.TauIdx)
 :Bool**


Full check combining canonical basis, finite spectral support,
and projection formula.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.basis_ortho_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L387-L388)
**theorem
Tau.BookII.Hartogs.basis_ortho_3_30 :basis_orthogonality_check 3 30 = true**


---

### `Tau.BookII.Hartogs.basis_complete_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L391-L392)
**theorem
Tau.BookII.Hartogs.basis_complete_3_30 :basis_completeness_check 3 30 = true**


---

### `Tau.BookII.Hartogs.basis_indep_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L395-L396)
**theorem
Tau.BookII.Hartogs.basis_indep_4 :basis_independence_check 4 = true**


---

### `Tau.BookII.Hartogs.basis_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L399-L400)
**theorem
Tau.BookII.Hartogs.basis_3_30 :canonical_basis_check 3 30 = true**


---

### `Tau.BookII.Hartogs.spectral_support_3_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L403-L404)
**theorem
Tau.BookII.Hartogs.spectral_support_3_30 :finite_spectral_support_check 3 30 = true**


---

### `Tau.BookII.Hartogs.proj_delta_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L407-L408)
**theorem
Tau.BookII.Hartogs.proj_delta_3 :projection_delta_check 3 = true**


---

### `Tau.BookII.Hartogs.proj_recovery_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L411-L412)
**theorem
Tau.BookII.Hartogs.proj_recovery_3 :projection_recovery_check 3 = true**


---

### `Tau.BookII.Hartogs.bipolar_ortho_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L415-L416)
**theorem
Tau.BookII.Hartogs.bipolar_ortho_20 :bipolar_channel_orthogonality 20 = true**


---

### `Tau.BookII.Hartogs.full_basis_3_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/CanonicalBasis.lean#L419-L420)
**theorem
Tau.BookII.Hartogs.full_basis_3_20 :full_canonical_basis_check 3 20 = true**
