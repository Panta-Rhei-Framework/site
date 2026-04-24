---
layout: program-doc
title: "Cite"
lane: support
type: support_page
support_type: cite
status: canonical
updated: "April 2026"
permalink: /cite/
summary: "Citation guidance for the Panta Rhei Research Program, the public website, the books, TauLib, Research Notes, and individual public artifacts."
summary_short: "How to cite the Panta Rhei Research Program, the public website, the books, TauLib, Research Notes, and individual public artifacts."
summary_cards:
- title: "Seven DOIs"
  body: "Each book has a Zenodo DOI identifying the canonical 2nd-edition manuscript record."
- title: "One program"
  body: "Cite individual books by DOI, or cite the public Atlas and research program via canonical URLs."
- title: "Edition discipline"
  body: "Always cite the specific edition consulted. The DOI identifies the exact manuscript version."
right_rail:
  related:
  - title: Publications
    url: /publications/
  - title: The Seven Books
    url: /publications/books/
  - title: Research Notes
    url: /publications/research-notes/
  - title: Corpus
    url: /corpus/
  - title: Program
    url: /program/about/
  meta:
    type: "Support page"
    scope: "Citation"
    status: "Canonical"
    updated: "April 2026"
---

## Cite the website / public Atlas

Use this page to cite the Panta Rhei Research Program, the public website, the books, TauLib, Research Notes, and individual pages or artifacts.

> Fuchs, T. & Fuchs, A.-S. (2026). *Panta Rhei Research Program*. Public research website and Atlas. [https://panta-rhei.site](https://panta-rhei.site)

When a citation depends on a specific surface, prefer the canonical page URL: [Corpus]({{ '/corpus/' | relative_url }}), [Results]({{ '/results/' | relative_url }}), [Verify]({{ '/verify/' | relative_url }}), [Publications]({{ '/publications/' | relative_url }}), or an individual page.

## Cite the books

Each [book]({{ '/publications/books/' | relative_url }}) in the Panta Rhei series has a **Zenodo DOI** that identifies the canonical manuscript record for the current 2nd Edition. Retail formats (Kindle, hardcover, paperback) share the same manuscript content; the DOI is the stable scholarly identifier.

When citing, please reference the **specific edition consulted** and use the version DOI.

## Book citation strings

{% for d in site.data.publications.dois %}
### Book {{ d.book_id }}: {{ d.title }}

{{ d.creators | join: " & " }} ({{ d.publication_date | slice: 0, 4 }}). *{{ d.title }}: {{ d.subtitle }}*. Panta Rhei Research Program, 2nd Edition. Zenodo. [{{ d.version_doi_url }}]({{ d.version_doi_url }})

**DOI**: [`{{ d.version_doi }}`]({{ d.version_doi_url }})
{% if d.concept_doi %} **All versions**: [`{{ d.concept_doi }}`]({{ d.concept_doi_url }}){% endif %}
{% if d.isbn_hardcover_or_primary %} **ISBN**: {{ d.isbn_hardcover_or_primary }}{% endif %}
**Zenodo record**: [{{ d.record_url }}]({{ d.record_url }})
**Book page**: [{{ d.title }}]({{ '/publications/books/' | append: d.slug | append: '/' | relative_url }})

{% endfor %}

## Cite TauLib

> Fuchs, T. & Fuchs, A.-S. (2026). *TauLib: Lean 4 Formalization Library for Category τ*. [https://github.com/Panta-Rhei-Research/taulib](https://github.com/Panta-Rhei-Research/taulib)

For more on TauLib and what the [formalization]({{ '/verify/taulib/' | relative_url }}) covers, see the Verify lane and the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}).

## Cite Research Notes

For Research Notes, cite the individual note URL and publication date shown on the note page:

> Fuchs, T. & Fuchs, A.-S. (2026). *[Research Note title]*. Panta Rhei Research Program. [canonical note URL]

Browse current notes at [Research Notes]({{ '/publications/research-notes/' | relative_url }}).

## Cite individual pages

For a specific result, registry item, publication surface, or verification page, cite the page title, the site name, and its canonical URL:

> Fuchs, T. & Fuchs, A.-S. (2026). *[Page title]*. Panta Rhei Research Program. [canonical page URL]

This is the right pattern for individual [Results]({{ '/results/' | relative_url }}), [Corpus registry]({{ '/corpus/registry/' | relative_url }}) pages, [TauLib documentation]({{ '/verify/taulib/docs/' | relative_url }}), and support pages such as this one.

## Citation notes

- **Edition discipline**: If a future edition changes the manuscript materially, a new Zenodo version will be minted with a new DOI. Always cite the version you consulted.
- **Retail identifiers**: ASINs and ISBNs identify retail formats, not manuscript versions. For academic citation, use the Zenodo DOI.
- **BibTeX**: Machine-readable citation exports are planned for a future release. In the meantime, see the [bibliography]({{ '/bibliography/' | relative_url }}) for the program's reference list.
