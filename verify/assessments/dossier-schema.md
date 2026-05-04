---
layout: program-doc
title: "Dossier Output Schema"
lane: verify
permalink: /verify/assessments/dossier-schema/
summary_short: "The 10-section structure that every AI-assisted first-pass assessment dossier must follow, with a downloadable JSON template for machine-readable output."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Assessment Scorecard"
      url: /verify/assessments/scorecard/
    - title: "Structured Inspection Workflow"
      url: /verify/assessments/structured-inspection-workflow/
  meta:
    type: "Assessment Protocol"
    scope: "Dossier structure"
    status: "Published"
    updated: "April 2026"
---

## Purpose

Every assessment run produces a **typed dossier** --- a structured document that follows a fixed schema so that dossiers from different reviewers, models, and dates can be compared systematically. The schema enforces completeness: every section must be present, even if a section's content is "not assessable at this scope."


## The 10-Section Structure

1. **Header** --- Protocol version, model used, date, materials consulted, and review mode (series-level, book-level, or domain-level). This metadata makes the dossier auditable and reproducible.

2. **Executive summary** --- A 5--10 sentence overview of the assessment, followed by a one-line recommendation. The summary should be intelligible to a non-specialist reader.

3. **Object identification** --- What is the work? What does it claim to be? What domains does it address? What is its visible architecture? This section establishes the object under review before scoring begins.

4. **Gate 1: Research-form legitimacy** --- For each of the 7 criteria (G1-1 through G1-7): a score on the 0--4 scale, a confidence label for the assessment, a citation of the visible evidence, and any caveats.

5. **Gate 2: Novelty and relevance** --- For each of the 5 criteria (G2-8 through G2-12): score, confidence, evidence, and caveats, following the same structure as Gate 1.

6. **Gate 3: Impact and salvage value** --- For each of the 5 criteria (G3-13 through G3-17): score, confidence, evidence, and caveats, following the same structure as Gate 1.

7. **Required external validation** --- A list specifying which human experts are needed, what they should evaluate, and what cannot be settled by AI alone. Organised by domain (mathematics, physics, formal methods, philosophy, prior-art review, other).

8. **Red-team questions** --- The 10 strongest fair-minded sceptical questions the reviewer can formulate about the work. These are intended to sharpen the review agenda, not to discredit the project.

9. **Review-readiness judgment** --- A single label chosen from a closed set:
   - Not yet review-ready
   - Review-ready but needs stronger reproducibility scaffolding
   - Review-ready but novelty claims need narrowing
   - Review-ready as a serious unconventional artefact
   - Review-ready, high-risk / high-upside

10. **Confidence note** --- An explanation of what the confidence labels used throughout the dossier mean and, critically, what they do not mean. This section must state explicitly that confidence refers to assessment visibility and scope, not to the probability that the claims are true.

**Appendix** (attached to the dossier): materials used, extracted claims, key caveats, and a reference to the scoring table.


## Download

[Download dossier template (JSON)]({{ '/assets/assessments/dossier-template.json' | relative_url }})

The JSON template provides a machine-readable skeleton that can be filled programmatically or by hand. Its field names mirror the section structure above.


## JSON Structure Reference

The following code block shows the template's top-level shape. Each gate array expects one object per criterion, with fields for `criterion_id`, `criterion_name`, `score`, `confidence`, `evidence`, and `caveat`.

```json
{
  "protocol_version": "1.0",
  "model": "",
  "date": "",
  "review_mode": "",
  "materials_used": [],
  "executive_summary": "",
  "object_identification": {
    "what_is_the_work": "",
    "what_it_claims_to_be": "",
    "domains_addressed": [],
    "visible_architecture": ""
  },
  "gate_1_research_form_legitimacy": [],
  "gate_2_novelty_and_relevance": [],
  "gate_3_impact_and_salvage_value": [],
  "required_external_validation": {
    "mathematics": [],
    "physics": [],
    "formal_methods": [],
    "philosophy": [],
    "prior_art_review": [],
    "other": []
  },
  "red_team_questions": [],
  "review_readiness_judgment": "",
  "confidence_note": "",
  "next_step_recommendation": "",
  "appendix": {
    "materials": [],
    "extracted_claims": [],
    "key_caveats": [],
    "scoring_table_reference": ""
  }
}
```

Each element in a gate array should follow this shape:

```json
{
  "criterion_id": "G1-1",
  "criterion_name": "Claim typing",
  "score": 0,
  "confidence": "High | Medium | Low",
  "evidence": "",
  "caveat": ""
}
```

When filling the template, leave no field empty. If a field is not applicable at the chosen review scope, enter a brief explanation (e.g., "Not assessable at series level --- requires book-level analysis").
