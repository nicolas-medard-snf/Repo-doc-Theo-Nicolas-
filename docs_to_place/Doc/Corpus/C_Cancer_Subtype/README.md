# Corpus — `C_Cancer_Subtype`

## Purpose

Predictive value is **subtype-dependent**: a biomarker validated in TNBC must not be misapplied to HR+/HER2+ data. This corpus captures the molecular subtype context (TNBC, HER2+, HR+/ER+, pan-breast) that conditions which genomic signal is relevant and which treatment regimen applies. It supports **AQ-1** and **AQ-2** by scoping every biomarker claim to the subtype(s) in which it holds.

## Scope

- **In scope**: definitions and molecular characteristics of breast cancer subtypes, subtype-specific biology relevant to neoadjuvant response, and subtype eligibility/stratification for the project's treatments. The project core is **TNBC** and **HER2+** (per `project_overview.md` §1).
- **Out of scope**: the signal biology itself (route to `A_Genomic_Signal`), drug mechanism (route to `B_Therapeutic_Context`), endpoint definitions (route to `D_Clinical_Endpoint`), assay details (route to `E_Study_Type`), and any non-breast cancer type.

## Reasoning interface

Agents reason through `CROSS_REFERENCE_INDEX.md` first, then the enriched layer, then cross-corpus bridges. Do not reason from raw documents when indexed markdown exists.

## Corpus Categories

| Category | Count |
|----------|-------|
| `C1_TNBC` | 0 |
| `C2_HER2_Positive` | 0 |
| `C3_HR_ER_Positive` | 0 |
| `C4_Pan_Breast_Unspecified` | 0 |
| **Total** | **0** |

## Full Registry

> One line per ingested source, organized by category. A source is not fully ingested until it appears here.

### `C1_TNBC`
- _(none yet)_

### `C2_HER2_Positive`
- _(none yet)_

### `C3_HR_ER_Positive`
- _(none yet)_

### `C4_Pan_Breast_Unspecified`
- _(none yet)_

## Adding sources

See `Doc/Corpus/HOW_TO_ADD_PAPERS.md` and `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

## Owner

Expert agent: `.cursor/Agents/expert_cancer_subtype.md`
