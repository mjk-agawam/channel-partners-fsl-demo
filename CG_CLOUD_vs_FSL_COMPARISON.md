# Channel Partners Solution: Consumer Goods Cloud + Field Service Lightning

**Document Purpose:** Compare Consumer Goods Cloud (Retail Execution) and Field Service Lightning capabilities against Channel Partners' documented requirements, mapped to specific Lines of Business (LOBs).

**Key Finding:** Channel Partners needs **BOTH products** working together:
- **Consumer Goods Cloud (65% of business):** Merchandising + Audits
- **Field Service Lightning (35% of business):** Break-fix + Installations + Construction

---

## 📋 LOB-to-Product Mapping

| LOB | % of Business | Product | Why |
|-----|--------------|---------|-----|
| **Merchandising** | ~50% | **CG Cloud** | Store visits, shelf resets, planogram compliance, recurring routes |
| **Audits** | ~15% | **CG Cloud** | Compliance surveys (600-1,200 questions), Perfect Store metrics |
| **Break-Fix** | ~20% | **FSL** | Equipment repair, parts tracking, WMS integration, SLA compliance |
| **Installations** | ~10% | **FSL** | Display installations, multi-person crews, travel management |
| **Construction** | ~5% | **FSL** | Contractor management, large buildouts, project-based billing |

---

## 📅 Scheduling & Workforce Optimization

**Pain Point Context:** SVPs and EVPs spending 10-hour weekend calls building spreadsheet schedules that get retrofitted into OpenSky. Jay's quote: "10-hour call, four of them doing a scheduling all Saturday, all Sunday" - this was for **Target 1,900-store merchandising waves** (recurring retail visits).

---

### Automated scheduling using skills/tactics, distance, and availability

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising LOB (50% of business)**
- This solution fully supports automated scheduling by pairing its native retail data model for Target and Best Buy with advanced multi-month routing algorithms that automatically match reps to stores based on territory, availability, and specific product-tactic profiles.
- **Use case:** Target merchandising wave (1,900 stores, 8-week campaign, recurring weekly visits)
- **Feature:** Visit Plans with route optimization

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs (30% of business)**
- This solution provides a highly granular, real-time mathematical optimization engine to dynamically dispatch reps based on intricate skill sets, live travel distance, and immediate availability.
- **Use case:** Samsung display repair at Best Buy (reactive dispatch, 2-hour SLA)
- **Feature:** Einstein Optimization with real-time scheduling
- ⚠️ **Note:** Requires custom configuration to understand retail-specific metrics like shelf compliance or planograms

**Winner for biggest pain point:** **CG Cloud** (merchandising scheduling is their #1 pain point)

---

### Capacity planning — capturing availability 3 weeks out

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs**
- This solution captures rep availability 3 weeks out using standard user calendars, allowing its automated system to generate and push stable multi-week visit schedules to Target and Best Buy stores without manual spreadsheets.
- **Feature:** Visit Plans with multi-week capacity view

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution maps availability 3 weeks out via structured shifts and operating hours, enabling its core engine to run continuous capacity planning that balances forecasted work against future rep availability to flag staffing gaps well in advance.
- **Feature:** Resource Absences + Operating Hours + Capacity dashboards

**Verdict:** Both handle this equally well for their respective LOBs.

---

### Real-time exception visibility instead of daily batch reporting

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs**
- This solution gives managers instant visibility when a Target or Best Buy visit is missed or delayed, automatically triggering real-time alerts and dynamic in-app notifications so supervisors can re-route work immediately instead of waiting for a daily batch report.
- **Current gap:** Snowflake ETL 4x/day (6-hour batch delay)
- **CG Cloud solves:** Real-time visit completion tracking

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution uses a live, interactive dispatcher console to provide second-by-second visibility into actual versus scheduled rep locations, immediately flagging delays or scheduling exceptions via visual alerts the moment a rep falls behind.
- **Feature:** Live Dispatcher Console with GPS tracking

**Verdict:** Both needed for different LOBs. CG Cloud for merchandising coverage, FSL for break-fix SLA monitoring.

---

### Multi-tactic resource optimization — training reps on multiple skills and scheduling them across retailers

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising LOB - PRIMARY USE CASE**
- This solution optimizes multi-skilled reps by automatically dynamically assigning different, retailer-specific action plans (like a Target display setup vs. a Best Buy electronics audit) to the same rep based on the specific tactics required for each store on their route.
- **From docs:** Jay's vision of "fluid resources" working across Target, Best Buy, Walmart = **CG Cloud multi-retailer Visit Plans**
- **Feature:** Multi-skill Service Resources with cross-retailer Action Plans

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution uses its core algorithmic engine to mathematically evaluate a rep's complex matrix of multiple certified skills, perfectly matching and scheduling them across different retailers based on whichever store requires their specific blend of tactical expertise that day.
- **From docs:** Break-fix rep certified for Samsung + LG installations = **FSL skills-based routing**
- **Feature:** Skills Matrix with multi-certification matching

**Winner for stated goal:** **CG Cloud** (their goal is merchandising reps working across multiple retailers, not break-fix techs)

---

## 🛠️ Field Execution & "Go-Backs"

**Pain Point Context:** 10% go-back rate = $260M/year cost. John's quote: "number one thing in our goback data shows as materials" (30-40% root cause = parts not delivered).

---

### Work orders with parts/material tracking baked in

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising LOB - promotional materials only**
- This solution tracks store-level assets, promotional materials, and display kits within the retail data model, ensuring that reps have visibility into whether marketing materials or POP displays have arrived at a Target or Best Buy before a visit is scheduled.
- **What it tracks:** Promotional signage, shelf tags, POP displays (merchandising materials)
- ⚠️ **What it does NOT track:** WMS-level repair parts inventory (Samsung display cables, LG components)

**Salesforce Field Service:**
- ✅ **Break-fix LOB - repair parts inventory - PRIMARY USE CASE**
- This solution natively features a robust Product Requests and Inventory tracking system that explicitly ties parts and materials to specific Work Orders, preventing "go-backs" by automatically blocking a visit from being scheduled until the required inventory is confirmed to be in the rep's vehicle or at the store.
- **From docs:** 30-40% of go-backs caused by parts not delivered = **FSL + WMS (Sphere) integration solves this**
- **Feature:** ProductRequired + ProductConsumed + LocationInventory + Shipment tracking

**Winner for #1 go-back cause:** **FSL** (parts-related go-backs are break-fix work, not merchandising)

**Both needed:** Merchandising materials (CG Cloud) + repair parts (FSL)

---

### Mobile-first offline-capable app — comparable to what they've built in OpenSky

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs**
- This solution includes the native Consumer Goods Cloud Offline Mobile App, which is explicitly designed for the retail storefront to execute complex shelf audits, penny-perfect pricing, and planogram checks entirely offline at Target or Best Buy before auto-syncing with Salesforce.
- **Designed for:** Shelf counts, pricing audits, planogram photos, product placement

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution features a highly customizable Field Service Mobile App with standard offline database capabilities powered by Lightning Web Components (LWC) and Briefcase Builder, tailored for technicians completing on-site work orders, inventory logging, and asset tracking without cellular service.
- **Designed for:** Equipment repair, parts tracking, time logging, asset troubleshooting

**From docs - Kari's concern:**
> "A mobile app that works consistently in all different environments... man is that hard to keep clean."

**Their requirements:**
- 8-hour shifts offline (retail stores have "very spotty coverage deep in stores")
- 600-1,200 question surveys
- 50+ photos per shift
- Sync reliability when 500 reps sync simultaneously

⚠️ **CRITICAL REALITY CHECK:**
**Both apps work offline, but NEITHER handles 600-1,200 question surveys out-of-the-box. Custom Lightning Web Component development required for BOTH products.**

**CG Cloud Assessment Tasks** = better starting point for retail surveys (OOTB 50-100 questions)
**FSL Service Work Plans** = more basic (OOTB 10-20 steps)

**Both require stress testing:** 600-question survey, 8-hour offline, 50 photos, 500 concurrent syncs

---

### Survey/checklist capabilities with conditional logic

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs - BETTER STARTING POINT**
- This solution uses native Assessment Tasks and Action Plans designed specifically for retail, allowing reps at Target or Best Buy to go through guided, conditional-logic surveys (like triggering an extra pricing question only if an item is flagged as out-of-stock).
- **OOTB capability:** 50-100 question surveys with basic conditional logic
- **From docs:** 600-1,200 questions with grid questions (10 columns × 10 rows) = **custom LWC required**

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs - MORE CUSTOM DEV NEEDED**
- This solution uses Service Work Plans and Salesforce Flows to dynamically surface step-by-step checklists to the rep's mobile device, using conditional logic to inject new safety procedures or troubleshooting tasks based on the specific answers recorded during a work order.
- **OOTB capability:** 10-20 step work plans with basic conditional logic
- **From docs:** 600-1,200 questions = **significantly more custom LWC development required**

⚠️ **CRITICAL REALITY CHECK:**
**CG Cloud Assessment Tasks** = designed for retail surveys, handles complexity better
**FSL Service Work Plans** = designed for equipment checklists, requires more customization

**Winner for 600-1,200 question surveys:** **CG Cloud** (but custom development still required)

**Kari will test this immediately** - don't oversell OOTB capabilities.

---

### Material logistics tracking tied directly to the work order

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising LOB - promotional materials**
- This solution links marketing materials, display kits, and point-of-sale assets directly to Retail Store records and Action Plans, giving reps real-time visibility into whether the required promotional items have been delivered to Target or Best Buy before they begin their execution tasks.
- **What it tracks:** Promotional signage, shelf tags, POP displays, demo units (merchandising materials)

**Salesforce Field Service:**
- ✅ **Break-fix LOB - repair parts inventory**
- This solution natively embeds a full inventory logistics suite directly into the Work Order lifecycle, tracking serialized or non-serialized parts from the warehouse to the rep's trunk stock to ensure a visit is only dispatched once the specific materials are marked as available.
- **What it tracks:** Samsung display cables, LG components, repair tools, serialized equipment (WMS-level inventory)
- **Integration:** Sphere WMS integration for parts availability, shipment tracking, pre-arrival validation

**Verdict:** Both needed for different material types. CG Cloud for merchandising materials, FSL for repair parts.

---

## 🔧 Break-Fix / Case Management

**Context:** Break-fix team uses Freshdesk + OpenSky simultaneously with no automation between them (dual-screen juggling).

---

### Cases + Work Orders in one platform — no dual-screen juggling

**Consumer Goods Cloud (Enterprise Edition):**
- ⚠️ **Less optimized for equipment repair**
- By utilizing the core Service Cloud foundation underneath CG Cloud, this solution unifies customer support and retail execution on a single platform, allowing a Best Buy or Target service case to be immediately converted into an in-store execution visit on the same screen.
- **Use case:** Client complaint about merchandising work quality → Investigation visit

**Salesforce Field Service:**
- ✅ **Break-fix LOB - PURPOSE-BUILT FOR THIS**
- Designed natively for break-fix scenarios, this solution combines cases and work orders into a single, automated lifecycle where a support ticket instantly generates a dispatched job, completely eliminating dual-screen juggling for the team.
- **From docs:** Freshdesk + OpenSky dual-screen workflow = **FSL solves this directly**
- **Feature:** Case → Work Order automation via Flow

**Winner:** **FSL** (break-fix is its core use case)

---

### Automated case creation from client requests, no manual intake

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Via Service Cloud foundation**
- By leveraging its underlying Service Cloud foundation, this solution uses native intake tools like Email-to-Case or API integrations to automatically convert incoming client requests into retail service cases for Target and Best Buy without manual data entry.

**Salesforce Field Service:**
- ✅ **Via Service Cloud foundation**
- Built natively on top of Service Cloud, this solution utilizes automated ingestion channels—such as Email-to-Case or client portals—to immediately transform an incoming customer request into a live case and a scheduled work order without any human intervention.

**Verdict:** Both use same underlying Service Cloud Email-to-Case capability. No advantage either way.

---

### Tier-1 field ambassador enablement — reps identifying and resolving issues on-the-fly

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising reps CREATE cases for break-fix issues**
- This solution enables field reps at Target or Best Buy to spot real-time store issues and instantly generate a new, context-rich ad-hoc visit or store-level task right from their mobile app to resolve the problem on-the-fly.
- **From docs - Jay's quote:** "A merch goes to a target, sees one of the install broken or a display broken. There is not even an incentive for the person to capture that and send it."

**Salesforce Field Service:**
- ✅ **Break-fix techs RESOLVE work orders**
- This solution empowers reps to act as true field ambassadors by allowing them to create and dispatch a new Work Order or Case directly from their mobile device the moment they discover a broken display or broken asset in the store.

**REALITY: BOTH PRODUCTS WORKING TOGETHER**

**Correct workflow:**
1. **CG Cloud rep** (merchandising) visits Target for shelf reset
2. Notices broken Samsung display (not their job)
3. Creates **Case** via CG Cloud mobile app
4. Case auto-converts to **FSL Work Order**
5. **FSL break-fix tech** dispatched to repair display

**This is the integrated solution** - CG Cloud for issue reporting, FSL for issue resolution.

---

## 👷 Subcontractor Management

**Context:** Construction work uses third-party contractors (invoice-based payment, link-based call form access). From docs: John's quote "it's like a link on a phone to a website that they fill out" - NO system login, NO mobile app access required.

---

### Contractor management handles non-employee workers, time tracking, and invoicing

**Consumer Goods Cloud (Enterprise Edition):**
- ⚠️ **Requires more configuration**
- This solution enables third-party contractor labor to access the core retail execution data model through tailored Experience Cloud portals, allowing subcontractors to execute, log, and submit Target and Best Buy store audits without requiring full internal platform access.
- **What's needed:** Experience Cloud Community licenses + custom portal development to replicate link-based workflow

**Salesforce Field Service:**
- ✅ **Construction LOB - BETTER OOTB FEATURES**
- This solution features native Contractor Management licensing built specifically for blended workforces, automatically routing jobs to external vendors, tracking their time, and managing their invoicing directly within the core optimization engine.
- **OOTB features:** Service Resource Type = Contractor, invoice-based payment model, Experience Cloud portal
- **What's needed:** Experience Cloud Community licenses + custom portal development for link-based call form workflow

**From docs - Current workflow:**
- Link-based access (no login required)
- Complete call form via web browser
- Invoice generated from completed work
- Paid via AP (not payroll)

⚠️ **REALITY CHECK:**
**FSL has better OOTB contractor features, BUT:**
- Both require Experience Cloud licenses (additional cost)
- Both require custom portal development to match link-based workflow
- FSL handles invoice-based payment models better

**Winner:** **FSL** (better OOTB contractor management, but both require custom work)

---

## 🤖 AI & Automation (Jay's 3 Design Concepts)

**Context:** Jay described 3 priority AI use cases (17+ total documented). From docs: "That's what we're looking at. So there's about 17 different use cases... probably 20 plus at this point."

---

### Bidirectional field rep chatbot → Agentforce + Knowledge Base

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs**
- This solution integrates with Agentforce and Salesforce Knowledge to provide field reps at Target or Best Buy with an intelligent, bidirectional conversational assistant that can instantly pull product schemas, display guidelines, or retail execution instructions right from the mobile app.
- **From docs - Jay's quote:** "Having a bidirectional AI that you can ask specific questions that can be put in place for your field employees"
- **Use case:** "How do I set up the Samsung OLED display at Best Buy?" → Bot returns KB article + past Work Order examples

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution leverages native Agentforce for Field Service combined with the FSL Knowledge Base, allowing reps to have interactive, text-based conversations with an AI agent to troubleshoot complex asset fixes, update work order statuses, and query parts availability on-the-fly.
- **Use case:** "How do I troubleshoot Samsung display flickering?" → Bot returns KB article + similar repair tickets

**Verdict:** Both integrate with Agentforce equally well. No advantage either way.

---

### Planogram compliance via image recognition → Vision AI

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs - PRIMARY USE CASE**
- This solution uses Einstein Vision for Consumer Goods natively within the mobile app, allowing reps to take a single photo of a Target or Best Buy shelf that instantly analyzes planogram compliance, shares of shelf, and out-of-stocks to trigger immediate corrective in-store actions.
- **From docs - Jay's vision:** "We have reference images of planograms... the AI can compare those two images"
- **From docs - ROI:** $13.2M annual QC cost reduction
- **OOTB feature:** Planogram compliance is core CG Cloud capability
- **Use case:** Rep takes shelf photo → Einstein Vision compares to reference planogram → Pass/Fail in <2 seconds → If Fail, create Action Plan for immediate correction

**Salesforce Field Service:**
- ⚠️ **Requires more configuration**
- This solution integrates with Salesforce Vision AI to analyze uploaded field images, automatically generating a follow-up corrective Work Order and dispatching a technician the moment the AI detects a planogram violation or broken display element.
- **Use case:** Rep takes photo of broken display → Einstein Vision detects damage → Auto-create Work Order for repair

**Winner:** **CG Cloud** (planogram compliance is its core use case, FSL is for equipment repair validation)

**REALITY: CG Cloud for planogram QC, FSL for repair validation** - both use Einstein Vision but for different purposes.

---

### Dynamic task creation from exceptions → automated work order routing

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs**
- This solution instantly transforms real-time audit exceptions—such as a missing display at a Target or Best Buy—into dynamic, store-level assessment tasks that are automatically pushed to the field rep's active in-store checklist.
- **Feature:** Action Plans auto-created from Assessment Task exceptions
- **Use case:** Audit finds out-of-stock → Auto-create Action Plan for store manager follow-up

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution leverages its automated routing engine to instantly generate and dispatch a reactive Work Order to the closest qualified technician the moment an asset exception, IoT alert, or compliance failure is detected in the system.
- **Feature:** Einstein Optimization auto-assigns Work Orders to nearest qualified tech
- **Use case:** Display malfunctions → Auto-create Work Order → Einstein assigns to Samsung-certified tech 10 minutes away

**Verdict:** Both needed for different exception types. CG Cloud for merchandising exceptions, FSL for equipment failures.

---

## 📊 KPIs & Real-Time Reporting

**Context:** Current state = Snowflake ETL 4x/day (6-hour batch delay), daily batch Tableau reports. James wants real-time exception reporting. From docs: "Spreadsheets 3 days later" sent to Samsung/LG clients.

---

### Scheduling KPIs out of the box (utilization, go-back rates, SLA compliance)

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Merchandising + Audits LOBs**
- This solution provides real-time, in-flight dashboards through Salesforce Data Cloud and CRM Analytics that track immediate retail execution metrics—such as store compliance rates, audit completion speed, and out-of-stock percentages—the moment a rep submits their Target or Best Buy visit data.
- **CG Cloud KPIs:** Visit completion rate, store coverage, Perfect Store scores, planogram compliance %, out-of-stock rates, audit completion time

**Salesforce Field Service:**
- ✅ **Break-fix + Installation LOBs**
- This solution delivers instant, out-of-the-box operational dashboards focused heavily on field efficiency, giving management real-time visibility into technician utilization rates, SLA compliance deadlines, and "go-back" rates as work orders are closed out live in the field.
- **FSL KPIs:** Tech utilization %, SLA compliance, first-time fix rate (inverse of go-backs), travel time vs work time, overtime trending

**Verdict:** Both needed for different KPI types. CG Cloud for merchandising metrics, FSL for break-fix metrics.

---

### Tableau integration — they already mentioned wanting real-time data

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Via Data Cloud + Einstein Analytics (Tableau CRM)**
- This solution integrates with Tableau via Data Cloud to supply pre-built industry dashboards, transforming immediate store compliance, out-of-stock data, and Best Buy or Target brand performance metrics into real-time, actionable business insights.
- **From docs:** Current Tableau sources from Snowflake (4x/day batch) → CG Cloud provides real-time via Data Cloud connectors

**Salesforce Field Service:**
- ✅ **Via Data Cloud + Einstein Analytics (Tableau CRM)**
- This solution channels live operational data directly into Tableau, allowing management to build dynamic, real-time analytics around workforce productivity, live field exceptions, dispatcher efficiency, and long-term subcontractor utilization trends.
- **From docs:** Current PowerBI sources from Snowflake (4x/day batch) → FSL provides real-time via Data Cloud connectors

⚠️ **Note:** "Tableau Next" not explicitly mentioned in docs. Assuming this means Tableau Cloud with real-time connectors via Salesforce Data Cloud.

**Verdict:** Both integrate with Tableau/PowerBI via Data Cloud. Can maintain existing Tableau investment while adding real-time capabilities.

---

### Client-facing dashboards replacing static spreadsheets sent to Samsung/LG

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Samsung merchandising data (planogram compliance, shelf placement)**
- Via Experience Cloud, this solution provides Samsung-branded portals showing real-time merchandising work (planogram compliance, product placement, shelf photos) across Best Buy stores.
- **From docs:** "Spreadsheets 3 days later" replaced with real-time portal

**Salesforce Field Service:**
- ✅ **Samsung installation work (equipment installations, repair status)**
- Via Experience Cloud, this solution provides Samsung-branded portals showing real-time installation progress (display installations, repair completions, before/after photos) across Best Buy stores.
- **From docs:** Samsung integration is for installation work and parts tracking → FSL portal shows Work Order status

**REALITY: Samsung likely needs BOTH portals**
- **Merchandising data** (planogram compliance) → **CG Cloud Experience Cloud portal**
- **Installation/repair data** (equipment work) → **FSL Experience Cloud portal**
- Both can be unified in single Samsung-branded portal (custom Experience Cloud site with both data sources)

---

## 🔗 Integration Architecture

**Context:** Current stack (OpenSky → Snowflake → PowerBI/Tableau, Samsung API gateway, Sphere WMS) needs to persist during transition.

---

### API Gateway strategy for Samsung integration — system of record without forcing Samsung to re-engineer

**Consumer Goods Cloud (Enterprise Edition):**
- ⚠️ **Secondary role for Samsung**
- This solution serves as the definitive system of record for all retail store data and accounts, utilizing the Samsung API gateway to ingest external inputs and update Best Buy or Target records without requiring any structural re-engineering of the existing Samsung stack.
- **Use case:** Samsung wants merchandising/planogram data

**Salesforce Field Service:**
- ✅ **Primary role for Samsung - PRIMARY USE CASE**
- This solution functions as the operational system of record for jobs and inventory logistics, using the Samsung API gateway to seamlessly receive external event triggers and output real-time work order data without disrupting the existing infrastructure.
- **From docs - Jay's quote:** "API gateway... hijack that make that talk to open sky" - Samsung integration is for installation work and WMS integration
- **Use case:** Samsung wants installation work progress and parts tracking
- **Integration:** MuleSoft as API gateway/proxy → Samsung sees same API contract, backend swaps from OpenSky to FSL

**Winner:** **FSL** (Samsung integration documented as installation/parts tracking, not merchandising)

**But:** If Samsung also wants merchandising data (planogram compliance), CG Cloud integration needed too.

---

### Phased team-by-team rollout — maps to multi-tenant deployment model

**Consumer Goods Cloud (Enterprise Edition):**
- ✅ **Supports phased rollout**
- This solution accommodates a phased rollout by using standard Salesforce Sandboxes and custom metadata types to deploy new retail execution workflows and store groups (such as launching Best Buy stores first and Target second) without disrupting active users.
- **From docs - Kari's validation:** "That's what we've done in the past... rolling out functionality one team at a time"
- **Approach:** Phase 1 = California merchandising team (500 reps), Phase 2 = Texas audit team (300 reps), etc.

**Salesforce Field Service:**
- ✅ **Better OOTB support for phased rollout**
- This solution natively supports a phased, team-by-team rollout by using built-in Service Territories and Scheduling Policies, allowing the organization to onboard specific regional teams or sub-contractor networks one at a time while isolating data configurations.
- **Feature:** Service Territories designed for geographic/team isolation
- **Approach:** Phase 1 = California break-fix team (200 reps), Phase 2 = Texas installation team (150 reps), etc.

**Slight edge to FSL** (Service Territories designed for this), but both support phased rollout equally well.

---

## 💰 Licensing & Cost Implications

**Critical gap in original value proposition:** Treated as "$73.5K for 70 licenses" opportunity. Reality = significantly larger.

### Licensing Requirements

| Product | Users | Est. Cost/User/Year | Annual Cost |
|---------|-------|---------------------|-------------|
| **Consumer Goods Cloud (Enterprise)** | 2,500 merchandising/audit reps | $1,800-2,400 | $4.5M-6M |
| **Field Service Lightning** | 1,640 break-fix/installation reps | $1,980-2,400 | $3.2M-4M |
| **Experience Cloud (Community)** | ~500 contractors + clients | $600-1,200 | $300K-600K |
| **Data Cloud** | Full org (real-time reporting) | Included or add-on | $500K-1M |
| **Einstein AI (Vision + Bots)** | All users | Included or add-on | $200K-500K |
| **MuleSoft (API Gateway)** | Integration layer | Per API call or flat fee | $200K-500K |

**Total 3-year TCO:** $26-35M (licenses + implementation + support)

**vs. original "$73.5K for 70 licenses"** = This was FSL pilot only, missing CG Cloud for 60% of business.

---

## ✅ Recommended Solution Architecture

### Integrated Platform: CG Cloud + FSL

**Phase 1 (Months 1-3): Pilot - 100 reps**
- **50 merchandising reps** (California) → **CG Cloud**
  - Visit Plans for Target stores
  - Assessment Tasks for audits
  - Einstein Vision planogram compliance
- **50 break-fix reps** (Texas) → **FSL**
  - Case → Work Order automation (Freshdesk integration)
  - Parts tracking (Sphere WMS integration)
  - Einstein Optimization scheduling

**Phase 2 (Months 4-6): Expand - +300 reps**
- **200 merchandising reps** (multi-region) → **CG Cloud**
- **100 break-fix reps** (multi-region) → **FSL**
- **Integration:** CG Cloud rep creates Case → FSL Work Order auto-created

**Phase 3 (Months 7-12): Scale - +1,200 reps**
- **800 merchandising/audit reps** → **CG Cloud**
- **400 installation reps** → **FSL**
- **Client portals:** Samsung Experience Cloud portal (both CG Cloud + FSL data)

**Phase 4 (Months 13-18): Full rollout - +2,540 reps**
- **Remaining 1,450 merchandising reps** → **CG Cloud**
- **Remaining 1,090 break-fix/installation reps** → **FSL**
- **Construction contractors** → **FSL** (Experience Cloud portal)
- **RMS acquisition (1,500 employees)** → **CG Cloud** (Minnesota merchandising team)

---

## 🚨 Critical Success Factors

### 1. Survey Complexity (Highest Technical Risk)

**Requirement:** 600-1,200 question surveys with grid questions (10 columns × 10 rows), task subdivision, complex conditional logic.

**Reality:**
- ❌ Neither CG Cloud nor FSL handles this out-of-the-box
- ✅ CG Cloud Assessment Tasks = better starting point (OOTB 50-100 questions)
- ✅ FSL Service Work Plans = more basic (OOTB 10-20 steps)
- ⚠️ **Custom Lightning Web Component development required for BOTH products**

**Recommendation:**
- Build 200-question prototype in CG Cloud (merchandising/audit surveys)
- Build 50-question prototype in FSL (break-fix checklists)
- **Let Kari test hands-on** before committing to full rollout
- Budget $300K-500K for custom survey LWC development

---

### 2. Offline Mobile Reliability

**Requirement:** 8-hour shifts offline, 600+ question surveys, 50+ photos, sync reliability for 500 concurrent reps.

**Reality:**
- ✅ Both apps work offline OOTB
- ⚠️ **Stress testing required:** 600-question survey completion, 8 hours no connectivity, 50 photo uploads, 500 simultaneous syncs

**Recommendation:**
- Conduct stress test BEFORE pilot (not during)
- Document exact limitations (photo storage limits, sync failure scenarios)
- If gaps found, custom development plan with timeline/cost

---

### 3. Change Management (Bigger Risk Than Technology)

**From docs - Stephen's quote:**
> "Participants reiterated that successful digital transformation relies more on organizational adoption than software functionality."

**"Have It Your Way" culture blocks scalability:**
- Sales says yes to every custom client request
- Each LOB has bespoke workflows
- Managers revert to spreadsheets if system doesn't work exactly how they want

**Risk:** Implement CG Cloud + FSL but don't fix culture → customize both platforms into oblivion → same problem, new platforms.

**Mitigation:**
- Leadership public commitment (CEO all-hands mandate for standardization)
- Manager accountability (bonuses tied to system adoption metrics)
- Champion network (20 high-performers train peers)
- Standard vs Custom pricing (custom work priced 2x higher)

---

## 📋 Summary: What to Tell Stakeholders

**Original framing:** "Field Service solves all your problems"

**Correct framing:**

> "Channel Partners has a hybrid business model spanning retail execution (merchandising/audits) and field service (break-fix/installations). Consumer Goods Cloud + Field Service Lightning provide unified workforce management across all LOBs:
>
> **Consumer Goods Cloud (65% of business):**
> - Merchandising: Target/Best Buy/Walmart store visits, shelf resets, planogram compliance
> - Audits: 600-1,200 question compliance surveys, Perfect Store metrics
> - Einstein Vision: Planogram QC with $13.2M ROI
>
> **Field Service Lightning (35% of business):**
> - Break-fix: Samsung/LG equipment repair, parts tracking, WMS integration
> - Installations: Display installations, multi-person crews, travel management
> - Construction: Contractor management, project-based billing
>
> **Integrated workflow:**
> - CG Cloud merchandising rep finds broken display → Creates Case
> - Case auto-converts to FSL Work Order
> - FSL break-fix tech dispatched, repairs equipment, tracks parts
> - Both systems feed unified client portal (Samsung sees merchandising + repair work)
>
> **Investment:** $8-10M/year licensing (2,500 CG Cloud + 1,640 FSL + Experience Cloud)
>
> **Critical success factors:**
> 1. Custom LWC development for 600-1,200 question surveys (both products)
> 2. Offline stress testing before pilot (not during)
> 3. Change management > technology (leadership mandate for standardization)"

---

## 🎯 Next Steps

1. **Demo Strategy:** Show BOTH products working together (30 min CG Cloud, 30 min FSL, 15 min integration, 15 min AI)
2. **Survey Prototype:** Build 200-question CG Cloud Assessment Task + 50-question FSL Work Plan, let Kari test
3. **Offline Stress Test:** 600-question survey, 8 hours offline, 50 photos, 500 concurrent syncs
4. **Cost Model:** Update opportunity from "$73.5K pilot" to "$8-10M/year full solution"
5. **Executive Alignment:** Present dual-product strategy, get buy-in on $26-35M 3-year TCO

**The research was excellent. The pain points are accurate. The solution just needs to be CG Cloud + FSL, not FSL alone.**
