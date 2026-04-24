---
layout: program-doc
title: "AI-Assisted First-Pass Assessment"
lane: verify
permalink: /verify/assessments/
summary_short: "A public method for producing initial dossiers on inspectability, novelty signals, and possible impact using only public materials."
summary_cards:
  - title: "What these are"
    body: "Structured assessment protocols that use a frontier AI model to produce typed dossiers evaluating research-form legitimacy, novelty, and potential impact."
  - title: "Three questions"
    body: "Is the work a serious, inspectable research artifact? Do its claims appear novel and relevant? If the strongest claims held or partly failed, what would remain significant?"
  - title: "How to use"
    body: "Choose a prompt (series-level, book-level, or domain-level), load the public materials, run the protocol on a frontier model, and interpret the dossier against the three-gate rubric."
right_rail:
  related:
    - title: "Verify Overview"
      url: /verify/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Methodology"
      url: /verify/assessments/methodology/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
  meta:
    type: "Assessment Protocol"
    status: "Published"
    updated: "April 2026"
---

## What This Protocol Does

The Panta Rhei Research Program makes unusually large claims across mathematics, physics, life sciences, and metaphysics. For readers, critics, journalists, and domain specialists who want a structured first signal before investing deeper human time, we provide an **AI-assisted first-pass assessment protocol**.

The protocol is designed to help outsiders evaluate three preliminary questions using only public materials and a frontier AI model:

1. **Research-form legitimacy** --- Does the work appear to be a serious, inspectable research artifact that has earned external scrutiny?
2. **Novelty and relevance** --- Do its claims appear potentially novel and materially relevant relative to frontier work in the domains addressed?
3. **Impact and salvage value** --- If the strongest claims held, or partly failed, what would remain scientifically, formally, or methodologically significant?

The output is a **typed dossier** --- not a verdict, not a truth-probability, not a peer-review substitute. It is a structured first signal designed to make the preliminary question more disciplined.


## Who This Is For

The protocol is intended for anyone who needs an initial, structured public assessment of whether the framework appears serious enough to warrant deeper attention:

- **Journalists** covering the research or its claims
- **Critics** evaluating the work's methodological seriousness
- **Policymakers** assessing potential significance for science-policy decisions
- **Investors** conducting due-diligence on the research program
- **Domain experts** deciding whether the work merits a closer look from their specialty


## Three Assessment Modes

The protocol provides three prompt templates, each scoped to a different level of analysis.

### Series-level assessment

Evaluates the entire seven-book monograph series and the research architecture as a whole. This is the recommended starting point for a general first-pass assessment.

[Open the series-level prompt]({{ '/verify/assessments/series-assessment/' | relative_url }})

### Book-level assessment

Evaluates a single book, its corresponding Guided Tour, and its Lean companion. Use this when you want a focused assessment of one domain (e.g., only the physics books, or only the foundations).

[Open the book-level prompt]({{ '/verify/assessments/book-assessment/' | relative_url }})

### Domain-level assessment

Evaluates the framework from the perspective of a particular discipline --- pure mathematics, particle physics, cosmology, philosophy of science, or any other relevant field. Use this when you want a specialist's-eye-view dossier.

[Open the domain-level prompt]({{ '/verify/assessments/domain-assessment/' | relative_url }})


## Start Here

If you are new to the protocol, work through these in order:

1. **Read the [Methodology]({{ '/verify/assessments/methodology/' | relative_url }})** --- understand the three-gate structure, what AI can and cannot do, and what question this protocol actually answers.
2. **Review the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }})** --- the 17-criterion scoring framework that structures every dossier.
3. **Review the [Usage Rules]({{ '/verify/assessments/usage-rules/' | relative_url }})** --- the 10 rules that govern responsible use.
4. **Choose a prompt** --- series-level, book-level, or domain-level --- and run it on a frontier model with the public materials loaded.


## Public Materials for Pre-Loading

When running the protocol, provide the model with the relevant public sources. Suggested URLs:

- **Main site:** [https://panta-rhei.site](https://panta-rhei.site)
- **TauLib (Lean 4 library):** [https://github.com/Panta-Rhei-Research/taulib](https://github.com/Panta-Rhei-Research/taulib)
- **Guided Tours:** [Guided Tours]({{ '/publications/guided-tours/' | relative_url }})
- **Books:** [Books]({{ '/publications/books/' | relative_url }})

Do not upload confidential, unpublished, or third-party restricted materials into general-purpose AI systems. The protocol is designed to work entirely with public materials.


## Downloads

- **[Scorecard template (CSV)]({{ '/assets/downloads/assessment-scorecard.csv' | relative_url }})** --- a blank three-gate scorecard for recording assessment results (includes `assessment_id`, `review_mode`, `book_or_domain` header columns for collating multiple runs)
- **[Dossier template (JSON)]({{ '/assets/assessments/dossier-template.json' | relative_url }})** --- the structured output schema for typed dossiers


> **This protocol is not peer review.** It is a first-pass assessment method. Any serious judgment about correctness, novelty, or scholarly priority must ultimately be made by human experts. A positive outcome means the work appears serious enough to deserve structured scrutiny --- it does not mean the claims are proven true or that expert review is no longer necessary.
