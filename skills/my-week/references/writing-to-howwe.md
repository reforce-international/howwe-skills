# Writing to Howwe

> Shared reference. Identical copies live in each skill that uses it; CI fails if they differ. Edit one and copy it to the others.

How to change anything in the customer's Howwe. Follow it every time a skill writes, whatever the user asked for.

## Show first, then write

1. **Collect everything before writing anything.** When the user reports several things at once, gather them all first.
2. **Show exactly what you will write**, as a short list: one line per change, with the item's name as it stands in Howwe, the field and the new value. For a number, also show what it was before, when there was one.
3. **Wait for a clear yes.** "Yes", "go ahead" or the same in the user's language. Anything else, including silence or a new question, is not a yes. Change the list and show it again when the user corrects something.
4. **Write only what you showed.** Nothing more, nothing in addition.
5. **Confirm what was written**, item by item, with the value Howwe answered with. Say plainly what failed and why.

Ask again for each new batch of changes. A yes covers the list it answered, never later changes.

## Writing safely

- **Read before you change.** Tools that change an item need its `rev`. Take it from a `read_*` call or the answer of the change before, never from memory. When a call is refused because the item has changed, read it again, show the user what changed and ask before retrying.
- **Reports add, they do not replace.** `create_activity_report` logs an increment, not a new total. When the user gives a total ("we are at 40 now"), work out the increment from the activity's reports and show both numbers.
- **Goal actuals replace.** `report_mig_actual` replaces any actual already in that period. Read the goal first with `read_migs` and show the number it replaces. When the goal takes its actuals from an external source (`externallyUpdated`), say that a later sync may overwrite the number.
- **Commitments need an assignee.** An activity without an assignee cannot be committed to. Ask who owns it rather than guessing.
- **Never create a user, delete or archive anything** from these skills. When the user asks for that, explain that it is done in the Howwe app, or by asking for it directly in a separate request.
- **The user's own rights apply.** Howwe only lets the user change what they may change in the app. When a call is refused for lack of rights, say so and suggest who can do it.

## Language

Write titles and notes in the user's own words and language. Use the customer's names for items and for the acceleration meeting, as in the customer profile or the tenant's `accelerationMeetingName`.
