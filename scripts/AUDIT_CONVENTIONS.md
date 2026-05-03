# Corpus Audit Conventions

This file documents non-obvious conventions a regex-based audit might flag as defects but which are actually intentional. New audits should consult this list before treating matches as defects.

---

## 1. TauLib `projection_version` frontmatter

**Pattern:** `projection_version: "v3.0"` appearing in YAML frontmatter on ~512 pages under `corpus/taulib/docs/`.

**Status:** intentional metadata.

**Rationale:** The TauLib projection version tracks the imported Lean snapshot, not the surrounding Corpus narrative version. Site-wide construction-spine versions (e.g. v4) cover the public construction narrative and are independent of TauLib projection numbering. A bump to TauLib v4.0 would signal a new imported Lean snapshot, not a change of spine prose.

**Surface in UI:** `corpus/taulib/status/index.md` carries a "Projection version" row in the metric table and a "Projection versioning" section explaining the convention.

**Audit policy:** ignore — do not flag as stale version reference.

---

## 2. YAML expanded-style list-item delimiters

**Pattern:** lines matching the regex `^\s*-\s*$` — a dash followed only by whitespace, with mapping keys indented on the next lines. ~2,583 matches across the corpus, especially in `right_rail.related`, `summary_cards`, `related_taulib_modules`, `related_books`, `related_results`.

**Example:**
```yaml
related:
  -
    title: "Research Monograph artifact"
    url: "/publications/books/book-vii/"
  -
    title: "Registry"
    url: "/registry/books/book-vii/"
```

**Status:** valid YAML, intentional.

**Rationale:** This is YAML's expanded "block-mapping" style for list items where each item is a mapping. It is functionally equivalent to inline-style:
```yaml
related:
  - title: "Research Monograph artifact"
    url: "/publications/books/book-vii/"
```
The expanded style is the convention used by the Corpus monograph-projection generator (`corpus/monograph-projections`) and is mirrored in hand-authored construction-spine pages for consistency. Generated pages are marked `do_not_edit: true`.

**Audit policy:** do not flag `^\s*-\s*$` as an "empty bullet" defect — confirm it is followed by indented mapping keys before raising any concern.

**When this WOULD be a defect:** if a `^\s*-\s*$` line is followed by a blank line or by a non-indented YAML key, the list item is genuinely empty and should be removed or completed. None of the current 2,583 matches fall in that category.

---

## 3. Voice-discipline forbidden phrases

The corpus enforces voice discipline against five core phrases (and four softer extensions):
- Core: "externally verified", "this proves", "this settles", "obviously correct", "follows without assumptions"
- Extensions: "without doubt", "definitively", "the truth is", "as everyone knows"

**Audit policy:** zero hits expected across all `.md` source under `corpus/`. Any new hit should be treated as a defect and corrected.

---

## 4. Hardcoded release metrics

Public-facing numbers that drift over releases (modules / theorems / lines / references / named falsifications / numerical predictions / etc.) MUST use the `release-metric.html` include against `_data/release-manifest.yml`.

**Tooling:** `scripts/check_hardcoded_release_numbers.py` enforces this pre-commit. Any new occurrence of a manifest-tracked number in body prose should be replaced with the include.

**Audit policy:** zero hits expected; runner must pass exit 0.

---

## 5. Briefing-required H2 sections (construction-spine step pages)

Every page under `corpus/construction-spine/<step>/` must contain four H2 sections:
1. "What this step must build"
2. "construction challenge" (matches "The construction challenge")
3. "What Panta Rhei builds"
4. "matches the required answer-shape"

**Audit policy:** all 10 step pages must hit 4/4 in rendered HTML before any spine-touching PR ships.

---

Last updated: 2026-05-03 (Construction Spine v4 enrichment audit wave).
