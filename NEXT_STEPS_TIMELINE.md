# Next Steps & Timeline

**Last Updated:** June 24, 2026  
**Source:** Architecture session wrap-up discussion

---

## Immediate Actions (Next 2 Weeks)

### 1. Field Ride-Alongs

**Timing:** Week after next (tentative)

**Locations:**
- **Irvine, CA:** Merchandising or break-fix rep (1 full day)
- **Dallas, TX:** Different LOB or geography validation (1 full day)

**Purpose:**
- Salesforce (and/or partner) shadows field rep for full workday
- Observe real workflows, environmental constraints, customer interactions
- See mobile app usage, photo capture, parts verification, time tracking
- Understand pain points firsthand (not just system screenshots)

**Attendees:**
- **Channel Partners:** 1 merchandising rep (Irvine), 1 break-fix rep (Dallas), optional manager for context
- **Salesforce:** Solution Architect + FSL Specialist (or partner consultant if identified)

**Deliverable:**
- Field observations report with photos/videos (with permission)
- FSL mobile design recommendations based on real rep workflows
- Pain point prioritization (what hurts most in daily work?)

---

### 2. Reverse Demo 2.0

**Timing:** Wednesday (specific date TBD)

**Purpose:**
- Channel Partners demonstrates current workflows to Salesforce
- Salesforce sees OpenSky, Project Center, manager spreadsheets in action
- Better understanding of pain points → More accurate FSL demo scenarios

**Format:**
- Screen share of OpenSky (rep scheduling, manager assignment, survey completion)
- Screen share of Project Center (construction project setup, contractor call form)
- Screen share of manager spreadsheet (manual scheduling process)
- Q&A (Salesforce asks clarifying questions)

**Attendees:**
- **Channel Partners:** Jay (CTO), Kari (Dev Lead), 1-2 managers (merchandising + break-fix), 1-2 reps (field perspective)
- **Salesforce:** AE, SA, FSL Specialist (if available)

**Duration:** 2 hours

**Deliverable:**
- Salesforce produces pain point → FSL feature mapping document
- Prioritized list of "must have" vs. "nice to have" features

---

### 3. Leadership Alignment on Value Story

**Timing:** Before Reverse Demo 2.0 (this week or early next week)

**Purpose:**
> "The team focused on ensuring leadership alignment on the 'value story' and KPIs before the session."

**What Needs Alignment:**

**1. Define Success Metrics (KPIs):**
- Which KPIs matter most to CEO, CFO, COO?
- Examples:
  - Resource utilization (target: 85% billable hours)
  - Go-back rate (target: <5%)
  - Overtime (target: <5% of total hours)
  - Client satisfaction (target: NPS >50)
  - Rep retention (target: <15% annual turnover)

**2. Prioritize Pain Points:**
- What hurts most? (Scheduling bottleneck? Go-backs? Client reporting? KPI trust gap?)
- What's most urgent? (RMS integration? Cross-LOB optimization? AI QC?)
- What's most valuable? ($130M go-back reduction? $32M capacity unlock? $10M client retention?)

**3. Agree on ROI Targets:**
- What ROI is required to justify $26M investment?
- 10:1? 15:1? 20:1?
- What payback period is acceptable? (6 months? 12 months? 18 months?)

**4. Align on Change Management Reality:**
> "Participants reiterated that technical implementation is secondary to user adoption. They acknowledged that successful digital transformation requires cultural shifts, as the technology will fail if the team resists standardized processes or continues to rely on legacy manual workflows."

**Key Questions for Leadership:**
- Are we committed to single standardized process? (No more "have it your way" culture?)
- Will we hold managers accountable for system adoption? (Bonuses tied to FSL usage?)
- Are we willing to say "No" to client custom requests that hurt our KPIs?
- Will CEO publicly champion this change? (All-hands announcement, model behavior?)

---

**Meeting Format:**
- 90-minute executive session (no Salesforce, internal only)
- Attendees: CEO, CFO, COO, CTO (Jay), Stephen
- Facilitator: Stephen (as Salesforce sponsor)
- Output: One-page "Value Story" document with agreed KPIs, prioritized pain points, ROI targets, change management commitments

---

## Short-Term Actions (Weeks 3-4)

### 4. AI Use Case Workshop (Optional)

**Timing:** After field ride-alongs, before FSL decision

**Purpose:**
- Validate AI use cases with Salesforce specialists
- Identify top 2-3 use cases for POC
- De-risk AI assumptions before $26M commitment

**Format:**
- 1 week onsite at Channel Partners HQ
- Salesforce AI specialists (Einstein experts, FSL + AI hybrid)
- Day 1: Discovery (stakeholder interviews, data review)
- Day 2: Use case brainstorming (20-30 potential use cases)
- Day 3: Prioritization (score on impact, feasibility, data readiness, time to value)
- Day 4: POC planning (top 2-3 use cases, define success criteria, data requirements)
- Day 5: Roadmap presentation (exec team, decision: proceed with POC?)

**Deliverable:**
- Prioritized AI use case roadmap
- POC plan for top 2-3 use cases (Einstein Vision QC, Einstein GPT Lead Scoring, etc.)
- Data requirements (how many labeled images, call transcripts, etc. needed?)

**Cost:** $50K-100K (negotiate free/discounted as part of FSL evaluation)

---

### 5. Start Data Foundation (Immediately)

**Purpose:**
> "Stephen emphasized the importance of immediately beginning to capture high-quality data and images to establish a historical baseline that will be critical for training and deploying future AI models."

**Actions Starting This Week:**

**1. Display Photos (For Einstein Vision QC):**
- Update OpenSky survey instructions: "Photo requirements: wide-angle, well-lit, 1920×1080 minimum"
- Train reps on consistent photo capture (10-minute video, Trailhead-style)
- Goal: 5,000+ high-quality photos by Month 6 (ready for AI model training)

**2. Go-Back Reasons (For Predictive Model):**
- Add required field to OpenSky survey: "Go-Back Reason" (dropdown)
- Options: Parts not delivered, Store closed early, Customer refused access, Quality issue, Other
- Free-text notes: "Additional details"
- Goal: 6 months of go-back data (identify patterns, train predictive model)

**3. Lead Call Recordings (For Einstein GPT Lead Scoring):**
- Enable call recording for all sales reps (Zoom, Teams, phone system)
- Store recordings in cloud (Google Drive, OneDrive, or Salesforce Files)
- Transcript calls (Otter.ai, Rev.com, or Zoom built-in)
- Goal: 500+ transcribed sales calls by Month 6 (train lead scoring model)

**4. Baseline Metrics Dashboard:**
- Create dashboard in OpenSky (or Tableau) showing 8 key metrics:
  - Go-back rate, Overtime hours, Manager scheduling time, Rep utilization, Client NPS, Photo QC pass rate, Lead response time, Mobile app usage
- Capture weekly starting this week
- Goal: 6 months of baseline data (prove Salesforce ROI post-implementation)

---

### 6. Partner Selection (If Hybrid Model Chosen)

**Timing:** Weeks 3-4 (after Reverse Demo 2.0, before final decision)

**Purpose:**
- Identify 2-3 FSL implementation partners for evaluation
- Request proposals, check references, compare cost/approach

**Process:**

**Step 1: Get Partner Recommendations (From Salesforce AE)**
- Request: "FSL partners with retail field service experience, 1,000+ rep deployments, US-based"
- Salesforce provides: 3-5 partner names with profiles

**Step 2: RFI (Request for Information)**
- Send to 3 partners: Project scope, timeline, team size, budget range
- Partners respond: Approach, team composition, cost estimate, references

**Step 3: Partner Interviews**
- 2-hour video call with each partner
- Meet: Partner exec, FSL practice lead, proposed architect
- Ask: Similar projects, team composition (onsite/offshore mix), change management approach, post-launch support model

**Step 4: Reference Checks**
- Call 2-3 references per partner (companies that deployed FSL with this partner)
- Ask: Did they deliver on time/budget? Quality of work? Would you hire them again?

**Step 5: Partner Selection**
- Score each partner: Industry experience (30%), cost (25%), team quality (25%), references (20%)
- Select top partner, negotiate SOW

---

## Medium-Term Actions (Months 2-3)

### 7. Finalize Value Story & Cost Estimate

**Timing:** Month 2 (after field ride-alongs, Reverse Demo 2.0, AI workshop if done)

**Purpose:**
- Refine ROI model with validated assumptions (not hypothesis)
- Present final value story to executive team for decision

**Components:**

**1. Value Story Document (10-15 pages):**
- Executive summary (1 page): ROI, payback, timeline
- Business pain points (2 pages): Scheduling bottleneck, go-backs, KPI trust gap, client reporting
- FSL capabilities (3 pages): How FSL solves each pain point
- ROI model (2 pages): Cost vs. benefit over 3 years, sensitivity analysis
- Implementation approach (2 pages): Phased rollout, change management, partner selection
- Risk mitigation (1 page): What could go wrong, how to mitigate
- Next steps (1 page): Timeline, decision gates, resource requirements

**2. Cost Estimate (Refined from Directional):**
- Licenses: Validate with Salesforce AE (volume discounts? multi-year commit discounts?)
- Implementation: Partner proposal (actual cost, not estimate)
- Ongoing: AMS cost, Salesforce support (included?), MuleSoft licenses (if needed)
- Contingency: 10-20% buffer for unknowns

**3. Executive Decision Meeting:**
- Present value story + cost estimate to CEO, CFO, COO, Board (if PE-backed)
- Decision: Proceed with FSL implementation? (Go/No-Go)
- If Go: Commit budget, sign Salesforce contract, kick off implementation

---

### 8. Begin Implementation (If Approved)

**Timing:** Month 3 (if decision made in Month 2)

**Phase 1 Kickoff:**
- Sign Salesforce contract (licenses + professional services)
- Sign partner contract (if hybrid model chosen)
- Hire/contract Program Director ("CTO role" for oversight)
- Identify pilot team (100 reps, single LOB, single geography)
- Schedule Phase 1 kickoff meeting (Salesforce + Partner + Channel Partners)

---

## Change Management: Non-Negotiables

**Quote (paraphrased):**
> "Participants reiterated that technical implementation is secondary to user adoption. They acknowledged that successful digital transformation requires cultural shifts, as the technology will fail if the team resists standardized processes or continues to rely on legacy manual workflows."

---

### Cultural Shift Requirements

**1. Leadership Public Commitment:**
- **CEO all-hands announcement:** "We are standardizing on one process, one platform. This is not optional."
- **Incentives aligned:** Manager bonuses tied to FSL adoption (% of scheduling done in FSL, not spreadsheets)
- **No exceptions:** If CEO grants exception to one manager ("you can keep using spreadsheets"), entire change effort collapses

**2. Accountability Metrics:**
- Track FSL adoption weekly: % scheduling in FSL, % reps using mobile, % surveys completed in FSL
- Manager scorecard: >80% adoption = Green (bonus), 60-80% = Yellow (coaching), <60% = Red (performance plan)
- Rep scorecard: Active FSL Mobile usage (logins per week), survey completion rate, photo quality

**3. Champion Network:**
- Identify 10-20 champions (1 per 200 reps): High-performing reps/managers, respected by peers
- Champions attend FSL training FIRST (before general rollout)
- Champions train their peers (peer-to-peer training more credible than corporate IT)
- Champions publicly model adoption (use FSL exclusively, no spreadsheets, share success stories)

**4. Manager Training (Not Just Rep Training):**
- Managers are biggest change barrier (revert to spreadsheets because "system doesn't work")
- Dedicate 2× training time for managers vs. reps (managers need to trust system, understand why it's better)
- Manager-specific use cases: "How to schedule 5-person crew in FSL," "How to handle emergency dispatch," "How to see rep capacity across projects"

**5. Communication Cadence:**
- **Pre-launch (2 months before):** CEO announcement, rep FAQ, manager FAQ
- **During rollout (weekly):** Wins highlights, issue transparency, rep success stories
- **Post-launch (monthly):** ROI updates, feature releases, top FSL power users recognition (gamification)

---

### What Happens If Cultural Shift Fails

**Scenario: Technology Succeeds, People Fail**

**Month 6 Post-Launch:**
- FSL deployed to 500 reps (Phase 1 + Phase 2)
- Technology works (no major outages, mobile app stable, integrations functioning)
- BUT: Only 40% of managers using FSL scheduling (60% still using spreadsheets)
- Reps follow managers' lead (use mobile app minimally, complain it's "extra work")

**Month 12:**
- ROI not realized ($32M capacity unlock never happens because managers not optimizing in system)
- Go-back rate unchanged (10% still, because pre-arrival checklist bypassed by reps)
- Client satisfaction unchanged (still sending basic spreadsheets, not using Experience Cloud portals)
- Executive team frustrated: "We spent $26M and nothing changed"

**Outcome:**
- Salesforce blamed ("system doesn't work")
- Partner blamed ("bad implementation")
- **Reality:** Technology works fine, but people didn't change behavior
- **Result:** FSL abandoned, revert to OpenSky, $26M wasted

---

### How to Prevent This

**1. Leadership Holds Line:**
- Manager reverts to spreadsheets → Performance improvement plan (not "it's okay, use what works for you")
- Rep refuses to use mobile app → Coaching, then termination if no improvement (not "we'll try harder to train them")
- Sales team continues "have it your way" custom deals → CEO says "No" publicly (model behavior change)

**2. Early Warning System:**
- Weekly adoption metrics reviewed by CEO, CFO, COO, CTO
- Red flags raised immediately: "Phase 1 manager X only 30% FSL usage after 4 weeks, action needed now"
- Intervention: CEO calls manager X directly, reiterates commitment, offers support but demands compliance

**3. Celebrate Wins Loudly:**
- Champion success stories shared in all-hands meetings, Slack channels, email newsletters
- Example: "Manager Sarah's team 95% FSL adoption, reduced overtime 18% in 8 weeks, $50K savings"
- Peer pressure works: Other managers see Sarah's success, want same recognition

**4. Tie to Business Results:**
- Don't just track FSL adoption (lagging indicator)
- Track business outcomes (leading indicator): Go-back rate, overtime, client NPS, rep retention
- Show causation: "Teams with >80% FSL adoption have 30% lower go-back rate than <60% adoption teams"
- Managers see: "FSL adoption = better business results = my bonus increases"

---

## Summary Timeline

| Timeframe | Action | Owner | Deliverable |
|-----------|--------|-------|-------------|
| **This Week** | Leadership alignment on value story/KPIs | Stephen + Jay | One-page Value Story doc |
| **This Week** | Start data foundation (photos, go-backs, baselines) | Kari | Updated OpenSky surveys, baseline dashboard |
| **Week After Next** | Field ride-alongs (Irvine, Dallas) | Salesforce SA | Field observations report |
| **Week After Next** | Reverse Demo 2.0 | Jay + Kari | Pain point → FSL feature mapping |
| **Weeks 3-4** | AI Use Case Workshop (optional) | Salesforce AI team | Prioritized AI roadmap, POC plan |
| **Weeks 3-4** | Partner selection (if hybrid model) | Jay + Stephen | Partner SOW signed |
| **Month 2** | Finalize value story & cost estimate | Salesforce AE | Executive decision-ready package |
| **Month 2** | Executive decision meeting | CEO + CFO + COO | Go/No-Go decision |
| **Month 3** | Phase 1 kickoff (if approved) | Program Director | Pilot team identified, kickoff meeting scheduled |

---

**End of Next Steps & Timeline Documentation**
