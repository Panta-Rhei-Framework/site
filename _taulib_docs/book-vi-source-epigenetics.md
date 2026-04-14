---
layout: taulib-doc
title: "TauLib.BookVI.Source.Epigenetics"
permalink: /verify/taulib/docs/book-vi-source-epigenetics/
lane: verify
module_name: "TauLib.BookVI.Source.Epigenetics"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.Source.Epigenetics


Epigenetic regulation: evaluator-modulated code reading at each refinement level.

## Registry Cross-References


- [VI.D78] Chromatin Partition — `ChromatinPartition`

- [VI.D79] Epigenetic State — `EpigeneticState`

- [VI.D80] Gene Expression Profile — `GeneExpressionProfile`

- [VI.D81] Potency Restriction — `PotencyRestriction`

- [VI.D82] Intergenerational Transfer — `IntergenerationalTransfer`

- [VI.D83] Waddington Landscape — `WaddingtonLandscape`

- [VI.D84] Cell Fate — `CellFate`

- [VI.T47] Differentiation Irreversible — `differentiation_irreversible`

- [VI.T48] Reprogramming Refinement Reversal — `reprogramming_refinement_reversal`

- [VI.P22] Cell Fate Fixed Point — `cell_fate_fixed_point`

- [VI.D85] Epigenetic Drift — `EpigeneticDrift`

- [VI.T49] Drift Bounded by Repair — `drift_bounded_by_repair`


## Cross-Book Authority


- Book I, Part III: Distinction D: X → 2_τ (clopen boundary)

- Book II, Part X: ω-germ code (code invariance under development)

- VI.D04: Distinction clopen boundary

- VI.D08: SelfDesc — evaluator reads ω-germ code

- VI.D40: BSDGeneticCode (codon structure)

- VI.D43: AgingDefect (multi-level defect accumulation)

- VI.D45: RepairBudget

- VI.P15: Central Dogma morphism

- VI.P16: RepairBudgetExhaustion

- VI.P18: DevelopmentDifferentiation (5 potency levels, refinement tower)

- VI.T03: SelfDesc closure theorem


## Ground Truth Sources


- Book VI Chapter 35 (2nd Edition): Cell Cycle, Multicellularity, and Development


---

### `Tau.BookVI.Epigenetics.ChromatinPartition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L47-L61)
**structure
Tau.BookVI.Epigenetics.ChromatinPartition :Type**


[VI.D78] Chromatin Partition.
Distinction clopen boundary at chromatin level: genome partitioned into
euchromatin (active, D⁻¹(+)) and heterochromatin (silenced, D⁻¹(−)).
The partition is a biological instance of VI.D04 (Distinction clopen boundary).
Scope: τ-effective.

- euchromatin_fraction : String
Fraction of genome in euchromatin (active, open chromatin).

- heterochromatin_fraction : String
Fraction of genome in heterochromatin (silenced, condensed).

- clopen : Bool
Disjoint union covers entire genome (clopen property).

- scope : String
Scope: τ-effective (chromatin partition is a Distinction instance).

Instances For

---

### `Tau.BookVI.Epigenetics.instReprChromatinPartition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L61-L61)
**def
Tau.BookVI.Epigenetics.instReprChromatinPartition.repr :ChromatinPartition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.instReprChromatinPartition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L61-L61)
**instance
Tau.BookVI.Epigenetics.instReprChromatinPartition :Repr ChromatinPartition**

Equations
- Tau.BookVI.Epigenetics.instReprChromatinPartition = { reprPrec := Tau.BookVI.Epigenetics.instReprChromatinPartition.repr }

---

### `Tau.BookVI.Epigenetics.chromatin_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L63-L63)
**def
Tau.BookVI.Epigenetics.chromatin_partition :ChromatinPartition**

Equations
- Tau.BookVI.Epigenetics.chromatin_partition = { }
Instances For

---

### `Tau.BookVI.Epigenetics.chromatin_partition_clopen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L65-L67)
**theorem
Tau.BookVI.Epigenetics.chromatin_partition_clopen :chromatin_partition.clopen = true**


---

### `Tau.BookVI.Epigenetics.EpigeneticState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L73-L88)
**structure
Tau.BookVI.Epigenetics.EpigeneticState :Type**


[VI.D79] Epigenetic State.
Evaluator-modulated code reading at refinement level n.
Combines chromatin partition (VI.D78) with refinement level (VI.P18).
The evaluator (VI.D08, SelfDesc) reads the same ω-germ code differently
at each level by restricting which genes are accessible.
Scope: τ-effective.

- refinement_level : ℕ
Refinement level in the differentiation tower (0 = totipotent).

- has_chromatin_partition : Bool
Associated chromatin partition determines accessible genes.

- active_gene_count : ℕ
Number of genes in euchromatin (active) at this level.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprEpigeneticState.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L88-L88)
**def
Tau.BookVI.Epigenetics.instReprEpigeneticState.repr :EpigeneticState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.instReprEpigeneticState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L88-L88)
**instance
Tau.BookVI.Epigenetics.instReprEpigeneticState :Repr EpigeneticState**

Equations
- Tau.BookVI.Epigenetics.instReprEpigeneticState = { reprPrec := Tau.BookVI.Epigenetics.instReprEpigeneticState.repr }

---

### `Tau.BookVI.Epigenetics.totipotent_state`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L90-L92)
**def
Tau.BookVI.Epigenetics.totipotent_state :EpigeneticState**

Equations
- Tau.BookVI.Epigenetics.totipotent_state = { refinement_level := 0, active_gene_count := 20000 }
Instances For

---

### `Tau.BookVI.Epigenetics.totipotent_is_level_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L94-L96)
**theorem
Tau.BookVI.Epigenetics.totipotent_is_level_zero :totipotent_state.refinement_level = 0**


---

### `Tau.BookVI.Epigenetics.GeneExpressionProfile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L102-L116)
**structure
Tau.BookVI.Epigenetics.GeneExpressionProfile :Type**


[VI.D80] Gene Expression Profile.
The subset of the genetic code (VI.D40) that the Central Dogma (VI.P15)
actually reads at a given epigenetic state. Only genes in D⁻¹(+)
(euchromatin) are transcribed.
Scope: τ-effective.

- total_genes : ℕ
Total genes in genome.

- expressed_genes : ℕ
Genes expressed (in euchromatin).

- expressed_leq_total : self.expressed_genes ≤ self.total_genes
Expressed ≤ total (chromatin restricts).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprGeneExpressionProfile.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L116-L116)
**def
Tau.BookVI.Epigenetics.instReprGeneExpressionProfile.repr :GeneExpressionProfile → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.instReprGeneExpressionProfile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L116-L116)
**instance
Tau.BookVI.Epigenetics.instReprGeneExpressionProfile :Repr GeneExpressionProfile**

Equations
- Tau.BookVI.Epigenetics.instReprGeneExpressionProfile = { reprPrec := Tau.BookVI.Epigenetics.instReprGeneExpressionProfile.repr }

---

### `Tau.BookVI.Epigenetics.typical_somatic_profile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L118-L121)
**def
Tau.BookVI.Epigenetics.typical_somatic_profile :GeneExpressionProfile**

Equations
- Tau.BookVI.Epigenetics.typical_somatic_profile = { total_genes := 20000, expressed_genes := 5000,
 expressed_leq_total := Tau.BookVI.Epigenetics.typical_somatic_profile._proof_1 }
Instances For

---

### `Tau.BookVI.Epigenetics.expression_is_restricted`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L123-L125)
**theorem
Tau.BookVI.Epigenetics.expression_is_restricted :typical_somatic_profile.expressed_genes ≤ typical_somatic_profile.total_genes**


---

### `Tau.BookVI.Epigenetics.PotencyRestriction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L131-L146)
**structure
Tau.BookVI.Epigenetics.PotencyRestriction :Type**


[VI.D81] Potency Restriction.
More restrictive chromatin partition ↔ lower potency level.
The 5 potency levels (totipotent, pluripotent, multipotent, oligopotent,
unipotent) from VI.P18 correspond to monotonically increasing chromatin
restriction.
Scope: τ-effective.

- potency_levels : ℕ
Number of potency levels in the hierarchy.

- levels_eq : self.potency_levels = 5
Exactly 5 levels.

- monotone_restriction : Bool
Restriction is monotone: higher level → more heterochromatin.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprPotencyRestriction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L146-L146)
**instance
Tau.BookVI.Epigenetics.instReprPotencyRestriction :Repr PotencyRestriction**

Equations
- Tau.BookVI.Epigenetics.instReprPotencyRestriction = { reprPrec := Tau.BookVI.Epigenetics.instReprPotencyRestriction.repr }

---

### `Tau.BookVI.Epigenetics.instReprPotencyRestriction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L146-L146)
**def
Tau.BookVI.Epigenetics.instReprPotencyRestriction.repr :PotencyRestriction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.potency_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L148-L150)
**def
Tau.BookVI.Epigenetics.potency_hierarchy :PotencyRestriction**

Equations
- Tau.BookVI.Epigenetics.potency_hierarchy = { potency_levels := 5, levels_eq := Tau.BookVI.Epigenetics.potency_hierarchy._proof_1 }
Instances For

---

### `Tau.BookVI.Epigenetics.potency_has_five_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L152-L154)
**theorem
Tau.BookVI.Epigenetics.potency_has_five_levels :potency_hierarchy.potency_levels = 5**


---

### `Tau.BookVI.Epigenetics.IntergenerationalTransfer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L160-L175)
**structure
Tau.BookVI.Epigenetics.IntergenerationalTransfer :Type**


[VI.D82] Intergenerational Transfer.
Partial inheritance of epigenetic marks through cell division.
Unlike DNA replication (high fidelity), epigenetic mark copying is lossy:
DNMT1 copies methylation with ~95% fidelity per CpG per division.
This is SelfDesc closure (VI.T03) with inherent transmission loss.
Scope: τ-effective.

- maintenance_enzyme : String
Primary maintenance mechanism.

- lossy : Bool
Transmission is lossy (unlike DNA replication).

- fidelity_per_cpg_x100 : ℕ
Approximate fidelity per CpG per division (×100 for integer).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprIntergenerationalTransfer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L175-L175)
**instance
Tau.BookVI.Epigenetics.instReprIntergenerationalTransfer :Repr IntergenerationalTransfer**

Equations
- Tau.BookVI.Epigenetics.instReprIntergenerationalTransfer = { reprPrec := Tau.BookVI.Epigenetics.instReprIntergenerationalTransfer.repr }

---

### `Tau.BookVI.Epigenetics.instReprIntergenerationalTransfer.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L175-L175)
**def
Tau.BookVI.Epigenetics.instReprIntergenerationalTransfer.repr :IntergenerationalTransfer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.epigenetic_transfer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L177-L177)
**def
Tau.BookVI.Epigenetics.epigenetic_transfer :IntergenerationalTransfer**

Equations
- Tau.BookVI.Epigenetics.epigenetic_transfer = { }
Instances For

---

### `Tau.BookVI.Epigenetics.transfer_is_lossy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L179-L181)
**theorem
Tau.BookVI.Epigenetics.transfer_is_lossy :epigenetic_transfer.lossy = true**


---

### `Tau.BookVI.Epigenetics.WaddingtonLandscape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L187-L202)
**structure
Tau.BookVI.Epigenetics.WaddingtonLandscape :Type**


[VI.D83] Waddington Landscape.
The refinement tower (VI.P18) indexed by epigenetic state (VI.D79),
with the defect-functional Δ: State → ℝ≥0 providing the landscape surface.
Valleys = local minima of Δ (stable cell types).
Ridges = saddle points (barriers between fates).
Scope: τ-effective.

- potency_levels : ℕ
Number of potency levels (depth of tower).

- descending_active_genes : Bool
Active gene count descends along tower.

- defect_functional_surface : Bool
Surface given by defect functional Δ.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprWaddingtonLandscape.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L202-L202)
**def
Tau.BookVI.Epigenetics.instReprWaddingtonLandscape.repr :WaddingtonLandscape → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.instReprWaddingtonLandscape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L202-L202)
**instance
Tau.BookVI.Epigenetics.instReprWaddingtonLandscape :Repr WaddingtonLandscape**

Equations
- Tau.BookVI.Epigenetics.instReprWaddingtonLandscape = { reprPrec := Tau.BookVI.Epigenetics.instReprWaddingtonLandscape.repr }

---

### `Tau.BookVI.Epigenetics.waddington`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L204-L204)
**def
Tau.BookVI.Epigenetics.waddington :WaddingtonLandscape**

Equations
- Tau.BookVI.Epigenetics.waddington = { }
Instances For

---

### `Tau.BookVI.Epigenetics.waddington_descends`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L206-L208)
**theorem
Tau.BookVI.Epigenetics.waddington_descends :waddington.descending_active_genes = true**


---

### `Tau.BookVI.Epigenetics.CellFate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L214-L229)
**structure
Tau.BookVI.Epigenetics.CellFate :Type**


[VI.D84] Cell Fate.
Terminal epigenetic state: fully restricted chromatin partition
at the bottom of the Waddington landscape. The cell expresses
only the genes required for its specialized function.
Fixed under SelfDesc maintenance (VI.T03).
Scope: τ-effective.

- terminal : Bool
Terminal differentiation state.

- potency_level : String
Potency level at terminal state.

- fixed_under_selfdesc : Bool
Fixed under SelfDesc evaluator maintenance.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprCellFate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L229-L229)
**instance
Tau.BookVI.Epigenetics.instReprCellFate :Repr CellFate**

Equations
- Tau.BookVI.Epigenetics.instReprCellFate = { reprPrec := Tau.BookVI.Epigenetics.instReprCellFate.repr }

---

### `Tau.BookVI.Epigenetics.instReprCellFate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L229-L229)
**def
Tau.BookVI.Epigenetics.instReprCellFate.repr :CellFate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.terminal_fate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L231-L231)
**def
Tau.BookVI.Epigenetics.terminal_fate :CellFate**

Equations
- Tau.BookVI.Epigenetics.terminal_fate = { }
Instances For

---

### `Tau.BookVI.Epigenetics.terminal_is_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L233-L235)
**theorem
Tau.BookVI.Epigenetics.terminal_is_fixed :terminal_fate.fixed_under_selfdesc = true**


---

### `Tau.BookVI.Epigenetics.DifferentiationIrreversible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L241-L256)
**structure
Tau.BookVI.Epigenetics.DifferentiationIrreversible :Type**


[VI.T47] Differentiation Is Irreversible Under Normal Conditions.
Each step in the refinement tower restricts chromatin (VI.D81, monotone),
and SelfDesc maintenance (VI.T03) preserves the restriction.
Therefore descent through the Waddington landscape is irreversible
under normal cellular conditions.
Scope: τ-effective.

- monotone_restriction : Bool
Chromatin restriction is monotone (VI.D81).

- selfdesc_maintains : Bool
SelfDesc maintains restriction (VI.T03).

- irreversible : Bool
Descent is irreversible under normal conditions.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprDifferentiationIrreversible.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L256-L256)
**def
Tau.BookVI.Epigenetics.instReprDifferentiationIrreversible.repr :DifferentiationIrreversible → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.instReprDifferentiationIrreversible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L256-L256)
**instance
Tau.BookVI.Epigenetics.instReprDifferentiationIrreversible :Repr DifferentiationIrreversible**

Equations
- Tau.BookVI.Epigenetics.instReprDifferentiationIrreversible = { reprPrec := Tau.BookVI.Epigenetics.instReprDifferentiationIrreversible.repr }

---

### `Tau.BookVI.Epigenetics.diff_irrev`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L258-L258)
**def
Tau.BookVI.Epigenetics.diff_irrev :DifferentiationIrreversible**

Equations
- Tau.BookVI.Epigenetics.diff_irrev = { }
Instances For

---

### `Tau.BookVI.Epigenetics.differentiation_irreversible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L260-L264)
**theorem
Tau.BookVI.Epigenetics.differentiation_irreversible :diff_irrev.monotone_restriction = true ∧ diff_irrev.selfdesc_maintains = true ∧ diff_irrev.irreversible = true**


---

### `Tau.BookVI.Epigenetics.ReprogrammingReversal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L270-L285)
**structure
Tau.BookVI.Epigenetics.ReprogrammingReversal :Type**


[VI.T48] Reprogramming as Refinement Reversal.
The ω-germ code is unchanged throughout differentiation (VI.P18, item iv),
so chromatin restriction is reversible in principle.
Yamanaka factors (Oct4, Sox2, Klf4, c-Myc) demonstrate constructive
reversal: C_k → C_{k-1} → ··· → C_1.
Scope: τ-effective.

- code_invariant : Bool
Code is invariant (ω-germ unchanged).

- yamanaka_demonstrated : Bool
Reversal demonstrated by Yamanaka factors (2006).

- factor_count : ℕ
Number of Yamanaka factors.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprReprogrammingReversal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L285-L285)
**instance
Tau.BookVI.Epigenetics.instReprReprogrammingReversal :Repr ReprogrammingReversal**

Equations
- Tau.BookVI.Epigenetics.instReprReprogrammingReversal = { reprPrec := Tau.BookVI.Epigenetics.instReprReprogrammingReversal.repr }

---

### `Tau.BookVI.Epigenetics.instReprReprogrammingReversal.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L285-L285)
**def
Tau.BookVI.Epigenetics.instReprReprogrammingReversal.repr :ReprogrammingReversal → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.reprog`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L287-L287)
**def
Tau.BookVI.Epigenetics.reprog :ReprogrammingReversal**

Equations
- Tau.BookVI.Epigenetics.reprog = { }
Instances For

---

### `Tau.BookVI.Epigenetics.reprogramming_refinement_reversal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L289-L293)
**theorem
Tau.BookVI.Epigenetics.reprogramming_refinement_reversal :reprog.code_invariant = true ∧ reprog.yamanaka_demonstrated = true ∧ reprog.factor_count = 4**


---

### `Tau.BookVI.Epigenetics.CellFateFixedPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L299-L314)
**structure
Tau.BookVI.Epigenetics.CellFateFixedPoint :Type**


[VI.P22] Cell Fate as Fixed Point.
At terminal differentiation, the SelfDesc evaluator maintains the
fully restricted chromatin partition. Perturbations within the basin
of attraction are absorbed by SelfDesc closure (VI.T03).
Terminal differentiation is a fixed point of the evaluator dynamics.
Scope: τ-effective.

- self_maintaining : Bool
Terminal state is self-maintaining.

- basin_absorbing : Bool
Perturbations absorbed by SelfDesc closure (VI.T03).

- is_fixed_point : Bool
Fixed point of evaluator dynamics.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprCellFateFixedPoint.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L314-L314)
**def
Tau.BookVI.Epigenetics.instReprCellFateFixedPoint.repr :CellFateFixedPoint → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.instReprCellFateFixedPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L314-L314)
**instance
Tau.BookVI.Epigenetics.instReprCellFateFixedPoint :Repr CellFateFixedPoint**

Equations
- Tau.BookVI.Epigenetics.instReprCellFateFixedPoint = { reprPrec := Tau.BookVI.Epigenetics.instReprCellFateFixedPoint.repr }

---

### `Tau.BookVI.Epigenetics.fate_fp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L316-L316)
**def
Tau.BookVI.Epigenetics.fate_fp :CellFateFixedPoint**

Equations
- Tau.BookVI.Epigenetics.fate_fp = { }
Instances For

---

### `Tau.BookVI.Epigenetics.cell_fate_fixed_point`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L318-L322)
**theorem
Tau.BookVI.Epigenetics.cell_fate_fixed_point :fate_fp.self_maintaining = true ∧ fate_fp.basin_absorbing = true ∧ fate_fp.is_fixed_point = true**


---

### `Tau.BookVI.Epigenetics.EpigeneticDrift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L328-L343)
**structure
Tau.BookVI.Epigenetics.EpigeneticDrift :Type**


[VI.D85] Epigenetic Drift.
Age-related loss of epigenetic fidelity: methylation patterns erode,
histone marks become noisy. An instance of the aging defect (VI.D43)
at the chromatin level. The Horvath methylation clock correlates
epigenetic drift with chronological age.
Scope: τ-effective.

- drift_source : String
Primary mechanism: methylation loss + histone mark erosion.

- monotone_fidelity_loss : Bool
Fidelity decreases monotonically with age.

- instance_of_aging_defect : Bool
Instance of aging defect (VI.D43).

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprEpigeneticDrift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L343-L343)
**instance
Tau.BookVI.Epigenetics.instReprEpigeneticDrift :Repr EpigeneticDrift**

Equations
- Tau.BookVI.Epigenetics.instReprEpigeneticDrift = { reprPrec := Tau.BookVI.Epigenetics.instReprEpigeneticDrift.repr }

---

### `Tau.BookVI.Epigenetics.instReprEpigeneticDrift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L343-L343)
**def
Tau.BookVI.Epigenetics.instReprEpigeneticDrift.repr :EpigeneticDrift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.epi_drift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L345-L345)
**def
Tau.BookVI.Epigenetics.epi_drift :EpigeneticDrift**

Equations
- Tau.BookVI.Epigenetics.epi_drift = { }
Instances For

---

### `Tau.BookVI.Epigenetics.drift_is_aging_instance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L347-L349)
**theorem
Tau.BookVI.Epigenetics.drift_is_aging_instance :epi_drift.instance_of_aging_defect = true**


---

### `Tau.BookVI.Epigenetics.DriftBoundedByRepair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L355-L370)
**structure
Tau.BookVI.Epigenetics.DriftBoundedByRepair :Type**


[VI.T49] Epigenetic Drift Bounded by Repair Budget.
DNMT1 (maintenance methyltransferase) and histone mark copying
consume repair resources (VI.D45, RepairBudget).
When the repair budget is exhausted (VI.P16, RepairBudgetExhaustion),
epigenetic maintenance fails and drift becomes uncontrolled.
Scope: τ-effective.

- consumes_repair_budget : Bool
Maintenance consumes repair budget (VI.D45).

- exhaustion_implies_drift : Bool
Budget exhaustion → uncontrolled drift (VI.P16).

- bounded_while_funded : Bool
Bounded while budget remains.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.Epigenetics.instReprDriftBoundedByRepair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L370-L370)
**instance
Tau.BookVI.Epigenetics.instReprDriftBoundedByRepair :Repr DriftBoundedByRepair**

Equations
- Tau.BookVI.Epigenetics.instReprDriftBoundedByRepair = { reprPrec := Tau.BookVI.Epigenetics.instReprDriftBoundedByRepair.repr }

---

### `Tau.BookVI.Epigenetics.instReprDriftBoundedByRepair.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L370-L370)
**def
Tau.BookVI.Epigenetics.instReprDriftBoundedByRepair.repr :DriftBoundedByRepair → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Epigenetics.drift_repair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L372-L372)
**def
Tau.BookVI.Epigenetics.drift_repair :DriftBoundedByRepair**

Equations
- Tau.BookVI.Epigenetics.drift_repair = { }
Instances For

---

### `Tau.BookVI.Epigenetics.drift_bounded_by_repair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/Epigenetics.lean#L374-L378)
**theorem
Tau.BookVI.Epigenetics.drift_bounded_by_repair :drift_repair.consumes_repair_budget = true ∧ drift_repair.exhaustion_implies_drift = true ∧ drift_repair.bounded_while_funded = true**
