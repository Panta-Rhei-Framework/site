---
layout: program-doc
title: "Problem Ledger Source Policy"
lane: program
v2_lane: program
section: research-agenda
type: "Source Policy"
status: "Canonical"
summary_short: "How external stress-test problems are selected, pinned, imported, and classified."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Recovery Requirements"
      url: /program/research-agenda/recovery-requirements/
    - title: "Results Mirror"
      url: /results/problem-ledger-answers/
  meta:
    type: "Source Policy"
    scope: "Problem Ledger"
    status: "Canonical"
    updated: "April 2026"
---

## Why source policy matters

The Problem Ledger exists to keep the Research Agenda accountable to external stress tests. It is not a list of preferred victories. It is a source-pinned record of problems the program agrees should remain visible.

## Open problems vs recovery requirements

Open problems test whether the kernel illuminates what is not yet settled. Recovery requirements test whether the kernel recovers what is already established and must not be broken.

The two burdens are related, but they are not the same ledger.

## Physics import rule

Physics uses the full Wikipedia list of unsolved problems in physics as its master ledger. The pinned import captured revision `1349830343` from April 19, 2026 and v1.0 maps all 102 extracted named entries into public Problem Ledger items.

## Life import rule

Life uses two master ledgers: the Wikipedia list of unsolved problems in biology and the Wikipedia list of unsolved problems in neuroscience. The pinned imports captured biology revision `1350634388` from April 23, 2026 and neuroscience revision `1330874647` from January 3, 2026. v1.0 maps 112 source entries into 102 public items and 10 explicit overlap merges. The Wikipedia list of unsolved problems in medicine is not used as a master Life ledger in v2.

## Metaphysics / Philosophy import rule

Metaphysics / Philosophy uses Wikipedia's list of philosophical problems. The pinned import captured revision `1338262080` from February 14, 2026 and v1.0 maps all 27 extracted entries into public items. This source is not labeled as an unsolved-problems-in-philosophy source, and the Corpus manifest records the source-page warning about possible unverifiable material.

## Mathematics selection rule

Mathematics uses selected foundational stress tests: the seven Clay Millennium Problems and the Langlands Program. Problem Ledger v1.0 exposes all eight mathematics items. GRH and Grand GRH are not initial standalone Problem Ledger entries.

## Wholesale import vs supplemental selection

In Problem Ledger v1.0, declared source entries have been promoted, merged, excluded, or deferred through the Corpus import workflow. Future source updates will go through the same review process before promotion.

Master ledgers are imported wholesale from pinned revisions. Supplemental items may be added later only with explicit inclusion rationale.

## v1.0 public projection status

Problem Ledger v1.0 has promoted the declared source ledgers into the public site projection. Each declared source entry is now accounted for as one of:

- promoted public problem item;
- merged into another canonical problem item;
- excluded with rationale;
- deferred with reason.

Current v1.0 coverage is summarized on the [Problem Ledger root]({{ '/program/research-agenda/problem-ledger/' | relative_url }}).

## Revision pinning and source metadata

The Corpus import pipeline records revision IDs, retrieval timestamps, raw captures, normalized source-entry records, mapping records, and import reports. In v1.0 every declared source entry is promoted or explicitly merged; no mapped source entry remains hidden as an unclassified import.

## Classification after import

After import, each problem receives program classification fields: tier, agenda role, expressibility status, result status, recovery status, priority, notes, and related links.

## What this policy does not claim

Import is not endorsement, solution, or priority. It means the problem is visible to the agenda and can be classified honestly.
