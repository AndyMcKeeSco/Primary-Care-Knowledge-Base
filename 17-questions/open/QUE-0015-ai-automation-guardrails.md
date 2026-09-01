---
id: QUE-0015
type: question
title: What safety and governance guardrails must AI or automation in primary care satisfy to be acceptable?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [safety, governance, guardrails, clinical-safety, trust, artificial-intelligence]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
    - agents/shared/clinical-safety-boundaries.md
---

# What safety and governance guardrails must AI or automation in primary care satisfy to be acceptable?

## Question

What safety, governance, regulatory and trust requirements must any AI or automation in Scottish primary care meet to be acceptable to clinicians, patients and regulators?

## Why it matters

Guardrails are a cross-cutting constraint on every opportunity in the model. An intervention that ignores clinical safety, information governance, liability or equity will fail regardless of efficiency gains, so these requirements bound what is worth proposing at all.

## Decision enabled

Whether a candidate opportunity is admissible for testing, and what evidence of safety and governance it must carry before any pilot.

## Current knowledge

Partially framed by the repository's own `agents/shared/clinical-safety-boundaries.md`, but no evidence-based set of external requirements has been extracted.

## Evidence gap

No extracted findings enumerate the applicable clinical-safety, information-governance, regulatory and consent requirements for AI/automation in Scottish primary care.

## Proposed method

Extract requirements from governance, regulatory and clinical-safety sources; represent them as constraint entities that opportunities and experiments must satisfy. Any function touching diagnosis, triage, prescribing, treatment, prioritisation or safeguarding is flagged as requiring qualified clinical and safety scrutiny.

## Priority rationale

High as an enabling guardrail: it constrains and de-risks every technology and AI opportunity, especially patient-facing ones (`QUE-0005`) and automation (`QUE-0004`).

## Dependencies

Should populate the constraints layer (`12-constraints`). Constrains `QUE-0004`, `QUE-0005`, `QUE-0014`.

## Answer/closure criteria

Closed when the core safety and governance requirements are represented as sourced constraints that any primary-care AI/automation opportunity must satisfy, with Scottish applicability stated.
