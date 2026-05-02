---
layout: program-doc
title: "How to Engage"
lane: engage
v2_lane: engage
type: "Engagement Guide"
status: "Canonical"
permalink: /engage/how-to-engage/
summary_short: "A routing guide for structured open-research engagement: public questions, critique, review, corrections, contribution, contact, and support."
og_image: "/assets/images/plates/plate-09-engagement-without-endorsement-og.jpg"
twitter_image: "/assets/images/plates/plate-09-engagement-without-endorsement-og.jpg"
og_image_alt: "Scientific plate showing the Engage lane as structured open-research engagement: read carefully, inspect claims, challenge weak links, review bounded areas, contribute infrastructure, communicate responsibly, open institutional dialogue, and support continuation without endorsement."
summary_cards:
  - title: "No agreement required"
    body: "Engagement does not require agreement; it requires attention to a specific public object."
  - title: "Choose the route"
    body: "Use Discussions, Issues, Pull Requests, or email depending on what kind of attention you can offer."
  - title: "Bounded is better"
    body: "Useful engagement names the target page, claim, artifact, module, status label, or correction route."
right_rail:
  related:
    - title: "Engage"
      url: /engage/
    - title: "Public Discussions"
      url: /engage/discussions/
    - title: "Review the Work"
      url: /engage/review-the-work/
    - title: "Read & Explore"
      url: /engage/read-explore/
    - title: "Inspect & Verify"
      url: /engage/inspect-verify/
    - title: "Critique & Challenge"
      url: /engage/critique-challenge/
    - title: "Contact"
      url: /engage/contact/
  meta:
    type: "Engagement Guide"
    status: "Canonical"
    updated: "April 2026"
tags:
  - engage
  - open-research
  - github-discussions
  - scrutiny
  - critique
  - review
  - contribution
  - non-endorsement
  - public-discussion
---

## Engagement without endorsement

Engagement does not require agreement.

The program needs different kinds of attention: careful readers, public questions, specific critique, reproducibility checks, domain review, corrections, infrastructure contributions, responsible communication, institutional dialogue, and non-endorsement support.

## Choose the kind of attention you can offer

Engagement does not begin with agreement. It begins with a useful form of attention: reading, inspection, critique, review, contribution, responsible communication, institutional dialogue, or support without endorsement.

{% assign how_to_engage_plate_caption = "The Engage lane separates attention modes from endorsement: readers can ask questions, critique, review, contribute, communicate, or support without being asked to agree first." %}
{% include scientific-plate.html id="plate-09-engagement-without-endorsement" variant="thumb" class="scientific-plate--compact" caption=how_to_engage_plate_caption loading="lazy" %}

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/engage/read-explore/' | relative_url }}">
    <h3>Read carefully</h3>
    <p>Use Discover, Program, Agenda, Publications, and Results before judging isolated claims.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/discussions/' | relative_url }}">
    <h3>Ask a public question</h3>
    <p>Use GitHub Discussions when the question and answer may help other readers.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/inspect-verify/' | relative_url }}">
    <h3>Inspect a claim</h3>
    <p>Trace claims into Corpus, Results, Verify, TauLib, release manifests, and assessment protocols.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/critique-challenge/' | relative_url }}">
    <h3>Challenge a weak link</h3>
    <p>Name the claim, the suspected failure mode, and what would count as correction or failure.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/review-the-work/' | relative_url }}">
    <h3>Offer bounded review</h3>
    <p>Review one problem item, recovery target, result, research note, TauLib module, briefing, or page template.</p>
  </a>
  <a class="v2-tile" href="https://github.com/Panta-Rhei-Research/site/issues">
    <h3>Report a defect</h3>
    <p>Use Issues for broken links, wrong metadata, bad redirects, build failures, or reproducible public defects.</p>
  </a>
  <a class="v2-tile" href="https://github.com/Panta-Rhei-Research">
    <h3>Propose a correction</h3>
    <p>Use Pull Requests for concrete wording, metadata, documentation, formalization, or site improvements.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/for-engineering-contributors/' | relative_url }}">
    <h3>Contribute infrastructure</h3>
    <p>Improve documentation, search, templates, registry hygiene, TauLib docs, import reports, or site structure.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/media/' | relative_url }}">
    <h3>Communicate responsibly</h3>
    <p>Describe the work as independent open research under scrutiny, not as settled external acceptance.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/contact/' | relative_url }}">
    <h3>Open institutional dialogue</h3>
    <p>Use email for private, institutional, media, sensitive, support, or non-public collaboration context.</p>
  </a>
  <a class="v2-tile" href="{{ '/engage/support-the-research/' | relative_url }}">
    <h3>Support continuation</h3>
    <p>Support ongoing public artifacts, infrastructure, formalization, correction workflows, and open-research engagement.</p>
  </a>
</div>

## Discussions, Issues, Pull Requests, Email

<table>
  <thead>
    <tr>
      <th scope="col">If you want to...</th>
      <th scope="col">Use</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Ask a public question</td><td><a href="https://github.com/orgs/Panta-Rhei-Research/discussions">GitHub Discussions</a></td></tr>
    <tr><td>Challenge a claim publicly</td><td><a href="https://github.com/orgs/Panta-Rhei-Research/discussions">GitHub Discussions</a></td></tr>
    <tr><td>Report a concrete defect</td><td><a href="https://github.com/Panta-Rhei-Research/site/issues">GitHub Issues</a></td></tr>
    <tr><td>Propose a concrete fix</td><td>Pull Request</td></tr>
    <tr><td>Offer domain review</td><td><a href="{{ '/engage/discussions/' | relative_url }}">GitHub Discussions</a> or email</td></tr>
    <tr><td>Contact privately</td><td>Email</td></tr>
    <tr><td>Discuss institutional review</td><td>Email</td></tr>
    <tr><td>Follow Research Notes</td><td><a href="{{ '/engage/follow-the-research/' | relative_url }}">Follow the Research</a></td></tr>
    <tr><td>Support continuation</td><td><a href="{{ '/engage/support-the-research/' | relative_url }}">Support the Research</a></td></tr>
  </tbody>
</table>

## Where to start

If your question can help other readers, begin with [Public Discussions]({{ '/engage/discussions/' | relative_url }}).

If your concern is concrete and actionable, use the relevant issue tracker:

- [Site issues](https://github.com/Panta-Rhei-Research/site/issues)
- [TauLib issues](https://github.com/Panta-Rhei-Research/taulib/issues)
- [Publications issues](https://github.com/Panta-Rhei-Research/publications/issues)
- [Research issues](https://github.com/Panta-Rhei-Research/research/issues)
- [Community issues](https://github.com/Panta-Rhei-Research/community/issues)

If your message is private, institutional, media-related, sensitive, or support-related, use [Contact]({{ '/engage/contact/' | relative_url }}).

## Minimum good-faith posture

You do not need to agree with the framework. You do need to engage the right object: a book, a result, a registry object, a formalization surface, an empirical prediction, a source record, a public briefing, or a stated assumption. The engagement routes above are designed to make that object easy to find.
