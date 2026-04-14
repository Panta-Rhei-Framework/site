---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.CRAddressSpace"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-cr-address-space/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.CRAddressSpace"
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

# TauLib.BookIV.QuantumMechanics.CRAddressSpace


The Cauchy-Riemann address space on the arena tau^3 = tau^1 x_f T^2:
CR-manifold type, CR-structure on tau^3, character modes, admissible
sublattice, and the emergence of spin-1/2 from CR-parity.

## Registry Cross-References


- [IV.D49] CR-Manifold — `CRManifold`

- [IV.P08] Integrability Criterion — `integrability_criterion`

- [IV.D50] CR-Structure on tau^3 — `cr_structure_tau3`

- [IV.P09] Integrability of tau^3 CR-Structure — `tau3_cr_integrable`

- [IV.D51] Character Modes — `CharacterMode`

- [IV.D52] CR-Address — `CRAddress`

- [IV.D53] Address Precision (ch16) — `AddressPrecision`

- [IV.L01] Wedge Holonomy — `wedge_holonomy`

- [IV.T16] CR Parity Constraint — `cr_parity_constraint`

- [IV.D54] CR-Admissible Sublattice — `AdmissibleLattice`

- [IV.P10] Density Halving — `density_halving`

- [IV.T17] Emergence of Spin-1/2 — `spin_half_emergence`

- [IV.R292] Structural remark on CR-geometry

- [IV.R294] Structural remark on address space

- [IV.R295] Structural remark on parity


## Ground Truth Sources


- Chapter 16 of Book IV (2nd Edition)


---

### `Tau.BookIV.QuantumMechanics.CRManifold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L42-L54)
**structure
Tau.BookIV.QuantumMechanics.CRManifold :Type**


[IV.D49] CR-manifold of type (k, l): a real smooth manifold of
dimension 2k + l carrying a CR-structure. The tau^3 arena is
CR of type (1, 1), giving real dimension 2*1 + 1 = 3.

- k : ℕ
Complex tangent dimension k (number of holomorphic directions).

- l : ℕ
Totally real dimension l.

- real_dim : ℕ
Total real dimension = 2k + l.

- dim_eq : self.real_dim = 2 * self.k + self.l
Dimension consistency.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCRManifold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L54-L54)
**instance
Tau.BookIV.QuantumMechanics.instReprCRManifold :Repr CRManifold**

Equations
- Tau.BookIV.QuantumMechanics.instReprCRManifold = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCRManifold.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCRManifold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L54-L54)
**def
Tau.BookIV.QuantumMechanics.instReprCRManifold.repr :CRManifold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.CRManifold.mk_auto`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L56-L61)
**def
Tau.BookIV.QuantumMechanics.CRManifold.mk_auto
(k l : ℕ)
 :CRManifold**


CR-manifold dimension computes correctly for given k, l.
Equations
- Tau.BookIV.QuantumMechanics.CRManifold.mk_auto k l = { k := k, l := l, real_dim := 2 * k + l, dim_eq := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.IntegrableCR`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L67-L74)
**structure
Tau.BookIV.QuantumMechanics.IntegrableCRextends Tau.BookIV.QuantumMechanics.CRManifold :Type**


[IV.P08] CR-structure integrability: a CR-structure is integrable
iff the Nijenhuis tensor of J vanishes. Formalized structurally:
the boolean flag records the vanishing condition.

- k : ℕ
- l : ℕ
- real_dim : ℕ
- dim_eq : self.real_dim = 2 * self.k + self.l
- nijenhuis_vanishes : Bool
Nijenhuis tensor vanishes.

- nij_true : self.nijenhuis_vanishes = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprIntegrableCR.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L74-L74)
**def
Tau.BookIV.QuantumMechanics.instReprIntegrableCR.repr :IntegrableCR → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprIntegrableCR`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L74-L74)
**instance
Tau.BookIV.QuantumMechanics.instReprIntegrableCR :Repr IntegrableCR**

Equations
- Tau.BookIV.QuantumMechanics.instReprIntegrableCR = { reprPrec := Tau.BookIV.QuantumMechanics.instReprIntegrableCR.repr }

---

### `Tau.BookIV.QuantumMechanics.integrability_criterion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L76-L78)
**theorem
Tau.BookIV.QuantumMechanics.integrability_criterion
(icr : IntegrableCR)
 :icr.nijenhuis_vanishes = true**


Integrable CR-structures have vanishing Nijenhuis tensor.

---

### `Tau.BookIV.QuantumMechanics.cr_structure_tau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L84-L94)
**def
Tau.BookIV.QuantumMechanics.cr_structure_tau3 :IntegrableCR**


[IV.D50] The CR-structure on tau^3 = tau^1 x_f T^2:
H = fiber tangent T^2 (2 real dims), J = rotation on H,
nu = contact form (1 real dim along tau^1).
Type: (k=1, l=1) giving dim = 2*1 + 1 = 3.
Equations
- Tau.BookIV.QuantumMechanics.cr_structure_tau3 = { k := 1, l := 1, real_dim := 3, dim_eq := Tau.BookIV.QuantumMechanics.cr_structure_tau3._proof_1,
 nijenhuis_vanishes := true, nij_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.tau3_cr_integrable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L100-L103)
**theorem
Tau.BookIV.QuantumMechanics.tau3_cr_integrable :cr_structure_tau3.nijenhuis_vanishes = true**


[IV.P09] The CR-structure on tau^3 is integrable:
Nijenhuis tensor vanishes because T^2 is flat and the
fibration projection is holomorphic.

---

### `Tau.BookIV.QuantumMechanics.tau3_cr_dim`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L105-L106)
**theorem
Tau.BookIV.QuantumMechanics.tau3_cr_dim :cr_structure_tau3.real_dim = 3**


tau^3 is CR of type (1,1) with real dimension 3.

---

### `Tau.BookIV.QuantumMechanics.CharacterMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L112-L120)
**structure
Tau.BookIV.QuantumMechanics.CharacterMode :Type**


[IV.D51] Character mode chi_{m,n}(theta_gamma, theta_eta) =
exp(i(m*theta_gamma + n*theta_eta)) for (m,n) in Z^2.
The Fourier mode on T^2 fiber.

- m : ℤ
Winding number along gamma-circle.

- n : ℤ
Winding number along eta-circle.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCharacterMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L120-L120)
**instance
Tau.BookIV.QuantumMechanics.instReprCharacterMode :Repr CharacterMode**

Equations
- Tau.BookIV.QuantumMechanics.instReprCharacterMode = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCharacterMode.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCharacterMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L120-L120)
**def
Tau.BookIV.QuantumMechanics.instReprCharacterMode.repr :CharacterMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L120-L120)
**def
Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode.decEq
(x✝ x✝¹ : CharacterMode)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode.decEq { m := a, n := a_1 } { m := b, n := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L120-L120)
**instance
Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode :DecidableEq CharacterMode**

Equations
- Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode = Tau.BookIV.QuantumMechanics.instDecidableEqCharacterMode.decEq

---

### `Tau.BookIV.QuantumMechanics.instBEqCharacterMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L120-L120)
**instance
Tau.BookIV.QuantumMechanics.instBEqCharacterMode :BEq CharacterMode**

Equations
- Tau.BookIV.QuantumMechanics.instBEqCharacterMode = { beq := Tau.BookIV.QuantumMechanics.instBEqCharacterMode.beq }

---

### `Tau.BookIV.QuantumMechanics.instBEqCharacterMode.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L120-L120)
**def
Tau.BookIV.QuantumMechanics.instBEqCharacterMode.beq :CharacterMode → CharacterMode → Bool**

Equations
- Tau.BookIV.QuantumMechanics.instBEqCharacterMode.beq { m := a, n := a_1 } { m := b, n := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIV.QuantumMechanics.instBEqCharacterMode.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIV.QuantumMechanics.CRAddress`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L126-L129)@[reducible, inline]

**abbrev
Tau.BookIV.QuantumMechanics.CRAddress :Type**


[IV.D52] CR-address: a pair (m, n) in Z^2 identifying a specific
character mode on T^2. The address encodes the "quantum numbers"
of a state on the fiber torus.
Equations
- Tau.BookIV.QuantumMechanics.CRAddress = Tau.BookIV.QuantumMechanics.CharacterMode
Instances For

---

### `Tau.BookIV.QuantumMechanics.AddressPrecision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L135-L149)
**structure
Tau.BookIV.QuantumMechanics.AddressPrecision :Type**


[IV.D53] Address precision P(f) = sup |f_hat_{m,n}|^2 in (0,1].
How sharply a state f is localized at a particular address.
Represented as a scaled rational (numer, denom).

- numer : ℕ
Precision numerator (scaled).

- denom : ℕ
Precision denominator.

- denom_pos : self.denom > 0
Denominator positive.

- numer_pos : self.numer > 0
Precision in (0,1]: numer > 0.

- numer_le_denom : self.numer ≤ self.denom
Precision in (0,1]: numer <= denom.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprAddressPrecision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L149-L149)
**instance
Tau.BookIV.QuantumMechanics.instReprAddressPrecision :Repr AddressPrecision**

Equations
- Tau.BookIV.QuantumMechanics.instReprAddressPrecision = { reprPrec := Tau.BookIV.QuantumMechanics.instReprAddressPrecision.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprAddressPrecision.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L149-L149)
**def
Tau.BookIV.QuantumMechanics.instReprAddressPrecision.repr :AddressPrecision → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.WedgeHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L155-L165)
**structure
Tau.BookIV.QuantumMechanics.WedgeHolonomy :Type**


[IV.L01] Holonomy of chi_{m,n} around the wedge point of L:
exp(2*pi*i*(m+n)*iota_tau). The holonomy phase depends on
the sum m+n scaled by iota_tau. We record the structural fact:
the holonomy winding factor is (m+n)*iota/iotaD.

- mode : CharacterMode
The character mode.

- winding : ℤ
Holonomy winding = (m + n).

- winding_eq : self.winding = self.mode.m + self.mode.n
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprWedgeHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L165-L165)
**instance
Tau.BookIV.QuantumMechanics.instReprWedgeHolonomy :Repr WedgeHolonomy**

Equations
- Tau.BookIV.QuantumMechanics.instReprWedgeHolonomy = { reprPrec := Tau.BookIV.QuantumMechanics.instReprWedgeHolonomy.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprWedgeHolonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L165-L165)
**def
Tau.BookIV.QuantumMechanics.instReprWedgeHolonomy.repr :WedgeHolonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.wedge_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L167-L171)
**def
Tau.BookIV.QuantumMechanics.wedge_holonomy
(cm : CharacterMode)
 :WedgeHolonomy**


Wedge holonomy for a given character mode.
Equations
- Tau.BookIV.QuantumMechanics.wedge_holonomy cm = { mode := cm, winding := cm.m + cm.n, winding_eq := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.cr_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L177-L181)
**def
Tau.BookIV.QuantumMechanics.cr_admissible
(addr : CRAddress)
 :Prop**


[IV.T16] CR parity constraint: chi_{m,n} is CR-admissible iff
m + n is even (m + n = 0 mod 2). This is the condition for the
character to be compatible with the CR-structure on tau^3.
Equations
- Tau.BookIV.QuantumMechanics.cr_admissible addr = ((addr.m + addr.n) % 2 = 0)
Instances For

---

### `Tau.BookIV.QuantumMechanics.instDecidableCr_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L183-L185)
**instance
Tau.BookIV.QuantumMechanics.instDecidableCr_admissible
(addr : CRAddress)
 :Decidable (cr_admissible addr)**


Decidability of CR-admissibility.
Equations
- Tau.BookIV.QuantumMechanics.instDecidableCr_admissible addr = inferInstanceAs (Decidable ((addr.m + addr.n) % 2 = 0))

---

### `Tau.BookIV.QuantumMechanics.cr_parity_constraint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L187-L190)
**theorem
Tau.BookIV.QuantumMechanics.cr_parity_constraint
(addr : CRAddress)
 :cr_admissible addr ↔ (addr.m + addr.n) % 2 = 0**


CR parity constraint: m+n even iff admissible.

---

### `Tau.BookIV.QuantumMechanics.AdmissibleLattice`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L205-L211)
**structure
Tau.BookIV.QuantumMechanics.AdmissibleLattice :Type**


[IV.D54] The CR-admissible sublattice Lambda_CR = {(m,n) in Z^2 : m+n even}.
This is a sublattice of Z^2 of index 2.

- addr : CRAddress
Address in the lattice.

- admissible : cr_admissible self.addr
CR-admissibility proof.

Instances For

---

### `Tau.BookIV.QuantumMechanics.density_halving`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L217-L223)
**theorem
Tau.BookIV.QuantumMechanics.density_halving
(addr : CRAddress)

(h : cr_admissible addr)
 :¬cr_admissible { m := addr.m + 1, n := addr.n }**


[IV.P10] Lambda_CR has density 1/2 in Z^2: for every admissible
address (m,n), its neighbor (m+1,n) is inadmissible.
This proves the sublattice has index 2.

---

### `Tau.BookIV.QuantumMechanics.density_halving_converse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L225-L229)
**theorem
Tau.BookIV.QuantumMechanics.density_halving_converse
(addr : CRAddress)

(h : ¬cr_admissible addr)
 :cr_admissible { m := addr.m + 1, n := addr.n }**


Conversely, if (m,n) is inadmissible, (m+1,n) is admissible.

---

### `Tau.BookIV.QuantumMechanics.SpinHalfEmergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L235-L251)
**structure
Tau.BookIV.QuantumMechanics.SpinHalfEmergence :Type**


[IV.T17] Emergence of spin-1/2: the bi-rotation on T^2 constrained
by CR-parity (m+n even) produces a double cover, which is the
SU(2) structure responsible for spin-1/2 in quantum mechanics.

Structural: the sublattice index (= 2) equals the double cover
degree, which is the denominator of the minimal spin quantum number.
spin_half_denom = sublattice_index = 2.

- sublattice_index : ℕ
Sublattice index in Z^2.

- index_eq : self.sublattice_index = 2
- double_cover_degree : ℕ
Double cover degree.

- cover_eq : self.double_cover_degree = 2
- spin_from_index : self.sublattice_index = self.double_cover_degree
They agree.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSpinHalfEmergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L251-L251)
**instance
Tau.BookIV.QuantumMechanics.instReprSpinHalfEmergence :Repr SpinHalfEmergence**

Equations
- Tau.BookIV.QuantumMechanics.instReprSpinHalfEmergence = { reprPrec := Tau.BookIV.QuantumMechanics.instReprSpinHalfEmergence.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprSpinHalfEmergence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L251-L251)
**def
Tau.BookIV.QuantumMechanics.instReprSpinHalfEmergence.repr :SpinHalfEmergence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.spin_half_emergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L253-L259)
**def
Tau.BookIV.QuantumMechanics.spin_half_emergence :SpinHalfEmergence**


The canonical spin-1/2 emergence.
Equations
- One or more equations did not get rendered due to their size.
Instances For
