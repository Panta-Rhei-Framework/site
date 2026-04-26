---
layout: program-doc
title: "For Engineering Contributors"
lane: engage
v2_lane: engage
type: "Contribute"
status: "Open"
permalink: /engage/for-engineering-contributors/
summary_short: "Lean 4, CI, docstring hygiene, registry bookkeeping — the project accepts small PRs liberally and opens the door to the Lean community."
summary_cards:
  - title: "Open to external PRs"
    body: "TauLib's CONTRIBUTING guide is published and the repository is now accepting outside contributions for the first time."
  - title: "Small PRs merged liberally"
    body: "Typos, docstring fixes, tactic simplifications, registry bookkeeping, broken links — no issue required, open a PR."
  - title: "CI enforces the invariants"
    body: "lake build green, axioms=3, sorry=0, tactics-only-Mathlib, docstring hygiene — checked automatically on every PR."
right_rail:
  related:
    - title: "Engage Overview"
      url: /engage/
    - title: "Public Discussions"
      url: /engage/discussions/
    - title: "Verify Lane"
      url: /verify/
    - title: "Collaborate"
      url: /engage/collaborate/
    - title: "Contact"
      url: /engage/contact/
    - title: "About the Framework"
      url: /framework/about/
  artifacts:
    - title: "TauLib repository"
      url: https://github.com/Panta-Rhei-Research/taulib
    - title: "CONTRIBUTING.md"
      url: https://github.com/Panta-Rhei-Research/taulib/blob/main/CONTRIBUTING.md
    - title: "TauLib issues"
      url: https://github.com/Panta-Rhei-Research/taulib/issues
    - title: "Apache-2.0 LICENSE"
      url: https://github.com/Panta-Rhei-Research/taulib/blob/main/LICENSE
  meta:
    type: "Contribute"
    scope: "Engineering"
    status: "Open"
    updated: "April 2026"
---

## For Engineering Contributors

Lean 4, CI, docstring hygiene, registry bookkeeping — the project accepts small PRs liberally and opens the door to the Lean community. This page is the engineering on-ramp: what to send, what not to send, how PRs are reviewed, and what the CI gate actually checks.

## Current Status

As of April 2026, **TauLib is a public artifact, solo-authored, opening for external contributions for the first time**. We are not claiming a vibrant community — just an open door. The [CONTRIBUTING guide](https://github.com/Panta-Rhei-Research/taulib/blob/main/CONTRIBUTING.md) was published alongside the first external-review wave, and the repository is now accepting outside pull requests under the conventions documented there.

If you are the first external contributor to land a PR: good. That is the point of opening the door.

## Three Contribution Paths

### Small PR — merged liberally

Typos, docstring corrections, `simp` / `omega` / `decide` tactic simplifications, registry bookkeeping (summaries out of sync with Lean definitions), broken links. **No issue required.** Open a PR directly, follow the conventions in [CONTRIBUTING.md](https://github.com/Panta-Rhei-Research/taulib/blob/main/CONTRIBUTING.md), and it will be reviewed and merged as soon as CI is green and the diff is obviously correct.

If you are unsure whether a change qualifies as "small," open [an issue](https://github.com/Panta-Rhei-Research/taulib/issues) and ask — the answer is usually yes.

### Medium PR — issue first

New lemmas supporting existing theorems, alternative proofs that do not introduce new axioms, refactors of a single module's internals. Open an [issue](https://github.com/Panta-Rhei-Research/taulib/issues) first describing the intent; we will triage, confirm scope, and then you open the PR against the agreed approach. This saves you from writing a large diff that gets rejected on scope grounds.

### Large change — discussion first

New axioms, scope-label changes (e.g. promoting a `conjectural` entry to `tau-effective`), `BookI/Kernel` refactors, anything that changes the public API of the core generators or the `TauLib.Main` surface. Start with a GitHub issue thread describing the proposal and the rationale. If GitHub Discussions is enabled on the repo, use that; otherwise the issue thread is the canonical discussion venue. Large changes are not rejected as a category — they are just discussed in public before the PR is written.

## What NOT to PR

- **`sorry` additions.** CI merge-blocks via `scripts/check_no_sorry.py`. The three existing methodological `sorry` entries in Book VII are flagged and scoped; no new ones are accepted.
- **Mathlib content imports.** TauLib is tactics-only with respect to Mathlib: we import tactics (e.g. `Mathlib.Tactic.Ring`) but not Mathlib content (no `Mathlib.Analysis.*` definitions pulled into proofs). CI enforces this with a grep-guard.
- **K0–K6 kernel axiom changes without discussion.** The seven axioms are load-bearing for the entire framework. Axiom-level changes are not merged without a public discussion thread.
- **Anything that would push axiom count above 3.** The current invariant is `axioms=3, sorry=0`. A PR that would change the axiom count is a framework-level change, not an engineering change, and belongs in a discussion thread.

## CI Invariants

Every PR runs against the following gates. A red CI is not a blocker to opening the PR — it is a signal for where to iterate.

- **`lake build` green.** The entire library must compile cleanly.
- **`scripts/check_no_sorry.py` returns `axioms=3, sorry=0`.** No new axioms, no new `sorry`.
- **Tactics-only-Mathlib grep-guard.** Imports are restricted to Mathlib tactics; content imports fail the check.
- **Docstring hygiene.** Module headers follow the format specified in [CONTRIBUTING.md](https://github.com/Panta-Rhei-Research/taulib/blob/main/CONTRIBUTING.md) — a one-line summary, a provenance line, and a scope-label line where applicable.

## Community Channels

- **[Organization Discussions]({{ '/engage/discussions/' | relative_url }})** - public questions, review offers, claim challenges, and routing that is broader than one repository.
- **[GitHub issues](https://github.com/Panta-Rhei-Research/taulib/issues)** — the primary async channel for bugs, proposals, and discussion. Triaged within 7 calendar days.
- **Lean Zulip** — [leanprover.zulipchat.com](https://leanprover.zulipchat.com/). There is not yet a project-specific thread; a launch thread will be announced in the `#new members` stream when it opens. Do not assume a URL exists before the announcement.
- **Direct email** — [review@panta-rhei.site](mailto:review@panta-rhei.site) for substantive engineering feedback that does not fit an issue thread (e.g. confidential review comments, pre-publication reports).

## Licensing

Two separate licenses apply depending on what you are contributing to:

- **TauLib (code, Lean sources, scripts):** [Apache-2.0](https://github.com/Panta-Rhei-Research/taulib/blob/main/LICENSE). See the `LICENSE` file in the repository root.
- **Site prose (research notes, this page, lane documentation):** CC BY 4.0.
- **No CLA.** We do not require a Contributor License Agreement.
- **DCO sign-off.** All commits to TauLib must carry a `Signed-off-by:` trailer (the Developer Certificate of Origin). `git commit -s` handles this automatically.

## Maintainer Responsiveness

These are commitments, not aspirations. If a window lapses, please ping the thread — silence is a failure mode, not a deliberate signal.

- **Issues triaged within 7 calendar days.** Triage means labeled, scoped, and responded to — not necessarily resolved.
- **Small PRs reviewed within 14 days.** If CI is green and the diff is obviously correct, usually much faster.
- **Larger PRs and substantive issues addressed publicly in-thread.** No back-channel resolutions: if a decision is made, it is written down in the thread so future contributors can read the reasoning.

## Good First Contributions

Concrete, not a vague invitation. Any of the following is welcome as a first PR:

1. **Spot a typo in a module docstring.** Open the PR; fix it; CI will do the rest.
2. **Propose a tactic simplification** where you see a collapsible chain like `simp; simp; ring` or a hand-unfolded proof that `decide` or `omega` could close.
3. **Flag a registry-entry summary that is out of sync with the Lean definition.** The `registry/*.tsv` files are human-edited and drift is real — reconciliation PRs are genuinely valuable.
4. **Propose a missing `#eval` check** that would make a theorem's numerical claim concrete (e.g. an `#eval` next to a `tau-effective` scope label that computes the predicted quantity).
5. **Fix a broken link or stale file path** in a module docstring, `README`, or site-adjacent artifact referenced from Lean source.

---

*TauLib is opening for external contributions for the first time. The door is open; the conventions are written down; the CI checks what it checks. The rest is in the PR.*
