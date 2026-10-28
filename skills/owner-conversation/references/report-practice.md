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

This applies to reports delivered as a document. Each report skill names its formats and its recommendation in its own SKILL.md.

1. **Fetch and analyse first.** Reading changes nothing and does not depend on the format, so do not stop to ask before it. When a question has to be asked before fetching (which tenant or unit, which owner, which initiative, which recipient), ask the format question in the same message, so the user answers both at once.
2. **Then ask once, and wait for the answer.** Ask about what is still open:
    - **Format**, always written with the file type: PowerPoint (.pptx), Word (.docx), PDF (.pdf) or a web page (link or .html). Put the recommended one first, mark it as recommended and say why in a few words. The recommendation is the format the customer profile gives for this recipient, otherwise PowerPoint (.pptx). Ask for every report: a format chosen for an earlier report does not carry over, and a saved default format, in the profile or the user's own preferences, is the recommendation, never a reason to skip. Skip the question only when the user has already named a format for this report.
    - **Template, only when the customer profile has none and the user has given no file.** Ask whether there is a template or an earlier report to take colours, fonts and logo from.
    - **The current situation.** Is anything right now affecting how the numbers should be read (a disruption, a reorganisation, budget work)? Use recent reports in the conversation or files when they exist.
    - **The outline, when this is the first report for the customer or there is no profile.** Five lines: verdict, the three main observations, the decisions you will propose.
3. **Build** from the answer, without asking again. When the answer about the situation changes how a number should be read, say so in the report.

**Asking well.** Put everything in one message that reads as a single question with a proposal for each part, so the user can answer with one word or a short line. For example: "Shall I make a PowerPoint file (.pptx, recommended), with no special situation to account for and this angle: ...? Or tell me what to change: Word (.docx), PDF (.pdf) or a web page." The user's own rules about how many questions to ask, or whether to ask at all, come first. When they leave no room for a question, or nobody can answer (a scheduled or unattended run), do not ask: build in the recommended format, PowerPoint (.pptx) unless the profile says otherwise, and say in the first line which format you chose and that it can be changed, then which situation and angle you assumed.

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

- Use the customer's own template (colours, fonts, logo) from the customer profile or from files the user provides. When there is none, the one question in "Before you build" has asked for it; if the user has none, use a clean, neutral, high-contrast layout. Never stop to ask about the template separately.
- Deliver in the format the user chose: PowerPoint (.pptx), Word (.docx), PDF (.pdf), or a web page. When a format cannot be made here, say so in the question and offer the closest one.
- **PowerPoint means a .pptx file**, made with the client's own tool for PowerPoint files when it has one. When the user chooses PowerPoint, always deliver a .pptx file. A presentation viewed in the browser, or a link to slides, is a web page: make one only when the user asks for a shareable link.
- **A web page** is one self-contained page. Publish it as a shareable link when the client can, private to the user until they share it. Otherwise deliver it as a single .html file. Never publish customer data where anyone with the address can read it without the user choosing to share it.
- File name: `<Customer>-<Unit>-<Report>-<YYYY-MM-DD>`, ASCII only.
- Language: the customer profile's language, or the user's.

## Check before delivering

- Every number and date matches the raw data.
- Every owner name is spelled as in Howwe.
- No Howwe system term is visible where the customer has its own word.
- Every observation has an action, owner and date.
- When you produced a file, open it and look at every page.
