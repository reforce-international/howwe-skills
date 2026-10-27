# The Howwe model

> Shared reference. Identical copies live in each skill that uses it; CI fails if they differ. Edit one and copy it to the others.

How strategy is modelled in Howwe, what each item means, and how to read it correctly.

## The chain from strategy to work

```
Strategic plan  (vision, goals and initiatives agreed in the strategy workshop)
└─ Goal         a number the organization must move, with a target and actual per period
   └─ Initiative        the big bet that moves the goal; has an owner, a purpose and objectives
      └─ Sub-initiative an initiative supporting another initiative
         ├─ Milestone        a concrete result with an owner and a deadline
         ├─ Aggregate target a number a team reaches through several activities ("team activity" in the app)
         └─ Activity         the work a team commits to in the acceleration meeting ("key activity")
```

Goals at company level are **Company Goals**; teams can have Goals of their own. Always call them Goals or Company Goals. The tools and fields still say "mig" (`read_migs`, `list_global_migs`, `list_team_migs`, `materializedMigId`): that is the same thing under its old name, which never appears in anything you write.

Items are linked by `supports` (what this item supports) and `supportedBy` (what directly supports it). Follow `supports` upward to explain why work matters, and `supportedBy` downward to explain why a goal is moving or not.

Teams contribute to initiatives and milestones. Activities belong to one team, which commits to them in its **acceleration meeting**: the recurring meeting where the team reviews the period behind and commits to the period ahead. Each tenant may have renamed it; the product's own name is "Strategy Stand-up" (Swedish: "Strategi Stand-up").

## Default names in the app

Use the customer's own words when the customer profile gives them. Otherwise use these.

| Howwe item | English | Swedish |
|---|---|---|
| Company-level goal | Company Goal | Företagsmål |
| Team goal | Goal | Mål |
| Initiative | Initiative | Företagsinitiativ |
| Sub-initiative | Sub-initiative | Subinitiativ |
| Initiative objectives | Objectives | Målsättning på initiativ |
| Initiative description | Purpose | Syfte |
| Team-owned initiative | Team initiative | Teaminitiativ |
| Milestone | Milestone | Milstolpe |
| Aggregate target | Team activity | Teamaktivitet |
| Activity | Key activity | Nyckelaktivitet |
| Acceleration meeting | Strategy Stand-up | Strategi Stand-up |

## Reading the data correctly

- **Published plan, not the workshop draft.** The strategic plan comes in two parts: the published plan, and a live workshop draft while a strategy workshop is in progress. Report from the published plan. Its APPROVED items carry `materializedMigId` or `materializedInitiativeId`, which lead to the real Goal or initiative. CANDIDATE and IDEA items are still under discussion: leave them out, or show them apart as proposals when asked. Without a published plan, say so, and build the picture from the tenant's Company Goals and initiatives instead.
- **Goal series.** A Goal has a target and an actual per period, oldest first. Periods with a target and no actual are still to come. The latest period with an actual is the current result, also when that period has not ended yet. A start point, when present, is where the plan begins, not a period.
- **How a goal is read.** A Goal's numbers alone do not say how the customer reads them. Some goals are better when lower (injury rates, cost). Some are read over a cycle or a rolling twelve months, or relative to competitors. Take this from the customer profile; when it is missing, say how you read the goal and ask.
- **Placeholders apply to targets only.** A target value that looks like a round placeholder (0, 1, 100, the same value every period) is worth flagging rather than reporting as a real target.
- **Reported actuals are results.** An actual the customer has reported is their result, also for a period that has not ended. It can be a result already settled (contracted MRR) or a total so far (sales in the current month). Say when the period is still running, and compare a total so far with the target in that light. Never call a reported actual an error, a placeholder or a copy of the target, even when it equals the target. When a number looks unusual and it matters for the conclusion, ask.
- **Aggregate targets.** The goal and what the member activities' own goals add up to can differ. When they do, point it out.
- **Activities.** An activity with a target is measured in a number; one without is a task, done or not done.
- **Acceleration meetings.** A meeting is held once it is completed (`heldAt` set). An unfinished row may be under way, planned or abandoned; do not count it as held.
- **Missing data is a finding.** An initiative without objectives, a milestone without owner or deadline, a goal with no supporting initiative: report it as something to fix, never fill the gap with a guess.
