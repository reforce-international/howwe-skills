---
name: report-progress
description: Update Howwe from the conversation, always showing the changes and waiting for a yes before writing. Report progress or an outcome on an activity, report a goal's actual, commit to activities for the coming period, tick off kept commitments, add a new activity, or mark an activity or milestone as done. Use for "report our progress", "log that we did", "we reached", "we did what we promised", "mark the milestone as done", "add an activity", "commit to an activity", "what we will do before the next stand-up", "rapportera utfall", "bocka av", "lägg upp en aktivitet", "vi har nått".
---

# Report progress

Let a team keep Howwe up to date straight from the conversation: outcomes, goal actuals, commitments, new activities and completed items. Nothing is written until the user has seen exactly what will change and said yes.

Read `references/writing-to-howwe.md` and `references/howwe-model.md` before you start. Follow both. The writing rules apply to every change, including small ones.

## 1. Find the user and the items

- Call `get_current_user`, then `list_tenants`. Use the tenant's `accelerationMeetingName` when you talk about the meeting.
- Start from `get_user_assignments` for what the user owns. When the user speaks for a team, use `list_team_activities` and `list_team_milestones` for that team.
- Match what the user says to items in Howwe. When two items could fit, ask which one. Never create a new item because a match is uncertain.

## 2. Work out the changes

| The user says | Tool | Read first |
|---|---|---|
| What was done, or how much, on an activity | `create_activity_report` (value and/or note) | `read_activities` with commitments and reports, for the unit and earlier reports |
| What a goal reached in a period | `report_mig_actual` | `read_migs`, for the period's `targetDate`, the rev and any actual it replaces |
| What the team will do before the next meeting | `create_activity_commitment` | the activity, to check that it has an assignee and a target |
| A promise from the last meeting is kept | `complete_activity_commitment` | `read_activities` with commitments and reports, for the commitment id and the rev |
| A new piece of work | `create_activity`, with `assigneeId` | the team, the initiative or milestone it supports, and who owns it. Ask for the owner: without one the activity cannot be committed to |
| The work itself is finished for good | `complete_item` for an activity or milestone | the item with its `read_*` tool, for the rev |

A report on a commitment counts towards it: pass the `commitmentId` when the user reports on what they committed to.

**A kept promise is not a finished activity.** "We did what we promised" ticks off the commitment with `complete_activity_commitment`; the activity stays open for the next period. Use `complete_item` on an activity only when the user says the work as a whole is done or will not continue. When it is unclear which they mean, ask.

## 3. Show, confirm, write

Follow `references/writing-to-howwe.md`: one list, a clear yes, then the writes, then a short confirmation of what Howwe now holds.

## 4. After writing

Offer one natural next step in a line, for example to commit to the next period after reporting the last one, or to prepare the acceleration meeting with the stand-up-brief skill. Do not write anything more without a new yes.
