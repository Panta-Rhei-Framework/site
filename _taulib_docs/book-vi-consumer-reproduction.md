---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.Reproduction"
permalink: /verify/taulib/docs/book-vi-consumer-reproduction/
lane: verify
module_name: "TauLib.BookVI.Consumer.Reproduction"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.Consumer.Reproduction


Sexual reproduction: recombination functor and the second distinction.

## Registry Cross-References


- [VI.D49] Recombination Functor — `RecombinationFunctor`

- [VI.T26] Sex as Second Distinction — `sex_is_second_distinction`


## Cross-Book Authority


- Book II, Part III: lemniscate 𝕃 = S¹ ∨ S¹ (gamete channels via two lobes)

- Book II, Part II: τ³ fibration (haploid/diploid cycling on fiber T²)


## Ground Truth Sources


- Book VI Chapter 36 (2nd Edition): Sexual Reproduction


---

### `Tau.BookVI.Reproduction.RecombinationFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L30-L47)
**structure
Tau.BookVI.Reproduction.RecombinationFunctor :Type**


[VI.D49] Recombination Functor: binary input, stochastic output.
Gamete fusion: two haploid inputs → one diploid output.
The two lemniscate lobes (Book II, Part III) provide
two independent channels for gamete production.

- input_arity : ℕ
Number of inputs (gametes).

- arity_eq : self.input_arity = 2
Binary: exactly 2 inputs.

- haploid_fusion : Bool
Haploid fusion produces diploid.

- stochastic : Bool
Crossover is stochastic.

- channels : ℕ
Number of gamete channels (= lemniscate lobes).

- channels_eq : self.channels = 2
Exactly 2 channels.

Instances For

---

### `Tau.BookVI.Reproduction.instReprRecombinationFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L47-L47)
**instance
Tau.BookVI.Reproduction.instReprRecombinationFunctor :Repr RecombinationFunctor**

Equations
- Tau.BookVI.Reproduction.instReprRecombinationFunctor = { reprPrec := Tau.BookVI.Reproduction.instReprRecombinationFunctor.repr }

---

### `Tau.BookVI.Reproduction.instReprRecombinationFunctor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L47-L47)
**def
Tau.BookVI.Reproduction.instReprRecombinationFunctor.repr :RecombinationFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Reproduction.recomb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L49-L53)
**def
Tau.BookVI.Reproduction.recomb :RecombinationFunctor**

Equations
- Tau.BookVI.Reproduction.recomb = { input_arity := 2, arity_eq := Tau.BookVI.Reproduction.recomb._proof_1, channels := 2,
 channels_eq := Tau.BookVI.Reproduction.recomb._proof_1 }
Instances For

---

### `Tau.BookVI.Reproduction.recombination_is_functor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L55-L60)
**theorem
Tau.BookVI.Reproduction.recombination_is_functor :recomb.input_arity = 2 ∧ recomb.haploid_fusion = true ∧ recomb.stochastic = true ∧ recomb.channels = 2**


---

### `Tau.BookVI.Reproduction.SecondDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L66-L79)
**structure
Tau.BookVI.Reproduction.SecondDistinction :Type**


[VI.T26] Sex as Second Distinction.
Life's first distinction (VI.D04): self vs non-self.
Sex introduces a second: self vs other-self.
This is a refinement (level 1) of the base distinction.

- first : String
First distinction: self vs non-self (VI.D04).

- second : String
Second distinction: self vs other-self.

- refinement_level : ℕ
Refinement level (0 = base, 1 = first refinement).

- level_eq : self.refinement_level = 1
Exactly level 1.

Instances For

---

### `Tau.BookVI.Reproduction.instReprSecondDistinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L79-L79)
**instance
Tau.BookVI.Reproduction.instReprSecondDistinction :Repr SecondDistinction**

Equations
- Tau.BookVI.Reproduction.instReprSecondDistinction = { reprPrec := Tau.BookVI.Reproduction.instReprSecondDistinction.repr }

---

### `Tau.BookVI.Reproduction.instReprSecondDistinction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L79-L79)
**def
Tau.BookVI.Reproduction.instReprSecondDistinction.repr :SecondDistinction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Reproduction.second_dist`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L81-L83)
**def
Tau.BookVI.Reproduction.second_dist :SecondDistinction**

Equations
- Tau.BookVI.Reproduction.second_dist = { refinement_level := 1, level_eq := Tau.BookVI.Reproduction.second_dist._proof_1 }
Instances For

---

### `Tau.BookVI.Reproduction.sex_is_second_distinction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Reproduction.lean#L85-L89)
**theorem
Tau.BookVI.Reproduction.sex_is_second_distinction :second_dist.refinement_level = 1 ∧ second_dist.first = "self_nonself" ∧ second_dist.second = "self_otherself"**
