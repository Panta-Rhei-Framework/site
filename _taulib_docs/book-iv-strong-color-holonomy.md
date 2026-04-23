---
layout: taulib-doc
title: "TauLib.BookIV.Strong.ColorHolonomy"
permalink: /verify/taulib/docs/book-iv-strong-color-holonomy/
lane: verify
module_name: "TauLib.BookIV.Strong.ColorHolonomy"
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

# TauLib.BookIV.Strong.ColorHolonomy


Color charge from eta-circle holonomy: ternary structure from depth-3,
SU(3) gauge algebra, gluon self-interaction, Wilson loops.

## Registry Cross-References


- [IV.D154] Color Charge — `ColorCharge`

- [IV.D155] Anticolor — `Anticolor`

- [IV.D156] Color Neutrality — `ColorNeutrality`

- [IV.D157] Wilson Loop — `WilsonLoopDef`

- [IV.P88] Ternary Decomposition of the Circle — `ternary_decomposition`

- [IV.P89] Color Quantization — `color_quantization`

- [IV.P90] Color-charged modes — `color_charged_criterion`

- [IV.P91] Dominance Forces Noncommutativity — `dominance_noncommutativity`

- [IV.P92] Tracelessness from Color-neutral Vacuum — `tracelessness`

- [IV.P93] Gluon Self-interaction — `gluon_self_interaction`

- [IV.T69] SU(3) Gauge Algebra — `su3_gauge_algebra`

- [IV.T70] Color Number Theorem — `color_number_theorem`

- [IV.R53-R60] Structural remarks (comment-only)


## Mathematical Content


At primorial depth 3, winding classes on the eta-circle decompose into
exactly three equivalence classes mod 3 (color charges). The gauge algebra
is forced to be su(3) by chi_minus dominance (non-abelian), depth-3
(three colors, rank 2), and color-neutral vacuum (traceless generators).

## Ground Truth Sources


- Chapter 38 of Book IV (2nd Edition)


---

### `Tau.BookIV.Strong.TernaryDecomposition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L45-L55)
**structure
Tau.BookIV.Strong.TernaryDecomposition :Type**


[IV.P88] At primorial depth 3, winding classes on the eta-circle
decompose into exactly three equivalence classes modulo the strong
vacuum normalization: color(n) = n mod 3 in {0, 1, 2}.

- num_classes : ℕ
Number of color classes.

- depth : ℕ
Primorial depth that forces ternary structure.

- classification : String
The classification is mod-3 reduction of eta-winding.

Instances For

---

### `Tau.BookIV.Strong.instReprTernaryDecomposition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L55-L55)
**instance
Tau.BookIV.Strong.instReprTernaryDecomposition :Repr TernaryDecomposition**

Equations
- Tau.BookIV.Strong.instReprTernaryDecomposition = { reprPrec := Tau.BookIV.Strong.instReprTernaryDecomposition.repr }

---

### `Tau.BookIV.Strong.instReprTernaryDecomposition.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L55-L55)
**def
Tau.BookIV.Strong.instReprTernaryDecomposition.repr :TernaryDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.ternary_decomposition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L57-L57)
**def
Tau.BookIV.Strong.ternary_decomposition :TernaryDecomposition**

Equations
- Tau.BookIV.Strong.ternary_decomposition = { }
Instances For

---

### `Tau.BookIV.Strong.three_color_classes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L59-L60)
**theorem
Tau.BookIV.Strong.three_color_classes :ternary_decomposition.num_classes = 3**


---

### `Tau.BookIV.Strong.depth_forces_ternary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L62-L63)
**theorem
Tau.BookIV.Strong.depth_forces_ternary :ternary_decomposition.depth = 3**


---

### `Tau.BookIV.Strong.ColorClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L69-L74)
**inductive
Tau.BookIV.Strong.ColorClass :Type**


Color class labels: red (0), green (1), blue (2) in Z/3Z.

- red : ColorClass
- green : ColorClass
- blue : ColorClass
Instances For

---

### `Tau.BookIV.Strong.instReprColorClass.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**def
Tau.BookIV.Strong.instReprColorClass.repr :ColorClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprColorClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**instance
Tau.BookIV.Strong.instReprColorClass :Repr ColorClass**

Equations
- Tau.BookIV.Strong.instReprColorClass = { reprPrec := Tau.BookIV.Strong.instReprColorClass.repr }

---

### `Tau.BookIV.Strong.instDecidableEqColorClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**instance
Tau.BookIV.Strong.instDecidableEqColorClass :DecidableEq ColorClass**

Equations
- Tau.BookIV.Strong.instDecidableEqColorClass x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Strong.instBEqColorClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**instance
Tau.BookIV.Strong.instBEqColorClass :BEq ColorClass**

Equations
- Tau.BookIV.Strong.instBEqColorClass = { beq := Tau.BookIV.Strong.instBEqColorClass.beq }

---

### `Tau.BookIV.Strong.instBEqColorClass.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**def
Tau.BookIV.Strong.instBEqColorClass.beq :ColorClass → ColorClass → Bool**

Equations
- Tau.BookIV.Strong.instBEqColorClass.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Strong.instInhabitedColorClass.default`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**def
Tau.BookIV.Strong.instInhabitedColorClass.default :ColorClass**

Equations
- Tau.BookIV.Strong.instInhabitedColorClass.default = Tau.BookIV.Strong.ColorClass.red
Instances For

---

### `Tau.BookIV.Strong.instInhabitedColorClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L74-L74)
**instance
Tau.BookIV.Strong.instInhabitedColorClass :Inhabited ColorClass**

Equations
- Tau.BookIV.Strong.instInhabitedColorClass = { default := Tau.BookIV.Strong.instInhabitedColorClass.default }

---

### `Tau.BookIV.Strong.ColorCharge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L76-L84)
**structure
Tau.BookIV.Strong.ColorCharge :Type**


[IV.D154] Color charge of a character mode chi_{m,n} on T^2:
the holonomy class c(chi_{m,n}) := n mod 3, determined by
the eta-winding number n.

- color : ColorClass
Eta-winding number mod 3.

- source : String
Source: eta-circle holonomy at depth 3.

Instances For

---

### `Tau.BookIV.Strong.instReprColorCharge.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L84-L84)
**def
Tau.BookIV.Strong.instReprColorCharge.repr :ColorCharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprColorCharge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L84-L84)
**instance
Tau.BookIV.Strong.instReprColorCharge :Repr ColorCharge**

Equations
- Tau.BookIV.Strong.instReprColorCharge = { reprPrec := Tau.BookIV.Strong.instReprColorCharge.repr }

---

### `Tau.BookIV.Strong.winding_to_color`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L86-L91)
**def
Tau.BookIV.Strong.winding_to_color
(n : ℕ)
 :ColorClass**


Map a natural number eta-winding to its color class.
Equations
- Tau.BookIV.Strong.winding_to_color n = match n % 3 with
 | 0 => Tau.BookIV.Strong.ColorClass.red
 | 1 => Tau.BookIV.Strong.ColorClass.green
 | x => Tau.BookIV.Strong.ColorClass.blue
Instances For

---

### `Tau.BookIV.Strong.winding_0_is_red`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L93-L93)
**theorem
Tau.BookIV.Strong.winding_0_is_red :winding_to_color 0 = ColorClass.red**


---

### `Tau.BookIV.Strong.winding_1_is_green`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L94-L94)
**theorem
Tau.BookIV.Strong.winding_1_is_green :winding_to_color 1 = ColorClass.green**


---

### `Tau.BookIV.Strong.winding_2_is_blue`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L95-L95)
**theorem
Tau.BookIV.Strong.winding_2_is_blue :winding_to_color 2 = ColorClass.blue**


---

### `Tau.BookIV.Strong.winding_3_is_red`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L96-L96)
**theorem
Tau.BookIV.Strong.winding_3_is_red :winding_to_color 3 = ColorClass.red**


---

### `Tau.BookIV.Strong.winding_6_is_red`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L97-L97)
**theorem
Tau.BookIV.Strong.winding_6_is_red :winding_to_color 6 = ColorClass.red**


---

### `Tau.BookIV.Strong.anticolor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L103-L109)
**def
Tau.BookIV.Strong.anticolor
(c : ColorClass)
 :ColorClass**


[IV.D155] Anticolor: the conjugate class c_bar := (3-c) mod 3.
Anti-red = red, anti-green = blue, anti-blue = green.
Equations
- Tau.BookIV.Strong.anticolor Tau.BookIV.Strong.ColorClass.red = Tau.BookIV.Strong.ColorClass.red
- Tau.BookIV.Strong.anticolor Tau.BookIV.Strong.ColorClass.green = Tau.BookIV.Strong.ColorClass.blue
- Tau.BookIV.Strong.anticolor Tau.BookIV.Strong.ColorClass.blue = Tau.BookIV.Strong.ColorClass.green
Instances For

---

### `Tau.BookIV.Strong.anticolor_involution`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L111-L114)
**theorem
Tau.BookIV.Strong.anticolor_involution
(c : ColorClass)
 :anticolor (anticolor c) = c**


Anticolor is an involution.

---

### `Tau.BookIV.Strong.red_self_conjugate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L116-L117)
**theorem
Tau.BookIV.Strong.red_self_conjugate :anticolor ColorClass.red = ColorClass.red**


Red is self-conjugate (the singlet class).

---

### `Tau.BookIV.Strong.ColorNeutrality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L123-L130)
**structure
Tau.BookIV.Strong.ColorNeutrality :Type**


[IV.D156] Color-neutral (color singlet): total eta-holonomy is
trivial, i.e., sum of eta-winding numbers is 0 mod 3.

- total_mod3 : ℕ
Total winding sum mod 3.

- is_singlet : Bool
Singlet condition.

Instances For

---

### `Tau.BookIV.Strong.instReprColorNeutrality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L130-L130)
**instance
Tau.BookIV.Strong.instReprColorNeutrality :Repr ColorNeutrality**

Equations
- Tau.BookIV.Strong.instReprColorNeutrality = { reprPrec := Tau.BookIV.Strong.instReprColorNeutrality.repr }

---

### `Tau.BookIV.Strong.instReprColorNeutrality.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L130-L130)
**def
Tau.BookIV.Strong.instReprColorNeutrality.repr :ColorNeutrality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.is_color_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L132-L134)
**def
Tau.BookIV.Strong.is_color_singlet
(windings : List ℕ)
 :Bool**


Check whether a list of winding numbers forms a color singlet.
Equations
- Tau.BookIV.Strong.is_color_singlet windings = (List.foldl (fun (x1 x2 : ℕ) => x1 + x2) 0 windings % 3 == 0)
Instances For

---

### `Tau.BookIV.Strong.empty_is_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L136-L136)
**theorem
Tau.BookIV.Strong.empty_is_singlet :is_color_singlet [] = true**


---

### `Tau.BookIV.Strong.baryon_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L137-L137)
**theorem
Tau.BookIV.Strong.baryon_singlet :is_color_singlet [0, 1, 2] = true**


---

### `Tau.BookIV.Strong.meson_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L138-L138)
**theorem
Tau.BookIV.Strong.meson_singlet :is_color_singlet [1, 2] = true**


---

### `Tau.BookIV.Strong.ColorQuantization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L144-L153)
**structure
Tau.BookIV.Strong.ColorQuantization :Type**


[IV.P89] Color charge is quantized: takes values in the discrete
group Z/3Z because the compact eta-circle has discrete pi_1 = Z.

- group : String
Group structure: Z/3Z.

- discrete : Bool
Discrete (not continuous).

- source : String
Source: pi_1(S^1) = Z, then mod-3 projection.

Instances For

---

### `Tau.BookIV.Strong.instReprColorQuantization.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L153-L153)
**def
Tau.BookIV.Strong.instReprColorQuantization.repr :ColorQuantization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprColorQuantization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L153-L153)
**instance
Tau.BookIV.Strong.instReprColorQuantization :Repr ColorQuantization**

Equations
- Tau.BookIV.Strong.instReprColorQuantization = { reprPrec := Tau.BookIV.Strong.instReprColorQuantization.repr }

---

### `Tau.BookIV.Strong.color_quantization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L155-L155)
**def
Tau.BookIV.Strong.color_quantization :ColorQuantization**

Equations
- Tau.BookIV.Strong.color_quantization = { }
Instances For

---

### `Tau.BookIV.Strong.is_color_charged`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L161-L163)
**def
Tau.BookIV.Strong.is_color_charged
(eta_winding : ℕ)
 :Bool**


[IV.P90] A mode carries nontrivial color iff n not equiv 0 mod 3.
Equations
- Tau.BookIV.Strong.is_color_charged eta_winding = (eta_winding % 3 != 0)
Instances For

---

### `Tau.BookIV.Strong.color_charged_criterion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L165-L166)
**def
Tau.BookIV.Strong.color_charged_criterion :String**

Equations
- Tau.BookIV.Strong.color_charged_criterion = "chi_{m,n} has nontrivial color iff n not equiv 0 mod 3"
Instances For

---

### `Tau.BookIV.Strong.zero_winding_neutral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L168-L168)
**theorem
Tau.BookIV.Strong.zero_winding_neutral :is_color_charged 0 = false**


---

### `Tau.BookIV.Strong.one_winding_charged`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L169-L169)
**theorem
Tau.BookIV.Strong.one_winding_charged :is_color_charged 1 = true**


---

### `Tau.BookIV.Strong.three_winding_neutral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L170-L170)
**theorem
Tau.BookIV.Strong.three_winding_neutral :is_color_charged 3 = false**


---

### `Tau.BookIV.Strong.DominanceNoncommutativity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L176-L185)
**structure
Tau.BookIV.Strong.DominanceNoncommutativity :Type**


[IV.P91] Chi_minus-dominant sector has non-commutative endomorphism
algebra, forcing a non-abelian gauge group.

- chi_minus_implies_nonabelian : Bool
Chi_minus dominance implies non-abelian.

- polarity_negation : Bool
The polarity involution acts as negation on the dominant lobe.

- gauge_nonabelian : Bool
Resulting gauge group is non-abelian.

Instances For

---

### `Tau.BookIV.Strong.instReprDominanceNoncommutativity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L185-L185)
**instance
Tau.BookIV.Strong.instReprDominanceNoncommutativity :Repr DominanceNoncommutativity**

Equations
- Tau.BookIV.Strong.instReprDominanceNoncommutativity = { reprPrec := Tau.BookIV.Strong.instReprDominanceNoncommutativity.repr }

---

### `Tau.BookIV.Strong.instReprDominanceNoncommutativity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L185-L185)
**def
Tau.BookIV.Strong.instReprDominanceNoncommutativity.repr :DominanceNoncommutativity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.dominance_noncommutativity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L187-L187)
**def
Tau.BookIV.Strong.dominance_noncommutativity :DominanceNoncommutativity**

Equations
- Tau.BookIV.Strong.dominance_noncommutativity = { }
Instances For

---

### `Tau.BookIV.Strong.Tracelessness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L193-L202)
**structure
Tau.BookIV.Strong.Tracelessness :Type**


[IV.P92] The strong vacuum is color-neutral (total holonomy 0 mod 3),
so only det U = 1 transformations preserve it: U(3) -> SU(3).

- vacuum_neutral : Bool
Vacuum is color-neutral.

- traceless : Bool
Tracelessness condition: det = 1.

- u3_to_su3 : Bool
Reduces U(3) to SU(3).

Instances For

---

### `Tau.BookIV.Strong.instReprTracelessness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L202-L202)
**instance
Tau.BookIV.Strong.instReprTracelessness :Repr Tracelessness**

Equations
- Tau.BookIV.Strong.instReprTracelessness = { reprPrec := Tau.BookIV.Strong.instReprTracelessness.repr }

---

### `Tau.BookIV.Strong.instReprTracelessness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L202-L202)
**def
Tau.BookIV.Strong.instReprTracelessness.repr :Tracelessness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.tracelessness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L204-L204)
**def
Tau.BookIV.Strong.tracelessness :Tracelessness**

Equations
- Tau.BookIV.Strong.tracelessness = { }
Instances For

---

### `Tau.BookIV.Strong.SU3GaugeAlgebra`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L210-L228)
**structure
Tau.BookIV.Strong.SU3GaugeAlgebra :Type**


[IV.T69] The gauge algebra of the strong sector is isomorphic to su(3).
Forced by three structural constraints:

- Chi_minus-dominant polarity (non-abelian)

- Primorial depth 3 (three color classes, rank 2)

- Color-neutral vacuum (traceless: U(3) -> SU(3))


Dimension: 3^2 - 1 = 8 generators (the 8 gluon types).

- dimension : ℕ
Lie algebra dimension: N_c^2 - 1.

- num_colors : ℕ
Number of colors N_c.

- rank : ℕ
Rank of the algebra.

- constraint_1 : String
The three forcing constraints.

- constraint_2 : String
- constraint_3 : String
Instances For

---

### `Tau.BookIV.Strong.instReprSU3GaugeAlgebra.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L228-L228)
**def
Tau.BookIV.Strong.instReprSU3GaugeAlgebra.repr :SU3GaugeAlgebra → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprSU3GaugeAlgebra`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L228-L228)
**instance
Tau.BookIV.Strong.instReprSU3GaugeAlgebra :Repr SU3GaugeAlgebra**

Equations
- Tau.BookIV.Strong.instReprSU3GaugeAlgebra = { reprPrec := Tau.BookIV.Strong.instReprSU3GaugeAlgebra.repr }

---

### `Tau.BookIV.Strong.su3_gauge_algebra`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L230-L230)
**def
Tau.BookIV.Strong.su3_gauge_algebra :SU3GaugeAlgebra**

Equations
- Tau.BookIV.Strong.su3_gauge_algebra = { }
Instances For

---

### `Tau.BookIV.Strong.su3_dimension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L232-L232)
**theorem
Tau.BookIV.Strong.su3_dimension :su3_gauge_algebra.dimension = 8**


---

### `Tau.BookIV.Strong.su3_num_colors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L233-L233)
**theorem
Tau.BookIV.Strong.su3_num_colors :su3_gauge_algebra.num_colors = 3**


---

### `Tau.BookIV.Strong.su3_rank`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L234-L234)
**theorem
Tau.BookIV.Strong.su3_rank :su3_gauge_algebra.rank = 2**


---

### `Tau.BookIV.Strong.dimension_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L236-L239)
**theorem
Tau.BookIV.Strong.dimension_formula :su3_gauge_algebra.num_colors ^ 2 - 1 = su3_gauge_algebra.dimension**


N_c^2 - 1 = 8.

---

### `Tau.BookIV.Strong.GluonSelfInteraction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L245-L257)
**structure
Tau.BookIV.Strong.GluonSelfInteraction :Type**


[IV.P93] Gluons carry color charge and self-interact:
[T^a, T^b] = i f^{abc} T^c is nonzero, producing 3-gluon
and 4-gluon vertices. This is the structural origin of confinement.

- carries_color : Bool
Gluons carry color charge.

- nonzero_structure_constants : Bool
Structure constants f_{abc} are nonzero.

- three_vertex : Bool
Three-gluon vertex exists.

- four_vertex : Bool
Four-gluon vertex exists.

Instances For

---

### `Tau.BookIV.Strong.instReprGluonSelfInteraction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L257-L257)
**def
Tau.BookIV.Strong.instReprGluonSelfInteraction.repr :GluonSelfInteraction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprGluonSelfInteraction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L257-L257)
**instance
Tau.BookIV.Strong.instReprGluonSelfInteraction :Repr GluonSelfInteraction**

Equations
- Tau.BookIV.Strong.instReprGluonSelfInteraction = { reprPrec := Tau.BookIV.Strong.instReprGluonSelfInteraction.repr }

---

### `Tau.BookIV.Strong.gluon_self_interaction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L259-L259)
**def
Tau.BookIV.Strong.gluon_self_interaction :GluonSelfInteraction**

Equations
- Tau.BookIV.Strong.gluon_self_interaction = { }
Instances For

---

### `Tau.BookIV.Strong.ColorNumberTheorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L265-L289)
**structure
Tau.BookIV.Strong.ColorNumberTheorem :Type**


[IV.T70] N_c = 3 is uniquely determined by:


- Primorial depth d = 3

- CRT decomposition Z/30Z = Z/2Z x Z/3Z x Z/5Z

- Removal of polarity factor Z/2Z

- Chi_minus-dominant resolution selects the Z/3Z factor


The primorial 30 = 2 * 3 * 5, and depth 3 activates all three
prime factors. The Z/2Z factor is absorbed by polarity,
and Z/5Z is the EM depth-2 factor. The remaining Z/3Z gives N_c = 3.

- num_colors : ℕ
Number of colors.

- primorial_3 : ℕ
Primorial at depth 3.

- crt_factor_2 : ℕ
CRT factors.

- crt_factor_3 : ℕ
- crt_factor_5 : ℕ
- polarity_absorbs : String
Z/2Z absorbed by polarity.

- em_factor : String
Z/5Z is the EM depth-2 factor.

- strong_factor : String
Z/3Z is the strong color factor.

Instances For

---

### `Tau.BookIV.Strong.instReprColorNumberTheorem.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L289-L289)
**def
Tau.BookIV.Strong.instReprColorNumberTheorem.repr :ColorNumberTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprColorNumberTheorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L289-L289)
**instance
Tau.BookIV.Strong.instReprColorNumberTheorem :Repr ColorNumberTheorem**

Equations
- Tau.BookIV.Strong.instReprColorNumberTheorem = { reprPrec := Tau.BookIV.Strong.instReprColorNumberTheorem.repr }

---

### `Tau.BookIV.Strong.color_number_theorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L291-L291)
**def
Tau.BookIV.Strong.color_number_theorem :ColorNumberTheorem**

Equations
- Tau.BookIV.Strong.color_number_theorem = { }
Instances For

---

### `Tau.BookIV.Strong.nc_equals_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L293-L293)
**theorem
Tau.BookIV.Strong.nc_equals_3 :color_number_theorem.num_colors = 3**


---

### `Tau.BookIV.Strong.primorial_3_is_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L295-L301)
**theorem
Tau.BookIV.Strong.primorial_3_is_30 :color_number_theorem.crt_factor_2 * color_number_theorem.crt_factor_3 * color_number_theorem.crt_factor_5 = color_number_theorem.primorial_3**


Primorial(3) = 2 * 3 * 5 = 30.

---

### `Tau.BookIV.Strong.WilsonLoopDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L307-L318)
**structure
Tau.BookIV.Strong.WilsonLoopDef :Type**


[IV.D157] Wilson loop W(gamma) = (1/3) Tr U(gamma):
gauge-invariant trace of holonomy around a closed path.
Area-law decay signals confinement; perimeter-law signals deconfinement.

- normalization_numer : ℕ
Normalization factor: 1/N_c.

- normalization_denom : ℕ
- is_order_parameter : Bool
Order parameter for confinement.

- area_law_implies_confinement : Bool
Area law implies confinement.

Instances For

---

### `Tau.BookIV.Strong.instReprWilsonLoopDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L318-L318)
**instance
Tau.BookIV.Strong.instReprWilsonLoopDef :Repr WilsonLoopDef**

Equations
- Tau.BookIV.Strong.instReprWilsonLoopDef = { reprPrec := Tau.BookIV.Strong.instReprWilsonLoopDef.repr }

---

### `Tau.BookIV.Strong.instReprWilsonLoopDef.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L318-L318)
**def
Tau.BookIV.Strong.instReprWilsonLoopDef.repr :WilsonLoopDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.wilson_loop_def`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L320-L320)
**def
Tau.BookIV.Strong.wilson_loop_def :WilsonLoopDef**

Equations
- Tau.BookIV.Strong.wilson_loop_def = { }
Instances For

---

### `Tau.BookIV.Strong.wilson_normalization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/ColorHolonomy.lean#L322-L324)
**theorem
Tau.BookIV.Strong.wilson_normalization :wilson_loop_def.normalization_denom = su3_gauge_algebra.num_colors**
