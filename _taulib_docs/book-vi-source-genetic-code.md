---
layout: taulib-doc
title: "TauLib.BookVI.Source.GeneticCode"
permalink: /verify/taulib/docs/book-vi-source-genetic-code/
lane: verify
module_name: "TauLib.BookVI.Source.GeneticCode"
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

# TauLib.BookVI.Source.GeneticCode


Genetic code: codon structure, central dogma morphism, error minimization.

## Registry Cross-References


- [VI.D40] BSD Motivic Structure of Genetic Code — `BSDGeneticCode`

- [VI.T22] Codon Degeneracy as Error Correction — `codon_error_correction`

- [VI.P15] Central Dogma as Morphism Composition — `central_dogma_morphism`

- [VI.T21] Turing Patterns as Hodge Eigenmodes — `turing_hodge_eigenmodes`

- [VI.P14] Reaction-Diffusion from τ³ Structure — `reaction_diffusion_tau3`


## Cross-Book Authority


- Book III, Part V: BSD force (rank of rational points → code structure)

- Book III, Part IV: Hodge force (Laplacian eigenmodes → morphogenesis)

- Book II, Part II: τ³ = τ¹ ×_f T² (central dogma maps between factors)

- Book II, Ch 116: τ-Hodge Theory (Hodge decomposition on τ³)


## Ground Truth Sources


- Book VI Chapter 26 (2nd Edition): Morphogenesis

- Book VI Chapter 27 (2nd Edition): The Genetic Code


---

### `Tau.BookVI.GeneticCode.BSDGeneticCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L34-L53)
**structure
Tau.BookVI.GeneticCode.BSDGeneticCode :Type**


[VI.D40] BSD Motivic Structure of the Genetic Code.
The 20 standard amino acids and 64 codons reflect
BSD-force structure (Book III, Part V) on the carrier's code space.
Degeneracy pattern = error-correcting code.

- amino_acids : ℕ
Number of standard amino acids.

- aa_eq : self.amino_acids = 20
Exactly 20.

- codons : ℕ
Number of codons.

- codons_eq : self.codons = 64
Exactly 64 = 4³.

- stop_codons : ℕ
Stop codons.

- stop_eq : self.stop_codons = 3
Exactly 3 stop codons.

- bsd_connection : Bool
Connected to BSD force (Book III, Part V).

Instances For

---

### `Tau.BookVI.GeneticCode.instReprBSDGeneticCode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L53-L53)
**instance
Tau.BookVI.GeneticCode.instReprBSDGeneticCode :Repr BSDGeneticCode**

Equations
- Tau.BookVI.GeneticCode.instReprBSDGeneticCode = { reprPrec := Tau.BookVI.GeneticCode.instReprBSDGeneticCode.repr }

---

### `Tau.BookVI.GeneticCode.instReprBSDGeneticCode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L53-L53)
**def
Tau.BookVI.GeneticCode.instReprBSDGeneticCode.repr :BSDGeneticCode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.genetic_code`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L55-L61)
**def
Tau.BookVI.GeneticCode.genetic_code :BSDGeneticCode**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.genetic_code_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L63-L67)
**theorem
Tau.BookVI.GeneticCode.genetic_code_structure :genetic_code.amino_acids = 20 ∧ genetic_code.codons = 64 ∧ genetic_code.stop_codons = 3**


---

### `Tau.BookVI.GeneticCode.CodonErrorCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L73-L88)
**structure
Tau.BookVI.GeneticCode.CodonErrorCorrection :Type**


[VI.T22] Codon Degeneracy as Error Correction Theorem.
Standard code in top 0.01% for error minimization (Freeland-Hurst).
Redundancy: 1.68 bits/codon (log₂(64/20) ≈ 1.68).
Established result from information theory + computational biology.

- percentile_rank_x100 : ℕ
Percentile rank for error minimization.

- rank_eq : self.percentile_rank_x100 = 9999
Top 0.01% → 9999 out of 10000.

- redundancy_x100 : ℕ
Redundancy in bits/codon (×100 for integer).

- redundancy_eq : self.redundancy_x100 = 168
1.68 bits → 168.

- scope : String
Scope: established (Shannon + Freeland-Hurst).

Instances For

---

### `Tau.BookVI.GeneticCode.instReprCodonErrorCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L88-L88)
**instance
Tau.BookVI.GeneticCode.instReprCodonErrorCorrection :Repr CodonErrorCorrection**

Equations
- Tau.BookVI.GeneticCode.instReprCodonErrorCorrection = { reprPrec := Tau.BookVI.GeneticCode.instReprCodonErrorCorrection.repr }

---

### `Tau.BookVI.GeneticCode.instReprCodonErrorCorrection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L88-L88)
**def
Tau.BookVI.GeneticCode.instReprCodonErrorCorrection.repr :CodonErrorCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.codon_err`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L90-L94)
**def
Tau.BookVI.GeneticCode.codon_err :CodonErrorCorrection**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.codon_error_correction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L96-L99)
**theorem
Tau.BookVI.GeneticCode.codon_error_correction :codon_err.percentile_rank_x100 = 9999 ∧ codon_err.redundancy_x100 = 168**


---

### `Tau.BookVI.GeneticCode.CentralDogmaMorphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L105-L120)
**structure
Tau.BookVI.GeneticCode.CentralDogmaMorphism :Type**


[VI.P15] Central Dogma as Morphism Composition.
DNA → mRNA → Protein maps between τ³ factors:
τ¹_DNA → (τ¹ × T²)_mRNA → T²_Protein.
Authority: Book II, Part II (τ³ = τ¹ ×_f T² factor structure).

- steps : ℕ
Number of morphism steps.

- steps_eq : self.steps = 2
Exactly 2 steps (transcription + translation).

- source_factor : String
Source factor: τ¹ (DNA, temporal/base).

- intermediate : String
Intermediate: τ¹ × T² (mRNA, mixed).

- target_factor : String
Target factor: T² (Protein, fiber/spatial).

Instances For

---

### `Tau.BookVI.GeneticCode.instReprCentralDogmaMorphism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L120-L120)
**def
Tau.BookVI.GeneticCode.instReprCentralDogmaMorphism.repr :CentralDogmaMorphism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.instReprCentralDogmaMorphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L120-L120)
**instance
Tau.BookVI.GeneticCode.instReprCentralDogmaMorphism :Repr CentralDogmaMorphism**

Equations
- Tau.BookVI.GeneticCode.instReprCentralDogmaMorphism = { reprPrec := Tau.BookVI.GeneticCode.instReprCentralDogmaMorphism.repr }

---

### `Tau.BookVI.GeneticCode.central_dogma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L122-L124)
**def
Tau.BookVI.GeneticCode.central_dogma :CentralDogmaMorphism**

Equations
- Tau.BookVI.GeneticCode.central_dogma = { steps := 2, steps_eq := Tau.BookVI.GeneticCode.central_dogma._proof_1 }
Instances For

---

### `Tau.BookVI.GeneticCode.central_dogma_morphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L126-L130)
**theorem
Tau.BookVI.GeneticCode.central_dogma_morphism :central_dogma.steps = 2 ∧ central_dogma.source_factor = "tau1_DNA" ∧ central_dogma.target_factor = "T2_Protein"**


---

### `Tau.BookVI.GeneticCode.TuringHodgeEigenmodes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L136-L149)
**structure
Tau.BookVI.GeneticCode.TuringHodgeEigenmodes :Type**


[VI.T21] Turing Patterns as Hodge Eigenmode Instantiations.
Morphogenetic patterns = eigenfunctions of the Hodge Laplacian Δ_H.
Reaction from τ¹ base, diffusion from T² fiber.
Authority: Book III, Part IV (Hodge force); Book II, Ch 116 (τ-Hodge).

- reaction_source : String
Reaction source: τ¹ (base, temporal).

- diffusion_domain : String
Diffusion domain: T² (fiber, spatial).

- hodge_laplacian : Bool
Governed by Hodge Laplacian Δ_H.

- scope : String
Scope: τ-effective.

Instances For

---

### `Tau.BookVI.GeneticCode.instReprTuringHodgeEigenmodes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L149-L149)
**instance
Tau.BookVI.GeneticCode.instReprTuringHodgeEigenmodes :Repr TuringHodgeEigenmodes**

Equations
- Tau.BookVI.GeneticCode.instReprTuringHodgeEigenmodes = { reprPrec := Tau.BookVI.GeneticCode.instReprTuringHodgeEigenmodes.repr }

---

### `Tau.BookVI.GeneticCode.instReprTuringHodgeEigenmodes.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L149-L149)
**def
Tau.BookVI.GeneticCode.instReprTuringHodgeEigenmodes.repr :TuringHodgeEigenmodes → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.turing_hodge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L151-L151)
**def
Tau.BookVI.GeneticCode.turing_hodge :TuringHodgeEigenmodes**

Equations
- Tau.BookVI.GeneticCode.turing_hodge = { }
Instances For

---

### `Tau.BookVI.GeneticCode.turing_hodge_eigenmodes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L153-L157)
**theorem
Tau.BookVI.GeneticCode.turing_hodge_eigenmodes :turing_hodge.hodge_laplacian = true ∧ turing_hodge.reaction_source = "tau1_base" ∧ turing_hodge.diffusion_domain = "T2_fiber"**


---

### `Tau.BookVI.GeneticCode.ReactionDiffusionTau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L163-L174)
**structure
Tau.BookVI.GeneticCode.ReactionDiffusionTau3 :Type**


[VI.P14] Reaction-Diffusion from τ³ Structure.
The fibered product τ³ = τ¹ ×_f T² naturally separates
reaction (temporal, base) from diffusion (spatial, fiber).
Authority: Book II, Part II (τ³ fibration).

- reaction_is_base : Bool
Reaction = base dynamics.

- diffusion_is_fiber : Bool
Diffusion = fiber dynamics.

- tau3_separated : Bool
Natural separation from τ³ structure.

Instances For

---

### `Tau.BookVI.GeneticCode.instReprReactionDiffusionTau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L174-L174)
**instance
Tau.BookVI.GeneticCode.instReprReactionDiffusionTau3 :Repr ReactionDiffusionTau3**

Equations
- Tau.BookVI.GeneticCode.instReprReactionDiffusionTau3 = { reprPrec := Tau.BookVI.GeneticCode.instReprReactionDiffusionTau3.repr }

---

### `Tau.BookVI.GeneticCode.instReprReactionDiffusionTau3.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L174-L174)
**def
Tau.BookVI.GeneticCode.instReprReactionDiffusionTau3.repr :ReactionDiffusionTau3 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.GeneticCode.rxn_diff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L176-L176)
**def
Tau.BookVI.GeneticCode.rxn_diff :ReactionDiffusionTau3**

Equations
- Tau.BookVI.GeneticCode.rxn_diff = { }
Instances For

---

### `Tau.BookVI.GeneticCode.reaction_diffusion_tau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Source/GeneticCode.lean#L178-L182)
**theorem
Tau.BookVI.GeneticCode.reaction_diffusion_tau3 :rxn_diff.reaction_is_base = true ∧ rxn_diff.diffusion_is_fiber = true ∧ rxn_diff.tau3_separated = true**
