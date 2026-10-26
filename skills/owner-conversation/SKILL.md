---
name: owner-conversation
description: One-page brief from live Howwe data before a manager's one-to-one with the owner of an initiative, in the customer's own language: purpose, objectives, milestones, what is overdue, what is due, where the manager can help, and three questions. Also prepares planning sessions that fill gaps in an owner's plan. Use for "one-to-one with <name>", "prepare my conversation with <name>", "what should I raise with <name>", "ägarsamtal", "underlag inför samtal med <name>".
---

# Owner conversation

One page that lets the manager walk into the conversation with the whole picture of the owner's initiative, and three questions that move execution forward. The tone is supportive and concrete. The brief describes work and commitments, never the person.

Read `references/howwe-model.md` and `references/report-practice.md` before you start. Follow both.

## 1. Customer context and owner

- Call `get_current_user`, then `list_tenants`. If the user can read several tenants, ask once which unit is meant.
- Load the customer profile as described in `references/report-practice.md`.
- Find the owner with `list_users` (`nameContains`) and confirm with `read_users` if several match.
- Find the owner's initiatives with `get_user_assignments` for the owner's user id and tenant, with types limited to initiatives. If there are several, cover all of them or ask which one the conversation is about.

## 2. Get the data

- `read_initiative_tree` per initiative the owner holds, with activities, skipping any that already appear inside another's tree: sub-initiatives, milestones, aggregate targets, activities and the teams behind them.
- `read_initiatives` for purpose and objectives.
- `read_migs` for the goals each initiative supports, following `supports`.
- `list_contributing_teams`, then `list_team_acceleration_meetings` once per distinct team: when each team last held its acceleration meeting.
- The brief from the previous conversation, when it is in the conversation or files: what was agreed and what was to be followed up.

## 3. Analyse

- **The initiative**: purpose and objectives as they stand in Howwe.
- **Commitments**: sub-initiatives and milestones with dates, as done, in progress and overdue.
- **Link to the goals**: which goal each commitment supports, and how much that goal depends on this initiative.
- **Next 30 days**: what falls due and what it takes to hold the plan.
- **Local ownership**: which teams or sites have planned activities against the milestones, and where nobody has.
- **Patterns**: recurring delays, dependencies on other initiatives or units, milestones without activities behind them, sub-initiatives without milestones.
- **Where the manager can help**: decisions, resources or priorities that sit with the manager.
- **Three questions**, open, each tied to a number or a date.
- **One next step** to agree in the conversation and follow up next time, phrased so it goes straight into the owner's personal goals or scorecard as the profile describes them.

## 4. Structure (one page, two at most)

1. Heading: owner's name, initiative, date of the conversation.
2. The situation in two sentences.
3. Purpose and objectives.
4. Commitments: done, in progress, overdue.
5. Next 30 days.
6. Where I as manager can help.
7. Three questions.
8. Follow-up from the last conversation, when there is an earlier brief.

## 5. Variant: planning session

When the manager or a support function plans with an owner: the same data, with the focus on what is missing from the plan. Initiatives without purpose, initiatives without objectives, sub-initiatives without milestones, milestones without owner or deadline. Milestones should be concrete results with a deadline, four to six per sub-initiative. End with proposed milestones for the owner to decide on. Do not create them in Howwe from this skill; if the owner wants them added, confirm first and then use the relevant create tool.

## 6. Deliver

One page, PDF by default. File name `<Customer>-<Unit>-Owner-conversation-<Firstname-Lastname>-<YYYY-MM-DD>`. Follow the form and checking rules in `references/report-practice.md`. Write in the owner's working language.
