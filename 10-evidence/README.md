# Evidence

Structured findings derived from catalogued sources; source artefacts belong in `_sources/`.

- `assignments/` contains human-approved, non-entity extraction assignments for bounded routine runs. Each assignment carries a `question_id` linking it to the open `QUE` question it helps answer, so every extraction is traceable to a decision-relevant question.
- `evidence-extraction-log.md` records assignment approvals, completed runs and blockers.
- Evidence-category folders contain production `EVD` entities; assignment and log files are control documents and are excluded from entity validation and generated indexes.
