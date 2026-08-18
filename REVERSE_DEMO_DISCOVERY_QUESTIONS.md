# Reverse Demo/Discovery Questions - Channel Partners

**Session Date:** TBD (couple of days from June 29, 2026)  
**Purpose:** Determine if Channel Partners needs align with CG Cloud Retail Execution (REX) or Field Service Lightning (FSL)

---

## 🎯 Opening Frame-Setting Questions

### What's driving this evaluation?

**Ask:**
1. "OpenSky is rolling out July 6. What specific gaps or pain points is OpenSky NOT solving that prompted you to look at Salesforce?"
2. "If you could wave a magic wand and fix ONE thing about your field operations today, what would it be?"
3. "What does success look like 12 months from now? What would have to change for this to be worth the investment?"

**Why this matters:**
- Reveals if this is "replace OpenSky" (expensive, unlikely) or "augment OpenSky" (realistic)
- Uncovers the REAL pain point (not just "better scheduling")
- Helps size the opportunity and set realistic expectations

---

## 📋 Merchandising vs. Service Work Ratio

### What percentage of your work is planned/recurring vs. reactive?

**CG Cloud signals:**
- Planned store visits scheduled weeks in advance
- Recurring routes (same stores, same cadence)
- Retail execution work (shelf resets, planograms, audits)
- Client dictates the schedule (Target wave schedules, Best Buy project timelines)

**FSL signals:**
- Reactive work (equipment breaks, emergency calls)
- Unpredictable workload (can't plan 3 weeks out)
- SLA-driven (2-hour response time, same-day service)
- Parts/inventory required (can't complete job without specific materials)

**Ask:**
1. "For your merchandising team: How far in advance do you know which stores they'll visit? Days? Weeks? Months?"
2. "For your break-fix team: What percentage of work is emergency/same-day vs. scheduled maintenance?"
3. "If a Best Buy calls with a broken Samsung display, what's the expected response time? (2 hours? Same day? Next day?)"
4. "Do your reps visit the same stores repeatedly (recurring routes) or different stores every week?"

**Why this matters:**
- CG Cloud excels at **planned, recurring retail visits** (Visit Plans, multi-week routes)
- FSL excels at **reactive, SLA-driven service** (Work Orders, real-time dispatch)
- If 70%+ work is planned/recurring → CG Cloud  
- If 70%+ work is reactive/emergency → FSL  
- If it's 50/50 → You need both products

---

## 🗓️ Scheduling Pain Points

### The "10-hour weekend SVP scheduling call" problem

**From June 24 workshop:** Jay mentioned SVPs/EVPs spending entire weekends building schedules in spreadsheets for Target 1,900-store merchandising waves.

**Ask:**
1. "Walk me through that 10-hour weekend scheduling call. What are they actually DOING for 10 hours?"
   - Building routes from scratch? (CG Cloud Visit Plans solve this)
   - Dealing with last-minute changes/exceptions? (FSL Einstein Optimization solves this)
   - Matching specific skills to specific stores? (Both products handle this)
   - Balancing utilization across reps? (Both products handle this)

2. "When the spreadsheet is done, what happens next? How does it get into OpenSky?"
   - Manual data entry? (Integration opportunity)
   - CSV upload? (API integration)
   - OpenSky re-optimizes it? (Duplicate optimization = waste)

3. "Why is this being done in spreadsheets instead of OpenSky? What's missing in OpenSky?"
   - Can't model the complexity? (Custom constraints)
   - Takes too long to run? (Performance issue)
   - Doesn't consider the right variables? (Optimization rules)
   - Results are wrong? (Algorithm issue)

4. "How often do those plans change AFTER they're built? Daily? Hourly?"
   - If plans are stable → CG Cloud Visit Plans (build once, execute for weeks)
   - If plans change constantly → FSL real-time optimization (dynamic re-assignment)

**Why this matters:**
- CG Cloud Visit Plans = **strategic, multi-week route planning** (plan once, execute many times)
- FSL Einstein Optimization = **tactical, real-time re-assignment** (dynamic, handles exceptions)
- If the pain is "building the plan" → CG Cloud
- If the pain is "plan breaks immediately" → FSL

---

## 📸 Survey & Data Collection Requirements

### The "600-1,200 question survey" complexity

**From June 24 workshop:** Some audits have 600-1,200 questions with grid questions (10 columns × 10 rows), conditional logic, task subdivision.

**Ask:**
1. "Show me your most complex survey. Walk me through it question by question."
   - How many questions total?
   - How many are grid questions? (Same question repeated across rows/columns)
   - How much conditional logic? ("If you answer X, then ask Y")
   - How are tasks subdivided? (Can a rep pause and resume mid-survey?)

2. "What happens when a rep is in the middle of a survey and loses connectivity?"
   - How long can they work offline? (4 hours? 8 hours? All day?)
   - When they reconnect, does everything sync? (Offline reliability)
   - Have you ever lost data because of sync failures? (Risk tolerance)

3. "How many photos do reps take per shift? Per survey?"
   - 5 photos? 50 photos? 100 photos?
   - What happens to those photos? (Stored locally? Auto-upload? Reviewed by QA?)
   - Are photos tagged/labeled? (Compliance photo, before/after, specific product)

4. "Does OpenSky handle these surveys today? Or is this a gap?"
   - If OpenSky handles it → Why replace what works?
   - If it's a gap → This is a strong Salesforce use case

**Why this matters:**
- **Neither CG Cloud nor FSL handles 600-1,200 question surveys out-of-the-box**
- CG Cloud Assessment Tasks = better starting point (OOTB 50-100 questions)
- FSL Service Work Plans = more basic (OOTB 10-20 steps)
- **Both require custom Lightning Web Component development** ($300K-500K)
- Don't oversell OOTB capabilities → Let them test a prototype before committing

---

## 🔧 Parts & Materials Tracking

### The "30-40% of go-backs are materials-related" problem

**From June 24 workshop:** John said "number one thing in our goback data shows as materials" - parts not delivered, wrong parts, missing tools.

**Ask:**
1. "Walk me through the parts workflow today. Rep gets assigned a job - how do they know if they have the right parts?"
   - Check inventory in their van? (Trunk stock management)
   - Call dispatch? (Manual process)
   - System tells them? (WMS integration)
   - Find out when they arrive at the site? (Too late)

2. "When a rep needs a part that's not in their van, what happens?"
   - Drive to warehouse? (Travel time waste)
   - Another rep brings it? (Coordination complexity)
   - Reschedule the job? (Go-back)
   - Client provides it? (Billing issue)

3. "Do your reps manage their own van inventory? Or does someone stock their vans for them?"
   - Self-managed → Need mobile inventory visibility
   - Centrally managed → Need replenishment alerts

4. "How do you track parts usage and billing?"
   - Parts consumed tied to specific jobs? (Cost tracking)
   - Parts billed to client separately? (Invoice line items)
   - Parts included in labor rate? (No tracking needed)

**Why this matters:**
- **FSL has native parts tracking** (ProductRequired, ProductConsumed, LocationInventory)
- **CG Cloud has basic asset tracking** (promotional materials, POP displays) but NOT repair parts
- If 30-40% of go-backs are materials → FSL + WMS integration is highest ROI opportunity
- If materials = merchandising supplies (signage, shelf tags) → CG Cloud handles it
- If materials = repair parts (cables, components, tools) → FSL required

---

## 👷 Contractor vs. W-2 Employee Mix

### The "Construction uses third-party contractors" model

**From June 24 workshop:** Construction work uses invoice-based contractors with link-based call form access (no system login).

**Ask:**
1. "What percentage of your field workforce is W-2 employees vs. contractors/1099?"
   - If 90%+ W-2 → Simpler licensing (everyone gets same license type)
   - If 30%+ contractors → Need Experience Cloud + contractor management

2. "How do contractors access your systems today?"
   - Link-based (no login) → Experience Cloud guest access
   - Contractor portal → Experience Cloud Community
   - Full system access (same as W-2) → Expensive, security risk

3. "How are contractors paid?"
   - Hourly (like W-2 but different rate) → FSL handles this
   - Flat fee per job → FSL handles this
   - Invoice-based (submit invoice after completion) → FSL + AP integration

4. "Do W-2 employees and contractors ever work on the same project together?"
   - Yes → FSL Crew Management (mixed resource types)
   - No → Can isolate contractor work to separate workflows

**Why this matters:**
- **Experience Cloud licenses are cheaper** ($600-1,200/year vs. $1,980-2,400/year for FSL)
- If you can put contractors on Experience Cloud → Significant cost savings
- FSL supports Resource Type = Contractor (different payment models, limited system access)
- CG Cloud doesn't have strong contractor support → FSL advantage

---

## 🤖 AI & Automation Priorities

### Jay's "bidirectional chatbot" and planogram QC use cases

**From June 24 workshop:** Jay described 17+ AI use cases, with bidirectional field chatbot and $13.2M planogram QC automation as top priorities.

**Ask:**
1. "Show me the planogram compliance workflow today. Rep takes a photo of a shelf - then what?"
   - QA team manually reviews? (Human bottleneck)
   - Algorithm checks compliance? (Existing AI)
   - Client reviews? (External dependency)
   - No formal QC? (Risk exposure)

2. "If Einstein Vision could auto-check planogram compliance in 2 seconds, what would that unlock?"
   - Faster QA turnaround? (Speed)
   - Eliminate manual QA cost? ($13.2M savings)
   - Real-time corrective action? (Rep fixes on-site immediately)
   - Better client reporting? (Prove compliance)

3. "For the bidirectional chatbot: What questions are reps asking most often?"
   - "How do I set up this display?" → Knowledge Base article retrieval
   - "Where's my next job?" → Scheduling/routing question
   - "Do I have the right parts?" → Inventory lookup
   - "What's the pay rate for this job?" → Payroll/compensation question

4. "What systems would the chatbot need to access to answer those questions?"
   - OpenSky? (Scheduling data)
   - Sphere/WMS? (Inventory data)
   - ADP? (Payroll data)
   - Knowledge Base? (Training docs)
   - All of the above? (Integration complexity)

**Why this matters:**
- **CG Cloud has Einstein Vision for planogram compliance** (OOTB feature, strong ROI)
- **FSL has Einstein Bots for field chatbots** (Service Cloud foundation required)
- Both products integrate with Agentforce (bidirectional AI)
- If planogram QC is top priority → CG Cloud is obvious choice
- If chatbot is top priority → Works with both products (not a differentiator)

---

## 💰 Budget & ROI Expectations

### Setting realistic expectations

**Ask:**
1. "What's the budget for this project? (Ballpark order of magnitude: $500K? $2M? $5M? $10M+?)"
   - Helps frame realistic scope (70 users vs. 4,140 users)

2. "What's the expected payback period? (6 months? 12 months? 3 years?)"
   - Aggressive ROI → Focus on highest-pain use case only
   - Long-term transformation → Can justify broader scope

3. "If we solve the go-backs problem (10% → 5%), what's that worth to you annually?"
   - From docs: 10% go-back rate = $260M/year cost
   - 5% reduction = $130M/year savings (half the problem)
   - Even 2% reduction = $52M/year savings (massive ROI)

4. "What happens if you do nothing? Is OpenSky July 6 rollout solving these problems?"
   - If OpenSky solves it → No Salesforce needed
   - If OpenSky leaves gaps → Salesforce fills gaps (smaller scope)

**Why this matters:**
- $73.5K pilot (70 users) → Break-fix team only, FSL, narrow scope
- $2-3M/year → Platform licenses + Scheduler for all 4,140 users (scheduling only)
- $8-10M/year → CG Cloud + FSL for all 4,140 users (full replacement)
- Budget drives scope, not the other way around

---

## 🎯 Recommended Question Sequencing

**Start broad, narrow down based on answers:**

### Round 1: What's the REAL pain? (15 min)
1. What's driving this evaluation? (OpenSky gaps)
2. Magic wand: Fix one thing - what is it?
3. Success in 12 months = what changed?

### Round 2: Merchandising vs. Service work split (15 min)
4. % planned/recurring vs. reactive?
5. How far in advance do you schedule merchandising work?
6. Break-fix response time expectations?
7. Same stores repeatedly or different every week?

### Round 3: Deep dive on #1 pain point (20 min)

**If scheduling is #1 pain:**
- Walk through the 10-hour weekend call
- What's missing in OpenSky?
- How often do plans change after they're built?

**If go-backs are #1 pain:**
- Walk through parts workflow
- When does rep learn they have wrong parts?
- How do you track parts usage/billing?

**If surveys are #1 pain:**
- Show me your most complex survey
- How long can reps work offline?
- Does OpenSky handle this today?

### Round 4: Scope & Budget reality check (10 min)
- What's the budget order of magnitude?
- Expected payback period?
- What happens if you do nothing?

---

## 🚨 Red Flags to Listen For

**These answers mean "walk away" or "much smaller scope":**

1. **"OpenSky is great, we just want to see what else is out there"**
   - Translation: No burning pain, tire-kicking
   - Response: Not worth pursuing unless you can uncover hidden pain

2. **"We need to replace OpenSky before July 6"**
   - Translation: Impossible timeline (3 days from now)
   - Response: Can't replace in 3 days, but can augment for specific gaps post-July 6

3. **"Budget is flexible"**
   - Translation: They haven't thought about cost
   - Response: Ground them in reality ($73.5K pilot vs. $8M full deployment)

4. **"We want everything Salesforce can do"**
   - Translation: Scope creep guaranteed
   - Response: Narrow to ONE pain point, prove value, expand later

5. **"Our reps love OpenSky, management wants Salesforce"**
   - Translation: Change management nightmare
   - Response: User adoption will kill this project

---

## ✅ Green Flags to Listen For

**These answers mean "strong opportunity":**

1. **"10% go-back rate is killing us financially"**
   - Clear, quantified pain
   - FSL parts tracking + WMS integration = obvious solution

2. **"SVPs spend weekends building schedules manually"**
   - Executive-level pain (budget authority)
   - CG Cloud Visit Plans or FSL Einstein Optimization solve this

3. **"OpenSky can't handle our survey complexity"**
   - Functional gap that OpenSky won't solve
   - CG Cloud Assessment Tasks = starting point (but custom dev required)

4. **"We just acquired RMS, have 2 more acquisitions coming"**
   - PE roll-up playbook = recurring revenue opportunity
   - Salesforce M&A integration story strong

5. **"We're losing Samsung as a client because of poor reporting"**
   - Client retention risk (revenue at stake)
   - Experience Cloud client portals solve this

---

## 📝 Output Format for Session Notes

After the discovery session, document answers in this format:

**Pain Point Ranking:**
1. [Primary pain] - CG Cloud / FSL / Both / Neither
2. [Secondary pain] - CG Cloud / FSL / Both / Neither
3. [Tertiary pain] - CG Cloud / FSL / Both / Neither

**Product Fit Assessment:**
- **CG Cloud fit:** [0-100%] - Justification
- **FSL fit:** [0-100%] - Justification
- **Both needed:** [Yes/No] - Why?

**Recommended Scope:**
- **Users:** [X reps from Y team/LOB]
- **Use case:** [Specific pain point to solve]
- **Est. investment:** [$X licenses + $Y implementation]
- **Est. ROI:** [$Z annual benefit]

**Next Steps:**
- [ ] Build prototype (CG Cloud / FSL)
- [ ] Stress test (survey complexity / offline sync)
- [ ] Executive briefing (cost/benefit analysis)
- [ ] OR walk away (reason)

---

**End of Discovery Questions**
