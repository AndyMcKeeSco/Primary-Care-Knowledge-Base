---
id: QUE-0004
type: question
title: What gets done in primary care that could be automated?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [automation, workflow, capacity, administrative-burden, technology-opportunity]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
---

# What gets done in primary care that could be automated?

## Question

Which recurring tasks and workflow steps in Scottish primary care are candidates for automation — being rule-governed, high-volume, low-judgement or repetitive — and what proportion of role time do they consume?

## Why it matters

Automation of appropriate tasks is a primary route to releasing clinical and administrative capacity, a core aim of the model. Identifying genuinely automatable work — distinct from work that only appears routine — is the precondition for any credible technology opportunity.

## Decision enabled

Which tasks to prioritise for automation pilots, and where automation would be unsafe or counterproductive because human judgement, relationship or accountability is essential.

## Current knowledge

Not yet established. No workflow entities or task-level time evidence exist. The synthetic medication-query example gestures at one candidate but is not evidence.

## Evidence gap

No extracted evidence characterises task volume, judgement content, or the current time cost of routine work by role.

## Proposed method

Model workflows and decisions in context; extract evidence on task frequency and administrative burden from activity and workforce sources; classify each candidate task by automatability and by safety/accountability risk. Flag any task touching diagnosis, triage, prescribing or safeguarding for mandatory clinical scrutiny.

## Priority rationale

High and central to the objective, but methodologically demanding: it requires workflow modelling and careful separation of automatable from judgement-bearing work.

## Dependencies

Depends on workflow (`05-workflows`) and decision (`06-decisions`) layers, currently empty. Relates to `QUE-0006` (administrative burden), `QUE-0005` (patient self-service) and `QUE-0015` (guardrails).

## Answer/closure criteria

Closed when at least one high-volume task is evidenced with its role, frequency and time cost, and assessed for automatability and safety risk, with judgement-bearing work explicitly excluded.
