# Field Service Discovery Questions — Channel Partners Solutions
**Date:** June 24, 2026  
**SE:** Mike Knight  
**AE:** Daniel Jenks  
**Account:** Channel Partners Solutions, LLC  
**Context:** Reverse demo completed June 18. Building on OpenSky walkthrough to identify FSL fit and gaps.

---

## Context from June 18 Reverse Demo

**What we learned:**
- OpenSky is a homegrown field service system supporting merchandising, break/fix, installations, and dedicated brand teams
- Mix of hard scheduling (manager-assigned) and self-scheduling (rep drags to calendar)
- **PE-backed consolidator:** Unified 6 acquired companies (Apollo, BDS, WhiteHawk, BTR, MAG, MaaS)
- **4,140 W-2 field reps** across all business units (not 31 — that's corporate staff)
- **Current opportunity:** $73.5K crawl (70 licenses = 1.7% coverage)
- **Full deployment potential:** $4M-$5M (all 4,140 reps on FSL + potential Retail Execution hybrid)
- Rolling out OpenSky across 6-7 business units in July
- Key pain points: intelligent scheduling, mobile stability, cross-LOB optimization, real-time exception reporting
- Tech stack: OpenSky, ADP (payroll), Business Central (finance), third-party LMS, warehouse integration

**Magic wand answers from the team:**
- Jay: "Intelligent scheduling, field efficiency, real-time exception reporting to minimize go-backs"
- Ki: "Mobile app that works consistently across devices"
- Mario: "Smarter scheduling for reactive breaks and sick callouts"
- Tambra: "Better rep mobile dashboard to guide daily work"
- James: "Lower-latency data with delta/CDC instead of batch extracts"

---

## 1. Scheduling & Optimization (Top Priority)

### Current State Deep Dive
- **Walk us through how scheduling works today in OpenSky.** We saw hard scheduling vs. self-scheduling in the demo — what % of work falls into each bucket?
- **What drives the decision to hard-schedule vs. self-schedule?** (Project type, client requirement, LOB, rep type?)
- **Jay mentioned "intelligent scheduling" as your #1 wish.** What does "intelligent" mean to you? (AI-driven? Skill-based? Route-optimized? Cross-LOB?)
- **You mentioned scheduling is currently "spreadsheet-based" for complex projects.** When does the spreadsheet come in vs. using OpenSky's bucket/matching tool?
- **Multi-rep teams (5-15 people at same store, same time):** Walk us through the pain of scheduling these today. What makes it hard? (Availability, skills, geography, equipment?)
- **Self-scheduling has overnight route optimization.** Does it work well? What breaks? What would you change?
- **Hard scheduling does NOT have route optimization today.** What's the impact? (Inefficient routes, excess mileage reimbursement, rep complaints?)

### Reactive Scheduling & Exceptions
- **Mario mentioned "reactive breaks" and "someone got sick today."** How often does the schedule blow up mid-day? What triggers it? (Sick rep, job runs long, store closed, part missing?)
- **When a schedule breaks, what's the process to reassign work?** (Bulk reschedule tool, line-by-line, call reps?) How long does it take? Who does it?
- **Do you have real-time visibility into rep location/status?** Or is it manual check-ins? How do dispatchers know who's available to take a reassignment?
- **Can the system suggest the "next best rep" for a reassignment?** (Closest, right skills, available, already going to nearby store?)
- **Overtime management:** You mentioned you can't see overtime until payroll processing runs. What's the business impact? (Unexpected costs, overloaded reps, compliance risk?)
- **What does "exception reporting" mean to you?** (Jobs missed, SLA breached, defects found, reps running late, parts missing?)

### Cross-LOB & Multi-Client Work
- **Jay said the org is moving toward "fluid resources who can work on multiple clients."** What's driving this? (Cost, efficiency, client demand?)
- **What prevents cross-LOB work today?** (Incentives, training, system limitations, LOB politics, client contracts?)
- **Example: A merch rep spots a broken LG display.** What should happen? What happens today? Why doesn't it happen automatically?
- **If we could enable one rep to do merch + break/fix in the same store visit, what needs to be true?** (Training, parts on truck, time allocation, billing model, client approval?)
- **How do you bill when a rep does work for multiple clients in one visit?** (Split time, separate job codes, different pay rates?)

---

## 2. Workforce Structure & Culture

### Rep Types & Scheduling Flexibility
- **Dedicated teams (LG, Samsung) vs. shared teams (merch, flex).** What % of your workforce is each? What's the trend?
- **Full-time vs. part-time vs. gig/contract reps.** What's the mix? Are you trying to shift it?
- **Self-scheduling is a "people-friendly philosophy."** Jay mentioned the CEO challenges this because of cost. What's the debate? What's the data showing?
- **If you had to move away from self-scheduling, what would the resistance be?** (Rep attrition, harder to recruit, morale hit?)
- **Do reps want more flexibility or more stability?** (Pick their own schedule vs. predictable income?)

### Skills, Certifications & Territories
- **Do reps specialize (break/fix, installations, merch) or are they cross-trained?**
- **Are there certifications or skills required for certain work?** (LG-certified, electrical, heights, forklift?)
- **Do reps have assigned territories, or do they roam?** How often do they travel overnight?
- **Travel spend is "insane."** What's driving it? (Projects require teams from multiple regions? Not enough local reps? Client timing constraints?)
- **What would reduce travel spend?** (Better local scheduling, hire more local reps, clients accept longer lead times?)

---

## 3. Mobile Experience & Rep Tools

### Current Mobile Pain Points
- **Ki said mobile stability is a challenge across devices/environments.** What breaks? (Android vs. iOS? Offline mode? Specific device models? Network conditions?)
- **Offline mode:** How long are reps offline? What data needs to sync? What breaks when sync fails?
- **Tambra wants a "better rep mobile dashboard."** What's wrong with the calendar view today? What do reps need to see first thing in the morning?

### Historical Context & Asset Visibility
- **Kalin asked if reps can see historical work at a location.** You said no. How important is this? (Especially for dedicated teams?)
- **What would a rep do with historical context?** (See last install date, previous issues, contact history, photos of last visit, parts used?)
- **Do reps need to see asset/equipment history?** (Serial numbers, warranty status, maintenance records, install base?)

### On-Site Workflows
- **Walk us through a rep's day from leaving home to completing the last visit.** (Check schedule, route to store, check in, complete survey, capture time, check out, sync, repeat?)
- **What happens when a rep encounters something unexpected?** (Store closed, wrong parts shipped, contact unavailable, display already fixed by someone else?)
- **Support center:** Reps call in for help. What % of calls are system issues vs. "how do I do this work" vs. parts/travel logistics?
- **Training/knowledge content:** Reps access Wistia/YouTube videos in Resources. Is it easy to find? Do they actually use it? What's missing?

---

## 4. Break/Fix & Parts Management

### Current Workflow Pain Points
- **Walk us through break/fix end-to-end today.** (Call center intake → troubleshoot → parts order → approval → warehouse → ship → track → rep install → close ticket)
- **What % of break/fix is call-in vs. discovered during a merch visit?** (If merch finds it, does it get captured? Or lost?)
- **Parts ordering requires call center approval today.** You want to automate with safeguards. What are the safeguards? (Dollar threshold, manager approval, specific parts only?)
- **Parts are shipped to store location, not rep's home — mostly.** Jay said that's changing. What's driving reps to have parts shipped home? (Scheduling flexibility, stockpiling for multi-store routes?)
- **Do reps carry a truck stock of common parts?** Or is everything ordered per-job?
- **Warranty parts vs. billable parts.** How do you track this? Does it matter for billing? For client reporting?

### Go-Backs & Rework
- **Jay mentioned "minimize go-backs" as a top priority.** What causes go-backs today? (Wrong parts, incomplete work, quality issue, store not ready, rep didn't have right skills?)
- **How often do you have to send a rep back to the same store within a week?** What's the cost impact? (Mileage, time, client frustration?)
- **When a defect is found in a survey, it's manually exported and rescheduled.** How long does that take? Who does it? What gets missed?
- **What would automated exception handling look like?** (Auto-create ticket, auto-route to right rep, auto-order parts, auto-schedule go-back?)

---

## 5. Project & Survey Management

### Call Forms, Waves & Surveys
- **In OpenSky, a "call form" = project, and "waves" = execution windows.** Does this model work well? What would you change?
- **Surveys are highly configurable (conditional logic, products, stores, date ranges).** How much time does a client service manager spend building a survey? Is it fast enough?
- **Question library & question sets:** Do teams reuse surveys, or is every project custom?
- **How often do surveys change mid-wave?** (Client changes requirements, products go out of stock, store list changes?) What breaks when that happens?

### Client Service vs. Field Operations Roles
- **You have separate teams: client service (project setup, billing) and field operations (manage reps, payroll).** Does this work? Or is there friction?
- **Small dedicated teams do both roles (one person).** Is that better or worse?
- **What handoffs break between client service and field ops?** (Survey not ready, stores not uploaded, reps not assigned, billing mismatch?)

---

## 6. Data, Reporting & Integrations

### Real-Time Data & Analytics
- **James (data services) wants lower-latency data with delta/CDC.** What business decisions need real-time data? (Overtime alerts, SLA breach warnings, inventory levels, schedule compliance?)
- **Today: 4-hour batch to data warehouse → Tableau/PowerBI.** What can't you answer fast enough?
- **Jay mentioned "real-time exception reporting."** What exceptions? (Rep late, job missed, defect found, part missing, store closed, SLA at risk?)
- **Overtime visibility:** If you could see a rep approaching 40 hours mid-week, what would you do? (Stop assigning work, reassign to another rep, get manager approval?)

### Integration Landscape
- **ADP (payroll):** Timekeeping flows from OpenSky → payroll processing app → ADP. What breaks? What's manual? How often are there payroll errors?
- **Business Central (finance/ERP):** Job costing by project. Does this work well? What's the lag between field work and invoicing?
- **LMS (learning management):** Two-way feed (send users/teams, receive course completions). Do reps actually take required courses before going on-site? How do you enforce it?
- **Warehouse system:** Materials/shipping requests. What % of shipments track correctly? What gets lost? Where's the manual reconciliation?
- **CRM (sales):** Currently separate from OpenSky. Should it be integrated? (Lead → project → field execution → upsell opportunity?)

---

## 7. Business Model & Billing

### How Work is Billed
- **Every visit is billable (unless it's a go-back for your mistake).** Hourly vs. salary vs. per-diem vs. door fee. Explain the models.
- **Dedicated teams (salary):** They can "go off on tangents" because client pays flat rate. Shared teams can't. How do you manage scope creep?
- **Job costing by project:** Does BC get real-time job cost data? Or is it after-the-fact? Can you see project profitability mid-execution?
- **Client contracts:** Are they per-visit, per-project, retainer, or some mix? Do SLAs matter? (Response time, completion time, quality metrics?)

---

## 8. Change Management & Future State

### July 6 Rollout & Stabilization
- **You're rolling out OpenSky across 6-7 business units in July.** What's at risk? (Reps trained? Surveys migrated? Data clean? Integrations tested?)
- **Post-rollout, you expect "massive stabilization effort."** What typically breaks in a rollout like this?
- **What does stabilization mean for bandwidth to evaluate Salesforce?** (Pause until Q4? Continue in parallel? Phased demo/pilot?)

### Organizational Shifts (Next 2-3 Months)
- **Jay mentioned org structure is changing:** LOB silos → geographic model, potentially. What's driving this? What's the timeline?
- **If reporting structure changes, does your OpenSky hierarchy model break?** (Position trees by LOB vs. by geography?)

### AI & Automation Appetite
- **Kalin asked about AI. Jay said: "lot of interest, some small pilots (chatbot, image validation)."** What's the use case for image validation? (Rep takes photo, AI checks if display is correct?)
- **What would AI-powered scheduling solve that rules-based scheduling can't?** (Learn rep productivity, predict travel time, factor in traffic/weather, auto-balance workload?)
- **Chatbot for reps:** What would it do? (Answer "where's my next job?", "how do I fix this display?", "where's my part shipment?", "who do I call if store is closed?")

---

## 9. Success Metrics & Deal-Breakers

### What Does Success Look Like?
- **If you replace OpenSky with Salesforce, what does "success" look like in 90 days?** (Reps love mobile app? Scheduling is faster? Fewer go-backs? Better margin visibility?)
- **What would make this a failure?** (Mobile doesn't work offline? Reps hate it? Client service can't build surveys fast enough? Integrations break?)
- **What KPIs matter most to your business?** (Jobs completed per rep per day, first-time completion rate, on-time %, mileage cost per visit, overtime %, margin per project, client satisfaction?)

### Evaluating Alternatives
- **Are you evaluating other FSL platforms?** (ServiceTitan, FieldEdge, BuildOps, custom-build OpenSky v2?)
- **What does OpenSky do really well that a new platform MUST match or beat?** (Survey flexibility? Offline mobile? Travel management? Multi-LOB support?)
- **What's the risk of staying on OpenSky vs. moving to Salesforce?** (Maintenance cost, can't scale, talent hard to find, features lag?)

---

## 10. Open Discussion

**Questions for us:**
- What questions do you have for Salesforce based on the June 18 demo?
- What did you see in Salesforce products/demos before that you liked or didn't like?
- What would you want to see in a Salesforce FSL demo tailored to your business?
- Are there specific workflows we should prioritize? (Scheduling? Mobile? Break/fix? Reporting?)

**Next Steps:**
- Architecture session June 24 to map integrations
- Follow-up demo (post-architecture session)
- Align on rollout timeline (post-July 6 stabilization? Pilot? Phased?)

---

## Notes from Tomorrow's Discovery

**Top Pain Points:**
- 

**Top 3 Must-Haves for FSL:**
1. 
2. 
3. 

**Deal-Breakers / Red Flags:**
- 

**Integration Priorities:**
- 

**Demo Focus Areas:**
- 

**Timeline & Next Steps:**
- 
