---
layout: program-doc
title: "Errata"
lane: publications
permalink: /publications/errata/
summary_short: "Public changelog for substantial corrections to the Panta Rhei 2nd Edition books, verification surfaces, registry entries, and associated publications."
summary_cards:
  - title: "Substantial only"
    body: "Entries here are corrections that affect a registered theorem, definition, registry ID, downstream citation, or public verification surface."
  - title: "Append-only"
    body: "Issued errata are never deleted. Superseded entries remain visible and point to their replacement."
  - title: "Active record"
    body: "Four active errata are currently issued for the 2nd Edition corpus and associated public artifacts."
right_rail:
  related:
    - title: "Publications Overview"
      url: /publications/
    - title: "The Seven Books"
      url: /publications/books/
    - title: "The Panta Rhei Conspectus"
      url: /publications/conspectus/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Public Changelog"
    scope: "2nd Edition corpus"
    status: "Active"
    updated: "April 2026"
---

## Purpose

This page records **substantial corrections** to the published 2nd Edition of the *Panta Rhei* monograph series and its public companion surfaces. A correction appears here when it changes a registered theorem, a definition used downstream, a registry object, a citation target, or a public verification claim.

Purely typographical fixes are intentionally excluded from this page. The purpose is not to make ordinary copy-editing visible; it is to keep the public mathematical and verification record citeable.

## Issued Errata

{% assign errata = site.data.publications.errata | sort: "id" %}
{% for entry in errata %}
### {{ entry.id }} — {{ entry.affected }}

| Field | Value |
|---|---|
| Issued | {{ entry.issued }} |
| Status | {{ entry.status }} |
| Severity | {{ entry.severity }} |
{% if entry.registry_ids.size > 0 %}
| Registry anchors | {% for reg_id in entry.registry_ids %}[{{ reg_id }}]({{ '/registry/object/' | append: reg_id | append: '/' | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %} |
{% endif %}

{{ entry.summary }}

**Correction.** {{ entry.replacement }}

{% endfor %}

## Status Convention

- **Active** means the correction is citeable and should be used when reading or quoting the affected material.
- **Superseded** means a later erratum refines or replaces the correction while preserving the historical record.
- **Applied** means the correction has landed in a later print run, registry release, or verification artifact.

## Citation Guidance

When citing affected material, cite the original book location and the relevant erratum ID together. Example: *Book I, Theorem I.T05, as corrected by ERRATUM-001*.
