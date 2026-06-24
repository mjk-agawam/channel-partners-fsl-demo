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

## Implementation Oversight: "CTO Role" for Accountability

### Stephen's Proposal

**Quote (paraphrased):**
> "Stephen proposed a 'CTO role' as an oversight position to bridge the gap between the company, Salesforce, and the implementation partner. This individual would sit onsite, interface with Salesforce, and ensure the partner team remains accountable and efficient."

**Role Definition:**
- **Title:** Implementation Program Director (or "Embedded CTO")
- **Reporting:** Reports to Jay (Channel Partners CTO)
- **Duration:** Full-time during implementation (18 months), transition to part-time post-launch
- **Location:** Onsite at Channel Partners HQ (not remote, not partner office)

---

### Responsibilities

**1. Bridge Between Three Parties:**
- **Channel Partners:** Represents business needs, translates to technical requirements
- **Salesforce:** Interfaces with AE/SA/CSM, escalates issues, validates architecture decisions
- **Partner:** Manages day-to-day delivery, ensures quality, holds partner accountable

**Daily Activities:**
- Stand-up with partner team (remote or onsite): What shipped yesterday? What's blocked?
- Weekly check-in with Jay/Kari: Progress, risks, decisions needed
- Bi-weekly with Salesforce: Architecture review, product roadmap alignment, escalation path
- Monthly steering committee: CFO, COO, Jay, Stephen → ROI tracking, phase gate decisions

---

**2. Ensure Partner Accountability:**

**Without Oversight Role:**
- Partner says "we're on track" (but silently slipping schedule)
- Channel Partners discovers delay 2 months later (too late to course-correct)
- Partner blames Salesforce ("platform limitation"), Salesforce blames partner ("poor implementation")
- Channel Partners stuck in middle, project fails

**With Oversight Role:**
- Program Director reviews partner's daily commits (code, config, documentation)
- Spots issues early ("this integration is too fragile, refactor now")
- Escalates to partner leadership if quality slips ("your offshore team needs more FSL training")
- Provides air cover for Jay ("I'm watching partner closely, they're performing well")

---

**3. Maintain Efficiency:**

**Common Inefficiencies:**
- Partner spins wheels on wrong solution (building custom feature that FSL already has out-of-box)
- Partner waits for Channel Partners feedback (requirements unclear, waiting days for answer)
- Partner blocked on Salesforce support ticket (P3 ticket sitting in queue for weeks)

**Program Director Interventions:**
- Technical review: "Stop building custom. Use FSL OOTB feature X instead."
- Requirements clarification: "I'll get you an answer from business in 2 hours, not 2 days."
- Salesforce escalation: "Upgrade this ticket to P1, blocking go-live."

**Result:**
- Partner team 20-30% more productive (less rework, fewer blockers, faster decisions)
- Timeline compression: 18 months → 15 months (3-month savings)
- Cost savings: 3 months × partner burn rate $200K/month = **$600K saved**

---

### Ideal Candidate Profile

**Background:**
- 10+ years Salesforce implementation experience (architect-level, not just admin)
- FSL expert (deployed FSL at 3+ companies, 1,000+ users scale)
- Field service domain knowledge (ideally retail, CPG, or merchandising)
- Program/project management experience (led $5M+ implementations)

**Skills:**
- Technical: Can review Apex code, validate architecture, debug integrations
- Business: Can translate business requirements to technical specs
- Communication: Can bridge technical/non-technical stakeholders
- Leadership: Can manage without authority (influence partner, not direct reports)

**Personality:**
- **Assertive:** Comfortable challenging partner ("your approach is wrong, redo it")
- **Diplomatic:** Can escalate without burning relationships
- **Detail-oriented:** Reviews daily progress, doesn't accept "trust me, it's fine"
- **Pragmatic:** Balances perfect vs. good enough (scope control)

---

### Sourcing Options

**Option 1: Hire Full-Time Employee**
- **Pros:** Fully dedicated, builds institutional knowledge, stays post-launch
- **Cons:** Hard to find (rare skillset), expensive ($200K+ salary), may not need full-time post-launch
- **Timeline:** 2-3 months to hire (too slow for immediate start)

**Option 2: Contract Through Salesforce**
- **Pros:** Salesforce vouches for quality, fast start (2-4 weeks)
- **Cons:** Expensive ($250-$300/hour), Salesforce consultant loyalty (may favor Salesforce over Channel Partners)
- **Cost:** $250/hour × 40 hours/week × 78 weeks (18 months) = **$780K**

**Option 3: Contract Through Partner**
- **Pros:** Partner provides oversight (conflicts of interest, can't oversee themselves)
- **Cons:** Defeats purpose (can't hold partner accountable if partner paying the overseer)
- **Verdict:** ❌ Don't do this

**Option 4: Independent Consultant**
- **Pros:** Neutral third party, no conflicts, experienced with multiple partners/implementations
- **Cons:** Must vet carefully (check references, validate FSL expertise)
- **Cost:** $200/hour × 40 hours/week × 78 weeks = **$624K**

**Option 5: Fractional Consulting Firm**
- **Pros:** Bench strength (backup if primary consultant unavailable), firm reputation
- **Cons:** Slightly more expensive than independent
- **Cost:** $225/hour × 40 hours/week × 78 weeks = **$702K**

**Recommendation:** Option 4 or 5 (Independent or Fractional Firm)
- Cost-effective vs. Salesforce consultant
- No conflicts vs. Partner-provided
- Fast start vs. FTE hire
- Ask Salesforce AE for independent FSL consultant referrals

---

## Team Composition: Offshore vs. Onsite Resource Mix

### Discussion Context

**Quote (paraphrased):**
> "They explored the possibility of customizing the implementation team's makeup, specifically regarding the ratio of offshore versus onsite resources, though the feasibility of this flexibility remains uncertain."

---

### Standard Partner Team Models

**Model 1: Onsite-Heavy (Accenture, Deloitte)**
- 80% onsite (at Channel Partners HQ or partner office in US)
- 20% offshore (India, Philippines, Eastern Europe)
- **Cost:** $200-$250/hour blended rate
- **Pros:** Face-to-face collaboration, fast communication, cultural alignment
- **Cons:** Expensive, partner may have capacity constraints (limited onsite consultants available)

**Model 2: Offshore-Heavy (Persistent, Tech Mahindra, Infosys)**
- 20% onsite (architect, PM, leads)
- 80% offshore (India delivery center)
- **Cost:** $100-$150/hour blended rate
- **Pros:** Cost-effective (50% cheaper), large bench (easy to scale up/down)
- **Cons:** Time zone challenges (8-10 hour delay), communication overhead, less domain knowledge

**Model 3: Hybrid (Most Common)**
- 50% onsite, 50% offshore
- Onsite: Architect, PM, functional leads, training team
- Offshore: Developers, QA testers, configuration, documentation
- **Cost:** $150-$200/hour blended rate
- **Pros:** Balances cost and collaboration
- **Cons:** Coordination overhead (daily standups at 6am PT to catch India EOD)

---

### Channel Partners' Customization Needs

**Factors to Consider:**

**1. Complexity of Requirements:**
- High complexity (custom integrations, custom mobile components, AI features) → Need more onsite (face-to-face design sessions)
- Low complexity (OOTB FSL, standard configs) → Can use more offshore (follow documented patterns)

**2. Change Management Intensity:**
- High change management needs (train 4,140 reps, ride-alongs, go-live support) → Need onsite (in-person training, on-site go-live war room)
- Low change management (small pilot, tech-savvy users) → Can use more offshore (remote training, remote support)

**3. Timeline Pressure:**
- Fast timeline (12 months aggressive) → Need more onsite (reduce communication delays)
- Standard timeline (18-24 months) → Can use more offshore (time to iterate across time zones)

**4. Budget Constraints:**
- Limited budget ($2M implementation) → Need more offshore (cost-effective)
- Flexible budget ($5M+ implementation) → Can use more onsite (optimize for speed/quality)

---

### Recommended Mix for Channel Partners

**Phase 1: Pilot (Months 1-3)**
- **70% onsite:** Architect, PM, 2 functional leads, training lead (face-to-face with 100 pilot reps)
- **30% offshore:** 2 developers, 1 QA tester (build integrations, test)
- **Rationale:** High touch needed for pilot success, establish patterns for later phases

**Phase 2-3: Scale (Months 4-12)**
- **40% onsite:** Architect (part-time), PM, 1 functional lead (oversight, training)
- **60% offshore:** 4 developers, 2 QA testers, 2 config specialists (scale configurations, integrations)
- **Rationale:** Patterns established, offshore can execute, onsite provides direction

**Phase 4: Full Rollout (Months 13-18)**
- **50% onsite:** PM, training team (3 people), go-live support (war room)
- **50% offshore:** Developers, QA (bug fixes, enhancements)
- **Rationale:** Training intensive phase (need onsite for field training), but most build complete

---

### Negotiation Strategy

**What Partners Can Flex:**
- Ratio of onsite/offshore (within limits of their delivery model)
- Specific roles onsite (e.g., "must have architect onsite 3 days/week minimum")
- Location of onsite resources (Channel Partners HQ vs. partner office vs. remote)

**What Partners Can't Flex:**
- Total cost below their margin threshold (partners won't do unprofitable deals)
- Quality of offshore team (can't demand "only senior offshore," offshore team is mix of junior/mid/senior)
- Time zone (offshore is offshore, can't change India to US time zone)

**How to Negotiate:**

**Option A: Fixed Price with Specified Mix**
- "We'll pay $3M fixed price for 18-month implementation, but we require 50% onsite minimum."
- Partner adjusts their margin or offshore cost structure to fit
- Risk: Partner may cut corners elsewhere (fewer hours, junior staff)

**Option B: Time & Materials with Rate Card**
- Partner provides rate card: Onsite $250/hour, Offshore $125/hour
- Channel Partners decides mix: "This month we need 80% onsite (design phase), next month 20% onsite (build phase)"
- Risk: Total cost unpredictable, could overspend

**Option C: Phased with Flex (Recommended)**
- Fixed price per phase (Phase 1 = $600K, Phase 2 = $900K, etc.)
- Partner commits to minimum onsite % per phase (Phase 1 = 70%, Phase 2 = 40%)
- Channel Partners can request more onsite (pay delta: $250/hr onsite - $125/hr offshore = $125/hr premium)
- Example: Phase 2 budgeted for 40% onsite, Channel Partners wants 50% onsite → Pay $125/hr × 160 hours (10% of 1,600-hour phase) = $20K upcharge

---

## Financial Structuring: CapEx vs. OpEx

### Jay's Question

**Quote (paraphrased):**
> "Jay inquired about structuring implementation contracts to differentiate between licensing and consulting fees, aiming to optimize for capital expenditure versus operational expenditure accounting."

---

### Accounting Context

**CapEx (Capital Expenditure):**
- One-time investment in long-term asset
- Amortized over useful life (typically 3-5 years for software)
- Shows up on balance sheet (asset), not P&L (expense) in Year 1
- **CFO prefers CapEx:** Makes Year 1 P&L look better (lower expenses → higher profit)

**OpEx (Operational Expenditure):**
- Recurring expense, consumed within year
- Full cost hits P&L in year incurred
- No balance sheet impact
- **CFO prefers OpEx:** For recurring costs (licenses, support), predictable, easier to budget

---

### How Salesforce Deals Are Typically Structured

**Licenses (Almost Always OpEx):**
- Salesforce licenses are subscription (monthly or annual)
- Accounting standard: Recognize as OpEx in year consumed
- **Can't capitalize licenses** (no perpetual ownership, no asset created)
- FSL: $7.65M/year → $7.65M OpEx per year (for 3 years)

**Implementation Services (Can Be CapEx):**
- One-time consulting to configure, integrate, train
- Creates "internal-use software asset" (configured Salesforce org)
- **Can capitalize if:**
  - Creates long-term value (multi-year benefit)
  - Cost is significant ($1M+)
  - Project reaches "development stage" (not just planning/training)
- Implementation: $3.2M → $3.2M CapEx (amortized over 5 years = $640K/year expense)

**Ongoing Support/Enhancements (OpEx):**
- Annual managed services (AMS), partner retainer
- Consumed within year, no long-term asset created
- $100K/year AMS → $100K OpEx per year

---

### Optimization Strategies

**Strategy 1: Maximize CapEx (Make Year 1 P&L Look Better)**

**Structure:**
- **Capitalize:** All implementation services ($3.2M)
- **OpEx:** Licenses ($7.65M Year 1) + Ongoing ($100K Year 2+)

**Year 1 Impact:**
- P&L Expense: $7.65M (licenses) + $640K (amortization) = **$8.29M**
- Balance Sheet: $3.2M asset (implementation), amortize $640K/year over 5 years
- **Benefit:** $3.2M doesn't hit Year 1 P&L, spread over 5 years

**Year 2-5 Impact:**
- P&L Expense: $7.65M (licenses) + $640K (amortization) + $100K (AMS) = **$8.39M/year**

**When to Use:**
- Year 1 budget constrained (CFO says "can't spend more than $10M in Year 1")
- Private equity wants strong Year 1 EBITDA (for exit valuation)
- Public company wants to smooth expenses (avoid Year 1 spike)

---

**Strategy 2: Maximize OpEx (Simplify Accounting)**

**Structure:**
- **OpEx:** Everything (licenses + implementation + ongoing)
- No capitalization

**Year 1 Impact:**
- P&L Expense: $7.65M (licenses) + $3.2M (implementation) = **$10.85M**
- Balance Sheet: No asset

**Year 2-5 Impact:**
- P&L Expense: $7.65M (licenses) + $100K (AMS) = **$7.75M/year**

**When to Use:**
- CFO prefers simple (no amortization tracking, no asset impairment risk)
- Tax optimization (OpEx deductible in Year 1, CapEx deducted over 5 years → worse cash flow)
- Year 1 budget not constrained (can absorb $10.85M)

---

**Strategy 3: Hybrid (Split Implementation)**

**Structure:**
- **CapEx:** Core platform build ($2.5M - configuration, integrations, custom dev)
- **OpEx:** Training, change management, go-live support ($700K - consumed immediately, no long-term asset)
- **OpEx:** Licenses ($7.65M/year), Ongoing ($100K/year)

**Year 1 Impact:**
- P&L Expense: $7.65M (licenses) + $700K (training OpEx) + $500K (amortization) = **$8.85M**
- Balance Sheet: $2.5M asset (platform build), amortize $500K/year over 5 years

**Rationale:**
- Training/change management doesn't create "asset" (can't resell trained employees)
- Platform build does create asset (configured Salesforce org has multi-year value)
- Most conservative approach (auditor-friendly)

---

### How to Structure Contract

**Separate Line Items in SOW:**

```
STATEMENT OF WORK - CHANNEL PARTNERS FSL IMPLEMENTATION

1. Salesforce Licenses (OpEx)
   - FSL Licenses (4,140 users): $7,452,000/year
   - Experience Cloud (500 users): $60,000/year
   - Sales Cloud (50 users): $90,000/year
   - Subtotal: $7,602,000/year (billed annually, 3-year commit)

2. Implementation Services - Platform Build (CapEx-Eligible)
   - Architecture & Design: $200,000
   - Configuration & Development: $800,000
   - Integration Development: $500,000
   - Data Migration: $200,000
   - Testing & QA: $300,000
   - Subtotal: $2,000,000 (one-time, capitalize over 5 years)

3. Implementation Services - Training & Change Mgmt (OpEx)
   - Training Curriculum Development: $300,000
   - Rep Training Delivery: $800,000
   - Change Management: $400,000
   - Go-Live Support: $200,000
   - Subtotal: $1,700,000 (one-time, OpEx in Year 1)

4. Ongoing Support (OpEx)
   - Partner Managed Services (AMS): $100,000/year (Years 2-3)

TOTAL 3-YEAR COST: $26,702,000
- Year 1: $7,602,000 (licenses) + $2,000,000 (platform CapEx) + $1,700,000 (training OpEx) = $11,302,000
- Year 2: $7,602,000 (licenses) + $100,000 (AMS) = $7,702,000
- Year 3: $7,602,000 (licenses) + $100,000 (AMS) = $7,702,000
```

**Accounting Treatment:**
- Year 1 P&L: $7,602,000 + $1,700,000 + $400,000 (CapEx amortization) = **$9,702,000**
- Balance Sheet: $2,000,000 asset, depreciate $400K/year

---

### Tax Considerations

**Section 174 R&D Capitalization (US Tax Law Change):**
- Effective 2022+, software development costs must be capitalized for tax purposes (can't deduct immediately)
- Amortized over 5 years (US) or 15 years (offshore development)
- **Impact:** Even if Channel Partners wants to OpEx for book accounting, IRS requires CapEx for tax
- **Result:** May create book/tax difference (OpEx on P&L, CapEx on tax return)
- **Recommendation:** Consult Channel Partners' tax advisor, may prefer CapEx for both (simplifies)

---

## AI Initiative: Pre-Purchase Use Case Workshop

### Stephen's Proposal

**Quote (paraphrased):**
> "Stephen suggested a week-long program where specialized staff could work onsite to help identify and develop AI use cases, which is an option available even prior to a formal software purchase."

---

### Workshop Structure

**Format:**
- **Duration:** 1 week (5 days)
- **Location:** Channel Partners HQ (onsite, not remote)
- **Team:** Salesforce AI specialists (Einstein experts, FSL + AI hybrid)
- **Deliverable:** AI use case roadmap with prioritized recommendations

---

**Day 1: Discovery**
- Meet with key stakeholders (Jay, Kari, Stephen, LOB managers, reps)
- Understand current pain points (go-backs, scheduling, quality control, support center)
- Review existing data (OpenSky database, Snowflake warehouse, survey photos, time entries)
- Identify AI opportunities (where can ML/AI add value?)

**Day 2: Use Case Brainstorming**
- Workshop with cross-functional team (ops, IT, finance, reps)
- Generate 20-30 potential AI use cases
- Examples:
  - Einstein Vision: Auto-QC for photo surveys
  - Einstein Bot: Knowledge base chatbot
  - Einstein Scheduling: Predictive go-back risk scoring
  - Einstein Analytics: Margin forecasting by project type
  - Einstein Discovery: Root cause analysis for overtime spikes

**Day 3: Use Case Prioritization**
- Score each use case on:
  - **Business impact:** High (>$10M/year), Medium ($1M-$10M), Low (<$1M)
  - **Technical feasibility:** Easy (OOTB Einstein), Medium (custom model), Hard (new AI tech)
  - **Data readiness:** Ready (data exists, clean), Partial (data exists, needs cleanup), Not ready (data doesn't exist)
  - **Time to value:** Quick (<6 months), Medium (6-12 months), Long (12+ months)
- Prioritization matrix: High impact + Easy + Ready + Quick = **Priority 1**

**Day 4: Proof of Concept (POC) Planning**
- Select top 2-3 use cases for POC
- Define success criteria (e.g., Einstein Vision must achieve >85% accuracy on QC pass/fail)
- Identify data requirements (e.g., need 1,000 labeled "good" and "bad" installation photos)
- Outline POC timeline (e.g., 8 weeks: 2 weeks data prep, 4 weeks model training, 2 weeks testing)

**Day 5: Roadmap & Next Steps**
- Present findings to executive team (CEO, CFO, CTO, COO)
- Recommended roadmap:
  - **Phase 1 (Months 1-6):** POC for Priority 1 use cases
  - **Phase 2 (Months 7-12):** Production rollout of successful POCs
  - **Phase 3 (Year 2):** Expand to Priority 2 use cases
- Decision point: Proceed with POC? (Can do POC without buying FSL licenses)

---

### Benefits of Pre-Purchase Workshop

**1. Validate AI Value Before Buying:**
- Salesforce claims Einstein can save $13M/year (automated QC)
- Workshop validates: Do we have right data? Is accuracy achievable? Will reps use it?
- **Outcome:** High confidence in AI ROI → Easier to justify FSL purchase

**2. No Long-Term Commitment:**
- Workshop is standalone engagement (not tied to FSL purchase)
- If workshop reveals AI won't work (bad data, low accuracy, cultural barriers) → Don't buy FSL, save $26M
- Low cost to de-risk large investment

**3. Build Internal Buy-In:**
- Reps, managers see AI in action (real photos, real predictions)
- Not just "Salesforce says AI will help," it's "We tested AI on our data, here's proof"
- Accelerates adoption (people trust what they've seen)

**4. Identify Quick Wins:**
- Some AI use cases can launch in 3-6 months (Einstein Bot, Einstein Analytics dashboards)
- Can deliver ROI BEFORE full FSL rollout completes (18 months)
- Early wins build momentum for broader FSL adoption

---

### Workshop Cost

**Typical Pricing:**
- **Salesforce AI Workshop:** $50K-$100K (1 week, 2-3 specialists onsite)
- **Included in FSL Deal:** Often Salesforce AE includes free/discounted workshop to win deal
- **Standalone:** If Channel Partners wants workshop before committing to FSL, pay full price

**Negotiation Strategy:**
- Request free workshop as part of FSL evaluation ("We need to validate AI use cases before committing to $26M investment")
- Salesforce AE likely agrees (small cost to Salesforce, high value to close deal)
- Worst case: Pay $50K, get $13M+ ROI insight (0.4% of total deal size, worth it)

---

### Recommended Timing

**Option 1: Workshop First, Then FSL Decision (Lower Risk)**
1. Week 1: AI workshop
2. Weeks 2-4: POC for top use case (e.g., Einstein Vision QC)
3. Week 5: Present POC results to exec team
4. Week 6: Decide: Proceed with FSL? (Yes if POC successful)

**Option 2: Workshop During FSL Evaluation (Parallel Track)**
1. Month 1: Reverse demo + field ride-alongs + AI workshop (all in parallel)
2. Month 2: Salesforce delivers value story + POC results + cost estimate
3. Month 3: Channel Partners decides: Proceed with FSL implementation?

**Option 3: Workshop After FSL Commitment (Highest Risk)**
1. Month 1: Commit to FSL implementation ($26M, 18 months)
2. Month 2: AI workshop (discover data quality issues, low accuracy potential)
3. Month 3: Realize AI ROI won't materialize → $13M of projected ROI disappears
4. Problem: Already committed to FSL, can't back out

**Recommendation:** Option 1 or 2 (de-risk AI assumptions before full commitment)

---

**End of Implementation Strategy Documentation (Updated)**


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
