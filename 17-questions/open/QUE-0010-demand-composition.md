---
id: QUE-0010
type: question
title: What repeat and low-complexity contacts dominate primary-care demand?
status: open
created: 2026-09-01
updated: 2026-09-02
tags: [demand, activity, workload, efficiency, general-practice]
relationships:
  - type: interacts_with
    target: EVD-0002
    note: "Partially answers recorded general-practice activity composition; contact reason, repeat status and complexity remain unresolved."
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

`EVD-0002` provides a partial answer for recorded Scottish general-practice activity in January 2026. It reports 7,949,664 whole-practice encounters across participating practices: 53.0% indirect, 36.0% direct, 10.9% undefined and 0.1% external direct. The largest named groups were surgery consultation (28.5%), general administration (25.2%), clinical administration (13.7%) and medicines management (10.6%).

This establishes recorded encounter composition for one month, not the composition of underlying need or all primary-care demand. It does not identify contact reason, repeat status, complexity, duration, appropriateness, clinical value or suitability for automation, self-service or redirection.

## Evidence gap

No extracted evidence yet breaks down Scottish primary-care demand by contact reason, repeat status or complexity, and community-pharmacy demand remains outside the current finding. Further source discovery is required before the largest repeat or low-complexity contact categories can be identified.

## Proposed method

Extract bounded evidence from recorded-activity sources; classify contacts by reason, repeat status and complexity where the source supports it. Preserve definitions, coverage and period. No patient-level data.

## Priority rationale

High as an enabling question: several other questions (`QUE-0004`, `QUE-0005`, `QUE-0008`) depend on it, and it is served by accessible activity data.

## Dependencies

Feeds `QUE-0004`, `QUE-0005`, `QUE-0008`. Relates to `CS-0001`.

## Answer/closure criteria

Closed when demand is evidenced by contact reason for at least general practice, with the largest repeat/low-complexity categories identified, and coverage, definitions and limitations stated.
