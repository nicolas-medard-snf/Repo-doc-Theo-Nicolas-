# Cross-Reference Index — `A_Genomic_Signal`

> This index is the **primary reasoning interface** of the corpus. Agents start here for every substantive task. Keep it navigable: it is a map, not a dump.

## Concepts → Entries

| Concept | Entries (`paper_id`) |
|---------|----------------------|
| HRD / homologous recombination deficiency | `davies_2017_hrdetect`, `telli_2016_hrd_score`, `sammut_2022_multiomic_ml` |
| Mutational signatures (SBS / indel / rearrangement) | `davies_2017_hrdetect` |
| Tumor mutational burden (TMB) | `tmb_immune_infiltration` (OCR pending), `sammut_2022_multiomic_ml` |
| Immune infiltration / TILs / T-cell signatures | `integrated_genomic_immune_tme` (OCR pending), `tmb_immune_infiltration` (OCR pending), `sammut_2022_multiomic_ml` |
| Somatic drivers / CNV / structural variants | `sammut_2022_multiomic_ml`, `integrated_genomic_immune_tme` (OCR pending) |
| Chromatin remodeling / epigenetic regulators | `giovani_2025_chromatin_remodeling` |
| Integrated multi-omic / transcriptomic signature | `sammut_2022_multiomic_ml` |

## Methods / Mechanisms / Schools of Thought → Entries

| Method / mechanism | Entries |
|--------------------|---------|
| HRDetect (lasso logistic regression on mutational-signature exposures) | `davies_2017_hrdetect` |
| Combined HRD score (LOH + TAI + LST; threshold ≥42) | `telli_2016_hrd_score` |
| HR deficiency = HRD ≥42 OR tBRCA1/2 mutation | `telli_2016_hrd_score` |
| scarHRD on WES | `sammut_2022_multiomic_ml` |
| Ensemble ML (elastic-net LR + SVM + RF) for pCR | `sammut_2022_multiomic_ml` |
| Multi-omic feature integration (6-tier schema) | `sammut_2022_multiomic_ml` |
| TIDE T-cell dysfunction / exclusion scoring | `sammut_2022_multiomic_ml` |
| ATP-dependent chromatin remodeling (SWI/SNF, ISWI, CHD, INO80) | `giovani_2025_chromatin_remodeling` |
| Synthetic lethality (ARID1A↔ARID1B; ARID1A→PARP/ATR; BRG1-deficient→SMARCA2) | `giovani_2025_chromatin_remodeling` |

## Open Questions / Problems → Entries

| Open question | Entries that engage it |
|---------------|------------------------|
| AQ-1 — which WES mutational drivers correlate with pCR? | `davies_2017_hrdetect`, `telli_2016_hrd_score`, `sammut_2022_multiomic_ml` |
| AQ-2 — chemo vs targeted/immuno differentiation | `sammut_2022_multiomic_ml` |
| AQ-3 — which genes are high-priority drivers vs background noise? | `davies_2017_hrdetect`, `telli_2016_hrd_score`, `sammut_2022_multiomic_ml`, `giovani_2025_chromatin_remodeling` |

## Contradictions / Tensions

| Tension | Entries in tension | How to interpret |
|---------|--------------------|------------------|
| SWI/SNF complex labeled tumor-suppressor vs oncogenic BRG1/BRM ATPases | `giovani_2025_chromatin_remodeling` | Resolve at subunit + subtype level before AQ-3 ranking; do not collapse to "SWI/SNF = LOF driver". |
| HRD scar-sum (LOH+TAI+LST ≥42) vs HRDetect mutational-signature classifier | `telli_2016_hrd_score` vs `davies_2017_hrdetect` | Two different operationalizations of the same HRD signal; reconcile feature choice when extracting HRD from project WES. |

## Hub Entries

> Entries that connect many others. Read these first when entering the corpus cold.

- `sammut_2022_multiomic_ml` — central pCR-prediction hub; integrates HRD, TMB, immune, drivers; read first for A6 and AQ-1/2/3.
- `davies_2017_hrdetect` — defines the operative HRD composite signal and WES/WGS trade-offs.
- `telli_2016_hrd_score` — anchors the HRD-scar threshold and its link to neoadjuvant platinum pCR.

## Unexplored Combinations

- HRDetect score × neoadjuvant pCR in TNBC/HER2+ WES cohorts (not validated at scale yet).
- WES-only reimplementation of the Sammut DNA tier (8 features) without RNA/digital pathology — project-scoped benchmark vs AUC 0.80.
- TMB (A2) + immune infiltration (A3) joint stratification for neoadjuvant pCR (pending OCR of the two image-only sources).

## Gaps (curation priorities)

- Priority axis to grow first (per `project_overview.md` §6): `A1_HRD_Mutational_Signatures_DNA_Repair` and `A3_Immune_Microenvironment` — most established treatment-linked pCR biomarkers.
- **OCR backlog**: `tmb_immune_infiltration` (A2) and `integrated_genomic_immune_tme` (A3) are image-only PDFs ingested as reference stubs — OCR required before promotion to decision.
- `A4_Genomic_Landscape_Drivers_CNV_SV` is still empty; driver/CNV catalog lives cross-corpus in `E4` (`kim_2025_wgs_breast_landscape`) — consider a primary A4 entry.

## Agent Entry Points

> Quick-start pointers for the owning expert: "for question X, start at section Y / entry Z."

- For **AQ-1** (drivers correlated with pCR): start at the HRD concept row (`davies_2017_hrdetect`, `telli_2016_hrd_score`) and the hub `sammut_2022_multiomic_ml`.
- For **AQ-3** (driver vs noise prioritization): start at Hub Entries, then `A6` integrated signatures and the `A5` chromatin gene catalog.
- Upstream dependency: methods that compute these signals live in `E_Study_Type` (`kim_2020_hrd_wes`, `sztupinszki_2018_scarhrd`, `kim_2025_wgs_breast_landscape`); downstream drug mapping in `B_Therapeutic_Context` (`schmid_2024_keynote522_os`).
