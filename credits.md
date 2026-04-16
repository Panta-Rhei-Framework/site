---
layout: default
title: "Credits & Attributions"
permalink: /credits/
description: "Third-party assets, open-source libraries, and tooling that power panta-rhei.site."
---

# Credits & Attributions

The Panta Rhei research site is handcrafted with the help of excellent open-source and third-party work. We thank the authors and communities behind the following tools and assets.

## Content license

All original site content — prose, diagrams, mathematics, registry objects, and results — is released under
[**Creative Commons Attribution 4.0 International (CC&nbsp;BY&nbsp;4.0)**](https://creativecommons.org/licenses/by/4.0/).
You may share and adapt freely with attribution.

The Panta Rhei project's formalization repository [TauLib](https://github.com/Panta-Rhei-Research/taulib) is licensed separately under its own terms; see the repository for details.

## Formalization & verification

- **[Lean 4](https://lean-lang.org/)** — the proof assistant hosting TauLib.
- **[Mathlib](https://leanprover-community.github.io/)** — the Lean community's mathematics library; TauLib uses its tactics and basic algebra infrastructure.

## Fonts

- **[Inter](https://rsms.me/inter/)** by Rasmus Andersson — UI typeface, served via [Google Fonts](https://fonts.google.com/specimen/Inter) under the SIL Open Font License 1.1.
- **Georgia / Times New Roman** — system serif fallbacks for display math and decorative glyphs.

## Site infrastructure

- **[Jekyll](https://jekyllrb.com/)** — the static site generator that builds every page.
- **[Kramdown](https://kramdown.gettalong.org/)** — Jekyll's Markdown engine.
- **[Rouge](https://rouge.jneen.net/)** — syntax highlighting.
- **[jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap)** — sitemap.xml generation.

## Search & analytics

- **[Pagefind](https://pagefind.app/)** — privacy-preserving, client-side full-text search. No server, no tracking.
- **[Umami](https://umami.is/)** — self-hostable, cookie-free web analytics.
- **[Buttondown](https://buttondown.email/)** — minimal, privacy-respecting newsletter tooling.

## Diagrams & figures

- **[TikZ](https://tikz.dev/)** / **[pgf](https://ctan.org/pkg/pgf)** — source language for the framework diagrams, compiled to standalone SVG via the project's diagram pipeline.

## Data sources

- **[CODATA 2018](https://physics.nist.gov/cuu/Constants/)** — recommended values of the fundamental physical constants.
- **[Particle Data Group](https://pdg.lbl.gov/)** — particle physics reference data (masses, mixing angles, lifetimes).

## Bibliography

The bibliography is built from hand-curated BibTeX entries with per-entry editorial overrides. Classical and modern sources are linked to their canonical publisher, DOI, or arXiv record wherever available. The full reference list is downloadable as [`references.bib`]({{ '/assets/bibliography/references.bib' | relative_url }}).

---

If you notice a missing attribution or a licensing error, please [get in touch]({{ '/engage/media-and-contact/' | relative_url }}) — we'll correct it promptly.
