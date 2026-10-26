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
6. Keep skills customer agnostic. Customer names, people, plans and templates belong in the customer's own profile (see the `customer-profile` skill), never in this public repository.
7. Shared references (`howwe-model.md`, `report-practice.md`, `writing-to-howwe.md`) are copied into each skill that uses them, since every skill is packaged on its own. Edit one copy and copy it to the others.
8. Every skill that writes to Howwe follows `writing-to-howwe.md`: show the changes, wait for a yes, then write.
9. Write for the customer. The skills are the customer's tool: no references to Howwe staff or consultants.

## Skills

| Skill | For |
|---|---|
| `stand-up-brief` | Brief per team before the acceleration meeting |
| `my-week` | What is late, due and promised, for one person |
| `report-progress` | Report outcomes and goal actuals, commit, add activities, mark items done. Shows every change and waits for a yes |
| `initiative-status` | How one initiative is going |
| `status-report` | Status report for a company's or unit's leadership team |
| `leadership-report` | The plan and progress for the board, a board committee, group management or a steering group |
| `owner-conversation` | Brief before a one-to-one with an initiative owner |
| `customer-profile` | The customer's words, goals, routines and template, read by the report skills |

## Checks

```
python3 scripts/check_descriptions.py  # frontmatter passes claude.ai's upload rules
python3 scripts/check_tools.py   # tool names in skills exist on the MCP server
bash scripts/check_shared.sh     # shared references are identical in every skill
claude plugin validate .         # Claude plugin structure
bash scripts/build.sh            # zips per skill in dist/
```

CI runs all five on every push and every weekday morning. With the `HOWWE_MCP_TOKEN` secret set, the contract test checks against the live server; without it, against `tools.snapshot.json`.

Rule for the MCP server: tools are never renamed or removed, only deprecated.

Merging to `main` publishes to customers, since Claude picks up plugin updates from this repository.
