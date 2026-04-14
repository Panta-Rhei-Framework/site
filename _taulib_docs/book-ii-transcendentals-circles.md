---
layout: taulib-doc
title: "TauLib.BookII.Transcendentals.Circles"
permalink: /verify/taulib/docs/book-ii-transcendentals-circles/
lane: verify
module_name: "TauLib.BookII.Transcendentals.Circles"
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

# TauLib.BookII.Transcendentals.Circles


Solenoidal circles and S^1 as a profinite limit.

## Registry Cross-References


- [II.D26] Solenoidal Circle -- `solenoidal_b_orbit`, `solenoidal_c_orbit`

- [II.T21] S^1 as Profinite Limit -- `circle_profinite_check`

- [II.D27] Geometric-Topological Unification -- `geo_topo_check`


## Mathematical Content


Solenoidal circles: B and C coordinates cycle through residues mod p_k
at each stage k. The B-orbit at prime p_k is the residue class of B mod p_k.

S^1 = profinite limit of Z/p_k Z: all residues 0..p_k-1 appear in the
B-coordinate of some tau-admissible point.

The two solenoidal directions (B-orbit, C-orbit) are independently cyclic
at each stage, witnessing the T^2 = S^1 x S^1 torus structure.

---

### `Tau.BookII.Transcendentals.solenoidal_b_orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L35-L39)
**def
Tau.BookII.Transcendentals.solenoidal_b_orbit
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D26] Solenoidal B-orbit at the k-th prime: B mod p_k.
This is the residue of the exponent coordinate in the k-th cyclic factor
of the profinite group hat(Z).
Equations
- Tau.BookII.Transcendentals.solenoidal_b_orbit x k = (Tau.BookII.Interior.from_tau_idx x).b % Tau.Polarity.nth_prime k
Instances For

---

### `Tau.BookII.Transcendentals.solenoidal_c_orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L41-L43)
**def
Tau.BookII.Transcendentals.solenoidal_c_orbit
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


Solenoidal C-orbit at the k-th prime: C mod p_k.
Equations
- Tau.BookII.Transcendentals.solenoidal_c_orbit x k = (Tau.BookII.Interior.from_tau_idx x).c % Tau.Polarity.nth_prime k
Instances For

---

### `Tau.BookII.Transcendentals.exists_with_b_residue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L49-L59)
**def
Tau.BookII.Transcendentals.exists_with_b_residue
(r k bound : Denotation.TauIdx)
 :Bool**


Check whether a given residue r appears as a B-residue mod p_k
in some tau-admissible point in [2, bound].
Equations
- Tau.BookII.Transcendentals.exists_with_b_residue r k bound = Tau.BookII.Transcendentals.exists_with_b_residue.go r k bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Transcendentals.exists_with_b_residue.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L54-L58)@[irreducible]

**def
Tau.BookII.Transcendentals.exists_with_b_residue.go
(r k bound : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.exists_with_c_residue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L61-L70)
**def
Tau.BookII.Transcendentals.exists_with_c_residue
(r k bound : Denotation.TauIdx)
 :Bool**


Check whether a given residue r appears as a C-residue mod p_k.
Equations
- Tau.BookII.Transcendentals.exists_with_c_residue r k bound = Tau.BookII.Transcendentals.exists_with_c_residue.go r k bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Transcendentals.exists_with_c_residue.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L65-L69)@[irreducible]

**def
Tau.BookII.Transcendentals.exists_with_c_residue.go
(r k bound : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.circle_profinite_b_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L72-L83)
**def
Tau.BookII.Transcendentals.circle_profinite_b_check
(k bound : Denotation.TauIdx)
 :Bool**


[II.T21] S^1 as profinite limit: all residues 0..p_k-1 appear
in the B-coordinate of some tau-admissible point in [2, bound].
This witnesses the surjectivity of the B-projection onto Z/p_k Z.
Equations
- Tau.BookII.Transcendentals.circle_profinite_b_check k bound = Tau.BookII.Transcendentals.circle_profinite_b_check.go k bound 0 (Tau.Polarity.nth_prime k + 1)
Instances For

---

### `Tau.BookII.Transcendentals.circle_profinite_b_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L79-L82)@[irreducible]

**def
Tau.BookII.Transcendentals.circle_profinite_b_check.go
(k bound : Denotation.TauIdx)

(r fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.circle_profinite_c_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L85-L94)
**def
Tau.BookII.Transcendentals.circle_profinite_c_check
(k bound : Denotation.TauIdx)
 :Bool**


Same for C-coordinate.
Equations
- Tau.BookII.Transcendentals.circle_profinite_c_check k bound = Tau.BookII.Transcendentals.circle_profinite_c_check.go k bound 0 (Tau.Polarity.nth_prime k + 1)
Instances For

---

### `Tau.BookII.Transcendentals.circle_profinite_c_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L90-L93)@[irreducible]

**def
Tau.BookII.Transcendentals.circle_profinite_c_check.go
(k bound : Denotation.TauIdx)

(r fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.geo_topo_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L100-L110)
**def
Tau.BookII.Transcendentals.geo_topo_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D27] Geometric-topological unification: B and C orbits are
independently cyclic at each stage. T^2 = S^1_B x S^1_C.

Evidence: both B and C projections are surjective onto Z/p_k Z
for the first few primes.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.bc_independence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L112-L121)
**def
Tau.BookII.Transcendentals.bc_independence_check :Bool**


Independence check: B and C orbits are genuinely independent.
Witness: find points with same B but different C, and vice versa.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.circle_b_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L149-L149)
**theorem
Tau.BookII.Transcendentals.circle_b_k1 :circle_profinite_b_check 1 100 = true**


---

### `Tau.BookII.Transcendentals.circle_b_k2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L150-L150)
**theorem
Tau.BookII.Transcendentals.circle_b_k2 :circle_profinite_b_check 2 100 = true**


---

### `Tau.BookII.Transcendentals.circle_c_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L151-L151)
**theorem
Tau.BookII.Transcendentals.circle_c_k1 :circle_profinite_c_check 1 200 = true**


---

### `Tau.BookII.Transcendentals.geo_topo_200`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L152-L152)
**theorem
Tau.BookII.Transcendentals.geo_topo_200 :geo_topo_check 200 = true**


---

### `Tau.BookII.Transcendentals.bc_indep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/Circles.lean#L153-L153)
**theorem
Tau.BookII.Transcendentals.bc_indep :bc_independence_check = true**
