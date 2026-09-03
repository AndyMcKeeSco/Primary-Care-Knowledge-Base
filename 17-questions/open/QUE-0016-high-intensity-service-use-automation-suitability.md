---
id: QUE-0016
type: question
title: Which services used by patients with high-intensity primary-care use are suitable for automation or supported self-service?
status: draft
created: 2026-09-03
updated: 2026-09-03
tags: [high-intensity-use, automation, self-service, demand, safety, equity]
relationships:
  - type: depends_on
    target: QUE-0010
    note: "Requires an evidence-based account of high-intensity and repeat demand."
  - type: depends_on
    target: QUE-0017
    note: "Requires explicit service and task characteristics for suitability assessment."
  - type: interacts_with
    target: QUE-0004
    note: "Narrows the general automation question to services used by high-intensity users."
  - type: interacts_with
    target: QUE-0005
    note: "Separates supported self-service from blanket patient diversion."
  - type: interacts_with
    target: QUE-0015
    note: "All candidates remain subject to clinical-safety, governance and equity guardrails."
confidence: unknown
provenance:
  sources:
    - QUE-0010
    - EVD-0003
    - EVD-0004
    - EVD-0005
    - EVD-0007
---

# Which services used by patients with high-intensity primary-care use are suitable for automation or supported self-service?

## Question

Among services and recurring tasks used by patients with high-intensity primary-care use, which are suitable for full automation, supported self-service, assisted digital access, redirection to another appropriate service, or no automation—and under what safeguards and escalation rules?

## Why it matters

A minority of users can account for a disproportionate share of contacts, creating potential leverage for service redesign. High use is not evidence of low complexity or avoidability, however, and may coexist with mental-health needs, multimorbidity, vulnerability or legitimate continuity requirements. Suitability must therefore be assessed at service and task level rather than assigned to patients as a group.

## Decision enabled

Which bounded services or tasks should enter a small, reversible automation or supported-self-service experiment, and which must retain direct human access because they involve clinical judgement, uncertainty, relationship, safeguarding, accessibility or accountability.

## Current knowledge

`EVD-0003` and `EVD-0005` indicate that repeated use is concentrated among a minority in Scottish out-of-hours and UK general-practice datasets. `EVD-0004` shows that high users have heterogeneous reasons for contact and relatively more mental-health-related contacts; it does not identify low-complexity or automatable demand. `EVD-0007` reports that many surveyed Scottish minor-ailment-service users viewed general practice as their alternative, but this does not prove causal diversion or suitability for unsupported self-service.

## Evidence gap

No reviewed evidence links high-intensity users' specific service or task types to frequency, judgement content, safety risk, digital access, outcomes, re-contact or successful automation. Current Scottish in-hours service-level data are particularly limited.

## Proposed method

Segment demand by task and service rather than patient label. Combine aggregate activity evidence, workflow and decision modelling, staff and patient research, accessibility analysis and safety review. Score candidate tasks against `QUE-0017`; exclude diagnosis, autonomous clinical triage, prescribing decisions, safeguarding and urgent or uncertain presentations unless separately governed by qualified clinical review. Test only opt-in, reversible pathways with immediate human alternatives and measure completion, escalation, re-contact, safety, equity and staff time.

## Priority rationale

High, because it converts demand-concentration evidence into a testable service-design decision while preventing the unsafe inference that frequent use is automatically simple or avoidable.

## Dependencies

Depends on `QUE-0010` and `QUE-0017`; relates to `QUE-0004`, `QUE-0005`, `QUE-0008`, `QUE-0015`, workflow entities and decision entities.

## Answer/closure criteria

Closed when at least one high-volume service or task used by a defined high-intensity cohort has evidenced volume, user need and current pathway; has been assessed for judgement, safety, accessibility, equity, integration and escalation; and has either passed a small monitored experiment or been explicitly ruled unsuitable. Closure must not depend on contact volume alone.
