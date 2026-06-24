
**Date:** June 24, 2026  
**Account:** Channel Partners Solutions, LLC  
**Context:** Architecture session following June 18 OpenSky reverse demo. Focus on gaps, integration points, and Salesforce positioning.

---

## Executive Summary from June 18 Reverse Demo

**Company Reality:**
- **PE-backed consolidator:** Unified 6 companies (Apollo, BDS, WhiteHawk, BTR, MAG, MaaS) + recent RMS acquisition (Minnesota-based, 80% single-retailer merchandising)
- **4,140 W-2 field reps** nationwide (31 corporate staff) + RMS reps (count TBD)
- **Hybrid services:** Break-fix, installations (5-15 person teams), merchandising, audits, training, parts fulfillment, experiential/activations
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

**Business Performance Assessment (Stephen's Exercise):**
- **Marketing:** 3/10 (resource optimization issues: capacity constraints, unbalanced ratios, part-timer segmentation gaps, no cross-training)
- **Sales/Contracting:** 5/10 (people-driven not systemic, manual processes, no cohesive glue)
- **Project Kickoff:** 5/10 (fragmented systems, custom client requirements without standardized provisioning, procurement delays)
- **Execution/Scheduling:** Core bottleneck (managers use "spreadsheet magic" based on personal relationships instead of trusting OpenSky, lack of system-captured capacity data, prevents cross-training optimization)
- **Cultural Challenge:** "Have it your way" culture blocks scalability (bespoke workflows per LOB, regional variations, no standardization across 6 merged companies)

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

### Integration Map Overview

**ANSWERED - Full Integration Architecture:**

```
iCIMS (recruiting/onboarding)
  ↓
GAMS (payroll aggregation + unique enterprise ID)
  ↓
ADP (payroll processing)
  ↓
AWS (middleware: step functions + microservices)
  ↓
OPEN SKY PLATFORM
  ↓
  ├→ Business Central (ERP: job costing, invoicing)
  ├→ LearnUpon LMS (certifications, training)
  ├→ WMS (3 systems: Project Center, Sphere, Launch)
  ├→ Agency (travel booking: flights/hotels)
  ├→ Snowflake (data warehouse: ETL 4x/day)
  ├→ Client APIs (Samsung, LG: file/API feeds)
  ├→ SmarterMail (part-time staff email)
  ├→ Go Happy (mass communication: email/text campaigns)
  └→ Target (schedule/check-in/check-out data)
       ↓
    Tableau (client portals + internal BI)
```

**Data Flow Details:**
- ✅ **Employee lifecycle:** iCIMS → GAMS (unique ID assignment + incentive calculations + SmarterMail trigger) → ADP → AWS → OpenSky
- ✅ **GAMS expanded role:** Third-party application for incentive/commission calculations, payroll aggregation, creates SmarterMail accounts for part-time staff
- ✅ **WMS landscape:** 3 systems (Project Center homegrown, Sphere third-party, Launch third-party) → consolidation planned with API gateway/proxy layer to protect Samsung integrations
- ✅ **Data integration architecture:** SFTP → S3 staging → Snowflake (central ETL provider) → Tableau/PowerBI
- ✅ **Snowflake sources:** OpenSky operational data + client POS data + ADP HR reports + third-party site data (geospatial, demographics, retail traffic) + Mars (third-party labor)
- ✅ **Mars system:** Manages third-party labor (contractors/partners), tracks hours, handles invoicing/billing, NOT integrated into OpenSky employee workflows
- ✅ **RMS "Portal" system:** Recent acquisition (Minnesota-based), 80% merchandising for single retailer, homegrown system NOT integrated with OpenSky (payroll migrated to ADP, full OpenSky migration delayed)
- ✅ **Freshdesk system:** Support center ticketing (phone/chat), handles internal employee support + external client-facing issues, NOT automated with OpenSky (account teams manually upload issues)
- ✅ **Break/Fix operations:** Field technicians maintain interactive displays, collaborate live with support center, parts ship directly to stores
- ✅ **Travel Management:** Travel requests initiated in OpenSky, booking done in "Agency" (Amex) portal by managers/travel agents, NOT integrated back to OpenSky
- ✅ **Experiential/Activations:** Billable work (events, brand activations), mechanics happen OUTSIDE OpenSky today, desire to bring into platform
- ✅ **Client data sharing:** File extracts (CSV), legacy API gateways, modern APIs (migration in progress)
- ✅ **Reporting:** Tableau (client portals, limited access due to licensing), PowerBI (internal ops)
- ✅ **Communication:** SmarterMail (part-time staff, avoids Microsoft E3 license costs), ARSCONNECT.COM email (corporate), Go Happy (bidirectional mass campaigns)

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
- **ANSWERED:**
  - ✅ **Employee master data flow:** iCIMS (recruiting/onboarding) → GAMS (payroll aggregation + unique enterprise ID) → ADP (payroll processing) → AWS step functions/microservices → OpenSky (profiles, teams, hierarchies)
  - ✅ **GAMS purpose:** Custom middleware that assigns enterprise-wide unique ID (solves cross-country ADP file number conflicts) and aggregates payroll data (overtime + regional calculations) before ADP export
  - ✅ **Time card flow:** OpenSky → GAMS → ADP (for payroll processing)
- **Questions:**
  - What's the payroll error rate? (Disputed time entries, missing expenses, incorrect mileage?)
  - How often do reps call support about payroll issues?
  - Could Salesforce replace GAMS, or just feed it better data?

**Warehouse Management System (WMS):**
- Data flows: Shipping requests (OpenSky → WMS), tracking data (WMS → OpenSky)
- Pain point: Partner warehouse data is manual (spreadsheet upload)
- **ANSWERED:**
  - ✅ **Current WMS landscape - 3 systems:**
    1. **Project Center WMS** (homegrown)
    2. **Sphere** (third-party platform)
    3. **Launch** (third-party system)
  - ✅ **Integration priority:** Consolidate 3 WMS into single enterprise solution
  - ✅ **Integration risk:** Breaking existing custom integrations, particularly Samsung
  - ✅ **Mitigation strategy:** API gateway/proxy layer to decouple integrations from underlying WMS (allows system swaps without forcing clients to rework their integrations)
  - ✅ **WMS integration:** "OS Integration with a WMS system for all shipping. WMS is then integrated with the shipping providers for rates and service. The integration provides inventory on all parts/products in the warehouse to OS users creating shipments"
  - ✅ **Shipping Module:** "Module to enable users to create shipping requests that go into a queue for the team/warehouse to manage. Requests go through statuses until they are approved by the warehouse and flow (through an integration) into the Warehouse Management System (WMS) for processing"
  - ✅ **Warehouse Queue:** "Warehouse request queue where warehouse can edit/move requests into the WMS for processing"
  - ✅ **One-off vs Bulk shipments:** Simple (one person, 1-many products) vs Complex (many people, multiple products, linked to project/call form + job costing)
  - ✅ **Parts Management:** "Module to add/edit parts from all CP partners. Users can add manually or upload a list with the required attributes"
  - ✅ **CP warehouse integration:** If parts shipped from CP Warehouse, WMS integrated to provide shipping info after completion
  - ✅ **Partner warehouse workaround:** Manual upload of shipping details where fulfillment partner is not CP warehouse
- **Questions:**
  - What % of shipments come from each WMS? (Project Center vs Sphere vs Launch?)
  - What % of shipments come from CP warehouse vs. partners?
  - Timeline for WMS consolidation? (In progress? Planned for 2027?)
  - Samsung integration specifics - what would break if we swapped WMS without API gateway?
  - If Salesforce FSL replaced OpenSky, could MuleSoft serve as the API gateway/proxy layer you need?
  - Do you need real-time inventory visibility, or is shipment tracking enough?

**LMS (Learning Management System):**
- Data flows: Users/teams (OpenSky → LMS), course completions (LMS → OpenSky)
- Enforcement: Required courses block reps from starting work
- **ANSWERED:**
  - ✅ **LMS vendor:** LearnUpon
  - ✅ **Two-way integration:** OpenSky sends users/teams to LMS, LMS sends course completions back
  - ✅ **Training validation:** Field reps are not able to schedule or begin work until they have completed their required work in the LMS system
  - ✅ **Resources/training content:** On-the-fly training content stored in cloud and linked within OpenSky as resources (not full LMS courses), accessible via mobile app Resources section
- **Questions:**
  - How well does the two-way feed work? (Data quality, sync frequency, error handling?)
  - Do reps actually complete required courses before going on-site, or do they skip?
  - Is training content contextual (tied to specific projects/stores), or just a library?
  - Could Salesforce replace the LMS with Trailhead + myTrailhead, or just integrate better?

**Travel Platform (Agency):**
- Data flows: Travel requests (OpenSky → Agency), bookings/itineraries (Agency → OpenSky)
- Pain point: "Insane" travel spend, frequent last-minute changes
- **ANSWERED:**
  - ✅ **Travel Management workflow:** "Travel request process for travel team who books travel. Travel request form which is approved by manager. Travel team has queue for approved travel requests and can book travel and put in details back to manager"
  - ✅ **Travel Estimator:** "Break Fix module allowing Field Managers to create an itinerary for travel for a rep and an approval process."
  - ✅ **Travel Hours tracked:** "Call forms specifically for travel - Airline, Rental Car, Hotel"
  - ✅ **Rep availability:** "Ability for a rep to designate what time they have available per day to work. This is used by the team to schedule reps according to their set availability when projects are schedule for them. This is especially useful for 2 or 3 person projects where a team needs to go in to do work together."
- **Questions:**
  - Which travel platform vendor?
  - How often do travel plans change after booking? (Cost of change fees?)
  - What triggers a travel request? (Manager manually creates? Auto-triggered by project schedule?)
  - Do reps see their travel itinerary in OpenSky mobile app?
  - Could better local scheduling reduce travel spend? (What % is avoidable?)
  - If we integrated travel data into Salesforce, what would that enable? (Proactive alerts, cost optimization, calendar integration?)
  - Travel Estimator vs Travel Management - are these the same workflow or two different processes?

**Data Warehouse + BI:**
- Data flows: OpenSky → data warehouse (4x/day ETL), warehouse → Tableau/PowerBI
- Pain point: James wants real-time delta/CDC, not batch extracts
- **ANSWERED:**
  - ✅ **Platform:** Snowflake
  - ✅ **ETL frequency:** 4 times per day (6-hour intervals on average, not 4-hour)
  - ✅ **Snowflake data sources beyond OpenSky:**
    1. Client POS data (via client API integrations - Samsung, LG, etc.)
    2. ADP HR reports (payroll/personnel data)
    3. Third-party site data: geospatial, demographics, retail traffic (e.g., Best Buy foot traffic)
  - ✅ **Tableau usage:** Client portals (company-controlled data models), limited user access (licensing costs), clients can pay for raw data access for self-service analytics
  - ✅ **PowerBI usage:** Internal operations dashboards, same Snowflake source (4x/day)
  - ✅ **Data ownership:** Company prefers internal retention ("authoritative intelligence"), but major clients (Samsung, LG) require direct access
- **Questions:**
  - What's the batch extract process? (API date range query, bulk export, ETL tool?)
  - What decisions need real-time data that you can't make today? (Overtime alerts, SLA breach warnings, project profitability, schedule adherence?)
  - If we provided MuleSoft + Salesforce Platform Events (streaming CDC), what would you build first?
  - Who owns the Tableau/PowerBI dashboards? (James's team? LOB managers build their own?)

**CRM (Sales):**
- Current state: Separate from OpenSky (no integration except job costing)
- Gap: No lead → project → field execution → upsell closed loop
- **ANSWERED:**
  - ✅ **Contact Management (SRM):** "Questions that can be asked per contact during a visit. Current answers for each contact is brought back on each visit."
  - ✅ **Contact associations:** "Ability to enter contacts by location visited, including detailed contact card. After creating a contact can that contact be connected through meta data to a store location, a reps position in the system, the retail chains position hierarchy"
  - ✅ **Bulk contact upload:** "Ability to upload a list of contacts and associate to stores or positions"
  - ✅ **Field rep contact access:** "Field rep access on a mobile device to contacts they have created. This includes all meta data and the answering of contact questions during store visits"
- **Questions:**
  - Do you have a CRM today? (Salesforce Sales Cloud? HubSpot? Zoho? Spreadsheets?)
  - Why is CRM separate from workforce management? (Different buyers? Different systems? Legacy from acquisitions?)
  - Do sales reps ever go into the field with service reps? (Joint calls, upsells, relationship building?)
  - If we unified CRM + FSL, what would that enable? (Lead to cash workflow, upsell opportunities from field, client 360 view?)
  - The SRM Contact Management - is this for store contacts (retail staff) or for client contacts (LG, Samsung decision makers)?

### Future State Requirements

**Real-Time Data Streaming:**
- James: "When we last spoke, this is where we were at. Please give us a delta."
- Use cases mentioned: Overtime alerts, SLA breach warnings, exception reporting, project profitability
- **ANSWERED:**
  - ✅ **Current reporting capabilities:**
    - **Question Alerts:** "User created alerts linked to call form questions messaging a person or group to something that needs to be followed up"
    - **GeoTracking Dashboard:** "Reporting or dashboarding providing feedback about the location of reps and whether check in/out was done correctly on call forms"
    - **Payroll Reporting:** "Reporting used to find issues and export data regarding payroll (hours, mileage, drive time, etc.)"
    - **Image Gallery:** "Ability to filter/view/export/provide access to images collected on call forms"
    - **Target PML Email:** "Custom email send to Target internal store staff after each execution visit to one of their stores"
  - ✅ **Reporting platforms:** Tableau (client portals, custom reports sourced from Snowflake), SSRS (offline reports in OS for self-service)
- **Questions:**
  - Beyond the 4 use cases above, what else needs real-time data?
  - What's the acceptable latency? (Seconds? Minutes? Sub-hour?)
  - Who consumes this data? (Managers? Reps? Clients? Executives?)
  - Would you build event-driven workflows if data was real-time? (Auto-reassign work when rep checks out late, auto-escalate if SLA at risk, auto-alert manager if rep hits 38 hours mid-week?)
  - Question Alerts - are these working today, or a planned feature? Are they real-time or batch?

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

- **ANSWERED:**
  - ✅ **Routing optimization exists:** "Ability for teams to load in store visits and the system supply routing for the field reps assigned to minimize mileage and drive time"
  - ✅ **Rep can optimize their own route:** "Enable reps to turn on or run themselves an optimization for the appointments on their calendar to reduce drive time and mileage and improve efficiency"
  - ✅ **Nightly optimization:** Self-scheduled work gets optimized overnight (mentioned in reverse demo)
  - ✅ **Gap for hard scheduling:** Hard-scheduled (manager-assigned) work does NOT get optimized - manual process today
  - ✅ **High-volume scenario:** "Field reps may do greater than 25 visits in a day during busy seasons. For optimization engines this has caused issues with our partners optimization routines"
- **Questions:**
  - For hard scheduling (multi-rep teams), what does "optimal" look like? (Minimize total travel? Balance workload across team? Ensure all skills are covered? Minimize project duration?)
  - Can you quantify the inefficiency today? (e.g., "10% of travel spend is avoidable if we had better route optimization"?)
  - Do you track "what should have happened" vs. "what actually happened"? (Missed consolidation opportunities, inefficient routes, wrong rep assigned?)
  - If Einstein could suggest improvements in real-time, who would see it? (Manager building the schedule? Dispatcher mid-day? Rep self-scheduling?)
  - Which optimization partner are you using today? What are the limitations causing issues with 25+ visits/day?

### Multi-Rep Team Scheduling

**Kari: "How do you schedule single projects and how do you schedule multiple teams when you need maybe five to 15 people at the store on the same day at the same time?"**

- **ANSWERED:**
  - ✅ **Multi Rep Scheduling capability:** "Ability to upload locations that need multiple field reps to perform the work at the same time. For example we need 2 reps to work at the same date/time because a display is too heavy for one rep to perform the work. At it's simplest allows for a schedule upload with the reps associated. At it's best the system find the reps and find the ideal scheduling for those reps"
  - ✅ **Current state:** At simplest = schedule upload with reps pre-assigned. At best = system finds and schedules ideal reps (aspirational, not current state)
  - ✅ **Rep availability tracking:** "Ability for a rep to designate what time they have available per day to work. This is used by the team to schedule reps according to their set availability when projects are schedule for them. This is especially useful for 2 or 3 person projects where a team needs to go in to do work together."
- **Questions:**
  - What makes team scheduling hardest? (Finding 15 people with the right skills all available the same 3 days? Minimizing travel cost for people flying in from multiple regions? Ensuring crew lead is available?)
  - Do teams have fixed compositions, or does it change per project? (Same 10 people always work together? Or dynamically assembled based on availability?)
  - What happens when one team member cancels last-minute? (Scramble for replacement? Shrink the team? Delay the project?)
  - Could Einstein optimize team assembly? (Suggest the best 10 people based on skills, availability, location, cost, historical performance?)
  - The "at it's best the system find the reps" - is this built today or a future requirement?

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

- **ANSWERED:**
  - ✅ **Offline capability:** Ability to work offline during a visit and sync calendar/call form/messages when a connection is available
  - ✅ **Retail environment:** "Retail locations can have very spotty coverage at time deep into the large box stores" (from feature list)
  - ✅ **Partial save/pause:** Ability to pause call form entry and save questions already answered, then return where they left off
  - ✅ **Data available offline:** Schedule, survey questions, contacts, messages, resources (files/videos), materials tracking
- **Questions:**
  - How long are reps typically offline? (Entire shift? Just in-store? Intermittent connectivity?)
  - How much data do reps sync daily? (MB? GB? Varies by LOB?)
  - What happens if sync fails? (Rep's work is lost? Queued for retry? Manual intervention required?)
  - Do reps ever work multi-day projects with no connectivity? (Rural areas, construction sites, overnight travel?)

### Dashboard & Guided Workflows

**Tambra: "A better rep mobile dashboard" (Context: Calendar-first view doesn't provide enough guidance)**

- **ANSWERED:**
  - ✅ **Current rep dashboard:** "Mobile dashboard providing field reps a summary of work to be completed with links to start the work broken down by type of work. Access and links to messages from their team, their profile, stores assigned to them etc."
  - ✅ **Work list:** "List of work assigned/available for the field rep to schedule or start entering"
  - ✅ **Last visit preview:** "Access during the call form entry flow to the previous entered call form questions for a specific store and call form. Used to familiarize them on what happened during the previous visit."
  - ✅ **Prioritization:** "Ability for a rep to have work presented to them prioritized list to schedule"
  - ✅ **Materials tracking visible:** "Want to see tracking number, link to tracking, date of delivery, status, was it delivered to the rep assigned"
  - ✅ **Mobile UI redesign:** "New Work order view that is responsive and allows field reps to access the work orders from a mobile browser without needed an app. The mobile UI is designed with task completion in mind and was made to enable a rep an easy to use interaction with upwards of hundreds of tasks in a single work order which is common among construction remodel projects."
- **Questions:**
  - What do reps need to see first thing in the morning? (Today's schedule? Alerts/messages? Required actions before first visit? Travel itinerary?)
  - Should the dashboard be different per LOB? (Break-fix reps see open tickets, merch reps see consolidation opportunities, construction reps see team roster?)
  - What guidance do reps need? ("Visit Store A before Store B to optimize route"? "Part for this job shipped, expected delivery Tuesday"? "Required training expires in 3 days"?)
  - Would Einstein Next Best Action help? ("Based on your location and skills, we recommend picking up Job XYZ on your way home"?)
  - Do reps ever proactively look for extra work to fill gaps? (Gig-style: "I have 2 hours free this afternoon, are there any jobs nearby?")
  - The new responsive Mobile UI - is this replacing the native iOS/Android apps, or complementing them?

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

- **ANSWERED:**
  - ✅ **Payroll types tracked:** In Store Hours, Admin Hours, Drive Time Hours, Mileage, Course Hours, Additional Pay $, Travel Hours, Meal Break Time
  - ✅ **Payroll management:** "Regular and expense payroll approval by Managers. Approved payroll then becomes available to the HR/Payroll Department to run the 'payroll processing' action, that becomes the file uploaded to ADP."
  - ✅ **Payroll verification:** "Mechanism for managers to verify payroll hours before posting to Payroll"
  - ✅ **Rep can view/edit payroll:** "Ability for field reps on their mobile app to view and edit all of their payroll related time, mileage, drive time"
  - ✅ **End of day questionnaire:** "Questionnaire asking if the field rep was compensated for all of their pay for the day"
- **Questions:**
  - You mentioned overtime is calculated after-the-fact. What's the business impact? (Labor cost overruns? Compliance issues? Budget surprises?)
  - If you could see a rep approaching 40 hours mid-week, what would you do? (Stop assigning new work? Reassign to another rep? Get manager approval to go over?)
  - Do reps game the system? (Slow down to hit overtime? Rush to finish before 40 hours?)
  - Would you want proactive alerts? ("Rep A is at 38 hours Tuesday morning — 3 more jobs scheduled this week will put them at 46 hours total.")
  - Could Einstein predict who's likely to hit overtime based on historical job durations? ("This rep takes 20% longer than average on LG installs, so they'll hit 42 hours if you assign them 3 more this week.")
  - Does the payroll verification process catch overtime issues before they hit ADP, or only after?

---

## 6. Survey Flexibility & Configuration (Competitive Advantage)

### Current State Assessment

**Kari: "We create very detailed surveys. When I say detailed, I mean lots of questions, lots of functionality... tons of conditionality."**

- **ANSWERED:**
  - ✅ **Survey scale:** 600-1,200 questions per survey (potential), though individual visits typically involve fewer
  - ✅ **Survey structure:** Subdivided into "tasks" for mobile app stability/performance (field reps navigate specific sections like inventory or fixture installation, not a single massive form)
  - ✅ **Question library:** Reusable question bank allowing shared question instances across multiple call forms/projects
  - ✅ **Question types:**
    - Standard: multiple choice, text, photo, signature, date/time
    - Grid questions: ask same question across multiple items/SKUs simultaneously
    - Conditional questions: parent/child logic, display rules based on prior answers, store attributes, date ranges, product/SKU presence
  - ✅ **Mobile workflow:** Synced to mobile app, offline-first architecture with local XML file, data entry works without cellular connectivity
  - ✅ **Data output:** Primary = internal reporting, Secondary = client exports (Samsung, LG) via files or APIs
  - ✅ **Client service manager setup:** Creates one survey, attributes to multiple waves/stores, create once use across many visits
- **Questions:**
  - How many surveys does a client service manager build per month? (One per client? One per wave? Dozens?)
  - How long does it take to build a complex survey from scratch? (Hours? Days?)
  - How often do surveys get reused vs. built fresh? (80% reuse? 50% custom?)
  - What's the most complex survey you've ever built? (How many questions? How many conditional branches?)
  - Do you ever hit limits in OpenSky's survey engine? (Too many questions? Too much conditionality? Performance issues?)

### Salesforce Compatibility Check

- **ANSWERED:**
  - ✅ **Non-negotiable features identified:**
    - 600-1,200 question scale
    - Task subdivision (section navigation)
    - Grid questions (multi-item efficiency)
    - Conditional logic (parent/child, date-based, product-based)
    - Reusable question library
    - Offline-first (critical for retail environments with poor connectivity)
  - ✅ **Competitive risk:** Survey flexibility is HIGH RISK area for OpenSky replacement - must demonstrate equivalent or superior capability
- **Questions:**
  - If we showed you Salesforce Lightning Web Components (custom mobile forms) + Flow Builder (conditional logic), could you replicate your most complex survey?
  - What OpenSky survey features are non-negotiable beyond what we've documented? (Product/SKU pivoting? Date-based question visibility? Photo capture with GPS tagging? Signature? Barcode scanning?)
  - Do you use any third-party survey tools? (SurveyMonkey, Typeform, etc.) Or is OpenSky's survey engine sufficient?
  - If Salesforce survey builder was 80% as flexible but 50% faster to build, would that be acceptable?
  - Would AppExchange partners (FormAssembly, Survey Force) be acceptable for advanced survey needs?

---

## 7. Go-Backs & Quality (Cost Impact)

**Jay: "Real time exception reporting minimize the gobacks."**

- **ANSWERED:**
  - ✅ **Definition (John):** "Go-backs" refer to instances where a field representative must return to a store to complete work that was originally missed or could not be finished during the first visit
  - ✅ **Common causes identified:**
    - Incomplete kits (missing materials)
    - Customer density (store too crowded to complete work)
    - Store unavailability (closed unexpectedly, remodeling, etc.)
    - Wrong parts shipped
    - Rep didn't have required skills/training
  - ✅ **Call Form Quality Assurance:** "Client service tool to flag particular answers to questions as needing follow up, creates revisits for the reps to complete"
  - ✅ **Deficiency Reporting:** "Itemized issue tracking by scope of work. Issues that are reported by the reps are trackable items with their own statuses and data fields including any resolutions, follow-up, go back dates and shipment tracking info associated with that issue."
  - ✅ **Work Order Scopes:** "Scopes serve as a container for all associated photos and documents as well as issues reported. Scopes are statused and trackable"
  - ✅ **Parts/Issue Resolution tracking:** Field reps can provide updates/feedback about all Part Issues/Orders for the location, see active part orders requiring status and completion photos
- **Questions:**
  - How many go-backs per week? (Across all 4,140 reps? By LOB?)
  - What's the cost of a go-back? (Mileage, labor, client frustration, reputation damage?)
  - Do you track go-back root causes? (Categorize by reason? Track trends over time?)
  - What % of go-backs are due to incomplete kits vs customer density vs store unavailability vs wrong parts vs rep skills?
  - If AI could predict "this job is likely to require a go-back based on incomplete survey responses," would that help? (Alert manager before rep leaves site?)
  - Could Einstein detect patterns? ("Rep C has 3x higher go-back rate on Samsung installs — recommend additional training?")
  - How does the Call Form QA process work? Manual review or automated flagging based on answer patterns?

---

## 8. Organizational Transformation (Next 2-3 Months)

### LOB Silos → Geographic Model

**Jay: "There is some opportunity there and then Mike to your specific question... in the near future."**

- **ANSWERED:**
  - ✅ **Timeline:** Next 2-3 months (mentioned in June 18 reverse demo)
  - ✅ **Vision:** Shift from LOB silos to geographic model for "fluid resources" who can work across multiple clients/work types
  - ✅ **Requires changes to:** Incentives, training, systems, reporting hierarchy
- **Questions:**
  - What's driving the shift from LOB silos to geographic model? (Cost? Efficiency? Client demand? PE mandate?)
  - What's the timeline? (Announced? In planning? Rolling out by region?)
  - How will reporting structure change? (Field managers report to geographic RVP instead of LOB director?)
  - Will reps report to new managers? (Could cause attrition if relationships disrupted?)
  - How does this affect OpenSky? (Hierarchy model is LOB-based today — does it need to be rebuilt?)
  - If you're doing a major org change AND an OpenSky rollout simultaneously, what's the risk? (Too much change at once?)

### Incentives for Cross-LOB Work

- **ANSWERED:**
  - ✅ **Current gap (Jay quote):** "A merch goes to a target, sees one of the install broken or a display broken. There is not even an incentive for the person to capture that and send it because that's not the line of business."
  - ✅ **No automated workflow:** Even if issue is sent, there's no automatic trigger/escalation workflow happening on back end
  - ✅ **Billing complexity:** Different work types have different billing models (hourly for shared teams, salary for dedicated teams, per-diem for some projects, alternate pay rates for specific stores)
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

## 11. Competitive Landscape & Privacy Constraints

**Dan asked: "Are you evaluating other solutions?"**  
**Jay deferred in demo — can we ask now?**

- **ANSWERED:**
  - ✅ **Legal/privacy constraints identified:**
    - NO body cams or glasses recording in retail environments (loss prevention policies)
    - Cannot capture customer footage (legal constraints)
    - Photo capture limited to products/fixtures/compliance (not people)
  - ✅ **FSL demo implication:** No wearables or AR demo components for retail use cases
  - ✅ **Other platform features identified:**
    - **Localization:** "Ability for the system to support other languages and localization (time zone, etc)."
    - **Territory Mapping:** "Ability for Account Teams to draw territories on a map for a rep, supervisor and use that geopoint data to assign stores for projects and do reporting"
    - **Single Sign On:** "Users can login using their Active Directory single sign instead of username and password"
    - **Blackout days:** "Ability to set by chain what days reps cannot schedule for"
    - **Rain payday advancement integration:** "Integration with RAIN payday advance for reps to get paid prior to pay day"
- **Questions:**
  - Are you evaluating ServiceMax, FieldAware, FieldOne, or other workforce management platforms?
  - Did you evaluate any platforms before deciding to build OpenSky? (What did you rule out and why?)
  - Are you still considering "build OpenSky v2" as an alternative to Salesforce?
  - What would make you choose Salesforce over continuing to invest in OpenSky?

---

## 12. Mars Third-Party Labor System

**ANSWERED:**
- ✅ **Mars system purpose:** Manages third-party labor (contractors/partners) for projects where Channel Partners does not have market coverage
- ✅ **Mars functionality:** Track hours, handle invoicing/billing for partner work
- ✅ **Separation:** NOT integrated into main OpenSky employee workflows
- ✅ **Data flow:** Mars → SFTP → S3 → Snowflake → Tableau (for combined reporting)
- ✅ **Partner data gap:** Partner call form data does NOT flow automatically into OpenSky today (manual export/import from Mars)

**Questions:**
- Which vendor/platform is Mars? (Custom-built? Third-party?)
- How many third-party contractors managed in Mars? (Dozens? Hundreds? Thousands?)
- What % of field work is done by contractors vs. W-2 employees?
- Do contractors use mobile apps to complete work? Or just time tracking?
- Do contractors complete surveys/call forms like W-2 reps?
- How is quality controlled for contractor work? (Same QA process as W-2?)
- What's the invoicing process? (Partner bills CP, CP bills client?)
- Are contractors ever assigned to same projects as W-2 reps? (Mixed teams?)
- Timeline for Mars replacement or integration with OpenSky?
- If Salesforce replaced OpenSky, would you also replace Mars?
- Could MuleSoft integrate Mars → Salesforce if Mars stays?
- Would Experience Cloud guest access work for third-party partner reps?

---

## 13. Open Discussion

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
