# Source discovery: QUE-0010 demand gaps

## Scope

Bounded search for Scottish sources that could address the parts of `QUE-0010` not answered by `EVD-0002`: contact reason, repeat contacts, complexity, administrative or low-complexity demand and community-pharmacy demand. Intended use was source verification followed by draft evidence extraction where complete accessible material and methodology were sufficient. No patient-level data were sought or stored.

## Repository inspection

Existing sources reviewed for duplication and fitness included `SRC-0005`, `SRC-0009`, `SRC-0022`, `SRC-0028` and `SRC-0030`. `SRC-0005` already supports `EVD-0002` but lacks contact reason, repeat status and complexity. `SRC-0028` and `SRC-0030` are useful context on multimorbidity and deprived-practice workload but do not quantify the requested demand dimensions. `SRC-0009` is a discovery gateway rather than a verified release-specific measure of community-pharmacy reasons for contact.

## Searches performed

Search date: 2026-09-02.

- Europe PMC: `(general practice OR primary care) AND Scotland AND (consultation reason OR presenting problem)`.
- Europe PMC: `(general practice OR primary care) AND Scotland AND (repeat consultation OR frequent attender)`.
- Europe PMC: `(general practice OR primary care) AND Scotland AND (multimorbidity OR complexity)`.
- Europe PMC: `(community pharmacy OR Pharmacy First) AND Scotland AND (consultation OR activity)`.
- Targeted title and DOI checks for frequent-attender, missed-appointment, out-of-hours complexity and Pharmacy First candidates.
- Public Health Scotland, Scottish Government and NHS National Services Scotland routes were tested for community-pharmacy activity or consultation-reason material; the attempted legacy routes returned 404 and did not yield a verified release package.
- Existing catalogue locators and source records were checked before allocating a new ID.

## Retained source

### SRC-0031

- **Title:** *Statistical complexity of reasons for encounter in high users of out of hours primary care: analysis of a national service*.
- **Authors:** Sarah Stegink, Alison M Elliott and Christopher Burton.
- **Published:** 2019-02-08, *BMC Health Services Research*.
- **Identifiers:** DOI `10.1186/s12913-019-3938-z`; PMID `30736776`; PMCID `PMC6368808`.
- **Geography:** Scotland; NHS 24 national primary-care out-of-hours service.
- **Period:** 2011.
- **Access:** open full text; article XML and relevant sections inspected.
- **Descriptive mode:** measured activity and statistical analysis.
- **Likely evidential value:** direct evidence on concentration of repeat out-of-hours contacts, coded reasons for encounter and statistical reason diversity.
- **Limitations:** historical, out-of-hours only, adult population, call-handler coding, one calendar year, and statistical rather than clinical complexity.
- **Recommended action:** completed as draft `EVD-0003` and `EVD-0004` for human review.

## Other candidates and rejections

- `SRC-0028` (*Epidemiology of multimorbidity…*) was retained as contextual background only. Multimorbidity prevalence is not a measure of contact reason or repeat-contact volume, and open complete article access was not established in this run.
- `SRC-0030` (*General Practitioners at the Deep End*) was retained as contextual qualitative material; the catalogue landing page did not provide a sufficiently bounded national contact-composition measure for this extraction.
- *Social prescribing for frequent attenders in primary care* (`10.3389/fpubh.2022.902199`) was rejected for this task because the inspected metadata and abstract did not establish a Scotland-specific national demand-composition population.
- Missed-appointment and hospital-utilisation studies were rejected because they did not directly answer repeat-contact composition.
- England Pharmacy First material was rejected as non-Scottish and structurally non-transferable without a specific comparison question.
- No verified Scottish community-pharmacy dataset breaking contacts down by presenting reason was found in the bounded search.

## Coverage, gaps and stopping reason

Coverage confidence is **low to medium**. The search found one strong, open, directly relevant national Scottish out-of-hours study and tested official, bibliographic and existing-repository routes. Coverage is incomplete because the configured web-search provider was unavailable, several legacy official routes returned 404, and no release-specific community-pharmacy contact-reason dataset was verified.

The search stopped after repeated query variants produced irrelevant, non-Scottish, contextual or duplicate material and one source met the extraction threshold. The remaining gaps are current in-hours contact reasons, explicit low-complexity classification, repeat-contact patterns in routine general practice, and Scottish community-pharmacy reasons for contact. Suggested next searches are NHS 24 successor datasets, SPIRE or GP activity metadata that expose reason codes, Scottish community-pharmacy service evaluation reports, and Board-level service datasets with clear national-transferability limits.
