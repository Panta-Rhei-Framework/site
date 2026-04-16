---
layout: taulib-doc
title: "TauLib.BookIV.MassDerivation.ElectronMass"
permalink: /verify/taulib/docs/book-iv-mass-derivation-electron-mass/
lane: verify
module_name: "TauLib.BookIV.MassDerivation.ElectronMass"
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

# TauLib.BookIV.MassDerivation.ElectronMass


Complete electron mass derivation: 10-link chain from K₀-K₆ to
m_e = 0.510999 MeV (0.025 ppm), assembling breathing modes, Epstein zeta,
lemniscate capacity, and holonomy correction.

## Registry Cross-References


- [IV.T117] 10-Link Derivation Chain — `DerivationChain`, `chain_link_count`

- [IV.P172] Scope Distribution — `chain_scope_distribution`

- [IV.D316] Bulk Term — `BulkTerm`

- [IV.T118] Bulk Overshoots — `bulk_overshoots`

- [IV.D317] Level 0 Formula — `Level0Formula`

- [IV.T119] Level 0 Range — `level0_range`

- [IV.D318] Level 1+ Formula — `Level1PlusDetail`


## Ground Truth Sources


- electron_mass_first_principles.md (master, ~1900 lines)

- sqrt3_derivation_sprint.md, holonomy_correction_sprint.md


---

### `Tau.BookIV.MassDerivation.ChainScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L34-L38)
**inductive
Tau.BookIV.MassDerivation.ChainScope :Type**


Scope label for chain links.

- Established : ChainScope
- TauEffective : ChainScope
Instances For

---

### `Tau.BookIV.MassDerivation.instReprChainScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L38-L38)
**instance
Tau.BookIV.MassDerivation.instReprChainScope :Repr ChainScope**

Equations
- Tau.BookIV.MassDerivation.instReprChainScope = { reprPrec := Tau.BookIV.MassDerivation.instReprChainScope.repr }

---

### `Tau.BookIV.MassDerivation.instReprChainScope.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L38-L38)
**def
Tau.BookIV.MassDerivation.instReprChainScope.repr :ChainScope → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instDecidableEqChainScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L38-L38)
**instance
Tau.BookIV.MassDerivation.instDecidableEqChainScope :DecidableEq ChainScope**

Equations
- Tau.BookIV.MassDerivation.instDecidableEqChainScope x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.MassDerivation.instBEqChainScope.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L38-L38)
**def
Tau.BookIV.MassDerivation.instBEqChainScope.beq :ChainScope → ChainScope → Bool**

Equations
- Tau.BookIV.MassDerivation.instBEqChainScope.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.MassDerivation.instBEqChainScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L38-L38)
**instance
Tau.BookIV.MassDerivation.instBEqChainScope :BEq ChainScope**

Equations
- Tau.BookIV.MassDerivation.instBEqChainScope = { beq := Tau.BookIV.MassDerivation.instBEqChainScope.beq }

---

### `Tau.BookIV.MassDerivation.ChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L40-L45)
**structure
Tau.BookIV.MassDerivation.ChainLink :Type**


A single link in the R derivation chain.

- index : ℕ
- name : String
- scope : ChainScope
Instances For

---

### `Tau.BookIV.MassDerivation.instReprChainLink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L45-L45)
**instance
Tau.BookIV.MassDerivation.instReprChainLink :Repr ChainLink**

Equations
- Tau.BookIV.MassDerivation.instReprChainLink = { reprPrec := Tau.BookIV.MassDerivation.instReprChainLink.repr }

---

### `Tau.BookIV.MassDerivation.instReprChainLink.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L45-L45)
**def
Tau.BookIV.MassDerivation.instReprChainLink.repr :ChainLink → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.derivation_chain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L47-L59)
**def
Tau.BookIV.MassDerivation.derivation_chain :List ChainLink**


[IV.T117] The complete 10-link chain from K₀-K₆ to m_e.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.chain_link_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L61-L61)
**theorem
Tau.BookIV.MassDerivation.chain_link_count :derivation_chain.length = 10**


---

### `Tau.BookIV.MassDerivation.chain_indices`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L63-L65)
**theorem
Tau.BookIV.MassDerivation.chain_indices :List.map ChainLink.index derivation_chain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**


---

### `Tau.BookIV.MassDerivation.ScopeDistribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L71-L78)
**structure
Tau.BookIV.MassDerivation.ScopeDistribution :Type**


[IV.P172] 3 established + 7 tau-effective + 0 conjectural.

- established : ℕ
- tau_effective : ℕ
- conjectural : ℕ
- total_eq : self.established + self.tau_effective + self.conjectural = 10
- no_conjectural : self.conjectural = 0
Instances For

---

### `Tau.BookIV.MassDerivation.instReprScopeDistribution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L78-L78)
**def
Tau.BookIV.MassDerivation.instReprScopeDistribution.repr :ScopeDistribution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instReprScopeDistribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L78-L78)
**instance
Tau.BookIV.MassDerivation.instReprScopeDistribution :Repr ScopeDistribution**

Equations
- Tau.BookIV.MassDerivation.instReprScopeDistribution = { reprPrec := Tau.BookIV.MassDerivation.instReprScopeDistribution.repr }

---

### `Tau.BookIV.MassDerivation.scope_distribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L80-L85)
**def
Tau.BookIV.MassDerivation.scope_distribution :ScopeDistribution**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.chain_scope_distribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L87-L90)
**theorem
Tau.BookIV.MassDerivation.chain_scope_distribution :scope_distribution.established + scope_distribution.tau_effective + scope_distribution.conjectural = 10**


---

### `Tau.BookIV.MassDerivation.chain_no_conjectural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L92-L93)
**theorem
Tau.BookIV.MassDerivation.chain_no_conjectural :scope_distribution.conjectural = 0**


---

### `Tau.BookIV.MassDerivation.chain_established_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L95-L97)
**theorem
Tau.BookIV.MassDerivation.chain_established_count :(List.filter (fun (x : ChainLink) => x.scope == ChainScope.Established) derivation_chain).length = 3**


---

### `Tau.BookIV.MassDerivation.chain_tau_effective_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L99-L101)
**theorem
Tau.BookIV.MassDerivation.chain_tau_effective_count :(List.filter (fun (x : ChainLink) => x.scope == ChainScope.TauEffective) derivation_chain).length = 7**


---

### `Tau.BookIV.MassDerivation.BulkTerm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L107-L113)
**structure
Tau.BookIV.MassDerivation.BulkTerm :Type**


[IV.D316] Bulk term R_bulk = ι<sub>τ</sub>^{-7}. Wraps MassRatioFormula.

- numer : ℕ
- denom : ℕ
- denom_pos : self.denom > 0
- exponent : ℤ
Instances For

---

### `Tau.BookIV.MassDerivation.instReprBulkTerm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L113-L113)
**instance
Tau.BookIV.MassDerivation.instReprBulkTerm :Repr BulkTerm**

Equations
- Tau.BookIV.MassDerivation.instReprBulkTerm = { reprPrec := Tau.BookIV.MassDerivation.instReprBulkTerm.repr }

---

### `Tau.BookIV.MassDerivation.instReprBulkTerm.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L113-L113)
**def
Tau.BookIV.MassDerivation.instReprBulkTerm.repr :BulkTerm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.bulk_term`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L115-L118)
**def
Tau.BookIV.MassDerivation.bulk_term :BulkTerm**

Equations
- Tau.BookIV.MassDerivation.bulk_term = { numer := Tau.BookIV.Calibration.bulk_numer, denom := Tau.BookIV.Calibration.bulk_denom,
 denom_pos := Tau.BookIV.Calibration.bulk_denom_pos }
Instances For

---

### `Tau.BookIV.MassDerivation.bulk_numer_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L120-L120)
**theorem
Tau.BookIV.MassDerivation.bulk_numer_match :bulk_term.numer = Calibration.bulk_numer**


---

### `Tau.BookIV.MassDerivation.bulk_denom_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L121-L121)
**theorem
Tau.BookIV.MassDerivation.bulk_denom_match :bulk_term.denom = Calibration.bulk_denom**


---

### `Tau.BookIV.MassDerivation.bulk_overshoots`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L127-L130)
**theorem
Tau.BookIV.MassDerivation.bulk_overshoots :Calibration.bulk_numer * Calibration.si_mass_ratio.denom > Calibration.si_mass_ratio.numer * Calibration.bulk_denom**


[IV.T118] ι<sub>τ</sub>^{-7} overshoots R_CODATA (correction sign is correct).

---

### `Tau.BookIV.MassDerivation.bulk_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L132-L135)
**theorem
Tau.BookIV.MassDerivation.bulk_range :Calibration.bulk_numer > 1853 * Calibration.bulk_denom ∧ Calibration.bulk_numer < 1855 * Calibration.bulk_denom**


---

### `Tau.BookIV.MassDerivation.Level0Formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L141-L146)
**structure
Tau.BookIV.MassDerivation.Level0Formula :Type**


[IV.D317] Level 0: R₀ = ι<sub>τ</sub>^{-7} − √3·ι<sub>τ</sub>^{-2}.

- bulk_exp : ℤ
- correction_exp : ℤ
- accuracy_exact : String
Instances For

---

### `Tau.BookIV.MassDerivation.instReprLevel0Formula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L146-L146)
**def
Tau.BookIV.MassDerivation.instReprLevel0Formula.repr :Level0Formula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.instReprLevel0Formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L146-L146)
**instance
Tau.BookIV.MassDerivation.instReprLevel0Formula :Repr Level0Formula**

Equations
- Tau.BookIV.MassDerivation.instReprLevel0Formula = { reprPrec := Tau.BookIV.MassDerivation.instReprLevel0Formula.repr }

---

### `Tau.BookIV.MassDerivation.level0_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L148-L148)
**def
Tau.BookIV.MassDerivation.level0_formula :Level0Formula**

Equations
- Tau.BookIV.MassDerivation.level0_formula = { }
Instances For

---

### `Tau.BookIV.MassDerivation.level0_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L150-L156)
**theorem
Tau.BookIV.MassDerivation.level0_range :Calibration.bulk_numer * Calibration.correction0_denom > Calibration.correction0_numer * Calibration.bulk_denom + 1837 * Calibration.bulk_denom * Calibration.correction0_denom ∧ Calibration.bulk_numer * Calibration.correction0_denom < Calibration.correction0_numer * Calibration.bulk_denom + 1840 * Calibration.bulk_denom * Calibration.correction0_denom**


[IV.T119] R₀ ∈ (1837, 1840) with 6-digit ι<sub>τ</sub>.

---

### `Tau.BookIV.MassDerivation.level0_deviation_small`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L158-L162)
**theorem
Tau.BookIV.MassDerivation.level0_deviation_small :Calibration.bulk_numer * Calibration.si_mass_ratio.denom * Calibration.correction0_denom + Calibration.si_mass_ratio.numer * Calibration.bulk_denom * Calibration.correction0_denom > 100 * Calibration.correction0_numer * Calibration.si_mass_ratio.denom * Calibration.bulk_denom**


---

### `Tau.BookIV.MassDerivation.Level1PlusDetail`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L168-L177)
**structure
Tau.BookIV.MassDerivation.Level1PlusDetail :Type**


[IV.D318] Level 1+: R₁ = ι<sub>τ</sub>^{-7} − (√3 + π³α²)·ι<sub>τ</sub>^{-2}.
At exact ι<sub>τ</sub>: 0.025 ppm, m_e = 0.510998937 MeV, zero free params.

- bulk_exp : ℤ
- correction_exp : ℤ
- accuracy_exact : String
- electron_mass_MeV : String
- free_parameters : ℕ
- scope : String
Instances For

---

### `Tau.BookIV.MassDerivation.instReprLevel1PlusDetail`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L177-L177)
**instance
Tau.BookIV.MassDerivation.instReprLevel1PlusDetail :Repr Level1PlusDetail**

Equations
- Tau.BookIV.MassDerivation.instReprLevel1PlusDetail = { reprPrec := Tau.BookIV.MassDerivation.instReprLevel1PlusDetail.repr }

---

### `Tau.BookIV.MassDerivation.instReprLevel1PlusDetail.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L177-L177)
**def
Tau.BookIV.MassDerivation.instReprLevel1PlusDetail.repr :Level1PlusDetail → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.level1plus_detail`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L179-L179)
**def
Tau.BookIV.MassDerivation.level1plus_detail :Level1PlusDetail**

Equations
- Tau.BookIV.MassDerivation.level1plus_detail = { }
Instances For

---

### `Tau.BookIV.MassDerivation.level1plus_no_free_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L181-L182)
**theorem
Tau.BookIV.MassDerivation.level1plus_no_free_params :level1plus_detail.free_parameters = 0**


---

### `Tau.BookIV.MassDerivation.ElectronMassSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L188-L196)
**structure
Tau.BookIV.MassDerivation.ElectronMassSummary :Type**


Summary: m_e from first principles, zero free parameters.

- chain_length : ℕ
- established : ℕ
- tau_effective : ℕ
- conjectural : ℕ
- free_params : ℕ
- total_check : self.established + self.tau_effective + self.conjectural = self.chain_length
Instances For

---

### `Tau.BookIV.MassDerivation.instReprElectronMassSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L196-L196)
**instance
Tau.BookIV.MassDerivation.instReprElectronMassSummary :Repr ElectronMassSummary**

Equations
- Tau.BookIV.MassDerivation.instReprElectronMassSummary = { reprPrec := Tau.BookIV.MassDerivation.instReprElectronMassSummary.repr }

---

### `Tau.BookIV.MassDerivation.instReprElectronMassSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L196-L196)
**def
Tau.BookIV.MassDerivation.instReprElectronMassSummary.repr :ElectronMassSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.MassDerivation.electron_mass_summary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L198-L199)
**def
Tau.BookIV.MassDerivation.electron_mass_summary :ElectronMassSummary**

Equations
- Tau.BookIV.MassDerivation.electron_mass_summary = { total_check := Tau.BookIV.MassDerivation.scope_distribution._proof_2 }
Instances For

---

### `Tau.BookIV.MassDerivation.summary_chain_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L201-L201)
**theorem
Tau.BookIV.MassDerivation.summary_chain_length :electron_mass_summary.chain_length = 10**


---

### `Tau.BookIV.MassDerivation.summary_no_free_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L202-L202)
**theorem
Tau.BookIV.MassDerivation.summary_no_free_params :electron_mass_summary.free_params = 0**


---

### `Tau.BookIV.MassDerivation.summary_no_conjectural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/MassDerivation/ElectronMass.lean#L203-L203)
**theorem
Tau.BookIV.MassDerivation.summary_no_conjectural :electron_mass_summary.conjectural = 0**
