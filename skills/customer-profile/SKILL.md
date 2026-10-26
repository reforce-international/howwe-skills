---
name: customer-profile
description: Set up or update a Howwe customer profile: the customer's own words for goals, initiatives and forums, how each goal is read, who owns what, their management routines, report template and house rules. The report skills read it so that reports fit the customer from the first draft. Use for "set up a customer profile", "teach Claude about <customer>", "update the profile", "kundprofil", or when a report skill offers to create one.
---

# Customer profile

The difference between a generic report and one that fits the customer is context: their words, their forums, how they read their goals and what they want from a report. The customer profile writes that context down once, so every report starts from it.

The profile belongs to the customer and the consultant. It never goes into this repository.

## 1. Start from Howwe

- Call `get_current_user` and `list_tenants`. One profile can cover several tenants of the same customer; ask which ones belong together.
- Per tenant: `get_strategic_plan` for the published plan's title, vision, horizon, goals, initiatives and owners (not the workshop draft); `read_migs` on the approved goals for units and period types; `accelerationMeetingName` from `list_tenants`.
- Fill in everything this answers in `references/profile-template.md`. Mark it as "from Howwe" with today's date: owners and initiatives change, so the profile records them as a snapshot and the reports always verify them live.

## 2. Ask for what Howwe cannot know

Ask in one message, as a short numbered list, only for what is still missing:

1. What do you call the levels? (goals, initiatives, sub-initiatives, milestones, activities, the acceleration meeting) Offer the app names from `references/howwe-model.md` as defaults.
2. How should each goal be read? (better when lower, over a cycle, rolling twelve months, relative to competitors)
3. Which forums and routines does the strategy feed? (leadership meeting, monthly report, quarterly review, scorecards, personal goals)
4. Words and names the customer uses about their own business, and words to avoid.
5. Who receives the reports, and what does each recipient want to see?
6. Template: colours, fonts, logo, or a file to take them from.

Also use what you already know from the conversation, attached files (earlier reports, presentations, strategy documents) and memory. Anything from earlier reports the user liked is the best guide to what they expect.

## 3. Write and save it

Write the profile following `references/profile-template.md`, in the customer's language. Show it, ask for corrections, then save it where the user will have it next time: as a project file, a document they attach, or in memory when that is available. Name it "Howwe customer profile <Customer>".

## 4. Update

After a report, when the user corrects a word, a reading of a goal or the form, offer in one line to add it to the profile. Small corrections compound: this is how the reports become as good as the consultant's own.
