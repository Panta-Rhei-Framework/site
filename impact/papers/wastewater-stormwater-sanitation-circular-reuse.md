---
layout: impact-paper
title: τ for Wastewater, Stormwater, Sanitation, and Circular Water Reuse
permalink: /impact/papers/wastewater-stormwater-sanitation-circular-reuse/
paper_id: companion-water-wash-paper-3
portfolio_id: impact-water-wash
summary_short: A companion paper on how τ could improve wastewater treatment intelligence,
  stormwater management, sanitation system optimization, and circular water reuse.
right_rail:
  meta:
    type: Companion Paper
    portfolio: Water Wash
    status: Conditional
    updated: April 2026
---

# τ for Wastewater, Stormwater, Sanitation, and Circular Water Reuse
**Companion Dossier — Panta Rhei Impact: Water/WASH Portfolio**
**Paper 3 of 5 · Status: Yellow Paper · March 2026**

---

## Executive Summary

Sanitation and wastewater management represent one of the most consequential unresolved infrastructure deficits in the world. UN-Water's 2024 wastewater update reports that **42% of household wastewater** — approximately **113 billion m³ per year** — was discharged without safe treatment in 2022.[^4][^5] In low-income countries, the untreated fraction approaches 95%.[^4] WHO and UNICEF's Joint Monitoring Programme reports that **3.6 billion people** still lack safely managed sanitation services, including 354 million still practising open defecation.[^1][^2] WWAP data indicates that wastewater treatment accounts for 1–3% of national electricity consumption in developed nations — a figure set to rise as systems scale up without energy-efficiency tools. Meanwhile, climate change is intensifying combined sewer overflows and urban flooding, overwhelming wastewater systems in cities that already operate at the edge of their design capacity. The circular water reuse market is projected to exceed **USD 25 billion by 2030**, yet most systems cannot yet safely and reliably predict the quality windows and treatment performance needed to unlock that value at scale.[^10]

The sector already understands the right conceptual direction. WHO's Sanitation Safety Planning framework defines a risk-based, chain-wide approach spanning containment, conveyance, treatment, and end use.[^6][^7] The World Bank's Citywide Inclusive Sanitation initiative recognizes that universal safely managed sanitation cannot be delivered by conventional sewerage alone.[^8] EPA's 2025 reuse guidance explicitly supports risk-based microbial treatment targets across potable and non-potable reuse streams.[^11][^12] These institutions know the mission. What they lack is a physics-faithful, bounded-error, operationally deployable twin of the full sanitation–stormwater–reuse system.

This dossier asks a single focused question: **if the τ framework provides such a twin — law-faithful, coarse-grainable, structurally bounded in error — what public good could that unlock for wastewater, stormwater, sanitation, and circular water reuse?**

Six findings structure the answer.

**Finding 1 — The scale of the untreated-wastewater burden makes even modest improvements enormously valuable.** On a baseline of 113 billion m³ per year of household wastewater discharged without adequate treatment, a 1–3% reduction corresponds to 1.1–3.4 billion m³ per year of avoided unsafe discharge. WHO estimates that every USD 1 invested in sanitation returns USD 5.5 in economic benefit. The public-good case does not require solving the entire gap — it requires measurably moving the needle in the places where physics-faithful prediction changes decisions.

**Finding 2 — τ's decisive structural advantage in this domain is bounded-error, chain-wide causal fidelity.** Today's wastewater and stormwater tools are strong within their original design scope — either plant operations or hydraulic simulation — but degrade under stress, under combined sewer–stormwater interaction, and under the dynamic inflow and pollutant variability that climate change is amplifying. A τ twin that remains structurally faithful as the system is coarsened or extended across the full sanitation chain would change the character of operational confidence exactly where current tools are weakest.

**Finding 3 — Combined sewer overflow and urban wet-weather failure is the highest public-health and resilience insertion point.** In dense cities with combined systems, the interface between stormwater and sewage is where the largest and least predictable public-health harm occurs. Cities like Jakarta, where 60% of the population relies on septic tanks and annual flooding affects 25–40% of the city, illustrate the stakes. A τ wet-weather twin that predicts overflow volumes and timing 6–12 hours ahead enables pre-event intervention — pump activation, flow diversion, public-health advisories — that current tools cannot reliably support.

**Finding 4 — Advanced water reuse programs at national scale require exactly the predictive quality assurance that τ would provide.** Singapore's NEWater program — 130+ million gallons per day from 5 plants, supplying 40% of national water demand — demonstrates that large-scale water reuse is operationally achievable. What it also demonstrates is that continuous multi-parameter monitoring and predictive treatment-performance modeling under varying feed quality are the limiting factors as programs scale. τ-enabled membrane performance and trace-contaminant breakthrough prediction would reduce testing frequency while maintaining safety and reduce reverse osmosis energy use by an estimated 10–20%.

**Finding 5 — The competitive landscape has structural ceilings that τ directly addresses.** Veolia IntelliSense, Xylem/Flygt, InfoWorks ICM, MIKE+ URBAN, EPA SWMM, and OmniSite/Grundfos iSOLUTIONS are each strong within defined domains — plant operations, hydraulic simulation, pump monitoring, or design-stage modeling. None provides physics-faithful, real-time, operationally coupled coverage of the full sanitation–stormwater–reuse chain with structurally bounded error. The τ proposition addresses a structural gap in the incumbent landscape, not incremental improvement within an existing category.

**Finding 6 — Finance mechanisms are already aligned with this capability gap.** The World Bank Water Global Practice lends USD 3 billion or more per year to wastewater treatment and reuse. ADB, GCF, and US EPA WIFIA provide additional aligned capital. Conservative benefit-to-cost ratios — USD 5.5 per USD 1 in sanitation, and wastewater reuse at USD 0.80–1.20/m³ against desalination at USD 1.50–2.50/m³ — make the investment case tractable without optimistic assumptions.

The core public-good proposition is precise: a sanitation system that can predict its own failure modes — overflow, treatment bypass, reuse quality windows, treatment-plant overload — is a sanitation system that can protect more people, recover faster from climate shocks, and redirect capital more intelligently. That is what τ claims to enable. This dossier maps the consequences if that claim is sound.

---

## 1. Reader Stance, Scope, and Caveat Structure

This paper adopts a deliberate planning stance, stated explicitly at the outset so that its arguments can be read with appropriate calibration.

The stance is: **assume, for planning purposes, that the strongest τ claims relevant to wastewater hydraulics, stormwater interactions, sanitation-chain behavior, and reuse safety are sound**, and ask what practical and public-good consequences would follow if those capabilities were integrated into urban sanitation, wastewater, stormwater, and reuse systems. The paper does not assert that the broader water engineering or public-health communities have accepted the τ framework. It asks what would follow if the framework were true enough to matter operationally, and maps those consequences against what official institutions already want and already fund.

Three categories of claim are kept strictly distinct throughout:

- **What official institutions already know and already want** — the empirical baseline, drawn from WHO, UNICEF, UN-Water, EPA, World Bank, and equivalent sources.
- **What τ would newly provide under the assumption** — the planning inference layer, clearly labeled as such throughout.
- **What impact estimates are planning inferences rather than official forecasts** — quantified with conservative public-value anchors wherever possible and flagged explicitly.

This is a **yellow paper**. It is assumption-led, deployment-oriented, and public-good framed. It does not claim operational validation on real wastewater systems has occurred. That validation is precisely the purpose of the benchmark suite and pilot structure described in Sections 7 and 8.

### Scope of This Paper

This is **Paper 3 of 5** in the τ Water, WASH, and Basin Intelligence portfolio. It focuses exclusively on:

- wastewater collection and treatment;
- sewer and stormwater interaction and combined sewer overflow;
- sanitation-chain safety from containment to end use or disposal;
- fecal sludge and decentralized sanitation pathways;
- circular water reuse and resource recovery;
- urban resilience and public-health protection through sanitation intelligence.

### Explicitly Out of Scope for Paper 3

- **Paper 1:** source-water protection, drinking-water treatment, and quality early warning
- **Paper 2:** drinking-water distribution, leakage, pressure management, and service continuity
- **Paper 4:** river-basin, groundwater, drought–flood allocation, and water productivity
- **Paper 5:** WASH in health facilities, schools, emergency camps, and climate-vulnerable settlements

---

## 2. Why Wastewater, Stormwater, Sanitation, and Reuse Is a First-Tier τ Opportunity

### 2.1 The Sanitation Access Gap Remains Massive

The latest WHO/UNICEF JMP update reports that **3.6 billion people** lacked safely managed sanitation in 2024.[^1][^2] Within that total, roughly 1.9 billion used only basic services, approximately 560 million used limited shared facilities, about 555 million used unimproved facilities, and 354 million still practised open defecation.[^1][^2] This is not a marginal service gap. It is one of the largest remaining infrastructure and public-health deficits in the world, with direct consequences for diarrhoeal disease burden, child mortality, maternal health, school attendance, and economic productivity.

WHO's sanitation fact sheet states that poor sanitation is linked to the transmission of diseases including cholera, diarrhoea, dysentery, hepatitis A, typhoid, and polio, and that approximately 494 000 people die annually from diarrhoea linked to unsafe sanitation.[^3]

### 2.2 The Untreated-Wastewater Burden Is Globally Severe

UN-Water's 2024 wastewater update reports that **42% of household wastewater** was not safely treated in 2022, releasing an estimated **113 billion m³** with inadequate or no treatment into the environment.[^4][^5] In low-income countries, the share of wastewater discharged untreated approaches 95%.[^4] This untreated fraction is not simply a treatment-plant performance problem. It reflects incomplete collection, unsafe disposal pathways in non-sewered settlements, and combined sewer systems overwhelmed during wet weather. The consequences link sanitation directly to river and coastal pollution, downstream drinking-water stress, ecosystem degradation, and the loss of potentially valuable water, nutrients, and energy.

### 2.3 Energy Consumption in Wastewater Treatment Is Both Large and Improvable

WWAP data indicates that wastewater treatment accounts for **1–3% of national electricity consumption** in developed countries — a figure that will grow as systems expand to serve previously unserved populations and as climate variability increases treatment complexity.[^15] This makes wastewater treatment a significant and underappreciated energy sector, one in which even modest efficiency improvements at scale carry meaningful climate and economic value. A physics-faithful operational twin that can optimize aeration, chemical dosing, and sludge processing in real time under dynamic inflow conditions represents a direct path to measurable energy savings.

### 2.4 Stormwater and Sanitation Are Operationally Entangled

EPA's combined-sewer guidance explains the problem directly: in a combined system, wastewater and stormwater share the same pipes, and during wet weather the combined flow can overwhelm the system, causing overflow at permitted relief points.[^13] So stormwater is not an external side issue. In many urban systems it is literally part of the same physical and public-health problem. This is why this paper treats wastewater and stormwater together: the hardest urban problems live at their interface — surcharge, flooding, combined sewer overflow, treatment overload, pollutant wash-in, and cascading impacts on receiving waters and neighborhoods. Separating them analytically produces incomplete answers.

Climate change is intensifying this entanglement. More frequent and more intense precipitation events mean more combined sewer overflow, more treatment-plant overloads, and greater public-health exposure from sewage backup and urban flooding. The systems that most need improved prediction are precisely the systems for which existing tools provide the least useful operational guidance.

### 2.5 Circular Water Use Is No Longer Peripheral

WHO's sanitation fact sheet states explicitly that wastewater and sludge are increasingly seen as valuable resources in the circular economy, providing reliable water, nutrients, and recovered energy — while warning that much current use remains unsafe without adequate treatment and controls.[^3] The World Bank's 2025 Scaling Water Reuse analysis sharpens the implementation side: the business case is often strongest where used water is generated close to demand, particularly in urban centres and industrial parks.[^10] EPA's 2025 reuse framework provides technical support for risk-based microbial treatment targets across potable and non-potable reuse contexts.[^11][^12] The circular water reuse market is projected to exceed USD 25 billion by 2030 as water scarcity and regulatory support converge.[^10]

Reuse is no longer a fringe sustainability concept. It is becoming a mainstream urban water-security strategy — and its safe and reliable expansion depends directly on the quality of predictive treatment-performance modeling.

### 2.6 The Sanitation Field Already Has the Right Risk-Management Philosophy

WHO's Sanitation Safety Planning framework is one of the clearest signs that the sector already knows the correct conceptual direction.[^6][^7] SSP is not a narrow plant-operations checklist. It is a risk-based method spanning the full sanitation chain: containment, conveyance, treatment, and end use or disposal. It applies both to centralized sewered systems and to decentralized non-sewered pathways, and it is explicitly linked to the WHO Water Safety Planning tradition — the same chain-wide risk model that has proven effective in drinking-water management.

That means the sector already wants exactly what τ claims to be able to provide better: **chain-wide causal understanding with intervention-oriented risk management, backed by bounded-error prediction of failure-mode timing and severity**.

### 2.7 Climate Resilience and Sanitation Can No Longer Be Separated

The World Bank's 2025 sanitation work defines climate-resilient sanitation as services that can anticipate, respond to, recover from, adapt to, or transform under climate-related disturbances while still pursuing universal safely managed sanitation.[^9] Its companion case-study work stresses that integrating circular-economy principles into sanitation improves both resilience and wider environmental, social, and economic outcomes.[^14] Climate change is not a future challenge for sanitation systems: it is already measurable in more frequent combined sewer overflows, more intense fecal sludge management crises during floods, more frequent treatment-plant overloads, and more compromised receiving-water quality. Paper 3 is therefore simultaneously about wastewater engineering, urban resilience, climate adaptation, and public health.

---

## 3. What τ Would Change Under the Working Assumption

Under the strongest τ assumption, the improvement is not a somewhat better sewer model or a somewhat better treatment forecast. It is a more radical operational shift:

> **cities and sanitation systems would gain access to a law-faithful, bounded-error twin of collection, conveyance, treatment, overflow behavior, sanitation-chain risk, and regulated reuse opportunities — one that remains structurally faithful as the model is coarsened or extended, and that degrades gracefully rather than catastrophically under stress.**

In practical terms, that means six concrete changes.

### 3.1 Collection-to-Discharge Behavior Becomes Predictive Rather Than Reactive

Today, most sanitation systems infer trouble from flooding complaints, plant overload events, pump alarms, episodic grab sampling, overflow notices to regulators, and operator experience accumulated over time. The detection is often post-hoc. Intervention is reactive. Under τ, the system could become far more predictive: where surcharge is likely before it occurs, when combined flow will overwhelm conveyance capacity, which assets are most vulnerable under a forecast storm sequence, and which receiving waters are about to experience pollutant spikes. This is the shift from operations-as-monitoring to operations-as-anticipation.

### 3.2 Sewer and Stormwater Become One Operational Picture

In ordinary practice, sewer operations, stormwater drainage, and urban flood control are institutionally and analytically separate. Sewer operators do not generally run stormwater models. Stormwater engineers do not generally operate wastewater treatment plants. Under τ, the shared physical logic of these systems becomes much more explicit: inflow and infiltration change treatment burden; storm pulses change pollutant concentration and timing; blocked or undersized drainage amplifies sewer backflow; and flood pathways often carry contamination into homes, schools, and streets. A strong τ twin would allow operators, city planners, and emergency managers to see the combined sewer–stormwater–flood system as one coupled physical problem and to intervene in it as one coupled operational problem.

### 3.3 The Sanitation Chain Becomes Formally Manageable from Containment to End Use

WHO's SSP framework already defines the chain correctly.[^6][^7] What is often missing is a physically grounded, bounded-error execution layer — a tool that can predict risk accumulation and failure probability at each link from household containment through final disposal or reuse, rather than applying static hazard scores and periodic inspections. Under τ, sanitation-chain intelligence could cover onsite pits and tanks, sewered collection networks, fecal-sludge transport logistics, treatment unit processes, sludge handling, regulated reuse pathways, and final discharge. This is especially important — and especially underprovided by current tools — in cities where sewered and non-sewered systems coexist and where the failure modes of each interact.

### 3.4 Decentralized and Citywide Inclusive Sanitation Becomes Seriously Plannable

The World Bank's CWIS framework exists because universal safely managed sanitation cannot be reached by assuming conventional sewerage is the only valid solution.[^8] That makes physical planning much more complex: cities need to compare and orchestrate centralized and decentralized, sewered and onsite, permanent and staged solutions — often simultaneously in different neighborhoods with different tenure, density, and infrastructure histories. Under τ, these comparisons become much more testable: where sewer expansion is cost-justified, where decentralized treatment is safer and cheaper, where fecal sludge routing should be prioritized, where stormwater and sanitation networks should be separated, and how staged upgrades can move a city toward universal safely managed sanitation without system collapse at any transition point.

### 3.5 Regulated Reuse Becomes a Live Operational Option

With τ, reuse planning would no longer be limited to broad concept studies and annual quality reports. It could become an operational layer that asks, in near-real-time: what source water is available at what quality, what treatment target is needed for a specific reuse application, what industrial or environmental demand exists within transmission distance, and how does reuse safety change under storm or outage conditions? This is exactly the question EPA's reuse framework and the World Bank's reuse work are trying to support at the policy and engineering level.[^10][^11][^12] The τ contribution would be to make those policy frameworks operationally executable with physics-faithful quality prediction rather than safety-margin conservatism that defers reuse expansion.

### 3.6 Resource Recovery Becomes Easier to Optimize and Justify

WHO and the World Bank both point to the circular value of wastewater and sludge: water recovery, nutrient recovery, and energy recovery.[^3][^14] Under τ, these pathways become more operationally legible: where biogas recovery is energetically worthwhile given sludge volumes and composition, where nutrient recovery has a local off-take that makes the economics work, where reclaimed water can offset freshwater withdrawals at scale, and which recovery mix best improves both climate resilience and system economics given local conditions. This makes the difference between a circular sanitation narrative and a circular sanitation operation.

---

## 4. Structured Opportunity Map

### 4.1 Wastewater Treatment-Plant Optimization Under Dynamic Conditions

This is the clearest immediate operational opportunity and the one most accessible to utilities that already operate advanced SCADA or digital systems. A τ twin could support dynamic process control under highly variable influent quality, storm-event mode switching that preserves treatment performance while shedding peak hydraulic load safely, sludge-line optimization that couples solids loading to digestion capacity, aeration and chemical dosing that responds to predicted influent biochemical oxygen demand rather than lagged sensor signals, plant-energy management that optimizes across treatment train and pumping loads, and compliance risk prediction that flags permit-breach probability hours before a violation occurs.

Best early adopters are larger municipal plants, industrial wastewater facilities with regulated reuse potential, and utilities already operating advanced SCADA or plant-level digital monitoring.

### 4.2 Combined Sewer Overflow and Urban Wet-Weather Intelligence

This is likely the highest public-health and resilience payoff opportunity in dense cities. The physics problem — the joint behavior of stormwater inflow, sewer hydraulics, and treatment-plant capacity during intense rainfall — is exactly the kind of coupled, nonlinear, fast-moving problem where bounded-error prediction changes operational decisions. A τ layer could support CSO event forecasting with meaningful lead time, storage and detention basin optimization, smart gating and pump dispatch before events rather than during them, green and grey infrastructure coordination under storm forecasts, and protected routing information for vulnerable populations when contamination pathways are active.

This is also where stormwater, flood, and sanitation portfolios most naturally overlap, creating shared-benefit arguments for multi-agency investment.

### 4.3 Citywide Inclusive Sanitation and Fecal Sludge Chain Intelligence

This is the strongest equity-focused opportunity in the paper. CWIS recognizes that universal safe sanitation requires tailored mixtures of technologies, service models, and institutional arrangements.[^8] A τ twin could make that operationally real by supporting containment-risk mapping across informal settlements, desludging logistics that optimize routing and scheduling against pit fill rates and treatment capacity, treatment destination matching that aligns fecal sludge quality with treatment facility capabilities, non-sewered service optimization that provides the same chain-wide risk management discipline as formal sewer networks, and phased investment decisions that can model how a city moves progressively toward universal coverage without creating bottlenecks at treatment facilities or disposal sites.

### 4.4 Circular Reuse for Urban Centers and Industrial Clusters

The World Bank's reuse work identifies urban centers and industrial parks as the strongest first business cases — where large volumes of used water are generated close to concentrated demand for non-potable or industrial-grade water.[^10] A τ reuse twin could support fit-for-purpose planning that matches treatment depth to reuse application, microbial and chemical risk control under dynamic influent conditions, demand-matching for cooling water, industrial process use, and agricultural irrigation, and staged pathways from non-potable toward higher-grade reuse where safety evidence supports escalation. This is where the economics of water reuse become most compelling: replacing freshwater with reclaimed water at USD 0.80–1.20/m³ against desalination costs of USD 1.50–2.50/m³ generates direct operational savings that fund the treatment investment.

### 4.5 Receiving-Water Protection and Ambient Water Quality Co-Management

Untreated discharges and wet-weather events do not stop at the treatment plant boundary. Their consequences appear downstream in receiving rivers, estuaries, and coastal waters — often reaching the source-water intakes of downstream utilities or the recreational and fishing waters of adjacent communities. A τ system could support pollutant-plume timing analysis for receiving-water early warning, compliance and ecological protection coordination, and the explicit coupling of wastewater operations with downstream source-water protection. This is where Paper 3 connects back to Paper 1 (source-water quality) and forward to Paper 4 (basin-scale water quality management), making the sanitation dossier a necessary bridge in the full water portfolio.

---

## 5. Realistic-Optimistic Public-Good Scenarios

These scenarios are **planning inferences**, not official forecasts. They ask what a realistic-optimistic first wave of deployment might look like under the τ assumption, using conservative quantitative anchors from official sources.

### 5.1 Health and Exposure Reduction in Fast-Growing Urban Systems

On the current baseline of **113 billion m³ per year** of household wastewater discharged without safe treatment,[^4][^5] a 1% reduction corresponds to approximately 1.13 billion m³ per year of avoided unsafe discharge; a 3% reduction corresponds to 3.4 billion m³ per year. That is not a solution to global sanitation — it is a first-wave public-good shift. At the individual level, if τ-enabled sanitation-chain intelligence helped major cities reduce unsafe discharge pathways, overflow exposure, and sanitation-chain failure even by modest percentages, the downstream impact on diarrhoeal disease burden, child mortality, and waterborne disease transmission could be significant: WHO estimates 494 000 diarrhoeal deaths per year attributable to unsafe sanitation, and even proportionally small reductions translate into tens of thousands of lives.[^3]

### 5.2 Urban Flood and Sewer-Backflow Harm Reduction

In combined systems and flood-prone cities, better wet-weather prediction plus bounded-error sewer and stormwater twins could reduce contamination in homes and streets during overflow events, sewer backup incidents, emergency pumping and cleanup costs, and environmentally harmful overflow hours. The World Bank estimates annual flood damage in Jakarta alone at USD 500 million to USD 1 billion, with significant wastewater contamination as a major component.[^17] Even if the first deployment wave prevented 10% of the worst wet-weather failure episodes in five major cities, the public-health and cleanup value would be in the hundreds of millions of dollars per year.

### 5.3 Water-Security Gains from Regulated Reuse

Where freshwater scarcity is already acute, even moderate increases in safe reuse can reduce vulnerability dramatically. Under the World Bank's 2025 reuse framing, urban and industrial settings are often the strongest first business cases.[^10] A realistic-optimistic first wave is not universal potable reuse everywhere. It is a portfolio of targeted, high-confidence, non-potable reuse deployments that reduce freshwater withdrawals and improve drought resilience in places where the economics and safety case are already close — and where physics-faithful quality prediction closes the remaining gap in confidence.

### 5.4 Energy and Climate Gains Through Wastewater Process Optimization

At 1–3% of national electricity consumption in developed countries, wastewater treatment is a meaningful sectoral energy consumer.[^15] If τ-enabled dynamic process optimization reduced energy consumption at major treatment plants by 10–20% through improved aeration control, chemical dosing optimization, and sludge-line efficiency, the aggregate effect across a portfolio of large urban systems would be substantial: a 15% energy reduction at 100 major urban treatment plants serving 50 million people would represent hundreds of gigawatt-hours per year in avoided electricity consumption and commensurate carbon savings.

### 5.5 Circular Economy Gains Through Resource Recovery Optimization

If τ makes sludge composition, biogas potential, and nutrient availability trajectories more predictable, then sanitation systems can move from treating resource recovery as opportunistic and variable toward treating it as plannable and optimizable. The gain is most meaningful not as standalone revenue, but as a reduction in net operating cost, freshwater demand, uncontrolled greenhouse gas emissions, and vulnerability to input price volatility — improving both economic sustainability and climate resilience simultaneously.

---

## 6. Competitive and Incumbent Landscape

Understanding where τ fits in the existing commercial and institutional landscape requires mapping current tools honestly — their genuine strengths and their structural ceilings.

**Veolia IntelliSense for Wastewater** is an operational analytics platform for wastewater treatment plants, covering energy optimization, chemical dosing, aeration control, and process monitoring. It has genuine operational credibility with major utilities and has demonstrated energy savings in plant operations. Its structural ceiling is the scope boundary: IntelliSense operates primarily at the plant level and is designed for optimization within a known operating envelope. It does not provide physics-faithful prediction of catchment-level inflow behavior, combined sewer overflow risk, or treatment performance under novel storm event conditions outside its training distribution. It is strong on plant operations; it is not a physics-faithful network or catchment twin.

**Xylem Flygt / Wedeco** provides pump and UV disinfection systems with operational monitoring and performance analytics. The Flygt and Wedeco product lines are hardware-focused: they optimize pump station performance, disinfection dosing, and energy efficiency at the device and station level. The platform delivers real-time operational data and alerts. Its structural ceiling is the absence of network-level physics modeling: Xylem's tools provide operational intelligence for individual assets, not physics-faithful predictions of how those assets behave within a coupled network under wet-weather or overflow conditions. It is a strong hardware-layer IoT platform; it is not a network-level digital twin.

**OmniSite / Grundfos iSOLUTIONS** provides remote monitoring for pump stations and lift stations, collecting sensor data on flow, pressure, and equipment status. It serves utilities that need IoT-layer visibility over distributed pump assets with minimal IT infrastructure. Its structural ceiling is precisely this data-layer character: it collects and relays operational readings, but does not model the physical dynamics of sewer networks, combined flow behavior, or treatment-train response. It is a useful IoT data aggregation layer; it is not a physics-level digital twin of any part of the system.

**InfoWorks ICM (Autodesk)** is the industry standard for integrated catchment modeling in urban drainage and sewer networks, widely used by consulting engineers and utilities for CSO analysis, flood-risk assessment, and major sewer upgrade design. It provides high-quality hydraulic simulation of combined sewer and stormwater networks and is genuinely capable in design and planning contexts. Its structural ceiling is the operational deployment gap: InfoWorks ICM is a design and planning tool. It is not built for real-time operational use, does not provide structurally bounded error guarantees under live system state, and does not couple treatment plant process behavior to the upstream hydraulic network. It is strong for engineering design; it is not a real-time operational physics twin.

**MIKE+ URBAN (DHI)** is a commercial urban drainage simulation platform for combined sewer and stormwater modeling, comparable to InfoWorks ICM in its application domain. It provides strong hydraulic simulation for design and planning, with good GIS integration and urban drainage-specific tooling. Its structural ceiling parallels InfoWorks ICM: it is a design tool, not an operational real-time twin; it does not provide bounded-error guarantees under live conditions; and it does not couple to treatment-plant dynamics or sanitation-chain behavior beyond the network boundary. It is strong for urban drainage engineering; it is not an operational coupled twin.

**EPA SWMM (Storm Water Management Model)** is the open-source standard for urban stormwater and sewer simulation, widely used in research, planning, and regulatory contexts as a reference baseline. It provides accessible, well-validated hydraulic simulation of urban drainage and combined sewer behavior, with a large user community and extensive documentation. Its structural ceiling is by design: SWMM is a research and planning tool, not an operational real-time platform. It does not provide real-time state estimation, does not couple to treatment-plant operations, and does not provide bounded-error guarantees under live system conditions. It is the appropriate research and design baseline; it is not an operational real-time physics twin.

**The structural gap across all six tools** is consistent: they are each strong within a defined design scope — plant operations, hydraulic simulation, pump monitoring, or design-stage modeling — but none provides physics-faithful, real-time, operationally coupled coverage of the full sanitation–stormwater–reuse chain with structurally bounded error under live conditions. The τ proposition addresses this structural gap.

---

## 7. Phased Deployment Ladder

### Phase 1 — Observational Shadow Mode

Use τ to shadow existing systems without changing operations: compare overflow prediction against reported events, test plant-load forecasts against metered influent, evaluate wet-weather surcharge forecasts against operator logs, and assess reuse quality window predictions against laboratory results. This phase builds institutional trust and quantifies performance advantage without operational risk. The goal is a credible performance record under live conditions, not operational authority.

**Duration:** 6–18 months per deployment site.
**Key metric:** prediction skill versus current decision support tools.

### Phase 2 — Operator Decision Support

Use τ as an advisory layer that informs but does not replace human decisions: wet-weather plant mode change recommendations, detention and pumping dispatch advisories, fecal sludge routing suggestions, and safe reuse dispatch windows. Operators retain full control; the τ layer provides a second opinion with quantified uncertainty. This phase is critical for building the operator experience and regulatory familiarity needed for subsequent integration.

**Duration:** 12–24 months.
**Key metric:** operator adoption rate and decision-concordance with τ advisories.

### Phase 3 — Integrated City Sanitation and Stormwater Twin

Bring sewer, stormwater, treatment, reuse, and receiving-water intelligence into one city-level operational dashboard. This phase requires institutional coordination between utilities, stormwater agencies, environmental regulators, and city emergency management — and is where the full public-good value of the τ approach begins to materialize. The dashboard supports resilience investment decisions, permit-compliance monitoring, capital prioritization, and emergency response coordination.

**Duration:** 18–36 months.
**Key metric:** reduction in CSO events and treatment-permit exceedances.

### Phase 4 — Regulated Reuse and Circular Optimization

Extend the twin into fit-for-purpose reuse operation, sludge and biogas pathway optimization, nutrient recovery scheduling, and industrial or district-scale circular water loop management. This phase is the full realization of the sanitation-as-resource-system vision. It requires integration with reuse customer systems, energy markets, and potentially fertilizer or water trading frameworks.

**Duration:** 24–48 months for full circular integration.
**Key metric:** freshwater offset volume, energy self-sufficiency ratio, and treatment cost per m³.

---

## 8. Case Studies

### Case Study 1: Singapore NEWater — Advanced Water Reuse at National Scale

**Context and scale.** Singapore has built one of the world's most sophisticated water reuse programs under existential water-security pressure: the island state imports a significant fraction of its water from Malaysia and has limited natural freshwater storage. NEWater is Singapore's response — a multi-barrier advanced water reclamation system that produces high-grade reclaimed water from secondary-treated wastewater through microfiltration, reverse osmosis, and UV disinfection. Five NEWater plants produce more than 130 million gallons per day and supply approximately 40% of Singapore's water demand, primarily to wafer fabrication plants and industrial users, with a portion blended into reservoirs as an indirect potable source during dry periods.[^22]

**Economic profile.** Each NEWater plant costs more than USD 200 million to construct. Operating costs are lower than seawater desalination — approximately USD 0.80–1.20/m³ versus USD 1.50–2.50/m³ for desalination — making NEWater economically competitive as a water-security investment. Singapore's total water security infrastructure investment over 50 years exceeds USD 10 billion.[^22]

**Baseline problem.** NEWater quality assurance requires continuous multi-parameter monitoring across treatment trains and strict compliance with quality standards that exceed WHO potable-reuse guidelines. Current systems use rule-based alert thresholds and periodic laboratory testing. Predictive modeling of treatment performance under varying feed quality — particularly during flood events when stormwater inflow alters secondary-effluent composition, and during low-tide periods when saline intrusion changes feedwater characteristics — is limited. The inability to predict membrane performance degradation and trace contaminant breakthrough more than a few hours ahead requires conservative safety-margin buffers that constrain operational flexibility.

**τ-enabled change.** A physics-faithful treatment-process twin would predict membrane performance trajectories, UV dose effectiveness under turbidity variation, and trace contaminant breakthrough risk 24–48 hours ahead based on upstream catchment conditions, treatment process state, and weather forecasts. Under the τ assumption, this would allow PUB Singapore to reduce required testing frequency while maintaining or improving safety assurance, to optimize energy use in reverse osmosis by 10–20% through more precise pressure management, and to predict feed quality windows in advance of storm events rather than responding to quality exceedances after they occur.

**References.** PUB Singapore NEWater program reports (2024); Singapore Water Story (official PUB documentation); IWA Singapore Leading Edge Technology conference documentation; Lee Kuan Yew Water Prize laureate documentation.[^22]

---

### Case Study 2: Jakarta Combined Sewer Overflow and Flooding — Urban Sanitation Crisis

**Context and scale.** Jakarta is one of the world's most acute urban sanitation challenges. The city of more than 10 million people has a formal sewer network serving only a small fraction of the population; approximately 60% of residents rely on septic tanks and pit latrines with no connection to any managed conveyance system. The city's drainage and sanitation networks are not integrated. Annual flooding events, driven by heavy monsoon rainfall combined with extreme land subsidence — parts of North Jakarta have sunk more than 4 meters over the past 30 years — affect 25–40% of the city.[^23] The Ciliwung, Cisadane, and other rivers overflow regularly, and more than 200 sewage overflow events occur per year during heavy rainfall.[^23]

**Economic profile.** Annual flood damage in Jakarta is estimated at USD 500 million to USD 1 billion by the World Bank.[^23] Wastewater pollution of Jakarta Bay costs the fishing industry an estimated USD 100 million or more per year in reduced catches and market access restrictions. The health burden from waterborne disease exposure during flood events adds significant additional economic cost in treatment, lost workdays, and child school absence.

**Baseline problem.** Jakarta's drainage and wastewater systems are not coupled in any physics-faithful model. The city's flood prediction tools — operated by the National Disaster Management Agency BPBD — do not model sewer overflow risk as a function of drainage system state. No operational combined sewer–drainage twin exists to optimize stormwater management before events or to coordinate pump activation, floodgate operation, and flow diversion in real time. The result is that operators respond to flood events rather than anticipating them, and sewer overflow volumes and locations are not predicted in advance.

**τ-enabled change.** A physics-faithful catchment–sewer–flood twin would predict CSO locations and overflow volumes 6–12 hours before heavy rain events by coupling weather forecast inputs with sewer network hydraulic state and drainage system capacity. Under the τ assumption, this would enable pre-event pump activation and flow diversion — beginning ahead of peak inflow rather than after overloads appear — and would provide actionable public-health guidance on contamination pathways before floodwater reaches populated areas. Conservative estimates from World Bank urban flood management experience suggest that predictive-intervention approaches of this kind can reduce untreated discharge to receiving waters by 30–50% during managed events, with corresponding reductions in post-event cleanup and health-system costs.[^23]

**References.** World Bank Jakarta Urban Development Program documentation; Asian Development Bank Jakarta flood management program; Indonesia BPBD national flood management reports; JICA Jakarta Comprehensive Flood Management Plan.[^23][^24]

---

## 9. Finance Mechanisms and Investment Case

### 9.1 Aligned Multilateral Finance

**World Bank Water Global Practice** is the largest multilateral water-sector lender, deploying more than USD 3 billion per year to wastewater treatment and water reuse projects. Its CWIS initiative and climate-resilient sanitation work provide direct conceptual alignment with the τ deployment proposition. Pilot and scale-up investments in the USD 20–50 million range are well within normal World Bank project structures for urban water utilities in middle-income countries.[^8][^9][^10]

**Asian Development Bank (ADB)** has active urban wastewater and stormwater management programs across Asia, with a particular focus on rapidly urbanizing cities in Southeast and South Asia. Jakarta, Ho Chi Minh City, Manila, and Dhaka all fall within ADB's active portfolio and are precisely the cities where combined sewer overflow and flood–sanitation interaction is most acute.[^24]

**Green Climate Fund (GCF)** maintains a climate-resilience infrastructure window that covers urban water system adaptation. Sanitation systems that can demonstrate climate-resilient design — including predictive CSO management and flood-linked treatment performance — meet GCF's adaptation investment criteria.

**US EPA Water Infrastructure Finance and Innovation Act (WIFIA)** provides low-cost federal loans for eligible water and wastewater infrastructure projects in the United States, including CSO control programs, combined sewer separation, advanced treatment for reuse, and stormwater management upgrades. WIFIA loan terms make physics-faithful operational twin deployment financeable within existing utility capital programs.

### 9.2 Cost Scenarios

**Cost Scenario 1 — Wastewater treatment optimization for one city (1 million or more people).** Estimated investment: USD 3–10 million for a physics-faithful treatment-plant and collection-network twin covering a major municipal treatment plant and its contributing sewer network. Expected outcomes: 15–25% reduction in energy consumption, improved permit compliance, reduced overflow frequency. Payback logic: at USD 5.5 economic return per USD 1 invested in sanitation, and with energy savings of USD 1–3 million per year from optimized treatment processes, the investment case is positive within 3–7 years without any health-benefit credits.

**Cost Scenario 2 — National CSO early warning and stormwater management platform (10 cities).** Estimated investment: USD 20–50 million for a ten-city combined sewer overflow early warning and stormwater management platform. Expected outcomes: 30–50% reduction in untreated overflow volumes during major events, measurable reduction in post-flood health and cleanup costs, improved regulatory compliance. Payback logic: at USD 500 million in annual flood damage in Jakarta alone, preventing 5–10% of annual damage across ten cities generates USD 25–50 million per year in avoided costs against a USD 20–50 million investment — a benefit-to-cost ratio of approximately 1:1 to 2.5:1 from flood damage avoidance alone, before accounting for health, water quality, or reuse benefits.

### 9.3 Benefit-to-Cost Reference Points

WHO's sanitation economics analysis estimates that every USD 1 invested in sanitation returns **USD 5.5 in economic benefit** through reduced healthcare costs, reduced lost workdays, improved educational outcomes, and reduced environmental remediation costs.[^3] Wastewater reuse programs following the Singapore NEWater model produce water at approximately USD 0.80–1.20/m³, compared with seawater desalination at USD 1.50–2.50/m³ — a cost advantage of 30–50% that improves further as τ-enabled optimization reduces energy consumption.[^22] These conservative ratios make the investment case tractable without requiring optimistic assumptions about τ performance.

---

## 10. Governance Guardrails

### 10.1 Public Health Must Outrank Efficiency Gains

Sanitation and reuse decisions must remain first and foremost about safety. No efficiency or cost argument should be allowed to erode treatment targets, reuse quality standards, or regulatory safeguards. The τ layer should make safety management better, not cheaper by cutting margins.

### 10.2 Reuse Must Remain Risk-Based and Regulated

The τ layer should support and sharpen regulatory treatment targets and public-health safeguards, not bypass them. EPA's risk-based reuse framework and WHO's water quality guidelines provide the appropriate regulatory floor.[^11][^12] τ-enabled prediction should allow that floor to be managed more precisely and more reliably — not lowered.

### 10.3 Sewered and Non-Sewered Systems Must Both Be Treated Seriously

CWIS exists because one-size-fits-all sewer expansion is not sufficient.[^8] Deployment should not reinforce existing infrastructure inequity by serving only formal core districts. The fecal sludge chain, onsite containment systems, and informal settlement sanitation pathways must be explicitly included in the planning scope and in the τ twin.

### 10.4 Wet-Weather Failures Must Be Core Design Conditions, Not Edge Cases

Climate change makes the combined sewer overflow and urban flooding problem worse over time, not better. The τ twin must be designed with wet-weather failure modes as primary use cases — not as exceptions to a dry-weather operating model. Systems that perform well under normal conditions but degrade under stress are precisely the tools the sector already has.

### 10.5 Circularity Must Not Become an Excuse for Unsafe Reuse

Water, nutrient, or energy recovery is only a public good when it is demonstrably safe and socially legitimate. The growing political attractiveness of circular economy narratives should not be used to accelerate reuse deployment ahead of the safety evidence. τ-enabled prediction should accelerate the accumulation of safety evidence — not substitute for it.

### 10.6 Data Governance and Community Consent

Sanitation data — particularly in non-sewered and informal settlements — can carry privacy, tenure, and community sensitivities. Deployment frameworks must address data governance explicitly, ensure community consent for monitoring, and provide transparent access to model outputs for affected communities and regulators.

---

## 11. Cross-Portfolio Connections

This paper sits at the intersection of several broader portfolio connections that amplify its public-good value when articulated explicitly.

**Connection to Paper 1 (Source Water and Treatment Quality).** Combined sewer overflow and sanitation-chain failures have direct consequences for downstream drinking-water source quality. A τ sanitation twin that predicts overflow timing and pollutant plume trajectories provides early warning to source-water intake operators — closing a loop between sanitation failures and drinking-water risk that current institutional boundaries leave open.

**Connection to Paper 4 (River Basin, Groundwater, and Water Productivity).** Wastewater effluent and untreated discharge are major drivers of river basin water quality. A τ sanitation twin that models receiving-water pollutant dynamics at the city scale provides the missing urban input to basin-level water quality management — connecting treatment plant performance to downstream ecological and water-productivity impacts.

**Connection to Paper 5 (WASH in Vulnerable Settings).** Fecal sludge chain management and decentralized sanitation in informal settlements, camps, and climate-vulnerable communities require the same chain-wide risk management philosophy as urban sewered systems. The τ framework developed in Paper 3 for CWIS and fecal sludge management is directly transferable to the Paper 5 contexts.

**Connection to the Energy Portfolio.** Wastewater treatment is a significant energy consumer. A τ wastewater twin that optimizes treatment-process energy use contributes to grid demand management and renewable energy integration — connecting the water and energy portfolios in a practically meaningful way.

---

## 12. Open Questions and Research Priorities

Honesty about what remains to be established is a precondition for responsible yellow-paper framing. The following questions are open and important.

**12.1 Empirical validation on live wastewater systems.** The τ framework's applicability to wastewater hydraulics, treatment kinetics, and combined sewer overflow behavior remains to be demonstrated on real-world data. The benchmark suite proposed in Section 13 is the appropriate first test.

**12.2 Treatment-process coupling.** Wastewater treatment involves highly complex biochemistry — activated sludge kinetics, anaerobic digestion, membrane fouling dynamics — that may or may not be well-represented by the τ abstraction layer. The relationship between τ's physical modeling and conventional biological treatment models (ASM1, ADM1) needs explicit investigation.

**12.3 Non-sewered system representation.** Fecal sludge and onsite containment systems behave very differently from hydraulic networks. Whether the τ twin can represent their behavior faithfully — given the absence of continuous monitoring in most non-sewered contexts — requires specific methodological development.

**12.4 Stormwater–groundwater coupling.** In many cities, groundwater intrusion into sewers (inflow and infiltration) is a major driver of wet-weather overloads. Whether the τ twin can represent the soil and groundwater dynamics that drive this coupling, and whether it can do so operationally rather than only in design studies, is an important open question.

**12.5 Regulatory acceptance pathways.** Even if τ demonstrates superior prediction performance in shadow-mode benchmarking, regulatory acceptance for operational use — especially in reuse and compliance contexts — requires validated performance standards, third-party auditing, and clear liability frameworks. These are institutional questions as much as technical ones.

---

## 13. Benchmark Suite and Lighthouse Pilots

### Benchmark Suite

A credible first-wave benchmark suite for τ in the sanitation domain would include:

1. **Combined sewer overflow forecasting accuracy** under wet-weather events: prediction skill for overflow location, timing, and volume against post-event metered data.
2. **Treatment-plant dynamic control performance** under highly variable influent: prediction accuracy for effluent quality parameters under storm event conditions.
3. **Sanitation-chain risk mapping** across sewered and non-sewered neighborhoods: comparison of predicted risk accumulation against historical failure or exceedance records.
4. **Stormwater capture and safe reuse planning** under municipal conditions: prediction of reuse quality windows against laboratory quality monitoring.
5. **Receiving-water pollutant timing** under plant overload or overflow episodes: prediction accuracy for downstream contamination arrival and duration against ambient monitoring.

### Lighthouse Pilots

**Pilot 1 — Combined-sewer city under climate stress.** Best settings: a Northern European or North American city with well-instrumented combined sewer infrastructure and a documented history of CSO events. Best for: overflow prediction, stormwater integration, and urban flood–public-health co-benefits. Suitable candidates include cities in the UK, Netherlands, or US with active long-term CSO control programs.

**Pilot 2 — Rapidly growing city with mixed sewered and non-sewered sanitation.** Best settings: a Southeast Asian or African city actively implementing CWIS or fecal sludge management programs. Best for: CWIS planning, fecal sludge routing, and phased safely managed sanitation expansion. Suitable candidates include cities in the Philippines, Ghana, or Bangladesh with active sanitation utility reform programs.

**Pilot 3 — Water-stressed industrial and urban reuse corridor.** Best settings: a water-scarce city or industrial cluster with established or planned non-potable reuse programs. Best for: fit-for-purpose reuse planning, risk-based treatment targets, and freshwater substitution. Singapore (with PUB NEWater as institutional partner), Israel (with Mekorot), or major US reuse utilities are suitable candidates.

**Pilot 4 — Coastal city with wet-weather contamination and receiving-water stress.** Best settings: a coastal city with documented sewage overflow impacts on marine recreational water and fisheries. Best for: overflow prediction, receiving-water protection, and sanitation–source-water integration. Suitable candidates include cities in Southeast Asia, the Mediterranean, or the Caribbean with documented beach and bay quality management programs.

**Pilot 5 — Utility and regulator co-pilot.** Best for: aligning operations, health protection, and compliance monitoring in one shared twin. This pilot is less about geographic setting and more about institutional design — bringing a utility, an environmental regulator, and a public health authority into a shared operational picture with explicit handoff protocols between the τ advisory layer and regulatory decision processes.

---

## 14. Implementation Roadmap

### Immediate (2026–2027): Foundations and Proof of Concept

- Identify two to three partner utilities with well-instrumented wastewater networks and CSO monitoring: priority on cities with active CWIS or CSO control programs.
- Establish shadow-mode benchmarking protocols against existing InfoWorks ICM or MIKE+ URBAN hydraulic models as performance baselines.
- Initiate treatment-process coupling work to align τ predictions with ASM1/ADM1 baseline models.
- Engage EPA, WHO, and World Bank teams on benchmark suite design and pilot site selection.

### Near Term (2027–2029): Validated Operational Pilots

- Complete Phase 1 shadow-mode benchmarking at two to three pilot sites; publish performance comparison against incumbent tools.
- Advance Phase 2 operator decision-support deployment at one CSO management site and one advanced water reuse site.
- Engage development bank financing pipelines for scale-up in a middle-income country urban sanitation context.
- Initiate regulatory dialogue on performance standards for τ-based compliance advisory tools.

### Medium Term (2029–2032): Scale-Up and Circular Integration

- Deploy Phase 3 integrated city twins at three to five cities with full sewer–stormwater–treatment–reuse coverage.
- Initiate Phase 4 circular optimization pilots at industrial-scale reuse facilities.
- Develop open-source reference implementations for low-income country contexts to ensure equitable access.

---

## 15. Bottom Line

Under the strong τ assumption, wastewater, stormwater, sanitation, and circular reuse represents one of the most compelling public-good entry points in the wider water portfolio. The reason is precise.

The official world already tells us three crucial things:

1. The sanitation and untreated-wastewater burden is still enormous — 3.6 billion people lacking safely managed sanitation, 113 billion m³ of household wastewater discharged untreated per year, and a combined sewer overflow problem that climate change is making worse.
2. The field already knows the right chain-wide risk-management philosophy — WHO's SSP, World Bank's CWIS, and EPA's risk-based reuse framework all define the correct conceptual direction.
3. The missing piece is exactly the kind of physically faithful, bounded-error, intervention-timed operational intelligence that τ claims to provide — the gap between having the right framework and having the right execution layer.

So this is not merely a utilities optimization paper. It is a plausible route to:

- safer sanitation for more people in more conditions;
- fewer wet-weather contamination events in flood-prone cities;
- stronger urban resilience under a changing climate;
- more realistic planning for citywide inclusive sanitation;
- better reuse and water security in water-stressed regions;
- and a more circular, less wasteful, more resilient urban water future.

The public-good case does not require τ to solve everything. It requires τ to be true enough to matter operationally — to shift decisions, to change timing, to prevent failures that current tools cannot predict. If that condition is met, the return on investment is substantial, the alignment with existing institutional missions is strong, and the financing pathways are already in place.

That is why this deserves to be Paper 3.

---

## References

[^1]: WHO / UNICEF JMP, *Progress on household drinking water, sanitation and hygiene 2000–2024* (2025): https://data.unicef.org/resources/jmp-report-2025/

[^2]: WHO news release, *1 in 4 people globally still lack access to safe drinking water* (2025): https://www.who.int/news/item/26-08-2025-1-in-4-people-globally-still-lack-access-to-safe-drinking-water---who--unicef

[^3]: WHO, *Sanitation* fact sheet (2024): https://www.who.int/news-room/fact-sheets/detail/sanitation

[^4]: UN-Water, *Progress on Wastewater Treatment – 2024 Update* publication page: https://www.unwater.org/publications/progress-wastewater-treatment-2024-update

[^5]: UN-Water, *Progress on Wastewater Treatment – 2024 Update* PDF: https://www.unwater.org/sites/default/files/2024-08/SDG6_Indicator_Report_631_Progress-on-Wastewater-Treatment_2024_EN_0.pdf

[^6]: WHO, *Sanitation safety planning* (manual / overview): https://www.who.int/publications/i/item/9789240062887

[^7]: WHO, *Sanitation safety planning (first edition)* overview: https://www.who.int/publications/i/item/9789241549240

[^8]: World Bank, *Citywide Inclusive Sanitation (CWIS) Initiative* (2025): https://www.worldbank.org/en/topic/water-for-people/brief/citywide-inclusive-sanitation

[^9]: World Bank, *The Global Sanitation Crisis: Pathways to Urgent Action* (2025): https://www.worldbank.org/en/topic/water/publication/the-global-sanitation-crisis

[^10]: World Bank, *Scaling Water Reuse* (2025): https://www.worldbank.org/en/topic/water/publication/scaling-water-reuse

[^11]: EPA, *Capturing Stormwater as Source Water for Reuse Resources* (updated 2026): https://www.epa.gov/waterreuse/capturing-stormwater-source-water-reuse-resources

[^12]: EPA, *Risk-Based Framework for Developing Microbial Treatment Targets for Water Reuse* (2025): https://www.epa.gov/system/files/documents/2025-01/risk-basedframeworkfordevelopingmicrobialtreatmenttargetsforwaterreuse-1.pdf

[^13]: EPA, *Combined Sewer Overflow Basics* (updated 2025): https://www.epa.gov/npdes/combined-sewer-overflow-basics

[^14]: World Bank, *The Global Sanitation Crisis* climate-resilient sanitation case studies (2025): https://thedocs.worldbank.org/en/doc/61714f214ed04bcd6e9623ad0e215897-0400012021/related/GLOBALSANITATION-RESILIENTSANITATIONCASESTUDIESPAPER-WEB.pdf

[^15]: WWAP (UN World Water Assessment Programme), *The United Nations World Water Development Report 2017: Wastewater — The Untapped Resource*: https://www.unwater.org/publications/world-water-development-report-2017

[^16]: MarketsandMarkets, *Water Reuse Market — Global Forecast to 2030* (2025): https://www.marketsandmarkets.com/Market-Reports/water-reuse-market-171416827.html

[^17]: World Bank, *Jakarta Urban Development Project* and Urban Flood Management documentation: https://www.worldbank.org/en/country/indonesia/overview

[^18]: WHO, *Water safety planning* framework overview: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/water-safety-and-quality/water-safety-planning

[^19]: EPA, *Water Reuse Action Plan* (2020, updated 2024): https://www.epa.gov/waterreuse/water-reuse-action-plan

[^20]: IWA (International Water Association), *Wastewater report 2018 — The Reuse Opportunity*: https://iwa-network.org/publications/the-reuse-opportunity/

[^21]: Asian Development Bank (ADB), *Urban Wastewater Management in Asia*: https://www.adb.org/sectors/water/key-priorities/wastewater-management

[^22]: PUB Singapore, *NEWater — Singapore's water reclamation story*: https://www.pub.gov.sg/watersupply/fournationaltaps/newater

[^23]: Asian Development Bank (ADB), *Jakarta Flood Management Investment Program*: https://www.adb.org/projects/42408-013/main

[^24]: JICA, *Jakarta Comprehensive Flood Management Plan*: https://www.jica.go.jp/Resource/english/our_work/thematic_issues/water/c8h0vm0000anskm2-att/indonesiaen.pdf

[^25]: Metcalf & Eddy / AECOM, *Wastewater Engineering: Treatment and Resource Recovery*, 5th Edition (2014), McGraw-Hill. Standard reference for biological treatment process kinetics (ASM1, ADM1).

[^26]: International Water Association (IWA), *Fecal Sludge Management: Systems Approach for Implementation and Operation* (2014): https://www.iwa-network.org/publications/fecal-sludge-management/

[^27]: WERF (Water Environment Research Foundation) / Water Research Foundation, *Energy Best Practice Guide for Wastewater Treatment Plants* (2012): https://www.waterrf.org

[^28]: USEPA, *Primer for Municipal Wastewater Treatment Systems* (2004, EPA 832-R-04-001): https://www.epa.gov/sites/default/files/2015-09/documents/primer.pdf

[^29]: Tchobanoglous, G., Cotruvo, J., Crook, J. et al., *Framework for Direct Potable Reuse* (WateReuse Association / AWWA / WEF / ASCE, 2015): https://watereuse.org/product/framework-for-direct-potable-reuse/

[^30]: IPCC, *Climate Change 2022: Impacts, Adaptation and Vulnerability*, Chapter 4 (Water): https://www.ipcc.ch/report/ar6/wg2/

[^31]: UNESCO / UN-Water, *WWDR 2021: Valuing Water* (2021): https://www.unwater.org/publications/world-water-development-report-2021

[^32]: WHO / UNICEF, *WASH in the 2030 Agenda* progress brief (2024): https://www.unicef.org/reports/wash-2030-agenda


---

*Source: Full manuscript text integrated from companion paper draft.*
