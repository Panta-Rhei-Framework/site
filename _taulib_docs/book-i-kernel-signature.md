---
layout: taulib-doc
title: "TauLib.BookI.Kernel.Signature"
permalink: /verify/taulib/docs/book-i-kernel-signature/
lane: verify
module_name: "TauLib.BookI.Kernel.Signature"
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

# TauLib.Kernel.Signature


The foundational signature of Category τ: five generators in strict total order,
and the sole primitive iterator ρ.

## Registry Cross-References


- [I.K0] Universe Postulate — implicit in Lean's type system (see below)

- [I.D01] Five Generators — `Generator` inductive type

- [I.D02] Progression Operator ρ — `rho` function

- [I.D04] Static Kernel τ₀ — `TauZero` structure


## Axiom K0: Universe Postulate


The zeroth axiom K0 postulates the existence of τ as a universe of discourse —
the ambient totality that contains all five generators and all orbit elements.
In Lean 4, K0 is realized by the type system itself:

`inductive Generator : Type` — declares the generator type exists
`structure TauObj : Type` — declares the object universe exists

K0 distinguishes τ (the ambient type/universe) from ω (the fixed-point element
*within* τ). τ is not an element of itself; ω is. τ is the Type; ω is a term.
This distinction is foundational: ω lives inside the system as an algebraic
citizen (the unique ρ-fixed point, K2), while τ is the ground that makes the
system possible.

## Mathematical Content


τ begins with exactly five generators in strict total order:
α < π < γ < η < ω

Each generator has a canonical role:


- α: radial seed (its orbit O_α becomes τ-Idx, the internal natural numbers)

- π: prime base / multiplicative spine

- γ: exponent / outer-power channel

- η: tetration / inner-power channel

- ω: fixed-point absorber / closure beacon


## Notation (2nd Edition)


The 1st Edition used π, π', π'' for the three solenoidal generators.
The 2nd Edition replaces π' → γ, π'' → η for cleaner typesetting and
robust Lean identifiers. The solenoidal triple is {π, γ, η}.

---

### `Tau.Kernel.Generator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L64-L73)
**inductive
Tau.Kernel.Generator :Type**


[I.D01] The five generators of Category τ.
These are the ONLY primitive objects. All other objects are orbit elements
produced by applying ρ to these generators.

- alpha : Generator
- pi : Generator
- gamma : Generator
- eta : Generator
- omega : Generator
Instances For

---

### `Tau.Kernel.instDecidableEqGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L73-L73)
**instance
Tau.Kernel.instDecidableEqGenerator :DecidableEq Generator**

Equations
- Tau.Kernel.instDecidableEqGenerator x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.Kernel.instReprGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L73-L73)
**def
Tau.Kernel.instReprGenerator.repr :Generator → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
- Tau.Kernel.instReprGenerator.repr Tau.Kernel.Generator.pi prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Kernel.Generator.pi")).group
 prec✝
- Tau.Kernel.instReprGenerator.repr Tau.Kernel.Generator.eta prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Kernel.Generator.eta")).group
 prec✝
Instances For

---

### `Tau.Kernel.instReprGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L73-L73)
**instance
Tau.Kernel.instReprGenerator :Repr Generator**

Equations
- Tau.Kernel.instReprGenerator = { reprPrec := Tau.Kernel.instReprGenerator.repr }

---

### `Tau.Kernel.Generator.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L77-L83)
**def
Tau.Kernel.Generator.toNat :Generator → Nat**


Canonical ordering index for generators: α=0, π=1, γ=2, η=3, ω=4.
Equations
- Tau.Kernel.Generator.alpha.toNat = 0
- Tau.Kernel.Generator.pi.toNat = 1
- Tau.Kernel.Generator.gamma.toNat = 2
- Tau.Kernel.Generator.eta.toNat = 3
- Tau.Kernel.Generator.omega.toNat = 4
Instances For

---

### `Tau.Kernel.instLTGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L85-L87)
**instance
Tau.Kernel.instLTGenerator :LT Generator**


[I.K1 prerequisite] Strict ordering on generators derived from their indices.
Equations
- Tau.Kernel.instLTGenerator = { lt := fun (a b : Tau.Kernel.Generator) => a.toNat < b.toNat }

---

### `Tau.Kernel.instDecidableLtGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L89-L91)
**instance
Tau.Kernel.instDecidableLtGenerator
(a b : Generator)
 :Decidable (a < b)**


The ordering on generators is decidable.
Equations
- Tau.Kernel.instDecidableLtGenerator a b = inferInstanceAs (Decidable (a.toNat < b.toNat))

---

### `Tau.Kernel.nonOmegaGenerators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L93-L94)
**def
Tau.Kernel.nonOmegaGenerators :List Generator**


[I.D01] The four non-omega generators that seed orbit rays.
Equations
- Tau.Kernel.nonOmegaGenerators = [Tau.Kernel.Generator.alpha, Tau.Kernel.Generator.pi, Tau.Kernel.Generator.gamma, Tau.Kernel.Generator.eta]
Instances For

---

### `Tau.Kernel.TauZero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Signature.lean#L96-L102)
**structure
Tau.Kernel.TauZero :Type**


[I.D04] The static kernel τ₀: the 5 generators before the generative act.
This is the complete specification — ρ has not yet been applied.

- generators : Fin 5 → Generator
The five generators are present

- canonical_order
(i j : Fin 5)
 : i < j → (self.generators i).toNat < (self.generators j).toNat
They are listed in canonical order

Instances For
