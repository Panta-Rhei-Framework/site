# panta-rhei.site — Jekyll source

This repository is the public source for **[panta-rhei.site](https://panta-rhei.site)**, the web presence of the **Panta Rhei Research Program**.

The program develops **Category τ**, a constrained formal kernel (5 generators, 7 axioms, 1 operator ρ) that aims to derive results across mathematics, physics, life, and metaphysics from one foundation. Master constant ι<sub>τ</sub> = 2/(π+e).

## What's in the program

| Surface | Repo | Purpose |
|---|---|---|
| **Public website** | [`Panta-Rhei-Research/site`](https://github.com/Panta-Rhei-Research/site) (this repo) | Jekyll source for `panta-rhei.site` — the program hub |
| **Publications** | [`Panta-Rhei-Research/publications`](https://github.com/Panta-Rhei-Research/publications) | Open-access publication artefacts and source files |
| **TauLib** | [`Panta-Rhei-Research/taulib`](https://github.com/Panta-Rhei-Research/taulib) | Lean 4 formalization (450 modules, 125,771 lines, 4,332 theorems, 3 axioms, 0 sorry) — documented at `taulib.site` |
| **Research** | [`Panta-Rhei-Research/research`](https://github.com/Panta-Rhei-Research/research) | Public workspace for open notebooks, scripts, and supplementary analyses |
| **Community** | [`Panta-Rhei-Research/community`](https://github.com/Panta-Rhei-Research/community) | Public discussion and onboarding surface |
| **Historical archive** | [`Panta-Rhei-Research/formalization`](https://github.com/Panta-Rhei-Research/formalization) | Archived historical formalization snapshot |

The program is published as a seven-book canonical monograph series (3,431 pages, 79 parts, 535 chapters — available now on Amazon KDP), with a free 190-page **Physics Ledger** companion carrying 67 numerical predictions + 30-item falsification pack.

## Building locally

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

Requires Ruby 3.3+ and Bundler. The full deploy runs on GitHub Pages via `.github/workflows/jekyll.yml`.

## Edge headers

GitHub Pages does not interpret repository `_headers` files. The `_headers`
file remains the portable declaration for Cloudflare Pages / Netlify-style
hosts, while the current GitHub Pages + Cloudflare proxy setup uses the
Cloudflare Worker in `workers/site-edge-headers.js`.

```bash
npm run headers:test
npm run headers:dry-run
# after the Worker is deployed at the Cloudflare edge:
npm run headers:live
```

Deploy the Worker with Wrangler from the repository root:

```bash
npm run headers:deploy
```

## Content license

All original site content — prose, diagrams, mathematics, registry objects, and results — is released under [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](https://creativecommons.org/licenses/by/4.0/). TauLib is separately licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

See [`/credits/`](https://panta-rhei.site/credits/) for the full attribution list.

## Corrections, reviews, collaboration

- **Editorial errata:** [errata@panta-rhei.site](mailto:errata@panta-rhei.site)
- **Media / reviews:** [press@panta-rhei.site](mailto:press@panta-rhei.site) — structured assets at [`/media/`](https://panta-rhei.site/media/)
- **Specialist review routes:** [`/verify/how-to-audit/`](https://panta-rhei.site/verify/how-to-audit/) (six inspection routes: formal methods / mathematician / physicist / philosopher / prior-art specialist / journalist-generalist)
- **Legal:** [`/impressum/`](https://panta-rhei.site/impressum/) · [`/datenschutz/`](https://panta-rhei.site/datenschutz/)

## How to cite

See [`/cite/`](https://panta-rhei.site/cite/) for canonical citations, DOIs, and ORCID IDs.
