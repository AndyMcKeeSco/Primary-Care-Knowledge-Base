# Naming and Stable IDs

| Prefix | Type | Example |
|---|---|---|
| ORG | Organisation | ORG-0001 |
| CS | Care setting | CS-0001 |
| SVC | Service | SVC-0001 |
| PER | Persona | PER-0001 |
| JRN | Journey | JRN-0001 |
| WFL | Workflow | WFL-0001 |
| DEC | Decision | DEC-0001 |
| INT | Interface | INT-0001 |
| PRB | Problem | PRB-0001 |
| CLM | Claim | CLM-0001 |
| EVD | Evidence | EVD-0001 |
| OBS | Observation | OBS-0001 |
| CON | Constraint | CON-0001 |
| SOL | Solution | SOL-0001 |
| HYP | Hypothesis | HYP-0001 |
| OPP | Opportunity | OPP-0001 |
| EXP | Experiment | EXP-0001 |
| QUE | Question | QUE-0001 |
| SRC | Source | SRC-0001 |

IDs are permanent, never reused, and remain stable when titles, filenames, status or locations change. Allocate the next unused number after a repository-wide search. Relationships use IDs rather than depending on filenames.

Use uppercase IDs and lowercase kebab-case slugs, for example `PRB-0001-medication-query-handoffs.md`, `OBS-0003-repeat-context-gathering.md`, and `OPP-0002-medication-query-routing.md`. A moved or renamed file must retain its ID and inbound relationships must remain valid.
