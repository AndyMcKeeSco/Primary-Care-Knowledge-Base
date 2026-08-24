# Source Catalogue

This is the human-readable control document for source holdings. Source records remain the authoritative descriptions of individual artefacts; this catalogue records library-level integrity, lineages, collisions, and work still requiring review. It is not an evidence index and does not endorse any source or its assertions.

## Catalogue health

- **Last audited:** 2026-08-24
- **Scope:** Markdown source records in `_sources/catalogue/`
- **Integrity status:** ID collisions and probable duplicate artefact records are present; do not allocate another `SRC` ID until they have been reconciled.
- **Next action:** the Source Catalogue Steward must establish allocation history and inbound-reference intent before renumbering or consolidating any record.

## ID collision register

The following IDs occur in more than one source record. Every path is listed so that the conflict is visible and reviewable; listing a file here does not decide which record owns the ID.

| ID | Records | Status |
|---|---|---|
| `SRC-0001` | `SRC-0001-2018-gms-contract-scotland.md`<br>`SRC-0001-evaluation-primary-care-transformation-fund.md`<br>`SRC-0001-public-health-scotland-general-practice-workforce-survey.md`<br>`SRC-0001-scottish-government-primary-care-case-studies.md`<br>`SRC-0001-the-2018-general-medical-services-contract-in-scotland.md` | Open; includes a probable duplicate GMS-contract record that requires provenance comparison. |
| `SRC-0002` | `SRC-0002-evaluation-links-worker-programme.md`<br>`SRC-0002-health-and-social-care-delivery-plan.md`<br>`SRC-0002-healthcare-improvement-scotland-primary-care-resources.md`<br>`SRC-0002-primary-care-monitoring-evaluation-strategy.md`<br>`SRC-0002-public-health-scotland-general-practice-in-hours-activity.md` | Open. |
| `SRC-0003` | `SRC-0003-achieving-excellence-in-pharmaceutical-care.md`<br>`SRC-0003-digital-health-and-care-innovation-centre-case-studies.md`<br>`SRC-0003-evaluation-gp-recruitment-retention-fund.md`<br>`SRC-0003-nhs-scotland-open-data-gp-practice-contact-details-list-sizes.md`<br>`SRC-0003-primary-care-transformation-fund-evaluation.md` | Open; includes a probable duplicate Primary Care Transformation Fund evaluation that requires provenance comparison. |
| `SRC-0004` | `SRC-0004-general-practice-workforce-survey-2023.md`<br>`SRC-0004-national-health-and-social-care-workforce-plan-part-3.md`<br>`SRC-0004-public-health-scotland-scottish-disease-prevalence-data.md` | Open. |
| `SRC-0005` | `SRC-0005-general-practice-in-hours-activity.md`<br>`SRC-0005-national-clinical-strategy-for-scotland.md`<br>`SRC-0005-public-health-scotland-prescriptions-in-the-community.md` | Open; the activity record may duplicate a `SRC-0002` artefact and requires provenance comparison. |
| `SRC-0006` | `SRC-0006-health-care-experience-survey-2023-24.md`<br>`SRC-0006-public-health-scotland-community-pharmacy.md` | Open. |
| `SRC-0007` | `SRC-0007-achieving-excellence-pharmaceutical-care.md`<br>`SRC-0007-scottish-government-scottish-health-survey.md` | Open; the pharmaceutical-care record may duplicate a `SRC-0003` artefact and requires provenance comparison. |

`SRC-0008` currently occurs once. That observation does not reserve lower collided IDs or prove that `SRC-0008` was allocated correctly; allocation history still needs review.

## Correction log

Record completed collision resolutions and consolidations here. Each entry must include the date, old ID and path, retained or new ID and path, rationale, provenance used to decide ownership, inbound references reviewed, and reviewer. Never remove an entry when the catalogue later becomes clean.

No corrections have yet been recorded.

## Maintenance rule

The operating procedure, required metadata, allocation checks, duplicate handling, and review cadence are defined in [`README.md`](README.md). The responsible role is [`agents/research/source-catalogue-steward.md`](../agents/research/source-catalogue-steward.md).
