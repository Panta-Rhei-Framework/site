# Content Quality & Narrative Flow (CQNF) — Evaluation Framework

## Purpose

A rigorous, quantitative framework for evaluating content quality, user journeys, and narrative flow across the Panta Rhei Research Program site. Designed for a research website where trust, orientation, and intellectual honesty matter more than conversion or engagement metrics.

---

## The Five Dimensions (each scored 1–5)

### Dimension 1: Prose Substance (PS)

*Does this page have enough meaningful prose to justify its existence?*

| Score | Criteria |
|:-----:|----------|
| 1 | Empty or metadata-only — no prose, just frontmatter/title |
| 2 | Stub — under 50 words of prose, placeholder-like feel |
| 3 | Minimal — 50–150 words, conveys basic information but feels thin |
| 4 | Adequate — 150–400 words, explains its topic sufficiently |
| 5 | Substantial — 400+ words of purposeful, well-structured prose |

**Page type baselines (minimum acceptable PS)**:
- Lane root: 4
- Framework about page / research note: 5
- Result page (major): 4
- Result page (indexed): 3
- Publication chapter: 3
- Bibliography entry: 3
- Changelog entry: 3

### Dimension 2: Reader Orientation (RO)

*Does this page tell the reader where they are, why they're here, and where to go next?*

| Score | Criteria |
|:-----:|----------|
| 1 | No orientation — reader has no idea what this page is about or how it relates to anything |
| 2 | Minimal — title and lane label present but no context or next steps |
| 3 | Basic — eyebrow + summary explain the page, but no explicit forward guidance |
| 4 | Good — clear context, summary, and at least one explicit next-step link or CTA |
| 5 | Excellent — rich orientation: eyebrow, summary, summary cards, explicit reading path, multiple CTAs, and relation to the larger argument stated |

### Dimension 3: Narrative Coherence (NC)

*Does this page contribute to a coherent larger argument, or does it feel isolated?*

| Score | Criteria |
|:-----:|----------|
| 1 | Orphaned — no connection to adjacent pages, no cross-references, feels disconnected |
| 2 | Weakly linked — has right-rail related pages but no in-text connections |
| 3 | Connected — references other pages or concepts in its prose, fits its lane |
| 4 | Woven — explicitly builds on previous pages and sets up subsequent ones |
| 5 | Architecturally integrated — cross-references framework modules, results, publications; shows how this page is one piece of a larger structure |

### Dimension 4: Trust Language (TL)

*Does this page's language earn trust through precision, honesty, and scope discipline?*

| Score | Criteria |
|:-----:|----------|
| 1 | Misleading — overclaims, hype language, or marketing tone |
| 2 | Vague — generic academic language without specifics |
| 3 | Factual — states claims clearly but doesn't address scope or limits |
| 4 | Disciplined — uses scope labels, acknowledges limits, distinguishes established from conjectural |
| 5 | Exemplary — every claim typed, scope explicit, falsification routes mentioned, reader can assess independently |

### Dimension 5: Craft Quality (CQ)

*Is the prose well-written at the sentence level?*

| Score | Criteria |
|:-----:|----------|
| 1 | Unreadable — garbled text, extraction artifacts, broken formatting |
| 2 | Rough — readable but choppy, repetitive, or generic |
| 3 | Clean — grammatically correct, clear, but unremarkable |
| 4 | Polished — well-paced, varied sentence structure, precise word choice |
| 5 | Distinctive — recognizable voice; every sentence does work; enjoyable to read |

---

## Scoring

### Page-Level Score
**CQNF = PS + RO + NC + TL + CQ** (out of 25)

### Quality Tiers

| Tier | Score | Meaning |
|------|:-----:|---------|
| **Frontier** | 22–25 | World-class research communication |
| **Strong** | 18–21 | Professional, trustworthy, well-crafted |
| **Adequate** | 14–17 | Functional, serves its purpose, room for improvement |
| **Thin** | 10–13 | Needs attention — reader may lose trust or orientation |
| **Critical** | 5–9 | Actively harmful to the site's credibility |

### Site-Level Targets for Public Release
- Mean CQNF >= 19 (Strong tier)
- 0 pages below 14 (no Thin or Critical)
- Floor score >= 14
- No dimension score of 1 or 2 on any lane root

---

## Sampling Strategy

### Tier 1: Mandatory (every page scored) — ~43 pages
- Homepage (1)
- All lane root pages (7)
- All research-program/about subpages (10)
- All framework/about subpages (16)
- All research notes (3)
- Founders, Cite, Impressum, Datenschutz (4)
- Media Kit, Review Kit (2)

### Tier 2: Stratified sample — ~97 pages
- 7 book pages + 7 archived book pages
- 14 part pages (2 per book) + 14 chapter pages (2 per book)
- 20 result pages (5 per status tier)
- 10 framework modules (stratified by layer)
- 10 bibliography entries (stratified by domain)
- 5 changelog entries + 5 impact portfolios + 5 registry dashboards

### Total: ~140 pages (2% of site, all types covered)

---

## User Journey Evaluation

### 5 Canonical Journeys

| ID | Persona | Entry | Path | Gate |
|----|---------|-------|------|------|
| J1 | First encounter | Homepage | About → Why → Framework | Natural transitions, no dead ends |
| J2 | Skeptic audit | Verify / Results | Result → Registry → TauLib | Every claim linkable to evidence |
| J3 | Book buyer | Publications | Book → Chapters → Amazon | Clear path, sufficient context |
| J4 | Scholar/citer | Cite / Bibliography | DOI → Zenodo → BibTeX | Citation complete and consistent |
| J5 | Follower | Engage | Follow → Subscribe → Notes | Frictionless, non-promotional |

### Journey Score (1–5)
| Score | Criteria |
|:-----:|----------|
| 1 | Breaks — dead end or missing page |
| 2 | Completes but feels accidental |
| 3 | Works — navigable with some guessing |
| 4 | Smooth — explicit forward guidance at each step |
| 5 | Designed — reader feels guided by an author who anticipated their questions |

---

## Audit Execution Phases

### Phase 1: Baseline
Score Tier 1 (43 pages). Compute mean, tiers, heat map.

### Phase 2: Deep Dive
Score Tier 2 (97 pages). Full site metrics + lane comparisons.

### Phase 3: Remediation
Fix pages below thresholds. Priority:
1. Critical/Thin (CQNF <= 13) — immediate
2. Lane roots below 19 — upgrade to Strong
3. Weakest dimension site-wide — targeted wave

### Phase 4: Re-score
Verify improvements. Compute delta.

---

## Reporting Template

```
Phase: [1/2/3/4]
Pages scored: N
Mean CQNF: X.X / 25
Tier distribution: Frontier X% | Strong X% | Adequate X% | Thin X% | Critical X%
Weakest dimension: [name] (mean X.X)
Strongest dimension: [name] (mean X.X)
Floor score: X (page: [url])
Remediation needed: N pages
Journey scores: J1=X J2=X J3=X J4=X J5=X

Delta (vs. previous):
  Mean CQNF: X.X → Y.Y (+Z.Z)
  Below-threshold: N → M (-K)
  Floor: X → Y (+Z)
```
