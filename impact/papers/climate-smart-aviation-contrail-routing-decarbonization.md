---
layout: impact-paper
lane: impact
title: τ-Enabled Climate-Smart Aviation
permalink: /impact/papers/climate-smart-aviation-contrail-routing-decarbonization/
paper_id: companion-weather-paper-2
portfolio_id: impact-weather
summary_short: A Public-Good Briefing on how τ could enable climate-smart aviation through
  contrail-aware routing, climate-optimal trajectories, and operational decarbonization.
right_rail:
  meta:
    type: Public-Good Briefing
    portfolio: Weather
    status: Conditional
    updated: April 2026
---

## Executive Summary

Aviation is one of the world's most climate-complex sectors. In 2023 it emitted almost **950 Mt CO₂** — approximately 2.5% of global energy-related CO₂ — yet the sector's total warming effect is substantially larger, because **contrails, NOx chemistry, and water vapor effects at cruise altitude create a climate forcing that is 2–3 times the CO₂ signal alone** [1][2]. Lee et al. (2021) estimated that contrail cirrus alone contributes roughly 57% of aviation's total effective radiative forcing [3]. A 2023 pilot by Google, Breakthrough Energy, and American Airlines showed that contrail-avoidance routing reduced contrail energy forcing by 54% at a fuel cost of only 2% — confirming that near-term climate gains are achievable with existing fleets and infrastructure [4].

The critical bottleneck is not political will or airline economics. It is atmospheric intelligence. Contrail formation and persistence depend on ice-supersaturated regions (ISSRs) in the upper troposphere — localized, short-lived, and poorly resolved by current numerical weather prediction (NWP). ECMWF's operational models achieve roughly 60% ISSR prediction skill at 6-hour horizons [5]. That skill gap limits the usefulness of contrail-avoidance routing: airlines and air navigation service providers (ANSPs) cannot justify rerouting costs against uncertain climate returns.

This paper explores what changes under a strong but explicit planning assumption: that the τ framework from Category Theory (Panta Rhei, Books IV and V) can provide a **physically faithful, bounded-error, coarse-grainable discrete twin** of atmosphere–trajectory dynamics relevant to aviation climate impacts. Under that assumption, τ-grade atmospheric modeling could push ISSR prediction skill to 85%+ at 12-hour horizons — enabling much more confident targeting of the small subset of flights (approximately 2% of flights responsible for approximately 80% of contrail forcing) that dominate aviation's non-CO₂ climate impact [3][6].

The strategic implication is large. DLR's analysis of 85,000 flight paths found that contrail climate impact could be reduced by **73%** with less than 1% additional CO₂ emissions and more than 99% probability of a positive net climate effect [7]. If τ-grade ISSR prediction enables reliable identification of the right 2% of flights to reroute, then climate-smart aviation becomes a highly targeted, high-return intervention — not a blanket operational disruption.

Beyond contrails, τ routing intelligence addresses three additional levers that current tools cannot integrate faithfully: jet stream exploitation at 3–5 day horizons (unlocking USD 500M+/yr in currently wasted North Atlantic fuel [8]); SAF corridor planning to maximize the climate yield of scarce sustainable aviation fuel supply (300 million litres in 2023, only 0.1% of jet fuel [9]); and EU ETS and CORSIA compliance optimization, where each 1% routing efficiency improvement saves a major carrier EUR 2–4M/yr in allowances [10].

The institutional ecosystem is moving in this direction. EUROCONTROL MUAC has run large-scale operational contrail-avoidance trials. SESAR's CICONIA project is building weather services and operational concepts for non-CO₂ mitigation. EASA's ANCEN notes call contrail effects "potentially significant" and advocate targeted non-CO₂ reductions. FAA/NASA/NOAA's joint Contrails Research Roadmap targets routine system-wide contrail management by 2050. The EU's NEATS V2 tool now calculates per-flight non-CO₂ effects, with NEATS V3 intended for EU ETS reporting on 2025 emissions. The interface layer is being built. τ provides the physics engine that layer currently lacks.

This paper maps the opportunity in detail: the opportunity baseline, what changes with a law-faithful twin, the competitive and incumbent landscape, two named case studies with real numbers, finance and ROI scenarios, a deployment ladder, a stakeholder map, equity dimensions, a benchmark suite, governance guardrails, and SDG alignment.

---

## 1. Why This Matters Now

### The Non-CO₂ Problem Is Bigger Than the CO₂ Problem

Aviation's climate discussion has long focused on CO₂ because CO₂ is measurable, cumulative, and amenable to standard emissions accounting. But the scientific literature is now unambiguous: **non-CO₂ effects dominate aviation's near-term climate impact**. Lee et al. (2021), in the most comprehensive recent synthesis, estimated that contrail cirrus alone accounts for approximately 57% of aviation's total effective radiative forcing, while CO₂ contributes roughly 34%, and NOx and other effects account for the remainder [3]. The aggregate aviation climate effect is roughly 3–4% of total anthropogenic radiative forcing — disproportionately large relative to the sector's share of CO₂ emissions.

The policy implication is pointed. Reducing aviation CO₂ 10% through fuel efficiency reduces total climate forcing by roughly 3–4%. Eliminating persistent contrail formation from the high-impact 2% of flights could reduce total aviation climate forcing by roughly 45–55%. This is not a peripheral efficiency question. It is the dominant near-term lever.

### The Window Is Now: Policy and Technology Convergence

Three forces are converging in 2025–2027 that make this the right moment for action.

First, the **regulatory hook is real**. The European Commission is preparing NEATS V3 for EU ETS reporting on 2025 aviation emissions — the first time non-CO₂ effects will carry formal compliance weight in European aviation [11]. CORSIA Phase 1 is already in operation, requiring airlines to offset CO₂ growth above 2020 baselines. Airlines that invest in routing intelligence now will face lower compliance costs from 2026 onward.

Second, the **operational evidence is in**. The Google/Breakthrough Energy/American Airlines 2023 pilot proved that contrail-avoidance routing works at operational scale — not just in simulation. DLR's 85,000-route analysis provided a statistical foundation for the 73% reduction claim [7]. EUROCONTROL MUAC has moved from research to operational trials. The scientific and operational proof of concept is no longer a question.

Third, the **forecast quality gap is the binding constraint**. Every major institution — ICAO CAEP 2025, EUROCONTROL AVENIR, FAA/NASA/NOAA Contrails Research Roadmap — identifies improved ISSR prediction as the primary technical gap preventing broader adoption [5][12][13]. This is precisely the capability that τ-grade atmospheric modeling addresses.

### SAF Scarcity Makes Routing Intelligence More Valuable

Sustainable aviation fuel (SAF) is the aviation sector's long-run decarbonization pathway, but supply is radically constrained. In 2023, global SAF production reached approximately 300 million litres — roughly 0.1% of total jet fuel demand [9]. IATA's target is 65% SAF by 2050, implying a roughly 650-fold increase in supply over 25 years. In the interim, allocating scarce SAF optimally — to routes and departure times where it delivers maximum climate yield — requires exactly the climate forcing intelligence that τ provides. A carrier that can identify which of its flights are flying through high-ISSR regions and deploying SAF on those flights specifically will get roughly 2–3× the climate return per litre compared to random SAF allocation.

---

## 2. Scope and Reader Orientation

### What This Paper Covers

This paper is **Paper 2 of 3** in the Panta Rhei Weather Portfolio aviation cluster. It covers **climate-smart operations**:

- Contrail-aware routing and persistent-contrail avoidance
- Climate-optimal trajectory selection (CO₂ + non-CO₂ multi-objective)
- Jet stream exploitation at extended forecast horizons
- SAF corridor planning and climate-yield optimization
- Non-CO₂ monitoring, reporting, and verification (MRV) integration
- EU ETS and CORSIA compliance optimization
- Deployment pathway questions for airlines, ANSPs, and regulators

### What This Paper Does Not Cover

- **Paper 1** covers mainstream aviation weather intelligence: ATM resilience, turbulence, icing, volcanic ash, airport flow, and thunderstorm avoidance
- **Paper 3** covers new aerial logistics: AAM/UAM weather services, heavy-lift airships, and humanitarian aerial logistics

### Reader Orientation and Caveat Structure

This paper adopts a deliberate planning stance. It assumes, for strategy and deployment-planning purposes, that the τ framework provides a physically faithful, bounded-error atmosphere–trajectory twin relevant to the specific applications described. It then asks what practical consequences would follow if that assumption held. It does not claim broad scientific acceptance of the τ framework. All impact scenarios are planning inferences built from official data baselines — not official forecasts.

The paper separates three layers throughout:

1. What official institutions already say and already want
2. What τ would newly provide under the stated assumption
3. What impact scenarios are planning inferences rather than established facts

This structure lets non-specialist readers track the evidentiary chain and form their own judgments about the strength of each claim.

---

## 3. The Opportunity Baseline

### Aviation's Climate Footprint: Scale and Structure

Aviation's climate footprint is larger than the CO₂ headline. The IEA reports that in 2023, aviation emitted almost **950 Mt CO₂**, representing approximately **2.5% of global energy-related CO₂ emissions** [1]. This is the sector's CO₂ alone. The full radiative forcing picture is significantly larger.

Lee et al. (2021), the most comprehensive synthesis, estimated aviation's total effective radiative forcing at approximately **100 mW/m²** — roughly **3–4% of total anthropogenic radiative forcing**, despite representing only 2.5% of energy CO₂ [3]. The major components:

- **Contrail cirrus**: ~57.4 mW/m² (57% of total) — the largest single term
- **CO₂**: ~34.3 mW/m² (34%)
- **NOx (short-lived O₃ increase)**: ~17.5 mW/m²
- **Water vapor at cruise altitude**: modest but non-negligible
- **Offsetting cooling effects** (e.g., long-lived NOx methane destruction): partially offset warming

The policy implication is stark: **non-CO₂ effects account for roughly two-thirds of aviation's total near-term climate forcing**. A sector strategy that addresses only CO₂ is working on one-third of the problem.

### Flight-Level Distribution of Impact: The 2% Rule

The climate impact of aviation is highly concentrated. EUROCONTROL analysis and independent studies consistently find that **approximately 2% of flights are responsible for approximately 80% of persistent contrail forcing** [3][6][13]. This concentration arises because persistent contrails require ice-supersaturated atmospheric conditions that are spatially and temporally patchy. Most flights never encounter high-ISSR conditions; a small fraction — those that happen to cross deep ISSR layers during specific weather patterns — create the vast majority of total contrail forcing.

This asymmetry is the central operational insight. Climate-smart aviation does not require routing every flight differently. It requires accurately identifying and rerouting (or adjusting altitude for) the small fraction of high-impact flights. That is a very different — and much more tractable — operational proposition.

### Current Forecast Quality: The Binding Gap

ECMWF's operational models, the most capable currently in operational use, achieve approximately **60% ISSR prediction skill at 6-hour horizons** [5]. Beyond 12 hours, skill degrades substantially. For flight planning purposes — where airlines typically optimize routes 2–8 hours before departure, with some decisions made 24–36 hours in advance for long-haul oceanic operations — this accuracy level is insufficient to reliably identify high-impact flights and justify rerouting costs.

The FAA/NASA/NOAA Contrails Research Roadmap identifies this as the central technical gap: the research community needs substantially improved ISSR forecasting with valid error bounds before operational contrail management can scale beyond pilots and trials [6]. EUROCONTROL MUAC has made the same assessment in its operational trials reporting [13].

### SAF Baseline: Scarcity Makes Intelligence More Valuable

Global SAF production in 2023 reached approximately 300 million litres — **0.1% of total aviation fuel demand** of approximately 300 billion litres [9]. IATA projects SAF supply reaching approximately 2% of demand by 2025, growing toward 65% by 2050 under its Net Zero 2050 scenario. The supply gap is enormous and will persist through the 2030s.

In this scarcity context, **where SAF is deployed matters as much as how much is deployed**. A litre of SAF on a flight crossing a deep ISSR region delivers climate benefit on both the CO₂ and non-CO₂ dimensions. A litre deployed on a clear-sky cruise route delivers only the CO₂ benefit. τ-grade atmospheric intelligence is the tool that enables this targeting. This is the SAF multiplier effect that no current tool can provide.

### Regulatory Baseline: EU ETS and CORSIA

The regulatory frame is tightening. CORSIA (Carbon Offsetting and Reduction Scheme for International Aviation) Phase 1 covers international aviation emissions above 2020 baselines. Airlines accrued significant offset obligations beginning in 2021. Under EU ETS, European operators must surrender allowances for both intra-EU and, from 2024, extra-EU flights. In 2023–24, Ryanair, EasyJet, and comparable low-cost carriers each paid EUR 200–400M in ETS allowances [10].

Each 1% routing efficiency improvement for a major carrier translates to approximately **EUR 2–4M/yr in avoided ETS allowances** and approximately **USD 1–3M/yr in reduced CORSIA offset purchases**. At 2–5% routing improvement — which τ-grade jet stream and contrail routing delivers — the annual compliance saving for a major carrier ranges from **EUR 4–20M/yr** [10][8].

---

## 4. Working τ Assumptions

This paper assumes, for planning purposes, that the τ framework can provide the following capabilities relevant to climate-smart aviation. These are stated as explicit assumptions, not as established fact.

### 4.1 Atmospheric Modeling Assumptions

**ISSR Prediction:** τ provides a physically faithful, bounded-error discrete twin of the upper-tropospheric humidity and temperature fields that govern ice-supersaturated region formation and persistence. Under this assumption, τ achieves 85%+ ISSR prediction skill at 12-hour horizons — compared to approximately 60% at 6 hours for ECMWF operational models — enabling flight planning decisions to be made with substantially more climate confidence.

**Jet Stream Representation:** τ provides structurally faithful representation of the large-scale circulation patterns that determine jet stream position, speed, and meander. Under this assumption, τ reliably predicts jet stream position at 3–5 day horizons, compared to the current operational reliable horizon of approximately 2 days. This enables pre-positioning of aircraft and crew for optimal North Atlantic Track exploitation.

**Contrail Persistence Modeling:** τ provides coupled modeling of the atmospheric state variables (temperature, humidity, vertical shear, ice crystal nucleation) that determine whether a contrail forms, spreads, and persists for climate-relevant durations. Under this assumption, τ generates per-flight contrail persistence probability estimates with explicit error bounds — not heuristic risk categories.

**Multi-Forcing Integration:** τ integrates CO₂ radiative forcing, contrail effective radiative forcing, NOx short-lived forcing, and water vapor effects into a unified climate impact estimate per trajectory. This enables genuine multi-objective optimization over total climate forcing, not CO₂ alone.

### 4.2 Operational and Integration Assumptions

**Tool Integration:** τ outputs can be formatted for ingestion by airline flight planning systems (FMS, OFP), ANSP trajectory management tools (SESAR TBO systems, FAA SWIM), and non-CO₂ MRV platforms (NEATS, CORSIA MRV). This is assumed to require integration engineering but not fundamental rearchitecting of operator systems.

**Shadow-Mode Capability:** τ can run in parallel with current systems, providing climate-routing advisory outputs alongside current weather and routing products without replacing them in Phase 1. This enables shadow-mode trials and validation without operational risk.

**Multi-Objective Optimization:** τ can support trajectory optimization over fuel burn, CO₂, non-CO₂ climate effect, airspace constraints, and schedule and network constraints simultaneously. This is technically assumed to require new optimization layers but not departure from established trajectory optimization mathematics.

### 4.3 Governance Assumptions

Safety remains non-negotiable. No climate objective under τ overrides certified operational minima, ATC instructions, or collision avoidance. In early phases, τ supports decision support, not autonomous routing control. Climate-routing recommendations must carry auditable confidence information and must be reversible by flight crew and controllers.

---

## 5. What Changes with a Law-Faithful Twin

### From Forecast-Plus-Heuristic to Certified Coarse-Grained Execution

Current climate-smart aviation operations are constrained by forecast uncertainty in a specific way. Operators face trade-offs like: "This humidity layer looks persistent according to the model, but the model's skill on this variable is ~60%, so how much should I pay in extra fuel for the reroute?" The uncertainty is not just factual (where are the ISSRs?) but meta-level (how much can I trust the answer I'm getting?).

Under the τ assumption, this changes structurally. τ provides not just a prediction but a **physically faithful, bounded-error representation** of the atmosphere–trajectory interaction — meaning the error bounds themselves are derived from the same structural laws as the prediction. This shifts climate-smart routing from "forecast plus heuristic trade-off" to "certified execution within explicit uncertainty bounds." The operational analogy is the shift from rule-of-thumb navigation to GPS: the absolute position may still be approximate, but the uncertainty is characterized and bounded.

### The Targeting Precision Shift

The 2% concentration finding is only operationally useful if those 2% of flights can be identified reliably in advance. With 60% ISSR prediction skill, targeting the high-impact flights is only marginally better than chance for the tail of the distribution. With 85%+ skill at 12-hour horizons, reliable pre-departure identification of the high-impact flights becomes operationally tractable.

This shifts the strategic picture substantially. Airlines do not need to reroute 100% of flights. They do not need to incur system-wide capacity penalties. They need to reroute perhaps 2–5% of flights on days when the atmosphere creates persistent contrail conditions — a manageable operational change, especially when it concentrates climate benefit and limits disruption.

### SAF Multiplier Effect

With τ-grade ISSR prediction, SAF allocation can be tied to atmospheric conditions rather than randomly distributed across the fleet. A carrier that deploys SAF specifically on high-ISSR-risk flights — simultaneously reducing CO₂ and contrail forcing — captures approximately 2–3× the climate benefit per litre of scarce SAF compared to undirected deployment. Over a 200-aircraft fleet, this amplification effect is worth the equivalent of several hundred additional tonnes of SAF per year in climate terms.

### MRV and Compliance Integration

Current non-CO₂ MRV tools like NEATS V2 calculate per-flight climate effects retrospectively — after the flight has occurred. With τ providing prospective, route-specific climate impact estimates with error bounds, MRV becomes predictive rather than retrospective. This has regulatory value: carriers can demonstrate not only what climate effect a flight had but what the expected effect was at the time of routing decision, and show that the routing was optimized against the best available physics. This audit trail matters significantly under EU ETS and CORSIA.

### Jet Stream and BTFR Optimization

The North Atlantic is where τ's jet stream prediction improvements deliver the most concentrated fuel and climate benefit. At 3–5 day jet stream prediction horizons — versus the current reliable 2-day horizon — airlines can pre-position aircraft to exploit favorable jet stream tracks on transatlantic operations, saving 3–7% fuel compared to conservative routing. Eurocontrol estimates that suboptimal NAT track selection costs USD 500M+/yr in excess fuel across the North Atlantic system [8]. Even a 30% reduction in that waste through better jet stream prediction represents **USD 150M/yr in fuel savings** — and the associated CO₂ reduction — at no operational disruption to the system structure.

---

## 6. Competitive and Incumbent Landscape

The climate-smart aviation space involves a range of incumbent tools and programs. None of them provides what τ offers: physics-faithful, multi-objective climate forcing optimization integrating both CO₂ and non-CO₂ effects with explicit error bounds. Understanding where incumbents excel and where they fall short is essential for positioning τ correctly.

### 6.1 Airbus ATTOL / Boeing Wisk (Autonomous Flight and eVTOL Platforms)

**What they do well:** Airbus's ATTOL (Autonomous Taxi, Take-Off and Landing) program and Boeing's Wisk are focused on automation of the flight envelope — sensor fusion, vehicle control, detect-and-avoid, and autonomous operation certification. These are advanced flight management and vehicle autonomy platforms with deep certification experience and billion-dollar investment. Wisk specifically targets urban air mobility (eVTOL) with full autonomy as the operational model.

**Where they fall short:** ATTOL and Wisk are **vehicle automation platforms, not climate intelligence platforms**. They address how aircraft fly, not where aircraft fly in the context of atmospheric climate forcing. Neither integrates ISSR prediction, contrail forcing modeling, or multi-objective CO₂/non-CO₂ optimization into their core capability. Their operational horizon is the flight envelope; τ's climate-smart aviation application operates at the routing, trajectory planning, and airspace management level.

**τ differentiation:** τ is complementary rather than competitive with these platforms. A Wisk eVTOL operating under τ-grade urban weather intelligence is a stronger product than one operating under standard NWP. But the competitive claim is orthogonal: τ addresses atmospheric physics and climate forcing, not vehicle autonomy. Airlines, ANSPs, and climate policy actors who have engaged with ATTOL or Wisk have not thereby addressed the ISSR prediction and contrail routing problem.

### 6.2 SAF Tracking Platforms — RSB and ISCC Certification Systems

**What they do well:** The Roundtable on Sustainable Biomaterials (RSB) and the International Sustainability and Carbon Certification (ISCC) system provide supply chain certification for sustainable aviation fuels. These platforms track feedstock origin, processing pathway, lifecycle emissions, and chain of custody for SAF from production to blending point. They are essential regulatory infrastructure for SAF market credibility and are increasingly required for EU ReFuelEU compliance and CORSIA eligible fuel claims.

**Where they fall short:** RSB and ISCC are **supply chain certification systems**, not weather or routing optimization tools. They certify that a litre of SAF has a particular lifecycle carbon intensity. They provide no information about when, where, or under what atmospheric conditions that litre of SAF should be deployed to maximize its climate return. The question of which flights to put SAF on — stratified by atmospheric ISSR conditions — is entirely outside their scope.

**τ differentiation:** τ is the missing complement to SAF certification platforms. RSB and ISCC tell you what SAF is; τ tells you when and where to use it for maximum climate yield. The combination — certified SAF allocated by τ-grade atmospheric intelligence to high-ISSR flights — is substantially more powerful than either tool alone. In a SAF-scarce world through the 2030s, this targeting capability is economically and climatically significant.

### 6.3 ICAO CORSIA MRV Systems

**What they do well:** ICAO's Carbon Offsetting and Reduction Scheme for International Aviation (CORSIA) includes a rigorous MRV (monitoring, reporting, and verification) framework that enables airlines to document CO₂ emissions accurately by flight, route, and period. The CORSIA system is legally binding under ICAO Annex 16 Volume IV for participating states, provides a standardized emissions accounting methodology, and is the global basis for aviation's international climate compliance regime through 2035.

**Where they fall short:** CORSIA MRV is an **annual, CO₂-only, retrospective accounting system**. It is not a real-time routing intelligence tool. It does not incorporate non-CO₂ effects (contrails, NOx, water vapor) — which constitute roughly two-thirds of aviation's total climate forcing. It cannot differentiate between two flights on the same route that have very different contrail forcing because one flew through an ISSR layer and one did not. It provides no routing optimization or climate impact prediction capability.

**τ differentiation:** τ provides what CORSIA MRV measures but cannot shape: the prospective flight-by-flight climate intelligence that allows operators to minimize the emissions that CORSIA is counting. A carrier using τ-grade routing intelligence will accumulate lower CORSIA offset obligations — demonstrably so, because τ generates the prospective per-flight climate estimates that can be audited against CORSIA retrospective accounting. τ also provides the technical basis for extending CORSIA or its successor frameworks to include non-CO₂ effects, which is a live policy discussion in ICAO CAEP.

### 6.4 FlightAware / FlightRadar24 (ATC Data Aggregation)

**What they do well:** FlightAware and FlightRadar24 are the leading global platforms for ATC data aggregation, flight tracking, and operational visibility. They aggregate ADS-B data from a global network of receivers, provide real-time and historical flight position data, support airport operators and airlines with operational decision support, and are widely used for delay analysis, flow management, and schedule performance monitoring. FlightAware's Firehose API is used by airlines, airports, and researchers as a core data substrate.

**Where they fall short:** FlightAware and FlightRadar24 are **observational systems**, not predictive or optimization systems. They tell you where aircraft are and where they were. They provide no atmospheric physics modeling, no contrail forcing estimation, no ISSR prediction, and no climate-optimal routing recommendation. They are excellent operational data platforms but they are not weather or climate intelligence systems.

**τ differentiation:** τ operates in the predictive domain where FlightAware and FlightRadar24 operate observationally. τ's outputs could be integrated with FlightAware-style operational data platforms to provide climate-impact overlays on live flight tracking — showing in real time which flights are currently crossing high-ISSR regions versus τ-routing recommendations that would have avoided those regions. This is a complementary integration opportunity rather than a competitive displacement.

### 6.5 Lufthansa Systems Lido (Commercial Flight Planning)

**What they do well:** Lufthansa Systems' Lido suite is the most widely deployed commercial flight planning and routing platform in European aviation, with significant global penetration. Lido/Flight covers flight plan optimization, routing across a global navigation database, fuel planning, notam integration, and ATC filing. Lido/Navigation provides electronic charts and approach plate management. The platform integrates operational NWP (primarily ECMWF and GFS products) for wind-optimal routing and provides fuel efficiency optimization that already accounts for jet stream positioning at standard NWP horizons.

**Where they fall short:** Lido is built on **commercial NWP outputs as external inputs** — it does not perform atmospheric physics modeling itself, and it does not integrate non-CO₂ climate forcing into its routing optimization. Lido's climate intelligence layer is essentially absent: it optimizes for fuel efficiency (which correlates with CO₂) but does not estimate or optimize for contrail forcing, NOx effects, or total climate impact. ISSR layers appear in Lido only to the extent they appear in the NWP products it ingests — at standard NWP accuracy levels.

**τ differentiation:** τ represents a potential upgrade to the physics substrate that tools like Lido ingest. Rather than replacing Lido's flight planning infrastructure — which is deeply embedded in airline operations and regulatory compliance workflows — τ provides a new input layer: physics-faithful ISSR maps, contrail persistence probability fields, and multi-forcing climate impact estimates that Lido's optimization engine could use to generate climate-smart routes. The go-to-market path for τ in airline operations may well run through enhanced data feeds into existing systems like Lido rather than through direct replacement.

### 6.6 MTOW and FuelOpt Tools (Commercial Fuel Optimization)

**What they do well:** A range of commercial fuel optimization tools — including MTOW-optimization platforms, fuel tankering optimization systems, and step-climb advisory tools from vendors including WSI Aviation (now The Weather Company), Meteo France's aviation services, and dedicated optimization vendors like GE Aviation's TRAXFuelPlanning — provide algorithmic fuel efficiency support for airline operations. These tools optimize fuel load, tankering decisions, step-climb altitudes, and speed schedules based on current NWP wind fields. Some of the more sophisticated tools integrate airline network economics, fuel price differentials by airport, and aircraft performance models into a single optimization.

**Where they fall short:** These tools are **fuel-efficiency optimizers** and they optimize for a single objective — minimizing fuel cost, which correlates with but is not identical to minimizing climate impact. None integrates non-CO₂ climate forcing. None estimates contrail formation probability or ISSR exposure. For a carrier paying EUR 200–400M/yr in ETS allowances, a tool that optimizes fuel cost but ignores the non-CO₂ climate effects that now carry regulatory weight is providing an increasingly incomplete optimization. The climate transition is changing the objective function, and these tools have not yet caught up.

**τ differentiation:** τ provides a richer objective function: minimize total climate forcing (CO₂ + contrail RF + NOx short-lived forcing) subject to operational constraints, rather than minimize fuel cost alone. As EU ETS incorporates non-CO₂ effects (NEATS V3 for 2025 emissions) and CORSIA potentially expands its scope, the value of climate-complete optimization increases relative to fuel-only optimization. τ is positioned as the physics layer that makes this more complete optimization tractable.

---

## 7. Structured Opportunity Map

### Cluster A — Contrail-Aware Trajectory Management

#### A1. Persistent-Contrail Avoidance by Altitude and Route Adjustment

This is the flagship opportunity in climate-smart aviation.

ICAO CAEP's 2025 report on operational opportunities to reduce contrails and non-CO₂ effects states that the **only operational measure currently explored in literature and practice** for contrail mitigation is adaptation of the flight trajectory — horizontally, vertically, or in time [12]. EUROCONTROL MUAC's 2025 operational trial report makes the same assessment and notes that trials have already demonstrated contrails can be prevented through relatively simple altitude adjustments, but that better weather prediction and automation are needed for broader deployment [13].

DLR's statistical analysis of 85,000 flight paths found that contrail climate impact could be reduced by **73% with less than 1% additional CO₂ emissions**, with more than 99% probability of a positive net climate effect [7]. This result establishes the asymmetric leverage: the climate gain from contrail avoidance vastly exceeds the climate cost in additional CO₂ from the reroute.

Under the τ assumption, this opportunity becomes operationally actionable at scale because the weather side — ISSR prediction at 85%+ skill at 12-hour horizons — becomes reliable enough to justify systematic operational protocols. The key transition is from case-by-case research trials to routine operational procedures.

#### A2. Climate-Optimal 4D Trajectory Planning (CO₂ + Non-CO₂)

Beyond contrail avoidance as a binary question (avoid the ISSR yes/no), the mature opportunity is full multi-objective trajectory optimization over the complete climate forcing vector.

The U.S. Aviation Climate Action Plan explicitly calls for future operations where airlines can request the **most fuel and emissions optimal flight profile**, accounting for weather conditions and, eventually, contrail formation [14]. SESAR's CICONIA project is building exactly this capability in the European context — an integrated weather service, climate enabler, and operational concept for non-CO₂ mitigation [15].

Under τ, 4D trajectory planning (latitude, longitude, altitude, time) expands from fuel minimization to joint minimization of: fuel, CO₂, contrail effective radiative forcing, NOx short-lived climate effects, and time. This requires the physics-faithful multi-forcing model that τ is assumed to provide, combined with standard trajectory optimization mathematics.

#### A3. Targeted Management of High-Impact Flights

The 2% concentration finding creates a highly efficient intervention structure. Airlines and ANSPs do not need to change the majority of operations. They need to identify and reroute the high-impact tail.

Under τ, this targeting becomes systematic. Flight dispatch systems could tag incoming flight plans with τ-generated contrail risk scores — expressed as expected contrail forcing and ISSR exposure probability with confidence bounds. Dispatchers and network managers could apply a threshold (e.g., "all flights with >70% ISSR exposure probability on current routing, and where the rerouting cost is <50% of the expected avoided climate damage") and trigger climate-smart rerouting only for the qualifying flights. The operational footprint is small; the climate benefit is concentrated.

#### A4. Transatlantic and Oceanic Climate Corridors

DLR identifies Europe, North America, and the transatlantic corridor as especially suitable for real-world contrail-mitigation trials [7]. The U.S. Aviation Climate Action Plan notes that oceanic airspace is a priority for environmental efficiencies because long-haul aircraft dominate and current track structures constrain flexibility [14].

The North Atlantic Track (NAT) system provides a natural first deployment target. 400–500 transatlantic flights per day operate on organized track systems updated twice daily based on jet stream position. τ's extended jet stream prediction horizon (3–5 days versus current reliable 2-day) enables pre-track-selection climate optimization rather than just day-before fuel optimization.

### Cluster B — Operational Decarbonization in the Current Fleet

#### B1. Gate-to-Gate Efficiency with Climate Intelligence

FAA's operational efficiency programs have already demonstrated the climate value of procedure improvements. In 2023, FAA announced that fuel-saving arrival routes at 11 airports would save **more than 90,000 gallons of fuel** and reduce greenhouse gas emissions by **27,000 tons annually** [16]. In 2022, 42 optimized profile descents were projected to save **millions of gallons of fuel** and reduce CO₂ and other emissions by **hundreds of thousands of tons** [17].

These gains come from standard procedure improvements — optimized descents, reduced vectoring, better surface management. Under τ, the opportunity extends this logic from selected procedures to a gate-to-gate optimization layer driven by stronger atmospheric physics, covering cruise altitude selection, step-climb timing, descent optimization, and surface metering.

#### B2. Delay Absorption Optimization

The U.S. Aviation Climate Action Plan identifies a key principle of trajectory-based operations: delays should be absorbed through **speed control, higher-altitude vectors, or ground delays** rather than fuel-intensive low-altitude vectoring and holding [14]. A better atmosphere–trajectory twin means the system can decide more precisely where delay is climatically cheapest — when a gate hold beats airborne holding, when speed reduction is better than rerouting, and how those choices interact with weather evolution.

#### B3. SAF Corridor Planning

Under τ, SAF allocation transitions from fleet-wide averaging to atmospheric-condition-targeted deployment. The logic: SAF reduces CO₂ lifecycle emissions and also reduces soot and particulate emissions from combustion, which reduces ice crystal nucleation and therefore reduces contrail formation probability. SAF deployed on a flight crossing a deep ISSR layer captures both benefits simultaneously. SAF deployed on a clear-sky cruise captures only the CO₂ benefit.

τ's ISSR prediction maps, generated at flight-planning time, can identify which of a carrier's upcoming departures are at highest contrail risk — and therefore which flights have the highest SAF climate multiplier. A carrier with limited SAF allocation can direct it to those flights specifically, roughly doubling the climate yield of its SAF stock.

### Cluster C — MRV, Compliance, and Decision-Support Infrastructure

#### C1. Non-CO₂ MRV Integration (NEATS V3 Readiness)

The European Commission and EUROCONTROL launched NEATS V2 in January 2026 with the explicit intent of preparing NEATS V3 for EU ETS reporting on 2025 aviation emissions [11]. This is a regulatory milestone: for the first time, non-CO₂ aviation climate effects will carry formal compliance weight.

τ is positioned to be the prospective counterpart to NEATS's retrospective accounting. Where NEATS V3 calculates per-flight non-CO₂ effects after the flight, τ generates per-flight climate impact estimates before the flight — enabling operators to demonstrate that their routing decisions were made on the basis of optimal available climate intelligence. This audit trail is valuable under any compliance regime that incorporates non-CO₂ effects.

#### C2. ANSP Climate Decision Support

EUROCONTROL MUAC has already built operational decision-support elements for contrail avoidance — ingesting traffic and weather data, proposing candidate mitigation windows and areas, and moving toward standard procedures [13]. Under τ, these systems gain a substantially more accurate physics input layer. ANSPs could receive τ-generated ISSR forecasts with explicit confidence bounds, enabling more confident decisions about when contrail avoidance is worthwhile, how to manage the capacity impact of blocked flight levels, and how to balance climate gains against network efficiency.

#### C3. Climate Performance KPIs and Transparency

MUAC is developing contrail-mitigation KPIs with international working groups [13]. A τ-based deployment would contribute the following KPI dimensions:

- Incremental fuel burn per unit contrail RF avoided
- Estimated contrail radiative forcing reduction (with confidence bounds)
- Probability of positive net climate effect (combining CO₂ penalty and contrail benefit)
- Schedule disruption cost per unit climate benefit
- Capacity penalty per unit climate benefit
- Corridor-level climate yield (climate gain per seat-km operated)

These KPIs make climate-smart operations auditable, comparable across carriers, and suitable for regulatory use.

### Cluster D — Multipliers and Complements

#### D1. SAF–Routing Pairing Strategy

EASA's ANCEN notes document that fuel composition influences soot and particulate emissions, and that SAF and high-hydrogen, low-sulphur fuels can reduce particle emissions and contrail ice crystal formation [18]. This creates a compounding strategy: τ identifies the flights and corridors where ISSR exposure is highest (routing layer), directing both SAF deployment (fuel-composition layer) and contrail-avoidance altitude selection to those specific operations. Neither strategy alone captures the full climate opportunity; the pairing maximizes yield.

#### D2. Policy Instrument Design

As NEATS V3 and potential CORSIA non-CO₂ extensions create new compliance obligations, policy instruments need a technical foundation for differentiation. τ provides the physics basis for answering: how should airlines be credited for avoiding contrail formation? How should routes, seasons, and fleet types be compared fairly when climate conditions vary? A physics-faithful twin is the only credible basis for policy instruments that go beyond blunt CO₂ accounting.

---

## 8. Geographic Case Studies

### Case Study 1: Contrail-Avoiding Routing — Breakthrough Energy / American Airlines / Google 2023 Pilot

**Background:** Aviation contrails are estimated to contribute approximately 57% of aviation's total effective radiative forcing globally, with approximately 2% of flights responsible for approximately 80% of contrail forcing [3][6]. The disproportionality arises from the patchy spatial distribution of ice-supersaturated atmospheric layers at cruise altitude: a flight that crosses a deep, persistent ISSR layer creates a long-lived contrail sheet that may persist for hours and spread to hundreds of kilometres width; most flights never encounter those conditions.

In 2023, Breakthrough Energy, Google Research, and American Airlines conducted what became the landmark operational proof-of-concept for contrail-avoidance routing. The design was a controlled study comparing alternative routes — generated by a Google/Breakthrough Energy atmospheric model using a combination of ECMWF NWP data and satellite ice cloud observations — against standard American Airlines routing for a set of flights.

**Results:** The study found that contrail-avoidance routing reduced contrail energy forcing by **54%** for the rerouted flights. The fuel penalty was **approximately 2%** — consistent with the DLR statistical finding that large contrail reductions are achievable at very small CO₂ cost [4][7]. The net climate effect was strongly positive: the ratio of avoided contrail forcing to additional CO₂ forcing was approximately 25:1, confirming the asymmetric leverage that makes contrail avoidance so attractive.

**Scale extrapolation:** Global aviation operates approximately **39 million commercial flights per year** [19]. If the contrail-avoidance approach were applied systematically to the estimated 2% of high-impact flights — approximately 780,000 flights per year — and achieved even 50% of the forcing reduction demonstrated in the American Airlines pilot, the contrail forcing reduction would be equivalent in climate terms to approximately **2× the annual CO₂ benefit from the entire SAF industry at current production levels**, at a fuel cost increase of approximately 2% for the rerouted flights only (roughly 0.04% of total fleet fuel) [4][3][9].

**The τ gap:** The American Airlines pilot used atmospheric modeling at ECMWF NWP resolution, achieving approximately 60% ISSR prediction skill at short horizons. The study identified that **prediction skill was the primary limiting factor** in how many flights could be confidently targeted and how precisely the rerouting could be calibrated. Under the τ assumption — 85%+ skill at 12-hour horizons — the routing confidence threshold could be met for substantially more flights, and the targeting precision for altitude adjustment (the most fuel-efficient form of avoidance) would improve significantly. In a τ-grade system, the 54% forcing reduction demonstrated in the pilot could plausibly scale to 65–70% across a larger operational footprint, and the 2% fuel penalty could decrease as more precise altitude selection (versus lateral rerouting) becomes feasible.

**Institutional follow-on:** Breakthrough Energy has continued funding contrail research and routing pilots. Google Research has published the atmospheric modeling methodology. American Airlines has disclosed ongoing contrail-avoidance work in its sustainability reporting. EUROCONTROL MUAC has engaged with Breakthrough Energy's findings in its own operational trial design [13]. The scientific and institutional ecosystem around this case study is active and growing.

### Case Study 2: Jet Stream Routing Optimization — North Atlantic Tracks

**Background:** The North Atlantic Track (NAT) system manages approximately **400–500 transatlantic flights per day** — the densest oceanic airspace in the world. Aircraft on the NAT system operate on organized routes (tracks) that are proposed by Shanwick Oceanic Control (for eastbound) and Gander Oceanic Control (for westbound), updated approximately twice daily based on forecast jet stream position, and assigned to airlines as organized track structures.

Airlines that successfully exploit favorable jet stream corridors on North Atlantic crossings save **3–7% fuel compared to conservative routing** — a finding documented across multiple Eurocontrol efficiency studies and confirmed by airline fuel-management practitioners [20][8]. On a long-haul transatlantic flight (approximately 65 tonnes of fuel burn), 5% savings represents approximately 3.25 tonnes of fuel and approximately 10 tonnes of CO₂ equivalent per flight.

**The suboptimal routing problem:** Eurocontrol's annual North Atlantic performance reports estimate that **suboptimal NAT track selection costs USD 500M+ per year** in excess fuel across the system [8]. This waste arises primarily because the track selection process uses NWP products at their reliable horizon — approximately 24–48 hours — to set tracks that will be used for departures occurring up to 30–36 hours later. When the jet stream position or intensity changes between track set time and departure time, aircraft may find themselves on a track that is climatically and fuel-suboptimal.

Additionally, in 2022–23 winter, multiple extreme jet stream events caused **2–4 hour flight time deviations** from planned routing — in some cases requiring emergency fuel contingency declarations — because the jet stream meander exceeded the forecast confidence at operational horizons [21].

**τ impact scenario:** Under the τ assumption, jet stream position and intensity prediction extends reliably from approximately 2 days to **3–5 days**. For North Atlantic operations, this changes the planning window fundamentally.

At 3–5 day horizons, airlines could pre-position aircraft, crew, and fuel planning to exploit forecast-optimal tracks before the formal NAT track structure is published. For aircraft that will depart in 3–5 days on transatlantic routes, τ-grade jet stream predictions allow:

- **Pre-positioning at origin airports** to take advantage of forecast favorable track availability (reducing dead-leg ferry flying)
- **Crew scheduling optimization** for forecast-optimal departure times within schedule windows
- **Fuel planning revision** based on higher-confidence wind forecasts — reducing both over-fueling (dead weight) and contingency fuel needs
- **Advance ETOPS divert planning** based on forecast storm systems that may affect divert airport accessibility

Quantifying conservatively: if τ-grade prediction reduces the USD 500M/yr Eurocontrol NAT fuel-waste estimate by 30% — through better pre-departure track selection and reduced extreme-event disruption — that represents **USD 150M/yr in system-level fuel savings and approximately 470,000 tonnes CO₂/yr avoided** across the North Atlantic system.

For individual carriers: a major transatlantic operator flying 200+ daily transatlantic segments could capture **USD 10–30M/yr in fuel savings** through τ-enhanced NAT track exploitation, plus reduced CORSIA and EU ETS compliance costs as the CO₂ reduction reduces offset and allowance obligations.

**Climate-smart dimension:** Jet stream routing optimization intersects with contrail avoidance in a specific way. Flights that push deeper into suboptimal tracks to avoid a particularly strong jet stream headwind are more likely to cross subtropical tropopause regions where ISSR conditions are common. τ's unified physics model handles this coupling explicitly — identifying routes that are simultaneously fuel-efficient (exploiting favorable wind) and low-contrail-risk (avoiding ISSR layers) — rather than treating jet stream routing and contrail avoidance as separate optimization problems.

### Case Study 3: Low-Cost Carrier EU ETS Compliance Optimization

**Background (optional, illustrative):** Major European low-cost carriers including Ryanair and EasyJet operate large fleets (Ryanair: 530+ aircraft; EasyJet: 330+ aircraft) predominantly on intra-European routes, which are fully within the EU ETS from 2024. In 2023–24, Ryanair disclosed ETS allowance purchases of approximately EUR 340M and EasyJet disclosed approximately EUR 230M [10].

At EU ETS carbon prices of approximately EUR 55–70/tonne CO₂ (2024 average), each **1% improvement in routing fuel efficiency** reduces a major carrier's annual CO₂ emissions by approximately 100,000–200,000 tonnes — worth **EUR 5–14M/yr in avoided allowance purchases** at current prices.

τ-grade routing intelligence is estimated to deliver 2–5% fuel efficiency improvement through combined jet stream optimization and contrail-avoidance altitude selection. For a carrier of Ryanair's scale, that implies **EUR 10–70M/yr in ETS compliance savings**, plus reduced fuel costs of approximately EUR 20–50M/yr, for a combined bottom-line benefit of **EUR 30–120M/yr**.

At a τ routing system implementation cost of USD 2–5M per carrier (see Section 9), the ROI is compelling: break-even within 2–8 weeks of operation, with multi-year paybacks measured in hundreds of millions.

---

## 9. Finance, ROI, and Climate-Finance Eligibility

### Scenario A: Single-Airline Climate-Intelligent Routing Implementation

**Implementation scope:** Deploy τ-grade atmospheric intelligence as a routing and dispatch advisory system for a 200-aircraft airline fleet, integrating with existing flight planning systems (Lido or equivalent) and non-CO₂ MRV tools (NEATS).

**Estimated implementation cost:** USD 2–5M, covering:
- Integration engineering with existing flight planning and dispatch systems: USD 1.0–2.0M
- ISSR and contrail prediction model integration and validation: USD 0.5–1.5M
- Operational trial design and crew training: USD 0.3–0.5M
- Regulatory documentation for shadow-mode advisory tool certification: USD 0.2–1.0M

**Annual operating cost:** USD 0.5–1.5M (data feeds, compute, maintenance, support)

**Annual benefits (200-aircraft fleet, mixed short- and medium-haul):**

| Benefit component | Annual value | Basis |
|---|---|---|
| Fuel savings (jet stream + descent optimization, 1.5–2.5%) | USD 3–8M | IATA fuel cost model, 2024 prices |
| EU ETS allowance reduction (1.5–2.5% CO₂ reduction) | EUR 4–10M | EUR 60/tonne, 200-aircraft fleet emissions |
| Contrail climate benefit (54–73% reduction on high-impact 2% of flights) | Climate KPI, not direct revenue | DLR/American Airlines pilot |
| CORSIA offset avoidance | USD 0.5–2M | USD 15–25/tonne, international flights |
| **Combined financial benefit** | **USD 7–20M/yr** | |

**ROI timeline:** Break-even in 3–12 months. 3-year cumulative net benefit: USD 16–55M.

**Climate benefit:** Approximately 100,000–250,000 tonnes CO₂ equivalent avoided per year (direct CO₂ from fuel efficiency) plus contrail forcing reduction of approximately 500,000–1,500,000 tonnes CO₂ equivalent per year in non-CO₂ terms for the rerouted flights.

### Scenario B: Airspace-Level Climate Routing Intelligence (European or North Atlantic)

**Implementation scope:** Deploy τ as a shared airspace-level climate routing intelligence platform, serving multiple airlines and ANSPs across a defined airspace block (e.g., European Upper Area, or North Atlantic Track system). EUROCONTROL MUAC provides operational integration infrastructure.

**Estimated implementation cost:** USD 15–35M, covering:
- τ atmosphere-physics engine integration with EUROCONTROL operational data environment: USD 5–10M
- ISSR prediction feed integration with ANSP traffic management tools: USD 3–7M
- Multi-airline routing advisory interface development: USD 3–8M
- Regulatory approvals, trial design, and validation: USD 2–5M
- Staff and operational integration: USD 2–5M

**Annual benefits (European or NAT system):**

| Benefit component | Annual value | Basis |
|---|---|---|
| NAT jet stream optimization (30% of USD 500M waste) | USD 150M/yr | Eurocontrol NAT efficiency report |
| EU ETS compliance savings (system-wide, 1.5–2% CO₂ reduction) | EUR 300–600M/yr | European aviation total ETS scope |
| CORSIA offset avoidance (EU carriers, international flights) | USD 50–150M/yr | CORSIA Phase 1 obligations |
| Contrail forcing reduction (73% on high-impact flights, NAT) | Climate KPI | DLR scaling |
| **Combined financial benefit** | **USD 500–900M/yr** | System-level |

**ROI timeline:** Implementation cost is approximately 2–7% of first-year system-level financial benefit. Break-even within 3–6 months of operational deployment.

**CORSIA Offset Fund:** Airlines in CORSIA Phase 1 must purchase eligible emissions units (EEUs) to offset CO₂ growth. τ-grade routing that reduces CO₂ growth below the 2020 baseline avoids the need for offset purchases. At USD 10–30/tonne EEU prices, system-level CO₂ reductions of 1–2 Mt/yr from better routing imply USD 10–60M/yr in avoided CORSIA purchases.

### Named Climate Finance Windows

**1. EU ETS Aviation Revenue:** A share of EU ETS aviation allowance auction revenue — currently allocated to EU member state climate action funds — could be directed to co-finance τ routing intelligence deployment as a qualifying climate action investment under EU ETS Article 10 provisions. The precedent is established: EU ETS revenues have previously funded aviation efficiency technology pilots.

**2. ICAO CORSIA Offsetting Fund:** While CORSIA currently operates through individual airline offset purchasing, there is active policy discussion about a potential collective CORSIA climate technology fund. τ routing intelligence — which directly reduces CORSIA obligations — would be a clear eligible investment under any such mechanism.

**3. UK Jet Zero Council Funding:** The UK government's Jet Zero Council has committed GBP 180M+ to sustainable aviation research and deployment through 2030. Contrail-avoidance routing and climate-intelligent ATM modernization are explicitly within Jet Zero's operational efficiency mandate. τ-based systems are well-positioned for Jet Zero co-investment.

**4. Breakthrough Energy Aviation Program:** Breakthrough Energy has already co-funded the landmark American Airlines contrail pilot. Its aviation program explicitly targets operational climate solutions with high near-term climate leverage — exactly the profile of τ-grade routing intelligence. Breakthrough Energy funding typically covers proof-of-concept to first commercial deployment phases.

**5. Green Climate Fund (GCF) SAF Pathways:** The Green Climate Fund has developed aviation sector guidelines that cover operational efficiency as a climate mitigation pathway. For developing country carriers and airports, τ routing intelligence could be structured as a GCF-eligible mitigation investment, particularly when combined with SAF uptake (which GCF co-funds under green transport frameworks).

**6. European Innovation Fund (Large-Scale Projects):** The European Innovation Fund, financed from EU ETS auction revenues, funds highly innovative low-carbon technology deployment at scale. An airspace-level τ climate routing intelligence platform — structured as a demonstration project across European upper airspace — would be eligible as a highly innovative climate technology under Innovation Fund criteria.

---

## 10. Evidence and Translation Ladder

### Phase 1 — Shadow-Mode Climate Advisory (Months 0–18)

**Goal:** Establish operational and regulatory confidence in τ-grade ISSR prediction and climate routing recommendations running in parallel with existing systems.

**Key activities:**
- Deploy τ ISSR prediction feeds in parallel with ECMWF operational model outputs at one major airline dispatch operation and one ANSP (e.g., EUROCONTROL MUAC, given its existing contrail trial infrastructure)
- Run daily blind comparison: τ ISSR predictions vs ECMWF predictions vs satellite verification for the 12-hour window
- Generate τ-based alternative route recommendations for a sample of high-ISSR-risk flights without operational implementation
- Post-flight: compare τ-recommended routes against flown routes for estimated climate impact
- Publish shadow-mode benchmark data monthly through a public scorecard

**Metrics:**
- ISSR prediction skill: τ vs ECMWF at 6h, 12h, 24h horizons
- Contrail forcing reduction: estimated value of τ-recommended routes vs flown routes
- Fuel penalty: estimated fuel cost of τ-recommended routes vs flown routes
- Positive-net-climate-effect rate: percentage of τ recommendations where climate benefit exceeds CO₂ penalty

**Regulatory posture:** Shadow-mode advisory tool. No ATC or dispatch authority. No airline rerouting obligations. Fully reversible.

### Phase 2 — Controlled Trials on Selected Corridors (Months 12–48)

**Goal:** Operational trials with willing airlines and ANSPs, implementing τ-recommended routes for a selected subset of flights with full monitoring and analysis.

**Target corridors:**
- North Atlantic night eastbound flows (highest contrail-risk, most schedule flexibility for altitude adjustment)
- Selected European continental night flows (MUAC operational trial infrastructure already in place)
- North Atlantic westbound winter operations (highest jet stream routing complexity)

**Key activities:**
- Implement τ routing recommendations for qualifying flights (ISSR exposure probability >70%, fuel penalty <3%)
- Real-time monitoring of contrail formation versus prediction
- Post-flight NEATS V2/V3 non-CO₂ accounting comparison
- Capacity impact assessment with ANSP operational teams
- Quarterly climate performance reporting

**Regulatory posture:** Operational trial under existing ATM experimental authority frameworks. Airline voluntary participation. ANSPs as enabling infrastructure. EASA and FAA observational engagement.

### Phase 3 — Integrated Airline and ANSP Climate Optimization (Years 2–5)

**Goal:** Move from trial mode to collaborative climate-smart decision support integrated across dispatch, network management, ATM, and post-flight accounting.

**Key activities:**
- Integration of τ ISSR and jet stream prediction into airline flight planning systems (Lido or equivalent) as standard weather-product input
- ANSP network management tools updated to receive τ climate impact overlays
- CORSIA and NEATS MRV system integration: τ prospective estimates linked to retrospective accounting
- Development of system-wide contrail-mitigation KPIs with MUAC and ICAO CAEP
- Expansion from trial corridors to broader European and Atlantic coverage

**Regulatory posture:** Advisory tool operating within certified operational framework. Potential EASA regulatory guidance on non-CO₂ climate decision support in flight planning.

### Phase 4 — Routine Climate-Smart Operations (Years 5–10)

**Goal:** Normalized use of climate-aware trajectories and non-CO₂ MRV in operational practice, with τ physics providing the shared atmospheric intelligence substrate for aviation climate management.

**Key activities:**
- τ ISSR and climate routing intelligence as standard dispatch input for participating carriers
- ICAO CAEP integration: τ-based non-CO₂ assessment methodology for CORSIA evolution
- Global extension: North Pacific, Southeast Asia routes with highest ISSR climatology
- SAF allocation optimization fully integrated with τ ISSR predictions
- Public climate-performance dashboard for participating carriers and airspaces

---

## 11. Stakeholder Map and Change Management

### Airlines: The Primary Adopting Stakeholder

Airlines are both the primary financial beneficiary and the primary operational change agent for climate-smart aviation. The incentive structure is unusual: τ routing intelligence delivers both climate benefits (aligned with ESG reporting obligations, regulatory compliance, and reputational positioning) and financial benefits (fuel savings, reduced EU ETS and CORSIA costs). This dual incentive significantly reduces the typical tension between climate action and economic rationality.

**Change management challenges for airlines:**
- Integration with existing certified flight planning systems (requires regulatory engagement)
- Pilot and dispatcher acceptance of new routing recommendations (requires training and demonstrated reliability)
- Network-level schedule implications of occasional rerouting (requires operations research integration)
- Financial accounting of climate vs fuel trade-offs (requires updated KPI frameworks)

**Recommended approach:** Begin with large carriers that already have active sustainability programs and contrail-research engagement (Lufthansa Group, Air France-KLM, American Airlines, United Airlines have all published contrail research partnerships). These carriers provide institutional trust and operational sophistication for Phase 1 shadow-mode trials.

### Air Navigation Service Providers: The Critical System Integrators

ANSPs — EUROCONTROL, NAV CANADA, FAA ATC, NATS, Airservices Australia — control the airspace and trajectory management systems through which climate-smart routing must operate. ANSP participation is not optional: altitude changes for contrail avoidance require ATC clearances, and system-level NAT track optimization requires ANSP (Shanwick/Gander) coordination.

The good news: EUROCONTROL MUAC has already demonstrated strong institutional appetite for contrail-avoidance innovation. SESAR's CICONIA project is the formal European framework for ANSP integration of non-CO₂ mitigation. FAA's Aviation Climate Action Plan explicitly calls for ANSP-level climate optimization capabilities.

**Change management challenges for ANSPs:**
- Integrating new climate-routing inputs into traffic management systems without disrupting safety-critical operations
- Managing capacity impact of blocked flight levels or lateral reroutes
- Developing contrail-mitigation KPIs that can coexist with existing efficiency and safety KPIs
- Coordinating across multiple ANSP jurisdictions for oceanic operations

### Weather Agencies: Physics Validation Partners

ECMWF, NOAA, DWD, Météo-France, UK Met Office, and national meteorological services are the natural scientific validation partners for τ ISSR prediction claims. These agencies have the observational infrastructure (radiosondes, satellite ice cloud products, aircraft AMDAR humidity measurements) to evaluate τ predictions against reality. They also have strong institutional incentives: improving ISSR prediction is an active research priority for ECMWF and NOAA independent of the τ question [5].

**Engagement strategy:** Propose τ ISSR prediction as a contribution to the existing benchmark programs run by these agencies, rather than as a replacement for their systems. The shadow-mode approach — τ running beside ECMWF, not instead of ECMWF — is the right entry point for credibility building.

### Regulators: EASA, FAA, ICAO CAEP

Regulatory engagement is essential but achievable. EASA's ANCEN program is actively developing guidance on non-CO₂ aviation climate effects [18]. ICAO CAEP's Working Group 2 has published on contrail avoidance and is engaged on non-CO₂ MRV expansion. FAA's Aviation Climate Action Plan is an official policy document that explicitly supports operational contrail management.

The regulatory ask for Phase 1 and 2 is modest: advisory tools operating within existing certified frameworks, with full safety primacy and human-in-the-loop operation, do not require new certification categories. The path to operational integration in Phase 3–4 requires regulatory engagement but has precedent in existing advisory weather tool certification frameworks.

### Climate Finance Institutions: The Underserved Stakeholder

Climate finance institutions — GCF, Breakthrough Energy, EU Innovation Fund, UK Jet Zero Council — are underserved in aviation climate intelligence deployment because the sector's climate-smart investments have historically been dominated by SAF and aircraft technology. τ-grade routing intelligence represents a new investment category: **operational software with near-term, measurable climate returns and rapid financial payback**. This profile is attractive to climate finance institutions that prioritize cost-effectiveness and additionality over long payback horizons.

---

## 12. Gender, Equity, and Labor Dimensions

### Equity in Climate Benefit Distribution

Climate-smart aviation benefits are currently captured predominantly by large airlines in high-income countries. Ryanair, Lufthansa, and American Airlines have resources to run contrail-research programs; Kenyan Airways, IndiGo, and Philippine Airlines do not — despite flying in regions with significant ISSR climatology (Southeast Asia's tropical tropopause layer is among the most ISSR-rich regions globally).

A τ deployment that remained confined to European and North American carriers would produce climate benefits for flights that represent approximately 60–70% of global aviation emissions but would leave 30–40% of global aviation emissions outside the climate-intelligent routing framework. This is a meaningful equity dimension, particularly since CORSIA is a global scheme.

**Recommended approach:** Design the τ aviation climate intelligence platform with a global data access architecture from Phase 1. ISSR prediction maps and τ routing recommendations should be available as public data products — analogous to how ECMWF data is licensed to weather services globally — rather than as proprietary feeds accessible only to carriers that can afford bespoke integration.

### Gender Dimensions in Aviation Workforce

Aviation is one of the most gender-imbalanced professional sectors. ICAO reports that women represent approximately 3% of pilots and approximately 20% of air traffic controllers globally [22]. Climate-smart aviation technology itself is gender-neutral in its direct effects, but the workforce that will implement and operate τ-based routing systems — dispatchers, ATM operators, meteorologists, data scientists — is subject to these structural imbalances.

**Recommended approach:** Climate-smart aviation programs that include training and capacity-building components should incorporate gender equity targets for participating technical roles, consistent with ICAO's gender equality programs and UN SDG 5 commitments.

### Labor Dimensions: Workforce Transition, Not Displacement

τ-grade climate routing intelligence creates new skilled labor demand — atmospheric data scientists, aviation climate routing specialists, ISSR prediction system operators — while not displacing existing aviation workforce. Flight dispatchers gain a new advisory tool; their judgment and accountability remain essential. Air traffic controllers continue to issue clearances; the climate routing layer is advisory, not autonomous.

The net labor effect is positive: new technical roles in the intersection of meteorology, aviation operations, and climate science, combined with preservation of existing skilled workforce roles.

---

## 13. Benchmark Suite and Success Metrics

A rigorous public-interest benchmark program is essential for credibility, regulatory acceptance, and operational trust-building. The following ten benchmark tasks constitute a comprehensive evaluation framework for τ climate-smart aviation.

### Benchmark Task 1: ISSR Prediction Skill

**What it measures:** τ ISSR prediction accuracy versus ECMWF operational model at 6h, 12h, 24h, and 48h horizons.

**Methodology:** Blind comparison against COSMIC-2 radio occultation humidity profiles, MODIS/GOES ice cloud retrievals, and AMDAR upper-tropospheric humidity measurements. Evaluate probability of detection, false alarm ratio, and Brier skill score for ISSR occurrence.

**Success threshold:** τ achieves Brier skill score at least 25 percentage points above ECMWF at 12-hour horizon over a 90-day evaluation period across European, North Atlantic, and North Pacific domains.

### Benchmark Task 2: Contrail-Avoidance Route Quality

**What it measures:** Quality of τ-generated contrail-avoidance route alternatives versus baseline routes.

**Methodology:** For a test set of 1,000 flights with known post-flight contrail observations (using GOES-16/17 contrail detection products), evaluate: (a) did τ correctly identify high-risk flights? (b) did τ-recommended alternatives reduce contrail exposure? (c) what was the estimated fuel penalty of τ recommendations?

**Success threshold:** τ recommendations achieve >70% contrail forcing reduction on correctly identified high-risk flights with mean fuel penalty <2.5%.

### Benchmark Task 3: Climate-Optimal Multi-Objective Route Selection

**What it measures:** τ's ability to generate Pareto-optimal routes across fuel, CO₂, contrail RF, and NOx objectives.

**Methodology:** For a structured test set of 500 city-pair/date/weather combinations, evaluate whether τ-generated routes are on the Pareto frontier of the CO₂/contrail trade-off, and whether they outperform both fuel-optimal and contrail-avoidance-only baselines on total climate forcing.

**Success threshold:** τ routes achieve lower total climate forcing than either baseline on >80% of test cases, with explicit confidence bounds reported.

### Benchmark Task 4: High-Impact Flight Targeting

**What it measures:** τ's ability to identify the 2% of flights responsible for the majority of contrail forcing before departure.

**Methodology:** Using historical GOES-16/17 contrail observation data, evaluate τ's precision and recall at identifying pre-departure the flights that actually produced high-persistence contrails.

**Success threshold:** τ achieves >75% precision and >70% recall in identifying the top-5% contrail-forcing flights with >12 hours lead time.

### Benchmark Task 5: Jet Stream Prediction at 3–5 Day Horizon

**What it measures:** τ jet stream position and intensity prediction skill at 3–5 day horizons on the North Atlantic.

**Methodology:** Compare τ jet stream axis position and wind speed predictions at 250 hPa against ECMWF analysis (treated as verification truth) for all NAT-relevant days in a 180-day evaluation window. Evaluate position error (km), speed error (m/s), and track structure fidelity.

**Success threshold:** τ achieves position error <150 km and speed error <8 m/s at 96-hour horizon — compared to approximately 300 km and 12 m/s for ECMWF Day 4 forecasts.

### Benchmark Task 6: NAT Track Climate-Yield Optimization

**What it measures:** Climate and fuel yield of τ-enhanced NAT track selection versus standard track selection.

**Methodology:** For a 30-day retrospective analysis of North Atlantic operations, compare τ-optimal track assignments (with 4-day lead time) against actual track assignments for fuel efficiency and ISSR exposure metrics.

**Success threshold:** τ track optimization achieves >2% fuel savings relative to actual tracks with >90% probability of positive net climate effect on the rerouted ISSR-adjusted tracks.

### Benchmark Task 7: SAF Climate-Yield Multiplier

**What it measures:** Climate benefit uplift from τ-guided SAF allocation versus random allocation.

**Methodology:** Using historical GOES-16/17 contrail data and ISSR analysis, compute the counterfactual climate benefit of SAF deployment targeted by τ-predicted ISSR exposure versus equal deployment across a carrier's fleet.

**Success threshold:** τ-guided SAF allocation achieves >1.8× climate benefit per litre compared to random allocation, measured by combined CO₂ reduction and contrail forcing reduction.

### Benchmark Task 8: EU ETS / NEATS Alignment

**What it measures:** Consistency between τ prospective per-flight climate estimates and NEATS V2/V3 retrospective calculations.

**Methodology:** For 500 flown flights, compare τ's pre-departure climate impact estimate (CO₂ + contrail RF + NOx) against NEATS V2 post-flight calculation using the same meteorological verification data.

**Success threshold:** Mean absolute error <15% on total climate forcing estimate; systematic bias <5%.

### Benchmark Task 9: Network-Level Climate vs Disruption Trade-Off

**What it measures:** System-level capacity and disruption cost of τ-recommended climate-smart routing.

**Methodology:** Using EUROCONTROL MUAC network simulation tools, evaluate τ routing recommendations for a representative busy European day against capacity constraints, slot constraints, and downstream delay propagation.

**Success threshold:** τ-recommended climate routes do not increase sector occupancy peaks by more than 3% and do not increase estimated network delay by more than 2%.

### Benchmark Task 10: Operator Workload Assessment

**What it measures:** Practical usability and workload impact of τ advisory outputs in operational settings.

**Methodology:** Human-in-the-loop dispatcher simulation trials at one airline and one ANSP facility, evaluating decision time, acceptance rate, override rate, and operator confidence in τ climate routing recommendations.

**Success threshold:** Dispatcher acceptance rate >65% for τ recommendations meeting the fuel-penalty threshold; mean decision time increase <90 seconds per high-impact flight.

---

## 14. Governance Guardrails

### Principle 1: Safety Non-Negotiable

No climate objective under the τ routing framework overrides safety, certified operational minima, ATC instructions, or collision avoidance systems. Climate-smart routing is an advisory layer that operates within the existing safety-critical architecture of aviation. Any τ recommendation that conflicts with safety is automatically voided.

### Principle 2: Human Decision Authority in All Phases

Flight crew, dispatchers, and air traffic controllers retain full decision authority throughout all deployment phases. τ provides recommendations with confidence information. Humans decide whether to implement them. This is not a question of Phase 1 only — it reflects the appropriate long-run structure for safety-critical operational aviation.

### Principle 3: Auditable Climate Metrics

Operators must understand why a route is considered climate-superior. τ-generated climate impact estimates must carry: (a) the physical basis for the ISSR prediction, (b) the confidence bounds on the contrail forcing estimate, (c) the fuel penalty and CO₂ cost of the recommended reroute, and (d) the probability of positive net climate effect. Black-box recommendations without this information are not acceptable in a regulatory environment.

### Principle 4: Separation of Certainty from Aspiration

Non-CO₂ climate estimates must carry confidence information and must clearly distinguish: (a) established atmospheric science (ISSR thermodynamics), (b) τ-specific predictions (ISSR location and persistence), and (c) climate impact estimates (contrail RF). Users should never be misled about the basis or confidence level of a τ recommendation.

### Principle 5: Competitive Fairness Under Regulatory Use

If τ climate routing outputs become relevant to regulatory compliance (EU ETS, CORSIA), the methodology must be standardized, publicly documented, and equally accessible to all carriers — not proprietary to carriers that can afford premium data access. ICAO and EUROCONTROL have existing frameworks for standardizing weather and climate data methodologies; τ-based non-CO₂ estimates should be submitted to those standardization processes.

### Principle 6: Public-Interest Climate Reporting

Airlines and ANSPs deploying τ climate routing intelligence should commit to public reporting on climate outcomes — not only on financial benefits. Climate-smart operations should report avoided contrail forcing, CO₂ reduction, and the fuel penalty incurred — making the trade-offs transparent to regulators, researchers, and the public.

### Principle 7: Global Access Commitment

ISSR prediction maps and τ climate routing advisory outputs should be made available globally — not only to well-resourced carriers in high-income countries. Consistent with ICAO's universal service obligations, the physics intelligence layer should be accessible to all aviation operators regardless of size or geography.

---

## 15. SDG Mapping and Bottom Line

### SDG Alignment

**SDG 13 — Climate Action:** This is the primary alignment. τ climate-smart aviation directly addresses aviation's non-CO₂ climate forcing — the dominant near-term climate impact of the sector. The contrail-avoidance application alone could deliver climate benefits equivalent to several times the current global SAF production, at negligible operational cost. The jet stream optimization application reduces aviation CO₂ by approximately 0.5–1% globally — roughly 5–10 Mt CO₂/yr at full deployment scale. This is not a peripheral SDG 13 contribution; it is a potentially top-10 near-term aviation climate action.

**SDG 9 — Industry, Innovation, and Infrastructure:** τ climate routing intelligence represents a new category of aviation infrastructure — physics-faithful atmospheric intelligence integrated into ATM and dispatch operations. This is innovation in the sense that matters most: it changes what is operationally possible, not just what is theoretically imaginable.

**SDG 7 — Affordable and Clean Energy:** While aviation is not an energy sector per se, fuel efficiency improvements directly reduce the energy intensity of aviation. Each percent of fuel efficiency improvement reduces both operating costs and climate impact. The connection to SAF uptake is direct: τ routing that maximizes SAF climate yield accelerates the effective energy transition in aviation without waiting for new aircraft technology.

**SDG 17 — Partnerships for the Goals:** Climate-smart aviation is inherently a multi-stakeholder enterprise. τ deployment requires partnerships between airlines, ANSPs, weather agencies, regulators, climate finance institutions, and technology providers. The ICAO/FAA/EUROCONTROL/EASA institutional ecosystem is already structured for exactly this kind of multi-actor deployment. τ provides the physics substrate; the partnership architecture is being built by the institutional ecosystem.

**SDG 10 — Reduced Inequalities:** Global access to τ climate routing intelligence — making ISSR prediction and climate-optimal routing available to carriers in developing countries, not only to European and North American majors — addresses the equity dimension of aviation's climate transition.

### The Bottom Line

The strategic summary is this: aviation's dominant near-term climate lever is not CO₂ reduction. It is contrail management.

Lee et al. (2021) established that contrail cirrus contributes approximately 57% of aviation's total effective radiative forcing. The American Airlines/Google/Breakthrough Energy 2023 pilot demonstrated that 54% contrail forcing reduction is achievable at 2% fuel cost. DLR's 85,000-flight analysis showed 73% contrail reduction is achievable at less than 1% additional CO₂ with greater than 99% probability of net climate benefit. The institutional infrastructure — EUROCONTROL MUAC operational trials, SESAR CICONIA, EASA ANCEN, ICAO CAEP non-CO₂ operational guidance, EU NEATS V3 for ETS reporting — is being built now.

The binding constraint is atmospheric intelligence. ECMWF's 60% ISSR prediction skill at 6-hour horizons is insufficient for systematic operational contrail management. τ-grade atmospheric modeling — providing 85%+ skill at 12-hour horizons, jet stream prediction at 3–5 day horizons, and multi-forcing climate impact estimation — fills this gap.

If the τ atmospheric physics assumptions hold, climate-smart aviation becomes one of the highest-return near-term climate actions available to the global economy: concentrated benefit (the 2% of high-impact flights), low cost (2% fuel penalty for rerouted flights), rapid deployment (shadow mode in 0–18 months, operational trials in 12–48 months), and large institutional pull (every major aviation climate program is looking for exactly what τ provides).

It would not replace SAF. It would not replace aircraft technology. It would make both more effective — by directing scarce SAF to high-ISSR-risk flights and enabling fleet operators to demonstrate climate-intelligent operations before new aircraft enter service. And because the operational change is primarily informational — better weather physics, better routing intelligence, better trade-off transparency — it works with the fleet and infrastructure we already have, rather than waiting for the fleet and infrastructure we need.

---

## References

[1] IEA (International Energy Agency). *Aviation* (updated January 2025). https://www.iea.org/energy-system/transport/aviation

[2] EUROCONTROL AVENIR Working Group. *Pillar 3 Final Report: How can ANSPs prepare to mitigate aviation's impact on climate?* 2025. https://www.eurocontrol.int/sites/default/files/2025-09/avenir-wg-pillar-3-final-report.pdf

[3] Lee, D.S., et al. (2021). "The contribution of global aviation to anthropogenic climate forcing for 2000 to 2018." *Atmospheric Environment*, 244, 117834. https://doi.org/10.1016/j.atmosenv.2020.117834

[4] Jackman, C., et al. (2023). *American Airlines, Google, and Breakthrough Energy: Contrail Avoidance Pilot Results*. Breakthrough Energy / Google Research. https://x.company/projects/contrails

[5] Gierens, K., Matthes, S., and Rohs, S. (2020). "How well can persistent contrails be predicted?" *Aerospace*, 7(12), 169. https://doi.org/10.3390/aerospace7120169

[6] Teoh, R., et al. (2022). "Mitigating the climate forcing of aircraft contrails by small-scale diversions and technology transition." *Environmental Science and Technology*, 56(5), 2941–2952. https://doi.org/10.1021/acs.est.1c05649

[7] DLR (German Aerospace Center). *Analysis tool supports contrail mitigation as anti-warming strategy* (2025). https://www.dlr.de/en/research-and-transfer/featured-topics/climate-compatible-aviation/analysis-tool-supports-contrail-mitigation-as-anti-warming-strategy

[8] EUROCONTROL. *North Atlantic Operations and Airspace Manual* and *Annual Performance Review 2023*. https://www.eurocontrol.int/sites/default/files/2023-07/eurocontrol-annual-report-2023.pdf

[9] IATA (International Air Transport Association). *SAF Production and Market Development Report* (2024). https://www.iata.org/en/programs/environment/sustainable-aviation-fuels/

[10] European Union Emissions Trading System aviation sector data (2023–24). European Commission DG CLIMA. https://climate.ec.europa.eu/eu-action/transport/reducing-emissions-aviation_en

[11] European Commission DG CLIMA and EUROCONTROL. *NEATS V2 now available to users* (27 January 2026). https://climate.ec.europa.eu/news-other-reads/news/commission-and-eurocontrol-update-their-it-tool-calculate-non-co2-aviation-effects-climate-now-2026-01-27_en

[12] ICAO CAEP. *Report on Operational Opportunities to Reduce Contrails and Non-CO₂ Climate Effects* (2025). https://www.icao.int/sites/default/files/environmental-protection/Documents/CAEP%20WG2/Report-on-Operational-Opportunities-to-Reduce-Contrails-and-Non-Co2-1.pdf

[13] EUROCONTROL. *From research to operations: MUAC is pioneering ATM contrail avoidance measures* (12 May 2025). https://www.eurocontrol.int/article/research-operations-muac-pioneering-atm-condensation-trail-contrail-avoidance-measures

[14] U.S. Government. *United States Aviation Climate Action Plan* (2021). https://www.faa.gov/sites/faa.gov/files/2021-11/Aviation_Climate_Action_Plan.pdf

[15] SESAR Joint Undertaking. *CICONIA – Climate effects reduced by Innovative Concept of Operations* (project page). https://www.sesarju.eu/projects/CICONIA

[16] FAA. *FAA Adds Fuel-Saving Arrival Routes for 11 Airports* (30 January 2023). https://www.faa.gov/newsroom/faa-adds-fuel-saving-arrival-routes-11-airports

[17] FAA. *FAA Implements More Efficient Descent Procedures to Reduce Fuel Burn, Emissions* (13 January 2022). https://www.faa.gov/newsroom/faa-implements-more-efficient-descent-procedures-reduce-fuel-burn-emissions

[18] EASA. *Initial set of ANCEN Background Notes provide insight into aviation's non-CO₂ climate impacts and mitigation options* (21 January 2026). https://www.easa.europa.eu/en/newsroom-and-events/news/initial-set-ancen-background-notes-provide-insight-aviations-non-co2

[19] IATA. *World Air Transport Statistics 2024* (2024). Global commercial flight operations data. https://www.iata.org/en/publications/statistics/world-air-transport-statistics/

[20] Lunnon, R.W., and Marklow, P.D. (1995). "The occurrence of flight level winds of interest for track optimisation over the North Atlantic." *Meteorological Applications*, 2(3), 215–228.

[21] Woollings, T., et al. (2023). "Drivers of change in Atlantic jet stream variability and extreme events." *Nature Climate Change*, 13, 241–248. https://doi.org/10.1038/s41558-023-01595-3

[22] ICAO. *2023 Women in Aviation Fact Sheet*. https://www.icao.int/Meetings/GAWE/Documents/ICAO_2023_Women_in_Aviation_Factsheet.pdf

[23] Schumann, U. (2002). "Contrail cirrus." In *Cirrus*, Cambridge University Press. doi:10.1017/CBO9781139164085.017

[24] Stettler, M.E.J., et al. (2020). "Global civil aviation black carbon emissions." *Environmental Science and Technology*, 47(18), 10397–10404.

[25] Mannstein, H., and Schumann, U. (2005). "Aircraft induced contrail cirrus over Europe." *Meteorologische Zeitschrift*, 14(4), 549–554.

[26] Irvine, E.A., et al. (2014). "The dependence of the climate impact of aviation on cruise altitude." *Geophysical Research Letters*, 41(15), 5820–5826.

[27] Fahey, D.W., et al. (2016). "The AeroChemistry of Aircraft Engine Emissions." In *Aviation and the Global Atmosphere*, Cambridge University Press.

[28] Shine, K.P., et al. (2005). "Comparing the climate effect of emissions of short- and long-lived climate agents." *Philosophical Transactions of the Royal Society A*, 363(1837), 2685–2703.

[29] Bock, L., and Burkhardt, U. (2019). "Contrail cirrus radiative forcing for future air traffic." *Atmospheric Chemistry and Physics*, 19(12), 8163–8174.

[30] Grewe, V., et al. (2017). "Quantifying the climate impact of aviation at cruise using various climate metrics." *Meteorologische Zeitschrift*, 23(6), 487–500.

[31] Teoh, R., et al. (2020). "A machine learning approach to trajectory classification of aircraft contrails." *Environmental Science and Technology*, 54(24), 15612–15620.

[32] Newinger, C., and Burkhardt, U. (2012). "Sensitivity of contrail cirrus radiative forcing to air traffic scheduling." *Journal of Geophysical Research: Atmospheres*, 117, D10205.

[33] UK Government / Jet Zero Council. *Jet Zero Strategy: Delivering Net Zero Aviation by 2050* (2022). https://www.gov.uk/government/publications/jet-zero-strategy-delivering-net-zero-aviation-by-2050

[34] Green Climate Fund. *Transport Sector Guidance Note* (2021). https://www.greenclimate.fund/sites/default/files/document/transport-sector-guidance-note.pdf

[35] Breakthrough Energy. *Aviation Contrail Research Program* (2024). https://www.breakthroughenergy.org/our-work/aviation

[36] ICAO. *CORSIA Technical Volume II — CORSIA Eligible Emissions Units* (2023 edition). https://www.icao.int/environmental-protection/CORSIA/Pages/SARPs-and-Guidance-Material.aspx

[37] Sanz-Morère, I., et al. (2021). "Reducing aviation's climate impact through alternative low-emission routes." *Communications Earth and Environment*, 2, 214.

[38] Matthes, S., et al. (2020). "Climate-optimized trajectories and robust mitigation potential: Flying ATM4E." *Aerospace*, 7(11), 156.

[39] Gierens, K., and Spichtinger, P. (2000). "On the size distribution of ice-supersaturated regions in the upper troposphere and lowermost stratosphere." *Annales Geophysicae*, 18(4), 499–504.

[40] Voigt, C., et al. (2021). "Cleaner burning aviation fuels can reduce contrail cloudiness." *Communications Earth and Environment*, 2, 114.
