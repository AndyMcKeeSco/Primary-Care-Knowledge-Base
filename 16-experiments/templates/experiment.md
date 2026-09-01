# Experiment Template

Copy this file into `16-experiments/backlog/`, replace every placeholder, and remove this introductory paragraph.

```yaml
---
id: EXP-XXXX
type: experiment
title: Replace with a concise title
status: proposed
created: YYYY-MM-DD
updated: YYYY-MM-DD
approved_by:
maximum_runs: 3
runs_completed: 0
maximum_sources: 10
maximum_duration_minutes: 30
allowed_writes:
  - 16-experiments/
  - 11-observations/
  - 09-claims/
  - _sources/catalogue/
external_actions_allowed: false
human_review_required: true
tags: []
relationships: []
confidence: unknown
provenance:
  sources: []
---
```

# Replace with title

## Hypothesis

<!-- State the hypothesis being tested. -->

## Uncertainty

<!-- Identify the decision-relevant uncertainty. -->

## Population / environment

<!-- Define the bounded population or environment. -->

## Method

<!-- Describe the smallest safe method that can resolve the uncertainty. -->

## Evidence required

<!-- Identify the source artefacts or repository evidence needed. -->

## Data collected

<!-- List only the data needed. Do not include identifiable patient data. -->

## Success criterion

<!-- Define the criterion before the experiment begins. -->

## Failure criterion

<!-- Define what result would fail to support proceeding. -->

## Safety considerations

<!-- Record clinical, privacy, operational and governance boundaries. -->

## Expected learning

<!-- State what the experiment should teach. -->

## Decision enabled

<!-- State the decision that the result will inform. -->

## Analysis plan

<!-- Define how results will be assessed. -->

## Stop conditions

<!-- State when the experiment must stop or escalate. -->

## Results

<!-- Complete only during approved execution. -->

## Recommended next action

<!-- After review, recommend stop, repeat, refine, escalate or reject. -->
