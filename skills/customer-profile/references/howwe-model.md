# The Howwe model

> Shared reference. Identical copies live in each skill that uses it; CI fails if they differ. Edit one and copy it to the others.

How strategy is modelled in Howwe, what each item means, and how to read it correctly.

## The chain from strategy to work

```
Strategic plan  (the strategic goals and initiatives, see below)
└─ Goal         a number the organization must move, with a target and actual per period
   └─ Initiative        the big bet that moves the goal; has an owner, a purpose and objectives
      └─ Sub-initiative an initiative supporting another initiative
         ├─ Milestone        a concrete result with an owner and a deadline
         ├─ Aggregate target a number a team reaches through several activities ("Team Activity" in the app)
         └─ Activity         the work a team commits to in the acceleration meeting
```

A goal or a top-level initiative that is strategic (see below) is a **strategic goal** or a **strategic initiative**; every other one is simply a goal or an initiative. The tools say goal, as the app does, but keep two older names: an aggregate target is a Team Activity, and an acceleration meeting is the Strategy Stand-up or the tenant's own name for it. Those tool names never appear in anything you write.

Items are linked by `supports` (what this item supports) and `supportedBy` (what directly supports it). Follow `supports` upward to explain why work matters, and `supportedBy` downward to explain why a goal is moving or not.

Teams contribute to initiatives and milestones. Activities belong to one team, which commits to them in its **acceleration meeting**: the recurring meeting where the team reviews the period behind and commits to the period ahead. Each tenant may have renamed it; the product's own name is "Strategy Stand-up" (Swedish: "Strategi Stand-up").

## Strategic goals and initiatives

Strategic is a flag on a goal or a top-level initiative, not membership of a particular plan. An item becomes strategic when someone adds it to the strategic plan in the app, either by hand or by publishing a plan from the Strategy Planner. It stays strategic until someone removes it, through any number of plans. So the strategic items need not be the items of the plan `get_strategic_plan` returns:

- many tenants promoted theirs by hand, before the Strategy Planner existed;
- items from an earlier year's plan keep running while they are not done;
- an item the published plan created may have been removed since.

Whether an item is strategic is its `strategic` field alone, which every goal and initiative carries. `list_strategic_goals` lists the strategic goals, also those that have ended or not started yet, so read their `startDate` and `endDate` to find the current ones. The strategic initiatives are those `list_initiatives` answers with `strategic: true`. The published plan's `materializedGoalId` and `materializedInitiativeId` only say which item that plan created. No tool adds an item to the strategic plan or removes it; that is done in the app.

## Default names in the app

Use the customer's own words when the customer profile gives them. Otherwise use these.

| Howwe item | English | Swedish |
|---|---|---|
| Strategic goal (`strategic: true`) | Strategic goal | Strategiskt mål |
| Any other goal | Goal | Mål |
| Strategic initiative (`strategic: true`) | Strategic initiative | Strategiskt initiativ |
| Any other initiative | Initiative | Initiativ |
| Sub-initiative | Sub-initiative | Delinitiativ |
| Initiative objectives | Objectives | Målsättning på initiativ |
| Initiative description | Purpose | Syfte |
| Milestone | Milestone | Milstolpe |
| Aggregate target | Team Activity | Teamaktivitet |
| Activity | Activity | Aktivitet |
| Acceleration meeting | Strategy Stand-up | Strategi Stand-up |

In running text these are lowercase, except Team Activity and Strategy Stand-up. People may still use the app's older words: MIG, Most Important Goal, Company Goal, Team Goal, company initiative, Key Activity, team target and Acceleration Meeting (Swedish företagsmål, bolagsmål, teammål, företagsinitiativ, subinitiativ, nyckelaktivitet and accelerationsmöte). Take them to mean the same items, and write the words above unless the customer profile gives the customer's own.

## Reading the data correctly

- **The strategic items, in the published plan's frame.** `get_strategic_plan` answers with two parts: the plan published from the Strategy Planner, and a live workshop draft while a strategy workshop is in progress. Take the plan's title, vision and horizon from the published plan, never from the draft. Take the goals and initiatives to report on from the `strategic` flag, as above, not from the plan's items. The plan's CANDIDATE and IDEA items are still under discussion: leave them out, or show them apart as proposals when asked. Without a published plan, say so, and report on the strategic goals and initiatives without a vision or horizon.
- **Goal series.** A goal has a target and an actual per period, oldest first. Periods with a target and no actual are still to come. The latest period with an actual is the current result, also when that period has not ended yet. A start point, when present, is where the plan begins, not a period.
- **How a goal is read.** A goal's numbers alone do not say how the customer reads them. Some goals are better when lower (injury rates, cost). Some are read over a cycle or a rolling twelve months, or relative to competitors. Take this from the customer profile; when it is missing, say how you read the goal and ask.
- **Placeholders apply to targets only.** A target value that looks like a round placeholder (0, 1, 100, the same value every period) is worth flagging rather than reporting as a real target.
- **Reported actuals are results.** An actual the customer has reported is their result, also for a period that has not ended. It can be a result already settled (contracted MRR) or a total so far (sales in the current month). Say when the period is still running, and compare a total so far with the target in that light. Never call a reported actual an error, a placeholder or a copy of the target, even when it equals the target. When a number looks unusual and it matters for the conclusion, ask.
- **Aggregate targets.** The goal and what the member activities' own goals add up to can differ. When they do, point it out.
- **Activities.** An activity with a target is measured in a number; one without is a task, done or not done.
- **Acceleration meetings.** A meeting is held once it is completed (`heldAt` set). An unfinished row may be under way, planned or abandoned; do not count it as held.
- **Missing data is a finding.** An initiative without objectives, a milestone without owner or deadline, a goal with no supporting initiative: report it as something to fix, never fill the gap with a guess.
