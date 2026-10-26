#!/usr/bin/env python3
"""Contract test: every Howwe MCP tool named in a skill must exist on the server.

Tool names come from the live server when HOWWE_MCP_TOKEN is set, otherwise
from tools.snapshot.json. Run with --update-snapshot to refresh the snapshot
from the live server.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "tools.snapshot.json"
MCP_URL = os.environ.get("HOWWE_MCP_URL", "https://api.howwe.io/v1/mcp")
# Tool names are snake_case and wrapped in backticks in SKILL.md files.
TOOL_REF = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")


def rpc(method, params, token, session=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Authorization": f"Bearer {token}",
    }
    if session:
        headers["Mcp-Session-Id"] = session
    req = urllib.request.Request(MCP_URL, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode()
        sid = resp.headers.get("Mcp-Session-Id", session)
    # Streamable HTTP may answer as SSE; take the last data line.
    if raw.lstrip().startswith("event:") or "\ndata:" in raw:
        raw = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")][-1]
    return json.loads(raw), sid


def live_tools(token):
    _, sid = rpc("initialize", {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "howwe-skills-ci", "version": "1"},
    }, token)
    names, cursor = [], None
    while True:
        res, sid = rpc("tools/list", {"cursor": cursor} if cursor else {}, token, sid)
        result = res["result"]
        names += [t["name"] for t in result["tools"]]
        cursor = result.get("nextCursor")
        if not cursor:
            return sorted(set(names))


def main():
    token = os.environ.get("HOWWE_MCP_TOKEN")
    if "--update-snapshot" in sys.argv:
        if not token:
            sys.exit("HOWWE_MCP_TOKEN is required to update the snapshot")
        SNAPSHOT.write_text(json.dumps(live_tools(token), indent=2) + "\n")
        print(f"Snapshot updated: {SNAPSHOT.name}")
        return

    if token:
        tools, source = set(live_tools(token)), "live server"
    else:
        tools, source = set(json.loads(SNAPSHOT.read_text())), SNAPSHOT.name

    missing = []
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        for name in sorted(set(TOOL_REF.findall(skill.read_text()))):
            if name not in tools:
                missing.append(f"{skill.relative_to(ROOT)}: `{name}`")

    if missing:
        print(f"Tools referenced in skills but missing on the MCP server ({source}):")
        print("\n".join(f"  {m}" for m in missing))
        sys.exit(1)
    print(f"OK: all tool references found ({source}).")


if __name__ == "__main__":
    main()
