---
layout: program-doc
title: "Three-Gate Rubric"
lane: verify
permalink: /verify/assessments/three-gate-rubric/
summary_short: "The 17-criteria scoring framework that structures every AI-assisted first-pass assessment dossier, organised into three gates: research-form legitimacy, novelty and relevance, and impact and salvage value."
right_rail:
  related:
    - title: "Assessment Overview"
      url: /verify/assessments/
    - title: "Series-Level Prompt"
      url: /verify/assessments/series-level-prompt/
    - title: "Dossier Output Schema"
      url: /verify/assessments/dossier-schema/
    - title: "Assessment Scorecard"
      url: /verify/assessments/scorecard/
    - title: "Reviewer Workflow"
      url: /verify/assessments/reviewer-workflow/
  meta:
    type: "Assessment Protocol"
    scope: "Scoring framework"
    status: "Published"
    updated: "April 2026"
---

## Scoring Philosophy

The rubric does not score truth. It scores the **public evidence of seriousness, novelty signal, and possible impact**.

Each of the 17 criteria is rated on a 0--4 scale:

| Score | Meaning |
|:-----:|---------|
| 0 | Absent --- no discernible evidence |
| 1 | Weak --- minimal or ambiguous evidence |
| 2 | Partial --- some evidence, but gaps remain |
| 3 | Strong --- clear, verifiable evidence |
| 4 | Unusually strong --- evidence exceeds what is typical for the genre |

The correct interpretive unit is the **profile**, not the sum. A work that scores 4 on novelty but 1 on reproducibility scaffolding tells a different story from one that scores 2 across the board, even if the arithmetic totals coincide. Do not average these into a single composite number or treat the total as a truth score.


## Gate 1 --- Research-Form Legitimacy

Gate 1 asks whether the work looks like a serious research artifact that has earned external scrutiny. It evaluates the structural and methodological surface of the project, not the correctness of its claims.

| ID | Criterion | What It Evaluates |
|:---|:----------|:------------------|
| G1-1 | Claim typing | Whether internal claims, bridge claims, empirical mappings, and worldview/commitment claims are clearly distinguished |
| G1-2 | Method visibility | Whether the methods are stated openly enough for an outsider to inspect them |
| G1-3 | Hinge visibility | Whether the load-bearing hinges or decisive claims are identifiable |
| G1-4 | Reproducibility scaffolding | Whether meaningful public routes into verification exist (formalisation, claim maps, tours, repository) |
| G1-5 | Falsification readiness | Whether the work names fair failure modes or break points |
| G1-6 | Scope discipline | Whether the work avoids silently inflating from an internal result to a stronger public claim |
| G1-7 | Review-worthiness | Whether the public evidence suggests the work has earned serious human scrutiny |


## Gate 2 --- Novelty and Relevance

Gate 2 asks whether the claims, if they survived scrutiny, would constitute a genuine contribution. It evaluates novelty signals without adjudicating priority or correctness.

| ID | Criterion | What It Evaluates |
|:---|:----------|:------------------|
| G2-8 | Novelty signal | Whether the claims appear potentially non-trivial and not obviously standard |
| G2-9 | Domain relevance | Whether, if true, the claims would matter to active research domains |
| G2-10 | Prior-art awareness | Whether the project appears aware of the need to distinguish novelty from rediscovery |
| G2-11 | Cross-domain relevance | Whether the work connects domains in a way that would matter if valid |
| G2-12 | Specificity of contribution | Whether the contributions are articulated specifically enough to judge novelty |


## Gate 3 --- Impact and Salvage Value

Gate 3 asks what remains significant under three scenarios: if the core claims substantially hold, if major bridges weaken, and if the core spine fails entirely. It evaluates resilience and reusability, not probability.

| ID | Criterion | What It Evaluates |
|:---|:----------|:------------------|
| G3-13 | Upside magnitude | How large the contribution could be if the core claims held |
| G3-14 | Partial-hold value | Whether significant value would remain if major bridges weakened |
| G3-15 | Salvage value | Whether methods, tools, formalisations, taxonomies, or conceptual structures would remain useful if the core spine failed |
| G3-16 | Reusability of artifacts | Whether reusable public artifacts exist independent of ultimate truth (repository, tours, formal maps, structured dossiers) |
| G3-17 | Strategic importance of inspection | Whether, even under uncertainty, the work is important enough to merit serious review because the upside is large |


## Interpretation Profiles

The 17 scores form a profile. The following archetypes help calibrate interpretation.

### Strong review-ready

- Gate 1 scores mostly 3--4
- Gate 2 includes at least some 3s
- Gate 3 includes at least one or two 4s
- Low inflation and strong scope discipline throughout

This profile indicates a work that appears methodologically serious, potentially novel, and consequential enough to warrant structured expert engagement.

### High-risk / high-upside

- Gate 1 strong
- Gate 2 mixed
- Gate 3 very high
- Clear need for expert checking of the strongest claims

This profile indicates a work whose potential significance is large but whose novelty claims require careful independent validation. The review priority is high precisely because the stakes are high.

### Interesting but premature

- Some novelty signal in Gate 2
- Weak reproducibility scaffolding or weak claim typing in Gate 1

This profile indicates a work that may contain genuine ideas but has not yet built the structural apparatus needed for disciplined external scrutiny. The recommended action is to improve the inspectability surface before seeking review.

### Weak

- Weak hinge visibility
- Weak method visibility
- Little basis for specialist attention

This profile indicates that the public materials do not currently provide enough evidence of seriousness to justify the investment of expert time.


## Confidence Labels

For each gate, the dossier should also assign a confidence label to the *assessment itself* --- not to the claims under review. The three levels are:

- **High** --- The public materials provide enough evidence to score this gate with reasonable assurance. Example: high confidence in Gate 1 because the repository, tours, and scope labels are publicly visible and inspectable.
- **Medium** --- The assessment is plausible but would benefit from domain-specific verification. Example: medium confidence in Gate 2 because prior-art comparisons require specialist knowledge the model may lack.
- **Low** --- The assessment is provisional and should not be relied upon without human expert evaluation. Example: low confidence in Gate 3 specifics because upside magnitude depends on judgments that exceed AI competence.

Confidence labels are a self-audit mechanism. They tell the reader where the dossier is most and least trustworthy, and where human expertise is most urgently needed.
