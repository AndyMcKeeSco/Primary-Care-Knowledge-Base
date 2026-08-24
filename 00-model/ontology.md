# Ontology

Every knowledge entity has one permanent ID. Required common metadata for every entity is `id`, `type`, `title`, `status`, `created`, `updated`, `tags`, `relationships`, `confidence`, and `provenance`. Dates use ISO `YYYY-MM-DD`; relationships use `{type, target, note?}`. `confidence` uses the controlled vocabulary. Entity-specific required and optional metadata below supplement that base. Permitted relationships list common targets, not permission to assert an unsupported edge.
## ORGANISATION (`ORG`)
- **Purpose:** A bounded institution or accountable organisational unit.
- **Represents:** an organisation with governance or delivery responsibility.
- **Does not represent:** a care location or informal stakeholder group.
- **Required entity metadata:** jurisdiction, role.
- **Optional entity metadata:** parent organisation, governance.
- **Permitted relationships:** services, care settings, interfaces, constraints, using approved verbs.
- **Lifecycle/status:** active, changed, merged, retired.

## CARE_SETTING (`CS`)
- **Purpose:** Describe a context in which care work occurs.
- **Represents:** a setting archetype or bounded delivery environment.
- **Does not represent:** a specific service or organisation.
- **Required entity metadata:** setting category, scope.
- **Optional entity metadata:** archetype, geography.
- **Permitted relationships:** organisations, services, personas, workflows, observations, using approved verbs.
- **Lifecycle/status:** active, historical, retired.

## SERVICE (`SVC`)
- **Purpose:** Model a defined offer of care or support.
- **Represents:** a service with users, purpose and delivery model.
- **Does not represent:** an organisation or individual workflow step.
- **Required entity metadata:** service purpose, users.
- **Optional entity metadata:** eligibility, hours, channel.
- **Permitted relationships:** organisations, care settings, personas, journeys, workflows, using approved verbs.
- **Lifecycle/status:** planned, active, changed, retired.

## PERSONA (`PER`)
- **Purpose:** Represent a research-grounded actor perspective.
- **Represents:** a role/archetype with goals, needs and responsibilities.
- **Does not represent:** a named individual or demographic stereotype.
- **Required entity metadata:** role, goals.
- **Optional entity metadata:** capabilities, needs, variation.
- **Permitted relationships:** care settings, workflows, decisions, problems, solutions, using approved verbs.
- **Lifecycle/status:** draft, active, challenged, retired.

## JOURNEY (`JRN`)
- **Purpose:** Trace an experience across time and boundaries.
- **Represents:** a goal-directed sequence from an actor perspective.
- **Does not represent:** a detailed operational procedure.
- **Required entity metadata:** actor, start, end.
- **Optional entity metadata:** stages, variants, outcomes.
- **Permitted relationships:** personas, services, workflows, interfaces, problems, using approved verbs.
- **Lifecycle/status:** draft, active, challenged, retired.

## WORKFLOW (`WFL`)
- **Purpose:** Represent coordinated work and hand-offs.
- **Represents:** a repeatable sequence of activities and actors.
- **Does not represent:** an individual experience or unsupported ideal process.
- **Required entity metadata:** trigger, steps, outcome.
- **Optional entity metadata:** frequency, variants, measures.
- **Permitted relationships:** personas, settings, decisions, interfaces, problems, using approved verbs.
- **Lifecycle/status:** draft, observed, validated, retired.

## DECISION (`DEC`)
- **Purpose:** Expose a consequential choice within work.
- **Represents:** a choice, inputs, rules, judgement and consequences.
- **Does not represent:** a workflow step with no meaningful alternatives.
- **Required entity metadata:** decision statement, maker, trigger.
- **Optional entity metadata:** inputs, guidance, variability, risk.
- **Permitted relationships:** workflows, personas, evidence, constraints, questions, using approved verbs.
- **Lifecycle/status:** draft, active, changed, retired.

## INTERFACE (`INT`)
- **Purpose:** Model a boundary and transfer.
- **Represents:** movement of information, work or responsibility between parties.
- **Does not represent:** mere co-location without exchange.
- **Required entity metadata:** from, to, transfer.
- **Optional entity metadata:** channel, latency, failure modes.
- **Permitted relationships:** organisations, settings, workflows, problems, constraints, using approved verbs.
- **Lifecycle/status:** draft, active, changed, retired.

## PROBLEM (`PRB`)
- **Purpose:** Define an evidenced undesirable condition.
- **Represents:** a bounded gap affecting outcomes, experience, capacity or efficiency.
- **Does not represent:** a technology absence or proposed solution.
- **Required entity metadata:** summary, affected actors/context.
- **Optional entity metadata:** scale, causes, workarounds.
- **Permitted relationships:** personas, workflows, claims, evidence, constraints, opportunities, using approved verbs.
- **Lifecycle/status:** candidate, active, challenged, resolved, retired.

## CLAIM (`CLM`)
- **Purpose:** Make a proposition reviewable.
- **Represents:** a falsifiable or qualifiable assertion.
- **Does not represent:** raw source text, observation or assumption.
- **Required entity metadata:** proposition, confidence.
- **Optional entity metadata:** scope, rationale, contradiction notes.
- **Permitted relationships:** evidence, observations, problems, hypotheses, questions, using approved verbs.
- **Lifecycle/status:** active, challenged, retired.

## EVIDENCE (`EVD`)
- **Purpose:** Capture a structured finding with provenance.
- **Represents:** a bounded result derived from source artefacts.
- **Does not represent:** the source itself or untraceable opinion.
- **Required entity metadata:** finding, source linkage, applicability.
- **Optional entity metadata:** method, population, limitations.
- **Permitted relationships:** sources, claims, problems, hypotheses, using approved verbs.
- **Lifecycle/status:** active, challenged, superseded, retired.

## OBSERVATION (`OBS`)
- **Purpose:** Record what was seen, recorded or reported.
- **Represents:** a time/context-bounded research observation.
- **Does not represent:** a general truth or inferred cause.
- **Required entity metadata:** observation, context, provenance.
- **Optional entity metadata:** participants, method, limitations.
- **Permitted relationships:** sources, personas, settings, workflows, claims, using approved verbs.
- **Lifecycle/status:** raw, structured, synthesised, withdrawn.

## CONSTRAINT (`CON`)
- **Purpose:** Represent a condition limiting action.
- **Represents:** a safety, legal, technical, financial or adoption boundary.
- **Does not represent:** a problem statement or immutable assumption.
- **Required entity metadata:** constraint, category, scope.
- **Optional entity metadata:** owner, mitigations, review date.
- **Permitted relationships:** workflows, decisions, solutions, opportunities, experiments, using approved verbs.
- **Lifecycle/status:** active, changing, retired.

## SOLUTION (`SOL`)
- **Purpose:** Record an existing or attempted intervention.
- **Represents:** a deployed, pilot, historical or abandoned intervention.
- **Does not represent:** an unevidenced opportunity presented as validated.
- **Required entity metadata:** description, lifecycle, users.
- **Optional entity metadata:** supplier, evaluation, alternatives.
- **Permitted relationships:** problems, evidence, constraints, organisations, opportunities, using approved verbs.
- **Lifecycle/status:** deployed, pilot, historical, abandoned, retired.

## HYPOTHESIS (`HYP`)
- **Purpose:** State a proposition that an experiment can test.
- **Represents:** a testable explanation or predicted mechanism.
- **Does not represent:** an established fact or broad aspiration.
- **Required entity metadata:** statement, uncertainty, confidence.
- **Optional entity metadata:** mechanism, assumptions, criteria.
- **Permitted relationships:** claims, evidence, problems, experiments, opportunities, using approved verbs.
- **Lifecycle/status:** active, supported, challenged, rejected.

## OPPORTUNITY (`OPP`)
- **Purpose:** Frame a problem-led intervention possibility.
- **Represents:** a mechanism and expected benefit worth evaluating.
- **Does not represent:** a validated solution or technology looking for a problem.
- **Required entity metadata:** problem, mechanism, uncertainty.
- **Optional entity metadata:** alternatives, impact, feasibility, risks.
- **Permitted relationships:** problems, workflows, constraints, solutions, hypotheses, experiments, using approved verbs.
- **Lifecycle/status:** candidate, prioritised, investigating, rejected.

## EXPERIMENT (`EXP`)
- **Purpose:** Resolve a decision-relevant uncertainty safely.
- **Represents:** a bounded learning activity with criteria.
- **Does not represent:** a technical demo with no learning decision.
- **Required entity metadata:** hypothesis, method, criteria, safety.
- **Optional entity metadata:** population, measures, analysis.
- **Permitted relationships:** hypotheses, opportunities, evidence, constraints, using approved verbs.
- **Lifecycle/status:** proposed, active, completed, abandoned.

## QUESTION (`QUE`)
- **Purpose:** Make a material knowledge gap actionable.
- **Represents:** a bounded question whose answer could update the model.
- **Does not represent:** a vague topic or rhetorical prompt.
- **Required entity metadata:** question, rationale, priority.
- **Optional entity metadata:** owner, method, decision enabled.
- **Permitted relationships:** claims, evidence, problems, opportunities, experiments, using approved verbs.
- **Lifecycle/status:** open, investigating, answered, closed.

## SOURCE (`SRC`)
- **Purpose:** Catalogue an artefact and its origin.
- **Represents:** an external/internal document, dataset, transcript or notes.
- **Does not represent:** an extracted finding or endorsement of content.
- **Required entity metadata:** title, source type, locator, origin.
- **Optional entity metadata:** author, publication date, access date, rights.
- **Permitted relationships:** evidence, observations, predecessor sources, using approved verbs.
- **Lifecycle/status:** catalogued, unavailable, superseded, retired.
