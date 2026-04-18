---
layout: program-doc
title: "Spectral ζ vs Hilbert-Pólya / Connes / Berry-Keating"
permalink: /framework/prior-art/spectral-zeta-vs-hilbert-polya/
lane: framework
section: prior-art
summary_short: "Honest comparison between Book III's Critical Line Theorem (III.T19) — the τ-framework's spectral approach to the Riemann Hypothesis — and the Hilbert-Pólya, Connes adelic, Berry-Keating, and de Branges traditions of spectral-theoretic RH programs."
right_rail:
  related:
    - title: "Prior-Art Overview"
      url: /framework/prior-art/
    - title: "Riemann Hypothesis claim"
      url: /results/problem/riemann-hypothesis/
    - title: "Spectral Approach claim"
      url: /results/problem/riemann-hypothesis-spectral-approach/
    - title: "Millennium & Langlands briefing"
      url: /results/fields/millennium-langlands/
  meta:
    type: "Prior-Art Comparison"
    scope: "Spectral theory of ζ"
    status: "Canonical"
    updated: "April 2026"
---

Book III's **Critical Line Theorem (III.T19)** and the follow-on **Prime Polarity Scaling Theorem (III.T20)** establish that all non-trivial τ-zeta zeros lie on the critical line, via a spectral trichotomy argument. This sits in heavily-tilled territory: the idea that ζ's zeros should be the spectrum of a self-adjoint operator goes back nearly a century.

## What the prior art claims

The **Hilbert-Pólya conjecture** (attributed to Hilbert and Pólya in early 20th-century correspondence, never published by either) proposes that the non-trivial zeros of the Riemann zeta function are the eigenvalues of a self-adjoint operator. If such an operator were exhibited, the Riemann Hypothesis would follow immediately from the self-adjointness (real eigenvalues → zeros on critical line after the standard shift).

The conjecture has inspired many concrete programs:

- **Montgomery-Odlyzko law** (1973 and onward): the pair-correlation of ζ-zeros matches the Gaussian Unitary Ensemble (GUE) eigenvalue statistics, consistent with a random-matrix-theoretic origin for the zero distribution.
- **Berry-Keating conjecture** (1999): the relevant Hamiltonian should be H = xp (with appropriate quantization), the classical Hamiltonian of a particle in a dilation-flow potential. The Berry-Keating framework made the Hilbert-Pólya picture semiclassically quantitative.
- **Alain Connes' adelic spectral approach** (1996 and onward): a cohomological trace formula on the adele class space, where the explicit formula for ζ-zeros arises as a spectral trace. Connes' program is the most mathematically developed realization of the Hilbert-Pólya idea to date, though the RH-implying trace-positivity step remains conjectural.
- **Louis de Branges' spaces** (1980s onward): Hilbert spaces of entire functions (de Branges spaces) provide an operator-theoretic framework in which certain zero-distribution statements become positivity of associated operator spectra. De Branges has claimed RH multiple times; the proofs have not been accepted by the community, though the framework remains used.
- **Selberg trace formula analogues**: zeros of Selberg zeta functions are eigenvalues of the Laplacian on hyperbolic surfaces. The Hilbert-Pólya dream is sometimes summarized as "find the analogue of the Selberg trace formula for ℚ".

The shape of these programs is: **define an operator whose spectrum contains the non-trivial ζ-zeros; prove the operator is self-adjoint (or otherwise has real spectrum) to conclude RH**.

## What τ claims in this territory

Book III advances four load-bearing results in this territory:

- **III.T19 — Critical Line Theorem.** All non-trivial zeros of the τ-zeta function ζ_τ lie on the critical line, via a **spectral trichotomy argument** (three alternatives: boundary, interior, or critical line; the first two are excluded structurally).
- **III.T14 — Spectral Trichotomy.** The underlying operator-theoretic mechanism that forces zeros onto the critical line.
- **III.T20 — Prime Polarity Scaling Theorem.** Extends the Critical Line claim from ζ_τ to all τ-framework automorphic L-functions (the Grand GRH analogue; see III.D31).
- **III.T27 — Master Schema.** The bridge from internal τ-results to orthodox formulations, *marked conjectural*, consisting of a B ↔ I ↔ S triangle structure.

**Crucially:** the framework explicitly labels these results **τ-effective / finite-window**. They are internal theorems of the τ framework. The bridge to the classical Riemann Hypothesis as stated by the Clay Mathematics Institute — i.e., zeros of the standard Riemann ζ on the classical critical line — is **not** claimed as a theorem. Book III's "ledger of limitations and next steps" explicitly says so.

## What is structurally the same

A specialist in spectral approaches to RH will recognize the shared territory immediately:

- **Operator-theoretic framing.** Both Hilbert-Pólya and τ seek to force RH (or a τ-analogue) via the spectrum of an operator with constrained structure. This is the common DNA of the approach.
- **Finite-window / finite-rank approximations.** Connes' adelic trace formula is infinite-dimensional; regularization procedures make finite-dimensional approximations tractable. Book III's "finite-window" discipline parallels this: specific results are proved for bounded-interface configurations, with infinite-limit statements marked as separate.
- **Trichotomy-style arguments.** A family of spectral approaches establishes a target statement by ruling out alternatives (zero off the critical line, zero below a line, etc.). The τ spectral trichotomy is formally a member of this family.
- **Explicit formula structure.** Classical analytic number theory relates zero distribution to prime distribution via the explicit formula. Book III develops a τ-internal analogue (III.T20, Prime Polarity Scaling); this is recognizable as the same kind of tool.

## What is structurally different

1. **Scope discipline is explicit and load-bearing.** Connes' adelic program is presented as a route to classical RH; its open step (trace-positivity) is the bridge to RH, and the program is judged on whether it crosses that step. τ Book III is explicit that the τ-zeros are **not** the classical ζ-zeros without a separate bridge argument (Master Schema, III.T27), and that bridge is marked conjectural. τ is therefore a different *kind* of claim: a τ-internal theorem with an explicit bridge gap, not a direct attempt at the Clay problem.

2. **The operator is earned from kernel structure, not postulated.** Hilbert-Pólya is a conjecture about the existence of an operator. Berry-Keating postulates a specific operator (H = xp) and then asks whether its quantization gives the right spectrum. Connes constructs a specific operator on the adele class space. τ *derives* its spectral operator from the seven kernel axioms (K0–K6); the operator is not chosen to give a particular spectral result, and the spectral trichotomy is a consequence of the kernel's internal structure.

3. **Categorical setting.** Connes' adelic program lives on the adele class space of ℚ; Selberg-type programs live on hyperbolic surfaces; Berry-Keating lives in classical/quantum phase-space dynamics. τ's spectral machinery is categorical — functions on τ³, characters on 𝕃. A specialist should check whether τ's spectral objects have faithful translations to one of these more-traditional settings, or whether they are genuinely new mathematical objects.

4. **Scope labels on every claim.** Book III carries explicit scope labels: **established / τ-effective / conjectural / metaphorical**. Each sub-claim in III is marked. Connes' and de Branges' programs do not use this scope taxonomy; their programs are usually judged as a single "route to RH" that either crosses its final gap or does not.

5. **Lean-verified internal architecture.** The Lean formalization of III.T19 and III.T20 is in TauLib (Book III directory); see the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) for the pinned commit. A specialist can inspect the formal statement directly — a level of verification not available for most of the historical Hilbert-Pólya program.

## What is genuinely new (claimed)

If the Book III Critical Line Theorem holds as stated:

- **A proved internal RH-analogue with explicit bridge labeling.** A theorem plus an honest gap is a different artifact than an attempted theorem with a hidden gap. The τ framework's approach is to ship the internal theorem and name the bridge, which is structurally different from programs that ship "a route to RH" and let specialists find the gaps.
- **Unified with the rest of τ's mathematics.** III.T19 is not standalone — it connects to II's Central Theorem (via spectral structure on the boundary 𝕃), to the prime-polarity scaling law III.T20, and to the full Book III spectral dictionary for Millennium problems. If the internal theorems hold, they form a coherent cluster, not isolated results.
- **Extension to Grand GRH.** The Prime Polarity Scaling Theorem (III.T20) claims the spectral trichotomy extends to the entire Grand GRH class — all automorphic L-functions in the τ framework. Most prior-art programs address ζ specifically; τ claims the same machinery covers the broader Grand Riemann hierarchy.

## What a specialist would want to see

An analytic number theorist or operator theorist should ask:

1. **The operator identification.** What is the τ spectral operator, explicitly, as an operator on a named Hilbert space? Is it self-adjoint, and what is the proof?
2. **Relation to Connes' adelic operator.** The Connes adelic operator is the closest specialist analogue. Does the τ operator reduce to a known construction on the adele class space (or on ℚ) under a specific translation, or is it a genuinely different operator?
3. **Pair correlation and GUE statistics.** Do the τ-zeta zeros obey the Montgomery-Odlyzko law (GUE pair correlation)? If yes, this is strong consistency with classical ζ; if no, τ is making a different prediction about zero statistics.
4. **Bridge functor definition.** The Master Schema (III.T27) is the formal bridge between τ-internal and classical statements. What is the functor, what does it send ζ_τ to, and what is the obstruction to proving it equals the classical ζ?
5. **Scope of "τ-admissible" data.** The τ results apply to τ-admissible data (finite-window, bounded-interface). How much of the classical RH problem remains when the results are pulled through the Master Schema — is it the full problem, or a proper sub-problem?
6. **Zero distribution of ζ_τ on the critical line.** Classical ζ has a known distribution of zeros (Riemann-von Mangoldt formula). Does ζ_τ have the same zero-counting formula on the critical line, or does it predict a different density?

Until questions 1–4 are answered explicitly by specialists, τ's spectral approach is best read as **a new member of the Hilbert-Pólya family with an unusually honest scope discipline**. Whether it is a genuine advance on Connes or de Branges or a parallel construction that ultimately translates into their framework is exactly what specialist review should determine.

## Status summary

| Claim | Status | Bridge to Clay RH |
|-------|:-----:|:------------------|
| III.T19 Critical Line (τ-internal) | Formalized | Internal theorem |
| III.T20 Prime Polarity Scaling (τ-internal) | Formalized | Internal theorem |
| III.T27 Master Schema bridge | Conjectural | Explicit bridge; gap is the τ-↔-classical identification |
| Clay RH resolution | **Not claimed** | Requires III.T27 bridge to be closed |

The framework's honesty is on display here: the τ-internal critical-line theorem is load-bearing and Lean-verified, while the Clay-RH bridge is marked conjectural and not claimed. This is structurally different from programs that leave their gaps implicit.

## Cross-links

- [Riemann Hypothesis claim page]({{ '/results/problem/riemann-hypothesis/' | relative_url }}) — τ-side statement with explicit bridge status
- [Spectral Approach claim page]({{ '/results/problem/riemann-hypothesis-spectral-approach/' | relative_url }}) — the spectral trichotomy detail
- [Grand GRH claim page]({{ '/results/problem/grand-grh-approach/' | relative_url }}) — extension to automorphic L-functions
- [Millennium & Langlands briefing]({{ '/results/fields/millennium-langlands/' | relative_url }}) — full Millennium claim set
- [Prior-Art Overview]({{ '/framework/prior-art/' | relative_url }}) — the other four prior-art zones
