---
layout: program-doc
title: "Cite"
lane: utility
permalink: /cite/
summary_short: "How to cite the Panta Rhei Research Program and the seven-book monograph series."
summary_cards:
- title: "Seven DOIs"
  body: "Each book has a Zenodo DOI identifying the canonical 2nd-edition manuscript record."
- title: "One program"
  body: "Cite individual books by DOI, or cite the program as a whole via the site URL."
- title: "Edition discipline"
  body: "Always cite the specific edition consulted. The DOI identifies the exact manuscript version."
right_rail:
  related:
  - title: Publications
    url: /publications/
  - title: The Seven Books
    url: /publications/books/
  - title: About the Research
    url: /program/about/
  meta:
    type: "Citation"
    status: "Canonical"
    updated: "April 2026"
---

## How to Cite

Each [book]({{ '/publications/books/' | relative_url }}) in the Panta Rhei series has a **Zenodo DOI** that identifies the canonical manuscript record for the current 2nd Edition. Retail formats (Kindle, hardcover, paperback) share the same manuscript content — the DOI is the stable scholarly identifier.

When citing, please reference the **specific edition consulted** and use the version DOI.

## Citation Strings

{% for d in site.data.publications.dois %}
### Book {{ d.book_id }}: {{ d.title }}

{{ d.creators | join: " & " }} ({{ d.publication_date | slice: 0, 4 }}). *{{ d.title }}: {{ d.subtitle }}*. Panta Rhei Research Program, 2nd Edition. Zenodo. [{{ d.version_doi_url }}]({{ d.version_doi_url }})

**DOI**: [`{{ d.version_doi }}`]({{ d.version_doi_url }})
{% if d.concept_doi %} **All versions**: [`{{ d.concept_doi }}`]({{ d.concept_doi_url }}){% endif %}
{% if d.isbn_hardcover_or_primary %} **ISBN**: {{ d.isbn_hardcover_or_primary }}{% endif %}
**Zenodo record**: [{{ d.record_url }}]({{ d.record_url }})
**Book page**: [{{ d.title }}]({{ '/publications/books/' | append: d.slug | append: '/' | relative_url }})

{% endfor %}

## Citing the Research Program

To cite the research program as a whole rather than an individual book:

> Fuchs, T. & Fuchs, A.-S. (2026). *Panta Rhei: Category τ and the Four-Layer Architecture of Reality*. 7-volume monograph series, 2nd Edition. [https://panta-rhei.site](https://panta-rhei.site)

## Citing the Formalization

> Fuchs, T. & Fuchs, A.-S. (2026). *TauLib: Lean 4 Formalization Library for Category τ*. [https://github.com/Panta-Rhei-Research/taulib](https://github.com/Panta-Rhei-Research/taulib)

For more on TauLib and what the [formalization]({{ '/verify/taulib/' | relative_url }}) covers, see the Verify lane.

## Notes

- **Edition discipline**: If a future edition changes the manuscript materially, a new Zenodo version will be minted with a new DOI. Always cite the version you consulted.
- **Retail identifiers**: ASINs and ISBNs identify retail formats, not manuscript versions. For academic citation, use the Zenodo DOI.
- **BibTeX**: Machine-readable citation exports are planned for a future release. In the meantime, see the [bibliography]({{ '/bibliography/' | relative_url }}) for the program's reference list.
