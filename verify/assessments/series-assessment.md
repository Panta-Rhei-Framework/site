---
layout: program-doc
title: "Series-Level Assessment Prompt"
lane: verify
permalink: /verify/assessments/series-assessment/
summary_short: "A full prompt template for assessing the entire Panta Rhei research architecture across three gates."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Book-Level Prompt"
      url: /verify/assessments/book-assessment/
    - title: "Domain-Level Prompt"
      url: /verify/assessments/domain-assessment/
  meta:
    type: "Assessment Prompt"
    scope: "Full series"
    status: "Published"
    updated: "April 2026"
---

## Series-Level Assessment

This is the primary assessment mode. It evaluates the entire seven-book Panta Rhei research architecture across three gates: research-form legitimacy, novelty and relevance, and impact and salvage value.

The prompt below is pre-filled with the actual public URLs for the Panta Rhei site, Guided Tours, Lean companions, TauLib repository, and book index. Copy it into any frontier AI model --- Claude, GPT-4, Gemini, or equivalent --- and the model will produce a typed dossier structured by the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}).

The protocol works with public materials only. No confidential or unpublished material is required.


## The Prompt

{% include copy-prompt-button.html id="series-prompt" %}

```text
You are conducting an AI-assisted first-pass assessment of a public research architecture.

Your job is not to decide whether the framework is true.
Your job is to produce a typed dossier answering three bounded questions:

1. Research-form legitimacy
   Does this work appear to be a serious, inspectable, review-worthy research artifact?

2. Novelty and relevance
   If yes, do its claims appear potentially novel and materially relevant relative to
   mainstream frontier work in the domains it addresses?

3. Impact and salvage value
   If the core claims held, what would the likely magnitude of contribution be?
   If the core claims partly failed, what might still remain scientifically, formally,
   or methodologically valuable?

## Materials to use

Use only the following public materials:
- Series overview / website: https://panta-rhei.site
- Guided Tours index: https://panta-rhei.site/publications/guided-tours/
- Lean companions index: https://panta-rhei.site/verify/taulib/docs/
- TauLib public repository: https://github.com/Panta-Rhei-Research/taulib
- Public book pages / product pages / abstracts: https://panta-rhei.site/publications/books/
- Other public-facing clarification materials:
  https://panta-rhei.site/results/
  https://panta-rhei.site/registry/

Do not assume access to private or unpublished material.

## Required method

Read the materials and produce a dossier with these sections:

### A. Scope and object identification
- What is the framework claiming to be?
- What is the visible architecture?
- What is the visible series structure?
- What are the strongest visible claim clusters?

### B. Gate 1 — Research-form legitimacy
Assess whether the work appears:
- inspectable
- methodologically structured
- claim-typed
- reproducibility-aware
- falsification-aware
- review-worthy

For every judgment, cite visible evidence from the public materials.

### C. Gate 2 — Novelty and relevance
Assess:
- which claims seem likely to be genuinely novel
- which claims may risk rediscovery / overlap / relabeling
- which disciplines would need to judge the strongest novelty claims
- where prior-art review is especially necessary

### D. Gate 3 — Impact and salvage value
Produce three scenario assessments:
1. If the core claims substantially hold
2. If major bridge claims weaken but the internal architecture remains strong
3. If the core spine fails, but the work remains methodologically serious

For each scenario, identify:
- likely scientific value
- likely formal value
- likely philosophical value
- likely reusable artifacts (e.g. formalization, claim taxonomy,
  verification infrastructure, conceptual mappings)

### E. External validation map
List the exact kinds of human validation still required:
- mathematician(s)
- physicist(s)
- formal methods expert(s)
- philosopher(s) of science / mind / metaphysics
- prior-art specialists
- reproducibility specialists

### F. Red-team questions
Provide the 10 strongest fair-minded skeptical questions a serious expert should ask first.

### G. Review-readiness judgment
Choose one:
- Not yet review-ready
- Review-ready but needs stronger reproducibility scaffolding
- Review-ready but novelty claims need narrowing
- Review-ready as a serious unconventional research artifact
- Review-ready, high-risk/high-upside

### H. Confidence typing
For each major section, use confidence labels like:
- High confidence in inspectability
- Medium confidence in novelty signal
- Low confidence in correctness without expert review
- Low confidence in priority without prior-art review

Do not provide a single global truth probability.

## Style rules
- Be calm, precise, non-rhetorical
- Distinguish clearly between visible evidence and inference
- Separate internal claim structure from broader bridge claims
- State uncertainties explicitly
- Assume the reader wants a serious first-pass dossier, not a promotional summary

Now perform the assessment.
```


## After Running the Prompt

Once the model produces its dossier, score the output using the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}). The rubric provides a 17-criterion, 0--4 scoring framework organized by gate. Use the profile of scores, not the sum, as the primary signal.


## Related Assessment Modes

For more targeted assessments, use the book-level or domain-level prompts:

- **[Book-Level Assessment]({{ '/verify/assessments/book-assessment/' | relative_url }})** --- evaluates a single book, its Guided Tour, and its Lean companion
- **[Domain-Level Assessment]({{ '/verify/assessments/domain-assessment/' | relative_url }})** --- evaluates the framework from the standpoint of a particular discipline
- **[Assessment Overview]({{ '/verify/assessments/' | relative_url }})** --- the full protocol landing page with methodology and usage guidance
