---
id: EVD-0004
type: evidence
title: Reasons for encounter differed among high users of Scottish out-of-hours primary care
status: draft
created: 2026-09-02
updated: 2026-09-02
tags: [scotland, general-practice, out-of-hours, contact-reason, complexity, mental-health, research]
relationships:
  - type: interacts_with
    target: QUE-0010
    note: "Partially addresses reason mix and statistical complexity among repeat out-of-hours users."
confidence: unknown
provenance:
  sources:
    - SRC-0031
    - https://doi.org/10.1186/s12913-019-3938-z
    - https://pmc.ncbi.nlm.nih.gov/articles/PMC6368808/
---

# Reasons for encounter differed among high users of Scottish out-of-hours primary care

## Finding

Among the 13,981 adults designated high users of Scottish NHS 24 out-of-hours primary care in 2011, 19.4% had at least one contact coded for a mental-health reason and 8.4% had at least one contact specifically coded for a major illness such as cancer or diabetes. Compared with other users, contacts with high users were relatively more likely to have a mental-health reason (odds ratio 3.26) and less likely to be coded for upper-respiratory infection (0.43) or skin, eye, ear, nose and throat reasons (0.33).

The study found that statistical diversity of reasons for encounter increased with contact count, but its reason-for-encounter complexity measures did not independently predict ongoing high use. A previous mental-health reason was modestly predictive of another consultation above five contacts, with reported odds ratios between 1.2 and 1.9 depending on prior contact count.

## Source context

`SRC-0031` analysed call-handler-coded presenting reasons in national Scottish NHS 24 out-of-hours data. Its “complexity” construct is statistical diversity and sequencing of reason categories, not a clinical assessment of case complexity.

## Population and geography

Adults aged over 18 in the study's 2011 Scotland-wide NHS 24 out-of-hours dataset. These detailed comparisons concern the 13,981 people meeting the study threshold of five or more contacts, compared with remaining adult users where stated.

## Method

Call-handler reason codes were mapped into 14 symptom-based categories. The authors calculated number of reason categories, Herfindahl index, Shannon state entropy and transition entropy, then examined associations with patient characteristics and subsequent contact. Odds ratios for reason categories compare contacts involving high users with contacts involving other users.

## Time period

Calendar year 2011.

## Applicability to Scotland

Directly applicable to coded adult NHS 24 out-of-hours contacts in Scotland for 2011. It gives historical evidence about repeat-contact reason mix and statistical heterogeneity, but not in-hours general-practice demand, community-pharmacy demand, clinical complexity or current service patterns.

## Supports

Not assessed in this extraction.

## Challenges

Not assessed in this extraction.

## Limitations

Reasons were selected by call handlers from a menu and represent presenting symptoms rather than final diagnoses. The data cannot distinguish new symptoms from exacerbations of existing conditions and identify mental health only when it was the stated reason, not when it was a comorbidity or contributing factor. The study used one year of out-of-hours data, limited demographics and no richer clinical covariates. Short contact sequences constrain entropy measures. The findings do not identify “low complexity”, avoidable contacts or work suitable for automation.

## Extraction notes

- Driving question: `QUE-0010`.
- Canonical source: `SRC-0031`.
- Exact locations: body sections *Categories of reason for consultation*, *Results*, *Relationship of complexity to patient characteristics*, *Predictive value of complexity of RfE on future contact*, *Summary of main findings*, *Strengths and limitations* and *Conclusion*; Table 2 and Figure 3.
- Full text inspected through PubMed Central on 2026-09-02.
- Claim bearing was not authorised and was not assessed.
- Confidence recommendation for human review: medium for the bounded historical comparisons; low for transfer to current, in-hours or clinical-complexity questions.
