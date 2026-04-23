---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.PrimorialLadder"
permalink: /verify/taulib/docs/book-iii-spectral-primorial-ladder/
lane: verify
module_name: "TauLib.BookIII.Spectral.PrimorialLadder"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Spectral.PrimorialLadder


Primorial ladder as inverse system and primorial cofinality theorem.

## Registry Cross-References


- [III.D19] Primorial Ladder -- `PrimorialStage`, `primorial_ladder_check`

- [III.T09] Primorial Cofinality -- `cofinal_level`, `primorial_cofinal_check`


## Mathematical Content


**III.D19 (Primorial Ladder):** Primorial numbers Prim(k) = p₁·p₂·…·pₖ
form an inverse system ℤ/Prim(1)ℤ ← ℤ/Prim(2)ℤ ← …. The inverse limit
is the profinite completion Ẑ_τ. Canonical cofinal filtration.

**III.T09 (Primorial Cofinality):** The primorial tower is cofinal: every
ℤ/Nℤ maps to ℤ/Prim(k)ℤ for k large enough. Checking at primorial
levels is SUFFICIENT. The cutoff k₀ is always computable.

---

### `Tau.BookIII.Spectral.PrimorialStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L34-L40)
**structure
Tau.BookIII.Spectral.PrimorialStage :Type**


[III.D19] A stage in the primorial ladder:
the inverse system ℤ/Prim(1)ℤ ← ℤ/Prim(2)ℤ ← …

- depth : Denotation.TauIdx
- modulus : Denotation.TauIdx
- value : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Spectral.instReprPrimorialStage.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L40-L40)
**def
Tau.BookIII.Spectral.instReprPrimorialStage.repr :PrimorialStage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instReprPrimorialStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L40-L40)
**instance
Tau.BookIII.Spectral.instReprPrimorialStage :Repr PrimorialStage**

Equations
- Tau.BookIII.Spectral.instReprPrimorialStage = { reprPrec := Tau.BookIII.Spectral.instReprPrimorialStage.repr }

---

### `Tau.BookIII.Spectral.instDecidableEqPrimorialStage.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L40-L40)
**def
Tau.BookIII.Spectral.instDecidableEqPrimorialStage.decEq
(x✝ x✝¹ : PrimorialStage)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instDecidableEqPrimorialStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L40-L40)
**instance
Tau.BookIII.Spectral.instDecidableEqPrimorialStage :DecidableEq PrimorialStage**

Equations
- Tau.BookIII.Spectral.instDecidableEqPrimorialStage = Tau.BookIII.Spectral.instDecidableEqPrimorialStage.decEq

---

### `Tau.BookIII.Spectral.instBEqPrimorialStage.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L40-L40)
**def
Tau.BookIII.Spectral.instBEqPrimorialStage.beq :PrimorialStage → PrimorialStage → Bool**

Equations
- Tau.BookIII.Spectral.instBEqPrimorialStage.beq { depth := a, modulus := a_1, value := a_2 }
 { depth := b, modulus := b_1, value := b_2 } = (a == b && (a_1 == b_1 && a_2 == b_2))
- Tau.BookIII.Spectral.instBEqPrimorialStage.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Spectral.instBEqPrimorialStage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L40-L40)
**instance
Tau.BookIII.Spectral.instBEqPrimorialStage :BEq PrimorialStage**

Equations
- Tau.BookIII.Spectral.instBEqPrimorialStage = { beq := Tau.BookIII.Spectral.instBEqPrimorialStage.beq }

---

### `Tau.BookIII.Spectral.primorial_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L42-L44)
**def
Tau.BookIII.Spectral.primorial_stage
(x k : Denotation.TauIdx)
 :PrimorialStage**


[III.D19] Build a primorial stage from a value and depth.
Equations
- Tau.BookIII.Spectral.primorial_stage x k = { depth := k, modulus := Tau.Polarity.primorial k, value := Tau.Polarity.reduce x k }
Instances For

---

### `Tau.BookIII.Spectral.primorial_ladder_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L46-L60)
**def
Tau.BookIII.Spectral.primorial_ladder_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D19] Primorial ladder check: the inverse system property.
For each k ≤ bound: reduce(reduce(x, k+1), k) = reduce(x, k).
Equations
- Tau.BookIII.Spectral.primorial_ladder_check bound = Tau.BookIII.Spectral.primorial_ladder_check.go bound 0 1 (bound * (bound + 1))
Instances For

---

### `Tau.BookIII.Spectral.primorial_ladder_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L51-L59)@[irreducible]

**def
Tau.BookIII.Spectral.primorial_ladder_check.go
(bound : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.primorial_divisibility_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L62-L73)
**def
Tau.BookIII.Spectral.primorial_divisibility_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D19] Primorial divisibility: Prim(k) | Prim(k+1) for all k ≥ 1.
Equations
- Tau.BookIII.Spectral.primorial_divisibility_check bound = Tau.BookIII.Spectral.primorial_divisibility_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.primorial_divisibility_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L66-L72)@[irreducible]

**def
Tau.BookIII.Spectral.primorial_divisibility_check.go
(bound : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.primorial_growth_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L75-L84)
**def
Tau.BookIII.Spectral.primorial_growth_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D19] Primorial growth: Prim(k+1) > Prim(k) (strictly increasing).
Equations
- Tau.BookIII.Spectral.primorial_growth_check bound = Tau.BookIII.Spectral.primorial_growth_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.primorial_growth_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L79-L83)@[irreducible]

**def
Tau.BookIII.Spectral.primorial_growth_check.go
(bound : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.cofinal_level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L90-L98)
**def
Tau.BookIII.Spectral.cofinal_level
(n : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.T09] Find the smallest primorial level k such that Prim(k) ≥ n.
Equations
- Tau.BookIII.Spectral.cofinal_level n = Tau.BookIII.Spectral.cofinal_level.go n 0 (n + 1)
Instances For

---

### `Tau.BookIII.Spectral.cofinal_level.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L94-L97)@[irreducible]

**def
Tau.BookIII.Spectral.cofinal_level.go
(n : Denotation.TauIdx)

(k fuel : ℕ)
 :Denotation.TauIdx**

Equations
- Tau.BookIII.Spectral.cofinal_level.go n k fuel = if fuel = 0 then k
 else if Tau.Polarity.primorial k ≥ n then k else Tau.BookIII.Spectral.cofinal_level.go n (k + 1) (fuel - 1)
Instances For

---

### `Tau.BookIII.Spectral.primorial_cofinal_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L100-L111)
**def
Tau.BookIII.Spectral.primorial_cofinal_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T09] Primorial cofinality: for each N ≤ bound, there exists k
such that Prim(k) ≥ N. Checking at primorial levels is sufficient.
Equations
- Tau.BookIII.Spectral.primorial_cofinal_check bound = Tau.BookIII.Spectral.primorial_cofinal_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.primorial_cofinal_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L105-L110)@[irreducible]

**def
Tau.BookIII.Spectral.primorial_cofinal_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.prime_cofinal_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L113-L128)
**def
Tau.BookIII.Spectral.prime_cofinal_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T09] Cofinality for prime moduli: for each prime p ≤ bound,
p | Prim(k) for some k.
Equations
- Tau.BookIII.Spectral.prime_cofinal_check bound = Tau.BookIII.Spectral.prime_cofinal_check.go bound 1 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.prime_cofinal_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L118-L127)@[irreducible]

**def
Tau.BookIII.Spectral.prime_cofinal_check.go
(bound : Denotation.TauIdx)

(i fuel _dummy : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.primorial_ladder_8`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L154-L155)
**theorem
Tau.BookIII.Spectral.primorial_ladder_8 :primorial_ladder_check 8 = true**


---

### `Tau.BookIII.Spectral.primorial_div_6`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L158-L159)
**theorem
Tau.BookIII.Spectral.primorial_div_6 :primorial_divisibility_check 6 = true**


---

### `Tau.BookIII.Spectral.primorial_growth_6`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L162-L163)
**theorem
Tau.BookIII.Spectral.primorial_growth_6 :primorial_growth_check 6 = true**


---

### `Tau.BookIII.Spectral.primorial_cofinal_50`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L166-L167)
**theorem
Tau.BookIII.Spectral.primorial_cofinal_50 :primorial_cofinal_check 50 = true**


---

### `Tau.BookIII.Spectral.prime_cofinal_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L170-L171)
**theorem
Tau.BookIII.Spectral.prime_cofinal_30 :prime_cofinal_check 30 = true**


---

### `Tau.BookIII.Spectral.primorial_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L177-L178)
**theorem
Tau.BookIII.Spectral.primorial_zero :Polarity.primorial 0 = 1**


[III.D19] Structural: primorial 0 = 1 (empty product).

---

### `Tau.BookIII.Spectral.primorial_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L180-L181)
**theorem
Tau.BookIII.Spectral.primorial_one :Polarity.primorial 1 = 2**


[III.D19] Structural: primorial 1 = 2.

---

### `Tau.BookIII.Spectral.primorial_three`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L183-L184)
**theorem
Tau.BookIII.Spectral.primorial_three :Polarity.primorial 3 = 30**


[III.D19] Structural: primorial 3 = 30 = 2·3·5.

---

### `Tau.BookIII.Spectral.cofinal_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L186-L187)
**theorem
Tau.BookIII.Spectral.cofinal_30 :cofinal_level 30 = 3**


[III.T09] Structural: cofinal level of 30 is 3.

---

### `Tau.BookIII.Spectral.reduce_coherence_42`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/PrimorialLadder.lean#L189-L191)
**theorem
Tau.BookIII.Spectral.reduce_coherence_42 :Polarity.reduce (Polarity.reduce 42 4) 3 = Polarity.reduce 42 3**


[III.D19] Structural: reduce coherence at specific values.
