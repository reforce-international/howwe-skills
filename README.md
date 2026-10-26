# Howwe skills

Skills for working with Howwe in Claude, ChatGPT and Microsoft Copilot. One source of truth for the methodology, packaged per platform.

The skills use the [Howwe MCP server](https://claude.ai/directory/howwe) (`https://api.howwe.io/v1/mcp`). Every user signs in with their own Howwe account.

## Structure

```
skills/<name>/SKILL.md            the skill (open Agent Skills format)
skills/<name>/references/         Howwe methodology the skill reads
skills/<name>/agents/openai.yaml  optional ChatGPT display metadata
.claude-plugin/plugin.json        Claude plugin manifest
.claude-plugin/marketplace.json   lets this repo act as a Claude marketplace
.mcp.json                         Howwe MCP connector for the Claude plugin
tools.snapshot.json               known MCP tool names for the contract test
```

## Install

**Claude.** Install the Howwe plugin from the Claude directory. Before it is listed, an admin can add this repository as a plugin marketplace and make the plugin required for the organization.

**ChatGPT.** Upload `dist/<skill>.zip` under Skills.

**Microsoft Copilot Studio.** Add the skill to an agent under Skills, using `dist/<skill>.zip`.

## Writing skills

1. Keep the frontmatter to `name` and `description`. Nothing platform specific.
2. Refer to Howwe MCP tools by name in backticks, for example `read_initiative_tree`. Never refer to a specific AI product's UI.
3. Put methodology in `references/`, keep `SKILL.md` short.
4. No scripts for now. Plain Markdown works everywhere.
5. Test each skill in Claude, ChatGPT and Copilot before release.

## Checks

```
python3 scripts/check_tools.py   # tool names in skills exist on the MCP server
claude plugin validate .         # Claude plugin structure
bash scripts/build.sh            # zips per skill in dist/
```

CI runs all three on every push and every weekday morning. With the `HOWWE_MCP_TOKEN` secret set, the contract test checks against the live server; without it, against `tools.snapshot.json`.

Rule for the MCP server: tools are never renamed or removed, only deprecated.

Merging to `main` publishes to customers, since Claude picks up plugin updates from this repository.
