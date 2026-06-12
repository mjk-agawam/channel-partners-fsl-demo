# Scripts

## org62_query.py

Queries Salesforce org62 (internal CRM) via the Salesforce Platform MCP (sobject-reads endpoint).

**Auth:** Reads the OAuth token from the macOS Keychain (same entry Claude Desktop uses). Auto-refreshes on expiry.

**Usage:**
```bash
# SOQL query
python3 scripts/org62_query.py "SELECT Id, Name, StageName, Amount FROM Opportunity WHERE Id = '006ed00000YQ5i1AAD'"

# Full-text search
python3 scripts/org62_query.py --find "Channel Partners"

# Force token refresh (run if queries fail with auth errors)
python3 scripts/org62_query.py --refresh
```

**Requirements:** macOS only (uses `security` CLI to read from Keychain). Requires the Org62-Sobject-Read MCP to be authenticated in Claude Desktop at least once to populate the Keychain entry.
