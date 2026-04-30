---
layout: program-doc
title: "TauLib Audit Routes"
permalink: /verify/taulib/audit/
lane: verify
v2_lane: verify
type: "Verification Audit"
status: "Canonical"
summary_short: "Concrete audit routes for inspecting the TauLib formalization claims yourself: build the library, count axioms, count sorries, verify the claimed scope coverage, and check the trust budget."
hero_ctas:
  - label: "How to Audit"
    url: /verify/how-to-audit/
    primary: true
  - label: "Trust Budget (TCB)"
    url: /verify/tcb/
  - label: "Formalization Status"
    url: /verify/taulib/status/
right_rail:
  related:
    - title: "How to Audit"
      url: /verify/how-to-audit/
    - title: "How to Verify"
      url: /verify/how-to-verify/
    - title: "Trust Budget Disclosure"
      url: /verify/tcb/
    - title: "Custom Axiom Inventory"
      url: /verify/custom-axioms/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Scope Labels"
      url: /verify/taulib/scope-labels/
    - title: "Filter Rules"
      url: /verify/filter-rules/
    - title: "TauLib Browse"
      url: /verify/taulib/docs/
  meta:
    type: "Verification Audit Hub"
    scope: "TauLib formalization"
    status: Canonical
    updated: April 2026
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verification Matrix — the routes by which a reader can audit each TauLib claim independently of trust in any single page."
---

This page is a hub for the **concrete, hands-on routes** by which an external reader can audit the TauLib formalization's claims. Every claim on this site that depends on TauLib is reachable from one of the routes below.

## What you can audit, and how

| Claim category | Audit route | Tool |
|---|---|---|
| **3 custom axioms, exactly** | [`/verify/custom-axioms/`](/verify/custom-axioms/) — full inventory; or `rg -n '^axiom ' TauLib/` on the live repo | `rg` / [TauLib](https://github.com/Panta-Rhei-Research/taulib) |
| **0 sorry across all 7 books** | [`/verify/taulib/status/`](/verify/taulib/status/); or `rg -n ':= sorry' TauLib/` on the live repo | `rg` / [TauLib](https://github.com/Panta-Rhei-Research/taulib) |
| **Module / theorem / `#eval` counts** | [`/verify/release-manifest/`](/verify/release-manifest/) — pinned counts at the release SHA | manifest checksum |
| **`native_decide` trust-budget cost** | [`/verify/tcb/`](/verify/tcb/) — explicit disclosure of `Lean.ofReduceBool` and `Lean.trustCompiler` extension; ~1,824 use sites | `#print axioms` at REPL |
| **Each scope label is honest** | [`/verify/taulib/scope-labels/`](/verify/taulib/scope-labels/) and [`/verify/filter-rules/`](/verify/filter-rules/) | review |
| **Each registry-ID claim has a Lean witness** | [`/verify/taulib/docs/`](/verify/taulib/docs/) — Corpus-native browser; per-result page links to the Lean module | site cross-reference |
| **Build the library yourself** | [`/verify/how-to-audit/`](/verify/how-to-audit/) — `lake build` from a fresh clone | `lake` |

## Two-minute audit

For a journalist, reviewer, or specialist who has 120 seconds:

```bash
git clone https://github.com/Panta-Rhei-Research/taulib && cd taulib
rg -n '^axiom ' TauLib/                    # expect 3 matches
rg -n ':= sorry' TauLib/                   # expect 0 matches
rg -c 'native_decide' TauLib/ | head        # disclosure: ~1,824 — see /verify/tcb/
```

If those three checks return what the site claims, the headline TauLib invariants are independently verified. The harder claims (each prediction's chain through the registry) require the page-level audit routes above.

## Where the trust ends and the engineering begins

This audit hub is intentionally short. It is **not** the verification narrative — that lives at [`/verify/`](/verify/) and [`/verify/how-to-verify/`](/verify/how-to-verify/). It is the concrete *route* surface: where to click, what to run, what to grep, when you have decided to inspect rather than read.

For the trust-budget question — *what does "machine-checked in Lean 4" actually mean here?* — start at [`/verify/tcb/`](/verify/tcb/). For the scope-label question — *which claims are formal-only, which are bridged to physics, which are metaphorical?* — start at [`/verify/taulib/scope-labels/`](/verify/taulib/scope-labels/) and [`/verify/filter-rules/`](/verify/filter-rules/).
