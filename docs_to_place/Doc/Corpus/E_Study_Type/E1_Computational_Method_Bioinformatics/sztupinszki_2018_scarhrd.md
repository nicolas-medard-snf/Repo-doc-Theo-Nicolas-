# Migrating the SNP array-based homologous recombination deficiency measures to next generation sequencing data of breast cancer

## Metadata

```yaml
---
paper_id: "sztupinszki_2018_scarhrd"
title: "Migrating the SNP array-based homologous recombination deficiency measures to next generation sequencing data of breast cancer"
authors: "Zsofia Sztupinszki, Miklos Diossy, Marcin Krzystanek, Lilla Reiniger, István Csabai, Francesco Favero, Nicolai J. Birkbak, Aron C. Eklund, Ali Syed, Zoltan Szallasi"
year: 2018
venue: "npj Breast Cancer"
paper_type: "methodological"
domain: "E_Study_Type"
subdomain: "HRD measure migration SNP-array → NGS"
relevance_score: 5
priority_level: "CRITICAL"
corpus_role: "reference"
temporal_status: "active_candidate"
relevance_tags:
  - "scarHRD"
  - "HRD"
  - "LOH"
  - "TAI"
  - "LST"
  - "NtAI"
  - "SNP_array"
  - "WES"
  - "WXS"
  - "WGS"
  - "NGS"
  - "Sequenza"
  - "allele_specific_copy_number"
  - "TCGA"
  - "TNBC"
  - "BRCA1"
  - "BRCA2"
  - "platform_migration"
  - "genomic_scar"
doi: "10.1038/s41523-018-0066-6"
isbn: ""
url: "https://doi.org/10.1038/s41523-018-0066-6"
pdf_file: "sztupinszki_2018_scarhrd.pdf"
---
```

---

## One-Sentence Summary

Sztupinszki et al. (2018) introduce **scarHRD**, an R package that re-implements SNP-array genomic scar HRD metrics (LOH, telomeric allelic imbalance/TAI, LST) from NGS allele-specific copy-number profiles — the upstream computational bridge needed to compute HRD-sum on WES/WGS breast cancer data when SNP arrays are unavailable.

---

## Key Contributions

- Publishes the **scarHRD R package** (`https://github.com/sztup/scarHRD`) to derive HRD-LOH, HRD-TAI (NtAI), and HRD-LST from NGS data rather than Affymetrix SNP 6.0 arrays.
- Defines a **platform-migration workflow**: NGS BAMs → allele-specific segmentation (notably Sequenza-compatible inputs) → scar scar-score computation → optional HRD-sum (unweighted LOH + TAI + LST).
- Validates cross-platform comparability in **TCGA breast cancer** samples with both SNP-array and NGS profiling, focusing on **triple-negative breast cancer (TNBC)** and **BRCA1/2 deficiency** discrimination.
- Positions NGS-derived scar scores as a **drop-in replacement** for the SNP-array scar step in composite HRD frameworks (including HRDetect), preserving the same three-metric genomic-scar vocabulary established by Abkevich (LOH), Birkbak (TAI), and Popova (LST).

---

## Core Idea / Mechanism / Argument

### Problem framing

Genomic scar-based HRD quantification was originally developed on **SNP arrays**. As clinical and research pipelines shift to **NGS (WES/WGS)**, methods must reproduce the same LOH/TAI/LST scar definitions from sequencing-derived copy-number profiles or HRD features computed on WES cannot be compared to the SNP-array literature (e.g., Telli 2016 HRD-score thresholding, Davies 2017 HRDetect scar integration).

### Mechanism (conceptual — not verified against local PDF)

1. **Input**: Allele-specific copy-number segmentation from paired tumor–normal NGS (Sequenza `.seqz` or equivalent six-column segmentation: total CN, A-allele CN, B-allele CN per segment).
2. **HRD-LOH**: Count genome-wide LOH regions exceeding a minimum length threshold (SNP-array literature uses ~15 Mb; this paper evaluates NGS-appropriate cutoffs — details pending OCR).
3. **HRD-TAI (NtAI)**: Count telomeric allelic imbalances — AI events extending to the telomeric end of a chromosome.
4. **HRD-LST**: Count large-scale transitions — chromosomal breaks between adjacent ≥10 Mb regions with inter-segment distance ≤3 Mb (Popova definition lineage).
5. **HRD-sum**: Unweighted numeric sum LOH + TAI + LST, aligned with combined HRD score usage in Telli et al. and scar integration in HRDetect.
6. **Output**: Per-sample scar counts usable for BRCA1/2 status stratification and downstream composite HRD models.

### Claimed vs demonstrated (pending full-text verification)

**Claimed (from title, abstract-level publisher metadata, and package documentation — not body-verified in local PDF):** NGS-based scarHRD scores correlate well with SNP-array scores; NGS HRD-sum distinguishes BRCA1/2-deficient from intact TNBC similarly to array-based scores; scarHRD enables WES/WGS pipelines to replace SNP-array scar computation.

**Demonstrated in local corpus:** *Not yet verified* — local PDF text layer is not extractable; this entry is **reference-grade only** until OCR/full-text re-ingestion.

### Novel vs inherited

| Inherited | Novel in this paper |
|-----------|---------------------|
| LOH, TAI, LST definitions (Abkevich 2012; Birkbak 2012; Popova 2012) | **scarHRD** implementation for NGS inputs |
| Combined HRD-sum concept (Telli 2016; Marquard 2015 pan-cancer scars) | Cross-platform SNP 6.0 vs WES validation in TCGA breast/TNBC |
| Sequenza allele-specific CN from NGS (Favero 2015) | R package workflow bridging Sequenza output → scar scores |
| HRDetect scar integration (Davies 2017) | Explicit argument that NGS scars can replace SNP-array step in advanced HRD models |

---

## Methodology / Evidence Base

### If methodological / applied / "how-to"

- **What the method does**: Computes three genomic scar HRD metrics and their sum from NGS-derived allele-specific copy-number profiles, mirroring SNP-array scar algorithms.
- **What it requires (inputs, skills, time)**:
  - Paired tumor–normal WES or WGS with sufficient coverage for reliable segmentation.
  - Allele-specific copy-number estimation (Sequenza or compatible segmentation format).
  - R environment; scarHRD package from GitHub.
  - Reference genome (GRCh37/GRCh38 supported per package docs).
- **Where used in practice**: TCGA breast cancer cross-platform benchmark; cited as the standard NGS migration tool for scar-based HRD in subsequent HRD/HRDetect pipelines and diagnostic landscape reviews.

### Empirical validation (high-level — pending OCR)

- **Design**: Cross-platform comparison (Affymetrix SNP 6.0 vs WES) within TCGA breast samples with both data types.
- **Sample / setting**: TCGA breast cohort; TNBC subset (IHC-defined receptor status); subset with prior published SNP-array HRD estimates (Marquard/Szallasi group).
- **BRCA1/2 status**: Composite definition using deep deletion, co-occurring germline/somatic mutation with LOH, or promoter methylation with LOH (exact rules pending OCR).
- **Measurements**: LOH, TAI, LST, HRD-sum via scarHRD vs array-based scores.
- **Replication**: Single public cohort (TCGA); no independent neoadjuvant pCR validation in this paper.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus**: `E_Study_Type` → `E1_Computational_Method_Bioinformatics`
- **Anchor question(s)**: **AQ-1** (WES-derived genomic features — HRD scars must be computable from exome data before any driver/HRD–pCR association analysis); **AQ-3** (method-grade evidence for prioritizing HRD-related biology vs noise — platform-valid migration reduces false deprioritization of scar-based candidates on WES).
- **Bridge corpora**:
  - `A_Genomic_Signal` / `A1_HRD_Mutational_Signatures_DNA_Repair` — defines how LOH/TAI/LST/HRD-sum are extracted on NGS.
  - `E6_Sequencing_Platform` — SNP-array vs NGS comparability, WES segmentation caveats (LOH sensitivity to segmentation granularity).

### How it could be used

- **Directly reusable**: scarHRD is the operative tool to compute HRD-sum from WES segmentation in the project's TNBC/HER2+ WES pipeline — upstream of any HRD–pCR modeling.
- **Indirectly inspiring**: Cross-platform validation framing for auditing WES HRD calls against array literature thresholds (e.g., HRD ≥42 from Telli 2016).
- **Mainly background / framing**: TCGA TNBC BRCA stratification context; not a neoadjuvant pCR outcome paper.

### Main fit with the project

The project relies on **WES**; scarHRD is the published migration path from SNP-array HRD scars to NGS, directly unblocking HRD feature extraction for AQ-1/AQ-3 without abandoning the established LOH/TAI/LST composite used in platinum-response biomarker literature.

### Main mismatch or risk

- **Endpoint gap**: Validates BRCA1/2 status discrimination and platform correlation, **not neoadjuvant pCR** — pCR predictive value of NGS HRD-sum must come from other sources (e.g., Telli 2016 on SNP-array HRD-score).
- **WES segmentation bias**: Publisher abstract notes WES-based LOH counts can differ from SNP-array LOH (segmentation/coverage effects); ROC for BRCA status may still be comparable — full nuance pending OCR.
- **Coverage dependence**: Down-sampling experiments reported in supplementary material (not verified locally) — WES depth and tumor purity remain failure modes.
- **HER2+ scope**: Primary validation cohort is TNBC-focused within TCGA; generalization to HER2+ neoadjuvant WES cohorts is assumed, not demonstrated here.

### Concrete follow-up

1. **OCR or replace local PDF** with text-extractable version; upgrade to `corpus_role: decision` with body-verified quotes and effect sizes.
2. Wire scarHRD into WES preprocessing spec (Sequenza → scarHRD → HRD-sum) and document minimum coverage/purity thresholds from supplementary figures.
3. Cross-link `telli_2016_hrd_score` (threshold ≥42) and `davies_2017_hrdetect` (scar integration) in `A_Genomic_Signal` index after OCR confirms compatibility claims.
4. Flag WES LOH under-segmentation as a QC check in E6 platform notes.

---

## Assumptions

- Allele-specific copy-number segmentation from NGS (Sequenza or equivalent) is sufficiently accurate to reproduce SNP-array scar calls.
- The LOH/TAI/LST definitions and length thresholds calibrated on SNP arrays transfer to WES/WGS with modest parameter tuning (15 Mb LOH minimum discussed in package/manuscript lineage).
- TCGA TNBC BRCA1/2 labels and paired SNP+WES samples are representative of the segmentation challenges in clinical FFPE WES biopsies.
- HRD-sum on NGS preserves the biological meaning of the combined SNP-array HRD score used in prior biomarker work.

---

## Limitations / Failure Modes

- **OCR REQUIRED — local PDF not text-extractable**: `pdftotext`, `pypdf`, and `pdfplumber` were unavailable or failed on the co-located PDF; all quantitative specifics below are **not body-verified** against the local file. Re-ingest after OCR before using as decision-grade evidence.
- **WES LOH underestimation**: Segmentation granularity on exome data can reduce LOH event counts relative to SNP arrays even when composite HRD-sum/BRCA discrimination remains usable (per publisher abstract — verify in body after OCR).
- **No pCR endpoint**: Platform migration ≠ treatment-response validation; do not infer neoadjuvant pCR AUC from this paper alone.
- **TNBC-centric TCGA subset**: Limited direct evidence for HER2+ neoadjuvant WES cohorts.
- **Dependency chain failure**: Poor Sequenza segmentation (low purity, insufficient off-target coverage on WES) propagates to unreliable scar scores.
- **Threshold portability**: Telli HRD ≥42 threshold was defined on SNP-array training data; applying it to NGS HRD-sum requires independent calibration or cross-platform concordance checks.

---

## Key Quantitative or Qualitative Results

**Not extracted from local PDF — OCR REQUIRED.**

Publisher abstract (DOI landing page only; **not verified against co-located PDF**) reports Pearson correlations between SNP-array and NGS scar metrics roughly in the **0.73–0.87** range (component-dependent), HRD-sum correlation **~0.87**, and BRCA1/2 discrimination AUC **~80.8%** for NGS HRD-sum in TCGA TNBC. **Do not cite these numbers as corpus-grounded until OCR confirms them in the local PDF body.**

Qualitative results expected after OCR: Fig. 1 cross-platform scatter plots; Fig. 2 HRD-sum by BRCA status; supplementary ROC comparisons SNP vs WXS; coverage down-sampling stability (Supplementary Figures S7–S8).

---

## Key Quotes

**No direct body quotes extracted — OCR REQUIRED.**

Do not use block quotes from this entry in agent reasoning until the co-located PDF is OCR'd and 5–10 body quotes are added per `HOW_TO_ADD_PAPERS.md` decision-ingestion standard.

---

## Cross-References

### Complements entries in corpus

- `telli_2016_hrd_score` (A1): Defines combined HRD score (LOH+TAI+LST) and ≥42 threshold on SNP-array assay; scarHRD enables the same composite on NGS.
- `davies_2017_hrdetect` (A1): Integrates HRD scar index among mutational-signature features; NGS scar step can replace SNP-array scar computation per authors' stated aim (verify wording after OCR).

### Contradicts / Tensions

- **WES vs WGS coverage**: Davies 2017 notes WES degrades signature-based HRDetect sensitivity; scarHRD addresses scar metrics specifically but does not resolve full HRDetect WES limitations.
- **LOH count platform gap**: Potential tension between per-component LOH discordance and preserved composite/ROC performance — interpret cautiously until supplementary methods are indexed.

### Cross-corpus connections

- **A_Genomic_Signal / A1**: Downstream consumer of scarHRD outputs (HRD-sum, individual scars) as genomic signal definitions.
- **E6_Sequencing_Platform** (to be populated): SNP-array vs WES comparability, Sequenza prerequisites, minimum coverage — natural home for platform QC derived from this paper's supplementary analyses.

### Related entries to add

- **HIGH**: Marquard 2015 pan-cancer SNP-array HRD scars (TCGA precursor scores referenced by authors).
- **HIGH**: Favero 2015 Sequenza (segmentation dependency).
- **MEDIUM**: Abkevich 2012, Birkbak 2012, Popova 2012 (original scar definitions).
- **MEDIUM**: E6 entry for WES HRD pipeline QC checklist once OCR complete.

---

## Author Notes

### Priority justification

**CRITICAL** for `E_Study_Type` because it is the standard published tool chain for computing SNP-array-equivalent HRD scars on NGS/WES — without it, the project's WES-first HRD features lack a validated extraction method. Held at `reference` corpus_role only until OCR upgrades ingestion fidelity.

### Use this source for

- "How do we compute LOH/TAI/LST/HRD-sum from WES data?"
- "What R package migrates SNP-array HRD scars to NGS?"
- "What segmentation input does scarHRD require (Sequenza format)?"
- "Why might WES HRD scores differ from SNP-array scores?"
- "What upstream method paper supports HRDetect's scar component on NGS?"

### Do NOT use this source for

- Neoadjuvant **pCR prediction** effect sizes → use `telli_2016_hrd_score` or trial biomarker papers.
- **HRDetect probability scores** or mutational-signature HRD → use `davies_2017_hrdetect`.
- Body-verified correlation coefficients or AUC values → **OCR REQUIRED** first.
- HER2+ subtype-specific HRD validation → not the primary cohort; use subtype-appropriate evidence.

### Curation notes

> **⚠ OCR REQUIRED**: Local PDF `sztupinszki_2018_scarhrd.pdf` could not be text-extracted (`pdftotext` not installed; Python/pypdf/pdfplumber unavailable in environment). Entry built from title, domain knowledge, DOI metadata, and GitHub package documentation only. **Upgrade to `decision` after OCR** with body quotes, verified effect sizes, supplementary figure indexing, and explicit Sequenza/scarHRD parameter table.

- Harmonize terminology: **TAI** vs **NtAI** (telomeric allelic imbalance count); **WXS** vs **WES** (authors use "WXS" in abstract).
- Index under E1 methods, E6 platform comparability, and A1 HRD scar computation after OCR.
- Update `CROSS_REFERENCE_INDEX.md` and `README.md` registry (suggested additions returned to orchestrator — not edited in this ingestion pass).

---

## Related Concepts

scarHRD, HRD-sum, genomic scar, LOH, TAI, NtAI, LST, allele-specific copy number, Sequenza, SNP array migration, WES, WGS, NGS, TCGA, TNBC, BRCA1, BRCA2, platform concordance, segmentation, HRDetect scar component, homologous recombination deficiency, cross-platform validation

---

## Quality Checklist

- [x] precise terminology of the discipline is used throughout (where domain-known)
- [x] the source-type contextualization in Author Notes is complete
- [x] assumptions are explicit
- [x] novel contributions are distinguished from inherited components
- [ ] quantitative or qualitative results include body-verified specifics — **blocked: OCR REQUIRED**
- [ ] at least 5 useful direct quotes — **blocked: OCR REQUIRED**
- [x] cross-references are present (including cross-corpus when relevant)
- [x] the project-relevance relationship section is complete
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated — deferred per ingestion constraints
- [ ] the corpus `README.md` registry and counts have been updated — deferred per ingestion constraints
