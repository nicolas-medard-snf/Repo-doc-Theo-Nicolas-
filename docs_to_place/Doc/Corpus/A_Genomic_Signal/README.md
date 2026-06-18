# Corpus — `A_Genomic_Signal`

## Purpose

This corpus defines the **biological feature class** (HRD, TMB, immune microenvironment, drivers/CNV/SV, chromatin/epigenetics, integrated multi-omic signatures) that each candidate gene belongs to. It is the *what to look for* axis: it produces the gene/feature-level substrate the rest of the pipeline filters and validates. It primarily engages **AQ-1** (which WES mutational drivers correlate with pCR) and **AQ-3** (which genes are high-priority drivers vs background noise).

## Scope

- **In scope**: definitions, mechanisms, and gene/feature catalogs for DNA-repair deficiency, mutational signatures, mutational burden, immune infiltration signals, somatic drivers, copy-number and structural variants, chromatin-remodeling/epigenetic regulators, and integrated multi-omic/transcriptomic signatures — insofar as they are derivable from sequence data.
- **Out of scope**: drug–biomarker matching (route to `B_Therapeutic_Context`), subtype-specific applicability (route to `C_Cancer_Subtype`), endpoint validation (route to `D_Clinical_Endpoint`), and how a signal is computed as a method/tool (route to `E_Study_Type`). Non-DNA-derivable standalone signals (pure proteomics/metabolomics/imaging) are out of scope per `project_overview.md`.

## Reasoning interface

Agents reason through `CROSS_REFERENCE_INDEX.md` first, then the enriched layer, then cross-corpus bridges. Do not reason from raw documents when indexed markdown exists.

## Corpus Categories

| Category | Count |
|----------|-------|
| `A1_HRD_Mutational_Signatures_DNA_Repair` | 2 |
| `A2_Tumor_Mutational_Burden` | 1 |
| `A3_Immune_Microenvironment` | 1 |
| `A4_Genomic_Landscape_Drivers_CNV_SV` | 0 |
| `A5_Chromatin_Remodeling_Epigenetics` | 1 |
| `A6_Integrated_Multiomic_Transcriptomic` | 1 |
| **Total** | **6** |

## Full Registry

> One line per ingested source, organized by category. A source is not fully ingested until it appears here.

### `A1_HRD_Mutational_Signatures_DNA_Repair`
- `davies_2017_hrdetect` — Lasso logistic-regression HRDetect classifier integrating six WGS mutational-signature/HRD features (AUC 0.98) to detect biallelic BRCA1/BRCA2 deficiency and broader BRCAness. [decision]
- `telli_2016_hrd_score` — Combined HRD score (LOH+TAI+LST, ≥42) and HR deficiency predict pCR/RCB 0/I to neoadjuvant platinum in TNBC, including BRCA1/2 wild-type tumors. [decision]

### `A2_Tumor_Mutational_Burden`
- `tmb_immune_infiltration` — TMB × immune-infiltration biomarker axis (A2/A3 bridge). **Image-only PDF — OCR required before evidence use.** [reference]

### `A3_Immune_Microenvironment`
- `integrated_genomic_immune_tme` — Integrated tumor genomics + immune microenvironment. **Scanned image PDF — authors/year/results pending OCR.** [reference]

### `A4_Genomic_Landscape_Drivers_CNV_SV`
- _(none yet)_

### `A5_Chromatin_Remodeling_Epigenetics`
- `giovani_2025_chromatin_remodeling` — 2025 review cataloging SWI/SNF, ISWI, CHD/NuRD, and INO80 remodeler subunits with tumor-suppressive vs oncogenic roles; AQ-3 gene-class background. [reference]

### `A6_Integrated_Multiomic_Transcriptomic`
- `sammut_2022_multiomic_ml` — TransNEO prospective multi-omic (WES/sWGS/RNA/digital pathology) ensemble ML pCR predictor; external validation n=75 AUC 0.87; WES tier AUC 0.80. **Hub.** [decision]

## Adding sources

See `Doc/Corpus/HOW_TO_ADD_PAPERS.md` and `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

## Owner

Expert agent: `.cursor/Agents/expert_genomic_signal.md`
