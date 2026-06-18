# Multi-omic machine learning predictor of breast cancer therapy response

## Metadata

```yaml
---
paper_id: "sammut_2022_multiomic_ml"
title: "Multi-omic machine learning predictor of breast cancer therapy response"
authors: "Stephen-John Sammut, Mireia Crispin-Ortuzar, Suet-Feung Chin, Elena Provenzano, Helen A. Bardwell, Wenxin Ma, Wei Cope, Ali Dariush, Sarah-Jane Dawson, Jean E. Abraham, Janet Dunn, Louise Hiller, Jeremy Thomas, David A. Cameron, John M. S. Bartlett, Larry Hayward, Paul D. Pharoah, Florian Markowetz, Oscar M. Rueda, Helena M. Earl, Carlos Caldas"
year: 2022
venue: "Nature"
paper_type: "primary_research"
domain: "A_Genomic_Signal"
subdomain: "integrated multi-omic / ML predictor of pCR"
relevance_score: 5
priority_level: "CRITICAL"
corpus_role: "decision"
temporal_status: "active_candidate"
relevance_tags:
  - "multi_omic_integration"
  - "machine_learning"
  - "pCR_prediction"
  - "neoadjuvant_therapy"
  - "WES"
  - "RNA_seq"
  - "digital_pathology"
  - "TP53"
  - "PIK3CA"
  - "HRD"
  - "TMB"
  - "HLA_LOH"
  - "immune_microenvironment"
  - "TIDE"
  - "ensemble_classifier"
  - "TransNEO"
  - "RCB"
doi: "10.1038/s41586-021-04278-5"
isbn: ""
url: "https://doi.org/10.1038/s41586-021-04278-5"
pdf_file: "sammut_2022_multiomic_ml.pdf"
---
```

---

## One-Sentence Summary

Sammut et al. (2022) prospectively profile pre-treatment breast tumours with WES, shallow WGS, RNA-seq, and digital pathology in 168 TransNEO patients, integrate 34 baseline ecosystem features via an ensemble ML pipeline, and externally validate pCR prediction in 75 independent cases with AUC 0.87 — establishing the central multi-omic benchmark for which WES-derived drivers (TP53, PIK3CA, HRD, TMB, HLA LOH) and immune/transcriptomic signals jointly stratify neoadjuvant response across TNBC and HER2+ subtypes.

---

## Key Contributions

- Prospective **TransNEO** cohort (168 multi-omic pre-treatment biopsies; 147 ML training cases) with chemotherapy ± anti-HER2 and RCB-graded surgical endpoints, spanning ER+/HER2−, HER2+, and TNBC subtypes.
- Systematic univariate mapping of **clinical, genomic (WES/sWGS), transcriptomic, and digital pathology** features to pCR/residual disease, showing monotonic RCB associations for TMB, HRD score, chromosomal instability, proliferation (GGI), and immune activation (STAT1, cytolytic activity, lymphocyte density).
- Six-tier **ensemble ML predictor** (elastic-net logistic regression + SVM + random forest, unweighted average) with progressive data integration; **external validation AUC 0.87** for the fully integrated model (clinical + DNA + RNA + digital pathology + treatment) on n=75 independent patients (ARTemis control arm + PBCP).
- Gene-level prioritization evidence for **AQ-3**: TP53 mutations enrich pCR (OR 2.9); PIK3CA mutations enrich residual disease (OR 2.1); HLA class I LOH enriches resistance (OR 3.5); proliferation–immune co-enrichment defines a responsive phenotype while T cell dysfunction/exclusion marks resistant tumours despite high proliferation.
- Demonstrates that **no single omic layer** predicts robustly alone, but RNA features dominate the integrated model while DNA features (TMB, HRD, TP53/PIK3CA, neoantigens, HLA LOH) provide essential WES-extractable signal — directly actionable for WES-first gene prioritization pipelines.

---

## Core Idea / Mechanism / Argument

### Claimed vs demonstrated

**Claimed:** Neoadjuvant response is determined by the baseline characteristics of the totality of the tumour ecosystem; integrating clinicopathological, genomic, transcriptomic, and digital pathology data through machine learning yields robust pCR predictors applicable beyond breast cancer and potentially actionable for trial enrichment.

**Demonstrated:** In TransNEO, individual pre-therapy features associate with RCB class but none alone is a robust standalone predictor. An ensemble ML pipeline trained on n=147 TransNEO cases and validated externally (n=75) achieves AUC 0.70 (clinical alone) rising to **0.87 (fully integrated)**. Predictor scores correlate monotonically with RCB in both training (P = 3 × 10⁻¹⁰) and validation (P = 1 × 10⁻⁶). Dominant model features include age, lymphocyte density, PGR/ESR1/ERBB2 expression, plus proliferation, immune activation, and immune evasion scores.

### Information flow

1. **Pre-treatment biopsy** → shallow WGS (168), WES (168), RNA-seq (162), digitized H&E (166).
2. **Step 1 — Feature discovery:** Univariate/logistic and ordinal regression across clinical, DNA (mutations, TMB, HRD, CNAs, iC10, HLA LOH, neoantigens), RNA (GGI, STAT1, TIDE dysfunction/exclusion, Danaher immune deconvolution), and digital pathology (lymphocyte density).
3. **Step 2 — Feature selection:** 34 predictive features retained after univariable filtering and collinearity reduction (Supplementary Table 4).
4. **Step 3 — Ensemble training:** Three parallel classifiers (elastic-net logistic regression, SVM, random forest) averaged into an unweighted ensemble; 5-fold cross-validation for hyperparameter optimization.
5. **Step 4 — External validation:** Independent cohort n=75 (ARTemis randomized control + PBCP); ROC/AUC comparison across six integration tiers.
6. **Biological interpretation:** Responsive tumours are proliferative with engaged innate/adaptive immunity; resistant tumours show subclonal complexity, PIK3CA mutations, HLA LOH, T cell dysfunction/exclusion, and mast cell enrichment.

### Novel vs inherited

- **Inherited:** TP53–pCR association (Bonnefoi EORTC 10994); PIK3CA–resistance (Yuan et al.); lymphocyte density from digital pathology (Ali et al. ARTemis); iC10 integrative clusters (Curtis/Ali); HRD scar scoring (Sztupinszki scarHRD); TIDE immune evasion metrics (Jiang et al.); taxane metagene (Juul et al.).
- **Novel:** Prospective single-protocol multi-omic profiling linked to RCB; formal six-tier integration benchmark with published feature list and external validation; demonstration that HER2+ response is proliferation-independent while HER2− genomic features (TMB, HRD, neoantigens) track proliferation; simulation of clinical trial enrichment using confusion matrices at fixed false-negative thresholds.

---

## Methodology / Evidence Base

### Design
Prospective observational molecular profiling study (TransNEO) with binary pCR vs residual disease endpoint, ordinal RCB secondary analysis, and external validation on independent neoadjuvant cohorts.

### Sample / setting

| Cohort | N | Role | Context |
|--------|---|------|---------|
| TransNEO enrolled | 180 | Discovery | Cambridge University Hospitals, 2013–2017; neoadjuvant chemotherapy ± anti-HER2 |
| TransNEO profiled | 168 | Discovery | Pre-treatment multi-omic biopsies (WES + sWGS + RNA-seq ± digital pathology) |
| TransNEO ML training | 147 | Model training | After exclusions; 5-fold CV within pipeline |
| TransNEO RCB-assessed | 161 | Endpoint | 42 pCR (26%), 25 RCB-I (16%), 65 RCB-II (40%), 29 RCB-III (18%) |
| External validation | 75 | Validation | ARTemis trial control arm + Personalised Breast Cancer Programme (PBCP) |

**Subtype breakdown (profiled n=168):** HER2+ n=65; ER+ HER2− n=65; ER− HER2− (TNBC) n=38.

**Treatment:** Median 18 weeks block-sequential taxane + anthracycline (145 cases); HER2+ received median 3 cycles anti-HER2 + taxane.

### Intervention or exposure
Neoadjuvant chemotherapy (taxane ± anthracycline ± carboplatin/cyclophosphamide) with or without anti-HER2 therapy (trastuzumab-based) before surgery.

### Measurements / instruments

| Layer | Platform / method | N | Key outputs |
|-------|-------------------|---|-------------|
| DNA — exome | Illumina Nextera WES, Mutect2, median ×162 tumour coverage | 168 | Somatic mutations, TMB (45.54 Mb denominator), clonal/subclonal CCF, driver calls (TP53, PIK3CA, etc.) |
| DNA — copy number | Shallow WGS (×0.1), QDNAseq + ASCAT | 168 | CNAs, chromosomal instability, iC10 classification |
| DNA — HRD / immune escape | scarHRD on WES+ASCAT; LOHHLA; pVACtools neoantigens | 168 | HRD score, HLA class I LOH, expressed neoantigen count |
| DNA — signatures | DeconstructSigs (30 COSMIC SBS) | 168 | HRD, APOBEC signature exposures |
| RNA | Illumina TruSeq stranded mRNA, STAR 2-pass, median 87M reads | 162 | GGI, STAT1, cytolytic (CYT), TIDE dysfunction/exclusion, Danaher/MCPcounter/Immunophenoscore deconvolution |
| Digital pathology | Digitized diagnostic H&E; computational lymphocyte density | 166 (153–166 for analyses) | Lymphocyte density score |
| Clinical | Pathology reports, trial records | 168 | ER/HER2, grade, stage, age, nodal status, treatment variables |
| Endpoint | RCB pathology protocol (MD Anderson) | 161 | pCR (no residual invasive cancer) vs RCB-I/II/III |

### Statistical analysis approach
Univariable logistic/ordinal regression with FDR correction for feature discovery; ensemble ML with univariable pre-selection, collinearity removal, 5-fold CV hyperparameter tuning, and external hold-out validation; feature importance by drop-one AUC z-score; Wilcoxon/ordinal logistic tests for monotonic RCB associations.

### Replication or pre-registration status
External validation on independent n=75 cohort; no pre-registration stated. Code and data availability declared at Nature DOI landing page.

---

## Relationship with the project's goals

### Which corpus scope and anchor question(s) this source engages with

- **Corpus:** `A_Genomic_Signal` (A6 integrated multi-omic); bridges `D_Clinical_Endpoint` (pCR/RCB), `E_Study_Type` (predictive ML ensemble model), `B_Therapeutic_Context` (chemo ± anti-HER2), `C_Cancer_Subtype` (TNBC vs HER2+ vs ER+).
- **Anchor question(s):** **AQ-1** (WES mutational drivers correlated with pCR — TP53, PIK3CA, TMB, HRD, HLA LOH); **AQ-2** (genomic biomarkers differentiating chemo vs anti-HER2 response — proliferation-independent HER2+ pathway vs HER2− TMB/HRD/neoantigen axis); **AQ-3** (high-priority drivers vs noise — explicit OR-ranked gene/signal list with integration weights).
- **Bridge corpus:** D (pCR endpoint), E (ML method), B (treatment regimen), C (subtype conditioning).

### How it could be used

- **Directly reusable:** Canonical feature set for WES-derived pCR predictors; TP53/PIK3CA directionality; HRD and TMB thresholds in HER2− tumours; HLA LOH as immune-evasion resistance marker; ensemble integration pattern (clinical + DNA + RNA) as benchmark architecture.
- **Indirectly inspiring:** Proliferation–immune co-enrichment framework (GGI × STAT1 quadrant analysis); TIDE dysfunction/exclusion as immune-evasion layer atop TMB/neoantigen signal; iC10 subtype gating of response expectations.
- **Mainly background / framing:** TransNEO as the reference neoadjuvant multi-omic cohort design; RCB ordinal endpoint hierarchy beyond binary pCR.

### Main fit with the project

This is the **central hub paper** for pCR prediction in breast neoadjuvant therapy. It explicitly profiles WES alongside RNA and clinical variables, ranks DNA features by model contribution, and validates externally — providing the evidence base against which any WES-only gene shortlist must be calibrated. TP53 (promote pCR), PIK3CA (promote resistance), HRD/TMB/neoantigens (HER2− only), and HLA LOH (resistance) are directly extractable from WES pipelines.

### Main mismatch or risk

- Project scope is **WES-first**; the best-performing integrated model relies most heavily on **RNA and digital pathology** features (PGR, ESR1, ERBB2, GGI, STAT1, lymphocyte density) that are not fully recoverable from WES alone — WES-only tier reached AUC 0.80 (clinical + DNA), not 0.87.
- Training n=147 and validation n=75 are modest; subtype-stratified performance not fully disaggregated in main text.
- Heterogeneous regimens (taxane/anthracycline combinations, variable anti-HER2 cycles) may limit transfer to single-regimen cohorts.
- iC10 and scarHRD require copy-number and optionally expression inputs beyond bare mutation lists.

### Concrete follow-up

- Extract the 34-feature list (Supplementary Table 4) into `E_Study_Type` as the reference ML feature schema.
- Cross-tag TP53, PIK3CA, HRD, TMB entries in A1/A2/A4 with Sammut effect directions.
- Bridge to `D_Clinical_Endpoint` for RCB ordinal endpoint semantics and pCR definition used here.
- Compare WES-only AUC 0.80 benchmark when evaluating project gene panels without RNA.
- Add Ali et al. 2016/2017 (lymphocyte density) and Jiang 2018 (TIDE) as immune-bridge entries if absent.

---

## Assumptions

- Pre-treatment core biopsy is representative of the tumour ecosystem determining post-therapy response.
- pCR (binary) is an adequate training label despite RCB providing finer ordinal resolution.
- Mutect2 somatic calls with gnomAD filtering and ≥×25 coverage capture clinically relevant drivers.
- TMB computed over 45.54 Mb coding territory is comparable across WES batches.
- External validation cohorts (ARTemis control + PBCP) share sufficient regimen and assay similarity with TransNEO for AUC generalization.
- Ensemble averaging of logistic regression, SVM, and random forest scores is appropriate despite potentially different calibration properties.
- HER2 status from diagnostic pathology (IHC/FISH) correctly partitions proliferation-dependent vs proliferation-independent response biology.

---

## Limitations / Failure Modes

- **Sample size:** 147 training and 75 validation cases limit power for subtype-specific models and rare mutation strata.
- **WES-only ceiling:** Clinical + DNA model AUC 0.80 vs 0.87 fully integrated — a WES-only pipeline cannot reach the paper's top performance without RNA/digital pathology proxies.
- **Regimen heterogeneity:** Mixed chemotherapy backbones and anti-HER2 exposure durations confound treatment-feature interpretation.
- **Single-institution discovery:** TransNEO enrolled at Cambridge; batch effects partially mitigated but not eliminated.
- **Feature selection leakage risk:** Univariable pre-filtering on the same cohort used for ensemble training may optimistic-bias internal CV; external validation partially addresses this.
- **Binary training label:** 26% pCR rate with RCB-II/III grouped as "residual disease" collapses clinically distinct non-pCR outcomes.
- **HER2+ proliferation independence:** Genomic predictors validated mainly in HER2− strata may not transfer to HER2+ anti-HER2-treated patients.

---

## Key Quantitative or Qualitative Results

### Cohort and endpoint

| Metric | Value |
|--------|-------|
| Discovery profiled | n=168 |
| ML training (TransNEO) | n=147 |
| External validation | n=75 |
| pCR rate (161 RCB-assessed) | 42/161 (26%) |
| WES samples | 168 |
| RNA-seq samples | 162 |

### External validation AUC by integration tier

| Model tier | External validation AUC |
|------------|-------------------------|
| Clinical only | 0.70 |
| Clinical + DNA | 0.80 |
| Clinical + RNA | 0.86 |
| Clinical + DNA + RNA | 0.86 |
| Clinical + DNA + RNA + digital pathology | 0.85 |
| **Fully integrated (+ treatment)** | **0.87** |

### Key univariate genomic associations (discovery)

| Feature | Association | Effect |
|---------|-------------|--------|
| TP53 mutation | pCR | OR 2.9 (95% CI 1.3–6.6, P=0.01) |
| PIK3CA mutation | Residual disease | OR 2.1 (95% CI 1.3–3.4, P=0.002) |
| TMB | pCR (monotonic RCB) | Median 2.3 vs 1.4 mut/Mb (P=0.0005); HER2− only |
| HRD score | pCR (monotonic RCB) | P=0.00001 overall; P=3×10⁻⁶ HER2− |
| HLA class I LOH | Residual disease | OR 3.5 (95% CI 1.1–14.2, P<0.05) |
| Subclonal mutations | Residual disease | Higher % subclonal in non-pCR |
| Neoantigen burden | pCR | Median 28 vs 17 (P=0.009); HER2− only |

### 34 predictive features (fully integrated model)

**Clinical (7):** tumour size, lymph node involvement, age at diagnosis, histological subtype, HER2 status, ER status, histological grade.

**DNA / WES-derived (8):** TMB, coding TMB, PIK3CA mutation status, TP53 mutation status, chromosomal instability, HRD score, expressed neoantigens, HLA LOH.

**RNA (11):** PGR expression, ESR1 expression, ERBB2 expression, GGI score (proliferation), embryonic stem-cell score, taxane response score, STAT1 score (immune activation), cytolytic score, T cell dysfunction score (TIDE), T cell exclusion score (TIDE), mast cell score.

**Digital pathology (1):** lymphocyte density.

**Treatment (4):** anthracycline therapy, number of chemotherapy cycles, anti-HER2 therapy, therapy sequence.

### Model feature importance (drop-one AUC z-score)

Dominant contributors: age, lymphocyte density, PGR, ESR1, ERBB2 expression; RNA features collectively largest modality contribution; DNA features include TMB, TP53, PIK3CA, HRD, neoantigens, HLA LOH.

### Clinical simulation (external validation confusion matrix)

At zero false-negative threshold: clinical model identifies 15 non-responders vs 31 for fully integrated model (per 100 hypothetical patients). At ≤2 false negatives: 24 vs 52 non-responders identified respectively.

---

## Key Quotes

> "We collected clinical, digital pathology, genomic and transcriptomic profiles of pre-treatment biopsies of breast tumours from 168 patients treated with chemotherapy with or without HER2 (encoded by ERBB2)-targeted therapy before surgery."

> "Combining these features into a multi-omic machine learning model predicted a pathological complete response in an external validation cohort (75 patients) with an area under the curve of 0.87."

> "TP53 mutations were associated with pCR (OR: 2.9, CI: 1.3–6.6, P = 0.01), as previously reported, whereas PIK3CA mutations were associated with residual disease (OR: 2.1, CI: 1.3–3.4, P = 0.002)."

> "Tumour mutation burden was higher in tumours that attained pCR (median mutations per megabase pCR: 2.3, residual disease: 1.4, P = 0.0005) and monotonically associated with RCB class (P = 0.004)."

> "Loss of heterozygosity (LOH) over the HLA class I locus was identified in 29 cases and associated with residual disease (OR: 3.5, CI: 1.1–14.2, P < 0.05; logistic regression) independently of global LOH and copy number instability."

> "Tumours that attained pCR mostly had high proliferation and high immune activation, with both signatures decreasing in a stepwise manner as the degree of residual disease increased."

> "Above, we identified clinical, digital pathology, genomic and transcriptomic features present in the naive tumour ecosystem that associated with response to therapy, although individually none of these features performed robustly."

> "In the external cohort, the models achieved the following areas under the curve: 0.70 (clinical), 0.80 (clinical and DNA), 0.86 (clinical and RNA), 0.86 (clinical, DNA and RNA), 0.85 (clinical, DNA, RNA and digital pathology), 0.87 (fully integrated model (clinical, DNA, RNA, digital pathology and treatment))."

> "The fully integrated model relied on features obtained from all modalities of data, with RNA features having the largest contribution."

> "Our findings showed that response is determined to a great degree by the baseline characteristics of the totality of the tumour ecosystem."

---

## Cross-References

### Complements entries in corpus
- `davies_2017_hrdetect` (when ingested): Sammut uses scarHRD on WES — HRDetect/scarHRD pipeline is upstream of the HRD feature in this predictor; HRD–pCR association in HER2− tumours validates HRD as a treatment-predictive signal beyond BRCA status.
- Future A1 HRD entries (Sztupinszki scarHRD, Natrajan HRD score): direct methodological dependency for the HRD feature used here.
- Future A3 immune entries (Ali lymphocyte density; Jiang TIDE): digital pathology and RNA immune-evasion layers in the integrated model.

### Contradicts / Tensions
- **Proliferation as universal predictor:** Sammut shows HER2+ pCR is proliferation-independent, tension with metagene-based predictors (Callari, Juul taxane score) that assume proliferation–response coupling across all subtypes.
- **Single-gene clinical utility:** TP53 and PIK3CA reach significance individually but the paper explicitly states individual features do not perform robustly alone — tension with single-biomarker clinical adoption.
- **WES-only project scope vs full model:** DNA tier AUC 0.80 vs integrated 0.87 — tension between project WES focus and paper's RNA-dominated optimal model.

### Cross-corpus connections
- **`D_Clinical_Endpoint`:** pCR definition (absence of residual invasive cancer on H&E); RCB-I/II/III as ordinal residual disease classes; 26% pCR rate as benchmark.
- **`E_Study_Type`:** Ensemble ML pipeline (elastic-net LR + SVM + RF); 5-fold CV; 34-feature schema; external validation design — reference implementation pattern for predictive models.
- **`B_Therapeutic_Context`:** Chemotherapy (taxane + anthracycline) ± anti-HER2; treatment variables (anthracycline, cycles, anti-HER2, sequence) as model inputs — biomarkers are regimen-conditioned.
- **`C_Cancer_Subtype`:** n=38 TNBC, n=65 HER2+, n=65 ER+HER2−; HER2−-specific TMB/HRD/neoantigen associations vs HER2+ proliferation-independent response.

### Related entries to add
- **HIGH:** Ali et al. 2016/2017 (computational lymphocyte density, ARTemis validation) — digital pathology feature source.
- **HIGH:** Jiang et al. 2018 (TIDE dysfunction/exclusion) — immune evasion metrics used directly.
- **HIGH:** Sztupinszki et al. 2018 (scarHRD) — HRD quantification method on WES.
- **MEDIUM:** Curtis/Ali iC10 integrative clusters — subtype-level response stratification.
- **MEDIUM:** Bonnefoi EORTC 10994 (TP53–taxane response) — prior TP53–pCR evidence cited.
- **MEDIUM:** Yuan et al. (PIK3CA–resistance) — prior PIK3CA directionality.

---

## Author Notes

### Priority justification
**CRITICAL** — This is the project's central pCR-prediction hub: prospective multi-omic design, WES-derived feature set with effect sizes, external validation AUC 0.87, and explicit gene-level prioritization (TP53↑, PIK3CA↓, HLA LOH↓) directly feeding AQ-1, AQ-2, and AQ-3. No other single paper in the neoadjuvant breast cancer space integrates WES features into a validated ML benchmark as comprehensively.

### Use this source for
- Benchmark AUC targets for WES-based pCR prediction (0.80 clinical+DNA; 0.87 fully integrated).
- Gene prioritization: TP53 (high-priority pro-response), PIK3CA (deprioritize / resistance marker), HLA LOH (immune evasion / resistance).
- Feature schema for multi-omic ML model design (34 features, six integration tiers).
- Subtype-specific interpretation: HER2− TMB/HRD/neoantigen axis vs HER2+ proliferation-independent pathway.
- Immune microenvironment framing: proliferation + immune activation vs T cell dysfunction/exclusion.
- TransNEO cohort characteristics as reference for neoadjuvant WES study design.

### Do NOT use this source for
- WES-only maximum performance claims → full model requires RNA and digital pathology (AUC 0.87 not achievable with DNA alone).
- Subtype-agnostic gene lists → many DNA associations are HER2−-specific.
- Single-gene clinical decision rules → paper states individual features are not robust alone.
- Non-breast cancer direct transfer → framework claimed generalizable but validated only in breast neoadjuvant setting.
- Adjuvant therapy prediction → discussed as future direction, not validated here.

### Curation notes
- Harmonize TMB denominator (45.54 Mb coding) with other corpus TMB definitions.
- Flag scarHRD vs HRDetect vs SNP-array HRD score as distinct HRD computation paths.
- Index under A6 hub entry, AQ-1/AQ-2/AQ-3 open questions, and ensemble ML methods.
- Supplementary Tables 1–6 (cohort characteristics, mutations, gene sets, 34 features, validation cohort, feature importance) contain granular data for downstream extraction.
- `corpus_role: decision` + `temporal_status: active_candidate` — treat as living benchmark until superseded by larger multi-cohort validations.

---

## Related Concepts

TransNEO, neoadjuvant therapy, pathological complete response (pCR), residual cancer burden (RCB), ensemble machine learning, elastic-net logistic regression, support vector machine, random forest, whole-exome sequencing (WES), shallow whole-genome sequencing (sWGS), tumour mutational burden (TMB), homologous recombination deficiency (HRD), APOBEC signature, HLA loss of heterozygosity (LOH), neoantigen burden, integrative cluster (iC10), Genomic Grade Index (GGI), STAT1 immune score, cytolytic activity (CYT), TIDE dysfunction, T cell exclusion, lymphocyte density, digital pathology, tumour immune microenvironment (TiME), clonal/subclonal architecture, chromosomal instability, PIK3CA, TP53, ERBB2, ESR1, PGR, anti-HER2 therapy, ARTemis trial, PBCP

---

## Quality Checklist

- [x] precise terminology of the discipline is used throughout
- [x] the source-type contextualization in Author Notes is complete
- [x] assumptions are explicit
- [x] novel contributions are distinguished from inherited components
- [x] quantitative or qualitative results include the relevant specifics
- [x] at least 5 useful direct quotes are included
- [x] cross-references are present (including cross-corpus when relevant)
- [x] the project-relevance relationship section is complete
- [ ] the relevant `CROSS_REFERENCE_INDEX.md` has been updated *(deferred per ingestion constraints — suggestions provided to parent agent)*
- [ ] the corpus `README.md` registry and counts have been updated *(deferred per ingestion constraints — one-line description provided to parent agent)*
