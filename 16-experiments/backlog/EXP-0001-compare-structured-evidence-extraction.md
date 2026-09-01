---
id: EXP-0001
type: experiment
title: Compare structured and baseline evidence extraction
status: proposed
created: 2026-09-01
updated: 2026-09-01
tags: [repository-methodology, evidence-extraction, offline, human-review]
relationships:
  - type: tests
    target: HYP-0001
  - type: contributes_to
    target: OPP-0001
confidence: unknown
provenance:
  sources:
    - README.md
    - 00-model/evidence-model.md
    - agents/shared/evidence-rules.md
    - agents/shared/clinical-safety-boundaries.md
---

# Compare structured and baseline evidence extraction

## Hypothesis

`HYP-0001`: a workflow constrained by the repository evidence template and rules will produce more reviewable draft evidence records than a minimal extraction prompt.

## Uncertainty

Whether the structured workflow materially improves provenance completeness and reduces unsupported assertions without creating unacceptable additional review effort.

## Population / environment

Three pre-approved, publicly accessible and non-sensitive Scottish primary-care source artefacts already represented in `_sources/catalogue/`: one intended-policy document, one statistical publication and one programme evaluation. The repository maintainer selects the exact records before the experiment and records why the sample is sufficient for this limited workflow decision. No patient-level material is permitted.

## Method

1. The repository maintainer approves the three source artefacts, confirms access and freezes a scoring rubric before any extraction.
2. For each artefact, run two independent offline draft extractions: a baseline using a minimal request for a summary finding, and a structured run using the evidence template, Evidence Rules and safety boundaries.
3. Randomise run order and prevent either run from seeing the other output.
4. Label outputs with neutral identifiers so the reviewer is blinded to condition where practical.
5. A human reviewer scores every draft against the frozen rubric. Outputs remain experiment artefacts and must not be added to `10-evidence/` during this experiment.
6. Compare paired results by artefact and record exceptions rather than pooling away source-type differences.

This is an offline documentation experiment, not a clinical evaluation or automation trial.

## Data collected

- Completion of required evidence fields.
- Correct and locatable provenance.
- Factual or transcription errors.
- Unsupported assertions and source-to-evidence category errors.
- Missing population, geography, method, period, applicability or limitation context.
- Safety-boundary violations.
- Reviewer correction count and review time.
- Source type, run order and reviewer notes needed to interpret variation.

Do not collect personal, patient-level or confidential data.

## Success criterion

Proceed to a larger offline validation only if all three structured drafts:

- contain correct, locatable provenance;
- contain no fabricated quotation, date, locator or finding;
- contain no unsupported clinical assertion or safety-boundary violation;
- complete at least 90% of rubric-required context fields; and
- outperform their paired baseline on either required-field completeness or reviewer correction count without increasing median review time by more than 25%.

These criteria support only a decision about further offline validation, not routine production use.

## Failure criterion

Do not proceed if any structured draft fabricates provenance or content, introduces an unsupported clinical assertion, contains sensitive material, fails the 90% completeness threshold, or shows no paired improvement. An inconclusive result is treated as failure to proceed, not evidence that the workflow is ineffective in all contexts.

## Safety considerations

- Use only public, non-sensitive source artefacts approved by the repository maintainer.
- Do not use patient-level data, contact patients or professionals, or influence live care.
- Do not perform diagnosis, triage, prescribing, treatment, prioritisation or safeguarding work.
- Keep all outputs as unapproved drafts outside the production evidence collection.
- Require human review of every scored output and escalate any clinical, privacy, rights or provenance concern.

## Expected learning

Whether the structured controls improve draft completeness and unsupported-assertion performance, what review burden remains, and which source types or rubric fields need stronger controls.

## Decision enabled

Decision owner: repository maintainer.

The result enables a choice between stopping, revising the workflow, or approving a larger offline validation. It does not enable production adoption or clinical use.

## Analysis plan

Report each paired artefact result and a small aggregate summary. Compare rubric completeness, error categories, correction counts and review time. Preserve contrary cases and source-type variation. Do not perform significance testing on this three-artefact sample or change criteria after seeing results.

## Stop conditions

Stop before extraction if source access, rights, sample justification, the frozen rubric, reviewer availability or run independence cannot be established. Stop immediately if identifiable or confidential data appears, a run makes patient-specific recommendations, provenance cannot be verified, or outputs could influence live care. Escalate rather than weakening the criteria.
