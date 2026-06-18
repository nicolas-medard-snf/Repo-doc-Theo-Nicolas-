# Corpus — `D_Clinical_Endpoint`

## Purpose

This corpus is the **relevance filter**: it prioritizes genes tied directly to **pCR** over softer outcomes (survival, resistance). It is the downstream sink where a genomic signal — in its treatment and subtype context — is validated against an endpoint. It primarily engages **AQ-3** (confident high-priority drivers vs background noise) by weighting evidence according to how directly it connects to pCR.

## Scope

- **In scope**: endpoint definitions and the evidence linking biomarkers to them — pathological complete response (the project target), survival metrics (OS/EFS/DFS) as supporting context, and resistance/relapse/clonal-evolution as mechanistic context.
- **Out of scope**: the signal biology (route to `A_Genomic_Signal`), the drug (route to `B_Therapeutic_Context`), the subtype (route to `C_Cancer_Subtype`), and the assay/method (route to `E_Study_Type`). Per `project_overview.md`, non-pCR endpoints are supporting context only and never the prediction goal.

## Reasoning interface

Agents reason through `CROSS_REFERENCE_INDEX.md` first, then the enriched layer, then cross-corpus bridges. Do not reason from raw documents when indexed markdown exists.

## Corpus Categories

| Category | Count |
|----------|-------|
| `D1_pCR` | 0 |
| `D2_Survival_OS_EFS_DFS` | 0 |
| `D3_Resistance_Relapse_Clonal_Evolution` | 2 |
| **Total** | **2** |

## Full Registry

> One line per ingested source, organized by category. A source is not fully ingested until it appears here.

### `D1_pCR`
- _(none yet)_

### `D2_Survival_OS_EFS_DFS`
- _(none yet)_

### `D3_Resistance_Relapse_Clonal_Evolution`
- `caswelljin_2019_clonal_replacement` — Multi-region WES + spatial/branching models disentangle intra-tumor heterogeneity from clonal replacement after neoadjuvant HER2 therapy in non-pCR tumors (2/5 replacement; tHFR statistic; large pre-existing resistant subclones). [decision]
- `powles_2020_swog_s0800_genome` — SWOG S0800 paired pre/post WES: COSMIC signature 3 (HRD) higher in pCR (median 24% vs 0%, p=0.007); E2F/G2M VAF enrichment in residual disease after neoadjuvant chemo (n=29 pre, n=9 paired). **Body grounded on DOI-matched text; OCR of local PDF pending.** [decision]

## Adding sources

See `Doc/Corpus/HOW_TO_ADD_PAPERS.md` and `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

## Owner

Expert agent: `.cursor/Agents/expert_clinical_endpoint.md`
