---
id: HYP-0001
type: hypothesis
title: A structured evidence workflow improves draft reviewability
status: active
created: 2026-09-01
updated: 2026-09-01
tags: [repository-methodology, evidence-extraction, traceability]
relationships:
  - type: derived_from
    target: PRB-0001
  - type: contributes_to
    target: OPP-0001
  - type: tests
    target: EXP-0001
confidence: unknown
provenance:
  sources:
    - README.md
    - 00-model/evidence-model.md
    - agents/shared/evidence-rules.md
---

# A structured evidence workflow improves draft reviewability

## Hypothesis

For a small, bounded sample of public Scottish primary-care source artefacts, an agent workflow constrained by the repository evidence template and rules will produce draft evidence records with more complete provenance and fewer unsupported assertions than a minimal extraction prompt.

## Mechanism

Explicit field requirements, source-versus-evidence distinctions, applicability checks and predeclared safety boundaries should make omissions and unjustified inferences less likely and make reviewer corrections easier to identify.

## Basis

The repository defines these controls but has no production evidence records or completed experiment demonstrating their combined performance.

## Assumptions

- A bounded set of accessible public artefacts can represent more than one source type.
- A reviewer can apply a predeclared rubric consistently.
- The baseline and structured runs can be kept independent enough for a useful comparison.
- If these assumptions fail, the experiment will not support a workflow decision.

## Supporting evidence

None. Repository documentation provides a rationale, not performance evidence.

## Challenging evidence

None identified. The structured workflow may increase effort without improving accuracy or reviewability.

## Key uncertainty

Whether the structured workflow materially improves provenance completeness and unsupported-assertion rates on draft evidence records.

## Test criteria

Compare structured and baseline draft extractions using a fixed rubric for provenance, required context, unsupported assertions, factual accuracy, safety-boundary compliance and reviewer correction time.

## Related opportunity

`OPP-0001` proposes a constrained, review-gated evidence-extraction workflow.
