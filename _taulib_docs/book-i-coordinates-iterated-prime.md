---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.IteratedPrime"
permalink: /verify/taulib/docs/book-i-coordinates-iterated-prime/
lane: verify
module_name: "TauLib.BookI.Coordinates.IteratedPrime"
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

# TauLib.Coordinates.IteratedPrime


The iterated prime tower: k-fold composition of the prime enumeration
function nthPrime. Each generator's orbit carries a natural scalar
projection via iterated prime enumeration.

## Registry Cross-References


- [I.D94] Orbit-Set Map — connection to semantic projection


## Mathematical Content


### The Iterated Prime Tower


Define P^(k)(n) = k-fold iterated nthPrime:


- P^(0)(n) = n (identity, α-orbit)

- P^(1)(n) = nthPrime(n) (primes, π-orbit)

- P^(2)(n) = nthPrime(nthPrime(n)) (super-primes, γ-orbit)

- P^(3)(n) = nthPrime^3(n) (η-orbit)

- P^(4)(n) = nthPrime^4(n) (ω-orbit)


Key values:
γ₁ = P^(2)(1) = 3, γ₂ = P^(2)(2) = 5, γ₃ = P^(2)(3) = 11
η₁ = P^(3)(1) = 5, η₂ = P^(3)(2) = 11, η₃ = P^(3)(3) = 31
ω₁ = P^(4)(1) = 11, ω₂ = P^(4)(2) = 31, ω₃ = P^(4)(3) = 127

### Connection to α Formula


The fine-structure constant is expressed entirely in tower values:
α = (ω₁ / (γ₁ · γ₂))² · ι<sub>τ</sub>⁴ = (11/15)² · ι<sub>τ</sub>⁴

The Euler sieve factor:
8/15 = (1 - 1/γ₁)(1 - 1/η₁) = (2/3)(4/5)

The S₅ correction:
(8/15) · (1 + 1/η₁!) = (8/15) · (121/120) = 121/225 = (11/15)²

### Tower Nesting


ω-values ⊂ η-values ⊂ γ-values ⊂ π-values (as value sets).
Cross-level shift: η_n = γ_{π_n} for all n.

## Ground Truth Sources


- Book I ch83: Orbit-set correspondence, semantic projection

- Book IV ch11: Dimensionless cascade, Route C tower formula

- Book IV ch29: Fine-structure constant derivation


---

### `Tau.Coordinates.factorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L58-L61)
**def
Tau.Coordinates.factorial :Nat → Nat**


Simple factorial function for tower connections.
Equations
- Tau.Coordinates.factorial 0 = 1
- Tau.Coordinates.factorial n.succ = (n + 1) * Tau.Coordinates.factorial n
Instances For

---

### `Tau.Coordinates.iteratedPrime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L67-L78)
**def
Tau.Coordinates.iteratedPrime :Nat → Nat → Nat**


The k-fold iterated prime function P^(k)(n).
iteratedPrime 0 n = n (identity).
iteratedPrime (k+1) n = nthPrime(iteratedPrime k n).

NOTE: nthPrime is 0-indexed in Lean (nthPrime 0 = 2),
but the tower convention uses 1-indexed input:
val(α_n) = n, val(π_n) = p_n where p_1 = 2.
We use the RAW function here; users apply the index
shift when mapping to generator orbits.
Equations
- Tau.Coordinates.iteratedPrime 0 x✝ = x✝
- Tau.Coordinates.iteratedPrime k.succ x✝ = Tau.Coordinates.nthPrime (Tau.Coordinates.iteratedPrime k x✝)
Instances For

---

### `Tau.Coordinates.towerVal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L115-L122)
**def
Tau.Coordinates.towerVal :Nat → Nat → Nat**


Tower value with 1-indexed input (physics convention).
towerVal 0 n = n (identity, α-orbit).
towerVal 1 n = nthPrime(n-1) (primes, π-orbit, 1-indexed).
towerVal 2 n = nthPrime(nthPrime(n-1) - 1) (super-primes, γ-orbit).
The index shift accounts for nthPrime being 0-indexed.
Equations
- Tau.Coordinates.towerVal 0 x✝ = x✝
- Tau.Coordinates.towerVal k.succ x✝ = Tau.Coordinates.nthPrime (Tau.Coordinates.towerVal k x✝ - 1)
Instances For

---

### `Tau.Coordinates.gamma_1_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L174-L175)
**theorem
Tau.Coordinates.gamma_1_eq :towerVal 2 1 = 3**


γ₁ = 3 (first value of γ-orbit).

---

### `Tau.Coordinates.gamma_2_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L177-L178)
**theorem
Tau.Coordinates.gamma_2_eq :towerVal 2 2 = 5**


γ₂ = 5 (second value of γ-orbit).

---

### `Tau.Coordinates.gamma_3_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L180-L181)
**theorem
Tau.Coordinates.gamma_3_eq :towerVal 2 3 = 11**


γ₃ = 11 (third value of γ-orbit).

---

### `Tau.Coordinates.eta_1_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L183-L184)
**theorem
Tau.Coordinates.eta_1_eq :towerVal 3 1 = 5**


η₁ = 5 (first value of η-orbit).

---

### `Tau.Coordinates.eta_2_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L186-L187)
**theorem
Tau.Coordinates.eta_2_eq :towerVal 3 2 = 11**


η₂ = 11 (second value of η-orbit).

---

### `Tau.Coordinates.eta_3_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L189-L190)
**theorem
Tau.Coordinates.eta_3_eq :towerVal 3 3 = 31**


η₃ = 31 (third value of η-orbit).

---

### `Tau.Coordinates.omega_1_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L192-L193)
**theorem
Tau.Coordinates.omega_1_eq :towerVal 4 1 = 11**


ω₁ = 11 (first value of ω-orbit).

---

### `Tau.Coordinates.omega_2_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L195-L196)
**theorem
Tau.Coordinates.omega_2_eq :towerVal 4 2 = 31**


ω₂ = 31 (second value of ω-orbit).

---

### `Tau.Coordinates.omega_3_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L198-L199)
**theorem
Tau.Coordinates.omega_3_eq :towerVal 4 3 = 127**


ω₃ = 127 (third value of ω-orbit).

---

### `Tau.Coordinates.gamma_product_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L205-L207)
**theorem
Tau.Coordinates.gamma_product_15 :towerVal 2 1 * towerVal 2 2 = 15**


γ₁ · γ₂ = 15 (denominator of α).

---

### `Tau.Coordinates.omega_1_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L209-L211)
**theorem
Tau.Coordinates.omega_1_squared :towerVal 4 1 * towerVal 4 1 = 121**


ω₁² = 121 (numerator of α).

---

### `Tau.Coordinates.tower_ratio_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L213-L216)
**theorem
Tau.Coordinates.tower_ratio_identity :towerVal 4 1 * 15 = 11 * (towerVal 2 1 * towerVal 2 2)**


ω₁ / (γ₁ · γ₂) = 11/15 as cross-multiplied identity:
ω₁ · 15 = 11 · (γ₁ · γ₂).

---

### `Tau.Coordinates.tower_alpha_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L218-L221)
**theorem
Tau.Coordinates.tower_alpha_ratio :towerVal 4 1 ^ 2 * 225 = 121 * (towerVal 2 1 * towerVal 2 2) ^ 2**


(ω₁)² / (γ₁ · γ₂)² = 121/225 = (11/15)² as cross-multiplied:
(ω₁)² · 225 = 121 · (γ₁ · γ₂)².

---

### `Tau.Coordinates.euler_sieve_tower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L227-L231)
**theorem
Tau.Coordinates.euler_sieve_tower :(towerVal 2 1 - 1) * (towerVal 3 1 - 1) * 15 = 8 * towerVal 2 1 * towerVal 3 1**


The Euler sieve factor: (1 - 1/γ₁)(1 - 1/η₁) = 8/15.
Cross-multiplied: (γ₁ - 1)(η₁ - 1) · 15 = 8 · γ₁ · η₁.

---

### `Tau.Coordinates.eta_1_is_generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L237-L238)
**theorem
Tau.Coordinates.eta_1_is_generator_count :towerVal 3 1 = 5**


η₁ = 5 = number of generators {α, π, γ, η, ω}.

---

### `Tau.Coordinates.eta_1_factorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L240-L241)
**theorem
Tau.Coordinates.eta_1_factorial :factorial (towerVal 3 1) = 120**


η₁! = 120 = |S₅|.

---

### `Tau.Coordinates.s5_correction_yields_tower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L243-L247)
**theorem
Tau.Coordinates.s5_correction_yields_tower :8 * (factorial (towerVal 3 1) + 1) * 225 = 121 * 15 * factorial (towerVal 3 1)**


The S₅ correction: (8/15)(1 + 1/η₁!) = 121/225.
Cross-multiplied: 8 · (η₁! + 1) · 225 = 121 · 15 · η₁!.

---

### `Tau.Coordinates.cross_level_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L253-L255)
**theorem
Tau.Coordinates.cross_level_1 :towerVal 3 1 = towerVal 2 (towerVal 1 1)**


Cross-level shift: η_n = γ_{π_n} for n = 1..5.
towerVal 3 n = towerVal 2 (towerVal 1 n).

---

### `Tau.Coordinates.cross_level_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L256-L256)
**theorem
Tau.Coordinates.cross_level_2 :towerVal 3 2 = towerVal 2 (towerVal 1 2)**


---

### `Tau.Coordinates.cross_level_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L257-L257)
**theorem
Tau.Coordinates.cross_level_3 :towerVal 3 3 = towerVal 2 (towerVal 1 3)**


---

### `Tau.Coordinates.cross_level_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L258-L258)
**theorem
Tau.Coordinates.cross_level_4 :towerVal 3 4 = towerVal 2 (towerVal 1 4)**


---

### `Tau.Coordinates.cross_level_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L259-L259)
**theorem
Tau.Coordinates.cross_level_5 :towerVal 3 5 = towerVal 2 (towerVal 1 5)**


---

### `Tau.Coordinates.omega_3_mersenne`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L261-L262)
**theorem
Tau.Coordinates.omega_3_mersenne :towerVal 4 3 = 2 ^ 7 - 1**


ω₃ = 127 = 2⁷ - 1 (Mersenne prime).

---

### `Tau.Coordinates.factorial_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L268-L269)
**theorem
Tau.Coordinates.factorial_5 :factorial 5 = 120**


factorial 5 = 120.

---

### `Tau.Coordinates.factorial_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L271-L272)
**theorem
Tau.Coordinates.factorial_3 :factorial 3 = 6**


factorial 3 = 6.

---

### `Tau.Coordinates.factorial_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L274-L275)
**theorem
Tau.Coordinates.factorial_4 :factorial 4 = 24**


factorial 4 = 24.

---

### `Tau.Coordinates.factorial_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L277-L278)
**theorem
Tau.Coordinates.factorial_6 :factorial 6 = 720**


factorial 6 = 720.

---

### `Tau.Coordinates.factorial_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L280-L281)
**theorem
Tau.Coordinates.factorial_7 :factorial 7 = 5040**


factorial 7 = 5040.

---

### `Tau.Coordinates.perfect_square_at_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L283-L289)
**theorem
Tau.Coordinates.perfect_square_at_5 :8 * (120 + 1) = 121 * 8 ∧ 15 * 120 = 225 * 8 ∧ 121 = 11 * 11 ∧ 225 = 15 * 15**


For N = 5: 8·(N!+1) / (15·N!) = 121/225 = 11²/15².
We verify: 8·121 = 968, 15·120 = 1800, gcd = 8, giving 121/225.

---

### `Tau.Coordinates.not_perfect_square_at_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L291-L294)
**theorem
Tau.Coordinates.not_perfect_square_at_3 :((List.range 8).all fun (m : Nat) => m * m != 56) = true**


For N = 3: 8·(3!+1) = 56 is NOT a perfect square.
Verified: no m ∈ {0,...,7} satisfies m² = 56 (and m ≥ 8 ⟹ m² ≥ 64 > 56).

---

### `Tau.Coordinates.not_perfect_square_at_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L296-L299)
**theorem
Tau.Coordinates.not_perfect_square_at_4 :((List.range 15).all fun (m : Nat) => m * m != 200) = true**


For N = 4: 8·(4!+1) = 200 is NOT a perfect square.
Verified: no m ∈ {0,...,14} satisfies m² = 200 (and m ≥ 15 ⟹ m² ≥ 225 > 200).

---

### `Tau.Coordinates.not_perfect_square_at_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L301-L304)
**theorem
Tau.Coordinates.not_perfect_square_at_6 :((List.range 76).all fun (m : Nat) => m * m != 5768) = true**


For N = 6: 8·(6!+1) = 5768 is NOT a perfect square.
Verified: no m ∈ {0,...,75} satisfies m² = 5768 (and m ≥ 76 ⟹ m² ≥ 5776 > 5768).

---

### `Tau.Coordinates.denom_not_square_at_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L306-L309)
**theorem
Tau.Coordinates.denom_not_square_at_7 :((List.range 275).all fun (m : Nat) => m * m != 75600) = true**


For N = 7: 15·7! = 75600 is NOT a perfect square.
Verified: no m ∈ {0,...,274} satisfies m² = 75600 (and m ≥ 275 ⟹ m² ≥ 75625 > 75600).

---

### `Tau.Coordinates.pi_1_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L327-L328)
**theorem
Tau.Coordinates.pi_1_eq :towerVal 1 1 = 2**


π₁ = 2 (first value of π-orbit).

---

### `Tau.Coordinates.solenoidal_balance_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L330-L334)
**theorem
Tau.Coordinates.solenoidal_balance_identity :towerVal 1 1 * towerVal 3 2 = 2 * towerVal 4 1**


Solenoidal balance identity: π₁ · η₂ = 2 · ω₁.
The product of the first π-value and second η-value equals twice
the first ω-value, connecting all three solenoidal generators to ω.

---

### `Tau.Coordinates.solenoidal_half_normalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L336-L339)
**theorem
Tau.Coordinates.solenoidal_half_normalization :towerVal 1 1 * towerVal 3 2 / 2 = towerVal 4 1**


Solenoidal half-normalization: (π₁ · η₂) / 2 = ω₁.
This is the Nat division form: 22 / 2 = 11.

---

### `Tau.Coordinates.solenoidal_alpha_form`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L341-L346)
**theorem
Tau.Coordinates.solenoidal_alpha_form :(towerVal 1 1 * towerVal 3 2) ^ 2 * 225 = 4 * 121 * (towerVal 2 1 * towerVal 2 2) ^ 2**


The solenoidal balance form of α: (π₁ · η₂)² · 225 = 4 · 121 · (γ₁ · γ₂)².
Cross-multiplied identity encoding
((π₁ · η₂) / (2 · γ₁ · γ₂))² = 121/225 = (11/15)².

---

### `Tau.Coordinates.geometric_mean_departure_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L356-L358)
**theorem
Tau.Coordinates.geometric_mean_departure_1 :towerVal 1 1 * towerVal 3 1 = 10**


Geometric mean departure at n=1: π₁ · η₁ = 2 · 5 = 10 (vs γ₁² = 9).

---

### `Tau.Coordinates.geometric_mean_departure_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L360-L362)
**theorem
Tau.Coordinates.geometric_mean_departure_2 :towerVal 1 2 * towerVal 3 2 = 33**


Geometric mean departure at n=2: π₂ · η₂ = 3 · 11 = 33 (vs γ₂² = 25).

---

### `Tau.Coordinates.geometric_mean_departure_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L364-L366)
**theorem
Tau.Coordinates.geometric_mean_departure_3 :towerVal 1 3 * towerVal 3 3 = 155**


Geometric mean departure at n=3: π₃ · η₃ = 5 · 31 = 155 (vs γ₃² = 121).

---

### `Tau.Coordinates.gamma_1_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L368-L369)
**theorem
Tau.Coordinates.gamma_1_squared :towerVal 2 1 ^ 2 = 9**


γ₁² = 9, for comparison with π₁ · η₁ = 10.

---

### `Tau.Coordinates.gamma_2_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L371-L372)
**theorem
Tau.Coordinates.gamma_2_squared :towerVal 2 2 ^ 2 = 25**


γ₂² = 25, for comparison with π₂ · η₂ = 33.

---

### `Tau.Coordinates.gamma_3_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/IteratedPrime.lean#L374-L375)
**theorem
Tau.Coordinates.gamma_3_squared :towerVal 2 3 ^ 2 = 121**


γ₃² = 121, for comparison with π₃ · η₃ = 155.
