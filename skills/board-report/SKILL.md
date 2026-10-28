---
name: board-report
description: Board report on a company's or business unit's strategic plan and progress, for the board or a board committee (AU), and also for group management, a business review or a steering group. Built from live Howwe data in the customer's own language. Leads with what has been achieved, shows progress and a trend per goal, follows up earlier decisions and ends in the decisions needed now. Works for stand-alone companies and for units within a group. Use for "board report", "report to the board", "board meeting", "board committee", "styrelserapport", "rapport till styrelsen", "styrelsemöte", "AU-rapport", "arbetsutskott", "report to group management", "business review", "steering group report", "koncernrapport", "rapport till koncernledningen", "styrgrupp".
---

# Board report

The board report is the most important report a CEO makes from Howwe. It gives the people the organisation answers to a clear and convincing picture of the plan and how far the organisation has come, so that they can make decisions. That is the board or a board committee (AU) for most companies, and group management or a steering group for a unit within a group.

Convincing means leading with what has been achieved and tying each initiative to business value in the customer's own numbers. It never means hiding bad news: the summary always says plainly whether the plan is on course. Initiative owners are named; nothing more is said about individuals.

Read `references/howwe-model.md` and `references/report-practice.md` before you start. Follow both, with the exceptions this skill names.

## 1. Customer context and recipient

- Call `get_current_user`, then `list_tenants`. If the user can read several tenants, ask once which company or unit the report is for, with the format and, when unclear, the recipient in the same message.
- Load the customer profile as described in `references/report-practice.md`.
- Settle the recipient in one question if it is unclear: the board, a board committee (AU), group management, a business review or a steering group. Ask the format in the same message, as in "Before you build" in `references/report-practice.md`. The profile may say how each wants the plan framed (for example as a multi-year journey, or around a named programme).
- **The board version** is for the board and AU. They own the strategy and follow up on it: lead with whether the plan is on course for its goals, the risks to it, and the decisions only they can take. Keep execution detail to what explains the goals. At most eight pages plus appendix; a page is a slide in PowerPoint.
- **The group version** is for group management, a business review or a steering group. It shows how the unit's plan fits the group.
- **A preparatory forum.** When the profile names a forum that prepares this meeting, for example an AU some weeks before the board, this report builds on the version that forum saw and shows what has changed since.

## 2. Get the data

- `get_strategic_plan`: the published plan's title, vision, horizon, goals, initiatives, sub-initiatives and owners. APPROVED items only (see `references/howwe-model.md` for a tenant mid-workshop or without a published plan); show CANDIDATE and IDEA items in a separate box marked "proposals in preparation" only when the user asks.
- `read_migs` on each approved goal's `materializedMigId`: target, actual and attainment per period.
- `read_initiative_tree` per top-level initiative: sub-initiatives, aggregate targets and milestones. The tree already holds the sub-initiatives, so do not call it for them.
- `read_initiatives` for objectives; `read_milestones` and `read_activities` for dates and status.
- From the conversation and files, when they are there: the previous report; the minutes or decision list from the recipient's previous meeting; the version the preparatory forum saw. What is missing is asked for in the question after the analysis, never in a question of its own.

## 3. Analyse

- **What has been achieved** since the last report: milestones and initiatives completed, goals that moved. This is where the report starts.
- **Progress per goal**: target, actual and attainment, read the way the customer measures each goal.
- **Trend per goal**, as described below.
- **Business value per initiative**: the goal or the customer's own figure each initiative moves, taken from Howwe or the customer profile. Never estimate a value yourself. Without a figure, say which goal the initiative supports.
- **Earlier decisions**: per decision in the previous minutes or decision list, whether it is done, under way, not started or changed, with its owner, and the evidence in Howwe where there is one. Without minutes or a list, leave this out of the report and say so to the user in one line.
- **Since the preparatory forum**, when there is one and its version is available: what has changed in numbers, milestones and proposed decisions.
- **Milestones per month** to the end of the year, and further where objectives are dated beyond it.
- **How the plan meets the recipient's requirements**: for a unit in a group, how it feeds the group's management system (scorecards, personal goals, reviews) as the profile describes it. For the board, how it follows the strategy and targets the board has set.
- **Upcoming decision points** for the recipient: investments, capacity and structure, dependencies on other units, resources.
- **Risks and observations**: at most three, each with a proposed way to handle it.

Every section ends with what happens next, with a date.

### Trend per goal

A trend tells the board where the goal is heading at the current pace. It is not a forecast, and the report says so.

- **Only with enough data.** A goal needs reported actuals in at least three periods. With fewer, give no trend.
- **The calculation.** Fit a straight line to the reported actuals of the current plan period, at most the last twelve periods, and extend it to the goal's own last period in the plan. That is often not the calendar year-end. When the latest period is a total so far rather than a settled result (see `references/howwe-model.md`), leave it out of the line. Do the calculation in code when the client can run code; otherwise calculate by hand and keep the working with the raw data.
- **The wording.** "At the current pace we reach X against the target Y by <period>", marked as a trend. Put one line per goal in the summary.
- **Goals that a straight line misreads.** Give no trend for a goal the customer reads seasonally or over a cycle, and say why in the appendix. For a goal that is better when lower, say in which direction the trend is good.
- **The method in the appendix**: which periods, and that the trend is a straight line through them.

### Data hygiene goes to the user, not the recipient

This is an exception to "Missing data is a finding" in `references/howwe-model.md`: the finding stays, but not in the report. Gaps such as milestones without owner or deadline, initiatives without objectives, or sub-initiatives without milestones go in a separate list to the user in the conversation, each with a suggestion for what to fix in Howwe before the meeting. The recipient sees the plan and the progress.

When a gap changes a number the recipient sees, for example a goal without an actual for the latest period, say so next to that number in the report.

### The question before building

Then ask the question in "Before you build" in `references/report-practice.md`, leaving out format when it was already answered together with an earlier question, and wait for the answer. In the same message, ask for the previous minutes or decision list, and the preparatory forum's version, when they are not in the conversation or files.

**Format:** PowerPoint (.pptx), Word (.docx), PDF (.pdf) or a web page (link or .html). Recommend PowerPoint, or Word when the recipient wants to build on the text.

## 4. Structure

### Board version: the board and AU, at most eight pages plus appendix

1. Summary: what has been achieved, whether the plan is on course, one trend line per goal, and the decisions expected.
2. The plan on one page: title, vision, horizon, and how the initiatives support the goals.
3. Goals on one or two pages: target, actual, attainment, trend, and the initiatives that move each goal.
4. What has been achieved, per initiative, with owner and business value.
5. Since the preparatory forum, when there is one.
6. Follow-up of earlier decisions, when there are minutes or a decision list.
7. Decisions for the board.
8. Risks and observations, at most three, each with how to handle it.

Appendix: milestones per month, all open milestones in the period, and the method behind the trends.

### Group version: group management, a business review or a steering group

1. Summary: what has been achieved, whether the plan is on course, one trend line per goal, and the decisions expected.
2. The plan: title, vision, horizon.
3. One page per goal, with the goal as a large heading: target, actual, attainment, trend, supporting initiatives.
4. Initiatives with sub-initiatives, owners and business value.
5. Milestones per month.
6. How the plan meets the group's management requirements.
7. Since the preparatory forum, when there is one.
8. Follow-up of earlier decisions, when there are minutes or a decision list.
9. Upcoming decision points.
10. Observations and questions for the recipient.

Appendix: all open milestones in the period, and the method behind the trends.

## 5. Deliver

In the format the user chose. Large headings, clear high-contrast colours within the customer's template. Follow the form, file-name and checking rules in `references/report-practice.md`.

In the same reply, outside the file: the data hygiene list, and one line for anything the report left out for lack of material (no minutes, no preparatory version, goals without a trend).

For the company's or unit's own leadership team, use the status-report skill. Before a one-to-one with an initiative owner, use the owner-conversation skill.
