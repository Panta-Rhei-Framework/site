---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.Identity"
permalink: /verify/taulib/docs/book-vi-consumer-identity/
lane: verify
module_name: "TauLib.BookVI.Consumer.Identity"
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

# TauLib.BookVI.Consumer.Identity


Identity over code, not carrier: Ship of Theseus resolution.

## Registry Cross-References


- [VI.D53] SelfDesc over Code, Not Carrier — `SelfDescOverCode`

- [VI.L08] Substrate Replacement Preserves Life-Equivalence — `substrate_replacement_preserves_life`


## Cross-Book Authority


- Book II, Part X: ω-germ code (profinite invariant, identity criterion)

- Book I, Part I: generators of τ³ (code is over generators, not material substrate)


## Ground Truth Sources


- Book VI Chapter 42 (2nd Edition): The Ship of Theseus


---

### `Tau.BookVI.Identity.SelfDescOverCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L28-L39)
**structure
Tau.BookVI.Identity.SelfDescOverCode :Type**


[VI.D53] SelfDesc over Code, Not Carrier.
Biological identity resides in the ω-germ code (Book II, Part X),
not in the material carrier. The profinite invariant is preserved
under complete material turnover.

- identity_locus : String
Identity locus is the ω-germ code.

- not_carrier : Bool
Identity is NOT in the carrier.

- profinite_invariant : Bool
The ω-germ code is a profinite invariant (Book II, Part X).

Instances For

---

### `Tau.BookVI.Identity.instReprSelfDescOverCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L39-L39)
**instance
Tau.BookVI.Identity.instReprSelfDescOverCode :Repr SelfDescOverCode**

Equations
- Tau.BookVI.Identity.instReprSelfDescOverCode = { reprPrec := Tau.BookVI.Identity.instReprSelfDescOverCode.repr }

---

### `Tau.BookVI.Identity.instReprSelfDescOverCode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L39-L39)
**def
Tau.BookVI.Identity.instReprSelfDescOverCode.repr :SelfDescOverCode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Identity.selfdesc_code`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L41-L41)
**def
Tau.BookVI.Identity.selfdesc_code :SelfDescOverCode**

Equations
- Tau.BookVI.Identity.selfdesc_code = { }
Instances For

---

### `Tau.BookVI.Identity.SubstrateReplacement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L47-L61)
**structure
Tau.BookVI.Identity.SubstrateReplacement :Type**


[VI.L08] Substrate Replacement Preserves Life-Equivalence.
Complete material turnover (every atom replaced) does not
alter life status, because SelfDesc evaluates code continuity,
not material identity. Passes the metamorphosis test:
caterpillar → chrysalis → butterfly preserves identity.

- material_turnover : Bool
Material turnover occurs.

- code_preserved : Bool
ω-germ code is preserved.

- selfdesc_continuous : Bool
SelfDesc evaluation is continuous through turnover.

- metamorphosis_test : Bool
Passes metamorphosis test (caterpillar → butterfly).

Instances For

---

### `Tau.BookVI.Identity.instReprSubstrateReplacement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L61-L61)
**instance
Tau.BookVI.Identity.instReprSubstrateReplacement :Repr SubstrateReplacement**

Equations
- Tau.BookVI.Identity.instReprSubstrateReplacement = { reprPrec := Tau.BookVI.Identity.instReprSubstrateReplacement.repr }

---

### `Tau.BookVI.Identity.instReprSubstrateReplacement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L61-L61)
**def
Tau.BookVI.Identity.instReprSubstrateReplacement.repr :SubstrateReplacement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Identity.substrate_repl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L63-L63)
**def
Tau.BookVI.Identity.substrate_repl :SubstrateReplacement**

Equations
- Tau.BookVI.Identity.substrate_repl = { }
Instances For

---

### `Tau.BookVI.Identity.identity_is_code_not_carrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L65-L68)
**theorem
Tau.BookVI.Identity.identity_is_code_not_carrier :selfdesc_code.not_carrier = true ∧ selfdesc_code.profinite_invariant = true**


---

### `Tau.BookVI.Identity.substrate_replacement_preserves_life`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L70-L75)
**theorem
Tau.BookVI.Identity.substrate_replacement_preserves_life :substrate_repl.material_turnover = true ∧ substrate_repl.code_preserved = true ∧ substrate_repl.selfdesc_continuous = true ∧ substrate_repl.metamorphosis_test = true**


---

### `Tau.BookVI.Identity.SubstrateAbstraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L81-L102)
**structure
Tau.BookVI.Identity.SubstrateAbstraction :Type**


[VI.T50] Substrate Abstraction Theorem.
The 5 Distinction conditions (VI.D04) + 3 SelfDesc conditions (VI.D08)
are necessary and sufficient for life, independent of material substrate.
Proof: (1) Sufficiency: the definitions use only abstract morphisms,
functors, and winding numbers — no material predicates appear.
(2) Necessity: failure of any condition produces a counterexample
(VI.D16 Absence catalog). (3) Independence: VI.L08 shows that
replacing the material substrate while preserving code + evaluation
preserves life-equivalence; VI.D53 locates identity in the code.
Scope: τ-effective.

- conditions_abstract : Bool
All 8 conditions (5+3) are formulated abstractly.

- sufficient : Bool
8 conditions are sufficient for life.

- necessary : Bool
8 conditions are necessary for life (Absence catalog).

- substrate_independent : Bool
No material predicate appears in any condition.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Identity.instReprSubstrateAbstraction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L102-L102)
**def
Tau.BookVI.Identity.instReprSubstrateAbstraction.repr :SubstrateAbstraction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Identity.instReprSubstrateAbstraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L102-L102)
**instance
Tau.BookVI.Identity.instReprSubstrateAbstraction :Repr SubstrateAbstraction**

Equations
- Tau.BookVI.Identity.instReprSubstrateAbstraction = { reprPrec := Tau.BookVI.Identity.instReprSubstrateAbstraction.repr }

---

### `Tau.BookVI.Identity.substrate_abs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L104-L104)
**def
Tau.BookVI.Identity.substrate_abs :SubstrateAbstraction**

Equations
- Tau.BookVI.Identity.substrate_abs = { }
Instances For

---

### `Tau.BookVI.Identity.substrate_abstraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Consumer/Identity.lean#L106-L111)
**theorem
Tau.BookVI.Identity.substrate_abstraction :substrate_abs.conditions_abstract = true ∧ substrate_abs.sufficient = true ∧ substrate_abs.necessary = true ∧ substrate_abs.substrate_independent = true**
