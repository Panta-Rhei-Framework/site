---
layout: program-doc
title: "Review Kit"
permalink: /media/review-kit/
lane: support
type: support_page
support_type: review_kit
status: canonical
updated: "April 2026"
summary: "A structured entry point for reviewers who want to inspect, challenge, or assess the Panta Rhei Research Program."
summary_short: "Structured entry paths for reviewers, domain experts, and institutional readers."
summary_cards:
- title: "For reviewers"
  body: "Recommended routes into Program, Corpus, Results, Verify, Publications, and Assessment Protocols."
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
  - title: Assessment Protocols
    url: /verify/assessment-protocols/
  - title: Program
    url: /program/
  - title: Problem Ledger
    url: /results/problem-ledger/
  artifacts:
  - title: TauLib (contributor)
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  - title: Formalization (frozen)
    url: https://github.com/Panta-Rhei-Research/formalization
    external: true
  meta:
    type: "Support page"
    scope: "Review kit"
    status: "Canonical"
    updated: "April 2026"
---

## Recommended review paths

The Panta Rhei Research Program is an **independent open research program** — not a journal submission, not a textbook, not a software project. It is a seven-book monograph series accompanied by a Lean 4 formalization library, a public research website, and structured verification surfaces.

The [books]({{ '/publications/books/' | relative_url }}) are the canonical monograph release. The site provides navigable access in understanding-order. [TauLib]({{ '/verify/taulib/' | relative_url }}) provides machine-checked verification. The guided tours and companion papers lower the threshold for structured engagement.

## Research-form legitimacy

Start with [Scope, Status & Scrutiny]({{ '/program/about/scope-status-and-scrutiny/' | relative_url }}) and the [Research Agenda]({{ '/program/research-agenda/' | relative_url }}). These pages state what kind of research object this is, what it refuses, and how its claims should be challenged.

## Corpus and registry inspection

Use [Corpus]({{ '/corpus/' | relative_url }}) for the public research body and [Corpus > Registry]({{ '/corpus/registry/' | relative_url }}) for the current registry projection. The registry is the inspection route for definitions, theorem objects, and dependency contexts.

## Results and problem ledger

Use [Results]({{ '/results/' | relative_url }}) for typed answer surfaces and [Results > Problem Ledger]({{ '/results/problem-ledger/' | relative_url }}) for the problem-facing map. Pick one result page and follow its linked Corpus and Verify routes before generalizing.

## Verification and TauLib

Use [Verify > Scientific Rigor]({{ '/verify/scientific-rigor/' | relative_url }}), [Verify > Formal Verification Stack]({{ '/verify/formal-verification-stack/' | relative_url }}), and [TauLib]({{ '/verify/taulib/' | relative_url }}) for the formal verification surface. Lean compilation checks internal formal claims; empirical claims still require empirical testing.

## Falsification and predictions

Use [Verify > Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }}) for prediction and falsification ownership. Results links these surfaces where relevant, but Verify is the canonical lane for assessment and challenge.

## Assessment protocols

Use [Verify > Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) for structured critique. These protocols are the first place to route formal-methods review, domain review, prior-art review, and LLM-assisted review workflows.

## Suggested first-pass reviewer workflow

1. Start with [Program > Scope, Status & Scrutiny]({{ '/program/about/scope-status-and-scrutiny/' | relative_url }}).
2. Read [Program > Research Agenda]({{ '/program/research-agenda/' | relative_url }}).
3. Inspect [Corpus > Registry]({{ '/corpus/registry/' | relative_url }}).
4. Choose one [Results]({{ '/results/' | relative_url }}) page.
5. Follow supporting Corpus links.
6. Check [Verify > Formal Verification Stack]({{ '/verify/formal-verification-stack/' | relative_url }}).
7. Review relevant [TauLib]({{ '/verify/taulib/' | relative_url }}) and proof surfaces.
8. Use [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) for structured critique.

## Domain-oriented paths

### Mathematics-first path
1. [Book I: Categorical Foundations]({{ '/publications/books/book-i/' | relative_url }})
2. [Book II: Categorical Holomorphy]({{ '/publications/books/book-ii/' | relative_url }})
{% assign math_results = site.data.results.results | where: "topic", "mathematics" %}3. [Results by Domain: Mathematics]({{ '/results/topic/mathematics/' | relative_url }}) ({{ math_results | size }} results)
4. [Registry — Book I]({{ '/registry/books/book-i/' | relative_url }})
5. [Guided Tours — Foundations](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/Foundations.lean)

### Physics-first path
1. [Book III: Categorical Spectrum]({{ '/publications/books/book-iii/' | relative_url }}) (the hinge)
2. [Book IV: Categorical Microcosm]({{ '/publications/books/book-iv/' | relative_url }})
3. [Book V: Categorical Macrocosm]({{ '/publications/books/book-v/' | relative_url }})
{% assign phys_results = site.data.results.results | where: "topic", "physics" %}4. [Results by Domain: Physics]({{ '/results/topic/physics/' | relative_url }}) ({{ phys_results | size }} results)
5. [Guided Tours — Physics](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/Physics.lean)

### Life and metaphysics path
1. [Book VI: Categorical Life]({{ '/publications/books/book-vi/' | relative_url }})
2. [Book VII: Categorical Metaphysics]({{ '/publications/books/book-vii/' | relative_url }})
{% assign bio_results = site.data.results.results | where: "topic", "biology" %}{% assign phil_results = site.data.results.results | where: "topic", "philosophy" %}3. [Results by Domain: Biology]({{ '/results/topic/biology/' | relative_url }}) ({{ bio_results | size }} results)
4. [Results by Domain: Philosophy]({{ '/results/topic/philosophy/' | relative_url }}) ({{ phil_results | size }} results)

### Formal verification path
1. [Verify]({{ '/verify/' | relative_url }})
2. [TauLib repository](https://github.com/Panta-Rhei-Research/taulib) — clone and run `lake build`
3. [Guided Tours — VerifyItYourself](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/VerifyItYourself.lean)
{% assign reg_count = site.data.registry.objects | size %}4. [Registry]({{ '/corpus/registry/' | relative_url }}) — {{ reg_count }} objects with dependency graphs

## Suggested starter packet

For a reviewer who wants to form a first impression in 30-60 minutes:

1. **[Program > About the Program]({{ '/program/about/' | relative_url }})** — what the program is (5 min)
2. **[Why So Many Results Are Possible]({{ '/results/why-so-many-results/' | relative_url }})** — how constraint enables breadth (5 min)
3. **[Status and Claim Typing]({{ '/results/status-and-claim-typing/' | relative_url }})** — how claims are typed (5 min)
4. **Pick 3 results** from [Results]({{ '/results/' | relative_url }}) in your domain (15 min)
5. **[Verify]({{ '/verify/' | relative_url }})** — how to inspect further (5 min)
6. **One guided tour** from [Guided Tours]({{ '/publications/guided-tours/' | relative_url }}) (15 min)

## What This Page Does Not Claim

- This is **not a substitute for expert review**. The program invites scrutiny; it does not pre-empt it.
- **Lean compilation verifies internal consistency**, not physical truth. Empirical claims require empirical testing.
- **No expectation** that one reader resolves the whole program in one sitting. The review paths are starting points.
- The program is **independent research** — not yet peer-reviewed in traditional journals. All claims carry explicit [scope labels]({{ '/results/status-and-claim-typing/' | relative_url }}).

## Contact

- **Peer review**: [review@panta-rhei.site](mailto:review@panta-rhei.site)
- **Media**: [press@panta-rhei.site](mailto:press@panta-rhei.site)
- **Technical inquiries**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject: "Technical Inquiry"
- **Institutional**: [inquiry@panta-rhei.site](mailto:inquiry@panta-rhei.site)
- **Corrections / errata**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)
