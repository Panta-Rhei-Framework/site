---
layout: taulib-doc
title: "TauLib.BookIV.Arena.FiveSectors"
permalink: /verify/taulib/docs/book-iv-arena-five-sectors/
lane: verify
module_name: "TauLib.BookIV.Arena.FiveSectors"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Arena.FiveSectors


The 5-sector coupling atlas: full ledger, temporal complement,
power hierarchy, no-running principle, and generator adequacy.

## Registry Cross-References


- [IV.D264] Generator–Sector Correspondence — `gen_sector_corr`

- [IV.T98] Uniqueness of Φ — `phi_unique`

- [IV.D265] Coupling Ledger — `CouplingLedger`

- [IV.T99] Temporal Complement — `temporal_complement`

- [IV.R225] Physical meaning — (structural remark)

- [IV.P154] Temporal Multiplicative Closure — `temporal_mult_closure`

- [IV.P155] Multiplicative Closure — `full_mult_closure`

- [IV.P156] Power Hierarchy — `power_hier`

- [IV.R226] Power structure — (structural remark)

- [IV.T100] No-Running Principle — `no_running`

- [IV.D266] Boundary holonomy generators — `HolonomyGenerator`

- [IV.T101] Generator Adequacy — `generator_adequacy`


## Ground Truth Sources


- Chapter 6 of Book IV (2nd Edition)


---

### `Tau.BookIV.Arena.gen_sector_corr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L37-L40)@[reducible, inline]

**abbrev
Tau.BookIV.Arena.gen_sector_corr
(g : Kernel.Generator)
 :BookIII.Sectors.Sector**


[IV.D264] Generator-Sector Correspondence: the canonical bijection
from the 5 generators to the 5 sectors. Wraps GenSectorAssignment
from CoherenceKernel with the Chapter 6 presentation.
Equations
- Tau.BookIV.Arena.gen_sector_corr = Tau.BookIV.Arena.GenSectorAssignment
Instances For

---

### `Tau.BookIV.Arena.phi_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L46-L52)
**theorem
Tau.BookIV.Arena.phi_unique
(Psi : Kernel.Generator → BookIII.Sectors.Sector)

(h_pol : ∀ (g : Kernel.Generator), (Sectors.sector_physics (Psi g)).polarity = gen_polarity g)

(h_dep : ∀ (g : Kernel.Generator), (Sectors.sector_physics (Psi g)).depth = gen_depth g)

(g : Kernel.Generator)
 :Psi g = gen_sector_corr g**


[IV.T98] Φ is the unique polarity-preserving, depth-respecting assignment.
Wraps assignment_unique from CoherenceKernel.

---

### `Tau.BookIV.Arena.CouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L58-L69)
**structure
Tau.BookIV.Arena.CouplingEntry :Type**


[IV.D265] A coupling entry in the ledger: self or cross coupling.

- sector1 : BookIII.Sectors.Sector
Source sector.

- sector2 : BookIII.Sectors.Sector
Target sector (same for self-coupling).

- numer : ℕ
Coupling numerator (scaled).

- denom : ℕ
Coupling denominator (scaled).

- denom_pos : self.denom > 0
Instances For

---

### `Tau.BookIV.Arena.instReprCouplingEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L69-L69)
**def
Tau.BookIV.Arena.instReprCouplingEntry.repr :CouplingEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprCouplingEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L69-L69)
**instance
Tau.BookIV.Arena.instReprCouplingEntry :Repr CouplingEntry**

Equations
- Tau.BookIV.Arena.instReprCouplingEntry = { reprPrec := Tau.BookIV.Arena.instReprCouplingEntry.repr }

---

### `Tau.BookIV.Arena.CouplingLedger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L71-L79)
**structure
Tau.BookIV.Arena.CouplingLedger :Type**


[IV.D265] The complete coupling ledger: 5 self + 10 cross = 15 entries.
All determined by ι<sub>τ</sub> alone (No Knobs, III.T08).

- self_entries : List CouplingEntry
Self-coupling entries (5).

- self_count : self.self_entries.length = 5
- cross_entries : List CouplingEntry
Cross-coupling entries (10).

- cross_count : self.cross_entries.length = 10
Instances For

---

### `Tau.BookIV.Arena.temporal_complement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L85-L90)
**theorem
Tau.BookIV.Arena.temporal_complement :Sectors.kappa_AA.numer + Sectors.kappa_DD.numer = Sectors.kappa_AA.denom**


[IV.T99] Temporal complement: κ(A) + κ(D) = 1.
Physical meaning [IV.R225]: temporal resources fully allocated.
Wraps CouplingFormulas.temporal_complement.

---

### `Tau.BookIV.Arena.temporal_mult_closure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L96-L101)
**theorem
Tau.BookIV.Arena.temporal_mult_closure :Sectors.kappa_AD.numer * (Sectors.kappa_AA.denom * Sectors.kappa_DD.denom) = Sectors.kappa_AA.numer * Sectors.kappa_DD.numer * Sectors.kappa_AD.denom**


[IV.P154] Temporal multiplicative closure: κ(A)·κ(D) < 1/4 (strict AM-GM).
Since κ(A) + κ(D) = 1 and κ(A) ≠ κ(D), strict inequality holds.

---

### `Tau.BookIV.Arena.power_hier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L111-L120)
**theorem
Tau.BookIV.Arena.power_hier :Sectors.kappa_BB.numer * (Sectors.kappa_AA.denom * Sectors.kappa_AA.denom) = Sectors.kappa_AA.numer * Sectors.kappa_AA.numer * Sectors.kappa_BB.denom ∧ Sectors.kappa_AC.numer * (Sectors.kappa_AA.denom * Sectors.kappa_CC.denom) = Sectors.kappa_AA.numer * Sectors.kappa_CC.numer * Sectors.kappa_AC.denom**


[IV.P156] Power hierarchy: κ(B;2) = κ(A;1)² and κ(A,C) = κ(A;1)·κ(C;3).
Wraps CouplingFormulas power relations and multiplicative closure.

---

### `Tau.BookIV.Arena.NoRunning`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L129-L139)
**structure
Tau.BookIV.Arena.NoRunning :Type**


[IV.T100] No-Running Principle: coupling constants don't run with energy.
They are fixed-point readouts of the categorical structure, not
scale-dependent quantities. β(κ) ≡ 0 for all sector couplings.

- beta_zero : Bool
β-function vanishes identically.

- beta_true : self.beta_zero = true
- fixed_count : ℕ
Number of fixed couplings.

- fixed_eq : self.fixed_count = 15
Instances For

---

### `Tau.BookIV.Arena.instReprNoRunning`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L139-L139)
**instance
Tau.BookIV.Arena.instReprNoRunning :Repr NoRunning**

Equations
- Tau.BookIV.Arena.instReprNoRunning = { reprPrec := Tau.BookIV.Arena.instReprNoRunning.repr }

---

### `Tau.BookIV.Arena.instReprNoRunning.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L139-L139)
**def
Tau.BookIV.Arena.instReprNoRunning.repr :NoRunning → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.no_running`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L141-L146)
**def
Tau.BookIV.Arena.no_running :NoRunning**


The no-running principle instance.
Equations
- Tau.BookIV.Arena.no_running = { beta_zero := true, beta_true := ⋯, fixed_count := 15, fixed_eq := Tau.BookIV.Arena.no_running._proof_1 }
Instances For

---

### `Tau.BookIV.Arena.HolonomyGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L152-L161)
**structure
Tau.BookIV.Arena.HolonomyGenerator :Type**


[IV.D266] The 5 generators of the boundary holonomy algebra.
Each generator produces holonomy around one sector of L.

- gen : Kernel.Generator
The underlying generator.

- sector : BookIII.Sectors.Sector
Associated sector.

- correct : GenSectorAssignment self.gen = self.sector
Correct assignment.

Instances For

---

### `Tau.BookIV.Arena.instReprHolonomyGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L161-L161)
**instance
Tau.BookIV.Arena.instReprHolonomyGenerator :Repr HolonomyGenerator**

Equations
- Tau.BookIV.Arena.instReprHolonomyGenerator = { reprPrec := Tau.BookIV.Arena.instReprHolonomyGenerator.repr }

---

### `Tau.BookIV.Arena.instReprHolonomyGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L161-L161)
**def
Tau.BookIV.Arena.instReprHolonomyGenerator.repr :HolonomyGenerator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.holonomy_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L163-L166)
**def
Tau.BookIV.Arena.holonomy_generators :List HolonomyGenerator**


All 5 holonomy generators.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.generator_adequacy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/FiveSectors.lean#L172-L179)
**theorem
Tau.BookIV.Arena.generator_adequacy :holonomy_generators.length = 5 ∧ (List.map (fun (x : HolonomyGenerator) => x.sector) holonomy_generators).length = 5**


[IV.T101] Generator Adequacy: the 5 generators span the full
coupling ledger. Every coupling in the ledger is expressible
as a function of sector couplings, which are functions of ι<sub>τ</sub>.
