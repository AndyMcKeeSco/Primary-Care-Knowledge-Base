---
id: PRB-0001
type: problem
title: Catalogue-to-evidence workflow is not yet proven
status: candidate
created: 2026-09-01
updated: 2026-09-01
tags: [repository-methodology, evidence, traceability, quality]
relationships:
  - type: interacts_with
    target: OPP-0001
    note: "The candidate opportunity proposes a constrained workflow to address this gap."
confidence: low
provenance:
  sources:
    - README.md
    - _indexes/entities.md
    - _sources/catalogue.md
---

# Catalogue-to-evidence workflow is not yet proven

## Summary

The repository has a governed source catalogue but no production `EVD` entities. It has not yet demonstrated that a repeatable agent-assisted workflow can turn source artefacts into bounded, traceable evidence drafts without unsupported claims or avoidable review burden.

## Who experiences it?

Repository maintainers, evidence reviewers and constrained research agents.

## Where does it occur?

Between source cataloguing in `_sources/` and evidence representation in `10-evidence/`.

## Frequency / scale

The generated entity index currently contains 26 production source records and no production evidence records. This establishes the present repository gap, not the likely frequency of extraction errors in future work.

## Impact

Without a tested workflow, evidence extraction may be inconsistent, difficult to review, or too burdensome to scale. The size and direction of that impact are unknown.

## Current process

The repository provides an evidence template, evidence rules, provenance requirements and constrained agent roles. No completed production extraction demonstrates how these components perform together.

## Root causes

Unknown. The absence of production evidence may reflect repository maturity, source-access constraints, review capacity or another cause.

## Contributing factors

Source artefacts differ in format, method and accessibility. Clinical and policy language also creates a risk of turning intended policy or reported material into claims about actual practice.

## Evidence

No `EVD` finding establishes workflow performance. The repository state directly shows a populated source catalogue and an empty production evidence collection.

## Observations

As of 2026-09-01, repository validation reports 48 entities: 26 production sources, 11 other production care-setting/persona entities, and 11 synthetic examples. None of the production entities is an evidence record.

## Current workarounds

Contributors can manually follow the evidence template and shared rules, but consistency, review effort and error rates have not been measured.

## Existing solutions

The evidence template, Evidence Rules, confidence model, validator and link checker provide controls. Their combined effectiveness for extraction has not been tested.

## Previous attempts

None recorded as a production experiment.

## Constraints

The workflow must not use identifiable patient data, provide clinical guidance, make patient-specific decisions, bypass human review or treat policy intent as proof of implementation.

## Related decisions

Whether to adopt a structured agent-assisted evidence-extraction workflow for routine repository use.

## Related interfaces

Source artefact to draft evidence record, and draft evidence record to human review.

## Open questions

- Does the structured workflow improve provenance completeness and reduce unsupported assertions compared with a minimal baseline?
- What reviewer effort remains after structured extraction?
- Which source types require additional controls?
