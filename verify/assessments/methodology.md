---
layout: program-doc
title: "Assessment Methodology"
lane: verify
permalink: /verify/assessments/methodology/
summary_short: "Why this protocol exists, what question it answers, how it uses three gates, and what AI can and cannot do in a first-pass assessment."
summary_cards:
  - title: "The question it answers"
    body: "Not 'is this true?' but 'does this appear to be a serious, inspectable, review-worthy research artifact --- and where should expert scrutiny begin?'"
  - title: "Three gates"
    body: "Research-form legitimacy, novelty and relevance, impact and salvage value. Each gate is scored independently; no global truth score is produced."
  - title: "Public materials only"
    body: "The protocol runs on public Atlas materials, Guided Tours, Lean companions, TauLib source, and published books. No confidential documents are used."
right_rail:
  related:
    - title: "Assessment Protocols"
      url: /verify/assessments/
    - title: "Usage Rules"
      url: /verify/assessments/usage-rules/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Verify Overview"
      url: /verify/
  meta:
    type: "Assessment Protocol"
    status: "Published"
    updated: "April 2026"
---

## Why This Protocol Exists

The Panta Rhei Research Program makes unusually large claims across mathematics, physics, life sciences, and metaphysics. When a research architecture spans this many domains, many outsiders face a preliminary question before they invest serious human time:

> Is this worth looking at seriously, and if so, where should scrutiny begin?

This protocol is designed to answer that preliminary question in a disciplined way. It provides a structured method for producing an initial dossier --- not a verdict, but a first signal that is more rigorous than a casual impression and more transparent than an unstructured opinion.


## What Question It Answers

The protocol does **not** attempt to answer:

> "Is this true?"

It attempts to answer:

> "Does this appear to be a serious, inspectable, review-worthy research artifact; do its claims seem potentially novel and relevant; and where should further expert scrutiny begin?"

This distinction is fundamental. Large research architectures are difficult to evaluate from headlines alone. The protocol helps readers separate structure from rhetoric, identify visible methods and load-bearing hinges, distinguish internal claims from broader bridge claims, and produce a structured first-pass assessment.


## The Three Gates

The protocol is built around three gates, applied in sequence.

### Gate 1 --- Research-Form Legitimacy

Does the work look like a serious research artifact that has earned external scrutiny?

This gate examines:

- Whether claims are typed and inspectable
- Whether methods are stated and visible
- Whether the load-bearing hinges and dependencies are identifiable
- Whether reproducibility routes are available (formalization, claim maps, tours, repositories)
- Whether falsification routes are named
- Whether the project distinguishes internal derivation, bridge claims, empirical mappings, and worldview or commitment readings

### Gate 2 --- Novelty and Relevance

If Gate 1 is passed, do the claims appear genuinely novel and materially relevant relative to frontier work in the domains addressed?

This gate examines:

- Likely novelty signals
- Likely rediscovery risks
- Priority-check needs
- Field relevance and disciplinary fit
- Specificity of contribution

### Gate 3 --- Impact and Salvage Value

Under three scenarios, what appears to be the likely magnitude of contribution?

1. **If the core claims substantially hold** --- what is the potential scale of the contribution?
2. **If the claims hold partially or with major bridge weakness** --- what significant value remains?
3. **If the core spine fails, but the project remains methodologically serious** --- what tools, formalizations, taxonomies, or conceptual structures would still be reusable?


## What AI Can Do Well Here

A frontier model is well suited to several tasks in this context:

- **Extracting claims** from structured source material
- **Classifying claim types** (internal derivation, bridge, empirical, interpretive)
- **Identifying visible methods** and their scope
- **Comparing stated claims** to mainstream domain structures
- **Generating counter-questions** that a human reviewer should address
- **Producing typed, review-ready dossiers** in a consistent format


## What AI Should Not Be Trusted to Do Alone

A frontier model should **not** be treated as authoritative on:

- **Correctness** of the strongest mathematical derivations
- **Correctness** of physical bridge mappings
- **Definitive scholarly priority** --- whether a result is genuinely novel or a rediscovery
- **Peer-review verdicts** --- the model cannot substitute for expert adjudication
- **Truth-probabilities** on the overall framework

These determinations require human experts with domain-specific training.


## The Confidence Rule

The protocol should never assign a single global truth-probability. Confidence in this context refers to **evidence visibility and assessment scope**, not to the likelihood that the framework is correct. For example:

- **High confidence** that the work is inspectable (because the public documentation is extensive)
- **Medium confidence** that novelty signals appear plausible (because domain prior-art review has not been completed)
- **Low confidence** on definitive priority without human experts
- **Low confidence** on correctness of the strongest claims without human verification

This is a deliberate constraint. A dossier that assigns "85% likely true" has exceeded its epistemic authority. A dossier that reports "high evidence visibility, medium novelty plausibility, low priority certainty" has stayed within its proper scope.


## The Correct Output Type

The protocol should yield five deliverables:

1. A **typed dossier** --- structured, claim-level analysis organized by gate
2. A **three-gate scorecard** --- the 17-criterion rubric filled with 0--4 scores and confidence labels
3. A **list of required external validations** --- what human experts would need to check
4. A **review-readiness judgment** --- whether the work has earned structured expert scrutiny
5. A **next-step recommendation** --- where deeper human review should begin

This is the correct use of AI in this setting: **structured triage under human oversight**.


## Audience

The protocol is designed for journalists, critics, policymakers, investors, and domain experts who need a disciplined first signal. It is not designed for casual readers or for use as a substitute for expert engagement. Anyone who uses this protocol should read the [Usage Rules]({{ '/verify/assessments/usage-rules/' | relative_url }}) before running a prompt.


## Public Materials Only

The protocol is intended to be run exclusively on public materials:

- Public Atlas materials at [panta-rhei.site](https://panta-rhei.site)
- Public Guided Tours
- Public Lean companions and TauLib source
- Published books
- Public talks, interviews, and clarifications

Do not upload confidential, unpublished, or third-party restricted materials into general-purpose AI systems. The protocol is designed so that any outsider can reproduce it from public sources alone.
