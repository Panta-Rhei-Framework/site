---
layout: program-doc
title: "Reviewer Workflow"
lane: verify
permalink: /verify/assessments/reviewer-workflow/
summary_short: "The end-to-end eight-step process for producing an AI-assisted first-pass assessment dossier, from choosing a review mode through human escalation."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Dossier Output Schema"
      url: /verify/assessments/dossier-schema/
    - title: "Assessment Scorecard"
      url: /verify/assessments/scorecard/
  meta:
    type: "Assessment Protocol"
    scope: "Reviewer process"
    status: "Published"
    updated: "April 2026"
---

## Goal

Produce an initial structured dossier on the public Panta Rhei materials using a frontier large language model, while keeping the process transparent, bounded, and non-authoritative. The dossier is a triage instrument --- it helps decide whether deeper human review is warranted, which experts to involve, and where the strongest attack surfaces lie.


## The Eight Steps


### Step 1 --- Choose the review mode

Select one of three scopes:

- **Series-level** --- evaluates the entire seven-book monograph and the research architecture as a whole. This is the recommended starting point.
- **Book-level** --- evaluates a single book, its Guided Tour, and its Lean companion. Use this when you want a focused assessment of one domain.
- **Domain-level** --- evaluates the framework from the perspective of a particular discipline (e.g., particle physics, category theory, philosophy of science).

The choice of mode determines which prompt template to use and which materials to load.


### Step 2 --- Gather only public materials

Assemble the materials the model will analyse. All sources must be publicly available. Suitable materials include:

- The main website pages
- Guided Tours
- Lean companions and TauLib repository
- Public talks, clarifications, and errata
- Published book pages and product listings

Do not upload confidential manuscripts, unpublished drafts, or third-party restricted content into general-purpose AI systems. The protocol is designed to work entirely from the public surface.


### Step 3 --- Choose the correct prompt

Each review mode has a dedicated prompt template:

- [Series-level prompt]({{ '/verify/assessments/series-assessment/' | relative_url }})
- [Book-level prompt]({{ '/verify/assessments/book-assessment/' | relative_url }})
- [Domain-level prompt]({{ '/verify/assessments/domain-assessment/' | relative_url }})

Load the chosen prompt into a frontier model alongside the gathered materials. The prompts are designed to elicit a dossier that conforms to the [Dossier Output Schema]({{ '/verify/assessments/dossier-schema/' | relative_url }}).


### Step 4 --- Run the prompt

Execute the prompt on a frontier model. Preserve the following metadata for the audit trail:

- The exact prompt text used
- The model name and version
- The date and time of the run
- The complete list of materials provided


### Step 5 --- Score the dossier

Apply the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}) to the model's output. Record each criterion's score, confidence label, evidence excerpt, and caveats using the [Assessment Scorecard]({{ '/verify/assessments/scorecard/' | relative_url }}).


### Step 6 --- Produce a typed output

Organise the model's output into the 10-section structure defined in the [Dossier Output Schema]({{ '/verify/assessments/dossier-schema/' | relative_url }}). If the model's raw output does not cover all sections, note which sections are incomplete and why.


### Step 7 --- Compare if possible

When the stakes are high or when the assessment will inform public communication, run the protocol a second time using:

- A different frontier model, or
- A different human reviewer, or
- Both

Compare the two dossiers for convergence and divergence. Points of divergence are especially valuable --- they identify the criteria where assessment confidence is lowest and human expertise is most needed.


### Step 8 --- Escalate to humans

The dossier is a triage instrument, not a verdict. Use it to decide:

- Whether deeper expert review is warranted
- Which domain experts to involve and what they should evaluate
- Where the strongest attack surfaces lie --- the points where sceptical scrutiny would be most productive

The dossier should never be cited as evidence that the claims are correct. It is evidence that a structured first pass found certain signals, subject to the confidence caveats stated in the dossier itself.


## Minimum Retention Requirements

To make the process auditable, retain the following materials from every assessment run:

- The prompt text (including any modifications)
- The model name and version identifier
- The date and time of execution
- The complete list of materials provided to the model
- The full output dossier
- The completed scoring table
- Any human reviewer notes or annotations

These records allow a future reader to reconstruct the conditions under which the assessment was produced and to evaluate whether those conditions were appropriate.


## Recommended Reviewer Note

Every dossier should include the following disclaimer, or language substantively equivalent to it:

> This dossier is an AI-assisted first-pass assessment based only on public materials. It is intended to improve the structure and legibility of the review process. It is not a substitute for expert judgment, formal checking, or peer review.

This note should appear in the dossier's header or executive summary. It sets the correct epistemic frame for anyone who reads the output.


## Tools and References

- [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}) --- the 17-criterion scoring framework
- [Assessment Scorecard]({{ '/verify/assessments/scorecard/' | relative_url }}) --- the blank scoring table (CSV)
- [Dossier Output Schema]({{ '/verify/assessments/dossier-schema/' | relative_url }}) --- the 10-section dossier structure (JSON template)
- [Series-level prompt]({{ '/verify/assessments/series-assessment/' | relative_url }})
- [Book-level prompt]({{ '/verify/assessments/book-assessment/' | relative_url }})
- [Domain-level prompt]({{ '/verify/assessments/domain-assessment/' | relative_url }})
