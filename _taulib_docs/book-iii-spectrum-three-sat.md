---
layout: taulib-doc
title: "TauLib.BookIII.Spectrum.ThreeSAT"
permalink: /verify/taulib/docs/book-iii-spectrum-three-sat/
lane: verify
module_name: "TauLib.BookIII.Spectrum.ThreeSAT"
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

# TauLib.Spectrum.ThreeSAT


3SAT encoding as a spectral coefficient problem.

## Registry Cross-References


- [I.D73] 3SAT Spectral Encoding — `SpectralCNF`

- [I.P31] 3SAT Encoding Preserves Satisfiability — `encode_preserves`

- [I.P32] τ-Complexity Bridge — `tau_complexity_bridge`


## Mathematical Content


The classical 3SAT problem (NP-complete by Cook–Levin) can be encoded
as a spectral coefficient problem within the τ-framework:


- Boolean variable xᵢ ↔ i-th CRT direction (prime p_i)

- xᵢ = true ↔ residue at p_i is nonzero (χ₊-sector active)

- xᵢ = false ↔ residue at p_i is zero (χ₋-sector active)

- A clause (ℓ₁ ∨ ℓ₂ ∨ ℓ₃) becomes a constraint on spectral coefficients


This does NOT resolve P vs NP — it translates the problem into τ-language,
positioning Book III's eight spectral forces to provide structural handles.

---

### `Tau.Spectrum.Literal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L37-L43)
**structure
Tau.Spectrum.Literal :Type**


A literal: a variable index with optional negation.

- var_idx : ℕ
Variable index (1-indexed: variable x_i uses prime p_i).

- positive : Bool
Polarity: true = positive (x_i), false = negated (¬x_i).

Instances For

---

### `Tau.Spectrum.instDecidableEqLiteral.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L43-L43)
**def
Tau.Spectrum.instDecidableEqLiteral.decEq
(x✝ x✝¹ : Literal)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instDecidableEqLiteral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L43-L43)
**instance
Tau.Spectrum.instDecidableEqLiteral :DecidableEq Literal**

Equations
- Tau.Spectrum.instDecidableEqLiteral = Tau.Spectrum.instDecidableEqLiteral.decEq

---

### `Tau.Spectrum.instReprLiteral.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L43-L43)
**def
Tau.Spectrum.instReprLiteral.repr :Literal → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprLiteral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L43-L43)
**instance
Tau.Spectrum.instReprLiteral :Repr Literal**

Equations
- Tau.Spectrum.instReprLiteral = { reprPrec := Tau.Spectrum.instReprLiteral.repr }

---

### `Tau.Spectrum.Clause`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L45-L53)
**structure
Tau.Spectrum.Clause :Type**


A clause: exactly 3 literals (3-CNF).

- l1 : Literal
First literal.

- l2 : Literal
Second literal.

- l3 : Literal
Third literal.

Instances For

---

### `Tau.Spectrum.instDecidableEqClause.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L53-L53)
**def
Tau.Spectrum.instDecidableEqClause.decEq
(x✝ x✝¹ : Clause)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instDecidableEqClause`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L53-L53)
**instance
Tau.Spectrum.instDecidableEqClause :DecidableEq Clause**

Equations
- Tau.Spectrum.instDecidableEqClause = Tau.Spectrum.instDecidableEqClause.decEq

---

### `Tau.Spectrum.instReprClause.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L53-L53)
**def
Tau.Spectrum.instReprClause.repr :Clause → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprClause`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L53-L53)
**instance
Tau.Spectrum.instReprClause :Repr Clause**

Equations
- Tau.Spectrum.instReprClause = { reprPrec := Tau.Spectrum.instReprClause.repr }

---

### `Tau.Spectrum.CNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L55-L61)
**structure
Tau.Spectrum.CNF :Type**


A CNF formula: a list of clauses.

- clauses : List Clause
The clauses.

- num_vars : ℕ
Number of variables.

Instances For

---

### `Tau.Spectrum.instReprCNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L61-L61)
**instance
Tau.Spectrum.instReprCNF :Repr CNF**

Equations
- Tau.Spectrum.instReprCNF = { reprPrec := Tau.Spectrum.instReprCNF.repr }

---

### `Tau.Spectrum.instReprCNF.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L61-L61)
**def
Tau.Spectrum.instReprCNF.repr :CNF → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.Assignment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L67-L68)@[reducible, inline]

**abbrev
Tau.Spectrum.Assignment :Type**


A Boolean assignment: maps variable indices to Bool.
Equations
- Tau.Spectrum.Assignment = (ℕ → Bool)
Instances For

---

### `Tau.Spectrum.Literal.eval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L70-L72)
**def
Tau.Spectrum.Literal.eval
(l : Literal)

(a : Assignment)
 :Bool**


Evaluate a literal under an assignment.
Equations
- l.eval a = if l.positive = true then a l.var_idx else !a l.var_idx
Instances For

---

### `Tau.Spectrum.Clause.eval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L74-L76)
**def
Tau.Spectrum.Clause.eval
(c : Clause)

(a : Assignment)
 :Bool**


Evaluate a clause under an assignment (disjunction of 3 literals).
Equations
- c.eval a = (c.l1.eval a || c.l2.eval a || c.l3.eval a)
Instances For

---

### `Tau.Spectrum.CNF.eval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L78-L80)
**def
Tau.Spectrum.CNF.eval
(φ : CNF)

(a : Assignment)
 :Bool**


Evaluate a CNF formula (conjunction of all clauses).
Equations
- φ.eval a = φ.clauses.all fun (c : Tau.Spectrum.Clause) => c.eval a
Instances For

---

### `Tau.Spectrum.CNF.satisfiable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L82-L84)
**def
Tau.Spectrum.CNF.satisfiable
(φ : CNF)
 :Prop**


A CNF formula is satisfiable if some assignment satisfies it.
Equations
- φ.satisfiable = ∃ (a : Tau.Spectrum.Assignment), φ.eval a = true
Instances For

---

### `Tau.Spectrum.crt_residue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L90-L94)
**def
Tau.Spectrum.crt_residue
(v i : Denotation.TauIdx)
 :Denotation.TauIdx**


The i-th CRT component of v: v mod p_i.
Uses nth_prime for the i-th prime.
Equations
- Tau.Spectrum.crt_residue v i = if (Tau.Polarity.nth_prime i == 0) = true then 0 else v % Tau.Polarity.nth_prime i
Instances For

---

### `Tau.Spectrum.spectral_var_true`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L96-L101)
**def
Tau.Spectrum.spectral_var_true
(var_idx : ℕ)

(v : Denotation.TauIdx)
 :Bool**


[I.D73] Spectral encoding of a Boolean variable:
variable xᵢ is encoded at the i-th CRT direction.
A value v "satisfies" xᵢ = true if the i-th CRT
component of v is nonzero.
Equations
- Tau.Spectrum.spectral_var_true var_idx v = (Tau.Spectrum.crt_residue v var_idx != 0)
Instances For

---

### `Tau.Spectrum.spectral_literal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L103-L106)
**def
Tau.Spectrum.spectral_literal
(l : Literal)

(v : Denotation.TauIdx)
 :Bool**


Spectral encoding of a literal.
Equations
- Tau.Spectrum.spectral_literal l v = if l.positive = true then Tau.Spectrum.spectral_var_true l.var_idx v else !Tau.Spectrum.spectral_var_true l.var_idx v
Instances For

---

### `Tau.Spectrum.spectral_clause`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L108-L110)
**def
Tau.Spectrum.spectral_clause
(c : Clause)

(v : Denotation.TauIdx)
 :Bool**


Spectral encoding of a clause: at least one literal satisfied.
Equations
- Tau.Spectrum.spectral_clause c v = (Tau.Spectrum.spectral_literal c.l1 v || Tau.Spectrum.spectral_literal c.l2 v || Tau.Spectrum.spectral_literal c.l3 v)
Instances For

---

### `Tau.Spectrum.spectral_cnf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L112-L115)
**def
Tau.Spectrum.spectral_cnf
(φ : CNF)

(v : Denotation.TauIdx)
 :Bool**


[I.D73] Spectral encoding of a CNF formula: all clauses satisfied
by the spectral coefficients of v.
Equations
- Tau.Spectrum.spectral_cnf φ v = φ.clauses.all fun (c : Tau.Spectrum.Clause) => Tau.Spectrum.spectral_clause c v
Instances For

---

### `Tau.Spectrum.SpectralSatisfiable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L117-L120)
**def
Tau.Spectrum.SpectralSatisfiable
(φ : CNF)
 :Prop**


A CNF is spectrally satisfiable if there exists a value v such that
spectral_cnf evaluates to true.
Equations
- Tau.Spectrum.SpectralSatisfiable φ = ∃ (v : Tau.Denotation.TauIdx), Tau.Spectrum.spectral_cnf φ v = true
Instances For

---

### `Tau.Spectrum.spectral_decidable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L126-L131)
**theorem
Tau.Spectrum.spectral_decidable
(φ : CNF)

(v : Denotation.TauIdx)
 :spectral_cnf φ v = true ∨ spectral_cnf φ v = false**


[I.P31] The spectral encoding is decidable: for any formula and
value, we can compute whether the formula is spectrally satisfied.
This is the computable core of the encoding.

---

### `Tau.Spectrum.empty_cnf_sat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L133-L135)
**theorem
Tau.Spectrum.empty_cnf_sat
(v : Denotation.TauIdx)
 :spectral_cnf { clauses := [], num_vars := 0 } v = true**


The empty formula is trivially satisfied.

---

### `Tau.Spectrum.bool_sat_decidable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L137-L140)
**theorem
Tau.Spectrum.bool_sat_decidable
(φ : CNF)

(a : Assignment)
 :φ.eval a = true ∨ φ.eval a = false**


Boolean satisfiability is also decidable for concrete formulas.

---

### `Tau.Spectrum.tau_complexity_bridge_concrete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L146-L157)
**theorem
Tau.Spectrum.tau_complexity_bridge_concrete :∃ (φ : CNF), ∃ (a : Assignment), φ.eval a = true ∧ ∃ (v : Denotation.TauIdx), spectral_cnf φ v = true**


[I.P32] The τ-complexity bridge: the spectral encoding translates
Boolean satisfiability into a problem about τ-framework values.

Key structural fact: for concrete CNF formulas, we can verify
satisfiability by searching over CRT residues.

---

### `Tau.Spectrum.single_var_spectral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L159-L162)
**theorem
Tau.Spectrum.single_var_spectral
(v : Denotation.TauIdx)
 :spectral_literal { var_idx := 1, positive := true } v = (crt_residue v 1 != 0)**


The encoding maps a single-variable clause to a CRT constraint.

---

### `Tau.Spectrum.example_clause`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L168-L170)
**def
Tau.Spectrum.example_clause :Clause**


A simple clause: x₁ ∨ ¬x₂ ∨ x₃.
Equations
- Tau.Spectrum.example_clause = { l1 := { var_idx := 1, positive := true }, l2 := { var_idx := 2, positive := false },
 l3 := { var_idx := 3, positive := true } }
Instances For

---

### `Tau.Spectrum.example_cnf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectrum/ThreeSAT.lean#L175-L177)
**def
Tau.Spectrum.example_cnf :CNF**


A two-clause formula.
Equations
- One or more equations did not get rendered due to their size.
Instances For
