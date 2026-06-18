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
| `A1_HRD_Mutational_Signatures_DNA_Repair` | 0 |
| `A2_Tumor_Mutational_Burden` | 0 |
| `A3_Immune_Microenvironment` | 0 |
| `A4_Genomic_Landscape_Drivers_CNV_SV` | 0 |
| `A5_Chromatin_Remodeling_Epigenetics` | 0 |
| `A6_Integrated_Multiomic_Transcriptomic` | 0 |
| **Total** | **0** |

## Full Registry

> One line per ingested source, organized by category. A source is not fully ingested until it appears here.

### `A1_HRD_Mutational_Signatures_DNA_Repair`
- _(none yet)_

### `A2_Tumor_Mutational_Burden`
- _(none yet)_

### `A3_Immune_Microenvironment`
- _(none yet)_

### `A4_Genomic_Landscape_Drivers_CNV_SV`
- _(none yet)_

### `A5_Chromatin_Remodeling_Epigenetics`
- _(none yet)_

### `A6_Integrated_Multiomic_Transcriptomic`
- _(none yet)_

## Adding sources

See `Doc/Corpus/HOW_TO_ADD_PAPERS.md` and `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

## Owner

Expert agent: `.cursor/Agents/expert_genomic_signal.md`
