---
layout: impact-paper
lane: impact
title: Tau-Grade Clean-Air Digital Twins, Exposure Intelligence, and Urban/Regional
  Health Protection
permalink: /impact/papers/clean-air-digital-twins-exposure-intelligence/
paper_id: companion-pollution-circularity-paper-1
portfolio_id: impact-pollution-circularity
summary_short: A companion paper showing how a law-faithful tau atmosphere-emissions-chemistry-exposure
  twin could unlock major public-good gains in urban air-quality protection, hyperlocal
  exposure intelligence, source attribution, and clean-air policy—addressing 7 million
  premature deaths annually.
right_rail:
  meta:
    type: Companion Paper
    portfolio: Pollution Circularity
    status: Conditional
    updated: April 2026
---

# Tau-Grade Clean Air Digital Twins and Exposure Intelligence
**Companion Dossier — Panta Rhei Impact: Pollution & Circularity Portfolio**
**Paper 1 of 4 · Status: Yellow Paper · 2026-03-16**

---

## Executive Summary

Air pollution is the largest single environmental cause of premature death on Earth. WHO reports that **99% of the global population breathes air that exceeds WHO guideline limits**, and that combined ambient and household air pollution is associated with **7 million premature deaths annually**.[^1] UNEP frames the full pollution burden at approximately **9 million deaths per year**, of which air pollution accounts for nearly seven million.[^2] The economic toll is staggering: air pollution costs the global economy approximately **USD 8.1 trillion per year**, equivalent to **6.1% of global GDP**.[^3] Indoor air pollution from household solid fuels and biomass cooking alone accounts for an estimated **3.2 million deaths per year**, predominantly among women and children in low- and middle-income countries.[^1]

Official institutions are not waiting for this problem to solve itself. EPA's AirNow system already issues daily air-quality forecasts because the public need is immediate and operational.[^4] NOAA and the Unified Forecast System community are actively building the UFS Air Quality Model to bring stronger smoke, dust, and ozone forecasting into national operational services.[^5] The Copernicus Atmosphere Monitoring Service provides regional forecasts and long-range transport information across Europe.[^6] The European Environment Agency reports that **94% of the EU urban population** is still exposed to PM2.5 levels exceeding WHO guidelines — even after decades of improvement.[^7] Delhi's air quality exceeds WHO safe limits by a factor of fifteen or more during the worst winter episodes.[^8] Western US wildfire smoke in 2020 degraded air quality across eleven states for more than 45 days and contributed to an estimated 3,000 or more premature deaths.[^9]

These systems already prove that the mission is understood, the demand is real, and the public-health urgency cannot be overstated. What they do not provide — and what this paper argues τ could provide — is a **law-faithful, bounded-error, coarse-grainable discrete twin** of the full atmosphere–emissions–chemistry–dispersion–exposure chain. That distinction matters enormously. Today's operational stack combines numerical weather prediction, emissions inventories, chemistry solvers, observational assimilation, and statistical correction into products that are useful but structurally incomplete. They improve, but they do not converge on a physically coherent substrate that can be reliably refined, scaled down to street level, or used to test interventions before deployment.

This paper asks a focused question under an explicitly caveated planning stance: **if the τ framework is sound, what public good could a τ-grade clean-air digital twin unlock?**

Six findings structure the answer.

**Finding 1 — The health burden is large enough that even modest improvements at scale justify very substantial investment.** WHO's estimate of 7 million premature deaths per year means that a 1% improvement in exposure protection corresponds to 70,000 lives per year — at a scale far larger than most medical interventions. The USD 8.1 trillion annual economic cost means that a 1% improvement in avoidance is worth USD 81 billion in annual welfare. The public-good case does not require transforming the entire global air-quality system. It requires moving the needle measurably in the cities, corridors, and regions where τ-grade intelligence changes decisions.

**Finding 2 — The critical gap is not monitoring — it is the physics-to-action chain.** The world already has thousands of monitoring stations, satellites, low-cost sensors, and mobile platforms. What is missing is a physically faithful causal chain from emissions sources through atmospheric transport, chemistry, and boundary-layer behavior to hyperlocal human exposure, with sufficient resolution and error characterization to support protective action at the neighborhood and facility scale. That is precisely the gap a τ-grade twin addresses.

**Finding 3 — Source attribution is the missing operational layer for policy.** Current systems can tell you that air quality is bad. They are much weaker at telling you which sources are responsible for how much of a given episode, under what transport conditions, with what confidence. Without that attribution, clean-air governance defaults to broad compliance logic rather than targeted causal action. τ pushes toward real-time causal attribution: this freight corridor, this open-burning plume, this inversion-trapped industrial cluster.

**Finding 4 — The incumbent landscape has structural ceilings that τ directly addresses.** ECMWF CAMS, IQAir/AirVisual, EPA AirNow/WAQI, BreezoMeter, Plume Labs/Clarity, and AERMOD/ADMS each serve important functions. None provides physics-faithful, operationally coupled, street-scale source-to-exposure simulation with bounded error. The τ proposition is not incremental improvement within an existing category — it is a structurally different substrate.

**Finding 5 — Geographic case studies in Delhi and the Western US wildfire corridor illustrate what is concretely at stake.** Delhi's annual October–February air-quality crisis causes an estimated 54,000 premature deaths per year in the city alone, with PM2.5 levels exceeding 400–500 AQI for 30–60 days annually. Current forecast uncertainty of 25–35% in PM2.5 peaks limits actionable warning to 24 hours. A τ-grade twin could extend skillful warnings to 5–7 days, enabling school closures, transport restrictions, and health advisories with meaningful lead time. In the Western US, wildfire smoke forecast skill collapses beyond 36 hours. A τ-grade atmospheric dynamics and fire-behavior coupling could extend skillful smoke forecasting to 5–7 days, giving hospitals, outdoor workers, and sensitive populations four additional days to prepare.

**Finding 6 — Finance mechanisms are already aligned with this capability gap.** The World Bank Clean Air Fund, Green Climate Fund, EU LIFE Programme, ADB Clean Air for Asia, and UNEP Clean Air Initiative all represent named funding windows actively seeking better clean-air intelligence. Conservative city-scale deployment costs of USD 3–8 million against a WHO-estimated health benefit baseline of USD 4.6 trillion per year from air-pollution health costs make the investment case tractable without heroic assumptions.

The core public-good proposition is precise: a city or region that can predict its own air-quality failure modes — inversions, episode spikes, smoke arrival, source contributions — days in advance is a city that can protect its most vulnerable populations before harm accumulates, not merely respond after it has. That is what τ claims to enable. This dossier maps the consequences if that claim is sound.

---

## 1. Why This Matters Now

### 1.1 The Burden Has Not Peaked

The air-pollution burden is not a legacy problem trending toward resolution. WHO's most recent assessment places 7 million premature deaths per year as the combined ambient and household toll, with the share attributable to ischemic heart disease, stroke, chronic obstructive pulmonary disease, lung cancer, and acute lower respiratory infections rising as medical attribution methods improve.[^1] UNEP's broader framing sets the all-pollution mortality at approximately 9 million deaths per year, making pollution collectively responsible for more premature deaths than HIV/AIDS, tuberculosis, and malaria combined.[^2]

The regional burden is deeply unequal. Southeast Asia and the Western Pacific region carry the heaviest absolute toll. Sub-Saharan Africa faces a rising burden from both ambient pollution linked to rapid urbanization and from the persistent household air pollution associated with solid-fuel cooking, which UNEP and WHO both identify as a leading driver of the 3.2 million household air pollution deaths per year — a figure almost entirely concentrated among women and children in low-income settings.[^1][^10]

### 1.2 Cities Are Where the Crisis Becomes Operational

The EEA's 2025 status report documents that 94% of EU urban residents are still exposed to PM2.5 above WHO guidelines, despite decades of regulatory pressure and real progress on emissions.[^7] If Europe — with its relatively mature monitoring networks, regulatory infrastructure, and political commitment — has not yet closed the urban exposure gap, the situation in cities without that baseline is more severe. IQAir's 2023 World Air Quality Report found that only 13 of 134 countries met WHO annual PM2.5 guidelines, and 9 of 10 of the world's most polluted cities were in South Asia.[^11]

The operational problem is concentrated in urban and peri-urban environments precisely because that is where the interaction of traffic, freight, industry, buildings, port operations, open burning, and meteorological boundary-layer behavior creates the highest and most variable exposures. These are not abstract global averages. They are neighborhood, school, hospital, and corridor-scale questions: which children are breathing the worst air today, what is driving that exposure, and what protective action is available in the next 6–72 hours?

### 1.3 The Forecast Gap Is the Actionability Gap

Air-quality forecasting at national and regional scales is already operationally mature. The problem is not that cities lack any forecast product. The problem is that forecast skill at the spatial resolution and temporal specificity needed for protective action collapses precisely where it would be most valuable: at the neighborhood scale during pollution episodes, in the first 2–5 days before major events, and in the attribution of specific sources during complex inversion-trapped or long-range transport conditions.

NOAA's HRRR smoke forecast skill degrades significantly beyond 36 hours.[^5] Current IMD/CPCB forecasts of PM2.5 peaks in Delhi carry 25–35% uncertainty even at 24-hour lead time.[^12] These are not failures of effort or investment — they are consequences of structural gaps in the physics substrate. The atmosphere is continuous, nonlinear, and multi-scale. The tools used to simulate it are discretized, parameterized, and assimilated from sparse observations. A τ-grade twin addresses that structural gap.

### 1.4 Indoor Air Quality Remains Underserved

Almost all operational air-quality intelligence is designed around outdoor ambient conditions. Yet WHO attributes 3.2 million premature deaths per year specifically to household air pollution — predominantly from cooking and heating with solid fuels, biomass, charcoal, and kerosene.[^1] The epidemiological burden of household air pollution is comparable to the ambient burden, but the monitoring network, forecast infrastructure, and protective action toolkit for indoor air quality are dramatically weaker.

A τ-grade exposure intelligence framework has the structural advantage of being applicable across both domains: outdoor transport and chemistry driving ambient concentrations, combined with indoor–outdoor coupling and building envelope behavior driving actual human exposure. This integration is not technically achievable within today's fragmented operational systems.

---

## 2. Scope and Reader Orientation

This paper adopts a deliberate planning stance, stated explicitly so that its arguments can be read with appropriate calibration.

The stance is: **assume, for planning purposes, that the strongest τ claims relevant to atmospheric transport, chemical transformation, boundary-layer dynamics, and source-to-receptor exposure pathways are sound**, and ask what practical and public-good consequences would follow if those capabilities were integrated into urban, regional, and national air-quality systems. This paper does not assert that the broader scientific or regulatory communities have accepted the τ framework. It asks what would follow if the framework were true enough to matter operationally, and maps those consequences against what official institutions already want and already fund.

Three categories of claim are kept strictly distinct throughout:

- **What official institutions already know and already want** — the empirical baseline, drawn from WHO, UNEP, EPA, NOAA, CAMS, EEA, World Bank, EPIC India, and equivalent authoritative sources.
- **What τ would newly provide under the assumption** — the planning inference layer, clearly labeled as such throughout.
- **What impact estimates are planning inferences rather than official forecasts** — quantified with conservative public-value anchors wherever possible and flagged explicitly.

This is a **yellow paper**. It is assumption-led, deployment-oriented, and public-good framed. It does not claim that operational validation of the τ framework on real atmospheric systems has occurred. That validation is precisely the purpose of the benchmark suite and pilot structure described in Sections 10 and 13.

### Scope of This Paper

This is **Paper 1 of 4** in the Pollution/Circularity portfolio and focuses exclusively on:

- urban and regional air-quality digital twins;
- outdoor ambient air quality (PM2.5, PM10, NO2, O3, SO2, CO);
- indoor/household air quality and exposure coupling;
- hyperlocal exposure intelligence at neighborhood, facility, and corridor scale;
- daily and multi-day AQI protection and episode management;
- wildfire smoke, long-range dust transport, and compound event protection;
- source attribution sufficient for operational public-health action;
- and public-good deployment pathways for cities, regions, and national air-quality authorities.

### Explicitly Out of Scope for Paper 1

These are deferred to later papers in the portfolio:

- **Paper 2:** τ for industrial, transport, and agricultural emissions attribution, compliance, and high-return abatement targeting;
- **Paper 3:** τ for chemicals, toxic releases, lead/PFAS/heavy metals, plume intelligence, and remediation;
- **Paper 4:** τ for waste systems, plastics leakage, and zero-waste transitions.

---

## 3. The Opportunity Baseline

### 3.1 Mortality and Morbidity

WHO's air-pollution health statistics establish the ceiling of the opportunity:[^1]

- **7 million premature deaths per year** from combined ambient and household air pollution
- **3.2 million deaths per year** attributed specifically to household/indoor air pollution
- **4.2 million deaths per year** attributed to ambient (outdoor) air pollution
- 91% of air-pollution-related deaths occurring in low- and middle-income countries
- Air pollution implicated in ischemic heart disease, stroke, lung cancer, COPD, lower respiratory infections, and diabetes

The Lancet Commission on pollution and health has affirmed that pollution is responsible for 16% of all deaths globally — more than AIDS, tuberculosis, and malaria combined.[^13] The Institute for Health Metrics and Evaluation (IHME) finds ambient air pollution to be the fourth-leading risk factor for death worldwide.[^14]

### 3.2 Economic Cost

UNEP's economic framing sets the air-pollution cost at approximately **USD 8.1 trillion per year**, equivalent to 6.1% of global GDP.[^3] The World Bank and IHME joint work on the cost of air pollution found that in 2013, welfare losses from premature mortality attributable to air pollution were approximately USD 5.11 trillion.[^15] The EPA's own regulatory impact assessments consistently estimate that every USD 1 invested in clean air regulation returns USD 30 in economic benefit, primarily through avoided healthcare costs and premature deaths.[^16]

EPIC India estimates the productivity losses from air pollution in India at over **USD 30 billion per year** for Delhi alone, a figure that captures only a fraction of the health-system burden.[^17] The WHO estimates total global health costs attributable to air pollution at **USD 4.6 trillion per year** — making the investment case for better exposure intelligence tractable at even very small percentage-point reductions in exposure.[^1]

### 3.3 Coverage and Equity Gaps

IQAir's 2023 World Air Quality Report found that only **7.8% of monitored cities** meet WHO annual PM2.5 guidelines.[^11] EPA AirNow coverage is strong in the United States but leaves large rural and peri-urban areas with no proximate monitoring station.[^4] During the 2020 Western US wildfire season, more than **40 million people** had no local AQI data during peak smoke events.[^18]

In South Asia, Africa, and parts of Latin America, the monitoring infrastructure deficit is severe. A τ-grade physics-based simulation can extend coverage beyond where physical monitors exist — a critical advantage in exactly the regions where the health burden is highest.

### 3.4 The Household Air Pollution Gap

WHO attributes 3.2 million deaths per year to household air pollution, primarily from solid-fuel cooking — over 90% of these in low- and middle-income countries.[^1][^10] Women bear the greatest burden, spending more hours near cooking fires. Children under 5 in biomass-fuel households face dramatically elevated pneumonia risk. Yet household air quality receives only a small fraction of the monitoring infrastructure, forecast tool development, and policy attention directed at ambient air quality.

A τ-grade exposure intelligence framework covering both outdoor and indoor domains — using the same physical substrate for boundary-layer dynamics and indoor–outdoor infiltration — would address this structural gap.

---

## 4. Working τ Assumptions

This section defines the planning-stance assumptions that underpin the opportunity analysis in this paper. These are stated explicitly so that readers can assess which conclusions depend on which assumptions.

### 4.1 Physics-Side Assumptions

For the purposes of this analysis, we assume that τ provides:

- A **discrete, constructive, countable, bounded-error substrate** for atmosphere–emissions–transport–chemistry dynamics at urban and regional scales.
- Native and coherent treatment of urban and regional advection, plume dispersion, turbulent mixing, planetary boundary-layer structure, temperature inversions and nocturnal jet formation, smoke and mineral dust transport and deposition, aerosol formation and pollutant transformation, and source-to-receptor transport across the full spatial hierarchy from street canyons to continental plume transport.
- **Coarse-grainable fidelity**: lower-resolution urban/regional twins remain tied to explicit error bounds rather than becoming ad hoc discretizations. The system degrades gracefully as resolution decreases, rather than failing abruptly.
- **Stable convergence of refinement and precision**: as more computational resource or observation data is added, the twin converges on the physical truth rather than overfitting to current observations.

### 4.2 Exposure-Side Assumptions

We further assume that τ outputs can be transformed into operationally useful exposure intelligence products including:

- Hyperlocal AQI and pollutant-specific concentration projections at block, neighborhood, and facility scale;
- School, hospital, childcare, and workplace exposure envelopes covering 24–72 hour windows;
- Source contribution estimates that are operationally useful for public-health action, not merely academically descriptive;
- Indoor–outdoor infiltration estimates incorporating building stock typology and ventilation behavior;
- Multi-pollutant compound exposure maps combining PM2.5, ozone, NO2, and where relevant SO2, CO, and benzene.

### 4.3 Policy and Operations Assumptions

We assume that τ outputs can support daily operational protective decisions including school closure and outdoor activity guidance, hospital preparation and respiratory-care staffing, worker protection triggers for outdoor labor, traffic or freight restriction decisions, industrial curtailment during episodes, wildfire-smoke preparation and shelter-in-place guidance, and targeted mask or filtration deployment advisories.

### 4.4 What This Paper Does Not Assume

This paper does not require immediate acceptance of the full τ framework by regulatory or scientific communities. Practical value could begin much earlier if τ simply outperformed existing systems on selected high-value tasks:

- next-day and 5-day PM2.5 and ozone skill at neighborhood scale;
- smoke and dust arrival timing and severity;
- episode source attribution at the corridor and district level;
- hyperlocal exposure mapping for facilities;
- and intervention what-if scenarios for clean-air planning.

A phased demonstration against these tasks, using the benchmark suite in Section 13, is the appropriate validation pathway before broader operational integration.

---

## 5. What Changes with a Law-Faithful Twin

### 5.1 The Current Stack and Its Structural Ceiling

Today's operational air-quality stack is genuinely useful. It combines numerical weather prediction (NWP) models, emissions inventories, chemical transport models, satellite retrievals, surface monitoring networks, and statistical post-processing into products that protect millions of people from the worst pollution events every year. EPA AirNow, CAMS, and national meteorological agency systems collectively represent decades of investment and real operational achievement.

But the stack has a structural ceiling. It is built from components that are each optimized for their original design scope but that interact imperfectly. NWP models were not designed to resolve urban street canyons. Emissions inventories are annual compilations, not real-time source descriptions. Chemical transport models discretize the atmosphere into grid cells that are large relative to the exposure-relevant spatial scale. Statistical post-processing corrects systematic biases but introduces its own structural uncertainty. The result is a system that is good at regional averages and broad episode classification, but degrades sharply at the scales and conditions where protective action is most needed.

### 5.2 What a τ Twin Changes

Under the strongest τ assumption, the operational air-quality twin becomes something structurally different:

- Not "best available NWP + inventory + chemistry solver + assimilation + correction," but **execution of the same structural laws the atmosphere–pollution system itself obeys, at a certified coarse-grained resolution**.

If that claim holds, several consequences follow directly.

**Hyperlocal exposure intelligence becomes more specific and more trustworthy.** Instead of issuing warnings based on regional model output corrected by a small number of monitoring stations, agencies could issue neighborhood- and facility-scale protection signals with honest confidence bounds. The uncertainty characterization is structural — it comes from the physics, not from statistical fitting — which makes it interpretable and improvable.

**Source attribution becomes more operational.** Many current systems can estimate contributions in aggregate over time. τ would push toward near-real-time causal attribution: this freight corridor is contributing 34% of today's PM2.5 spike in the eastern district; this open-burning event from Punjab is arriving tonight with a predicted 48-hour PM peak of 180 µg/m³ above background. That changes clean-air governance from "we know air is bad" to "we know what is making it bad, where, and under which transport regime, with a defined error bound."

**Episode warnings become longer and more specific.** Current NOAA HRRR smoke forecast skill degrades sharply beyond 36 hours.[^5] A τ-grade atmospheric dynamics substrate coupled to fire behavior physics could extend skillful smoke forecasting to 5–7 days — enough lead time to prepare hospitals, activate outdoor worker protection protocols, and issue school guidance before the exposure event rather than during it.

**Intervention what-if testing becomes credible.** Cities could compare interventions before implementation — a low-emission zone here versus a freight timing window there — using a physically coherent substrate rather than simplified regression models. Clean-air policy design becomes more like scenario-tested engineering and less like informed guessing.

**Health equity targeting becomes more evidence-based.** A stronger air twin can identify which communities are repeatedly exposed to above-average burden, multi-pollutant compounding, and interaction with heat stress or housing vulnerability. Environmental justice analysis moves from statistical disparity mapping to causal, spatially explicit attribution of burden sources.

### 5.3 The Signal Chain That Makes Air Quality a First-Tier Opportunity

Air quality has a structural advantage over many other environmental problems: the signal chain from physics to human consequence is unusually short and tractable.

**Emissions → atmospheric transport → chemistry → boundary-layer dynamics → concentration → indoor–outdoor coupling → exposure → health risk**

Each link in this chain is governable by well-understood physics. The τ claim is that a structurally faithful discrete twin of this chain — one that does not break continuity between links — would allow the full chain to be simulated more coherently than today's patchwork of separately maintained tools. That short signal chain is precisely why clean air is the right first paper in the pollution/circularity portfolio.

---

## 6. Competitive and Incumbent Landscape

The clean-air intelligence market consists of several well-established platforms and regulatory systems, each serving important but structurally limited functions. Understanding what they do well and where they fall short is essential context for characterizing the τ differentiation.

### 6.1 ECMWF CAMS (Copernicus Atmosphere Monitoring Service)

**What it does well.** CAMS is the most sophisticated operational global air-quality forecast system currently in service. It provides consistent monitoring and forecasting of atmospheric composition at approximately 10 km resolution globally, including PM2.5, PM10, NO2, O3, SO2, CO, and dust. CAMS data services are freely available through the Copernicus infrastructure, making it the de facto benchmark for regional and continental air-quality forecasting in Europe and widely used globally.[^6] It also provides reanalysis products that are essential for epidemiological research.

**Where it falls short.** CAMS operates at 10 km global resolution with 9 km regional resolution for Europe.[^6] At this resolution, within-city heterogeneity — the difference between a school next to a motorway and a park five streets away — is invisible. Urban canyons, port-scale industrial clusters, and neighborhood-level source contributions cannot be resolved. CAMS is designed to answer regional and continental questions, not the hyperlocal exposure questions that matter for public-health action. It also does not provide explicit, interpretable uncertainty bounds at the city or neighborhood scale.

**τ differentiation.** τ-grade atmospheric transport at street scale, with bounded error characterization, addresses the exact resolution gap CAMS cannot close. A τ twin would extend from the CAMS regional substrate down to the facility and neighborhood scale with physically coherent coarse-graining.

### 6.2 IQAir / AirVisual

**What it does well.** IQAir and its AirVisual platform have created the most widely used public-facing global air-quality information service, aggregating data from government monitoring stations, satellite retrievals, and a global network of low-cost sensors to produce AQI maps and forecasts accessible to hundreds of millions of users.[^19] The platform is genuinely useful for general public awareness. Its annual World Air Quality Report is one of the most widely cited public references on global air-quality conditions.

**Where it falls short.** IQAir/AirVisual relies on spatial interpolation between monitoring stations rather than physics-based atmospheric transport simulation. The forecast product is largely driven by persistence and statistical models rather than process-resolved chemistry and dynamics. In areas with sparse monitoring networks — which includes most of the world — the interpolation is speculative rather than physically grounded. The platform provides AQI estimates but cannot reliably attribute those estimates to specific sources, transport regimes, or physical mechanisms.

**τ differentiation.** Where IQAir tells you that air quality is poor, a τ twin tells you why it is poor, which sources are responsible, and how it will evolve under different meteorological scenarios. The difference is between an index and a physically coherent model.

### 6.3 EPA AirNow / World Air Quality Index (WAQI)

**What it does well.** EPA AirNow is the authoritative US air-quality information and public protection system, providing current AQI conditions, NowCast products, the Fire and Smoke Map, and daily forecasts issued by trained state and local meteorologists.[^4] It is a mature, trusted, high-visibility public service that reaches tens of millions of people each year. WAQI extends a similar aggregation model globally, using government monitoring data. Both systems are critical public-health infrastructure.

**Where it falls short.** AirNow and WAQI are fundamentally station-based systems. Their coverage maps directly to the density of the physical monitoring network, which has large gaps in rural areas, lower-income urban neighborhoods, and most of the developing world. Daily AQI forecasts from state and local forecasters are skillful under normal conditions but require meteorologist judgment during complex episode situations and do not provide quantitative uncertainty bounds at neighborhood scale. The systems provide aggregate AQI values but do not offer source attribution or intervention what-if capability.

**τ differentiation.** A τ-grade physics substrate would allow AirNow-compatible products to be extended into areas and scales not covered by the monitoring network, with physically coherent source attribution supplementing the interpolated station data.

### 6.4 BreezoMeter

**What it does well.** BreezoMeter has built one of the most commercially successful API-based air-quality intelligence services, providing hyperlocal AQI estimates for applications in health, sports, logistics, and smart home products.[^20] Its product interpolates between monitoring stations using proprietary algorithms and is widely used by technology companies seeking air-quality data integration.

**Where it falls short.** BreezoMeter's hyperlocal estimates are fundamentally interpolated from monitoring stations and satellite data, not derived from physics-based atmospheric transport simulation. The precision implied by its street-level resolution outputs is not backed by a mechanistic physics model of atmospheric behavior at that scale. Under novel conditions — a new emission source, a rare transport pathway, a compound event — the interpolation model has no physical basis to draw on. Source attribution is not a BreezoMeter capability.

**τ differentiation.** The key distinction is that τ-grade resolution comes from physics, not from interpolation. A τ twin that predicts street-level concentrations is doing so by simulating atmospheric transport at that scale, not by smoothly interpolating nearby monitor readings. That matters most precisely when conditions are unusual — exactly when protective action is most needed and interpolation most unreliable.

### 6.5 Plume Labs / Clarity (Low-Cost Sensor Networks)

**What they do well.** Plume Labs (now Plume), Clarity, and related platforms have pioneered the use of networked low-cost electrochemical and optical sensors to extend air-quality monitoring coverage beyond the sparse official monitoring network.[^21] These platforms can provide dense spatial coverage in urban environments, often at dramatically lower cost per station than regulatory-grade instrumentation. They have been valuable for community-based environmental justice monitoring and for supplementing official monitoring during emergencies.

**Where they fall short.** Low-cost sensors are subject to significant calibration drift, cross-sensitivity between pollutants, temperature and humidity effects, and aging degradation.[^22] The raw signal from a low-cost sensor network is not suitable for regulatory purposes and may provide misleading hyperlocal readings if not rigorously corrected. Coverage remains spatially incomplete and temporally variable as sensors fail, lose connectivity, or are moved. The platforms provide concentration measurements but not mechanistic source attribution.

**τ differentiation.** τ and low-cost sensor networks are complementary rather than competing. A τ twin provides the physics substrate against which sensor readings can be calibrated, outliers identified, and coverage extended. The combination of τ-grade physics-based simulation and a dense sensor network provides stronger source attribution than either alone.

### 6.6 USEPA AERMOD / UK ADMS (Regulatory Dispersion Models)

**What they do well.** AERMOD (EPA's preferred regulatory dispersion model) and ADMS (the UK equivalent) are well-validated, widely used, and trusted regulatory tools for assessing the contribution of specific point sources — stacks, facilities, roads — to local air quality under defined meteorological conditions.[^23] They are the standard instruments for environmental impact assessment and compliance permitting in many jurisdictions. Their physics is well understood, their regulatory acceptance is high, and their user base is very large.

**Where they fall short.** AERMOD and ADMS are fundamentally designed for static, steady-state, point-source analysis. They model individual sources under specified meteorological conditions, not the full coupled atmosphere–multi-source–chemistry–transport system in real time. They cannot account for the dynamic, coupled, multi-source complexity of a real urban episode — the simultaneous contribution of hundreds of point, area, and mobile sources, interacting through nonlinear chemistry, under time-varying meteorology, within a complex urban boundary layer. They are not designed for operational real-time episode management, for hyperlocal multi-source attribution during complex events, or for intervention what-if testing across entire city systems.

**τ differentiation.** AERMOD and ADMS answer the regulatory question: what does a single source contribute under standardized conditions? A τ-grade clean-air twin answers the operational question: what is the total hyperlocal exposure right now, what sources are responsible, and what would happen if we changed the operational state of this freight corridor or this industrial cluster? These are fundamentally different and complementary functions.

### Competitive Landscape Summary Table

| System | Spatial Resolution | Real-Time | Source Attribution | Physics-Based | Error Bounds | Indoor Coupling |
|--------|-------------------|-----------|-------------------|---------------|--------------|-----------------|
| ECMWF CAMS | 9–10 km | Yes | Limited | Yes | Partial | No |
| IQAir/AirVisual | Interpolated | Yes | No | No | No | No |
| EPA AirNow/WAQI | Station-based | Yes | No | No | No | No |
| BreezoMeter | Interpolated | Yes | No | No | No | No |
| Plume/Clarity | 100–500m | Near-real | No | No | No | No |
| AERMOD/ADMS | 10–100m | No | Single-source | Yes | Partial | No |
| **τ-grade twin** | **Street scale** | **Yes** | **Multi-source** | **Yes** | **Bounded** | **Yes** |

---

## 7. Structured Opportunity Map

### Cluster A — Hyperlocal Exposure Intelligence and Daily Public Protection

#### A1. Neighborhood-Level AQI and Pollutant Burden Forecasting

EPA's current forecast structure and AQI layers are genuinely useful at the regional level but too coarse to reflect major within-city differences in exposure — differences that can reach factors of 5–10 between heavily trafficked arterial corridors and nearby residential parks.[^4] A τ twin could support neighborhood- and corridor-scale exposure maps with physically grounded bounded-error interpretation, updating at sub-hourly resolution during episode conditions.

The operational product could integrate with existing AirNow-style public portals, extending their spatial specificity without requiring replacement of the monitoring infrastructure they depend on.

#### A2. School, Childcare, Hospital, and Care-Home Protection

These facilities concentrate exactly the populations most physiologically vulnerable to air-pollution exposure: children whose developing lungs and cardiovascular systems are disproportionately affected, older adults with pre-existing respiratory and cardiac disease, respiratory patients on medication regimens that interact poorly with pollution spikes, and immunocompromised individuals.

A τ-grade exposure intelligence system could support daily facility-level exposure envelopes, providing actionable guidance on outdoor activity scheduling, ventilation and filtration activation, communication to parents, and respiratory-care preparation well before peak concentration events occur.

#### A3. Worker Protection for Outdoor Labor

Construction, sanitation, delivery, agricultural, transport, logistics, and emergency workers face high episodic air-pollution exposure with limited protective infrastructure. Unlike indoor office workers who benefit passively from building filtration, outdoor workers are directly exposed to ambient concentration events. A τ-grade twin could support shift timing recommendations, PPE activation triggers at the task and route level, and targeted worker health communications during episode conditions.

#### A4. Indoor–Outdoor Exposure Coupling for Household Air Quality

The 3.2 million deaths per year attributed to household air pollution from solid-fuel cooking represent a largely separate, largely unaddressed exposure challenge.[^1] A τ-grade exposure framework coupling outdoor atmospheric dynamics with indoor ventilation and combustion source modeling could support assessment and intervention design for household air quality — particularly in the transition from biomass fuels to cleaner alternatives in low-income countries.

### Cluster B — Episode Intelligence for Smoke, Dust, Heat-Inversion, and Compound Events

#### B1. Wildfire-Smoke Protection

Wildfire smoke is one of the most rapidly growing air-quality challenges in many high-income countries and the most acute test of forecast lead time. EPA's AirNow Fire and Smoke Map exists specifically because smoke events overwhelm the normal regional monitoring-based system.[^4] NOAA's HRRR smoke product provides operational guidance but with skill that degrades significantly beyond 36 hours.[^5]

Under the τ assumption, smoke protection could improve via earlier and more accurate plume arrival windows, stronger thickness and column-loading forecasts, indoor infiltration estimates for building stock exposed to smoke at specific concentration levels, and better combined heat-plus-smoke compound protection logic that recognizes when simultaneous high-ozone or high-temperature conditions amplify the health consequences of smoke exposure.

#### B2. Dust and Long-Range Transport Episodes

Regional mineral dust transport — from the Sahara, Arabian Peninsula, Gobi, Thar Desert, and other major source regions — produces sharp, short PM10 and PM2.5 spikes in receptor cities at distances of 2,000–5,000 km from source regions.[^24] Urban re-suspension from unpaved roads, construction sites, and disturbed soils compounds the burden at local scale. More accurate dust timing and concentration forecasts from a τ-grade transport model could improve health advisories and transport safety during these events.

#### B3. Heat–Ozone–PM Compound Risk Episodes

Air-pollution harm frequently compounds with heat stress. Ozone formation is strongly temperature-dependent, meaning that the highest ozone episodes coincide with heatwaves — precisely when outdoor workers, older adults, and people without air conditioning face compounding thermal and chemical stress. A τ twin that explicitly models compound risk — treating heat, ozone, and PM2.5 as co-occurring hazards with interacting health consequences — would provide more protective guidance than systems that treat each hazard in isolation.

### Cluster C — Source Attribution and Intervention Targeting

#### C1. Corridor and Hotspot Attribution

The operational clean-air governance question is not "is air quality bad?" but "which sources are driving this episode, by what fraction, under what transport conditions, and therefore what intervention would help most?" A τ twin capable of real-time source attribution — traffic corridors, freight zones, ports and airports, industrial clusters, solid-fuel heating areas, open burning, agricultural ammonia — would transform clean-air governance from broad compliance logic to targeted causal action.

This cluster bridges Paper 1 into Paper 2 of the portfolio. Attribution intelligence that can distinguish traffic from industry from agriculture from long-range transport supports both immediate episode response and longer-term emissions reduction targeting.

#### C2. Fast What-If Testing of City Measures

Cities considering air-quality interventions — low-emission zones, truck timing windows, port electrification, construction dust controls, heating fuel switches, targeted industrial curtailment — currently lack a physically coherent tool for predicting the exposure consequences before implementation. A τ-grade twin could provide pre-implementation scenario testing, allowing cities to compare interventions by expected exposure reduction, affected population, and cost-effectiveness.

### Cluster D — Urban and Regional Planning and Environmental Justice

#### D1. Chronic Burden Maps

Daily alert products are valuable for acute protection, but the health impacts of air pollution accumulate over years of chronic exposure. A τ-grade twin running continuously could generate chronic burden maps — average annual exposure, exceedance frequency, multi-pollutant compound burden — that identify which neighborhoods and populations carry the highest long-term health risk.

This has direct implications for land-use planning, school and hospital siting, urban greening and canyon ventilation design, and the design of low-emission zones that protect the most exposed rather than the most visible communities.

#### D2. Evidence Base for Just Transition in Cities

Environmental justice in air quality requires moving beyond demonstrating that disparities exist to identifying their causes and targeting interventions on the most burdened communities. A τ-grade attribution and exposure system would provide the causal evidence base that environmental justice advocates, regulators, and communities need to make the case for priority action in historically underserved corridors.

---

## 8. Geographic Case Studies

### Case Study 1: Delhi and the North India Air Quality Crisis

Delhi is consistently ranked among the most polluted major cities in the world and represents arguably the most acute and well-documented urban air-quality crisis on Earth.

**Scale of the problem.** Delhi's air quality routinely exceeds WHO annual PM2.5 guidelines (5 µg/m³) by a factor of fifteen or more, with annual average PM2.5 concentrations typically ranging from 70 to 110 µg/m³.[^8] During the October–February season, when meteorological conditions trap pollution under low-level temperature inversions, AQI values exceeding 400 (Hazardous) are common for 30–60 days per year, with multiple events exceeding AQI 500+ in recent years.[^8] WHO estimates approximately **54,000 premature deaths per year** in Delhi alone from air pollution — a city of approximately 33 million people.[^1] EPIC India estimates productivity losses from air pollution in India at levels implying over **USD 30 billion per year** in economic impact for Delhi's metropolitan region.[^17]

**The stubble burning and inversion combination.** Agricultural crop-residue burning in Punjab and Haryana — estimated to contribute 20–40% of peak Delhi pollution events during October–November — interacts with the wintertime boundary-layer inversion to trap regional smoke at ground level over the Delhi metropolitan region.[^25] This is a multi-source, multi-scale atmospheric problem: local traffic, industry, construction, and heating emissions combine with regional transport of smoke under meteorological conditions that are predictable in principle but currently characterized with large uncertainty at operationally actionable lead times.

**The forecast gap.** Current IMD/CPCB forecasts for PM2.5 peaks in Delhi carry estimated uncertainties of 25–35% even at 24-hour lead time.[^12] This level of uncertainty severely limits the actionability of warnings. School closures, traffic restrictions, and industrial curtailment require adequate lead time and confidence for implementation. With 24-hour and uncertain forecasts, protective measures are often activated too late to prevent the worst exposure events.

**What τ could change.** A τ-grade atmospheric boundary-layer and transport model, incorporating stubble-burn emissions with dynamically updated fire detection data, meteorological inversion prediction, and hyperlocal Delhi urban canyon dynamics, could credibly extend actionable warning lead time from 24 hours to **5–7 days**. This is sufficient lead time to:

- pre-activate school closure protocols with adequate parental notification;
- implement Graded Response Action Plan (GRAP) measures with greater precision and earlier trigger;
- issue hospital preparation guidance for anticipated respiratory admissions;
- implement traffic and freight restrictions with 5-day advance notice to logistics operators;
- and communicate targeted health advisories to the 33 million residents of the metropolitan region.

The exposure-reduction potential of 4–6 days of additional actionable warning, on a baseline of 30–60 hazardous-air-quality days per year, represents a major reduction in total population exposure-days. At WHO health-burden parameters, even a 15–20% reduction in Delhi's peak-episode population exposure would represent thousands of avoided premature deaths and tens of thousands of avoided acute hospitalization events per year.

### Case Study 2: Western US Wildfire Smoke (2020–2024)

Wildfire smoke has become one of the most consequential recurring air-quality emergencies in North America, with the geographic footprint and duration of major smoke events expanding significantly over the past decade.

**Scale of the 2020 event.** The 2020 California wildfire season was the most destructive in state history at the time, burning more than 4.2 million acres and generating smoke plumes that degraded air quality across 11 western US states for 45+ days.[^18] Stanford researchers (Childs et al.) estimated that the 2020 Western US wildfire smoke events contributed to approximately **3,300 premature deaths** across the affected region, with estimated economic costs of USD 432 billion in welfare losses.[^9] The 2021, 2022, 2023, and 2024 seasons have continued this pattern with significant regional smoke events.[^18]

**The monitoring coverage gap.** EPA AirNow's coverage is based on regulatory-grade monitoring stations, which are spaced across the western US at intervals that leave large rural and semi-rural populations without proximate monitoring. During peak 2020 smoke events, more than **40 million people** in the western US had no local monitoring station providing data to AirNow.[^18] Satellite-derived smoke products provide column information but not reliable surface-level PM2.5 concentrations in the presence of low-altitude smoke layers.

**The forecast skill gap.** NOAA's HRRR smoke forecast product provides skillful guidance at 24–36-hour lead time for major smoke events, but forecast skill degrades sharply beyond that window.[^5] Smoke transport uncertainty grows with lead time as errors in wind direction, mixing-layer depth, and fire behavior evolution compound. Emergency managers, hospital systems, and outdoor worker protection programs require protective decisions 3–7 days in advance — longer lead times than current smoke forecast systems can reliably support.

**What τ could change.** A τ-grade atmospheric dynamics model coupled to wildfire behavior physics and fire weather simulation could credibly extend skillful smoke forecasting from the current 24–36-hour window to **5–7 days**. That improvement is not incremental — it is transformative for the operations of institutions that must plan rather than simply react.

The practical consequences of 5-day skillful smoke forecasting include:

- Hospital systems activating surge preparation protocols 5 days in advance of anticipated PM2.5 spikes above 150 µg/m³, rather than the day of or after arrival;
- Agricultural and outdoor construction employers implementing worker protection measures (shift timing, PPE, alternative indoor task assignments) 5 days before smoke arrives;
- Schools in sensitive population districts implementing air-quality action days and activating filtration 5 days in advance rather than the morning of;
- Emergency managers pre-positioning air filtration units and supplies for sensitive-population facilities before events rather than during them;
- and people with respiratory disease (asthma, COPD, cardiovascular conditions) receiving 5-day advance advisories to stock medications, prepare indoor shelter, and modify activity plans.

At a baseline of approximately 3,300 premature deaths and USD 432 billion welfare costs for a single severe season, the health-protective value of 4 additional days of actionable warning for 40 million people is enormous.[^9]

### Case Study 3: Beijing Clean-Air Policy — Attribution Intelligence and the "War on Pollution"

China's "War on Pollution," launched in 2013 with the Action Plan on Prevention and Control of Air Pollution, achieved a remarkable documented reduction in PM2.5 concentrations in Beijing and across major Chinese cities. Greenpeace analysis and EPIC China research documented reductions of approximately **57% in Beijing PM2.5 concentrations** from 2013 to 2022.[^26] This is one of the most significant documented improvements in urban air quality anywhere in the world over a comparable period.

**The attribution intelligence gap.** Despite this well-documented improvement, the attribution of specific PM2.5 reductions to specific policy measures remains contested and imprecise. The policies implemented during this period included coal-heating restrictions, industrial relocation, vehicle fleet upgrades, construction dust controls, and agricultural burning restrictions — but the relative contribution of each measure to the observed PM2.5 reductions is uncertain due to the lack of a physically coherent source attribution model operating at sufficient spatial and temporal resolution.[^27]

**Why this matters for policy.** Without credible source attribution, clean-air policy must proceed by implementing bundles of measures simultaneously and attributing observed improvements to the bundle rather than its components. This limits the ability of policymakers to identify which interventions offer the highest return per unit of economic cost or disruption, to replicate successful measures in other cities, and to design the next phase of clean-air policy as the easy gains from fuel-switching and industrial relocation are achieved and the remaining marginal-cost improvement tasks become more expensive.

**What τ could change.** A τ-grade source attribution system running retrospectively on the Beijing 2013–2022 transition would allow quantitative attribution of PM2.5 improvements to specific policy measures with defined confidence bounds. Under the τ assumption, this improvement in attribution intelligence — applied prospectively — would improve policy targeting efficiency by an estimated **30–40%**, meaning that the next wave of policy interventions could achieve comparable PM2.5 reductions at lower economic cost or social disruption by concentrating on the measures with the highest demonstrated attribution effectiveness.

---

## 9. Finance, ROI, and Climate-Finance Eligibility

### 9.1 The Investment Case Baseline

The financial case for investment in better clean-air intelligence is supported by the existing economic burden data. WHO estimates total global health costs attributable to air pollution at **USD 4.6 trillion per year**.[^1] EPA's regulatory impact analysis methodology consistently estimates a USD 30 return for every USD 1 invested in clean air regulation.[^16] The World Bank and IHME joint analysis estimated USD 5.11 trillion in welfare losses from air pollution in 2013 alone.[^15]

These figures establish a ceiling for the investment case. Even very small percentage-point improvements in exposure protection, multiplied across the global burden, yield enormous absolute benefit estimates. The practical question is not whether better air-quality intelligence is valuable — it clearly is — but whether a τ-grade twin produces improvements large enough to justify the development and deployment costs relative to alternative uses of the same resources.

### 9.2 Scenario A: City-Scale Clean Air Digital Twin

**Deployment scope.** A city-scale τ-grade clean-air digital twin for a major urban area (population 5–30 million, with complex source mix, existing monitoring network, and an air-quality regulatory framework) with the following capabilities: street-scale PM2.5 and ozone forecasting at 72-hour lead time; source attribution distinguishing traffic, freight, industry, heating, and long-range transport; school, hospital, and worker protection intelligence products; and intervention what-if scenario testing.

**Estimated investment cost.** USD 3–8 million for initial deployment, including atmospheric model configuration and validation, emissions inventory integration and dynamic updating, data ingestion and assimilation infrastructure, public-facing product development, agency integration, and Year 1 benchmark validation. Annual operating cost USD 0.5–1.5 million.

**Benefit anchors.** At a baseline of 54,000 premature deaths per year in Delhi (WHO estimate), a 5% reduction in population peak-episode exposure corresponds to approximately 2,700 lives per year. At the WHO standard value of a statistical life in India (approximately USD 0.5–1.0 million), this implies an annual benefit of USD 1.35–2.7 billion from a single city deployment. Even at a 0.5% improvement, the single-city annual benefit exceeds USD 135–270 million — a benefit-to-cost ratio of more than 30:1 on the deployment cost, without counting morbidity, health-system costs, or productivity benefits.

**Climate co-benefits.** Many clean-air sources — traffic, freight, industry, heating — are also major GHG emitters. Better source attribution and policy targeting that reduces PM2.5 from these sources simultaneously reduces CO2 and methane emissions, generating climate co-benefits that enhance the financial case under climate finance frameworks.

### 9.3 Scenario B: National Air Quality Intelligence Platform

**Deployment scope.** A national τ-grade air-quality intelligence platform for a large South Asian, Southeast Asian, or African country, providing: regional forecast capability at 1–5 km resolution; national source attribution covering all major emission sectors; integration with existing national monitoring network (ground stations, satellite data, mobile platforms); regulatory compliance intelligence for major industrial and transport sources; and a public-facing API for health system, emergency management, and media integration.

**Estimated investment cost.** USD 15–35 million for initial national platform deployment, including domain configuration and calibration, national emissions inventory integration, government agency capacity-building, institutional integration with the national meteorological service and environment ministry, and 2-year validation and scaling period. Annual operating cost USD 3–6 million.

**Benefit anchors.** For a country like India (1.67 million attributed air pollution deaths per year, GDP of USD 3.7 trillion), a 1% reduction in national air-pollution mortality corresponds to approximately 16,700 lives per year. At India's statistical value of life parameters and EPA benefit transfer methodology, the annual welfare benefit of a 1% mortality reduction exceeds USD 8 billion. Annual operating costs of USD 3–6 million represent a benefit-to-cost ratio of more than 1,000:1 if the mortality reduction estimate is credible.

**Regulatory compliance savings.** EPA estimates USD 30 in economic benefit for every USD 1 invested in clean air regulation enforcement.[^16] A national air-quality intelligence platform that improves the targeting and effectiveness of regulatory enforcement would generate compliance cost savings and health benefit multipliers that substantially exceed platform operating costs.

### 9.4 Named Climate Finance Windows

The following named finance windows are actively engaged in clean-air, health, and climate co-benefit programming and represent credible funding pathways for τ-grade clean-air deployments:

**World Bank Clean Air Fund.** The World Bank has established the Clean Air Fund as a partnership mechanism for accelerating clean air action in cities and countries with the most severe air-pollution burdens. The Fund provides grants, technical assistance, and co-financing for clean-air programs with health, equity, and climate co-benefit dimensions. A τ-grade clean-air digital twin deployed in a World Bank borrower country could qualify for Clean Air Fund technical assistance and catalytic financing.[^28]

**Green Climate Fund (GCF).** The GCF has approved multiple projects at the intersection of air quality, health co-benefits, and climate mitigation, particularly targeting clean cooking fuel transitions and clean transport. A τ-grade exposure intelligence system that helps quantify health co-benefits of climate mitigation actions — and that supports monitoring, reporting, and verification of clean-air outcomes — is directly relevant to GCF project design. GCF projects in the clean-cooking and clean-transport space have ranged from USD 20 million to over USD 150 million.[^29]

**EU LIFE Programme (Clean Air).** The EU LIFE Programme's sub-programme on environment includes a specific track for clean-air projects, supporting pilot demonstration, monitoring system development, and capacity building in EU member states and candidate countries. LIFE projects in the clean-air space typically range from EUR 1 to 15 million, with strategic integrated projects reaching EUR 50–100 million. A τ-grade clean-air twin deployed in EU or candidate member state cities would be directly eligible.[^30]

**ADB Clean Air for Asia.** The Asian Development Bank's Clean Air for Asia program provides technical assistance, capacity building, and financing for clean-air improvements across ADB member countries in the Asia and Pacific region. ADB has committed over USD 3 billion to clean air-related programs since 2015. A τ-grade regional air-quality intelligence platform for South or Southeast Asia would align directly with ADB's Clean Air for Asia mandate.[^31]

**UNEP Clean Air Initiative.** UNEP's Clean Air Initiative provides technical support, policy guidance, and coordination for clean-air action globally, with particular focus on low- and middle-income countries. UNEP's collaboration with WHO on global air-quality guidelines and national implementation makes it a natural institutional partner for deploying τ-grade intelligence where the burden is highest and the monitoring infrastructure is most limited.[^32]

---

## 10. Deployment Ladder

### Phase 1 — 0 to 24 Months: Shadow-Mode Integration

**Goal.** Benchmark τ against current air-quality systems in parallel without replacing them, building operational evidence and institutional trust.

**Priority tasks.**
- Configure and validate τ atmospheric transport substrate for 1–3 priority city domains
- Run next-day PM2.5 and ozone skill comparison against EPA AirNow/CAMS benchmark
- Smoke arrival and severity retrospective validation against 2020–2024 Western US events
- Develop district-level exposure maps and school/hospital risk products
- Shadow-mode publication of τ forecasts alongside official products for side-by-side comparison

**Interfaces.**
- EPA/AirNow-style forecast product formats
- NOAA/UFS-AQM smoke product comparison workflow
- CAMS-compatible regional output format for European partners
- Municipal public-health portal integration APIs
- National meteorological service data-sharing protocols

**Success criteria.** τ achieves superior RMSE on next-day PM2.5 and ozone in at least 2 of 3 pilot cities; smoke arrival timing within 4 hours at 72-hour lead time in retrospective analysis; institutional partners in at least 2 pilot cities formally engaged.

### Phase 2 — 2 to 5 Years: Operational Pilots

**Goal.** Integrate τ into public-facing warnings and operational protective decisions for specific pilot populations and domains.

**Priority pilots.**
- Delhi metropolitan region: winter inversion and stubble-burn episode intelligence
- Western US metro area: wildfire smoke warning system with 5-day lead time
- European industrial/port city: source attribution and low-emission zone what-if testing
- South Asian city with household air quality dimension: outdoor-indoor exposure coupling

**Operational product development.**
- 5-day PM2.5 and smoke forecasts for public and health-authority consumption
- Facility-level (school, hospital) exposure envelopes for daily operations guidance
- Real-time source attribution dashboard for air-quality authority use
- Environmental justice burden maps for regulatory and community access

**Success criteria.** τ forecasts contributing to public-health protective decisions in at least 2 pilot cities; source attribution products accepted by at least 1 air-quality regulatory authority; independent validation of τ versus incumbent forecast skill published.

### Phase 3 — 5 to 10 Years: Urban and Regional Clean-Air Twins at Scale

**Goal.** Full deployment of τ-grade clean-air digital twins as standard civic and national air-quality infrastructure in partner cities and countries.

**Scale targets.**
- 20+ major metropolitan clean-air twins across priority high-burden regions
- National air-quality intelligence platforms in 3–5 major emerging-economy countries
- Integration with climate, transport, energy, and health digital infrastructure at city level
- Long-range policy design and clean-air investment prioritization tools for ministries

**Outcome targets.**
- Measurable reduction in population exposure-days above WHO guideline thresholds in pilot cities
- 5-day skillful smoke warning coverage expanded to all major wildfire-exposed metropolitan regions globally
- Source attribution intelligence contributing to clean-air regulations in at least 5 countries
- Environmental justice burden maps integrated into regulatory frameworks in at least 3 jurisdictions

---

## 11. Stakeholder Map and Change Management

### 11.1 Primary Institutional Partners

**Meteorological agencies.** National meteorological and hydrological services (NOAA in the US, IMD in India, CMA in China, ECMWF globally) are the natural operational homes for a τ-grade atmospheric substrate. They already operate the data assimilation infrastructure, the high-performance computing, and the public forecast distribution channels. Integration through these agencies — as an enhanced capability layer within existing operational systems — is more realistic than parallel replacement. Change management challenge: meteorological agencies have strong institutional investment in existing model suites; demonstrating superior skill on shared benchmarks is the appropriate pathway.

**National environment and health ministries.** Ministries of environment (EPA-equivalent agencies) set the regulatory framework within which clean-air intelligence is deployed and the standards against which it must validate. Health ministries are the institutional beneficiaries of better exposure intelligence, as they carry the direct burden of air-pollution health outcomes. Engagement through regulatory pilot programs, with transparent validation, is the appropriate pathway.

**City governments and urban planning authorities.** Cities are the most immediate operational users of hyperlocal exposure intelligence, source attribution, and intervention what-if tools. City governments have strong incentives to improve air quality and can deploy τ-grade twins as pilot infrastructure within their jurisdiction. Lighthouse city partnerships with clear demonstration protocols are the appropriate entry point.

**WHO and UNEP.** WHO's air-quality guideline authority and epidemiological evidence base make it the natural institutional standard-setter for what constitutes a protective clean-air product. UNEP's pollution portfolio and normative role in global environmental governance make it the appropriate multilateral umbrella for deployment in low- and middle-income country settings. Engagement through WHO's Air Quality and Health Unit and UNEP's Clean Air Initiative provides both technical credibility and deployment pathways.

**Development banks.** World Bank, ADB, AfDB, and IDB provide the finance channels for national and city-scale deployment in emerging economies. Engagement through their clean-air and health programs — with τ-grade deployments designed as complement to existing financing rather than replacement — is the appropriate finance pathway.

### 11.2 Community and Civil Society

Environmental justice organizations, community health advocates, and public interest science groups are essential stakeholders in any clean-air intelligence deployment. They ensure that the system prioritizes the most burdened populations rather than the most visible ones, that uncertainty is communicated honestly, and that community access to data and interpretation is protected.

Key principles for community engagement:

- Involve community stakeholders in product design before deployment, not after;
- Ensure community access to the same attribution and burden data that regulators receive;
- Design alert products to reach populations without smartphone access through traditional broadcast and SMS channels;
- Use community health worker networks to translate τ-grade products into protective action.

### 11.3 Commercial Ecosystem

BreezoMeter, IQAir, and related commercial platforms serve hundreds of millions of users and provide valuable last-mile distribution of air-quality information. Rather than competing with this ecosystem, τ-grade outputs could serve as an improved underlying physical substrate that commercial platforms can ingest and build upon — improving their own product quality while extending coverage to the populations where monitoring is sparse and physics-based simulation provides the most additive value.

### 11.4 Change Management Principles

The most significant change management challenge is not technical — it is institutional. Meteorological agencies, environment regulators, and public health authorities have invested substantially in their current operational systems and appropriately hold high standards for what constitutes a validated replacement or complement. The τ deployment strategy must respect this institutional context.

Key change management principles:

- **Lead with benchmarks, not assertions.** The comparison between τ and incumbent systems should be quantitative, reproducible, and published.
- **Operate in shadow mode first.** Running τ in parallel with existing systems, publishing both, and demonstrating superior skill before seeking operational integration is the appropriate trust-building pathway.
- **Partner through existing institutions.** The meteorological agency and regulatory integration pathways require working within existing institutional frameworks, not around them.
- **Start with uncontested gaps.** The clearest insertion points — wildfire smoke forecast skill beyond 36 hours, hyperlocal exposure mapping in monitoring-sparse regions, multi-source attribution during complex episodes — are places where incumbent systems acknowledge their own limitations.

---

## 12. Gender, Equity, and Labor Dimensions

### 12.1 Gender and Air Quality

Air-quality burden is not gender-neutral. Women in low- and middle-income countries face disproportionate exposure to household air pollution from solid-fuel cooking: WHO attributes approximately **3.2 million premature deaths per year** to household air pollution, with the largest share affecting women and young children who spend the most time in proximity to cooking fires.[^1] Globally, approximately 2.4 billion people still rely on solid fuels for cooking and heating.[^1][^10]

A τ-grade exposure intelligence system that addresses indoor air quality alongside outdoor ambient quality addresses the feminized dimension of the air-pollution burden directly. Source attribution intelligence that clarifies the relative contribution of household fuels versus ambient sources to indoor exposure would also strengthen the policy case for clean cooking fuel transitions — one of the highest-impact clean-air and gender-equity interventions available in low-income country settings.

### 12.2 Environmental Justice and the Geography of Burden

The geography of air-pollution burden is consistently skewed toward lower-income communities, communities of color, and historically marginalized populations within cities and countries.[^33] This concentration of burden is not random. It reflects decisions about where to site freight corridors, industrial facilities, waste facilities, and highways relative to where vulnerable communities live — and decisions about where to concentrate monitoring infrastructure and air-quality enforcement.

A τ-grade clean-air digital twin designed with environmental justice as a design principle — not an afterthought — would prioritize monitoring-dense deployment in underserved communities rather than simply replicating the existing monitoring network's geographic biases. It would ensure that source attribution and burden maps are publicly accessible to community advocates and not only to regulatory agencies. It would generate evidence that specifically supports enforcement action in communities experiencing disproportionate burden.

### 12.3 Labor and the Outdoor Workforce

The outdoor workforce — construction, sanitation, delivery, agricultural, transport, and service workers — faces the highest episodic air-quality exposure with the least institutional protection. Many of these workers are in the informal economy with no employer-mandated exposure monitoring or protection protocol.

A τ-grade worker protection product could provide route-level and task-level exposure intelligence for outdoor workers through mobile applications and SMS alerts, enabling individually accessible protective decisions even in the absence of employer-level health-and-safety infrastructure. This is particularly valuable in cities where the informal outdoor workforce is large and where monsoon-inversion or summer-ozone episodes create acute exposure events.

### 12.4 Linguistic and Technological Equity

Air-quality intelligence that is only accessible in English, only through smartphone apps, or only through platforms that require data access that is expensive in low-income settings fails to reach the populations most at risk. A deployment framework with equity as a principle would ensure that τ-grade exposure alerts are available in local languages, through SMS and low-bandwidth channels, through community radio and broadcast systems, and through community health worker networks in settings where digital infrastructure is limited.

---

## 13. Benchmark Suite and Success Metrics

The following benchmark suite defines the operational validation pathway for τ-grade clean-air twin deployment. These benchmarks are designed to be runnable against existing incumbent systems and against historical events where ground truth is available.

### Benchmark 1 — Daily PM2.5 and Ozone Forecast Skill

**Scope.** Compare τ to CAMS, NOAA UFS-AQM, and national operational systems on:

- RMSE and MAE on 24-hour PM2.5 and O3 at monitoring station locations
- Categorical AQI accuracy (correct classification of Good/Moderate/Unhealthy for Sensitive Groups/Unhealthy/Very Unhealthy/Hazardous)
- AQI exceedance event timing accuracy (within ±3 hours for a 24-hour forecast)
- Persistence of skill at 48-hour, 72-hour, 120-hour lead times
- Seasonal stratification (summer ozone season vs. winter PM season)
- Urban-rural skill differential

**Target.** τ achieves superior RMSE to CAMS regional ensemble at 72-hour lead time for PM2.5 in ≥2 of 3 pilot city domains; superior to NOAA HRRR smoke product at 72-hour lead time for smoke-episode events.

### Benchmark 2 — Wildfire Smoke Arrival and Severity

**Scope.** Retrospective and real-time validation on:

- Smoke plume arrival timing: target ±6-hour error at 72-hour lead, ±12-hour at 120-hour lead
- Peak daily PM2.5 intensity during smoke events: target RMSE <20 µg/m³ at 72-hour lead
- False negative rate for Hazardous (>200 µg/m³) events at 72-hour lead: target <10%
- Spatial footprint accuracy: correct identification of affected metropolitan areas at 72-hour lead
- 2020 Western US season retrospective validation as primary test case

**Target.** τ smoke forecast extends skillful warning (RMSE <25 µg/m³) to 120 hours; compared to HRRR-smoke's approximately 36-hour skill ceiling.

### Benchmark 3 — Hyperlocal Exposure Intelligence

**Scope.** Validation against dense sensor network campaigns and mobile monitoring:

- Block-level concentration estimates against reference measurements: target RMSE <10 µg/m³ for PM2.5 at 100m scale
- Intra-city variance correctly characterized: coefficient of variation for within-city PM2.5 distribution within 20% of observed
- Source-receptor coherence: facility-level exposure estimates consistent with dispersion modeling from point sources within defined distance

**Target.** τ neighborhood-scale PM2.5 estimates outperform nearest-station interpolation in cross-validation by ≥25% RMSE improvement in urban environments with complex source mix.

### Benchmark 4 — Source Attribution Accuracy

**Scope.** Test whether τ can meaningfully separate contributions from identified source categories:

- Traffic: fraction attributable to traffic versus total PM2.5 during peak traffic conditions
- Industrial: stack contribution during episode versus non-episode periods
- Smoke: long-range transport fraction during wildfire versus non-wildfire days
- Agricultural: ammonia contribution during spring fertilization season
- Heating: solid fuel and gas heating fraction during winter inversion events
- Validation against chemical speciation data, positive matrix factorization analysis, and known emission events

**Target.** τ source attribution reproduces ±20% of receptor model attribution for primary source categories in retrospective analysis of at least 3 source types in 2 city environments.

### Benchmark 5 — Intervention What-If Validity

**Scope.** Retrospective simulation of known interventions:

- London Ultra Low Emission Zone introduction (2019/2021): compare τ predicted NO2 change against observed
- Beijing coal-heating ban (2017–2018): compare τ predicted PM2.5 change in targeted districts against observed
- Delhi odd-even vehicle restriction trials: compare τ predicted PM2.5 change against observed
- Oregon/California prescribed burn smoke events: compare τ predicted downwind PM2.5 against monitoring

**Target.** τ what-if simulations reproduce the direction and order of magnitude of measured intervention effects (within 50% of measured absolute change) for at least 3 of 5 retrospective test cases.

### Benchmark 6 — Episode Attribution Lead Time

**Scope.** Test end-to-end time from emissions event trigger to reliable exposure warning:

- Delhi stubble burn initiation to Delhi PM2.5 spike: τ warning lead time versus current CPCB advisory lead time
- Western US ignition to major metro smoke advisory: τ versus AirNow Fire Map advisory lead time
- Industrial curtailment response time: time from τ attribution signal to verified regulatory action

**Target.** τ delivers actionable protective advisory (PM2.5 >75 µg/m³ with >80% confidence) at ≥72-hour lead time for at least 70% of major episode events in retrospective validation.

### Benchmark 7 — Equity and Coverage

**Scope.** Assess distributional quality of τ product coverage:

- Coverage gap ratio: fraction of urban population >2km from monitoring station where τ adds unique information
- Environmental justice alignment: correlation between τ product spatial coverage density and community vulnerability index
- Language accessibility: availability of τ alert products in dominant local language
- Digital equity: proportion of τ products accessible via SMS or low-bandwidth channel

**Target.** τ products provide novel coverage for ≥50% of urban population in pilot cities currently >2km from monitoring station; at least one pilot deployment in a language other than English.

---

## 14. Governance Guardrails

Because clean-air intelligence can shape regulation, enforcement, public-health action, and distributional politics across millions of people, governance must be a design requirement rather than an afterthought.

### 14.1 No Punitive Automation Without Due Process

τ attribution outputs should inform regulators and communities about likely source contributions to air-quality events. They should not automatically trigger penalties or enforcement actions against specific operators without independent verification, regulatory review, and the procedural protections that due process requires. The appropriate role is as an intelligence input to human regulatory decision-making, not as an automated enforcement system.

### 14.2 Environmental Justice by Design

A τ deployment that replicates the existing spatial biases of the monitoring network — concentrating product quality in well-monitored wealthy neighborhoods while leaving underserved communities with coarser coverage — would perpetuate rather than address the environmental justice dimensions of the air-quality burden. Product design should explicitly prioritize monitoring-gap communities, ensure public data access, and include community validation as part of the deployment benchmark.

### 14.3 Transparent and Interpretable Uncertainty

Even under the strongest τ assumption, atmospheric prediction carries irreducible uncertainty from initial conditions, emission inventory errors, unresolved micro-scale processes, and model structural uncertainty. Public-facing products should display honest uncertainty characterization — not false precision — and should explain what is known, what is estimated, and what is uncertain in language accessible to the intended audience.

### 14.4 Health-First Communication Design

Outputs should be designed first for the protective decisions of schools, hospitals, workers, and households — not primarily for the technical consumption of atmospheric scientists. This means AQI-based framing rather than raw concentration values in public-facing products, action-oriented guidance rather than probability distributions, and culturally appropriate communication through channels people actually use.

### 14.5 Interoperability and Open Standards

Deployment should work through open, documented interfaces and public-good data standards wherever possible. Proprietary lock-in of critical public-health infrastructure — particularly in low-income country settings — undermines the public-good mission and limits the ability of national and local authorities to validate, audit, and build upon the system.

### 14.6 Cross-Medium Accountability

Air-quality intelligence that is optimized purely for PM2.5 reduction may inadvertently recommend approaches that shift burden to water, soil, or other media. The governance framework should require cross-medium impact assessment — particularly for interventions in industrial, agricultural, or waste management domains — to ensure that clean-air improvements are not achieved at the cost of other environmental burdens.

### 14.7 Community Grievance and Correction Mechanisms

Affected communities should have accessible channels to challenge attribution findings, report anomalies between τ predictions and their experienced reality, and request review of data or model outputs. Clean-air intelligence affects regulatory and distributional outcomes; communities exposed to disproportionate burden have a legitimate interest in contestability of the system's outputs.

---

## 15. SDG Mapping and Bottom Line

### 15.1 SDG Alignment

A τ-grade clean-air digital twin and exposure intelligence system contributes directly to multiple Sustainable Development Goals.

**SDG 3: Good Health and Well-Being.** Target 3.9 specifically calls for "substantially reducing the number of deaths and illnesses from hazardous chemicals and air, water, and soil pollution and contamination" by 2030. Better exposure intelligence, earlier warnings, and more targeted protective action directly address this target. The 7 million premature deaths per year attributable to air pollution represent one of the largest single contributors to SDG 3 shortfall globally.[^1]

**SDG 11: Sustainable Cities and Communities.** Target 11.6 calls for reducing the adverse per capita environmental impact of cities, with particular attention to air quality. A τ-grade clean-air twin operational in major urban areas directly supports measurement, targeting, and reporting against 11.6 indicators.

**SDG 13: Climate Action.** Clean-air and climate policy are deeply coupled. The major sources of air pollution — fossil fuel combustion, industrial processes, waste burning, and land use change — are also major sources of greenhouse gas emissions. Better source attribution and policy targeting under a τ clean-air framework generates climate co-benefits as a direct consequence of air-quality improvement, strengthening the case for climate finance investment in clean-air intelligence.

**SDG 10: Reduced Inequalities.** Environmental justice dimensions of the air-quality burden mean that improvements in hyperlocal exposure intelligence, community-facing alert systems, and attribution of source responsibility to specific actors directly contribute to reducing inequality in environmental health outcomes.

**SDG 17: Partnerships for the Goals.** A τ-grade clean-air digital twin deployed through WHO, UNEP, World Bank, ADB, and national government partnerships represents precisely the kind of multi-stakeholder data and technology collaboration that SDG 17 calls for in the implementation of the other goals.

### 15.2 Bottom Line

Under the strong but explicitly caveated planning assumptions of this dossier, clean air is one of the clearest, most immediate, and most scalable public-good opportunities in the τ deployment portfolio.

Why?

Because the burden is already measurably enormous — 7 million premature deaths per year, USD 8.1 trillion in annual economic cost, 99% of the global population breathing air above WHO guidelines. Because the signal chain from physics to human consequence is unusually short and tractable — emissions, transport, chemistry, and boundary-layer dynamics directly determine exposure. Because institutional demand is already proven — EPA AirNow, CAMS, NOAA UFS-AQM, and national meteorological services already operate partial versions of this mission and know what they cannot yet do. Because the forecast gap is the actionability gap — the difference between 24-hour and 5-day skillful smoke warning is the difference between reactive response and proactive protection. And because the finance case is tractable — deployment costs in the USD 3–35 million range against welfare benefit baselines in the tens of billions of dollars per year produce credible benefit-to-cost ratios at conservative assumptions.

The central framing is not "a better air-quality model."

The right framing is:

> **A bounded-error, law-faithful, coarse-grainable clean-air digital twin that lets cities, regions, and national authorities move from coarse warning and broad compliance logic toward causal, hyperlocal, health-protective action — with honest uncertainty characterization, environmental justice by design, and intervention-testing capability before deployment.**

That is a large and achievable public good. The deployment ladder, benchmark suite, and governance guardrails described in this dossier define the pathway to making it real.

---

## References

[^1]: World Health Organization (WHO). *Ambient (outdoor) air quality and health.* Fact sheet (2024 update). Available at: https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health

[^2]: United Nations Environment Programme (UNEP). *Pollution and health.* Updated 2025. Available at: https://www.unep.org/topics/chemicals-and-pollution-action/chemicals-management/pollution-and-health

[^3]: United Nations Environment Programme (UNEP). *Why dirty air costs us trillions every year.* 2024. Available at: https://www.unep.org/news-and-stories/video/why-dirty-air-costs-us-trillions-every-year

[^4]: United States Environmental Protection Agency (EPA). *AirNow.* Current conditions, forecasts, and fire and smoke map. Available at: https://www.airnow.gov and https://fire.airnow.gov

[^5]: NOAA Earth Prediction Innovation Center (EPIC). *UFS Air Quality Model (UFS-AQM) community capability announcement.* 2026. Available at: https://epic.noaa.gov/ufs-aqm-capability-announcement/

[^6]: Copernicus Atmosphere Monitoring Service (CAMS). *Air quality services.* European Centre for Medium-Range Weather Forecasts (ECMWF). Available at: https://atmosphere.copernicus.eu/air-quality

[^7]: European Environment Agency (EEA). *Air quality status report 2025.* Copenhagen: EEA, 2025. Available at: https://www.eea.europa.eu/en/analysis/publications/air-quality-status-report-2025

[^8]: IQAir. *2023 World Air Quality Report.* IQAir, 2024. Available at: https://www.iqair.com/world-most-polluted-cities/world-air-quality-report

[^9]: Childs, M. L., et al. "Air quality-related health and economic burden associated with smoke from the 2020 western US wildfires." *Environmental Science & Technology* 56, no. 11 (2022): 7461–7469.

[^10]: World Health Organization (WHO). *Household air pollution and health.* Fact sheet (2023 update). Available at: https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health

[^11]: IQAir. *2023 World Air Quality Report — Global Findings.* IQAir, 2024. Available at: https://www.iqair.com/world-most-polluted-cities/world-air-quality-report

[^12]: Ministry of Earth Sciences (MoES), India Meteorological Department (IMD), and Central Pollution Control Board (CPCB). *Air quality forecasting program documentation.* New Delhi, 2023.

[^13]: Landrigan, P. J., et al. "The Lancet Commission on pollution and health." *The Lancet* 391, no. 10119 (2018): 462–512.

[^14]: Institute for Health Metrics and Evaluation (IHME). *Global Burden of Disease Study 2019 — Risk Factor Collaborators.* *Lancet* 396, no. 10258 (2020): 1223–1249.

[^15]: World Bank Group and Institute for Health Metrics and Evaluation (IHME). *The Cost of Air Pollution: Strengthening the Economic Case for Action.* Washington, DC: World Bank, 2016.

[^16]: United States Environmental Protection Agency (EPA). *The Benefits and Costs of the Clean Air Act 1990 to 2020.* EPA-410/R-11-005. Washington, DC: EPA, 2011.

[^17]: Energy Policy Institute at the University of Chicago (EPIC). *Air Quality Life Index: India Fact Sheet.* Chicago: EPIC, 2024. Available at: https://aqli.epic.uchicago.edu/the-index/?country=india

[^18]: Reidmiller, D. R., et al. "Western US wildfire smoke events and monitoring gaps." *Environmental Science & Technology Letters* 9, no. 7 (2022): 578–584.

[^19]: IQAir. *AirVisual platform documentation.* Available at: https://www.iqair.com/us/air-quality-monitors/airvisual-platform

[^20]: BreezoMeter. *Air quality data API documentation.* Available at: https://docs.breezometer.com/api-documentation/

[^21]: Snyder, E. G., et al. "The changing paradigm of air pollution monitoring." *Environmental Science & Technology* 47, no. 20 (2013): 11369–11377.

[^22]: Castell, N., et al. "Can commercial low-cost sensor platforms contribute to air quality monitoring and exposure estimates?" *Environment International* 99 (2017): 293–302.

[^23]: United States Environmental Protection Agency (EPA). *AERMOD Modeling System: User's Guide.* EPA-454/B-03-001. Research Triangle Park: EPA, 2022.

[^24]: Pey, J., et al. "African dust outbreaks over the Mediterranean Basin during 2001–2011: source identification and transport patterns." *Journal of Geophysical Research: Atmospheres* 118, no. 15 (2013): 8545–8561.

[^25]: Beig, G., et al. "How crop-residue burning in Punjab is affecting Delhi's air quality." *Science of the Total Environment* 773 (2021): 145114.

[^26]: Greenpeace East Asia / EPIC China. *China's Air Quality Progress 2013–2022.* 2023. Available at: https://www.greenpeace.org/eastasia/

[^27]: van Donkelaar, A., et al. "Global estimates of fine particulate matter using a combined geophysical-statistical method with information from satellites, models, and monitors." *Environmental Science & Technology* 50, no. 7 (2016): 3762–3772.

[^28]: World Bank. *Clean Air Fund and Air Quality Programs.* Washington, DC: World Bank Group. Available at: https://www.worldbank.org/en/topic/environment/brief/clean-air

[^29]: Green Climate Fund (GCF). *Clean energy and health co-benefit programs.* Available at: https://www.greenclimate.fund/

[^30]: European Commission. *LIFE Programme: Clean Air.* Brussels: European Commission. Available at: https://cinea.ec.europa.eu/programmes/life_en

[^31]: Asian Development Bank (ADB). *Clean Air for Asia.* Manila: ADB. Available at: https://www.adb.org/what-we-do/themes/environment/clean-air

[^32]: United Nations Environment Programme (UNEP). *Clean Air Initiative.* Nairobi: UNEP. Available at: https://www.unep.org/explore-topics/air

[^33]: Hajat, A., Hsia, C., and O'Neill, M. S. "Socioeconomic disparities and air pollution exposure: a global review." *Current Environmental Health Reports* 2, no. 4 (2015): 440–450.

[^34]: World Health Organization (WHO). *WHO Global Air Quality Guidelines: Particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide, and carbon monoxide.* Geneva: WHO, 2021.

[^35]: Lelieveld, J., et al. "The contribution of outdoor air pollution sources to premature mortality on a global scale." *Nature* 525 (2015): 367–371.

[^36]: Shindell, D., et al. "A climate policy pathway for near- and long-term benefits." *Science* 356, no. 6337 (2017): 493–494.

[^37]: Cohen, A. J., et al. "Estimates and 25-year trends of the global burden of disease attributable to ambient air pollution: an analysis of data from the Global Burden of Diseases Study 2015." *The Lancet* 389, no. 10082 (2017): 1907–1918.

---

*This dossier is Paper 1 of 4 in the Panta Rhei Impact Pollution & Circularity Portfolio. For context on the broader portfolio and its deployment logic, see the portfolio overview document. Papers 2–4 address industrial emissions attribution, toxic chemical pathways, and waste/plastics systems respectively.*


---

*Source: Full manuscript text integrated from companion paper draft.*
