# Contributing

## Minimum knowledge workflow
1. Search for existing related entities and IDs.
2. Decide whether to update an entity or create one; prefer updating.
3. Copy the relevant `_templates/` file.
4. Allocate the next unused permanent ID using `00-model/naming-and-ids.md`.
5. Add provenance, including source IDs and origin/applicability.
6. Add explicit relationships using stable IDs and approved verbs.
7. Represent uncertainty and contrary findings explicitly.
8. Run `python _scripts/validate_repository.py` and `python _scripts/check_links.py`.
9. Run `python _scripts/build_index.py` and commit generated indexes.
10. Commit with a meaningful message explaining material model changes.

Never add invented evidence, anonymous unsupported factual assertions, patient-identifiable information, or assumptions presented as facts. Use lifecycle states instead of erasing challenged knowledge. Follow clinical-safety boundaries and obtain appropriate review.
