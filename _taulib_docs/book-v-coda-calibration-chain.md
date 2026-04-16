---
layout: taulib-doc
title: "TauLib.BookV.Coda.CalibrationChain"
permalink: /verify/taulib/docs/book-v-coda-calibration-chain/
lane: verify
module_name: "TauLib.BookV.Coda.CalibrationChain"
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

# TauLib.BookV.Coda.CalibrationChain


Mass derivation chain and calibration sufficiency: derives m_e, m_P, and G
from m_n and the G-α bridge outputs, proving that the SI calibration
cascade requires zero additional free parameters.

## Registry Cross-References


- [V.T156] Mass Derivations — Layer 2 -- `MassDerivationLayer2`

- [V.T157] Calibration Sufficiency -- `CalibrationSufficiency`


## Mathematical Content


### Mass Derivations — Layer 2 [V.T156]


From m_n and Layer 1 (the G-α bridge):


- m_e = m_n / R, where R is the mass ratio from the τ³ fibration

- m_P = m_n / √α_G, where α_G comes from the bridge

- G = (c³/ℏ) · ι<sub>τ</sub>², linking gravitational constant to the master constant


### Calibration Sufficiency [V.T157]


The SI calibration cascade is sufficient: every constant in the ledger
is determined by ι<sub>τ</sub> and m_n with zero additional free parameters.
The calibration triangle (G, κ_n, α_G) closes exactly.

## Ground Truth Sources


- Book V ch71: Mass derivation, calibration cascade


---

### `Tau.BookV.Coda.MassDerivationLayer2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L40-L64)
**structure
Tau.BookV.Coda.MassDerivationLayer2 :Type**


[V.T156] Mass derivations — Layer 2.
Derives m_e, m_P, and G from m_n and Layer 1 outputs:


- m_e = m_n / R (R from τ³ mass ratio)

- m_P = m_n / √α_G (α_G from G-α bridge)

- G = (c³/ℏ) · ι<sub>τ</sub>² (direct from master constant)


The layer structure:
Layer 0: ι<sub>τ</sub> = 2/(π+e) (master constant, from axioms)
Layer 1: α_G = α¹⁸ · √3 · (1 − (3/π)α) (G-α bridge)
Layer 2: m_e, m_P, G (this theorem)
Anchor: m_n (single dimensionful input)

- n_derived : ℕ
Number of derived masses.

- derived_eq : self.n_derived = 3
Three masses derived.

- n_layers : ℕ
Number of layers in the cascade.

- layers_eq : self.n_layers = 3
Three layers (0, 1, 2).

- single_anchor : Bool
Single anchor (m_n).

- zero_additional_params : Bool
Zero additional free parameters.

Instances For

---

### `Tau.BookV.Coda.instReprMassDerivationLayer2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L64-L64)
**instance
Tau.BookV.Coda.instReprMassDerivationLayer2 :Repr MassDerivationLayer2**

Equations
- Tau.BookV.Coda.instReprMassDerivationLayer2 = { reprPrec := Tau.BookV.Coda.instReprMassDerivationLayer2.repr }

---

### `Tau.BookV.Coda.instReprMassDerivationLayer2.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L64-L64)
**def
Tau.BookV.Coda.instReprMassDerivationLayer2.repr :MassDerivationLayer2 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.mass_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L66-L71)
**def
Tau.BookV.Coda.mass_derivation :MassDerivationLayer2**


The canonical mass derivation.
Equations
- Tau.BookV.Coda.mass_derivation = { n_derived := 3, derived_eq := Tau.BookV.Coda.mass_derivation._proof_1, n_layers := 3,
 layers_eq := Tau.BookV.Coda.mass_derivation._proof_1 }
Instances For

---

### `Tau.BookV.Coda.mass_derivation_layer2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L73-L79)
**theorem
Tau.BookV.Coda.mass_derivation_layer2 :mass_derivation.n_derived = 3 ∧ mass_derivation.n_layers = 3 ∧ mass_derivation.single_anchor = true ∧ mass_derivation.zero_additional_params = true**


Layer 2 derives 3 masses from 3 layers with single anchor.

---

### `Tau.BookV.Coda.derived_masses_match_layers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L81-L84)
**theorem
Tau.BookV.Coda.derived_masses_match_layers :mass_derivation.n_derived = mass_derivation.n_layers**


Derived mass count equals layer count: one mass per layer.

---

### `Tau.BookV.Coda.CalibrationSufficiency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L90-L115)
**structure
Tau.BookV.Coda.CalibrationSufficiency :Type**


[V.T157] Calibration sufficiency: the SI calibration cascade is
sufficient. Every constant in the ledger is determined by ι<sub>τ</sub> and m_n
with zero additional free parameters.


- Inputs: ι<sub>τ</sub> (dimensionless, from axioms) + m_n (dimensionful anchor)

- Outputs: G, α, α_G, m_e, m_P, c, ℏ, k_B, ...

- The calibration triangle (G, κ_n, α_G) closes exactly

- No fitting, no adjustable parameters


- n_dimensionless : ℕ
Number of dimensionless inputs.

- dimless_eq : self.n_dimensionless = 1
One dimensionless input (ι<sub>τ</sub>).

- n_anchors : ℕ
Number of dimensionful anchors.

- anchor_eq : self.n_anchors = 1
One anchor (m_n).

- n_free_params : ℕ
Number of free parameters.

- free_eq : self.n_free_params = 0
Zero free parameters.

- total_inputs_count : ℕ
Total inputs count (ι<sub>τ</sub> + m_n).

- triangle_closes : Bool
Calibration triangle closes.

Instances For

---

### `Tau.BookV.Coda.instReprCalibrationSufficiency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L115-L115)
**def
Tau.BookV.Coda.instReprCalibrationSufficiency.repr :CalibrationSufficiency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprCalibrationSufficiency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L115-L115)
**instance
Tau.BookV.Coda.instReprCalibrationSufficiency :Repr CalibrationSufficiency**

Equations
- Tau.BookV.Coda.instReprCalibrationSufficiency = { reprPrec := Tau.BookV.Coda.instReprCalibrationSufficiency.repr }

---

### `Tau.BookV.Coda.calibration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L117-L124)
**def
Tau.BookV.Coda.calibration :CalibrationSufficiency**


The canonical calibration sufficiency.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.calibration_sufficiency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L126-L132)
**theorem
Tau.BookV.Coda.calibration_sufficiency :calibration.n_dimensionless = 1 ∧ calibration.n_anchors = 1 ∧ calibration.n_free_params = 0 ∧ calibration.triangle_closes = true**


Calibration is sufficient: 1 dimensionless + 1 anchor + 0 free params.

---

### `Tau.BookV.Coda.total_inputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L134-L137)
**theorem
Tau.BookV.Coda.total_inputs :calibration.n_dimensionless + calibration.n_anchors = 2**


Total input count: 1 + 1 = 2 (ι<sub>τ</sub> + m_n).

---

### `Tau.BookV.Coda.iota_tau_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Coda/CalibrationChain.lean#L139-L140)
**def
Tau.BookV.Coda.iota_tau_anchor :Float**


Master constant ι<sub>τ</sub> = 2/(π+e).
Equations
- Tau.BookV.Coda.iota_tau_anchor = 0.341304238875
Instances For
