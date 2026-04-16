---
layout: program-doc
title: "Assessment Scorecard"
lane: verify
permalink: /verify/assessments/scorecard/
summary_short: "The blank 17-row scoring table for recording three-gate assessment results, with a downloadable CSV template and instructions for use."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Dossier Output Schema"
      url: /verify/assessments/dossier-schema/
    - title: "Reviewer Workflow"
      url: /verify/assessments/reviewer-workflow/
  meta:
    type: "Assessment Protocol"
    scope: "Scoring table"
    status: "Published"
    updated: "April 2026"
---

## Purpose

The scorecard is the tabular companion to the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}). It provides a single table in which to record all 17 criterion scores, confidence labels, evidence excerpts, caveats, and reviewer notes for one assessment run. A completed scorecard, together with the typed dossier, constitutes the minimum structured output of the protocol.


## Scorecard Structure

The table contains one row per criterion, organised by gate. The columns are:

- **ID** --- The criterion identifier (e.g., G1-1, G2-8, G3-13).
- **Gate** --- Which of the three gates the criterion belongs to.
- **Criterion** --- The name of the criterion as defined in the rubric.
- **Score (0--4)** --- The rating on the five-point scale (0 = absent, 4 = unusually strong).
- **Confidence** --- The confidence label for this particular assessment (High, Medium, or Low).
- **Evidence** --- A brief excerpt or citation of the public material that supports the score.
- **Caveat** --- Any qualification, limitation, or uncertainty that applies to the score.
- **Notes** --- Optional reviewer observations that do not fit the other columns.


## Blank Scorecard

| ID | Gate | Criterion | Score (0--4) | Confidence | Evidence | Caveat | Notes |
|:---|:-----|:----------|:------------:|:----------:|:---------|:-------|:------|
| G1-1 | Gate 1 | Claim typing | | | | | |
| G1-2 | Gate 1 | Method visibility | | | | | |
| G1-3 | Gate 1 | Hinge visibility | | | | | |
| G1-4 | Gate 1 | Reproducibility scaffolding | | | | | |
| G1-5 | Gate 1 | Falsification readiness | | | | | |
| G1-6 | Gate 1 | Scope discipline | | | | | |
| G1-7 | Gate 1 | Review-worthiness | | | | | |
| G2-8 | Gate 2 | Novelty signal | | | | | |
| G2-9 | Gate 2 | Domain relevance | | | | | |
| G2-10 | Gate 2 | Prior-art awareness | | | | | |
| G2-11 | Gate 2 | Cross-domain relevance | | | | | |
| G2-12 | Gate 2 | Specificity of contribution | | | | | |
| G3-13 | Gate 3 | Upside magnitude | | | | | |
| G3-14 | Gate 3 | Partial-hold value | | | | | |
| G3-15 | Gate 3 | Salvage value | | | | | |
| G3-16 | Gate 3 | Reusability of artifacts | | | | | |
| G3-17 | Gate 3 | Strategic importance of inspection | | | | | |


## Download

[Download scorecard template (CSV)]({{ '/assets/downloads/assessment-scorecard.csv' | relative_url }})

The CSV template includes additional header columns for `assessment_id`, `review_mode`, and `book_or_domain`, which allow multiple completed scorecards to be collated into a single dataset for comparison across runs.


## How to Fill In the Scorecard

1. **Run the protocol.** Complete the [Reviewer Workflow]({{ '/verify/assessments/reviewer-workflow/' | relative_url }}) through Step 4 (running the prompt on a frontier model with the appropriate materials loaded).

2. **Score each criterion.** Read the model's output alongside the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}). For each of the 17 criteria, assign a score from 0 to 4 based on the evidence visible in the public materials.

3. **Assign confidence labels.** For each score, record whether your confidence in that particular assessment is High, Medium, or Low. Confidence refers to the quality and completeness of the evidence available, not to the probability that the underlying claim is correct.

4. **Cite evidence.** In the Evidence column, note the specific public material (page, file, tour, repository path) that supports the score. Keep citations brief but precise enough for a third party to locate the source.

5. **Record caveats.** If the score depends on assumptions, if the evidence is ambiguous, or if domain expertise would be needed to verify the rating, note that in the Caveat column.

6. **Add reviewer notes.** Use the Notes column for any observations that do not fit elsewhere --- patterns across criteria, open questions for human experts, or cross-references to the dossier's red-team questions.

7. **Attach to the dossier.** The completed scorecard should accompany the typed dossier as a structured appendix. Together, they form the auditable output of a single assessment run.
