---
id: CS-0001
type: care_setting
title: Scottish general practice
status: active
created: 2026-08-24
updated: 2026-09-01
tags: [scotland, general-practice, archetype]
relationships:
  - type: interacts_with
    target: PER-0001
    note: "Service-user perspective; detailed experiences remain unextracted."
  - type: interacts_with
    target: PER-0002
    note: "GP perspective; detailed responsibilities and variation remain unextracted."
  - type: interacts_with
    target: PER-0003
    note: "Broad multidisciplinary-team placeholder pending role-level extraction."
  - type: interacts_with
    target: PER-0004
    note: "Reception perspective; responsibilities and local variation remain unextracted."
  - type: interacts_with
    target: PER-0005
    note: "General-practice nursing perspective; clinical scope remains unextracted."
  - type: interacts_with
    target: PER-0006
    note: "Specialist-nursing umbrella pending specialty-specific evidence."
  - type: interacts_with
    target: PER-0007
    note: "Phlebotomy perspective; employment and service model remain unextracted."
  - type: interacts_with
    target: PER-0008
    note: "Practice-management perspective; remit remains unextracted."
  - type: interacts_with
    target: PER-0009
    note: "Healthcare-support perspective; terminology and delegated scope remain unextracted."
confidence: low
provenance:
  sources:
    - _sources/catalogue/SRC-0012-the-2018-general-medical-services-contract-in-scotland.md
    - _sources/catalogue/SRC-0020-general-practice-workforce-survey-2023.md
    - _sources/catalogue/SRC-0005-public-health-scotland-general-practice-in-hours-activity.md
    - _sources/catalogue/SRC-0022-health-care-experience-survey-2023-24.md
---

# Scottish general practice

## Definition

A setting archetype for care work occurring in Scottish general practice. The catalogued 2018 General Medical Services contract is a source for the intended contractual and service model. This record does not establish that the intended model was implemented uniformly or that it produced particular outcomes.

This is not a profile of an individual practice, organisation or service.

## Scope

- **Setting category:** general practice
- **Archetype:** Scottish general-practice delivery environment
- **Geography:** Scotland
- **Included:** work represented by the catalogued sources as general-practice workforce, in-hours activity or reported experience.
- **Excluded:** out-of-hours care, patient-level clinical guidance, and assumptions about any individual practice.

## Actors

Nine draft actor perspectives are now linked to this setting:

- `PER-0001`: a person using Scottish general practice;
- `PER-0002`: a general practitioner in Scottish general practice; and
- `PER-0003`: a deliberately broad multidisciplinary-team member supporting Scottish general practice;
- `PER-0004`: a receptionist;
- `PER-0005`: a nurse in general practice;
- `PER-0006`: a specialist nurse supporting general practice;
- `PER-0007`: a phlebotomist supporting general practice;
- `PER-0008`: a practice manager; and
- `PER-0009`: a healthcare support worker.

These records identify perspectives for further research; they are not detailed, validated personas. Their catalogue sources distinguish reported service-user experience, intended contractual roles and measured workforce, but no bounded `EVD` finding has yet been extracted. The named records deliberately expose differences hidden by the broad multidisciplinary placeholder without asserting job content. Employment, co-location, availability, goals, responsibilities, capabilities and variation remain open.

## Services

The 2018 contract describes an intended contractual and service model. The source has not yet been extracted into bounded evidence, so this record does not enumerate services or imply that a stated service is available in every Scottish practice.

## Typical work

The catalogued in-hours activity series may describe recorded activity in participating practices. Release-specific encounter definitions, coverage, exclusions and data-supply changes have not been inspected. Typical work, its frequency and its distribution between roles therefore remain open rather than being inferred from the series title.

## Variation

Variation between practices and over time is expected but has not been characterised from extracted evidence. In particular, participating-practice coverage in the activity series and geographic or practice-level variation in survey results require verification before they can support a more detailed archetype.

## Technology

No technology finding has been extracted from the catalogued research for this setting.

## Constraints

No setting-specific constraint has been established through an evidence record. Contractual intent, workforce measures, recorded activity and reported patient experience are distinct research lenses and must not be treated as interchangeable measures of implementation, workload, need or care quality.

## Evidence

No `EVD` entity currently supports this care-setting record. Its bounded definition and research dimensions come from four Scottish source records:

- the 2018 GMS contract, catalogued as intended policy and service model;
- the General Practice Workforce Survey 2023, catalogued as measured workforce;
- General practice in-hours activity, catalogued as a recorded-activity publication series; and
- the Health and Care Experience Survey 2023/24, catalogued as reported patient experience.

The source catalogue records the historical `SRC` ID collisions as resolved and preserves their correction history. Provenance now uses the canonical catalogue paths and IDs. The source artefacts were not fully inspected in the research pass. Confidence is **low**: the Scottish origin and relevance of the source records are clear, but the available catalogue metadata does not warrant a detailed account of practice operations.

## Open questions

- Which named clinical, operational, administrative, management, support, carer and advocate actors are supported by bounded, release-specific findings from these sources?
- For each actor, what goals, responsibilities, capabilities, employment or governance arrangements, and variations are evidenced?
- How much of the activity series' participating-practice coverage is applicable to a national setting archetype?
- What variation by practice, geography, population and time should the archetype preserve?
- Which aspects of the 2018 intended model were implemented, changed, superseded or not implemented?
- What technology and cross-setting interfaces are evidenced rather than assumed?
