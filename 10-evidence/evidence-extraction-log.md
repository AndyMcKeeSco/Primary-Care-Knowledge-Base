# Evidence Extraction Log

Chronological record of approved evidence-extraction assignments and their outcomes. Assignment definitions live in `10-evidence/assignments/`; this log does not contain evidence findings.

| Date | Assignment | Source | Status | Evidence IDs | Notes |
|---|---|---|---|---|---|
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | approved | — | Awaiting bounded extraction. |
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | blocked | — | The canonical 2023 locator redirects to the 2022 release, so source identity and the required full 2023 publication package cannot be verified. Human action: correct or verify `SRC-0020` and provide an authoritative accessible 2023 artefact and methodology. |
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | unblocked | — | Year updated to 2022 as this is the correct year|
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | blocked | — | The canonical source now identifies the 2022 release and the authoritative URL resolves to the 2022 publication, but the approved assignment still asks for the 2023 survey and defines a 2023 population. Human action: update and re-approve the assignment title, question and population for the 2022 release, or provide a verified 2023 source record and artefact. |
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | unblocked | — | Assignment title, question and population updated and re-approved for the verified 2022 release. |
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | blocked | — | Extraction reached a review-ready draft, but the repository quality gate failed on 4 pre-existing duplicate source IDs and 20 stale broken links in the generated entity index; the draft and generated-index changes were reverted. Human action: resolve the duplicate `SRC-0001`–`SRC-0004` identities and stale index links, regenerate the indexes, then update and re-approve this assignment to reopen it. |
| 2026-09-01 | [daily-001](assignments/daily-001.md) | SRC-0020 | unblocked | — | Duplicate source IDs were reassigned to `SRC-0027`–`SRC-0030`, generated indexes were rebuilt, and repository validation and link checks pass. Assignment reopened. |
| 2026-09-02 | [daily-001](assignments/daily-001.md) | SRC-0020 | completed | EVD-0001 | Extracted the Scotland GP headcount (4,514) and estimated WTE (3,494) at 31 March 2022 with definitions, coverage, method and limitations preserved. |
