---
layout: program-doc
title: "Credits & Attributions"
lane: support
type: support_page
support_type: credits
status: canonical
updated: "April 2026"
permalink: /credits/
summary: "Third-party assets, open-source libraries, tooling, and license notes for panta-rhei.site."
summary_short: "Third-party assets, open-source libraries, and tooling that power panta-rhei.site — with licenses named explicitly."
right_rail:
  related:
  - title: Brand
    url: /brand/
  - title: Impressum
    url: /impressum/
  - title: Datenschutz
    url: /datenschutz/
  - title: Cite
    url: /cite/
  meta:
    type: "Support page"
    scope: "Credits"
    status: "Canonical"
    updated: "April 2026"
---

The Panta Rhei research site is handcrafted with the help of excellent open-source and third-party work. We thank the authors and communities behind the following tools and assets.

## Content license

All original site content — prose, diagrams, mathematics, registry objects, and results — is released under
[**Creative Commons Attribution 4.0 International (CC&nbsp;BY&nbsp;4.0)**](https://creativecommons.org/licenses/by/4.0/).
You may share and adapt freely with attribution.

The Panta Rhei project's formalization repository [TauLib](https://github.com/Panta-Rhei-Research/taulib) is licensed separately under the [**Apache License 2.0**](https://www.apache.org/licenses/LICENSE-2.0).

## Formalization & verification

- **[Lean 4](https://lean-lang.org/)** — the proof assistant hosting TauLib. Apache 2.0.
- **[Mathlib](https://leanprover-community.github.io/)** — the Lean community's mathematics library; TauLib uses its tactics and basic algebra infrastructure. Apache 2.0.

## Fonts

- **[Inter](https://rsms.me/inter/)** by Rasmus Andersson — UI / body typeface, self-hosted as a single variable `.woff2` under the SIL Open Font License 1.1 (zero external font requests).
- **Iowan Old Style → Palatino → Palatino Linotype → Book Antiqua → Georgia → serif** — the display / wordmark serif stack, resolved client-side against system fonts (no network request). See [Brand](/brand/) for typographic usage.

## Site infrastructure

- **[Jekyll](https://jekyllrb.com/)** — the static site generator that builds every page. MIT.
- **[Kramdown](https://kramdown.gettalong.org/)** — Jekyll's Markdown engine. MIT.
- **[Rouge](https://rouge.jneen.net/)** — syntax highlighting. MIT.
- **[jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap)** — sitemap.xml generation. MIT.

## Search & analytics

- **[Pagefind](https://pagefind.app/)** — privacy-preserving, client-side full-text search. No server, no tracking. MIT.
- **[Umami](https://umami.is/)** — cookieless, IP-anonymized web analytics (see [Datenschutz § 9](/datenschutz/) for the DSGVO-grade disclosure). MIT.
- **[Buttondown](https://buttondown.email/)** — minimal, privacy-respecting newsletter tooling.

## Diagrams & figures

- **[TikZ](https://tikz.dev/)** / **[pgf](https://ctan.org/pkg/pgf)** — source language for the framework diagrams, compiled to standalone SVG via the project's diagram pipeline. LPPL.

## Data sources

- **[CODATA 2018](https://physics.nist.gov/cuu/Constants/)** — recommended values of the fundamental physical constants.
- **[Particle Data Group](https://pdg.lbl.gov/)** — particle physics reference data (masses, mixing angles, lifetimes).

## Bibliography

The bibliography is built from hand-curated BibTeX entries with per-entry editorial overrides. Classical and modern sources are linked to their canonical publisher, DOI, or arXiv record wherever available. The full reference list (1,125 entries) is downloadable as [`references.bib`]({{ '/assets/bibliography/references.bib' | relative_url }}).

---

If you notice a missing attribution or a licensing error, please [get in touch]({{ '/engage/contact/' | relative_url }}) — we'll correct it promptly.
