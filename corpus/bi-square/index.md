---
layout: program-doc
title: "The Bi-Square Spine"
permalink: /corpus/bi-square/
lane: corpus
v2_lane: corpus
section: "bi-square"
type: "Corpus Route"
status: "Canonical"
summary_short: "The repeated proof-organizing shape of the kernel: tower coherence on the left, spectral naturality on the right, and a pasted constraint that becomes richer across the construction."
og_image: /assets/images/plates/plate-15-bi-square-spine-og.jpg
twitter_image: /assets/images/plates/plate-15-bi-square-spine-og.jpg
og_image_alt: "Scientific plate showing the Bi-Square Spine as a repeated two-by-three pasted diagram with tower coherence, spectral naturality, and a scaling chain from algebraic to computational bi-squares."
key_registry:
  - I.T41
  - II.D77
  - II.T49
  - III.D65
  - III.T39
  - III.D56
hero_ctas:
  - label: "Open I.T41"
    url: /registry/object/I.T41/
    primary: true
  - label: "Construction Spine"
    url: /corpus/construction-spine/
  - label: "TauLib Route"
    url: /verify/taulib/
right_rail:
  related:
    - title: "Construction Spine"
      url: /corpus/construction-spine/
    - title: "Foundational Hinges"
      url: /corpus/foundational-hinges/
    - title: "Registry"
      url: /corpus/registry/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Book I Bi-Square Chapter"
      url: /corpus/monographs/book-i/part-16-the-presheaf-essence/chapter-70-the-holomorphy-bi-square/
    - title: "Book II Geometric Bi-Square"
      url: /corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/chapter-60-the-geometric-bi-square/
    - title: "Book III Enriched Bi-Square"
      url: /corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-47-the-enriched-bi-square/
    - title: "Book III Computational Bi-Square"
      url: /corpus/monographs/book-iii/part-09-where-life-lives/chapter-61-the-computational-bi-square/
    - title: "Verify"
      url: /verify/
  artifacts:
    - title: "TauLib: Book I BiSquare"
      url: /verify/taulib/docs/book-i-holomorphy-presheaf-essence/
    - title: "TauLib: Geometric Bi-Square"
      url: /verify/taulib/docs/book-ii-closure-geometric-bi-square/
    - title: "TauLib: Enriched Bi-Square"
      url: /verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/
    - title: "TauLib: Computational Bi-Square"
      url: /verify/taulib/docs/book-iii-computation-comp-bi-square/
  meta:
    type: "Corpus Route"
    scope: "Bi-square scaling chain"
    status: "Canonical"
    updated: "April 2026"
---

## What the bi-square is

{% include scientific-plate.html id="plate-15-bi-square-spine" class="scientific-plate--bi-square-spine" loading="eager" %}

The bi-square is the Corpus route for a repeated categorical shape. It is a pasted `2 x 3` diagram: the left square records tower coherence, the right square records spectral naturality, and the whole pasted rectangle carries the layer-specific constraint.

The first form appears in Book I as [I.T41]({{ '/registry/object/I.T41/' | relative_url }}), the Bi-Square Characterization. There it says that a family is tau-holomorphic precisely when both squares commute. That same shape is then lifted into richer settings: geometry in Book II, arithmetic enrichment in Book III, and computation in the tau-admissible layer.

## Why it matters

The [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}) explains the build order of the Corpus. The Bi-Square Spine explains a different thing: the stable diagrammatic form that keeps reappearing inside that build.

That distinction matters. A reader can follow the construction step by step and still miss the repeated categorical shape. The bi-square makes that shape visible. It shows how the framework can preserve one proof architecture while changing the carried objects, morphisms, and pasting law.

## The scaling chain

| Stage | Registry anchor | Left square | Right square | Pasting constraint |
| --- | --- | --- | --- | --- |
| Algebraic / holomorphy | [I.T41]({{ '/registry/object/I.T41/' | relative_url }}) | Tower coherence of stage functions | Spectral naturality of the bipolar decomposition | tau-holomorphy and the limit principle |
| Geometric | [II.D77]({{ '/registry/object/II.D77/' | relative_url }}), [II.T49]({{ '/registry/object/II.T49/' | relative_url }}) | Holomorphic extension on the geometric carrier | Boundary-value / spectral algebra compatibility | Central Theorem reading of holomorphic sections and spectral algebra |
| Enriched | [III.D65]({{ '/registry/object/III.D65/' | relative_url }}), [III.T39]({{ '/registry/object/III.T39/' | relative_url }}) | Sector-coupled tower coherence | Functorial spectral naturality | Finite factorization through sector components |
| Computational | [III.D56]({{ '/registry/object/III.D56/' | relative_url }}) | TTM execution as tower coherence | CRT-decomposed witness structure | Product-Meet Collapse in the tau-admissible fragment |

The public lesson is compact: same shape, richer objects.

## Source anchors

The bi-square is already present in the public Corpus, but until now it was distributed across several projections.

- Book I gives the algebraic seed in [Chapter 70: The Holomorphy Bi-Square]({{ '/corpus/monographs/book-i/part-16-the-presheaf-essence/chapter-70-the-holomorphy-bi-square/' | relative_url }}).
- Book II gives the geometric lift in [Chapter 60: The Geometric Bi-Square]({{ '/corpus/monographs/book-ii/part-10-closure-synthesis-and-bridge-to-book-iii/chapter-60-the-geometric-bi-square/' | relative_url }}).
- Book III gives the enriched lift in [Chapter 47: The Enriched Bi-Square]({{ '/corpus/monographs/book-iii/part-06-the-arithmetic-mirror/chapter-47-the-enriched-bi-square/' | relative_url }}).
- Book III gives the computational lift in [Chapter 61: The Computational Bi-Square]({{ '/corpus/monographs/book-iii/part-09-where-life-lives/chapter-61-the-computational-bi-square/' | relative_url }}).

Use this page as the synthesis route. Use the linked chapters, registry entries, and TauLib docs when you need exact local detail.

## Verification routes

The bi-square should be inspected through three public projections:

1. [Registry]({{ '/corpus/registry/' | relative_url }}) for atomic objects and dependencies.
2. [Corpus Monographs]({{ '/corpus/monographs/' | relative_url }}) for narrative proof order.
3. [TauLib]({{ '/verify/taulib/' | relative_url }}) for formalization surfaces where the corresponding modules are available.

The key TauLib routes are:

- [Book I Holomorphy / Presheaf Essence]({{ '/verify/taulib/docs/book-i-holomorphy-presheaf-essence/' | relative_url }})
- [Book II Geometric Bi-Square]({{ '/verify/taulib/docs/book-ii-closure-geometric-bi-square/' | relative_url }})
- [Book III Enriched Bi-Square]({{ '/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/' | relative_url }})
- [Book III Computational Bi-Square]({{ '/verify/taulib/docs/book-iii-computation-comp-bi-square/' | relative_url }})

## What this route does not claim

This page is an orientation route, not a substitute for proof checking or external review.

- The plate is a diagrammatic guide, not a proof.
- The bi-square is a proof-organizing shape, not empirical evidence.
- The four stages are not identical in content; they preserve shape while changing objects, morphisms, and constraints.
- The computational stage is about the tau-admissible fragment, not a claim about unrestricted classical complexity.

Use the page to see the spine. Use Registry, TauLib, the monographs, and external review to inspect whether the spine holds.
