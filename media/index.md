---
layout: program-doc
title: "Media Kit"
permalink: /media/
lane: utility
summary_short: "Press, podcast, and review resources for the Panta Rhei Research Program."
summary_cards:
- title: "What this is"
  body: "Downloadable materials, press resources, and structured entry surfaces for journalists, podcast hosts, reviewers, and institutions."
- title: "Current release"
  body: "Seven-book monograph series (2nd Edition, April 2026), TauLib formalization, research website."
- title: "Contact"
  body: "press@panta-rhei.site for journalists, review@ for peer review"
right_rail:
  related:
  - title: Review Kit
    url: /media/review-kit/
  - title: About the Research
    url: /research-program/about/
  - title: Media & Contact
    url: /engage/media-and-contact/
  - title: White Papers
    url: /publications/white-papers/
  meta:
    type: "Media Kit"
    status: "Active"
    updated: "April 2026"
---

## About the Program

The Panta Rhei Research Program is an independent open research program developing **Category τ** — a categorical framework built from five generators, seven axioms, and one operator that derives results across mathematics, physics, biology, and philosophy from a single coherence kernel.

{% assign book_count = site.data.publications.books | size %}{% assign result_count = site.data.results.results | size %}{% assign registry_count = site.data.registry.objects | size %}{% assign chapter_count = site.data.publications.chapters | size %}The program's canonical release (April 2026) includes:
- A **{{ book_count }}-book monograph series** (~3,430 pages, available on Amazon KDP)
- A **Lean 4 formalization library** (TauLib, 450 modules, 0 sorry in Books I–VI)
- This **research website** ({{ result_count }} key results, {{ registry_count }} registry objects)
- **Guided tours** and **structural falsification whitepapers**

## Quick Facts

- **Authors**: Dr. Thorsten Fuchs & Anna-Sophie Fuchs
- **Framework**: 5 generators, 7 axioms (K0–K6), 1 operator (ρ)
- **Master constant**: ι<sub>τ</sub> = 2/(π+e) ≈ 0.3413
- **Books**: {{ book_count }} volumes, {{ chapter_count }} chapters
- **Results**: {{ result_count }} key results across 4 domains
- **Formalization**: 125,771 lines of Lean 4, 4,332 theorems, zero sorry in Books I–VI
- **Registry**: {{ registry_count }} mathematical objects with dependency graphs
- **Falsification**: 220+ quantitative predictions with precision claims
- **Decisive test**: CMB-S4 tensor-to-scalar ratio r ≈ ι<sub>τ</sub>⁴ ≈ 0.0135
- **Status**: Independent research — not yet peer-reviewed in traditional journals

## Downloadable Materials

### Core Documents

| Document | Pages | Audience | Download |
|----------|:-----:|----------|----------|
| **Category τ at a Glance** | 1 | Everyone | [Download — Category τ at a Glance]({{ '/assets/media/category-tau-at-a-glance.pdf' | relative_url }}) |
| **Reader's Guide** | 3 | All readers | [Download — Reader's Guide]({{ '/assets/media/readers-guide.pdf' | relative_url }}) |
| **Falsification Pack** | 8 | Physicists, experimentalists | [Download — Falsification Pack]({{ '/assets/media/falsification-pack.pdf' | relative_url }}) |
| **Lean Verification Report** | 6 | Formal methods, mathematicians | [Download — Lean Verification Report]({{ '/assets/media/lean-verification-report.pdf' | relative_url }}) |
| **Reviewer's Dossier** | 4 | Journal reviewers, evaluators | [Download — Reviewer's Dossier]({{ '/assets/media/reviewers-dossier.pdf' | relative_url }}) |
| **Series Prospectus** | 23 | Academics, institutions | [Download — Series Prospectus]({{ '/assets/media/series-prospectus.pdf' | relative_url }}) |
| **Seminar Abstracts** | 4 | Seminar organizers | [Download — Seminar Abstracts]({{ '/assets/media/seminar-abstracts.pdf' | relative_url }}) |

### Guided Tours (one per book)

| Tour | Book | Download |
|------|------|----------|
| **Categorical Foundations** | Book I — How Mathematics Is Earned | [Download — Book I Tour]({{ '/assets/media/guided-tour-book-I.pdf' | relative_url }}) |
| **Categorical Holomorphy** | Book II — Finite Readouts of Infinity | [Download — Book II Tour]({{ '/assets/media/guided-tour-book-II.pdf' | relative_url }}) |
| **Categorical Spectrum** | Book III — Where Physics Lives | [Download — Book III Tour]({{ '/assets/media/guided-tour-book-III.pdf' | relative_url }}) |
| **Categorical Microcosm** | Book IV — The Self-Describing Universe | [Download — Book IV Tour]({{ '/assets/media/guided-tour-book-IV.pdf' | relative_url }}) |
| **Categorical Macrocosm** | Book V — The Biography of the Universe | [Download — Book V Tour]({{ '/assets/media/guided-tour-book-V.pdf' | relative_url }}) |
| **Categorical Life** | Book VI — Life as Self-Decoding Distinctions | [Download — Book VI Tour]({{ '/assets/media/guided-tour-book-VI.pdf' | relative_url }}) |
| **Categorical Metaphysics** | Book VII — The Final Self-Enrichment | [Download — Book VII Tour]({{ '/assets/media/guided-tour-book-VII.pdf' | relative_url }}) |

### Additional Research Assets

- **[BibTeX bibliography]({{ '/assets/bibliography/references.bib' | relative_url }})** — 1,124 references used by the program (downloadable .bib file)
- **[TauLib repository](https://github.com/Panta-Rhei-Research/taulib)** — Full Lean 4 source (clone and run `lake build`)

---

## Press Kit

### Program Boilerplate (copy-paste ready)

The Panta Rhei Research Program develops Category τ, a categorical framework that derives results across mathematics, physics, biology, and philosophy from five generators, seven axioms, and one operator. The program's seven-book monograph series (2nd Edition, April 2026) is accompanied by a Lean 4 formalization library, {{ result_count }} key results with typed epistemic status, and a public research website with {{ registry_count }} registry objects. All claims carry explicit scope labels and verification routes. The program is independent research — not yet peer-reviewed in traditional journals.

### Key Numbers

| Metric | Value |
|--------|------:|
| Books | {{ book_count }} |
| Total pages | ~3,430 |
| Chapters | {{ chapter_count }} |
| Key results | {{ result_count }} |
| Registry objects | {{ registry_count }} |
| Lean 4 modules | 450 |
| Lines of Lean 4 | 125,771 |
| Machine-checked theorems | 4,332 |
| Sorry (unproven) | 3 (Book VII only) |
| Free parameters | 0 |
| Quantitative predictions | 220+ |

### Author Bios

**Dr. Thorsten Fuchs** is the principal author of the Panta Rhei monograph series and the architect of Category τ. With a background in mathematics and over two decades in technology leadership, he returned to the foundational question — *what if reality is more deeply coherent than it first appears?* — and spent years developing the kernel, the proofs, the inter-book structure, and the formal verification layer through TauLib. He presents the work not as a finished final word, but as a research architecture published for scrutiny.

**Anna-Sophie Fuchs** is co-author of the series and co-developer of the research program's public engagement surfaces, guided tour architecture, and editorial structure. With a background in archaeology, she brings a distinctive perspective — layered structures, fragile connections, reconstruction from fragments — to a program that requires exactly those sensibilities. She is also the collaboration's first skeptical reader, pressing every large claim to justify not only its ambition, but also its language, scope, tone, and relation to human reality.

---

## Recommended Starting Points

### For general-audience journalists
1. [About the Research]({{ '/research-program/about/' | relative_url }})
2. [Claims overview]({{ '/results/' | relative_url }}) — {{ result_count }} results with typed status
3. [Why So Many Results Are Possible]({{ '/results/why-so-many-results/' | relative_url }})

### For science/mathematics journalists
1. [The Tau Framework]({{ '/framework/about/' | relative_url }})
2. [Results by Domain]({{ '/results/by-domain/' | relative_url }})
3. [Verify]({{ '/verify/' | relative_url }}) — how to inspect the claims

### For podcast hosts
1. Start with the [About the Research]({{ '/research-program/about/' | relative_url }}) page
2. Choose 2–3 results from [Claims]({{ '/results/' | relative_url }}) relevant to your audience
3. The [Status and Claim Typing]({{ '/results/status-and-claim-typing/' | relative_url }}) page explains the program's epistemic discipline

## Contact

**Media inquiries**: [press@panta-rhei.site](mailto:press@panta-rhei.site)

**Technical inquiries**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject line: "Technical Inquiry"

**Institutional contact**: [inquiry@panta-rhei.site](mailto:inquiry@panta-rhei.site)

**Peer review**: [review@panta-rhei.site](mailto:review@panta-rhei.site)

**Errata & corrections**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)

See also: [Review Kit]({{ '/media/review-kit/' | relative_url }}) for reviewer-specific entry paths, and [Media & Contact]({{ '/engage/media-and-contact/' | relative_url }}) for the full list of topic-specific routes.
