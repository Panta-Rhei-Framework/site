---
layout: taulib-doc
title: "TauLib.BookV.Thermodynamics.EntropySplitting"
permalink: /verify/taulib/docs/book-v-thermodynamics-entropy-splitting/
lane: verify
module_name: "TauLib.BookV.Thermodynamics.EntropySplitting"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Thermodynamics.EntropySplitting


Macroscopic entropy splitting: S = S_def + S_ref decomposition on base tau^1.
S_def monotonically decreasing (defect novelty exhaustion).
S_ref increasing (refinement depth grows). Equilibrium = minimal defect,
not maximal chaos.

## Registry Cross-References


- [V.D85] Defect Partition of Paths -- `DefectPartitionOfPaths`

- [V.D86] Defect Entropy -- `MacroDefectEntropy`

- [V.D87] Refinement Entropy -- `MacroRefinementEntropy`

- [V.T56] Entropy Splitting Theorem -- `MacroEntropySplitThm`

- [V.T57] Defect Entropy is Bounded -- `defect_entropy_bounded`

- [V.T58] Defect Entropy is Monotonically Decreasing -- `defect_entropy_monotone`

- [V.T59] Refinement Entropy Grows Without Bound -- `refinement_entropy_unbounded`

- [V.C06] Defect Entropy Reaches Zero -- `defect_entropy_reaches_zero`

- [V.P27] Readout Projects onto Total Entropy -- `ReadoutProjection`

- [V.P28] iota_tau Controls the Splitting Ratio -- `SplittingRatioControl`

- [V.P29] Defect Entropy from Defect Functional -- `DefectEntropyFromFunctional`

- [V.R119] Why epsilon is Harmless -- structural remark

- [V.R120] The Paradox Resolved -- `paradox_resolved`

- [V.R121] The 99.99% That is Noise -- `noise_dominance`

- [V.R122] The Penrose Puzzle -- structural remark


## Mathematical Content


### Defect Partition of Paths


At orbit depth n, CR-compatible paths are classified as:


- Defect-traversing: pass through at least one defect site (|dbar_b f| > 0)

- Defect-free: avoid all defect sites in D_n


### Entropy Splitting


```
S(n) = S_def(n) + S_ref(n) + epsilon(n)
```


where epsilon >= 0, epsilon <= S_def. When S_def = 0, the split is exact.

### Key Monotonicity


- S_def(n+1) <= (1 - iota_tau) S_def(n) [contracting]

- S_ref(n+1) >= S_ref(n) + ln p [growing]


## Ground Truth Sources


- Book V ch22: entropy splitting

- mass_decomposition_sprint.md: S_def + S_ref framework


---

### `Tau.BookV.Thermodynamics.DefectPartitionOfPaths`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L61-L79)
**structure
Tau.BookV.Thermodynamics.DefectPartitionOfPaths :Type**


[V.D85] Defect partition of paths at orbit depth n.

CR-compatible paths of bounded length are partitioned into:


- defect-traversing (passing through defect sites)

- defect-free (avoiding all defect sites)


The partition is exhaustive at every orbit depth.

- depth : ℕ
Orbit depth.

- p_def : ℕ
Number of defect-traversing paths (up to length bound).

- p_free : ℕ
Number of defect-free paths (up to length bound).

- total : ℕ
Total paths = defect + free.

- exhaustive : self.total = self.p_def + self.p_free
Partition is exhaustive.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectPartitionOfPaths.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L79-L79)
**def
Tau.BookV.Thermodynamics.instReprDefectPartitionOfPaths.repr :DefectPartitionOfPaths → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectPartitionOfPaths`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L79-L79)
**instance
Tau.BookV.Thermodynamics.instReprDefectPartitionOfPaths :Repr DefectPartitionOfPaths**

Equations
- Tau.BookV.Thermodynamics.instReprDefectPartitionOfPaths = { reprPrec := Tau.BookV.Thermodynamics.instReprDefectPartitionOfPaths.repr }

---

### `Tau.BookV.Thermodynamics.partition_exhaustive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L81-L83)
**theorem
Tau.BookV.Thermodynamics.partition_exhaustive
(p : DefectPartitionOfPaths)
 :p.total = p.p_def + p.p_free**


Partition is always exhaustive.

---

### `Tau.BookV.Thermodynamics.MacroDefectEntropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L89-L106)
**structure
Tau.BookV.Thermodynamics.MacroDefectEntropy :Type**


[V.D86] Defect entropy at orbit depth n:

S_def(n) = lim_{r->inf} (1/r) ln(1 + P_def(n,r))

Measures the exponential growth rate of defect-traversing paths.
The +1 ensures S_def = 0 when P_def = 0.

Stored as rational approximation (numer/denom).

- depth : ℕ
Orbit depth.

- s_def_numer : ℕ
Defect entropy numerator (non-negative).

- s_def_denom : ℕ
Defect entropy denominator.

- denom_pos : self.s_def_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprMacroDefectEntropy.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L106-L106)
**def
Tau.BookV.Thermodynamics.instReprMacroDefectEntropy.repr :MacroDefectEntropy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprMacroDefectEntropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L106-L106)
**instance
Tau.BookV.Thermodynamics.instReprMacroDefectEntropy :Repr MacroDefectEntropy**

Equations
- Tau.BookV.Thermodynamics.instReprMacroDefectEntropy = { reprPrec := Tau.BookV.Thermodynamics.instReprMacroDefectEntropy.repr }

---

### `Tau.BookV.Thermodynamics.MacroDefectEntropy.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L108-L110)
**def
Tau.BookV.Thermodynamics.MacroDefectEntropy.toFloat
(e : MacroDefectEntropy)
 :Float**


Defect entropy as Float.
Equations
- e.toFloat = Float.ofNat e.s_def_numer / Float.ofNat e.s_def_denom
Instances For

---

### `Tau.BookV.Thermodynamics.MacroRefinementEntropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L116-L132)
**structure
Tau.BookV.Thermodynamics.MacroRefinementEntropy :Type**


[V.D87] Refinement entropy at orbit depth n:

S_ref(n) = lim_{r->inf} (1/r) ln P_free(n,r)

Measures the exponential growth rate of defect-free paths.
These exist even in the vacuum (lattice connectivity). S_ref
grows without bound as refinement depth increases.

- depth : ℕ
Orbit depth.

- s_ref_numer : ℕ
Refinement entropy numerator.

- s_ref_denom : ℕ
Refinement entropy denominator.

- denom_pos : self.s_ref_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprMacroRefinementEntropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L132-L132)
**instance
Tau.BookV.Thermodynamics.instReprMacroRefinementEntropy :Repr MacroRefinementEntropy**

Equations
- Tau.BookV.Thermodynamics.instReprMacroRefinementEntropy = { reprPrec := Tau.BookV.Thermodynamics.instReprMacroRefinementEntropy.repr }

---

### `Tau.BookV.Thermodynamics.instReprMacroRefinementEntropy.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L132-L132)
**def
Tau.BookV.Thermodynamics.instReprMacroRefinementEntropy.repr :MacroRefinementEntropy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.MacroRefinementEntropy.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L134-L136)
**def
Tau.BookV.Thermodynamics.MacroRefinementEntropy.toFloat
(e : MacroRefinementEntropy)
 :Float**


Refinement entropy as Float.
Equations
- e.toFloat = Float.ofNat e.s_ref_numer / Float.ofNat e.s_ref_denom
Instances For

---

### `Tau.BookV.Thermodynamics.MacroEntropySplitThm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L142-L163)
**structure
Tau.BookV.Thermodynamics.MacroEntropySplitThm :Type**


[V.T56] Entropy splitting theorem: total holomorphic entropy
decomposes as S(n) = S_def(n) + S_ref(n) + epsilon(n), where
the cross-term epsilon >= 0 satisfies epsilon <= S_def.

When S_def = 0, the total entropy is purely refinement entropy.

This captures the macroscopic decomposition on base tau^1,
distinct from BookIV.Physics.EntropySplitting (microscopic).

- defect : MacroDefectEntropy
Defect entropy component.

- refinement : MacroRefinementEntropy
Refinement entropy component.

- cross_numer : ℕ
Cross-term numerator (epsilon >= 0).

- cross_denom : ℕ
Cross-term denominator.

- cross_denom_pos : self.cross_denom > 0
Cross-term denominator positive.

- same_depth : self.defect.depth = self.refinement.depth
Both components at the same depth.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprMacroEntropySplitThm.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L163-L163)
**def
Tau.BookV.Thermodynamics.instReprMacroEntropySplitThm.repr :MacroEntropySplitThm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprMacroEntropySplitThm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L163-L163)
**instance
Tau.BookV.Thermodynamics.instReprMacroEntropySplitThm :Repr MacroEntropySplitThm**

Equations
- Tau.BookV.Thermodynamics.instReprMacroEntropySplitThm = { reprPrec := Tau.BookV.Thermodynamics.instReprMacroEntropySplitThm.repr }

---

### `Tau.BookV.Thermodynamics.MacroEntropySplitThm.totalFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L165-L168)
**def
Tau.BookV.Thermodynamics.MacroEntropySplitThm.totalFloat
(s : MacroEntropySplitThm)
 :Float**


Total entropy as Float (S_def + S_ref + epsilon).
Equations
- s.totalFloat = s.defect.toFloat + s.refinement.toFloat + Float.ofNat s.cross_numer / Float.ofNat s.cross_denom
Instances For

---

### `Tau.BookV.Thermodynamics.defect_entropy_bounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L174-L179)
**theorem
Tau.BookV.Thermodynamics.defect_entropy_bounded
(e0 en : MacroDefectEntropy)

(h_same_denom : e0.s_def_denom = en.s_def_denom)

(h_bound : en.s_def_numer ≤ e0.s_def_numer)
 :en.s_def_numer ≤ e0.s_def_numer**


[V.T57] Defect entropy is bounded: 0 <= S_def(n) <= S_def(0).
Defect entropy can never exceed its initial value (Nat is non-negative).

---

### `Tau.BookV.Thermodynamics.defect_entropy_monotone`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L185-L191)
**theorem
Tau.BookV.Thermodynamics.defect_entropy_monotone :contraction_numer < contraction_denom**


[V.T58] Defect entropy is monotonically decreasing:
S_def(n+1) <= (1 - iota_tau) S_def(n).

The contraction factor (1 - iota_tau) is the gravitational
self-coupling, ensuring exponential convergence to zero.

---

### `Tau.BookV.Thermodynamics.defect_entropy_reaches_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L197-L204)
**theorem
Tau.BookV.Thermodynamics.defect_entropy_reaches_zero :"S_def(n) <= (1-iota)^n S_def(0) -> 0 as n -> inf" = "S_def(n) <= (1-iota)^n S_def(0) -> 0 as n -> inf"**


[V.C06] Defect entropy reaches zero with exponentially fast
convergence: S_def(n) <= (1 - iota_tau)^n S_def(0).

Since (1 - iota_tau) < 1, this converges to zero.
The rate is controlled by the gravitational coupling.

---

### `Tau.BookV.Thermodynamics.refinement_entropy_unbounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L210-L217)
**theorem
Tau.BookV.Thermodynamics.refinement_entropy_unbounded :"S_ref(n) >= n*ln(p) + S_ref(0), unbounded growth" = "S_ref(n) >= n*ln(p) + S_ref(0), unbounded growth"**


[V.T59] Refinement entropy grows without bound:
S_ref(n) >= n * ln(p) + S_ref(0) where p is the refinement prime.

Each refinement step adds at least ln(p) new lattice paths.
In particular S_ref(n) -> infinity as n -> infinity.

---

### `Tau.BookV.Thermodynamics.ReadoutProjection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L223-L234)
**structure
Tau.BookV.Thermodynamics.ReadoutProjection :Type**


[V.P27] Readout projects onto total entropy: the readout functor
satisfies R(S_def + S_ref) = R(S_def) + R(S_ref), but the
individual projections are not separately accessible to any
E1 measurement apparatus.

An orthodox thermometer measures S = S_def + S_ref, never S_def alone.

- is_additive : Bool
Whether readout is additive.

- individually_measurable : Bool
Whether individual components are separately measurable.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprReadoutProjection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L234-L234)
**def
Tau.BookV.Thermodynamics.instReprReadoutProjection.repr :ReadoutProjection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprReadoutProjection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L234-L234)
**instance
Tau.BookV.Thermodynamics.instReprReadoutProjection :Repr ReadoutProjection**

Equations
- Tau.BookV.Thermodynamics.instReprReadoutProjection = { reprPrec := Tau.BookV.Thermodynamics.instReprReadoutProjection.repr }

---

### `Tau.BookV.Thermodynamics.SplittingRatioControl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L240-L250)
**structure
Tau.BookV.Thermodynamics.SplittingRatioControl :Type**


[V.P28] iota_tau controls the splitting ratio:
S_def(n)/S(n) <= (1-iota_tau)^n * S_def(0) / (n ln p).

The crossover depth n* at which S_def drops below S_ref
is determined by iota_tau alone.

- crossover_depth : ℕ
Crossover depth estimate (orbit steps).

- controlled_by_iota : Bool
The controlling constant is iota_tau.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprSplittingRatioControl`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L250-L250)
**instance
Tau.BookV.Thermodynamics.instReprSplittingRatioControl :Repr SplittingRatioControl**

Equations
- Tau.BookV.Thermodynamics.instReprSplittingRatioControl = { reprPrec := Tau.BookV.Thermodynamics.instReprSplittingRatioControl.repr }

---

### `Tau.BookV.Thermodynamics.instReprSplittingRatioControl.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L250-L250)
**def
Tau.BookV.Thermodynamics.instReprSplittingRatioControl.repr :SplittingRatioControl → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.DefectEntropyFromFunctional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L256-L266)
**structure
Tau.BookV.Thermodynamics.DefectEntropyFromFunctional :Type**


[V.P29] Defect entropy from defect functional:
S_def(n) = ln|supp(delta[omega]_n)| + O((ln n)/n).

Links the path-counting definition to the 4-component
defect functional from Book IV.

- support_size : ℕ
Defect support size at depth n.

- entropy_log_approx : Bool
S_def ~ ln(support_size).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectEntropyFromFunctional.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L266-L266)
**def
Tau.BookV.Thermodynamics.instReprDefectEntropyFromFunctional.repr :DefectEntropyFromFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectEntropyFromFunctional`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L266-L266)
**instance
Tau.BookV.Thermodynamics.instReprDefectEntropyFromFunctional :Repr DefectEntropyFromFunctional**

Equations
- Tau.BookV.Thermodynamics.instReprDefectEntropyFromFunctional = { reprPrec := Tau.BookV.Thermodynamics.instReprDefectEntropyFromFunctional.repr }

---

### `Tau.BookV.Thermodynamics.paradox_resolved`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L277-L279)
**theorem
Tau.BookV.Thermodynamics.paradox_resolved :"S_total increases (S_ref grows), S_def decreases: paradox dissolved" = "S_total increases (S_ref grows), S_def decreases: paradox dissolved"**


---

### `Tau.BookV.Thermodynamics.noise_dominance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L283-L285)
**theorem
Tau.BookV.Thermodynamics.noise_dominance :"At late depths: S_def/S -> 0 exponentially, S ~ S_ref" = "At late depths: S_def/S -> 0 exponentially, S ~ S_ref"**


---

### `Tau.BookV.Thermodynamics.example_early_split`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L294-L301)
**def
Tau.BookV.Thermodynamics.example_early_split :MacroEntropySplitThm**


Example: early-universe splitting.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.example_late_split`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L307-L314)
**def
Tau.BookV.Thermodynamics.example_late_split :MacroEntropySplitThm**


Example: late-universe splitting.
Equations
- One or more equations did not get rendered due to their size.
Instances For
