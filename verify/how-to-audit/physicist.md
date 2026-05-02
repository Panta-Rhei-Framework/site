---
layout: program-doc
title: "How to Audit — Physicist Route"
permalink: /verify/how-to-audit/physicist/
lane: verify
v2_lane: verify
type: "Inspection Route"
status: "Canonical"
summary_short: "For specialists in particle physics, cosmology, quantum foundations, or general relativity. The 67-prediction Numerical Physics Ledger and the 30-item Falsification Pack are the empirical track; the load-bearing questions are whether ι<sub>τ</sub> is fitted or forced, whether the predictions are a priori or post-dictions, and whether the derivation chains survive independent checking."
plain_language_summary: "If you do physics professionally, the framework's most exposed claim is this: every numerical SI value in the Standard Model and cosmology comes out as an ι_τ-chain expression times an m_n-anchored dimensional factor. There are 67 such derivations on offer, with sub-ppm precision in the flagship cases. Your two load-bearing questions are: (1) is ι_τ ≈ 0.341304 a fitted parameter or a forced consequence? and (2) are the predictions genuinely a priori, or after-the-fact post-dictions? The page below tells you exactly where to look in TauLib for the derivations, where the published prediction timing and falsification timeline is, and what would settle each question for you."
right_rail:
  related:
    - title: "How to Audit (Hub)"
      url: /verify/how-to-audit/
    - title: "Master Constant Hinge"
      url: /corpus/foundational-hinges/master-constant-iota-tau/
    - title: "Predictions Browse"
      url: /results/predictions/browse/
    - title: "Falsification Pack"
      url: /results/falsifications/browse/
    - title: "Prediction Timing Ledger"
      url: /results/predictions/timing/
  meta:
    type: "Inspection Route"
    scope: "Physics claims audit"
    status: "Canonical"
    updated: "April 2026"
---

This route is for physicists evaluating the framework's empirical content. Books IV and V are the primary technical references, but the load-bearing claims sit in three specific artifacts that you can inspect in under two hours.

Before reading the numerical physics ledger, inspect whether the master constant is kernel-forced:

- [Hinge 3 — The Master Constant iota_tau]({{ '/corpus/foundational-hinges/master-constant-iota-tau/' | relative_url }})
- [The Master Constant iota_tau research paper]({{ '/publications/research-papers/master-constant-iota-tau/' | relative_url }})
- [Download the Master Constant PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-master-constant-iota-tau.pdf' | relative_url }})
- DOI [10.5281/zenodo.19820352](https://doi.org/10.5281/zenodo.19820352)

If this hinge fails, the ledger may still contain numerical patterns, but it cannot carry the same zero-parameter foundation claim.

## The three artifacts to inspect first

### 1. The [Numerical Physics Ledger PDF]({{ '/assets/downloads/physics-ledger.pdf' | relative_url }}) (209 pp, 1.11 MB, free download)

Contains the full derivation chains for all 67 zero-parameter numerical predictions from ι<sub>τ</sub> = 2/(π+e). Every prediction compares a τ-derived value directly to experimental measurement, typically to Planck/PDG/CODATA central values, with ppm-scale deviations reported.

**Load-bearing questions to ask while reading:**

- Is ι<sub>τ</sub> genuinely forced by the kernel axioms, or is its value effectively chosen to match a calibration target (e.g., the electron mass)? See the explicit answer at [Is ι<sub>τ</sub> forced or fitted?]({{ '/program/about/red-team-faq/#is-iota-tau-fitted-or-forced' | relative_url }}).
- Does any prediction's derivation smuggle in an auxiliary numerical choice (e.g., an integer selected post-hoc, a branch of a multi-valued function)? This is the first place specialist attention should focus.
- For ratios and dimensionless quantities (α, sin²θ_W, Koide Q, etc.), the comparisons are unambiguous. For dimensionful quantities (masses, coupling constants with units), what mass scale / normalization convention is being used?

### 2. The [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }})

A-priori-vs-post-diction accounting of the 67 predictions. Breaks the ledger into three categories:

| Category | Count | Character |
|----------|:----:|-----------|
| **A — Pre-existing measured constants** | ~50 | Structural a priori; historical post-diction (retro-consistency surface) |
| **B — Tension resolutions** | ~10 | Forward commitment on open empirical tensions (Hubble h, W mass, muon g−2, S<sub>8</sub>) |
| **C — Genuine forward predictions** | ~7 | Decisive tests ahead of measurement (CMB-S4 r, 0νββ at τ half-life, Σm<sub>ν</sub>, proton stability, no monopoles) |

**Load-bearing questions:**
- Are the ~50 Category-A agreements independently generated (one derivation per constant) or do they share a common calibration move? A shared calibration that aligns one target would inflate the apparent success rate.
- Do the Category-B tension-resolution values sit cleanly on one side of the tension or are they compromise values within error bars of both sides? The former is forward-committed; the latter is a wait-and-see straddle.
- For Category-C, have the predictions been pre-registered with a public time-stamped repository? The framework does **not** claim this yet (stated explicitly on the Timing Ledger).

### 3. The [Falsification Pack (N1–N30)]({{ '/results/falsifications/browse/' | relative_url }})

30 named-experiment tests with 5σ thresholds on 2025–2035 timelines. Load-bearing entry:

- **N1: CMB-S4 tensor-to-scalar ratio** — τ predicts r = ι<sub>τ</sub><sup>4</sup> ≈ 0.01363. CMB-S4 sensitivity σ(r) ≈ 0.001 implies 14σ discriminant power. If measured r is inconsistent with 0.01363 at ≥5σ, the framework's cosmological sector fails. **This is the single sharpest falsification test of the entire program.**

Other decisive tests: 0νββ **detected at τ-predicted half-life** (non-detection or detection at an inconsistent half-life refutes the Majorana + C-sector-zero-holonomy prediction); proton decay null; magnetic monopole null; sparticle null at all scales.

## The 30-minute fail-fast path

If you have 30 minutes to form an initial opinion:

1. **Open the Numerical Physics Ledger PDF and read the derivation chain for the electron mass** (claimed to 0.025 ppm precision). This is the most-precise sub-10-ppm prediction and the most-scrutinizable single derivation. Check: does the derivation use a pre-existing parameter that was not fixed by the kernel structure?

2. **Open the Prediction Timing Ledger's Category-C section** and confirm you agree with the claim that 7 predictions are genuinely forward-test predictions (CMB-S4 r, 0νββ at τ-predicted half-life, Σm<sub>ν</sub>, proton stability, no monopoles, no sparticles, r-process-related). If you disagree with any, that is useful feedback.

3. **Pick one claim in your specialty** (e.g., muon g−2 if you work on precision electroweak; the Bullet Cluster if you work on dark matter phenomenology; the Hubble tension if you work on cosmology) and trace its claim page → its derivation → the relevant cosmology/particle briefing → the falsification entry.

4. **Ask whether the prediction's value is a *closed-form* expression in ι<sub>τ</sub> or an approximate numerical statement**. Closed-form is much harder to fake.

## The 2-hour deep check

For a physicist willing to invest two hours:

- **Read the Falsification Pack** (N1–N30) with attention to timeline and σ threshold per entry. Are the thresholds fair (consistent with published experimental sensitivity projections)? Are the timelines realistic?
- **Follow three claim pages** from the Cosmology briefing, each into its detailed derivation: Hubble tension (h formula), CMB first peak (+69 ppm), and Cosmological Constant Problem (V.T139 vacuum energy = 0). Evaluate whether the mechanisms are independent of each other or share a common calibration step.
- **Read the [Prior-Art Comparison: No Dark Sectors vs MOND/Verlinde]({{ '/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }})**. The page's "what a specialist would want to see" section names specific comparisons that should decide the relabeling question.
- **Check the CMB peak structure beyond the first peak.** The site documents the first peak at +69 ppm; does the framework predict the full peak structure (peaks 2, 3, 4...) with zero free continuous parameters, or only peak 1? This is a concrete fact-check.
- **Check the Bullet Cluster account.** No-dark-sectors programs must account for the weak-lensing / X-ray separation. If the site does not document a specific account of this observation, that is a gap to report.

## Fail-fast exits

Your audit is **negative** if:

- A single derivation in the Numerical Physics Ledger uses a free parameter you can spot. "Zero free parameters" is a hard claim that breaks on any single counterexample.
- Category-B tension resolutions are all straddle-values within both sides' error bars. The "forward commitment" framing would be dishonest.
- CMB-S4 prediction is not a closed-form expression in ι<sub>τ</sub> (it is claimed to be r = ι<sub>τ</sub><sup>4</sup> — verify this is what the derivation yields, not a number matched after the fact).
- The no-dark-sectors account cannot address the Bullet Cluster or similar cluster-scale observations in concrete terms.

Your audit is **positive** if:

- The electron mass derivation is closed-form in ι<sub>τ</sub> and agrees to 0.025 ppm without adjustable parameters.
- The Falsification Pack entries are concretely testable on their stated timelines with fair σ thresholds.
- The categorization in the Prediction Timing Ledger survives your domain-specific reading (~50 / ~10 / ~7 is roughly right).
- The framework's treatment of at least one observation in your specialty is technically defensible, even if you disagree with the framing.

A positive physics audit means the framework has earned its empirical-track review-readiness; it does not mean the predictions will survive future measurement. That is precisely what the Falsification Pack is designed to settle.

## What to escalate

If you identify a specific disagreement (e.g., "the derivation for Higgs self-coupling on page 87 uses a branch of a multi-valued function that is not justified"), [contact the program]({{ '/engage/contact/' | relative_url }}) with the specific reference. This kind of technical objection is the most valuable feedback possible.

If the audit is positive and you want to go deeper, the next route depends on interest: [Mathematician route]({{ '/verify/how-to-audit/mathematician/' | relative_url }}) for the derivation-machinery foundations, or [Prior-Art Specialist route]({{ '/verify/how-to-audit/prior-art-specialist/' | relative_url }}) for the no-dark-sectors / three-generation comparison.

## Cross-links

- [Physics Predictions Browse]({{ '/results/predictions/browse/' | relative_url }}) — filterable 67-prediction catalogue
- [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}) — 30 named-experiment tests
- [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}) — a-priori vs post-diction breakdown
- [Cosmology briefing]({{ '/results/fields/cosmology-astrophysics/' | relative_url }}) — the highest-stakes physics claim set
- [Particle Physics briefing]({{ '/results/fields/particle-physics/' | relative_url }}) — SM-sector claim set
- [Red-team FAQ]({{ '/program/about/red-team-faq/' | relative_url }}) — the 10 hardest first-contact questions
- [How to Audit (Hub)]({{ '/verify/how-to-audit/' | relative_url }}) — all six reviewer routes
