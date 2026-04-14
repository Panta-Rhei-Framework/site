---
layout: impact-paper
lane: impact
title: τ for Distribution Networks, Leakage, Pressure, and Service Continuity
permalink: /impact/papers/distribution-networks-leakage-pressure-service-continuity/
paper_id: companion-water-wash-paper-2
portfolio_id: impact-water-wash
summary_short: A companion paper on how τ could improve drinking-water distribution
  network intelligence, leakage reduction, pressure management, and service continuity.
right_rail:
  meta:
    type: Companion Paper
    portfolio: Water Wash
    status: Conditional
    updated: April 2026
---

## Executive Summary

Drinking-water distribution networks are the hidden failure layer of the global water-access challenge. WHO and UNICEF report that 2.1 billion people still lacked safely managed drinking-water services in 2024, and the JMP definition makes clear that safety requires water to be not only sourced and treated but **available when needed** — reliably, on premises, and free from contamination at the point of use. That is fundamentally a network problem.

The global burden of non-revenue water (NRW) — water produced but not delivered, billed, or reaching an end user — stands at roughly 126 billion cubic metres per year, with a financial value exceeding US$39 billion annually (World Bank). In developing countries, NRW averages 35–50% of water produced; in developed countries, 15–25%. The UK loses approximately 3.1 billion litres per day, including some 600 million litres per day from Thames Water alone. WHO is explicit that pressurized, continuous piped supply is not merely a comfort standard but a safety and contamination-prevention requirement.

This paper asks a focused and clearly caveated question: **if the τ framework provides a law-faithful, bounded-error digital twin of distribution-network hydraulics, pressure behavior, leakage dynamics, water-age evolution, and residual disinfectant decay, what public good would that unlock?**

The answer, under that assumption, is substantial. Six interlocked capabilities become available: forward-looking pressure and leak-onset prediction before catastrophic failure; a single unified operational picture coupling leakage, pressure, and quality; a testable engineering pathway for intermittent-to-continuous supply conversion; active distribution-quality management from plant gate to tap; outage-aware critical-node resilience; and a dynamic evidence base for regulators and infrastructure financiers. Together, these represent a step change from reactive, fragmented utility operations to physics-faithful, predictive network intelligence.

Competitive tools — Pure Technologies (Xylem), Mueller Water Products (Echologics), Gutermann ZONESCAN, IBM Maximo, Aquadvanced (Suez), and WaterSight (Bentley Systems) — address parts of this space but remain acoustically constrained, hardware-intensive, ML-proxied, or limited to calibration rather than law-faithful predictive inference. τ's differentiator is causal completeness and bounded uncertainty across the full network state, not incremental signal processing or heuristic regression.

The practical scale is real. The World Bank's Ho Chi Minh City case recovered 92,000 m³/day in twenty months, enough to serve 500,000 people, by replacing less than 1% of the distribution system. Bangkok achieved 165,000 m³/day in comparable interventions. τ amplifies a value stream the sector already knows exists. Even a conservative 5–15% reduction in global NRW would recover 6.3–18.9 billion cubic metres per year — equivalent, at WHO's intermediate access benchmark of 50 litres per person per day, to the domestic water needs of 345 million to over 1 billion person-equivalents annually.

Finance pathways are established and well-funded: World Bank AMRUT at US$750M+, ADB water lending at US$2B+/year in Asia, UK Ofwat AMP regulatory cycles at £19B per five-year period, and USAID Water for the World programming. Unit economics are favorable: a τ network twin for a city utility of 500,000–2 million people would cost USD 3–8M while recovering 10–15 percentage points of NRW; a national platform for 50 cities on the India AMRUT model would cost USD 30–80M and save USD 500M–1.5B per year in lost water value. IWA estimates leakage management B:C ratios of 4:1 to 8:1.

This is not merely a utility-efficiency paper. Distribution intelligence under τ is a pathway to safer water, more reliable daily life, better drought resilience, lower energy waste, stronger emergency continuity, and more equitable service — exactly the outcomes that remain unfinished in the global water agenda.

---

## 1. Reader Stance, Scope, and Caveat Structure

### 1.1 Deliberate working stance

This paper adopts a deliberate and explicitly caveated planning stance:

1. **Assume, for planning purposes, that the strongest τ claims relevant to water-distribution hydraulics, water quality, and continuity management are sound.**
2. **Ask what practical and public-good consequences would follow** if those capabilities were integrated into utility operations, regulation, resilience planning, and water-service reform.
3. **Separate clearly:**
   - what official institutions already know and already want;
   - what τ would newly provide under that assumption;
   - and what impact estimates are reasoned planning inferences rather than official forecasts.

This is a yellow paper. It is assumption-led, deployment-oriented, and public-good framed. It does not claim that the water community has accepted the τ assumptions. It asks what follows if those assumptions are true enough to matter operationally.

### 1.2 Scope of this paper

This is **Paper 2 of 5** in the τ Water, WASH, and Basin Intelligence portfolio. Its scope is:

- drinking-water distribution networks;
- leakage and non-revenue water reduction;
- pressure management and pressure-transient risk;
- intermittent versus continuous service;
- continuity of supply to households and critical nodes;
- residual disinfectant, water age, and distribution quality hot spots;
- utility control, maintenance, and capital-priority intelligence.

### 1.3 Explicitly out of scope for Paper 2

The following are addressed elsewhere in the portfolio:

- **Paper 1:** source-water quality, treatment, and early warning;
- **Paper 3:** wastewater, stormwater, sanitation, and circular water reuse;
- **Paper 4:** river-basin, groundwater, drought–flood allocation, and water productivity;
- **Paper 5:** WASH in health facilities, schools, camps, and climate-vulnerable settlements.

Paper 2 focuses on the network layer between the treatment plant outlet and the consumer's tap.

---

## 2. Why Distribution Intelligence Is a First-Tier τ Opportunity

### 2.1 The drinking-water gap is increasingly a continuity and network-quality gap

The global safe-water challenge does not end at the treatment plant gate. WHO and UNICEF report that **2.1 billion people** still lacked safely managed drinking water in 2024.[^1] The JMP definition of safely managed drinking water requires an improved source that is accessible on premises, available when needed, and free from contamination.[^2][^3] In 2024, **1.7 billion people** still lacked an improved source accessible on premises.[^4]

This means the remaining gap is not simply "build a source." Much of it requires delivering **reliable, on-premises service with continuity and safety**. Many households may be connected to an improved source and still experience poor service because of intermittent supply, low pressure, distribution contamination, rooftop-storage dependence, or chronic unreliability. JMP reporting counts households as having water available when needed if they report availability "most of the time" — defined as at least 12 hours per day or four days per week.[^3] That threshold is already a substantial practical challenge for millions of urban utilities.

### 2.2 Continuity and pressure are water-quality conditions, not only utility-performance metrics

WHO's sanitary-inspection guidance for piped distribution networks is unusually direct: where possible, networks should be kept **pressurized** and should provide **continuous 24/7 supply**.[^5] WHO gives the causal reason explicitly: pressurized continuous supply helps avoid negative pressure, entry of contamination during periods of no service or low pressure, difficulties maintaining adequate free chlorine residual, and higher maintenance and replacement costs.[^5]

That is a crucial conceptual point. A distribution-network paper is not only about engineering efficiency. It is about **health protection at the network edge**. Pressure management and continuity are water-safety instruments.

### 2.3 The leakage and NRW burden is globally large

A recent World Bank background paper reports that water utilities around the world still experience very high water losses in distribution, with **non-revenue water accounting for 25–50% of total water supply** in many systems.[^6] A World Bank technical report cites an estimate of **346 million cubic metres per day** of NRW globally, equivalent to roughly **126 billion cubic metres per year**, with a financial value of **more than US$39 billion per year**.[^7]

Industry data sharpen the picture at national and utility scale. In developing countries, average NRW is 35–50% of water produced; in developed countries, 15–25%.[^8] The United Kingdom loses approximately **3.1 billion litres per day** across its water utilities, including roughly **600 million litres per day** from Thames Water alone, which serves 15 million customers in London and the Thames Valley.[^9] India's urban water systems average 40–50% NRW, with Delhi Jal Board losing approximately 40% of treated water from a system serving 20 million people.[^10]

These are not minor inefficiencies. They affect utility finances, household affordability, drought resilience, energy demand for pumping and treatment, source abstraction pressure, and the speed at which safe service can be extended to unserved populations.

### 2.4 Distribution losses are also an energy and climate problem

The World Bank's NRW work explicitly links water-loss reduction to energy efficiency.[^7] If treated water is pumped and then lost before delivery, the system also wastes treatment energy, pumping energy, chemicals, and plant capacity. The HCMC example cited in the World Bank report is instructive: a performance-based NRW intervention saved about **92,000 cubic metres per day** in 20 months, reduced leakage to roughly half its previous level, and saved about **23,000 kWh per day** — all while replacing less than 1% of the distribution system and creating enough saved water to serve approximately **500,000 people**.[^7] Bangkok achieved **165,000 m³/day** in comparable interventions.[^7]

That is before τ. The upside from a much stronger network twin amplifies a value stream the sector already knows is real.

### 2.5 Distribution is where climate stress and utility fragility become visible to households

Network fragility is how people most directly experience water stress: pressure loss during drought, outages during power failures, contamination after floods, pipe breaks after heat or ground-subsidence events, storage depletion during peak demand, and service collapse in already-vulnerable districts. Climate change is intensifying all of these stressors simultaneously.[^11]

That makes distribution intelligence a strong τ opportunity because it sits at the intersection of hydraulics, water quality, infrastructure reliability, energy dependence, and social equity — and because improvements in network predictability and resilience can translate directly into measurable improvements in service continuity for the most vulnerable populations.

---

## 3. What τ Would Change Under the Working Assumption

Under the strongest τ assumption, the improvement is not merely a somewhat better hydraulic model. It is a more fundamental operational shift: water utilities would gain access to a **law-faithful, bounded-error twin** of network hydraulics, pressure behavior, leakage, water age, residual disinfectant dynamics, and continuity under stress — capable of causal inference rather than statistical correlation, and of genuine physical prediction rather than pattern interpolation.

In practical terms, that shift would mean six things.

### 3.1 Network behavior becomes forward-looking instead of largely reactive

Today, most utilities infer network problems from customer complaints, periodic pressure checks, district-meter data, SCADA snapshots, break reports, and operator judgment. The dominant mode is reactive: find the problem after it manifests, repair it, and return to monitoring.

Under τ, the network layer becomes predictive before failure:
- where pressure is about to collapse under demand peaks or source variation;
- where a transient event is likely to create intrusion risk at a vulnerable junction;
- where a leak is emerging before it becomes a catastrophic burst;
- or where a supply interruption will propagate fastest through the service area.

This is not prediction by regression on historical data. It is prediction from causal network physics — a qualitatively different capability.

### 3.2 Leakage, pressure, and quality become one operational picture

In ordinary practice, leakage reduction, pressure management, and water-quality management are treated as related but partially separate agendas, often managed by different departments with different tools and different reporting cadences. Under τ, they become one causal system.

That matters because:
- high pressure drives real losses through the Bursts and Background Leakage (BABE) pressure-leakage relationship;[^12]
- low pressure increases intrusion risk during flow reversal;
- intermittent flow destabilizes residual disinfectant profiles;
- abnormal flow reversals can mobilize sediment and biofilm;
- and prolonged retention raises water age and presents trihalomethane and other formation risks.

A τ twin would let operators see those relationships together, in real time, rather than discovering them separately and belatedly.

### 3.3 Continuous-supply conversion becomes a testable engineering pathway

Many utilities want to move from intermittent to continuous service, but the transition is operationally and politically difficult. Current practice offers limited evidence on where continuity fails first, which district metered areas (DMAs) to prioritize, how much leak reduction is required before 24/7 becomes hydraulically feasible, and which sequence of valve, pump, storage, and rehabilitation actions minimizes both risk and cost.

Under τ, this transition becomes testable with genuine physical evidence:
- where pressure zones fail under continuous demand;
- which pipe segments are the binding constraints on continuity;
- how much NRW must be eliminated before storage can sustain 24/7 in each DMA;
- and what rehabilitation sequence carries the lowest risk and highest continuity gain per unit invested.

This could break the cycle — familiar across South Asia, sub-Saharan Africa, and parts of Latin America — in which intermittent service, rooftop storage, contamination risk, and weak public trust reinforce each other indefinitely.

### 3.4 Distribution water quality becomes actively manageable at the network edge

WHO guidance highlights the importance of maintaining adequate chlorine residual and the active management of dead legs, sediment, biofilms, abnormal flow events, and flushing schedules.[^5] Under τ, distribution quality control would become far stronger through physics-based prediction of:
- where residual decay is likely to fall below safe thresholds;
- where water age is accumulating in low-velocity zones;
- where sediment or biofilm release is likely after a flow change or pressure transient;
- where nitrification or other residual-breakdown pathways are likely to activate;
- and which nodes should be prioritized for monitoring, flushing, rechlorination, or operational intervention before rather than after a quality event.

### 3.5 Outage resilience becomes a built-in network capability

Distribution service is tightly linked to power availability, pump reliability, source stability, and storage dynamics. A τ network twin could therefore support:
- pre-outage service preservation through pressure-zone pre-filling;
- outage-aware pressure zoning that protects critical corridors;
- critical-node identification and supply-path protection;
- and better restoration sequencing that prioritizes health facilities, schools, and dense residential zones.

This is not just reduced losses under normal conditions. It is substantially improved performance on the difficult days — emergencies, extreme weather, source disruptions — when network intelligence matters most.

### 3.6 Regulators and funders gain a better evidence base for capital allocation

A persistent and widely acknowledged problem in distribution reform is that utilities and funders know they need to invest, but often lack the causal evidence to determine **where first**. Age-and-material heuristics, acoustic surveys, and lagged KPIs produce imprecise rehabilitation priorities.

Under τ, the network twin could support risk-ranked rehabilitation priorities, DMA creation and redesign, pressure-zone restructuring, storage optimization, critical-node reliability planning, and stronger evidence for public or concessional finance applications — transforming capital allocation from experience-based approximation to causally grounded planning.

---

## 4. Structured Opportunity Map

### Opportunity Area A — NRW Reduction, Leak Localization, and Pressure Management

**What the problem looks like now.** Utilities are attempting to reduce leaks with incomplete visibility into where losses originate, how pressure interacts with those losses, how quickly existing leaks are worsening, and how much network redesign versus targeted maintenance is actually needed. Acoustic correlation pinpoints some bursts but cannot predict incipient failures or provide a full-network leakage picture. DMA monitoring gives zone-level signals but not pipe-level physical causality.

**What τ would contribute.** Under the assumption: bounded-error leak localization at pipe-segment resolution; predictive deterioration windows based on pressure history, ground movement, and thermal cycling; better pressure-setpoint optimization that balances real losses against intrusion risk; and stronger DMA design and valve-control intelligence grounded in network physics rather than heuristic zones.

**Why this matters.** Saved water is often the cheapest incremental water supply a utility has — cheaper than new source development, treatment capacity, or long-distance conveyance.

### Opportunity Area B — Intermittent-to-Continuous Service Conversion

**The current challenge.** Intermittent systems suffer from contamination risk during low-pressure periods, public distrust, storage burdens on households (rooftop tanks, jerry cans), weak pressure control, and chronic inequality between well-served and poorly-served neighborhoods. WHO reports that intermittent supply affecting over **1 billion people** creates recurrent contamination risk during pressure drops.[^5] Utilities that want to convert to continuous supply often lack the technical evidence base to sequence the transition safely and affordably.

**What τ would change.** A τ twin would support: pressure-zone-by-zone feasibility mapping for 24/7 conversion; identification of which DMA-level leak repairs must precede continuity; storage and pump redesign with bounded hydraulic uncertainty; and lower-risk transition plans that demonstrate, in advance, which interventions are necessary and sufficient for continuous service in each zone.

**Public-good effect.** This is one of the clearest pathways from technical water modeling to household dignity, reliability, and equity. Continuous, pressurized supply directly addresses the contamination, storage, and reliability gaps that define the difference between improved and safely managed service.

### Opportunity Area C — Distribution Water-Quality Integrity and Hot-Spot Prediction

**The current challenge.** Water may leave the treatment plant in excellent condition and still degrade in the network because of low residual, long retention times, sediment mobilization, dead ends, abnormal flow reversals, or pressure-driven intrusion. These distribution failures are often invisible until a consumer complaint or laboratory detection confirms that quality has already deteriorated — by which point thousands of households may have been exposed.

**What τ would change.** A τ network-quality layer would support: water-age prediction at each node; residual optimization that considers full network flow dynamics; flushing prioritization based on predicted residual decay rather than calendar schedules; hot-spot surveillance maps that identify risk zones before events rather than after; and better targeting of finite monitoring resources toward the segments and times of highest predicted risk.

**Public-good effect.** Fewer invisible distribution failures and more confidence that treatment quality survives to the tap — the last mile of the safe-water chain that is currently most poorly characterized and least well managed.

### Opportunity Area D — Critical-Node Continuity and Emergency Operations

**The current challenge.** During outages, floods, heat waves, or source stress, utilities must protect hospitals, schools, dialysis centers, emergency shelters, and dense or highly vulnerable residential districts. Current practice often relies on manual rationing decisions, static valve-opening rules, and operator judgment with limited real-time physical evidence on where pressure will fail first or how far a supply disruption will propagate.

**What τ would change.** A τ continuity twin could help operators: identify and protect critical service paths under simulated outage conditions before outages occur; pre-position storage and pressure support at the most vulnerable nodes; plan rationing and rotation more intelligently when full supply cannot be maintained; and restore service in a sequence that prioritizes health outcomes rather than geographic convenience.

**Public-good effect.** This is the bridge from utility hydraulics to community resilience — converting network intelligence into protected service for the populations whose need is greatest when conditions are worst.

### Opportunity Area E — Utility Reform, Regulation, and Performance-Based Finance

**The current challenge.** Utilities, regulators, and financiers often work from lagged, static KPIs — annual NRW percentages, compliance percentages, incident logs — rather than dynamic causal evidence about where the network is failing and why. This limits the precision of investment decisions, weakens accountability mechanisms, and makes it difficult to design performance-based contracts with credible baselines and verifiable trajectories.

**What τ would change.** A shared network twin between utility and regulator could support: dynamic NRW baselines with causal attribution by zone and pipe class; regulator-visible service-continuity dashboards with physics-grounded projections; risk-ranked capital plans that can be compared across utilities on a common evidential basis; and more credible performance-based contract design that ties disbursement to measured network outcomes rather than proxy indicators.

**Public-good effect.** Better money spent in the places where network improvements really matter — closing the gap between what regulators want and what utilities can actually demonstrate they have achieved.

---

## 5. Realistic-Optimistic Public-Good Scenarios

These are not official forecasts. They are planning inferences under the strong τ assumption, intended to calibrate the plausible scale of benefit rather than to predict specific outcomes.

### Scenario 1 — Even Partial NRW Recovery Is Globally Large

The World Bank technical baseline cites **126 billion cubic metres per year** of NRW globally, with a financial value of **more than US$39 billion per year**.[^7] If τ enabled only a **5–15% reduction** in that global NRW burden over time — a conservative estimate given the World Bank's own examples of 40–50% reductions at city scale — that would correspond to:

- **6.3–18.9 billion cubic metres per year** of water recovered;
- **US$2–6 billion per year** in direct financial value.

Using WHO's intermediate access benchmark of approximately **50 litres per person per day** for on-plot access,[^13] that recovered water would be theoretically equivalent to the domestic water needs of roughly **345 million to just over 1 billion person-equivalents per year**.

That is a scale marker, not a deployment claim. The recovered water would not automatically appear in the places that need it most. But it shows how large the hidden opportunity is, and why even a modest realization of the τ assumption at global scale would represent a significant public-health gain.

### Scenario 2 — City-Scale Leakage Reduction Can Create Access-Equivalent Gains

The World Bank's HCMC case documents savings of approximately **92,000 m³/day**, enough to serve about **500,000 people**, with less than 1% of the distribution system replaced and about **23,000 kWh/day** saved.[^7] Bangkok achieved **165,000 m³/day** in comparable interventions.[^7] These results were achieved with conventional acoustic and DMA tools.

Under τ, the argument is not that every city will replicate these results. It is that the sector already has evidence that network intelligence can unlock very large service-equivalent gains even before total system rebuilding — and that τ's causal completeness and forward-looking capability would enable faster identification of the interventions that matter most.

### Scenario 3 — Continuity-Grade Service Could Improve Safely Managed Coverage Without Building Every New Source

Because safely managed service requires water to be **available when needed** and **free from contamination**, distribution upgrades can directly contribute to safely managed coverage even where the source and treatment backbone already exist.[^2][^3] Many households that count as having "access" in aggregate statistics are receiving intermittent, pressure-compromised, or contamination-vulnerable supply that does not meet the safely managed threshold.

A τ network twin could therefore increase safe service counts not only by adding supply but by improving the network conditions that make existing supply reliable, continuous, and uncontaminated — addressing the gap between nominal access and genuine safety that JMP data increasingly reveal.

### Scenario 4 — Water and Energy Savings Reinforce One Another

The HCMC example confirms that leakage reduction generates a double dividend: more water available, and lower energy use per unit of delivered water. In drought- and tariff-stressed utilities, this can materially improve financial viability, enabling utilities to sustain investment in maintenance and expansion that might otherwise be deferred. Network intelligence that simultaneously reduces losses and reduces energy costs per cubic metre improves the economic case for further investment — a self-reinforcing pathway from technical capability to financial sustainability to service expansion.

### Scenario 5 — Equity Effects Are Likely to Be Disproportionately Large in Low-Income Districts

In most urban water systems, leakage and pressure problems are concentrated in older, lower-income, or informally served parts of the network — precisely the areas where continuous, pressurized supply is most critical for health and where households have the least capacity to compensate with private storage or alternative sources. A τ twin that enables equity-explicit prioritization of maintenance and rehabilitation could amplify its public-good effect by directing improvement to the parts of the network where the social return on investment is highest.

---

## 6. Competitive Landscape

The distribution-network intelligence market contains several established players. All address parts of the problem. None provides the full causal, law-faithful, bounded-error network twin that τ describes. Understanding their limitations clarifies τ's differentiated position.

### Pure Technologies (Xylem)

Pure Technologies, now part of Xylem, specializes in acoustic leak detection and pipe condition assessment using free-swimming sensors, acoustic fiber monitoring, and pipe-wall-thickness profiling.[^14] Their tools are strong for inspecting existing pipes and identifying gross deterioration. They are not physics-based predictive models: they detect current conditions rather than forecasting future failure, cannot propagate hydraulic uncertainty through a full network state, and provide limited integration between leakage, pressure, and quality dynamics. Their primary value is in targeted inspection rather than network-level causal intelligence.

### Mueller Water Products (Echologics)

Mueller's Echologics platform uses acoustic correlators and SmartPipe embedded acoustic monitoring to detect leaks and assess pipe condition in real time.[^15] It is hardware-intensive, requiring deployment of sensors at regular intervals throughout the distribution network. Like Pure Technologies, it is signal-processing-based rather than physics-model-based: it identifies acoustic signatures of leaks rather than modeling the hydraulic and structural conditions that make leaks likely. It does not provide a physics-faithful digital twin of network state, cannot predict incipient failures before acoustic signatures emerge, and does not couple leakage to pressure and quality in a unified causal model.

### Gutermann ZONESCAN

Gutermann's ZONESCAN platform provides district metered area (DMA) acoustic monitoring through permanently installed noise loggers that detect and log leak sounds continuously.[^16] It is operationally effective for large-zone leak-flag monitoring and is widely used by European utilities. Its limitations are geographic scope (DMA-level signals without pipe-level resolution), absence of predictive hydraulic physics, and no integration with network-wide pressure, quality, or continuity modeling. ZONESCAN is a detection tool, not a causal twin.

### IBM Maximo Water Management

IBM Maximo is an enterprise asset management platform adapted for water utilities that supports maintenance scheduling, work-order management, and asset-lifecycle tracking.[^17] It is a strong operational and financial management tool, widely deployed in large utilities. It is not a hydraulic simulation or physics-faithful digital twin. It does not model pressure dynamics, does not predict leakage from first principles, and does not couple network hydraulics to water quality or continuity risk. Maximo is a management system; τ would be the physical layer that feeds better evidence into it.

### Aquadvanced (Suez)

Aquadvanced, developed by Suez (now part of Veolia), is a smart water network management platform that provides pressure optimization, leakage detection analytics, and demand forecasting.[^18] It uses machine-learning models trained on historical data to identify anomalous patterns associated with leakage and to recommend pressure-zone setpoints. Aquadvanced is ML-based, not physics-based: its predictions are interpolations from historical patterns rather than inferences from a causal model of network hydraulics. This limits its ability to predict novel failure modes, to provide bounded-error uncertainty estimates, or to generalize to networks with sparse historical data. It also does not fully couple leakage, pressure dynamics, water quality, and continuity risk in a single physical model.

### WaterSight (Bentley Systems)

WaterSight is Bentley's real-time digital twin platform for water distribution networks, built on hydraulic simulation (EPANET/WaterGEMS) with live data integration for model calibration.[^19] It is the closest existing tool to a physics-level network twin, offering SCADA-connected hydraulic model updating and real-time visualization. Its primary mode, however, is model calibration — adjusting a hydraulic simulation to match current sensor readings — rather than law-faithful predictive inference with rigorous bounded-error guarantees. It is proprietary, requires extensive setup and calibration data, is not designed to provide causal uncertainty propagation through the network state, and does not integrate residual disinfectant kinetics and water-age evolution in a unified causal framework. WaterSight represents the current state of the art; τ's differentiator is the step from calibration-based matching to genuinely physics-faithful forward prediction.

### τ's Differentiated Position

Across all six platforms, the pattern is consistent: each addresses one or two of the dimensions (acoustic detection, zone-level monitoring, asset management, ML anomaly detection, hydraulic calibration) without providing a causally complete, bounded-error, physics-faithful twin that couples pressure, leakage, quality, and continuity in a single inferential system. τ's value proposition is that causal completeness — not better acoustic hardware or richer ML training data — is what utilities actually need to move from reactive leak repair to anticipatory network management.

---

## 7. Benchmark Suite

A rigorous benchmark suite for Paper 2 should include the following test cases, each designed to distinguish physics-faithful prediction from pattern interpolation.

**Benchmark 1 — Leak Onset and Localization.** Detect and localize an emerging physical loss at a specific pipe segment before catastrophic burst, using only network-scale pressure and flow signals without acoustic hardware. Success criterion: pipe-segment-level localization more than 24 hours before visible failure, with bounded uncertainty estimate.

**Benchmark 2 — Pressure-Transient and Intrusion-Risk Prediction.** Forecast where low-pressure events or hydraulic transients create contamination intrusion risk, specifying affected junctions and expected duration. Success criterion: correct identification of intrusion-risk windows with false-positive rate below a specified threshold.

**Benchmark 3 — Water Age and Residual Disinfectant Hot-Spot Prediction.** Predict where chlorine residual will fall below the WHO guideline of 0.5 mg/L within the distribution network, given current demand patterns and system operations. Success criterion: spatial and temporal accuracy validated against network monitoring data at blind locations not used in model calibration.

**Benchmark 4 — Intermittent-to-Continuous Conversion Planning.** Given a DMA currently operating on intermittent supply, determine what repair, pressure setpoint, and storage configuration sequence is necessary and sufficient for 24/7 service, including the minimum NRW reduction required. Success criterion: technical-feasibility determination validated against observed network behavior when recommended changes are implemented.

**Benchmark 5 — Outage and Restoration Sequencing.** Optimize service continuity under a simulated pump failure or power outage scenario, identifying which valve and pump actions preserve critical-node supply for the longest period. Success criterion: outperform historical utility response time-to-restoration and critical-node coverage metrics.

**Benchmark 6 — Risk-Ranked Rehabilitation and DMA Design.** Rank pipe segments by predicted failure risk over a five-year horizon and recommend DMA boundary adjustments that maximize leak-detection sensitivity within budget constraints. Success criterion: rehabilitation predictions validated against observed failure events in a blind holdout period.

Success across these benchmarks should be judged not only by technical accuracy but also by water recovered, continuity improved, residual hot spots reduced, energy saved, and operator acceptance.

---

## 8. Case Studies

### Case Study 1: Thames Water — 600 Million Litres Per Day Lost

**Scale and regulatory context.** Thames Water is the UK's largest water utility, serving approximately **15 million customers** in London and the Thames Valley. It loses approximately **600 million litres per day** — roughly 25% of total production — to leakage.[^9] Under Ofwat's Asset Management Plan 7 (AMP7), Thames Water was required to reduce leakage by **15% by 2025** as a condition of the five-year regulatory settlement.[^20] Thames Water is also experiencing severe financial distress driven in part by the capital cost of aging infrastructure, deferred maintenance, and reactive repair cycles: the utility entered special administration proceedings in 2024 under the weight of debts exceeding £14 billion and operating costs that reactive leakage management has significantly inflated.[^21]

**Baseline problem.** Thames Water's leakage detection relies on acoustic correlation surveys, district-meter-based night-line analysis, and pressure management zones. Pipe-failure prediction uses age and material-class heuristics. There is no real-time, physics-faithful pressure-to-leak-rate twin capable of anticipating burst locations before they occur. Reactive repairs account for a substantial fraction of the utility's annual capital expenditure, which has run at £500M+ per year without meeting leakage reduction targets.[^22] Each burst in London's Victorian-era network creates not only water loss but road closures, property flooding, and service disruption to businesses and households — costs that extend well beyond the direct repair bill.

**τ-enabled change.** A physics-faithful hydraulic twin with pipe-wall stress modeling would enable Thames Water to predict likely burst locations 24–72 hours before failure based on pressure transients, soil moisture signals, temperature gradients, and ground-movement data that already exist in the utility's SCADA and environmental monitoring feeds. The predictive window is critical: it converts burst response from reactive emergency repair to scheduled, planned intervention — reducing emergency mobilization premiums, traffic management costs, and service disruption. Conservative industry estimates for predictive-versus-reactive leakage repair suggest **cost reductions of 20–35%** on reactive maintenance budgets. Separately, physics-faithful pressure-zone optimization — setting pressure setpoints based on real network state rather than static rules — is expected to contribute an additional **8–15% reduction in leakage** beyond the current Ofwat target, reducing the capital exposure associated with under-performance on AMP7 and AMP8 obligations.[^23]

**Relevance to financial distress.** Thames Water's financial position makes the cost-reduction dimension of τ particularly urgent. A utility under special administration cannot defer infrastructure costs indefinitely; it needs to demonstrate to Ofwat, to lenders, and to the UK government that there is a credible pathway to reducing operating costs while meeting leakage obligations. A physics-faithful twin that simultaneously reduces reactive repair costs and improves leakage performance would materially strengthen that case.

**Key references.** Thames Water Annual Performance Report 2023–24; Ofwat Water Industry Annual Performance Report 2023–24; UKWIR (UK Water Industry Research) leakage management technical reports; UK Government Thames Water special administration proceedings 2024.[^9][^20][^21][^22]

---

### Case Study 2: India Urban Water Supply — 40–50% NRW in Major Cities

**Scale and economic context.** India's urban water systems average **40–50% NRW**, with Delhi Jal Board serving approximately **20 million people** and losing roughly **40% of treated water**; Mumbai's system loses **25–30%** (better managed but still severe at scale).[^10] The AMRUT (Atal Mission for Rejuvenation and Urban Transformation) program, launched in 2015 and extended as AMRUT 2.0 in 2021, explicitly targets NRW reduction across **500 cities** with more than 100,000 population, supported by World Bank and central-government funding exceeding **US$750 million**.[^24]

The economic scale of NRW in India is substantial. Urban water systems lose an estimated **USD 3–5 billion per year** to NRW. Treatment and pumping costs for the water that is produced but lost add a further **USD 1–2 billion** in wasted energy and chemicals annually.[^25] These costs fall primarily on state governments and urban local bodies that are already fiscally constrained, diverting resources from network expansion to covering the operational costs of inefficiency.

**Baseline problem.** Indian utilities face a distinctive challenge: they typically lack real-time pressure monitoring, their network models are outdated or non-existent, and leakage detection relies primarily on manual field surveys that are slow, expensive, and unable to cover large networks systematically. Crucially, **intermittent supply** — often two to four hours per day in many cities — masks continuous leakage signals, because background-leakage signals that acoustic methods depend on are suppressed when pressure is low or absent for most of the day.[^26] This creates a technical trap: the cities that most need leakage intelligence are precisely the cities where the standard acoustic detection methods work least well.

**τ-enabled change.** A physics-faithful hydraulic twin, calibrated from sparse sensor data rather than requiring dense acoustic sensor networks, would break the intermittent-supply detection trap. Under τ, network state can be inferred from pressure and flow signals at a small number of district-meter points, without acoustic hardware throughout the pipe network. Optimal pressure zone management, designed from first-principles hydraulic inference, can reduce burst frequency by an estimated **20–30%** — consistent with World Bank case studies showing large burst-frequency reductions from pressure management alone.[^7]

Continuous leakage estimation based on the twin identifies priority zones for physical surveys and repair, dramatically improving the efficiency of field crews relative to uniform-coverage manual surveys. Perhaps most importantly, the τ twin enables **24/7 supply transition planning** — identifying which zones can sustain continuous pressure after specific leak repairs, allowing cities to move toward continuous supply in phases rather than requiring whole-system rehabilitation before any continuity improvement is achieved. Delhi's experience with AMRUT pilots shows that targeted pressure-zone management and leak reduction in selected DMAs can improve continuity from two-hour to eight-hour supply without full network replacement — but the sequencing decisions require better network physics than utilities currently have.[^10]

**Finance and implementation pathway.** AMRUT 2.0 provides a direct finance vehicle: World Bank and central-government grants for urban water infrastructure, with NRW reduction explicitly identified as a program objective. ADB water-supply lending in India and South Asia provides additional funding at USD 2B+ per year in the region. A national NRW reduction platform covering 50 cities on the AMRUT model — deploying τ network twins with shared calibration and training infrastructure — is estimated at USD 30–80 million, with expected savings of USD 500 million to USD 1.5 billion per year in lost water value once fully operational.[^24][^25]

**Key references.** World Bank India Urban Water Supply NRW Study; AMRUT Mission program reports; Delhi Jal Board annual reports; Asian Development Bank India water sector assessment; IWA Water Loss Specialists Group technical publications.[^10][^24][^25][^27]

---

## 9. Finance Pathways and Cost Scenarios

### 9.1 Major finance vehicles

**World Bank AMRUT (India).** The World Bank's AMRUT partnership provides **US$750M+** for urban water infrastructure across 500 Indian cities, with NRW reduction explicitly mandated as a program objective. This is a direct and near-term deployment vehicle for a τ network-intelligence platform in one of the highest-NRW urban water markets in the world.[^24]

**Asian Development Bank — Water Supply Modernization.** ADB provides approximately **US$2B+/year** in water supply lending in Asia, with programs in Bangladesh, Pakistan, Sri Lanka, Vietnam, Indonesia, and elsewhere that are explicitly addressing NRW and intermittent supply.[^28] Distribution intelligence tools that can be deployed with sparse sensor infrastructure are particularly well-suited to ADB borrower contexts.

**UK Ofwat Asset Management Plans.** Ofwat's five-year regulatory AMP cycles commit approximately **£19 billion per AMP period** across English and Welsh water utilities, with explicit leakage reduction targets.[^20] The AMP8 period (2025–2030) includes tightened leakage obligations and performance-based incentives that reward utilities for meeting or exceeding NRW reduction targets. The financial structure of AMPs directly rewards the kind of physics-faithful, performance-verifiable leakage intelligence that τ would provide.

**USAID Water for the World.** USAID's Water for the World program supports water systems improvement in priority developing countries, with emphasis on resilience, continuity, and NRW reduction in fragile and conflict-affected settings.[^29] Distribution intelligence tools with low data and hardware requirements are well-aligned with USAID's deployment contexts.

**Green Climate Fund and Climate-Resilience Finance.** Distribution network resilience is increasingly framed as a climate-adaptation investment, particularly in drought-prone, coastal, and subsidence-affected areas where network stress is intensifying. GCF and multilateral development bank climate facilities provide additional finance pathways for the resilience dimensions of τ network intelligence.

### 9.2 Unit cost scenarios

**Scenario A — Single city utility (500,000–2 million people).** Deployment of a τ network twin for a medium-large urban utility, including sensor integration, model calibration, operator training, and twelve-month supported operations: estimated **USD 3–8 million**. Expected NRW reduction: **10–15 percentage points** relative to baseline, generating USD 10–30M in annual water-value recovery depending on tariff levels and NRW starting point. Payback period: one to three years.

**Scenario B — National NRW reduction platform for 50 cities (India AMRUT model).** A shared-infrastructure deployment of τ network twins across 50 cities, with central calibration and training infrastructure, regional support capacity, and integration into AMRUT reporting frameworks: estimated **USD 30–80 million**. Expected annual savings: **USD 500M–1.5B** in recovered water value. B:C ratio: 6:1 to 20:1 at the upper end of the recovery range.

**Scenario C — UK regulatory compliance deployment (AMP8).** Deployment across two to five English water utilities to support AMP8 leakage compliance and performance-incentive maximization, integrated with existing SCADA and DMA infrastructure: estimated **USD 15–40 million**. Primary value driver: reduced regulatory penalty exposure plus reactive repair cost reduction. Secondary value driver: performance-incentive rewards for exceeding leakage targets.

### 9.3 Benefit-to-cost benchmarks

IWA estimates that **$1 invested in leakage management returns $4–8 in avoided production costs**, implying a B:C ratio of **4:1 to 8:1** for well-designed NRW programs — and this is before accounting for the avoided costs of new source development, treatment plant expansion, and associated infrastructure that becomes unnecessary when losses are reduced.[^27] The World Bank's HCMC case, with water recovered equivalent to new service for 500,000 people at less than 1% system replacement, implies an even higher effective B:C ratio when service-equivalent gains are monetized.[^7] τ's contribution would be to improve the precision and speed of leakage identification, compressing the time from investment decision to realized savings and reducing the cost of the investigation and diagnostic phase that currently absorbs a large share of NRW program budgets.

---

## 10. Deployment Ladder

### Phase 1 — Shadow-Mode Network Twin and DMA Intelligence

Run τ in parallel with existing network operations without operational integration. Deliverables: leak-risk maps updated daily; pressure and transient-risk forecasts by zone; water-age and residual hot-spot prediction; post-event hydraulic reconstruction for burst and quality events. Goal: demonstrate superior predictive value relative to current methods before any operational dependence is established. Duration: six to twelve months per utility.

### Phase 2 — Operator Support for Pressure, Leakage, and Continuity Management

Connect τ to day-to-day utility decision workflows. Deliverables: pressure-setpoint support for pumps and valve operations; DMA prioritization for leak survey dispatch; continuity-feasibility maps for targeted rehabilitation; risk-ranked maintenance queues with predictive deterioration windows. Goal: reduce avoidable uncertainty in network operations and support data-driven dispatch of maintenance resources. Duration: twelve to twenty-four months.

### Phase 3 — Outage Resilience and Critical-Service Continuity Layer

Embed τ into emergency planning and operational protocols. Deliverables: outage-aware service-preservation plans by zone; critical-node protection sequences; tested restoration-sequencing playbooks; stress-test simulation libraries for climate and infrastructure scenarios. Goal: improve bad-day performance, not just normal-day efficiency. Duration: twelve to eighteen months post-Phase 2.

### Phase 4 — Regulator- and Finance-Facing Reform Layer

Use τ evidence to support investment programs and regulatory accountability. Deliverables: dynamic NRW baselines with causal attribution for regulator reporting; continuity and risk dashboards shared between utility and regulator; risk-ranked capital plans supporting AMP and investment-program design; performance-based contract design supported by verifiable network-physics baselines. Goal: improve the quality of sector investment and the credibility of reform compacts. Duration: ongoing from Phase 2 onward.

---

## 11. Governance Guardrails

### 11.1 Utilities and regulators must retain accountability

The τ layer should augment and support professional engineering judgment, not replace it. Pressure decisions, valve operations, and service-allocation choices have public-health consequences that require qualified human accountability. τ provides evidence; engineers and operators provide judgment and bear responsibility.

### 11.2 Water continuity decisions cannot be black-boxed

Service allocation, rationing, and pressure decisions affect public health and social equity and must be explainable and auditable. Any operator-facing recommendation from a τ twin must be accompanied by a physical explanation in terms that utility engineers can evaluate and that regulators can verify. Black-box recommendations — even accurate ones — are inappropriate for safety-critical infrastructure.

### 11.3 Equity must be explicit

A network twin should not be used to optimize already well-served districts while low-income, informal, or periurban areas remain on intermittent supply. Equity-explicit prioritization — weighting rehabilitation decisions by service gap, population vulnerability, and health burden, not only by network cost-efficiency — must be designed into the deployment architecture from the start, not retrofitted afterward.

### 11.4 Safe degradation matters more than nominal average performance

The τ twin should be judged heavily by how it performs under outages, pressure transients, extreme demand events, and rare failure modes — not only under normal operating conditions. A model that performs well on average but fails badly under stress is likely to be worse than useless in the moments when it matters most.

### 11.5 Distribution quality and continuity must be managed together

If leakage, pressure, continuity, and residual quality remain managed in separate institutional silos — as they commonly are in large utilities — much of the value of a unified τ twin is lost. Governance reform that integrates these functions, or at minimum creates shared operational views across them, is a prerequisite for realizing the full benefit of network-level causal intelligence.

### 11.6 Calibration and data quality are shared infrastructure responsibilities

A physics-faithful twin is only as good as its calibration data. Utilities and implementing agencies must invest in the metering, pressure monitoring, and data management infrastructure needed to keep the twin calibrated. This is not a one-time cost but an ongoing operational responsibility that needs to be embedded in standard utility practice and regulatory reporting frameworks.

---

## 12. Research and Development Agenda

### 12.1 Sparse-sensor calibration for data-poor networks

Many of the utilities with the highest NRW and the greatest public-good need — in South Asia, sub-Saharan Africa, and fragile-state contexts — have sparse metering and monitoring infrastructure. A priority R&D challenge for τ is demonstrating calibration accuracy at minimum sensor densities, establishing the floor of data requirement for useful physics-faithful inference, and developing deployment protocols for sparse-data environments.

### 12.2 Intermittent-supply hydraulics

The physics of intermittent supply — with demand waves, air intrusion, partial pressurization, and rapidly changing boundary conditions — is substantially more complex than the hydraulics of continuous pressurized distribution. Extending τ's bounded-error guarantees to the intermittent-supply regime is necessary to address the cities where the public-health need is greatest.

### 12.3 Pipe-wall deterioration and burst prediction

Integrating soil mechanics, ground-movement data, thermal history, and pipe-material degradation models with the hydraulic twin would enable genuine predictive failure modeling — not only statistical deterioration curves based on age and material class, but physical inference about which specific segments are under elevated stress right now. This requires coupling structural mechanics with network hydraulics in a unified causal model.

### 12.4 Distribution-quality kinetics

Coupling a τ hydraulic twin to reactive-transport models for residual disinfectant decay, trihalomethane formation, and biofilm dynamics would complete the pipeline from network physics to public-health outcome. This is a well-characterized research area in water quality (the EPANET-MSX and similar multi-species extension frameworks provide starting points) but the coupling to a physics-faithful, bounded-error hydraulic twin has not been fully demonstrated.

### 12.5 Equity metrics and prioritization algorithms

Developing formal equity-weighted prioritization algorithms — that direct maintenance, rehabilitation, and continuity-improvement resources to the zones with the highest combination of service gap and population vulnerability — is both a technical and a governance challenge. It requires engagement with the communities most affected by poor distribution service, not only with utility managers and regulators.

---

## 13. Lighthouse Pilot Specifications

### Pilot 1 — High-NRW Metropolitan Utility

Best candidates: utilities with NRW above 30%, existing SCADA and DMA infrastructure, and regulatory pressure to reduce leakage. Best for: demonstrating leak localization, pressure management, and rapid operational savings. Success metrics: NRW reduction percentage points, reactive repair cost reduction, operator adoption rate.

### Pilot 2 — Intermittent-Supply City Targeting 24/7 Conversion

Best candidates: cities with two-to-six-hour supply per day, aspirations for continuous supply in the AMRUT or similar program context, and an existing DMA structure. Best for: continuity-feasibility mapping, equity-focused rehabilitation prioritization, and contamination-risk reduction. Success metrics: hours of supply per day in pilot zone, verified residual disinfectant compliance, household survey on service reliability.

### Pilot 3 — Coastal, Drought-Stressed, or Subsidence-Prone Network

Best candidates: utilities in areas experiencing ground subsidence, increasing drought frequency, or coastal aquifer depletion that is intensifying pressure on existing infrastructure. Best for: pressure-resilience planning, burst/leak prediction under environmental stress, and critical-node continuity under climate scenarios. Success metrics: burst frequency reduction, days with sub-minimum pressure, demonstrated continuity under stress scenarios.

### Pilot 4 — Hospital and School Service Corridor

Best candidates: utilities with identified critical-node continuity obligations in healthcare and education infrastructure. Best for: critical-node protection logic, restoration-sequencing validation, and public-health continuity assurance. Success metrics: hours of continuous supply at critical nodes during simulated outage events, restoration-time improvement relative to historical performance.

### Pilot 5 — Regulator–Utility Co-Pilot

Best candidates: a regulator willing to share a network twin with a regulated utility for joint performance assessment. Best for: demonstrating regulator-facing continuity and risk dashboards, performance-based contract design support, and translation of τ network intelligence into oversight and sector reform. Success metrics: regulator acceptance of τ-based NRW baselines for regulatory reporting, number of performance-based contract clauses enabled by causal network evidence.

---

## 14. Links to Wider Water Portfolio

Paper 2 connects to and depends on the wider τ Water, WASH, and Basin Intelligence portfolio in several ways.

**Paper 1 (Source Water and Treatment Quality)** provides the upstream boundary condition for the distribution network. The quality and variability of treated water entering the distribution system — its residual disinfectant concentration, temperature, and turbidity — directly affect what distribution-quality management needs to achieve. A τ twin coupling source-to-treatment-to-distribution would provide the most complete picture of water quality from catchment to tap.

**Paper 3 (Wastewater and Circular Reuse)** connects through the pressure and infrastructure management of dual networks. In cities developing non-potable reuse schemes, managing pressure differentials between potable and non-potable distribution networks is a distribution-intelligence challenge that τ is well-placed to address.

**Paper 5 (WASH in Health Facilities and Vulnerable Settings)** is directly served by the critical-node continuity capabilities developed in Paper 2. Hospitals, health centers, schools, and emergency camps are precisely the critical nodes that the τ distribution twin must protect during outages and stress events.

The **climate and resilience framing** across all five papers depends on distribution networks performing reliably under increasing climate stress. Paper 2's Opportunity Area D (critical-node continuity) and the deployment ladder's Phase 3 (outage resilience) are direct contributions to the cross-portfolio climate-adaptation case.

---

## 15. Bottom Line

Under the strong τ assumption, distribution networks, leakage, pressure, and service continuity represent one of the most compelling public-good opportunities in the entire water portfolio.

Why? Because the official world already tells us all three things needed to build the case.

First, safely managed drinking water requires water to be **available when needed**, not merely sourced or treated.[^2][^3] The safe-water gap is increasingly a continuity, pressure, and network-quality gap as much as a source gap.

Second, WHO already states explicitly that piped systems should, where possible, remain **pressurized and continuous** to avoid contamination and quality failure.[^5] This is not an engineering nicety; it is the physical mechanism by which network-level decisions produce or prevent public-health outcomes.

Third, the global NRW burden is so large — 126 billion cubic metres per year, worth more than US$39 billion annually — that even modest, realistically achievable improvements would produce **multi-billion-dollar** and **multi-billion-cubic-metre** benefits.[^6][^7] The HCMC and Bangkok examples demonstrate that this value stream is real, accessible without full system rebuilding, and amplified by better network intelligence.

The competitive landscape confirms that no existing tool provides what τ would provide: a causally complete, bounded-error, physics-faithful twin that couples pressure, leakage, quality, and continuity in a single forward-predictive system. The closest — Bentley WaterSight — offers calibration-based hydraulic matching; τ's step change is from calibration to genuine physical prediction.

The finance pathways are established and funded. The institutional demand — from Ofwat, AMRUT, ADB, USAID, and climate-resilience programs — exists and is active. The pilots are definable and bounded. The public-good case is clear and quantifiable.

This is not only a utility-efficiency paper. Distribution intelligence under τ is a pathway to:

- safer water at the network edge;
- more reliable daily life for households currently dependent on rooftop storage and intermittent supply;
- better drought resilience through recovered water that is already treated and need not be sourced again;
- lower energy waste per cubic metre delivered;
- stronger emergency continuity for hospitals, schools, and vulnerable districts;
- more equitable service in the parts of cities that need improvement most;
- and more credible, accountable, and precisely targeted public investment in water infrastructure.

That is why distribution networks, leakage, and service continuity deserve to be **Paper 2**.

---

## References

[^1]: WHO/UNICEF, *Progress on household drinking water, sanitation and hygiene 2000–2024* (2025). Available at: https://data.unicef.org/resources/jmp-report-2025/

[^2]: JMP, *Drinking water* topic page, WHO/UNICEF Joint Monitoring Programme. Available at: https://washdata.org/topics/drinking-water

[^3]: WHO/UNICEF, *State of the world's drinking water* (2022), on the meaning of "available when needed." Available at: https://cdn.who.int/media/docs/default-source/wash-documents/water-safety-and-quality/state-of-drinking-water-report-web.2_v-lowres.pdf

[^4]: WHO/UNICEF JMP 2025 report, improved water accessible on premises in 2024. Available at: https://cdn.who.int/media/docs/default-source/wash-documents/wash-coverage/jmp/jmp-2025-wash-households-lowres-launch.pdf

[^5]: WHO, *Sanitary inspection form for drinking water — Piped distribution network* (2023). Available at: https://cdn.who.int/media/docs/default-source/wash-documents/water-safety-and-quality/water-safety-planning/sanitary-inspection-packages/9.-piped-distribution---network_web.pdf

[^6]: World Bank, *Making the economic and financial case for circular water* (2024). Available at: https://thedocs.worldbank.org/en/doc/553c323db2132d2ee349da34a88a388b-0320082024/original/2024-03-06-WICER-Economic-and-Financial.pdf

[^7]: World Bank / PPP Unit, *Energy Efficiency and Nonrevenue Water* (2019), citing 346 million m³/day of NRW globally and case studies from HCMC and Bangkok. Available at: https://ppp.worldbank.org/sites/default/files/2022-04/EE_NRW_report_2019_082.pdf

[^8]: Liemberger, R. and Wyatt, A., "Quantifying the global non-revenue water problem," *Water Supply*, 19(3), 831–837 (2019). IWA Publishing.

[^9]: Thames Water, *Annual Performance Report 2023–24*. Ofwat Water Industry Annual Performance Report 2023–24. Available at: https://www.ofwat.gov.uk/regulated-companies/company-obligations/annual-performance-reports/

[^10]: World Bank, *India Urban Water Supply Nonrevenue Water Study* (2020–2022). Delhi Jal Board Annual Reports 2022–23. Asian Development Bank, *India Urban Infrastructure Assessment* (2021).

[^11]: IPCC, *Sixth Assessment Report (AR6) — Impacts, Adaptation and Vulnerability* (2022), Chapter 4: Water. Available at: https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-4/

[^12]: Lambert, A., "International report: water losses management and techniques," *Water Supply*, 2(4), 1–20 (2002). IWA Water Loss Task Force; BABE methodology for pressure-leakage relationships in distribution systems.

[^13]: WHO, *Domestic water quantity, service level and health* (2020). Available at: https://iris.who.int/bitstream/handle/10665/338044/9789240015241-eng.pdf

[^14]: Pure Technologies (Xylem), *SmartBall and PipeDiver acoustic inspection platforms*, product documentation. Available at: https://www.xyleminc.com/en-us/brands/pure-technologies/

[^15]: Mueller Water Products (Echologics), *SmartPipe and ePulse acoustic monitoring*, product documentation. Available at: https://www.muellercompany.com/water-products/echologics/

[^16]: Gutermann, *ZONESCAN Alpha district metered area acoustic monitoring*, product documentation. Available at: https://www.gutermann-water.com/products/zonescan/

[^17]: IBM, *Maximo Application Suite for water asset management*, product documentation. Available at: https://www.ibm.com/products/maximo

[^18]: Suez (Veolia), *Aquadvanced water network management platform*, product documentation. Available at: https://www.suez.com/en/what-we-offer/our-offers/smart-water/aquadvanced

[^19]: Bentley Systems, *WaterSight real-time digital twin for water distribution networks*, product documentation. Available at: https://www.bentley.com/software/watersight/

[^20]: Ofwat, *Water Industry Annual Performance Report 2023–24*. Ofwat, *AMP7 Final Determinations* (2019). Available at: https://www.ofwat.gov.uk/regulated-companies/company-obligations/annual-performance-reports/

[^21]: UK Government, *Thames Water special administration — Regulatory and financial proceedings* (2024). See Ofwat regulatory notices and UK DEFRA water infrastructure review documents.

[^22]: UKWIR (UK Water Industry Research), *Leakage target-setting methodology and cost assessment reports*, AMP7 and AMP8 planning documents (2020–2024). Available at: https://www.ukwir.org/

[^23]: Thornton, J., Sturm, R., and Kunkel, G., *Water Loss Control Manual*, Third Edition. McGraw-Hill (2017). Standard reference for pressure-leakage relationships and pressure management ROI.

[^24]: Ministry of Housing and Urban Affairs, Government of India, *AMRUT 2.0 Mission Document* (2021). World Bank, *India: AMRUT Urban Water Supply Program* (2022). Available at: https://amrut.gov.in/

[^25]: Asian Development Bank, *Water supply and sanitation sector assessment, India* (2022). World Bank, *India water sector economic analysis* (2020). NRW cost estimates for Indian urban water systems.

[^26]: Kingdom, B., Liemberger, R., and Marin, P., "The Challenge of Reducing Non-Revenue Water in Developing Countries," *Water Supply and Sanitation Sector Board Discussion Paper Series* No. 8. World Bank (2006). Limitations of acoustic detection under intermittent supply conditions.

[^27]: IWA Water Loss Specialists Group, *Benchmarking Performance Indicators for Non-Revenue Water* (2006, updated 2021). B:C ratio estimates for leakage management programs. Available at: https://iwa-network.org/groups/water-loss/

[^28]: Asian Development Bank, *Water sector lending program summary*, annual report (2022–2023). ADB Water Domain, NRW reduction programs in Bangladesh, Pakistan, Sri Lanka, Vietnam, Indonesia. Available at: https://www.adb.org/what-we-do/topics/water/overview

[^29]: USAID, *Water for the World Act implementation — Water supply, sanitation, and hygiene programs* (2022–2025). Available at: https://www.usaid.gov/water

[^30]: Ofwat, *PR24 Final Determinations* (2024), including AMP8 leakage performance commitments and outcome delivery incentive structures. Available at: https://www.ofwat.gov.uk/regulated-companies/price-review/2024-price-review/

[^31]: van Zyl, J.E. and Clayton, C.R.I., "The pressure leakage relationship in water distribution systems: from theory to practice," *Water Management*, 160(WM2), 113–119 (2007). ICE Publishing. Physical basis of pressure-leakage interaction in urban distribution networks.

[^32]: WHO, *Guidelines for Drinking-water Quality*, 4th edition incorporating the 1st addendum (2022). Chapter 9: Distribution systems. Available at: https://www.who.int/publications/i/item/9789240045064

[^33]: Rossman, L.A. et al., *EPANET 2.2 User Manual*. US Environmental Protection Agency (2020). Standard reference for water distribution hydraulic and quality modeling. Available at: https://epanetmanual.readthedocs.io/

[^34]: Colombo, A.F. and Karney, B.W., "Energy and costs of leaky pipes: toward comprehensive picture," *Journal of Water Resources Planning and Management*, 128(6), 441–450 (2002). ASCE. Energy cost of NRW in pressurized systems.

[^35]: McKenzie, R. and Seago, C., "Assessment of real losses in potable water distribution systems: some recent developments," *Water Supply*, 5(1), 33–40 (2005). IWA Publishing. Minimum night-flow and DMA methodology for NRW assessment.

[^36]: UN-Water, *Progress on water use efficiency — Global baseline for SDG Indicator 6.4.1* (2021). Available at: https://www.unwater.org/publications/progress-water-use-efficiency

[^37]: UNICEF and WHO, *Progress on WASH in health care facilities 2000–2021* (2022): baseline on critical-node water continuity requirements. Available at: https://www.who.int/publications/i/item/9789240050808

[^38]: Alegre, H. et al., *Performance Indicators for Water Supply Services*, 3rd edition. IWA Publishing (2016). Standard reference for NRW performance benchmarking and service-continuity metrics.


---

*Source: Full manuscript text integrated from companion paper draft.*
