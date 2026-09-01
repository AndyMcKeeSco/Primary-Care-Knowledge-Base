---
id: QUE-0007
type: question
title: Where do handoffs between general practice and community pharmacy fail or duplicate work?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [interfaces, community-pharmacy, general-practice, handoffs, duplication]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
---

# Where do handoffs between general practice and community pharmacy fail or duplicate work?

## Question

At which points do information, work or responsibility transferred between Scottish general practice and community pharmacy fail, stall or duplicate effort — and what triggers the failure?

## Why it matters

The GP–pharmacy interface is a deliberate initial focus of the model. Failed or duplicated handoffs (for example, medication queries, prescription changes, or referrals) waste capacity in both settings and risk patient harm, making the interface a high-leverage target.

## Decision enabled

Which interface interactions to redesign or support with technology to reduce failure and duplication across the two settings.

## Current knowledge

Not yet established. The synthetic medication-query example (`INT-9001`) models this interface for demonstration only and is not evidence.

## Evidence gap

No extracted evidence documents real handoff failure modes, their frequency, or their consequences at this interface.

## Proposed method

Model the interface (`07-interfaces`) and the workflows either side; extract evidence of handoff failure and duplication from evaluation and audit sources; represent transfers with explicit `transfers_to`/`connects` relationships. Preserve uncertainty.

## Priority rationale

High: squarely within the model's initial scope and a recognised source of avoidable work, though it depends on interface modelling not yet present.

## Dependencies

Depends on the empty interfaces layer. Relates to `QUE-0002`, `QUE-0011`, and care settings `CS-0001`/`CS-0002`.

## Answer/closure criteria

Closed when at least one handoff failure or duplication mode is evidenced with its trigger, frequency indication and consequence, sources and limitations preserved.
