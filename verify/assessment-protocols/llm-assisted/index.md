---
layout: program-doc
title: "LLM-Assisted Protocols"
permalink: /verify/assessment-protocols/llm-assisted/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: assessment_protocol
status: "Canonical"
summary_short: "Structured prompts and review procedures for using frontier language models to audit aspects of the program."
right_rail:
  related:
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
    - title: "Methodology"
      url: /verify/assessments/methodology/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "How to Verify"
      url: /verify/how-to-verify/
    - title: "AI-Assisted Discovery"
      url: /discover/ai-assisted-discovery/
  meta:
    type: "LLM-Assisted Assessment Protocol"
    status: "Canonical"
    updated: "May 2026"
---

## Purpose

These protocols allow external users to use frontier language models to inspect structural derivations, test result support, compare stated standards against exposed artifacts, and identify gaps or unsupported transitions.

LLM-assisted assessment must cite public pages and route findings back into Verify. Model output is not peer review, proof checking, empirical validation, or final adjudication.

For lighter first-contact orientation prompts (program overview, agenda summary, lane navigation), use [Discover → AI-Assisted Discovery]({{ '/discover/ai-assisted-discovery/' | relative_url }}). For deeper assessment workflows that produce typed dossiers and three-gate rubric output, stay here.

## Protocol Families

- **Structural integrity audit:** does the public argument expose its load-bearing moves?
- **Derivation support audit:** do cited Corpus and TauLib surfaces support the stated result?
- **Consistency audit:** do public pages, manifests, and generated artifacts agree?
- **Falsifiability audit:** are failure conditions explicit and reviewable?
- **Research-form legitimacy audit:** does the program merit serious human attention?

## Detailed Prompt Library

Use the existing public templates:

- [Series-Level Assessment Prompt]({{ '/verify/assessments/series-assessment/' | relative_url }})
- [Book-Level Assessment Prompt]({{ '/verify/assessments/book-assessment/' | relative_url }})
- [Expert-Domain Assessment Prompt]({{ '/verify/assessments/domain-assessment/' | relative_url }})
- [Dossier Output Schema]({{ '/verify/assessments/dossier-schema/' | relative_url }})
- [Assessment Scorecard]({{ '/verify/assessments/scorecard/' | relative_url }})

Do not treat model output as peer review, proof checking, empirical validation, or final adjudication. It is a structured first-pass signal that must be cited and traced back into the Verify, Corpus, and Results surfaces.
