---
layout: impact-paper
lane: impact
title: τ for Solar-Plus-Storage, Microgrids, and Critical-Infrastructure Resilience
permalink: /impact/papers/solar-storage-microgrids-critical-infrastructure-resilience/
paper_id: companion-solar-paper-3
portfolio_id: impact-solar
summary_short: A companion paper on how τ could improve solar-plus-storage system
  design, microgrid operations, and critical-infrastructure resilience for hospitals,
  water systems, and community hubs.
right_rail:
  meta:
    type: Companion Paper
    portfolio: Solar
    status: Conditional
    updated: April 2026
---

# τ for Solar-Plus-Storage, Microgrids, and Critical-Infrastructure Resilience
**Companion Dossier — Panta Rhei Impact: Solar Portfolio**
**Paper 3 of 5 · Status: Yellow Paper · March 2026**

---

## Executive Summary

The United States experienced an average of **11 hours of electricity interruptions per customer in 2024** — nearly twice the annual average of the previous decade — driven by **27 billion-dollar weather disasters** and major hurricanes that alone accounted for 80% of outage hours.[^3][^4] More than **3 million Medicare beneficiaries** depend on electricity for life-sustaining home medical equipment, meaning prolonged outages are not merely inconveniences but medical emergencies.[^5][^6] Battery storage is now crossing the threshold of operational relevance: cumulative U.S. utility-scale capacity exceeded **26 GW** in 2024, with another **24 GW** planned for 2026.[^7][^8]

Against this backdrop, solar-plus-storage, microgrids, and resilience hubs are no longer boutique sustainability investments. They are the next tier of critical infrastructure. The limiting constraint is no longer hardware availability. It is the quality of the physics modeling, dispatch logic, and survivability planning that governs how these systems are sized, operated, and proven.

This paper asks a targeted planning question: **if the τ framework provides a physically faithful, bounded-error, coarse-grainable discrete twin of weather–irradiance–PV–battery–load–microgrid dynamics, what public good could that unlock?** The answer is substantial and near-term relative to many deeper τ implications.

Under the strong τ assumption, the shift is not merely better sizing software or smarter dispatch heuristics. It is a move toward a **law-faithful resilience twin** that can support forecast-informed battery pre-charging before a storm event, physically bounded outage-survivability analysis rather than scenario guesswork, auditable blue-sky and black-sky co-optimization on the same computational substrate, and structured local restoration using grid-forming inverter capabilities.

The deployment opportunity spans five intersecting domains: healthcare campuses and medically vulnerable households; water and wastewater utilities; community resilience hubs in underserved or outage-prone neighborhoods; utility feeder-level resilience orchestration; and remote, off-grid, and edge-of-grid communities in the United States, Australia, and Sub-Saharan Africa.

Financing pathways are well-established: DOE LPO Section 1706, USAID Power Africa, World Bank ESMAP Lighting Africa, IFC Scaling Solar, and IRENA Climate Promise collectively represent tens of billions of dollars directed at exactly this problem space. Benefit-to-cost ratios for critical-facility resilience routinely exceed 4:1 when avoided outage costs are valued at $10,000–50,000 per day for hospitals and emergency services.

This paper is **Paper 3 of 5** in the solar/PV opportunity portfolio. It adopts the same explicit caveat structure as the series: it does not claim that the broader power sector has accepted τ assumptions. It asks what would follow if those assumptions were true enough to matter operationally.

---

## 1. Reader Stance, Scope, and Caveat Structure

### 1.1 Analytical discipline

This paper adopts the same three-level discipline as the rest of the solar impact portfolio:

1. **Assume, for planning purposes, that the strongest τ claims relevant to solar-plus-storage and resilience are sound** — specifically, that τ provides a bounded-error, physically faithful, refinable discrete twin of weather-to-grid dynamics.
2. **Ask what practical and public-good consequences would follow** if those claims were integrated into current resilience planning, critical-facility operations, and microgrid deployment practice.
3. **Keep three layers rigorously separate:**
   - what official institutions already know and already want;
   - what τ would newly provide under the strong assumption;
   - and what impact scenarios are reasoned planning inferences rather than forecasts or commitments.

The caveat is structural, not rhetorical. The τ framework is under active development as a mathematical physics research program. Its physical predictions at the level relevant to solar forecasting and microgrid physics have not been accepted by mainstream power engineering. This paper's value lies in its clarity about that boundary.

### 1.2 Scope of this paper

This paper focuses on:

- solar-plus-storage for outage survivability and critical-facility continuity;
- community resilience hubs at schools, community centers, and emergency shelters;
- microgrids and islanded operation including grid-forming restoration;
- remote and off-grid solar-plus-storage with physics-faithful dispatch;
- and deployment pathways for utilities, public agencies, site operators, and development finance.

### 1.3 Explicitly out of scope

Deferred to other papers in this five-paper portfolio:

- **Paper 1:** τ-grade solar forecasting for bulk-grid operations and market dispatch;
- **Paper 2:** τ for distributed PV visibility and distribution-grid orchestration;
- **Paper 4:** τ for PV asset protection, storm-hardening, and long-term system planning;
- **Paper 5:** τ for solar-synchronized flexible demand and grid logistics.

---

## 2. Why Solar-Plus-Storage and Microgrids Are a First-Tier τ Opportunity

### 2.1 The outage burden is real, rising, and directly legible

EIA's 2025 reliability report provides the sharpest statistical framing available: the average U.S. electricity customer experienced **11 hours without power in 2024**, nearly double the annual average of the prior decade.[^3] Major weather events — Hurricanes Beryl, Helene, and Milton among them — accounted for **80%** of those interruption hours.[^3] NOAA counted **27 separate billion-dollar weather and climate disasters** in the United States in 2024, maintaining the elevated pace seen since 2020.[^4]

This matters for τ deployment positioning for a specific reason: resilience investments are easiest to justify when the baseline burden is both empirically clear and directionally rising. Solar-plus-storage and microgrids are not pitching against skepticism about whether outages are a problem. The problem is settled. The dispute is about whether current tools are adequate for the design and operational complexity now required.

### 2.2 Official institutions have already named solar, storage, and microgrids as the answer

The policy framing is unusually well-aligned with the technology opportunity. DOE's **Solar and Resilience Basics** page states explicitly that solar-plus-storage can keep solar power available during outages and that microgrids can provide resiliency benefits — and notes that with grid-forming inverters, a solar-plus-storage system may be able to restart the grid after disruptions if the system is large enough.[^1]

DOE's **Resilient Distribution Systems Powered by Solar Energy** page frames resilient distribution systems around the ability to use PV and battery storage to quickly reconfigure power flows and recover electricity services during disturbances including cyberattacks, accidents, and weather events.[^2]

DOE's 2024 **Solar and DERs for Community Energy Resilience Workshop** was organized around solar, storage, and DERs as tools that help communities prepare, adapt, and recover from disruptions while supporting decarbonization goals.[^9] These are not aspirational statements from advocacy organizations. They are program planning documents from the department that funds most U.S. energy research and deployment.

The consequence for τ is favorable: the external demand signal is already articulated and funded. What is needed is not to create a new policy conversation but to offer a capability step change within an already-open conversation.

### 2.3 Battery storage is crossing the operational-significance threshold

The hardware base now justifies modeling investment. EIA reports cumulative U.S. utility-scale battery storage at **more than 26 GW** as of end-2024, with operators planning to add another **24 GW** in 2026 and with utility-scale solar additions expected to set a new record at **43.4 GW** in 2026 alone.[^7][^8] These numbers mean that solar-plus-storage is no longer a small-scale demonstration technology. It is core grid infrastructure in multiple U.S. regions and in energy-access markets worldwide.

The limiting constraint has shifted. It is no longer hardware cost or availability. It is the quality of the modeling, dispatch logic, and survivability analysis that governs how these systems are designed and run.

### 2.4 Critical-facility stakes are immediate and highly legible

The public-good case is at its strongest at critical facilities because outage harm is immediate, measurable, and politically visible. FEMA's power-outage incident annex explicitly names water treatment plants, hospitals, wastewater treatment plants, and shelters as high-priority outage-sensitive facilities.[^10] DOE and NREL resilience materials return to these site categories repeatedly because the human cost of failure is unambiguous.[^11][^12]

The healthcare case carries particular moral force. HHS emPOWER data covers **more than 4.6 million Medicare beneficiaries**, of whom **over 3 million** have a documented claim for electricity-dependent durable medical equipment — ventilators, oxygen concentrators, infusion pumps, and similar life-sustaining devices.[^5] CDC and ASTHO research documents what happens when those systems lose power: during the 2021 Texas grid failure, one ambulance provider received more than 50 calls in two days from patients with failing life-sustaining devices; after Hurricane Sandy, power outages drove hundreds of home-equipment users to hospital emergency departments solely to access electricity.[^6]

This is not a population-health abstraction. It is a predictable, repeated mechanism of harm during major outages. Better resilience systems for critical facilities and neighborhoods with medically vulnerable residents address this harm directly.

### 2.5 Solar-plus-storage offers dual-use value that changes the investment logic

Standard backup systems offer value only during outages — which by definition are rare. Solar-plus-storage can simultaneously deliver everyday bill reduction and peak shaving, local grid services, outage survivability, and carbon reduction. NREL and DOE valuation research consistently finds that when resilience value is included in the analysis, the economics of PV-plus-storage look materially different: larger, differently configured, or more widely deployed systems become cost-justified.[^13][^14]

This dual-use character is where τ could have its clearest first-wave impact. If the same physically faithful twin supports both day-to-day dispatch optimization and outage-mode survivability planning, solar-plus-storage resilience becomes less like an insurance purchase and more like a continuously productive operating asset.

---

## 3. Working τ Assumptions for Solar-Plus-Storage and Resilience

The following are the strongest τ claims relevant to this domain. They are stated as planning assumptions, not as accepted physical results.

### 3.1 Weather-to-PV-to-storage dynamics are physically faithful inside τ

τ is assumed to provide a bounded-error, coarse-grainable physical twin of cloud and irradiance dynamics affecting PV output; temperature effects on panel efficiency and battery performance; storage charge-discharge electrochemistry and state-of-health degradation; critical-load profiles at building, campus, and feeder scale; and islanded versus grid-connected control dynamics. The key distinction from current modeling practice is not higher resolution per se — it is structural fidelity across the full chain from weather to power delivery.

### 3.2 Outage survivability is treated as a structural envelope, not a scenario collection

Under the strong τ stance, outage survivability can be evaluated as a physically constrained envelope determined by outage start time, critical-load profile, weather and irradiance over the event window, initial battery state of charge, asset availability and health, and islanding and restoration rules. Current best practice (exemplified by NREL's REopt probabilistic survivability outputs) already moves in this direction. τ would deepen it by reducing the gap between the physical twin and the planning model.

### 3.3 Precision and refinement remain structurally aligned at every scale

τ is assumed to ensure that as modeling resolution increases — from site-level to campus-level to feeder-level to district-level — the physical consistency of the twin is preserved rather than degraded. This addresses a recognized failure mode in current practice: coarse planning models, fine transient models, and operational dispatch tools are often built with incompatible assumptions, and error accumulates at each interface.

### 3.4 The τ twin supports deployable operational artifacts, not only analysis

For this paper's practical scenarios to be actionable, τ must support not only offline proof and simulation but also operational outputs: day-ahead outage-preparation plans; battery pre-charge strategies aligned to forecast weather and threat windows; critical-load shedding prioritization; microgrid mode-transition logic; and post-event restoration scheduling. These are strong assumptions. The purpose is to ask what follows if they are true enough to matter.

---

## 4. What Changes if τ Is a Law-Faithful Resilience Twin Rather Than a Better Optimizer?

### 4.1 From backup sizing by rule of thumb to physically bounded survivability design

Current resilience design blends heuristics, representative outage scenarios, design-day assumptions, and probabilistic tools. NREL's REopt already improves this substantially — its resilience outputs include explicit probability-of-surviving-an-N-day-outage curves, and NREL's microgrid design guide emphasizes the sensitivity of survivability to load profile, solar availability, battery state of charge, and outage timing.[^15][^16]

Under τ, the planning question shifts from: "What set of representative outage scenarios should we test?" to: "Given a law-faithful site twin, what are the actual survivability envelopes and optimal intervention strategies across the relevant event space?"

That is a qualitative change in confidence level, not just a quantitative improvement in accuracy. It transforms outage survivability from a scenario-sampled guess to a structurally derived bound.

### 4.2 From static resilience plans to live blue-sky/black-sky co-optimization

Many resilience systems are designed in one operational mode and used in another, producing a chronic mismatch between design assumptions and operational realities. Under τ, blue-sky and black-sky operations can share a single computational twin:

- **Blue-sky mode:** demand management, peak shaving, energy arbitrage, local ancillary services, emissions reduction.
- **Black-sky mode:** seamless islanding, critical-load support, staged load shedding, restoration sequencing, emergency communications and shelter operations.

NREL's resilience-hub guidance explicitly distinguishes these two modes and notes the design challenge of optimizing for both simultaneously.[^17] Under τ, that separation becomes more tractable because both modes are governed by the same physically faithful twin.

### 4.3 From isolated facilities to coordinated resilience networks

Once individual facility resilience can be simulated and scheduled faithfully, the natural planning unit expands. Rather than designing each hospital, water plant, or community center in isolation, planners can work with:

- a hospital campus with multiple buildings and priority tiers;
- a municipal cluster linking emergency operations, fire stations, and shelters;
- a neighborhood microgrid serving a medically vulnerable population;
- or a city-scale resilience-hub network linked to feeder restoration planning.

DOE and NREL are already oriented toward this multi-asset framing through community resilience programs, resilience-hub projects, and resilient-distribution-system work.[^2][^9][^17][^18] τ would reduce the modeling and control burden that currently limits the scale of multi-asset coordination.

### 4.4 From qualitative resilience claims to auditable, deployable metrics

DOE's Customer Damage Function calculator exists because organizations need a structured way to estimate the cost of inaction and compare it to resilience investment costs.[^19] NREL's valuation research shows that when outage costs are valued explicitly, PV-plus-storage economics can change materially.[^13][^14]

Under τ, outage cost, survivability probability, and mission continuity become mutually consistent quantities tied to the same physically constrained twin rather than to disconnected spreadsheet assumptions. This makes resilience procurement more auditable and more defensible to regulators, boards, and public funders.

---

## 5. Structured Opportunity Map

### Opportunity family A — Healthcare, medical continuity, and public health

#### A1. Hospital campus microgrids and mission assurance

Hospitals are the clearest first-tier resilience targets. DOE-backed programs cite them repeatedly as high-priority sites.[^10][^12] A current high-profile example is Valley Children's Healthcare, where DOE reports that a renewable-energy microgrid is expected to supply 80% of current hospital energy demand and reduce greenhouse-gas emissions by more than 50% while enabling the campus to remain operational during regional outages.[^18]

Under τ, the opportunity is not only to design more hospital microgrids but to design them with better outage survivability estimates, better battery pre-charge logic ahead of approaching storms, better load prioritization within the campus, and more defensible confidence bounds on restoration sequencing. For a facility where a 24-hour outage can trigger patient transfers, generator failures, and staff overload, the margin of safety matters more than the average-case performance.

#### A2. Home medical-device resilience and prevention of hospital surge

HHS emPOWER and the CDC/ASTHO preparedness research establish a well-documented chain: power outages → home medical device failures → ambulance calls and emergency department visits → hospital surge during the precise moment when hospital systems are most stressed.[^5][^6] Preventing that chain from completing is a public-health intervention, not merely a convenience.

This creates downstream resilience opportunities for utilities, municipalities, and community organizations: resilience hubs with medical refrigeration and device charging; neighborhood microgrids sited specifically for medically vulnerable populations; and forecast-informed pre-positioning of mobile power support resources. A τ twin would strengthen all three by making outage timing, duration, and local solar availability substantially more predictable.

### Opportunity family B — Water, wastewater, and public-service continuity

#### B1. Water and wastewater microgrids

FEMA and EPA both classify water and wastewater utilities as outage-sensitive critical infrastructure.[^10][^20] EPA's Power Resilience Guide for the water sector explicitly discusses microgrids and on-site generation, and provides wastewater-utility case studies involving solar, batteries, and microgrids for outage ride-through.[^20]

Under τ, the opportunity expands from generic backup power to weather-informed pre-event energy management; critical-process prioritization (e.g., maintaining primary treatment during extended outages); water-energy operational coordination; and outage-duration-aware dispatch logic that conserves battery capacity for the most chemically sensitive processes.

#### B2. Public-safety and municipal service campuses

Police departments, fire stations, emergency operations centers, communications hubs, and municipal campuses face the same structural vulnerability. NREL and DOE resilience materials use these sites as case studies because they combine high public value with immediately legible outage harm.[^11][^17]

Under τ, municipalities could move from the current paradigm — a backup generator at each building, managed independently — toward portfolio-level resilience orchestration across a shared planning twin.

### Opportunity family C — Community resilience hubs and equitable resilience

#### C1. Resilience hubs at schools, churches, and community centers

NREL's resilience-hub research is clear: community centers, schools, and similar civic sites can be equipped with solar-plus-storage to provide cooling and warming during climate events, food and medical refrigeration, device charging, communications, and other essential services during outages.[^17][^21][^22] The Sabathani Community Center project documented by NREL provides a worked example of a solar-plus-storage resilience hub serving a historically underserved neighborhood.[^22]

This opportunity family has the strongest combination of technical feasibility, public-health impact, equity alignment, and community trust. It links climate adaptation, energy access, public health, local governance, and visible material benefit in a single installation. τ would strengthen this by improving siting, sizing, survivability planning, and operations — including the prediction of how long a hub can sustain operations under a specific weather scenario.

#### C2. Underserved communities and energy burden reduction

NREL's 2024 utility guidance on commercial solar and solar-plus-storage in underserved communities identifies outage survivability and community resilience hubs as two of four primary use cases.[^21] It notes that resilience hubs can provide medical refrigeration, communications, shelter, and other essential services during emergencies and that these benefits are most valuable in communities with high outage risk and limited private backup options.[^21]

Projects that simultaneously reduce energy burden and improve resilience are easier to sustain politically and easier to finance through equity-focused grant and loan programs.

### Opportunity family D — Utility and feeder resilience

#### D1. Resilient distribution systems with PV and storage

DOE's resilient-distribution-systems program frames PV and storage as tools that can reconfigure power flows and recover service faster after disturbances — whether caused by cyberattacks, physical accidents, or severe weather.[^2] This is no longer fringe thinking in utility planning. It is a funded federal research direction, and several states have regulatory requirements or performance metrics that explicitly reward faster restoration.

Under τ, utilities could move toward better feeder-level outage survivability maps; more intelligent switching and sectionalization plans; better coordination between utility-owned storage and customer-sited resilience assets; and dynamic operating envelopes that explicitly account for resilience mode alongside normal operations.

#### D2. Grid-forming restoration and black-start-adjacent capabilities

DOE's article on grid-forming inverters notes that these technologies may eventually allow solar and storage systems to restart portions of the grid independently, without waiting for conventional synchronous generators.[^23] This is one of the most consequential long-horizon implications of the hardware transition underway.

Under τ, this becomes a tractable medium-term opportunity: not only using solar-plus-storage to survive outages passively, but using it actively to contribute to structured local restoration — in sequence, with predictable power quality, and with physically grounded confidence bounds.

### Opportunity family E — Remote, tribal, campus, and edge-of-grid systems

Remote and edge-of-grid systems are often where microgrids make the most immediate and self-evident sense. The outage burden is already high, often chronic rather than episodic, and the value of energy continuity is unambiguous for residents, schools, health clinics, and water systems. DOE's tribal-energy and microgrid resources treat microgrids as a way to operate autonomously when the larger grid is unavailable or unaffordable to extend.[^24]

Under τ, these systems benefit especially because local weather, solar, load, and storage dynamics can be integrated into a single operating twin without the complex feeder and system modeling required for grid-connected sites. The physics is simpler; the stakes are high; and the modeling improvement from a faithful twin translates directly into reduced diesel consumption, fewer unplanned outages, and extended battery life.

---

## 6. Competitive Landscape

The solar-plus-storage resilience and microgrid dispatch software market is active. The following six platforms represent the current commercial and academic benchmark set against which τ-enabled tools would need to differentiate.

### Tesla Powerpack + Autobidder

Tesla's Powerpack system is a commercial benchmark for large-scale battery storage, and Autobidder is its automated dispatch and market-bidding software. Tesla has deployed large-scale battery storage systems in Australia (Hornsdale), the United States, and internationally, with Autobidder providing rule-based and optimization-driven dispatch for energy arbitrage and ancillary services. Autobidder's strengths are in market-facing revenue optimization and fast-response dispatch for frequency and voltage services. Its limitations for the resilience use case are that it is optimized for grid-connected arbitrage rather than physics-faithful survivability planning, it does not integrate weather-to-irradiance-to-battery dynamics as a unified physical twin, and its resilience planning capabilities are rule-based rather than structurally derived. For critical-facility survivability under multi-day storm scenarios, Autobidder's design philosophy does not address the core gap τ is intended to fill.

### Schneider Electric EcoStruxure Microgrid

Schneider Electric's EcoStruxure Microgrid Advisor and related platforms provide integrated microgrid management including real-time control, islanding capability, protection coordination, and energy management. EcoStruxure is widely deployed in hospital campuses, data centers, industrial sites, and utility substations. Its strengths are in real-time control and islanding — particularly the operational transition from grid-connected to islanded mode and the protection logic required to execute that transition safely. Its limitations are on the planning side: EcoStruxure does not provide long-horizon weather-resilience optimization, does not treat weather-to-PV-to-storage dynamics as a unified physical twin, and offers limited probabilistic survivability analysis for multi-day outage scenarios. The platform is operationally strong but planning-shallow.

### Bloom Energy Server + Grid Intelligence

Bloom Energy's solid oxide fuel cell systems (running on natural gas, biogas, or hydrogen) provide highly reliable on-site generation with minimal fuel storage constraints. Bloom's Grid Intelligence platform manages dispatch and grid interaction. Bloom is often used in hospitals, data centers, and food production facilities where availability requirements are extremely high. Its strengths are exceptional reliability for continuous baseload and backup generation independent of solar conditions. Its limitations for the solar-plus-storage resilience use case are that Bloom systems are not solar-coupled by design, do not provide physics-faithful solar-weather-storage modeling, and are not well-suited to community resilience hubs, remote microgrids, or facilities where cost-per-kWh and decarbonization are primary drivers alongside reliability.

### Swell Energy VPP (now part of Swell)

Swell Energy operates a virtual power plant platform aggregating residential and small commercial battery fleets to provide demand flexibility and grid services. Swell's strengths are in demand-side flexibility at scale — aggregating thousands of Enphase, Tesla Powerwall, and similar residential systems to respond to utility dispatch signals. Its limitations are that the VPP model is fundamentally a demand-flexibility tool, not a physics-faithful grid modeling platform. Swell does not provide outage survivability analysis, does not model weather-to-storage dynamics at the physical level, and is not designed for critical-facility resilience or microgrid management. It addresses a different problem in the portfolio.

### HOMER Energy (UL Solutions)

HOMER Pro is the closest existing analog to the long-horizon planning role τ could play in this domain. HOMER has been an industry standard for microgrid design and optimization for more than two decades, covering sizing, dispatch strategy comparison, and economic analysis for solar, wind, storage, diesel, and grid-connected configurations. HOMER's strengths are broad technology coverage, well-validated cost models, and a large installed user base among project developers, NGOs, utilities, and researchers. Its limitations are directly relevant to the τ opportunity: HOMER uses deterministic or scenario-sampled optimization rather than a bounded-error physical twin; it does not provide structurally derived survivability envelopes; its weather modeling is statistical rather than physics-derived; and its battery degradation modeling is simplified relative to what a full electrochemical twin would provide. The gap between HOMER's planning outputs and operational reality is a known limitation that practitioners routinely work around. This is the gap τ is positioned to close.

### Ageto Energy / Willowglen Systems

Ageto Energy (acquired by Rolls-Royce Power Systems) and Willowglen Systems provide microgrid controllers, energy management systems, and SCADA platforms for off-grid, hybrid, and utility-tied microgrids. These are operational control layer tools — they execute dispatch decisions in real time, manage generator start-stop logic, coordinate battery and inverter behavior, and provide operator visibility. Their strengths are reliable real-time control and proven deployment in remote and hybrid systems. Their limitations are that they are not advanced simulation or planning platforms: they do not provide physics-faithful survivability analysis, do not model weather-to-storage dynamics as a unified twin, and do not support long-horizon resilience planning. They are execution platforms rather than planning and optimization platforms.

### τ differentiator summary

The competitive gap τ is positioned to address is the absence of a **physics-faithful, structurally consistent, bounded-error planning and operational twin** across the full weather-to-storage-to-load chain. HOMER is the closest planning analog but is deterministic and weather-statistical. EcoStruxure is the closest operational analog but is planning-shallow. Tesla Autobidder is the closest dispatch analog but is arbitrage-optimized rather than survivability-grounded. None of these platforms provides the structural consistency across scales that τ is assumed to offer under the strong planning assumption.

---

## 7. Deployment Ladder

### Phase 1 — 0 to 24 months: site-level twins for critical facilities

First-wave deployments should target sites where outage harm is legible, mission continuity is politically visible, and the value of improved survivability analysis is easiest to demonstrate:

- hospitals and healthcare campuses in hurricane, wildfire-PSPS, and winter-storm corridors;
- water and wastewater treatment plants serving populations of 10,000 or more;
- emergency operations centers and public-safety campuses;
- resilience hubs at schools and community centers in underserved or high-outage-risk neighborhoods;
- telecom facilities and data nodes with existing backup power systems;
- and tribal and remote community systems with existing solar-plus-storage.

**Phase 1 deliverables:**
- τ-based outage survivability studies for 10–20 pilot sites with side-by-side comparison to current REopt and HOMER outputs;
- battery pre-charge and dispatch rule sets for storm-preparation scenarios;
- critical-load prioritization maps for multi-tier load shedding;
- and documented accuracy comparisons against historical outage events at each site.

### Phase 2 — 2 to 5 years: utility and city integration

Second-wave deployment connects site twins into utility outage planning, feeder-level restoration planning, city resilience programs, and state and municipal resilience finance mechanisms:

- portfolio-level resilience maps linking critical facilities, hubs, and grid assets on shared feeders;
- resilience-hub siting tools for municipal capital planning;
- feeder reconfiguration studies that explicitly account for distributed PV and storage assets;
- and standard resilience valuation templates usable by public utilities commissions and municipal finance offices.

**Phase 2 deliverables:**
- τ-informed resilience procurement standards for DOE, FEMA, and state energy offices;
- validated feeder-level survivability models for three to five pilot utility service territories;
- and open benchmark validation packages for independent review.

### Phase 3 — 5 to 10 years: regional resilience fabrics

If Phase 1 and Phase 2 succeed, the next step is not simply more sites but **coordinated resilience networks** that treat solar, storage, and load across a region as a coherent physical system:

- clusters of hospitals, shelters, and municipal sites coordinated for mutual support;
- distributed resilience services for medically vulnerable populations at neighborhood scale;
- and restoration-aware DER fleets that actively support local grid recovery rather than only serving individual sites.

---

## 8. Case Studies

### Case Study 1: Australia — Solar-Plus-Storage for Remote Communities (Northern Territory)

**Scale and context.** More than 120 remote Australian communities currently depend on diesel microgrids for electricity. The Northern Territory government has committed to 50% renewable electricity by 2030. Projects on the Gove Peninsula and in the Katherine region have demonstrated that solar-plus-storage can reduce diesel consumption by 50–70% in tropical-climate remote microgrids. The Power and Water Corporation (PWC) manages these remote microgrids; diesel delivered to remote Northern Territory communities costs approximately $0.50–1.20 per kWh including logistics, and communities typically range from 200 to 3,000 people. The Australian Renewable Energy Agency (ARENA) has funded multiple remote community solar programs, and CSIRO's Remote Area Power Supply research has documented the technical and operational constraints of these systems.[^25][^26]

**Baseline problem.** Solar PV intermittency without physics-faithful forecasting causes voltage and frequency instability in island-mode diesel microgrids. Battery dispatch is rule-based — typically simple state-of-charge thresholds — rather than weather-informed and physics-optimized. Diesel backup capacity is over-committed because operators cannot reliably predict how much solar generation will be available during cloudy periods or tropical storms. This over-commitment wastes capital and fuel while also degrading battery cycling efficiency because charging and discharging patterns are not optimized for battery chemistry.

**τ-enabled change.** A physics-faithful solar-battery dispatch twin would provide: accurate multi-hour irradiance forecasts that account for tropical cloud dynamics specific to the Northern Territory; optimized battery dispatch that reduces cycling stress while maintaining adequate reserve margin; reduced diesel backup margin of 20–30% through improved solar availability prediction; and storm-season pre-positioning strategies that charge batteries before forecast cloud events. The estimated financial impact is $500,000–2,000,000 per community per year in reduced fuel and logistics costs, depending on community size and current diesel intensity. For 120 communities, the aggregate fuel cost reduction at the conservative end exceeds $60 million per year — and that excludes the emissions reduction, generator maintenance, and reliability improvement benefits.

**Relevance.** This case study illustrates the remote-microgrid opportunity family (Section 5E) and demonstrates that the HOMER-replacement gap identified in Section 6 is not theoretical. Communities relying on rule-based dispatch are leaving material value on the table in fuel costs, battery life, and reliability. Physics-faithful optimization directly addresses all three.

### Case Study 2: Sub-Saharan Africa — Solar Microgrid Rollout in East Africa

**Scale and context.** More than 600 million people in Sub-Saharan Africa lack reliable electricity access. More than 10,000 solar microgrids have been deployed across Kenya, Tanzania, Ethiopia, and Uganda, operated by commercial mini-grid companies including Powered by Sun (Kenya), PowerGen Renewable Energy, SteamaCo, and CrossBoundary Energy. The World Bank / IFC provides financing through the ESMAP and Scaling Solar programs; GOGLA reports an off-grid solar market exceeding $1 billion per year. A typical community microgrid in this market ranges from 50–500 kW of solar with 100–1,000 kWh of storage serving 200–2,000 customers.[^27][^28][^29][^30]

**Baseline problem.** Microgrid dispatch in this market is predominantly primitive: rule-based charge and discharge thresholds, manual or statistical load forecasting, and no physics-faithful modeling of the weather-to-solar-to-storage chain. Battery degradation is accelerated by sub-optimal cycling — particularly deep cycling during extended cloud periods and inadequate equalization charging in humid tropical environments. Unserved energy events damage the commercial operators' revenue and the communities' trust in the service. Cash flow problems arise when load growth does not match generation assumptions from the initial design, and HOMER-based design tools are used with generic weather data that may not reflect local cloud dynamics or seasonal patterns accurately enough to support bankable project finance.

**τ-enabled change.** A physics-faithful load-solar-storage twin would provide: accurate seasonal and event-driven solar availability forecasting using local atmospheric physics; optimal battery dispatch that reduces depth-of-discharge excursions and extends battery calendar life by 20–40%; reduced unserved energy by 30–50% through better storage management ahead of extended cloud events; improved project finance by providing bankable performance predictions with explicit uncertainty bounds; and micro-utility service agreements tied to auditable performance metrics rather than design-model assumptions. For a $500,000–1,000,000 capital investment in a community microgrid, a 30% reduction in battery degradation rate alone can shift the project economics from marginal to viable by extending the battery replacement cycle.

**Relevance.** This case study illustrates the intersection of the energy-access, remote-microgrid, and development-finance opportunity families. It also demonstrates a specific feature of the τ opportunity in emerging markets: the financing barrier is often not the total capital required but the bankability of the performance predictions. Bounded-error physical twins produce more credible project finance documents than statistical models, and that credibility directly affects the availability and cost of concessional financing.

---

## 9. Finance and Funding Landscape

### 9.1 Major funding programs

**World Bank ESMAP / Lighting Africa.** The World Bank's Energy Sector Management Assistance Program has committed more than $1 billion for off-grid solar and mini-grid deployment in Sub-Saharan Africa and South Asia. Lighting Africa has been operational since 2007 and has catalyzed both grant and commercial capital for off-grid solar markets. ESMAP results-based financing instruments are specifically designed for projects where performance verification is challenging — making them natural candidates for τ-based performance validation.[^27]

**IFC Scaling Solar.** The International Finance Corporation's Scaling Solar program provides a bundled package of financing, risk guarantees, and technical assistance for utility solar and hybrid microgrid projects in developing economies. IFC Scaling Solar has operated in Zambia, Senegal, Ethiopia, Madagascar, and other countries and has been extended to include storage and mini-grid components. The program's emphasis on bankable technical documentation aligns directly with the bounded-error modeling that τ is assumed to provide.[^28]

**USAID Power Africa.** Power Africa is a U.S. government initiative with a goal of adding 30,000 megawatts of new generating capacity and 60 million new electricity connections in Sub-Saharan Africa. Power Africa coordinates across USAID, DOE, OPIC/DFC, and EXIM Bank, and has funded mini-grid development, off-grid solar, and critical-facility energy access projects. Its transaction advisory services and de-risking instruments make it relevant to commercial mini-grid operators seeking to scale.[^29]

**IRENA Climate Promise.** The International Renewable Energy Agency's Climate Promise program supports developing countries in strengthening their nationally determined contributions (NDCs) under the Paris Agreement, including renewable energy deployment financing. IRENA has specifically identified mini-grids and off-grid solar as priorities for energy-access NDC targets in Africa and island developing states.[^30]

**U.S. DOE Loan Programs Office — Section 1706.** The DOE Loan Programs Office's Section 1706 program was established by the Energy Act of 2020 to provide loans and loan guarantees for distributed energy projects serving rural or remote communities, including tribal energy projects. This program is directly relevant to the remote and tribal microgrid opportunity family (Section 5E) and to critical-facility resilience projects in rural areas of the United States.[^31]

**DOE Office of Indian Energy.** The Office of Indian Energy provides grants, technical assistance, and financing for tribal energy projects including microgrids, solar-plus-storage, and off-grid systems. The alignment between tribal energy sovereignty goals and the reliability benefits of physics-faithful dispatch twins is direct.[^24]

### 9.2 Cost scenarios

**Scenario 1: Solar-plus-storage plus τ-twin for 100 remote communities (Sub-Saharan Africa).** Hardware and installation cost for 100 community-scale microgrids (50–500 kW solar, 100–1,000 kWh storage, 200–2,000 customers each): USD 20–50 million total, or $200,000–500,000 per community at the low to mid-range of the market. τ software and modeling layer: estimated USD 2–5 million for initial deployment at this scale. Expected fuel-cost savings: $500,000–2,000,000 per community per year compared to diesel-only baseline. Payback period on incremental τ investment: less than one year at any reasonable cost assumption.

**Scenario 2: Climate-resilient critical facility energy systems in 5 countries.** Covering 500+ critical facilities (hospitals, water plants, emergency shelters) across 5 countries: USD 10–25 million in hardware and installation plus a τ modeling layer of USD 1–3 million. Expected avoided outage cost per facility: $10,000–50,000 per day for hospital-class facilities (per NREL valuation research).[^13][^19] At even one avoided multi-day outage per facility per year, the benefit-to-cost ratio across 500 facilities is substantial.

**Scenario 3: U.S. critical-facility resilience program under DOE LPO Section 1706.** A portfolio of 50 rural and tribal critical-facility microgrids: USD 50–150 million in hardware and installation. τ modeling and dispatch optimization layer: USD 5–10 million. Expected benefit-to-cost ratio: 4:1 to 15:1 depending on critical-service valuation, consistent with NREL's resilience valuation research.[^13][^14]

### 9.3 Revenue and value stacking

Solar-plus-storage systems in grid-connected markets can access multiple value streams simultaneously: energy arbitrage, demand charge reduction, frequency regulation, spinning reserves, capacity payments, resilience value (avoided outage cost), and resilience-hub service contracts with municipalities. A τ-enabled dispatch twin that optimizes across all of these simultaneously — rather than sequentially or heuristically — captures more total value from the same hardware investment, improving returns for commercial operators and public agencies alike.

---

## 10. Public-Good Impact Scenarios Under Realistic-Optimistic τ Deployment

These scenarios are planning inferences, not official forecasts or commitments.

### Scenario 1 — Critical-facility survivability becomes a standard design metric, not a boutique exercise

DOE and NREL tools already quantify resilience in terms of outage survivability and cost of inaction.[^15][^19] A realistic-optimistic consequence of τ deployment is that survivability analysis — with explicit, auditable uncertainty bounds — becomes standard for hospitals, wastewater plants, resilience hubs, telecom nodes, and emergency shelters in high-outage-risk regions. The threshold shifts from "we don't know how to prove the value" to "we can now show blue-sky and black-sky benefits in one auditable twin."

**Public-good effect:** more facilities designed for multi-day continuity; less dependence on diesel-only backup; more transparent and contestable resilience procurement; fewer critical-service failures during major outage events.

### Scenario 2 — Medically vulnerable populations face fewer crisis escalations during outages

If τ enables better siting and operation of neighborhood resilience assets and critical hubs, the realistic-optimistic effect is not that all outage risk disappears but that fewer people are forced into emergency departments or shelters solely to keep essential devices powered. The HHS emPOWER and CDC/ASTHO evidence base[^5][^6] establishes that the current mechanism of harm is predictable and repeatable — which means it is also preventable with better-placed, better-operated resilience assets.

**Public-good effect:** lower emergency-response strain during major outages; lower hospital surge when storm-related outages coincide with storm-related injuries; safer sheltering-in-place for some medically vulnerable residents; and better triage and resource pre-positioning.

### Scenario 3 — Water and wastewater continuity improves during severe-weather outages

EPA and FEMA already treat power continuity for water and wastewater as essential.[^10][^20] Under τ, better outage-duration modeling, pre-event battery charging, and process-aware dispatch could meaningfully improve operational continuity at these facilities, reducing the secondary public-health effects of water service interruption — sewage overflows, loss of fire suppression capacity, dehydration risks — that compound the direct harms of major outage events.

**Public-good effect:** fewer cascading failures from water service interruption; fewer emergency generator and fuel-delivery bottlenecks during regional events; stronger sanitation and public-health continuity during multi-day disasters.

### Scenario 4 — Community resilience hubs become easier to justify and scale

NREL's resilience-hub work and DOE's 2024 resilience workshop both identify the design, metrics, and financing of resilience hubs as open problems.[^9][^17][^21] Under τ, the barrier could shift from "we don't know how to prove the value" to "we can now show blue-sky and black-sky benefits in one auditable twin that regulators, insurers, and community development finance institutions can independently validate."

**Public-good effect:** more neighborhoods — especially in disadvantaged or historically outage-prone areas — with reliable access to cooling, warming, communications, food refrigeration, and device charging during emergencies; more confidence for cities and mission-driven funders to invest.

### Scenario 5 — Utility resilience planning becomes more distributed and less diesel-centric

Utilities and regulators already care about faster service recovery and resilience metrics.[^2][^9][^19] Under τ, they may gain a stronger basis for comparing feeder hardening, substation investment, utility-owned storage, customer-sited resilience assets, and hybrid restoration strategies on a common physically consistent platform. The current mismatch between planning tools and operational reality makes this comparison difficult to do rigorously.

**Public-good effect:** better value for resilience spending; more targeted and defensible hardening investment; and potentially faster restoration for some communities during severe-weather events.

### Scenario 6 — Off-grid and remote communities gain access to physics-faithful dispatch at accessible cost

For the 600 million people in Sub-Saharan Africa lacking reliable electricity, and for the 120+ remote Australian communities depending on diesel microgrids, the marginal value of a physics-faithful dispatch twin is highest precisely because alternative tools are weakest. Rule-based dispatch is the current operational baseline in most of this market. The transition from rule-based dispatch to physics-faithful optimization does not require grid infrastructure upgrades or regulatory reform. It requires only software and modeling capability.

**Public-good effect:** reduced diesel fuel costs and emissions for remote communities; extended battery life and reduced replacement capital; fewer unserved energy events; and stronger project finance for commercial mini-grid operators deploying at scale.

---

## 11. Constraints, Frictions, and Reasons the Transition May Still Be Slow

Even under the strong τ assumption, the following barriers are real and do not disappear with better physics modeling.

### 11.1 Capital, procurement, and financing remain difficult

Resilience projects often fail not because the physics is unknown but because the financing case is hard to assemble. DOE, NREL, and FEMP provide extensive guidance specifically because resilience value is systematically undercounted or difficult to monetize under conventional utility ratemaking and capital planning frameworks.[^13][^19] A better physics twin helps build the business case but does not resolve the institutional barriers to financing and procurement.

### 11.2 Physical engineering and interconnection constraints do not disappear

Improved modeling does not remove the need for safe switchgear design, interconnection studies, protection coordination, fire-code compliance, battery enclosure safety, operational training, and ongoing maintenance. These are irreducible physical and regulatory constraints. τ reduces modeling uncertainty; it does not reduce installation complexity.

### 11.3 Community governance and equity are not physics problems

Resilience hubs and critical-facility systems fail socially when governance is weak, access is inequitable, or emergency protocols are unclear. NREL's resilience-hub and utility-guidance work both emphasize stakeholder coordination, community planning, and equitable access as prerequisites for effective deployment.[^17][^21] Physics-faithful modeling is a necessary but not sufficient condition for social effectiveness.

### 11.4 Cybersecurity and control integrity become more important as systems become more active

The more a resilience system becomes coordinated, networked, and remotely dispatched, the more control integrity and cybersecurity matter. A physics-faithful twin that is also a control surface is a more attractive attack target than a passive battery system. This is a design and policy requirement, not an argument against the technology.

### 11.5 τ does not remove every uncertainty

Even with a faithful physical twin, residual uncertainties remain around equipment failure (particularly battery module failures and inverter faults that are hard to predict from electrochemical models alone), human operations and decision errors, fuel delivery for hybrid systems in extended grid outages, component degradation at timescales beyond the modeling horizon, and rare event combinations that are outside the training distribution of any physical model. τ may reduce modeling uncertainty substantially. It does not eliminate operational uncertainty.

---

## 12. Governance and Public-Interest Guardrails

### 12.1 Critical-load transparency

Any public-interest deployment should make explicit which loads are protected, for how long, under what weather and event assumptions, and with what survivability probability. Opaque resilience claims — "this system provides backup power" without specifying duration, conditions, and load priority — are inadequate for critical-facility procurement and should be replaced with auditable survivability specifications.

### 12.2 Equity-aware siting

The strongest social case for resilience hubs and critical-facility systems lies in communities with high outage risk, high vulnerability, or weak existing backup options. DOE and NREL resilience programs increasingly recognize this, and the Justice40 Initiative creates federal policy alignment.[^9][^17][^21] τ-enabled resilience planning should incorporate equity metrics alongside survivability metrics in siting and prioritization decisions.

### 12.3 Open benchmark validation

Utilities, regulators, and communities should be able to validate benchmark claims independently. Proprietary black-box resilience models that cannot be audited by regulators or challenged by communities are not consistent with public-interest deployment. τ-based tools should be deployable with open benchmark suites comparable to NREL's published REopt validation datasets.

### 12.4 Blue-sky/black-sky accountability

Systems sold on resilience value should be evaluated on everyday bill and emissions performance, system readiness and maintenance state, and actual outage behavior when events occur — not only on design-time modeling outputs. This requires metering, reporting, and accountability frameworks that go beyond installation certificates.

### 12.5 Avoid resilience-washing

There is a documented risk of systems being marketed as "resilience" without clear survivability evidence — particularly in community resilience hub and critical-facility markets where buyers may lack technical sophistication. τ should be used to tighten survivability standards, not to add a new layer of complexity that obscures whether a system actually works.

---

## 13. Benchmark Suite

A serious public-interest deployment program would require transparent, independently verifiable benchmark problems. The following five benchmarks address the core use cases of this paper.

### Benchmark 1 — Seven-day hospital campus outage survivability

Model a hospital campus with defined PV capacity, battery storage, critical-load tiers (life safety, clinical operations, administrative), and a multi-day outage window across multiple seasonal weather profiles. Compare current design methods, current REopt probabilistic survivability outputs, and τ-based survivability envelopes and dispatch strategies. Metric: probability of sustaining critical loads at each tier through day 7 under 100 independent weather scenarios.

### Benchmark 2 — Wastewater plant continuity under wildfire-season PSPS conditions

Use a real wastewater plant load profile, PSPS-style outage risk window (3–7 days), and weather-informed solar availability during California or Pacific Northwest wildfire season. Compare diesel-only backup, solar-plus-storage with rule-based dispatch, and τ-optimized dispatch. Metrics: total unserved energy, critical-process continuity, diesel consumption, battery state-of-health trajectory.

### Benchmark 3 — Community resilience hub blue-sky/black-sky co-optimization

Benchmark a resilience hub site (school or community center, 50–200 kW solar, 100–400 kWh storage) across three simultaneous objectives: daily bill management and peak shaving; grid-services participation; and black-sky shelter operations for 3–5 days. Metric: Pareto frontier of economic value versus survivability probability versus shelter-service days.

### Benchmark 4 — Grid-forming restoration sequence on a campus microgrid

Test mode-transition logic for a campus with grid-forming inverters: grid-connected normal operation, planned and unplanned islanding transitions, stable islanded operation under variable solar and load, and staged restoration reconnection. Metrics: transition time, frequency deviation, voltage stability, critical-load continuity through transitions.

### Benchmark 5 — Remote community microgrid optimization (Northern Territory profile)

Model a 200-person remote community with 150 kW solar, 300 kWh storage, and diesel backup under Northern Territory tropical weather including cloud events and wet-season irradiance profiles. Compare rule-based dispatch baseline with τ-optimized dispatch. Metrics: diesel consumption reduction, battery cycling depth, unserved energy events, annual fuel cost.

---

## 14. Integration with the Broader τ Solar Portfolio

This paper (Paper 3) sits within a five-paper solar portfolio that collectively spans the full scope of τ implications for solar energy systems. The portfolio is designed to avoid duplication while ensuring that the connections between papers are explicit.

**Paper 1** (solar forecasting for bulk-grid operations) establishes the foundational claim that τ provides a physics-faithful irradiance forecasting capability. Paper 3 inherits that capability and applies it to the resilience and storage dispatch context. The connection is direct: better irradiance forecasting is the upstream input to better battery pre-charge decisions and survivability planning.

**Paper 2** (distributed PV visibility and distribution-grid orchestration) addresses the utility's view of rooftop and distributed solar. Paper 3 addresses the facility operator's view of on-site solar-plus-storage. The two papers overlap in the feeder-level resilience opportunity (Section 5D) where utility and customer assets interact.

**Paper 4** (PV asset protection and long-term system planning) addresses physical durability, storm-hardening, and asset degradation. Paper 3 addresses operational dispatch and survivability during outage events. The connection is that a physics-faithful twin used for dispatch (Paper 3) and a physics-faithful twin used for asset degradation modeling (Paper 4) should be computationally consistent — they are different outputs of the same underlying physical model.

**Paper 5** (solar-synchronized flexible demand and grid logistics) addresses demand-side response synchronized to solar variability. Paper 3 addresses supply-side storage dispatch. Together, Papers 3 and 5 address the full solar-plus-storage-plus-demand flexibility system that is the next-generation grid architecture.

---

## 15. Bottom Line

Solar-plus-storage, microgrids, and critical-infrastructure resilience are one of the clearest near-term τ deployment stories because the external institutions that fund, regulate, and operate this domain have already articulated the demand for exactly the capability τ is assumed to provide.

Official institutions already know the pieces:

- solar-plus-storage can keep power available during outages and grid-forming inverters may eventually help restart portions of the grid;[^1][^23]
- resilient distribution systems can use PV and storage to reconfigure power flows and recover service more quickly after disruptions;[^2]
- critical facilities — hospitals, water plants, shelters — need multi-day continuity during major outages;[^10]
- over 3 million medically vulnerable Americans rely on electricity for life-sustaining equipment at home;[^5][^6]
- and resilience valuation matters because the cost of inaction is real, legible, and rising.[^13][^19]

What τ adds, under the strong planning assumption, is a step change from the current fragmented toolchain — separate weather models, separate PV models, separate battery models, separate load models, stitched together with simplifying approximations at each interface — toward something closer to a **bounded, law-faithful resilience twin** that maintains physical consistency across the full weather-to-storage-to-load chain.

If that assumption is correct, one of the most practical public-good consequences of the τ framework may be this: it could make resilient electricity for critical services easier to design, easier to finance, and more reliable to operate.

That would matter for hospitals, water utilities, medically vulnerable households, emergency shelters and resilience hubs, remote communities in Australia and East Africa, utilities navigating rising outage burdens, and the 600 million people in Sub-Saharan Africa still waiting for reliable power. In a world of rising weather disruption, rising electrification, and rising dependence on electricity for life-critical services, that is not a niche benefit. It is foundational.

---

## References

[^1]: U.S. Department of Energy, *Solar and Resilience Basics* (accessed 2026-03-07). <https://www.energy.gov/eere/solar/solar-and-resilience-basics>

[^2]: U.S. Department of Energy, *Resilient Distribution Systems Powered by Solar Energy* (accessed 2026-03-07). <https://www.energy.gov/eere/solar/resilient-distribution-systems-powered-solar-energy>

[^3]: U.S. Energy Information Administration, *Hurricanes in 2024 led to the most hours without power in the United States in 10 years* (2025), including the 11-hour average interruption figure and the 80% major-event share. <https://www.eia.gov/todayinenergy/detail.php?id=66744>

[^4]: NOAA National Centers for Environmental Information, *Billion-Dollar Weather and Climate Disasters* and *Assessing the U.S. Climate in 2024* (2025), reporting 27 billion-dollar disasters in 2024. <https://www.ncei.noaa.gov/access/billions/> and <https://www.ncei.noaa.gov/news/national-climate-202413>

[^5]: HHS emPOWER Program, *About the HHS emPOWER Program* and *HHS emPOWER Map Job Aid* (accessed 2026-03-07), reporting coverage of over 4.6 million Medicare beneficiaries and more than 3 million with claims for electricity-dependent durable medical equipment. <https://empowerprogram.hhs.gov/about.html> and <https://empowerprogram.hhs.gov/Map-Job-Aid.pdf>

[^6]: ASTHO / CDC-supported report, *Advancing Preparedness for Life Support Users During Power Outages* (2023), including the Texas-grid-failure ambulance-call example and the Hurricane Sandy emergency-department surge example. <https://stacks.cdc.gov/view/cdc/149778>

[^7]: U.S. Energy Information Administration, *U.S. battery capacity increased 66% in 2024* (2025), reporting cumulative utility-scale battery storage above 26 GW in 2024. <https://www.eia.gov/todayinenergy/detail.php?id=64705>

[^8]: U.S. Energy Information Administration, *New U.S. electric generating capacity expected to reach a record high in 2026* (2026), including planned 24 GW of utility-scale battery additions and 43.4 GW of utility-scale solar additions in 2026. <https://www.eia.gov/todayinenergy/detail.php?id=67205>

[^9]: U.S. Department of Energy Solar Energy Technologies Office, *2024 Workshop: Solar and DERs for Community Energy Resilience* pre-read and agenda (2024). <https://www.energy.gov/sites/default/files/2025-01/Resilience_Workshop_Pre-Read%20Material%20and%20Agenda.pdf>

[^10]: FEMA, *Power Outage Incident Annex to the Response and Recovery Federal Interagency Operational Plans* (2017), including references to hospitals, water treatment plants, wastewater treatment plants, and shelters. <https://www.fema.gov/sites/default/files/documents/fema_incident-annex_power-outage.pdf>

[^11]: NREL, *Resilience Valuation and Planning for Solar and Storage on Critical Infrastructure* (2024). <https://www.nrel.gov/docs/fy24osti/90010.pdf>

[^12]: NREL, *Enhancing Resilience at Critical Facilities through Solar, Storage, and Microgrids* (2025). <https://www.nrel.gov/docs/fy25osti/91764.pdf>

[^13]: DOE Office of Indian Energy / NREL, *Valuing the Resilience Provided by Solar and Battery Energy Storage Systems* (2017), showing that including resilience value materially changes cost-optimal PV and storage sizing. <https://www.energy.gov/indianenergy/articles/valuing-resilience-provided-solar-and-battery-energy-storage-systems>

[^14]: NREL, *Resilience and economics of microgrids with PV, battery storage, and networked diesel generators* (2020). <https://www.nrel.gov/docs/fy21osti/78837.pdf>

[^15]: NREL, *REopt Lite Tutorial: Resilience Outputs* (2020), illustrating outage survivability probability metrics including a seven-day outage example. <https://docs.nrel.gov/docs/fy20osti/76678.pdf>

[^16]: NREL, *Microgrids for Energy Resilience: A Guide to Conceptual Design and Lessons from Defense Projects* (2019). <https://www.nrel.gov/docs/fy19osti/72586.pdf>

[^17]: NREL, *Ensuring Resilient Operations of Solar-Plus-Storage Community Resilience Hubs* (2024). <https://www.nrel.gov/docs/fy24osti/89601.pdf>

[^18]: U.S. Department of Energy, *Better Climate Challenge Partner Valley Children's Healthcare Installing Renewable Energy Microgrid* (2024), including the 80% energy-demand and >50% emissions-reduction figures. <https://www.energy.gov/cmei/articles/better-climate-challenge-partner-valley-childrens-healthcare-installing-renewable>

[^19]: U.S. Department of Energy FEMP, *Estimate the Value of Resilience with the Customer Damage Function Calculator* (2023). <https://www.energy.gov/femp/articles/estimate-value-resilience-customer-damage-function-calculator>

[^20]: U.S. Environmental Protection Agency, *Power Resilience: Guide for Water and Wastewater Utilities* (2019/2023). <https://www.epa.gov/system/files/documents/2023-05/PowerResilienceGuide_2023_508c.pdf>

[^21]: NREL / RMI, *Guidance on Utility Options to Support Commercial Solar and Solar+Storage Deployment in Underserved Communities* (2024), use cases on outage survivability and community resilience hubs. <https://www.nrel.gov/docs/fy24osti/89918.pdf>

[^22]: NREL, *Sabathani Community Center Solar + Battery Resilience Hub* (2024). <https://docs.nrel.gov/docs/fy24osti/88960.pdf>

[^23]: U.S. Department of Energy, *Powering On with Grid-Forming Inverters* (2021), on inverter-based resources helping restart the grid independently. <https://www.energy.gov/eere/solar/articles/powering-grid-forming-inverters>

[^24]: U.S. Department of Energy Office of Indian Energy, *Microgrids* (accessed 2026-03-07). <https://www.energy.gov/indianenergy/tribal-energy-guide/microgrids>

[^25]: Australian Renewable Energy Agency (ARENA), *Remote Area Energy Supply (RAES) program and remote community solar projects* (2022–2024). <https://arena.gov.au/knowledge-bank/remote-area-energy-supply/>

[^26]: CSIRO, *Remote Area Power Supply research and off-grid hybrid energy systems* (accessed 2026-03-07). <https://www.csiro.au/en/research/technology-space/energy/remote-area-power-supply>

[^27]: World Bank / ESMAP, *Off-Grid Solar Market Trends Report 2022* (2022), including mini-grid market data and financing instruments for Sub-Saharan Africa. <https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099923312212239759>

[^28]: IFC Scaling Solar, *Scaling Solar program overview and results* (accessed 2026-03-07). <https://www.ifc.org/en/projects-transactions/programs/scalingsolar>

[^29]: USAID Power Africa, *Power Africa overview and transaction advisory services* (accessed 2026-03-07). <https://www.usaid.gov/powerafrica>

[^30]: IRENA, *Off-grid Renewable Energy Solutions: Global and Regional Status and Trends* (2018) and IRENA Climate Promise documentation (accessed 2026-03-07). <https://www.irena.org/publications/2018/Oct/Off-grid-renewable-energy-solutions>

[^31]: U.S. Department of Energy Loan Programs Office, *Section 1706: Energy Infrastructure Reinvestment and Community Lender program* (accessed 2026-03-07). <https://www.energy.gov/lpo/energy-infrastructure-reinvestment>


---

*Source: Full manuscript text integrated from companion paper draft.*
