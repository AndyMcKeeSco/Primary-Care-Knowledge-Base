# Research Backlog

Prioritised open questions should be represented as `QUESTION` entities in `open/`; this page records cross-cutting sequencing decisions.

## Open questions

Seventeen `QUE` entities are seeded in [`open/`](open/). Each records its own priority rationale and dependencies; the sequencing below is a cross-cutting view only.

| ID | Question | Depends on |
|---|---|---|
| `QUE-0001` | Perception of primary care service, good and bad | — |
| `QUE-0002` | Inefficiencies that make other areas inefficient | `QUE-0007`, workflows |
| `QUE-0003` | Where primary care blocks rather than enables patients | `QUE-0009`, journeys |
| `QUE-0004` | What could be automated | `QUE-0006`, `QUE-0010` |
| `QUE-0005` | What patients could self-serve with AI | `QUE-0010`, `QUE-0009`, `QUE-0015` |
| `QUE-0006` | Administrative work consuming clinical time | — |
| `QUE-0007` | GP–community pharmacy handoff failures | interfaces |
| `QUE-0008` | Contacts resolvable at first contact by another role/channel | `QUE-0010` |
| `QUE-0009` | Which groups face the greatest access barriers | — |
| `QUE-0010` | Demand composition: repeat/low-complexity contacts | — |
| `QUE-0011` | Fragmented information causing repeated context-gathering | journeys, workflows |
| `QUE-0012` | Inter-practice workflow variation and its effect | workflows |
| `QUE-0013` | Workforce capacity and skill-mix constraints | `daily-001` / `SRC-0020` |
| `QUE-0014` | Underused existing digital tools and adoption barriers | — |
| `QUE-0015` | Safety/governance guardrails for AI and automation | — |
| `QUE-0016` | Services used by high-intensity users that are suitable for automation or supported self-service | `QUE-0010`, `QUE-0017` |
| `QUE-0017` | Characteristics that distinguish automation-suitable services for high-intensity users | workflows, decisions, `QUE-0015` |

## Suggested sequencing

1. **Foundational, source-backed, and already actionable:** `QUE-0013` (an approved extraction, `daily-001`, is queued), then `QUE-0010`, `QUE-0001`, `QUE-0009` — each is served by an accessible national source and unlocks several downstream questions.
2. **Enabling constraints:** `QUE-0015` (guardrails) and `QUE-0017` (automation-suitability characteristics) should be developed early because they bound technology, AI and supported-self-service opportunities.
3. **Structure-dependent:** `QUE-0002`, `QUE-0003`, `QUE-0007`, `QUE-0011`, `QUE-0012` require the journeys, workflows and interfaces layers to be populated first.
4. **Opportunity-shaping:** `QUE-0004`, `QUE-0005`, `QUE-0006`, `QUE-0008`, `QUE-0014` and `QUE-0016` build on the demand, workforce and assessment-framework evidence above.

Sequencing is indicative and should be revisited by the research planner as evidence accrues.
