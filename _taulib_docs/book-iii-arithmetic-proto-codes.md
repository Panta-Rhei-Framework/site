---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.ProtoCodes"
permalink: /verify/taulib/docs/book-iii-arithmetic-proto-codes/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.ProtoCodes"
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

# TauLib.BookIII.Arithmetic.ProtoCodes


Proto-Code, BSD Functional, and Bridgehead Proposition.

## Registry Cross-References


- [III.D61] Proto-Code -- `ProtoCode`, `proto_code_check`

- [III.D62] BSD Functional -- `bsd_functional`, `bsd_functional_check`

- [III.P26] Bridgehead Proposition -- `bridgehead_check`


## Mathematical Content


**III.D61 (Proto-Code):** E₁ object with discrete carrier, self-verification,
but no decoder. Necessary but not sufficient for computation. A proto-code
has BNF components and carries rank information, but cannot decode itself.

**III.D62 (BSD Functional):** BSD_τ(k) = rank(k) · L'_τ(1,k). Measures
proto-code density at each primorial level. The L-value derivative at s=1
is approximated by the defect functional ratio.

**III.P26 (Bridgehead Proposition):** Proto-codes provide the necessary
ingredient for E₂ emergence. Non-trivial iff rank > 0.

---

### `Tau.BookIII.Arithmetic.ProtoCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L40-L47)
**structure
Tau.BookIII.Arithmetic.ProtoCode :Type**


[III.D61] Proto-code: E₁ object with discrete carrier and self-verification
but no decoder. Has BNF + gauge data but cannot self-modify.

- address : Denotation.TauIdx
- depth : Denotation.TauIdx
- rank : Denotation.TauIdx
- verified : Bool
Instances For

---

### `Tau.BookIII.Arithmetic.instReprProtoCode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L47-L47)
**def
Tau.BookIII.Arithmetic.instReprProtoCode.repr :ProtoCode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.instReprProtoCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L47-L47)
**instance
Tau.BookIII.Arithmetic.instReprProtoCode :Repr ProtoCode**

Equations
- Tau.BookIII.Arithmetic.instReprProtoCode = { reprPrec := Tau.BookIII.Arithmetic.instReprProtoCode.repr }

---

### `Tau.BookIII.Arithmetic.instDecidableEqProtoCode.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L47-L47)
**def
Tau.BookIII.Arithmetic.instDecidableEqProtoCode.decEq
(x✝ x✝¹ : ProtoCode)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.instDecidableEqProtoCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L47-L47)
**instance
Tau.BookIII.Arithmetic.instDecidableEqProtoCode :DecidableEq ProtoCode**

Equations
- Tau.BookIII.Arithmetic.instDecidableEqProtoCode = Tau.BookIII.Arithmetic.instDecidableEqProtoCode.decEq

---

### `Tau.BookIII.Arithmetic.instBEqProtoCode.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L47-L47)
**def
Tau.BookIII.Arithmetic.instBEqProtoCode.beq :ProtoCode → ProtoCode → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Arithmetic.instBEqProtoCode.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Arithmetic.instBEqProtoCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L47-L47)
**instance
Tau.BookIII.Arithmetic.instBEqProtoCode :BEq ProtoCode**

Equations
- Tau.BookIII.Arithmetic.instBEqProtoCode = { beq := Tau.BookIII.Arithmetic.instBEqProtoCode.beq }

---

### `Tau.BookIII.Arithmetic.make_proto_code`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L49-L59)
**def
Tau.BookIII.Arithmetic.make_proto_code
(x k : Denotation.TauIdx)
 :ProtoCode**


[III.D61] Construct a proto-code from address and depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.proto_code_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L61-L77)
**def
Tau.BookIII.Arithmetic.proto_code_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D61] Proto-code check: all proto-codes are well-formed and
self-verifying.
Equations
- Tau.BookIII.Arithmetic.proto_code_check bound db = Tau.BookIII.Arithmetic.proto_code_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.proto_code_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L66-L76)@[irreducible]

**def
Tau.BookIII.Arithmetic.proto_code_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_functional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L83-L103)
**def
Tau.BookIII.Arithmetic.bsd_functional
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D62] BSD functional: BSD_τ(k) = rank_count(k) · derivative_approx(k).
rank_count = number of distinct ranks at level k.
derivative_approx = difference of split-zeta products.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_functional.count_ranks`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L98-L103)@[irreducible]

**def
Tau.BookIII.Arithmetic.bsd_functional.count_ranks
(x pk k acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_functional_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L105-L119)
**def
Tau.BookIII.Arithmetic.bsd_functional_check
(db : Denotation.TauIdx)
 :Bool**


[III.D62] BSD functional check: the functional is well-defined and
non-negative at each level.
Equations
- Tau.BookIII.Arithmetic.bsd_functional_check db = Tau.BookIII.Arithmetic.bsd_functional_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.bsd_functional_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L110-L118)@[irreducible]

**def
Tau.BookIII.Arithmetic.bsd_functional_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bridgehead_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L125-L146)
**def
Tau.BookIII.Arithmetic.bridgehead_check
(db : Denotation.TauIdx)
 :Bool**


[III.P26] Bridgehead: proto-codes are non-trivial (rank > 0 somewhere)
at sufficiently high depth. This is the seed for E₂ emergence.
Equations
- Tau.BookIII.Arithmetic.bridgehead_check db = Tau.BookIII.Arithmetic.bridgehead_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.bridgehead_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L130-L139)@[irreducible]

**def
Tau.BookIII.Arithmetic.bridgehead_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.bridgehead_check.check_nontrivial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L141-L146)@[irreducible]

**def
Tau.BookIII.Arithmetic.bridgehead_check.check_nontrivial
(x pk k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.proto_code_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L161-L162)
**theorem
Tau.BookIII.Arithmetic.proto_code_15_4 :proto_code_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.bsd_functional_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L164-L165)
**theorem
Tau.BookIII.Arithmetic.bsd_functional_5 :bsd_functional_check 5 = true**


---

### `Tau.BookIII.Arithmetic.bridgehead_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L167-L168)
**theorem
Tau.BookIII.Arithmetic.bridgehead_4 :bridgehead_check 4 = true**


---

### `Tau.BookIII.Arithmetic.proto_zero_verified`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L174-L176)
**theorem
Tau.BookIII.Arithmetic.proto_zero_verified :(make_proto_code 0 3).verified = true**


[III.D61] Structural: proto-code of 0 is verified.

---

### `Tau.BookIII.Arithmetic.bsd_nonneg_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L178-L180)
**theorem
Tau.BookIII.Arithmetic.bsd_nonneg_1 :bsd_functional 1 ≥ 0**


[III.D62] Structural: BSD at depth 1 is non-negative.

---

### `Tau.BookIII.Arithmetic.bridgehead_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L182-L184)
**theorem
Tau.BookIII.Arithmetic.bridgehead_1 :bridgehead_check 1 = true**


[III.P26] Structural: bridgehead at depth 1.
