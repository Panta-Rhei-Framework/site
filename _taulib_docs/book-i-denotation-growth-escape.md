---
layout: taulib-doc
title: "TauLib.BookI.Denotation.GrowthEscape"
permalink: /verify/taulib/docs/book-i-denotation-growth-escape/
lane: verify
module_name: "TauLib.BookI.Denotation.GrowthEscape"
book: "I"
book_label: "Foundations"
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Denotation.GrowthEscape


Tetration escapes the primorial tower: an independent quantitative argument
that tetration values eventually exceed any fixed primorial, making them
impossible to capture modularly.

## Registry Cross-References


- [I.L02] Growth Escape — `growth_escape`


## Mathematical Content


The primorial tower (M_1 = 2, M_2 = 6, M_3 = 30, M_4 = 210, M_5 = 2310, ...)
grows polynomially-like, while tetration grows super-exponentially.
For any tower depth d, there exists a tetration height c such that
2↑↑c > M_d, meaning the tetration value "escapes" the primorial modulus.

This provides an independent arithmetic reason — beyond the algebraic
degradation and channel exhaustion arguments — for why tetration cannot
be canonically integrated into the primorial tower framework.

Concrete witness: 2↑↑4 = 65536 > 2310 = M_5.

---

### `Tau.Denotation.GrowthEscape.tetration_exceeds_primorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/GrowthEscape.lean#L37-L40)
**theorem
Tau.Denotation.GrowthEscape.tetration_exceeds_primorial
(d : TauIdx)
 :∃ (c : Nat), Orbit.tetration 2 c > Polarity.primorial d**


For any primorial depth d, tetration 2 eventually exceeds primorial d.

---

### `Tau.Denotation.GrowthEscape.growth_escape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/GrowthEscape.lean#L53-L65)
**theorem
Tau.Denotation.GrowthEscape.growth_escape
(d : TauIdx)
 :∃ (c : Nat), Orbit.tetration 2 c % Polarity.primorial d ≠ Orbit.tetration 2 c**


[I.L02] **Growth Escape**: Tetration escapes the primorial tower.

For any tower depth d ≥ 1, there exists a tetration height c such that
2↑↑c mod M_d ≠ 2↑↑c — the tetration value cannot be represented
faithfully within the primorial modulus.

This is the quantitative shadow of saturation: the 4th hyperoperation
level produces values that outrun the finite primorial approximations,
no matter how deep the tower extends.
