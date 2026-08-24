# Scottish primary-care evaluation source discovery

## Scope and assumptions

The request was interpreted as a first-pass search for high-value evaluation artefacts about Scottish primary care, with general practice and community-linked services in scope and no supplied claim, question, entity ID, date boundary or intended decision. "Top" was interpreted as direct Scottish relevance and a preference for official programme evaluations, not as a quality ranking or a claim that the retained set is exhaustive.

This pass performed source finding and cataloguing only. It did not extract findings or assess whether any source supports, challenges or qualifies a claim.

## Repository inspection and ID allocation

The repository-wide entity and filename search on 2026-08-24 found no allocated `SRC` IDs and no existing catalogue records beyond `_sources/catalogue/.gitkeep`. `SRC-0001` through `SRC-0003` were therefore allocated in sequence. The synthetic records under `examples/` were excluded as evidence and source candidates.

## Search vocabulary and routes

Concepts included `primary care`, `general practice`, `community pharmacy`, `community link worker`, `workforce`, `transformation`, `evaluation`, `review`, `audit`, `limitations`, `failure`, `discontinued`, `withdrawn`, `superseded`, `abandoned`, and `lessons learned`, combined with `Scotland`, `Scottish Government`, `Public Health Scotland`, `NHS Health Scotland`, `Healthcare Improvement Scotland`, `Audit Scotland`, and `Scottish Parliament`.

Search routes attempted on 2026-08-24 were:

1. repository-wide filename and content search for existing sources, evaluation titles and `SRC` identifiers;
2. web-search queries restricted to `gov.scot`, `healthcareimprovementscotland.scot`, `publichealthscotland.scot`, and `audit.scot` for Scottish primary-care evaluations; and
3. direct access attempts to authoritative publication landing pages for known candidate titles.

The internet search service returned an authentication error and direct HTTPS access was blocked by the environment's network proxy. Consequently, a systematic result screen, citation chaining, historical-version search and full-text verification could not be completed.

## Retained catalogue records

- `SRC-0001`: *Evaluation of the Primary Care Transformation Fund: final report*. Retained as a direct national Scottish primary-care programme evaluation. The title, publisher locator and publication date were recorded, but the artefact could not be opened during this pass.
- `SRC-0002`: *Evaluation of the Links Worker Programme in 'Deep End' general practices in Glasgow*. Retained as a geographically bounded Scottish general-practice evaluation. Publication date, current custodian and full-text access remain unverified.
- `SRC-0003`: *Evaluation of the GP Recruitment and Retention Fund*. Retained provisionally as a Scottish general-practice workforce evaluation. Its locator and metadata require verification before evidence extraction.

No duplicate or revised-version groupings were established.

## Rejected and deferred candidates

No additional candidate was rejected on substantive quality grounds because web results could not be screened reproducibly. Potential community-pharmacy, out-of-hours, multidisciplinary-team, digital-primary-care and local NHS Board evaluations were deferred rather than guessed. Policy descriptions, news releases and search-result snippets were not substituted for evaluation artefacts.

## Access failures, gaps and uncertainty

- All external candidates have incomplete accessibility checks; none had full text inspected.
- `SRC-0002` may require a successor-site or archive locator because NHS Health Scotland no longer operates as the publishing organisation.
- `SRC-0003` is explicitly provisional pending confirmation of the authoritative locator and bibliographic metadata.
- Community pharmacy is a material coverage gap.
- NHS Board and Health and Social Care Partnership evaluations, peer-reviewed studies, Scottish Parliament material, Audit Scotland work and negative, discontinued or abandoned initiatives remain materially under-searched.
- The absence of records in these categories must not be interpreted as absence of evaluations.

## Confidence, next actions and stopping reason

Coverage confidence is **low**. The retained records cover several directly relevant official-evaluation themes, but network failure prevented the multi-route verification, deduplication, version tracing and breadth required for a completed Source Finder search.

`SRC-0001` is the strongest candidate for a separate evidence-extraction task after full-text verification. `SRC-0002` may be useful for a locally bounded general-practice and community-links question after archive resolution. `SRC-0003` should not proceed to extraction until its identity is confirmed.

Suggested next searches are the documented vocabulary combinations above, followed by citation chaining from each verified report and targeted searches for `community pharmacy evaluation Scotland`, `primary care out of hours evaluation Scotland`, `primary care multidisciplinary team evaluation Scotland`, and the same queries with `failure`, `discontinued`, `superseded`, `abandoned`, and `lessons learned`.

The pass stopped because repeated internet access attempts failed at the authentication or proxy layer. Further metadata entry without access would have required speculation and would have violated the repository's provenance rules.
