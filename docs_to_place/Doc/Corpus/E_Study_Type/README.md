# Corpus — `E_Study_Type`

## Purpose

This corpus tells the system **what kind of evidence and sequencing data** each source provides (method/algorithm, ML model, clinical trial, genomic cohort/landscape, review, sequencing platform). It is the **most upstream** axis: methods and algorithms define *how* each genomic signal is computed, so without E's tooling the features in `A_Genomic_Signal` cannot be extracted from raw sequence. It supports **AQ-1** and **AQ-3** by establishing data/method compatibility (e.g., WES vs WGS vs SNP-array) for any candidate gene.

## Scope

- **In scope**: computational methods and bioinformatics algorithms, predictive ML models, clinical-trial designs, genomic cohort/landscape studies, reviews, and sequencing platforms/assays — characterized by *evidence type and data provenance* rather than by biological content.
- **Out of scope**: the biological meaning of the signal a method computes (route to `A_Genomic_Signal`), the drug context (route to `B_Therapeutic_Context`), subtype (route to `C_Cancer_Subtype`), and the endpoint (route to `D_Clinical_Endpoint`).

## Reasoning interface

Agents reason through `CROSS_REFERENCE_INDEX.md` first, then the enriched layer, then cross-corpus bridges. Do not reason from raw documents when indexed markdown exists.

## Corpus Categories

| Category | Count |
|----------|-------|
| `E1_Computational_Method_Bioinformatics` | 2 |
| `E2_Predictive_ML_Model` | 0 |
| `E3_Clinical_Trial` | 0 |
| `E4_Genomic_Cohort_Landscape` | 1 |
| `E5_Review` | 0 |
| `E6_Sequencing_Platform` | 0 |
| **Total** | **3** |

## Full Registry

> One line per ingested source, organized by category. A source is not fully ingested until it appears here.

### `E1_Computational_Method_Bioinformatics`
- `kim_2020_hrd_wes` — WES-based scarHRD (Sequenza→LOH/TAI/LST) HRD scoring in neoadjuvant breast cancer; WES–OncoScan concordance and pCR/near-pCR associations. **OCR of local PDF pending; body via external bibliographic record.** [reference]
- `sztupinszki_2018_scarhrd` — scarHRD R package migrating SNP-array LOH/TAI/LST genomic scars to NGS/WES allele-specific copy-number profiles; TCGA TNBC cross-platform validation. **OCR pending.** [reference]

### `E2_Predictive_ML_Model`
- _(none yet)_

### `E3_Clinical_Trial`
- _(none yet)_

### `E4_Genomic_Cohort_Landscape`
- `kim_2025_wgs_breast_landscape` — CUBRICS WGS cohort (N=1,364): 41 IntOGen drivers, SNV/indel/SV signatures, HRD/TMB/MATH biomarkers, and a neoadjuvant TCHP HER2+ pCR substudy (n=75). **Body grounded on publisher HTML; OCR of local PDF pending.** [decision]

### `E5_Review`
- _(none yet)_

### `E6_Sequencing_Platform`
- _(none yet)_

## Adding sources

See `Doc/Corpus/HOW_TO_ADD_PAPERS.md` and `Doc/Corpus/PAPER_TEMPLATE_GENERAL.md`.

## Owner

Expert agent: `.cursor/Agents/expert_study_type.md`
