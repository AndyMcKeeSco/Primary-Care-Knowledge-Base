---
id: QUE-0010
type: question
title: What repeat and low-complexity contacts dominate primary-care demand?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [demand, activity, workload, efficiency, general-practice]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
---

# What repeat and low-complexity contacts dominate primary-care demand?

## Question

What is the composition of primary-care demand in Scotland by contact reason — and which repeat, administrative or low-complexity contact types account for the largest volumes?

## Why it matters

Demand composition is foundational: it tells us where volume actually concentrates, and therefore where automation, self-service, or role redirection could have the largest effect. It underpins several downstream questions rather than standing alone.

## Decision enabled

Which contact types to target first for automation, self-service or redirection, based on volume rather than salience.

## Current knowledge

Not yet established. Activity publications exist (for example in-hours activity, `SRC-0005`) but have not been inspected or extracted.

## Evidence gap

No extracted evidence breaks down demand by contact reason and complexity for Scottish primary care.

## Proposed method

Extract bounded evidence from recorded-activity sources; classify contacts by reason, repeat status and complexity where the source supports it. Preserve definitions, coverage and period. No patient-level data.

## Priority rationale

High as an enabling question: several other questions (`QUE-0004`, `QUE-0005`, `QUE-0008`) depend on it, and it is served by accessible activity data.

## Dependencies

Feeds `QUE-0004`, `QUE-0005`, `QUE-0008`. Relates to `CS-0001`.

## Answer/closure criteria

Closed when demand is evidenced by contact reason for at least general practice, with the largest repeat/low-complexity categories identified, and coverage, definitions and limitations stated.
