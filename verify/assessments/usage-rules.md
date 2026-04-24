---
layout: program-doc
title: "Usage Rules"
lane: verify
permalink: /verify/assessments/usage-rules/
summary_short: "Ten rules governing responsible use of the AI-assisted first-pass assessment protocol --- what the protocol may be used for, what it must not be mistaken for, and how to handle its outputs."
summary_cards:
  - title: "10 rules"
    body: "Governing evidence, confidence, claim types, uncertainty, and the proper scope of AI-generated dossiers."
  - title: "Core principle"
    body: "The protocol produces structured first signals, not verdicts. Every dossier is the beginning of review, not the end."
  - title: "Responsibility"
    body: "Anyone who uses the protocol is responsible for understanding what it does and does not establish."
right_rail:
  related:
    - title: "Assessment Protocols"
      url: /verify/assessments/
    - title: "Methodology"
      url: /verify/assessments/methodology/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Verify Overview"
      url: /verify/
  meta:
    type: "Assessment Protocol"
    status: "Published"
    updated: "April 2026"
---

## Rules for Responsible Use

The following ten rules govern the responsible use of the AI-assisted first-pass assessment protocol. Anyone running the protocol should read and understand these rules before producing or citing a dossier.


### Rule 1 --- Public Materials Only

Do not upload confidential manuscripts, reviewer correspondence, private drafts, or any other non-public documents into general-purpose AI systems.

The protocol is designed to work entirely from public materials --- the main site, Guided Tours, Lean companions, TauLib source, and published books. This constraint is deliberate: it ensures that any outsider can reproduce the assessment from the same sources, and it protects the integrity of unpublished work.


### Rule 2 --- AI Is a Dossier Engine, Not a Verdict Engine

Use the model to extract claims, classify methods, identify visible strengths and vulnerabilities, and produce a typed dossier. Do not use it as a substitute for expert adjudication.

The distinction matters. A frontier model can organize and structure an assessment with considerable skill. It cannot determine whether a novel mathematical derivation is correct, whether a physical bridge claim is sound, or whether a result constitutes genuine priority over existing work. Those judgments require human experts.


### Rule 3 --- Separate Truth from Review-Worthiness

A positive outcome on this protocol means three things: the work appears serious enough to deserve scrutiny, the claims may be novel enough to warrant expert attention, and the likely impact could be large if the claims hold.

It does **not** mean the work is proven true, that peer review is no longer necessary, or that expert disagreement has been resolved. The protocol assesses review-worthiness, not correctness. Conflating the two is the most common misuse.


### Rule 4 --- Confidence Is Local, Not Global

Confidence scores must refer to specific, bounded dimensions: evidence visibility, adequacy of public documentation, apparent novelty signals, clarity of dependencies, and the assessment's own reliability.

Do not assign a single global truth score. A dossier that reports "overall confidence: 78%" has exceeded its epistemic authority. A dossier that reports "high confidence in inspectability, medium confidence in novelty plausibility, low confidence on priority without domain experts" has stayed within its proper scope.


### Rule 5 --- Demand Explicit Evidence

The model must quote or paraphrase the exact visible evidence for each judgment. No assessment should rest on an unsupported assertion by the model.

This rule exists because frontier models can produce confident-sounding evaluations that are not grounded in the source material. By requiring explicit citation of evidence, the protocol makes it possible for a human reader to verify each judgment independently.


### Rule 6 --- Distinguish Claim Types

At minimum, the model should distinguish five categories of claims:

- **Internal derivation claims** --- results that follow from the framework's own axioms
- **Bridge claims** --- identifications between internal structures and external mathematics or physics
- **Empirical mapping claims** --- predictions that can be tested against experiment
- **Interpretive or worldview claims** --- readings of what the framework means for broader questions
- **Commitment or stance implications** --- positions the framework entails on contested philosophical questions

These categories carry different epistemic weight and require different kinds of expert review. A dossier that treats all claims as equivalent has failed to apply the protocol correctly.


### Rule 7 --- Require "What Would Change My Mind?"

For each major positive judgment, the dossier should name what additional human evidence would be required to strengthen it or to weaken it.

This rule enforces intellectual honesty. A dossier that asserts strong novelty signals without naming the prior-art checks that could undermine that judgment is incomplete. The point is not to weaken the assessment but to make its conditionality visible.


### Rule 8 --- Never Hide Uncertainty

The dossier should explicitly mark every point where the assessment reaches the boundary of what public materials and AI analysis can establish:

- Where human experts are required
- Where prior-art review is required
- Where correctness cannot be judged from public materials alone
- Where the model may be extrapolating beyond the evidence

Uncertainty is not a weakness of the dossier --- it is part of its content. A dossier that presents clean conclusions without marking their limits has concealed the most important information.


### Rule 9 --- Use Multiple Models If Possible

If the stakes of the assessment are high, run the protocol on more than one frontier model and compare the results. Look for:

- **Convergence** --- where do different models agree?
- **Divergence** --- where do they disagree, and why?
- **Missing points** --- what does one model catch that another misses?
- **Different vulnerability emphasis** --- do the models identify different weak points?

Cross-model comparison does not guarantee correctness, but it reduces the risk of systematic blind spots inherent in any single model.


### Rule 10 --- Treat the Dossier as the Beginning of Review

The right output of the protocol is not "done." The right output is:

- A **structured first signal** that organizes the preliminary evidence
- An **attack surface** that identifies where the framework is most vulnerable
- A **map** of where deeper human scrutiny should go next

The dossier is a starting point for expert engagement, not an endpoint. Anyone who treats a first-pass dossier as a final assessment has misunderstood the protocol's purpose and exceeded its designed scope.
