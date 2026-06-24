# Implementation Strategy & Next Steps

**Last Updated:** June 24, 2026  
**Source:** Architecture session - strategic planning discussion

---

## Deployment Approach: Team-by-Team Rollout (NOT "Flip the Switch")

### Risk Assessment

**"Flip the Switch" Migration = Too Risky**

**Quote (paraphrased):**
> "The team agreed that a 'flip the switch' migration is too risky. The established, successful method for their organization is a team-by-team rollout, adding functionality as gaps are filled."

**Why "Big Bang" Fails:**
1. **Too many variables:** 4,140 reps, 6+ LOBs, 15+ integrated systems, dozens of custom workflows
2. **No rollback plan:** If migration fails on Day 1, can't revert 4,140 users back to old system quickly
3. **Training overwhelm:** Can't train entire organization on new system simultaneously
4. **Business continuity risk:** If system down during critical client projects (Target 1,900 stores/week), massive revenue impact
5. **OpenSky July 6 context:** Just rolling out OpenSky to replace 3 legacy platforms, can't add another major change immediately after

---

### Proven Methodology: Team-by-Team Rollout

**Channel Partners' Successful Pattern:**
- Roll out new functionality to one team at a time
- Add functionality incrementally as gaps identified and filled
- Learn from each team's experience, refine before next team
- Maintain stability for rest of organization while pilot team tests new system

**Example: OpenSky Rollout (Likely Approach for July 6):**
1. **Pilot team:** Single LOB (merchandising? audits?), single geography (California?), 50-100 reps
2. **Month 1:** Core functionality only (schedule, time tracking, basic surveys)
3. **Month 2:** Add parts management, expense reporting
4. **Month 3:** Add advanced scheduling, multi-project assignments
5. **Month 4:** Roll out to 2nd team (different LOB or geography), incorporate lessons learned
6. **Months 5-12:** Progressive rollout to remaining teams

---

## Salesforce Implementation Rollout Plan

### Phase 1: Pilot (Months 1-3, ~100 reps)

**Scope:**
- **LOB:** Single line of business (recommend: Merchandising or Audits, simpler workflow than break-fix)
- **Geography:** Single region (recommend: California or Texas, large rep population, major clients)
- **Functionality:**
  - FSL Core: Work Orders, Service Appointments, scheduling
  - FSL Mobile: Time tracking, survey completion, photo upload
  - Einstein Scheduling: Automated optimization (replace manager spreadsheet magic)
  - Basic integrations: LearnUpon LMS (training validation), Business Central (job costing)

**Success Criteria:**
- Rep satisfaction score >7/10 (mobile app usability)
- Manager time savings: 10+ hours/week (vs. manual scheduling)
- Scheduling efficiency: 10%+ utilization improvement (vs. OpenSky baseline)
- Go-back rate: 5%+ reduction (vs. OpenSky baseline)
- No critical outages (99.5%+ uptime)

**Deliverables:**
- Pilot report (what worked, what didn't, lessons learned)
- Refined rollout plan for Phase 2 (incorporate feedback)
- ROI validation (actual vs. projected savings)

---

### Phase 2: Expand to 2nd LOB (Months 4-6, +200 reps)

**Scope:**
- **LOB:** Break-fix (more complex: parts management, support center integration, go-back workflows)
- **Functionality added:**
  - Freshdesk integration (Case → Work Order automation)
  - WMS integration (parts tracking, shipment status)
  - Einstein Vision QC (automated photo review)
  - Experience Cloud portal (Samsung client portal, pilot with 1 major client)

**Success Criteria:**
- Break-fix specific: Go-back rate reduction 10%+ (parts tracking, pre-arrival checklist)
- Freshdesk integration: 50%+ reduction in manual issue uploads
- Client portal adoption: 1 major client actively using portal, satisfaction score >8/10

---

### Phase 3: Scale to Remaining LOBs (Months 7-12, +1,000 reps)

**Scope:**
- **LOBs:** Installations, Audits, Training (if not already in Phases 1-2)
- **Functionality added:**
  - Multi-project team scheduling (5-15 person crews)
  - Travel management integration (Agency/Amex API)
  - CPQ for project setup (standardized vs. custom offerings)
  - Einstein Bot (conversational chatbot for knowledge base)

**Success Criteria:**
- 50% of organization on FSL (2,000 reps)
- Cross-LOB scheduling: 5%+ capacity unlocked (merchandising reps flex to break-fix during busy weeks)
- Client portal expansion: 3-5 major clients using portals
- System trust: Managers using FSL scheduling (not reverting to spreadsheets)

---

### Phase 4: Full Rollout + Advanced Features (Months 13-18, +2,840 reps)

**Scope:**
- **Remaining reps:** All 4,140 W-2 employees on FSL
- **Advanced features:**
  - Construction group contractors (Experience Cloud portal, invoice-based payment)
  - RMS acquisition integration (Minnesota team, migrate from Portal to FSL)
  - Mars third-party labor integration (unified workforce view: W-2 + contractors + partners)
  - Advanced Einstein Analytics (predictive go-back risk, scheduling optimization, margin forecasting)

**Success Criteria:**
- 100% of W-2 employees on FSL
- OpenSky decommissioned (cost savings, one less system to maintain)
- Validated ROI: $32M revenue capacity + $8M overtime savings + $130M go-back reduction (or revised targets based on actuals)
- Client satisfaction: NPS improvement (better reporting, real-time visibility)

---

## Implementation Oversight: Salesforce-Led vs. Partner-Led

### Discussion Context

**Salesforce Preference:**
> "There is a discussion on whether to have Salesforce lead the implementation versus utilizing an outside partner. While Salesforce prefers direct accountability, they acknowledged that specific partners have deep expertise in their field service and retail execution solutions."

---

### Option 1: Salesforce-Led Implementation

**Pros:**
- **Direct accountability:** Salesforce owns end-to-end delivery (no finger-pointing)
- **Integrated team:** Solution engineers, architects, project managers all Salesforce employees
- **Product expertise:** Deep understanding of FSL roadmap, beta features, upcoming releases
- **Cost transparency:** Fixed Professional Services rates, no partner markup

**Cons:**
- **Generalist approach:** Salesforce PSng team handles all industries (not retail field service specialists)
- **Less customization:** Salesforce prefers clicks-not-code, may push back on custom requirements
- **Capacity constraints:** Salesforce PSng heavily booked, may have longer start date
- **Post-launch support:** Salesforce PSng exits after go-live, handoff to customer success (not ongoing dev partner)

---

### Option 2: Partner-Led Implementation (FSL Specialist)

**Pros:**
- **Industry expertise:** Partners specialize in field service, retail execution, CPG merchandising
- **Customization depth:** Partners build complex integrations, custom mobile components, industry accelerators
- **Reference customers:** Partners have deployed FSL for similar companies (Best Buy field services, retail merchandising firms)
- **Ongoing relationship:** Partners provide post-launch support, enhancements, training (not just implementation)

**Cons:**
- **Accountability:** Salesforce + Partner split responsibility (potential finger-pointing if issues arise)
- **Cost:** Partner markup on top of Salesforce licenses (25-50% premium vs. Salesforce-led)
- **Partner variability:** Quality varies across partners (must vet carefully, check references)
- **Lock-in risk:** Deep customization by partner may create dependency (hard to switch partners later)

---

### Hybrid Approach (Recommended)

**Salesforce + Partner Joint Delivery:**

**Roles:**
- **Salesforce:** Account team (AE, SA, CSM), architecture review, product roadmap alignment
- **Partner:** Day-to-day implementation, custom development, integrations, training, post-launch support

**Example Split:**
| Responsibility | Salesforce | Partner |
|----------------|-----------|---------|
| **Architecture design** | ✅ Lead (SA + Architect) | ⚠️ Input (validate feasibility) |
| **Project management** | ⚠️ Oversight (CSM check-ins) | ✅ Lead (partner PM) |
| **Configuration** | ❌ Not hands-on | ✅ Lead (partner consultants) |
| **Custom development** | ❌ Not hands-on | ✅ Lead (partner developers) |
| **Integrations** | ⚠️ MuleSoft architecture | ✅ Lead (partner builds connectors) |
| **Training** | ⚠️ Product training (Trailhead) | ✅ Lead (custom training for Channel Partners workflows) |
| **Go-live support** | ✅ War room participation | ✅ Lead (partner on-site) |
| **Post-launch** | ✅ CSM ongoing | ✅ Partner managed services (AMS) |

**Benefits:**
- Salesforce accountability (architecture, product roadmap)
- Partner execution speed (industry expertise, custom development)
- Channel Partners gets best of both worlds

**Recommended Partners (FSL + Retail Execution Specialists):**
- Accenture (large scale, global delivery)
- Deloitte Digital (industry depth, FSL practice)
- Simplus (mid-market FSL specialist, fast delivery)
- Persistent Systems (offshore delivery, cost-effective)
- **Ask Salesforce for:** Partner recommendations with retail field service references, similar scale (1,000+ reps)

---

## Headcount Planning: Model Future State (Not Current Silos)

### Current State Problem

**Quote (paraphrased):**
> "The team recognized the need to model organization size and structure for future state planning rather than relying on current, siloed line-of-business headcount."

**Why Current Headcount is Misleading:**
- **LOB silos:** 500 merchandising reps, 500 break-fix reps, 200 audit reps, etc.
- **Assumes dedicated roles:** Each rep locked into one tactic, can't flex across LOBs
- **Ignores efficiency gains:** Doesn't account for 15% capacity unlock from better scheduling
- **Doesn't model cross-training:** Future state has multi-tactic reps, can't map from current silos

**Example:**
- Today: Need 500 break-fix reps + 500 merchandising reps = 1,000 reps total
- Future (cross-trained): 700 multi-tactic reps can handle same workload (30% headcount reduction)
- If we model based on current silos → Over-hire by 300 reps → $15M/year wasted labor cost

---

### Future State Modeling Approach

**Bottom-Up Capacity Model:**

**Step 1: Define Work Volume (Not Headcount)**
- Merchandising: 10,000 store visits/week × 2 hours/visit = 20,000 hours/week
- Break-fix: 2,000 service calls/week × 3 hours/call = 6,000 hours/week
- Audits: 500 audits/week × 4 hours/audit = 2,000 hours/week
- Installations: 100 projects/week × 40 hours/project = 4,000 hours/week
- **Total: 32,000 hours/week**

**Step 2: Calculate Rep Capacity (With Efficiency Gains)**
- Baseline: 40 hours/week per rep × 75% utilization = 30 billable hours/week
- With FSL: 40 hours/week × 85% utilization = 34 billable hours/week (13% improvement)
- With go-back reduction: 34 billable hours × 95% first-time-fix = 32.3 effective hours/week

**Step 3: Calculate Required Headcount**
- Today (OpenSky): 32,000 hours ÷ 30 hours/rep = **1,067 reps**
- Future (FSL): 32,000 hours ÷ 32.3 hours/rep = **991 reps**
- **Savings: 76 fewer reps = $3.8M/year** (at $50K loaded cost per rep)

**Step 4: Model Cross-Training Flex**
- 20% of reps cross-trained on 2+ tactics
- Can flex 10% capacity across LOBs during demand spikes
- Reduces need for overtime: 10% × 991 reps × 4 hours OT/week × 50 weeks × $37.50/hour (1.5× rate) = **$743K/year savings**

**Total Efficiency Gain: $4.5M/year** (fewer reps + less overtime)

---

## Change Management: People > Technology

### Cultural Reality Check

**Quote (paraphrased):**
> "The team emphasized that regardless of the technology, success depends on people adopting new processes. Acknowledging previous cultural resistance to standardization, they highlighted that leadership commitment to a single, consolidated process is essential for efficiency."

**Key Insight:**
- Technology is easy (Salesforce FSL is proven, works for 1,000+ companies)
- **People are hard** (changing 4,140 reps' daily habits, getting managers to trust system instead of spreadsheets)

---

### Historical Change Resistance

**Examples:**
1. **"Have it your way" culture:** Each LOB prefers bespoke workflows, resists standardization
2. **Manager trust gap:** Managers don't trust OpenSky scheduling, revert to manual spreadsheets
3. **Regional variations:** RMS (Minnesota) operates differently, 6 original companies not fully unified post-merger
4. **Sales custom commitments:** Sales says "Yes" to every client request, operations must support custom workflows

**Result:**
- OpenSky rollout (July 6) will face same resistance
- Salesforce FSL will face same resistance
- **Technology doesn't fix culture problems**

---

### Change Management Requirements

**1. Leadership Commitment (Non-Negotiable)**

**What Leadership Must Do:**
- **CEO publicly commits:** "We are standardizing on one process, one platform. No more bespoke workflows."
- **Incentives aligned:** Manager bonuses tied to system adoption (% of scheduling done in FSL, not spreadsheets)
- **No exceptions:** If CEO says "single process," then CEO doesn't grant exceptions to favorite managers/clients
- **Model behavior:** CEO, CTO, COO use FSL dashboards in executive meetings (not spreadsheets)

**If Leadership Doesn't Commit:**
- Managers will revert to spreadsheets ("leadership doesn't really care, I'll do it my way")
- LOB teams will demand custom workflows ("we're special, need bespoke solution")
- Salesforce investment wasted (licenses bought but not used, ROI never realized)

---

**2. Front-Line Champion Network**

**Identify Champions in Each LOB/Region:**
- Merchandising champion (high-performing rep, respected by peers)
- Break-fix champion (manager with strong team relationships)
- Regional champions (California, Texas, Minnesota, etc.)

**Champion Role:**
- Attend FSL training FIRST (before general rollout)
- Provide feedback on pilot (what works, what doesn't)
- Train their peers (rep-to-rep training more credible than corporate IT training)
- Model adoption (use FSL mobile exclusively, no paper/spreadsheets)

**Champion Incentives:**
- Public recognition (CEO shout-out in all-hands)
- Financial bonus ($1K-$5K for pilot participation)
- Career advancement (champions first in line for promotions)

---

**3. Manager Accountability**

**System Adoption Metrics (Tracked Monthly):**
- % of scheduling done in FSL (vs. spreadsheets)
- % of reps actively using FSL Mobile (logins per week)
- % of time entries submitted in FSL (vs. manual/paper)
- % of surveys completed in FSL (vs. skipped/incomplete)

**Manager Scorecard:**
- >80% adoption = Green (on track for bonus)
- 60-80% adoption = Yellow (coaching required)
- <60% adoption = Red (bonus at risk, performance improvement plan)

**Consequence:**
- Managers who drive adoption: Promoted, bonuses, recognized
- Managers who resist adoption: Demoted, no bonus, eventually terminated

---

**4. Rep Training & Support**

**Multi-Modal Training (Not Just Classroom):**
- Classroom (1 day): FSL Mobile basics, survey completion, time entry
- Video (15 min each): "How to X" for common tasks (self-paced, Trailhead-style)
- On-the-job shadowing: Champion works alongside new user for first week
- Just-in-time help: Einstein Bot in mobile app ("How do I complete a survey?")

**Ongoing Support:**
- Dedicated support Slack channel (#fsl-help)
- Office hours (weekly Zoom call, ask questions)
- Regional super-users (1 per 50 reps, can answer questions on-site)

---

**5. Communication Cadence**

**Pre-Launch (2 months before):**
- CEO announcement: "Why we're doing this, what it means for you"
- Rep FAQ: "Will I lose my job? Will my pay change? Will scheduling change?"
- Manager FAQ: "How do I schedule differently? What if system doesn't work?"

**During Rollout (Weekly):**
- Wins highlights: "This week, 200 reps onboarded, 50% already love mobile app"
- Issue transparency: "This week, 3 bugs reported, 2 fixed, 1 in progress"
- Rep stories: "Hear from Sarah (merchandising rep) on how FSL saves her 30 min/day"

**Post-Launch (Monthly):**
- ROI updates: "Month 3 results: 12% utilization improvement, $500K savings"
- Feature releases: "New feature: Pre-arrival checklist reduces go-backs"
- Recognition: "Top 10 FSL power users this month (gamification)"

---

## Next Steps (Immediate Actions)

### 1. Organize Reverse Demos

**Purpose:**
- Salesforce sees Channel Partners' current workflows in action (OpenSky, Project Center, manager spreadsheets)
- Better understanding of pain points → more accurate demo scenarios

**Format:**
- Screen share of OpenSky (walk through rep scheduling, manager assignment, survey completion)
- Screen share of Project Center (construction project setup, contractor call form)
- Screen share of manager spreadsheet (manual scheduling process)
- Q&A (Salesforce asks clarifying questions)

**Attendees:**
- Channel Partners: Jay (CTO), Kari (Dev Lead), 1-2 managers (merchandising + break-fix), 1-2 reps (field perspective)
- Salesforce: AE, SA, FSL Specialist (if available)

**Duration:** 2 hours

**Deliverable:**
- Salesforce produces pain point → FSL feature mapping doc
- Prioritized list of "must have" vs. "nice to have" features

---

### 2. Schedule Field Ride-Alongs

**Purpose:**
- Salesforce (and/or partner) shadows field rep for full day
- See reality of rep's daily workflow (not just system screenshots)
- Understand environmental constraints (poor connectivity, store conditions, customer interactions)

**Locations:**
- **Irvine, CA:** Major market, likely merchandising or break-fix work
- **Dallas, TX:** Different geography, validate consistency (or regional differences)

**Format:**
- Full day (7am-5pm): Follow rep from first visit to last visit
- Observe: Mobile app usage, photo capture, parts verification, time tracking, customer interactions
- Ask questions: "Why did you do it that way? What would make this easier?"

**Attendees:**
- Channel Partners: 1 rep (merchandising), 1 rep (break-fix), 1 manager (optional, for context)
- Salesforce: SA + FSL Specialist (or partner consultant)

**Duration:** 2 full days (1 Irvine, 1 Dallas)

**Deliverable:**
- Field observations report (what works, what doesn't, FSL mobile design recommendations)
- Photos/videos of rep workflow (with permission, for demo scenario development)

---

### 3. Refine Value Story (Technical Features → Business KPIs)

**Current Gap:**
- Salesforce demos show features ("Einstein Scheduling optimizes routes!")
- Channel Partners needs to see KPI impact ("Reduces overtime 20%, saves $8M/year")

**Value Story Template:**

| Business Pain | Current Impact | FSL Capability | Quantified Benefit |
|---------------|----------------|----------------|-------------------|
| **Manual scheduling** | Managers work 10-15 hrs/week in spreadsheets | Einstein Scheduling | Save 12 hrs/week × 50 managers × $50/hr = **$1.5M/year** |
| **Go-backs** | 2.6M go-backs/year × $100 each = $260M cost | Real-time parts tracking + pre-arrival checklist | 50% reduction = **$130M/year** |
| **Overtime** | 10% OT × 4,140 reps × $5K/year = $2.1M | Capacity visibility + optimization | 20% OT reduction = **$420K/year** |
| **Client reporting** | Basic spreadsheets, risk losing renewals | Experience Cloud portals | Retain 1 major client = **$10M/year revenue** |
| **System trust gap** | Managers revert to spreadsheets, ROI not realized | Training + change management + system accuracy | Achieve 80% adoption = **Unlock all ROI above** |

**Total Annual Value: $142M+** (needs validation with actual data)

---

### 4. Establish Directional Cost Range

**Purpose:**
- Channel Partners needs budget estimate to evaluate ROI
- Not final pricing, but "order of magnitude" ($1M? $5M? $10M?)

**Cost Components:**

**1. Salesforce Licenses (Annual):**
- FSL licenses: 4,140 reps × $150/user/month × 12 months = **$7.5M/year**
- Experience Cloud (contractors/clients): 500 users × $10/user/month × 12 months = **$60K/year**
- Sales Cloud (if included): 50 users × $150/user/month × 12 months = **$90K/year**
- **Total Licenses: $7.65M/year**

**2. Implementation Services (One-Time):**
- Salesforce PSng: 1,000 hours × $250/hour = **$250K**
- Partner services: 3,000 hours × $200/hour = **$600K**
- Custom development: 500 hours × $200/hour = **$100K**
- Integrations: MuleSoft × 5 systems × $50K each = **$250K**
- Training: 4,140 reps × $500/rep (blended) = **$2M**
- **Total Implementation: $3.2M**

**3. Ongoing (Annual):**
- Salesforce support: Included in licenses
- Partner managed services (AMS): 500 hours/year × $200/hour = **$100K/year**
- **Total Ongoing: $100K/year**

**Total 3-Year TCO:**
- Licenses: $7.65M/year × 3 = **$22.95M**
- Implementation (Year 1): **$3.2M**
- Ongoing (Years 2-3): $100K × 2 = **$200K**
- **Total: $26.35M over 3 years**

**ROI Payback:**
- Annual benefit: $142M (if all ROI realized)
- Annual cost: $7.65M licenses + $100K AMS = $7.75M/year
- **ROI: 18:1** (every $1 spent returns $18)
- **Payback: 2 months** (investment recovered in 2 months)

**CRITICAL:** These are directional estimates with MANY assumptions. Needs validation:
- Actual FSL pricing (volume discounts?)
- Actual go-back reduction (50% achievable?)
- Actual adoption rate (80%? 60%?)
- Actual implementation complexity (more or less than 3,000 hours?)

---

## Summary: Keys to Success

**1. Phased Rollout (Not Big Bang)**
- Team-by-team, add functionality incrementally
- Learn from each phase, refine before next

**2. Hybrid Implementation Model**
- Salesforce architecture + accountability
- Partner execution + industry expertise

**3. Model Future State Headcount**
- Capacity-based (not silo-based)
- Account for cross-training, efficiency gains

**4. Change Management = Priority #1**
- Leadership commitment (CEO, incentives, no exceptions)
- Champion network (peer-to-peer training)
- Manager accountability (adoption metrics, bonuses tied)

**5. Immediate Next Steps**
- Reverse demos (Salesforce sees current workflows)
- Field ride-alongs (Irvine, Dallas)
- Value story refinement (features → KPIs → $$$)
- Directional cost estimate (validate ROI)

---

**End of Implementation Strategy Documentation**
