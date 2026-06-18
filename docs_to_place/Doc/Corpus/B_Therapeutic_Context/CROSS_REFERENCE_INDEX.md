# Cross-Reference Index — `B_Therapeutic_Context`

> This index is the **primary reasoning interface** of the corpus. Agents start here for every substantive task. Keep it navigable: it is a map, not a dump.

## Concepts → Entries

| Concept | Entries (`paper_id`) |
|---------|----------------------|
| Neoadjuvant chemotherapy (taxane/anthracycline) | `schmid_2024_keynote522_os` (chemo backbone) |
| HER2-targeted therapy (trastuzumab/pertuzumab/T-DM1) | _(none yet)_ |
| Immune checkpoint inhibition (anti-PD-1/PD-L1) | `schmid_2024_keynote522_os` |
| PARP inhibition / platinum (DNA-damaging) | `schmid_2024_keynote522_os` (carboplatin component) |
| Biomarker–therapy association | `schmid_2024_keynote522_os` (treatment anchor; genomic biomarkers pending) |

## Methods / Mechanisms / Schools of Thought → Entries

| Method / mechanism | Entries |
|--------------------|---------|
| Neoadjuvant pembrolizumab + platinum-taxane-anthracycline (KEYNOTE-522 regimen) | `schmid_2024_keynote522_os` |

## Open Questions / Problems → Entries

| Open question | Entries that engage it |
|---------------|------------------------|
| AQ-2 — how do biomarkers differentiate chemo vs targeted/immunotherapy response? | `schmid_2024_keynote522_os` |

## Contradictions / Tensions

| Tension | Entries in tension | How to interpret |
|---------|--------------------|------------------|
| _(none yet)_ | _(none yet)_ | _(none yet)_ |

## Hub Entries

> Entries that connect many others. Read these first when entering the corpus cold.

- `schmid_2024_keynote522_os` — B3 hub for early-stage TNBC pembrolizumab context (regimen + endpoint evidence).

## Unexplored Combinations

- PD-L1 CPS / TMB / immune-signature stratification of the KEYNOTE-522 regimen (genomic predictor of who benefits) — bridges to `A2`/`A3`.

## Gaps (curation priorities)

- No `B2_HER2_Targeted_Therapy` or `B4_PARP_Platinum` primary entry yet; anti-HER2 evidence currently lives cross-corpus in `D3` (`caswelljin_2019_clonal_replacement`) and HRD→platinum logic in `A1` (`telli_2016_hrd_score`).
- KEYNOTE-522 biomarker/WES companion analyses not yet ingested.

## Agent Entry Points

> Quick-start pointers for the owning expert: "for question X, start at section Y / entry Z."

- For **AQ-2** (drug-specific biomarker response): start at `B3` (`schmid_2024_keynote522_os`) for the immunotherapy regimen and endpoint deltas.
- Upstream dependency: the signal being matched comes from `A_Genomic_Signal`; subtype eligibility is gated by `C_Cancer_Subtype` (TNBC); validation lands in `D_Clinical_Endpoint` (pCR + OS/EFS); trial design detail in `E_Study_Type` (E3).
