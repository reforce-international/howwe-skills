---
name: leadership-report
description: Persuasive report on a business unit's strategic plan and progress for group management, a business review or a programme steering group, built from live Howwe data in the customer's own language. Focuses on goals and initiatives, names initiative owners, and ends in the decisions that are needed. Use for "report to group management", "business review", "steering group report", "board briefing on the strategy", "koncernrapport", "rapport till koncernledningen", "styrgrupp".
---

# Leadership report

Give group management, or a steering group, a clear and convincing picture of the unit's plan and how far the organisation has come, so that they can make decisions. The focus is goals and initiatives. Initiative owners are named; nothing more is said about individuals.

Read `references/howwe-model.md` and `references/report-practice.md` before you start. Follow both.

## 1. Customer context and recipient

- Call `get_current_user`, then `list_tenants`. If the user can read several tenants, ask once which unit the report is for.
- Load the customer profile as described in `references/report-practice.md`.
- Ask the one-line question about the current situation (`references/report-practice.md`).
- Settle the recipient in one question if it is unclear: group management, a business review or a steering group. The profile may say how each wants the plan framed (for example as a multi-year journey, or around a named programme).

## 2. Get the data

- `get_strategic_plan`: the published plan's title, vision, horizon, goals, initiatives, sub-initiatives and owners. APPROVED items only (see `references/howwe-model.md` for a tenant mid-workshop or without a published plan); show CANDIDATE and IDEA items in a separate box marked "proposals in preparation" only when the user asks.
- `read_migs` on each approved goal's `materializedMigId`: goal, actual and attainment per period.
- `read_initiative_tree` per top-level initiative: sub-initiatives, aggregate targets and milestones. The tree already holds the sub-initiatives, so do not call it for them.
- `read_initiatives` for objectives; `read_milestones` and `read_activities` for dates and status.
- The previous report, when it is in the conversation or files, to show what has changed.

## 3. Analyse

- **The plan as a whole**: the goals and how the initiatives support them.
- **Progress per goal**: goal, actual and attainment, read the way the customer measures each goal.
- **Milestones per month** to the end of the year, and further where objectives are dated beyond it.
- **Since the last report**: completed, moved and new.
- **How the plan meets the group's requirements**: how it feeds the customer's own management system (scorecards, personal goals, reviews) as the profile describes it.
- **Upcoming decision points** for the recipient: investments, capacity and structure, dependencies on other units, resources.
- **Risks and observations**: at most three, each with a proposed way to handle it.

Every section ends with what happens next, with a date.

## 4. Structure

1. Summary: the situation in three sentences, and the decisions expected.
2. The plan: title, vision, horizon.
3. One page per goal, with the goal as a large heading: goal, actual, attainment, supporting initiatives.
4. Initiatives with sub-initiatives and owners.
5. Milestones per month.
6. How the plan meets the group's management requirements.
7. Upcoming decision points.
8. Observations and questions for the recipient.
9. Appendix: all open milestones in the period.

## 5. Deliver

Slides by default; an editable document when the recipient wants to build on it; PDF on request. Large headings, clear high-contrast colours within the customer's template. Follow the form, file-name and checking rules in `references/report-practice.md`.

For the unit's own leadership team, use the status-report skill. Before a one-to-one with an initiative owner, use the owner-conversation skill.
