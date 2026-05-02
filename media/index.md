---
layout: program-doc
title: "Media Kit"
permalink: /media/
lane: support
type: support_page
support_type: media
status: canonical
updated: "April 2026"
summary: "Resources for journalists, public communicators, and external readers covering the Panta Rhei Research Program."
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
  - title: Story Angles
    url: /media/story-angles/
  - title: Journalist FAQ
    url: /media/journalist-faq/
  - title: Social Media Kit
    url: /media/social-media-kit/
  - title: Review Kit
    url: /media/review-kit/
  - title: Scientific Plates
    url: /media/posters/
  - title: Program
    url: /program/
  - title: Discover
    url: /discover/
  - title: Engage · Media
    url: /engage/media/
  - title: Engage · Contact
    url: /engage/contact/
  - title: White Papers
    url: /publications/white-papers/
  meta:
    type: "Support page"
    scope: "Media kit"
    status: "Canonical"
    updated: "April 2026"
---

## Short description

The Panta Rhei Research Program is an independent open research program developing **Category τ** — a categorical framework built from five generators, seven axioms, and one operator that derives results across mathematics, physics, biology, and philosophy from a single coherence kernel.

## What this is

This page gathers public materials for journalists, podcast hosts, public communicators, reviewers, and institutional readers. It is an entry surface into the current public site, not a replacement for the canonical lanes.

{% assign book_count = site.data.publications.books | size %}{% assign result_count = site.data.results.results | size %}{% assign registry_count = site.data.registry.objects | size %}{% assign chapter_count = site.data.publications.chapters | size %}The program's canonical release (April 2026) includes:
- A **{{ book_count }}-book monograph series** (~3,430 pages, available on Amazon KDP)
- A **Lean 4 formalization library** (TauLib, {% include release-metric.html id="taulib.modules" unit=true %}; the published formalized modules are built without `sorry`, while Book VI remains registry-planned and not yet fully Lean-formalized — see [filter rules]({{ '/verify/filter-rules/' | relative_url }}))
- This **research website** ({{ result_count }} key results, {{ registry_count }} registry objects)
- **Guided tours** and **structural falsification whitepapers**

## What this is not

This media kit is not a peer-review certificate, not a claim that every result is settled, and not a shortcut around the verification surfaces. Use it for orientation, then follow the relevant Program, Corpus, Results, Verify, and Publications routes.

---

## Press kit subpages

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/media/story-angles/' | relative_url }}">
    <h3>Story Angles</h3>
    <p>Five framings for journalists — independence, zero free parameters, falsification on day one, cross-domain scope, open verification. Each with a headline, 30-second pitch, and key-fact anchor.</p>
  </a>
  <a class="v2-tile" href="{{ '/media/journalist-faq/' | relative_url }}">
    <h3>Journalist FAQ</h3>
    <p>Common press questions: peer-review status, funding, citation, interview windows, embargo policy, headshots, and what to avoid writing.</p>
  </a>
  <a class="v2-tile" href="{{ '/media/social-media-kit/' | relative_url }}">
    <h3>Social Media Kit</h3>
    <p>Suggested posts for X, LinkedIn, Bluesky, Mastodon · hashtags · share-card recommendations · email signature blocks. All CC BY 4.0.</p>
  </a>
  <a class="v2-tile" href="{{ '/media/review-kit/' | relative_url }}">
    <h3>Review Kit</h3>
    <p>Reviewer-facing entry paths, verification surfaces, audit orientation, domain-specific paths, suggested first-pass workflow.</p>
  </a>
  <a class="v2-tile" href="{{ '/media/posters/' | relative_url }}">
    <h3>Scientific Plates</h3>
    <p>The program's visual atlas — print-quality 1536 × 864 master JPGs of every published scientific plate. CC BY 4.0; CORS-permissive index at /api/plates.json.</p>
  </a>
  <a class="v2-tile" href="{{ '/publications/white-papers/' | relative_url }}">
    <h3>White Papers</h3>
    <p>Concise documents for specific claims, falsification routes, interpretive bridges, and the TauLib v2.0 self-contained library.</p>
  </a>
</div>

## Decisive test — CMB-S4 r ≈ 0.0136

The single most journalism-leverageable framing: the program ships a **decisive falsification test on day one**. Category τ predicts the CMB-S4 tensor-to-scalar ratio at

> r ≈ ι<sub>τ</sub>⁴ ≈ **0.0136**

CMB-S4 — the next-generation CMB experiment, operational around 2030 — will measure r at a precision that distinguishes this prediction from competing inflationary models. **The framework is committed in advance.** If r ≈ 0.0136 the prediction succeeds; if r is materially different, the framework is in serious trouble.

For the full timeline + all {% include release-metric.html id="falsifications.records" %} named falsification tests, see [Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }}). For the angle's deeper framing, see [Story Angles → Falsification on day one]({{ '/media/story-angles/' | relative_url }}#angle-3--falsification-on-day-one).

## Quick Facts

- **Authors**: Dr. Thorsten Fuchs & Anna-Sophie Fuchs
- **Corpus kernel**: 5 generators, 7 axioms (K0–K6), 1 operator (ρ)
- **Master constant**: ι<sub>τ</sub> = 2/(π+e) ≈ 0.3413
- **Books**: {{ book_count }} volumes, {{ chapter_count }} chapters
- **Results**: {{ result_count }} key results across 4 domains
- **Formalization**: {% include release-metric.html id="taulib.lines" unit=true %} of Lean 4 and {% include release-metric.html id="taulib.theorems_lemmas" unit=true %} in the current public projection; published formalized modules are built without `sorry`
- **Registry**: {{ registry_count }} mathematical objects with dependency graphs
- **Predictions and falsification**: {% include release-metric.html id="predictions.records" %} quantitative prediction records plus {% include release-metric.html id="falsifications.records" %} named falsification tests in the current public projection
- **Decisive test**: CMB-S4 tensor-to-scalar ratio r ≈ ι<sub>τ</sub>⁴ ≈ 0.0136 (~2030)
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

### Recent Research Papers

The program publishes its research papers as standalone PDFs under [`/publications/research-papers/`]({{ '/publications/research-papers/' | relative_url }}), each with a Zenodo DOI for citation. Recent releases:

| Paper | DOI | Download |
|-------|-----|----------|
| **The Master Constant ι_τ** | [10.5281/zenodo.19820352](https://doi.org/10.5281/zenodo.19820352) | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-master-constant-iota-tau.pdf' | relative_url }}) |
| **Hyperfactorization Theorem** | _(see paper page)_ | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-hyperfactorization-theorem.pdf' | relative_url }}) |
| **Prime Polarity Theorem** | _(see paper page)_ | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-prime-polarity-theorem.pdf' | relative_url }}) |
| **τ-Holomorphy Boundary Algebra** | _(see paper page)_ | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-tau-holomorphy-boundary-algebra.pdf' | relative_url }}) |
| **Split-Complex Boundary Algebra** | _(see paper page)_ | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-split-complex-boundary-algebra.pdf' | relative_url }}) |
| **Address Resolution, Not Calculation** | _(see paper page)_ | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-address-resolution-not-calculation.pdf' | relative_url }}) |
| **Panta Rhei Foundational Bundle** | _(see paper page)_ | [Download PDF]({{ '/assets/pdfs/research-papers/research-paper-2026-04-27-panta-rhei-foundational-bundle.pdf' | relative_url }}) |

### Additional Research Assets

- **[Brand Assets & Guidelines]({{ '/brand/' | relative_url }})** — πρ mark (SVG/PNG), wordmark lockups, social headers, color palette, and usage rules for press and collaborators
- **[BibTeX bibliography]({{ '/assets/bibliography/references.bib' | relative_url }})** — {% include release-metric.html id="bibliography.references" unit=true %} used by the program (downloadable .bib file)
- **[Author headshots](https://github.com/Panta-Rhei-Research/site/blob/main/assets/media/headshots/README.md)** — high-resolution editorial headshots (request via [press@panta-rhei.site](mailto:press@panta-rhei.site) until publication)
- **[TauLib repository](https://github.com/Panta-Rhei-Research/taulib)** — Full Lean 4 source (clone and run `lake build`)

---

## Suggested starting points

- [Homepage]({{ '/' | relative_url }}) — high-level orientation.
- [Discover]({{ '/discover/' | relative_url }}) — guided entry routes.
- [Program]({{ '/program/' | relative_url }}) — identity, purpose, and research agenda.
- [Corpus]({{ '/corpus/' | relative_url }}) — central research artifact and registry projection.
- [Results]({{ '/results/' | relative_url }}) — typed answer surfaces and world readouts.
- [Verify]({{ '/verify/' | relative_url }}) — formalization, falsification, and assessment protocols.
- [Publications]({{ '/publications/' | relative_url }}) — books, white papers, Research Briefings, and Research Notes.
- [Engage]({{ '/engage/' | relative_url }}) — contact, media, critique, and participation routes.

## Key public surfaces

Use these lanes when describing the public site: Program for identity and agenda, Corpus for the central research body, Results for current answer surfaces, Verify for inspection and challenge, Publications for citable artifacts, and Engage for contact.

## Press kit

### Program Boilerplate (copy-paste ready)

Three lengths are provided — pick whichever fits your headline / lede / body needs.

#### One-line (under 30 words)

> Panta Rhei is an independent open research program developing **Category τ** — a categorical framework deriving results across mathematics, physics, biology, and philosophy with zero free parameters.

#### Standard (≈100 words)

> The Panta Rhei Research Program develops **Category τ**, a categorical framework that derives results across mathematics, physics, biology, and philosophy from five generators, seven axioms, and one operator. The program's seven-book monograph series (2nd Edition, April 2026) is accompanied by a Lean 4 formalization library, {{ result_count }} key results with typed epistemic status, a public research website with {{ registry_count }} registry objects, and a published falsification ledger including a decisive CMB-S4 prediction (r ≈ 0.0136 by 2030). All claims carry explicit scope labels and verification routes. The program is independent research — not yet peer-reviewed in traditional journals.

#### Long-form (≈200 words, original)

> The Panta Rhei Research Program develops Category τ, a categorical framework that derives results across mathematics, physics, biology, and philosophy from five generators, seven axioms, and one operator. The program's seven-book monograph series (2nd Edition, April 2026) is accompanied by a Lean 4 formalization library, {{ result_count }} key results with typed epistemic status, and a public research website with {{ registry_count }} registry objects. All claims carry explicit scope labels and verification routes. The program is independent research — not yet peer-reviewed in traditional journals.
>
> Distinctively, the framework operates with **zero dimensionless free parameters**: a single algebraic constant ι_τ = 2/(π+e) ≈ 0.3413, derived from the categorical kernel, plus one empirical anchor (the neutron mass) jointly determine every dimensionless ratio in the published constants ledger. The program publishes its falsification tests alongside its claims — most decisively, the CMB-S4 tensor-to-scalar prediction r ≈ ι_τ⁴ ≈ 0.0136, scheduled for measurement around 2030. The Lean 4 formalization (TauLib, {% include release-metric.html id="taulib.modules" unit=true %}) checks the framework's internal consistency; the published formalized modules are built without `sorry`. All review surfaces are public from day one.

### Key Numbers

| Metric | Value |
|--------|------:|
| Books | {{ book_count }} |
| Total pages | ~3,430 |
| Chapters | {{ chapter_count }} |
| Key results | {{ result_count }} |
| Registry objects | {{ registry_count }} |
| Lean 4 modules | {% include release-metric.html id="taulib.modules" %} |
| Lines of Lean 4 | {% include release-metric.html id="taulib.lines" %} |
| Machine-checked theorems | {% include release-metric.html id="taulib.theorems_lemmas" %} |
| Sorry (unproven) | 0 in the published formalized modules; Book VI remains registry-planned and not yet fully Lean-formalized |
| Free parameters | 0 |
| Quantitative predictions | {% include release-metric.html id="predictions.records" %} prediction records plus {% include release-metric.html id="falsifications.records" %} named falsification tests |

### Author Bios

**Dr. Thorsten Fuchs** is the principal author of the Panta Rhei monograph series and the architect of Category τ. With a background in mathematics and over two decades in technology leadership, he returned to the foundational question — *what if reality is more deeply coherent than it first appears?* — and spent years developing the kernel, the proofs, the inter-book structure, and the formal verification layer through TauLib. He presents the work not as a finished final word, but as a research architecture published for scrutiny.

**Anna-Sophie Fuchs** is co-author of the series and co-developer of the research program's public engagement surfaces, guided tour architecture, and editorial structure. With a background in archaeology, she brings a distinctive perspective — layered structures, fragile connections, reconstruction from fragments — to a program that requires exactly those sensibilities. She is also the collaboration's first skeptical reader, pressing every large claim to justify not only its ambition, but also its language, scope, tone, and relation to human reality.

Editorial-quality author headshots are available on request — see [Journalist FAQ → headshots and brand assets]({{ '/media/journalist-faq/' | relative_url }}#are-headshots-and-brand-assets-available) or write directly to [press@panta-rhei.site](mailto:press@panta-rhei.site).

---

## Images and attribution

Brand assets, diagrams, and public figures should be reused with attribution to the Panta Rhei Research Program unless a specific asset states otherwise. See [Credits & Attributions]({{ '/credits/' | relative_url }}) for licensing and third-party notices.

### Scientific plates — visual atlas

The program publishes a series of **scientific plates** — editorial-quality structural maps that compress key arguments into single-frame, scan-readable visuals. The full atlas (currently {{ site.data.plates | size }} plates, all CC BY 4.0) lives at [`/media/posters/`]({{ '/media/posters/' | relative_url }}), each with a print-quality 1536 × 864 master JPG suitable for editorial layouts, conference talks, slide decks, and printed handouts. A machine-readable index for cross-site embedding is published at [`/api/plates.json`]({{ '/api/plates.json' | relative_url }}) (CORS-permissive).

For social-media share cards, see [Social Media Kit → Share cards]({{ '/media/social-media-kit/' | relative_url }}#share-cards-visual-assets).

## Coverage tracker

**As of April 2026 — no third-party press coverage yet.** The program is independent research, openly published; coverage is welcome but not yet present. If you publish a piece on the program, please send the link to [press@panta-rhei.site](mailto:press@panta-rhei.site) and we will add it to a future "Recent Coverage" surface.

## Contact

**Media inquiries**: [press@panta-rhei.site](mailto:press@panta-rhei.site)

**Technical inquiries**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject line: "Technical Inquiry"

**Institutional contact**: [inquiry@panta-rhei.site](mailto:inquiry@panta-rhei.site)

**Peer review**: [review@panta-rhei.site](mailto:review@panta-rhei.site)

**Errata & corrections**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)

See also: [Journalist FAQ]({{ '/media/journalist-faq/' | relative_url }}) for press Q&A, [Story Angles]({{ '/media/story-angles/' | relative_url }}) for suggested framings, [Social Media Kit]({{ '/media/social-media-kit/' | relative_url }}) for share-ready posts, [Review Kit]({{ '/media/review-kit/' | relative_url }}) for reviewer-specific entry paths, [Engage · Media]({{ '/engage/media/' | relative_url }}) for press and public-communication context, and [Engage · Contact]({{ '/engage/contact/' | relative_url }}) for the full list of topic-specific routes.
