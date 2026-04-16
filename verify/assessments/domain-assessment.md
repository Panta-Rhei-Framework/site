---
layout: program-doc
title: "Expert-Domain Assessment Prompt"
lane: verify
permalink: /verify/assessments/domain-assessment/
summary_short: "A prompt template for assessing the Panta Rhei framework from the perspective of a particular scientific or philosophical discipline."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Three-Gate Rubric"
      url: /verify/assessments/three-gate-rubric/
    - title: "Series-Level Prompt"
      url: /verify/assessments/series-assessment/
    - title: "Book-Level Prompt"
      url: /verify/assessments/book-assessment/
  meta:
    type: "Assessment Prompt"
    scope: "Single domain"
    status: "Published"
    updated: "April 2026"
---

## Expert-Domain Assessment

This prompt evaluates the Panta Rhei framework from the standpoint of a particular scientific or philosophical discipline. Use it when you want a specialist's-eye-view dossier --- for example, what a category theorist, particle physicist, or philosopher of mind would see when inspecting the public materials.

Choose a domain from the suggested list below (or specify your own), fill in the relevant Atlas lane URLs, and copy the completed prompt into any frontier AI model --- Claude, GPT-4, Gemini, or equivalent.


## Suggested Domains

The framework makes claims across several disciplines. The following domains are natural entry points for expert-domain assessment, listed with the most relevant Atlas lanes and books.

| Domain | Primary Atlas Lane | Books |
|--------|-------------------|-------|
| Pure mathematics | [Mathematics Layer](https://panta-rhei.site/framework/mathematics/) | I, II |
| Category theory / topos theory | [Mathematics Layer](https://panta-rhei.site/framework/mathematics/) | I, II, III |
| Particle physics | [Physics Layer](https://panta-rhei.site/framework/physics/) | IV |
| Cosmology | [Physics Layer](https://panta-rhei.site/framework/physics/) | V |
| Philosophy of science | [Framework Overview](https://panta-rhei.site/framework/about/) | I--VII |
| Philosophy of mind | [Metaphysics Layer](https://panta-rhei.site/framework/metaphysics/) | VII |
| Formal methods / theorem proving | [TauLib Overview](https://panta-rhei.site/verify/taulib/) | I--VII |

Additional domains that may be relevant: condensed matter physics, mathematical physics, algebraic geometry, biological systems theory, philosophy of mathematics, philosophy of biology, and scientific methodology.


## The Prompt

Fill in the template variables marked with `{% raw %}{{...}}{% endraw %}` below using the domain table above, then use the button to copy.

{% include copy-prompt-button.html id="domain-prompt" %}

```text
You are assisting a domain specialist with a first-pass assessment of a public
research framework.

## Domain perspective
Review from the standpoint of: {{DOMAIN}}
Examples:
- pure mathematics
- category theory / topos theory
- formal methods / theorem proving
- particle physics
- cosmology
- philosophy of science
- philosophy of mind
- metaphysics

## Materials
- Domain-relevant Atlas lane: {{DOMAIN_ATLAS_URL}}
- Relevant Guided Tour(s): {{DOMAIN_GUIDED_TOURS}}
- Relevant Lean companion(s): {{DOMAIN_LEAN_COMPANIONS}}
- TauLib repository: https://github.com/Panta-Rhei-Research/taulib
- Optional relevant public talks / notes: {{OPTIONAL_PUBLIC_URLS}}

## Required task

Please answer:

### A. Domain fit
- Which parts of the framework most directly belong to this domain?
- Which parts should be ignored for this first-pass domain review?

### B. Domain seriousness
- Does the public material appear serious enough for a domain expert to inspect?
- Are the visible methods appropriate to the kinds of claims being made in this domain?
- What domain-specific evidence is present?
- What domain-specific evidence is missing?

### C. Domain novelty and overlap
- Which claims seem potentially novel in this domain?
- Which may risk rediscovery, relabeling, or overstatement?
- Which would require close prior-art comparison?

### D. Domain-specific attack surface
- What are the strongest domain-specific skeptical questions?
- What should a fair-minded expert test first?
- What visible weaknesses or gaps stand out from this domain's perspective?

### E. Domain-specific impact under three scenarios
1. If the domain-relevant claims hold
2. If some bridge claims fail but internal structure remains interesting
3. If the domain core fails but some methods / artifacts remain reusable

### F. Recommendation
Choose one:
- Ignore for now
- Worth limited specialist attention
- Worth serious domain review
- Worth urgent high-level domain attention

### G. Confidence typing
Use confidence labels for the quality of your assessment.

## Important rule
Do not pretend to have conclusively settled the domain questions.
Produce a serious first-pass domain dossier only.

Now produce the dossier.
```


## Pre-Filled Examples

Below are two worked examples showing how to fill in the template variables for common domains.

### Category theory

- `{{DOMAIN}}`: category theory / topos theory
- `{{DOMAIN_ATLAS_URL}}`: https://panta-rhei.site/framework/mathematics/
- `{{DOMAIN_GUIDED_TOURS}}`: https://panta-rhei.site/publications/guided-tours/ (Books I, II, III)
- `{{DOMAIN_LEAN_COMPANIONS}}`: https://panta-rhei.site/verify/taulib/docs/ (Books I, II, III)
- `{{OPTIONAL_PUBLIC_URLS}}`: https://panta-rhei.site/results/, https://panta-rhei.site/registry/

### Particle physics

- `{{DOMAIN}}`: particle physics
- `{{DOMAIN_ATLAS_URL}}`: https://panta-rhei.site/framework/physics/
- `{{DOMAIN_GUIDED_TOURS}}`: https://panta-rhei.site/publications/guided-tours/ (Book IV)
- `{{DOMAIN_LEAN_COMPANIONS}}`: https://panta-rhei.site/verify/taulib/docs/ (Book IV)
- `{{OPTIONAL_PUBLIC_URLS}}`: https://panta-rhei.site/results/, https://panta-rhei.site/registry/

### Cosmology

- `{{DOMAIN}}`: cosmology
- `{{DOMAIN_ATLAS_URL}}`: https://panta-rhei.site/framework/physics/
- `{{DOMAIN_GUIDED_TOURS}}`: https://panta-rhei.site/publications/guided-tours/ (Book V)
- `{{DOMAIN_LEAN_COMPANIONS}}`: https://panta-rhei.site/verify/taulib/docs/ (Book V)
- `{{OPTIONAL_PUBLIC_URLS}}`: https://panta-rhei.site/results/, https://panta-rhei.site/registry/

### Philosophy of mind

- `{{DOMAIN}}`: philosophy of mind
- `{{DOMAIN_ATLAS_URL}}`: https://panta-rhei.site/framework/metaphysics/
- `{{DOMAIN_GUIDED_TOURS}}`: https://panta-rhei.site/publications/guided-tours/ (Book VII)
- `{{DOMAIN_LEAN_COMPANIONS}}`: https://panta-rhei.site/verify/taulib/docs/ (Book VII)
- `{{OPTIONAL_PUBLIC_URLS}}`: https://panta-rhei.site/results/

### Philosophy of science

- `{{DOMAIN}}`: philosophy of science
- `{{DOMAIN_ATLAS_URL}}`: https://panta-rhei.site/framework/about/
- `{{DOMAIN_GUIDED_TOURS}}`: https://panta-rhei.site/publications/guided-tours/ (all books)
- `{{DOMAIN_LEAN_COMPANIONS}}`: https://panta-rhei.site/verify/taulib/docs/
- `{{OPTIONAL_PUBLIC_URLS}}`: https://panta-rhei.site/results/, https://panta-rhei.site/verify/

### Formal methods

- `{{DOMAIN}}`: formal methods / theorem proving
- `{{DOMAIN_ATLAS_URL}}`: https://panta-rhei.site/verify/taulib/
- `{{DOMAIN_GUIDED_TOURS}}`: https://panta-rhei.site/publications/guided-tours/ (all books)
- `{{DOMAIN_LEAN_COMPANIONS}}`: https://panta-rhei.site/verify/taulib/docs/
- `{{OPTIONAL_PUBLIC_URLS}}`: https://github.com/Panta-Rhei-Research/taulib, https://panta-rhei.site/verify/taulib/architecture/


## After Running the Prompt

Score the output using the [Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }}). Domain-level dossiers naturally weight certain criteria more heavily --- a category theory review will focus on Gate 1 (method visibility, claim typing) and Gate 2 (novelty signal, prior-art awareness), while a cosmology review will weight Gate 3 (impact magnitude, falsification readiness) more strongly. The rubric accommodates this by design: use the profile of scores, not the sum.


## Related Assessment Modes

- **[Series-Level Assessment]({{ '/verify/assessments/series-assessment/' | relative_url }})** --- evaluates the entire seven-book architecture (recommended starting point)
- **[Book-Level Assessment]({{ '/verify/assessments/book-assessment/' | relative_url }})** --- evaluates a single book, its Guided Tour, and its Lean companion
- **[Assessment Overview]({{ '/verify/assessments/' | relative_url }})** --- the full protocol landing page with methodology and usage guidance
