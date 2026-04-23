---
layout: taulib-doc
title: "TauLib.BookVI.Consumer.ConsumerMixer"
permalink: /verify/taulib/docs/book-vi-consumer-consumer-mixer/
lane: verify
module_name: "TauLib.BookVI.Consumer.ConsumerMixer"
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

# TauLib.BookVI.Consumer.ConsumerMixer


Consumer mixer on (π', π''): the mixed-sector foundation of animal life.

## Registry Cross-References


- [VI.D46] Consumer Mixer on (π', π'') — `ConsumerMixer`

- [VI.T25] Signature Rigidity Determines Uniqueness — `signature_rigidity_uniqueness`

- [VI.L07] Consumer as Bridge-Head to E₃ — `bridge_head_e3`


## Cross-Book Authority


- Book I, Part I: generators α, π, π', π'' (five generators of τ³)

- Book II, Part II: π₁(T²) ≅ ℤ × ℤ (fiber fundamental group, two winding numbers)

- Book VI, Part 1: VI.D20 consumer sector (mixed sector in 4+1 classification)


## Ground Truth Sources


- Book VI Chapter 33 (2nd Edition): The Consumer Mixer


---

### `Tau.BookVI.Consumer.ConsumerMixer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L32-L50)
**structure
Tau.BookVI.Consumer.ConsumerMixer :Type**


[VI.D46] Consumer Mixer on (π', π''): mixed-sector pairing
of both fiber generators. The only non-primitive sector.
Generator pair: (π', π'') on fiber T² (Book I, Part I).
Winding: π₁(T²) ≅ ℤ × ℤ gives two independent winding numbers
(Book II, Part II). Both must be nontrivial.

- generator_pair : String
Generator pair label.

- is_mixed : Bool
Mixed sector (not primitive).

- winding_pi_prime : ℕ
Winding number on π' (must be ≥ 1).

- winding_pi_double : ℕ
Winding number on π'' (must be ≥ 1).

- pi_prime_nontrivial : self.winding_pi_prime ≥ 1
π' winding nontrivial.

- pi_double_nontrivial : self.winding_pi_double ≥ 1
π'' winding nontrivial.

Instances For

---

### `Tau.BookVI.Consumer.instReprConsumerMixer.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L50-L50)
**def
Tau.BookVI.Consumer.instReprConsumerMixer.repr :ConsumerMixer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consumer.instReprConsumerMixer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L50-L50)
**instance
Tau.BookVI.Consumer.instReprConsumerMixer :Repr ConsumerMixer**

Equations
- Tau.BookVI.Consumer.instReprConsumerMixer = { reprPrec := Tau.BookVI.Consumer.instReprConsumerMixer.repr }

---

### `Tau.BookVI.Consumer.canonical_mixer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L52-L56)
**def
Tau.BookVI.Consumer.canonical_mixer :ConsumerMixer**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consumer.consumer_is_mixed_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L58-L62)
**theorem
Tau.BookVI.Consumer.consumer_is_mixed_sector :FourPlusOne.consumer_sector.is_primitive = false ∧ canonical_mixer.is_mixed = true**


Consumer is the mixed sector from FourPlusOne.

---

### `Tau.BookVI.Consumer.consumer_generator_match`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L64-L67)
**theorem
Tau.BookVI.Consumer.consumer_generator_match :canonical_mixer.generator_pair = FourPlusOne.consumer_sector.generator**


Consumer matches FourPlusOne generator label.

---

### `Tau.BookVI.Consumer.SignatureRigidity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L73-L92)
**structure
Tau.BookVI.Consumer.SignatureRigidity :Type**


[VI.T25] Signature Rigidity Determines Uniqueness.
Among the 10 possible generator pairings on τ³:


- base–base (α,π): both base → no fiber innovation → unstable

- base–fiber (α,π') etc.: mixed base+fiber → partial → unstable

- fiber–fiber (π',π''): both fiber generators → full T² coverage → stable
Only (π',π'') yields a stable mixed sector.


- total_pairings : ℕ
Total possible pairings from 5 generators taken 2.

- base_base_stable : Bool
Only fiber–fiber is stable.

- base_fiber_stable : Bool
Base–fiber pairings unstable.

- fiber_fiber_stable : Bool
Fiber–fiber pairing stable (π',π'' only).

- stable_count : ℕ
Stable pairings count.

- stable_eq : self.stable_count = 1
Exactly 1 stable pairing.

Instances For

---

### `Tau.BookVI.Consumer.instReprSignatureRigidity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L92-L92)
**def
Tau.BookVI.Consumer.instReprSignatureRigidity.repr :SignatureRigidity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consumer.instReprSignatureRigidity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L92-L92)
**instance
Tau.BookVI.Consumer.instReprSignatureRigidity :Repr SignatureRigidity**

Equations
- Tau.BookVI.Consumer.instReprSignatureRigidity = { reprPrec := Tau.BookVI.Consumer.instReprSignatureRigidity.repr }

---

### `Tau.BookVI.Consumer.sig_rigid`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L94-L97)
**def
Tau.BookVI.Consumer.sig_rigid :SignatureRigidity**

Equations
- Tau.BookVI.Consumer.sig_rigid = { total_pairings := 10, stable_count := 1, stable_eq := Tau.BookVI.Consumer.sig_rigid._proof_1 }
Instances For

---

### `Tau.BookVI.Consumer.signature_rigidity_uniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L99-L104)
**theorem
Tau.BookVI.Consumer.signature_rigidity_uniqueness :sig_rigid.fiber_fiber_stable = true ∧ sig_rigid.base_base_stable = false ∧ sig_rigid.base_fiber_stable = false ∧ sig_rigid.stable_count = 1**


---

### `Tau.BookVI.Consumer.BridgeHeadE3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L110-L124)
**structure
Tau.BookVI.Consumer.BridgeHeadE3 :Type**


[VI.L07] Consumer as Bridge-Head to E₃.
Only the mixed sector supports Eval² = Eval ∘ Eval
(second-order self-description). This opens the bridge
from E₂ (life) to E₃ (consciousness/mind).
Primitive sectors have Eval¹ only.

- eval_order : ℕ
Evaluator order (2 = second-order self-description).

- order_eq : self.eval_order = 2
Exactly order 2.

- only_mixed_sector : Bool
Only mixed sector reaches E₃.

- opens_e3 : Bool
Opens enrichment layer E₃.

Instances For

---

### `Tau.BookVI.Consumer.instReprBridgeHeadE3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L124-L124)
**instance
Tau.BookVI.Consumer.instReprBridgeHeadE3 :Repr BridgeHeadE3**

Equations
- Tau.BookVI.Consumer.instReprBridgeHeadE3 = { reprPrec := Tau.BookVI.Consumer.instReprBridgeHeadE3.repr }

---

### `Tau.BookVI.Consumer.instReprBridgeHeadE3.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L124-L124)
**def
Tau.BookVI.Consumer.instReprBridgeHeadE3.repr :BridgeHeadE3 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Consumer.bridge_head`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L126-L128)
**def
Tau.BookVI.Consumer.bridge_head :BridgeHeadE3**

Equations
- Tau.BookVI.Consumer.bridge_head = { eval_order := 2, order_eq := Tau.BookVI.Consumer.bridge_head._proof_1 }
Instances For

---

### `Tau.BookVI.Consumer.bridge_head_e3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Consumer/ConsumerMixer.lean#L130-L134)
**theorem
Tau.BookVI.Consumer.bridge_head_e3 :bridge_head.eval_order = 2 ∧ bridge_head.only_mixed_sector = true ∧ bridge_head.opens_e3 = true**
