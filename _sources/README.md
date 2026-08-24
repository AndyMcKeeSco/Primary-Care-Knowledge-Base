# Source Library

`catalogue/` holds `SOURCE` entities for traceable artefacts. Catalogue entries are not evidence or endorsement; structured findings belong in `10-evidence/`. Never store patient-identifiable material.

The library's human-readable control document is [`catalogue.md`](catalogue.md). Keep it aligned with the source files: it must show the last audit date, unresolved ID collisions, version or duplicate lineages, correction history, unavailable holdings, and material gaps. It supplements rather than replaces the metadata in each source record.

## Responsibilities

The [Source Catalogue Steward](../agents/research/source-catalogue-steward.md) owns routine catalogue integrity. A contributor adding or changing a source is still responsible for following this procedure and leaving the catalogue consistent.

## Adding a source

1. Search the whole repository for the artefact by locator, DOI or other identifier, title variants, creator, and existing `SRC` references. Check `catalogue.md` for unresolved collisions and lineages.
2. Decide whether the item is the same artefact, a distinct edition or version, part of a publication series, or a genuinely new source. Update the existing record when it already represents the artefact; do not create a second record merely because a title or URL changed.
3. Copy `_templates/source.md` and catalogue only verified metadata. Record unknowns and failed access attempts explicitly; never infer bibliographic details from a title or search snippet.
4. Allocate the next unused four-digit `SRC` number only after a repository-wide search. An ID is permanent, never reused, and never silently changed. The filename starts with that ID and a lowercase kebab-case slug.
5. Describe geographic origin and applicability separately. Mark non-Scottish sources and do not imply that evidence from elsewhere applies to Scottish primary care.
6. Record the authoritative locator where known, access date and state, rights or sensitivity, quality limitations, and related evidence. Do not copy restricted full text into the repository.
7. Add or update the entry, lineage note, issue, and audit date in `catalogue.md` in the same change.
8. Run `python _scripts/validate_repository.py`, `python _scripts/check_links.py`, and `python _scripts/build_index.py`; inspect the generated indexes and final diff.

## Managing duplicates, versions, and ID collisions

- **Same artefact:** preserve one canonical record. Merge only verified complementary metadata and provenance, then mark the redundant record as superseded rather than deleting its history.
- **Different version or component:** retain separate records when a distinct edition, release, annex, dataset, or archived snapshot matters for traceability. Document the lineage and do not imply independent corroboration.
- **Similar title:** do not merge until identity has been established from identifiers, provenance, or the artefacts themselves.
- **Duplicate ID:** freeze new ID allocation, register the collision in `catalogue.md`, and inspect Git history and inbound references. Keep the ID with the demonstrably established allocation; give each other distinct artefact the next unused ID and update its filename, metadata, catalogue entry, and unambiguous references together. Log the correction permanently.
- **Ambiguous reference:** never guess which source an inbound `SRC` reference meant. Record and escalate it before changing IDs.

Lifecycle correction is preferred to deletion. A tidy folder is not worth losing provenance, prior locators, contradictory material, or the ability to explain an old reference.

## Catalogue review

Review the library after every material source change and periodically as a dedicated audit. Reconcile file paths, front-matter IDs, catalogue entries, statuses, locators, related-evidence links, and all inbound `SRC` references. Check for:

- duplicate IDs and IDs that do not match filenames;
- duplicate artefacts, changed titles or locators, new editions, and publication-series relationships;
- stale access states, broken or non-authoritative locators, and missing archive links;
- missing provenance, rights, sensitivity, geography, limitations, or access dates;
- sources presented as evidence, and evidence whose source cannot be identified; and
- restricted or patient-identifiable content that must not be stored here.

The review ends only when `catalogue.md` states either that these checks passed or which issues remain open, why they could not be resolved safely, and the next action.
