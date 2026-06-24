# AI and Automation Initiatives

**Last Updated:** June 24, 2026  
**Source:** Architecture session discussion

---

## Overview

Channel Partners has established an **"Automation Team"** focused on AI-driven process improvements to reduce manual work, improve quality control, and enable self-service knowledge access.

---

## Current AI Initiatives

### 1. Conversational Chatbot for Internal Knowledge Base

**Purpose:**
- Bidirectional AI for internal employee queries
- Self-service knowledge base access
- Reduce support center call volume

**Use Cases:**

**Field Rep Questions:**
- "How do I troubleshoot Samsung display flickering?"
- "What parts do I need for LG OLED installation?"
- "Where do I find training video for Microsoft Surface setup?"

**Manager Questions:**
- "What's the SLA for Target merchandising projects?"
- "How do I approve out-of-policy expenses?"
- "Which reps are certified for break/fix work in California?"

**Support Center Questions:**
- "What's the escalation path for client complaints?"
- "How do I create a parts order for emergency dispatch?"
- "Which WMS do I use for Samsung parts?"

---

**Current State:**
- Knowledge scattered across: LearnUpon courses, SharePoint docs, email chains, tribal knowledge
- Reps call support center for basic questions
- Support center doesn't have centralized knowledge base (search across multiple systems)

**Desired State:**
- Single conversational interface (Slack bot, mobile app chat, web portal)
- AI searches across all knowledge sources (LearnUpon, OpenSky help docs, SOPs, training videos)
- Bidirectional: Ask question → Get answer with sources → Drill down for details → Escalate to human if needed

---

**Salesforce Opportunity:**

**Einstein Bot + Knowledge Base:**
1. **Knowledge Articles:** Migrate scattered knowledge into Salesforce Knowledge (structured, searchable, versioned)
2. **Einstein Bot:** Conversational AI that searches Knowledge Articles, Work Order history, Case history
3. **Slack Integration:** Ask Einstein Bot in Slack → Get answer with Knowledge Article links
4. **Mobile Integration:** FSL Mobile app chat → Einstein Bot → Knowledge Article in-app
5. **Analytics:** Track which questions asked most → identify training gaps, improve documentation

**Example Flow:**
1. Rep in FSL Mobile app: "How do I troubleshoot Samsung display flickering?"
2. Einstein Bot searches Knowledge Articles + Samsung-specific Work Order history
3. Returns: "3 common causes: loose HDMI cable (60%), firmware update needed (30%), hardware failure (10%). See KB Article #1234 for troubleshooting steps. Last 5 Samsung flicker issues resolved in avg 15 minutes."
4. Rep follows KB steps, resolves issue, doesn't need to call support center

**ROI:**
- Reduce support center call volume 20-30% (simple questions answered by bot)
- Reduce rep downtime waiting for support callback (self-service instant answers)
- Improve rep onboarding (new reps can ask bot instead of bothering manager)

---

### 2. Automated Quality Control (QC) Using Image Comparison

**Purpose:**
- Verify task completion using AI image analysis
- Auto-generate exception task lists (incomplete work, quality issues)
- Reduce manual QA review time

---

**Current QC Process (Manual):**

1. **Rep completes work:**
   - Takes "before" and "after" photos (required by survey)
   - Submits survey with photos attached

2. **QA team reviews:**
   - Manually opens each completed survey
   - Views before/after photos
   - Checks against completion criteria (display installed correctly, signage placed, old materials removed)
   - Flags exceptions (incomplete work, quality issues, safety violations)

3. **Exception handling:**
   - QA creates manual list of exceptions
   - Manager assigns go-back visits to fix issues
   - Rep returns to store to complete work

**Pain Points:**
- QA team can only review 5-10% of completed work (too time-consuming to review 100%)
- Quality issues discovered days/weeks later (client complains, too late to fix quickly)
- Inconsistent QA criteria (different reviewers flag different issues)
- High-value clients get manual QA, low-value clients get spot checks (risk of quality issues slipping through)

---

**Desired State: AI-Powered QC**

**Image Comparison AI:**
1. **Rep submits survey:**
   - Before/after photos uploaded
   - AI analyzes photos in real-time (while rep still on-site)

2. **AI comparison checks:**
   - Display installed? (detect Samsung logo, product placement, power on)
   - Signage placed correctly? (compare to reference image, check placement, alignment)
   - Old materials removed? (detect debris, old displays, packaging in "after" photo)
   - Safety compliance? (detect blocked fire exits, exposed wiring, trip hazards)

3. **Real-time feedback:**
   - AI flags issues WHILE REP STILL ON-SITE
   - Mobile app alert: "AI detected old display not removed. Please remove before leaving store."
   - Rep fixes issue immediately, re-takes photo, AI re-checks

4. **Exception task list auto-generated:**
   - AI identifies issues that can't be fixed immediately (missing parts, store closed early, customer refused access)
   - Auto-creates go-back Work Order with specific issue flagged
   - Manager sees list of AI-flagged exceptions (prioritized by severity)

---

**Salesforce Opportunity:**

**Einstein Vision + Flow Automation:**

1. **Einstein Vision for Image Recognition:**
   - Train Einstein Vision model on "good" vs. "bad" installation photos
   - Categories: Display placement, signage alignment, cleanliness, safety
   - Confidence score: 90%+ = Pass, 70-89% = Manual review, <70% = Fail

2. **Real-Time QC in FSL Mobile:**
   - Rep takes photo in FSL Mobile app
   - Photo uploaded to Salesforce Files
   - Einstein Vision analyzes image (1-2 seconds)
   - Result displayed in mobile app: ✅ Pass, ⚠️ Review, ❌ Fail with specific issue

3. **Flow Automation for Exception Handling:**
   - If Einstein Vision returns Fail → Auto-create follow-up Work Order (go-back)
   - If Einstein Vision returns Review → Add to QA team queue (manual review)
   - If Einstein Vision returns Pass → Auto-approve survey (no manual QA needed)

4. **Exception Dashboard:**
   - Einstein Analytics dashboard showing:
     - AI QC pass rate by rep (identify training needs)
     - AI QC pass rate by work type (identify process issues)
     - Most common failure reasons (missing parts, signage misalignment, etc.)
     - Go-back reduction trend (as AI QC improves over time)

---

**ROI:**

**Quality Improvement:**
- 100% of work AI-reviewed (vs. 5-10% manual spot checks today)
- Real-time feedback prevents quality issues (fix on-site vs. go-back days later)
- Consistent QA criteria (AI doesn't have "bad day," applies same standards every time)

**Cost Reduction:**
- Reduce manual QA team headcount (AI reviews 95%, humans review 5% flagged by AI)
- Reduce go-backs caused by quality issues (fix on-site vs. return trip)
- Improve client satisfaction (fewer quality complaints)

**Quantification (Needs Validation):**
- Manual QA team: 5 FTEs × $60K/year = $300K/year
- AI QC reduces manual review 80% → Save 4 FTEs = $240K/year
- Go-back reduction: 10% of go-backs caused by quality issues = 260K go-backs × $100 each = $26M/year
- If AI QC reduces quality go-backs 50% → Save $13M/year

**Total ROI: $13.2M/year** (quality go-back reduction + manual QA savings)

---

## AI Strategy Alignment with Salesforce

**Einstein AI is Native to Salesforce Platform:**

**No Integration Needed:**
- Einstein Bot runs natively in Salesforce (Service Cloud, FSL Mobile, Experience Cloud, Slack)
- Einstein Vision analyzes images uploaded to Salesforce Files
- No third-party AI vendor, no API integration, no data sync

**Unified Data Model:**
- Einstein learns from Salesforce data (Work Orders, Cases, Knowledge Articles)
- Better predictions because AI sees full context (rep history, project type, client requirements)
- Continuous learning (AI improves as more data accumulated)

**Governance and Trust:**
- Einstein Trust Layer (data privacy, bias detection, explainability)
- Audit trail (see which AI model made which decision, why)
- Human override (manager can overrule AI QC decision if needed)

---

## Strategic Shift: From "Yes" to Strategic KPI Alignment

**Historical Approach:**
- Sales says "Yes" to every client request (custom workflows, custom reporting, tight timelines)
- Operations scrambles to deliver (rushed implementations, quality suffers)
- Leadership focuses on revenue growth (say yes to win deals)

**New Approach:**
> "The conversation emphasized shifting focus from high-level 'Yes' commitments to strategic alignment on KPIs, with a focus on optimizing resource utilization and reducing the need for new hires through better process standardization."

**What This Means:**

**1. Define Core KPIs:**
- Resource utilization (target: 85% billable hours)
- Go-back rate (target: <5%)
- SLA compliance (target: >95%)
- Client satisfaction (target: NPS >50)
- Rep retention (target: <15% annual turnover)

**2. Say "No" to Requests That Hurt KPIs:**
- Client wants custom workflow that reduces utilization → Counter-offer standard workflow
- Sales wants tight timeline that increases go-back risk → Extend timeline or charge premium
- Client wants custom reporting that requires manual work → Offer self-service portal instead

**3. Optimize Resources Instead of Hiring:**
- Marketing rated 3/10 because "can't pursue leads, no capacity"
- OLD solution: Hire 500 more reps to scale
- NEW solution: Improve scheduling, reduce go-backs, cross-train reps → unlock 15% capacity WITHOUT hiring

**Salesforce Positioning:**
> "Salesforce FSL is the platform for KPI-driven operations. Every decision traceable to impact on utilization, quality, client satisfaction. Stop saying 'Yes' to everything, start saying 'Yes' to what moves KPIs."

---

## Open Questions

**Conversational Chatbot:**
1. What knowledge sources exist today? (LearnUpon, SharePoint, where else?)
2. How many support center calls are "simple questions" vs. "complex issues"? (% that bot could deflect?)
3. Are there client-facing chatbot use cases? (Store managers ask questions?)
4. What's average support center call handle time? (Cost to deflect via bot?)

**Automated QC:**
5. What % of completed work gets manual QA review today? (5-10% estimated, confirm?)
6. How many FTEs on QA team? (Cost to reduce via AI?)
7. What % of go-backs caused by quality issues? (vs. parts logistics, scheduling, etc.?)
8. What "good" vs. "bad" image training data exists? (Need 1,000+ labeled images to train Einstein Vision)
9. Are there liability concerns with AI QC? (If AI says "Pass" but work actually defective, who's responsible?)

**AI Strategy:**
10. Who is on "automation team"? (Roles, budget, reporting structure?)
11. Are there other AI initiatives beyond chatbot + QC? (Scheduling optimization? Predictive maintenance?)
12. What AI vendors/platforms evaluated? (OpenAI, Google Vertex, AWS Bedrock, Einstein?)
13. Is there AI governance policy? (Data privacy, bias detection, human oversight?)

---

**End of AI Automation Initiatives Documentation**
