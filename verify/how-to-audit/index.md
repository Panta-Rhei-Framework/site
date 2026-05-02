---
layout: program-doc
title: "How to Audit — Per-Reviewer Routes"
permalink: /verify/how-to-audit/
lane: verify
v2_lane: verify
type: "Inspection Pathway Hub"
status: "Canonical"
summary_short: "Concrete inspection pathways by reviewer role. If you are a formal methods expert, a mathematician, a physicist, a philosopher, a prior-art specialist, or a journalist/skeptic, each route names exactly where to start, what to check first, and what would most efficiently settle your strongest skeptical question."
plain_language_summary: "Different reviewers have different fastest disconfirmation paths. A Lean specialist can check a single theorem in 20 minutes. A physicist needs to evaluate whether ι_τ is fitted or forced. A philosopher needs to check whether 'consciousness emerges from K_χ amplification' is a derivation or a redefinition. A journalist or skeptic needs a 15-minute scan to decide whether the program is serious enough to even cover. This page is the routing layer: pick your role below, and the linked page tells you what to clone, what to grep, what to suspect, and what would most efficiently settle your strongest objection."
right_rail:
  related:
    - title: "Verify Overview"
      url: /verify/
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Red-team FAQ"
      url: /program/about/red-team-faq/
    - title: "Prior-Art Comparisons"
      url: /program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/
  meta:
    type: "Inspection Pathway Hub"
    scope: "All reviewer roles"
    status: "Canonical"
    updated: "April 2026"
---

A research program this broad cannot be meaningfully audited in one sitting, and a generic "read the books" invitation is not a serious call to scrutiny. This page is a **hub of role-specific inspection routes**, each written for the reviewer who is most likely to find the decisive weakness in a particular claim family.

If you land here with a specific background, use your route directly. If you land without a specific expertise, the journalist/skeptic route is your starting point.

Each route is designed around three principles:

1. **Concrete first actions** — a specific URL to open, a specific command to run, a specific theorem ID to trace. Not "explore the framework" but "open X, run Y, check Z."
2. **Fail-fast checks** — the fastest path to discovering the most likely structural weakness in your domain. Not the most charitable path; the most *efficient* disconfirmation path.
3. **Load-bearing pointers** — each route names the load-bearing evidence that must hold for the claim in that domain to survive, and where specifically to find it.

These pages do not argue that the framework is correct. They argue that if you want to form a defensible opinion, here is the shortest route to the relevant evidence.

## Pick your role

### [Formal Methods / Proof Assistant Expert]({{ '/verify/how-to-audit/formal-methods/' | relative_url }})

If you work with Lean 4, Mathlib, Coq, Agda, Isabelle, or other proof assistants, the load-bearing question is whether TauLib's claimed formalization state (0 `sorry` across all 7 books, 3 named custom axioms in Book III, ~4,863 theorems, ~142K lines, plus the disclosed `native_decide` TCB extension) matches what actually compiles. This is the single most diagnostic check any reviewer can run.

### [Mathematician]({{ '/verify/how-to-audit/mathematician/' | relative_url }})

If you work in category theory, model theory, analytic number theory, operator theory, several complex variables, or algebraic geometry, specific headline theorems in Books I–III are where the framework's internal mathematical spine either holds or fails. Three theorems are particularly load-bearing: **I.T** (categoricity + rigidity of τ), **II.T40** (Central Theorem 𝒪(τ³) ≅ A_spec(𝕃)), and **III.T19** (Critical Line Theorem).

### [Physicist]({{ '/verify/how-to-audit/physicist/' | relative_url }})

If you work in particle physics, cosmology, quantum foundations, or general relativity, the empirical track of the framework lives in the 67-prediction Numerical Physics Ledger and in the 30-item Falsification Pack. The load-bearing questions are whether ι<sub>τ</sub> is fitted or forced, whether the predictions are a priori or post-dictions, and whether the single-constant derivation chains survive independent checking.

### [Philosopher (of science, mind, or metaphysics)]({{ '/verify/how-to-audit/philosopher/' | relative_url }})

If you work in philosophy of science, philosophy of mind, metaphysics, epistemology, ethics, or aesthetics, Books VI and VII contain the framework's most conceptually exposed claims — τ-life definition, consciousness as global section, Categorical Imperative derivation, structural realism. The load-bearing question is whether these claims are formal derivations or redefinitions of target phenomena inside the framework's vocabulary.

### [Prior-Art Specialist]({{ '/verify/how-to-audit/prior-art-specialist/' | relative_url }})

If you are a specialist in one of five literature-rich zones — Fueter-regular / quaternionic analysis, Hilbert-Pólya / Connes spectral programs, Furey / octonionic Standard Model, autopoiesis / IIT / FEP, or MOND / Verlinde / entropic gravity — the load-bearing question is whether τ's claims in your zone are genuinely new or an isomorphic relabeling of existing work. Five comparison pages are the starting point.

### [Journalist, Skeptic, or Generalist]({{ '/verify/how-to-audit/journalist-skeptic/' | relative_url }})

If you are arriving without specific domain expertise but want to evaluate whether the program warrants a closer look, the shortest-path tour covers the Release Manifest, the Red-team FAQ, and two specific load-bearing theorems that a non-specialist can still spot-check at the level of "does the scaffolding exist and does it claim what it says?"

---

## What this hub does NOT promise

- It does not claim that following a route will *settle* the framework's correctness for your domain. Correctness requires deeper engagement than any inspection pathway can provide on its own.
- It does not claim the routes are neutral. They are written by the framework's authors and therefore have a built-in sympathetic bias. The fail-fast design is intended to counter that bias by pointing at the most likely disconfirmation paths, but a hostile reviewer should expect to find issues the routes do not pre-disclose.
- It does not replace peer review. These routes are first-contact pathways, not referee reports.

## How this hub was built

The six routes correspond to the five specialist roles plus the generalist role named in the three frontier-LLM first-pass assessments of April 2026 ([Compass]({{ '/verify/assessments/' | relative_url }}), Deep Research, and Gate-1/2/3 dossier). Each assessment recommended role-specific external validation; this hub operationalizes that recommendation by naming exactly where each role should start.

## Cross-links

- [Verify Overview]({{ '/verify/' | relative_url }}) — the verify lane's top-level entry
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — pinned commit, build status, drift reconciliation (every route should start here)
- [Red-team FAQ]({{ '/program/about/red-team-faq/' | relative_url }}) — the 10 hardest first-contact questions
- [Prior-Art Comparisons]({{ '/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }}) — specialist-level comparisons across five zones
- [Scope, Status & Scrutiny]({{ '/program/about/scope-status-and-scrutiny/' | relative_url }}) — the program's own methodological self-description
