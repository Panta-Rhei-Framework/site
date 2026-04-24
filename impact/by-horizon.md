---
layout: program-doc
title: Impact by Horizon
permalink: /impact/by-horizon/
lane: impact
summary_short: Portfolios grouped by time horizon.
right_rail:
  meta:
    type: Index
    updated: April 2026
---

## Portfolios by Time Horizon

This optional support index remains available for older links. The canonical portfolio home is [Global Public Good]({{ '/impact/global-public-good/' | relative_url }}).

{% for p in site.data.impact.portfolios %}
- **[{{ p.title }}]({{ p.url | relative_url }})** - {{ p.summary_short }} ({{ p.paper_count }} {% if p.paper_count == 1 %}paper{% else %}papers{% endif %})
{% endfor %}
