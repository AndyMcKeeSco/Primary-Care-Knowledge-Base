---
id: QUE-0011
type: question
title: Where does fragmented information cause repeated context-gathering across a patient journey?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [information, interoperability, workflow, duplication, patient-journey]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
---

# Where does fragmented information cause repeated context-gathering across a patient journey?

## Question

At which points in Scottish primary-care journeys must staff or patients re-gather information that already exists elsewhere, because records, systems or communications are fragmented?

## Why it matters

Repeated context-gathering is a common, cumulative inefficiency that also frustrates patients and introduces error. It is a frequent target for both integration and AI-assisted summarisation, so locating it identifies concrete opportunities.

## Decision enabled

Where information integration, sharing or AI summarisation would remove avoidable rework, and where the constraint is instead governance or trust.

## Current knowledge

Not yet established. The synthetic example (`OBS-9001`) illustrates the pattern but is not evidence.

## Evidence gap

No extracted evidence documents real instances, their frequency, or the information that is missing versus merely inaccessible.

## Proposed method

Model journeys and workflows; extract evidence of repeated information-gathering from evaluation and experience sources; distinguish absent information from inaccessible-but-existing information. Preserve uncertainty about cause.

## Priority rationale

Medium-to-high: a recurring, addressable inefficiency, but dependent on journey and workflow modelling that does not yet exist.

## Dependencies

Depends on empty journeys and workflows layers. Relates to `QUE-0002`, `QUE-0007`.

## Answer/closure criteria

Closed when at least one instance of avoidable repeated context-gathering is evidenced with the information involved, the journey point, and whether the root cause is absence or inaccessibility.
