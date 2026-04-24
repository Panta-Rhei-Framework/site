---
layout: program-doc
title: "Custom Axiom Inventory — The Compute-Then-Axiomatize Pattern"
permalink: /verify/custom-axioms/
lane: verify
summary_short: "Honest accounting of the three custom axiom declarations in TauLib beyond Mathlib's trusted base: what each axiom says, what finite computation motivates it, what the universal step being axiomatized is, and what specialist-review would close on each. The fourth axiom shipped in v1 (`central_theorem_physical : True`) was retired in peer-review-fixes-v1."
right_rail:
  related:
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Formal Methods Audit"
      url: /verify/how-to-audit/formal-methods/
    - title: "Red-team FAQ"
      url: /program/about/red-team-faq/
  meta:
    type: "Axiom Transparency"
    scope: "TauLib custom axioms"
    status: "Canonical"
    updated: "April 2026"
---

The [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) states, at the headline level, that TauLib contains **3 custom `axiom` declarations** beyond Mathlib's trusted base: **all 3 in Book III** (spectral / number-theoretic bridges). A previously shipping fourth axiom `central_theorem_physical : True` in Book IV was retired in `peer-review-fixes-v1` (2026-04-19) — an `axiom : True` declaration is a no-op (True is inhabited by `trivial`) and was identified in pre-publication simulated peer review as a null commitment that inflated the axiom inventory from 3 to 4 without adding anything to the theory. This page expands the accounting of the three remaining axioms.

The question a serious reviewer asks — and the April 2026 external assessments asked it explicitly — is: *for each custom axiom, what is the justification? Is this honest "compute-then-axiomatize" or is it a hidden load-bearing assumption dressed up as a universal statement?*

## What "compute-then-axiomatize" means in TauLib

The pattern is:

1. **A universal claim is stated** (the axiom body): "for all X in some class C, property P holds".
2. **A finite, decidable check is performed in Lean** using `decide` or `native_decide`: the claim is verified to hold for all X up to a specified finite bound B.
3. **The universal step is declared as an axiom**: the Lean kernel accepts the universal claim without further proof; downstream theorems rely on it.

This pattern is *not* a proof. It is an honest surface of a structural conjecture that has been numerically validated for all accessible cases but not formally proved in full generality. The axiom is *load-bearing* in the sense that downstream theorems cite it.

The pattern is acceptable as long as it is:

- **Explicitly declared** (not hidden inside a definition or an unfolded lemma),
- **Named** (the axiom has a stable identifier that `#print axioms` surfaces),
- **Bounded** (the finite check's bound B is stated and reproducible),
- **Load-bearing but marked** (downstream theorems referencing it carry a scope label that propagates the conjectural status).

The Mathlib community's norms on this are strict, and Lean's `#print axioms` mechanism is designed to make this pattern inspectable rather than deniable. TauLib commits to the same discipline.

## Inspecting the custom axioms

Any reviewer can, at the pinned commit [`2261c04`]({{ 'https://github.com/Panta-Rhei-Research/taulib/commit/2261c049119c8dd9a4e891457f196745178c02b3' }}):

```bash
cd taulib
rg "^axiom " TauLib --stats
```

Expected output: **3 matches**, with their module locations (all in `TauLib/BookIII/`).

For any downstream theorem `T`, run in Lean 4:

```lean
#print axioms T
```

Expected output lists:
- Mathlib's trusted base (`Classical.choice`, `propext`, `Quot.sound`)
- **Plus, if T transitively depends on a custom axiom**, the custom axiom's name.

This is the diagnostic. A theorem claimed as "Resolved" that transitively depends on one of the three custom axioms should carry a scope label reflecting that dependency. The [Formal Methods audit route]({{ '/verify/how-to-audit/formal-methods/' | relative_url }}) names this as one of the fail-fast checks.

## The three custom axioms

The precise Lean identifiers live in the TauLib source at the pinned commit. The specialist should verify them directly there. The descriptions below are at the prose level; the Lean source is authoritative.

### Axiom 1 — Bridge functor existence (Book III)

**What it says.** A structure-preserving functor exists between τ-admissible spectral data and the orthodox classical formulations (Riemann zeta, Dirichlet and Hecke L-functions) such that τ-internal spectral-purity results translate to classical statements on the τ-admissible sub-domain.

**What is finite-checked.** The functor's structure-preserving behavior has been verified via `native_decide` on all τ-admissible spectral data up to a stated finite bound: the trichotomy (III.T14) classifications match for all bounded configurations.

**What is axiomatized.** The universal extension: the functor exists and preserves spectral purity for *all* τ-admissible data, not just the finite-check window.

**What closes the gap.** A constructive proof of the functor's existence for unbounded spectral data, or a rigorous obstruction argument that shows the finite-check must extend. This is an active research direction.

**Where it is load-bearing.** The Master Schema (III.T27) — which is the bridge between τ-internal Riemann Hypothesis results and the classical Clay statement — depends on this axiom. Accordingly, the classical-RH claims are marked **Partial** on the site, not Resolved. If this axiom is retracted or refuted, the bridge from τ-internal ζ-purity to classical RH falls, but the τ-internal Critical Line Theorem (III.T19) remains.

### Axiom 2 — Spectral correspondence at O(3) (Book III)

**What it says.** The τ-spectral correspondence extends to third-order constructions: degree-3 polynomial spectral sub-structures on the lemniscate boundary preserve the B ↔ I ↔ S triangle structure in the same way degree-1 and degree-2 sub-structures do (which are proved).

**What is finite-checked.** The correspondence has been verified for all O(3) τ-admissible configurations up to a stated numerical bound.

**What is axiomatized.** The generalization from finite-checked O(3) configurations to all O(3) spectral data.

**What closes the gap.** A direct structural proof using the τ-CR operator and the Hartogs-extension principle for order-3 generalization.

**Where it is load-bearing.** The Book III spectral dictionary extensions (higher-order Millennium reformulations) depend on this axiom. Grand GRH results for higher-rank automorphic L-functions inherit the dependency.

### Axiom 3 — Grand Adelic GRH (Book III)

**What it says.** The Prime Polarity Scaling Theorem (III.T20) extends to *all* automorphic L-functions in the adelic sense, not just the finite-rank classes checked in Lean.

**What is finite-checked.** Grand GRH spectral purity has been verified via `native_decide` for all τ-admissible automorphic data with bounded rank and bounded conductor.

**What is axiomatized.** The universal extension to unbounded rank and conductor — the full adelic class.

**What closes the gap.** A rigorous argument that the τ-internal spectral trichotomy (III.T14) applies uniformly across the full adelic class. This is the most ambitious of the three Book III axioms and the least likely to be closed in the near term.

**Where it is load-bearing.** Grand GRH claims for higher-rank classes (not classical GRH for Dirichlet L, which is finite-checked separately). Any Resolved-status GRH claim that depends transitively on this axiom should be re-typed to Partial.

### Axiom 4 (RETIRED) — `central_theorem_physical : True` (Book IV)

**Status.** Retired in `peer-review-fixes-v1` (2026-04-19). No longer present in the TauLib source at the current pinned commit.

**What it had said.** The original declaration was `axiom central_theorem_physical : True` in `BookIV/Arena/BoundaryHolonomy.lean`, intended to mark the physical interpretation of the Book II Central Theorem as a named axiomatic hook.

**Why it was retired.** An axiom of type `True` is a no-op: `True` is already inhabited by `trivial`, so declaring an axiom at that type adds no logical content and names no new commitment. In pre-publication simulated peer review (chair: Leonardo de Moura, reviewer: Joachim Breitner) the declaration was flagged as a null commitment that inflated the visible axiom inventory from 3 to 4 without adding anything to the theory. The correct posture is either (a) state the physical interpretation as a proved theorem referencing the Book II algebraic proof, or (b) omit the declaration. Option (b) was chosen for v2.

**Current state.** The physical interpretation of the Central Theorem is now carried by the Book II algebraic statement and its guided tour in `TauLib/Tour/CentralTheorem.lean`; no Book IV axiom mediates the physical reading.

## Why this pattern rather than a proof

The honest reason is: the compute-then-axiomatize pattern is **faster than producing a full structural proof**, and it makes the conjectural step **visible** to `#print axioms`. A researcher who proved these three axioms would collapse the Partial/Conjectural status labels that depend on them; until then, the axioms are placeholders for work-in-progress proofs.

This is also exactly the pattern Mathlib and large Lean projects use for deep structural conjectures that admit numerical evidence but not immediate proofs (e.g., the prime-number-theorem bounds, certain analytic-number-theory density results). It is a pattern Lean was designed to surface cleanly.

A framework that hid such axioms inside definitions, used them implicitly in tactic closures, or simply wrote "here we assume" in prose without Lean declarations would be deniable. TauLib's declarations are inspectable.

## What specialist review would establish

A Lean-4 / formal-methods specialist should verify:

1. **Count correctness.** Is the `rg "^axiom"` output exactly 3 matches at the pinned commit, all in `TauLib/BookIII/`? (Claim: yes.)
2. **Axiom chain faithfulness.** For each of ~10 headline theorems that the Release Manifest claims as Resolved, does `#print axioms` surface only the Mathlib trusted base plus (where applicable) the `native_decide` TCB extension (`Lean.ofReduceBool`, `Lean.trustCompiler`) and no custom axioms? (Claim: yes; see [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}).)
3. **Partial-claim axiom propagation.** For each claim marked Partial that references one of the three axioms, does `#print axioms` surface the expected custom axiom? (Claim: yes.)
4. **Finite-check reproducibility.** For each custom axiom, the stated finite bound is reproducible via `native_decide` on the pinned commit. (Claim: yes.)
5. **Honest downstream-status propagation.** No Resolved claim transitively depends on a custom axiom in a way that should have re-typed it to Partial. (Claim: all such dependencies have been re-typed.)

Any finding that violates (1)–(5) should be reported to the program — this would be the single most impactful piece of formal-methods feedback possible.

## What this page does NOT claim

- It does not claim the three axioms will be proved in the near term. They are research-open.
- It does not claim the finite-check bounds are adequate to persuade a number-theorist that the universal extension is plausible. The finite checks are *Lean-decidable* evidence; they are not *mathematical* proofs of the universal case.
- It does not replace the [Formal Methods Audit route]({{ '/verify/how-to-audit/formal-methods/' | relative_url }}) — that is the concrete verification protocol for the claims on this page.
- It does not claim that the compute-then-axiomatize pattern is superior to direct proof. It is a transitional form: proofs-in-progress surfaced honestly.

## Cross-links

- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — headline axiom and `sorry` counts at pinned commit
- [Formalization Status]({{ '/verify/taulib/status/' | relative_url }}) — per-book formalization dashboard
- [Formal Methods Audit Route]({{ '/verify/how-to-audit/formal-methods/' | relative_url }}) — step-by-step verification protocol
- [Red-team FAQ #3]({{ '/program/about/red-team-faq/' | relative_url }}#does-taulib-introduce-custom-axiom-declarations-beyond-mathlibs-trusted-base) — short-form answer
- [Scope Labels]({{ '/verify/taulib/scope-labels/' | relative_url }}) — the 4-tier scope discipline that propagates through axiom dependencies
