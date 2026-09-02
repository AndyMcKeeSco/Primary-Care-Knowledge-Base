---
id: EVD-0002
type: evidence
title: Recorded Scottish general-practice encounter composition in January 2026
status: draft
created: 2026-09-02
updated: 2026-09-02
tags: [scotland, general-practice, demand, activity, encounters, statistics]
relationships: []
confidence: unknown
provenance:
  sources:
    - SRC-0005
    - https://publichealthscotland.scot/publications/general-practice-in-hours-activity-visualisation/general-practice-in-hours-activity-visualisation-as-at-31-january-2026/
    - https://publichealthscotland.scot/media/37509/data-january2026.xlsx
---

# Recorded Scottish general-practice encounter composition in January 2026

## Finding

The Public Health Scotland release workbook records **7,949,664** whole-practice encounters for Scotland in January 2026. Of these, **4,214,544 (53.0%)** were classified as indirect, **2,860,541 (36.0%)** as direct, **869,243 (10.9%)** as undefined and **5,336 (0.1%)** as external direct. The largest named encounter groups were surgery consultation (**2,269,014; 28.5%**), general administration (**2,003,058; 25.2%**), clinical administration (**1,090,198; 13.7%**) and medicines management (**844,026; 10.6%**). Percentages were calculated by the extractor from the workbook's Scotland-level counts and rounded to one decimal place.

## Source context

`SRC-0005` is Public Health Scotland's monthly *General Practice in-hours activity visualisation* series. The inspected release, published on 3 March 2026 and last updated on 6 April 2026, is labelled "Official statistics in development" and reports encounters recorded in participating Scottish general-practice clinical systems. The publisher states that encounters are not synonymous with appointments: direct encounters involve patient contact for clinical care, while indirect encounters include activity without direct patient contact, such as reviewing prescriptions or clinical administration.

## Population and geography

The finding is the Scotland aggregate for encounters recorded by the whole practice team, including administrative staff, in participating general practices. The release reports that data were extracted from approximately 93% of practices across Scotland. Eight practices in multiple NHS Board areas were excluded from the January 2026 data because clinical-system migration affected data extraction and accuracy.

## Method

Counts were read from the release workbook's `Data` worksheet by filtering `MonthYear` to January 2026 and `Geography` to Scotland, then summing `Count` by `EncounterClass` and `EncounterGroup`. Class counts sum to the reported total of 7,949,664. Percentages are extractor calculations using that total; they are not copied from a source table. Public Health Scotland extracts the underlying activity from participating general-practice clinical systems and classifies recorded encounters by staff group, encounter class and encounter group.

## Time period

January 2026. The publication series contains a longer time series from January 2018, but this finding does not compare months or infer a trend.

## Applicability to Scotland

Directly applicable to recorded in-hours general-practice activity in participating Scottish practices for the stated month. It is not a complete measure of primary-care demand or workload and does not cover community pharmacy. The categories do not identify contact reason, repeat status, complexity, duration, appropriateness, clinical value or whether an encounter could be automated, self-served or redirected.

## Supports

Not assessed in this extraction.

## Challenges

Not assessed in this extraction.

## Limitations

Not all general-practice activity is recorded in clinical systems, and the release states that complexity and duration are unavailable. Practice coverage is approximately 93% and eight practices were excluded because of migration-related accuracy problems. The publisher subsequently paused the publication while those issues were investigated. Default entries in clinical systems may misclassify encounter type; recording improvements can affect trends; some encounters cannot be mapped to a staff group; monthly counts vary with working days; and data remain subject to revision. The counts therefore describe recorded encounters, not all work, appointments, patient need, low-complexity demand or avoidable demand. They are not directly comparable with NHS England or NHS Wales activity publications because methods differ.

## Extraction notes

- Driving question: `QUE-0010` — what repeat and low-complexity contacts dominate primary-care demand?
- Bounded extraction question: what encounter classes and named encounter groups made up recorded whole-practice Scottish general-practice activity in January 2026?
- Canonical source: `SRC-0005`.
- Exact release: *General Practice in-hours activity visualisation — as at 31 January 2026*, published 3 March 2026.
- Exact data location: `data-january2026.xlsx`, worksheet `Data`; `Geography = Scotland`; `MonthYear = 2026-01-01`; columns `EncounterClass`, `EncounterGroup` and `Count`.
- Release-page sections used for interpretation: *About this release*, *Main points* and *Data quality*.
- Claim bearing was not authorised and was not assessed.
- This finding partially addresses demand composition by recorded activity category. It does not answer the question's contact-reason, repeat-status or complexity components because the source does not supply them.
