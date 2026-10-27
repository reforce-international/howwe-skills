---
name: initiative-status
description: Summarize how a Howwe initiative is progressing, using Howwe's best practice for strategy execution. Use when someone asks how an initiative, objective or strategic bet is going, whether it is on track, or what needs attention before a review.
---

# Initiative status

Give an honest, decision-ready picture of how one initiative is doing, based on live data from Howwe.

## 1. Find the initiative

- Start with `get_current_user` to learn who is asking and which tenant they belong to.
- If the user names the initiative, find it with `list_initiatives` using `nameContains`. If several match, ask which one they mean.
- If they do not name one, call `get_user_assignments` and offer the initiatives they own or contribute to.

## 2. Read the whole tree in one call

Call `read_initiative_tree` with the initiative id, and ask for activities. This returns the initiative, every supporting initiative, milestone and aggregate target, and their activities. Do not walk the tree one level at a time.

The tree leaves out the goals the initiative supports. Read the root with `read_initiatives`, follow its `supports` to the goals, and read them with `read_migs`, so you can judge whether they are moving at the expected pace.

If you need descriptions or objectives, read those items with `read_initiatives` or `read_milestones`.

## 3. Assess it with Howwe's best practice

Read `references/best-practice.md` and assess the initiative against it. Read `references/howwe-model.md` for how to read the data, above all goal series: reported actuals are results, also for a period that has not ended. Base every judgement on the data. If something is missing, say so instead of guessing.

## 4. Answer

Use this structure, in the user's language:

1. **Verdict.** One sentence: on track, at risk or off track, and why.
2. **What is moving.** Milestones and activities completed or progressing.
3. **What needs attention.** Overdue milestones, stale activities, missing owners, targets falling behind. Name the owner of each item.
4. **Suggested next steps.** At most three, concrete, each with a suggested owner.

Keep it short enough to read aloud in an acceleration meeting. Use the tenant's own name for the acceleration meeting (from `list_tenants`, field `accelerationMeetingName`).

Do not change anything in Howwe from this skill. If the user wants to act on a next step, confirm first and then use the relevant update tool.
