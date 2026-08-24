# Baseline Scottish primary-care source discovery — 2026-08-24

## Scope and assumptions

This pass establishes a small baseline catalogue of high-value source families for research into Scottish general practice and community pharmacy. Because no narrower question or repository entity was supplied, the bounded coverage dimensions were: intended service model, implementation and evaluation, workforce, recorded activity, and reported patient experience. Scotland-specific sources were prioritised. Clinical guidance, individual NHS Board material, patient-level data, dentistry, optometry, and evidence extraction were out of scope.

“Top” means a useful starting set across distinct research functions, not a quality ranking and not an exhaustive bibliography. A source was not interpreted as evidence, and no claim bearing was assessed.

## Repository inspection

The catalogue contained no `SRC` entities before this search. The repository-wide ID search found no allocated production `SRC` IDs; synthetic examples use the separate `9000` range. `SRC-0001` through `SRC-0007` were therefore allocated sequentially. No claim, evidence, workflow, interface, problem, or question IDs were available to relate without inventing unsupported edges.

## Search vocabulary and hierarchy

Concept groups used were:

- geography and organisations: `Scotland`, `Scottish Government`, `Public Health Scotland`, `NHS Scotland`;
- settings: `general practice`, `primary care`, `community pharmacy`, `pharmaceutical care`;
- measurement: `workforce survey`, `in-hours activity`, `patient experience`, `evaluation`, `monitoring`;
- policy and change: `2018 GMS contract`, `transformation fund`, `strategy`, `implementation`, `review`, `limitations`, `failure`, `discontinued`, `superseded`, and `lessons learned`.

The planned hierarchy covered official Scottish policy, official statistics, programme evaluation, independent audit and parliamentary material, peer-reviewed research, and professional sources. Authoritative Scottish Government and Public Health Scotland publication families could be identified from established publication citations. Live web search and artefact retrieval were then attempted on 2026-08-24, but the environment's internet routes returned authentication or proxy-denial errors. Consequently, full-text inspection and the independent-audit, parliamentary, bibliographic, historical-version, failure, discontinuation, and citation-trail searches could not be completed reliably.

## Retained catalogue records

| ID | Source | Research function | Access verification |
|---|---|---|---|
| SRC-0001 | The 2018 General Medical Services Contract in Scotland | Intended general-practice contract and service model | Authoritative locator recorded; live access not rechecked |
| SRC-0002 | Primary care national monitoring and evaluation strategy | Intended evaluation framework | Authoritative locator recorded; live access not rechecked |
| SRC-0003 | Evaluation of the Primary Care Transformation Fund | Early programme evaluation | Locator recorded; authorship, method, and exact date unresolved |
| SRC-0004 | General Practice Workforce Survey 2023 | Measured workforce | Publication locator recorded; tables and methods not inspected |
| SRC-0005 | General practice in-hours activity | Recorded activity publication series | Series locator recorded; current release and coverage not inspected |
| SRC-0006 | Health and Care Experience Survey 2023/24 national results | Reported patient experience | Publication locator recorded; tables and technical report not inspected |
| SRC-0007 | Achieving excellence in pharmaceutical care | Intended community-pharmacy policy | Authoritative locator recorded; successors not checked |

The landing pages, downloads, tables, dashboards, questionnaires, and technical appendices belonging to one named release or publication package should be deduplicated as locators or components of that source, unless inspection shows that an item is a substantively independent artefact. Revised editions must instead be preserved as related versions.

## Rejected or deferred candidates

No candidate was rejected on substantive grounds because search results and full texts were unavailable. The following categories were deferred rather than populated with guessed records:

- Audit Scotland and Scottish Parliament reviews;
- peer-reviewed Scottish primary-care studies;
- NHS Board and Health and Social Care Partnership evaluations;
- professional and representative-body workforce sources;
- NHS Pharmacy First Scotland specifications, activity sources, and evaluations;
- superseded, withdrawn, failed, discontinued, or abandoned programmes; and
- current successors to older national strategies.

This preserves the gap rather than silently substituting English or UK-wide evidence.

## Access failures, uncertainty, and next actions

The retained records distinguish confirmed established citation metadata from unresolved metadata and explicitly state that live access was not rechecked. `full_text_inspected` is therefore false for every candidate in this pass. Publication dates given only as a year, report authorship for SRC-0003, series refresh dates, methodology, coverage, rights, and current availability remain unresolved.

Recommended next searches, once web access is available, are:

1. Reopen every recorded authoritative locator and inspect the complete publication package, recording identifiers, exact dates, authors, rights, period covered, methodology, and access status.
2. Search `site:audit.scot primary care general practice Scotland review evaluation`, and follow citations to original data and programme reports.
3. Search the Scottish Parliament site for `primary care`, `2018 GMS contract`, `multidisciplinary team`, `implementation`, `community pharmacy`, and `lessons learned`.
4. Search PubMed, Crossref, university repositories, and citation trails for Scotland-specific evaluated processes and outcomes, separating national from local evidence.
5. Search official sites and archives with `superseded`, `withdrawn`, `discontinued`, `failure`, `abandoned`, and former programme names.
6. Search specifically for NHS Pharmacy First Scotland service specifications, administrative activity, evaluation, limitations, and predecessor Minor Ailment Service material.

The strongest candidates for a later evidence-extraction task are SRC-0003 through SRC-0006 because they may contain evaluated process, measured activity, workforce, or reported-experience material. SRC-0001, SRC-0002, and SRC-0007 should be used to extract intended policy only and must not be used alone to infer actual practice.

## Coverage confidence and stopping reason

Coverage confidence is **low**. The starter set spans several principal research functions and is Scotland-specific, but live verification, independent scrutiny, peer-reviewed literature, local variation, community-pharmacy measurement, negative or discontinued initiatives, and version history remain material gaps. Searching stopped because repeated network attempts were blocked by the environment; continuing without artefact access would risk inventing metadata or overstating verification.
