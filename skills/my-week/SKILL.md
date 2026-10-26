---
name: my-week
description: Personal overview for anyone working in Howwe, not only managers. What is late, what is due in the next few days and what I have committed to, with the goal or initiative each item moves. Use for "my week", "what do I need to do", "what is late", "what have I promised", "what is on my plate", "min vecka", "vad ska jag göra", "vad har jag lovat", "vad är sent".
---

# My week

Most people come to Howwe to see what is theirs to do. This gives one person their own picture in a minute: what is late, what is due, what they have promised the team and why it matters.

Read `references/howwe-model.md` before you start. Read `references/writing-to-howwe.md` before you offer to change anything.

## 1. Get the data

- `get_current_user` for who the user is and which teams they belong to. Call `list_tenants` for the tenant's `accelerationMeetingName`.
- `get_user_assignments` with no arguments: the user's open initiatives, milestones and activities, with deadlines.
- `read_activities` with commitments and reports on the user's activities: what they committed to at the last acceleration meeting and what they have reported.
- `list_team_acceleration_meetings` for the user's teams: when the next meeting is, since commitments fall due before it.
- Resolve what the items support with `read_initiatives`, `read_milestones` or `read_migs`, only to name them.

Today's date decides what is late and what is due. Count "the next few days" as the next seven days, or until the next acceleration meeting when that is later.

## 2. What goes in

1. **Late.** Past its deadline and not done.
2. **Due soon.** Due within the window, in date order.
3. **My commitments.** What the user promised at the last meeting, how far they have come, and when it is due.
4. **Why it matters.** For the two or three most important items, the initiative or goal it moves, in one short line.

Use the customer's names for items and for the meeting. Address the user directly ("you"). Describe the work, never judge the person.

## 3. Form

Short and scannable, in the conversation. Nothing late? Say so first. Nothing at all? Say that too, and suggest looking at the team's milestones.

## 4. After the overview

Offer in one line to report progress or mark something as done. Follow `references/writing-to-howwe.md` for every change, or hand over to the report-progress skill.
