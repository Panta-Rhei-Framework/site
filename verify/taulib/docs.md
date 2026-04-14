---
layout: program-doc
title: "TauLib API Documentation"
permalink: /verify/taulib/docs/
lane: verify
summary_short: "445 module documentation pages generated from the TauLib Lean 4 source code."
summary_cards:
- title: "445 modules"
  body: "Complete API documentation for every TauLib module, generated from source annotations."
- title: "7 books"
  body: "Organized by book: Foundations through Metaphysics, plus Tours."
- title: "Searchable"
  body: "Browse by book or search the full site to find any declaration."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  - title: Formalization Status
    url: /verify/taulib/status/
  artifacts:
  - title: TauLib Repository
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Index"
    status: "Frozen"
    updated: "April 2026"
---

## Browse by Book

{% assign modules = site.data.verify.taulib_modules %}

{% assign books = "I,II,III,IV,V,VI,VII,Tour" | split: "," %}
{% for book in books %}
{% assign book_modules = modules | where: "book", book %}
{% if book_modules.size > 0 %}
### Book {{ book }} ({{ book_modules.size }} modules)

{% for m in book_modules %}- [{{ m.module }}]({{ m.url | relative_url }})
{% endfor %}
{% endif %}
{% endfor %}

{% assign other_modules = modules | where: "book", "" %}
{% if other_modules.size > 0 %}
### Other ({{ other_modules.size }} modules)

{% for m in other_modules %}- [{{ m.module }}]({{ m.url | relative_url }})
{% endfor %}
{% endif %}
