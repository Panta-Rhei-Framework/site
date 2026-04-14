---
layout: taulib-doc
title: "TauLib.BookI.Kernel.Diagonal"
permalink: /verify/taulib/docs/book-i-kernel-diagonal/
lane: verify
module_name: "TauLib.BookI.Kernel.Diagonal"
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

# TauLib.Kernel.Diagonal


The Diagonal Discipline: why exactly 4 orbit channels, and why
the iterator ladder saturates at tetration (level 3).

## Registry Cross-References


- [I.D03] Diagonal Discipline — `diagonal_discipline`


## Mathematical Content


The free diagonal on {α, π, γ, η} × {α, π, γ, η} has 12 off-diagonal
pairs (g, h) with g ≠ h. These 12 pairs organize into 3 rewiring levels:


- Level 1 (addition): consumes the π channel

- Level 2 (multiplication): consumes the γ channel

- Level 3 (exponentiation): consumes the η channel


The α channel is the counting scaffold (τ-Idx) and cannot be consumed.
Since K6 closes the universe at exactly 4 non-omega generators,
no 4th rewiring level exists. The iterator ladder saturates at 3 rewirings
(4 operations: ρ, +, ×, ^).

---

### `Tau.Kernel.diagonal_channel_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L35-L39)
**theorem
Tau.Kernel.diagonal_channel_count :nonOmegaGenerators.length = 4**


[I.D03] There are exactly 4 non-omega generators.
This is the source of the diagonal discipline:
4 generators yield 3 rewiring levels.

---

### `Tau.Kernel.nonOmega_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L41-L44)
**theorem
Tau.Kernel.nonOmega_complete
(g : Generator)

(hg : g ≠ Generator.omega)
 :g ∈ nonOmegaGenerators**


The complete list of non-omega generators is [α, π, γ, η].

---

### `Tau.Kernel.solenoidalGenerators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L50-L52)
**def
Tau.Kernel.solenoidalGenerators :List Generator**


The 3 solenoidal generators that serve as rewiring targets.
α is the counting scaffold and is NOT a rewiring target.
Equations
- Tau.Kernel.solenoidalGenerators = [Tau.Kernel.Generator.pi, Tau.Kernel.Generator.gamma, Tau.Kernel.Generator.eta]
Instances For

---

### `Tau.Kernel.solenoidal_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L54-L56)
**theorem
Tau.Kernel.solenoidal_count :solenoidalGenerators.length = 3**


Exactly 3 solenoidal generators.

---

### `Tau.Kernel.solenoidal_ne_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L58-L62)
**theorem
Tau.Kernel.solenoidal_ne_alpha
(g : Generator)

(hg : g ∈ solenoidalGenerators)
 :g ≠ Generator.alpha**


The solenoidal generators are distinct from α.

---

### `Tau.Kernel.solenoidal_ne_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L64-L68)
**theorem
Tau.Kernel.solenoidal_ne_omega
(g : Generator)

(hg : g ∈ solenoidalGenerators)
 :g ≠ Generator.omega**


The solenoidal generators are distinct from ω.

---

### `Tau.Kernel.rewiring_levels_eq_solenoidal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L70-L79)
**theorem
Tau.Kernel.rewiring_levels_eq_solenoidal :solenoidalGenerators.length = nonOmegaGenerators.length - 1**


[I.D03] The diagonal discipline: exactly 3 rewiring levels exist
because exactly 3 solenoidal generators are available as targets.
Each rewiring level consumes one generator:


- Level 1 (addition) ↔ π

- Level 2 (multiplication) ↔ γ

- Level 3 (exponentiation) ↔ η
No 4th level: α is the counting scaffold, ω is the beacon.


---

### `Tau.Kernel.alpha_unique_scaffold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Kernel/Diagonal.lean#L81-L85)
**theorem
Tau.Kernel.alpha_unique_scaffold :¬Generator.alpha ∈ solenoidalGenerators ∧ Generator.alpha ≠ Generator.omega**


Alpha is the unique non-omega, non-solenoidal generator:
the counting scaffold.
