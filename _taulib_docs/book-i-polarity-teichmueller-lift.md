---
layout: taulib-doc
title: "TauLib.BookI.Polarity.TeichmuellerLift"
permalink: /verify/taulib/docs/book-i-polarity-teichmueller-lift/
lane: verify
module_name: "TauLib.BookI.Polarity.TeichmuellerLift"
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

# TauLib.Polarity.TeichmuellerLift


Teichmüller-style canonical lifts from single-prime residues to omega-tails via CRT.

## Registry Cross-References


- [I.D30] Teichmüller Lift — `teich_lift`, `teich_component`

- [I.D29] CRT Decomposition — used for reconstruction at each stage


## Ground Truth Sources


- chunk_0177_M001919: Teichmüller chapter (Lift_ω, refinement coherence, multiplicativity)

- chunk_0314_M002691: Teichmüller lifts as CRT idempotent projections


## Mathematical Content


A Teichmüller lift embeds a single-prime residue r ∈ Z/p_iZ into the full
primorial tower as an omega-tail. The lift is constructed via CRT at each stage:
at depth k ≥ i, place residue r at position i and 0 at all other positions,
then reconstruct via crt_reconstruct.

Properties:


- Retraction: Lift_i(r) mod p_i = r mod p_i

- Orthogonality: Lift_i(r) mod p_j = 0 for j ≠ i

- Compatibility: Lift_i(r) is a compatible tower

- Decomposition: every omega-tail = Σ Lift_i(r_i)

- Multiplicativity: Lift_i(r) · Lift_i(s) = Lift_i(r·s)


---

### `Tau.Polarity.teich_residues`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L42-L45)
**def
Tau.Polarity.teich_residues
(r i k : Denotation.TauIdx)
 :List Denotation.TauIdx**


Teichmüller residue vector: r at position i (0-indexed), 0 elsewhere.
This is the input to CRT reconstruction for a single-prime lift.
Equations
- Tau.Polarity.teich_residues r i k = List.map (fun (j : Tau.Denotation.TauIdx) => if (j == i) = true then r % Tau.Polarity.nth_prime (i + 1) else 0)
 (List.range k)
Instances For

---

### `Tau.Polarity.teich_component`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L51-L54)
**def
Tau.Polarity.teich_component
(r i k : Denotation.TauIdx)
 :Denotation.TauIdx**


Teichmüller component at depth k: CRT reconstruction with single active residue.
Returns 0 for k < i+1 (prime p_{i+1} not yet in the primorial).
Equations
- Tau.Polarity.teich_component r i k = if k ≤ i then 0 else Tau.Polarity.crt_reconstruct (Tau.Polarity.teich_residues r i k) k
Instances For

---

### `Tau.Polarity.teich_lift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L70-L73)
**def
Tau.Polarity.teich_lift
(r i d : Denotation.TauIdx)
 :OmegaTail**


The Teichmüller omega-tail: canonical lift of residue r at prime p_{i+1}.
i is 0-indexed (i=0 → prime p_1=2).
Equations
- Tau.Polarity.teich_lift r i d = { depth := d, components := Tau.Polarity.teich_list✝ r i d, depth_eq := ⋯ }
Instances For

---

### `Tau.Polarity.teich_retract_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L79-L81)
**def
Tau.Polarity.teich_retract_check
(r i d : Denotation.TauIdx)
 :Bool**


Retraction check: Lift_i(r) at depth d, mod p_{i+1} = r mod p_{i+1}.
Equations
- Tau.Polarity.teich_retract_check r i d = (decide (i < d) && Tau.Polarity.teich_component r i d % Tau.Polarity.nth_prime (i + 1) == r % Tau.Polarity.nth_prime (i + 1))
Instances For

---

### `Tau.Polarity.teich_orthog_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L83-L85)
**def
Tau.Polarity.teich_orthog_check
(r i j d : Denotation.TauIdx)
 :Bool**


Orthogonality check: Lift_i(r) mod p_{j+1} = 0 for j ≠ i.
Equations
- Tau.Polarity.teich_orthog_check r i j d = (i == j || decide (i < d) && decide (j < d) && Tau.Polarity.teich_component r i d % Tau.Polarity.nth_prime (j + 1) == 0)
Instances For

---

### `Tau.Polarity.teich_compat_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L87-L89)
**def
Tau.Polarity.teich_compat_check
(r i d : Denotation.TauIdx)
 :Bool**


Compatibility check: the Teichmüller lift is a compatible tower.
Equations
- Tau.Polarity.teich_compat_check r i d = Tau.Polarity.compat_check (Tau.Polarity.teich_lift r i d)
Instances For

---

### `Tau.Polarity.teich_mult_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L91-L97)
**def
Tau.Polarity.teich_mult_check
(r s i d : Denotation.TauIdx)
 :Bool**


Multiplicativity check: Lift_i(r) * Lift_i(s) = Lift_i(r*s) (componentwise).
Equations
- Tau.Polarity.teich_mult_check r s i d = (((Tau.Polarity.teich_lift r i d).mul (Tau.Polarity.teich_lift s i d) ⋯).components == (Tau.Polarity.teich_lift (r * s) i d).components)
Instances For

---

### `Tau.Polarity.teich_decomp_check_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L99-L108)@[irreducible]

**def
Tau.Polarity.teich_decomp_check_go
(n d : Denotation.TauIdx)

(i fuel : ℕ)

(acc : List Denotation.TauIdx)
 :List Denotation.TauIdx**


Decomposition check: nat_to_tail(n) = Σ teich_lift(n mod p_i, i, d).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.teich_decomp_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L110-L114)
**def
Tau.Polarity.teich_decomp_check
(n d : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Polarity.teich_decomp_check n d = (Tau.Polarity.teich_decomp_check_go n d 0 d (List.map (fun (x : ℕ) => 0) (List.range d)) == (Tau.Polarity.mk_omega_tail n d).components)
Instances For

---

### `Tau.Polarity.teich_retraction_formal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L211-L219)
**theorem
Tau.Polarity.teich_retraction_formal
{r i d : Denotation.TauIdx}

(hi : i < d)

(hyp : CRTHyp d)
 :teich_component r i d % nth_prime (i + 1) = r % nth_prime (i + 1)**


Teichmüller retraction (formal):
teich_component r i d ≡ r (mod p_{i+1}) for i < d.

---

### `Tau.Polarity.teich_orthogonality_formal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/TeichmuellerLift.lean#L221-L230)
**theorem
Tau.Polarity.teich_orthogonality_formal
{r i j d : Denotation.TauIdx}

(hi : i < d)

(hj : j < d)

(hne : i ≠ j)

(hyp : CRTHyp d)
 :teich_component r i d % nth_prime (j + 1) = 0**


Teichmüller orthogonality (formal):
teich_component r i d ≡ 0 (mod p_{j+1}) for j ≠ i, both < d.
