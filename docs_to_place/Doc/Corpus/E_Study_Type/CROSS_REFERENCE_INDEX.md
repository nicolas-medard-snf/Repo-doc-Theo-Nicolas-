# Cross-Reference Index — `E_Study_Type`

> This index is the **primary reasoning interface** of the corpus. Agents start here for every substantive task. Keep it navigable: it is a map, not a dump.

## Concepts → Entries

| Concept | Entries (`paper_id`) |
|---------|----------------------|
| Computational method / bioinformatics algorithm | `kim_2020_hrd_wes`, `sztupinszki_2018_scarhrd` |
| Predictive ML model | _(none yet — see `sammut_2022_multiomic_ml` in A6)_ |
| Clinical trial | _(none yet — see `schmid_2024_keynote522_os` in B3)_ |
| Genomic cohort / landscape study | `kim_2025_wgs_breast_landscape` |
| Review | _(none yet — see `giovani_2025_chromatin_remodeling` in A5)_ |
| Sequencing platform (WGS / WES / SNP-array / NGS) | `kim_2020_hrd_wes`, `sztupinszki_2018_scarhrd`, `kim_2025_wgs_breast_landscape` |

## Methods / Mechanisms / Schools of Thought → Entries

| Method / mechanism | Entries |
|--------------------|---------|
| WES HRD scoring (Sequenza + scarHRD; LOH/TAI/LST sum; threshold ≥42) | `kim_2020_hrd_wes` |
| scarHRD (NGS HRD scar migration) | `sztupinszki_2018_scarhrd` |
| WES vs SNP-array/OncoScan HRD concordance | `kim_2020_hrd_wes`, `sztupinszki_2018_scarhrd` |
| IntOGen driver consensus (multi-algorithm) | `kim_2025_wgs_breast_landscape` |
| WGS HRD composite scoring (signatures + CNV) | `kim_2025_wgs_breast_landscape` |

## Open Questions / Problems → Entries

| Open question | Entries that engage it |
|---------------|------------------------|
| AQ-1 — WES-derived drivers (data/method compatibility) | `kim_2020_hrd_wes`, `sztupinszki_2018_scarhrd`, `kim_2025_wgs_breast_landscape` |
| AQ-3 — method-grade evidence for driver prioritization | `kim_2025_wgs_breast_landscape`, `kim_2020_hrd_wes`, `sztupinszki_2018_scarhrd` |

## Contradictions / Tensions

| Tension | Entries in tension | How to interpret |
|---------|--------------------|------------------|
| _(none yet)_ | _(none yet)_ | _(none yet)_ |

## Hub Entries

> Entries that connect many others. Read these first when entering the corpus cold.

- `kim_2025_wgs_breast_landscape` — primary E4 hub: breast WGS landscape (drivers + signatures) plus a neoadjuvant pCR substudy; the upstream data resource for A4/A1.
- `sztupinszki_2018_scarhrd` / `kim_2020_hrd_wes` — the WES/NGS HRD-computation methods that unblock the A1 HRD signal.

## Unexplored Combinations

- scarHRD HRD-sum + Telli ≥42 threshold applied to the project's WES cohorts (bridges `E1`→`A1`).
- Kim WGS driver priors + Caswell-Jin multi-region WES ITH framework for HER2+ neoadjuvant non-pCR interpretation.

## Gaps (curation priorities)

- **OCR backlog**: all three E entries are grounded on external/publisher text because the local PDFs are not text-extractable on this host — OCR or re-export needed before upgrading the two reference entries to decision-grade with body-verified quotes.
- `E6_Sequencing_Platform` has no primary entry yet (WES/WGS/SNP-array comparability is referenced inside the E1/E4 entries).

## Agent Entry Points

> Quick-start pointers for the owning expert: "for question X, start at section Y / entry Z."

- For data-compatibility questions (WES vs WGS vs panel): start at `kim_2020_hrd_wes` and `sztupinszki_2018_scarhrd` (HRD scar comparability) and `kim_2025_wgs_breast_landscape` (WGS pipeline).
- For "how is this signal computed?": start at `E1` (`sztupinszki_2018_scarhrd`, `kim_2020_hrd_wes`).
- Bridge: this is the most upstream corpus — its methods feed `A_Genomic_Signal` (A1 HRD via `telli_2016_hrd_score`/`davies_2017_hrdetect`; A4 drivers).
