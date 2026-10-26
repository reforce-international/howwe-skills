# How the reports are written

> Shared reference. Identical copies live in each skill that uses it; CI fails if they differ. Edit one and copy it to the others.

The practice behind every report these skills make, whoever it is for.

## Principles

- **Decision-ready.** Every section answers "what do we do now". Lead with the conclusion, then the evidence.
- **Every observation gets an action**, with an owner and a date.
- **Owners, not teams.** Name the person responsible for each item. Describe work and commitments, never the person.
- **Local ownership.** The teams and sites that plan activities against milestones own the execution. Write so that they recognise themselves as owners.
- **Questions that move things.** Open questions ("what would it take to ...", "what is stopping ..."), each tied to a number or a date.
- **The customer's language.** Use the customer's names for goals, initiatives, forums and roles, from the customer profile. Howwe's system terms appear only in tool calls, never in the report.
- **The customer's rhythm.** Tie next steps to the forums the customer already runs (acceleration meeting, leadership meeting, monthly report, quarterly review), so the report feeds their existing management system.

## The customer profile

The customer profile is a document called "Howwe customer profile <Customer>", made with the customer-profile skill. Look for it in the conversation, attached files, project files and memory. When you find it, its vocabulary, goal-reading rules, forums, recipients, template and house rules apply to the whole report and override the defaults here and in `howwe-model.md`. Owners and initiatives in it are a snapshot: verify them live in Howwe.

Without a profile, use the tenant's own name for the acceleration meeting and the app names in `howwe-model.md`, and offer once, after the report, to set up a profile.

## Before you build

1. **Ask once about the current situation.** One line: is anything right now affecting how the numbers should be read (a disruption, a reorganisation, budget work)? Use recent reports in the conversation or files when they exist.
2. **First report for this customer, or no profile?** Show a five-line outline first (verdict, the three main observations, the decisions you will propose) and ask whether it matches what they expect. It is much cheaper to correct the angle here than after the document is built.

## Working with the data

- Save the raw tool answers when you can, and do counts, dates and percentages in code. When you cannot run code, count from the data and keep the counts visible while you write.
- Today's date decides what is overdue and what is due in the next 30 or 60 days. State the date the report is based on.

## Writing rules

- Short sentences. Verb first in actions.
- Positive phrasing: say what to do, not what to avoid.
- No dashes as sentence punctuation. No "not X but Y" constructions.
- Numbers with unit and period. Dates as the customer writes them.
- Follow any further house rules in the customer profile.

## Form

- Use the customer's own template (colours, fonts, logo) from the customer profile or from files the user provides. When there is none, ask once for one; if the user has none, use a clean, neutral, high-contrast layout.
- File name: `<Customer>-<Unit>-<Report>-<YYYY-MM-DD>`, ASCII only.
- Language: the customer profile's language, or the user's.

## Check before delivering

- Every number and date matches the raw data.
- Every owner name is spelled as in Howwe.
- No Howwe system term is visible where the customer has its own word.
- Every observation has an action, owner and date.
- When you produced a file, open it and look at every page.
