---
layout: program-doc
title: "Corpus Versioning"
lane: corpus
v2_lane: corpus
permalink: /corpus/versioning/
type: "Corpus Guide"
status: "Draft"
summary_short: "How corpus objects, public releases, errata, and registry snapshots relate over time."
right_rail:
  related:
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Errata"
      url: /publications/errata/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Corpus Guide"
    status: "Draft"
    updated: "April 2026"
---

## Versioning stance

The corpus is living, but public claims must remain citeable. v2 separates living corpus state from released public artifacts.

Errata, changelog entries, release manifests, and registry snapshots together define how the public record changes over time.

## Current public surfaces

- [Errata]({{ '/publications/errata/' | relative_url }})
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }})
- [Changelog]({{ '/changelog/' | relative_url }})

## Snapshot model

<div class="v2-system-strip" aria-label="Corpus versioning model">
  <a href="{{ '/publications/books/' | relative_url }}">Book release</a>
  <span>-></span>
  <a href="{{ '/corpus/registry/' | relative_url }}">Registry state</a>
  <span>-></span>
  <a href="{{ '/verify/release-manifest/' | relative_url }}">Release manifest</a>
  <span>-></span>
  <a href="{{ '/publications/errata/' | relative_url }}">Errata</a>
  <span>-></span>
  <a href="{{ '/changelog/' | relative_url }}">Changelog</a>
</div>

## Working rule

Books and public release artifacts are citeable snapshots. The registry is the living source of truth for the corpus spine. When a correction changes the interpretation, status, or dependency structure of a corpus object, the public record should expose that change through errata, release notes, and manifest updates.
