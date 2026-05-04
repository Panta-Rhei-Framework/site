---
layout: "program-doc"
title: "Recovery Target Status"
permalink: "/results/recovery-target-status/"
lane: "results"
v2_lane: "results"
type: "Result Mirror"
status: "Canonical"
summary_short: "Current Results-side status against public Recovery Requirements."
---

> Current program status against the structures the kernel promised to recover.

This is the Results-side mirror of the Program-side Recovery Requirements ledger. Recovery requirements remain obligations; this surface reports their current public status.

<div class="notice note"><strong>Status note.</strong> Partial or internally addressed recovery is not the same as formal verification or external acceptance.</div>

## Browse by domain

{% assign recovery_items = site.data.recovery_requirements["recovery-requirements"] %}
{% assign recovery_domains = "mathematics,physics,life,metaphysics" | split: "," %}
<ul class="v2-grid v2-card-list">
{% for domain in recovery_domains %}
  {% assign domain_items = recovery_items | where: "domain_slug", domain %}
  {% assign partial_count = domain_items | where: "recovery_status", "partial" | size %}
  {% assign not_applicable_count = domain_items | where: "recovery_status", "not_applicable" | size %}
  {% assign pending_count = domain_items | where: "recovery_status", "pending_recovery" | size %}
  {% if partial_count >= not_applicable_count and partial_count >= pending_count %}
    {% assign dominant_status = "Partial" %}
  {% elsif not_applicable_count >= partial_count and not_applicable_count >= pending_count %}
    {% assign dominant_status = "Not applicable / refused" %}
  {% else %}
    {% assign dominant_status = "Pending recovery" %}
  {% endif %}
  <li>
    <article class="v2-tile">
      <h3>{{ domain | replace: '-', ' ' | capitalize }}</h3>
      <p>{{ domain_items | size }} public recovery/refusal item{% unless domain_items.size == 1 %}s{% endunless %}.</p>
      <p><strong>Dominant status:</strong> {{ dominant_status }}</p>
      <p><a href="{{ '/results/recovery-target-status/' | append: domain | append: '/' | relative_url }}">Results mirror</a> · <a href="{{ '/agenda/core-semantics/' | append: domain | append: '/' | relative_url }}">Recovery Requirements</a></p>
    </article>
  </li>
{% endfor %}
</ul>
