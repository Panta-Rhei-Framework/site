---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Distribution release"
updated: "May 2026"
title: "TauLib: A Self-Contained Lean 4 Library for Category τ"
subtitle: "Kernel + Mathlib Bridges + Registry-Driven Correspondence"
permalink: "/publications/white-papers/taulib/"
type: "White Paper"
summary_short: "v2.0 technical whitepaper for the TauLib Lean 4 library: kernel/Mathlib-bridges architecture, 8 hinge-paper foundations, 4,892 theorems and 0 sorry across all seven Panta Rhei books, 39/39 claims-map audit at the pinned TauLib commit."
right_rail:
  related:
    -
      title: "TauLib documentation site"
      url: "https://taulib.site"
    -
      title: "TauLib source repository"
      url: "https://github.com/Panta-Rhei-Research/taulib"
    -
      title: "Verify / TauLib"
      url: "/verify/taulib/"
    -
      title: "Whitepaper LaTeX source"
      url: "https://github.com/Panta-Rhei-Research/papers/tree/whitepaper-taulib-v2.0/whitepapers/taulib"
    -
      title: "Other White Papers"
      url: "/publications/white-papers/"
  meta:
    type: "White Paper"
    scope: "Distribution release"
    status: "Distribution release"
    updated: "May 2026"
---

## Download

[Download the PDF (20 pages, ≈ 210 KB)]({{ '/assets/pdfs/white-papers/white-paper-2026-05-01-taulib-self-contained-lean-4-library.pdf' | relative_url }})

Permanent archival copy on Zenodo: [`10.5281/zenodo.19976503`](https://doi.org/10.5281/zenodo.19976503).

## Status

- Version: **v2.0 (full rewrite)** · May 2026
- Publication date: 2026-05-01
- DOI: [10.5281/zenodo.19976503](https://doi.org/10.5281/zenodo.19976503)
- Pinned TauLib commit: [`72aa2b6c`](https://github.com/Panta-Rhei-Research/taulib/tree/72aa2b6c7d6be28511f9649d3120773179b19038)
- Whitepaper git tag: [`whitepaper-taulib-v2.0`](https://github.com/Panta-Rhei-Research/papers/tree/whitepaper-taulib-v2.0)
- Claims-map auditor: **39 / 39 checks passed** at the pinned commit
- Red-team review verdict: 6 / 7 simulated Lean 4 expert reviewers qualified-yes; 1 / 7 qualified-no contingent on substantive findings (all addressed in published v2.0)
- Cryptographic integrity: SHA-256 `7bb96caa…1a7`, SHA-512 `8816b614…e00`; full hashes in the publications-repo manifest

## Summary

TauLib is a public Lean 4 library that formalises Category τ — the categorical framework of the Panta Rhei Research Program — from seven structural axioms K0–K6 on five generators (α, π, γ, η, ω) and one operator (ρ).

This v2.0 whitepaper documents three structural changes since v1.0 (post-peer-review v3, April 2026):

1. **The kernel–bridges architecture is first-class.** The τ-kernel (Books I–VII outside `Bridge/` subdirectories) imports zero Mathlib mathematical content. Mathlib bridges live in a separately-typed orthogonal layer. CI enforces the boundary on every push.

2. **Book I foundations are substantially extended** along the eight *hinge papers* (kernel-foundation, iota-tau, hyperfactorization, prime-polarity, address-resolution, boundary-algebra, holomorphy-first, tau-topos) and one framing memo (bundle-memo) — all currently circulating as internal preprints, awaiting external preprint-server submission. Book I is now 157 files, 1,580 theorems and 720 definitions.

3. **Across all seven books TauLib carries 4,892 theorems, 3,762 definitions, 94 typeclass instances, exactly 3 conjectural axioms (all in Book III, all paired with finite-decidable witnesses), and zero `sorry`**. Each count is asserted by CI on every push; drift is a build break.

## What v2.0 contains

- **Bridges architecture chapter** — τ-kernel as self-contained foundation, Mathlib bridges as orthogonal layer, CI enforcement (12 Mathlib-typeclass bridge files / 52 instances under `BookI/Boundary/Bridge/`).
- **Foundations chapter** — five generators + seven axioms K0–K6 + one operator ρ; full case studies for the master constant ι_τ = 2/(π+e), the Hyperfactorization Theorem, and the Prime Polarity Theorem; brief treatment of the remaining hinge papers.
- **"What TauLib does strictly differently" chapter** — eight differentiators from "usual" foundational kernels (generator-based construction, tactics-only Mathlib policy, constructive-by-default, "earned arrows", compute-then-axiomatize, single root universe, registry-driven correspondence, bounded axiom budget).
- **Case studies** — Wave 51 TauProfinite separation bridge (Book I), Central Theorem 3.15 (Book II), CMB ℓ_1 prediction with honest tension framing (Book V; ~1.3 σ above Planck), Book VII Commitments pattern.
- **Limitations + future work** — three Book III conjectural axioms, ι_τ structural-derivation theorem in flight, missing Mathlib-bridge instances, axioms-as-hypotheses encoding roadmapped for v2.1, two strongly-recommended red-team findings deferred to v2.1 with explicit acknowledgement.
- **Reproducibility** — the pinned TauLib commit, the canonical reproduction sequence, the claims-map auditor's 39 / 39 result, and the long-term archival path via Zenodo.
- **Appendices** — per-book module inventory, repository structure + build + CI gates, red-team-findings synopsis with the 6 / 7 yes verdict and convergence map.

## Companion artefacts

The v2.0 release ships three companion artefacts alongside the paper PDF, all in the [whitepaper source directory](https://github.com/Panta-Rhei-Research/papers/tree/whitepaper-taulib-v2.0/whitepapers/taulib):

- `RED_TEAM_FINDINGS.md` — consolidated review by 7 simulated Lean 4 expert reviewers (de Moura, Ullrich, Carneiro, Massot, Avigad, Buzzard, van Doorn) with severity-classified findings.
- `main_claims_audit.md` — auditor report from `verify_claims_map.py` showing 39 / 39 checks passed against the pinned TauLib commit.
- `scripts/verify_claims_map.py` — reproducible audit script (~280L, stdlib-only) for re-auditing the paper's numerical and theorem citations against any TauLib commit.

## Claim Boundary

The whitepaper presents the architecture, foundations, and case studies of the TauLib library at the v2.0 pinned TauLib commit. The structural derivation theorem for ι_τ remains in flight (Lean module currently ships fiat constants pending closure of the `ROADMAP-3-HINGES.md` Phase 0–4 sequence). The CMB ℓ_1 prediction is reported as a measurable tension (~1.3 σ above the central Planck value), not a clean confirmation. The three Book III conjectural axioms are paired with finite-decidable witness functions; their universal claims are open in mathematical practice, not Lean-proven.

## Citation Guidance

> Thorsten Fuchs and Anna-Sophie Fuchs, *TauLib: A Self-Contained Lean 4 Library for Category τ — Kernel + Mathlib Bridges + Registry-Driven Correspondence*, v2.0, May 2026. DOI: [10.5281/zenodo.19976503](https://doi.org/10.5281/zenodo.19976503).

BibTeX:

{% raw %}
```bibtex
@misc{Fuchs-TauLib-Whitepaper-v2-2026,
  author       = {Fuchs, Thorsten and Fuchs, Anna-Sophie},
  title        = {{TauLib}: A Self-Contained {Lean}~4 Library for {Category} $\tau$ ---
                  Kernel + Mathlib Bridges + Registry-Driven Correspondence},
  year         = {2026},
  month        = may,
  version      = {v2.0},
  doi          = {10.5281/zenodo.19976503},
  howpublished = {Panta Rhei Research; Zenodo deposit
                  \url{https://doi.org/10.5281/zenodo.19976503}}
}
```
{% endraw %}

## Integrity

The PDF carries cryptographic SHA-256 / SHA-512 hashes in the canonical [publications-repo manifest](https://github.com/Panta-Rhei-Research/publications/blob/main/white-papers/2026-05-01-taulib-self-contained-lean-4-library/manifest.json). An OpenTimestamps receipt is generated by the publications-repo CI on merge to `main`. The integrity layer attests to the PDF bytes only; it does not certify correctness, peer review, legal status, DOI registration, or content validity.
