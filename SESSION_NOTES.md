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
