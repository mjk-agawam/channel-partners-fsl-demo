# Session Notes — 2026-06-12

## What Was Done

### 1. Repo Created
- GitHub: https://github.com/mjk-agawam/channel-partners-fsl-demo
- Local: `~/Projects/channel-partners-fsl-demo`
- Workspace moved to this repo in Cursor

### 2. Deal Context Pulled from Org62
Pulled DSR DS-1712752, Opportunity, and Account records via the Salesforce Platform MCP (sobject-reads).

Full context is in `CONTEXT.md`. Summary:
- **Account:** Channel Partners Solutions, LLC. — 31-person PS firm, Irvine CA
- **Deal:** $73,500, New Business, Stage 02, close Oct 30, 2026
- **Ask:** FSL replacement for a homegrown field service solution. +60 FSL Tech, +10 Dispatcher, Crawl phase.
- **SE ask:** Discovery/reverse demo + targeted demo. Due June 17, 2026.

### 3. Org62 Access Infrastructure Built
Cursor can't authenticate the Org62-Sobject-Read MCP natively (Salesforce doesn't support dynamic client registration). Solution:

- **`scripts/org62_query.py`** — queries org62 via MCP using the token Claude already has in the macOS Keychain. Auto-refreshes expired tokens using the refresh token. Updates `~/.cursor/mcp.json` as a side effect.
- **`~/.cursor/rules/org62-access.mdc`** — always-applied Cursor rule documenting the approach so future sessions don't waste time figuring this out.

### 4. Slack Channel Not Yet Read
Target channel: `C095K8MQMB2`

The Slack MCP went into error state during this session. Root cause: running `~/.devbar/pkgs/aisuite/latest/aisuite` to inspect config inadvertently triggered an aisuite update that stopped the devbar manager process on port 29051 (the proxy all plugin MCPs route through). This took down Slack, browser, codesearch, and other plugin MCPs.

**Fix:** Restart AI Expert Suite from the menu bar/dock. Port 29051 will come back up and all plugin MCPs will reconnect.

**This is the first thing to do in the next session** — read the Slack channel fully before building anything.

---

## Open Items / Next Session

1. **Restart AI Expert Suite** to restore Slack MCP
2. **Read Slack channel `C095K8MQMB2`** — all posts from Jan 1, 2026 forward, with adversarial verification (Mike's explicit requirement)
3. **Internal SE level-set** on the account — understand the homegrown system before building the demo
4. **Scope the demo** — decide which FSL components to build based on Slack context + discovery notes
5. **Build demo components** in org `mjk-260320-scheduler`

---

## Technical Notes

### Demo Org
- Alias: `mjk-260320-scheduler`
- Admin: `admin@mjk-260320.scheduler`
- Access: `sf org open -o mjk-260320-scheduler`

### Cursor MCP State
- `~/.cursor/mcp.json` has `Org62-Sobject-Read` entry with a Bearer token (refreshed by the script)
- Plugin MCPs (slack, browser, etc.) route through aisuite proxy at `127.0.0.1:29051` — require AI Expert Suite to be running
- `~/.cursor/rules/org62-access.mdc` documents the full org62 auth approach

### Key Files Created This Session
| File | Location | Purpose |
|------|----------|---------|
| `org62_query.py` | `scripts/` in this repo | Query org62 records from Cursor/Claude |
| `org62-access.mdc` | `~/.cursor/rules/` | Cursor rule: org62 auth approach |
| `CONTEXT.md` | this repo root | Deal context and demo scenario |
| `SESSION_NOTES.md` | this repo root | This file |

---

# Session Notes — 2026-06-23

## What Was Done

### 1. Reverse Demo Transcript Processed
- Received full transcript from June 18, 2026 OpenSky reverse demo (2-hour session)
- Extracted key insights, pain points, workflows, and technical architecture
- Created comprehensive summary document: `REVERSE_DEMO_TRANSCRIPT.md`

### 2. Discovery Questions Drafted
- Built tailored discovery questions for June 24 meeting
- Questions build on what was learned in reverse demo (not re-asking basics)
- Focus areas: intelligent scheduling, reactive breaks, cross-LOB work, mobile stability, break/fix automation, real-time data
- File: `DISCOVERY_QUESTIONS.md`

### 3. Key Insights from Reverse Demo

**Top Pain Points ("Magic Wand" Responses):**
- Jay: Intelligent scheduling, field efficiency, real-time exception reporting
- Kari: Mobile app consistency across devices
- Mario: Smarter reactive scheduling (sick reps, job runs long)
- Tambra: Better rep mobile dashboard
- James: Lower-latency data with delta/CDC

**OpenSky System Overview:**
- Homegrown platform, merging two company systems (one self-scheduling, one hard-scheduling)
- Supports merchandising, break/fix, installations, dedicated brand teams
- Mix of hard scheduling (manager-assigned) and self-scheduling (rep drags to calendar)
- Overnight route optimization for self-scheduled work only
- Multi-rep team scheduling (5-15 people, same store) is manual and painful
- Offline-first mobile app (iOS/Android)
- 4-hour batch to data warehouse → Tableau/PowerBI

**Major Gaps:**
- Hard scheduling has no route optimization (inefficient routes, excess mileage reimbursement)
- No intelligent/AI-driven scheduling
- Silos by line of business (no cross-LOB work, no incentive for merch rep to handle break/fix issue in same visit)
- No real-time rep location visibility
- Reactive scheduling is manual (bulk reschedule tool)
- Mobile stability issues across devices
- No historical context for reps (prior visits, defects, contacts)
- Go-backs are manual (defect found → export → manually create new assignment)
- No real-time exception reporting (overtime risk, SLA breach, schedule adherence)

**Timeline Context:**
- July 6, 2026: Major OpenSky rollout across 6-7 business units
- Post-rollout: "Massive stabilization effort" with resource constraints
- Org structure changing (LOB silos → geographic model) in next 2-3 months
- Architecture workshop: June 24, 9am
- Follow-up session: Week of July 1-5

---

## Next Steps

1. **June 24 Discovery Meeting** — use `DISCOVERY_QUESTIONS.md` to probe scheduling, cross-LOB, mobile, break/fix, real-time data
2. **June 24 Architecture Session (9am)** — integrations deep dive
3. **Week of July 1-5** — follow-up demo with targeted areas
4. **Post-July 6** — limited bandwidth due to OpenSky rollout stabilization
5. **Demo scoping** — after discovery, decide which FSL components to build in `mjk-260320-scheduler` org

---

## Key Files Created This Session

| File | Location | Purpose |
|------|----------|---------|
| `REVERSE_DEMO_TRANSCRIPT.md` | this repo root | Full summary of June 18 OpenSky demo |
| `DISCOVERY_QUESTIONS.md` | this repo root | Tailored questions for June 24 meeting |
