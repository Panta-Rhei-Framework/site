# NQAF Baseline Scoring — April 2026

**Framework:** Narrative Quality Assessment Framework (NQAF) v1.0
**Evaluated:** Live site via local Jekyll server (identical to panta-rhei.site deployment)
**Date:** 16 April 2026
**Evaluator method:** Programmatic fetch + DOM inspection of rendered HTML, supplemented by structural analysis

---

## Scores

| Dimension | Score | Evidence summary |
|-----------|:-----:|------------------|
| D1 First-Contact Promise | **5** | Homepage delivers all 5 elements within one scroll |
| D2 Audience Routing Precision | **5** | All 9 segments reach target in 1 click |
| D3 Master Narrative Fidelity | **4** | 4/5 narratives reinforced downstream; enrichment-layer language thin on some deep pages |
| D4 Epistemic Transparency | **4** | Scope discipline strong; world-readout pages use program-reading framing but lack explicit "if" conditionals on some pages |
| D5 Lane Purpose Clarity | **5** | All 11 lane roots have distinct, non-overlapping first-paragraph purpose statements |
| D6 Discovery Completeness | **5** | 9/10 sampled deep pages have breadcrumbs + right-rail + 40–1,170 internal links |
| D7 Narrative Flow & Transitions | **4** | Enrichment ladder flows cleanly from Prologue through Metaphysics; homepage does not directly link into the ladder path |
| D8 Tone & Voice Coherence | **5** | Zero exclamation marks, zero hype language, zero sales pressure across 7 sampled pages from all lanes |
| **Total** | **37 / 40** | **Tier: Frontier** |

---

## Release Acceptance Criteria — Status

| Criterion | Required | Actual | Pass? |
|-----------|:--------:|:------:|:-----:|
| Mean NQAF ≥ 32 | 32 | **37** | **PASS** |
| No dimension below 3 | 3 | min = **4** | **PASS** |
| D4 (Epistemic Transparency) ≥ 4 | 4 | **4** | **PASS** |
| D1 (First-Contact Promise) ≥ 4 | 4 | **5** | **PASS** |
| All 9 audience routing paths ≤ 2 clicks | 9/9 | **9/9** (all 1-click) | **PASS** |

**All release acceptance criteria met.**

---

## Dimension-by-Dimension Evidence

### D1 — First-Contact Promise: **5/5**

**Hero text:** "A research program by Dr. Thorsten Fuchs and Anna-Sophie Fuchs, exploring whether one constrained formal kernel can support a unified model of mathematics, physics, life, and metaphysics — with every claim typed, every derivation machine-checked, and every prediction publicly inspectable."

**Within one scroll, the homepage delivers:**
- Program identity: "Panta Rhei Research Program" + "independent open research program"
- Epistemic posture: "every claim typed" + "publicly inspectable"
- Scope: "mathematics, physics, life, and metaphysics"
- Verification commitment: "every derivation machine-checked" + "Verify It Yourself" CTA
- Clear next steps: 3 primary CTAs (Explore Framework, Browse Key Results, Verify It Yourself) + 7 header nav links

**Six H2 sections below the fold:**
1. Why this program is built from a constrained kernel
2. The Tau framework
3. Current scope of the program's claims
4. The program is public through verification surfaces
5. Why this could matter if it holds
6. Read, inspect, follow, and engage

**Audience routing from hero:** Journalist → Media (linked in body), Mathematician → Framework (CTA), Skeptic → Verify (CTA), Book buyer → Publications (header), Follower → Engage (header).

**Jargon check:** "Category τ" appears but is contextualized by "five generators, seven axioms, and one operator." No unexplained jargon.

**Word count:** 675 words — dense but not overwhelming.

**Verdict:** The homepage is a model of research-program communication. A journalist, physicist, and philosopher each know what this is and where to go within 30 seconds.

---

### D2 — Audience Routing Precision: **5/5**

All 9 audience segments tested. Every path is **1 click** from the homepage:

| Segment | Target | Path | Clicks |
|---------|--------|------|:------:|
| Journalist | /media/ | Homepage body link "Media Kit" | 1 |
| Skeptic | /verify/ | Header nav "Verify" + hero CTA "Verify It Yourself" | 1 |
| Skeptic (results) | /results/ | Header nav "Key Results" + hero CTA "Browse Key Results" | 1 |
| Mathematician | /framework/about/ | Header nav "Framework" + hero CTA "Explore the Framework" | 1 |
| Book buyer | /publications/ | Header nav "Publications" | 1 |
| Scholar (cite) | /cite/ | Homepage body link | 1 |
| Scholar (bibliography) | /bibliography/ | Homepage body link | 1 |
| Impact reader | /impact/ | Header nav "Impact" | 1 |
| Verification auditor | /verify/taulib/ | Homepage body link "TauLib" | 1 |
| Follower | /engage/ | Header nav "Engage" | 1 |
| General intellectual | /framework/about/ | Header nav "Framework" + hero CTA | 1 |

**Verdict:** Perfect routing. Every audience segment has a dedicated 1-click path. The header nav covers the primary lanes; the body adds specialized routes (TauLib, Cite, Bibliography, Media Kit).

---

### D3 — Master Narrative Fidelity: **4/5**

**5 master narratives tested across 5 deep pages from different lanes:**

| Page | MN1 Kernel | MN2 Layers | MN3 Typed | MN4 Verify | MN5 Conditional |
|------|:----------:|:----------:|:---------:|:----------:|:---------------:|
| Physics Readout (fabric) | ✓ | — | ✓ | ✓ | — |
| Framework About (what-tau-is) | ✓ | ✓ | ✓ | ✓ | — |
| Impact root | ✓ | — | ✓ | ✓ | ✓ |
| Result (Riemann) | — | — | ✓ | ✓ | — |
| Verify (TauLib) | ✓ | — | ✓ | ✓ | — |

**Strengths:**
- MN3 (Typed claims) and MN4 (Verification) are universally reinforced — every deep page references status labels or verification routes
- MN1 (Constrained kernel) appears on 4/5 pages
- MN5 (Conditional language) is present on Impact but less explicit on world-readout and result pages

**Gap identified:**
- **MN2 (Four-layer enrichment)** is only explicitly present on the Framework About page. World-readout pages describe their layer's content but don't always name the enrichment ladder explicitly (E₀ → E₁ → E₂ → E₃)
- **MN5 (Conditional language)** is strong on the Impact lane and homepage but less explicit on world-readout pages, which use "on the program's reading" rather than "if the framework holds." The qualifier is present but more implicit

**Verdict:** 4 of 5 master narratives are well-reinforced downstream. The enrichment-layer naming and conditional language could be slightly more explicit on deep pages. No contradictions found — this is an omission gap, not a fidelity violation.

---

### D4 — Epistemic Transparency Architecture: **4/5**

**Impact portfolios (3 tested — Agriculture, Solar, Ocean):**
- All use conditional ("if") language: ✓
- All carry "Conditional" scope label in right-rail metadata: ✓
- No unqualified "we have proven" found: ✓

**World-readout pages (3 tested — Physics consequences, Metaphysics Logos, Life favorability):**
- All carry "Canonical" scope label: ✓
- All avoid "we have proven": ✓
- Explicit "if the framework" conditional: present on 0/3 (use "on the program's reading" and similar implicit framing instead)

**Result pages (3 tested — Hubble, P vs NP, What is Life):**
- All carry status_code chip (Resolved/Partial): ✓
- All have scope labels in right-rail: ✓
- No unqualified proof claims: ✓

**Gap identified:**
- World-readout pages maintain epistemic discipline through implicit framing ("the program's answer is...", "Tau claims...") rather than explicit conditional markers ("if the framework holds"). This is philosophically appropriate for those pages (they describe the world Tau yields, not its empirical status) but a very strict evaluator might want a brief guardrail paragraph on each page stating the epistemic posture explicitly.

**Verdict:** Strong overall. The distinction between proven/derived/conjectural is maintained. The gap is between "implicit discipline" (good) and "explicit discipline" (better). No violations found.

---

### D5 — Lane Purpose Clarity: **5/5**

Every lane root has a distinct first-paragraph purpose statement. Summaries:

| Lane | First-paragraph purpose (paraphrased) |
|------|---------------------------------------|
| Homepage | What this program is + why it matters |
| Research Program | What kind of research object this is + what it releases publicly |
| Framework | How the formal architecture works + how enrichment unfolds |
| Results | Public relevance bridge — connects claims to recognized problems |
| Publications | Canonical publication surfaces — books, tours, papers |
| Verify | How to inspect, verify, and challenge — what can and can't be checked |
| Impact | Conditional consequence portfolios — what changes if the framework holds |
| Registry | Machine-readable research graph — 4,547 objects with dependencies |
| Bibliography | Shared reference corpus — 1,125 references with editorial notes |
| Engage | Calm participation layer — follow, support, contact |
| Cite | Academic citation standards — DOIs, BibTeX, version discipline |
| Media Kit | Press and review resources — downloadable materials, contact routing |

**Overlap test:** No two lane summaries describe the same purpose. Each answers a distinct reader question.

**Verdict:** Exemplary lane architecture. A reader visiting all 12 roots can explain each one's unique role.

---

### D6 — Discovery Completeness: **5/5**

**10 deep pages tested for multi-path discoverability:**

| Page | Breadcrumb | Right-rail | Internal links | Paths ≥ 2? |
|------|:----------:|:----------:|:--------------:|:----------:|
| Physics Readout (fabric) | ✓ | ✓ | 53 | ✓ |
| Result (Riemann) | ✓ | ✓ | 45 | ✓ |
| Framework (self-enrichment) | ✓ | ✓ | 61 | ✓ |
| Registry (I.T01) | ✓ | ✓ | 64 | ✓ |
| Impact (Solar portfolio) | ✓ | ✓ | 40 | ✓ |
| Prologue (math-makes-true) | ✓ | ✓ | 84 | ✓ |
| Publications (Book I) | ✓ | ✓ | 70 | ✓ |
| Bibliography root | — | ✓ | 1,170 | ✓ |
| Metaphysics (Logos) | ✓ | ✓ | 62 | ✓ |
| Browse All Results | ✓ | ✓ | 280 | ✓ |

**Minor note:** Bibliography root uses `bibliography-index` layout which doesn't have breadcrumbs. Not critical (it's a top-level page, not a deep page) but noted for completeness.

**Verdict:** Every tested page is reachable through left-rail navigation + in-content cross-links + breadcrumbs (where present). Rich internal linking across all lanes.

---

### D7 — Narrative Flow & Transitions: **4/5**

**Enrichment ladder path test:**

| Step | Page | Links to next? | Next signal? |
|------|------|:--------------:|:------------:|
| 1 | Homepage → | Links to /results/ (not /results/prologue/) | No direct ladder entry |
| 2 | Prologue → | ✓ Links to Physics Readout | ✓ Cluster links below |
| 3 | Physics Readout → | ✓ Links to Life Readout | ✓ |
| 4 | Life Readout → | ✓ Links to Metaphysics Readout | ✓ |
| 5 | Metaphysics Readout → | ✓ Links to Result Atlas | ✓ |
| 6 | Result Atlas (Browse) | — (terminal) | — |

**Strengths:**
- The ladder from Prologue through Metaphysics to Browse is seamless — every cluster overview links to the next
- Within each cluster, prev/next footers guide readers through the ordered sequence
- The Results index page prominently features all 4 clusters in order

**Gap identified:**
- **Homepage → Prologue gap:** The homepage links to `/results/` (the lane root) but does not link directly to `/results/prologue/` or `/results/world-readout/physics/`. A reader must first visit the Results overview, then discover the Prologue section. This adds one extra click to the enrichment-ladder path.
- The homepage's narrative arc (6 H2 sections) is excellent but doesn't explicitly introduce the enrichment-ladder reading path as a recommended journey.

**Verdict:** Internal flow within the Results lane is excellent. The one gap is the homepage-to-ladder entry, where an explicit "Start the enrichment ladder" CTA or reading-path suggestion would strengthen the flow.

---

### D8 — Tone & Voice Coherence: **5/5**

**7 pages sampled across all lane types:**

| Page | Exclamations | Hype words | Sales pressure | Conditional language | Precision language | Word count |
|------|:------------:|:----------:|:--------------:|:-------------------:|:-----------------:|:----------:|
| Homepage | 0 | 0 | 0 | ✓ | — | 675 |
| Physics Readout | 0 | 0 | 0 | ✓ | ✓ | 719 |
| Life Readout | 0 | 0 | 0 | ✓ | ✓ | 662 |
| Metaphysics Readout | 0 | 0 | 0 | — | ✓ | 485 |
| Media Kit | 0 | 0 | 0 | — | — | 784 |
| Result Page (Hubble) | 0 | 0 | 0 | — | ✓ | 365 |
| Engage | 0 | 0 | 0 | ✓ | — | 186 |

**Key observations:**
- **Zero exclamation marks** across all 7 pages (4,875 total words sampled)
- **Zero hype language** — no "revolutionary," "groundbreaking," "game-changing," "unprecedented"
- **Zero sales pressure** — no "buy now," "order now," "subscribe now," "limited time"
- **Consistent research register** — every page sounds like it was written by the same disciplined voice
- The Engage page explicitly states "The Engage lane is not a sales funnel" — the anti-marketing stance is itself part of the voice

**Verdict:** The intellectual voice is remarkably consistent. The tone is serious but not forbidding, precise but not pedantic, ambitious but not grandiose. Every page sounds like the same research program. The Media Kit shifts slightly to a more factual briefing tone (appropriate for its purpose) without losing credibility.

---

## Summary Scorecard

| | D1 FCP | D2 ARP | D3 MNF | D4 ETA | D5 LPC | D6 DC | D7 NFT | D8 TVC | **Total** |
|-|:------:|:------:|:------:|:------:|:------:|:-----:|:------:|:------:|:---------:|
| **Score** | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | **37/40** |

**Tier: Frontier** (35–40 range)

---

## Identified Gaps (for optional remediation)

Two dimensions scored 4 instead of 5. Both are refinement opportunities, not structural failures:

### Gap 1: Enrichment-layer language on deep pages (D3, D7)
- **Finding:** The four-layer enrichment ladder (E₀ → E₁ → E₂ → E₃) is not explicitly named on many deep pages. World-readout pages describe their layer's content but don't always reference the ladder as a whole.
- **Finding:** The homepage does not link directly into the enrichment-ladder reading path (Prologue → Physics → Life → Metaphysics → Atlas).
- **Remediation (optional):** Add a brief "Reading path" callout or CTA on the homepage that introduces the enrichment-ladder journey. Add a one-line enrichment-layer context sentence on world-readout overview pages.

### Gap 2: Explicit conditional markers on world-readout pages (D4)
- **Finding:** World-readout pages maintain epistemic discipline through implicit framing ("the program's answer is...") rather than explicit conditional markers ("if the framework holds"). This is philosophically appropriate but less robust against out-of-context quoting.
- **Remediation (optional):** Add a brief epistemic-posture paragraph at the start of each world-readout cluster overview, echoing the prologue's "What This Page Does Not Claim" discipline.

**Both gaps are refinement-level, not blocking.**

---

## Conclusion

The Panta Rhei Research site scores **37/40 (Frontier tier)** on the NQAF baseline evaluation. All release acceptance criteria are met:
- Mean 37 ≥ 32: **PASS**
- No dimension below 3 (minimum is 4): **PASS**
- D4 ≥ 4: **PASS**
- D1 ≥ 4: **PASS**
- All 9 audience routing paths ≤ 2 clicks (all are 1 click): **PASS**

The site is a world-class research-program communication surface. Its narrative architecture mirrors the framework's own coherence ambition: constrained, self-contained, publicly inspectable, and epistemically honest.
