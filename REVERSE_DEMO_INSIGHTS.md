# Reverse Demo Strategic Insights - June 18, 2026

**Analysis Date:** June 23, 2026  
**Source:** 2-hour OpenSky platform walkthrough

---

## Business Model Reality Check

**Initial Assumption:** Retail merchandising company (stock resets, planograms, order capture)  
**Actual Reality:** Hybrid field services + retail execution consolidator

They do **everything**:
- Break-fix reactive service (broken displays, equipment troubleshooting)
- Major construction projects (5-15 person teams, multi-day installations)
- Routine merchandising (cleaning, resets, audits)
- Product demos and training
- Parts fulfillment and logistics

**What They DON'T Do:**
- **Not restocking:** "Our reps are generally not restocking. Most of the time they will move stock around. But we're not usually giving counts of inventory back to our clients." - Kari
- **Not order capture:** No mention of taking product orders (confirms NOT traditional retail execution)
- **Not CRM for sales:** "Currently it's handled separately. We don't connect our CRM for sales directly except for at the project level and at the job level." - Kari

---

## Top Pain Points (Direct Quotes)

### Jay Chandran (CTO) - Intelligent Scheduling

> "Intelligent scheduling number one, right? And then field facing efficiency improvements and then real time exception reporting minimize the gobacks."

> "Multiple line of business and each line of business has their own preferred way of scheduling that limits our ability to optimize a resource across the line of business."

> "We believe that we attract a lot more talent pool because of the flexibility in terms of scheduling right which is true in most cases but also it kind of hurts us because we're not able to really schedule anything and and track our schedule right it's kind of a double-edged sword."

**Cross-LOB Optimization Gap:**
> "A merch goes to a target, sees one of the install broken or a display broken. There is not even an incentive for the person to capture that and send it because that's not the line of business. That's not the call form is working on. And even if it is sent, there's no automatic trigger escalation workflow that is happening back end."

**Client 360 View Missing:**
> "Today we look at as a project and each project is aligned to a line of business. We don't see them as a holistic plan and that's the big opportunity for us."

**Vision for Future:**
> "The positioning that we are taking now we're not yet there is to say the big clients that hey instead of we send four people doing four jobs we can send two consolidate the work and bring you more value more automation and more 360 view of what's happening in the store that's been liked by the store but the challenge though from both from a process operation and technology standpoint we're not set up there."

### Kari Kraus (Dev Lead) - Mobile Stability & Team Scheduling

> "A mobile app that works consistently in all different environments across multiple different types of devices. We have that, but man is that hard to keep clean."

> "How do you schedule single projects and how do you schedule multiple teams when you need maybe five to 15 people at the store on the same day at the same time and you have to look at availability. You have to see whether they're on other projects. All that stuff has to be taken in effect when you do it."

**Hard Scheduling Has No Optimization:**
> "The manager goes in when and they're looking at the store bucket and they're loading those stores, it doesn't prompt them that they're making a mistake because they should be grouping these together for these people for this reason. We only have it on the front end for self-scheduling."

**Team Projects:**
> "Most of our hard scheduling today is done for two or more people showing up at the same store on the same day to do a project."

### Mario Morales (Dev Manager) - Reactive Scheduling

> "The smarter scheduling and provisioning of slots for work figuring out who needs to be aware not just for pre-programmed things a month away or weeks away but just handling those issues that happened during the day reactive breaks things that people people couldn't come today they got sick So you had a plan and then it breaks."

### Tambra Owens (PM) - Mobile UX

> "A better rep mobile dashboard." 

(Context: Calendar-first view doesn't provide enough guidance for daily work)

### James Dyer (Data Director) - Real-Time Data

> "We would love to engage with a platform that is able to extract data not just like in a report... When we last spoke, this is where we were at. Please give us a delta."

> "When we have our data warehousing what we're looking for is more lower latency data which would imply some way to interface with the product to say, 'Look, we spoke an hour ago or this was some serialized value that I'm going to pass to you. When we when we last spoke, this is where we were at. Please give us a delta.'"

---

## The "Open Sky" Platform Deep Dive

### Core Concepts

**Call Form = Project Template:**
- Survey builder with conditional logic
- Store assignments and materials
- Job costing integration

**Wave = Time-Bounded Execution:**
- Week, month, or custom duration
- Store count and visit duration defined
- Can be recurring or one-time

**Bucket = Assignment Tool:**
- Matching logic: distance, skills, position type
- Manual overrides allowed
- Bulk assignment capabilities

### Scheduling Modes Explained

**Self-Scheduling:**
- Rep drags work from unscheduled list to calendar
- System forces consolidation (multiple visits at same store → same day)
- Nightly route optimization runs automatically
- **Only works for self-scheduled visits**

**Hard Scheduling:**
- Manager pushes schedule for team projects
- Used for 5-15 person installations
- **No automatic optimization today** (manual process)
- Critical gap for efficiency

### Survey Flexibility (Competitive Advantage)

**Question Sets:**
> "The client service manager sets up one survey or project and they can attribute however many waves or stores they want to that individual survey. They create one survey, they can do as many visits as they want on it." - Kari

**Features:**
- Reusable library of questions
- Conditional logic (show based on store, date, product, SKU)
- Photo capture, signature, multiple choice
- Can pivot based on products in store
- Date-based question visibility

**Configuration Complexity:**
> "We create very detailed surveys. When I say detailed, I mean lots of questions, lots of functionality where they can put in pictures, all the question answer types, plus tons of conditionality." - Kari

---

## Technical Architecture Details

### Mobile App (Offline-First)

**Critical Requirements:**
- Must work offline in stores (poor connectivity)
- Photo capture and conditional logic
- Check-in/check-out with GPS
- Time entry and expense reporting
- Syncs when connectivity returns

**Device Fragmentation Challenge:**
> "A mobile app that works consistently in all different environments across multiple different types of devices. We have that, but man is that hard to keep clean." - Kari

### Integration Landscape

**Business Central (ERP):**
- Job costing by project
- Payroll hours
- Invoicing

**Warehouse System:**
> "We can push the requests over to our warehouse and then they can pick and and make the shipment and then we get data back of what was shipped for each person for each thing that was shipped to them." - Kari

**ADP (Payroll):**
- Time cards pushed from Open Sky
- Expense reimbursement
- Overtime calculated after-the-fact

**LMS (Third-Party):**
- Course completions
- Required training enforcement

**Travel Platform (Agency):**
- Flight/hotel bookings
- Itinerary management

**Data Warehouse:**
- 4-hour batch extract (major pain point)
- Tableau/PowerBI dashboards

### Data Extraction Pain

**Current State:**
- Must request full date range, derive delta manually
- No change data capture capability
- 4-hour latency minimum

**James Dyer's Request:**
> "If I could just request the delta, that would be a huge win for the business."

(Use case: Real-time overtime alerts, SLA breach warnings, project profitability)

---

## Parts Management Workflow Details

**End-to-End Process:**

1. **Call center** receives issue report
2. **Troubleshoot** over phone (avoid unnecessary parts shipment)
3. **Approve** part order if needed (manual approval for high-value items)
4. **Ship** to store OR rep's home (inconsistent process, becoming more common to ship to rep)
5. **Assign** rep to install
6. **Track** completion and job costing

**Manual Upload Workaround:**
> "Some people do that. We have this other tab that's called upload, and they can upload it from the survey directly into here, and it creates the parts tickets for them." - Kari

(Context: Defects found in surveys can be manually exported and uploaded to create parts tickets — not automated)

---

## Operational Details

### Expense Management

> "So, when our reps go in and they put in work at the end of a call form, they're able to go in and enter their time... mileage, drive time, instore time, admin time." - Kari

**Features:**
- Tied to specific visit (job costing)
- Photo of receipt
- Manager approval workflow
- Automatically calculated mileage and drive time

### Alternate Pay Rates

> "Sometimes a person's paid their regular pay, sometimes they're paid an alternate pay rate. And we can and we have to send them an email saying you get paid a different rate for this job. Normally you get paid 17 an hour, we're going to now pay you 1650. We send them an email. They say yes, I accept the job at that rate." - Kari

(Context: Some stores pay premium rates, requires explicit rep acceptance)

### Travel Costs

> "Some of our teams do an extreme amount of travel. We're talking like we spend insane amount of money with travel every year moving our teams around the country to do projects." - Kari

**Driver:**
- Multi-person installation teams (5-15 reps)
- Often fly in from multiple regions
- Multi-day projects
- Last-minute changes common

---

## End-of-Call "Magic Wand" Question

### Dan Jenks Asked:
> "If you could wave a magic wand today, what's like the, you know, one or two things that you're like, 'Oh, I wish this would change.'"

### Responses (Prioritized):

1. **Jay:** "Intelligent scheduling number one"
2. **Kari:** "A mobile app that works consistently"
3. **Mario:** "Smarter scheduling and provisioning... handling those issues that happened during the day"
4. **Tambra:** "A better rep mobile dashboard"
5. **James:** "Lower latency data" (real-time delta extraction)

---

## Reverse Question to Salesforce Team

### Jay Chandran Asked:

> "Anybody in Salesforce team after seeing the product that we have, you guys have a good product, but here are the one, two, three top things that you are lacking, you're missing or that could enhance a product. What would be those one or two three things?"

### Dan Jenks' Response:

> "I think the short answer Jay is I think a lot comes into play with scheduling and and routing and especially knowing the impact it has on TN [travel & expenses]."

**Team Deferred:**
- Need to debrief internally first
- Architecture session (June 24) will inform deeper questions
- Follow-up session (week of July 1) for targeted gaps

---

## Timing & Context

### July 6, 2026 Rollout

> "We have a big roll out on July 6th" - Jay (mentioned multiple times)

**Scope:**
- Deploying Open Sky across all 6-7 business units
- Consolidating 3 legacy platforms
- All hands on deck

### Post-Rollout Expectations

> "There is a massive stabilization effort" - Jay

**Implications:**
- Resource constrained after July 6
- Q4 2026 earliest realistic evaluation window
- Must maintain relationship through stabilization

### AI Interest

> "That's been thought and since I came in a lot more interest lot more appetite and lot more adaptability on the business side but we did start a small team a couple of months and exploring some opportunity especially on the rep efficiency facing set of things chatbot some picture comparison picture validation." - Jay

**Focus Areas:**
- Rep efficiency (chatbot, knowledge access)
- Image validation (planogram compliance, quality checks)
- NOT yet working on AI scheduling (resource constrained)

---

## Salesforce Team Questions During Demo

### Dan Jenks (AE) - Strategic Focus

**Asked About:**
- CRM/lead management integration (currently separate)
- Routing efficiency and optimization (hard scheduling gap)
- Overtime management visibility (calculated after-the-fact)
- Billable work tracking (all visits billable except go-backs)
- Feedback loops (reactive work creation from surveys)
- Self-scheduling value proposition (talent attraction vs. cost control)
- Parts storage location (store vs. rep's home)

### Kalin Gabbert (SE) - Workflow Focus

**Asked About:**
- Work reassignment process (sick reps, emergencies → bulk reschedule tool)
- Signature capture requirements (via survey question, not standard)
- Historical visit data visibility (rep can't see prior visits — gap)
- Break-fix vs merchandising split (by revenue, not visit count)
- Survey template management (question sets, reusable library)
- Store closure handling (check-in validates store status)

### Stephen Jackson (Architect) - Documentation Focus

**Asked About:**
- Complete capability list (Kari's spreadsheet to be shared)
- Technical architecture deep dive (June 24 session)

---

## Strategic Takeaways

### This is NOT FSL vs Retail Execution

It's a **workforce management transformation** opportunity with:
- Complex scheduling optimization needs (Einstein AI)
- Offline mobile with sophisticated task management
- Real-time data integration (MuleSoft)
- Cross-functional visibility and workflow automation

**Why This Matters:**
- Can't position as pure FSL (they do merchandising)
- Can't position as pure Rex (they do break-fix and installations)
- Hybrid solution OR platform approach required

### The $73.5K "Crawl" is Misleading

**Reality Check:**
- 70 licenses for 4,140 reps = 1.7% coverage
- Clearly a pilot with massive expansion potential
- $3M-$5M full deployment scenario
- Need to think long-term relationship, not quick close

### Timing is Critical

**July 6 Rollout:**
- All hands on deck
- Post-rollout: Resource constrained
- Q4 2026 earliest realistic evaluation window

**What This Means:**
- Must maintain relationship through stabilization
- Share relevant content (case studies, best practices)
- Position as enhancement for 2027, not replacement now
- Don't push hard close before they're ready

### Positioning Strategy

**DON'T Position as Replacement:**
- They just spent massive effort building Open Sky
- Leadership invested in custom platform
- Recent consolidation of 6 companies
- July rollout is major milestone

**DO Position as Enhancement:**
- AI scheduling Open Sky lacks (Einstein)
- Real-time data capabilities (MuleSoft)
- Cross-LOB optimization (platform integration)
- Mobile UX improvements (offline stability)
- Ecosystem solutions (AppExchange)

**Focus on Gaps They Can't Close:**

1. **Intelligent, AI-driven scheduling**
   - Multi-constraint optimization
   - Team availability matching
   - Predictive analytics
   - Einstein scheduling APIs

2. **Real-time exception handling**
   - Streaming data (vs 4-hour batch)
   - Proactive alerts (overtime risk, SLA breach)
   - Event-driven workflows

3. **Cross-system workflow automation**
   - Merch rep spots issue → auto-create service ticket
   - Parts approval → warehouse → tracking → completion (end-to-end)
   - CRM → project → field execution → upsell (closed loop)

4. **Predictive analytics and insights**
   - Project profitability forecasting
   - Rep performance trends
   - Client relationship 360 view

---

## Key Competitive Differentiators

### 1. Einstein AI - Scheduling Optimization

**Their Need:**
- "Intelligent scheduling number one" - Jay

**Salesforce Answer:**
- Einstein Optimization (resource matching, route optimization)
- Einstein Next Best Action (guided mobile flows)
- Einstein Prediction Builder (forecast job duration, rep performance)
- Einstein Discovery (identify optimization opportunities)

### 2. Platform Integration - Unified Data Model

**Their Need:**
- "We don't see them as a holistic plan" - Jay
- "Lower latency data" - James

**Salesforce Answer:**
- MuleSoft for real-time integration (CDC, event-driven)
- Customer 360 (client view across all projects)
- Tableau CRM (real-time dashboards, not 4-hour batch)
- Slack (team collaboration, automated notifications)

### 3. Real-Time Capabilities

**Their Need:**
- "Real time exception reporting minimize the gobacks" - Jay
- "Please give us a delta" - James

**Salesforce Answer:**
- Platform Events (real-time streaming)
- MuleSoft Change Data Capture
- Einstein Analytics streaming datasets
- Flow automation (event-driven workflows)

### 4. Ecosystem - AppExchange Solutions

**Their Need:**
- Image validation (planogram compliance)
- Chatbot (rep knowledge access)
- Advanced mobile forms (survey flexibility)

**Salesforce Answer:**
- AppExchange partners for gaps
- FormAssembly / Survey Force (flexible surveys)
- Einstein Bots (rep chatbot)
- Computer vision ISVs (image validation)

### 5. Scale - Proven at Complex Enterprises

**Their Need:**
- 4,140 reps across 6 business units
- Multiple work types (break-fix, installations, merchandising, audits)
- Dedicated + shared workforce models
- Multi-client, multi-LOB complexity

**Salesforce Answer:**
- FSL deployed at 100K+ user enterprises
- Multi-tenant architecture (scale + security)
- Consumer Goods Cloud references (CPG, retail execution)
- Hybrid solutions (FSL + Rex + platform)

---

## Next Steps & Documents

### Immediate Follow-Up

**June 24, 9am:** Architecture review session
- Map integration landscape
- Understand July 6 rollout scope
- Identify technical constraints

**Week of July 1:** Follow-up discovery
- Address outstanding questions from reverse demo
- Deep-dive on specific modules (parts, travel, etc.)
- Clarify FSL vs Rex positioning

### Documents to be Shared by Channel Partners

1. **Kari's capability spreadsheet** (living document, being cleaned up)
2. **Open Sky feature list by role** (client service, field ops, reps, etc.)
3. **PowerPoint presentation from demo**

### Salesforce Team Deliverables

1. **Architecture diagram** (after June 24 session)
2. **Solution positioning deck** (FSL + Rex + platform approach)
3. **Reference customer list** (similar complexity, scale)
4. **Proof of concept scope** (for Q4 2026 evaluation)

---

## Open Questions for Follow-Up

### Business Model

1. What % of work is self-scheduled vs. hard-scheduled? (By visit count, by revenue)
2. What % of workforce is dedicated vs. shared? (By headcount, by revenue)
3. What % of work is break-fix vs. merch vs. installations? (By revenue preferred)
4. What's the average mileage reimbursement per rep per week?
5. What's the travel spend annually? What % is avoidable with better local scheduling?

### Operational

6. How often do schedules break mid-day? (Sick rep, job runs long, store closed)
7. What's the average number of stores per rep per day? (Shared teams vs. dedicated)
8. How many go-backs per week? What % are due to wrong parts vs. incomplete work?
9. What's the typical lag between field work completion and invoice to client?
10. How many parts tickets are created per week? What % are approved vs. rejected?

### Technical

11. What's the typical survey build time for a new project?
12. What's the payroll error rate? (Time entry disputes, overtime miscalculations)
13. What's the support center call volume per week? (System issues vs. work guidance)
14. What's the data warehouse extract volume? (Records per batch, data size)
15. What's the mobile app sync frequency? (How often do reps sync?)

### Organizational

16. What's the rep attrition rate? Does self-scheduling reduce attrition?
17. What's the timeline for org restructure (LOB silos → geographic model)?
18. How many client service managers are there per LOB?
19. How many field operations managers per region/LOB?
20. What's the IT team size supporting Open Sky?

---

## Risk Assessment

### Technical Risks

**High:**
- Mobile offline requirement (non-negotiable, FSL must match or beat Open Sky)
- Survey flexibility (Open Sky extremely configurable, FSL may require customization)
- Integration complexity (7 systems, real-time data requirements)

**Medium:**
- Data migration from Open Sky (3 legacy platforms consolidated)
- Self-scheduling culture (FSL scheduling model may face rep resistance)
- Team scheduling complexity (5-15 person projects, multi-day)

**Low:**
- Parts management workflow (FSL Asset Management covers this)
- Time entry and expenses (FSL handles this natively)

### Business Risks

**High:**
- Open Sky stabilization consumes budget (no funds for Salesforce if rollout fails)
- Pilot fails (70-license crawl doesn't work, no expansion)
- Competing priorities (AI investments, other platform upgrades)

**Medium:**
- Org structure in flux (LOB silos → geographic model, hierarchy changes)
- Self-scheduling sacred cow (CEO challenges it, but reps/managers defend it)
- Timeline compression (want results faster than realistic implementation)

**Low:**
- Competition from other vendors (they built custom, unlikely to evaluate many)
- Executive sponsor turnover (Jay seems committed to transformation)

### Mitigation Strategies

**Technical:**
1. Offline mobile POC (prove FSL works in store with no connectivity)
2. Survey builder demo (show flexibility, custom form components)
3. Integration architecture session (MuleSoft patterns, CDC approach)

**Business:**
1. Position as 2027 enhancement (not 2026 replacement)
2. Share Open Sky stabilization best practices (earn trust)
3. Pilot success criteria definition (before expansion commitment)

**Relationship:**
1. Monthly check-ins through stabilization (stay top-of-mind)
2. Share relevant content (AI scheduling case studies, references)
3. Architecture review follow-through (prove technical credibility)

---

## Competitive Positioning Summary

### What Open Sky Does REALLY Well

**Must Match or Beat:**
- Survey flexibility (conditional logic, product pivots, question library)
- Offline mobile (reps work in stores with poor connectivity)
- Multi-LOB support (dedicated + shared teams, different billing models)
- Job costing integration (Business Central, project-level tracking)

### What Open Sky CANNOT Do

**Salesforce Differentiators:**
- AI-driven intelligent scheduling (their #1 need, custom code can't scale)
- Real-time data streaming (stuck at 4-hour batch without major rearchitecture)
- Cross-LOB workflow automation (manual today, platform events enable this)
- Predictive analytics (Einstein, not just reporting)
- Client 360 view (project-focused today, CRM integration required)

### Messaging Framework

**For Jay (CTO):**
- "Intelligent scheduling with Einstein AI"
- "Real-time data platform (MuleSoft + Platform Events)"
- "Cross-LOB optimization you're envisioning"

**For Kari (Dev Lead):**
- "Enterprise mobile platform (offline-first, cross-platform consistency)"
- "Flexible survey engine (Lightning Web Components, custom forms)"
- "AppExchange ecosystem for gaps (no custom code for every feature)"

**For James (Data Director):**
- "Change data capture APIs (delta extraction you're asking for)"
- "Streaming data integration (MuleSoft + Kafka)"
- "Real-time dashboards (Tableau CRM, not 4-hour batch)"

**For Tambra (PM):**
- "Einstein Next Best Action (guided mobile flows)"
- "Contextual recommendations (not just calendar view)"
- "Field Service Mobile redesign (modern UX)"

---

**End of Strategic Insights**
