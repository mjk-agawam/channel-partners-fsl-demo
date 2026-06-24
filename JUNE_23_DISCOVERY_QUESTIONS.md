# Field Service Discovery Questions — Channel Partners Solutions
**Date:** June 24, 2026  
**SE:** Mike Knight  
**AE:** Daniel Jenks  
**Account:** Channel Partners Solutions, LLC  
**Context:** Architecture session following June 18 OpenSky reverse demo. Focus on gaps, integration points, and Salesforce positioning.

---

## Executive Summary from June 18 Reverse Demo

**Company Reality:**
- **PE-backed consolidator:** Unified 6 companies (Apollo, BDS, WhiteHawk, BTR, MAG, MaaS)
- **4,140 W-2 field reps** nationwide (31 corporate staff)
- **Hybrid services:** Break-fix, installations (5-15 person teams), merchandising, audits, training, parts fulfillment
- **Major retailers:** Target (1,900 stores/week), Best Buy, Walmart, Home Depot, CVS, 7-Eleven
- **Brand clients:** LG, Samsung, Microsoft, AMD, Meta, L'Oreal, Fossil

**Current Deal:**
- $73.5K crawl: 70 licenses (1.7% coverage)
- Full deployment potential: $4M-$5M (all 4,140 reps on FSL + potential Retail Execution hybrid)

**OpenSky Rollout:**
- July 6, 2026: Consolidating 3 legacy platforms into custom-built OpenSky
- Post-rollout: "Massive stabilization effort" (Jay's words)
- Q4 2026: Earliest realistic Salesforce evaluation window

**Top 5 "Magic Wand" Priorities:**
1. **Jay (CTO):** "Intelligent scheduling number one" + cross-LOB optimization + real-time exception reporting
2. **Kari (Dev Lead):** Mobile stability across devices/environments
3. **Mario (Dev Manager):** Reactive scheduling when "plan breaks" (sick reps, emergencies)
4. **Tambra (PM):** Better mobile dashboard (calendar-first doesn't guide daily work)
5. **James (Data Director):** Real-time delta data extraction (not 4-hour batch)

---

## Today's Focus: Architecture, Integration, Positioning

**Goals for this session:**
1. Map integration landscape (systems, data flows, APIs, latency requirements)
2. Understand July 6 rollout scope and stabilization risks
3. Clarify where Salesforce enhances vs. replaces OpenSky
4. Identify technical blockers and proof points needed
5. Align on Q4 evaluation approach

---

## 1. Integration Architecture Deep Dive

### Current State Mapping

**Business Central (ERP/Finance):**
- Data flows: Job costing (project-level), payroll hours, invoicing
- Direction: OpenSky → Business Central
- Frequency: Unknown (real-time? batch? daily?)
- Pain points: Lag between field work completion and invoicing? Real-time project profitability?
- **Questions:**
  - What's the integration method today? (API, batch file, MuleSoft, custom middleware?)
  - How often does job costing data sync? (Real-time, hourly, daily?)
  - Can you see project profitability mid-execution, or only after-the-fact?
  - What breaks most often in this integration?
  - If we replaced this with MuleSoft + Salesforce Billing, what would change?

**ADP (Payroll):**
- Data flows: Time cards, expenses, mileage, drive time
- Middleware: "Payroll processing app" (mentioned in demo)
- Pain point: Overtime calculated after-the-fact (can't prevent overages proactively)
- **Questions:**
  - What's the payroll processing app? (Custom, third-party?)
  - Why does overtime calculation happen outside OpenSky? (Multi-LOB time aggregation?)
  - What's the payroll error rate? (Disputed time entries, missing expenses, incorrect mileage?)
  - How often do reps call support about payroll issues?
  - Could Salesforce replace the payroll processing app, or just feed it better data?

**Warehouse Management System (WMS):**
- Data flows: Shipping requests (OpenSky → WMS), tracking data (WMS → OpenSky)
- Pain point: Partner warehouse data is manual (spreadsheet upload)
- **Questions:**
  - Which WMS vendor? (Kari wouldn't name it in demo — can you now?)
  - How many warehouses? (CP's 60K sq ft facility + partner warehouses?)
  - What % of shipments come from CP warehouse vs. partners?
  - Why is partner warehouse data manual? (No API access? Different WMS per partner?)
  - Do you need real-time inventory visibility, or is shipment tracking enough?
  - If we integrated via MuleSoft, could we unify CP + partner warehouse data?

**LMS (Learning Management System):**
- Data flows: Users/teams (OpenSky → LMS), course completions (LMS → OpenSky)
- Enforcement: Required courses block reps from starting work
- **Questions:**
  - Which LMS vendor?
  - How well does the two-way feed work? (Data quality, sync frequency, error handling?)
  - Do reps actually complete required courses before going on-site, or do they skip?
  - Is training content contextual (tied to specific projects/stores), or just a library?
  - Could Salesforce replace the LMS with Trailhead + myTrailhead, or just integrate better?

**Travel Platform (Agency):**
- Data flows: Travel requests (OpenSky → Agency), bookings/itineraries (Agency → OpenSky)
- Pain point: "Insane" travel spend, frequent last-minute changes
- **Questions:**
  - Which travel platform vendor?
  - How often do travel plans change after booking? (Cost of change fees?)
  - What triggers a travel request? (Manager manually creates? Auto-triggered by project schedule?)
  - Do reps see their travel itinerary in OpenSky mobile app?
  - Could better local scheduling reduce travel spend? (What % is avoidable?)
  - If we integrated travel data into Salesforce, what would that enable? (Proactive alerts, cost optimization, calendar integration?)

**Data Warehouse + BI:**
- Data flows: OpenSky → data warehouse (4-hour batch), warehouse → Tableau/PowerBI
- Pain point: James wants real-time delta/CDC, not batch extracts
- **Questions:**
  - What data warehouse platform? (Snowflake, Redshift, BigQuery, on-prem?)
  - What's the batch extract process? (API date range query, bulk export, ETL tool?)
  - Why 4-hour frequency? (Performance, complexity, business requirement?)
  - What decisions need real-time data that you can't make today? (Overtime alerts, SLA breach warnings, project profitability, schedule adherence?)
  - If we provided MuleSoft + Salesforce Platform Events (streaming CDC), what would you build first?
  - Who owns the Tableau/PowerBI dashboards? (James's team? LOB managers build their own?)

**CRM (Sales):**
- Current state: Separate from OpenSky (no integration except job costing)
- Gap: No lead → project → field execution → upsell closed loop
- **Questions:**
  - Do you have a CRM today? (Salesforce Sales Cloud? HubSpot? Zoho? Spreadsheets?)
  - Why is CRM separate from workforce management? (Different buyers? Different systems? Legacy from acquisitions?)
  - Do sales reps ever go into the field with service reps? (Joint calls, upsells, relationship building?)
  - If we unified CRM + FSL, what would that enable? (Lead to cash workflow, upsell opportunities from field, client 360 view?)

### Future State Requirements

**Real-Time Data Streaming:**
- James: "When we last spoke, this is where we were at. Please give us a delta."
- Use cases mentioned: Overtime alerts, SLA breach warnings, exception reporting, project profitability
- **Questions:**
  - Beyond the 4 use cases above, what else needs real-time data?
  - What's the acceptable latency? (Seconds? Minutes? Sub-hour?)
  - Who consumes this data? (Managers? Reps? Clients? Executives?)
  - Would you build event-driven workflows if data was real-time? (Auto-reassign work when rep checks out late, auto-escalate if SLA at risk, auto-alert manager if rep hits 38 hours mid-week?)

**Cross-LOB Workflow Automation:**
- Jay: "A merch goes to a target, sees one of the install broken or a display broken. There is not even an incentive for the person to capture that and send it."
- Gap: No automated escalation from survey finding → service ticket → parts order → scheduling
- **Questions:**
  - If we could auto-create a service ticket when a merch rep flags an issue, who approves it? (Parts team? Client service manager? Automated based on rules?)
  - How would billing work? (Separate job number? Bill client for reactive work? Absorb cost?)
  - Would the same rep go back, or a different rep? (Route to closest break-fix specialist?)
  - What data needs to flow from merch survey to service ticket? (Store, photos, issue description, product SKU, priority?)

**Client 360 View:**
- Jay: "Today we look at as a project and each project is aligned to a line of business. We don't see them as a holistic plan."
- Gap: No unified view of all work across LOBs for a single client (e.g., Target)
- **Questions:**
  - If you had a Client 360 view, who would use it? (Account managers? Executives? Sales reps? Client themselves?)
  - What would you want to see? (All projects, all visits, all reps, spend by LOB, SLA compliance, defects/issues, relationship contacts?)
  - Do clients ever ask for consolidated reporting across all work types? (Merch + break-fix + installations in one dashboard?)
  - Would you sell "total store services" if you could manage it holistically? (One rep, multiple services, one invoice?)

---

## 2. OpenSky Rollout: July 6 & Stabilization

### Scope & Risk Assessment

**Jay mentioned: "We have a big roll out on July 6th" (multiple times)**

- **Questions:**
  - What exactly is rolling out on July 6? (All 6-7 business units go live on OpenSky? Specific LOBs? Specific regions?)
  - What are the 6-7 business units? (Inherited from acquisitions? Organized by LOB? By geography?)
  - How many reps per business unit? (Want to understand blast radius if one unit has issues)
  - What's being retired? (3 legacy platforms — which companies used which systems?)
  - How long is the stabilization window? (Weeks? Months? Through end of year?)
  - What's your definition of "stable"? (Zero critical bugs? Reps trained? Managers comfortable? Payroll accurate?)

### Integration Rollout

- **Questions:**
  - Are all integrations live on July 6? (Business Central, ADP, WMS, LMS, Agency, data warehouse?)
  - Which integrations are most at risk? (New build vs. migrate from legacy?)
  - Do you have a rollback plan if integrations fail? (Go back to legacy systems? Manual workarounds?)
  - How will you know if integrations are working? (Monitoring, alerting, manual checks?)

### User Adoption & Training

- **Questions:**
  - How many reps are trained on OpenSky today? (Just pilot users? All 4,140?)
  - How long is training? (1 hour? 1 day? Self-paced online?)
  - What's the biggest user adoption risk? (Reps hate the mobile app? Managers can't build surveys? Dispatchers struggle with scheduling?)
  - Do you have change management / user adoption support? (Internal team? External consultants?)

### Bandwidth for Salesforce Evaluation

- **Jay: "There is a massive stabilization effort" + "resource constraint"**
- **Questions:**
  - When do you expect to have bandwidth for Salesforce evaluation? (Q4 2026? Q1 2027?)
  - What would need to be true about OpenSky stabilization for you to start evaluating? (Payroll accuracy 99%+? Rep NPS positive? No P1 bugs for 30 days?)
  - Do you want us to stay engaged during stabilization? (Monthly check-ins? Share best practices? Or go dark until you're ready?)
  - Would a lightweight POC in Q4 (just scheduling, no migration) be feasible? Or is Q1 2027 more realistic?

---

## 3. Intelligent Scheduling Deep Dive (Jay's #1 Priority)

### What "Intelligent" Means

**Jay: "Intelligent scheduling number one, right?"**

- **Questions:**
  - Define "intelligent" for us. What does OpenSky NOT do today that you need? (AI/ML? Predictive? Constraint-based optimization? Learning from history?)
  - When you say "AI-driven," what should the AI do? (Suggest optimal rep for a job? Auto-assign based on skills/proximity/availability? Predict job duration? Forecast travel time? Rebalance workload proactively?)
  - What constraints matter most? (Skills/certifications required? Rep availability windows? Travel time/cost? Overtime limits? Client preferences? SLA commitments?)
  - Should the system learn over time? (Rep A takes 20% longer than average for LG installs → factor that into future assignments?)

### Current State Gaps

**Kari: "The manager goes in and they're looking at the store bucket and they're loading those stores, it doesn't prompt them that they're making a mistake because they should be grouping these together."**

- **Questions:**
  - For hard scheduling (multi-rep teams), what does "optimal" look like? (Minimize total travel? Balance workload across team? Ensure all skills are covered? Minimize project duration?)
  - Can you quantify the inefficiency today? (e.g., "10% of travel spend is avoidable if we had better route optimization"?)
  - Do you track "what should have happened" vs. "what actually happened"? (Missed consolidation opportunities, inefficient routes, wrong rep assigned?)
  - If Einstein could suggest improvements in real-time, who would see it? (Manager building the schedule? Dispatcher mid-day? Rep self-scheduling?)

### Multi-Rep Team Scheduling

**Kari: "How do you schedule single projects and how do you schedule multiple teams when you need maybe five to 15 people at the store on the same day at the same time?"**

- **Questions:**
  - What makes team scheduling hardest? (Finding 15 people with the right skills all available the same 3 days? Minimizing travel cost for people flying in from multiple regions? Ensuring crew lead is available?)
  - Do teams have fixed compositions, or does it change per project? (Same 10 people always work together? Or dynamically assembled based on availability?)
  - What happens when one team member cancels last-minute? (Scramble for replacement? Shrink the team? Delay the project?)
  - Could Einstein optimize team assembly? (Suggest the best 10 people based on skills, availability, location, cost, historical performance?)

### Cross-LOB Optimization

**Jay: "Multiple line of business and each line of business has their own preferred way of scheduling that limits our ability to optimize a resource across the line of business."**

- **Questions:**
  - What does "preferred way of scheduling" mean per LOB? (Merch does self-scheduling, construction does hard scheduling, break-fix is reactive?)
  - If you could optimize across LOBs, what would that look like? (One rep does merch + break-fix same store visit? Break-fix team borrows merch reps when they have availability?)
  - What prevents this today beyond the system? (Union rules? Client contracts? Skills/training? Incentive structure? Billing complexity?)
  - If Salesforce enabled cross-LOB scheduling, what would need to change organizationally? (New incentive model? Cross-training program? Billing system updates?)

---

## 4. Mobile Stability & UX (Kari & Tambra's Priorities)

### Device Fragmentation

**Kari: "A mobile app that works consistently in all different environments across multiple different types of devices. We have that, but man is that hard to keep clean."**

- **Questions:**
  - What device types do your 4,140 reps use? (Company-issued? BYOD? Mix of iOS and Android? Specific device models?)
  - What breaks most often? (Offline sync fails? GPS inaccurate? Camera crashes? App freezes? OS updates break compatibility?)
  - Do you support tablets, or just phones? (Large forms on tablets for construction teams?)
  - How often do you push mobile app updates? (Weekly? Monthly? Ad-hoc when bugs found?)
  - What's your mobile testing process? (Automated tests? Manual QA on real devices? Beta user group?)
  - If Salesforce FSL mobile replaced OpenSky mobile, what would you need to prove in a POC? (Offline mode works for 8-hour shift with no connectivity? Sync doesn't fail when 500 reps sync at same time after shift?)

### Offline Requirements

- **Questions:**
  - How long are reps typically offline? (Entire shift? Just in-store? Intermittent connectivity?)
  - What data must be available offline? (Schedule, survey questions, contact info, photos from prior visits, training videos, parts inventory?)
  - How much data do reps sync daily? (MB? GB? Varies by LOB?)
  - What happens if sync fails? (Rep's work is lost? Queued for retry? Manual intervention required?)
  - Do reps ever work multi-day projects with no connectivity? (Rural areas, construction sites, overnight travel?)

### Dashboard & Guided Workflows

**Tambra: "A better rep mobile dashboard" (Context: Calendar-first view doesn't provide enough guidance)**

- **Questions:**
  - What do reps need to see first thing in the morning? (Today's schedule? Alerts/messages? Required actions before first visit? Travel itinerary?)
  - Should the dashboard be different per LOB? (Break-fix reps see open tickets, merch reps see consolidation opportunities, construction reps see team roster?)
  - What guidance do reps need? ("Visit Store A before Store B to optimize route"? "Part for this job shipped, expected delivery Tuesday"? "Required training expires in 3 days"?)
  - Would Einstein Next Best Action help? ("Based on your location and skills, we recommend picking up Job XYZ on your way home"?)
  - Do reps ever proactively look for extra work to fill gaps? (Gig-style: "I have 2 hours free this afternoon, are there any jobs nearby?")

---

## 5. Real-Time Exception Handling (Jay & Mario's Priorities)

### Reactive Scheduling When "Plan Breaks"

**Mario: "Handling those issues that happened during the day reactive breaks things that people people couldn't come today they got sick So you had a plan and then it breaks."**

- **Questions:**
  - How often does the schedule break mid-day? (Daily? Multiple times per day? Per region? Per LOB?)
  - What triggers schedule breaks? (Sick rep is #1? Job runs long? Store closed unexpectedly? Parts didn't arrive? Weather? Traffic?)
  - When a rep calls in sick at 8am, how long does it take to reassign their work? (Minutes? Hours? Some jobs just get missed?)
  - Who does the reassignment? (Dispatcher? Field ops manager? Automated? Client service manager?)
  - Do you have real-time visibility into rep location and status? (GPS tracking? Manual check-ins? Assume they're where the schedule says?)
  - If Salesforce could auto-suggest reassignments in real-time, what would that look like? ("Rep B is 10 min away, has the right skills, and has a 2-hour gap in schedule — assign to Rep B?")

### Exception Reporting & Alerts

**Jay: "Real time exception reporting minimize the gobacks."**

- **Questions:**
  - What exceptions do you need to know about in real-time? (Rep running late? Job taking longer than estimated? Defect found in survey? Part missing? Store closed? SLA at risk?)
  - Who needs to see these alerts? (Dispatchers? Field managers? Client service managers? Executives? Clients?)
  - How would you want to receive alerts? (Email? SMS? Slack? Dashboard notification? Mobile push?)
  - Would you want automated responses to some exceptions? (Rep running late → auto-notify customer with updated ETA? Defect found → auto-create service ticket?)
  - What's the cost of NOT having real-time exceptions today? (Missed SLAs? Customer complaints? Go-backs because issue wasn't flagged?)

### Overtime Prevention

- **Questions:**
  - You mentioned overtime is calculated after-the-fact. What's the business impact? (Labor cost overruns? Compliance issues? Budget surprises?)
  - If you could see a rep approaching 40 hours mid-week, what would you do? (Stop assigning new work? Reassign to another rep? Get manager approval to go over?)
  - Do reps game the system? (Slow down to hit overtime? Rush to finish before 40 hours?)
  - Would you want proactive alerts? ("Rep A is at 38 hours Tuesday morning — 3 more jobs scheduled this week will put them at 46 hours total.")
  - Could Einstein predict who's likely to hit overtime based on historical job durations? ("This rep takes 20% longer than average on LG installs, so they'll hit 42 hours if you assign them 3 more this week.")

---

## 6. Survey Flexibility & Configuration (Competitive Advantage)

### Current State Assessment

**Kari: "We create very detailed surveys. When I say detailed, I mean lots of questions, lots of functionality... tons of conditionality."**

- **Questions:**
  - How many surveys does a client service manager build per month? (One per client? One per wave? Dozens?)
  - How long does it take to build a complex survey from scratch? (Hours? Days?)
  - How often do surveys get reused vs. built fresh? (80% reuse? 50% custom?)
  - What's the most complex survey you've ever built? (How many questions? How many conditional branches?)
  - Do you ever hit limits in OpenSky's survey engine? (Too many questions? Too much conditionality? Performance issues?)

### Salesforce Compatibility Check

- **Questions:**
  - If we showed you Salesforce Lightning Web Components (custom mobile forms) + Flow Builder (conditional logic), could you replicate your most complex survey?
  - What OpenSky survey features are non-negotiable? (Product/SKU pivoting? Date-based question visibility? Photo capture with GPS tagging? Signature? Barcode scanning?)
  - Do you use any third-party survey tools? (SurveyMonkey, Typeform, etc.) Or is OpenSky's survey engine sufficient?
  - If Salesforce survey builder was 80% as flexible but 50% faster to build, would that be acceptable?

---

## 7. Go-Backs & Quality (Cost Impact)

**Jay: "Real time exception reporting minimize the gobacks."**

- **Questions:**
  - How many go-backs per week? (Across all 4,140 reps? By LOB?)
  - What causes go-backs? (Wrong parts? Incomplete work? Rep didn't have right skills? Store wasn't ready? Instructions unclear?)
  - What's the cost of a go-back? (Mileage, labor, client frustration, reputation damage?)
  - Do you track go-back root causes? (Categorize by reason? Track trends over time?)
  - If AI could predict "this job is likely to require a go-back based on incomplete survey responses," would that help? (Alert manager before rep leaves site?)
  - Could Einstein detect patterns? ("Rep C has 3x higher go-back rate on Samsung installs — recommend additional training?")

---

## 8. Organizational Transformation (Next 2-3 Months)

### LOB Silos → Geographic Model

**Jay: "There is some opportunity there and then Mike to your specific question... in the near future."**

- **Questions:**
  - What's driving the shift from LOB silos to geographic model? (Cost? Efficiency? Client demand? PE mandate?)
  - What's the timeline? (Announced? In planning? Rolling out by region?)
  - How will reporting structure change? (Field managers report to geographic RVP instead of LOB director?)
  - Will reps report to new managers? (Could cause attrition if relationships disrupted?)
  - How does this affect OpenSky? (Hierarchy model is LOB-based today — does it need to be rebuilt?)
  - If you're doing a major org change AND an OpenSky rollout simultaneously, what's the risk? (Too much change at once?)

### Incentives for Cross-LOB Work

- **Questions:**
  - Today: No incentive for merch rep to flag break-fix issue. What would the incentive be? (Bonus per referral? Paid for extra time? Recognition/gamification?)
  - Do reps get paid differently for different work types? (Higher rate for construction than merch?)
  - Would you pay one rep to do both merch + break-fix in same visit? (At which rate? Split time between two job codes?)
  - Could Salesforce gamification help? (Leaderboards, badges, points for cross-LOB work?)

---

## 9. Success Criteria & Evaluation Framework

### What "Better Than OpenSky" Looks Like

- **Questions:**
  - You just spent massive effort building OpenSky. Why would you replace it? (What would Salesforce need to do that OpenSky can't?)
  - If we positioned Salesforce as "enhancement" (augment OpenSky with Einstein scheduling, real-time data, cross-LOB workflows), would that be more palatable than "replacement"?
  - What's the one thing OpenSky does REALLY well that Salesforce absolutely must match? (Survey flexibility? Offline mobile? Multi-LOB support? Job costing integration?)
  - What's the one thing OpenSky CAN'T do that's hurting your business most? (Intelligent scheduling? Real-time data? Cross-LOB automation?)

### POC / Pilot Scope (Q4 2026)

- **Questions:**
  - If we did a proof of concept in Q4, what would you want to prove? (Einstein scheduling works? Mobile offline is rock-solid? Surveys are flexible enough? Integration to Business Central is seamless?)
  - Which LOB would be the pilot? (Break-fix because it's smallest? Merch because it's largest? Construction because it's hardest?)
  - How many reps in the pilot? (Same 70 as the crawl? Different cohort?)
  - How long would the pilot run? (30 days? 90 days? 6 months?)
  - What would make the pilot a success? (Rep NPS? Manager satisfaction? Cost savings? Fewer go-backs? Faster scheduling?)
  - What would make you cancel the pilot? (Mobile doesn't work offline? Survey builder too slow? Integration breaks payroll?)

### Commercial Framework

- **Questions:**
  - Current opportunity is $73.5K for 70 licenses. What's the walk phase? (500 licenses? 1,000 licenses? Full break-fix team?)
  - What's the run phase timeline? (2 years? 3 years? 5 years?)
  - Would you deploy FSL for service work (break-fix, construction) and Retail Execution for merchandising? Or FSL for everything?
  - Do you need Consumer Goods Cloud? (Perfect Store metrics, order capture, client portals?)
  - What's the MuleSoft opportunity? (Real-time integration you desperately need — James's ask.)
  - What's the Tableau CRM opportunity? (Replace 4-hour batch with real-time dashboards.)

---

## 10. Technical Proof Points Needed

### Must Prove Before You'll Evaluate

- **Questions:**
  - What technical proof points do you need to see before you'd formally evaluate Salesforce? (Offline mobile demo? Survey builder demo? Einstein scheduling demo? Integration architecture review?)
  - Do you want to see reference customers? (Similar scale? Similar complexity? Retail execution + field service hybrid?)
  - Do you want to talk to Salesforce customers who did a similar transformation? (Custom WFM → Salesforce migration?)
  - Would a hands-on workshop help? (Your team builds a survey in Salesforce, tests mobile offline, sees Einstein scheduling in action?)

---

## 11. Competitive Landscape

**Dan asked: "Are you evaluating other solutions?"**  
**Jay deferred in demo — can we ask now?**

- **Questions:**
  - Are you evaluating ServiceMax, FieldAware, FieldOne, or other workforce management platforms?
  - Did you evaluate any platforms before deciding to build OpenSky? (What did you rule out and why?)
  - Are you still considering "build OpenSky v2" as an alternative to Salesforce?
  - What would make you choose Salesforce over continuing to invest in OpenSky?

---

## 12. Open Discussion

**Questions for us:**
- Based on the June 18 demo, what did we NOT cover that you need to understand?
- Are there specific Salesforce capabilities you want to see demonstrated?
- What concerns do you have about Salesforce that we haven't addressed?
- What would make you feel confident that Salesforce is the right path vs. continuing with OpenSky?

**Next Steps:**
- What do you need from us between now and Q4 to stay engaged? (Monthly check-ins? Share OpenSky stabilization best practices? Case studies? Reference calls?)
- When should we reconnect for follow-up discovery? (Post-July 6 stabilization? Specific date in Q4?)
- Do you want a lightweight demo in Q4, or wait until Q1 2027 for formal evaluation?

---

## Notes from Today's Session

**Top Pain Points Confirmed:**
- 

**Integration Priorities (Ranked):**
1. 
2. 
3. 

**July 6 Rollout Risks:**
- 

**Technical Proof Points Needed:**
- 

**Organizational Changes Impacting Timeline:**
- 

**Q4 Evaluation Approach:**
- 

**Salesforce Positioning (Enhancement vs. Replacement):**
- 

**Next Steps & Owners:**
- 

---

## Post-Session To-Do

**Salesforce Team:**
- [ ] Document integration architecture (current + future state)
- [ ] Build reference customer list (similar scale/complexity)
- [ ] Schedule Einstein scheduling demo for Q4
- [ ] Identify MuleSoft specialists for real-time data architecture
- [ ] Draft POC scope options (break-fix pilot, merch pilot, hybrid)
- [ ] Prepare FSL + Retail Execution hybrid positioning deck
- [ ] Share OpenSky stabilization best practices (change management, user adoption)

**Channel Partners Follow-Up:**
- [ ] Share Kari's capability spreadsheet (cleaned up)
- [ ] Share OpenSky feature list by role
- [ ] Confirm Q4 reconnect date
- [ ] Identify pilot LOB and rep cohort
- [ ] Provide Business Central / ADP / WMS integration documentation
