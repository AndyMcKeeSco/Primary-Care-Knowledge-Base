# Scottish Primary Care Computational Model

## Mission
Build an evolving computational model of Scottish primary care that identifies and evaluates opportunities for technology and AI to improve patient outcomes, staff experience, capacity and system efficiency.

## What This Is
A human-readable knowledge graph in Markdown and YAML: permanent, typed entities connected by explicit ID relationships. It is designed for researchers, product teams and carefully constrained AI agents. Traceability, provenance, uncertainty and competing explanations are first-class concerns.

## What This Is Not
It is not an encyclopedia, clinical guidance, an AI diagnostic system, a vendor catalogue, or a collection of disconnected research notes.

## Model
The model connects system structures and care settings to personas, journeys, workflows, decisions and interfaces. Problems and claims are tested by evidence and observations; constraints and existing solutions shape hypotheses, opportunities and experiments. Questions make missing knowledge explicit, while sources preserve provenance. See [the ontology](00-model/ontology.md).

## How Knowledge Evolves

```text
Observation → Pattern → Claim/Problem → Evidence → Hypothesis
→ Opportunity → Experiment → Learning → Updated Model
```

This is iterative rather than a claim that every item follows one linear path. Contradictory findings remain visible.

## Process Flow and Agents

Work is carried out by [deliberately constrained specialist agents](agents/README.md), each reading the [shared rules](agents/shared/) and its own role file before acting. The stages below trace how knowledge moves from an open question to a tested opportunity, and which agent acts at each step.

```text
Question → Source → Evidence/Observation → Pattern → Claim/Problem
        → Constraint/Solution → Opportunity → Hypothesis → Experiment → Learning
```

| # | Stage | What happens | Primary entities | Agent role(s) |
|---|-------|--------------|------------------|---------------|
| 1 | **Frame & prioritise questions** | Make missing knowledge explicit; rank which questions deserve effort next | [`17-questions/`](17-questions/) `QUE` | [research-planner](agents/research/research-planner.md) |
| 2 | **Catalogue sources** | Discover candidate sources and keep the catalogue's integrity, IDs and lineage sound | [`_sources/`](_sources/) `SRC` | [source-finder](agents/research/source-finder.md), [source-catalogue-steward](agents/research/source-catalogue-steward.md) |
| 3 | **Extract evidence / record observations** | Turn an approved, question-linked assignment into bounded, provenance-tracked findings | [`10-evidence/`](10-evidence/) `EVD`, [`11-observations/`](11-observations/) `OBS` | [evidence-extractor](agents/research/evidence-extractor.md) (run routinely via the [daily extraction job](agents/research/daily-evidence-extractor-job.md)), [observation-synthesiser](agents/synthesis/observation-synthesiser.md) |
| 4 | **Find patterns & model context** | Surface candidate patterns and model the settings, workflows and interfaces they sit in | [`11-observations/`](11-observations/), [`02-care-settings/`](02-care-settings/), [`05-workflows/`](05-workflows/), [`07-interfaces/`](07-interfaces/) | [pattern-finder](agents/synthesis/pattern-finder.md), [care-setting-modeller](agents/synthesis/care-setting-modeller.md), [workflow-modeller](agents/synthesis/workflow-modeller.md), [interface-analyst](agents/discovery/interface-analyst.md) |
| 5 | **Test claims & problems** | Match findings to claims and problems; challenge them; keep contradictions visible | [`08-problems/`](08-problems/) `PRB`, [`09-claims/`](09-claims/) `CLM` | [observation-claim-matcher](agents/validation/observation-claim-matcher.md), [claim-challenger](agents/validation/claim-challenger.md), [evidence-auditor](agents/validation/evidence-auditor.md), [contradiction-hunter](agents/research/contradiction-hunter.md) |
| 6 | **Shape opportunities** | Map existing solutions and constraints; generate and critique problem-led opportunities | [`12-constraints/`](12-constraints/), [`13-solutions/`](13-solutions/), [`15-opportunities/`](15-opportunities/) | [solution-landscape-analyst](agents/discovery/solution-landscape-analyst.md), [opportunity-generator](agents/discovery/opportunity-generator.md), [opportunity-critic](agents/discovery/opportunity-critic.md) |
| 7 | **Form & test hypotheses** | Turn opportunities into testable hypotheses and the smallest safe experiment | [`14-hypotheses/`](14-hypotheses/) `HYP`, [`16-experiments/`](16-experiments/) `EXP` | [experiment-designer](agents/experimentation/experiment-designer.md), [experiment-reviewer](agents/experimentation/experiment-reviewer.md) |
| 8 | **Feed learning back** | Update entity status, confidence and questions from what was learned; reopen questions as needed | all layers, [`17-questions/`](17-questions/) | [research-planner](agents/research/research-planner.md), [contradiction-hunter](agents/research/contradiction-hunter.md) |

At every stage the [shared rules](agents/shared/) apply — [operating principles](agents/shared/operating-principles.md), [evidence rules](agents/shared/evidence-rules.md), [confidence rules](agents/shared/confidence-rules.md), [repository write rules](agents/shared/repository-write-rules.md) and, overriding output completion, the [clinical-safety boundaries](agents/shared/clinical-safety-boundaries.md). Agents propose changes outside their write scope rather than making them silently, and human review is mandatory before drafts become active or receive confidence. Some specialist roles are V1 placeholders pending specification; see [`agents/README.md`](agents/README.md).

A worked example of stages 1–3: question `QUE-0013` (workforce capacity) drove assignment `daily-001` against source `SRC-0020`, which the daily extractor turned into evidence `EVD-0001` (Scottish GP headcount and WTE), all traceable by ID.

## Getting Started

```bash
python _scripts/validate_repository.py
python _scripts/check_links.py
python _scripts/build_index.py
```

No third-party Python packages are required. Start with [CONTRIBUTING.md](CONTRIBUTING.md), the [model](00-model/objective.md), and the relevant [agent role](agents/README.md).

## Current Scope
Scottish primary care, initially with deeper focus on general practice, community pharmacy, and their interfaces with the wider system. Synthetic examples demonstrate structure only; they are not evidence.
