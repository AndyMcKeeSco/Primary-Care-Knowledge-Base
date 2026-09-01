---
id: OPP-0001
type: opportunity
title: Constrained agent-assisted evidence extraction
status: candidate
created: 2026-09-01
updated: 2026-09-01
tags: [repository-methodology, evidence-extraction, human-review]
relationships:
  - type: addresses
    target: PRB-0001
  - type: interacts_with
    target: HYP-0001
  - type: interacts_with
    target: EXP-0001
confidence: unknown
provenance:
  sources:
    - README.md
    - 00-model/evidence-model.md
    - agents/shared/evidence-rules.md
---

# Constrained agent-assisted evidence extraction

## Problem addressed

`PRB-0001`: the repository has not proven a repeatable path from catalogued source artefacts to bounded, traceable draft evidence records.

## Mechanism

Apply the existing evidence template, evidence rules and clinical-safety boundaries as a structured extraction workflow, then require human review before any draft becomes production evidence.

## Why now?

The source catalogue contains 26 production records, while the production evidence collection is empty. A small offline comparison can test the workflow before routine adoption.

## Affected personas

Repository maintainers, evidence reviewers and constrained research agents. No patient or care-professional persona is directly affected by this offline experiment.

## Affected settings

Repository research and review only; no live care setting.

## Existing alternatives

- Fully manual extraction using the template.
- Unstructured agent drafting followed by human review.
- Deferring extraction until role and tooling maturity improves.

## Evidence

No production evidence demonstrates that the proposed workflow is better than these alternatives. The opportunity remains unvalidated.

## Expected impact

Potentially more complete provenance, fewer unsupported assertions and more predictable review. Magnitude and reviewer-effort effects are unknown.

## Constraints

Use public, non-sensitive artefacts only. Keep outputs offline and draft. Do not use patient data, provide clinical guidance, assess care for an individual, or merge results without human approval.

## Risks

- A structured format may create false confidence in an inaccurate extraction.
- Reviewers may recognise the workflow condition and introduce bias.
- A small source sample may not transfer to other formats or topics.
- Additional structure may increase total effort.

## Novelty

The repository already contains the component controls. The untested opportunity is their use as one repeatable, review-gated workflow rather than a new extraction technology.

## Feasibility

An offline paired comparison can use existing public catalogue candidates and repository tooling without patient contact or live-system changes.

## Uncertainties

Accuracy, provenance completeness, unsupported-assertion rate, reviewer correction time and transferability across source types.

## Suggested next experiment

Run `EXP-0001`, a small offline paired comparison of baseline and structured draft extraction across three pre-approved source artefacts.
