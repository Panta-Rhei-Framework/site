---
layout: program-doc
title: "Scientific Plates — the visual atlas"
permalink: /media/posters/
lane: support
type: support_page
support_type: media
status: canonical
updated: "April 2026"
summary: "All scientific plates published as part of the Panta Rhei Research Program — wayfinding maps and τ-architecture visualisations, with print-quality master files for journalism, talks, conferences, and bulletin-board print."
summary_short: "Visual atlas of every scientific plate published by the program — print-quality masters under CC BY 4.0."
right_rail:
  related:
  - title: Media Kit
    url: /media/
  - title: Review Kit
    url: /media/review-kit/
  - title: Brand
    url: /brand/
  - title: Cite
    url: /cite/
  - title: Credits
    url: /credits/
  meta:
    type: "Visual Atlas"
    scope: "All published plates"
    status: "Canonical"
    updated: "April 2026"
---

The plates listed below are the program's **visual atlas**: editorial-quality scientific posters that compress structural arguments into single-frame readable maps. Each plate carries the same epistemic discipline as the prose: scope labels remain visible, failed alternatives stay in frame, and every map identifies what is *posited*, what is *constructed*, and what is *open*.

All plates are released under [**Creative Commons Attribution 4.0 International**](https://creativecommons.org/licenses/by/4.0/) — share, adapt, print, and re-host with attribution to the Panta Rhei Research Program.

## How to use these

- **For the press, podcasts, and reviewers** — each plate's print master is 1536 × 864 JPG, suitable for editorial layouts, conference talks, slide decks, and printed handouts. Right-click any "Download print master" link to save the high-resolution file.
- **For specialists** — each plate carries a list of pages where it is canonically embedded; the surrounding prose is the load-bearing argument, and the plate is the structural map of that argument.
- **For cross-site embedding** — the machine-readable index lives at [`/api/plates.json`](/api/plates.json) (CC BY 4.0; CORS-permissive).

If you publish or print any of these plates, we ask that the attribution remain visible — *Panta Rhei Research Program · panta-rhei.site* — and that you link to the canonical page where the plate is embedded so readers can locate the load-bearing prose.

## The atlas — {{ site.data.plates | size }} plates

{% assign plates_sorted = site.data.plates | sort: "id" %}
{% for plate in plates_sorted %}
<section id="{{ plate.id }}" class="scientific-plate-gallery-card">

### {{ plate.title }}

{% include scientific-plate.html id=plate.id variant="hero" loading="lazy" show_download=true %}

{% if plate.pages and plate.pages.size > 0 %}
**Embedded on:** {% for p in plate.pages %}<a href="{{ p | relative_url }}"><code>{{ p }}</code></a>{% if forloop.last == false %} · {% endif %}{% endfor %}
{% endif %}

</section>

{% unless forloop.last %}<hr class="plate-gallery-divider">{% endunless %}
{% endfor %}

## Attribution and re-use

Every plate is a derivative of the canonical prose argument it accompanies. When you cite or re-publish a plate, please cite the **canonical page** (the first entry in *Embedded on*), not just the plate file.

The recommended attribution line is:

> *Panta Rhei Research Program · [panta-rhei.site](https://panta-rhei.site) · CC BY 4.0*

For institutional citations, see [`/cite/`](/cite/) for canonical DOIs and ORCID IDs. For licensing edge cases, see [`/credits/`](/credits/) and [`/impressum/`](/impressum/).

## How to challenge a plate

A plate that misrepresents the underlying argument is a worse signal than a plate that is honestly imperfect. If you think any plate above is structurally inaccurate, mis-scoped, or hides a discipline that the prose carries, **please tell us**. Open an issue at [`Panta-Rhei-Research/site`](https://github.com/Panta-Rhei-Research/site/issues) or write to [errata@panta-rhei.site](mailto:errata@panta-rhei.site). Plates are versioned alongside the prose they map.
