#!/usr/bin/env python3
"""
org62_query.py — Query org62 via the Salesforce Platform MCP (sobject-reads).

Usage:
    python3 org62_query.py "SELECT Id, Name FROM Opportunity WHERE Id = '006ed00000YQ5i1AAD'"
    python3 org62_query.py --find "Channel Partners"
    python3 org62_query.py --related Deal_Support_Request__c a25ed000001yhxZAAQ

Reads the live access token from the macOS Keychain (same entry Claude uses).
If the token is expired, refreshes it automatically and updates the Keychain +
~/.cursor/mcp.json.
"""

import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

KEYCHAIN_ACCOUNT = "mikeknight"
KEYCHAIN_KEY = "Org62-Sobject-Read|bd86247d2b654d1d"
MCP_URL = "https://api.salesforce.com/platform/mcp/v1/platform/sobject-reads"
OAUTH_CLIENT_ID = "3MVG9WQsPp5nH_EpM_KnrLdttExiAuzLoaVZkfx52M1ORCimCnoSOKvZzy2bABbcT0dhhi80GJKgFbKkP4Rhf"
TOKEN_URL = "https://org62.my.salesforce.com/services/oauth2/token"
CURSOR_MCP_JSON = "/Users/mikeknight/.cursor/mcp.json"


# ---------------------------------------------------------------------------
# Keychain helpers
# ---------------------------------------------------------------------------

def _keychain_read() -> dict:
    result = subprocess.run(
        ["security", "find-generic-password", "-a", KEYCHAIN_ACCOUNT, "-g"],
        capture_output=True, text=True,
    )
    output = result.stdout + result.stderr
    match = re.search(r'password: "(.+)"', output, re.DOTALL)
    if not match:
        raise RuntimeError("Could not read MCP OAuth tokens from keychain")
    return json.loads(match.group(1))


def _keychain_write(data: dict) -> None:
    payload = json.dumps(data)
    subprocess.run(
        ["security", "add-generic-password", "-a", KEYCHAIN_ACCOUNT,
         "-s", "claude-code", "-w", payload, "-U"],
        check=True, capture_output=True,
    )


def get_tokens() -> tuple[str, str]:
    """Return (access_token, refresh_token), refreshing if expired."""
    data = _keychain_read()
    entry = data.get("mcpOAuth", {}).get(KEYCHAIN_KEY, {})
    access_token = entry.get("accessToken", "")
    refresh_token = entry.get("refreshToken", "")

    if _is_expired(access_token):
        print("[org62] Access token expired, refreshing...", file=sys.stderr)
        access_token = _refresh(refresh_token, data)

    return access_token, refresh_token


def _is_expired(token: str) -> bool:
    if not token:
        return True
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return True
        padding = parts[1] + "=="
        import base64
        payload = json.loads(base64.urlsafe_b64decode(padding))
        return payload.get("exp", 0) < time.time() + 60  # 60s buffer
    except Exception:
        return True


def _refresh(refresh_token: str, keychain_data: dict) -> str:
    body = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "client_id": OAUTH_CLIENT_ID,
        "refresh_token": refresh_token,
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read())

    new_token = result.get("access_token", "")
    if not new_token:
        raise RuntimeError(f"Token refresh failed: {result}")

    # Update keychain
    keychain_data["mcpOAuth"][KEYCHAIN_KEY]["accessToken"] = new_token
    if "refresh_token" in result:
        keychain_data["mcpOAuth"][KEYCHAIN_KEY]["refreshToken"] = result["refresh_token"]
    _keychain_write(keychain_data)

    # Update ~/.cursor/mcp.json
    _update_cursor_mcp(new_token)

    print("[org62] Token refreshed successfully.", file=sys.stderr)
    return new_token


def _update_cursor_mcp(token: str) -> None:
    try:
        with open(CURSOR_MCP_JSON) as f:
            config = json.load(f)
        servers = config.get("mcpServers", {})
        if "Org62-Sobject-Read" in servers:
            servers["Org62-Sobject-Read"]["headers"] = {"Authorization": f"Bearer {token}"}
            with open(CURSOR_MCP_JSON, "w") as f:
                json.dump(config, f, indent=2)
    except Exception as e:
        print(f"[org62] Warning: could not update Cursor MCP config: {e}", file=sys.stderr)


# ---------------------------------------------------------------------------
# MCP session
# ---------------------------------------------------------------------------

class Org62Session:
    def __init__(self):
        self.token, _ = get_tokens()
        self.session_id = self._initialize()

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "mcp-session-id": self.session_id,
        }

    def _post(self, method: str, params: dict = None, req_id: int = 1,
              notif: bool = False) -> dict | None:
        msg: dict = {"jsonrpc": "2.0", "method": method, "params": params or {}}
        if not notif:
            msg["id"] = req_id
        h = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        if hasattr(self, "session_id"):
            h["mcp-session-id"] = self.session_id
        payload = json.dumps(msg).encode()
        req = urllib.request.Request(MCP_URL, data=payload, headers=h, method="POST")
        with urllib.request.urlopen(req, timeout=20) as resp:
            if not hasattr(self, "session_id"):
                self.session_id = dict(resp.headers).get("mcp-session-id", "")
            body = resp.read().decode()
        if not body.strip():
            return None
        if body.strip().startswith("data:"):
            for line in body.split("\n"):
                if line.startswith("data:"):
                    return json.loads(line[5:].strip())
        return json.loads(body)

    def _initialize(self) -> str:
        msg = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "org62_query", "version": "1.0"},
        }}
        payload = json.dumps(msg).encode()
        h = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        req = urllib.request.Request(MCP_URL, data=payload, headers=h, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            sid = dict(resp.headers).get("mcp-session-id", "")
            resp.read()
        # Send initialized notification
        self.session_id = sid
        self._post("notifications/initialized", notif=True)
        return sid

    def _tool(self, name: str, args: dict, req_id: int = 10) -> str:
        resp = self._post("tools/call", {"name": name, "arguments": args}, req_id=req_id)
        if resp is None:
            return ""
        content = resp.get("result", {}).get("content", [])
        return content[0].get("text", "") if content else ""

    def soql(self, query: str) -> dict:
        text = self._tool("soqlQuery", {"q": query})
        return json.loads(text) if text else {}

    def find(self, query: str) -> dict:
        text = self._tool("find", {"q": query})
        return json.loads(text) if text else {}

    def related(self, sobject: str, record_id: str, path: str) -> dict:
        text = self._tool("getRelatedRecords", {
            "sobject-name": sobject, "id": record_id, "relationship-path": path
        })
        return json.loads(text) if text else {}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_records(data: dict) -> None:
    records = data.get("records") or data.get("searchRecords", [])
    if not records:
        print("No records returned.")
        return
    for rec in records:
        print()
        for k, v in rec.items():
            if k == "attributes":
                continue
            if isinstance(v, dict):
                v = v.get("Name", v)
            if v is not None:
                print(f"  {k}: {v}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    session = Org62Session()

    if args[0] == "--find":
        result = session.find(" ".join(args[1:]))
        _print_records(result)
    elif args[0] == "--related" and len(args) >= 4:
        result = session.related(args[1], args[2], args[3])
        _print_records(result)
    elif args[0] == "--refresh":
        # Force token refresh and update Cursor
        _, refresh_token = get_tokens()
        data = _keychain_read()
        _refresh(refresh_token, data)
        print("Done. Cursor mcp.json updated.")
    else:
        result = session.soql(" ".join(args))
        _print_records(result)


if __name__ == "__main__":
    main()
