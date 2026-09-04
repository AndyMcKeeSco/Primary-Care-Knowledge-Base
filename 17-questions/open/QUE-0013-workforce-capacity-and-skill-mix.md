---
id: QUE-0013
type: question
title: What are the workforce capacity and skill-mix constraints in Scottish primary care?
status: open
created: 2026-09-01
updated: 2026-09-04
tags: [workforce, capacity, skill-mix, general-practice, sustainability]
relationships:
  - type: interacts_with
    target: EVD-0009
    note: "Partially answers nurse workforce size, trend and designation mix at 31 March 2022."
  - type: interacts_with
    target: EVD-0010
    note: "Partially answers nurse-vacancy measures among responding practices during 2021/22."
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

Active `EVD-0009` records Public Health Scotland's estimate of 2,414 registered nurses and 1,690 nurse WTE in Scottish general practices at 31 March 2022. General Practice Nurses comprised 63% of estimated nurse headcount and 60% of estimated WTE, while Advanced Nurse Practitioners and Nurse Specialists together comprised 27% and 31%, respectively. The estimates are scaled from 517 usable practice returns and do not measure workload, workforce sufficiency or effective capacity.

Active `EVD-0010` records that 26% of responding practices reported nurse vacancies during 2021/22, including 10% reporting Advanced Nurse Practitioner vacancies and 19% reporting general-practice or treatment-room nurse vacancies. The reported hours-based nurse vacancy rate was 11.7%. These are respondent-based measures without item-level denominators or stated national scaling and do not establish national vacancy counts, causes or service effects.

Draft `EVD-0001` separately extracts GP headcount and estimated WTE from `SRC-0020`; it has not been activated by this review.

## Decision enabled

Whether a capacity-releasing opportunity is worth pursuing given real workforce headroom, and where skill-mix change is feasible.

## Evidence gap

The active evidence is confined to registered nurses in general practice and respondent-based nurse vacancies for 2021/22–2022. It does not establish current staffing, GP capacity, practice administration, community pharmacy, out-of-hours staffing, wider multidisciplinary-team composition, vacancy causes, geographical distribution, deployable capacity or the relationship between staffing and demand. Public Health Scotland excluded the source's multidisciplinary-team section because of poor data quality and completeness.

## Proposed method

Extract bounded workforce findings from official statistics (`SRC-0020` first, then related workforce publications), preserving definitions, denominator, period and limitations. Do not infer workload, capacity or care quality from headcount alone. No patient-level data.

## Priority rationale

High and foundational. Nurse workforce and vacancy evidence now provides a partial baseline, but broader and more current role coverage is required before judging system-wide capacity or feasible skill-mix change.

## Dependencies

Partially served by `EVD-0009` and `EVD-0010` from `SRC-0020`. Draft `EVD-0001` requires separate review. Feeds `QUE-0004`, `QUE-0006`, `QUE-0008`. Relates to `PER-0002`, `CS-0001`, `PRB-0001`.

## Answer/closure criteria

Closed when the workforce size, composition and trend are evidenced from official statistics with definitions and limitations preserved, and the distinction between headcount and effective capacity is explicit.
