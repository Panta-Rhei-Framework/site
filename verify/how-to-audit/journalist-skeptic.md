---
layout: program-doc
title: "How to Audit — Journalist / Skeptic / Generalist Route"
permalink: /verify/how-to-audit/journalist-skeptic/
lane: verify
v2_lane: verify
type: "Inspection Route"
status: "Canonical"
summary_short: "For journalists, science writers, skeptics, and generalist readers without deep domain expertise. A 15-minute scan that lets you decide whether the program is serious enough to warrant coverage or closer inspection — and what to ask a specialist if you go deeper."
plain_language_summary: "You don't need to be a Lean specialist or a particle physicist to evaluate whether this program is worth your attention. In 15 minutes you can answer: does it ship machine-checkable code? (yes — TauLib in public Lean 4). Does it commit to specific empirical predictions on a fixed timeline? (yes — 67 Numerical Predictions + 30 Falsifications, with named experiments for 2025–2035). Does it disclose its trust budget? (yes — three custom axioms named, zero sorries, TCB explicitly walled). Does it survive its own announced failure modes? (the Falsification Pack is the answer in 5 years). The page below is the 15-minute checklist plus a script of questions to put to a specialist if you decide to go deeper."
right_rail:
  related:
    - title: "How to Audit (Hub)"
      url: /verify/how-to-audit/
    - title: "Red-team FAQ"
      url: /program/about/red-team-faq/
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Media Kit"
      url: /media/
  meta:
    type: "Inspection Route"
    scope: "Generalist audit"
    status: "Canonical"
    updated: "April 2026"
---

This route is for anyone arriving at the program without deep domain expertise who wants to decide, quickly and honestly, whether the work is serious enough to warrant further attention — a second look, a specialist referral, a story, a closer read.

Being skeptical of ambitious theoretical programs is the right default. The framework's authors know this. The question this route helps you settle is not "is the framework right?" — a question you cannot answer on your own in 15 minutes — but "is the framework the kind of object that deserves more scrutiny, or is it one that can be safely dismissed?"

## The 15-minute scan

### Step 1 — Read the Red-team FAQ (~5 min)

Open the [Red-team FAQ]({{ '/program/about/red-team-faq/' | relative_url }}). These are the ten hardest first-contact skeptical questions, synthesized from three independent frontier-LLM first-pass assessments. Each is answered with honest reference to load-bearing evidence.

**What to check as you read:**
- Are the questions themselves the right questions? A framework's FAQ that answers easy questions is a marketing document; a framework's FAQ that answers hard questions is a research document.
- Are the answers direct or evasive? An evasive answer on "Is ι<sub>τ</sub> fitted?" would be a strong negative signal.
- Do the answers contain pointers to specific theorems, specific Lean files, specific registry IDs? If yes, the framework is inviting technical verification; if no, it is asking for trust.

Healthy signal: answers that say "here's what's proved, here's what isn't, and here's the Lean file that confirms it."

### Step 2 — Open the Release Manifest (~3 min)

Open the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}). This is the single-view snapshot of what the framework claims at the pinned commit level:

- Pinned commit SHA, Lean version, Mathlib version
- `sorry` count (should be 0, across all 7 books, post peer-review-fixes-v1)
- Custom axiom count (should be 3, all in Book III — spectral / number-theoretic bridges)
- Per-book reconciliation table showing counts across three surfaces

**What to check:**
- Does the Release Manifest flag drift between surfaces honestly? A research program that hides inconsistencies between its own summary pages is not review-ready; one that documents them is.
- Is there a "what this release does NOT claim" section? A framework that can list what it does not claim is one that has thought about its limits. A framework that only states positive claims has not.

The Release Manifest explicitly lists: "no Book VII formalization", "no proof-assistant verification of the physics bridge", "Millennium resolutions not Clay-valid formulations". That kind of transparency is the signal.

### Step 3 — Check a single falsification test (~5 min)

Open the [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}) and read entry **N1 — CMB-S4 tensor-to-scalar ratio**. The framework predicts **r = ι<sub>τ</sub><sup>4</sup> ≈ 0.01363**, with CMB-S4 experimental sensitivity giving 14σ discriminant power over the 2028–2035 observing window.

**What this tells you:**
- The framework commits to a specific number derived from a single constant.
- The test is a real experiment on a published timeline.
- If the measurement comes in inconsistent at 5σ, the framework's cosmological sector fails by its own stated criterion.

A program willing to stake its cosmology on one future measurement is behaving like science, not like speculation. A program that says "we'll adjust if needed" is not.

### Step 4 — Glance at the claim surface (~2 min)

Open [Browse All Results]({{ '/results/browse/' | relative_url }}) and skim. The catalogue surfaces 234 typed results across four domains. Pay attention to the status codes:

- **R (Internally addressed)** — full τ-internal theorem
- **P (Partial)** — theorem with conjectural bridge to orthodox formulation
- **Q (Qualitative)** — non-quantitative
- **C (Contradicted)** — framework takes an opposing position (3 claims: No Hawking Radiation, Panpsychism Excluded, ZFC Identity Slippage)
- **N (Not Addressed)** — open question

**Signal:** the Contradicted-status claims are a crucial test. A rhetorical-overreach framework would mark nothing as Contradicted (everything is resolved or ignored). A research-disciplined framework contradicts specific live positions and is accountable for those contradictions. Three is a small but non-zero number — consistent with a framework that takes falsifiable positions where the structure gives it reason to, and stays quiet where it doesn't.

## What you can decide after 15 minutes

After this scan, you can form a defensible judgment on one question: **is the framework the kind of object that deserves closer inspection?**

Negative signals (any of which is disqualifying):
- Red-team FAQ evades rather than answers.
- Release Manifest hides or does not document drift across surfaces.
- N1 CMB-S4 prediction is not a closed-form expression.
- No Contradicted-status claims; every claim is either resolved or deferred.

Positive signals (together these suggest the framework deserves follow-up):
- Red-team FAQ answers hard questions with pointers to concrete theorems.
- Release Manifest explicitly names drift and limitations.
- N1 prediction is r = ι<sub>τ</sub><sup>4</sup> = closed form with stated σ threshold.
- At least one Contradicted stance on a live position.

## What to do next

If the 15-minute scan is positive and you want to go deeper:

- **If you have a specific technical background,** take the corresponding route: [formal methods]({{ '/verify/how-to-audit/formal-methods/' | relative_url }}), [mathematician]({{ '/verify/how-to-audit/mathematician/' | relative_url }}), [physicist]({{ '/verify/how-to-audit/physicist/' | relative_url }}), [philosopher]({{ '/verify/how-to-audit/philosopher/' | relative_url }}), or [prior-art specialist]({{ '/verify/how-to-audit/prior-art-specialist/' | relative_url }}).
- **If you're writing about the program,** the [Media Kit]({{ '/media/' | relative_url }}) has structured assets, and the [Review Kit]({{ '/media/review-kit/' | relative_url }}) includes reviewer-ready materials.
- **If you want to find a specialist,** [contact the program]({{ '/engage/contact/' | relative_url }}) — the authors can help connect you with a domain reviewer they have engaged with.

## The honest framing

This 15-minute scan is designed to separate "framework worth taking seriously" from "framework worth ignoring." It is not designed to settle "framework correct" from "framework wrong" — no generalist scan can do that. Correctness requires specialist engagement in each domain, and the other five routes in this hub operationalize that engagement.

What the scan *can* establish is whether the framework is the kind of object that makes itself technically inspectable, publishes its own limitations, commits to falsifiable predictions, and contradicts specific live positions. A framework that does all four is review-worthy, whatever its eventual fate turns out to be.

A framework that does none of these is pseudoscience theatre, regardless of how sophisticated its presentation.

This framework, on the scan above, does all four. What to conclude from that is up to you.

## Cross-links

- [Red-team FAQ]({{ '/program/about/red-team-faq/' | relative_url }}) — the 10 hardest first-contact questions, answered
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — pinned commit snapshot with honest drift reconciliation
- [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}) — 30 named-experiment tests
- [Media Kit]({{ '/media/' | relative_url }}) — press and review resources
- [How to Audit (Hub)]({{ '/verify/how-to-audit/' | relative_url }}) — all six reviewer routes
