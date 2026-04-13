---
layout: program-doc
title: "Review Kit"
permalink: /media/review-kit/
lane: engage
summary_short: "Structured entry paths for reviewers, domain experts, and institutional readers."
summary_cards:
- title: "For reviewers"
  body: "Five domain-specific review paths with recommended reading order and verification routes."
- title: "For institutions"
  body: "Prospectus, reviewer's dossier, formalization overview, and contact routes."
- title: "What this is not"
  body: "Not a substitute for expert review. Not a certification. Not a claim of completion."
right_rail:
  related:
  - title: Media Kit
    url: /media/
  - title: Verify
    url: /verify/
  - title: About the Research
    url: /research-program/about/
  artifacts:
  - title: TauLib (contributor)
    url: https://github.com/Panta-Rhei-Framework/taulib
    external: true
  - title: Formalization (frozen)
    url: https://github.com/Panta-Rhei-Framework/formalization
    external: true
  meta:
    type: "Review Kit"
    status: "Active"
    updated: "April 2026"
---

## What Kind of Object This Is

The Panta Rhei Research Program is an **independent open research program** — not a journal submission, not a textbook, not a software project. It is a seven-book monograph series accompanied by a Lean 4 formalization library, a public research website, and structured verification surfaces.

The books are the canonical monograph release. The site provides navigable access in understanding-order. TauLib provides machine-checked verification. The guided tours and companion papers lower the threshold for structured engagement.

## Recommended Review Paths

### General orientation
1. [About the Research]({{ '/research-program/about/' | relative_url }})
2. [The Tau Framework]({{ '/framework/about/' | relative_url }})
3. [Key Results]({{ '/results/' | relative_url }})
4. [How to Read a Result Page]({{ '/results/how-to-read-a-result-page/' | relative_url }})

### Mathematics-first path
1. [Book I: Categorical Foundations]({{ '/publications/books/book-i/' | relative_url }})
2. [Book II: Categorical Holomorphy]({{ '/publications/books/book-ii/' | relative_url }})
{% assign math_results = site.data.results.results | where: "topic", "mathematics" %}3. [Results by Domain: Mathematics]({{ '/results/topic/mathematics/' | relative_url }}) ({{ math_results | size }} results)
4. [Registry — Book I]({{ '/registry/books/book-i/' | relative_url }})
5. [Guided Tours — Foundations](https://github.com/Panta-Rhei-Framework/taulib/blob/main/TauLib/Tour/Foundations.lean)

### Physics-first path
1. [Book III: Categorical Spectrum]({{ '/publications/books/book-iii/' | relative_url }}) (the hinge)
2. [Book IV: Categorical Microcosm]({{ '/publications/books/book-iv/' | relative_url }})
3. [Book V: Categorical Macrocosm]({{ '/publications/books/book-v/' | relative_url }})
{% assign phys_results = site.data.results.results | where: "topic", "physics" %}4. [Results by Domain: Physics]({{ '/results/topic/physics/' | relative_url }}) ({{ phys_results | size }} results)
5. [Guided Tours — Physics](https://github.com/Panta-Rhei-Framework/taulib/blob/main/TauLib/Tour/Physics.lean)

### Life and metaphysics path
1. [Book VI: Categorical Life]({{ '/publications/books/book-vi/' | relative_url }})
2. [Book VII: Categorical Metaphysics]({{ '/publications/books/book-vii/' | relative_url }})
{% assign bio_results = site.data.results.results | where: "topic", "biology" %}{% assign phil_results = site.data.results.results | where: "topic", "philosophy" %}3. [Results by Domain: Biology]({{ '/results/topic/biology/' | relative_url }}) ({{ bio_results | size }} results)
4. [Results by Domain: Philosophy]({{ '/results/topic/philosophy/' | relative_url }}) ({{ phil_results | size }} results)

### Formal verification path
1. [Verify]({{ '/verify/' | relative_url }})
2. [TauLib repository](https://github.com/Panta-Rhei-Framework/taulib) — clone and run `lake build`
3. [Guided Tours — VerifyItYourself](https://github.com/Panta-Rhei-Framework/taulib/blob/main/TauLib/Tour/VerifyItYourself.lean)
{% assign reg_count = site.data.registry.objects | size %}4. [Registry]({{ '/registry/' | relative_url }}) — {{ reg_count }} objects with dependency graphs

## Suggested Starter Packet

For a reviewer who wants to form a first impression in 30-60 minutes:

1. **[About the Research]({{ '/research-program/about/' | relative_url }})** — what the program is (5 min)
2. **[Why So Many Results Are Possible]({{ '/results/why-so-many-results/' | relative_url }})** — how constraint enables breadth (5 min)
3. **[Status and Claim Typing]({{ '/results/status-and-claim-typing/' | relative_url }})** — how claims are typed (5 min)
4. **Pick 3 results** from [Key Results]({{ '/results/' | relative_url }}) in your domain (15 min)
5. **[Verify]({{ '/verify/' | relative_url }})** — how to inspect further (5 min)
6. **One guided tour** from [Guided Tours]({{ '/publications/guided-tours/' | relative_url }}) (15 min)

## What This Page Does Not Claim

- This is **not a substitute for expert review**. The program invites scrutiny; it does not pre-empt it.
- **Lean compilation verifies internal consistency**, not physical truth. Empirical claims require empirical testing.
- **No expectation** that one reader resolves the whole program in one sitting. The review paths are starting points.
- The program is **independent research** — not yet peer-reviewed in traditional journals. All claims carry explicit scope labels.

## Contact

- **Media**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject: "Media Inquiry"
- **Technical review**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject: "Technical Inquiry"
- **Institutional**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject: "Institutional"
