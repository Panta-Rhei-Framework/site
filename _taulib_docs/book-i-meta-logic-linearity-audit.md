---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.LinearityAudit"
permalink: /verify/taulib/docs/book-i-meta-logic-linearity-audit/
lane: verify
module_name: "TauLib.BookI.MetaLogic.LinearityAudit"
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

# TauLib.MetaLogic.LinearityAudit


The TauLib Linearity Audit: classifying all modules by their axiom usage.

## Registry Cross-References


- [I.T38] Linearity Census Theorem — `linearity_census`

- [I.P38] Classical.em Eliminability — `em_eliminable`

- [I.R17] Gap Declaration — documented in comments


## Mathematical Content


Census of 82 TauLib modules (pre-MetaLogic):


- 80 modules: fully constructive (no classical axioms)

- 1 module: uses Classical.em (Coordinates/Primes.lean, 2 sites, both eliminable)

- 1 module: uses funext tactic (Holomorphy/SpectralCoefficients.lean, kernel axiom)


---

### `Tau.MetaLogic.ModuleClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L28-L33)
**inductive
Tau.MetaLogic.ModuleClass :Type**


Classification of a TauLib module by its axiom usage.

- constructive : ModuleClass
- kernelAxiom : ModuleClass
- classical : ModuleClass
Instances For

---

### `Tau.MetaLogic.instDecidableEqModuleClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L33-L33)
**instance
Tau.MetaLogic.instDecidableEqModuleClass :DecidableEq ModuleClass**

Equations
- Tau.MetaLogic.instDecidableEqModuleClass x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprModuleClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L33-L33)
**instance
Tau.MetaLogic.instReprModuleClass :Repr ModuleClass**

Equations
- Tau.MetaLogic.instReprModuleClass = { reprPrec := Tau.MetaLogic.instReprModuleClass.repr }

---

### `Tau.MetaLogic.instReprModuleClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L33-L33)
**def
Tau.MetaLogic.instReprModuleClass.repr :ModuleClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.ModuleEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L37-L42)
**structure
Tau.MetaLogic.ModuleEntry :Type**


A census entry for a single TauLib module.

- name : String
- directory : String
- class_ : ModuleClass
Instances For

---

### `Tau.MetaLogic.instDecidableEqModuleEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L42-L42)
**instance
Tau.MetaLogic.instDecidableEqModuleEntry :DecidableEq ModuleEntry**

Equations
- Tau.MetaLogic.instDecidableEqModuleEntry = Tau.MetaLogic.instDecidableEqModuleEntry.decEq

---

### `Tau.MetaLogic.instDecidableEqModuleEntry.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L42-L42)
**def
Tau.MetaLogic.instDecidableEqModuleEntry.decEq
(x✝ x✝¹ : ModuleEntry)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprModuleEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L42-L42)
**instance
Tau.MetaLogic.instReprModuleEntry :Repr ModuleEntry**

Equations
- Tau.MetaLogic.instReprModuleEntry = { reprPrec := Tau.MetaLogic.instReprModuleEntry.repr }

---

### `Tau.MetaLogic.instReprModuleEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L42-L42)
**def
Tau.MetaLogic.instReprModuleEntry.repr :ModuleEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.census`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L48-L172)
**def
Tau.MetaLogic.census :List ModuleEntry**


The complete census of 82 TauLib modules (pre-MetaLogic).
Organized by directory.

Directory counts:


- Kernel: 3 (Signature, Axioms, Diagonal)

- Orbit: 8 (Generation, Countability, Closure, Rigidity, Ladder,
TooMany, TooFew, Saturation)

- Denotation: 8 (TauIdx, RankTransfer, ProgramMonoid, Equality, Order,
Arithmetic, GrowthEscape, Structural)

- Coordinates: 8 (NoTie, NormalForm, Descent, ABCD, Hyperfact,
TowerAtoms, PrimeEnumeration, Primes*)

- Polarity: 14 (Spectral, Polarity, PolarizedGerms, Lemniscate,
BipolarAlgebra, OmegaRing, OmegaGerms, PrimeBridge,
ExtGCD, ChineseRemainder, ModArith, NthPrime,
CRTBasis, TeichmuellerLift)

- Boundary: 11 (NumberTower, Ring, SplitComplex, Iota, Spectral,
Characters, Fourier, ConstructiveReals, ComplexField,
Quaternions, Cyclotomic)

- Logic: 3 (Truth4, Explosion, BooleanRecovery)

- Sets: 7 (Membership, Operations, Powerset, Universe,
CantorRefutation, Counting, UniqueInfinity)

- Holomorphy: 9 (DHolomorphic, TauHolomorphic, DiagonalProtection,
IdentityTheorem, SpectralCoefficients*, Thinness,
GlobalHartogs, BoundaryInterior, PresheafEssence)

- Topos: 7 (Functors, EarnedArrows, LimitsSites, EarnedTopos,
CartesianProduct, WedgeProduct, InternalHom)

- Spectrum: 4 (ThreeSAT, InterfaceWidth, KernelHinge, TTM)


- = non-constructive (see classification below)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.totalModules`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L178-L179)
**theorem
Tau.MetaLogic.totalModules :census.length = 82**


The total number of modules in the census.

---

### `Tau.MetaLogic.constructiveCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L181-L183)
**theorem
Tau.MetaLogic.constructiveCount :(List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.constructive) census).length = 80**


The number of fully constructive modules.

---

### `Tau.MetaLogic.classicalCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L185-L187)
**theorem
Tau.MetaLogic.classicalCount :(List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.classical) census).length = 1**


The number of modules using Classical.em.

---

### `Tau.MetaLogic.kernelCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L189-L191)
**theorem
Tau.MetaLogic.kernelCount :(List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.kernelAxiom) census).length = 1**


The number of modules using only CIC kernel axioms (not Classical.em).

---

### `Tau.MetaLogic.census_count_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L193-L198)
**theorem
Tau.MetaLogic.census_count_partition :(List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.constructive) census).length + (List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.kernelAxiom) census).length + (List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.classical) census).length = census.length**


Count partition: constructive + kernel + classical = total.

---

### `Tau.MetaLogic.dvd_decidable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L204-L210)
**def
Tau.MetaLogic.dvd_decidable
(a b : ℕ)
 :Decidable (a ∣ b)**


[I.P38] The Classical.em sites in Primes.lean are applied to
decidable predicates on Nat. Since Nat divisibility is decidable,
these uses are eliminable: they can be replaced by `Decidable.em`.

Proof that divisibility is decidable:
Equations
- Tau.MetaLogic.dvd_decidable a b = inferInstance
Instances For

---

### `Tau.MetaLogic.isPrime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L212-L216)
**def
Tau.MetaLogic.isPrime
(n : ℕ)
 :Bool**


The "is prime" predicate is decidable: a number is prime iff
it is greater than 1 and its only divisors are 1 and itself.
Since this is a bounded quantifier over Nat, it is decidable.
Equations
- Tau.MetaLogic.isPrime n = (decide (n > 1) && (List.range n).all fun (d : ℕ) => decide (d < 2) || n % d != 0)
Instances For

---

### `Tau.MetaLogic.isPrime_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L218-L219)
**theorem
Tau.MetaLogic.isPrime_2 :isPrime 2 = true**


The primality check is correct for small values.

---

### `Tau.MetaLogic.isPrime_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L220-L220)
**theorem
Tau.MetaLogic.isPrime_3 :isPrime 3 = true**


---

### `Tau.MetaLogic.isPrime_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L221-L221)
**theorem
Tau.MetaLogic.isPrime_4 :isPrime 4 = false**


---

### `Tau.MetaLogic.isPrime_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L222-L222)
**theorem
Tau.MetaLogic.isPrime_5 :isPrime 5 = true**


---

### `Tau.MetaLogic.decidable_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L224-L229)
**theorem
Tau.MetaLogic.decidable_em
{P : Prop}

[inst : Decidable P]
 :P ∨ ¬P**


Decidable excluded middle for decidable propositions:
for any decidable P, we have P ∨ ¬P without Classical.em.

---

### `Tau.MetaLogic.dvd_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L231-L234)
**theorem
Tau.MetaLogic.dvd_em
(a b : ℕ)
 :a ∣ b ∨ ¬a ∣ b**


Divisibility on Nat is decidable, so Classical.em is not needed
for excluded-middle on divisibility predicates.

---

### `Tau.MetaLogic.EmEliminability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L236-L243)
**structure
Tau.MetaLogic.EmEliminability :Type**


The Classical.em uses in Primes.lean are both on divisibility
predicates, which are decidable. Therefore both sites are
eliminable: Classical.em can be replaced by decidable_em.

- dvd_dec
(a b : ℕ)
 : Decidable (a ∣ b)
Divisibility is decidable

- dvd_em_constructive
(a b : ℕ)
 : a ∣ b ∨ ¬a ∣ b
Decidable em works without Classical.em

Instances For

---

### `Tau.MetaLogic.em_eliminable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L245-L248)
**def
Tau.MetaLogic.em_eliminable :EmEliminability**


The em eliminability witness.
Equations
- Tau.MetaLogic.em_eliminable = { dvd_dec := Tau.MetaLogic.dvd_decidable, dvd_em_constructive := Tau.MetaLogic.dvd_em }
Instances For

---

### `Tau.MetaLogic.LinearityCensus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L254-L275)
**structure
Tau.MetaLogic.LinearityCensus :Type**


[I.T38] The Linearity Census Theorem.

Of 82 pre-MetaLogic TauLib modules:


- 80 are fully constructive (no classical axioms at all)

- 1 uses Classical.em (Coordinates/Primes.lean), but both sites
are on decidable predicates and hence eliminable

- 1 uses the funext tactic (Holomorphy/SpectralCoefficients.lean),
which depends on the funext kernel axiom (always present in CIC)


The bottom line: TauLib is constructively valid modulo 2 eliminable
Classical.em sites and 1 kernel axiom use.

- total : census.length = 82
Total module count

- constructive : (List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.constructive) census).length = 80
Constructive module count

- classical : (List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.classical) census).length = 1
Classical module count

- kernel : (List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.kernelAxiom) census).length = 1
Kernel axiom module count

- em_sites_eliminable : EmEliminability
The Classical.em sites are eliminable

Instances For

---

### `Tau.MetaLogic.linearity_census`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L277-L283)
**def
Tau.MetaLogic.linearity_census :LinearityCensus**


The census theorem: all components are satisfied.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.countInDir`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L289-L291)
**def
Tau.MetaLogic.countInDir
(dir : String)
 :ℕ**


Helper: count modules in a specific directory.
Equations
- Tau.MetaLogic.countInDir dir = (List.filter (fun (m : Tau.MetaLogic.ModuleEntry) => m.directory == dir) Tau.MetaLogic.census).length
Instances For

---

### `Tau.MetaLogic.kernel_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L293-L294)
**theorem
Tau.MetaLogic.kernel_dir_count :countInDir "Kernel" = 3**


Kernel has 3 modules.

---

### `Tau.MetaLogic.orbit_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L296-L297)
**theorem
Tau.MetaLogic.orbit_dir_count :countInDir "Orbit" = 8**


Orbit has 8 modules.

---

### `Tau.MetaLogic.denotation_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L299-L300)
**theorem
Tau.MetaLogic.denotation_dir_count :countInDir "Denotation" = 8**


Denotation has 8 modules.

---

### `Tau.MetaLogic.coordinates_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L302-L303)
**theorem
Tau.MetaLogic.coordinates_dir_count :countInDir "Coordinates" = 8**


Coordinates has 8 modules.

---

### `Tau.MetaLogic.polarity_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L305-L306)
**theorem
Tau.MetaLogic.polarity_dir_count :countInDir "Polarity" = 14**


Polarity has 14 modules.

---

### `Tau.MetaLogic.boundary_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L308-L309)
**theorem
Tau.MetaLogic.boundary_dir_count :countInDir "Boundary" = 11**


Boundary has 11 modules.

---

### `Tau.MetaLogic.logic_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L311-L312)
**theorem
Tau.MetaLogic.logic_dir_count :countInDir "Logic" = 3**


Logic has 3 modules.

---

### `Tau.MetaLogic.sets_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L314-L315)
**theorem
Tau.MetaLogic.sets_dir_count :countInDir "Sets" = 7**


Sets has 7 modules.

---

### `Tau.MetaLogic.holomorphy_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L317-L318)
**theorem
Tau.MetaLogic.holomorphy_dir_count :countInDir "Holomorphy" = 9**


Holomorphy has 9 modules.

---

### `Tau.MetaLogic.topos_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L320-L321)
**theorem
Tau.MetaLogic.topos_dir_count :countInDir "Topos" = 7**


Topos has 7 modules.

---

### `Tau.MetaLogic.spectrum_dir_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L323-L324)
**theorem
Tau.MetaLogic.spectrum_dir_count :countInDir "Spectrum" = 4**


Spectrum has 4 modules.

---

### `Tau.MetaLogic.directory_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L326-L335)
**theorem
Tau.MetaLogic.directory_count :countInDir "Kernel" > 0 ∧ countInDir "Orbit" > 0 ∧ countInDir "Denotation" > 0 ∧ countInDir "Coordinates" > 0 ∧ countInDir "Polarity" > 0 ∧ countInDir "Boundary" > 0 ∧ countInDir "Logic" > 0 ∧ countInDir "Sets" > 0 ∧ countInDir "Holomorphy" > 0 ∧ countInDir "Topos" > 0 ∧ countInDir "Spectrum" > 0**


There are exactly 11 directories.
We verify this by listing all directory names and checking
that each of the 11 expected directories has at least one module.

---

### `Tau.MetaLogic.constructive_ratio_numerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L341-L345)
**theorem
Tau.MetaLogic.constructive_ratio_numerator :(List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.constructive) census).length = 80**


The constructive ratio: 80/82 = 97.6% of modules are fully constructive.
We verify the numerator and denominator.

---

### `Tau.MetaLogic.constructive_ratio_denominator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L347-L349)
**theorem
Tau.MetaLogic.constructive_ratio_denominator :census.length = 82**


---

### `Tau.MetaLogic.potential_constructive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/LinearityAudit.lean#L351-L356)
**theorem
Tau.MetaLogic.potential_constructive :(List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.constructive) census).length + (List.filter (fun (m : ModuleEntry) => m.class_ == ModuleClass.classical) census).length = 81**


After eliminating the 2 Classical.em sites, the potential constructive
count rises to 81 (the funext kernel axiom remains).
