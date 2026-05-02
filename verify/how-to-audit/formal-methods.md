---
layout: program-doc
title: "How to Audit — Formal Methods / Proof Assistant Route"
permalink: /verify/how-to-audit/formal-methods/
lane: verify
v2_lane: verify
type: "Inspection Route"
status: "Canonical"
summary_short: "The fastest disconfirmation path for a Lean 4, Mathlib, Coq, Agda, or Isabelle specialist. What to clone, what to build, what to grep for, and which claims must survive your audit for the framework to remain review-worthy."
plain_language_summary: "If you write proof-assistant code for a living, the framework's claim is checkable in an afternoon: clone TauLib, build it, grep for `axiom`, grep for `sorry`, grep for `native_decide`, and verify that the three custom axioms aren't doing more work than the program admits. The page below names the exact commands, the load-bearing modules, and the specific properties (zero sorries, three axioms only, kernel-checked theorems for the Central Theorem) that must survive your audit."
right_rail:
  related:
    - title: "How to Audit (Hub)"
      url: /verify/how-to-audit/
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "TauLib Overview"
      url: /verify/taulib/
    - title: "Formalization Status"
      url: /verify/taulib/status/
  meta:
    type: "Inspection Route"
    scope: "Formal methods audit"
    status: "Canonical"
    updated: "April 2026"
---

This route is written for a reviewer comfortable with proof assistants — Lean 4 and Mathlib preferred, but Coq/Agda/Isabelle users will recognize the pattern. The load-bearing question you should resolve first is: **does TauLib's claimed formalization state actually hold when you build it?**

Every other claim in the program depends on this. If TauLib compiles cleanly with the claimed `sorry` and `axiom` inventory, the framework has earned its internal-mathematical review-readiness. If it does not, most of the bridge claims fail regardless of their external-physics content.

## The 15-minute core check

```bash
# 1. Clone at the pinned commit
git clone https://github.com/Panta-Rhei-Research/taulib
cd taulib
git checkout 2261c049119c8dd9a4e891457f196745178c02b3

# 2. Confirm toolchain pinning
cat lean-toolchain              # Expect: leanprover/lean4:v4.28.0-rc1
cat lake-manifest.json | head   # Expect: mathlib at commit 85028a6

# 3. Build
lake build                      # Expect: 0 errors, ~8–12 min on 8-core laptop

# 4. Audit sorry inventory
rg "^\s*sorry\s*$" TauLib --stats
# Expect: 0 matches across all 7 books

# 5. Audit custom axiom inventory
rg "^axiom " TauLib --stats
# Expect: 3 matches, all in TauLib/BookIII/

# 6. Per-module per-theorem axiom trace (spot check 3 headline theorems)
# In Lean 4 REPL or via a small script:
#   #print axioms Book2.CentralTheorem.centralTheorem        -- expect: only Mathlib axioms
#   #print axioms Book4.Generations.threeGenerationsTheorem  -- expect: only Mathlib axioms
#   #print axioms Book3.Spectrum.criticalLineTheorem         -- expect: 3 named axioms + Mathlib
```

If any of these six checks fail, the framework's formal-methods posture is not what it claims. The [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) is the authoritative snapshot you are verifying against.

## What to grep for next (30 minutes)

Once the core build succeeds, these are the highest-signal follow-up audits:

1. **Unused Mathlib imports.** The framework claims "tactics only — no Mathlib mathematical content." Audit imports:
   ```bash
   rg "^import Mathlib" TauLib --stats
   ```
   Check that only tactic-level Mathlib modules are imported (e.g., `Mathlib.Tactic.Linarith`, `Mathlib.Tactic.Ring`). Any `Mathlib.Analysis.*`, `Mathlib.Topology.*`, `Mathlib.NumberTheory.*` import would contradict the "no Mathlib content" claim.

2. **`@[instance]` and `@[simp]` attributes on core definitions.** Look for instance declarations that might be smuggling non-trivial content through typeclass resolution.
   ```bash
   rg "^@\[(instance|simp)\]" TauLib --stats
   ```

3. **`noncomputable` markers.** Count how many definitions are `noncomputable`. A kernel that claims constructivity should have few; a kernel that uses classical choice extensively will have many.

4. **Check-axioms discipline.** In Lean 4, `#print axioms X` reveals the full axiomatic dependency of any theorem. Spot-check **at least three** headline theorems from the registry's "formalized" entries and verify the axiom chain matches what the Release Manifest claims.

5. **Proof structure for core theorems.** Open `Book1/KernelCoherence.lean`, `Book2/CentralTheorem.lean`, and `Book4/Generations.lean` in an editor. Read the proofs. Do they appear to be genuine proofs with non-trivial content, or do they degenerate into `decide`, `trivial`, or `native_decide` tactics that would indicate missing proof content?

## The three headline theorems to read in source

If you have 60 minutes and want to understand the framework's formal-mathematical core, read these three Lean sources directly:

- **`Book1/Kernel.lean`** — the seven axioms K0–K6 and the categoricity + rigidity theorems. Load-bearing: if these theorems are trivial or circular in Lean, the entire framework is built on sand.
- **`Book2/CentralTheorem.lean`** — the ring isomorphism 𝒪(τ³) ≅ A_spec(𝕃). Load-bearing: this theorem is the bridge between the mathematical kernel (Book I) and the physics readout (Books IV–V). If it fails, the holography claim fails with it.
- **`Book3/CriticalLine.lean`** — the Critical Line Theorem III.T19, the τ-framework's spectral approach to RH. Load-bearing: this is the most load-bearing claim that sits in dense prior-art territory (Hilbert-Pólya, Connes). Specialist scrutiny of the proof structure is exactly the kind of check this route recommends.

## Fail-fast exits

Your audit is **done** (with a negative verdict) if any of the following is true:

- **Build fails.** `lake build` returns a non-zero exit code. The claimed 0-sorry state is inconsistent with the actual source.
- **Undeclared axioms appear in `#print axioms` output** on any theorem that registry marks "formalized". This contradicts the Release Manifest's axiom inventory claim.
- **Mathlib mathematical content is imported** (not just tactic modules). This contradicts the "no Mathlib content" architectural claim and means the "earned from seven axioms" story is not operationally clean.
- **Core kernel theorems have trivial or circular Lean proofs** (e.g., proving categoricity by declaring it as an axiom under a different name). The architectural claim of coherence-first derivation falls.

Any one of these is disqualifying.

Your audit is **positive** (the framework has passed the formal-methods gate) if:

- `lake build` is green at the pinned commit.
- `rg "sorry"` returns 0 matches across all 7 books (post `peer-review-fixes-v1`; the prior three Book VII methodological `sorry` declarations are now `def : Commitment` values).
- `rg "^axiom"` returns exactly 3 custom declarations, all in Book III and each documented in the TauLib browser.
- `#print axioms` on three randomly-chosen "formalized" registry entries returns only declared framework axioms plus standard Mathlib base axioms (`Classical.choice`, `propext`, `Quot.sound`) plus, where `native_decide` is used, the TCB extension (`Lean.ofReduceBool`, `Lean.trustCompiler`) disclosed on [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}).
- The three headline theorems read as genuine mathematical content rather than definitional rearrangements.

A positive formal-methods audit does **not** establish the framework is correct about physics, life, or metaphysics. It establishes that the internal mathematical scaffolding is what the program claims it is. This is a necessary condition for the program to deserve further domain-level review; it is not a sufficient condition for accepting any bridge claim.

## What to escalate

If your audit is positive, the next domain-specific routes are:
- For claims in Books IV–V: [Physicist route]({{ '/verify/how-to-audit/physicist/' | relative_url }})
- For claims in Books VI–VII: [Philosopher route]({{ '/verify/how-to-audit/philosopher/' | relative_url }})
- For specialist-level claims: [Mathematician route]({{ '/verify/how-to-audit/mathematician/' | relative_url }}) and [Prior-Art Specialist route]({{ '/verify/how-to-audit/prior-art-specialist/' | relative_url }})

If your audit is negative, [contact the program]({{ '/engage/contact/' | relative_url }}) with the specific check that failed — this is the single most valuable feedback the project can receive.

## Cross-links

- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — the snapshot you are verifying against
- [Formalization Status dashboard]({{ '/verify/taulib/status/' | relative_url }}) — per-book module counts, sorry and axiom inventories
- [TauLib Architecture]({{ '/verify/taulib/architecture/' | relative_url }}) — module dependency graph
- [How to Audit (Hub)]({{ '/verify/how-to-audit/' | relative_url }}) — all six reviewer routes
