---
id: QUE-0013
type: question
title: What are the workforce capacity and skill-mix constraints in Scottish primary care?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [workforce, capacity, skill-mix, general-practice, sustainability]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
---

# What are the workforce capacity and skill-mix constraints in Scottish primary care?

## Question

What is the measured size, composition and trend of the Scottish primary-care workforce, and which capacity or skill-mix constraints most limit the system's ability to meet demand?

## Why it matters

Workforce is the binding constraint on primary-care throughput. Any opportunity that assumes released or redirected capacity depends on a sound picture of who is available, in what roles, and how that is changing. This question provides the denominator for capacity claims across the model.

## Current knowledge

Not yet established as evidence, but a canonical source is catalogued and queued: the General Practice Workforce Survey (`SRC-0020`, currently the 2022 release), whose extraction is the subject of assignment `daily-001`.

## Decision enabled

Whether a capacity-releasing opportunity is worth pursuing given real workforce headroom, and where skill-mix change is feasible.

## Evidence gap

No production evidence records the workforce headcount, whole-time-equivalent, composition or trend; the first extraction (`daily-001`) is pending.

## Proposed method

Extract bounded workforce findings from official statistics (`SRC-0020` first, then related workforce publications), preserving definitions, denominator, period and limitations. Do not infer workload, capacity or care quality from headcount alone. No patient-level data.

## Priority rationale

High and foundational; it is the first question with an approved extraction assignment, making it the most immediately actionable.

## Dependencies

Directly served by assignment `daily-001` against `SRC-0020`. Feeds `QUE-0004`, `QUE-0006`, `QUE-0008`. Relates to `PER-0002`, `CS-0001`, `PRB-0001`.

## Answer/closure criteria

Closed when the workforce size, composition and trend are evidenced from official statistics with definitions and limitations preserved, and the distinction between headcount and effective capacity is explicit.
