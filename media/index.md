---
layout: program-doc
title: "Media Kit"
permalink: /media/
lane: utility
summary_short: "Press, podcast, and review resources for the Panta Rhei Research Program."
summary_cards:
- title: "What this is"
  body: "A structured entry surface for journalists, podcast hosts, reviewers, and institutions."
- title: "Current release"
  body: "Seven-book monograph series (2nd Edition, April 2026), TauLib formalization, research website."
- title: "Contact"
  body: "contact@panta-rhei.site — subject line: Media Inquiry"
right_rail:
  related:
  - title: Review Kit
    url: /media/review-kit/
  - title: About the Research
    url: /research-program/about/
  - title: Media & Contact
    url: /engage/media-and-contact/
  meta:
    type: "Media Kit"
    status: "Active"
    updated: "April 2026"
---

## About the Program

The Panta Rhei Research Program is an independent open research program developing **Category τ** — a categorical framework built from five generators, seven axioms, and one operator that derives results across mathematics, physics, biology, and philosophy from a single coherence kernel.

The program's canonical release (April 2026) includes:
{% assign book_count = site.data.publications.books | size %}{% assign result_count = site.data.results.results | size %}{% assign registry_count = site.data.registry.objects | size %}{% assign part_count = site.data.publications.parts | size %}{% assign chapter_count = site.data.publications.chapters | size %}- A **{{ book_count }}-book monograph series** (~3,430 pages, available on Amazon KDP)
- A **Lean 4 formalization library** (TauLib, 450 modules, 0 sorry in Books I-VI)
- This **research website** ({{ result_count }} key results, {{ registry_count }} registry objects)
- **Guided tours** and **structural falsification whitepapers**

## Quick Facts

- **Authors**: Dr. Thorsten Fuchs & Anna-Sophie Fuchs
- **Framework**: 5 generators, 7 axioms (K0-K6), 1 operator (ρ)
- **Master constant**: ι_τ = 2/(π+e) ≈ 0.3413
- **Books**: {{ book_count }} volumes, {{ chapter_count }} chapters, {{ part_count }} parts
- **Results**: {{ result_count }} key results across 4 domains
- **Formalization**: 125,771 lines of Lean 4 code, 4,332 theorems, 3,721 evals
- **Registry**: {{ registry_count }} mathematical objects with dependency graphs
- **Falsification**: 220+ quantitative predictions with precision claims
- **Status**: Independent research — not yet peer-reviewed in traditional journals

## Recommended Starting Points

### For general-audience journalists
1. [About the Research]({{ '/research-program/about/' | relative_url }})
2. [Key Results overview]({{ '/results/' | relative_url }}) — 85 results with typed status
3. [Why So Many Results Are Possible]({{ '/results/why-so-many-results/' | relative_url }})

### For science/mathematics journalists
1. [The Tau Framework]({{ '/framework/about/' | relative_url }})
2. [Results by Domain]({{ '/results/by-domain/' | relative_url }})
3. [Verify]({{ '/verify/' | relative_url }}) — how to inspect the claims

### For podcast hosts
1. Start with the [About the Research]({{ '/research-program/about/' | relative_url }}) page
2. Choose 2-3 results from [Key Results]({{ '/results/' | relative_url }}) relevant to your audience
3. The [Status and Claim Typing]({{ '/results/status-and-claim-typing/' | relative_url }}) page explains the program's epistemic discipline

## Downloadable Descriptions

### Short description (1 paragraph)
The Panta Rhei Research Program develops Category τ, a categorical framework that derives results across mathematics, physics, biology, and philosophy from five generators, seven axioms, and one operator. The program's seven-book monograph series (2nd Edition, April 2026) is accompanied by a Lean 4 formalization library, 85 key results with typed epistemic status, and a public research website with 4,547 registry objects. All claims carry explicit scope labels and verification routes.

### Author bios

**Dr. Thorsten Fuchs** is the principal author of the Panta Rhei monograph series and the architect of Category τ. The framework develops a unified mathematical foundation across four enrichment layers — mathematics, physics, life, and metaphysics — from a minimal axiomatic kernel.

**Anna-Sophie Fuchs** is co-author of the series and co-developer of the research program's public engagement surfaces, guided tour architecture, and editorial structure.

## Contact

**Media inquiries**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject line: "Media Inquiry"

**Technical inquiries**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject line: "Technical Inquiry"

**Institutional contact**: [contact@panta-rhei.site](mailto:contact@panta-rhei.site) — subject line: "Institutional"

See also: [Review Kit]({{ '/media/review-kit/' | relative_url }}) for reviewer-specific entry paths.
