---
layout: taulib-doc
title: "TauLib.BookI.Denotation.ProgramMonoid"
permalink: /verify/taulib/docs/book-i-denotation-program-monoid/
lane: verify
module_name: "TauLib.BookI.Denotation.ProgramMonoid"
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

# TauLib.Denotation.ProgramMonoid


The program monoid: instruction sequences, normal forms, and composition.

## Registry Cross-References


- [I.D14] Instruction Set — `Instruction`, `Program`

- [I.L02] Normal Form Confluence — `normalize_compose`

- [I.T03] Program Monoid — `compose_assoc`, `compose_id`


## Mathematical Content


Programs are finite sequences of two instruction types:


- `rho_inst`: apply ρ (increments depth for non-omega objects)

- `sigma_inst g h`: swap seeds g and h


Every program's effect on a TauObj is completely determined by:

- The net seed permutation (composition of all sigma swaps)

- The total rho count (number of rho_inst instructions)


This yields a normal form, and NF-equivalence is decidable.
The program monoid is the quotient by NF-equivalence.

---

### `Tau.Denotation.Instruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L36-L40)
**inductive
Tau.Denotation.Instruction :Type**


[I.D14] The two instruction types.

- rho_inst : Instruction
- sigma_inst : Kernel.Generator → Kernel.Generator → Instruction
Instances For

---

### `Tau.Denotation.instDecidableEqInstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L40-L40)
**instance
Tau.Denotation.instDecidableEqInstruction :DecidableEq Instruction**

Equations
- Tau.Denotation.instDecidableEqInstruction = Tau.Denotation.instDecidableEqInstruction.decEq

---

### `Tau.Denotation.instDecidableEqInstruction.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L40-L40)
**def
Tau.Denotation.instDecidableEqInstruction.decEq
(x✝ x✝¹ : Instruction)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
- Tau.Denotation.instDecidableEqInstruction.decEq Tau.Denotation.Instruction.rho_inst
 Tau.Denotation.Instruction.rho_inst = isTrue ⋯
- Tau.Denotation.instDecidableEqInstruction.decEq Tau.Denotation.Instruction.rho_inst
 (Tau.Denotation.Instruction.sigma_inst a a_1) = isFalse ⋯
- Tau.Denotation.instDecidableEqInstruction.decEq (Tau.Denotation.Instruction.sigma_inst a a_1)
 Tau.Denotation.Instruction.rho_inst = isFalse ⋯
Instances For

---

### `Tau.Denotation.instReprInstruction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L40-L40)
**def
Tau.Denotation.instReprInstruction.repr :Instruction → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Denotation.instReprInstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L40-L40)
**instance
Tau.Denotation.instReprInstruction :Repr Instruction**

Equations
- Tau.Denotation.instReprInstruction = { reprPrec := Tau.Denotation.instReprInstruction.repr }

---

### `Tau.Denotation.Program`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L42-L43)@[reducible, inline]

**abbrev
Tau.Denotation.Program :Type**


A program is a finite sequence of instructions.
Equations
- Tau.Denotation.Program = List Tau.Denotation.Instruction
Instances For

---

### `Tau.Denotation.execInstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L45-L49)
**def
Tau.Denotation.execInstruction
(i : Instruction)

(x : Kernel.TauObj)
 :Kernel.TauObj**


Execute a single instruction on a TauObj.
Equations
- Tau.Denotation.execInstruction Tau.Denotation.Instruction.rho_inst x = Tau.Kernel.rho x
- Tau.Denotation.execInstruction (Tau.Denotation.Instruction.sigma_inst a a_1) x = Tau.Denotation.sigma a a_1 x
Instances For

---

### `Tau.Denotation.execProgram`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L51-L53)
**def
Tau.Denotation.execProgram
(p : Program)

(x : Kernel.TauObj)
 :Kernel.TauObj**


Execute a program (left-to-right: first instruction applied first).
Equations
- Tau.Denotation.execProgram p x = List.foldl (fun (acc : Tau.Kernel.TauObj) (i : Tau.Denotation.Instruction) => Tau.Denotation.execInstruction i acc) x
 p
Instances For

---

### `Tau.Denotation.NormalForm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L59-L62)
**structure
Tau.Denotation.NormalForm :Type**


A program normal form: net seed permutation function + rho count.

- seedMap : Kernel.Generator → Kernel.Generator
- rhoCount : Nat
Instances For

---

### `Tau.Denotation.countRho`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L64-L68)
**def
Tau.Denotation.countRho :Program → Nat**


Count the number of rho instructions in a program.
Equations
- Tau.Denotation.countRho [] = 0
- Tau.Denotation.countRho (Tau.Denotation.Instruction.rho_inst :: rest) = 1 + Tau.Denotation.countRho rest
- Tau.Denotation.countRho (Tau.Denotation.Instruction.sigma_inst a a_1 :: rest) = Tau.Denotation.countRho rest
Instances For

---

### `Tau.Denotation.NormalForm.id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L70-L73)
**def
Tau.Denotation.NormalForm.id :NormalForm**


The identity normal form.
Equations
- Tau.Denotation.NormalForm.id = { seedMap := fun (g : Tau.Kernel.Generator) => g, rhoCount := 0 }
Instances For

---

### `Tau.Denotation.NormalForm.compose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L75-L78)
**def
Tau.Denotation.NormalForm.compose
(nf1 nf2 : NormalForm)
 :NormalForm**


Compose two normal forms.
Equations
- nf1.compose nf2 = { seedMap := fun (g : Tau.Kernel.Generator) => nf2.seedMap (nf1.seedMap g), rhoCount := nf1.rhoCount + nf2.rhoCount }
Instances For

---

### `Tau.Denotation.execNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L80-L83)
**def
Tau.Denotation.execNF
(nf : NormalForm)

(x : Kernel.TauObj)
 :Kernel.TauObj**


Execute a normal form on a TauObj (simplified: just apply rho count times).
Equations
- Tau.Denotation.execNF nf x = Tau.Orbit.iter_rho nf.rhoCount { seed := nf.seedMap x.seed, depth := x.depth }
Instances For

---

### `Tau.Denotation.Program.compose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L89-L90)
**def
Tau.Denotation.Program.compose
(p q : Program)
 :Program**


Program composition is concatenation.
Equations
- p.compose q = p ++ q
Instances For

---

### `Tau.Denotation.compose_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L92-L95)
**theorem
Tau.Denotation.compose_assoc
(p q r : Program)
 :(p.compose q).compose r = p.compose (q.compose r)**


[I.T03] Composition is associative.

---

### `Tau.Denotation.compose_id_left`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L97-L100)
**theorem
Tau.Denotation.compose_id_left
(p : Program)
 :Program.compose [] p = p**


The empty program is a left identity.

---

### `Tau.Denotation.compose_id_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L102-L105)
**theorem
Tau.Denotation.compose_id_right
(p : Program)
 :p.compose [] = p**


The empty program is a right identity.

---

### `Tau.Denotation.exec_compose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L111-L114)
**theorem
Tau.Denotation.exec_compose
(p q : Program)

(x : Kernel.TauObj)
 :execProgram (p.compose q) x = execProgram q (execProgram p x)**


Executing a concatenation is the same as executing sequentially.

---

### `Tau.Denotation.exec_nil`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L116-L118)
**theorem
Tau.Denotation.exec_nil
(x : Kernel.TauObj)
 :execProgram [] x = x**


The empty program is the identity.

---

### `Tau.Denotation.exec_rho`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L120-L123)
**theorem
Tau.Denotation.exec_rho
(x : Kernel.TauObj)
 :execProgram [Instruction.rho_inst] x = Kernel.rho x**


A single rho instruction applies rho.

---

### `Tau.Denotation.exec_sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L125-L128)
**theorem
Tau.Denotation.exec_sigma
(s t : Kernel.Generator)

(x : Kernel.TauObj)
 :execProgram [Instruction.sigma_inst s t] x = sigma s t x**


A single sigma instruction applies sigma.

---

### `Tau.Denotation.rho_count_compose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L134-L149)
**theorem
Tau.Denotation.rho_count_compose
(p q : Program)
 :countRho (p.compose q) = countRho p + countRho q**


[I.L02] Normal form confluence: the rho count of a composed program
is the sum of the individual rho counts.

---

### `Tau.Denotation.rho_count_nil`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/ProgramMonoid.lean#L151-L152)
**theorem
Tau.Denotation.rho_count_nil :countRho [] = 0**


The rho count of the empty program is 0.
