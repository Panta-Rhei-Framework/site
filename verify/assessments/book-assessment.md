---
layout: program-doc
title: "Book-Level Assessment Prompt"
lane: verify
permalink: /verify/assessments/book-assessment/
summary_short: "A prompt template for assessing a single book within the Panta Rhei series across three gates."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Series-Level Prompt"
      url: /verify/assessments/series-assessment/
    - title: "Domain-Level Prompt"
      url: /verify/assessments/domain-assessment/
  meta:
    type: "Assessment Prompt"
    scope: "Single book"
    status: "Published"
    updated: "April 2026"
---

## Book-Level Assessment

This prompt evaluates a single book within the Panta Rhei series, together with its corresponding Guided Tour and Lean companion. Use it when you want a focused assessment of one domain rather than the full architecture --- for example, only the mathematical foundations (Book I), or only the cosmological predictions (Book V).

Before running the prompt, choose the book you wish to assess and fill in the template variables from the reference table below. Then copy the completed prompt into any frontier AI model --- Claude, GPT-4, Gemini, or equivalent.


## The Seven Books

Use this table to fill in the template variables for the book you are assessing.

| Book | Title | Subtitle | Layer | Atlas URL |
|------|-------|----------|-------|-----------|
| I | Categorical Foundations | How Mathematics Is Earned | E&#x2080; Mathematics | [Book I](https://panta-rhei.site/publications/books/book-i/) |
| II | Categorical Holomorphy | Finite Readouts of Infinity | E&#x2080; Mathematics | [Book II](https://panta-rhei.site/publications/books/book-ii/) |
| III | Categorical Spectrum | Where Physics Lives | E&#x2080; Mathematics (Hinge) | [Book III](https://panta-rhei.site/publications/books/book-iii/) |
| IV | Categorical Microcosm | The Self-Describing Universe | E&#x2081; Physics (Microcosm) | [Book IV](https://panta-rhei.site/publications/books/book-iv/) |
| V | Categorical Macrocosm | The Biography of the Universe | E&#x2081; Physics (Macrocosm) | [Book V](https://panta-rhei.site/publications/books/book-v/) |
| VI | Categorical Life | Life as Self-Decoding Distinctions | E&#x2082; Life | [Book VI](https://panta-rhei.site/publications/books/book-vi/) |
| VII | Categorical Metaphysics | The Final Self-Enrichment | E&#x2083; Metaphysics | [Book VII](https://panta-rhei.site/publications/books/book-vii/) |

**Guided Tours** are available at [panta-rhei.site/publications/guided-tours/](https://panta-rhei.site/publications/guided-tours/).

**Lean companions** are available at [panta-rhei.site/verify/taulib/docs/](https://panta-rhei.site/verify/taulib/docs/).


## The Prompt

Fill in the six template variables marked with `{{...}}` below, then copy the entire block into a frontier model.

```text
You are conducting an AI-assisted first-pass assessment of one book within a larger
research architecture.

Your job is not to determine final truth.
Your job is to produce a book-level dossier on:

1. research-form legitimacy
2. novelty and relevance
3. impact and salvage value

## Book under review
- Book number/title: {{BOOK_TITLE}}
- Subtitle: {{BOOK_SUBTITLE}}
- Guided Tour URL/PDF: {{GUIDED_TOUR_URL}}
- Lean companion URL/file: {{LEAN_COMPANION_URL}}
- Atlas/book page: {{BOOK_PAGE_URL}}
- Optional related public materials: {{OPTIONAL_BOOK_URLS}}

## Required method

### 1. Identify the book's role in the series
- What does this book claim to do?
- What does it appear to export to later books?
- What are its stated load-bearing hinges?
- What does it explicitly not claim?

### 2. Gate 1 — Research-form legitimacy
Evaluate whether the book appears:
- structured
- inspectable
- hinge-explicit
- reproducibility-aware
- falsification-aware
- serious enough to deserve expert scrutiny

### 3. Gate 2 — Novelty and relevance
Evaluate:
- which claims seem likely to be novel
- which may risk rediscovery or relabeling
- which domain experts would be needed to judge novelty
- whether the Lean companion strengthens the book's review-worthiness

### 4. Gate 3 — Impact and salvage value
Evaluate three scenarios:
1. core claims hold
2. strongest bridge claims weaken
3. core spine fails, but the book remains methodologically serious

For each scenario, identify:
- scientific/formal/philosophical value
- likely reusable assets
- likely residual contribution

### 5. Red-team attack surface
List:
- the 5 strongest attack vectors
- the most load-bearing break points
- the most likely "misframing" risks
- what would need to be checked first by a serious reviewer

### 6. Review-readiness judgment
Choose one:
- Not yet review-ready
- Review-ready but needs stronger reproducibility scaffolding
- Review-ready but novelty claims need narrowing
- Review-ready as a serious unconventional artifact
- Review-ready, high-risk/high-upside

### 7. Confidence typing
For each major judgment, specify confidence in the assessment, not in the truth
of the framework.

## Style rules
- Quote or paraphrase specific visible evidence
- Distinguish evidence from inference
- Distinguish internal theorem-like claims from broader interpretations
- Be concise but serious
- Do not issue a single truth verdict

Now produce the dossier.
```


## Example: Filling in the Template

For **Book IV --- Categorical Microcosm**, you would fill in:

- `{{BOOK_TITLE}}`: Book IV: Categorical Microcosm
- `{{BOOK_SUBTITLE}}`: The Self-Describing Universe
- `{{GUIDED_TOUR_URL}}`: https://panta-rhei.site/publications/guided-tours/ (Book IV section)
- `{{LEAN_COMPANION_URL}}`: https://panta-rhei.site/verify/taulib/docs/ (Book IV modules)
- `{{BOOK_PAGE_URL}}`: https://panta-rhei.site/publications/books/book-iv/
- `{{OPTIONAL_BOOK_URLS}}`: https://panta-rhei.site/framework/physics/, https://panta-rhei.site/results/


## After Running the Prompt

Score the output using the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}). The rubric's 17 criteria apply at book level just as they do at series level --- use the profile of scores, not the sum, as the primary signal.


## Related Assessment Modes

- **[Series-Level Assessment]({{ '/verify/assessments/series-assessment/' | relative_url }})** --- evaluates the entire seven-book architecture (recommended starting point)
- **[Domain-Level Assessment]({{ '/verify/assessments/domain-assessment/' | relative_url }})** --- evaluates from the standpoint of a particular discipline
- **[Assessment Overview]({{ '/verify/assessments/' | relative_url }})** --- the full protocol landing page with methodology and usage guidance
