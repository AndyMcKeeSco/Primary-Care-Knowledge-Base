---
id: QUE-0017
type: question
title: What characteristics distinguish services suitable for automation for patients with high-intensity primary-care use?
status: draft
created: 2026-09-03
updated: 2026-09-03
tags: [high-intensity-use, automation, service-characteristics, assessment, safety, equity]
relationships:
  - type: interacts_with
    target: QUE-0016
    note: "Defines the assessment dimensions used to judge candidate services and tasks."
  - type: interacts_with
    target: QUE-0004
    note: "Extends the general task-automation criteria for a high-intensity-use context."
  - type: interacts_with
    target: QUE-0015
    note: "Requires clinical-safety and governance characteristics to be explicit."
confidence: unknown
provenance:
  sources:
    - QUE-0010
    - EVD-0003
    - EVD-0004
    - EVD-0005
    - EVD-0007
---

# What characteristics distinguish services suitable for automation for patients with high-intensity primary-care use?

## Question

What measurable service, task, user and system characteristics distinguish work that is suitable for automation or supported self-service from work that requires human judgement, continuity, relationship or clinical accountability when used by patients with high-intensity primary-care use?

## Why it matters

An automation decision needs more than volume. A service may be frequent and repetitive but still unsafe to automate because inputs are ambiguous, consequences are high, needs are complex, data are incomplete, or users face accessibility barriers. A reusable assessment framework would make candidate selection consistent and reviewable.

## Decision enabled

Which characteristics should form the eligibility, exclusion, escalation and monitoring criteria for evaluating services under `QUE-0016` and broader automation candidates under `QUE-0004`.

## Current knowledge

Existing evidence establishes concentration of use but not automation suitability. The reviewed process indicates candidate characteristics should include repeatability, rule boundedness, input quality, need for judgement, severity and uncertainty, reversibility, escalation availability, integration dependencies, continuity value, accessibility, digital exclusion, user preference, equity effects and measurable outcomes. These are proposed dimensions, not yet a validated scoring model.

## Evidence gap

No repository evidence validates which characteristics predict safe completion, reduced handling, acceptable re-contact, user benefit or equitable uptake in Scottish primary care. Thresholds and interactions between characteristics are unknown.

## Proposed method

Review automation, self-service and service-redirection frameworks from healthcare and other regulated services; compare them with Scottish clinical-safety and governance requirements; test the resulting dimensions against real workflows and adverse scenarios; involve high-intensity users and staff; and validate candidate criteria through small, reversible experiments. Keep service characteristics separate from assumptions about a person's capability or preference.

## Priority rationale

High and enabling: this question supplies the assessment framework needed before `QUE-0016` can responsibly select automation candidates.

## Dependencies

Relates to `QUE-0016`, `QUE-0004`, `QUE-0005`, `QUE-0006`, `QUE-0010` and `QUE-0015`; requires populated workflow, decision, interface and constraint layers.

## Answer/closure criteria

Closed when a reviewable assessment framework defines service/task characteristics, patient and equity considerations, exclusion and escalation rules, minimum evidence, and measurable success and stop criteria—and when the framework has been applied prospectively to at least one candidate service with qualified clinical and safety review.
