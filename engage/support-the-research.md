---
layout: program-doc
title: "Support the Research"
lane: engage
permalink: /engage/support-the-research/
summary_short: "Support the continuation of the research — books first, follow second, direct support third."
summary_cards:
  - title: "Books first"
    body: "The most direct and meaningful way to support the research is to buy, read, and engage with the canonical books."
  - title: "Then follow"
    body: "Follow the research, share it with domain experts, recommend it to colleagues whose expertise is relevant."
  - title: "Then direct support"
    body: "If you want to support the continuation of the work directly, options will be available as the program matures."
right_rail:
  related:
    - title: "Publications"
      url: /publications/
    - title: "The Seven Books"
      url: /publications/books/
    - title: "Engage Overview"
      url: /engage/
  meta:
    type: "Support"
    status: "Active"
    updated: "April 2026"
---

## Support the Continuation of the Research

Supporting the Panta Rhei Research Program does not mean endorsing the framework. It means valuing the attempt — the disciplined, inspectable, falsifiable pursuit of a coherent model of reality — and wanting it to continue under public scrutiny.

## 1. Read the Books

The most direct way to support the research is to **engage with the canonical publications**:

{% for book in site.data.publications.books %}
- **Book {{ book.roman }}**: [{{ book.title }}](/publications/books/{{ book.id }}/) — *{{ book.subtitle }}*
{% endfor %}

Available as hardcover, paperback, and Kindle on Amazon KDP.

## 2. Follow the Research

Stay connected to the program's development:
- [Follow the Research](/engage/follow-the-research/) for email updates
- Watch the [TauLib repository](https://github.com/Panta-Rhei-Framework/taulib) on GitHub
- Bookmark this Atlas for new content

## 3. Share with Domain Experts

The program benefits most from engagement by people with relevant expertise:
- Mathematicians who can evaluate the foundational claims
- Physicists who can assess the predictions
- Biologists who can examine the life-science claims
- Philosophers who can engage with the metaphysical architecture
- Formal methods researchers who can audit TauLib

## 4. Direct Support

Options for direct financial support of the research will be made available as the program matures. This page will be updated when they are ready.

---

*The research advances through rigorous engagement. The strongest form of support is structured scrutiny by qualified experts.*
