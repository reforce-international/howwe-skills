---
name: stand-up-brief
description: Short brief per team before its acceleration meeting (Strategy Stand-up), from live Howwe data and with the name the customer gives the meeting. What has happened since the last meeting, what is late or due soon, which goals and initiatives it affects, and what to decide. Short enough to read aloud. Use for "prepare the stand-up", "brief for our acceleration meeting", "before the meeting", "underlag inför stand-up", "förbered strategimötet", "inför accelerationsmötet".
---

# Stand-up brief

The acceleration meeting is where strategy meets the week. This brief lets the team walk in knowing what moved, what is stuck and what it needs to decide, so the meeting is spent on commitments rather than on catching up.

Read `references/howwe-model.md` and `references/report-practice.md` before you start. Follow both. Read `references/writing-to-howwe.md` before you offer to change anything.

## 1. Team and meeting

- Call `get_current_user`, then `list_tenants`. Call the meeting by the tenant's `accelerationMeetingName`; when it is null, use the product's name in the user's language.
- Load the customer profile as described in `references/report-practice.md`, when there is one.
- Find the team: the user's own team when they belong to one, otherwise ask which. For several teams, make one brief per team.
- `list_team_acceleration_meetings`: the last held meeting (`heldAt` set) marks "since last time". The next meeting is the newest row's planned time, carried as `nextScheduledAt` on the row before it. When there is no held meeting, use the last 14 days and say so.

## 2. Get the data

- `list_team_activities` with commitments and reports: what was committed at the last meeting, what was reported since, and what is still open.
- `list_team_aggregate_targets`: the team's shared numbers.
- `list_team_milestones`: the milestones the team works on, with deadlines.
- `list_team_migs` and `read_migs`: the team's own goals, when it has any.
- Follow `supports` upward with `read_initiatives` and `read_migs` to name the initiatives and goals the work moves. Only as far as needed to name them.

## 3. What goes in

1. **Since last time.** Commitments kept, commitments not kept, and outcomes reported. Numbers with their unit.
2. **Late.** Activities and milestones past their deadline, each with its owner.
3. **Coming up.** Deadlines before the next meeting and in the two weeks after it.
4. **What it affects.** For each late or upcoming item, the initiative or goal it supports, in the customer's words.
5. **To decide in the meeting.** At most three: what to commit to, what to move, where to ask for help.

Leave out everything that is on track and not due soon. One line per item, owner's name first.

## 4. Form

- Fits on one screen and can be read aloud in two minutes.
- Heading: the meeting's name, the team and the date.
- Plain text in the conversation by default. A document only when the user asks.
- Without anything late or due, say so in one line and go straight to the decisions.

## 5. After the brief

Offer in one line to record the meeting's outcomes: reports on last period's commitments and commitments for the next. Follow `references/writing-to-howwe.md` for every change, or hand over to the report-progress skill.
