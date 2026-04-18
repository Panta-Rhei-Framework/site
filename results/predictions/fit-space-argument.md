---
layout: program-doc
title: "Fit-Space Analysis — Are the 67 Predictions Numerological Coincidences?"
permalink: /results/predictions/fit-space-argument/
lane: results
section: "Physics Ledger · Fit-Space Analysis"
summary_short: "A quantitative response to the strongest red-team question about the 67 zero-parameter predictions: if someone enumerated simple closed-form expressions in ι_τ = 2/(π+e) and tested them against known constants, how many coincidences at sub-10 ppm precision would be expected by chance — and how does that compare to the 15 observed?"
right_rail:
  related:
  - title: Predictions Browse
    url: /results/predictions/browse/
  - title: Prediction Timing Ledger
    url: /results/predictions/timing/
  - title: Red-team FAQ
    url: /research-program/about/red-team-faq/
  meta:
    type: "Physics Ledger Appendix"
    status: "Canonical"
    updated: "April 2026"
---

One of the strongest first-contact red-team questions — raised explicitly in the April 2026 external assessments — is direct:

> "What is the fit-space? How many functional forms ι_τ^k · p/q with small integers were enumerated before each prediction was fixed? What is the expected number of sub-10-ppm coincidences one would find for a similar constant of similar algebraic complexity against the same measured constants, and how does the observed 15 at sub-10 ppm compare?"

This page answers the question as quantitatively as we can at first-pass level. The answer is not a statistical proof of non-coincidence — a full adversarial statistical analysis belongs to specialist review. But a first-order calculation is enough to separate "suspiciously plausible" from "numerologically inevitable," and the first-order calculation matters because it tells a reviewer whether a deeper analysis is worth their time.

## The null hypothesis

The null hypothesis to refute is: **the 15 sub-10-ppm agreements between τ-derived formulas and measured constants are a numerological coincidence produced by enumerating simple functional forms in a single constant until hits are found.**

To assess this null, three quantities matter:

1. **The fit-space size.** How many distinct "simple closed-form expressions in ι_τ" exist, where "simple" is bounded by integer coefficients, small exponents, and shallow composition depth?
2. **The target-space size.** How many independently measured physical constants exist at precision comparable to sub-10 ppm?
3. **The per-target hit probability.** For a random simple closed-form expression in ι_τ (drawn from the fit-space), what is the probability that its numerical value agrees with a specific target measurement at sub-10 ppm?

With these three numbers, the expected number of coincidence hits under the null is: **Fit-space size × Target-space size × Per-target hit probability**.

## First-order estimates

### 1. Fit-space size — how many "simple closed forms" in ι_τ?

Simple closed-form expressions of the shape **ι_τ^k · p/q** (where k is an integer with |k| ≤ 20, and p/q is a rational with small positive integers p, q ≤ 20) give approximately:

**20 (values of k) × 400 (p/q pairs) ≈ 8,000 first-order expressions**

Including slightly more complex forms like **ι_τ^k · (a+b·ι_τ)/(c+d·ι_τ)** with small integers, the count rises to perhaps **10^4 to 10^5** expressions. This is a conservative estimate; more permissive definitions of "simple" (allowing deeper composition, more integer bounds, or small transcendental factors like π and e separately) can push this to **10^6 or higher**.

For the first-order calculation we use **10^5** — a generous estimate that favors the null hypothesis.

### 2. Target-space size — how many independently measured constants?

Well-measured dimensionless physical constants with central values at precision ≥ 10^-5 (i.e., sub-10 ppm measurement precision):

- **Atomic / QED / electroweak:** α, α_s, sin²θ_W, Koide Q, muon g−2, electron/muon/tau mass ratios, proton/electron mass ratio, muon anomaly — roughly **20 constants**
- **Cosmological:** h, Ω_m, Ω_b, Ω_Λ, n_s, σ_8, A_s, τ_reion, T_CMB — roughly **10 constants**
- **Nuclear / QCD:** g_A/g_V, nucleon magnetic moments, selected quark mass ratios — roughly **10 constants**
- **Other (astrophysical ratios, particle lifetimes, etc.):** roughly **10 more**

Total: approximately **50 well-measured independent constants** at sub-10 ppm precision.

### 3. Per-target hit probability at sub-10 ppm

For a random simple closed-form expression evaluated against a specific target measurement with precision ≈ 10^-5, the probability of random coincidence at that level is approximately **2 × 10^-5** (the target's effective half-width relative to a reasonable dynamic range).

### Expected hits under the null

**Expected sub-10 ppm coincidences = 10^5 × 50 × 2 × 10^-5 = 100.**

At face value this is *more* than the 15 observed — which would seem to *support* the numerology hypothesis.

## Why this first-order estimate is misleading

But the first-order calculation has five structural problems that all push the expected coincidence rate *downward* relative to the naive 100, or push the observed rate's significance *upward* relative to 15:

### Problem 1: The observed predictions are not individually selected hits

If the null hypothesis were right, one would see: a researcher enumerates simple expressions, finds the few that happen to match measured constants at sub-10 ppm, and keeps those. The fit-space is effectively pruned to the hits. Critically, **the hits should be scattered across unrelated constants** — one expression per target, no structural relationship between the expressions.

What the framework instead reports is **a connected derivation chain**: the electron mass derives in 10 steps from K0–K6; the Koide relation derives from σ-equivariant mass-matrix symmetry; the Higgs mass derives from ω-crossing sector structure. These derivations share load-bearing intermediate theorems. If one intermediate theorem is wrong, **many downstream predictions fail together**. This is not the signature of independent coincidence hunting — it is the signature of a single kernel under compound empirical pressure.

**Empirical test a specialist can run:** take any mid-chain τ-theorem (e.g., the sector-coupling hierarchy in IV.T−/V.T−), perturb it slightly (change one ratio by 1%), and check how many of the 67 predictions still agree at sub-10 ppm. Under the numerology hypothesis, perturbation should leave most hits intact (because each is its own isolated coincidence). Under the derivation hypothesis, perturbation should break most hits simultaneously. The framework predicts the latter.

### Problem 2: The observed agreements span many orders of magnitude

A coincidence-hunt over a fixed fit-space would produce hits at roughly the fit-space's characteristic precision, typically 10^-3 to 10^-5 range. The framework reports 15 hits at **sub-10 ppm** (i.e., below 10^-5) — with the electron mass at **0.025 ppm** (below 10^-7). Hits at 10^-7 are roughly 100x rarer than 10^-5 in a random search; the expected coincidence count at that precision under the null is not 100 but **~1**.

The observed 15 at sub-10 ppm, including one at 0.025 ppm, is *not* what 10^5 × 50 × (10^-5) gives. The tail of the precision distribution matters and in the observed data the tail is heavy in a way uncharacteristic of pure-coincidence enumeration.

### Problem 3: The constant ι_τ itself is structurally selected, not numerologically chosen

The null hypothesis assumes the researcher had free choice of **constant** and **form**. In fact:

- The constant is fixed as **ι_τ = 2/(π+e)** by the kernel's compactness-and-consistency theorem (Book I), **before** any prediction is attempted.
- The form of expressions available is also constrained by the derivation chain, not free enumeration — one cannot arbitrarily write "ι_τ^5 · 17/3" unless the derivation chain produces it.

Both constraints are visible in the Lean formalization: expressions entering the Physics Ledger are outputs of formal derivations, not post-hoc searches.

**Empirical test a specialist can run:** attempt to replace ι_τ with a close-but-different constant (e.g., 2/(π+e+ε) for small ε) throughout the derivation chain. How many predictions still agree at sub-10 ppm? Under numerology, swapping ι_τ for any nearby constant should yield comparable hit rates (the form was chosen, the constant was free). Under structural derivation, only ι_τ itself yields the observed hit distribution.

### Problem 4: Dimensional / scale-setting constraints reduce the effective fit-space

A random closed-form expression in ι_τ has no guarantee of being **dimensionally correct** as a ratio against a measured constant. Most of the 10^5 expressions we enumerated will be dimensionally absurd (e.g., trying to predict α using an expression with the wrong scaling). The effective fit-space per target, after dimensional constraints, is roughly **10^3 to 10^4** — not 10^5.

Updated expected hits: **10^3.5 × 50 × 2 × 10^-5 ≈ 3**, with the observed 15 being roughly 5× above expected. Not a statistical slam-dunk against the null, but meaningfully above chance.

### Problem 5: Category-C forward predictions are not part of the "hit rate"

The strongest evidence against numerology is **Category-C forward predictions**: quantities that were not yet measured when the framework published them. A numerology enumeration cannot hit a not-yet-measured quantity by coincidence — there is no target to coincide with.

The framework commits to **7 Category-C forward predictions** ([Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }})) including CMB-S4 r = ι_τ^4 ≈ 0.01363 at 14σ discriminant power. **If even one of these is confirmed at published precision**, the numerology null hypothesis is decisively refuted — no fit-space enumeration can coincide with an unmeasured quantity.

Category-C is the framework's actual counter-proof. The fit-space analysis above is framework-level honest accounting; the **decisive** rejection of the numerology hypothesis happens at the Category-C experiments.

## What this page does NOT claim

- **It does not claim the 15 sub-10-ppm agreements are statistically extraordinary** in a formal adversarial-statistics sense. A rigorous analysis — with specific fit-space enumeration code, target-list curation, and a formal hypothesis test — belongs to specialist review.
- **It does not claim the compound-derivation argument (Problem 1) is formally proven**. The claim that perturbing an intermediate theorem breaks many predictions together is testable but the test has not been run in published form.
- **It does not claim the framework's honest first-order estimate of expected-hits-under-null is dispositive**. It is a first-order calculation that puts the observed rate in the "meaningfully above chance" region, not the "overwhelmingly above chance" region.

What the page claims is that **the numerology hypothesis is testable, that the framework has committed to making those tests concrete (Category-C predictions), and that first-order analysis does not support the null strongly enough to dismiss the framework on coincidence grounds**. The decisive test lies ahead.

## What a statistician would need to do

A formal adversarial fit-space analysis requires:

1. **Enumerate the fit-space explicitly.** Produce a concrete, reproducible enumeration of "simple closed-form expressions in ι_τ" under a precise specification — not a heuristic estimate. Specify the upper bound on composition depth, integer size, and operator set.
2. **Curate the target list.** Publish the exact list of measurement targets, their published precision, their measurement source, and their statistical independence structure. Correlations between targets matter.
3. **Define the search procedure under the null.** Specify exactly how a random-enumeration process would generate candidates and match them to targets, including any dimensional / scale-setting heuristics that would be applied.
4. **Compute the exact expected-hit distribution.** Monte-Carlo the enumeration against the target list with the null procedure and derive the full distribution of expected sub-10-ppm hits.
5. **Compare observed to expected.** Compute the p-value of 15 observed sub-10-ppm hits under the null.
6. **Adversarial choice of free parameters.** Allow the null-hypothesis advocate to choose the fit-space specification and target list in the way that maximizes the null's apparent plausibility. The framework's rebuttal must survive the adversarial choice.

This is a statistics PhD thesis worth of work, not a first-pass dossier item. The framework welcomes and publicly commits to cooperation with any specialist who wants to run this analysis.

## Cross-links

- [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}) — the three-category breakdown (Category C is the decisive test)
- [Predictions Browse]({{ '/results/predictions/browse/' | relative_url }}) — the full 67-prediction catalogue
- [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}) — 30 named-experiment tests
- [Red-team FAQ]({{ '/research-program/about/red-team-faq/' | relative_url }}) — the 10 hardest first-contact questions
- [How to Audit — Physicist Route]({{ '/verify/how-to-audit/physicist/' | relative_url }}) — concrete inspection path for a physics reviewer
