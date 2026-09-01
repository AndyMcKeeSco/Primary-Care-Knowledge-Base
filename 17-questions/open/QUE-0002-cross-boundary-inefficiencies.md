---
id: QUE-0002
type: question
title: What inefficiencies exist that cause other areas to become inefficient?
status: draft
created: 2026-09-01
updated: 2026-09-01
tags: [efficiency, workflow, system, interfaces, propagation]
relationships: []
confidence: unknown
provenance:
  sources:
    - 00-model/objective.md
    - 00-model/scope.md
---

# What inefficiencies exist that cause other areas to become inefficient?

## Question

Which inefficiencies within Scottish primary care propagate beyond their point of origin — creating rework, delay or avoidable demand in other roles, settings or parts of the system?

## Why it matters

Local fixes can miss the largest gains. Inefficiencies that cascade (for example, incomplete referrals, failed handoffs, or repeated information-gathering) impose costs elsewhere, so identifying them targets interventions with system-wide leverage.

## Decision enabled

Where to prioritise workflow or interface redesign for maximum downstream benefit, rather than optimising a single step in isolation.

## Current knowledge

Not yet established. The example set illustrates one candidate pattern (repeated context-gathering, `OBS-9001`) but this is synthetic and not evidence about Scottish primary care.

## Evidence gap

No extracted evidence traces an inefficiency from cause to downstream effect across a boundary, nor quantifies the propagated cost.

## Proposed method

Model workflows and interfaces in context; extract evidence of handoff failure, duplication and rework from audit and evaluation sources; represent propagation as explicit relationships between workflow, interface and problem entities. Preserve uncertainty about causal direction.

## Priority rationale

High: directly serves the "capacity" and "efficiency" objectives and identifies high-leverage targets, but depends on prior workflow modelling that does not yet exist.

## Dependencies

Depends on populated workflow (`05-workflows`) and interface (`07-interfaces`) layers, both currently empty. Relates to `PRB-0001` and care settings `CS-0001`/`CS-0002`.

## Answer/closure criteria

Closed when at least one inefficiency is documented with evidence of its origin and a downstream effect in another role or setting, with the causal claim appropriately qualified.
