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

## Getting Started

```bash
python _scripts/validate_repository.py
python _scripts/check_links.py
python _scripts/build_index.py
```

No third-party Python packages are required. Start with [CONTRIBUTING.md](CONTRIBUTING.md), the [model](00-model/objective.md), and the relevant [agent role](agents/README.md).

## Current Scope
Scottish primary care, initially with deeper focus on general practice, community pharmacy, and their interfaces with the wider system. Synthetic examples demonstrate structure only; they are not evidence.
