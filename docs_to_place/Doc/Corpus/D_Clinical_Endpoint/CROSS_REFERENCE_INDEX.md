# Cross-Reference Index — `D_Clinical_Endpoint`

> This index is the **primary reasoning interface** of the corpus. Agents start here for every substantive task. Keep it navigable: it is a map, not a dump.

## Concepts → Entries

| Concept | Entries (`paper_id`) |
|---------|----------------------|
| Pathological complete response (pCR) | `powles_2020_swog_s0800_genome` (signature-3 arm, supporting) |
| Survival (OS / EFS / DFS) | _(none yet — see `schmid_2024_keynote522_os` in B3)_ |
| Resistance / relapse / clonal evolution | `caswelljin_2019_clonal_replacement`, `powles_2020_swog_s0800_genome` |
| Treatment-induced genomic change | `powles_2020_swog_s0800_genome` |
| Intra-tumor heterogeneity (ITH) | `caswelljin_2019_clonal_replacement` |

## Methods / Mechanisms / Schools of Thought → Entries

| Method / mechanism | Entries |
|--------------------|---------|
| tHFR / HFR (temporal & spatial heterogeneity statistics) | `caswelljin_2019_clonal_replacement` |
| Multi-region WES (pre-biopsy + post-surgical) | `caswelljin_2019_clonal_replacement` |
| Spatial agent-based tumor growth + ABC inference | `caswelljin_2019_clonal_replacement` |
| VAF percentile-delta / treatment selection | `powles_2020_swog_s0800_genome` |
| COSMIC signature 3 / HRD chemosensitivity | `powles_2020_swog_s0800_genome` |
| MSigDB pathway mutation-frequency aggregation | `powles_2020_swog_s0800_genome` |

## Open Questions / Problems → Entries

| Open question | Entries that engage it |
|---------------|------------------------|
| AQ-2 — chemo vs targeted/immuno genomic differentiation | `caswelljin_2019_clonal_replacement`, `powles_2020_swog_s0800_genome` |
| AQ-3 — high-priority drivers vs background noise (by endpoint proximity) | `caswelljin_2019_clonal_replacement`, `powles_2020_swog_s0800_genome` |

## Contradictions / Tensions

| Tension | Entries in tension | How to interpret |
|---------|--------------------|------------------|
| _(none yet)_ | _(none yet)_ | _(none yet)_ |

## Hub Entries

> Entries that connect many others. Read these first when entering the corpus cold.

- `powles_2020_swog_s0800_genome` — paired-tissue trial WES linking signature-3/HRD to pCR and clone selection in residual disease.
- `caswelljin_2019_clonal_replacement` — ITH-vs-evolution disambiguation for HER2+ neoadjuvant non-pCR.

## Unexplored Combinations

- Signature-3/HRD as a pCR predictor (`powles_2020`) cross-checked against the A1 HRD entries (`telli_2016_hrd_score`, `davies_2017_hrdetect`).
- Pre-treatment resistant-subclone burden (`caswelljin_2019`) as a modifier of WES-driver-based pCR prediction.

## Gaps (curation priorities)

- `D1_pCR` is the project target; both current entries are `D3` (resistance/evolution) and only touch pCR as supporting context. **No primary `D1_pCR` entry yet** — the strongest direct pCR evidence currently lives cross-corpus (`sammut_2022_multiomic_ml` in A6, `schmid_2024_keynote522_os` in B3).
- No `D2_Survival` primary entry; OS/EFS evidence is in `schmid_2024_keynote522_os` (B3).

## Agent Entry Points

> Quick-start pointers for the owning expert: "for question X, start at section Y / entry Z."

- For **AQ-3** (driver vs noise): start at `D3` (`powles_2020_swog_s0800_genome`, `caswelljin_2019_clonal_replacement`) for how resistance/evolution reshapes driver interpretation; for direct pCR signal cross-reference `sammut_2022_multiomic_ml` (A6).
- Bridge: this corpus consumes signals from `A`, conditioned by `B` (`schmid_2024_keynote522_os`) and `C`; validated outcomes feed back to re-rank `A_Genomic_Signal`.
