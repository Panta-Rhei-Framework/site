---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.ConjectureGaps"
permalink: /verify/taulib/docs/book-iii-bridge-conjecture-gaps/
lane: verify
module_name: "TauLib.BookIII.Bridge.ConjectureGaps"
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

# TauLib.BookIII.Bridge.ConjectureGaps


Proof-theoretic gap analysis for Goldbach, Twin Primes, and ABC conjectures.
Classifies the exact nature of each gap between what the τ framework
can prove (finite-level, tower-decidable) and what the full conjectures
require (infinite, analytic).

## Registry Cross-References


- [III.D111] Tower Decidable Check — `tower_decidable_check`

- [III.D112] Gap Type — `GapType`, `conjecture_gap_type`

- [III.D113] Forbidden Move Mapping — `gap_forbidden_move`

- [III.T79] Tower Finite Decidable — `tower_finite_decidable_3`

- [III.T80] Bridge Necessary Insufficient — `bridge_necessary_insufficient`

- [III.R47] Comparison with Classical Approaches — (docstring)

- [III.R48] Honest Conclusion — (docstring)


## Mathematical Content


**III.D111 (Tower Decidable):** At each finite primorial level M_k,
every instance of all three conjectures is decidable: Goldbach for
a specific n is decidable by enumeration of pairs, twin primes below
N is a finite count, ABC for specific (a,b) is a finite radical
computation. The τ framework can verify any FINITE instance.

**III.D112 (Gap Type):** Three distinct gap types:


- **Parity** (Goldbach): The parity barrier blocks any sieve-based
approach from proving Goldbach for ALL n. The difficulty is that
no sieve can distinguish "n has a Goldbach representation" from
"n has many almost-prime representations."

- **Density** (Twin Primes): The density gap is the passage from
"admissible residue classes are nonempty" (algebraic, proven by CRT)
to "infinitely many primes actually occupy those classes" (analytic,
requires Bombieri-Vinogradov or stronger).

- **Structural** (ABC): The squarefree tower avoids ABC difficulty
entirely. The gap is that genuine ABC difficulty lives in
perfect-power parts, which the primorial tower systematically avoids.


**III.D113 (Forbidden Move Mapping):** Each gap maps to the
`exponential_quantification` forbidden move (K4 axiom violation):
the passage from finite to infinite requires quantifying over
exponentially many objects, which τ cannot express.

**III.T79 (Tower Finite Decidable):** All three conjectures are
decidable at each finite level. Goldbach(n) is decidable for each n.
TwinPrimeCount(N) is computable for each N. ABC(a,b) is computable
for each pair.

**III.T80 (Bridge Necessary Insufficient):** The bridge axiom is
NECESSARY for connecting τ-internal results to external conjectures.
But even the bridge functor is INSUFFICIENT for full proofs: the
bridge preserves finite-level structure but cannot create the analytic
content (circle method, sieve asymptotics, height theory) needed
for the infinite case.

**III.R47 (Classical Comparison):** τ provides the algebraic component
(CRT, local conditions, admissibility). Classical approaches provide
the analytic component (circle method, sieve asymptotics, height theory).
Neither alone suffices.

**III.R48 (Honest Conclusion):** τ reduces each conjecture to its
local conditions, which are always satisfiable. The local-to-global
passage requires analytic tools no finitary framework possesses.
This is not a failure but a precise characterization of difficulty.

---

### `Tau.BookIII.Bridge.GapType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L84-L89)
**inductive
Tau.BookIII.Bridge.GapType :Type**


[III.D112] The three gap types for additive conjectures.

- parity : GapType
- density : GapType
- structural : GapType
Instances For

---

### `Tau.BookIII.Bridge.instReprGapType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L89-L89)
**def
Tau.BookIII.Bridge.instReprGapType.repr :GapType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instReprGapType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L89-L89)
**instance
Tau.BookIII.Bridge.instReprGapType :Repr GapType**

Equations
- Tau.BookIII.Bridge.instReprGapType = { reprPrec := Tau.BookIII.Bridge.instReprGapType.repr }

---

### `Tau.BookIII.Bridge.instDecidableEqGapType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L89-L89)
**instance
Tau.BookIII.Bridge.instDecidableEqGapType :DecidableEq GapType**

Equations
- Tau.BookIII.Bridge.instDecidableEqGapType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqGapType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L89-L89)
**instance
Tau.BookIII.Bridge.instBEqGapType :BEq GapType**

Equations
- Tau.BookIII.Bridge.instBEqGapType = { beq := Tau.BookIII.Bridge.instBEqGapType.beq }

---

### `Tau.BookIII.Bridge.instBEqGapType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L89-L89)
**def
Tau.BookIII.Bridge.instBEqGapType.beq :GapType → GapType → Bool**

Equations
- Tau.BookIII.Bridge.instBEqGapType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.GapType.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L91-L95)
**def
Tau.BookIII.Bridge.GapType.toNat :GapType → ℕ**


[III.D112] Numeric index of each gap type.
Equations
- Tau.BookIII.Bridge.GapType.parity.toNat = 0
- Tau.BookIII.Bridge.GapType.density.toNat = 1
- Tau.BookIII.Bridge.GapType.structural.toNat = 2
Instances For

---

### `Tau.BookIII.Bridge.GapType.name`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L97-L101)
**def
Tau.BookIII.Bridge.GapType.name :GapType → String**


[III.D112] Human-readable name of each gap type.
Equations
- Tau.BookIII.Bridge.GapType.parity.name = "parity barrier"
- Tau.BookIII.Bridge.GapType.density.name = "density gap"
- Tau.BookIII.Bridge.GapType.structural.name = "structural avoidance"
Instances For

---

### `Tau.BookIII.Bridge.AdditiveConjecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L107-L112)
**inductive
Tau.BookIII.Bridge.AdditiveConjecture :Type**


Classification of the three conjectures.

- goldbach : AdditiveConjecture
- twin_primes : AdditiveConjecture
- abc : AdditiveConjecture
Instances For

---

### `Tau.BookIII.Bridge.instReprAdditiveConjecture.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L112-L112)
**def
Tau.BookIII.Bridge.instReprAdditiveConjecture.repr :AdditiveConjecture → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instReprAdditiveConjecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L112-L112)
**instance
Tau.BookIII.Bridge.instReprAdditiveConjecture :Repr AdditiveConjecture**

Equations
- Tau.BookIII.Bridge.instReprAdditiveConjecture = { reprPrec := Tau.BookIII.Bridge.instReprAdditiveConjecture.repr }

---

### `Tau.BookIII.Bridge.instDecidableEqAdditiveConjecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L112-L112)
**instance
Tau.BookIII.Bridge.instDecidableEqAdditiveConjecture :DecidableEq AdditiveConjecture**

Equations
- Tau.BookIII.Bridge.instDecidableEqAdditiveConjecture x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqAdditiveConjecture.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L112-L112)
**def
Tau.BookIII.Bridge.instBEqAdditiveConjecture.beq :AdditiveConjecture → AdditiveConjecture → Bool**

Equations
- Tau.BookIII.Bridge.instBEqAdditiveConjecture.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.instBEqAdditiveConjecture`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L112-L112)
**instance
Tau.BookIII.Bridge.instBEqAdditiveConjecture :BEq AdditiveConjecture**

Equations
- Tau.BookIII.Bridge.instBEqAdditiveConjecture = { beq := Tau.BookIII.Bridge.instBEqAdditiveConjecture.beq }

---

### `Tau.BookIII.Bridge.all_conjectures`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L114-L116)
**def
Tau.BookIII.Bridge.all_conjectures :List AdditiveConjecture**


All three conjectures as a list.
Equations
- Tau.BookIII.Bridge.all_conjectures = [Tau.BookIII.Bridge.AdditiveConjecture.goldbach, Tau.BookIII.Bridge.AdditiveConjecture.twin_primes, Tau.BookIII.Bridge.AdditiveConjecture.abc]
Instances For

---

### `Tau.BookIII.Bridge.conjecture_gap_type`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L118-L122)
**def
Tau.BookIII.Bridge.conjecture_gap_type :AdditiveConjecture → GapType**


[III.D112] Map each conjecture to its gap type.
Equations
- Tau.BookIII.Bridge.conjecture_gap_type Tau.BookIII.Bridge.AdditiveConjecture.goldbach = Tau.BookIII.Bridge.GapType.parity
- Tau.BookIII.Bridge.conjecture_gap_type Tau.BookIII.Bridge.AdditiveConjecture.twin_primes = Tau.BookIII.Bridge.GapType.density
- Tau.BookIII.Bridge.conjecture_gap_type Tau.BookIII.Bridge.AdditiveConjecture.abc = Tau.BookIII.Bridge.GapType.structural
Instances For

---

### `Tau.BookIII.Bridge.gap_forbidden_move`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L128-L135)
**def
Tau.BookIII.Bridge.gap_forbidden_move :AdditiveConjecture → ForbiddenMove**


[III.D113] All three gaps map to the same forbidden move:
exponential_quantification (K4 violation). The passage from
finite verification to infinite proof requires quantifying
over exponentially many objects.
Equations
- Tau.BookIII.Bridge.gap_forbidden_move Tau.BookIII.Bridge.AdditiveConjecture.goldbach = Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification
- Tau.BookIII.Bridge.gap_forbidden_move Tau.BookIII.Bridge.AdditiveConjecture.twin_primes = Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification
- Tau.BookIII.Bridge.gap_forbidden_move Tau.BookIII.Bridge.AdditiveConjecture.abc = Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification
Instances For

---

### `Tau.BookIII.Bridge.gap_violated_axiom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L137-L139)
**def
Tau.BookIII.Bridge.gap_violated_axiom
(c : AdditiveConjecture)
 :Hinge.ChainLink**


[III.D113] The violated axiom for all three gaps is K4.
Equations
- Tau.BookIII.Bridge.gap_violated_axiom c = Tau.BookIII.Bridge.violated_axiom (Tau.BookIII.Bridge.gap_forbidden_move c)
Instances For

---

### `Tau.BookIII.Bridge.conjecture_scope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L145-L149)
**def
Tau.BookIII.Bridge.conjecture_scope :AdditiveConjecture → ScopeLabel**


Scope of τ-internal results for each conjecture.
Equations
- Tau.BookIII.Bridge.conjecture_scope Tau.BookIII.Bridge.AdditiveConjecture.goldbach = Tau.BookIII.Bridge.ScopeLabel.tau_effective
- Tau.BookIII.Bridge.conjecture_scope Tau.BookIII.Bridge.AdditiveConjecture.twin_primes = Tau.BookIII.Bridge.ScopeLabel.tau_effective
- Tau.BookIII.Bridge.conjecture_scope Tau.BookIII.Bridge.AdditiveConjecture.abc = Tau.BookIII.Bridge.ScopeLabel.tau_effective
Instances For

---

### `Tau.BookIII.Bridge.full_conjecture_scope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L151-L155)
**def
Tau.BookIII.Bridge.full_conjecture_scope :AdditiveConjecture → ScopeLabel**


Full conjecture (infinite case) scope.
Equations
- Tau.BookIII.Bridge.full_conjecture_scope Tau.BookIII.Bridge.AdditiveConjecture.goldbach = Tau.BookIII.Bridge.ScopeLabel.conjectural
- Tau.BookIII.Bridge.full_conjecture_scope Tau.BookIII.Bridge.AdditiveConjecture.twin_primes = Tau.BookIII.Bridge.ScopeLabel.conjectural
- Tau.BookIII.Bridge.full_conjecture_scope Tau.BookIII.Bridge.AdditiveConjecture.abc = Tau.BookIII.Bridge.ScopeLabel.conjectural
Instances For

---

### `Tau.BookIII.Bridge.scope_discipline_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L157-L162)
**def
Tau.BookIII.Bridge.scope_discipline_check :Bool**


Scope discipline: finite results are τ-effective, infinite claims
are conjectural.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.tower_decidable_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L168-L182)
**def
Tau.BookIII.Bridge.tower_decidable_check :Bool**


[III.D111] At each finite level, all three conjectures are decidable.
This is a structural fact: each check function (goldbach_pair,
twin_prime_count, abc_triple_check) is a computable Lean function.
Here we verify the structural prerequisites: each conjecture has
a defined gap type, forbidden move, and scope label.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.bridge_necessary_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L188-L198)
**def
Tau.BookIII.Bridge.bridge_necessary_check :Bool**


[III.T80] Bridge is necessary: all three conjectures have status
"conjectural" or lower in the bridge taxonomy. Without the bridge,
τ-internal results cannot make claims about ℕ-level conjectures.
The bridge is necessary but NOT sufficient (even with bridge, the
analytic component is missing).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.gap_taxonomy_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L200-L205)
**def
Tau.BookIII.Bridge.gap_taxonomy_complete :Bool**


[III.T80] The three gap types form a complete taxonomy.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.tower_finite_decidable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L211-L214)
**theorem
Tau.BookIII.Bridge.tower_finite_decidable :tower_decidable_check = true**


[III.T79] Tower decidability: all three conjectures have defined
gap types, forbidden moves, and scope labels.

---

### `Tau.BookIII.Bridge.bridge_necessary_insufficient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L216-L218)
**theorem
Tau.BookIII.Bridge.bridge_necessary_insufficient :bridge_necessary_check = true**


[III.T80] Bridge is necessary but insufficient for full conjectures.

---

### `Tau.BookIII.Bridge.gap_taxonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L220-L222)
**theorem
Tau.BookIII.Bridge.gap_taxonomy :gap_taxonomy_complete = true**


[III.D112] Gap taxonomy is complete: three distinct gap types.

---

### `Tau.BookIII.Bridge.all_gaps_exponential`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L224-L228)
**theorem
Tau.BookIII.Bridge.all_gaps_exponential :(all_conjectures.all fun (c : AdditiveConjecture) => gap_forbidden_move c == ForbiddenMove.exponential_quantification) = true**


[III.D113] All three gaps map to exponential_quantification.

---

### `Tau.BookIII.Bridge.scope_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L230-L232)
**theorem
Tau.BookIII.Bridge.scope_check :scope_discipline_check = true**


Scope discipline: finite τ-effective, infinite conjectural.

---

### `Tau.BookIII.Bridge.parity_ne_density`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L238-L240)
**theorem
Tau.BookIII.Bridge.parity_ne_density :GapType.parity.toNat ≠ GapType.density.toNat**


[III.D112] Gap types are distinct.

---

### `Tau.BookIII.Bridge.gap_indices`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L242-L247)
**theorem
Tau.BookIII.Bridge.gap_indices :GapType.parity.toNat = 0 ∧ GapType.density.toNat = 1 ∧ GapType.structural.toNat = 2**


[III.D112] Three gap types cover indices 0, 1, 2.

---

### `Tau.BookIII.Bridge.goldbach_gap_parity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L249-L251)
**theorem
Tau.BookIII.Bridge.goldbach_gap_parity :conjecture_gap_type AdditiveConjecture.goldbach = GapType.parity**


[III.D113] Goldbach gap = parity.

---

### `Tau.BookIII.Bridge.twin_gap_density`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L253-L255)
**theorem
Tau.BookIII.Bridge.twin_gap_density :conjecture_gap_type AdditiveConjecture.twin_primes = GapType.density**


[III.D113] Twin primes gap = density.

---

### `Tau.BookIII.Bridge.abc_gap_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L257-L259)
**theorem
Tau.BookIII.Bridge.abc_gap_structural :conjecture_gap_type AdditiveConjecture.abc = GapType.structural**


[III.D113] ABC gap = structural.

---

### `Tau.BookIII.Bridge.all_gaps_K4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L261-L266)
**theorem
Tau.BookIII.Bridge.all_gaps_K4 :gap_violated_axiom AdditiveConjecture.goldbach = Hinge.ChainLink.K4 ∧ gap_violated_axiom AdditiveConjecture.twin_primes = Hinge.ChainLink.K4 ∧ gap_violated_axiom AdditiveConjecture.abc = Hinge.ChainLink.K4**


[III.D113] All gaps violate K4.

---

### `Tau.BookIII.Bridge.exponential_damage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L268-L270)
**theorem
Tau.BookIII.Bridge.exponential_damage :bridge_damage ForbiddenMove.exponential_quantification = 3**


[III.T80] Bridge damage at exponential_quantification is 3 (break).

---

### `Tau.BookIII.Bridge.three_conjectures`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/ConjectureGaps.lean#L272-L274)
**theorem
Tau.BookIII.Bridge.three_conjectures :all_conjectures.length = 3**


Exactly 3 conjectures analyzed.
