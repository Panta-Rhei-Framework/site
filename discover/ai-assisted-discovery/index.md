---
layout: program-doc
title: "AI-Assisted Discovery"
permalink: /discover/ai-assisted-discovery/
lane: discover
v2_lane: discover
section: guided-entry
type: "Discover Page"
status: "Canonical"
summary_short: "Copy-ready prompts for web-enabled LLMs to generate outside-in orientation reports, first-contact assessments, journalist briefs, and critical dossiers on the Panta Rhei Research Program."
tags:
  - discover
  - ai-assisted-discovery
  - llm-prompts
  - assessment-prompts
  - first-contact
  - journalist
  - reviewer
  - outside-in-assessment
  - web-enabled-llm
  - critical-review
  - media
  - verify
hero_ctas:
  - label: "Start with prompt 1"
    url: "#prompt-1"
    primary: true
  - label: "Open Verify"
    url: /verify/how-to-verify/
  - label: "Media Kit"
    url: /media/
right_rail:
  related:
    - title: "Discover"
      url: /discover/
    - title: "Start Here"
      url: /discover/start-here/
    - title: "Entry Routes"
      url: /discover/entry-routes/
    - title: "What to Read First"
      url: /discover/what-to-read-first/
    - title: "Media Kit"
      url: /media/
    - title: "How to Verify"
      url: /verify/how-to-verify/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
    - title: "Review the Work"
      url: /engage/review-the-work/
  meta:
    type: "Discover Page"
    status: "Canonical"
    updated: "May 2026"
---

# AI-Assisted Discovery

This page provides copy-ready prompts for visitors who want to use a web-enabled frontier LLM to generate a first-pass outside-in assessment of the Panta Rhei Research Program.

These prompts are discovery aids.

They are not peer review, formal verification, empirical validation, or endorsement.

Use them to orient yourself, generate questions, find the right pages, and decide which inspection route to follow next.

> **AI-assisted discovery is orientation, not verification.**

## How to use these prompts

1. Copy a prompt.
2. Paste it into a frontier LLM with web browsing enabled.
3. Ask the model to use only public pages from `panta-rhei.site`, public GitHub repositories, and public artifacts.
4. Require citations or source links.
5. Treat the output as a first-pass orientation report, not as verification.

For formal, empirical, or technical inspection, continue to [Verify]({{ '/verify/' | relative_url }}) and [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}).

## What AI-assisted discovery can and cannot do

**AI-assisted discovery can help:**

- summarize the site;
- identify the main claims and routes;
- produce a first-contact seriousness assessment;
- compare lanes;
- generate questions;
- find inspection surfaces;
- prepare a journalist or reviewer briefing.

**AI-assisted discovery cannot:**

- verify the theory;
- replace peer review;
- certify formal proof;
- validate empirical predictions;
- establish priority or novelty;
- determine scientific acceptance.

> **LLM outputs can be wrong.** Use them to find pages, generate questions, and route inspection. Continue to Verify for actual verification paths.

---

## Prompt catalog

Ten copy-ready prompts. Use the one that matches your intent. Then route the LLM's output back into the relevant lane — Program, Agenda, Corpus, Results, Verify, or Engage.

---

### <a id="prompt-1"></a>Prompt 1 — 90-second first-contact assessment

**Purpose.** Quickly decide whether the site appears serious enough to inspect.

**Best for.** Journalists, editors, first-time visitors, link-from-a-trusted-source readers.

{% include copy-prompt-button.html id="first-contact" %}

```text
You are an expert science journalist receiving a link from a trusted source. Perform a 90-second first-contact assessment of https://panta-rhei.site.

Use only public web pages and cite the pages you rely on.

Your task is not to decide whether the framework is true. Your task is to answer:

1. What is this site?
2. What does the program claim to be building?
3. Does the site appear to expose enough structure to be worth a deeper look?
4. What are the most important first-contact credibility signals?
5. What are the most important first-contact risk signals?
6. Which three pages should I inspect next?

Output format:
- Executive verdict in 5 sentences.
- Credibility signals.
- Risk signals.
- Recommended next clicks.
- One-sentence newsroom pitch.
```

**Next route.** [Media Kit]({{ '/media/' | relative_url }}) → [Open Research Brief]({{ '/media/open-research-brief/' | relative_url }}) → [Program]({{ '/program/' | relative_url }}) → [Verify]({{ '/verify/' | relative_url }}).

---

### Prompt 2 — Research-form legitimacy dossier

**Purpose.** Assess whether the public artifact is serious, inspectable, and review-worthy.

**Best for.** Reviewers, foundation officers, prospective collaborators, evaluators of high-scope open research.

{% include copy-prompt-button.html id="legitimacy-dossier" %}

```text
You are conducting an AI-assisted first-pass assessment of a public research architecture.

Use only public materials from https://panta-rhei.site and public repositories linked from that site.

Do not decide whether the framework is true.

Produce a typed dossier answering:

1. Research-form legitimacy:
   Does this work appear to be a serious, inspectable, review-worthy research artifact?

2. Novelty and relevance:
   If yes, do its claims appear potentially novel and materially relevant relative to mainstream frontier work in the domains it addresses?

3. Impact and salvage value:
   If the core claims held, what would the likely magnitude of contribution be?
   If the core claims partly failed, what might still remain scientifically, formally, educationally, or methodologically valuable?

Requirements:
- Cite every public page used.
- Distinguish internal program claims from external verification.
- Identify at least five inspection surfaces.
- Identify at least five overclaiming or risk areas.
- Provide a final recommendation: ignore, monitor, inspect narrowly, or prioritize expert review.
```

**Next route.** [Verify]({{ '/verify/' | relative_url }}) → [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) → [Corpus Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}).

---

### Prompt 3 — Site map and route recommendation

**Purpose.** Help a visitor navigate the observatory.

**Best for.** Information architects, librarians, anyone who wants a structured map before reading.

{% include copy-prompt-button.html id="route-recommendation" %}

```text
You are an information architect and research librarian.

Crawl the public site https://panta-rhei.site and create a visitor-facing map of the research observatory.

Use only public pages and cite all pages used.

Tasks:
1. Identify the main lanes and what each lane is for.
2. Identify the best starting route for:
   - journalist;
   - physicist;
   - mathematician;
   - philosopher;
   - formal methods expert;
   - general educated reader;
   - potential contributor.
3. Explain how Program, Agenda, Corpus, Results, Verify, Impact, Engage, and Publications differ.
4. Identify any confusing or redundant labels.
5. Recommend the shortest path for a critical first-time visitor.

Output as:
- Lane map table.
- Audience route table.
- Three recommended first paths.
- Five open navigation questions.
```

**Next route.** [Discover]({{ '/discover/' | relative_url }}) → [What to Read First]({{ '/discover/what-to-read-first/' | relative_url }}) → [Sitemap]({{ '/sitemap/' | relative_url }}).

---

### Prompt 4 — Journalist story-angle assessment

**Purpose.** Generate safe story angles without endorsing scientific claims.

**Best for.** Science journalists, editors, communicators preparing first coverage.

{% include copy-prompt-button.html id="journalist-angles" %}

```text
You are a senior science editor evaluating whether a journalist can responsibly cover https://panta-rhei.site.

Do not evaluate whether the theory is true.

Evaluate what stories can responsibly be written before expert review.

Use public pages only and cite sources.

Tasks:
1. Identify the safest first story.
2. Identify two follow-up stories.
3. State what journalists can responsibly say.
4. State what journalists should not say without expert review.
5. Identify which pages should be linked in the article.
6. Produce five possible headlines.
7. Produce one cautious 150-word article pitch for an editor.

Pay special attention to the Media Kit, Open Research Brief, Theory of Reality Brief, Public Research Observatory Brief, Program, Agenda, and Verify pages.
```

**Next route.** [Media Kit]({{ '/media/' | relative_url }}) → three package briefs.

---

### Prompt 5 — Coherent theory of reality explainer

**Purpose.** Explain the conceptual category.

**Best for.** Philosophers, conceptual writers, anyone who wants the category before the content.

{% include copy-prompt-button.html id="ctor-explainer" %}

```text
You are a philosopher of science writing a neutral explainer.

Using only public pages from https://panta-rhei.site, explain what Panta Rhei means by "a coherent theory of reality."

Do not decide whether the theory succeeds.

Address:
1. Why Panta Rhei avoids "theory of everything" as the main label.
2. What it means by theory.
3. What it means by reality.
4. What it means by coherent.
5. What "Core Semantics" means.
6. What "earned language, earned question, earned answer" means.
7. Why life, mind, language, proof, value, and commitment are in scope.
8. What the Construction Roadmap contributes.
9. What remains unresolved or risky.

Output:
- 800-word explainer.
- Glossary of 10 terms.
- Three objections a critic might raise.
- Recommended next pages.
```

**Next route.** [Program]({{ '/program/' | relative_url }}) → [Coherent Theory of Reality]({{ '/program/about/coherent-theory-of-reality/' | relative_url }}) → [Agenda]({{ '/agenda/' | relative_url }}).

---

### Prompt 6 — Corpus construction inspection

**Purpose.** Inspect the construction body without reading all monographs.

**Best for.** Formal methods reviewers, foundations researchers, anyone who wants the build before the consequences.

{% include copy-prompt-button.html id="corpus-inspection" %}

```text
You are an expert reviewer evaluating the Corpus lane of https://panta-rhei.site.

Do not assess the truth of the full theory.

Assess whether the Corpus is structured as an inspectable construction body.

Use public pages only and cite sources.

Tasks:
1. Explain the difference between Construction Spine, Monograph Corpus, Registry, TauLib, Graph, Results, Verify, and Publications.
2. Summarize the ten construction steps.
3. Identify whether the Corpus distinguishes construction from consequence.
4. Identify at least three strong inspection handles.
5. Identify at least three risks or missing mappings.
6. Recommend one narrow step for expert review.

Output:
- Executive summary.
- Construction map table.
- Inspection handles.
- Risks and missing links.
- Suggested next review action.
```

**Next route.** [Corpus]({{ '/corpus/' | relative_url }}) → [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}) → [Monograph Corpus]({{ '/corpus/monograph-corpus/' | relative_url }}) → [Verify]({{ '/verify/' | relative_url }}).

---

### Prompt 7 — Results and status audit

**Purpose.** Prevent a visitor from confusing internal results with external acceptance.

**Best for.** Domain experts, reviewers checking whether claim status is honestly disclosed.

{% include copy-prompt-button.html id="results-audit" %}

```text
You are auditing the Results lane of https://panta-rhei.site.

Your goal is to understand what the program claims follows from its Corpus, without treating internal program status as external acceptance.

Use public pages only and cite sources.

Tasks:
1. Explain the role of Results in the v4 observatory.
2. Summarize Landmark Results, World Readouts, Problem Ledger Answers, Recovery/Core Semantics status, Additional Derived Results, and Progress Against Agenda.
3. Identify the status language used.
4. Identify where the site warns against overclaiming.
5. List the top five result surfaces worth inspecting.
6. List the main verification routes for those result surfaces.

Output:
- Results lane summary.
- Status taxonomy observed.
- Five high-signal results.
- Verification routes.
- Risk notes.
```

**Next route.** [Results]({{ '/results/' | relative_url }}) → [Progress Against Agenda]({{ '/results/progress-against-agenda/' | relative_url }}) → [Verify]({{ '/verify/' | relative_url }}).

---

### Prompt 8 — Verify route planner

**Purpose.** Route a critic to the right verification surface.

**Best for.** Skeptical reviewers, technical evaluators, scrutiny-first readers.

{% include copy-prompt-button.html id="verify-planner" %}

```text
You are a technical reviewer planning how to inspect https://panta-rhei.site.

Use public pages only and cite sources.

Create a verification route planner for the following kinds of review:

1. Formal proof / Lean / TauLib review.
2. Corpus construction review.
3. Physical prediction / falsification review.
4. Agenda / source-policy review.
5. Result status review.
6. Media / public-communication review.
7. Contribution or correction route.

For each route, provide:
- starting page;
- next pages;
- what to inspect;
- what not to infer;
- expected output of the review.

End with a 10-step checklist for a skeptical reviewer.
```

**Next route.** [Verify]({{ '/verify/' | relative_url }}) → [How to Verify]({{ '/verify/how-to-verify/' | relative_url }}) → [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) → [Engage]({{ '/engage/' | relative_url }}).

---

### Prompt 9 — Related approaches comparison

**Purpose.** Help readers compare Panta Rhei with known programs.

**Best for.** Foundations researchers, comparative-philosophy readers, anyone placing the program in the wider landscape.

{% include copy-prompt-button.html id="related-approaches" %}

```text
You are a foundations-of-science researcher comparing Panta Rhei with related approaches.

Using only public pages from https://panta-rhei.site and public sources for related approaches, produce a cautious comparison report.

Compare Panta Rhei with:
- Wolfram Ruliad / Physics Project;
- Penrose twistor theory;
- Wheeler-Feynman absorber theory;
- It from Bit / Mathematical Universe Hypothesis;
- HoTT / Univalent Foundations;
- Free Energy Principle / IIT;
- Ontic Structural Realism.

For each:
1. What the related approach tries to solve.
2. What Panta Rhei shares.
3. Where Panta Rhei places the semantic or construction burden differently.
4. Which Panta Rhei page to inspect next.

Do not write a takedown. Do not claim Panta Rhei supersedes these approaches. Focus on positioning and burden placement.
```

**Next route.** [Program]({{ '/program/' | relative_url }}) → [Related Approaches]({{ '/program/about/related-approaches/' | relative_url }}).

---

### Prompt 10 — Custom question template

**Purpose.** Insert your own questions and route the answer.

**Best for.** Anyone with specific questions who wants the answer routed back into the right lane.

{% include copy-prompt-button.html id="custom-questions" %}

```text
You are helping me inspect https://panta-rhei.site.

Use only public pages from the site and public repositories linked from it. Cite every page you rely on.

My questions are:

1. [INSERT QUESTION 1]
2. [INSERT QUESTION 2]
3. [INSERT QUESTION 3]

For each question:
- answer from the public site;
- identify which lane owns the relevant content;
- distinguish internal program stance from external verification;
- identify the best next pages to inspect;
- state what remains unresolved.

Then summarize whether my questions are best pursued through Program, Agenda, Corpus, Results, Verify, Impact, or Engage.
```

---

## Locked language

> AI-assisted discovery is orientation, not verification.

> Use these prompts to find pages, generate questions, and choose inspection routes.

> LLM outputs can be wrong; continue to Verify for actual verification paths.

> Core Semantics is the language the theory must earn before it can answer.

> Agenda states obligations. Corpus builds. Results reports consequences. Verify inspects.

> Engagement and review do not require endorsement.

## What to do with the output

After running a prompt, the report is your starting point — not your conclusion.

- For **journalist briefings**, route through [Media Kit]({{ '/media/' | relative_url }}).
- For **technical inspection**, continue to [Verify]({{ '/verify/' | relative_url }}) and [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}).
- For **review and correction**, use [Engage: Review the Work]({{ '/engage/review-the-work/' | relative_url }}).
- For **claims about results or predictions**, use [Results]({{ '/results/' | relative_url }}) and the falsification ledger.
- For **conceptual orientation**, use [Program]({{ '/program/about/coherent-theory-of-reality/' | relative_url }}) and [Agenda]({{ '/agenda/' | relative_url }}).

These prompts are discovery aids. They are not peer review, formal verification, empirical validation, novelty proof, priority proof, or endorsement.
