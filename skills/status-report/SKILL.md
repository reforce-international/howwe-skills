---
name: status-report
description: Status report on a business unit's strategy execution for its own leadership team, built from live Howwe data in the customer's own management language: goals, initiatives, milestones, execution per owner and team, and decisions for the leadership meeting. Use for "status report", "execution report", "report to the leadership team", "how are we doing against the plan", "lägesrapport", "exekveringsrapport", "rapport till LG".
---

# Status report

A report the unit's head and leadership team can act on the same day. Every section answers "what do we do now", and the report feeds the management routines the customer already runs.

Read `references/howwe-model.md` and `references/report-practice.md` before you start. Follow both.

## 1. Customer context

- Call `get_current_user`, then `list_tenants`. If the user can read several tenants, ask once which unit the report is for.
- Load the customer profile as described in `references/report-practice.md`.
- Ask the one-line question about the current situation (`references/report-practice.md`) now, before fetching data.

## 2. Get the data

- `get_strategic_plan`: the published plan's vision, goals, initiatives, sub-initiatives and owners. APPROVED items only; see `references/howwe-model.md` for a tenant mid-workshop or without a published plan.
- `read_migs` on each approved goal's `materializedMigId`: goal, actual and series.
- `read_initiative_tree` per top-level initiative, with activities: sub-initiatives, milestones, aggregate targets and activities in one call. The tree already holds the sub-initiatives, so do not call it for them.
- `read_initiatives` for objectives and purpose; `read_milestones` and `read_activities` when you need more detail.
- `list_contributing_teams` per initiative, then `list_team_acceleration_meetings` once per distinct team: when each team last held its acceleration meeting.

## 3. Analyse

- **The situation in one sentence**, with direction and two or three numbers.
- **Goals**: goal, actual, attainment and outlook, read the way the customer reads each goal. Flag placeholder goal values.
- **Leading indicators**: which initiatives and milestones explain the movement in each goal. Follow `supports`, and translate into the customer's business drivers when the profile names them.
- **Execution**: milestones done, overdue and due in the next 30 days, per initiative owner and per team or site.
- **Patterns**: initiatives without milestones in the next 60 days, sub-initiatives without owner, goals without a supporting initiative, teams that have not held their acceleration meeting recently.
- **Decisions for the leadership team**: prioritise, resource, start or stop. At most five.
- **One question per initiative owner**, including the head's own initiatives, each with a number or date.
- **Into the routines**: per initiative, the indicators, reports and next steps that go straight into the customer's own follow-up (scorecard, monthly report, personal goals) as the profile names them.

## 4. Structure

1. Masthead: "Status report <unit>", date and a two-sentence lede.
2. The situation in one sentence.
3. Goals as KPI tiles.
4. Leading indicators.
5. Execution per owner and per team or site.
6. Decisions for the leadership team.
7. Action cards: one question per initiative owner.
8. Into the routines: indicators, reports and next steps per initiative.
9. A 60-minute agenda for the next leadership meeting.
10. Cadence: acceleration meeting weekly, leadership meeting and report monthly, review quarterly, unless the profile says otherwise.

## 5. Deliver

PDF by default, slides when asked. Follow the form, file-name and checking rules in `references/report-practice.md`. Offer an English version in one line when part of the leadership team works in English.

For the board, a board committee, group management or a steering group, use the leadership-report skill. Before the team's acceleration meeting, use the stand-up-brief skill. Before a one-to-one with an initiative owner, use the owner-conversation skill.
