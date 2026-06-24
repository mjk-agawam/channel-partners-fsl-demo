# Business Performance Assessment - Functional Area Ratings

**Last Updated:** June 24, 2026  
**Source:** Architecture session - Stephen's performance assessment exercise  
**Context:** Team rating effectiveness of different business functions on 1-10 scale

---

## Assessment Methodology

**Stephen initiated a structured assessment** asking the team to rate various business functions on a scale of 1 to 10, where:
- **1-3:** Significant dysfunction, major gaps
- **4-6:** Functional but needs improvement
- **7-8:** Working well, minor gaps
- **9-10:** Best-in-class, competitive advantage

---

## Marketing Effectiveness: 3/10

**Rating:** 3 out of 10 (consensus after discussion)

### Jay's "Loaded Question" Response

Jay described marketing effectiveness as a "loaded question" because **marketing challenges are symptoms of deeper systemic resource optimization issues**, not marketing team failures.

---

## Root Causes (Jay's Analysis)

### 1. Lead Generation Misses Due to Capacity Constraints

**Problem:**
- Opportunities for new business exist (inbound leads, referrals, market expansion)
- Team **lacks bandwidth to pursue them** because resources already constrained
- Large client projects (Target 1,900 stores/week, Samsung/LG installations) consume all available capacity
- Can't scale to take on new work without hiring more reps

**Quote (paraphrased):**
> "While opportunities for lead generation exist, the team often lacks the bandwidth to pursue them because resources are already constrained by large client projects and scheduling is inefficient."

**Impact:**
- Lost revenue (opportunities not pursued)
- Inability to grow beyond existing client base
- Competitive disadvantage (competitors can scale faster)

---

### 2. Unbalanced Resource Ratio (Full-Time vs. Part-Time vs. Floater)

**Problem:**
- Current ratio of **full-time to floating resources is not correctly sized**
- Too many full-time employees sitting idle during slow periods?
- OR too few full-time employees, causing over-reliance on part-time staff?
- No clear definition of "floating" vs. "part-time" vs. "full-time"

**Resource Segmentation Confusion:**
- **Full-time W-2:** Dedicated employees (40+ hours/week)
- **Part-time W-2:** Regular employees (10-30 hours/week, retained, reliable)
- **Floaters/Gig Workers:** On-demand labor (1-5 hours/week, unreliable availability)

**Current State:**
- Treating all "part-time" staff as interchangeable (they are NOT)
- Reliable part-timers should be treated more like full-time (dedicated, trained, predictable)
- True gig workers/floaters should be used only for overflow/peak demand

---

### 3. Over-Reliance on "Part-Timers" as Generic Bucket

**Problem:**
- Part-time staff treated as **"over-abused" generic bucket**
- No distinction between:
  - **Reliable, retained part-timers** (15-30 hours/week, trained, loyal, long-tenure)
  - **True gig workers/floaters** (5-10 hours/week, untrained, transient, no loyalty)

**Impact:**
- Reliable part-timers feel undervalued (treated same as gig workers)
- Scheduling assumes all part-timers are interchangeable (they are NOT)
- Quality issues when gig workers assigned to complex work
- Higher training costs (gig workers churn, must retrain constantly)

**Salesforce Opportunity:**
- **Service Resource Types** to distinguish Full-Time, Part-Time Retained, Floater/Gig
- **Skills-Based Routing** to prioritize reliable part-timers over gig workers
- **Einstein Scheduling** to optimize mix of resource types by project complexity

---

### 4. Lack of Cross-Training (Tactics Locked to Specific Skills)

**Problem:**
- Staff are **locked into specific "tactics"** (merchandising, break/fix, audits, installations)
- Cannot optimize availability or flexibility when assigning work
- Rep with 10 hours free this week CAN'T be assigned to different work type (not trained)
- Must hire new reps to scale new service lines (can't redeploy existing reps)

**Example:**
- Merchandising rep has slow week (only 20 hours scheduled, 20 hours idle)
- Break/fix work available in same geography (need 20 more hours of coverage)
- **Rep can't help** because not trained on break/fix
- Company pays overtime to break/fix reps while merchandising reps sit idle

**Ties to Earlier Discussion:**
- **Cross-functional resource model** (moving from dedicated break/fix teams to multi-tactic reps)
- Organizational resistance (reps/managers prefer dedicated teams)
- Skills/training gap (merch rep doesn't know how to troubleshoot displays)
- Billing complexity (how to allocate time across work types)

**Salesforce Opportunity:**
- **Multi-Skills on Service Resources** (rep can have: Merchandising + Break/Fix + Audits)
- **Skills-Based Routing** to match work to reps with required skills
- **Training Management** (LearnUpon integration OR Trailhead) to track certifications
- **Incentive Management** (bonus for handling multiple work types)

---

## Impact on Marketing Effectiveness

**Why these resource issues tank marketing effectiveness:**

1. **Can't scale to pursue leads:**
   - Sales team brings in new opportunity (new brand client, new retailer)
   - Operations says "we don't have capacity"
   - Lead dies, competitor wins deal

2. **Can't staff proof-of-concept projects:**
   - Prospect wants pilot project (10 stores, 2-week test)
   - Operations can't free up 5 reps for 2 weeks (all booked on existing clients)
   - Prospect goes with competitor who can staff immediately

3. **Can't offer new services:**
   - Market demand for new service line (e.g., EV charger installations, smart home device setup)
   - Would require training existing reps OR hiring new specialized reps
   - Company can't invest in training (reps already fully utilized)
   - Opportunity lost

4. **Inefficient pricing:**
   - Scheduling inefficiencies drive up labor costs (overtime, excess mileage)
   - Must price projects higher to maintain margins
   - Lose deals on price vs. competitors with better scheduling

---

## Salesforce FSL Positioning

**Key Message:**
> "You rated marketing 3/10, but the real issue is resource optimization. Salesforce FSL's intelligent scheduling, skills-based routing, and multi-tactic workforce management unlock 15-20% more capacity WITHOUT hiring. That's your growth engine."

**ROI Calculation:**
- 4,140 reps × 40 hours/week × 52 weeks = 8.6M labor hours/year
- 15% efficiency gain = 1.3M freed hours/year
- At $25/hour billing rate = **$32M additional revenue capacity**
- At 20% margin = **$6.4M/year incremental profit**

**Proof Points to Validate:**
1. What % of rep hours are idle today? (Target, Best Buy slow weeks, seasonal dips)
2. What % of overtime is "avoidable"? (Better scheduling could eliminate it)
3. How many leads were declined in last 12 months due to capacity? (Revenue left on table)
4. What's average drive time per rep per day? (Route optimization opportunity)
5. What % of reps are cross-trained on 2+ tactics today? (Baseline for cross-functional model)

---

---

## Sales and Contracting: 5/10

**Rating:** 5 out of 10

### Root Causes

#### Heavy People-Driven Process (Not Systemic)

**Problem:**
- Sales and contracting relies on individual relationships, tribal knowledge, manual handoffs
- No structured CRM or opportunity management system
- Contract terms not standardized (every deal is bespoke)
- Lack of cohesive "glue" to connect sales → contracting → project setup

**Quote (paraphrased):**
> "The process is heavily people-driven rather than systemic, largely manual and lacks a cohesive 'glue' to connect various processes."

**Impact:**
- Long sales cycles (manual proposal generation, custom contract negotiation)
- Inconsistent pricing (no CPQ, sales reps price deals based on intuition)
- Revenue leakage (custom terms not captured in systems, billing misses)
- Handoff failures (sales promises something operations can't deliver)

**Salesforce Opportunity:**
- **Sales Cloud** for opportunity management, pipeline visibility, forecasting
- **CPQ (Configure, Price, Quote)** for standardized pricing, automated proposal generation
- **Contract Lifecycle Management** for standardized contract templates, approval workflows
- **Slack integration** for sales → operations handoff (opportunity alert → project kickoff)

---

## Project Kickoff and Initiation: 5/10

**Rating:** 5 out of 10

### Root Causes

#### Fragmented System Landscape

**Problem:**
- Multiple systems involved in project setup: OpenSky, Project Center (WMS), homegrown tools
- No single source of truth for project definition
- Manual data entry across systems (Call Form in OpenSky, then parts order in Project Center, then...)

**Systems Involved:**
1. OpenSky (Call Form/Wave setup)
2. Project Center WMS (parts/materials if needed)
3. LearnUpon LMS (training assignment if required)
4. Business Central (job costing setup)
5. Homegrown tools (custom workflows for specific clients)

**Quote (paraphrased):**
> "Rated a 5 out of 10 due to the fragmented system landscape (including Open Sky, Project Center, and homegrown tools)."

---

#### Custom Client Requirements Without Standardized Provisioning

**Problem:**
- Sales agrees to custom client requirements (bespoke survey questions, custom reporting, unique workflow)
- **No standardized provisioning process** to implement these customizations
- Operations scrambles to build custom solution after contract signed
- Procurement and setup delays (must order special parts, build new survey, train reps on unique workflow)

**Example Scenario:**
1. Sales closes deal with new brand client (Samsung wants custom display audit process)
2. Contract includes 47 custom survey questions + photo requirements + parts ordering workflow
3. Operations receives contract AFTER signature
4. Must build custom Call Form, train reps, order parts, set up reporting
5. **2-4 week delay** before project can start
6. Client frustrated (expected immediate start after contract signed)

**Impact:**
- Project start delays (revenue recognition delayed)
- Rushed implementations (quality suffers, errors increase)
- Rep frustration (assigned to project without proper training)
- Client dissatisfaction (delays, quality issues)

**Salesforce Opportunity:**
- **Project Templates** (reusable Work Order templates for common project types)
- **Product Catalog + CPQ** (standardized service offerings, custom options priced and provisioned automatically)
- **Flow Automation** (contract signed → auto-create project → auto-assign resources → auto-trigger training)
- **Configuration Management** (custom client requirements tracked as metadata, provisioned via clicks not code)

---

## Execution and Scheduling: BOTTLENECK

**Rating:** Not explicitly rated, but identified as **core bottleneck**

### Root Causes

#### Managers Rely on Manual "Spreadsheet Magic"

**Problem:**
- OpenSky HAS scheduling capabilities (self-scheduling, buckets, matching logic)
- **Managers don't trust system recommendations**
- Revert to manual scheduling using spreadsheets
- Assign work based on **personal relationships with field reps** rather than system-generated matches

**Quote (paraphrased):**
> "Although Open Sky possesses scheduling capabilities, managers frequently rely on manual 'spreadsheet magic' to assign work based on personal relationships with field representatives rather than trusting system-generated recommendations."

**Why Managers Don't Trust OpenSky:**
1. **System recommendations don't match reality** (suggests rep who is actually unavailable, on vacation, working other project)
2. **No real-time capacity visibility** (system shows rep available, but manager knows rep is fully booked)
3. **Skills/certifications not accurate** (system says rep trained on break/fix, but manager knows rep hasn't done break/fix in 6 months)
4. **Personal knowledge of rep preferences** (manager knows rep prefers certain stores, certain work types, certain days)

**Impact:**
- Scheduling takes hours/days instead of minutes
- Managers work nights/weekends to manually schedule
- Suboptimal assignments (manager picks "favorite" rep, not best-fit rep)
- Rep burnout (high performers get overloaded because managers always pick them)
- Underutilization (low performers sit idle because managers avoid assigning them work)

---

#### Lack of System-Captured Capacity Data

**Problem:**
- **Employee availability NOT captured in OpenSky**
- No vacation calendar, no PTO tracking, no "I'm available 20 hours this week" input
- Managers must manually track availability in spreadsheets, mental models, Slack DMs

**Quote (paraphrased):**
> "The lack of system-captured capacity data (employee availability) forces managers to perform manual scheduling, often outside of work hours."

**What's Missing:**
1. **PTO/Vacation Calendar:** Rep takes vacation, doesn't block calendar in OpenSky
2. **Availability Preferences:** Part-time rep wants 15 hours/week, system doesn't know
3. **Multi-Project Conflicts:** Rep assigned to 2 projects simultaneously, neither manager sees the conflict
4. **Real-Time Status:** Rep calls out sick, manager doesn't see updated availability in system
5. **Skills Currency:** Rep trained 6 months ago, hasn't used skill since (rusty, but system shows "certified")

**Impact:**
- Double-booking (rep assigned to 2 projects same day)
- No-shows (rep on vacation, manager didn't know)
- Overwork (rep assigned 60 hours when they wanted 20)
- Underutilization (rep available 40 hours, only assigned 15)

**Salesforce Opportunity:**
- **Service Resource Capacity** (PTO, vacation, availability preferences in FSL)
- **Resource Absences** (sick days, emergencies automatically update availability)
- **Multi-Work Order Visibility** (see all assignments across all projects for a rep)
- **Real-Time Status** (mobile app: "I'm running late", "I'm available for emergency dispatch")

---

#### Prevents Cross-Training and Multi-Tactic Optimization

**Problem:**
- Manual scheduling based on personal relationships reinforces LOB silos
- Manager only assigns merchandising work to "my merchandising reps"
- Never considers assigning break/fix work to merchandising rep (even if rep trained and available)
- **No system incentive to cross-train** (can't see ROI of multi-tactic rep in scheduling workflow)

**Example:**
- Merchandising manager has 10 reps
- Break/fix manager has 10 reps
- Slow week for merchandising (only 100 hours of work, 10 reps × 40 hours = 400 hours capacity)
- Busy week for break/fix (500 hours of work, 10 reps × 40 hours = 400 hours capacity)
- **Result:** Merchandising reps idle, break/fix reps working overtime
- **Better outcome:** Cross-train 5 reps, flex them to break/fix for busy week
- **Blocker:** Managers don't see capacity across LOBs, don't trust system to optimize

---

## Cultural Standardization Challenge: "Have It Your Way" Culture

**Rating:** Not explicitly rated, but identified as **significant barrier to scalability**

### Root Cause

**Quote (paraphrased):**
> "The leadership identified a 'have it your way' culture as a significant barrier to scalability. Standardizing processes across lines of business remains a challenge, as various teams prefer bespoke workflows over a unified system approach."

**Manifestations:**

#### 1. Sales Agrees to Custom Requirements
- Every client deal includes custom terms
- "We can do that" culture (sales says yes to everything)
- No pushback to fit client into standard offerings

#### 2. LOB Teams Build Bespoke Workflows
- Merchandising team has their own survey structure
- Break/fix team has different time tracking process
- Installations team uses different approval hierarchy
- Audits team has custom reporting requirements

#### 3. Regional Variations
- Minnesota region (RMS acquisition) operates differently
- Each of the 6 original companies (Apollo, BDS, WhiteHawk, BTR, MAG, MaaS) had own processes
- Post-merger: didn't fully standardize, allowed regional flexibility

#### 4. Manager Preferences
- Each manager has own scheduling approach
- Some use OpenSky self-scheduling, some do hard scheduling, some do spreadsheets
- No enforcement of standard process

---

## Impact on Scalability

**Why "Have It Your Way" Culture Blocks Growth:**

1. **Can't onboard new acquisitions quickly** (RMS taking 12+ months to integrate)
2. **Can't scale operations team** (need specialized knowledge for each LOB's bespoke workflow)
3. **Can't automate** (every workflow is custom, no economies of scale)
4. **Can't train new managers** (too many variations, tribal knowledge required)
5. **Can't optimize resources** (cross-LOB visibility impossible when each LOB uses different process)

**PE Rollup Context:**
- Channel Partners is PE-backed, likely will acquire more companies
- Every acquisition will have own systems, processes, culture
- If Channel Partners can't standardize itself (6 merged companies still not fully unified), how will it integrate next 3-5 acquisitions?

---

## Salesforce Change Management Opportunity

**Key Message:**
> "Salesforce implementation is a forcing function for standardization. You can't have 5 different ways to do the same thing on one platform. This is a feature, not a bug."

**Approach:**
1. **Define "Standard" vs. "Custom":**
   - Standard: 80% of projects use same workflow (merchandising, audits, basic break/fix)
   - Custom: 20% of projects require bespoke workflow (installations, experiential, complex break/fix)

2. **Standardize the Standard:**
   - Merchandising Work Type (standard survey, standard time tracking, standard parts process)
   - Break/Fix Work Type (standard troubleshooting workflow, standard parts ordering)
   - Audit Work Type (standard checklist, standard photo requirements)

3. **Architect for Custom:**
   - Custom Work Types for bespoke projects (Samsung Installation, LG Display Refresh, etc.)
   - Field-level customization (add custom survey questions, custom approval steps)
   - Client-specific Experience Cloud portals (custom reporting, custom KPIs)

4. **Governance:**
   - Only Sales VPs can approve custom work (not every account exec)
   - Custom work must be priced higher (margin for complexity)
   - Quarterly review: migrate high-volume custom work to standard offerings

---

## Open Questions for Next Assessment Areas

**Other functional areas to rate:**
- Client service / account management
- Finance / billing / invoicing
- HR / recruiting / retention
- IT / systems / data
- Training / learning & development

**Hypothesis:**
- Finance will rate MEDIUM (Business Central works, but project profitability visibility is poor)
- IT will rate LOW (3 WMS systems, Freshdesk not integrated, RMS Portal not integrated, Mars not integrated)
- Client service will rate MEDIUM (Freshdesk works, but manual processes, no self-service portals)

---

## Summary: Core Themes Across Assessments

### 1. Manual Processes Blocking Scale
- Sales/contracting: manual proposals, no CPQ
- Project kickoff: manual data entry across fragmented systems
- Scheduling: "spreadsheet magic" instead of system optimization
- Result: Can't scale beyond current size without linear headcount growth

### 2. Lack of System Trust
- Managers don't trust OpenSky scheduling recommendations
- Fall back to personal relationships and tribal knowledge
- System data not accurate (availability, skills, real-time status)
- Result: System investment wasted, manual work continues

### 3. "Have It Your Way" Culture
- Sales agrees to custom requirements without standardization
- Each LOB operates differently (bespoke workflows)
- Regional variations (RMS, original 6 companies not fully unified)
- Result: Can't onboard acquisitions quickly, can't automate, can't optimize

### 4. Capacity Visibility Gap
- Employee availability not captured in system
- Managers manually track in spreadsheets/mental models
- Can't see capacity across LOBs (merchandising idle, break/fix overtime)
- Result: Underutilization + overtime simultaneously, can't pursue new leads

### 5. Cross-Training Blocker
- Manual scheduling reinforces LOB silos
- No system incentive to assign multi-tactic work
- Skills currency unknown (trained 6 months ago, rusty now)
- Result: Can't flex resources, must hire for each LOB separately

---

## Salesforce FSL Value Hypothesis

**If these 5 themes are solved, what's unlocked?**

1. **Automated scheduling** replaces "spreadsheet magic" → Managers save 10-15 hours/week
2. **Real-time capacity visibility** → Optimize utilization, reduce overtime 20%
3. **Skills-based routing** → Cross-train reps, flex across LOBs
4. **Standardized workflows** → Onboard RMS in 30 days (not 12 months)
5. **Sales Cloud + CPQ** → Standardize 80% of deals, custom only when needed

**ROI Impact:**
- 15% efficiency gain = 1.3M freed hours/year = $32M revenue capacity
- 20% overtime reduction = $8M/year cost savings (4,140 reps × $50k avg salary × 10% overtime × 20% reduction)
- 30-day acquisition onboarding = faster PE rollup execution = higher exit multiple

---

## Next Steps

1. **Continue performance assessment** (client service, finance, IT, HR, training)
2. **Quantify current state** (idle time %, overtime %, lead decline rate, manager scheduling hours)
3. **Map gaps to FSL capabilities** with specific feature-to-problem mapping
4. **Build ROI model** with validated assumptions (not hypothesis)
5. **Identify pilot scope** (single LOB, 100 reps, 90 days) to prove scheduling ROI
6. **Change management plan** to address "have it your way" culture and system trust gap

---

**End of Business Assessment Documentation**
