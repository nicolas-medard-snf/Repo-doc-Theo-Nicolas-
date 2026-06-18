# Corpus — `B_Therapeutic_Context`

## Purpose

A gene rarely predicts response in the absolute — it predicts response **for a specific drug**. This corpus matches genomic biomarkers to the treatment whose response they predict (neoadjuvant chemotherapy, anti-HER2, immunotherapy, PARP/platinum). It primarily engages **AQ-2** (how biomarkers differentiate response to chemotherapy vs targeted/immunotherapy) and supports **AQ-1**/**AQ-3** by constraining a gene's predictive claim to its drug context.

## Scope

- **In scope**: drug classes and regimens used in neoadjuvant breast cancer, their mechanisms of action, and the biomarker–therapy associations that make a genomic signal predictive of response to that therapy.
- **Out of scope**: the biology/definition of the signal itself (route to `A_Genomic_Signal`), subtype eligibility for a regimen (route to `C_Cancer_Subtype`), the response endpoint definition (route to `D_Clinical_Endpoint`), and assay/method details (route to `E_Study_Type`). Endocrine-only, radiotherapy, surgery technique and supportive care are out of scope per `project_overview.md`.

## Reasoning interface

Agents reason through `CROSS_REFERENCE_INDEX.md` first, then the enriched layer, then cross-corpus bridges. Do not reason from raw documents when indexed markdown exists.

## Corpus Categories

| Category | Count |
|----------|-------|
| `B1_Neoadjuvant_Chemotherapy` | 0 |
| `B2_HER2_Targeted_Therapy` | 0 |
| `B3_Immunotherapy_Checkpoint` | 1 |
| `B4_PARP_Platinum_DNA_Damaging` | 0 |
| **Total** | **1** |

## Full Registry

> One line per ingested source, organized by category. A source is not fully ingested until it appears here.

### `B1_Neoadjuvant_Chemotherapy`
- _(none yet)_

### `B2_HER2_Targeted_Therapy`
- _(none yet)_

### `B3_Immunotherapy_Checkpoint`
- `schmid_2024_keynote522_os` — KEYNOTE-522 final OS (N=1174): neoadjuvant/adjuvant pembrolizumab + chemo vs chemo in early TNBC; pCR +13.6 pp, 5-y EFS 81.2% vs 72.2% (HR 0.65), 5-y OS 86.6% vs 81.7% (P=0.002). Regimen/endpoint anchor, not a WES biomarker study. [decision]

### `B4_PARP_Platinum_DNA_Damaging`
- _(none yet)_

## Adding sources

See `Doc/Corpus/HOW_TO_ADD_PAPERS.md` and `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

## Owner

Expert agent: `.cursor/Agents/expert_therapeutic_context.md`
